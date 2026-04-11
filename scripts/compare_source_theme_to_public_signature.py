#!/usr/bin/env python3
"""
Compare a fetched local source theme tree against the known public asset signature.

This helps answer: "Does the fetched theme look like the current public site's theme?"
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path("/workspace")
SIGNATURE_PATH = ROOT / "docs" / "generated" / "kuulu-public-asset-signature.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def walk_local_files(base: Path):
    return [p for p in base.rglob("*") if p.is_file()]


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: compare_source_theme_to_public_signature.py <local-theme-dir>")

    local_base = Path(sys.argv[1]).resolve()
    if not local_base.exists() or not local_base.is_dir():
        raise SystemExit(f"Local theme dir not found: {local_base}")

    signature = json.loads(SIGNATURE_PATH.read_text(encoding="utf-8"))
    local_files = walk_local_files(local_base)
    local_names = {p.name: p for p in local_files}

    print(f"Local theme dir: {local_base}")
    portal_ids = signature.get("portal_ids", [])
    print(f"Known public portal(s): {', '.join(portal_ids) if portal_ids else 'unknown'}")
    print()

    matched = []
    missing = []

    unique_names = signature.get("summary", {}).get("unique_asset_names", [])
    for filename in unique_names:
        if filename in local_names:
            matched.append(
                {
                    "filename": filename,
                    "local_path": str(local_names[filename]),
                    "local_sha256": sha256(local_names[filename]),
                }
            )
        else:
            missing.append(filename)

    print(f"Matched by filename: {len(matched)}")
    for item in matched:
        print(f"  - {item['filename']} -> {item['local_path']}")

    print()
    print(f"Missing from local fetch: {len(missing)}")
    for name in missing:
        print(f"  - {name}")

    print()
    if matched:
        print("Interpretation:")
        print("  The fetched source likely contains files that correspond to the public theme build.")
    else:
        print("Interpretation:")
        print("  No direct filename matches found. Either the fetched theme is different,")
        print("  assets are renamed during build, or the wrong remote path was fetched.")


if __name__ == "__main__":
    main()
