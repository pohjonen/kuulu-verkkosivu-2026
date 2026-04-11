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

## Mitä ei ole vielä tehty

Tässä vaiheessa ei ole vielä:

- uploadattu mitään HubSpotiin
- watchattu mitään remote-polkuun
- kytketty näitä moduuleita v2-templateihin remote-puolella
- tehty lopullista fields.json-hienosäätöä todellisen editorikokemuksen perusteella

## Seuraavat foundation-moduulit

Luontevat seuraavat moduulit:

1. `service-pillars-v2`
2. `stats-trust-band-v2`
3. `lead-capture-form-cta-v2`

Näin saadaan kasaan ensimmäinen oikeasti käyttökelpoinen foundation-aalto:

- hero
- problem
- pillars
- stats
- form CTA

## Turvallisuussääntö

Kaikki tämän vaiheen työ tehdään vain:

- `hubspot/kuulu-theme-v2/`

Seuraaviin ei kosketa:

- `hubspot/source-theme/`
- nykyiset protected global/header/footer-rakenteet remote-puolella

## Yhteenveto

Nyt projekti on siirtynyt dokumentaatiovaiheesta ensimmäisiin oikeisiin v2-moduuliforkkeihin.

Ensimmäiset kaksi foundation-moduulia ovat olemassa paikallisessa v2-kloonissa, ja seuraava vaihe on laajentaa tätä foundation-kerrosta edelleen ennen sivukohtaista kokoamista.
