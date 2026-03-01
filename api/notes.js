const { Redis } = require("@upstash/redis");

const MAX_PAGE_KEY_LEN = 200;
const MAX_ID_LEN = 120;
const MAX_TEXT_LEN = 2000;
const MAX_AUTHOR_LEN = 80;
const PAGE_KEY_PATTERN = /^[a-zA-Z0-9._:-]+$/;

function createRedisClient() {
  const url =
    process.env.UPSTASH_REDIS_REST_URL || process.env.KV_REST_API_URL || "";
  const token =
    process.env.UPSTASH_REDIS_REST_TOKEN || process.env.KV_REST_API_TOKEN || "";

  if (!url || !token) return null;

  return new Redis({ url, token });
}

function badRequest(res, message) {
  return res.status(400).json({ error: message });
}

function normalizePageKey(input) {
  const value = String(input || "").trim();
  if (!value) return "";
  const clipped = value.slice(0, MAX_PAGE_KEY_LEN);
  if (!PAGE_KEY_PATTERN.test(clipped)) return "";
  return clipped;
}

function normalizePin(pin) {
  if (!pin || typeof pin !== "object") return null;
  const x = Number(pin.x);
  const y = Number(pin.y);
  if (!Number.isFinite(x) || !Number.isFinite(y)) return null;
  return {
    x: Math.max(0, Math.min(1, x)),
    y: Math.max(0, Math.min(1, y)),
  };
}

function normalizeNote(note) {
  if (!note || typeof note !== "object") return null;
  const id = String(note.id || "").trim().slice(0, MAX_ID_LEN);
  const text = String(note.text || "").trim().slice(0, MAX_TEXT_LEN);
  const author =
    String(note.author || "Anonymous").trim().slice(0, MAX_AUTHOR_LEN) || "Anonymous";
  const cardKey = String(note.cardKey || note.cardSlug || "").trim().slice(0, MAX_PAGE_KEY_LEN);
  const pin = normalizePin(note.pin);
  if (!id || !text || !pin) return null;
  const normalized = {
    id,
    text,
    author,
    pin,
    createdAt: String(note.createdAt || new Date().toISOString()),
  };
  if (cardKey) normalized.cardKey = cardKey;
  return normalized;
}

function normalizeNotes(items) {
  if (!Array.isArray(items)) return [];
  return items.map(normalizeNote).filter(Boolean);
}

async function readNotes(key) {
  const redis = createRedisClient();
  if (!redis) {
    throw new Error("Redis is not configured");
  }
  const raw = await redis.get(key);
  return normalizeNotes(raw);
}

function parseBody(req) {
  if (!req.body) return {};
  if (typeof req.body === "string") {
    try {
      return JSON.parse(req.body);
    } catch (_) {
      return {};
    }
  }
  if (typeof req.body === "object") {
    return req.body;
  }
  return {};
}

function getClientIp(req) {
  const forwarded = String(req.headers["x-forwarded-for"] || "").split(",")[0].trim();
  if (forwarded) return forwarded;
  const real = String(req.headers["x-real-ip"] || "").trim();
  return real || "unknown";
}

function parseHostFromUrl(value) {
  if (!value) return "";
  try {
    return new URL(String(value)).host.toLowerCase();
  } catch (_) {
    return "";
  }
}

function requestHost(req) {
  const host = String(req.headers["x-forwarded-host"] || req.headers.host || "")
    .split(",")[0]
    .trim()
    .toLowerCase();
  return host;
}

function isSameOriginRequest(req) {
  const host = requestHost(req);
  if (!host) return false;
  const originHost = parseHostFromUrl(req.headers.origin);
  if (originHost) return originHost === host;
  const refererHost = parseHostFromUrl(req.headers.referer || req.headers.referrer);
  if (refererHost) return refererHost === host;
  return false;
}

async function isRateLimited(redis, req) {
  const ip = getClientIp(req);
  const isWrite = req.method === "POST";
  const limit = Number(
    isWrite
      ? process.env.NOTES_RATE_LIMIT_WRITE_PER_MINUTE || 90
      : process.env.NOTES_RATE_LIMIT_READ_PER_MINUTE || 240
  );
  const safeLimit = Number.isFinite(limit) && limit > 0 ? limit : isWrite ? 90 : 240;
  const key = `ratelimit:notes:${isWrite ? "write" : "read"}:${ip}`;
  const count = await redis.incr(key);
  if (count === 1) {
    await redis.expire(key, 60);
  }
  return count > safeLimit;
}

module.exports = async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");

  const page = normalizePageKey(req.query.page || parseBody(req).page);
  if (!page) {
    return badRequest(res, "Missing page");
  }
  const key = `notes:${page}`;
  const redis = createRedisClient();
  if (!redis) {
    return res.status(500).json({ error: "Redis is not configured" });
  }

  try {
    if (!isSameOriginRequest(req)) {
      return res.status(403).json({ error: "Forbidden" });
    }

    if (await isRateLimited(redis, req)) {
      return res.status(429).json({ error: "Rate limit exceeded" });
    }

    if (req.method === "GET") {
      const notes = await readNotes(key);
      return res.status(200).json({ notes });
    }

    if (req.method !== "POST") {
      return res.status(405).json({ error: "Method not allowed" });
    }

    const body = parseBody(req);
    const action = String(body.action || "").trim();
    let notes = await readNotes(key);

    if (action === "add") {
      const note = normalizeNote(body.note);
      if (!note) return badRequest(res, "Invalid note");
      notes.push(note);
      await redis.set(key, notes);
      return res.status(200).json({ notes });
    }

    if (action === "update") {
      const id = String(body.id || "").trim().slice(0, MAX_ID_LEN);
      const text = String(body.text || "").trim().slice(0, MAX_TEXT_LEN);
      const author = String(body.author || "").trim().slice(0, MAX_AUTHOR_LEN);
      const cardKey = String(body.cardKey || body.cardSlug || "")
        .trim()
        .slice(0, MAX_PAGE_KEY_LEN);
      const pin = body.pin ? normalizePin(body.pin) : null;
      if (!id) return badRequest(res, "Invalid update payload");
      notes = notes.map((item) =>
        item.id === id
          ? {
              ...item,
              text: text || item.text,
              author: author || item.author || "Anonymous",
              pin: pin || item.pin,
              ...(cardKey ? { cardKey } : {}),
            }
          : item
      );
      await redis.set(key, notes);
      return res.status(200).json({ notes });
    }

    if (action === "delete") {
      const id = String(body.id || "").trim().slice(0, MAX_ID_LEN);
      if (!id) return badRequest(res, "Missing id");
      notes = notes.filter((item) => item.id !== id);
      await redis.set(key, notes);
      return res.status(200).json({ notes });
    }

    if (action === "clear") {
      await redis.del(key);
      return res.status(200).json({ notes: [] });
    }

    return badRequest(res, "Unknown action");
  } catch (_) {
    return res.status(500).json({ error: "Notes API failed" });
  }
};
