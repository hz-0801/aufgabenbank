# Stand: grenzwerte-und-verhalten-im-unendlichen

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
(2026-09-26T16:47:30+02:00)
Datum: 2026-09-27 14:53 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen,
0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|---|---|---|---|---|---|---|
| zone | 31 | – | 14 | 16 | – | 1 |
| e1 | 36 | 8 | 5 | 12 | 2 | 9 |
| e2 | 42 | 4 | 5 | 15 | 6 | 12 |
| e3 | 27 | 4 | 5 | 6 | 3 | 9 |

e1: 4 der 8 Vorstufenzeilen sind der Erkennungsschritt „Wer
gewinnt?“ (k1).

## Originale je Einheit

- e1: 2023-A-1a (auch Prüfungshöhe), 2021-A-1a, 2022-bebb-gk-B2.2a,
  2022-B-1a, 2022-bebb-lk-B2.1a, 2020-C-1a, 2026-bb-gk-B2.1a,
  2021-B-1a
- e2: 2025-bebb-gk-B2.2a, 2025MgrundlegendBAnalysisWTR2-1a,
  2022-bebb-gk-B2.1b, 2018-be-gk-B1.2a,
  2022MgrundlegendBAnalysisWTR2-1b, 2023-bebb-gk-B2.1a,
  2021-be-gk-B2.2b, 2020MgrundlegendBAnalysisWTR2-1b,
  2019-be-gk-B2.2a; Prüfungshöhe 2023-bebb-lk-B2.1b,
  2024MerhoehtBAnalysisWTR3-2a, 2017-bb-ea-B2.2a
- e3: 2026MerhoehtBAnalysisWTR3-1a, 2024MerhoehtBAnalysisWTR1-1a;
  Prüfungshöhe ohne Original (3 Zeilen)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund |
|---|---|---|---|
| zone | 1 | 0 | pruef nicht an der Ergebnisstelle (1) |
| e1 | 0 | 0 | – |
| e2 | 0 | 0 | – |
| e3 | 0 | 0 | – |

Keine Einheit scheiterte zweimal.

## Entscheidungen

- Zone: Fertigkeitszeilen ohne Doppelpunkt (Z. 31–34) tragen als
  kette den Text bis zum ersten Gedankenstrich.
- Zone-Paar in Fertigkeit 7 (Vorzeichen eines Produkts): das
  häufigste Muster der Mappe ist das übersehene Vorzeichen des
  Polynomfaktors.
- Erkennungsschritt „Wer gewinnt?“ als eigene Kette k1 in e1
  (erste Einheit seines Bereichs, Z. 36), gemischt aus Leitterm,
  e-Faktor und konstantem Summanden.
- sprosse_text ist der Sprossentext ohne Klammerzusatz; bei e2
  Sprosse 7 steht er wortgleich mit der inneren Klammer, bei e3
  Sprosse 1 mit „x → +∞“.
- Pflichtkette wie bei gleichungen-loesen (1 fehler, 2 begruenden,
  3 anwendung, 4 darstellung); e1 ohne Anwendung (kein
  Sachzusammenhang), e3 ohne Darstellung.
- e2 Prüfungshöhe: 2 Zeilen je Original, zusammen 6 Zeilen in
  einer Sprosse, weil der Katalog dort drei Originale nennt.
- Nicht verwendet: 2024-C-1a (Merkmal durch 2020-C-1a und
  2022-B-1a belegt), 2018-be-gk-cas-B1.2a (Funktion wie
  2018-be-gk-B1.2a), 2017MerhoehtBAnalysisWTR2-1a (Parameter im
  Leitkoeffizienten ist kein Merkmal der Kette von e1).
- Grenzverhalten ohne Ziffer in der Lösung trägt pruef "";
  mit Grenzwert trägt pruef die erste Zahl der Lösung.

## Befunde

- Katalog: Die Erkennungsschritte „Gerade oder ungerade, plus oder
  minus?“ (Z. 37) und „Welche Seite, welches Vorzeichen?“ (Z. 38)
  verlangen den Handgriff der Vorstufen von e1 und e2 (Z. 88, 89);
  sie entfallen, der Katalog führt beide.
- Katalog: „Wer gewinnt?“ (Z. 36) steht zusätzlich in den
  Vorstufen von e2 und e3 (Z. 89, 90) – dreifach geführt.
- Katalog Z. 24 nennt Nachzüge vom 28. und 29.09.2026, der
  Katalog-Commit ist vom 26.09.2026.
- Katalog Z. 90: die Sprosse „x → +∞“ enthält den Pfeil, der auch
  die Sprossen trennt; die Zeile ist maschinell nicht eindeutig
  teilbar.
- bank.md: Die Regel „Fertigkeit bis zum Doppelpunkt“ greift bei
  Z. 31–34 nicht; Z. 34 hat erst im Ermessen-Vermerk einen.
- Prüfskript: „→“ ist keine Ergebnisstelle; ein Grenzwert wird
  nur geprüft, wenn er die erste Zahl der Lösung ist.

## Offene Punkte

- Grafiken mit \funktion und exp (Darstellung in e1 und e2) sind
  nicht kompiliert; Achsenbereiche nur rechnerisch geprüft.
- Die Schreibweise lim (Z. 46) nutzt die Bank nicht; sie schreibt
  durchgehend den Pfeil, weil \lim als Baustein nicht geprüft ist.
