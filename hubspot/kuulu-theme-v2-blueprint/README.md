# Kuulu theme v2 blueprint

Tämä hakemisto on paikallinen blueprint-runko Kuulun v2-teemalle.

Se on generoitu manifesteistä:

- `docs/generated/kuulu-v2-page-manifest.json`
- `docs/generated/kuulu-v2-module-manifest.json`

## Tarkoitus

- antaa selkeä paikallinen runko ennen oikean HubSpot-teeman exportia
- helpottaa template- ja moduulirakenteen hahmottamista
- pienentää riskiä, että live-teemaan kosketaan ennenaikaisesti

## Sisältö

- 6 inventoidun ei-blogi-sivuston v2-sivua blueprint-muodossa
- 15 moduulia blueprint-muodossa

## Huomio

Tämä EI ole vielä oikea tuotantoteema. Kun HubSpot-auth/export on saatavilla:

1. haetaan nykyinen teema `hubspot/source-theme/`-hakemistoon
2. kloonataan siitä oikea `hubspot/kuulu-theme-v2/`
3. siirretään tämän blueprintin päätökset oikeaan v2-teemaan
