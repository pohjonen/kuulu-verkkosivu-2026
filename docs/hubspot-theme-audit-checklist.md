# HubSpot-teema-audit: tarkistusrunko authin jälkeen

## Tarkoitus

Tämä dokumentti määrittää täsmällisen auditointirungon heti sitä hetkeä varten, kun HubSpot-auth tai teeman export on käytettävissä.

Tavoite:

- selvittää nykyisen teeman rakenne turvallisesti
- löytää kaikki regressioriskit nykyiselle etusivulle ja muille live-sivuille
- päättää mitä voidaan käyttää uudelleen
- päättää mitä pitää versionoida v2:een

Pääperiaate:

> Auditointi tehdään ennen yhtäkään riskialtista teematason muutosta.

---

## 1. Ennen auditointia

## 1.1 Varmista pääsy

Tarvitaan vähintään toinen näistä:

- `hs account auth` onnistuneesti ajettuna
- nykyinen HubSpot-teema exporttina / repossa

## 1.2 Varmista kohde

Auditoinnissa pitää tietää:

- mikä account / portal on oikea
- mikä teema on tällä hetkellä productionissa
- mikä etusivu on oikeasti live-etusivu
- mitkä domainit ovat käytössä

## 1.3 Dokumentoi auditin konteksti

Kirjaa ylös:

- auditin päivämäärä
- portal/account
- teeman nimi
- live-domainit
- mahdolliset child theme / parent theme -suhteet

---

## 2. Korkeimman riskin kohteet

Auditissa pitää merkitä nämä heti ensimmäiseksi:

### 2.1 Nykyinen etusivu

- mikä template sitä renderöi
- mitä moduuleja sivu käyttää
- mitä global grouppeja sivu käyttää
- mitä CSS/JS-assetteja sivu käyttää

### 2.2 Shared-rakenteet

- header
- footer
- navigation / menu-rakenne
- global partials
- shared CSS
- shared JS
- theme settings / theme fields

### 2.3 Kaikki usean sivun käyttämät moduulit

Jos sama moduuli esiintyy:

- etusivulla
- videotuotannossa
- tv-mainossivulla
- tai useilla legacy-sivuilla

se pitää merkitä riskimoduuliksi.

---

## 3. Theme-rakenne: mitä selvitetään

## 3.1 Theme metadata

Tarkista:

- teeman nimi
- mahdollinen child/parent-rakenne
- käytössä olevat theme settingsit
- theme.json / fields / tokens

Kysymykset:

- onko teemassa jo design token -ajattelu
- löytyvätkö fontit, värit, spacingit, radiusit keskitetysti
- vai onko niitä hajallaan moduuleissa

## 3.2 Templates

Listaa kaikki käytössä olevat:

- page templates
- drag-and-drop templates
- blog templates
- system templates
- landing templates

Merkitse jokaiselle:

- nimi
- käyttötarkoitus
- onko live-käytössä
- käyttääkö sitä etusivu tai muu korkean riskin sivu
- tarvitseeko v2-version

## 3.3 Modules

Listaa kaikki moduulit, erityisesti:

- custom modules
- dnd-section-moduulit
- shared content modules
- form/CTA/video/reference-moduulit

Merkitse jokaiselle:

- nimi
- käyttötarkoitus
- missä sivuissa käytössä
- onko live-etusivulla
- rakenneriski:
  - low
  - medium
  - high
- päätös:
  - reuse
  - wrap
  - fork to v2
  - replace

## 3.4 Global content

Listaa:

- header global group
- footer global group
- mahdolliset global CTA-stripit
- mahdolliset alert / banner -alueet

Merkitse:

- missä käytössä
- voiko tehdä `*-v2` version
- onko pakko säilyttää täysin koskemattomana cutoveriin asti

## 3.5 Assets

Listaa:

- shared CSS
- shared JS
- fontit
- utility assets
- theme asset pipeline

Merkitse:

- mitkä ovat etusivun kannalta kriittisiä
- mitä voidaan kloonata v2:een
- mitä ei saa ylikirjoittaa

---

## 4. Modulaarisuuden auditointi

Auditin tärkeä osa on arvioida:

