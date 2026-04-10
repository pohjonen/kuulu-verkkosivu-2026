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
echo
echo "If you do not have a key yet, stop after hs init prompts for it and obtain the key first."
echo
hs init
