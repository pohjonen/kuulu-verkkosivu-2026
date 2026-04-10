# Kuulu v2: moduulien kenttämalli ja editor guardrails

## Tarkoitus

Tämä dokumentti määrittää, miten v2-moduulit rakennetaan niin, että ne ovat:

- modulaarisia
- helposti muokattavia ilman koodausta
- visuaalisesti brändinmukaisia
- turvallisia editorissa
- riittävän joustavia kuvalle, videolle, gifille, ikoneille ja tekstille

Pääperiaate:

> Editorille annetaan paljon sisältövaltaa, mutta vähän mahdollisuuksia rikkoa rakennetta.

---

## 1. Yhteinen kenttälogiikka kaikille moduuleille

Jokaisessa moduulissa kentät jaetaan samoihin ryhmiin.

### 1.1 Sisältö

Sisältöryhmä sisältää aina vain varsinaisen viestin:

- section tag
- otsikko
- korostussana tai korostusrakenne
- ingressi / body
- listat / kortit / stepit / FAQ-sisältö

### 1.2 CTA

CTA-ryhmä on erillinen ja vakioitu:

- primary CTA label
- primary CTA link
- primary CTA link type:
  - internal page
  - external url
  - meeting link
  - form trigger (jos käytössä)
- secondary CTA label
- secondary CTA link
- CTA visibility toggle

### 1.3 Media

Media-ryhmä erotetaan sisällöstä:

- media type:
  - image
  - video
  - gif
  - icon
  - none
- desktop media
- mobile media
- alt text
- caption (vain jos moduulin logiikka tarvitsee)
- poster image videoille
- optional thumbnail

### 1.4 Layout

Layoutia ei anneta täysin vapaaksi:

- media position:
  - left
  - right
  - top
  - background
- content width:
  - narrow
  - normal
  - wide
- alignment:
  - left
  - center
- section spacing:
  - compact
  - normal
  - spacious
- card columns:
  - auto
  - 2
  - 3
  - 4

### 1.5 Style

Tyylit rakennetaan rajatuista vaihtoehdoista:

- surface style:
  - transparent
  - dark
  - glass
  - elevated
- background variant:
  - default-dark
  - dark-surface
  - aurora-soft
  - aurora-strong
  - image-overlay
- accent mode:
  - green
  - green-peach
  - neutral
- show grain:
  - on
  - off

### 1.6 Advanced

Advanced-ryhmä on vain tarkoin valittuihin tarpeisiin:

- anchor id
- tracking label
- hide on mobile
- reduced-motion fallback mode

Ei anneta editorille vapaita custom class -kenttiä oletuksena.

---

## 2. Guardrails-periaatteet

## 2.1 Ei vapaita värejä

Editori ei valitse HEX-koodeja.

Sen sijaan käytetään valmiita vaihtoehtoja:

- default-dark
- surface
- aurora-soft
- aurora-strong
- glass
- green-accent

## 2.2 Ei vapaita fonttikokoja

Editori ei säädä otsikoiden tai bodyn typografiaa pikselitasolla.

Sen sijaan:

- heading size:
  - hero
  - section
  - compact
- body size:
  - normal
  - compact

Typografia mapataan aina Brand 2026 -tokenoituun järjestelmään.

## 2.3 Ei vapaita layout-hackeja

Editori ei saa:

- syöttää omia inline-tyylejä
- vaihtaa sarakemääriä rajattomasti
- säätää marginaaleja numerokentillä

Sen sijaan kaikki menee valmiiden varianttien kautta.

## 2.4 Ei vapaata rich textiä premium-rakenteissa

Vapaata rich textiä käytetään vain:

- legal-sivulla
- pitkillä artikkelimaisilla sisältömoduuleilla
- tarkkaan rajatuissa fallback-ratkaisuissa

Hero-, card-, stats-, process-, funnel- ja CTA-moduuleissa käytetään strukturoituja kenttiä.

## 2.5 Media on sallittua, mutta kehystettyä

Kuvaa, videota, giffejä ja ikoneita saa käyttää laajasti, mutta:

