# Media Enhancements - 2026-02-17

## Yhteenveto

Lisätty media-tuki (kuvat/videot) viiteen cinematic-moduuliin. Kaikki muutokset ovat taaksepäin yhteensopivia - vanhat moduuli-instanssit toimivat edelleen ilman mediaa.

---

## 1. cinematic_before_after.module

### Lisätyt kentät (fields.json)

```json
{
  "name": "before_image",
  "label": "Ennen – kuva",
  "type": "image"
}
```

```json
{
  "name": "after_image",
  "label": "Jälkeen – kuva",
  "type": "image"
}
```

### Template-muutokset (module.html)

- Lisätty kuva-elementti molempiin kortteihin (before/after)
- Kuva näytetään vain jos `module.before_image.src` / `module.after_image.src` on asetettu
- Kuvat renderöidään korttien yläosaan ennen otsikkoa
- Käyttää lazy loading -optimointia

### Käyttötapaus

Visuaalinen ennen/jälkeen -vertailu, esim.:
- Prosessi ennen ja jälkeen palvelun
- Dashboard-vertailut
- Tuloskuvat

---

## 2. cinematic_vertical_timeline.module

### Lisätyt kentät (fields.json)

Lisätty `steps`-ryhmän sisään:

```json
{
  "name": "step_image",
  "label": "Kuva (valinnainen)",
  "type": "image"
}
```

### Template-muutokset (module.html)

- Lisätty kuva jokaisen vaiheen sisältöön
- Kuva näytetään vain jos `step.step_image.src` on asetettu
- Sijoitettu kuvauksen jälkeen
- Tukee lazy loading -optimointia

### Käyttötapaus

Havainnollistaa prosessin vaiheita visuaalisesti:
- Prosessidiagrammit
- Työnkulun esimerkit
- Tulos-screenshotit jokaisessa vaiheessa

---

## 3. cinematic_accordion_cards.module

### Lisätyt kentät (fields.json)

Lisätty `accordion_items`-ryhmän sisään:

```json
{
  "id": "card_image",
  "name": "card_image",
  "label": "Kuva (valinnainen)",
  "required": false,
  "locked": false,
  "type": "image"
}
```

### Template-muutokset (module.html)

- Lisätty kuva accordion-sisällön alkuun (accordion-inner)
- Kuva näytetään vain jos `item.card_image.src` on asetettu
- Renderöidään ennen tekstisisältöä
- Lazy loading käytössä

### Käyttötapaus

Rikastaa FAQ- tai info-kortteja visuaalisella materiaalilla:
- Screenshot-esimerkit
- Kaaviot
- Infografiikat

---

## 4. cinematic_comparison_table.module

### Lisätyt kentät (fields.json)

Hero-media yläosaan (ennen vertailutaulukkoa):

```json
{
  "name": "header_media_type",
  "label": "Hero-media tyyppi",
  "type": "choice",
  "choices": [
    ["none", "Ei mediaa"],
    ["image", "Kuva"],
    ["video", "Video"]
  ],
  "default": "none"
}
```

```json
{
  "name": "header_image",
  "label": "Hero-kuva",
  "type": "image",
  "visibility": {
    "controlling_field": "header_media_type",
    "operator": "EQUAL",
    "controlling_value_regex": "image"
  }
}
```

```json
{
  "name": "header_video_url",
  "label": "Video URL",
  "type": "text",
  "visibility": {
    "controlling_field": "header_media_type",
    "operator": "EQUAL",
    "controlling_value_regex": "video"
  }
}
```

### Template-muutokset (module.html)

- Lisätty hero-media-osio otsikon ja ingressin jälkeen
- Ehdollinen renderöinti perustuen `header_media_type`-valintaan:
  - `image`: Näyttää kuvan
  - `video`: Näyttää video-iframe:n
  - `none`: Ei mediaa (oletusarvo)
- Video-wrapper responsive-embeddia varten
- Lazy loading molemmissa

### Käyttötapaus

Lisää visuaalista vaikuttavuutta vertailutaulukkoon:
- Demo-video palvelusta
- Hero-kuva joka kuvaa vertailun ytimen
- Infografiikka-video

---

## 5. cinematic_rich_pricing.module

### Lisätyt kentät (fields.json)

Sama hero-media-rakenne kuin #4:

```json
{
  "name": "header_media_type",
  "label": "Hero-media tyyppi",
  "type": "choice",
  "choices": [
    ["none", "Ei mediaa"],
    ["image", "Kuva"],
    ["video", "Video"]
  ],
  "default": "none"
}
```

