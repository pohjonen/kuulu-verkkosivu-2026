#!/usr/bin/env bash
set -euo pipefail

echo "== HubSpot auth bootstrap =="
echo
echo "This project uses the safer bootstrap path:"
echo "  1) hs init"
echo "  2) hs doctor"
echo "  3) hs account list / info"
echo "  4) fetch source theme"
echo
echo "Expected interactive flow:"
echo "- choose how to authenticate"
echo "- either open HubSpot to copy a personal access key"
echo "- or enter an existing personal access key"
echo "- if hs init fails due to global config mode, fall back to hs account auth"
echo
echo "If you do not have a key yet, stop after hs init prompts for it and obtain the key first."
echo
if ! hs init; then
  echo
  echo "hs init did not complete. Trying fallback:"
  echo "  hs account auth"
  hs account auth
fi
