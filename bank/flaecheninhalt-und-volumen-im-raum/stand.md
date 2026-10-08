# Stand: flaecheninhalt-und-volumen-im-raum

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27 14:47 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     29 |        – |        12 |      16 |        – |       1 |
| e1    |     46 |        8 |         5 |      15 |        6 |      12 |
| e2    |     43 |        4 |         5 |      15 |        7 |      12 |
| e3    |     35 |        4 |         5 |      12 |        5 |       9 |
| e4    |     44 |        4 |         5 |      15 |        8 |      12 |

## Originale je Einheit

- e1: 2017-bb-ea-A1.2a, 2017MerhoehtAAGLAA212-a, 2022-bebb-gk-A1.5b,
  2023-bebb-lk-B3c, 2023MerhoehtBAGLAA1WTR-2c, 2024-bebb-gk-A1.5a,
  2025MerhoehtBAGLAA1MMS-1b, 2025MgrundlegendAAGLAA212-b
- e2: 2017MerhoehtBAGLAA2WTR2-1e, 2017MgrundlegendAAGLAA212-a,
  2017MgrundlegendBAGLAA2WTR2-1g, 2019-be-gk-B3.2d, 2021-be-gk-B3f,
  2022-bebb-gk-B3a, 2022-bebb-gk-B3f, 2024MgrundlegendAAGLAA221
- e3: 2017MgrundlegendAAGLAA212-b, 2018-bb-ea-B3.1d,
  2019MgrundlegendAAGLAA212-b, 2020MgrundlegendAAGLAA212-a,
  2023-bebb-lk-B3d, 2024-bebb-lk-B3a, 2025-bebb-gk-B3a,
  2026-bb-ea-B3a, 2026MgrundlegendAAGLAA111-b,
  2026MgrundlegendAAGLAA222-a
- e4: 2018MerhoehtBAGLAA2CAS2-1d, 2018MgrundlegendBAGLAA2WTR1-1d,
  2018MgrundlegendBAnalysisWTR-1c, 2021-be-gk-B3i, 2022-bebb-gk-B3h,
  2022-bebb-lk-B3k, 2022MerhoehtBAGLAA2WTR2-1e,
  2022MgrundlegendBAnalysisWTR1-2b, 2023MgrundlegendAAGLAA22-b,
  2023MgrundlegendBAGLAA2WTR2-1f, 2024-bebb-lk-B3h,
  2025-bebb-lk-A1.3a, 2026MgrundlegendBAGLAA2MMS2-1e

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                  |
|-------|-------------:|----------:|-----------------------------------|
| zone  |            0 |         0 | –                                 |
| e1    |       6 (+2) |         0 | Sperre: Tripel aus den Originalen |
| e2    |            2 |         0 | Baustein \cos statt \mathrm{cos}  |
| e3    |            0 |         0 | –                                 |
| e4    |            0 |         0 | –                                 |

e1 brauchte zwei Korrekturrunden (6, dann 2 Sperrtreffer). Ab e2 lief
die Sperrprobe des Skripts schon vor dem ersten Schreiben mit (e2 1,
e3 1, e4 3 Treffer, vor dem Schreiben behoben); die Tabelle zählt
nur Läufe über die geschriebene Datei.

## Entscheidungen

- Die Fertigkeiten der Zone haben keinen Doppelpunkt; kette und
  sprosse_text sind der Text bis zum Gedankenstrich.
- Zone-Paar zum Kernfehlmuster „schräge Länge als Höhe“ in der
  Fertigkeit Flächenformeln; Fertigkeiten 1, 5 und 6 tragen je zwei
  Fallstricke.
- Die mehrteilige Prüfungshöhe ist eine Sprosse; sprosse_text ist ihr
  erster Teil, die weiteren Teile stehen als Varianten mit original.
- Kennungen der Prüfungshöhe ohne Eintrag in Abschnitt 2 der Mappe
  (2021MgrundlegendBAGLAA2WTR2-1b in e2, 2025MerhoehtBAGLAA2MMS-1a in
  e3) stehen als Prüfungshöhe mit original null, 3 Zeilen.
- An Kettensprossen trägt je genannte Kennung aus der Mappe höchstens
  eine verfremdete Zeile das Feld original.
- Typ ohne Kette in e2 ist nur der Schattentyp; das Viereck mit zwei
  parallelen senkrechten Seiten gilt als Trapez der Sprosse 3.
- e3 hat kein Pflichtelement darstellung, weil der Katalog für die
  Einheit „kein Deutungstyp“ führt.
- Pflichtelemente sind die Sprossen 1–4 der Pflichtkette; darstellung
  und anwendung tragen einen Typnamen der Einheit als sprosse_text.
- Achsen heißen x, y, z wie in den Landesheften; Punkte heißen P, Q,
  R, S, T, U, A steht nur für den Flächeninhalt.

## Befunde

- Katalog: „Höhe oder Kante?“, „Ein Drittel oder nicht?“ und „Ganz,
  Summe oder Differenz?“ sind als Erkennungsschritt und als Vorstufe
  von e1, e3, e4 geführt; die Erkennungsschritte entfallen.
- Katalog: „Welche Figur, welche Formel?“ steht als Erkennungsschritt
  (hier in e1) und zugleich als Vorstufe der Kette von e2.
- Mappe: Die Sprossenzeilen nennen 2021MgrundlegendBAGLAA2WTR2-1b und
  2025MerhoehtBAGLAA2MMS-1a als Prüfungshöhe, Abschnitt 2 führt sie
  nicht; original bleibt dort null.
- Prüfskript: Achsenpunkte wie (0 | 4 | 0) sind faktisch Einzelzahlen,
  die Sperre behandelt sie als Tripel; das macht ganzzahlige Körper im
  Raum sehr eng.

## Offene Punkte

- loesungsgrafik ist überall leer; Zeichenaufgaben beschreiben die
  Lösung über Punkte oder Eintragungen in Worten.
- 2026-10-08 Aufräumlauf: Sperre Punkte (3|0|0), (0|9|0) (Original 2020-be-gk-B3.1e) in e4-k1-s7-v2 → P(4|0|0), Q(0|6|0); Ergebnis t hängt nur von der Höhe 10 ab, unverändert; Prüfskript: Abweichungen 1 → 0.
