#!/usr/bin/env bash
set -euo pipefail

echo "== HubSpot bootstrap status =="
echo

echo "[1/5] CLI version"
hs --version || true
echo

echo "[2/5] Configured accounts"
if hs account list; then
  :
else
  echo "No authenticated accounts configured yet."
fi
echo

echo "[3/5] Doctor output"
mkdir -p "/workspace/hubspot/diagnostics"
hs doctor --output-dir "/workspace/hubspot/diagnostics" || true
if [ -n "$(ls -A "/workspace/hubspot/diagnostics" 2>/dev/null)" ]; then
  echo "Diagnostics written to /workspace/hubspot/diagnostics"
else
  echo "No diagnostics file generated yet."
fi
echo

echo "[4/5] Local config hints"
if [ -f "/workspace/.hsaccount" ]; then
  echo "/workspace/.hsaccount"
fi
if [ -f "$HOME/.hscli/config.yml" ]; then
  echo "$HOME/.hscli/config.yml"
fi
if [ -f "/workspace/hubspot.config.yml" ]; then
  echo "/workspace/hubspot.config.yml"
  if grep -q "portals: \[\]" "/workspace/hubspot.config.yml"; then
    echo "  -> Warning: local hubspot.config.yml is present but empty (portals: [])."
    echo "     Remove or replace it before attempting real auth/bootstrap."
  fi
fi
echo

echo "[5/5] Recommended next step"
echo "Run: hs init"
echo "If you already have a personal access key, you can also use:"
echo "  hs auth --auth-type personalaccesskey --personal-access-key \"<KEY>\""
echo "Then: bash scripts/hubspot_fetch_current_theme.sh <remote-theme-path>"
