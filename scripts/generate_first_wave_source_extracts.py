#!/usr/bin/env python3
"""
Generate structured source extracts for first-wave pages from the live public site.

Purpose:
- capture reusable raw source fragments before HubSpot build starts
- give editors a page-by-page snapshot of headings, paragraphs and CTAs
- provide machine-readable input for future module population
"""

from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path

import requests


ROOT = Path("/workspace")
FIRST_WAVE_HS_DATA = ROOT / "docs" / "generated" / "kuulu-first-wave-hs-data.json"
OUT_JSON = ROOT / "docs" / "generated" / "kuulu-first-wave-source-extracts.json"
OUT_MD = ROOT / "docs" / "generated" / "kuulu-first-wave-source-extracts.md"


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


def build_source_extract(page: dict):
    html = fetch_html(page["url"])
    title = extract_title(html)
    headings = extract_headings(html)
    paragraphs = extract_paragraphs(html)
    links = extract_links(html)
    ctas = classify_ctas(links)

    return {
        "page_id": page["page_id"],
        "url": page["url"],
        "preview_slug": page["preview_slug"],
        "template": page["template"],
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
        "# Kuulu v2: first wave source extracts",
        "",
        "Tämä tiedosto kokoaa ensimmäisen aallon sivuille nykyisestä live-sivusta poimitut raakasisältöfragmentit.",
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
                f"- Title: `{extract['title']}`",
                "",
                "### Headingit",
                "",
            ]
        )
        for item in extract["headings"][:12]:
            lines.append(f"- `{item['level']}`: {item['text']}")

        lines.extend(["", "### Ensimmäiset kappaleet", ""])
        for paragraph in extract["paragraphs"][:8]:
            lines.append(f"- {paragraph}")

        lines.extend(["", "### CTA-ehdokkaat", ""])
        for cta in extract["cta_candidates"][:8]:
            label = cta["label"] or "(ei tekstiä)"
            lines.append(f"- [{label}]({cta['href']})")

        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    payload = load_json(FIRST_WAVE_HS_DATA)
    extracts = [build_source_extract(page) for page in payload["pages"]]
    OUT_JSON.write_text(json.dumps(extracts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(extracts)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
