# Kuulu v2: theme token map

## Tarkoitus

Tämä dokumentti määrittää mitä Brand 2026 -design tokenit tarkoittavat käytännössä v2-teeman `theme.json`- ja base asset -rakenteessa.

Tavoite:

- ankkuroida värit, typografia, spacing, radius, motion ja efektit teematason yhteiseksi lähteeksi
- vähentää modulikohtaista kovakoodausta
- varmistaa, että blueprint ja myöhempi oikea v2-teema käyttävät samaa token-kieltä

---

## 1. Token-kerrokset

V2-teemassa suositellaan viittä token-kerrosta:

1. **Brand tokens**
2. **Semantic tokens**
3. **Layout tokens**
4. **Effect tokens**
5. **Component defaults**

### 1.1 Brand tokens

Nämä vastaavat suoraan Brand 2026 -määrittelyjä.

Esimerkkejä:

- `brand.cinematicBlack = #0a0a0a`
- `brand.cinematicSurface = #141414`
- `brand.neonGreen = #00FF87`
- `brand.greenDeep = #009F4E`
- `brand.textPrimary = #FFFFFF`
- `brand.textSecondary = #A0A0A0`
- `brand.textDim = #6B6B6B`
- `brand.footerBg = #002E27`
- `brand.softPeach = #F9AE8F`

### 1.2 Semantic tokens

Nämä kertovat käyttöroolin, eivät vain väriarvoa.

Esimerkkejä:

- `color.bg.default`
- `color.bg.surface`
- `color.text.default`
- `color.text.muted`
- `color.text.dim`
- `color.accent.primary`
- `color.accent.secondary`
- `color.border.subtle`
- `color.cta.primary.text`

### 1.3 Layout tokens

- `layout.container.maxWidth`
- `layout.section.paddingX`
- `layout.section.paddingY`
- `layout.grid.gap`
- `layout.grid.gapLg`

### 1.4 Effect tokens

- `effect.glow.sm`
- `effect.glow.lg`
- `effect.shadow.card`
- `effect.blur.glass`
- `effect.transition.fast`
- `effect.transition.default`
- `effect.transition.slow`

### 1.5 Component defaults

Komponenttitason oletuksia, joita moduulit käyttävät:

- `component.button.radius`
- `component.card.radius`
- `component.section.radius`
- `component.dropdown.radius`
- `component.input.radius`

---

## 2. Typografia-tokenit

### Fonttiperheet

- `font.display = Bebas Neue`
- `font.body = Inter`
- `font.mono = JetBrains Mono`
- `font.footer = Manrope`

### Koot

- `fontSize.h1 = clamp(3rem, 10vw, 10rem)`
- `fontSize.h2 = clamp(2.5rem, 5vw, 4rem)`
- `fontSize.h3 = 2.5rem`
- `fontSize.h4 = 2rem`
- `fontSize.body = 1.1rem`
- `fontSize.small = 0.875rem`

### Rytmi

- `lineHeight.heading = 1.1`
- `lineHeight.body = 1.6`
- `letterSpacing.heading = 0.02em`
- `letterSpacing.button = 0.05em`

---

## 3. Theme.json -tasolle vietävät päätökset

Kun oikea v2-teema rakennetaan, `theme.json`-tasolla pitäisi vähintään olla:

- värit
- fontit
- spacing-oletukset
- radius-oletukset
- mahdolliset style choices -valinnat editorille

### Valmiit style-variantit editorille

Vapaiden arvojen sijaan editorissa pitäisi näkyä valmiit vaihtoehdot, kuten:

- `default-dark`
- `dark-surface`
- `aurora-soft`
- `aurora-strong`
- `glass`
- `neutral`

Näiden taustalla olevat arvot tulevat theme-token-kerroksesta.

---

## 4. Base asset -runko

V2-teeman blueprintiin ja myöhemmin oikeaan teemaan kannattaa tehdä vähintään nämä jaetut assetit:

- `assets/css/theme-tokens.css`
- `assets/css/theme-base.css`
- `assets/css/theme-utilities.css`
- `assets/css/theme-components.css`
- `assets/js/theme-base.js`

### 4.1 `theme-tokens.css`

Sisältää:

- CSS custom properties
- värit
- fontit
- spacingit
- radiusit
- motion/effect-tokenit

### 4.2 `theme-base.css`

Sisältää:

- body/html resetit
- taustalogiikka
- typografian perustasot
- linkit
- focus state -oletukset
- reduced motion -säännöt

### 4.3 `theme-utilities.css`

Sisältää:

- container-utilityt
- section-spacing utilityt
- text-gradient utilityt
- aurora utilityt
- glass-surface utilityt
- visibility helpers

### 4.4 `theme-components.css`

Sisältää:

- button-variantit
- card-variantit
- badge-variantit
- CTA-variantit
- grid- ja panel-oletukset

### 4.5 `theme-base.js`

Sisältää vain kevyen yhteisen logiikan, esim:

- reduced-motion detection
- mahdolliset kevyt enhancementit
- ei raskasta sivukohtaista liiketoimintalogiikkaa

---

## 5. Mitä EI pidä tehdä

Älä:

- kirjoita joka moduuliin omia kovakoodattuja värejä
- anna jokaiselle moduulille omaa typografialinjaa
- tee aurora/glow-efektejä eri tavalla joka moduulissa
- piilota CTA-varianttien väri- tai padding-päätöksiä yksittäisiin module.css-tiedostoihin

Kaikki nämä kuuluvat teematason yhteiseen kerrokseen.

---

## 6. Blueprintin rooli

Blueprintiin rakennettava `theme.json` ja asset-runko ei vielä ole lopullinen tuotantotiedosto, mutta sen pitää:

- kuvata oikea token-rakenne
- näyttää miten moduulit nojaavat teematason assetteihin
- estää tilanne, jossa myöhempi toteutus lähtee rakentumaan moduulikohtaisesta sekamallista

---

## 7. Yhteenveto

V2-teeman tärkein periaate on:

> brandi asuu ensin teeman yhteisissä tokeneissa, vasta sitten yksittäisissä moduuleissa.

Kun tämä toteutuu:

- moduulit pysyvät kevyempinä
- editori pysyy turvallisempana
- etusivun ja muiden sivujen yhtenäisyys säilyy
- myöhemmät muutokset eivät hajoa moduulikohtaiseksi CSS-velaksi