- media-alueiden aspect ratio pitää olla määritelty
- videoiden overlayt vakioidaan
- gifit sallitaan vain niihin moduuleihin joissa ne eivät riko suorituskykyä
- ikonit tulevat valmiista valikoimasta tai rajatusta upload-logiikasta

---

## 3. Moduulikohtainen kenttämalli

## 3.1 Hero Cinematic v2

### Käyttö

- etusivu
- palvelusivu
- koulutussivu
- videopalvelusivu
- referenssidetail

### Pakolliset kentät

- section tag
- heading
- lead text
- primary CTA

### Valinnaiset kentät

- highlight word / phrase
- secondary CTA
- eyebrow / badge
- supporting bullet list
- trust row
- media
- background mode

### Guardrails

- max 2 CTA:ta
- max 1 hero media slot
- max 3 trust bullets
- ei vapaata pitkää rich textiä

---

## 3.2 Problem Grid v2

### Käyttö

- palvelusivut
- koulutussivut
- videopalvelusivut

### Rakenne

- section tag
- heading
- optional intro
- repeater cards

### Card-kentät

- icon
- title
- short description
- optional supporting line

### Guardrails

- 3–6 korttia
- yhden kortin kuvaus max rajattu
- ikoni valitaan ennalta määritellystä listasta

---

## 3.3 Audience Split / 95-5 v2

### Käyttö

- etusivu
- strategiset palvelusivut
- koulutussivut

### Rakenne

- heading
- left audience block
- right audience block
- optional conclusion

### Block-kentät

- audience label
- audience percentage
- state description
- key need
- CTA or next step

### Guardrails

- aina 2 blokkia
- prosentteja ei anneta täysin vapaaksi oletuksena
- voidaan käyttää valmiita 95/5 preset-arvoja

---

## 3.4 Service Pillars / Solution Cards v2

### Käyttö

- palvelusivut
- etusivu
- koulutussivut

### Rakenne

- heading
- optional intro
- repeater cards

### Card-kentät

- title
- body
- icon or image
- optional micro-CTA
- optional tag

### Guardrails

- max 4 korttia per rivi
- max 2 tekstikappaletta per kortti
- media valitaan joko icon tai image, ei molempia yhtä aikaa

---

## 3.5 Video Model Comparison v2

### Käyttö

- videotuotanto
- brändivideo
- TV-mainos

### Tarkoitus

Näyttää selkeästi:

- kuvattu
- hybridi
- AI-tehostettu

### Kentät

- section tag
- heading
- intro
- three mode cards

### Jokaisen mode cardin kentät

- model name
- positioning line
- best for
- bullet list
- optional media

### Guardrails

- aina 3 korttia
- järjestystä ei rikota
- terminologia pidetään yhtenäisenä koko sivustolla

---

## 3.6 Process Steps v2

### Käyttö

- palvelusivut
- videopalvelusivut
- koulutussivut

### Kentät

- heading
- intro
- repeater steps

### Step-kentät

- step number
- step title
- step description
- optional result line

### Guardrails

- 3–6 askelta
- step numbering tulee automaattisesti
- editori ei syötä numeroita käsin oletuksena

---

## 3.7 Stats / Trust Band v2

### Käyttö

- etusivu
- koulutussivut
- videopalvelusivut
- referenssidetailit

### Kentät

- repeater stat items

### Item-kentät

- number
- label
- optional context

### Guardrails

- 2–5 statia
- number ja label lyhyinä
- vältetään pitkiä kappaleita stats-bandissa

---

## 3.8 Reference Grid v2

### Käyttö

- etusivu
- referenssi-indeksi
- palvelusivut

### Kentät

- heading
- optional intro
- repeater case cards

### Case-kentät

- client
- challenge
- result
- image
- page link
- optional tag set

### Guardrails

- kortin sisältö pidetään lyhyenä
- linkin pitää olla page-link tai tarkistettu URL
- ei pitkiä tekstimassoja korteissa

---

## 3.9 Reference Detail Sections v2

### Käyttö

