#!/usr/bin/env python3
from __future__ import annotations

import html
import csv
import re
import unicodedata
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent.parent
IMAGE_DIR = ROOT / "Images"
PAGES_DIR = ROOT / "pages"
STYLE_FILE = ROOT / "styles.css"
INDEX_FILE = ROOT / "index.html"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
ANALYTICS_XLSX_CANDIDATES = [
    ROOT.parent / "Analytics.xlsx",
    ROOT / "Analytics.xlsx",
    Path("/Users/delchev/Downloads/Untitled spreadsheet.xlsx"),
    Path("/Users/delchev/Downloads/vivla-mail-analytics-ind (1).xlsx"),
    ROOT / "vivla-mail-analytics-ind.xlsx",
    ROOT / "data" / "vivla-mail-analytics-ind.xlsx",
    Path("/Users/delchev/Downloads/vivla-mail-analytics-ind.xlsx"),
]
ANALYTICS_HTML_CANDIDATES = [
    ROOT.parent / "[Vivla] OS Nurturing & Content Leadership" / "Dashboard nurturing.html",
    Path("/Users/delchev/Downloads/[Vivla] OS Nurturing & Content Leadership/Dashboard nurturing.html"),
]
EMAIL_LINKS_CSV_CANDIDATES = [
    ROOT.parent / "email_links.csv",
    ROOT / "email_links.csv",
    ROOT.parent / "email_links_template.csv",
    ROOT / "email_links_template.csv",
]
TIMELINE_SUMMARY_XLSX_CANDIDATES_BY_GROUP = {
    "timeline-1-onboarding-flujo-1-y-2-en-only": [
        ROOT.parent / "Timeline 1 - Onboarding Flujo 1 y 2 (EN Only).xlsx",
        ROOT / "Timeline 1 - Onboarding Flujo 1 y 2 (EN Only).xlsx",
        Path("/Users/delchev/Downloads/Timeline 1 - Onboarding Flujo 1 y 2 (EN Only).xlsx"),
    ],
    "timeline-2-nuevos-destinos-en-es": [
        ROOT.parent / "Timeline 2 - Nuevos Destinos (EN + ES).xlsx",
        ROOT / "Timeline 2 - Nuevos Destinos (EN + ES).xlsx",
        Path("/Users/delchev/Downloads/Timeline 2 - Nuevos Destinos (EN + ES).xlsx"),
    ],
}


