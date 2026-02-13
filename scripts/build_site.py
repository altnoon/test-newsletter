#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "pdfs"
PAGES_DIR = ROOT / "pages"
STYLE_FILE = ROOT / "styles.css"
INDEX_FILE = ROOT / "index.html"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def created_at(path: Path) -> float:
    stat = path.stat()
    # st_birthtime is available on macOS and some BSD systems.
    return getattr(stat, "st_birthtime", stat.st_ctime)


def slugify(value: str) -> str:
    base = Path(value).stem.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return slug or "document"


def unique_slug(existing: set[str], candidate: str) -> str:
    if candidate not in existing:
        existing.add(candidate)
        return candidate
    index = 2
    while f"{candidate}-{index}" in existing:
        index += 1
    final = f"{candidate}-{index}"
    existing.add(final)
    return final


def nav_for_root(docs: list[dict], active_slug: str) -> str:
    if not docs:
        return '<span class="nav-empty">No images found</span>'

    items = []
    for i, doc in enumerate(docs):
        href = "index.html" if i == 0 else f"pages/{doc['slug']}.html"
        active = " is-active" if doc["slug"] == active_slug else ""
        items.append(
            f'<a class="nav-link{active}" href="{href}">{doc["label"]}</a>'
        )
    return "\n".join(items)


def nav_for_page(docs: list[dict], active_slug: str) -> str:
    if not docs:
        return '<span class="nav-empty">No images found</span>'

    items = []
    for i, doc in enumerate(docs):
        if i == 0:
            href = "../index.html"
        else:
            href = f"{doc['slug']}.html"
        active = " is-active" if doc["slug"] == active_slug else ""
        items.append(
            f'<a class="nav-link{active}" href="{href}">{doc["label"]}</a>'
        )
    return "\n".join(items)


def render_page(
    title: str,
    nav: str,
    media_path: str | None,
    media_alt: str | None,
    css_href: str,
    script_href: str | None,
    page_key: str | None,
) -> str:
    if media_path:
        content = (
            '<div class="layout">'
            '<section class="main-pane">'
            '<div class="viewer-wrap">'
            f'<img class="media-viewer" src="{media_path}" alt="{media_alt or ""}" />'
            "</div>"
            "</section>"
            f'<aside class="comments" data-page-key="{page_key or ""}">'
            "<h2>Comments</h2>"
            '<form class="comment-form">'
            '<textarea class="comment-input" rows="3" '
            'placeholder="Add a comment"></textarea>'
            '<div class="comment-actions">'
            '<button class="comment-submit" type="submit">Save</button>'
            '<button class="comment-clear" type="button">Clear</button>'
            "</div>"
            "</form>"
            '<p class="comment-empty">No comments yet.</p>'
            '<ul class="comment-list"></ul>'
            "</aside>"
            "</div>"
        )
    else:
        content = (
            '<div class="empty-state">'
            "<h1>No image files found</h1>"
            "<p>Add files to the <code>pdfs/</code> folder and run "
            "<code>python3 scripts/build_site.py</code>.</p>"
            "</div>"
        )

    html_page = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <link rel="stylesheet" href="{css_href}" />
  </head>
  <body>
    <header class="topbar">
      <div class="brand">Image Timeline</div>
      <nav class="nav">{nav}</nav>
    </header>
    <main class="content">
      {content}
    </main>
  </body>
</html>
"""
    script_tag = f'\n    <script src="{script_href}"></script>' if script_href else ""
    return html_page.replace("  </body>", f"{script_tag}\n  </body>")


def main() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    STYLE_FILE.parent.mkdir(parents=True, exist_ok=True)

    for page in PAGES_DIR.glob("*.html"):
        page.unlink()

    media_files = sorted(
        [
            p
            for p in PDF_DIR.iterdir()
            if p.is_file() and p.suffix.lower() in IMAGE_EXTS
        ],
        key=lambda p: (created_at(p), p.name.lower()),
    )

    docs: list[dict] = []
    seen: set[str] = set()
    for path in media_files:
        label = html.escape(path.name)
        slug = unique_slug(seen, slugify(path.name))
        docs.append(
            {
                "path": path,
                "label": label,
                "slug": slug,
                "alt": html.escape(path.stem),
            }
        )

    if docs:
        first = docs[0]
        index_html = render_page(
            title=f"{first['label']} | Image Timeline",
            nav=nav_for_root(docs, first["slug"]),
            media_path=f"pdfs/{quote(first['path'].name)}",
            media_alt=first["alt"],
            css_href="styles.css",
            script_href="comments.js",
            page_key=first["slug"],
        )
        INDEX_FILE.write_text(index_html, encoding="utf-8")

        for doc in docs[1:]:
            page_html = render_page(
                title=f"{doc['label']} | Image Timeline",
                nav=nav_for_page(docs, doc["slug"]),
                media_path=f"../pdfs/{quote(doc['path'].name)}",
                media_alt=doc["alt"],
                css_href="../styles.css",
                script_href="../comments.js",
                page_key=doc["slug"],
            )
            (PAGES_DIR / f"{doc['slug']}.html").write_text(page_html, encoding="utf-8")
    else:
        INDEX_FILE.write_text(
            render_page(
                title="Image Timeline",
                nav=nav_for_root([], ""),
                media_path=None,
                media_alt=None,
                css_href="styles.css",
                script_href=None,
                page_key=None,
            ),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
