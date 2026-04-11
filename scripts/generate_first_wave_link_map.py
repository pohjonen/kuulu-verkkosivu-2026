#!/usr/bin/env python3
"""
Generate an internal link preservation map for first-wave pages.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests


ROOT = Path("/workspace")
OUT_JSON = ROOT / "docs" / "generated" / "kuulu-first-wave-link-map.json"
OUT_MD = ROOT / "docs" / "generated" / "kuulu-first-wave-link-map.md"

FIRST_WAVE = [
    ("homepage-v2", "https://www.kuulu.fi/"),
    ("video-service-v2", "https://www.kuulu.fi/videotuotanto"),
    ("training-v2", "https://www.kuulu.fi/koulutus"),
    ("digimarkkinointi-v2", "https://www.kuulu.fi/digimarkkinointi"),
    ("case-studies-v2", "https://www.kuulu.fi/case-studies"),
    ("yhteystiedot-v2", "https://www.kuulu.fi/yhteystiedot"),
]

ASSET_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".webp",
    ".pdf",
    ".mp4",
    ".mp3",
    ".css",
    ".js",
    ".ico",
)


def fetch(url: str) -> str:
    return requests.get(url, timeout=20).text


def normalize(url: str, base_url: str) -> str | None:
    if url.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None

    absolute = urljoin(base_url, url)
    parsed = urlparse(absolute)
    if parsed.netloc not in {"www.kuulu.fi", "kuulu.fi"}:
        return None

    path = parsed.path or "/"
    if path.endswith("/") and path != "/":
        path = path[:-1]

    if path.startswith(("/hubfs", "/hs-fs", "/_hcms", "/hs")):
        return None
    if path.endswith(ASSET_EXTENSIONS):
        return None

    return f"https://www.kuulu.fi{path}"


def classify_target(url: str) -> str:
    path = urlparse(url).path
    if path == "/":
        return "homepage"
    if path.startswith("/case-studies/") or path.startswith("/referenssit/"):
        return "reference-detail"
    if path in {"/case-studies", "/asiakasreferenssit"}:
        return "reference-index"
    if path.startswith("/ihmiset/"):
        return "person-profile"
    if path in {"/yhteystiedot", "/tietosuojaseloste"}:
        return "company-info"
    if any(x in path for x in ["koulutus", "tekoaly", "tekoalyn", "zero-click", "perjantaipulssi"]):
        return "training"
    if path in {"/videotuotanto", "/brandivideo", "/tv-mainos-tuotanto", "/videotuotanto_vanha"}:
        return "video-service"
    return "service-or-other"


def extract_links(page_id: str, url: str) -> dict:
    html = fetch(url)
    seen: dict[str, dict] = {}

    for href, body in re.findall(r'<a [^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.S):
        normalized = normalize(href, url)
        if not normalized:
            continue
        label = " ".join(re.sub(r"<[^>]+>", " ", body).split())
        if normalized not in seen:
            seen[normalized] = {
                "target_url": normalized,
                "target_type": classify_target(normalized),
                "labels": [],
            }
        if label and label not in seen[normalized]["labels"]:
            seen[normalized]["labels"].append(label)

    links = sorted(seen.values(), key=lambda item: item["target_url"])
    return {
        "page_id": page_id,
        "source_url": url,
        "link_count": len(links),
        "internal_links": links,
    }


def write_md(payload: list[dict]):
    lines = [
        "# Kuulu first wave link map",
        "",
        "Tämä tiedosto kokoaa ensimmäisen aallon sivujen sisäiset linkit, jotta v2-cutoverissa yksikään kriittinen sisäinen polku ei katoa.",
        "",
    ]

    for page in payload:
        lines.append(f"## {page['page_id']}")
        lines.append("")
        lines.append(f"- Source URL: `{page['source_url']}`")
        lines.append(f"- Internal links: {page['link_count']}")
        lines.append("")
        for link in page["internal_links"]:
            labels = ", ".join(f"`{label}`" for label in link["labels"]) if link["labels"] else "no text labels"
            lines.append(
                f"- `{link['target_url']}` ({link['target_type']}) — labels: {labels}"
            )
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    payload = [extract_links(page_id, url) for page_id, url in FIRST_WAVE]
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(payload)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
