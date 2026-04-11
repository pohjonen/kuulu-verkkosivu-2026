# Cinematic-teeman uudet moduulit - 17.2.2026

Luotu 7 uutta HubSpot-moduulia cinematic-teemalla.

## 1. TESTIMONIAL SLIDER (cinematic_testimonial_slider.module)
**Sijainti:** `/kuulu-theme-2025-dev/modules/cinematic_testimonial_slider.module/`

**Ominaisuudet:**
- Asiakassitaattien karuselli autoplay-toiminnolla
- Profiilikuva + yrityslogo + sitaatti
- Edellinen/Seuraava-nuolet
- Dot-navigaatio
- Glass-efekti kortissa
- Vihreä accent-väri (#00ff88)

**Kentät:**
- Osion otsikko & alaotsikko
- Testimonials (ryhmä, max 20)
  - Sitaatti (richtext)
  - Henkilön nimi, titteli
  - Yrityksen nimi
  - Profiilikuva
  - Yrityslogo
- Autoplay päällä/pois + nopeus

---

## 2. CASE STUDY CARD (cinematic_case_study_card.module)
**Sijainti:** `/kuulu-theme-2025-dev/modules/cinematic_case_study_card.module/`

**Ominaisuudet:**
- 2-sarake layout (media vasen, sisältö oikea)
- Tuki kuvalle tai videolle
- Haaste + Ratkaisu -osiot ikoneilla
- Metriikka-laatikot tuloksille (max 6)
- Käänteinen layout -vaihtoehto
- CTA-nappi

**Kentät:**
- Asiakkaan nimi, logo, toimiala
- Media-tyyppi (kuva/video)
- Haasteen & ratkaisun otsikot + tekstit
- Metriikka-ryhmä (arvo + selite)
- CTA-teksti & linkki
- Käänteinen layout (boolean)

---

## 3. STICKY NAVIGATION (cinematic_sticky_nav.module)
**Sijainti:** `/kuulu-theme-2025-dev/modules/cinematic_sticky_nav.module/`

**Ominaisuudet:**
- Sivuun kiinnittyvä navigaatio
- Linkit sivun osioihin (anchor-scroll)
- Aktiivinen osio korostettuna vihreällä
- Pystysuuntainen progress bar
- Smooth scroll -toiminto
- Sijainti vasen/oikea

**Kentät:**
- Navigaatio-linkit (ryhmä, max 10)
  - Linkin teksti
  - Anchor ID
- Näytä progress bar (boolean)
- Sijainti (vasen/oikea)

**Huom:** Edellyttää että sivun osioilla on ID-attribuutit.

---

## 4. ROI CALCULATOR (cinematic_roi_calculator.module)
**Sijainti:** `/kuulu-theme-2025-dev/modules/cinematic_roi_calculator.module/`

**Ominaisuudet:**
- 3 kustomoitavaa slideria
- Reaaliaikainen laskenta
- Näyttää: kuukausisäästö, vuosisäästö, ROI %, tehokkuushyöty
- Gradient-sliderit vihreällä
- Sticky results-kortti
- CTA-nappi

**Kentät:**
- Otsikko & alaotsikko
- Slider 1-3: nimi, min, max, oletusarvo
- Tuloksen otsikko
- CTA-teksti & linkki

**Huom:** Laskentakaava mukautettavissa module.html:n JS-osiossa.

---

## 5. HORIZONTAL SCROLL (cinematic_horizontal_scroll.module)
**Sijainti:** `/kuulu-theme-2025-dev/modules/cinematic_horizontal_scroll.module/`

**Ominaisuudet:**
- Vaakasuuntainen scroll-osio
- Snap-to-card toiminto
- Hiiren drag-scroll
- Progress bar + sivunumerointi
- Hover-efektit korteissa
- Kuva tai SVG-ikoni -tuki

**Kentät:**
- Osion otsikko & alaotsikko
- Kortit (ryhmä, 3-20)
  - Kuva tai SVG-ikoni
  - Otsikko
  - Kuvaus
  - Linkki & linkin teksti

---

## 6. ACCORDION CARDS (cinematic_accordion_cards.module)
**Sijainti:** `/kuulu-theme-2025-dev/modules/cinematic_accordion_cards.module/`

**Ominaisuudet:**
- Laajenevat kortit smooth-animaatiolla
- 1 tai 2 saraketta
- SVG-ikoni tuki
- Plus/miinus-ikoni togglena
- Glass-effect kortissa
- Vain yksi kortti kerrallaan auki

**Kentät:**
- Osion otsikko & alaotsikko
- Accordion-kortit (ryhmä, 2-15)
  - SVG-ikoni
  - Otsikko
  - Sisältö (richtext)
- Sarakkeiden määrä (1/2)
- Avaa ensimmäinen oletuksena (boolean)

---

## 7. FLOATING CTA (cinematic_floating_cta.module)
**Sijainti:** `/kuulu-theme-2025-dev/modules/cinematic_floating_cta.module/`

**Ominaisuudet:**
- Sticky CTA-nappi alalaidassa
- Ilmestyy kun scrollataan tietty määrä
- Glow-efekti & pulse-animaatio
- Piilotetaan footerissa
- Ripple-efekti klikkauksessa
- 3 sijaintivaihtoehtoa

**Kentät:**
- CTA-teksti & linkki
- Näytä ikoni (boolean)
- Sijainti (keskellä/vasen/oikea)
- Trigger offset (px)
- Piilota footerissa (boolean)

**Huom:** Global = true, voidaan lisätä kaikille sivuille.

---

## Cinematic-teeman tyylit

Kaikki moduulit käyttävät yhtenäistä tyyliä:

- **Taustaväri:** #0a0a0a (musta)
- **Accent-väri:** #00ff88 (vihreä)
- **Kortit:** Glass-effect (backdrop-blur + läpinäkyvä tausta)
- **Reunat:** rgba(255, 255, 255, 0.1)
- **Hover:** Vihreä glow + scale/translateY
- **Gradientit:** #00ff88 → #00cc6a
- **Box-shadowit:** Vihreä glow-efekti
- **Animaatiot:** Smooth cubic-bezier

---

## Käyttöönotto HubSpotissa

1. Lataa koko teema HubSpottiin: `hs upload kuulu-theme-2025-dev kuulu-theme-2025-dev`
2. Moduulit löytyvät Design Manager > Modules -osiosta
3. Lisää moduuleja sivuille Design Manager > Templates/Pages -osiosta
4. Muokkaa moduulien kenttiä Page Editor -näkymässä

---

## Tekninen info

- Kaikki moduulit responsive
- Breakpointit: 768px, 1024px, 1200px
- JS inline moduuleissa (ei external JS)
- CSS inline (ei external CSS)
- Ei riippuvuuksia ulkoisiin kirjastoihin
- HubL-templating käytössä

---

Luotu: 17.2.2026
Tekijä: Claude Sonnet 4.5
