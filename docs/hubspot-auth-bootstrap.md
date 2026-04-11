# HubSpot auth bootstrap ja turvallinen käyttöönotto

## Tarkoitus

Tämä dokumentti määrittää turvallisen järjestyksen, jolla HubSpot-yhteys otetaan käyttöön tässä projektissa ilman, että:

- nykyiseen live-teemaan kosketaan vahingossa
- väärä account / portal tulee käyttöön
- upload/watch-komennot kohdistuvat väärään paikkaan
- nykyinen etusivu tai muut tuotantosivut altistuvat regressioriskille

Pääperiaate:

> Ensin auth ja diagnostiikka. Sitten fetch. Vasta sen jälkeen teema-auditointi. Upload/watch vasta kun v2-kohde on varmistettu.

---

## 1. Turvallinen käyttöönottojärjestys

Suositeltu järjestys:

1. `hs init`
2. `hs doctor`
3. `hs account list`
4. `hs account info`
5. tarvittaessa `.hsaccount` override projektihakemistoon
6. nykyisen teeman fetch paikallisesti
7. teema-auditointi
8. vasta sitten v2-teeman kloonaus / upload / watch

---

## 2. Auth-vaihe

## 2.1 Ensisijainen komento

```bash
hs init
```

Tämän ympäristön testissä juuri `hs init` osoittautui turvallisimmaksi lähtöpisteeksi, koska se:

- käynnistää interaktiivisen auth-flow’n
- auttaa luomaan tarvittavan konfiguraation
- tekee samalla selväksi, puuttuuko henkilökohtainen access key

HubSpot CLI:n nykyinen käytännön käyttäytyminen tässä ympäristössä:

- `hs account auth` käynnistää interaktiivisen personal access key -dialogin
- `hs init` käynnistää saman personal access key -setupin
- `hs auth --auth-type personalaccesskey --personal-access-key "<KEY>"` ei ole tässä ympäristössä oikea pääpolku, koska CLI ohjaa käyttämään `hs account auth` -mallia
- jos avainta ei syötetä, auth pysähtyy interaktiiviseen vaiheeseen eikä konfiguraatio valmistu

Jos henkilökohtainen access key on jo tiedossa, vaihtoehtoinen polku on:

```bash
hs auth --auth-type personalaccesskey --personal-access-key "<KEY>"
```

Jos käytetään interaktiivista flow’ta, odotettavissa on tyyppisesti:

- valinta:
  - avaa HubSpot, kopioi personal access key
  - syötä olemassa oleva personal access key

Ilman avainta auth ei valmistu, joten tämä on edelleen todellinen blocker siihen asti kunnes käyttäjä syöttää keyn tai toimittaa exportin.

### 2.1.1 Käytännössä havaittu blocker tässä ympäristössä

Testatut polut:

- `hs init` → avaa interaktiivisen personal access key -flow’n
- `hs account auth` → avaa interaktiivisen personal access key -flow’n
- `hs auth --auth-type personalaccesskey --personal-access-key "<KEY>"` → ei ole käytännössä suositeltu polku tässä CLI-konfiguraatiomallissa

Johtopäätös:

> Auth on teknisesti käynnistettävissä, mutta ilman oikeaa personal access keytä tai valmista exporttia emme voi edetä fetch-vaiheeseen.

## 2.2 Heti authin jälkeen

Aja:

```bash
hs account list
hs account info
```

Tarkista:

- oikea portal / account näkyy
- accountin nimi on tunnistettava
- kyseessä on varmasti Kuulun oikea ympäristö

---

## 3. Diagnostiikka ennen mitään fetchiä

## 3.1 Aja doctor

```bash
hs doctor --output-dir ./.hs-diagnostics
```

Tämän tarkoitus:

- varmistaa config-polut
- dokumentoida tämän koneen auth-tila
- varmistaa että CLI toimii odotetusti

## 3.2 Tarkista config-tilanne

```bash
hs config --help
```

Sekä tarvittaessa:

```bash
hs account list
hs account info
```

Jos tilejä on useita, projektissa ei pidä luottaa globaaliin oletukseen.

### 3.3 Jos workspaceen syntyy tyhjä `hubspot.config.yml`

Probe- tai init-kokeilujen jälkeen workspaceen voi ilmestyä tiedosto:

- `hubspot.config.yml`

Jos sen sisältö on vain:

```yml
portals: []
```

se ei ole käyttökelpoinen konfiguraatio vaan tyhjä bootstrap-jälki.

Tällöin:

