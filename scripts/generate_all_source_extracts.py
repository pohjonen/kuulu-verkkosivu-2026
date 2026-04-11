#!/usr/bin/env python3
"""
Generate structured source extracts for all inventoried non-blog pages.

This extends the first-wave source extract approach to the full audited site.
"""

from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path

import requests


ROOT = Path("/workspace")
INVENTORY = ROOT / "docs" / "generated" / "kuulu-public-site-inventory.json"
OUT_JSON = ROOT / "docs" / "generated" / "kuulu-all-source-extracts.json"
OUT_MD = ROOT / "docs" / "generated" / "kuulu-all-source-extracts.md"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_html(url: str) -> str:
    return requests.get(url, timeout=20).text


def clean_html_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = unescape(value)
    return " ".join(value.split())


def extract_title(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    return clean_html_text(match.group(1)) if match else ""


def extract_headings(html: str):
    headings = []
    for level in ("h1", "h2", "h3"):
        for match in re.findall(fr"<{level}[^>]*>(.*?)</{level}>", html, re.I | re.S):
            text = clean_html_text(match)
            if text:
                headings.append({"level": level, "text": text})
    return headings


def extract_paragraphs(html: str):
    seen = set()
    paragraphs = []
    for match in re.findall(r"<p[^>]*>(.*?)</p>", html, re.I | re.S):
        text = clean_html_text(match)
        if text and text not in seen:
            seen.add(text)
            paragraphs.append(text)
    return paragraphs


def extract_links(html: str):
    seen = set()
    links = []
    for href, label in re.findall(r"<a [^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", html, re.I | re.S):
        text = clean_html_text(label)
        key = (href, text)
        if href and key not in seen:
            seen.add(key)
            links.append({"href": href, "label": text})
    return links


def classify_ctas(links: list[dict]):
    ctas = []
    keywords = ("varaa", "ota yhteyttä", "ilmoittaudu", "pyydä", "katso", "lue lisää", "tutustu", "aloita")
    for item in links:
        label = item["label"].lower()
        if label and any(keyword in label for keyword in keywords):
            ctas.append(item)
    return ctas


def page_id_from_preview_slug(slug: str, page_type: str) -> str:
    cleaned = slug.strip("/").replace("/", "__").replace("-", "_")
    if not cleaned:
        return "homepage_v2"
    return f"{cleaned}__{page_type}".replace(".", "_")


def build_source_extract(row: dict):
    html = fetch_html(row["url"])
    title = extract_title(html)
    headings = extract_headings(html)
    paragraphs = extract_paragraphs(html)
    links = extract_links(html)
    ctas = classify_ctas(links)
    return {
        "page_id": page_id_from_preview_slug(row["preview_slug"], row["page_type"]),
        "url": row["url"],
        "preview_slug": row["preview_slug"],
        "template": row["v2_template"],
        "page_type": row["page_type"],
        "title": title,
        "headings": headings[:40],
        "paragraphs": paragraphs[:30],
        "cta_candidates": ctas[:40],
        "raw_link_count": len(links),
        "raw_paragraph_count": len(paragraphs),
        "raw_heading_count": len(headings),
    }


def write_md(extracts: list[dict]):
    lines = [
        "# Kuulu v2: all-site source extracts",
        "",
        "Tämä tiedosto kokoaa kaikille inventoiduille ei-blogi-sivuille nykyisestä live-sivusta poimitut raakasisältöfragmentit.",
        "",
    ]

    for extract in extracts:
        lines.extend(
            [
                f"## {extract['page_id']}",
                "",
                f"- URL: `{extract['url']}`",
                f"- Preview slug: `{extract['preview_slug']}`",
                f"- Template: `{extract['template']}`",
                f"- Page type: `{extract['page_type']}`",
                f"- Title: `{extract['title']}`",
                "",
                "### Headingit",
                "",
            ]
        )
        for item in extract["headings"][:10]:
            lines.append(f"- `{item['level']}`: {item['text']}")

        lines.extend(["", "### Ensimmäiset kappaleet", ""])
        for paragraph in extract["paragraphs"][:6]:
            lines.append(f"- {paragraph}")

        lines.extend(["", "### CTA-ehdokkaat", ""])
        for cta in extract["cta_candidates"][:6]:
            label = cta["label"] or "(ei tekstiä)"
            lines.append(f"- [{label}]({cta['href']})")

        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    inventory = load_json(INVENTORY)
    extracts = [build_source_extract(row) for row in inventory]
    OUT_JSON.write_text(json.dumps(extracts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(extracts)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
