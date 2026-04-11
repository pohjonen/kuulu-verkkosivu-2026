# AGENTS.md

## Cursor Cloud specific instructions

### Projektin yleiskuvaus

Tämä on HubSpot CMS -teemamigraatioprojekti (kuulu.fi). Repo sisältää:
- **Python-skriptejä** (`scripts/`) artefaktien generointiin ja validointiin
- **HubSpot-teematiedostoja** (`hubspot/`) v2-blueprinttia ja myöhemmin source-themea varten
- **Dokumentaatiota** (`docs/`) migraatiosuunnitelmia, manifesteja ja generoitua dataa

### Riippuvuudet

- **Python 3** + `requests`-kirjasto (ainoa kolmannen osapuolen riippuvuus)
- **HubSpot CLI** (`hs`) — asennetaan: `npm install -g @hubspot/cli`
- Ei `package.json`-, `requirements.txt`- eikä muuta formaalia riippuvuustiedostoa

### Tärkeät komennot

Katso `README.md` ja `docs/START_HERE.md` komentojen yksityiskohdista. Tässä yhteenveto:

| Komento | Tarkoitus |
|---|---|
| `bash scripts/refresh_preauth_artifacts.sh` | Uudelleengeneroi kaikki pre-auth-artefaktit (11 vaihetta) |
| `bash scripts/hubspot_bootstrap_status.sh` | Tarkista HubSpot CLI:n ja authin tila |
| `python3 scripts/validate_v2_manifests.py` | Validoi v2-manifestit |
| `python3 scripts/validate_blueprint_scaffold.py` | Validoi blueprint scaffold |
| `python3 scripts/validate_preauth_artifacts.py` | Validoi pre-auth-artefaktien konsistenssi |

### Huomioita kehitysympäristölle

- **`main`-haara on lähes tyhjä.** Projektin varsinainen sisältö on feature-haarassa. Tarkista `git branch -a` nähdäksesi aktiiviset haarat.
- **Refresh-skripti hakee dataa live-sivustolta** (`kuulu.fi`), joten internet-yhteys vaaditaan.
- **HubSpot-autentikointi on suurin blokkeri** jatkotyöhön (source theme fetch, audit, v2 build). Pre-auth-artefaktien generointi ja validointi toimii ilman authia.
- Kaikki Python-skriptit käyttävät vain standardikirjastoa + `requests`. Ei tarvita virtual environmentia.
- Generoidut artefaktit kirjoitetaan `docs/generated/`-hakemistoon. Nämä voivat muuttua skriptien ajossa.
