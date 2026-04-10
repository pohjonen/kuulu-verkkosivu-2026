# Kuulu v2: moduulien toteutusjärjestys ja riippuvuudet

## Tarkoitus

Tämä dokumentti määrittää missä järjestyksessä v2-moduulit kannattaa rakentaa, jotta:

- saadaan nopeasti käyttökelpoinen v2-runko
- minimoidaan regressioriski nykyiseen etusivuun
- rakennetaan ensin eniten uudelleenkäyttöä tuottavat moduulit
- vältetään tilanne, jossa monimutkaiset moduulit estävät etenemisen

---

## 1. Perusperiaate

Rakennusjärjestys ei perustu siihen, mikä moduuli on “hienoin”, vaan siihen:

1. kuinka monta sivua se palvelee
2. kuinka suuri riippuvuus muilla moduuleilla siihen on
3. kuinka paljon se määrittää visuaalista kieltä
4. kuinka turvallisesti sitä voi rakentaa rinnakkain

---

## 2. Aalto 1 — foundation-moduulit

Nämä rakennetaan ensin, koska lähes kaikki sivut nojaavat niihin.

### 2.1 Hero Cinematic v2

**Miksi ensin:**

- määrittää koko v2-kielen
- ratkaisee heading-hierarkian, CTA-logiikan, media-asettelun ja aurora-tyylin
- käytössä lähes kaikilla tärkeillä sivuilla

**Riippuvuudet:**

- theme tokenit
- CTA-tyylit
- media-wrapper-logiikka

### 2.2 Final CTA v2

**Miksi heti alkuun:**

- käytetään lähes kaikilla sivuilla
- määrittää konversiologian loppupäässä
- helppo testata nopeasti

**Riippuvuudet:**

- CTA-patternit
- spacing-tokenit

### 2.3 Problem Grid v2

**Miksi alkuun:**

- toistuu palvelu-, koulutus- ja videopalvelusivuilla
- tärkeä osa Kuulun “tunnistatko nämä” -rakennetta

**Riippuvuudet:**

- icon-järjestelmä
- card-surface-logiikka

### 2.4 Service Pillars v2

**Miksi alkuun:**

- tukee etusivua, palvelusivuja ja koulutussivuja
- toimii moneen tarkoitukseen pienillä variaatioilla

**Riippuvuudet:**

- card-grid-peruslogiikka
- CTA micro-link -malli

---

## 3. Aalto 2 — järjestelmää selittävät moduulit

Nämä moduulit tekevät Kuulun strategisesta logiikasta näkyvän.

### 3.1 Audience Split / 95-5 v2

**Miksi toisessa aallossa:**

- ei välttämätön jokaiselle sivulle
- mutta kriittinen etusivulle ja strategisille palvelusivuille

**Riippuvuudet:**

- kahden palstan sisältölogiikka
- stats/label-tyyppiset elementit

### 3.2 Process Steps v2

**Miksi tässä vaiheessa:**

- prosessirakenteet toistuvat monilla sivuilla
- rakentaa luottamusta ja selkeyttä

**Riippuvuudet:**

- repeater-rakenne
- automaattinen step-numbering

### 3.3 Stats / Trust Band v2

**Miksi tässä vaiheessa:**

- tärkeä uskottavuuselementti
- tarvitaan etusivulla, koulutuksessa, videossa ja caseissa

**Riippuvuudet:**

- number-styling
- typografiatokenit

### 3.4 Reference Grid v2

**Miksi tässä vaiheessa:**

- tarvitaan etusivulla, referenssi-indeksissä ja palvelusivuilla
- auttaa sitomaan sivut referenssidataan

**Riippuvuudet:**

- card-grid-peruslogiikka
- image-ratio-logiikka
- link field -turvallisuus

---

## 4. Aalto 3 — sivutyyppikohtaiset erikoismoduulit

Nämä rakennetaan kun foundation + system-moduulit ovat kunnossa.

### 4.1 Video Model Comparison v2

**Miksi vasta nyt:**

- tarvitsee valmiin card- ja content-patternin
- videopuolen captured / hybrid / AI-logiikka on tärkeä mutta erikoistunut

**Riippuvuudet:**

- Service Pillars / card-rakenne
- media-logiikka

### 4.2 Training Agenda v2

**Miksi vasta nyt:**

- vaatii strukturoitua sisältöä
- hyötyy siitä, että muut spacing- ja typografialinjat ovat jo valmiina

**Riippuvuudet:**

- repeater + grouped content
- heading hierarchy

### 4.3 FAQ v2

