# Kuulu v2: HubSpot-moduulien HubL / fields.json -mapping

## Tarkoitus

Tämä dokumentti toimii siltana nykyisen suunnitteludokumentaation ja varsinaisen HubSpot-moduulien toteutuksen välillä.

Se määrittää:

- miten blueprintissä olevat kentät muunnetaan oikeiksi `fields.json`-määrityksiksi
- millaisia HubL-rakenteita eri moduulityypit tarvitsevat
- missä kohdissa pitää käyttää tarkkaa guardrail-ajattelua
- mitä ei saa jättää “päätetään myöhemmin” -tasolle varsinaista moduulia rakennettaessa

---

## 1. Yleinen mapping-periaate

Blueprintissä kentät on tällä hetkellä kuvattu näin:

- `required_fields`
- `optional_fields`
- `field_groups`
- `guardrails`

Varsinaisessa HubSpot-moduulissa nämä pitää muuntaa:

- `fields.json` kenttäobjekteiksi
- `module.html` HubL-logiikaksi
- `module.css` token-pohjaiseksi tyyliksi
- `module.js` vain kevyeksi progressiiviseksi enhancementiksi

### Sääntö

> `fields.json` ohjaa editoria. `module.html` ei saa joutua paikkaamaan huonosti suunniteltua editorimallia.

---

## 2. Kenttätyyppien suositusmapping

| Blueprint-kenttätyyppi | HubSpot-kenttätyyppi | Huomio |
| --- | --- | --- |
| lyhyt otsikko | `text` | esim. heading, eyebrow |
| pidempi ingressi | `textarea` tai `richtext` | premium-moduuleissa mieluummin `textarea` |
| CTA-label | `text` | lyhyt, max-pituus ohjeistettava |
| CTA-linkki | `link` | mieluummin aina `link`, ei vapaa teksti |
| media | `image`, `file`, `choice` | riippuu moduulin käyttötarkoituksesta |
| ikoni | `choice` | ennalta rajattu ikonilista |
| repeater-kortit | `group` + `repeater: true` | tärkein rakenne korteille |
| tyyli-/layout-variantti | `choice` | ei koskaan vapaa tekstikenttä |
| togglet | `boolean` | esim. show grain, hide on mobile |
| numerot / prosentit | `number` tai `choice` | jos mahdollista, preset-valinnat |

---

## 3. Kenttäryhmien käytännön toteutus

Kaikissa moduuleissa pidetään vakiojärjestys:

1. Content
2. CTA
3. Media
4. Layout
5. Style
6. Advanced

### Miksi tämä on tärkeää

Kun kaikki moduulit käyttäytyvät editorissa samalla tavalla:

- käyttö on nopeampaa
- sisällöntuottajan oppimiskynnys pienenee
- virheiden määrä vähenee

---

## 4. Moduulikohtainen HubL-mapping

## 4.1 Hero Cinematic v2

### Fields.json

Pakolliset:

- `section_tag` → `text`
- `heading` → `text`
- `lead_text` → `textarea`
- `primary_cta_label` → `text`
- `primary_cta_link` → `link`

Valinnaiset:

- `highlight_phrase` → `text`
- `secondary_cta_label` → `text`
- `secondary_cta_link` → `link`
- `eyebrow` → `text`
- `supporting_bullets` → `group repeater`
- `trust_row` → `group repeater`
- `desktop_media_type` → `choice`
- `desktop_image` / `desktop_video` / `desktop_gif`
- `mobile_media_type` → `choice`
- `mobile_image` / `mobile_video` / `mobile_gif`
- `background_variant` → `choice`
- `surface_style` → `choice`

### Module.html

Tarvitsee ehdollista HubL:ää ainakin:

- jos `section_tag` on täytetty → renderöi tag
- jos `highlight_phrase` löytyy otsikosta → korostusspan
- jos primary CTA löytyy → renderöi
- jos secondary CTA löytyy → renderöi
- jos media type = image → renderöi image
- jos media type = video → renderöi video
- jos media type = gif → renderöi file/embed
- jos media type = none → älä renderöi media-wrapperia

### Guardrails

- jos secondary CTA label on täytetty, linkki on myös pakollinen
- media slotteja ei saa olla useita rinnakkain
- hero ei saa sisältää vapaata richtext-blokkia

---

## 4.2 Problem Grid v2

### Fields.json

- `section_tag` → `text`
- `heading` → `text`
- `intro_text` → `textarea`
- `cards` → repeater group

Cardin kentät:

- `icon` → `choice`
- `title` → `text`
- `description` → `textarea`
- `supporting_line` → `text`

### Module.html

- loopataan `cards`
- renderöidään vain täytetyt kortit
- jos kortteja alle 3 tai yli 6, editori pitäisi estää tämä jo kenttätasolla tai ohjeistuksella

### Guardrails

