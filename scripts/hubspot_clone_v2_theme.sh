#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  hubspot_clone_v2_theme.sh <source-theme-dir> <dest-v2-dir>

Examples:
  hubspot_clone_v2_theme.sh "hubspot/source-theme" "hubspot/kuulu-theme-v2"

This script creates a safe local v2 copy from a fetched source theme.
It refuses to overwrite an existing destination.
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -ne 2 ]]; then
  usage
  exit 1
fi

SOURCE_DIR="$(realpath -m "$1")"
DEST_DIR="$(realpath -m "$2")"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Lähdeteemaa ei löydy: $SOURCE_DIR" >&2
  exit 1
fi

if [[ -e "$DEST_DIR" ]]; then
  echo "Kohde on jo olemassa, en ylikirjoita: $DEST_DIR" >&2
  exit 1
fi

if [[ "$SOURCE_DIR" == "$DEST_DIR" ]]; then
  echo "Lähde ja kohde eivät voi olla sama polku." >&2
  exit 1
fi

mkdir -p "$(dirname "$DEST_DIR")"
cp -a "$SOURCE_DIR" "$DEST_DIR"

echo "Created v2 clone:"
echo "  Source: $SOURCE_DIR"
echo "  Dest  : $DEST_DIR"
