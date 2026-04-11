# Cinematic-teema: moduulien käyttö etusivulla ja koulutussivulla

Tämä dokumentti kuvaa, mitä moduuleja käytetään missäkin ja varmistaa ettei ole päällekkäisyyksiä (duplikaattimoduuleja).

## Yhteinen teema

- **Etusivu (moduulit):** template `homepage-modules.html`, label "Cinematic – Etusivu"
- **Koulutussivu:** template `koulutus-modules.html`, label "Koulutukset"
- Molemmat käyttävät **samaa teemaa** `kuulu-theme-2025-dev` ja **samoja moduuleja** kansiosta `modules/`. Kaikki polut viittaavat aina `.module`-päätteisiin (esim. `cinematic_hero.module`).

---

## Etusivu (homepage-modules.html) – käytetyt moduulit

| # | Moduuli | Kansio |
|---|---------|--------|
| 01 | Hero-osio | `cinematic_hero.module` |
| 02 | Lomakeosio | `cinematic_early_bird.module` |
| 03 | Listaus (kuvake + teksti) | `cinematic_problem_list.module` |
| 04 | Korttipari | `cinematic_two_engines.module` |
| 05 | Teksti + kuva | `cinematic_text_image.module` |
| 06 | Askeleet / prosessi | `cinematic_steps.module` |
| 07 | Mittarit + kuva | `cinematic_metrics.module` |
| 08 | Tekstiosio (leveä) | `cinematic_authority.module` |
| 09 | Kuva-CTA-kortit | `cinematic_cta_cards.module` |
| 10 | Referenssit / caset | `cinematic_referenssit.module` |
| 11 | CTA-osio | `cinematic_contact_cta.module` |

---

## Koulutussivu (koulutus-modules.html) – käytetyt moduulit

| # | Moduuli | Kansio | Sama kuin etusivulla? |
|---|---------|--------|------------------------|
| 1 | Hero | `cinematic_hero.module` | ✅ Kyllä |
| 2 | Intro: Jonna video + prosessi | `cinematic_rich_text.module` | Ei (vain koulutus) |
| 3 | Intro: Tiimikuva + vaihtoehdot | `cinematic_rich_text.module` | Ei (vain koulutus) |
| 4 | Koulutusprosessi 4 vaihetta | `cinematic_steps.module` | ✅ Kyllä |
| 5 | Tekoälykoulutukset 2 korttia | `cinematic_cta_cards.module` | ✅ Kyllä |
| 6 | Suosituimmat koulutukset 4 korttia | `cinematic_cta_cards.module` | ✅ Kyllä |
| 7 | Koulutustalo CTA | `cinematic_contact_cta.module` | ✅ Kyllä |
| 8 | Asiakaskokemukset | `cinematic_testimonial_slider.module` | Ei (vain koulutus) |
| 9 | Tarjouspyyntölomake | `cinematic_koulutus_form.module` | Ei (vain koulutus) |
| 10 | Koulutusaiheet (accordion) | `cinematic_accordion_cards.module` | Ei (vain koulutus) |
| 11 | UKK | `cinematic_accordion_cards.module` | Ei (vain koulutus) |

---

## Jaetut moduulit (sama moduuli molemmilla sivuilla)

- **cinematic_hero.module** – Hero
- **cinematic_steps.module** – Askeleet / prosessi
- **cinematic_cta_cards.module** – CTA-kortit (etusivulla yksi lohko, koulutuksella kaksi)
- **cinematic_contact_cta.module** – CTA-osio

Ei päällekkäisyyksiä: sama moduuli on yksi teeman moduulikopio, käyttö vain eri sisällöllä ja asetuksilla sivukohtaisesti.

---

## Vain koulutuksella käytetyt moduulit (kaikki jo teemassa)

- `cinematic_rich_text.module` – tekstiosiot + kuva/video (Jonna-video, tiimikuva)
- `cinematic_testimonial_slider.module` – asiakassitaattien karuselli (eri kuin referenssit-grid)
- `cinematic_koulutus_form.module` – koulutustarjouspyyntölomake
- `cinematic_accordion_cards.module` – accordion (koulutusaiheet, UKK)

Uusia moduuleja ei ole lisätty; kaikki ovat samassa teemassa.

---

## Huomio: modules-kansion duplikaattikansiot

Kansiossa `modules/` on joitain moduuleja **ilman** `.module`-päätettä (esim. `cinematic_hero`, `cinematic_steps`). HubSpot vaatii teemamoduuleille päätteen `.module`. Kaikki templatet viittaavat vain `.module`-versioihin. Vanhat kansiot ilman päätettä eivät ole käytössä ja voidaan haluttaessa siivota pois.

---

Viimeksi tarkistettu: 2026-03
