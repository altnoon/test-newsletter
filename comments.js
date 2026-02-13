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

  sections.forEach((section) => {
    const pageKey = section.getAttribute("data-page-key");
    if (!pageKey) return;

    const storageKey = `image-timeline-comments:${pageKey}`;
    const form = section.querySelector(".comment-form");
    const input = section.querySelector(".comment-input");
    const list = section.querySelector(".comment-list");
    const empty = section.querySelector(".comment-empty");
    const clearBtn = section.querySelector(".comment-clear");

    if (!form || !input || !list || !empty || !clearBtn) return;

    let comments = safeRead(storageKey);

    const render = () => {
      list.innerHTML = "";
      if (!comments.length) {
        empty.style.display = "block";
        return;
      }

      empty.style.display = "none";
      comments.forEach((item) => {
        const li = document.createElement("li");
        li.className = "comment-item";

        const text = document.createElement("p");
        text.className = "comment-text";
        text.textContent = item.text;

        const time = document.createElement("time");
        time.className = "comment-time";
        const date = new Date(item.createdAt);
        time.textContent = Number.isNaN(date.getTime())
          ? ""
          : date.toLocaleString();

        li.appendChild(text);
        li.appendChild(time);
        list.appendChild(li);
      });
    };

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const text = input.value.trim();
      if (!text) return;

      comments.push({
        text,
        createdAt: new Date().toISOString(),
      });
      safeWrite(storageKey, comments);
      input.value = "";
      render();
    });

    clearBtn.addEventListener("click", () => {
      comments = [];
      try {
        localStorage.removeItem(storageKey);
      } catch (_) {
        // Ignore storage errors.
      }
      render();
    });

    render();
  });
})();
