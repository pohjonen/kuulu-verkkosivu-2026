# Kuulu v2: post-auth handoff ja execution-startti

## Tarkoitus

Tämä dokumentti kertoo täsmälleen, mitä tehdään sillä hetkellä kun HubSpot-auth tai nykyisen teeman export on saatu.

Tavoite:

- siirtyä valmisteludokumentaatiosta oikeaan HubSpot-toteutukseen ilman epäröintiä
- minimoida väärään accountiin, väärään teemaan tai väärään remote-polkuun liittyvät riskit
- tehdä ensimmäiset oikeat fetch-/audit-/clone-vaiheet hallitusti

---

## 1. Handoffin lähtötilanne

Tämän dokumentin käyttöhetkellä oletetaan:

- HubSpot CLI on asennettu
- repo sisältää blueprintin, manifestit, helperit ja dokumentaation
- nykyiseen live-teemaan ei ole vielä koskettu
- auth tai teeman export puuttui tähän asti, mutta on nyt saatavilla

---

## 2. Ensimmäinen 15 minuutin protokolla authin jälkeen

### 2.1 Varmista account

Aja:

```bash
hs account list
hs account info
```

Kirjaa ylös:

- account / portal
- portalId
- oletusaccount

### 2.2 Aja bootstrap-status

```bash
bash scripts/hubspot_bootstrap_status.sh
```

Tarkoitus:

- varmistaa että auth näkyy oikein
- tarkistaa syntyykö doctor-data
- varmistaa ettei ympäristö ole epäselvä

### 2.3 Lukitse oikea account työtilaan

Jos käytössä on useita accountteja:

```bash
hs account create-override <account>
```

Näin estetään vahinkofetch tai vahinkowatch väärään portaaliin.

---

## 3. Ensimmäinen oikea fetch

### 3.1 Hae source theme sellaisenaan

```bash
bash scripts/hubspot_fetch_current_theme.sh <remote-theme-path>
```

Tavoite:

- saada nykyinen teema paikalliseen `hubspot/source-theme/`-hakemistoon
- EI tehdä vielä yhtään muutosta teemaan

### 3.2 Dokumentoi fetched source

Kirjaa heti fetchin jälkeen:

- mikä remote path haettiin
- mihin local pathiin se tuli
- oliko kyseessä theme root vai pelkkä osakansio
- onko rakenne odotetun kaltainen

### 3.3 Aja source match + audit yhdellä runnerilla

Suositus:

```bash
bash scripts/run_post_auth_audit.sh hubspot/source-theme
```

Tämä kokoaa yhteen:

- bootstrap-statuksen
- julkisen asset-signaturen matchin
- fetched sourcen rakenteellisen auditoinnin

Lopputuloksena saat yhteen paikkaan:

- `docs/generated/post-auth-audit/public-signature-match.txt`
- `docs/generated/post-auth-audit/source-theme-audit.json`
- `docs/generated/post-auth-audit/source-theme-audit.md`

---

## 4. Ensimmäinen oikea audit

Käytä lähteinä:

- `docs/hubspot-theme-audit-checklist.md`
- `docs/hubspot-theme-v2-build-map.md`

Auditissa pitää ensimmäisenä selvittää:

1. mikä template renderöi nykyisen etusivun
2. mitä moduuleja etusivu käyttää
3. mitä globaaleja osia etusivu käyttää
4. mitä yhteisiä assetteja live käyttää
5. mitä voidaan reuse / fork / replace / protect

### 4.1 Tärkein sääntö

> Ensimmäinen oikea fetch ei ole toteutusvaihe. Se on auditointivaihe.

Älä vielä rakenna mitään `source-theme/`-kansioon.

---

## 5. V2-kloonin luonti

Kun auditointi on riittävästi tehty:

```bash
bash scripts/hubspot_clone_v2_theme.sh source-theme kuulu-theme-v2
```

Tavoite:

- tehdä paikallinen v2-haara oikeasta source-themestä
- siirtää kaikki toteutus tämän kansion sisään

### 5.1 Vertaa blueprintiin

Vertaile:

- `hubspot/source-theme/`
- `hubspot/kuulu-theme-v2/`
- `hubspot/kuulu-theme-v2-blueprint/`

Blueprint kertoo mitä haluamme rakentaa.
Source theme kertoo mitä oikeasti on olemassa.
V2-klooni on paikka jossa toteutus tapahtuu.

---

## 6. Ensimmäiset oikeat toteutuspäätökset

Kun `kuulu-theme-v2/` on luotu, päätä nämä:

### 6.1 Reuse

Mitkä moduulit voidaan pitää lähes sellaisinaan:

- CTA-osa
- korttigridi
- FAQ
- jokin nykyinen cinematic-osa

### 6.2 Fork

Mitkä moduulit pitää versionoida:

- etusivun käyttämät shared-moduulit joita pitää muuttaa
- globaalit osat joita ei saa rikkoa
- kaikki moduulit joiden kenttälogiikka ei riitä

### 6.3 Replace

Mitkä tehdään kokonaan uudestaan:

- legacy light -palikat
- kovakoodatut layoutit
- heikot editor guardrails -moduulit

---

## 7. Ensimmäinen oikea build-aalto

Kun auditointi ja v2-klooni ovat olemassa, aloita tästä järjestyksestä:

1. Hero Cinematic v2
2. Final CTA v2
3. Problem Grid v2
4. Service Pillars v2
5. Audience Split / 95-5 v2
6. Process Steps v2
7. Stats / Trust Band v2
8. Reference Grid v2

Perustelu:

- nämä moduulit avaavat suurimman osan ensimmäisen aallon sivuista
- ne määrittävät visuaalisen kielen
- ne voi rakentaa ilman että etusivua tarvitsee vielä vaihtaa

---

## 8. Ensimmäiset oikeat preview-sivut

Kun foundation-moduulit ovat olemassa, rakenna ensin:

1. `/v2-videotuotanto`
2. `/v2-koulutus`
3. `/v2-digimarkkinointi`
4. `/v2-case-studies`
5. `/v2-yhteystiedot`
6. `/v2-etusivu` viimeisimpänä ensimmäisessä aallossa

Näin etusivun riski pysyy pienempänä.

---

## 9. Watch-protokolla

Vasta kun:

- oikea account on lukittu
- oikea source theme on auditoitu
- oikea v2-klooni on olemassa

käynnistä watch:

```bash
bash scripts/hubspot_watch_v2.sh <local-src> <remote-dest>
```

### Watchin sääntö

Watch osoitetaan vain:

- v2:n remote-polkuun
- ei koskaan live source themen polkuun ilman eksplisiittistä syytä

---

## 10. Ensimmäinen handoff-checklist authin jälkeen

- [ ] `hs account list` toimii
- [ ] oikea portal varmistettu
- [ ] `.hsaccount` override tarvittaessa luotu
- [ ] bootstrap-status ajettu
- [ ] source theme fetchattu
- [ ] source theme auditoitu
- [ ] v2-klooni luotu
- [ ] blueprint vs source vs v2 vertailtu
- [ ] reuse/fork/replace päätetty foundation-moduuleille
- [ ] ensimmäinen build-aalto aloitettu oikeassa v2-kansiossa

---

## 11. Yhteenveto

Authin jälkeen ei hypätä suoraan koodimuokkauksiin.

Oikea järjestys on:

1. auth
2. account-lock
3. fetch
4. audit
5. clone
6. compare with blueprint
7. build foundation modules
8. build preview pages

Tärkein sääntö:

> Ensimmäinen oikea muutos tehdään vasta v2-klooniin, ei koskaan suoraan fetched sourceen tai live-rakenteeseen.