def normalize_text(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode("ascii")
    lowered = folded.lower()
    lowered = re.sub(r"[^a-z0-9]+", " ", lowered)
    return re.sub(r"\s+", " ", lowered).strip()


def flow_place_key(value: str) -> tuple[str, str, str] | None:
    flow, variant = analytics_key(value)
    if not flow:
        return None
    normalized = normalize_text(value)
    normalized = re.sub(r"\bw\d+\s*[- ]?\s*[edp]\s*\d+\b", " ", normalized)
    normalized = re.sub(r"\b202[0-9]\b", " ", normalized)
    normalized = re.sub(r"\b(?:en|es|intl|workflow|total|onboarding|nurturing|behavioral|destinos|casas|general)\b", " ", normalized)
    normalized = re.sub(r"\b(?:a|b)\b", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    if not normalized:
        return None
    return (flow, variant, normalized)


def analytics_key(value: str) -> tuple[str, str]:
    text = value or ""
    normalized = normalize_text(text)
    flow_match = re.search(r"\bw(\d+)\s*[- ]?\s*([edp])\s*(\d+)\b", normalized)
    flow = f"w{flow_match.group(1)}-{flow_match.group(2)}{flow_match.group(3)}" if flow_match else ""
    variant = ""
    paren_variant = re.search(r"\(([ab])\)", text, re.IGNORECASE)
    if paren_variant:
        variant = paren_variant.group(1).lower()
    else:
        prefixed_variant = re.match(r"^\s*\d+\s*([ab])\b", text, re.IGNORECASE)
        if prefixed_variant:
            variant = prefixed_variant.group(1).lower()
        else:
            compact_prefixed_variant = re.match(r"^\s*\d+([ab])\b", text, re.IGNORECASE)
            if compact_prefixed_variant:
                variant = compact_prefixed_variant.group(1).lower()
    return (flow, variant)


def phase_lang_place_key(value: str) -> tuple[str, str, str] | None:
    text = value or ""
    normalized = normalize_text(text)
    phase_match = re.search(r"\b(?:fase|f)\s*(\d+)\b", normalized)
    if not phase_match:
        return None
    phase = f"f{phase_match.group(1)}"
    lang = ""
    if re.search(r"\ben\b", normalized):
        lang = "en"
    elif re.search(r"\bes\b", normalized):
        lang = "es"
    if not lang:
        return None

    stripped = normalized
    stripped = re.sub(r"\b(?:fase|f)\s*\d+\b", "", stripped)
    stripped = re.sub(r"\bnuevos?\s+destinos?\b", "", stripped)
    stripped = re.sub(r"\bno\s+propietarios?\b", "", stripped)
    stripped = re.sub(rf"\b{lang}\b", "", stripped)
    stripped = re.sub(r"\s+", " ", stripped).strip(" -")
    place = stripped or "general"
    return (phase, lang, place)


def find_analytics_xlsx() -> Path | None:
    dynamic_candidates = sorted(
        [
            *ROOT.glob("Analytics*.xlsx"),
            *ROOT.parent.glob("Analytics*.xlsx"),
            *ROOT.glob("vivla-mail-analytics-ind*.xlsx"),
            *ROOT.parent.glob("vivla-mail-analytics-ind*.xlsx"),
        ],
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    for path in dynamic_candidates:
        if path.exists():
            return path
    for path in ANALYTICS_XLSX_CANDIDATES:
        if path.exists():
            return path
    return None


def find_analytics_html() -> Path | None:
    for path in ANALYTICS_HTML_CANDIDATES:
        if path.exists():
            return path
    return None


def preferred_analytics_source() -> tuple[str, Path] | None:
    xlsx_path = find_analytics_xlsx()
    html_path = find_analytics_html()
    if xlsx_path is None and html_path is None:
        return None
    if xlsx_path is None:
        return ("html", html_path)
    if html_path is None:
        return ("xlsx", xlsx_path)
    if xlsx_path.stat().st_mtime >= html_path.stat().st_mtime:
        return ("xlsx", xlsx_path)
    return ("html", html_path)


def find_email_links_csv() -> Path | None:
    for path in EMAIL_LINKS_CSV_CANDIDATES:
        if path.exists():
            return path
    return None


def load_email_links() -> dict[str, str]:
    csv_path = find_email_links_csv()
    if csv_path is None:
        return {}
    links: dict[str, str] = {}
    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            card_key = (row.get("card_key") or "").strip()
            web_url = (row.get("web_url") or "").strip()
            if card_key and web_url:
                links[card_key] = web_url
    return links


def parse_xlsx_rows(xlsx_path: Path) -> list[dict[str, str]]:
    ns = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rel_ns = {"p": "http://schemas.openxmlformats.org/package/2006/relationships"}
    with zipfile.ZipFile(xlsx_path) as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in root.findall("x:si", ns):
                text = "".join(node.text or "" for node in item.findall(".//x:t", ns))
                strings.append(text)

        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        workbook_rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        rel_map = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in workbook_rels.findall("p:Relationship", rel_ns)
        }
        first_sheet = workbook.find("x:sheets/x:sheet", ns)
        if first_sheet is None:
            return []
        sheet_rel_id = first_sheet.attrib.get(
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id", ""
        )
        sheet_target = rel_map.get(sheet_rel_id, "worksheets/sheet1.xml")
        sheet_target = sheet_target.lstrip("/")
        if not sheet_target.startswith("xl/"):
            sheet_target = f"xl/{sheet_target}"
        sheet = ET.fromstring(archive.read(sheet_target))
        parsed_rows = []
        for row in sheet.findall("x:sheetData/x:row", ns):
            values: dict[str, str] = {}
            for cell in row.findall("x:c", ns):
                ref = cell.attrib.get("r", "")
                col = re.sub(r"\d", "", ref)
                cell_type = cell.attrib.get("t")
                value_node = cell.find("x:v", ns)
                if cell_type == "inlineStr":
                    text_node = cell.find("x:is/x:t", ns)
                    values[col] = text_node.text if text_node is not None and text_node.text else ""
                elif value_node is None or value_node.text is None:
                    values[col] = ""
                elif cell_type == "s":
                    values[col] = strings[int(value_node.text)]
                else:
                    values[col] = value_node.text
            parsed_rows.append(values)
    return parsed_rows


class GoogleSheetHtmlTableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[str]] = []
        self._in_tr = False
        self._in_cell = False
        self._capture = False
        self._row: list[str] = []
        self._cell: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if tag == "tr":
            self._in_tr = True
            self._row = []
        elif self._in_tr and tag in {"td", "th"}:
            cell_class = attr_map.get("class", "") or ""
            self._in_cell = True
            self._capture = "freezebar-cell" not in cell_class
            self._cell = []
        elif self._capture and tag == "br":
            self._cell.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._in_cell:
            if self._capture:
                self._row.append(html.unescape("".join(self._cell)).strip())
            self._in_cell = False
            self._capture = False
        elif tag == "tr" and self._in_tr:
            if self._row:
                self.rows.append(self._row)
            self._in_tr = False

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._cell.append(data)


def parse_html_rows(html_path: Path) -> list[dict[str, str]]:
    parser = GoogleSheetHtmlTableParser()
    parser.feed(html_path.read_text(encoding="utf-8", errors="ignore"))
    if len(parser.rows) < 2:
        return []
    header_row = parser.rows[0]
    columns = header_row[1:]
    parsed_rows: list[dict[str, str]] = []
    for row in parser.rows[1:]:
        if len(row) < 2:
            continue
        row_number = row[0]
        if not row_number.isdigit():
            continue
        values: dict[str, str] = {"ROW": row_number}
        for index, value in enumerate(row[1:]):
            if index >= len(columns):
                continue
            col = columns[index]
            if col:
                values[col] = value
        parsed_rows.append(values)
    return parsed_rows


HTML_ANALYTICS_COLUMN_LABELS = {
    "C": "Baseline 2025",
    "D": "Target",
    "E": "Real Q1",
    "F": "% of target",
    "G": "01 Ene-12 Feb",
    "H": "13-19 Feb",
    "I": "20-26 Feb",
    "J": "27 Feb-05 Mar",
    "K": "06-12 Mar",
    "L": "13-19 Mar",
    "M": "20-26 Mar",
    "N": "27 Mar-02 Abr",
    "O": "03-09 Abr",
}


def html_analytics_columns(include_target: bool = False) -> list[tuple[str, str]]:
    columns = [
        ("C", HTML_ANALYTICS_COLUMN_LABELS["C"]),
        ("E", HTML_ANALYTICS_COLUMN_LABELS["E"]),
        ("G", HTML_ANALYTICS_COLUMN_LABELS["G"]),
        ("H", HTML_ANALYTICS_COLUMN_LABELS["H"]),
        ("I", HTML_ANALYTICS_COLUMN_LABELS["I"]),
        ("J", HTML_ANALYTICS_COLUMN_LABELS["J"]),
        ("K", HTML_ANALYTICS_COLUMN_LABELS["K"]),
        ("L", HTML_ANALYTICS_COLUMN_LABELS["L"]),
        ("M", HTML_ANALYTICS_COLUMN_LABELS["M"]),
        ("N", HTML_ANALYTICS_COLUMN_LABELS["N"]),
        ("O", HTML_ANALYTICS_COLUMN_LABELS["O"]),
    ]
    if include_target:
        columns.insert(1, ("D", HTML_ANALYTICS_COLUMN_LABELS["D"]))
    return columns


def parse_analytics_rows(xlsx_path: Path) -> list[dict]:
    parsed_rows = parse_xlsx_rows(xlsx_path)
    return parse_analytics_rows_from_parsed_rows(parsed_rows)


def parse_analytics_rows_from_parsed_rows(parsed_rows: list[dict[str, str]]) -> list[dict]:
    if not parsed_rows:
        return []
    default_labels = {
        "C": "Baseline 2025",
        "D": "Real Q1",
        "E": "01 Ene-12 Feb",
        "F": "13-19 Feb",
        "G": "20-26 Feb",
    }

    def normalized_col_label(raw: str, col: str) -> str:
        text = (raw or "").strip()
        if not text:
            return default_labels.get(col, col)
        if normalize_text(text) in {"valor referencia", "valor de referencia"}:
            return "Baseline 2025"
        return text

    metric_names = {"emails delivered", "open emails", "open rate", "clicks", "ctr"}
    entries: list[dict] = []
    i = 0
    while i < len(parsed_rows):
        row = parsed_rows[i]
        title = (row.get("A") or "").strip()
        normalized_title = normalize_text(title)
        if not title or normalized_title in {"name of image"}:
            i += 1
            continue
        if normalized_title in metric_names:
            i += 1
            continue

        date_columns = [
            ("C", normalized_col_label(row.get("C", ""), "C")),
            ("D", normalized_col_label(row.get("D", ""), "D")),
            ("E", normalized_col_label(row.get("E", ""), "E")),
            ("F", normalized_col_label(row.get("F", ""), "F")),
            ("G", normalized_col_label(row.get("G", ""), "G")),
        ]

        metrics = []
        j = i + 1
        while j < len(parsed_rows):
            metric_row = parsed_rows[j]
            metric_name = (metric_row.get("A") or "").strip()
            normalized_metric = normalize_text(metric_name)
            if not metric_name:
                break
            if normalized_metric not in metric_names:
                break
            points = []
            for col, label in date_columns:
                points.append({"label": label, "value": metric_row.get(col, "")})
            metrics.append({"name": metric_name, "points": points})
            j += 1

        if metrics:
            entries.append({"title": title, "metrics": metrics})
            i = j
        else:
            i += 1

    return entries


def parse_analytics_rows_from_dashboard_html(parsed_rows: list[dict[str, str]]) -> list[dict]:
    if not parsed_rows:
        return []
    metric_names = {"emails delivered", "open emails", "open rate", "clicks", "ctr"}
    point_columns = html_analytics_columns()
    entries: list[dict] = []
    i = 0
    while i < len(parsed_rows):
        row = parsed_rows[i]
        title = (row.get("A") or "").strip()
        normalized_title = normalize_text(title)
        if not title or normalized_title in metric_names:
            i += 1
            continue
        metrics = []
        j = i + 1
        while j < len(parsed_rows):
            metric_row = parsed_rows[j]
            metric_name = (metric_row.get("A") or "").strip()
            normalized_metric = normalize_text(metric_name)
            if not metric_name or normalized_metric not in metric_names:
                break
            points = [{"label": label, "value": metric_row.get(col, "")} for col, label in point_columns]
            metrics.append({"name": metric_name, "points": points})
            j += 1
        if metrics:
            entries.append({"title": title, "metrics": metrics})
            i = j
        else:
            i += 1
    return entries


def rows_in_ranges(parsed_rows: list[dict[str, str]], ranges: list[tuple[int, int]]) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for idx, row in enumerate(parsed_rows, start=1):
        if any(start <= idx <= end for start, end in ranges):
            selected.append(row)
    return selected


def is_row_range_analytics_source(path: Path | None) -> bool:
    if path is None:
        return False
    normalized = normalize_text(path.stem)
    return normalized.startswith("111 os nurturing content leadership")


def parse_summary_sections_from_parsed_rows(parsed_rows: list[dict[str, str]]) -> list[dict]:
    if not parsed_rows:
        return []
    metric_names = {"emails delivered", "open emails", "open rate", "clicks", "ctr"}
    default_labels = {
        "C": "Baseline 2025",
        "D": "Target",
        "E": "Real Q1",
        "F": "01 Ene-12 Feb",
        "G": "13-19 Feb",
        "H": "20-26 Feb",
    }
    sections: list[dict] = []
    i = 0
    while i < len(parsed_rows):
        row = parsed_rows[i]
        title = (row.get("A") or "").strip()
        normalized_title = normalize_text(title)
        if not title or normalized_title in metric_names:
            i += 1
            continue

        metrics = []
        j = i + 1
        while j < len(parsed_rows):
            metric_row = parsed_rows[j]
            metric_name = (metric_row.get("A") or "").strip()
            normalized_metric = normalize_text(metric_name)
            if not metric_name or normalized_metric not in metric_names:
                break
            values = {}
            for col in "CDEFGH":
                values[col] = format_analytics_value(metric_name, metric_row.get(col, ""))
            metrics.append({"name": metric_name, "values": values})
            j += 1
        if metrics:
            active_cols = []
            for col in "CDEFGH":
                has_values = any(metric["values"].get(col, "—") != "—" for metric in metrics)
                raw_label = (row.get(col) or "").strip()
                if normalize_text(raw_label) in {"valor referencia", "valor de referencia"}:
                    raw_label = "Baseline 2025"
                if has_values or raw_label:
                    active_cols.append({"key": col, "label": raw_label or default_labels.get(col, col)})
            sections.append({"title": title, "columns": active_cols, "metrics": metrics})
            i = j
            continue
        i += 1
    return sections


def parse_summary_section_from_dashboard_html(parsed_rows: list[dict[str, str]], title_match: str, display_title: str) -> list[dict]:
    metric_names = {"emails delivered", "open emails", "open rate", "clicks", "ctr"}
    summary_columns = html_analytics_columns(include_target=True)
    for i, row in enumerate(parsed_rows):
        title = (row.get("A") or "").strip()
        if normalize_text(title) != normalize_text(title_match):
            continue
        metrics = []
        j = i + 1
        while j < len(parsed_rows):
            metric_row = parsed_rows[j]
            metric_name = (metric_row.get("A") or "").strip()
            normalized_metric = normalize_text(metric_name)
            if not metric_name or normalized_metric not in metric_names:
                break
            metrics.append(
                {
                    "name": metric_name,
                    "values": {
                        col: format_analytics_value(metric_name, metric_row.get(col, ""))
                        for col, _label in summary_columns
                    },
                }
            )
            j += 1
        if metrics:
            active_columns = [
                {"key": col, "label": label}
                for col, label in summary_columns
                if any(metric["values"].get(col, "—") != "—" for metric in metrics)
            ]
            return [
                {
                    "title": display_title,
                    "columns": active_columns,
                    "metrics": metrics,
                }
            ]
    return []


def find_timeline_summary_xlsx(group_key: str) -> Path | None:
    dynamic_patterns = {
        "timeline-1-onboarding-flujo-1-y-2-en-only": "Timeline 1 - Onboarding*.xlsx",
        "timeline-2-nuevos-destinos-en-es": "Timeline 2 - Nuevos Destinos*.xlsx",
    }
    pattern = dynamic_patterns.get(group_key)
    dynamic_candidates = []
    if pattern:
        dynamic_candidates = sorted(
            [*ROOT.glob(pattern), *ROOT.parent.glob(pattern)],
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )
    for path in dynamic_candidates:
        if path.exists():
            return path
    for path in TIMELINE_SUMMARY_XLSX_CANDIDATES_BY_GROUP.get(group_key, []):
        if path.exists():
            return path
    return None


def format_table_cell_value(raw_value: str) -> str:
    value = (raw_value or "").strip()
    if not value:
        return "—"
    if re.fullmatch(r"-?\d+\.0+", value):
        return value.split(".", 1)[0]
    return value


def parse_timeline_one_summary_sections(xlsx_path: Path) -> list[dict]:
    rows = parse_xlsx_rows(xlsx_path)
    if not rows:
        return []
    metric_names = {"emails delivered", "open emails", "open rate", "clicks", "ctr"}
    default_labels = {
        "B": "Baseline 2025",
        "C": "Target",
        "D": "Real Q1",
        "E": "01 Ene-12 Feb",
        "F": "13-19 Feb",
        "G": "20-26 Feb",
    }
    sections: list[dict] = []
    i = 0
    while i < len(rows):
        row = rows[i]
        title = (row.get("A") or "").strip()
        normalized_title = normalize_text(title)
        header_hint = normalize_text(row.get("B", "")) in {
            "valor referencia",
            "valor de referencia",
            "baseline 2025",
            "target",
        } or normalize_text(row.get("C", "")) == "target"
        if not title or not header_hint:
            i += 1
            continue
        if normalized_title in metric_names:
            i += 1
            continue

        metrics = []
        j = i + 1
        while j < len(rows):
            metric_row = rows[j]
            metric_name = (metric_row.get("A") or "").strip()
            normalized_metric = normalize_text(metric_name)
            if not metric_name or normalized_metric not in metric_names:
                break
            metrics.append(
                {
                    "name": metric_name,
                    "values": {col: format_table_cell_value(metric_row.get(col, "")) for col in "BCDEFG"},
                }
            )
            j += 1
        if metrics:
            display_title = title
            if normalize_text(title) == normalize_text("Timeline 1 - Onboarding Flujo 1 y 2 (EN Only)"):
                display_title = "Total Onboarding EN"
            active_cols = []
            for col in "BCDEFG":
                has_values = any(metric["values"].get(col, "—") != "—" for metric in metrics)
                if has_values or (row.get(col) or "").strip():
                    raw_label = (row.get(col) or "").strip()
                    if normalize_text(raw_label) in {"valor referencia", "valor de referencia"}:
                        raw_label = "Baseline 2025"
                    active_cols.append({"key": col, "label": raw_label or default_labels.get(col, col)})
            sections.append({"title": display_title, "columns": active_cols, "metrics": metrics})
            i = j
            continue
        i += 1
    return sections


def load_timeline_summary_sections(group_key: str) -> list[dict]:
    xlsx_path = find_timeline_summary_xlsx(group_key)
    if xlsx_path is None:
        return []
    try:
        return parse_timeline_one_summary_sections(xlsx_path)
    except (OSError, ValueError, KeyError, ET.ParseError, zipfile.BadZipFile):
        return []


def timeline_one_summary_markup(summary_sections: list[dict]) -> str:
    if not summary_sections:
        return ""
    section_markup = []
    for section in summary_sections:
        header_cells = "".join(f"<th>{html.escape(col['label'])}</th>" for col in section["columns"])
        rows = []
        for metric in section["metrics"]:
            value_cells = "".join(
                f"<td>{html.escape(metric['values'].get(col['key'], '—'))}</td>" for col in section["columns"]
            )
            rows.append(f"<tr><th>{html.escape(metric['name'])}</th>{value_cells}</tr>")
        section_markup.append(
            '<section class="timeline-inline-analytics-section">'
            f"<h3>{html.escape(section['title'])}</h3>"
            '<div class="timeline-inline-analytics-table-wrap">'
            '<table class="timeline-inline-analytics-table">'
            f"<thead><tr><th>Metric</th>{header_cells}</tr></thead>"
            f"<tbody>{''.join(rows)}</tbody>"
            "</table>"
            "</div>"
            "</section>"
        )
    return f'<div class="timeline-inline-analytics">{"".join(section_markup)}</div>'


def load_analytics_map() -> dict[tuple[str, ...], dict]:
    analytics_source = preferred_analytics_source()
    if analytics_source is None:
        return {}
    source_kind, source_path = analytics_source
    try:
        if source_kind == "html":
            entries = parse_analytics_rows_from_dashboard_html(parse_html_rows(source_path))
        elif is_row_range_analytics_source(source_path):
            parsed_rows = parse_xlsx_rows(source_path)
            entries = parse_analytics_rows_from_parsed_rows(
                rows_in_ranges(parsed_rows, [(23, 134), (143, 211)])
            )
        else:
            entries = parse_analytics_rows(source_path)
    except (OSError, ValueError, KeyError, ET.ParseError, zipfile.BadZipFile):
        return {}
    result: dict[tuple[str, ...], dict] = {}
    for entry in entries:
        flow_key = analytics_key(entry["title"])
        place_key = flow_place_key(entry["title"])
        if place_key is not None:
            result[("flow_place", place_key[0], place_key[1], place_key[2])] = entry
        if flow_key != ("", ""):
            result[("flow", flow_key[0], flow_key[1])] = entry
        phase_key = phase_lang_place_key(entry["title"])
        if phase_key is not None:
            result[("phase", phase_key[0], phase_key[1], phase_key[2])] = entry
    return result


def entry_for_doc(analytics_map: dict[tuple[str, ...], dict], label: str) -> dict | None:
    flow, variant = analytics_key(label)
    if not flow:
        phase_key = phase_lang_place_key(label)
        if phase_key is None:
            return None
        direct = analytics_map.get(("phase", phase_key[0], phase_key[1], phase_key[2]))
        if direct:
            return direct
        if phase_key[2] != "general":
            fallback = analytics_map.get(("phase", phase_key[0], phase_key[1], "general"))
            if fallback:
                return fallback
        return None
    place_key = flow_place_key(label)
    if place_key is not None:
        exact_place = analytics_map.get(("flow_place", place_key[0], place_key[1], place_key[2]))
        if exact_place:
            return exact_place
        has_place_specific_family = any(
            key[:3] == ("flow_place", place_key[0], place_key[1]) for key in analytics_map
        )
        if has_place_specific_family:
            return None
    if variant and ("flow", flow, variant) in analytics_map:
        return analytics_map[("flow", flow, variant)]
    return analytics_map.get(("flow", flow, ""))


def format_analytics_value(metric_name: str, raw_value: str) -> str:
    value = (raw_value or "").strip()
    if value == "":
        return "—"
    metric_lower = metric_name.lower()
    try:
        number = float(value)
    except ValueError:
        return value
    if "rate" in metric_lower or metric_lower == "ctr":
        return f"{number * 100:.1f}%"
    if number.is_integer():
        return f"{int(number)}"
    return f"{number:.3f}".rstrip("0").rstrip(".")


def analytics_overlay_markup(entry: dict | None) -> str:
    if not entry:
        return (
            '<div class="miro-card-analytics" hidden>'
            '<button class="miro-card-analytics-close" type="button" aria-label="Close analytics">×</button>'
            '<h4>Analytics</h4>'
            '<p class="miro-card-analytics-empty">No analytics data yet.</p>'
            "</div>"
        )

    metric_rows = []
    for metric in entry["metrics"]:
        values = "".join(
            f'<li><span class="miro-card-analytics-point-label">{html.escape(point["label"])}</span>'
            f'<strong>{html.escape(format_analytics_value(metric["name"], point["value"]))}</strong></li>'
            for point in metric["points"]
        )
        metric_rows.append(
            '<li class="miro-card-analytics-metric">'
            f'<p>{html.escape(metric["name"])}</p>'
            f'<ul>{values}</ul>'
            "</li>"
        )

    return (
        '<div class="miro-card-analytics" hidden>'
        '<button class="miro-card-analytics-close" type="button" aria-label="Close analytics">×</button>'
        f'<h4>{html.escape(entry["title"])}</h4>'
        f'<ul class="miro-card-analytics-list">{"".join(metric_rows)}</ul>'
        "</div>"
    )


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
    stem = path.stem.strip()
    # Primary ordering: phase number regardless of the rest of the filename.
    phase_match = re.match(r"^\[(?:fase\s*|f)\s*(\d+)\]\s*(.+)$", stem, re.IGNORECASE)
    if phase_match:
        phase = int(phase_match.group(1))
        rest = phase_match.group(2).strip()
        # Secondary ordering inside a phase: owners first, then non-owners; ES before EN.
        audience_rank = 2
        if re.search(r"\bpropietarios\b", rest, re.IGNORECASE) and not re.search(
            r"\bno\s+propietarios\b", rest, re.IGNORECASE
        ):
            audience_rank = 0
        elif re.search(r"\bno\s+propietarios\b", rest, re.IGNORECASE):
            audience_rank = 1
        language_rank = 2
        if re.search(r"\bEN\b", rest, re.IGNORECASE):
            language_rank = 0
        elif re.search(r"\bES\b", rest, re.IGNORECASE):
            language_rank = 1
        return (0, phase, audience_rank, language_rank, rest.lower())

    pattern = re.compile(
        r"^\[(?:Fase\s*|F)\s*(\d+)\]\s*(?:Nuevos destinos\s*-\s*)?"
        r"(Propietarios|No propietarios)\s*-\s*(ES|EN)$",
        re.IGNORECASE,
    )
    match = pattern.match(stem)
    if match:
        phase = int(match.group(1))
        audience = match.group(2).strip().lower()
        language = match.group(3).strip().upper()
        audience_rank = 0 if audience == "propietarios" else 1
        language_rank = 0 if language == "EN" else 1
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
    - [Fase 2] Nuevos destinos Mallorca - No propietarios - EN -> [F2] - Nuevos destinos Mallorca - No propietarios - EN
    Other names are returned as-is (without extension).
    """
    stem = path.stem.strip()
    pattern = re.compile(r"^\[(?:Fase\s*|F\s*)(\d+)\]\s*(.+)$", re.IGNORECASE)
    match = pattern.match(stem)
    if match:
        phase = match.group(1)
        rest = match.group(2).strip()
        rest = re.sub(r"^Nuevos destinos\s*-\s*", "", rest, flags=re.IGNORECASE)
        # Timeline 2 naming cleanup: hide audience segment in UI labels.
        rest = re.sub(r"^No\s+propietarios\s*-\s*", "", rest, flags=re.IGNORECASE)
        rest = re.sub(r"\s*-\s*No\s+propietarios\b", "", rest, flags=re.IGNORECASE)
        rest = re.sub(r"\s{2,}", " ", rest).strip(" -")
        return f"[F{phase}] - {rest}"
    return stem


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


def timeline_content_for_root(
    timelines: list[dict], analytics_map: dict[tuple[str, ...], dict], email_links: dict[str, str]
) -> str:
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
            entry = entry_for_doc(analytics_map, doc.get("raw_label", doc["label"]))
            card_key = f'{group["key"]}::{doc["slug"]}'
            email_url = email_links.get(card_key)
            email_button = (
                f'<a class="miro-open-link miro-card-action miro-card-action-email" href="{html.escape(email_url, quote=True)}" '
                f'target="_blank" rel="noopener noreferrer" aria-label="Open {doc["label"]} in HubSpot web version">Email</a>'
                if email_url
                else ""
            )
            cards.append(
                '<article class="miro-card">'
                '<div class="miro-card-head">'
                '<div class="miro-card-head-row">'
                '<div class="miro-card-meta">'
                f'<span class="miro-card-index">#{i}</span>'
                f'<span class="miro-card-comment-count" data-card-count-for="{card_key}" aria-label="0 comments">0</span>'
                "</div>"
                '<div class="miro-card-actions">'
                f'<button class="miro-card-action miro-card-action-open" type="button" aria-label="Open {doc["label"]} in full screen">Open</button>'
                f"{email_button}"
                f'<button class="miro-card-action miro-card-action-analytics" type="button" aria-label="Analytics for {doc["label"]}">Analytics</button>'
                "</div>"
                "</div>"
                f'<p class="miro-card-title">{doc["label"]}</p>'
                "</div>"
                f'<div class="miro-card-stage" data-card-key="{card_key}" '
                f'data-card-label="{group["label"]} • {doc["label"]}">'
                f'<img class="miro-card-image" src="Images/{quote(doc["rel_path"])}" alt="{doc["alt"]}" loading="lazy" />'
                '<div class="pin-layer"></div>'
                f"{analytics_overlay_markup(entry)}"
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
        "<h1 class=\"timeline-root-title\">VIVLA HS FLOWS</h1>"
        "<p>Left-to-right sequence. <span class=\"timeline-helper-break\">Click on any email to view it full screen.</span></p>"
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


def timeline_content_for_group(
    group: dict,
    analytics_map: dict[tuple[str, ...], dict],
    summary_sections_by_group: dict[str, list[dict]],
    email_links: dict[str, str],
) -> str:
    cards = []
    for i, doc in enumerate(group["docs"], start=1):
        entry = entry_for_doc(analytics_map, doc.get("raw_label", doc["label"]))
        card_key = f'{group["key"]}::{doc["slug"]}'
        email_url = email_links.get(card_key)
        email_button = (
            f'<a class="miro-open-link miro-card-action miro-card-action-email" href="{html.escape(email_url, quote=True)}" '
            f'target="_blank" rel="noopener noreferrer" aria-label="Open {doc["label"]} in HubSpot web version">Email</a>'
            if email_url
            else ""
        )
        cards.append(
            '<article class="miro-card">'
            '<div class="miro-card-head">'
            '<div class="miro-card-head-row">'
            '<div class="miro-card-meta">'
            f'<span class="miro-card-index">#{i}</span>'
            f'<span class="miro-card-comment-count" data-card-count-for="{card_key}" aria-label="0 comments">0</span>'
            "</div>"
            '<div class="miro-card-actions">'
            f'<button class="miro-card-action miro-card-action-open" type="button" aria-label="Open {doc["label"]} in full screen">Open</button>'
            f"{email_button}"
            f'<button class="miro-card-action miro-card-action-analytics" type="button" aria-label="Analytics for {doc["label"]}">Analytics</button>'
            "</div>"
            "</div>"
            f'<p class="miro-card-title">{doc["label"]}</p>'
            "</div>"
            f'<div class="miro-card-stage" data-card-key="{card_key}" '
            f'data-card-label="{group["label"]} • {doc["label"]}">'
            f'<img class="miro-card-image" src="../Images/{quote(doc["rel_path"])}" alt="{doc["alt"]}" loading="lazy" />'
            '<div class="pin-layer"></div>'
            f"{analytics_overlay_markup(entry)}"
            "</div>"
            "</article>"
        )

    track_content = (
        f'<div class="miro-board-track">{"".join(cards)}</div>'
        if cards
        else '<p class="timeline-empty-group">No images in this folder yet.</p>'
    )
    summary_markup = timeline_one_summary_markup(summary_sections_by_group.get(group["key"], []))

    return (
        '<div class="layout">'
        '<section class="main-pane timeline-summary">'
        '<div class="miro-board-head">'
        f"<h1>{group['label']}</h1>"
        "<p>Left-to-right sequence. <span class=\"timeline-helper-break\">Click on any email to view it full screen.</span></p>"
        f"{summary_markup}"
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
    analytics_map = load_analytics_map()
    email_links = load_email_links()
    summary_sections_by_group = {
        group_key: load_timeline_summary_sections(group_key)
        for group_key in TIMELINE_SUMMARY_XLSX_CANDIDATES_BY_GROUP
    }
    analytics_source = preferred_analytics_source()
    if analytics_source is not None and analytics_source[0] == "html":
        try:
            html_rows = parse_html_rows(analytics_source[1])
            summary_sections_by_group["timeline-1-onboarding-flujo-1-y-2-en-only"] = (
                parse_summary_section_from_dashboard_html(
                    html_rows, "Total Onboarding EN", "Total Onboarding EN"
                )
            )
            summary_sections_by_group["timeline-2-nuevos-destinos-en-es"] = (
                parse_summary_section_from_dashboard_html(
                    html_rows, "Total Marketplace campaign", "Total Nuevos Destinos (EN + ES)"
                )
            )
        except OSError:
            pass
    elif analytics_source is not None and analytics_source[0] == "xlsx" and is_row_range_analytics_source(analytics_source[1]):
        try:
            parsed_rows = parse_xlsx_rows(analytics_source[1])
            summary_sections_by_group["timeline-1-onboarding-flujo-1-y-2-en-only"] = (
                parse_summary_sections_from_parsed_rows(rows_in_ranges(parsed_rows, [(2, 21)]))
            )
            summary_sections_by_group["timeline-2-nuevos-destinos-en-es"] = (
                parse_summary_sections_from_parsed_rows(rows_in_ranges(parsed_rows, [(135, 140)]))
            )
        except (OSError, ValueError, KeyError, ET.ParseError, zipfile.BadZipFile):
            pass
    docs: list[dict] = []
    seen: set[str] = set()
    for group in timeline_groups:
        group_docs: list[dict] = []
        for path in group["files"]:
            rel_path = path.relative_to(IMAGE_DIR).as_posix()
            label = html.escape(display_label(path))
            raw_label = display_label(path)
            slug = unique_slug(seen, slugify(rel_path))
            doc = {
                "path": path,
                "rel_path": rel_path,
                "label": label,
                "raw_label": raw_label,
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
                "label": "VIVLA HS FLOWS",
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
                custom_content=timeline_content_for_root(timeline_groups, analytics_map, email_links),
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
                custom_content=timeline_content_for_group(
                    group, analytics_map, summary_sections_by_group, email_links
                ),
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
