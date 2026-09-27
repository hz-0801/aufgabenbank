# Stand: schnittmengen

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     26 |        0 |        12 |      13 |        0 |       1 |
| e1    |     36 |        8 |         5 |      15 |        2 |       6 |
| e2    |     31 |        4 |         5 |      12 |        4 |       6 |
| e3    |     32 |        4 |         5 |      15 |        2 |       6 |
| gesamt|    125 |       16 |        27 |      55 |        8 |      19 |

## Originale je Einheit

- e1: 2017MerhoehtAAGLAA211-b, 2019MerhoehtAAGLAA21-a,
  2023-bebb-gk-B3d, 2026-bb-ea-B3c, 2026MerhoehtBAGLAA2WTR2-1c,
  2018-bb-ea-B3.1e, 2017-bb-ea-B3.2b, 2019-be-gk-B3.1b,
  2020MgrundlegendBAGLAA2WTR-1d, 2019MgrundlegendBAGLAA2WTR2-1g,
  2018-be-gk-B2.1e, 2023MerhoehtBAGLAA2WTR1-1e (Prüfungshöhe),
  2018MerhoehtBAGLAA2CAS2-1g
- e2: 2021MgrundlegendBAGLAA2WTR2-1c, 2023-bebb-gk-A1.4b,
  2023MgrundlegendAAGLAA212-b, 2018MerhoehtBAGLAA2WTR2-1f,
  2018-bb-ea-B3.1a, 2019-be-gk-B3.2f (Prüfungshöhe),
  2019MgrundlegendBAGLAA2WTR1-1f (Prüfungshöhe),
  2017MgrundlegendBAGLAA2CAS1-1e
- e3: 2020-be-gk-B3.1b, 2021-be-gk-B3h,
  2021MgrundlegendBAGLAA2WTR1-1e, 2017MerhoehtAAGLAA211-a,
  2018MerhoehtBAGLAA1WTR-1b, 2025-bebb-lk-A1.3b,
  2025MerhoehtAAGLAA212-b, 2018MgrundlegendBAGLAA2WTR1-1c,
  2018MerhoehtBAGLAA2WTR1-1d, 2021-be-gk-B3e,
  2020-be-gk-B3.1d (Prüfungshöhe)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | häufigster Grund                  | Warnungen |
|-------|-------------:|-----------------------------------|----------:|
| zone  |            0 | –                                 |         0 |
| e1    |            2 | Sperre (2)                        |         0 |
| e2    |            4 | Sperre (4)                        |         0 |
| e3    |            4 | Sperre (4)                        |         0 |

Nach der Korrektur: 0 Abweichungen, 0 Warnungen. Keine Einheit
scheiterte zweimal.

## Entscheidungen

- Zone: kette „Den Lagebefund vorweg führen (…)“ endet vor dem „ – “
  nach der Klammer; der erste „ – “ steht in der Klammer.
- Zone-Paar bei den Geradengleichungen (Aufpunkt vergessen), dem
  ersten Muster der Typischen Fehler.
- Der Erkennungsschritt „Was wird geschnitten …?“ („vor allen
  Einheiten“) steht als eigene Kette k1 in e1.
- Nennt eine Sprosse ein Original, tragen es alle Varianten; nennt sie
  mehrere, reihum; e1 s3 hat je Sonderfall eine Variante.
- Typen ohne Kette: e1 Höhe aus dem Schattenabstand, e2 Schatten auf
  einer Kante, je 3 Zeilen mit Original.
- Pflichtelemente nur fehler und begruenden, weil „Typen je
  Lerneinheit“ nur diese nennt; keine anwendung, keine darstellung.
- Schrägbilder als ksys3 mit Option xyz, weil Katalog und Landeshefte
  x, y, z schreiben; Strecken als \rgerade[0:1] mit leerem Label.
- 2020-be-gk-B3.1d trägt „(Abitur 2020 GK)“, obwohl der Katalog es
  LK-Stoff nennt; bank.md ordnet be-gk dem GK zu.
- Beschreibungsaufgaben (e1 s6) haben eine ziffernfreie Lösung, damit
  pruef leer bleiben darf.
- Kastenzahlen: 12, 18 und 36 sind mehrstellig (Kastenzeilen ohne
  Auswendig-, Formelsammlungs- und Quellenzeile); keine aufgabe hat sie.

## Befunde

- Katalog: Der Erkennungsschritt „Einsetzen oder gleichsetzen?“
  wiederholt die Vorstufe von e1 und entfällt.
- Katalog: Der Erkennungsschritt „Wie viele Gleichungen, welche ist
  die Probe?“ wiederholt die Vorstufe von e2 und entfällt.
- Katalog: Der Erkennungsschritt „Welche Koordinate ist null?“
  wiederholt die Vorstufe von e3 und entfällt.
- Katalog: Die Fertigkeitszeilen haben keinen Doppelpunkt, und in
  „Den Lagebefund vorweg führen“ steht ein „ – “ in der Klammer.
- Mappe: Sie meldet 2018-bb-ea als nicht gefunden, führt aber
  2018-bb-ea-B3.1a und -B3.1e mit Spalten; die Bank nutzt sie.
- Prüfskript: Die Sperre trifft einfache Achsen- und Eckpunkte wie
  (3|0|0), (0|0|2) oder (2|2|0); zehn Zeilen wurden deshalb umgebaut.
- Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die Gegenprobe
  lief separat.

## Offene Punkte

- Ohne Zeile: 2023MgrundlegendBAGLAA2WTR2-1d,
  2017MgrundlegendBAGLAA2WTR1-1d, 2018MerhoehtBAGLAA2CAS2-1a (Spitze
  auf der Achse, in e1 s3 nur eine Variante);
  2018MerhoehtBAGLAA2CAS1-1a und -1e nur über die wortgleichen
  Dubletten 2018-bb-ea-B3.1a und -B3.1e.
- Die Typen ohne Kette (Schattenhöhe, Schatten auf der Kante) sind im
  Katalog Ermessen; wandern sie, wandern die Zeilen mit.
- Kein LaTeX-Lauf; ksys3-Grafiken (\rpyramide, \rquader, \rgerade als
  Strecke) sind nur auf Bausteinname und Bereich geprüft.
