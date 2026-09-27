# Stand: kombinatorik

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, alle Dateien 0 Abweichungen,
0 Warnungen.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     22 |        0 |        10 |      11 |        0 |       1 |
| e1    |     35 |        4 |         5 |      15 |        2 |       9 |
| e2    |     40 |        4 |         5 |      18 |        4 |       9 |
| e3    |     35 |        4 |         5 |      15 |        2 |       9 |
| Summe |    132 |       12 |        25 |      59 |        8 |      28 |

## Originale je Einheit

- e1: 2023-A-3f, 2026-B-3e, 2024-bebb-lk-B4g,
  2023MgrundlegendBStochastikWTR1-1a, 2020-A-3e
- e2: 2017-be-gk-B3.1a, 2019-A-3d, 2022-C-3a, 2025-C-3d,
  2024-bebb-lk-B4h, 2022MerhoehtBStochastikWTR2-2,
  2020MerhoehtAStochastik22-a, 2026-B-3d,
  2025MgrundlegendBStochastikWTR2-1e
- e3: 2024-bebb-gk-A1.3a, 2024-bebb-gk-A1.3b,
  2026MgrundlegendBStochastikWTR2-1f, 2020MerhoehtAStochastik22-b,
  2023MerhoehtBStochastikWTR3-3, 2023MerhoehtAStochastik21-b,
  2022MerhoehtAStochastik22-b

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                           |
|-------|-----:|------:|--------------------------------------------|
| zone  |    0 |     0 | –                                          |
| e1    |    1 |     0 | Bruch nicht als Zahl an der Ergebnisstelle |
| e2    |   11 |     0 | pmatrix in aufgabe gilt als Umgebung (11)  |
| e3    |    0 |     0 | –                                          |

## Entscheidungen

- Zone: kette und sprosse_text bis zum Doppelpunkt gibt es nur
  bei „Pfadregeln“; die übrigen Fertigkeitszeilen haben keinen,
  dort gilt der Text bis zum Gedankenstrich.
- Zone: f2 übt nur Potenzen und Zehnerpotenz, keine Fakultät und
  keinen Binomialkoeffizienten (Begriffe des Themas); das
  Zone-Paar steht in f1 (unvollständiges Aufzählen).
- Keine Typen ohne Kette: jede Kette übt alle Typen ihrer
  Einheit.
- Keine Darstellung-Pflichtelemente: die Typen tragen keinen
  Darstellungswechsel; sprosse_text der Anwendung ist ein Stück
  der Lerneinheitszeile (quelle 11, 13, 15).
- Binomialkoeffizient: in loesung als pmatrix, in aufgabe als
  „(n über k)“ im Text (siehe Befunde).
- e2 Prüfungshöhe mit zwei Originalen: 4 Zeilen; der
  Sprossentext steht mit seiner Belegklammer wortgleich.
- Große Anzahlen als Zehnerpotenz: pruef zielt auf die Mantisse.
- Pool-Dubletten stehen unter der abi-Kennung
  (2024-bebb-gk-A1.3a/b, 2024-bebb-lk-B4g/h, 2017-be-gk-B3.1a).
- Eine Anwendung, die das Kastenbeispiel „drei von sechs
  Stühlen, drei Personen“ nachbildete, ist durch sieben Plätze
  und zwei Autos ersetzt.

## Befunde

- Katalog: Alle vier Erkennungsschritte („Zählt die
  Reihenfolge?“, „Mit oder ohne Wiederholung?“, „Mal oder
  plus?“, „Anzahl oder Wahrscheinlichkeit?“) wiederholen die
  Vorstufe einer Kette derselben Einheit; sie entfallen.
- Katalog: Die Sprossen nennen den Grundfall „viermal“, bank.md
  verlangt 5 Zeilen; die Bank folgt bank.md.
- Katalog: Die Zone-Fertigkeit nennt die Rechnertasten für
  Fakultät und Binomialkoeffizient; die Zone soll nach
  unterrichtsblatt 2.2 keinen Begriff des Themas nennen.
- Bausteine: \binom fehlt in _bausteine.md, und pmatrix wertet
  das Prüfskript in aufgabe als Umgebung; für (n über k) in
  Aufgaben gibt es keine zulässige Satzform.
- Mappe: Abschnitt 2 meldet die Papiere 2017-be-gk, 2024-bebb-gk
  und 2024-bebb-lk als nicht gefunden, führt ihre Kennungen aber;
  sie sind mit diesem papier verwendet.

## Offene Punkte

- Nicht verfremdet: 2023-C-3d und 2021-B-3a (fhr-Jahresform, e2
  hat mit 2019-A-3d, 2022-C-3a, 2025-C-3d drei Originale).
- Die Aufgaben mit „(n über k)“ im Text brauchen eine Satzform,
  sobald die Vorlage einen Baustein für den Binomialkoeffizienten
  hat.
