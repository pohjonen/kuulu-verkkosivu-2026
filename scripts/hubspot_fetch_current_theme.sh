#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  hubspot_fetch_current_theme.sh <remote-theme-path> <local-dest-dir> [account]

Examples:
  hubspot_fetch_current_theme.sh "/@hubspot/marketplace/kuulu-theme" "hubspot/source-theme"
  hubspot_fetch_current_theme.sh "themes/kuulu-theme" "hubspot/source-theme" "my-account"

This script:
  1. verifies HubSpot CLI is installed
  2. verifies authentication exists
  3. fetches the remote theme safely into a local destination
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -lt 2 || $# -gt 3 ]]; then
  usage
  exit 1
fi

REMOTE_PATH="$1"
LOCAL_DEST="$2"
ACCOUNT="${3:-}"

if ! command -v hs >/dev/null 2>&1; then
  echo "HubSpot CLI (hs) ei ole asennettu." >&2
  exit 1
fi

if ! hs account list >/dev/null 2>&1; then
  echo "HubSpot-auth puuttuu. Aja ensin: hs account auth" >&2
  exit 1
fi

DEST_DIR="$(realpath -m "$LOCAL_DEST")"
PARENT_DIR="$(dirname "$DEST_DIR")"

mkdir -p "$PARENT_DIR"

ACCOUNT_ARGS=()
if [[ -n "$ACCOUNT" ]]; then
  ACCOUNT_ARGS=(--account "$ACCOUNT")
fi

echo "Fetching theme from HubSpot:"
echo "  Remote: $REMOTE_PATH"
echo "  Local : $DEST_DIR"

hs cms fetch "$REMOTE_PATH" "$DEST_DIR" --overwrite "${ACCOUNT_ARGS[@]}"

echo "Done."
