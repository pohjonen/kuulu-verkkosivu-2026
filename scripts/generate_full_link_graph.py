#!/usr/bin/env python3
"""
Generate internal link graph for all inventoried non-blog pages.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests


ROOT = Path("/workspace")
INVENTORY = ROOT / "docs" / "generated" / "kuulu-public-site-inventory.json"
OUT_JSON = ROOT / "docs" / "generated" / "kuulu-full-link-graph.json"
OUT_MD = ROOT / "docs" / "generated" / "kuulu-full-link-graph.md"

SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "#")
SKIP_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".webp",
    ".pdf",
    ".zip",
    ".mp4",
    ".mp3",
    ".ico",
    ".css",
    ".js",
    ".xml",
)


def load_inventory():
    return json.loads(INVENTORY.read_text(encoding="utf-8"))


def fetch(url: str) -> str:
    return requests.get(url, timeout=20).text


def normalize(href: str, base_url: str) -> str | None:
    if href.startswith(SKIP_SCHEMES):
        return None
    absolute = urljoin(base_url, href)
    parsed = urlparse(absolute)
    if parsed.netloc not in {"www.kuulu.fi", "kuulu.fi"}:
        return None

    path = parsed.path or "/"
    if path.endswith("/") and path != "/":
        path = path[:-1]

    if path.startswith(("/hubfs", "/hs-fs", "/_hcms", "/hs")):
        return None
    if path.endswith(SKIP_EXTENSIONS):
        return None

    return f"https://www.kuulu.fi{path}"


def classify_link_strength(labels: list[str]) -> str:
    joined = " ".join(labels).lower()
    if any(token in joined for token in ["varaa", "ota yhteyttä", "ilmoittaudu", "pyydä tarjous"]):
        return "cta"
    if any(token in joined for token in ["referens", "case", "koulut", "digimarkkinointi", "videotuotanto"]):
        return "navigational"
    return "contextual"


def main():
    inventory = load_inventory()
    known_urls = {row["url"]: row for row in inventory}
    graph = {}
    inbound = defaultdict(list)

    for row in inventory:
        source_url = row["url"]
        html = fetch(source_url)
        seen: dict[str, list[str]] = {}

        for href, body in re.findall(r'<a [^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.S):
            normalized = normalize(href, source_url)
            if not normalized or normalized not in known_urls:
                continue
            label = " ".join(re.sub(r"<[^>]+>", " ", body).split())
            seen.setdefault(normalized, [])
            if label and label not in seen[normalized]:
                seen[normalized].append(label)

        outgoing = []
        for target, labels in sorted(seen.items()):
            strength = classify_link_strength(labels)
            outgoing.append(
                {
                    "target_url": target,
                    "target_type": known_urls[target]["page_type"],
                    "labels": labels,
                    "strength": strength,
                }
            )
            inbound[target].append(
                {
                    "source_url": source_url,
                    "source_type": row["page_type"],
                    "labels": labels,
                    "strength": strength,
                }
            )

        graph[source_url] = {
            "page_type": row["page_type"],
            "title": row["title"],
            "outgoing_count": len(outgoing),
            "outgoing": outgoing,
        }

    payload = {
        "summary": {
            "node_count": len(known_urls),
            "edge_count": sum(item["outgoing_count"] for item in graph.values()),
        },
        "graph": graph,
        "inbound": dict(sorted(inbound.items())),
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Kuulu full internal link graph",
        "",
        f"- Nodes: {payload['summary']['node_count']}",
        f"- Edges: {payload['summary']['edge_count']}",
        "",
        "## Inbound priority highlights",
        "",
    ]

    ranked = sorted(
        inbound.items(),
        key=lambda item: len(item[1]),
        reverse=True,
    )
    for target, sources in ranked[:25]:
        lines.append(f"- `{target}` ← {len(sources)} internal links")

    lines.extend(["", "## Per-page outgoing links", ""])
    for url, info in graph.items():
        lines.append(f"### {url}")
        lines.append(f"- Type: `{info['page_type']}`")
        lines.append(f"- Outgoing links: {info['outgoing_count']}")
        for item in info["outgoing"]:
            labels = ", ".join(f"`{label}`" for label in item["labels"]) if item["labels"] else "no labels"
            lines.append(
                f"  - `{item['target_url']}` ({item['target_type']}, {item['strength']}) — {labels}"
            )
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
