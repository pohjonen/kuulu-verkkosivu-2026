# Kuulu v2: foundation-forkkien eteneminen

## Tämän vaiheen tavoite

Ensimmäinen konkreettinen HubSpot-v2-toteutus tehdään vain paikalliseen:

- `hubspot/kuulu-theme-v2/`

Nykyinen:

- `hubspot/source-theme/`

toimii edelleen pelkkänä vertailupisteenä.

## Valmistuneet ensimmäiset oikeat v2-forkit

### 1. `hero-cinematic-v2`

Polku:

- `hubspot/kuulu-theme-v2/modules/hero-cinematic-v2.module/`

Tässä vaiheessa moduuli on viety blueprint-skeletonista eteenpäin niin, että:

- se käyttää selkeää v2-nimeämistä
- media-/CTA-/stats-logiikka on jäsennelty source-moduulista johdetuksi mutta siivotuksi
- se nojaa teematasoisiin tokeneihin
- siihen on lisätty README käyttötarkoituksen ja lähtömoduulin kuvaamiseen

Lähtömoduuli:

- `hubspot/source-theme/modules/cinematic_hero.module`

### 2. `problem-grid-v2`

Polku:

- `hubspot/kuulu-theme-v2/modules/problem-grid-v2.module/`

Tässä vaiheessa moduuli on viety blueprint-skeletonista eteenpäin niin, että:

- “problem list” -rakenne on muunnettu v2-problem-gridiksi
- media voidaan näyttää tai piilottaa kontrolloidusti
- kortit ovat rakenteisia ja guardrail-pohjaisia
- moduuli nojaa yhteisiin token-luokkiin eikä sivukohtaiseen kovakoodiin

Lähtömoduuli:

- `hubspot/source-theme/modules/cinematic_problem_list.module`

### 3. `service-pillars-v2`

Polku:

- `hubspot/kuulu-theme-v2/modules/service-pillars-v2.module/`

Tässä vaiheessa moduuli on rakennettu source-teeman kaksimoottori- ja palvelukorttirakenteiden pohjalta niin, että:

- pilarit ovat rakenteisia repeater-kortteja
- icon / subtitle / benefits / CTA on erotettu selkeästi editorikenttiin
- media on valinnainen ja kontrolloitu
- rakenne nojaa v2-token- ja utility-ajatteluun

Lähtömoduulit:

- `hubspot/source-theme/modules/cinematic_two_engines.module`
- `hubspot/source-theme/modules/services-grid.module`

### 4. `stats-trust-band-v2`

Polku:

- `hubspot/kuulu-theme-v2/modules/stats-trust-band-v2.module/`

Tässä vaiheessa moduuli on rakennettu source-teeman metrics-rakenteen pohjalta niin, että:

- statit on siirretty repeater-pohjaiseen malliin
- media on erotettu omaksi kenttäryhmäkseen
- CTA on hallittu ja valinnainen
- rakenne toimii luottamus- ja mittariosioihin useilla sivutyypeillä

Lähtömoduuli:

- `hubspot/source-theme/modules/cinematic_metrics.module`

### 5. `lead-capture-form-cta-v2`

Polku:

- `hubspot/kuulu-theme-v2/modules/lead-capture-form-cta-v2.module/`

Tässä vaiheessa moduuli on rakennettu source-teeman koulutuslomakemoduulin pohjalta niin, että:

- kuvaus, statit ja edustajablokki ovat rakenteisia kenttiä
- form-mode voidaan vaihtaa upotetun lomakkeen ja CTA-fallbackin välillä
- form-id, region, portal-id ja success-message ovat editorin hallinnassa
- moduuli nojaa v2-token-rakenteeseen eikä live-sourceen

Lähtömoduuli:

- `hubspot/source-theme/modules/cinematic_koulutus_form.module`

## Ensimmäinen oikea v2-sivukokonaisuus

### `homepage-v2`

Polut:

- `hubspot/kuulu-theme-v2/templates/homepage-v2.html`
- `hubspot/kuulu-theme-v2/templates/layouts/base-cinematic-v2.html`
- `hubspot/kuulu-theme-v2/templates/partials/header-cinematic-v2.html`
- `hubspot/kuulu-theme-v2/templates/partials/footer-cinematic-v2.html`

Tässä vaiheessa:

- ensimmäinen oikea v2-template on kytketty foundation-moduuleihin
- nykyisen cinematic-etusivun rakenteesta on tehty turvallinen v2-versio paikalliseen klooniin
- header ja footer on kopioitu v2-partialeiksi, jotta niitä voidaan myöhemmin siistiä rikkomatta source-themeä

Kytketyt foundation-moduulit:

- `hero-cinematic-v2`
- `problem-grid-v2`
- `service-pillars-v2`
- `stats-trust-band-v2`
- `lead-capture-form-cta-v2`

## Mitä ei ole vielä tehty

Tässä vaiheessa ei ole vielä:

- uploadattu mitään HubSpotiin
- watchattu mitään remote-polkuun
- kytketty näitä moduuleita remote-puolen v2-sivuihin
- tehty lopullista fields.json-hienosäätöä todellisen editorikokemuksen perusteella
- siivottu v2-headeriä ja v2-footeria täysin pois source-lähtöisestä sisällöstä

## Foundation-aallon tämänhetkinen tila

Tähän mennessä foundation-aallosta on olemassa:

- hero
- problem
- pillars
- stats
- form CTA

Tämä muodostaa ensimmäisen oikeasti käyttökelpoisen v2-peruskerroksen.

## Seuraavat luontevat moduulit

Luontevat seuraavat moduulit tämän jälkeen:

1. `reference-grid-v2`
2. `training-agenda-v2`
3. `team-grid-v2`

## Turvallisuussääntö

Kaikki tämän vaiheen työ tehdään vain:

- `hubspot/kuulu-theme-v2/`

Seuraaviin ei kosketa:

- `hubspot/source-theme/`
- nykyiset protected global/header/footer-rakenteet remote-puolella

## Yhteenveto

Nyt projekti on siirtynyt dokumentaatiovaiheesta ensimmäisiin oikeisiin v2-moduuliforkkeihin.

Ensimmäinen foundation-kerros on nyt olemassa ja ensimmäinen oikea v2-sivukokonaisuus (`homepage-v2`) on koottu paikalliseen klooniin. Seuraava vaihe on syventää moduuliforkkeja ja rakentaa seuraavat v2-sivut samalla mallilla.