**Miksi tässä vaiheessa:**

- teknisesti yksinkertainen, mutta ei kriittinen foundationille
- voidaan tehdä vakio-komponentiksi kun visuaalinen kieli on lukittu

**Riippuvuudet:**

- accordion-käytös
- spacing + surface pattern

### 4.4 Team Grid v2

**Miksi tässä vaiheessa:**

- tarvitaan lähinnä yhteystieto- ja henkilösivuilla

**Riippuvuudet:**

- image-card logic
- contact metadata

### 4.5 Contact Info v2

**Miksi tässä vaiheessa:**

- tärkeä mutta rajatumman käytön moduuli

**Riippuvuudet:**

- structured text fields
- form / meeting CTA integration

---

## 5. Aalto 4 — referenssidetailin vakiorunko

### 5.1 Reference Detail Sections v2

**Miksi vasta tässä:**

- kannattaa rakentaa vasta kun:
  - hero
  - stats
  - quote/testimonial
  - CTA
  - content sections
  ovat jo olemassa tai ainakin määritelty

**Riippuvuudet:**

- Hero Cinematic v2
- Stats / Trust Band v2
- Final CTA v2
- mahdollinen Testimonial-rakenne

---

## 6. Riippuvuusmatriisi lyhyesti

| Moduuli | Riippuu näistä |
| :--- | :--- |
| Hero Cinematic v2 | theme tokenit, CTA-patternit, media-rakenne |
| Final CTA v2 | CTA-patternit, spacing-tokenit |
| Problem Grid v2 | icon-järjestelmä, card surface |
| Service Pillars v2 | card-grid, micro-CTA logic |
| Audience Split / 95-5 v2 | grid logic, stats-style labels |
| Process Steps v2 | repeater logic, heading hierarchy |
| Stats / Trust Band v2 | typografiatokenit, spacing |
| Reference Grid v2 | image-card logic, safe link field |
| Video Model Comparison v2 | card logic, media logic |
| Training Agenda v2 | grouped repeater logic |
| FAQ v2 | accordion behavior |
| Team Grid v2 | people card logic |
| Contact Info v2 | structured contact fields |
| Reference Detail Sections v2 | hero/stats/cta/content blocks |

---

## 7. Ensimmäiset sivut, joilla moduulit kannattaa testata

### Testirakenne 1 — etusivu-v2

Sopii näiden moduulien testiin:

- Hero Cinematic v2
- Problem Grid v2
- Audience Split / 95-5 v2
- Service Pillars v2
- Process Steps v2
- Stats / Trust Band v2
- Reference Grid v2
- Final CTA v2

### Testirakenne 2 — videotuotanto-v2

Sopii näiden moduulien testiin:

- Hero Cinematic v2
- Problem Grid v2
- Video Model Comparison v2
- Process Steps v2
- Stats / Trust Band v2
- FAQ v2
- Final CTA v2

### Testirakenne 3 — koulutus-v2

Sopii näiden moduulien testiin:

- Hero Cinematic v2
- Problem Grid v2
- Service Pillars v2
- Training Agenda v2
- Stats / Trust Band v2
- FAQ v2
- Final CTA v2

---

## 8. Käytännön toteutusjärjestys

### Vaihe 1

- Hero Cinematic v2
- Final CTA v2
- Problem Grid v2
- Service Pillars v2

### Vaihe 2

- Audience Split / 95-5 v2
- Process Steps v2
- Stats / Trust Band v2
- Reference Grid v2

### Vaihe 3

- Video Model Comparison v2
- Training Agenda v2
- FAQ v2
- Team Grid v2
- Contact Info v2

### Vaihe 4

- Reference Detail Sections v2

---

## 9. Miksi tämä järjestys on turvallinen

Tämä järjestys minimoi riskin, koska:

- ensin rakennetaan yleisimmät ja uudelleenkäytettävimmät moduulit
- monimutkaiset erikoismoduulit tehdään vasta kun visuaalinen kieli on lukittu
- sivut voidaan testata vaiheittain rinnakkaisilla v2-sivuilla
- nykyiseen etusivuun ei tarvitse koskea missään vaiheessa

---

## 10. Yhteenveto

Oikea järjestys ei ole “sivu kerrallaan kaikki uusiksi”, vaan:

1. foundation-moduulit
2. järjestelmää selittävät moduulit
3. erikoismoduulit
4. referenssidetailien vakiorunko

Näin Kuulu v2:n modulaarinen järjestelmä voidaan rakentaa hallitusti, nopeasti ja ilman tarpeetonta riskiä live-sivustolle.
