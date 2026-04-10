#!/usr/bin/env bash
set -euo pipefail

echo "== HubSpot CLI =="
if ! command -v hs >/dev/null 2>&1; then
  echo "HubSpot CLI (hs) not found."
  exit 1
fi

hs --version
echo

echo "== Auth status =="
if hs account list; then
  echo
  echo "HubSpot authentication appears configured."
else
  echo
  echo "HubSpot authentication is not configured yet."
  echo "Run: hs account auth"
fi

echo
echo "== Local HubSpot config files =="
shopt -s nullglob
configs=(hubspot.config.yml hsconfig.* .hscli .config/hubspot)
found_any=0
for item in "${configs[@]}"; do
  if [ -e "$item" ]; then
    found_any=1
    echo "$item"
  fi
done

if [ "$found_any" -eq 0 ]; then
  echo "No local HubSpot project config detected in current directory."
fi
