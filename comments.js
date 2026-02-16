(() => {
  const topbar = document.querySelector(".topbar");
  if (topbar) {
    const navPrev = topbar.querySelector(".nav-arrow-left");
    const navNext = topbar.querySelector(".nav-arrow-right");
    const nav = topbar.querySelector(".nav");
    const isDesktopViewport = () =>
      typeof window !== "undefined" && window.matchMedia("(min-width: 701px)").matches;
    const centerActiveNavLink = () => {
      if (!nav) return;
      const active = nav.querySelector(".nav-link.is-active");
      if (!active) return;

      const navRect = nav.getBoundingClientRect();
      if (!navRect.width || nav.scrollWidth <= navRect.width + 1) return;

      const activeRect = active.getBoundingClientRect();
      const targetLeft =
        nav.scrollLeft +
        (activeRect.left - navRect.left) -
        (navRect.width / 2 - activeRect.width / 2);
      nav.scrollTo({ left: Math.max(0, targetLeft), behavior: "auto" });
    };

    const updateNavArrows = () => {
      if (!nav || !navPrev || !navNext) return;
      const maxScroll = Math.max(0, nav.scrollWidth - nav.clientWidth);
      const atStart = nav.scrollLeft <= 1;
      const atEnd = nav.scrollLeft >= maxScroll - 1;
      const hasOverflow = maxScroll > 1;
      navPrev.disabled = !hasOverflow || atStart;
      navNext.disabled = !hasOverflow || atEnd;
    };

    const scrollNavBy = (direction) => {
      if (!nav) return;
      const amount = Math.max(180, Math.floor(nav.clientWidth * 0.55));
      nav.scrollBy({ left: direction * amount, behavior: "smooth" });
    };

    if (nav) {
      let dragging = false;
      let dragStartX = 0;
      let dragStartScroll = 0;
      let movedDuringDrag = false;
      let suppressClick = false;

      nav.addEventListener("pointerdown", (event) => {
        if (!isDesktopViewport()) return;
        if (event.pointerType === "mouse" && event.button !== 0) return;
        dragging = true;
        movedDuringDrag = false;
        dragStartX = event.clientX;
        dragStartScroll = nav.scrollLeft;
        nav.classList.add("is-dragging");
      });

      nav.addEventListener("pointermove", (event) => {
        if (!dragging) return;
        const delta = event.clientX - dragStartX;
        if (Math.abs(delta) > 2) movedDuringDrag = true;
        nav.scrollLeft = dragStartScroll - delta;
        if (movedDuringDrag) event.preventDefault();
      });

      const endDrag = () => {
        if (!dragging) return;
        dragging = false;
        nav.classList.remove("is-dragging");
        if (movedDuringDrag) suppressClick = true;
      };

      nav.addEventListener("pointerup", endDrag);
      nav.addEventListener("pointercancel", endDrag);
      nav.addEventListener("pointerleave", endDrag);

      nav.addEventListener(
        "click",
        (event) => {
          if (!suppressClick) return;
          event.preventDefault();
          event.stopPropagation();
          suppressClick = false;
        },
        true
      );

      nav.addEventListener(
        "wheel",
        (event) => {
          if (!isDesktopViewport()) return;
          const delta = Math.abs(event.deltaX) > Math.abs(event.deltaY)
            ? event.deltaX
            : event.deltaY;
          if (!delta) return;
          nav.scrollLeft += delta;
          event.preventDefault();
        },
        { passive: false }
      );

      nav.addEventListener("scroll", updateNavArrows, { passive: true });
    }

    if (navPrev) {
      navPrev.addEventListener("click", () => {
        scrollNavBy(-1);
      });
    }

    if (navNext) {
      navNext.addEventListener("click", () => {
        scrollNavBy(1);
      });
    }

    const syncTopOffset = () => {
      const height = Math.ceil(topbar.getBoundingClientRect().height);
      if (height > 0) {
        document.documentElement.style.setProperty("--sticky-offset", `${height}px`);
      }
      updateNavArrows();
    };

    syncTopOffset();
    centerActiveNavLink();
    updateNavArrows();
    window.addEventListener("resize", syncTopOffset, { passive: true });
    window.addEventListener("orientationchange", syncTopOffset, { passive: true });

    if (document.fonts && document.fonts.ready) {
      document.fonts.ready
        .then(() => {
          syncTopOffset();
          centerActiveNavLink();
        })
        .catch(() => {});
    }

    if (typeof ResizeObserver !== "undefined") {
      const observer = new ResizeObserver(syncTopOffset);
      observer.observe(topbar);
    }
  }

  const sections = document.querySelectorAll(".comments[data-page-key]");
  if (!sections.length) return;

  const API_ENDPOINT = "/api/notes";
  const AUTHOR_STORAGE_KEY = "image-timeline-author";

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
    return `note-${Date.now()}-${Math.random().toString(16).slice(2)}`;
  };

  const toTimestamp = (value) => {
    const ts = Date.parse(String(value || ""));
    return Number.isNaN(ts) ? 0 : ts;
  };

  const normalizeComments = (items) =>
    items
      .map((item) => {
        if (!item || typeof item !== "object") return null;

        const text = String(item.text ?? "").trim();
        if (!text) return null;

        const sourcePin = item.pin && typeof item.pin === "object" ? item.pin : item;
        const pinX = Number(sourcePin.x);
        const pinY = Number(sourcePin.y);
        const hasPin = Number.isFinite(pinX) && Number.isFinite(pinY);
        if (!hasPin) return null;

        const createdAt = String(item.createdAt || new Date().toISOString());
        return {
          id: String(item.id || makeId()),
          text,
          author: String(item.author || "Anonymous").trim() || "Anonymous",
          createdAt,
          pin: { x: clamp01(pinX), y: clamp01(pinY) },
        };
      })
      .filter(Boolean);

  const sortChronological = (items) =>
    [...items].sort((a, b) => {
      const t = toTimestamp(a.createdAt) - toTimestamp(b.createdAt);
      if (t !== 0) return t;
      return a.id.localeCompare(b.id);
    });

  const formatDate = (value) => {
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? "" : date.toLocaleString();
  };

  const requestNotes = async (page, method, body) => {
    const query = `?page=${encodeURIComponent(page)}`;
    const response = await fetch(
      `${API_ENDPOINT}${method === "GET" ? query : ""}`,
      method === "GET"
        ? { method: "GET", headers: { Accept: "application/json" } }
        : {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            body: JSON.stringify({ page, ...body }),
          }
    );

    if (!response.ok) {
      throw new Error(`Notes request failed (${response.status})`);
    }
    const payload = await response.json();
    return normalizeComments(payload.notes || []);
  };

  const createEditor = () => {
    const editor = document.createElement("div");
    editor.className = "pin-note-editor";
    editor.innerHTML =
      '<p class="pin-note-meta"></p>' +
      '<label class="pin-note-author-label" for="pin-note-author">Name</label>' +
      '<input id="pin-note-author" class="pin-note-author" type="text" maxlength="40" placeholder="e.g. Ana" />' +
      '<textarea class="pin-note-input" rows="4" placeholder="Write a sticky note..."></textarea>' +
      '<div class="pin-note-actions">' +
      '<button class="pin-note-save" type="button">Save</button>' +
      '<button class="pin-note-cancel" type="button">Cancel</button>' +
      '<button class="pin-note-delete" type="button">Delete</button>' +
      "</div>";
    return editor;
  };

  sections.forEach((section) => {
    const pageKey = section.getAttribute("data-page-key");
    if (!pageKey) return;

    const layout = section.closest(".layout");
    const image = layout?.querySelector(".media-viewer");
    const commentsTop = section.querySelector(".comments-top");
    const hint = section.querySelector(".comment-hint");
    const authorInput = section.querySelector(".comment-author");
    const count = section.querySelector(".comment-count");
    const clearBtn = section.querySelector(".comment-clear");
    const log = section.querySelector(".comment-log");
    const logEmpty = section.querySelector(".comment-log-empty");
    if (
      !image ||
      !layout ||
      !commentsTop ||
      !hint ||
      !authorInput ||
      !count ||
      !clearBtn ||
      !log ||
      !logEmpty
    ) {
      return;
    }

    const ensureLiveRegion = (className, liveMode, role) => {
      let region = section.querySelector(`.${className}`);
      if (!region) {
        region = document.createElement("p");
        region.className = `${className} sr-only`;
        region.setAttribute("aria-live", liveMode);
        region.setAttribute("aria-atomic", "true");
        if (role) region.setAttribute("role", role);
        commentsTop.appendChild(region);
      }
      return region;
    };

    const liveRegion = ensureLiveRegion("comment-live", "polite", "status");
    const liveAlertRegion = ensureLiveRegion("comment-live-alert", "assertive");

    let announceToken = 0;
    const announce = (text, mode) => {
      const message = String(text || "").trim();
      if (!message) return;
      const target = mode === "warning" ? liveAlertRegion : liveRegion;
      if (!target) return;

      announceToken += 1;
      const token = announceToken;
      target.textContent = "";
      window.requestAnimationFrame(() => {
        if (token !== announceToken) return;
        target.textContent = message;
      });
    };

    const localStorageKey = `image-timeline-comments:${pageKey}`;
    let usingShared = true;

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

    let editor = stage.querySelector(".pin-note-editor");
    if (!editor) {
      editor = createEditor();
      stage.appendChild(editor);
    }

    const input = editor.querySelector(".pin-note-input");
    const noteAuthorInput = editor.querySelector(".pin-note-author");
    const meta = editor.querySelector(".pin-note-meta");
    const saveBtn = editor.querySelector(".pin-note-save");
    const cancelBtn = editor.querySelector(".pin-note-cancel");
    const deleteBtn = editor.querySelector(".pin-note-delete");
    if (
      !input ||
      !noteAuthorInput ||
      !meta ||
      !saveBtn ||
      !cancelBtn ||
      !deleteBtn
    ) {
      return;
    }

    editor.addEventListener("click", (event) => event.stopPropagation());

    let comments = normalizeComments(safeRead(localStorageKey));
    let activeCommentId = null;
    let draftPin = null;
    let editorPin = null;
    let editingCommentId = null;

    authorInput.value = localStorage.getItem(AUTHOR_STORAGE_KEY) || "";
    authorInput.addEventListener("input", () => {
      const value = authorInput.value.trim().slice(0, 40);
      localStorage.setItem(AUTHOR_STORAGE_KEY, value);
    });

    const setHint = (text, mode, shouldAnnounce = false) => {
      hint.textContent = text;
      hint.classList.toggle("is-warning", mode === "warning");
      hint.classList.toggle("is-info", mode !== "warning");
      if (shouldAnnounce) announce(text, mode);
    };

    const updateCount = () => {
      const total = comments.length;
      const mode = usingShared ? "shared" : "local";
      count.textContent = `${total} ${total === 1 ? "note" : "notes"} (${mode})`;
    };

    const persistLocal = () => {
      safeWrite(localStorageKey, comments);
    };

    const getAuthorName = () => authorInput.value.trim();

    const setEditorMeta = (mode, item) => {
      if (mode === "edit" && item) {
        const timestamp = formatDate(item.createdAt);
        meta.textContent = `${item.author || "Anonymous"}${timestamp ? ` • ${timestamp}` : ""}`;
        return;
      }
      const author = noteAuthorInput.value.trim() || getAuthorName();
      meta.textContent = author
        ? `New note by ${author}`
        : "Add your name in the note before saving";
    };

    const openEditor = (pin, initialText, mode, item) => {
      editorPin = pin;
      input.value = initialText || "";
      noteAuthorInput.value =
        mode === "edit" && item ? item.author || getAuthorName() : getAuthorName();
      editor.classList.add("is-open");
      editor.classList.toggle("is-edit", mode === "edit");
      deleteBtn.style.display = mode === "edit" ? "inline-flex" : "none";
      setEditorMeta(mode, item);
      positionEditor();
      setTimeout(() => input.focus(), 0);
    };

    const closeEditor = () => {
      editor.classList.remove("is-open");
      editor.classList.remove("is-edit");
      editingCommentId = null;
      editorPin = null;
      input.value = "";
      noteAuthorInput.value = "";
    };

    const isMobileViewport = () =>
      typeof window !== "undefined" &&
      window.matchMedia("(max-width: 700px)").matches;

    const positionEditor = () => {
      if (!editorPin) return;
      if (isMobileViewport()) {
        editor.style.removeProperty("left");
        editor.style.removeProperty("top");
        editor.style.removeProperty("width");
        editor.style.removeProperty("right");
        editor.style.removeProperty("bottom");
        return;
      }

      const rect = stage.getBoundingClientRect();
      const editorWidth = Math.min(260, Math.max(220, rect.width - 24));
      const editorHeight = 182;
      let left = editorPin.x * rect.width + 14;
      let top = editorPin.y * rect.height - 20;
      left = Math.min(left, rect.width - editorWidth - 8);
      left = Math.max(left, 8);
      top = Math.max(top, 8);
      if (top + editorHeight > rect.height - 8) {
        top = Math.max(8, editorPin.y * rect.height - editorHeight - 18);
      }
      editor.style.removeProperty("right");
      editor.style.removeProperty("bottom");
      editor.style.left = `${left}px`;
      editor.style.top = `${top}px`;
      editor.style.width = `${editorWidth}px`;
    };

    window.addEventListener(
      "resize",
      () => {
        if (editor.classList.contains("is-open")) positionEditor();
      },
      { passive: true }
    );

    window.addEventListener(
      "orientationchange",
      () => {
        if (editor.classList.contains("is-open")) positionEditor();
      },
      { passive: true }
    );

    const renderLog = (ordered) => {
      log.innerHTML = "";

      if (!ordered.length) {
        logEmpty.style.display = "block";
        return;
      }
      logEmpty.style.display = "none";

      ordered.forEach((item, index) => {
        const li = document.createElement("li");
        li.className = "comment-log-item";
        if (item.id === activeCommentId) li.classList.add("is-active");

        const header = document.createElement("div");
        header.className = "comment-log-header";

        const pin = document.createElement("span");
        pin.className = "comment-log-pin";
        pin.textContent = `#${index + 1}`;

        const author = document.createElement("span");
        author.className = "comment-log-author";
        author.textContent = item.author || "Anonymous";

        const when = document.createElement("span");
        when.className = "comment-log-date";
        when.textContent = formatDate(item.createdAt);

        header.appendChild(pin);
        header.appendChild(author);
        header.appendChild(when);

        const body = document.createElement("p");
        body.className = "comment-log-text";
        body.textContent = item.text;

        li.appendChild(header);
        li.appendChild(body);
        li.addEventListener("click", () => {
          activeCommentId = item.id;
          editingCommentId = item.id;
          draftPin = null;
          openEditor(item.pin, item.text, "edit", item);
          setHint(`Editing note by ${item.author || "Anonymous"}.`, "info");
          renderAll();
        });

        log.appendChild(li);
      });
    };

    const renderPins = (ordered) => {
      pinLayer.innerHTML = "";

      ordered.forEach((item, index) => {
        const marker = document.createElement("button");
        marker.type = "button";
        marker.className = "pin-marker";
        marker.style.left = `${item.pin.x * 100}%`;
        marker.style.top = `${item.pin.y * 100}%`;
        marker.textContent = String(index + 1);
        marker.title = `${item.author || "Anonymous"}: ${item.text}`;
        if (item.id === activeCommentId) marker.classList.add("is-active");
        marker.addEventListener("click", (event) => {
          event.stopPropagation();
          activeCommentId = item.id;
          editingCommentId = item.id;
          draftPin = null;
          openEditor(item.pin, item.text, "edit", item);
          setHint(`Editing note by ${item.author || "Anonymous"}.`, "info");
          renderAll();
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

    const renderAll = () => {
      const ordered = sortChronological(comments);
      renderPins(ordered);
      renderLog(ordered);
      updateCount();
    };

    const applyServerNotes = (serverNotes) => {
      comments = normalizeComments(serverNotes);
      persistLocal();
      renderAll();
    };

    const syncFromShared = async (silent) => {
      if (!usingShared || editor.classList.contains("is-open")) return;
      try {
        const sharedNotes = await requestNotes(pageKey, "GET");
        applyServerNotes(sharedNotes);
        if (!silent) setHint("Shared notes synced.", "info", true);
      } catch (_) {
        usingShared = false;
        renderAll();
        setHint(
          "Shared notes unavailable. Using local notes in this browser.",
          "warning",
          true
        );
      }
    };

    const mutateShared = async (action, payload) => {
      if (!usingShared) return false;
      try {
        const sharedNotes = await requestNotes(pageKey, "POST", {
          action,
          ...payload,
        });
        applyServerNotes(sharedNotes);
        return true;
      } catch (_) {
        usingShared = false;
        renderAll();
        setHint(
          "Could not update shared notes. Switched to local notes.",
          "warning",
          true
        );
        return false;
      }
    };

    noteAuthorInput.addEventListener("input", () => {
      if (!editor.classList.contains("is-open")) return;
      if (editor.classList.contains("is-edit")) return;
      setEditorMeta("create", null);
    });

    stage.addEventListener("click", (event) => {
      const rect = stage.getBoundingClientRect();
      if (!rect.width || !rect.height) return;

      const x = clamp01((event.clientX - rect.left) / rect.width);
      const y = clamp01((event.clientY - rect.top) / rect.height);

      draftPin = { x, y };
      activeCommentId = null;
      editingCommentId = null;
      openEditor(draftPin, "", "create", null);
      setHint("Pin placed. Add your note and save.", "info", true);
      renderAll();
    });

    saveBtn.addEventListener("click", async () => {
      const text = input.value.trim();
      if (!text) {
        setHint("Type a note before saving.", "warning", true);
        return;
      }
      const author = noteAuthorInput.value.trim() || getAuthorName();
      if (!author) {
        setHint("Add your name before saving.", "warning", true);
        noteAuthorInput.focus();
        return;
      }

      if (authorInput.value.trim() !== author) {
        authorInput.value = author;
        localStorage.setItem(AUTHOR_STORAGE_KEY, author);
      }

      saveBtn.disabled = true;
      cancelBtn.disabled = true;
      deleteBtn.disabled = true;

      try {
        if (editingCommentId) {
          const sharedOk = await mutateShared("update", {
            id: editingCommentId,
            text,
            author,
          });
          if (!sharedOk) {
            comments = comments.map((item) =>
              item.id === editingCommentId ? { ...item, text, author } : item
            );
            persistLocal();
          }
          activeCommentId = editingCommentId;
          setHint("Note updated.", "info", true);
        } else if (draftPin) {
          const newItem = {
            id: makeId(),
            text,
            author,
            createdAt: new Date().toISOString(),
            pin: { x: draftPin.x, y: draftPin.y },
          };

          const sharedOk = await mutateShared("add", { note: newItem });
          if (!sharedOk) {
            comments.push(newItem);
            persistLocal();
          }
          activeCommentId = newItem.id;
          setHint("Note saved.", "info", true);
        }

        draftPin = null;
        closeEditor();
        renderAll();
      } finally {
        saveBtn.disabled = false;
        cancelBtn.disabled = false;
        deleteBtn.disabled = false;
      }
    });

    cancelBtn.addEventListener("click", () => {
      if (!editingCommentId) draftPin = null;
      closeEditor();
      renderAll();
      setHint("Click on the image to place a pin and add a note.", "info");
    });

    deleteBtn.addEventListener("click", async () => {
      if (!editingCommentId) return;

      const deletedId = editingCommentId;
      saveBtn.disabled = true;
      cancelBtn.disabled = true;
      deleteBtn.disabled = true;

      try {
        const sharedOk = await mutateShared("delete", { id: deletedId });
        if (!sharedOk) {
          comments = comments.filter((item) => item.id !== deletedId);
          persistLocal();
        }
        activeCommentId = null;
        closeEditor();
        renderAll();
        setHint("Note deleted.", "info", true);
      } finally {
        saveBtn.disabled = false;
        cancelBtn.disabled = false;
        deleteBtn.disabled = false;
      }
    });

    clearBtn.addEventListener("click", async () => {
      saveBtn.disabled = true;
      cancelBtn.disabled = true;
      deleteBtn.disabled = true;

      try {
        const sharedOk = await mutateShared("clear", {});
        if (!sharedOk) {
          comments = [];
          persistLocal();
        }

        activeCommentId = null;
        editingCommentId = null;
        draftPin = null;
        closeEditor();
        renderAll();
        setHint(
          "All notes cleared. Click image to create a new pinned note.",
          "info",
          true
        );
      } finally {
        saveBtn.disabled = false;
        cancelBtn.disabled = false;
        deleteBtn.disabled = false;
      }
    });

    window.addEventListener("resize", () => {
      if (editor.classList.contains("is-open")) positionEditor();
    });

    renderAll();
    setHint("Connecting to shared notes...", "info", true);
    syncFromShared(false);
    setInterval(() => {
      syncFromShared(true);
    }, 12000);
  });
})();
