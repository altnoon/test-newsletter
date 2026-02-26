#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent.parent
IMAGE_DIR = ROOT / "Images"
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


def media_sort_key(path: Path):
    """
    Preferred order for newsletter assets:
    1) [Fase N] ... - Propietarios - ES
    2) [Fase N] ... - Propietarios - EN
    3) [Fase N] ... - No propietarios - ES
    4) [Fase N] ... - No propietarios - EN
    with phase ascending.
    Non-matching files are sorted after by creation time then name.
    """
    pattern = re.compile(
        r"^\[(?:Fase\s*|F)\s*(\d+)\]\s*(?:Nuevos destinos\s*-\s*)?"
        r"(Propietarios|No propietarios)\s*-\s*(ES|EN)$",
        re.IGNORECASE,
    )
    match = pattern.match(path.stem.strip())
    if match:
        phase = int(match.group(1))
        audience = match.group(2).strip().lower()
        language = match.group(3).strip().upper()
        audience_rank = 0 if audience == "propietarios" else 1
        language_rank = 0 if language == "ES" else 1
        return (0, phase, audience_rank, language_rank, path.name.lower())
    numeric_prefix = re.match(r"^(\d+)\s*([a-z])?\b", path.stem.strip(), re.IGNORECASE)
    if numeric_prefix:
        number = int(numeric_prefix.group(1))
        letter = (numeric_prefix.group(2) or "").lower()
        letter_rank = ord(letter) - 96 if letter else 0
        return (1, number, letter_rank, path.name.lower())
    return (2, created_at(path), path.name.lower())


def display_label(path: Path) -> str:
    """
    Format UI labels from source file names:
    - [Fase 1] Nuevos destinos - Propietarios - ES -> [F1] - Propietarios - ES
    - [Fase 2] Nuevos destinos - No propietarios - EN -> [F2] - No propietarios - EN
    Other names are returned as-is (without extension).
    """
    stem = path.stem.strip()
    pattern = re.compile(
        r"^\[Fase\s*(\d+)\]\s*Nuevos destinos\s*-\s*(.+)$",
        re.IGNORECASE,
    )
    match = pattern.match(stem)
    if not match:
        return stem
    phase = match.group(1)
    rest = match.group(2).strip()
    return f"[F{phase}] - {rest}"


