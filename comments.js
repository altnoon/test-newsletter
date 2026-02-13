(() => {
  const sections = document.querySelectorAll(".comments[data-page-key]");
  if (!sections.length) return;

  const safeRead = (key) => {
    try {
      const raw = localStorage.getItem(key);
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (_) {
      return [];
    }
  };

  const safeWrite = (key, value) => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (_) {
      // Ignore storage errors in private mode or blocked storage.
    }
  };

  const clamp01 = (value) => Math.min(1, Math.max(0, value));

  const makeId = () => {
    if (typeof crypto !== "undefined" && typeof crypto.randomUUID === "function") {
      return crypto.randomUUID();
    }
    return `c-${Date.now()}-${Math.random().toString(16).slice(2)}`;
  };

  const normalizeComments = (items) =>
    items
      .map((item) => {
        if (!item || typeof item !== "object") return null;

        const text = String(item.text ?? "").trim();
        if (!text) return null;

        const pinSource = item.pin && typeof item.pin === "object" ? item.pin : item;
        const x = Number(pinSource.x);
        const y = Number(pinSource.y);
        const hasPin = Number.isFinite(x) && Number.isFinite(y);

        return {
          id: String(item.id || makeId()),
          text,
          createdAt: String(item.createdAt || new Date().toISOString()),
          pin: hasPin ? { x: clamp01(x), y: clamp01(y) } : null,
        };
      })
      .filter(Boolean);

  sections.forEach((section) => {
    const pageKey = section.getAttribute("data-page-key");
    if (!pageKey) return;

    const layout = section.closest(".layout");
    const image = layout?.querySelector(".media-viewer");

    const storageKey = `image-timeline-comments:${pageKey}`;
    const form = section.querySelector(".comment-form");
    const input = section.querySelector(".comment-input");
    const list = section.querySelector(".comment-list");
    const empty = section.querySelector(".comment-empty");
    const clearBtn = section.querySelector(".comment-clear");

    if (!image || !form || !input || !list || !empty || !clearBtn) return;

    let stage = layout.querySelector(".media-stage");
    if (!stage) {
      stage = document.createElement("div");
      stage.className = "media-stage";
      image.parentNode.insertBefore(stage, image);
      stage.appendChild(image);
    }

    let pinLayer = stage.querySelector(".pin-layer");
    if (!pinLayer) {
      pinLayer = document.createElement("div");
      pinLayer.className = "pin-layer";
      stage.appendChild(pinLayer);
    }

    let hint = section.querySelector(".comment-hint");
    if (!hint) {
      hint = document.createElement("p");
      hint.className = "comment-hint";
      section.insertBefore(hint, form);
    }

    let comments = normalizeComments(safeRead(storageKey));
    let draftPin = null;
    let activeCommentId = null;

    const saveComments = () => safeWrite(storageKey, comments);

    const setHint = (text, mode) => {
      hint.textContent = text;
      hint.classList.toggle("is-warning", mode === "warning");
      hint.classList.toggle("is-info", mode === "info");
    };

    const renderPins = (pinIndexById) => {
      pinLayer.innerHTML = "";

      comments.forEach((item) => {
        if (!item.pin) return;

        const marker = document.createElement("button");
        marker.type = "button";
        marker.className = "pin-marker";
        if (item.id === activeCommentId) {
          marker.classList.add("is-active");
        }
        marker.style.left = `${item.pin.x * 100}%`;
        marker.style.top = `${item.pin.y * 100}%`;
        marker.textContent = String(pinIndexById.get(item.id) || "");
        marker.title = item.text;
        marker.addEventListener("click", (event) => {
          event.stopPropagation();
          activeCommentId = item.id;
          render();
          const linked = list.querySelector(`[data-comment-id="${item.id}"]`);
          linked?.scrollIntoView({ behavior: "smooth", block: "nearest" });
        });
        pinLayer.appendChild(marker);
      });

      if (draftPin) {
        const draft = document.createElement("div");
        draft.className = "pin-marker is-draft";
        draft.style.left = `${draftPin.x * 100}%`;
        draft.style.top = `${draftPin.y * 100}%`;
        pinLayer.appendChild(draft);
      }
    };

    const renderList = (pinIndexById) => {
      list.innerHTML = "";
      if (!comments.length) {
        empty.style.display = "block";
        return;
      }

      empty.style.display = "none";

      comments.forEach((item) => {
        const li = document.createElement("li");
        li.className = "comment-item";
        li.dataset.commentId = item.id;
        if (item.id === activeCommentId) {
          li.classList.add("is-active");
        }

        const label = document.createElement("div");
        label.className = "comment-label";
        label.textContent = item.pin
          ? `Pin ${pinIndexById.get(item.id) || ""}`
          : "Comment";

        const text = document.createElement("p");
        text.className = "comment-text";
        text.textContent = item.text;

        const time = document.createElement("time");
        time.className = "comment-time";
        const date = new Date(item.createdAt);
        time.textContent = Number.isNaN(date.getTime()) ? "" : date.toLocaleString();

        li.appendChild(label);
        li.appendChild(text);
        li.appendChild(time);
        li.addEventListener("click", () => {
          activeCommentId = item.id;
          render();
        });
        list.appendChild(li);
      });
    };

    const render = () => {
      const pinIndexById = new Map();
      let pinCounter = 0;
      comments.forEach((item) => {
        if (!item.pin) return;
        pinCounter += 1;
        pinIndexById.set(item.id, pinCounter);
      });
      renderPins(pinIndexById);
      renderList(pinIndexById);
    };

    stage.addEventListener("click", (event) => {
      const rect = stage.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      const x = clamp01((event.clientX - rect.left) / rect.width);
      const y = clamp01((event.clientY - rect.top) / rect.height);

      draftPin = { x, y };
      activeCommentId = null;
      setHint("Pin selected. Write a comment and click Save.", "info");
      render();
      input.focus();
    });

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const text = input.value.trim();
      if (!text) return;
      if (!draftPin) {
        setHint("Click the image first to place a pin.", "warning");
        return;
      }

      const item = {
        id: makeId(),
        text,
        createdAt: new Date().toISOString(),
        pin: { x: draftPin.x, y: draftPin.y },
      };
      comments.push(item);
      saveComments();

      input.value = "";
      draftPin = null;
      activeCommentId = item.id;
      setHint("Saved. Click anywhere else on the image to add another pin.", "info");
      render();
    });

    clearBtn.addEventListener("click", () => {
      comments = [];
      draftPin = null;
      activeCommentId = null;
      try {
        localStorage.removeItem(storageKey);
      } catch (_) {
        // Ignore storage errors.
      }
      setHint("All comments cleared. Click the image to create a new pin.", "info");
      render();
    });

    setHint("Click anywhere on the image to place a pin comment.", "info");
    render();
  });
})();
