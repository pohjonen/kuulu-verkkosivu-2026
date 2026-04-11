#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  hubspot_watch_v2.sh <local-v2-dir> <remote-v2-path> [account]

Examples:
  hubspot_watch_v2.sh "hubspot/kuulu-theme-v2" "themes/kuulu-theme-v2"
  hubspot_watch_v2.sh "hubspot/kuulu-theme-v2" "themes/kuulu-theme-v2" "my-account"

Starts a safe watch/upload flow for the v2 theme only.
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

LOCAL_DIR="$(realpath -m "$1")"
REMOTE_PATH="$2"
ACCOUNT="${3:-}"

if [[ ! -d "$LOCAL_DIR" ]]; then
  echo "Paikallista v2-teemaa ei löydy: $LOCAL_DIR" >&2
  exit 1
fi

if ! command -v hs >/dev/null 2>&1; then
  echo "HubSpot CLI (hs) ei ole asennettu." >&2
  exit 1
fi

if ! hs account list >/dev/null 2>&1; then
  echo "HubSpot-auth puuttuu. Aja ensin: hs account auth" >&2
  exit 1
fi

ACCOUNT_ARGS=()
if [[ -n "$ACCOUNT" ]]; then
  ACCOUNT_ARGS=(--account "$ACCOUNT")
fi

echo "Starting HubSpot watch for v2 theme:"
echo "  Local : $LOCAL_DIR"
echo "  Remote: $REMOTE_PATH"

hs cms watch "$LOCAL_DIR" "$REMOTE_PATH" --initial-upload "${ACCOUNT_ARGS[@]}"