def timeline_label_from_name(name: str) -> str:
    cleaned = name.strip()
    cleaned = re.sub(r"_+", " ", cleaned)
    cleaned = re.sub(r"\s*-\s*", " - ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        return "Timeline"
    if cleaned.lower() == "timeline 3 - flujo nurturing 3":
        return "Timeline 3 - Flujo Nurturing 3 EN"
    return cleaned


def timeline_group_sort_key(label: str) -> tuple[int, str]:
    normalized = re.sub(r"\s+", " ", label.strip().lower())
    match = re.search(r"timeline\s*(\d+)", normalized)
    if match:
        return (-int(match.group(1)), normalized)
    return (0, normalized)


def collect_timeline_groups() -> list[dict]:
    root_files = sorted(
        [p for p in IMAGE_DIR.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS],
        key=media_sort_key,
    )
    subdirs = sorted([p for p in IMAGE_DIR.iterdir() if p.is_dir()], key=lambda p: p.name.lower())

    groups: list[dict] = []

    for folder in subdirs:
        files = sorted(
            [
                p
                for p in folder.iterdir()
                if p.is_file() and p.suffix.lower() in IMAGE_EXTS
            ],
            key=media_sort_key,
        )
        groups.append(
            {
                "key": slugify(folder.name),
                "label": timeline_label_from_name(folder.name),
                "files": files,
            }
        )

    if not groups and root_files:
        groups.append(
            {
                "key": "timeline-root",
                "label": "Timeline",
                "files": root_files,
            }
        )
    return sorted(groups, key=lambda g: timeline_group_sort_key(g["label"]))


def nav_for_root_tabs(tabs: list[dict], active_key: str) -> str:
    items = []
    for tab in tabs:
        href = tab["href_root"]
        active = " is-active" if tab["key"] == active_key else ""
        items.append(
            f'<a class="nav-link{active}" href="{href}" title="{tab["label"]}">{tab["label"]}</a>'
        )
    return "\n".join(items)


def nav_for_page_tabs(tabs: list[dict], active_key: str) -> str:
    items = []
    for tab in tabs:
        href = tab["href_page"]
        active = " is-active" if tab["key"] == active_key else ""
        items.append(
            f'<a class="nav-link{active}" href="{href}" title="{tab["label"]}">{tab["label"]}</a>'
        )
    return "\n".join(items)


def mobile_menu_for_root_tabs(tabs: list[dict], active_key: str) -> str:
    items = []
    for tab in tabs:
        href = tab["href_root"]
        active = " is-active" if tab["key"] == active_key else ""
        items.append(
            f'<a class="mobile-menu-link{active}" href="{href}" title="{tab["label"]}">{tab["label"]}</a>'
        )
    return "\n".join(items)


def mobile_menu_for_page_tabs(tabs: list[dict], active_key: str) -> str:
    items = []
    for tab in tabs:
        href = tab["href_page"]
        active = " is-active" if tab["key"] == active_key else ""
        items.append(
            f'<a class="mobile-menu-link{active}" href="{href}" title="{tab["label"]}">{tab["label"]}</a>'
        )
    return "\n".join(items)


def mobile_controls(menu_links: str) -> str:
    return (
        '<div class="mobile-fab-stack" aria-label="Mobile navigation controls">'
        '<details class="mobile-menu">'
        '<summary class="mobile-menu-toggle" aria-label="Open pages menu">'
        '<span class="mobile-menu-bars" aria-hidden="true"></span>'
        '<span class="mobile-menu-bars" aria-hidden="true"></span>'
        '<span class="mobile-menu-bars" aria-hidden="true"></span>'
        '<span class="sr-only">Pages</span>'
        "</summary>"
        f'<nav class="mobile-menu-panel">{menu_links}</nav>'
        "</details>"
        "</div>"
    )


def render_page(
    title: str,
    nav: str,
    media_path: str | None,
    media_alt: str | None,
    css_href: str,
    script_href: str | None,
    page_key: str | None,
    mobile_nav: str,
    mobile_brand: str,
    custom_content: str | None = None,
) -> str:
    if custom_content is not None:
        content = custom_content
    elif media_path:
        content = (
            '<div class="layout">'
            '<section class="main-pane">'
            '<div class="viewer-wrap">'
            f'<img class="media-viewer" src="{media_path}" alt="{media_alt or ""}" />'
            "</div>"
            "</section>"
            f'<aside class="comments" data-page-key="{page_key or ""}">'
            '<div class="comments-top">'
            "<h2>Pin Notes</h2>"
            '<p class="comment-hint">'
            "Click on the image to place a pin and add a note."
            "</p>"
            '<p class="comment-live sr-only" aria-live="polite" '
            'aria-atomic="true" role="status"></p>'
            '<p class="comment-live-alert sr-only" aria-live="assertive" '
            'aria-atomic="true"></p>'
            '<label class="comment-author-label" for="comment-author">'
            "Your name"
            "</label>"
            '<input id="comment-author" class="comment-author" '
            'type="text" maxlength="40" placeholder="E.g. Sofía, Manuela, Oliver, Philip" />'
            '<p class="comment-count">0 notes</p>'
            '<button class="comment-clear" type="button">Clear all notes</button>'
            "</div>"
            '<div class="comment-log-wrap">'
            '<h3 class="comment-log-title">Chronological Notes</h3>'
            '<p class="comment-log-empty">No notes yet.</p>'
            '<ol class="comment-log"></ol>'
            "</div>"
            "</aside>"
            "</div>"
        )
    else:
        content = (
            '<div class="empty-state">'
            "<h1>No image files found</h1>"
            "<p>Add files to the <code>Images/</code> folder and run "
            "<code>python3 scripts/build_site.py</code>.</p>"
            "</div>"
        )

    html_page = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <title>{title}</title>
    <link rel="stylesheet" href="{css_href}" />
  </head>
  <body>
    <header class="topbar">
      <div class="brand">
        <span class="brand-page">{mobile_brand}</span>
      </div>
      <div class="topbar-nav" role="navigation" aria-label="Page navigation">
        <nav class="nav">{nav}</nav>
      </div>
    </header>
    <main class="content">
      {content}
    </main>
    {mobile_nav}
  </body>
</html>
"""
    script_tag = f'\n    <script src="{script_href}"></script>' if script_href else ""
    return html_page.replace("  </body>", f"{script_tag}\n  </body>")


def timeline_content_for_root(timelines: list[dict]) -> str:
    if not timelines:
        return (
            '<div class="empty-state">'
            "<h1>No image files found</h1>"
            "<p>Add files to the <code>Images/</code> folder and run "
            "<code>python3 scripts/build_site.py</code>.</p>"
            "</div>"
        )

    groups_markup = []
    for group in timelines:
        cards = []
        for i, doc in enumerate(group["docs"], start=1):
            cards.append(
                '<article class="miro-card">'
                '<div class="miro-card-head">'
                '<div class="miro-card-meta">'
                f'<span class="miro-card-index">#{i}</span>'
                f'<p class="miro-card-title">{doc["label"]}</p>'
                "</div>"
                "</div>"
                f'<div class="miro-card-stage" data-card-key="{group["key"]}::{doc["slug"]}" '
                f'data-card-label="{group["label"]} • {doc["label"]}">'
                f'<img class="miro-card-image" src="Images/{quote(doc["rel_path"])}" alt="{doc["alt"]}" loading="lazy" />'
                '<div class="pin-layer"></div>'
                "</div>"
                "</article>"
            )

        track_content = (
            f'<div class="miro-board-track">{"".join(cards)}</div>'
            if cards
            else '<p class="timeline-empty-group">No images in this folder yet.</p>'
        )

        groups_markup.append(
            '<section class="timeline-group">'
            '<div class="miro-board-head">'
            f"<h2>{group['label']}</h2>"
            "<p>Left-to-right sequence. Click on any image to pin feedback.</p>"
            "</div>"
            '<div class="miro-board-scroller" role="region" aria-label="Timeline board">'
            f"{track_content}"
            "</div>"
            "</section>"
        )

    return (
        '<div class="layout">'
        '<section class="main-pane timeline-summary">'
        '<div class="miro-board-head">'
        '<div class="timeline-controls" role="toolbar" aria-label="Timeline view controls">'
        '<button class="timeline-control-btn" type="button" data-timeline-action="fit">Fit to screen</button>'
        '<button class="timeline-control-btn" type="button" data-timeline-action="zoom-in">Zoom in</button>'
        '<button class="timeline-control-btn" type="button" data-timeline-action="zoom-out">Zoom out</button>'
        '<span class="timeline-zoom-readout" aria-live="polite">100%</span>'
        "</div>"
        "</div>"
        f'{"".join(groups_markup)}'
        "</section>"
        '<aside class="comments" data-board-key="timeline-board">'
        '<div class="comments-top">'
        "<h2>Pin Notes</h2>"
        '<p class="comment-hint">'
        "Click on a timeline image to place a pin and add a note."
        "</p>"
        '<p class="comment-live sr-only" aria-live="polite" '
        'aria-atomic="true" role="status"></p>'
        '<p class="comment-live-alert sr-only" aria-live="assertive" '
        'aria-atomic="true"></p>'
        '<label class="comment-author-label" for="comment-author">'
        "Your name"
        "</label>"
        '<input id="comment-author" class="comment-author" '
        'type="text" maxlength="40" placeholder="E.g. Sofía, Manuela, Oliver, Philip" />'
        '<p class="comment-count">0 notes</p>'
        '<button class="comment-clear" type="button">Clear all notes</button>'
        "</div>"
        '<div class="comment-log-wrap">'
        '<h3 class="comment-log-title">Chronological Notes</h3>'
        '<p class="comment-log-empty">No notes yet.</p>'
        '<ol class="comment-log"></ol>'
        "</div>"
        "</aside>"
        "</div>"
    )


def timeline_content_for_group(group: dict) -> str:
    cards = []
    for i, doc in enumerate(group["docs"], start=1):
        cards.append(
            '<article class="miro-card">'
            '<div class="miro-card-head">'
            '<div class="miro-card-meta">'
            f'<span class="miro-card-index">#{i}</span>'
            f'<p class="miro-card-title">{doc["label"]}</p>'
            "</div>"
            "</div>"
            f'<div class="miro-card-stage" data-card-key="{group["key"]}::{doc["slug"]}" '
            f'data-card-label="{group["label"]} • {doc["label"]}">'
            f'<img class="miro-card-image" src="../Images/{quote(doc["rel_path"])}" alt="{doc["alt"]}" loading="lazy" />'
            '<div class="pin-layer"></div>'
            "</div>"
            "</article>"
        )

    track_content = (
        f'<div class="miro-board-track">{"".join(cards)}</div>'
        if cards
        else '<p class="timeline-empty-group">No images in this folder yet.</p>'
    )

    return (
        '<div class="layout">'
        '<section class="main-pane timeline-summary">'
        '<div class="miro-board-head">'
        f"<h1>{group['label']}</h1>"
        '<div class="timeline-controls" role="toolbar" aria-label="Timeline view controls">'
        '<button class="timeline-control-btn" type="button" data-timeline-action="fit">Fit to screen</button>'
        '<button class="timeline-control-btn" type="button" data-timeline-action="zoom-in">Zoom in</button>'
        '<button class="timeline-control-btn" type="button" data-timeline-action="zoom-out">Zoom out</button>'
        '<span class="timeline-zoom-readout" aria-live="polite">100%</span>'
        "</div>"
        "</div>"
        '<section class="timeline-group">'
        '<div class="miro-board-scroller" role="region" aria-label="Timeline board">'
        f"{track_content}"
        "</div>"
        "</section>"
        "</section>"
        f'<aside class="comments" data-board-key="timeline-board-{group["key"]}">'
        '<div class="comments-top">'
        "<h2>Pin Notes</h2>"
        '<p class="comment-hint">'
        "Click on a timeline image to place a pin and add a note."
        "</p>"
        '<p class="comment-live sr-only" aria-live="polite" '
        'aria-atomic="true" role="status"></p>'
        '<p class="comment-live-alert sr-only" aria-live="assertive" '
        'aria-atomic="true"></p>'
        '<label class="comment-author-label" for="comment-author">'
        "Your name"
        "</label>"
        '<input id="comment-author" class="comment-author" '
        'type="text" maxlength="40" placeholder="E.g. Sofía, Manuela, Oliver, Philip" />'
        '<p class="comment-count">0 notes</p>'
        '<button class="comment-clear" type="button">Clear all notes</button>'
        "</div>"
        '<div class="comment-log-wrap">'
        '<h3 class="comment-log-title">Chronological Notes</h3>'
        '<p class="comment-log-empty">No notes yet.</p>'
        '<ol class="comment-log"></ol>'
        "</div>"
        "</aside>"
        "</div>"
    )


def main() -> None:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    STYLE_FILE.parent.mkdir(parents=True, exist_ok=True)

    for page in PAGES_DIR.glob("*.html"):
        page.unlink()

    timeline_groups = collect_timeline_groups()
    docs: list[dict] = []
    seen: set[str] = set()
    for group in timeline_groups:
        group_docs: list[dict] = []
        for path in group["files"]:
            rel_path = path.relative_to(IMAGE_DIR).as_posix()
            label = html.escape(display_label(path))
            slug = unique_slug(seen, slugify(rel_path))
            doc = {
                "path": path,
                "rel_path": rel_path,
                "label": label,
                "slug": slug,
                "alt": html.escape(display_label(path)),
            }
            docs.append(doc)
            group_docs.append(doc)
        group["docs"] = group_docs

    if docs:
        tabs = [
            {
                "key": "timeline",
                "label": "Timeline Board",
                "href_root": "index.html",
                "href_page": "../index.html",
            }
        ]
        for group in timeline_groups:
            tabs.append(
                {
                    "key": group["key"],
                    "label": group["label"],
                    "href_root": f"pages/timeline-{group['key']}.html",
                    "href_page": f"timeline-{group['key']}.html",
                }
            )

        root_menu_links = mobile_menu_for_root_tabs(tabs, "timeline")
        INDEX_FILE.write_text(
            render_page(
                title="Timeline | Image Timeline",
                nav=nav_for_root_tabs(tabs, "timeline"),
                media_path=None,
                media_alt=None,
                css_href="styles.css",
                script_href="comments.js",
                page_key=None,
                mobile_nav=mobile_controls(root_menu_links),
                mobile_brand="Timeline",
                custom_content=timeline_content_for_root(timeline_groups),
            ),
            encoding="utf-8",
        )

        for group in timeline_groups:
            group_menu_links = mobile_menu_for_page_tabs(tabs, group["key"])
            group_html = render_page(
                title=f"{group['label']} | Image Timeline",
                nav=nav_for_page_tabs(tabs, group["key"]),
                media_path=None,
                media_alt=None,
                css_href="../styles.css",
                script_href="../comments.js",
                page_key=None,
                mobile_nav=mobile_controls(group_menu_links),
                mobile_brand=group["label"],
                custom_content=timeline_content_for_group(group),
            )
            (PAGES_DIR / f"timeline-{group['key']}.html").write_text(group_html, encoding="utf-8")

        group_by_doc_slug = {}
        for group in timeline_groups:
            for doc in group["docs"]:
                group_by_doc_slug[doc["slug"]] = group

        for doc in docs:
            group = group_by_doc_slug.get(doc["slug"])
            active_tab_key = group["key"] if group else "timeline"
            page_menu_links = mobile_menu_for_page_tabs(tabs, active_tab_key)
            page_html = render_page(
                title=f"{doc['label']} | Image Timeline",
                nav=nav_for_page_tabs(tabs, active_tab_key),
                media_path=f"../Images/{quote(doc['rel_path'])}",
                media_alt=doc["alt"],
                css_href="../styles.css",
                script_href="../comments.js",
                page_key=doc["slug"],
                mobile_nav=mobile_controls(page_menu_links),
                mobile_brand=doc["label"],
            )
            (PAGES_DIR / f"{doc['slug']}.html").write_text(page_html, encoding="utf-8")
    else:
        INDEX_FILE.write_text(
            render_page(
                title="Image Timeline",
                nav=nav_for_root_tabs(
                    [
                        {
                            "key": "timeline",
                            "label": "Timeline",
                            "href_root": "index.html",
                            "href_page": "../index.html",
                        }
                    ],
                    "timeline",
                ),
                media_path=None,
                media_alt=None,
                css_href="styles.css",
                script_href=None,
                page_key=None,
                mobile_nav="",
                mobile_brand="Image Timeline",
            ),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
