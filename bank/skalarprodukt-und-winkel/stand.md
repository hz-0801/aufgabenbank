# Stand – skalarprodukt-und-winkel

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     31 |      – |      12 |      18 |      – |       1 |
| e1    |     26 |      4 |       5 |       9 |      2 |       6 |
| e2    |     38 |      8 |       5 |      12 |      4 |       9 |
| e3    |     31 |      4 |       5 |       9 |      4 |       9 |
| e4    |     29 |      4 |       5 |       9 |      2 |       9 |
| Summe |    155 |     20 |      32 |      57 |     12 |      34 |

## Originale je Einheit

- e1: 2024MerhoehtAAGLAA211-b, 2025MerhoehtAAGLAA211-a,
  2025MerhoehtAAGLAA211-b, 2024MgrundlegendBAGLAA1WTR-1f,
  2021MgrundlegendAAGLAA12-c
- e2: 2026-bb-gk-B3b, 2019-be-gk-B3.2c, 2018-bb-ea-B3.1c,
  2024-bebb-gk-B3b, 2021MgrundlegendBAGLAA2WTR2-1d,
  2023MerhoehtBAGLAA1WTR-2a, 2017-bb-ea-B3.1b
- e3: 2025-bebb-gk-B3c, 2024-bebb-gk-B3e, 2018-be-gk-B2.2c,
  2024MgrundlegendBAGLAA2WTR1-1c, 2022MerhoehtBAGLAA2WTR2-1d,
  2020MgrundlegendBAGLAA2WTR-1b, 2026MgrundlegendBAGLAA2WTR1-1e,
  2017-bb-ea-B3.1b
- e4: 2023MgrundlegendBAGLAA2WTR1-1f, 2017-bb-ea-B3.2a,
  2023MerhoehtBAGLAA2WTR1-1d, 2023MerhoehtBAnalysisWTR2-2e,
  2018MerhoehtBAGLAA2CAS2-1f

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                     |
|-------|-----:|------:|--------------------------------------|
| zone  |    9 |     0 | Tripel mit \mid in der Lösung        |
| e1    |    4 |     0 | pruef fehlt bei Begründung (3)       |
| e2    |    7 |     0 | Sperre Tripel aus der Mappe (4)      |
| e3    |    1 |     0 | Sperre Term 3x+4z                    |
| e4    |    1 |     0 | Sperre Tripel aus der Mappe          |

Keine Einheit scheiterte zweimal. Nachtrag: e4-k1-s4-v2 trug die
Kastenzahl 26 (M(0 | 26)); nachträglich geändert, dabei eine
Sperre (0|5) behoben; die Kastenzahl-Probe meldet jetzt 0.

## Entscheidungen

1. Nennt der Katalog an einer Kettensprosse ein Original, trägt es
   die letzte Variante mit Prüfkennung; die übrigen haben original
   null. In e3 s3 trägt jede Variante eines der drei Originale.
2. Prüfungshöhe mit zwei Originalen (e2, e3): eine Sprosse mit
   2 Zeilen je Original; sprosse_text ohne die Klammerbelege.
3. Pflichtelemente: fehler und begruenden überall, anwendung in
   e2 bis e4; e1 ohne Anwendung (reine Teil-A-Typen), darstellung
   nirgends, weil kein Typ einen Darstellungswechsel trägt.
4. Zone: kette und sprosse_text sind die Fertigkeit bis „ – “, da
   die Zeilen keinen Doppelpunkt haben; Folge wie im Eintrag.
5. Zone-Paar bei f5 (Neben- und Komplementwinkel): „Nachbarwinkel
   statt des verlangten“ hat unter den Zone-Fallstricken die
   meisten Belege in „Typische Fehler“.
6. e2-Prüfungshöhe Zelt gibt beide Wandebenen vor, weil Normalen
   von Ebenen erst e3 bringt; e3 verlangt die Nachbarebene selbst.
7. e4: der Schattentyp steht als Typ ohne Kette (k2), sein
   Original 2018MerhoehtBAGLAA2CAS2-1f an v3.
8. Tupel in loesung mit „|“, in aufgabe mit „\mid“ (Befund 6).
9. Winkel auf eine Nachkommastelle, Gradzeichen als ^\circ;
   Prüfkennung „(Abitur Jahr GK/LK)“ nach bank.md.

## Befunde

1. Katalog: Erkennungsschritt „Zahl oder Vektor?“ wiederholt die
   Vorstufe von e1; er entfällt.
2. Katalog: „Welche zwei Richtungen bilden den Winkel?“ wiederholt
   die Vorstufe von e2; er entfällt.
3. Katalog: „Kosinus oder Sinus?“ steckt in der Vorstufe von e3
   (und e4); er entfällt.
4. Katalog: „Der Formelwinkel oder sein Nachbar?“ steht als
   Erkennungsschritt in e2 und nochmals in der Vorstufe von e3.
5. Katalog: 2017-bb-ea-B3.1b ist Prüfungshöhe in e2 und e3; in e2
   verlangt es Ebenen-Normalen, die erst e3 einführt.
6. Skript: normiert() streicht \mid, die Ergebnisstelle erkennt
   Tupel nur mit „|“; die Sperre (mathnorm) wandelt \mid um.
7. Skript: pruef "" gilt nur bei pflicht begruenden; eine
   Begründung an einer Kettensprosse mit Ziffern in der Lösung
   meldet „pruef fehlt“, obwohl bank.md "" bei Begründen erlaubt.
8. Skript: pruef kennt nur math, nicht abs(); bank.md sagt nichts.
9. Mappe: Zeile 27 des Katalogs nennt Nachzüge vom 28./29.09.2026,
   der Katalog-Commit ist vom 26.09.2026.
10. bank.md: „Fertigkeit bis zum Doppelpunkt“ greift nicht, wenn
    die Zeile mit Gedankenstrich fortfährt.

## Offene Punkte

1. Kein Pflichtelement darstellung; Aufgaben mit ksys3-Grafik
   (Punkte ablesen, dann Winkel) wären möglich, wenn gewünscht.
2. Sachbild-Aufgaben (e3 s3, e3 s5) stehen ohne Grafik; eine
   Skizze mit \rpyramide oder \rebene würde sie stützen.