1. poista tai korvaa tiedosto ennen seuraavaa oikeaa auth-yritystä
2. älä commitoi sitä repositorioon
3. tee varsinainen auth vasta tämän jälkeen

---

## 4. Account override tähän projektiin

Jos auth-listassa on useampi account, käytetään projektikohtaista overridea.

Komento:

```bash
hs account create-override "<account-name-or-id>"
```

Tämä luo `.hsaccount`-tiedoston current working directoryyn.

### Miksi tämä on tärkeä

Näin:

- fetch kohdistuu oikeaan accountiin
- watch ei vahingossa työnnä vääriin assetteihin
- projektin komennot ovat deterministisempiä

### Sääntö

> Jos tilejä on useampi kuin yksi, `.hsaccount` kannattaa tehdä ennen ensimmäistäkään fetch- tai watch-komentoa.

---

## 5. Fetch-vaihe: nykyisen teeman turvallinen haku

Ennen fetchiä pitää tietää:

- oikea account
- oikea theme path HubSpotissa
- haetaanko draft vai publish

### Suositus

Haetaan ensin vain nykyinen lähdeteema paikallisesti.

Esim:

```bash
bash scripts/hubspot_fetch_current_theme.sh "<REMOTE_THEME_PATH>"
```

Jos komento ajetaan manuaalisesti:

```bash
hs cms fetch "<REMOTE_THEME_PATH>" "hubspot/source-theme" --cms-publish-mode draft
```

### Turvasäännöt

- fetchataan ensin **draft**, ei publish, jos tavoite on auditointi
- ei uploadata mitään takaisin tässä vaiheessa
- ei vielä käytetä `watch`-komentoa

---

## 6. Teema-auditointi ennen kloonausta

Kun source theme on haettu:

1. ajetaan audit checklist
2. tunnistetaan:
   - etusivun riippuvuudet
   - shared/global-riskit
   - reusable / fork / replace -kohteet

Vasta tämän jälkeen päätetään:

- kloonataanko koko teema v2:ksi
- vai rakennetaanko versionoidut modulit/template-rungot source themen rinnalle

---

## 7. V2-teeman luonti

Kun auditointi on valmis:

### Vaihtoehto A

Luodaan oikea paikallinen v2-teemakansio:

- `hubspot/source-theme/`
- `hubspot/kuulu-theme-v2/`

### Vaihtoehto B

Hyödynnetään jo generoitu paikallinen blueprint:

- `hubspot/kuulu-theme-v2-blueprint/`

ja siirretään sen päätökset oikeaan v2-teemaan.

---

## 8. Upload / watch vasta lopuksi

`watch`-komento on hyödyllinen, mutta myös riskialtis väärässä vaiheessa.

### Sääntö

> `hs cms watch` otetaan käyttöön vasta kun v2-dest-path on varmistettu eikä se osoita nykyiseen live-teemaan.

Turvallinen komento kulkee helperin kautta:

```bash
bash scripts/hubspot_watch_v2.sh "<LOCAL_V2_THEME_DIR>" "<REMOTE_V2_THEME_PATH>"
```

### Älä tee tätä ennen auditointia

Älä aja:

```bash
hs cms watch . <jokin-polku>
```

jos et ole 100 % varma, mikä remote path on.

---

## 9. Suositeltu käytännön komentopolku

Kun käyttäjä / auth on valmis:

```bash
hs init
hs doctor --output-dir ./.hs-diagnostics
hs account list
hs account info
hs account create-override "<account-name-or-id>"
bash scripts/hubspot_fetch_current_theme.sh "<REMOTE_THEME_PATH>"
```

Sen jälkeen:

1. audit checklist käyttöön
2. reuse/fork/replace/protect -päätökset
3. v2-teeman valmistelu
4. vasta lopuksi upload/watch

---

## 10. Mitä ei tehdä ennen oikeaa auditointia

Ei tehdä:

- `hs cms upload` nykyiseen live-teemaan
- `hs cms watch` ilman varmistettua v2-polkuja
- `hs cms delete`
- shared module -muutoksia suoraan remoteen

---

## 11. Yhteenveto

Turvallinen HubSpot bootstrap tässä projektissa on:

1. init/auth
2. diagnostiikka
3. account override
4. source theme fetch
5. teema-auditointi
6. v2-rakenteen muodostus
7. watch/upload vasta viimeisenä

Tärkein sääntö:

> Yhtään remote write -komentoa ei ajeta ennen kuin oikea account, oikea source theme ja oikea v2-dest-path on varmistettu.
