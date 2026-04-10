#!/usr/bin/env python3
"""
Generate a public CMS metadata snapshot for all inventoried non-blog pages.

This collects only data visible from the public HTML, but structures it into
machine-readable form for later HubSpot execution work.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urljoin

import requests


ROOT = Path("/workspace")
INVENTORY = ROOT / "docs" / "generated" / "kuulu-public-site-inventory.json"
OUT_JSON = ROOT / "docs" / "generated" / "kuulu-public-cms-metadata.json"
OUT_MD = ROOT / "docs" / "generated" / "kuulu-public-cms-metadata.md"


def load_inventory():
    return json.loads(INVENTORY.read_text(encoding="utf-8"))


def fetch_html(url: str) -> str:
    return requests.get(url, timeout=20).text


def first_match(pattern: str, html: str):
    match = re.search(pattern, html, re.I | re.S)
    return match.group(1) if match else ""


def all_matches(pattern: str, html: str):
    return re.findall(pattern, html, re.I | re.S)


def clean_spaces(value: str) -> str:
    return " ".join(value.split())


def build_page_metadata(row: dict):
    html = fetch_html(row["url"])
    content_id = first_match(r'hs-content-id-([0-9]+)', html)
    content_name = first_match(r'hs-content-name-([^"\']+)', html)
    content_path = first_match(r'hs-content-path-([^"\']*)', html)
    canonical = first_match(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', html)
    portal_id = first_match(r'portalId=(\d+)', html)

    form_ids = sorted(set(all_matches(r'formId["\']?\s*[:=]\s*["\']([a-f0-9-]{20,})["\']', html)))
    hs_form_count = len(re.findall(r'hs-form-frame', html, re.I))

    meeting_links = sorted(
        {
            urljoin(row["url"], href)
            for href in all_matches(r'href=["\']([^"\']*meetings[^"\']*)["\']', html)
        }
    )

    video_embeds = sorted(
        {
            urljoin(row["url"], src)
            for src in all_matches(r'(?:src|href)=["\']([^"\']*(?:vimeo|youtube|wistia)[^"\']*)["\']', html)
        }
    )

    inline_videos = sorted(
        {
            urljoin(row["url"], src)
            for src in all_matches(r'<video[^>]+src=["\']([^"\']+)["\']', html)
        }
    )

    cta_links = []
    for href, label in all_matches(r'<a [^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html):
        label_text = clean_spaces(re.sub(r'<[^>]+>', ' ', label))
        if label_text and any(
            token in label_text.lower()
            for token in ["varaa", "ota yhteyttä", "ilmoittaudu", "pyydä", "tutustu", "lue lisää", "aloita", "katso"]
        ):
            cta_links.append(
                {
                    "label": label_text,
                    "href": urljoin(row["url"], href),
                }
            )

    return {
        "url": row["url"],
        "page_type": row["page_type"],
        "status_code": row["status_code"],
        "title": row["title"],
        "h1": row["h1"],
        "portal_id": portal_id,
        "content_id": content_id,
        "content_name": content_name,
        "content_path": content_path,
        "canonical": canonical,
        "theme_guess": row["current_theme"],
        "uses_hs_form_flag": row["uses_hs_form"],
        "hs_form_count": hs_form_count,
        "form_ids": form_ids,
        "meeting_links": meeting_links,
        "video_embeds": video_embeds,
        "inline_videos": inline_videos,
        "cta_links": cta_links[:20],
    }


def write_md(payload: list[dict]):
    lines = [
        "# Kuulu.fi julkinen CMS metadata",
        "",
        "Tämä tiedosto kokoaa julkisesta HTML:stä saatavan CMS-metadata-snapshotin jokaiselle inventoidulle ei-blogi-sivulle.",
        "",
    ]

    for item in payload:
        lines.extend(
            [
                f"## {item['url']}",
                "",
                f"- Page type: `{item['page_type']}`",
                f"- Title: `{item['title']}`",
                f"- H1: `{item['h1']}`",
                f"- Portal ID: `{item['portal_id'] or 'n/a'}`",
                f"- Content ID: `{item['content_id'] or 'n/a'}`",
                f"- Content path token: `{item['content_path'] or 'n/a'}`",
                f"- Theme guess: `{item['theme_guess']}`",
                f"- HS form count: `{item['hs_form_count']}`",
                "",
                "### Form IDs",
                "",
            ]
        )
        if item["form_ids"]:
            for form_id in item["form_ids"]:
                lines.append(f"- `{form_id}`")
        else:
            lines.append("- none detected")

        lines.extend(["", "### Meeting links", ""])
        if item["meeting_links"]:
            for link in item["meeting_links"]:
                lines.append(f"- `{link}`")
        else:
            lines.append("- none detected")

        lines.extend(["", "### Video embeds", ""])
        if item["video_embeds"] or item["inline_videos"]:
            for link in item["video_embeds"]:
                lines.append(f"- embed: `{link}`")
            for link in item["inline_videos"]:
                lines.append(f"- inline: `{link}`")
        else:
            lines.append("- none detected")

        lines.extend(["", "### CTA links", ""])
        if item["cta_links"]:
            for cta in item["cta_links"]:
                lines.append(f"- `{cta['label']}` → `{cta['href']}`")
        else:
            lines.append("- none detected")

        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    rows = load_inventory()
    payload = [build_page_metadata(row) for row in rows]
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(payload)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
