#!/usr/bin/env bash
set -euo pipefail

echo "== Refresh Kuulu pre-auth planning artifacts =="
echo

echo "[1/10] Public site inventory"
python3 "/workspace/scripts/kuulu_public_audit.py"
echo

echo "[2/10] V2 manifests"
python3 "/workspace/scripts/generate_v2_manifests.py"
python3 "/workspace/scripts/validate_v2_manifests.py"
echo

echo "[3/10] Cutover registers"
python3 "/workspace/scripts/generate_cutover_registers.py"
echo

echo "[4/10] Public asset signature"
python3 "/workspace/scripts/generate_public_asset_signature.py"
echo

echo "[5/10] Public CMS metadata"
python3 "/workspace/scripts/generate_public_cms_metadata.py"
echo

echo "[6/10] First-wave content packs"
python3 "/workspace/scripts/generate_first_wave_content_packs.py"
python3 "/workspace/scripts/generate_first_wave_hs_data.py"
echo

echo "[7/10] Source extracts"
python3 "/workspace/scripts/generate_first_wave_source_extracts.py"
python3 "/workspace/scripts/generate_all_source_extracts.py"
echo

echo "[8/10] Link maps and graph"
python3 "/workspace/scripts/generate_first_wave_link_map.py"
python3 "/workspace/scripts/generate_full_link_graph.py"
echo

echo "[9/10] Build packets"
python3 "/workspace/scripts/generate_first_wave_page_build_packets.py"
python3 "/workspace/scripts/generate_all_page_build_packets.py"
echo

echo "[10/10] Blueprint scaffold"
python3 "/workspace/scripts/bootstrap_v2_blueprint.py"
python3 "/workspace/scripts/validate_blueprint_scaffold.py"
echo

echo "Refresh complete."
