# Hero Cinematic v2

Ensimmäinen oikea v2-forkki `cinematic_hero.module`-moduulista.

## Tavoite

- säilyttää nykyisen cinematic-etusivun vahva hero-logiikka
- siivota rakenne v2-guardrailien mukaiseksi
- erottaa CTA/media/layout/style-kentät selkeästi editorissa
- pitää toteutus täysin erillään source-theme- ja live-rakenteesta

## Lähtömoduuli

- `hubspot/source-theme/modules/cinematic_hero.module`

## V2-parannukset

- CTA:t siirretty `link`-kenttiin
- media-tilat selkeytetty (`background_video_url`, `background_video_file`, `background_image`, `none`)
- show_stats-logiikka muutettu repeater-pohjaiseen trust/stat-riviin
- lisätty tyylivaihtoehdot surface-, grain- ja aurora-logiikalle
- lisätty `anchor_id`, `tracking_label`, `hide_on_mobile`

## Huomio

Tämä on paikallinen v2-moduuli `hubspot/kuulu-theme-v2/`-kloonissa.
Sitä ei ole uploadattu takaisin HubSpotiin eikä kytketty liveen.
