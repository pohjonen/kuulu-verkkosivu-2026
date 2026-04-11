# Foundation seed data

Tämä tiedosto kokoaa ensimmäisten foundation-forkkien tärkeimmät seed-tiedot source-theme-moduuleista.

## hero-cinematic-v2

- Source module: `cinematic_hero.module`
- Target role: `hero`
- Exists in source: `True`
- Source label: `01 – Hero-osio`
- Categories: `['media']`
- Content types: `['LANDING_PAGE', 'SITE_PAGE']`

### Highlight fields

- `background_type` (choice) — label: `Taustan tyyppi`
- `background_video_url` (text) — label: `Taustavideon URL`
- `background_video_file` (file) — label: `Videotiedosto`
- `background_image` (image) — label: `Taustakuva`
- `section_tag` (text) — label: `Osion tunniste`
- `headline` (text) — label: `Pääotsikko`
- `headline_highlight` (text) — label: `Otsikon korostusosa (vihreä)`
- `lead_text` (text) — label: `Ingressi`
- `sub_text` (text) — label: `Alateksti`
- `cta_primary_text` (text) — label: `Ensisijainen CTA -teksti`
- `cta_primary_url` (text) — label: `Ensisijainen CTA -linkki`
- `cta_secondary_text` (text) — label: `Toissijainen CTA -teksti`
- `cta_secondary_url` (text) — label: `Toissijainen CTA -linkki`

## problem-grid-v2

- Source module: `cinematic_problem_list.module`
- Target role: `problem-grid`
- Exists in source: `True`
- Source label: `03 – Listaus (kuvake + teksti)`
- Categories: `['body_content', 'text']`
- Content types: `['SITE_PAGE']`

### Highlight fields

- `section_tag` (text) — label: `Osion tagi`
- `headline` (text) — label: `Pääotsikko`

## service-pillars-v2

- Source module: `cinematic_two_engines.module`
- Target role: `two-engines-to-pillars`
- Exists in source: `True`
- Source label: `04 – Korttipari`
- Categories: `['body_content']`
- Content types: `['SITE_PAGE']`

### Highlight fields

- `section_tag` (text) — label: `Osion tunniste`
- `headline` (text) — label: `Pääotsikko`
- `intro_text` (text) — label: `Ingressi`

## stats-trust-band-v2

- Source module: `cinematic_metrics.module`
- Target role: `metrics`
- Exists in source: `True`
- Source label: `07 – Mittarit + kuva`
- Categories: `['body_content']`
- Content types: `['SITE_PAGE']`

### Highlight fields

- `section_tag` (text) — label: `Osion tunniste`
- `headline` (text) — label: `Pääotsikko`

## lead-capture-form-cta-v2

- Source module: `cinematic_koulutus_form.module`
- Target role: `form-cta`
- Exists in source: `True`
- Source label: `12 – Koulutusyhteydenotto (lomake)`
- Categories: `['forms_and_buttons']`
- Content types: `['SITE_PAGE']`

### Highlight fields

- `section_tag` (text) — label: `Osion tunniste`
- `headline` (text) — label: `Pääotsikko`
- `form_id` (text) — label: `HubSpot Form ID`