```json
{
  "name": "header_image",
  "label": "Hero-kuva",
  "type": "image",
  "visibility": {
    "controlling_field": "header_media_type",
    "operator": "EQUAL",
    "controlling_value_regex": "image"
  }
}
```

```json
{
  "name": "header_video_url",
  "label": "Video URL",
  "type": "text",
  "visibility": {
    "controlling_field": "header_media_type",
    "operator": "EQUAL",
    "controlling_value_regex": "video"
  }
}
```

### Template-muutokset (module.html)

- Lisätty hero-media-osio otsikon ja ingressin jälkeen
- Sama ehdollinen renderöinti kuin comparison table
- Video-wrapper responsive-embeddia varten
- Lazy loading molemmissa

### Käyttötapaus

Tuo hinnoittelusivulle visuaalista sisältöä:
- Selitysvideo hinnoittelusta
- Hero-kuva joka kuvaa arvoa
- Demo-materiaalit

---

## Tekniset huomiot

### JSON-validointi

Kaikki fields.json-tiedostot validoitu:
- ✓ cinematic_before_after.module/fields.json
- ✓ cinematic_vertical_timeline.module/fields.json
- ✓ cinematic_accordion_cards.module/fields.json
- ✓ cinematic_comparison_table.module/fields.json
- ✓ cinematic_rich_pricing.module/fields.json

### Taaksepäin yhteensopivuus

- Kaikki media-kentät ovat valinnaisia
- Vanhassa sisällössä ei näytetään mediaa (ei rikkoudu)
- Ehdollinen renderöinti: `{% if module.field.src %}`

### Optimoinnit

- Lazy loading kaikissa kuvissa ja videoissa
- Video-iframe käyttää `loading="lazy"` attribuuttia
- Kuvat käyttävät alt-tekstiä saavutettavuuden vuoksi

### Tyylittely

- Ei muutettu olemassaolevaa CSS:ää
- Uudet elementit käyttävät luokkia:
  - `.card-image` (before_after)
  - `.step-image` (vertical_timeline)
  - `.accordion-image` (accordion_cards)
  - `.comparison-hero-media` / `.pricing-hero-media` (hero-media)
  - `.video-wrapper` (responsive video embed)

### Toiminnallisuus säilytetty

- Accordion-kortit toimivat edelleen normaalisti
- JavaScript-toiminnallisuus ei muuttunut
- Timeline AOS-animaatiot säilytetty
- Kaikki CTA:t ja linkit toimivat

---

## Muokatut tiedostot

1. `/kuulu-theme-2025-dev/modules/cinematic_before_after.module/fields.json`
2. `/kuulu-theme-2025-dev/modules/cinematic_before_after.module/module.html`
3. `/kuulu-theme-2025-dev/modules/cinematic_vertical_timeline.module/fields.json`
4. `/kuulu-theme-2025-dev/modules/cinematic_vertical_timeline.module/module.html`
5. `/kuulu-theme-2025-dev/modules/cinematic_accordion_cards.module/fields.json`
6. `/kuulu-theme-2025-dev/modules/cinematic_accordion_cards.module/module.html`
7. `/kuulu-theme-2025-dev/modules/cinematic_comparison_table.module/fields.json`
8. `/kuulu-theme-2025-dev/modules/cinematic_comparison_table.module/module.html`
9. `/kuulu-theme-2025-dev/modules/cinematic_rich_pricing.module/fields.json`
10. `/kuulu-theme-2025-dev/modules/cinematic_rich_pricing.module/module.html`

---

## Seuraavat askeleet

1. **Testaus HubSpotissa:**
   - Lataa moduulit HubSpot Design Manageriin
   - Testaa jokaista moduulia uudella sisällöllä
   - Varmista että vanhat instanssit toimivat

2. **CSS-tyylittely:**
   - Lisää tarvittavat tyylit cinematic.css:ään:
     - `.card-image` (max-width, border-radius, spacing)
     - `.step-image` (responsive sizing)
     - `.accordion-image` (max-width, margin)
     - `.comparison-hero-media`, `.pricing-hero-media`
     - `.video-wrapper` (16:9 aspect ratio responsive)

3. **Dokumentaatio:**
   - Päivitä käyttöohjeet editoreille
   - Lisää esimerkit mediakenttien käytöstä

---

**Päivitetty:** 2026-02-17  
**Tekijä:** Claude Sonnet 4.5  
**Tila:** Valmis testattavaksi
