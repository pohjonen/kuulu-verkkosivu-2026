# Kuulu pre-auth status index

- Portal ID: `450584`
- Auth status: `missing`
- Source theme status: `not_fetched`
- Public inventory pages: `35`
- V2 page manifest count: `6`
- V2 module manifest count: `15`
- First-wave packet count: `6`
- All-page packet count: `35`

## Key artifacts

### inventory
- `docs/generated/kuulu-public-site-inventory.csv`
- `docs/generated/kuulu-public-site-inventory.json`

### manifests
- `docs/generated/kuulu-v2-page-manifest.json`
- `docs/generated/kuulu-v2-module-manifest.json`

### build_packets
- `docs/generated/first-wave-page-build-packets/index.json`
- `docs/generated/all-page-build-packets/index.json`

### safety
- `docs/generated/kuulu-redirect-register.json`
- `docs/generated/kuulu-cutover-checklist.json`
- `docs/generated/kuulu-full-link-graph.json`
- `docs/generated/kuulu-public-asset-signature.json`
- `docs/generated/kuulu-public-cms-metadata.json`

### blueprint
- `hubspot/kuulu-theme-v2-blueprint/`
- `scripts/bootstrap_v2_blueprint.py`
- `scripts/validate_blueprint_scaffold.py`

## Next blocker

Run hs account auth or provide current HubSpot theme export.