- kaikki case-detailit

### Osat

- case hero
- key facts
- challenge
- solution
- execution
- results
- testimonial
- CTA

### Guardrails

- käytetään vakioitua järjestystä
- case-sivu ei rakennu täysin vapaasti, jotta kaikki caset pysyvät yhtenäisinä

---

## 3.10 Training Agenda v2

### Käyttö

- koulutussivut
- kampanjasivut

### Kentät

- heading
- optional intro
- repeater modules / tracks

### Item-kentät

- item type:
  - day
  - core
  - track
  - module
- title
- summary
- optional duration
- optional bullets

### Guardrails

- agenda on rakenteinen, ei pelkkä vapaa rich text
- päivän / trackin tyyppi valitaan valmiista listasta

---

## 3.11 FAQ v2

### Kentät

- heading
- repeater faq items

### Item-kentät

- question
- answer

### Guardrails

- max suositus 6–8 kysymystä per osio
- vastaukset pidetään tiiviinä

---

## 3.12 Team Grid v2

### Käyttö

- yhteystiedot
- henkilösivujen related experts

### Kentät

- heading
- repeater people

### Person-kentät

- name
- role
- image
- email
- phone
- profile link
- optional expertise tags

### Guardrails

- kuvakoot ja rajaukset yhtenäistetään
- ei vapaata korttirakennetta editorissa

---

## 3.13 Contact Info v2

### Käyttö

- yhteystiedot
- footer-adjacent CTA blocks

### Kentät

- office repeater
- billing info rich text
- optional form select
- optional meeting link

### Guardrails

- toimipistekortit rakenteisina kenttinä
- laskutustiedot voidaan sallia hallitussa rich text -kentässä

---

## 3.14 Final CTA v2

### Käyttö

- lähes kaikilla sivuilla loppukonversiona

### Kentät

- heading
- lead
- primary CTA
- secondary CTA
- optional trust line

### Guardrails

- aina selkeä seuraava askel
- ei yli kahta CTA:ta
- ei raskasta mediaa oletuksena

---

## 4. Media-logiikan erityissäännöt

### 4.1 Kuvat

- sallitaan hero-, card- ja team-moduuleissa
- editori ei säädä kuvasuhdetta vapaasti
- lazy load oletuksena, jos toteutus sallii

### 4.2 Videot

- sallitaan hero-, reference-, training- ja video-moduuleissa
- desktop ja mobile versio voidaan erottaa
- poster image pakollinen
- autoplay vain tarkkaan harkittuihin heroihin

### 4.3 Giffit

- sallitaan vain valituissa moduuleissa
- ei heroihin oletuksena
- käytetään tukimediana, ei ensisijaisena painopisteenä

### 4.4 Ikonit

- valitaan ennalta määritellystä kirjastosta
- vaihtoehtoisesti upload, mutta rajatulla koolla ja tyyliohjeella

---

## 5. Editorikokemuksen perussäännöt

Moduulin pitää olla editorissa:

- nopeasti ymmärrettävä
- ryhmitelty loogisesti
- käyttökelpoinen ilman ohjekirjaa

### Suositeltu kenttäjärjestys editorissa

1. Content
2. CTA
3. Media
4. Layout
5. Style
6. Advanced

### Kenttäotsikoinnin sääntö

Kenttien nimet kirjoitetaan editorissa liiketoimintalähtöisesti, ei koodilähtöisesti.

Hyvä:

- “Pääotsikko”
- “Ensisijainen CTA”
- “Kortit”
- “Median sijainti”

Huono:

- `hero_title`
- `cta_primary_label`
- `layout_variant_2`

---

## 6. Yhteenveto

Kuulu v2 -moduulit rakennetaan niin, että:

- sisältö on helppo päivittää
- rakenne pysyy hallittuna
- visuaalinen identiteetti ei hajoa editorissa
- live-etusivua ei vaaranneta shared-rakenteiden kautta

Tavoite ei ole maksimaalinen vapaus, vaan:

> maksimaalinen käytännön muokattavuus turvallisten raamien sisällä.
