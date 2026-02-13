(() => {
  const sections = document.querySelectorAll(".comments[data-page-key]");
  if (!sections.length) return;

  const API_ENDPOINT = "/api/notes";

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

        return {
          id: String(item.id || makeId()),
          text,
          createdAt: String(item.createdAt || new Date().toISOString()),
          pin: { x: clamp01(pinX), y: clamp01(pinY) },
        };
      })
      .filter(Boolean);

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
    const hint = section.querySelector(".comment-hint");
    const count = section.querySelector(".comment-count");
    const clearBtn = section.querySelector(".comment-clear");
    if (!image || !layout || !hint || !count || !clearBtn) return;

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
    const saveBtn = editor.querySelector(".pin-note-save");
    const cancelBtn = editor.querySelector(".pin-note-cancel");
    const deleteBtn = editor.querySelector(".pin-note-delete");
    if (!input || !saveBtn || !cancelBtn || !deleteBtn) return;

    editor.addEventListener("click", (event) => {
      event.stopPropagation();
    });

    let comments = normalizeComments(safeRead(localStorageKey));
    let activeCommentId = null;
    let draftPin = null;
    let editorPin = null;
    let editingCommentId = null;

    const setHint = (text, mode) => {
      hint.textContent = text;
      hint.classList.toggle("is-warning", mode === "warning");
      hint.classList.toggle("is-info", mode !== "warning");
    };

    const updateCount = () => {
      const total = comments.length;
      const mode = usingShared ? "shared" : "local";
      count.textContent = `${total} ${total === 1 ? "note" : "notes"} (${mode})`;
    };

    const persistLocal = () => {
      safeWrite(localStorageKey, comments);
    };

    const openEditor = (pin, initialText, mode) => {
      editorPin = pin;
      input.value = initialText || "";
      editor.classList.add("is-open");
      editor.classList.toggle("is-edit", mode === "edit");
      deleteBtn.style.display = mode === "edit" ? "inline-flex" : "none";
      positionEditor();
      setTimeout(() => input.focus(), 0);
    };

    const closeEditor = () => {
      editor.classList.remove("is-open");
      editor.classList.remove("is-edit");
      editingCommentId = null;
      editorPin = null;
      input.value = "";
    };

    const positionEditor = () => {
      if (!editorPin) return;
      const rect = stage.getBoundingClientRect();
      const editorWidth = Math.min(260, Math.max(220, rect.width - 24));
      const editorHeight = 170;
      let left = editorPin.x * rect.width + 14;
      let top = editorPin.y * rect.height - 20;
      left = Math.min(left, rect.width - editorWidth - 8);
      left = Math.max(left, 8);
      top = Math.max(top, 8);
      if (top + editorHeight > rect.height - 8) {
        top = Math.max(8, editorPin.y * rect.height - editorHeight - 18);
      }
      editor.style.left = `${left}px`;
      editor.style.top = `${top}px`;
      editor.style.width = `${editorWidth}px`;
    };

    const renderPins = () => {
      pinLayer.innerHTML = "";

      comments.forEach((item, index) => {
        const marker = document.createElement("button");
        marker.type = "button";
        marker.className = "pin-marker";
        marker.style.left = `${item.pin.x * 100}%`;
        marker.style.top = `${item.pin.y * 100}%`;
        marker.textContent = String(index + 1);
        marker.title = item.text;
        if (item.id === activeCommentId) {
          marker.classList.add("is-active");
        }
        marker.addEventListener("click", (event) => {
          event.stopPropagation();
          activeCommentId = item.id;
          editingCommentId = item.id;
          draftPin = null;
          openEditor(item.pin, item.text, "edit");
          setHint("Editing note.", "info");
          renderPins();
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

    const applyServerNotes = (serverNotes) => {
      comments = normalizeComments(serverNotes);
      persistLocal();
      updateCount();
      renderPins();
    };

    const syncFromShared = async (silent) => {
      if (!usingShared) return;
      if (editor.classList.contains("is-open")) return;
      try {
        const sharedNotes = await requestNotes(pageKey, "GET");
        applyServerNotes(sharedNotes);
        if (!silent) {
          setHint("Shared notes synced.", "info");
        }
      } catch (_) {
        usingShared = false;
        updateCount();
        setHint(
          "Shared notes unavailable. Using local notes in this browser.",
          "warning"
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
        updateCount();
        setHint(
          "Could not update shared notes. Switched to local notes.",
          "warning"
        );
        return false;
      }
    };

    stage.addEventListener("click", (event) => {
      const rect = stage.getBoundingClientRect();
      if (!rect.width || !rect.height) return;

      const x = clamp01((event.clientX - rect.left) / rect.width);
      const y = clamp01((event.clientY - rect.top) / rect.height);

      draftPin = { x, y };
      activeCommentId = null;
      editingCommentId = null;
      openEditor(draftPin, "", "create");
      setHint("Pin placed. Add your note and save.", "info");
      renderPins();
    });

    saveBtn.addEventListener("click", async () => {
      const text = input.value.trim();
      if (!text) {
        setHint("Type a note before saving.", "warning");
        return;
      }

      saveBtn.disabled = true;
      cancelBtn.disabled = true;
      deleteBtn.disabled = true;

      try {
        if (editingCommentId) {
          const sharedOk = await mutateShared("update", {
            id: editingCommentId,
            text,
          });
          if (!sharedOk) {
            comments = comments.map((item) =>
              item.id === editingCommentId
                ? { ...item, text, createdAt: new Date().toISOString() }
                : item
            );
            persistLocal();
            updateCount();
          }
          activeCommentId = editingCommentId;
          setHint("Note updated.", "info");
        } else if (draftPin) {
          const newItem = {
            id: makeId(),
            text,
            createdAt: new Date().toISOString(),
            pin: { x: draftPin.x, y: draftPin.y },
          };

          const sharedOk = await mutateShared("add", { note: newItem });
          if (!sharedOk) {
            comments.push(newItem);
            persistLocal();
            updateCount();
          }
          activeCommentId = newItem.id;
          setHint("Note saved.", "info");
        }

        draftPin = null;
        closeEditor();
        renderPins();
      } finally {
        saveBtn.disabled = false;
        cancelBtn.disabled = false;
        deleteBtn.disabled = false;
      }
    });

    cancelBtn.addEventListener("click", () => {
      if (!editingCommentId) {
        draftPin = null;
      }
      closeEditor();
      renderPins();
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
          updateCount();
        }

        activeCommentId = null;
        closeEditor();
        renderPins();
        setHint("Note deleted.", "info");
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
          updateCount();
        }

        activeCommentId = null;
        editingCommentId = null;
        draftPin = null;
        closeEditor();
        renderPins();
        setHint("All notes cleared. Click image to create a new pinned note.", "info");
      } finally {
        saveBtn.disabled = false;
        cancelBtn.disabled = false;
        deleteBtn.disabled = false;
      }
    });

    window.addEventListener("resize", () => {
      if (editor.classList.contains("is-open")) {
        positionEditor();
      }
    });

    updateCount();
    renderPins();
    setHint("Connecting to shared notes...", "info");

    syncFromShared(false);
    setInterval(() => {
      syncFromShared(true);
    }, 12000);
  });
})();
