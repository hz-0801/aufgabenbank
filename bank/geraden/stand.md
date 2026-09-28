# Stand: geraden

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, alle Dateien 0 Abweichungen,
0 Warnungen.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     30 |        – |        14 |      15 |        – |       1 |
| e1    |     39 |        8 |         5 |      12 |        2 |      12 |
| e2    |     44 |        4 |         5 |      24 |        2 |       9 |
| e3    |     29 |        4 |         5 |      12 |        2 |       6 |
| e4    |     31 |        4 |         5 |       9 |        4 |       9 |

## Originale je Einheit

- e1: 2023MgrundlegendAAGLAA213-a, 2021MerhoehtAAGLAA112-a,
  2019-be-gk-A1.3a, 2022MgrundlegendAAGLAA213-b,
  2021-be-gk-A1.5b (Prüfungshöhe)
- e2: 2023-bebb-gk-A1.4a, 2019MgrundlegendAAGLAA211-a,
  2019MgrundlegendAAGLAA22-a, 2018-be-gk-B2.2d, 2020-be-gk-A1.3a,
  2023MgrundlegendAAGLAA213-b, 2026MgrundlegendBAGLAA2MMS2-1d,
  2017MerhoehtBAGLAA2WTR1-1f, 2017MerhoehtBAGLAA2WTR3-1g,
  2017MgrundlegendBAGLAA2CAS1-1f, 2025-bebb-lk-A1.7a (Prüfungshöhe)
- e3: 2022MgrundlegendAAGLAA213-a, 2021-be-gk-B3b, 2018-be-gk-B2.1c,
  2019-be-gk-A1.3b (Prüfungshöhe)
- e4: 2022MgrundlegendBAGLAA2WTR1-1f, 2022MgrundlegendBAGLAA2WTR1-1e,
  2017MgrundlegendBAnalysisWTR-1g, 2018-be-gk-B2.2e und
  2025MgrundlegendBAGLAA2WTR1-1e (Prüfungshöhe)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund             |
|-------|-------------:|----------:|------------------------------|
| zone  |            6 |         0 | merkmal uneinheitlich (s1)   |
| e1    |            2 |         0 | Sperre: Tripel aus der Mappe |
| e2    |            6 |         0 | Sperre: Tripel aus der Mappe |
| e3    |            3 |         0 | Sperre: Tripel aus der Mappe |
| e4    |            1 |         0 | Sperre: Tripel aus der Mappe |

Keine Einheit scheiterte zweimal.

## Entscheidungen

1. Grundfälle tragen original null, auch wo die Sprosse eine Kennung
   nennt; Zwischensprossen mit einer Kennung aus Abschnitt 2 tragen
   sie in allen Varianten, mit Prüfkennung im Aufgabentext.
2. e2 Prüfungshöhe: die wortgleiche Dublette 2025-bebb-lk-A1.7a /
   2025MerhoehtAAGLAA221-a zählt als ein Original (2 Zeilen).
3. e4 Prüfungshöhe mit zwei Originalen: eine Sprosse, 4 Zeilen, je
   Original 2; sprosse_text ist die ganze Katalogspanne samt Klammer.
4. e3 s3 (Katalog nennt 2019-be-gk-B3.1c) trägt original null, weil
   die Kennung nicht in Abschnitt 2 der Mappe steht.
5. Zone: kette und sprosse_text sind die Fertigkeit bis zum
   Gedankenstrich (die Sek-II-Zeilen haben keinen Doppelpunkt);
   Reihenfolge nach erster Verwendung (e1 vor e2 vor e3 vor e4).
6. Zone-Paar bei „Lineare Gleichungen lösen …“: nur zwei von drei
   Gleichungen geprüft – das Zone-Gegenstück zur unvollständigen
   Punktprobe, dem häufigsten Muster der Typischen Fehler.
7. Pflichtelemente: fehler und begruenden in allen Einheiten,
   anwendung in e1, e2, e4 (Sachtypen), darstellung nur in e1
   (Schrägbild; quelle Zeile 101, Grundvorstellung).
8. Typen ohne Kette: e2 „Punkt … über eine quadratische Gleichung“
   (drei Originale, je Zeile eines), e4 „Horizontalabstand aus
   vorgegebener Neigung …“.
9. Oberstufenschreibweise x_1, x_2, x_3 und x_1x_2-Ebene durchgehend,
   auch wo der Katalog xy-Ebene schreibt.
10. Die senkrecht schneidende Gerade heißt q statt s (Original),
    damit ein Buchstabe nicht zugleich Gerade und Parameter ist.

## Befunde

- Katalog: die Erkennungsschritte „Punkt, Richtung, Parameter?“ (e1),
  „Aus welcher Koordinate …“ (e2) und „Identisch, parallel …“ (e3)
  verlangen denselben Handgriff wie die Vorstufe ihrer Kette und
  entfallen; der Katalog führt beide.
- Katalog: „Gerade oder Strecke?“ steht als Erkennungsschritt vor e1
  und e4 und zugleich als Vorstufe von e4; er steht nur in e1.
- Katalog: Sprossen nennen 2019-be-gk-B3.1c und
  2018MgrundlegendBAGLAA2WTR2-1e, die Mappe führt beide nicht in
  Abschnitt 2 – für diese Sprossen ist kein original möglich.
- bank.md: „Fertigkeit bis zum Doppelpunkt“ passt nicht auf die
  Sek-II-Fertigkeitszeilen, die mit Gedankenstrich trennen.
- Prüfskript: pruef "" ist nur bei pflicht begruenden erlaubt;
  Begründungssprossen der Ketten (e3 s1–s5, e2 s2) tragen deshalb
  eine Kontrollzahl, obwohl die Leistung verbal ist.

## Offene Punkte

- Die ksys3-Grafiken in e1 (Darstellung) sind nicht gesetzt worden;
  LaTeX ist in der Sitzung nicht verfügbar.
- e4 s4 v4: der vorgelegte Ansatz hat keine Lösung mit t zwischen
  null und eins; gefragt ist nur die Deutung, ein Blatt mit
  Rechenauftrag müsste das aufnehmen.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- geraden-e2-k2-s1-v1: pruef [0.6, 3] prüfte das Verhältnis 3 : 2 nur halb → pruef [0.6, 3, 2] (t = 0,6 mit sympy bestätigt) (Regel a).
- geraden-e4-k1-s4-v1: Lösungszusatz „eine Höhendifferenz, kein Lotabstand zu einer Ebene“ war falsch (beim waagerechten Dach in 4 m Höhe ist die Höhendifferenz genau der Lotabstand zur Ebene $x_3 = 4$) → Zusatz ersetzt durch „(beim waagerechten Dach ist diese Höhendifferenz zugleich der Lotabstand zur Dachebene)“ (Regel a).
- Prüfskript: Abweichungen 0.
