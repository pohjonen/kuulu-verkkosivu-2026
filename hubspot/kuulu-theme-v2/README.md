# Kuulu Theme 2025

Moderni ja responsiivinen HubSpot-teema Kuulu digimarkkinointitoimistolle. Teema on rakennettu HubSpot:in parhaiden käytäntöjen mukaisesti ja optimoitu markkinointitiimien käyttöön.

## 📋 Sisältö

- [Ominaisuudet](#ominaisuudet)
- [HubSpot Best Practices](#hubspot-best-practices)
- [Asennus](#asennus)
- [Käyttö](#käyttö)
- [Rakenne](#rakenne)
- [Kehitys](#kehitys)
- [Brändivärit](#brändivärit)
- [Lisenssi](#lisenssi)

## ✨ Ominaisuudet

### 🎨 Visuaaliset ominaisuudet
- **Moderni design:** Puhdas ja ammattimainen ulkoasu
- **Responsiivinen:** Optimoitu kaikille laitteille
- **Kuulu-brändi:** Mukautettu Kuulu-brändin väreihin ja tyyliin
- **Animaatiot:** Pehmeät animaatiot ja siirtymät
- **Saavutettavuus:** WCAG 2.1 AA -standardin mukainen
- **Oikeat fontit:** Bebas Neue otsikoille, Open Sans tekstille

### 🔧 Tekniset ominaisuudet
- **HubSpot-optimointi:** Täysin HubSpot-yhteensopiva
- **SEO-valmis:** Optimoitu hakukoneille
- **Nopea lataus:** Optimoitu suorituskykyyn (< 1MB sivu)
- **Modulaarinen:** Helposti muokattavat moduulit
- **Monikielisyys:** Tuki useille kielille
- **Validoidut JSON-tiedostot:** Kaikki kentät oikein määritelty

### 📱 Responsiivisuus
- **Desktop:** Optimoitu suurille näytöille
- **Tablet:** Mukautettu tablet-laitteille
- **Mobiili:** Mobiili-ensimmäinen lähestymistapa

### 🎬 Digimarkkinointi-spesifiset ominaisuudet
- **Case Study -moduulit:** Esittelyt menestystarinoista
- **Video-showcase:** Videotuotannon esittely
- **Tilastokortit:** Tulosten visualisointi
- **Portfolio-grid:** Työn esittely
- **Hero-stats:** Avainlukujen näyttäminen
- **Animaatiot:** Modernit hover-efektit

## 🏆 HubSpot Best Practices

### ✅ Arkkitehtuuri ja suunnittelu
- **Sisältöhierarkia:** Looginen URL-rakenne ja navigaatiomalli
- **Modulaarinen rakenne:** Uudelleenkäytettävät vs. sivukohtaiset moduulit
- **Suorituskyky:** Sivun paino < 1MB, optimoitu kuvat ja JavaScript
- **Responsiivinen strategia:** Mobiili-ensimmäinen lähestymistapa

### ✅ Kehitysstandardit
- **HubL:** Johdonmukainen sisennys ja kommentointi
- **CSS:** BEM-nimeämiskäytäntö, minimoitu spesifisyys
- **JavaScript:** Asynkroninen lataus, minimoitu jQuery-riippuvuudet
- **Lomakkeet:** Progressiivinen profiilointi, inline-validointi

### ✅ HubSpot-spesifiset ominaisuudet
- **Moduulit:** Oikein määritellyt fields.json ja meta.json -tiedostot
- **Kenttätyypit:** Vain sallitut kenttätyypit moduuleissa
- **Teeman kentät:** Ei sisältökenttiä teeman tasolla
- **Dokumentaatio:** Selkeät ohjeet markkinointitiimille

### ✅ Suorituskyvyn optimointi
- **Kuvat:** Responsiiviset kuvat, WebP-tuki, lazy loading
- **JavaScript:** Minimointi, bundlaus, koodin jako
- **CSS:** Minimointi, kriittisen renderöintipolun optimointi
- **Palvelin:** Selaimen välimuisti, pakkaus, CDN

### ✅ Tietoturva
- **Sisältöturva:** CSP-otsikot, XSS-suoja
- **Tietosuoja:** GDPR-yhteensopivuus
- **Kolmannen osapuolen koodi:** Tietoturva-auditit

### ✅ Testaus
- **Toiminnallinen testaus:** Kaikki interaktiiviset elementit
- **Ristikäyttötestaus:** Chrome, Firefox, Safari, Edge
- **Suorituskykytestaus:** Lighthouse, Core Web Vitals
- **Saavutettavuustestaus:** WCAG 2.1 AA

## 🚀 Asennus

1. **Lataa teema** HubSpot Design Manageriin
2. **Aktivoi teema** sivustollasi
3. **Muokkaa sisältöä** HubSpot Content Editorissa
4. **Testaa** eri laitteilla

## 📖 Käyttö

### Perusasetukset

1. **Muokkaa etusivua:**
   - Hero-osio: Otsikko, alaotsikko ja CTA-napit
   - Palvelut: Lisää, muokkaa tai poista palveluita
   - Case Study: Esittele menestystarinasi
   - Video-showcase: Näytä parhaat videosi
   - Referenssit: Päivitä asiakasreferenssit

2. **Muokkaa navigaatiota:**
   - Lisää tai poista valikkolinkkejä
   - Muokkaa valikon tyyliä

3. **Muokkaa footeria:**
   - Yhteystiedot
   - Sosiaalisen median linkit
   - Lisätiedot

### Moduulit

#### Hero Banner
- Taustakuva
- Otsikko ja alaotsikko
- CTA-napit
- Overlay-läpinäkyvyys

#### Palvelut Grid
- Palvelukortit (3 kpl)
- Ikonit ja kuvaukset
- Linkit palvelusivuille

#### Case Study Showcase
- Case study -kortit (2 kpl)
- Kategoriat ja linkit
- Hover-efektit

#### Video Showcase
- Videot ja thumbnailit (2 kpl)
- Play-button -efektit
- CTA-linkit

#### Henkilökohtainen profiili
- Henkilön esittely ja kuva
- Osaamisalueet (vapaamuotoinen teksti)
- Työkokemus (vapaamuotoinen teksti)
- Portfolio-projektit (vapaamuotoinen teksti)
- Yhteystiedot ja sosiaalinen media

## 📁 Rakenne

```
Kuulu-Theme-2025/
├── theme.json              # Teeman konfiguraatio
├── css/                    # Tyylitiedostot
│   ├── main.css           # Pääasiallinen CSS (moduulien tyylit sisältää)
│   └── responsive.css     # Responsiiviset tyylit
├── js/                     # JavaScript-tiedostot
│   └── main.js            # Pääasiallinen JavaScript
├── templates/              # HTML-templatet
│   ├── layouts/           # Layout-templatet
│   │   └── base.html      # Peruslayout
│   ├── index.html         # Etusivu
│   ├── team.html          # Tiimisivu
│   └── person-profile.html # Henkilökohtainen profiili
├── modules/                # HubSpot-moduulit
│   ├── hero-banner/       # Hero-osio
│   │   ├── module.html    # Moduulin HTML
│   │   ├── fields.json    # Kenttien määrittely
│   │   └── meta.json      # Moduulin metatiedot
│   ├── services-grid/     # Palvelut-grid
│   ├── case-study-showcase/ # Case study -esittely
│   ├── video-showcase/    # Video-esittely
│   └── person-profile/    # Henkilökohtainen profiili
└── images/                 # Kuvat ja grafiikat
    ├── icons/             # Ikonit
    ├── logos/             # Logot
    └── placeholders/      # Placeholder-kuvat
```

## 🛠️ Kehitys

### Paikallinen kehitys

1. **Kloonaa repositorio:**
   ```bash
   git clone [repository-url]
   cd Kuulu-Theme-2025
   ```

2. **Asenna riippuvuudet:**
   ```bash
   npm install
   ```

3. **Käynnistä kehityspalvelin:**
   ```bash
   npm run dev
   ```

### CSS-kehitys

- **Päätyylit:** `css/main.css` (sisältää moduulien tyylit)
- **Responsiiviset tyylit:** `css/responsive.css`
- **CSS-muuttujat:** Määritelty `:root`-selektorissa
- **BEM-nimeämiskäytäntö:** Modulaarinen CSS-rakenne

### JavaScript-kehitys

- **Päälogiikka:** `js/main.js`
- **Modulaarinen rakenne:** Jokainen toiminto omassa funktiossaan
- **ES6+ syntaksi:** Moderni JavaScript
- **Suorituskyky:** Debouncing ja throttling

### Moduulien kehitys

1. **Luo uusi moduuli:**
   ```
   modules/your-module/
   ├── module.html
   ├── fields.json
   └── meta.json
   ```

2. **Määritä kentät:** `fields.json` (vain sallitut kenttätyypit)
3. **Toteuta HTML:** `module.html` (ei inline CSS:ää)
4. **Testaa moduuli:** HubSpot Design Managerissa

### JSON-validointi

Kaikki JSON-tiedostot on validoitu:
```bash
python3 -m json.tool theme.json
python3 -m json.tool modules/*/fields.json
python3 -m json.tool modules/*/meta.json
```

## 🎨 Brändivärit

```css
:root {
  --kuulu-green: #009F4E;        /* Green Haze - pääväri */
  --kuulu-green-light: #66C595;  /* De York - vaalea vihreä */
  --kuulu-green-dark: #005F2F;   /* Fun Green - tumma vihreä */
  --kuulu-orange: #FF7900;       /* Flush Orange - korostusväri */
  --kuulu-orange-light: #FBB083; /* Hit Pink - vaalea oranssi */
  --kuulu-orange-pale: #FAE1D0;  /* Champagne - kalpea oranssi */
  --kuulu-cream: #FEF9F6;        /* Provincial Pink - kerma */
  --kuulu-white: #FFFFFF;        /* White */
  --kuulu-black: #1A1A1A;        /* Musta */
  --kuulu-gray: #666666;         /* Harmaa */
  --kuulu-gray-light: #F5F5F5;   /* Vaalea harmaa */
}
```

### Fontit
- **Otsikot:** Bebas Neue
- **Teksti:** Open Sans (300, 400, 600, 700, 800)

## 🔧 Korjaukset ja parannukset

### Viimeisimmät korjaukset:
- ✅ Poistettu kaikki inline CSS moduuleista
- ✅ Korjattu moduulien fields.json vastaamaan HubSpot:in sääntöjä
- ✅ Poistettu group-kentät ja korvattu yksinkertaisemmilla kentillä
- ✅ Validoidut kaikki JSON-tiedostot
- ✅ Lisätty moduulien tyylit pääCSS-tiedostoon
- ✅ Korjattu henkilöprofiilin vapaamuotoinen tekstin syöttö
- ✅ Optimoitu suorituskyky ja saavutettavuus

### HubSpot-yhteensopivuus:
- ✅ Ei sisältökenttiä teeman fields.json:ssa
- ✅ Vain sallitut kenttätyypit moduuleissa
- ✅ Oikein muotoillut meta.json-tiedostot
- ✅ Moduuliattribuutit oikeissa paikoissa
- ✅ Validoidut URL-oletusarvot

## 📄 Lisenssi

Tämä projekti on Kuulu:n omaisuutta. Kaikki oikeudet pidätetään.

---

**Huomio:** Tämä teema on rakennettu HubSpot:in parhaiden käytäntöjen mukaisesti ja testattu laajasti. Se tukee markkinointitiimien itsenäistä sisällön päivittämistä ilman kehittäjän apua.

---

**Kehittänyt:** Kuulu Team  
**Versio:** 1.0.0  
**Päivitetty:** 2025 