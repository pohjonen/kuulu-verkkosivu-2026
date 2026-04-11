# Cinematic-moduulit HubSpotissa – tarkistus

## KRIITTINEN: Miten moduulit pitää ladata

**Kun sivulla on teema käytössä (Kuulu 2026 DEV), HubSpot näyttää editorissa VAIN teeman omat moduulit + globaalit.** Account-level moduulit (`modules/cinematic_*` juuressa) EIVÄT näy.

**Oikea tapa:** Lataa **KOKO TEEMA** kerralla:
```bash
hs cms upload kuulu-theme-2025-dev kuulu-theme-2025-dev
```
ÄLÄ lataa moduuleja erikseen polkuun `modules/` – ne eivät tule teeman scopeen eivätkä näy editorissa.

---

## Mitä tehtiin (analyysin perusteella)

1. **meta.json siivottu** – Kaikista 11 cinematic-moduulista:
   - Poistettu epästandardi `tags`-kenttä (voi rikkoa listauksen).
   - Poistettu `host_template_types` – käytössä vain `content_types: ["SITE_PAGE"]`.
   - Lisätty `categories` (media, body_content, forms_and_buttons, text, design), jotta moduulit löytyvät kategorioista.
   - Pidetty vain: label, global, content_types, icon, smart_type, is_available_for_new_content, categories.

2. **Moduulit kahdessa paikassa** – Ladattu sekä:
   - **Teemaan:** `kuulu-theme-2025-dev/modules/cinematic_*` (template viittaa tähän).
   - **Juureen:** `modules/cinematic_*` (account-level, pitäisi näkyä "All"-listassa).

## Jos moduulit eivät vieläkään näy

1. **Design Manager – virheet**
   - Marketing → Files and Templates → Design Manager.
   - Avaa **modules** (juuressa) tai **kuulu-theme-2025-dev** → **modules**.
   - Avaa esim. **cinematic_hero**. Jos näkyy punainen virhe tai varoitus, korjaa se (yleensä meta.json tai module.html -syntaksi).

2. **Template ja dnd_area**
   - Templatessa on `{% dnd_area %}` ja sisällä 11 kpl `{% dnd_module %}`. Se on oikein: moduulit tulevat oletuksena uudelle sivulle, ja ne pitäisi silti näkyä "Add module" -listassa (voit lisätä toisen instanssin).

3. **BRANDER-vertailu**
   - Jos BRANDER-moduulit näkyvät, avaa yksi Design Managerissa ja vertaa **meta.json**-rakennetta (kentät, content_types, categories). Täsmennä cinematic-metat vastaavaksi tarvittaessa.

## Moduulien nimet listassa

- Cinematic Hero
- Early Bird -lomake
- Ongelmalista (noidankehä)
- Kaksi koneistoa
- Brand DNA ja Tekoäly
- Miten pääset alkuun
- Mittaamme suppilon
- Miksi Kuulu
- Koulutukset CTA
- Referenssit
- Yhteys-CTA

Haku: "Cinematic" tai "Hero" tai "Koulutukset".