### 4.1 Mitä voidaan käyttää uudelleen

Esim:

- hero-rakenne
- korttigridit
- CTA-moduulit
- FAQ
- testimonial
- reference cards

### 4.2 Mitä ei kannata käyttää sellaisenaan

Esim:

- legacy light -moduulit
- kovakoodatut content-layoutit
- moduulit joissa on liian vapaa rich text ja vähän guardrailsia
- moduulit joissa ei ole riittäviä media/CTA-rakenteita

### 4.3 Mitä pitää viedä v2-forkiksi

Esim:

- kaikki moduulit joita etusivu käyttää mutta joita pitäisi muuttaa
- kaikki globaalit osat joita ei saa rikkoa
- kaikki moduulit joiden kenttämalli ei tue uutta sisältölogiikkaa

---

## 5. Brand 2026 -yhteensopivuuden auditointi

Tarkista teemasta:

### 5.1 Värit

- onko Cinematic Dark -palette oikeasti olemassa
- käytetäänkö tokenoituja värejä vai kovakoodattuja arvoja
- löytyykö legacy-värivuotoja

### 5.2 Typografia

- onko Bebas Neue käytössä oikein
- onko Inter käytössä oikein
- onko JetBrains Mono / section-tag -tuki olemassa

### 5.3 CTA-logiikka

- onko nykyisissä CTA-moduuleissa pill-muotoinen logiikka
- onko CTA-variantit yhdenmukaiset
- pystyykö editori rikkomaan CTA-tyylin liian helposti

### 5.4 Visuaaliset efektit

- aurora
- glow
- grain
- glass-card
- hover behavior

### 5.5 Accessibility

- focus states
- reduced motion
- kontrastit
- body-fontin minimikoko

---

## 6. Editor guardrails -auditointi

Tarkista moduulikohtaisesti:

- onko kentät jaettu loogisiin ryhmiin
- onko liian paljon vapaata rich textiä
- onko vapaita väri-/spacing-hackeja
- voiko editori rikkoa rakenteen
- puuttuuko media slotteja tai CTA-kenttiä

Merkitse jokaiselle moduulille:

- editor risk:
  - safe
  - unstable
  - dangerous

---

## 7. Live-riskin auditointi

Jokaisesta templaatista / moduulista / assetista pitää tietää:

- vaikuttaako tämä etusivuun
- vaikuttaako tämä useisiin live-sivuihin
- vaikuttaako tämä navigaatioon
- vaikuttaako tämä globaaleihin osiin

Jos vastaus on kyllä, merkitään:

- `DO NOT EDIT DIRECTLY`

---

## 8. Auditin lopputulokset

Auditin jälkeen pitää pystyä tuottamaan nämä listat:

### 8.1 Reuse-lista

Mitä voidaan käyttää v2:ssa lähes sellaisenaan.

### 8.2 Fork-lista

Mistä tehdään v2-versio.

### 8.3 Replace-lista

Mikä rakennetaan kokonaan uudestaan.

### 8.4 Protected-lista

Mihin ei kosketa ennen cutoveria.

---

## 9. Minimituotokset auditista

Kun audit on valmis, vähintään nämä pitää olla dokumentoituna:

- nykyinen teeman rakennekartta
- etusivun dependency-kartta
- shared/global-riskit
- v2-versionoitavat moduulit
- reusable-moduulit
- cutoveriin asti suojatut rakenteet

---

## 10. Suositeltu käytännön suoritusjärjestys authin jälkeen

1. `hs account list`
2. tunnista oikea account / portal
3. listaa tai pullaa teema
4. listaa templates
5. listaa modules
6. tunnista etusivun käyttämät riippuvuudet
7. tunnista global content
8. tee riskimerkinnät
9. päätä:
   - reuse
   - fork
   - replace

---

## Yhteenveto

HubSpot-teema-auditin tarkoitus ei ole vain ymmärtää tiedostoja, vaan estää regressiot.

Tämän checklistin lopputulos on yksi tärkeä päätös:

> mitä voidaan käyttää turvallisesti uudelleen ja mitä ei saa koskea ilman v2-versionointia.
