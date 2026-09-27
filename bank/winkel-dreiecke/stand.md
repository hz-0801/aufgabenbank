# Stand: winkel-dreiecke

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        – |        10 |      11 |        – |       1 |    22 |
| e1    |        8 |         5 |      24 |        4 |       9 |    50 |
| e2    |        8 |         5 |      27 |        4 |       9 |    53 |
| e3    |        8 |         5 |      30 |        4 |       9 |    56 |
| e4    |        4 |         5 |      27 |        5 |       9 |    50 |
| e5    |        4 |         5 |      21 |        3 |       9 |    42 |
| Summe |       32 |        35 |     140 |       20 |      46 |   273 |

## Originale je Einheit

- E1: 2018-OS-K4a, 2016-OS-K7a
- E2: 2014-OS-B1f, 2020-OS-B1g, 2019-OS-B1a, 2021-OS-B1i,
  2023-OS-K2a, 2015-OS-B1d, 2026-FOR-B1i
- E3: 2017-OS-K4a, 2022-OS-K5c, 2018-OS-K4b, 2015-OS-K5b,
  2023-OS-K7a, 2026-FOR-B1c, 2016-OS-B1e, 2023-OS-B1g,
  2025-OS-K2c
- E4: 2020-OS-B1i
- E5: keins (Prüfungshöhe original null)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund          |
|-------|-------------:|----------:|---------------------------|
| zone  |            6 |         0 | merkmal uneinheitlich (5) |
| e1    |            0 |         0 | –                         |
| e2    |            0 |         0 | –                         |
| e3    |            7 |         0 | pruef fehlt (6)           |
| e4    |            3 |         0 | pruef fehlt (3)           |
| e5    |            0 |         0 | –                         |

## Entscheidungen

- Originale mitten in der Kette stehen an je einer Variante ihrer
  Sprosse; zwei Zeilen je Original nur an der Prüfungshöhe.
- 2016-OS-B1e (Zielmarke E2) steht in E3 an „Vierecks-Eigenschaft
  ankreuzen“, weil die Kette von E2 keine Ankreuzsprosse hat.
- E4: eine Prüfungssprosse mit 2 Zeilen 2020-OS-B1i und 3 Zeilen
  WSW-Konstruktion mit Beschreibung (original null).
- E5: Prüfungshöhe original null, 3 Zeilen; 2025-OS-K2c bleibt
  in E3, wo die Zuordnung den Typ führt.
- Anwendung (3 Zeilen) in jeder Einheit; Darstellungswechsel
  entfällt, kein Typ des Eintrags trägt ihn.
- Zone f2 und f3: Fertigkeitszeile ohne Doppelpunkt, kette reicht
  bis vor „ – Einheit …“.
- 90°, 180°, 360° gelten als Regelgrößen, nicht als Kastenzahlen;
  180 steht in 6 Aufgaben (Zone f2 v4–v6, Fehler finden E2, E3).
- Konstruktionen: pruef "" außer an der WSW-Prüfungshöhe;
  Kontrollwerte in loesung, Lösungsfigur als \dreieck mit
  berechneten Ecken in loesungsgrafik.
- E5 konstruiert auf dem Koordinatengitter (ksys mit \punkt),
  damit Mittelpunkte und Fußpunkte als (x|y) prüfbar sind.
- Lage an Parallelen steht im Text (oberhalb, links von k);
  \parallelenpaar ohne Labels, da deren Lage ungeprüft ist.

## Befunde

- Katalog: Die Erkennungsschritte „Welche Winkelart?“, „Wie liegen
  die Winkel zueinander?“, „Welches Dreieck?“, „Welche Stücke sind
  gegeben?“ und „Welche Linie?“ verlangen denselben Handgriff wie
  die Vorstufe ihrer Kette; sie entfallen, die Vorstufen bleiben.
- Katalog: Die Zielmarke führt 2016-OS-B1e unter Einheit 2, die
  Zuordnung den Typ „Eigenschaft einer Figur zuordnen“ unter 3.
- Prüfskript: pruef "" gilt nur bei hoehe pflicht/begruenden;
  Begründungen in der Kette und an der Prüfungshöhe sowie
  Konstruktionsbeschreibungen mit Schrittnummern verlangen pruef.

## Offene Punkte

- Ohne LaTeX-Lauf ungeprüft: Labelfolge von \geradenkreuzung
  (α bis δ reihum angenommen) und überstumpfe Winkel mit \winkel.
- Für Höhe und Seitenhalbierende im Dreieck fehlt ein Baustein;
  „Welches Teildreieck?“ und die Vorstufe von E5 sind reiner Text.
- Ankreuzen Winkelart: Die Option „überstumpf“ enthält „stumpf“;
  das Skript wertet die Lösung trotzdem als eindeutig.