- ei richtextiä korttisisällöissä
- ikonit rajatusta listasta

---

## 4.3 Audience Split / 95-5 v2

### Fields.json

- `heading` → `text`
- `left_block` → group
- `right_block` → group
- `conclusion_text` → `textarea`

Blockin kentät:

- `audience_label` → `text`
- `audience_percentage` → `choice` tai `number`
- `state_description` → `textarea`
- `key_need` → `text`
- `cta_label` → `text`
- `cta_link` → `link`

### Guardrails

- aina 2 blokkia
- jos mahdollista, 95/5 tehdään preset-oletuksilla

---

## 4.4 Service Pillars v2

### Fields.json

- `heading`
- `intro_text`
- `cards` repeater

Card:

- `title`
- `body`
- `media_mode` (`icon` / `image`)
- `icon`
- `image`
- `micro_cta_label`
- `micro_cta_link`
- `tag`

### Guardrails

- media_mode määrittää kumpi kenttä näytetään
- kumpaakaan ei renderöidä jos valinta on tyhjä

---

## 4.5 Video Model Comparison v2

### Fields.json

Ei täysin vapaa repeater.

Suositus:

- `section_tag`
- `heading`
- `intro_text`
- `captured_card` group
- `hybrid_card` group
- `ai_card` group

Näin korttien järjestys ei voi mennä sekaisin editorissa.

### Guardrails

- captured / hybrid / ai järjestys lukitaan
- tätä ei toteuteta avoimena repeaterina ilman erityistä syytä

---

## 4.6 Process Steps v2

### Fields.json

- `heading`
- `intro_text`
- `steps` repeater

Step:

- `title`
- `description`
- `result_line`

### Module.html

- käytä HubL loop + `loop.index`
- älä pyydä editoria syöttämään askelnumeroa

---

## 4.7 Stats / Trust Band v2

### Fields.json

- `section_tag`
- `heading`
- `stat_items` repeater

Item:

- `number`
- `label`
- `context`

### Guardrails

- ei pitkiä tekstikappaleita
- context vain valinnainen täydennys

---

## 4.8 Reference Grid v2

### Fields.json

- `heading`
- `intro_text`
- `tag_filters` repeater (valinnainen)
- `case_cards` repeater

Case:

- `client`
- `challenge`
- `result`
- `image`
- `page_link`
- `tags`

### Guardrails

- `page_link` mieluummin aina `link`-kentällä
- jos sivulinkki puuttuu, korttia ei pitäisi nostaa näkyviin

---

## 4.9 Training Agenda v2

### Fields.json

- `heading`
- `intro_text`
- `agenda_items` repeater

Agenda item:

- `item_type` → `choice`
- `title`
- `summary`
- `duration`
- `bullets` repeater tai textarea

### Guardrails

- item_type arvot rajattava:
  - day
  - core
  - track
  - module

---

## 4.10 FAQ v2

### Fields.json

- `heading`
- `faq_items` repeater

FAQ item:

- `question`
- `answer`

### Guardrails

- vastaus voi olla `textarea` tai rajattu `richtext`
- mieluummin ei vapaita monitasoisia sisältörakenteita

---

## 4.11 Team Grid v2

### Fields.json

- `heading`
- `people` repeater

Person:

- `name`
- `role`
- `image`
- `email`
- `phone`
- `profile_link`
- `expertise_tags`

### Guardrails

- kuva pakollinen jos henkilö näytetään korttina
- jos profile_link puuttuu, kortti voi silti toimia ilman linkkiä

---

## 4.12 Contact Info v2

### Fields.json

- `office_locations` repeater
- `billing_info` → `richtext`
- `form_select` / `form_id`
- `meeting_link`

Office:

- `city`
- `street`
- `postal_code`
- `extra_info`

### Guardrails

- vain laskutustiedoille sallitaan hallittu richtext
- toimistot rakenteisina kenttinä

---

## 5. Meta.json -periaatteet

Kaikille v2-moduuleille suositellaan:

- selkeä label
- kategoria vähintään:
  - `kuulu-v2`
  - `foundation/system/specialized/reference`
- ei oletuksena saataville ennen kuin moduuli on oikeasti toteutuskelpoinen

Blueprintissä `is_available_for_new_content` voi olla false.
Oikeassa v2-teemassa tämä voidaan avata vaiheittain.

---

## 6. Yhteenveto

Seuraava oikea tekninen vaihe authin jälkeen ei ole “mietitään kenttiä uudelleen”, vaan:

1. fetch current source theme
2. audit existing reusable modules
3. siirrä tästä dokumentista kenttälogiikka oikeisiin `fields.json`-määrityksiin
4. toteuta module.html / css / js oikeaan `kuulu-theme-v2`-teemaan

Tärkein sääntö:

> editorin joustavuus rakennetaan kenttäarkkitehtuurilla, ei jälkikäteen module.html-hackeilla.
