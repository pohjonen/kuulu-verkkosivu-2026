#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: bash scripts/run_post_auth_audit.sh <local-source-theme-dir>"
  exit 1
fi

SOURCE_DIR="$1"
REPORT_DIR="/workspace/docs/generated/post-auth-audit"

mkdir -p "$REPORT_DIR"

echo "== HubSpot post-auth audit runner =="
echo

echo "[1/4] Bootstrap status"
bash "/workspace/scripts/hubspot_bootstrap_status.sh" || true
echo

echo "[2/4] Public asset signature match"
python3 "/workspace/scripts/compare_source_theme_to_public_signature.py" "$SOURCE_DIR" | tee "$REPORT_DIR/public-signature-match.txt"
echo

echo "[3/4] Source theme audit"
python3 "/workspace/scripts/audit_fetched_source_theme.py" "$SOURCE_DIR"
if [ -f "/workspace/docs/generated/fetched-source-theme-audit.json" ]; then
  cp "/workspace/docs/generated/fetched-source-theme-audit.json" "$REPORT_DIR/source-theme-audit.json"
fi
if [ -f "/workspace/docs/generated/fetched-source-theme-audit.md" ]; then
  cp "/workspace/docs/generated/fetched-source-theme-audit.md" "$REPORT_DIR/source-theme-audit.md"
fi
echo

echo "[4/4] Next step"
echo "Review:"
echo "  - $REPORT_DIR/public-signature-match.txt"
if [ -f "$REPORT_DIR/source-theme-audit.json" ]; then
  echo "  - $REPORT_DIR/source-theme-audit.json"
fi
if [ -f "$REPORT_DIR/source-theme-audit.md" ]; then
  echo "  - $REPORT_DIR/source-theme-audit.md"
fi
echo
echo "Then decide reuse / fork / replace / protect before cloning v2."
