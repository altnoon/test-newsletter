const { Redis } = require("@upstash/redis");

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
  return value.slice(0, 200);
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
  const id = String(note.id || "").trim();
  const text = String(note.text || "").trim();
  const author = String(note.author || "Anonymous").trim() || "Anonymous";
  const pin = normalizePin(note.pin);
  if (!id || !text || !pin) return null;
  return {
    id,
    text,
    author,
    pin,
    createdAt: String(note.createdAt || new Date().toISOString()),
  };
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
      const id = String(body.id || "").trim();
      const text = String(body.text || "").trim();
      const author = String(body.author || "").trim();
      if (!id || !text) return badRequest(res, "Invalid update payload");
      notes = notes.map((item) =>
        item.id === id
          ? {
              ...item,
              text,
              author: author || item.author || "Anonymous",
              createdAt: new Date().toISOString(),
            }
          : item
      );
      await redis.set(key, notes);
      return res.status(200).json({ notes });
    }

    if (action === "delete") {
      const id = String(body.id || "").trim();
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
  } catch (error) {
    return res.status(500).json({ error: "Notes API failed" });
  }
};
