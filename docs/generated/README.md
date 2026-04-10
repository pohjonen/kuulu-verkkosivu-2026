## Generated artifacts

Tämä kansio sisältää koneellisesti tuotettuja inventaarioita ja manifesteja, joita käytetään Kuulu v2 -rakenteen suunnittelussa.

### Tiedostot

- `kuulu-public-site-inventory.csv`
  - julkisen ei-blogi-sivuston URL-inventaario taulukkomuodossa
- `kuulu-public-site-inventory.json`
  - sama inventaario JSON-muodossa
- `kuulu-v2-page-manifest.json`
  - ensimmäisen aallon v2-sivujen koneellisesti luettava manifesti
- `kuulu-v2-module-manifest.json`
  - v2-moduulien koneellisesti luettava manifesti

### Uudelleengenerointi

Inventaario:

```bash
python3 scripts/kuulu_public_audit.py
```

V2-manifestit:

```bash
python3 scripts/generate_v2_manifests.py
python3 scripts/validate_v2_manifests.py
```

### Huomio

Manifestit on tarkoitettu suunnittelun, auditoinnin ja myöhemmän HubSpot-toteutuksen pohjaksi. Ne eivät vielä ole HubSpotin lopullisia teematiedostoja.
