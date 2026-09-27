# Stand: rekonstruktion-von-funktionsgleichungen

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     27 |        0 |        12 |      14 |        0 |       1 |
| e1    |     37 |        4 |         5 |      18 |        4 |       6 |
| e2    |     42 |        4 |         5 |      21 |        6 |       6 |
| e3    |     40 |        4 |         5 |      21 |        4 |       6 |
| gesamt|    146 |       12 |        27 |      74 |       14 |      19 |

## Originale je Einheit

- e1: 2022-C-2b, 2022-bebb-gk-B2.2g, 2019-C-2a, 2023-C-2b,
  2026-C-2c, 2023-A-2a, 2026-B-2a, 2018MerhoehtBAnalysisWTR1-1a,
  2022MgrundlegendAAnalysis12-a, 2026MerhoehtAAnalysis13-b,
  2025-bebb-lk-A1.2b, 2025-C-2d, 2021-A-2a (Prüfungshöhe),
  2020-C-2a (Prüfungshöhe)
- e2: 2021-be-gk-B2.1k, 2019-be-gk-B2.1c, 2023-bebb-gk-B2.2k,
  2022-bebb-lk-B2.1i, 2020-be-gk-A1.2a, 2020MgrundlegendAAnalysis12,
  2018-be-gk-B1.1e, 2022-bebb-gk-B2.2k, 2023-bebb-lk-A1.4b,
  2026-bb-ea-B2.1g, 2018-bb-ea-B2.2h (Prüfungshöhe),
  2022MerhoehtAAnalysis2 (Prüfungshöhe), 2025-A-2a (Prüfungshöhe),
  2017MgrundlegendBAnalysisCAS-1e
- e3: 2022MerhoehtBAnalysisWTR1-2a, 2022MgrundlegendBAnalysisWTR1-1g,
  2023-bebb-lk-B2.1l (Prüfungshöhe), 2023MerhoehtAAnalysis22
  (Prüfungshöhe), 2018MerhoehtBAnalysisCAS3-2e, 2017-be-gk-B1.2f,
  2017MerhoehtBAnalysisWTR3-2i

## Prüfskript vor der Korrektur

| Datei | Abweichungen | häufigster Grund                  | Warnungen |
|-------|-------------:|-----------------------------------|----------:|
| zone  |            1 | Sperre (1)                        |         0 |
| e1    |            7 | grafik leer (4)                   |         0 |
| e2    |            1 | Sperre (1)                        |         0 |
| e3    |            5 | grafik leer (3)                   |         0 |

Nach der Korrektur: 0 Abweichungen, 0 Warnungen. Keine Einheit
scheiterte zweimal.

## Entscheidungen

- Zone: kette endet am Doppelpunkt, sonst vor „ – “ (Ableitungsregeln,
  Sinus- und Kosinusgraph), wie bei ableitungsregeln.
- Zone-Paar bei den LGS (Vorzeichen beim Subtrahieren), weil das LGS
  das Lösungswerkzeug aller drei Einheiten ist.
- Zone „Lineare Funktionen" hat zwei Fallstricke: Vorzeichen der
  Steigung und die senkrechte Steigung, die e2 s8 braucht.
- e1 s2 „Gerade nachweisen“ ist eine eigene Sprosse (Umkehrung),
  obwohl der Katalog sie mit „und“ an den Grundfall hängt.
- e1 s1 v5 verfremdet 2022-C-2b ohne den senkrechten Anstieg, damit
  der Grundfall kein zweites Merkmal bekommt.
- Die Prüfungshöhe nimmt die fhr-Zielmarke der Kette mit auf (e1
  2020-C-2a, e2 2025-A-2a), je 2 Zeilen neben dem Prüfungsoriginal.
- Nennt eine Sprosse ein Original, tragen es alle Varianten; nennt sie
  mehrere, trägt jede Variante eines; ohne passende Form original null.
- Pflichtelemente nur fehler und begruenden, weil „Typen je
  Lerneinheit“ nur diese nennt; keine anwendung, keine darstellung.
- Typen ohne Kette: e2 Exponentialfunktion aus Wert und Rate, e3
  Bogenlänge, Existenzfrage und Randtangenten, je 3 Zeilen mit Original.
- Kastenzahlen: nur 10 und 220 sind mehrstellig (Kastenzeilen ohne
  Auswendig-, Formelsammlungs- und Quellenzeile); keine aufgabe enthält
  sie.

## Befunde

- Katalog: Der Erkennungsschritt „Wie viele Unbekannte, wie viele
  Bedingungen?“ wiederholt die Vorstufe von e1 und entfällt.
- Katalog: Der Erkennungsschritt „Welche Gleichung steckt in diesem
  Wort?“ wiederholt die Vorstufe von e2 und entfällt.
- Katalog: Der Erkennungsschritt „Wie weit bis zum nächsten
  Hochpunkt?“ wiederholt die Vorstufe von e3 und entfällt.
- Katalog: Die Prüfungshöhe von e1 (2021-A-2a) verlangt die
  Tiefpunktbedingung f'(x) = 0, die erst Einheit 2 einführt.
- Katalog: 2025-C-2d steht an zwei Sprossen von e1 (Symmetrie und
  markante Punkte); die Bank führt es nur an der zweiten.
- Mappe: 2018MerhoehtBAnalysisWTR1-1g, 2026-bb-ea-B2.1i und
  2023-bebb-lk-B2.1m (e3 s3–s5) fehlen in Abschnitt 2; original null.
- Prüfskript: pruef "" gilt nur bei pflicht begruenden; Begründungen an
  Prüfungshöhe oder als Typ ohne Kette brauchen eine ziffernfreie
  Lösung oder ein pruef.
- Prüfskript: „im Koordinatensystem“ in einer Maßstabsangabe gilt als
  Ableseauftrag; sieben Zeilen wurden deshalb umformuliert.
- Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die Gegenprobe
  lief separat.

## Offene Punkte

- Ohne Zeile: 2017-be-gk-B1.1f, 2018-be-gk-cas-B1.1f,
  2017MerhoehtBAnalysisWTR3-2h, 2017MerhoehtBAnalysisCAS2-4,
  2018MerhoehtBAnalysisCAS1-3a, 2018MerhoehtBAnalysisCAS2-2f;
  2025MerhoehtAAnalysis13-b nur über die wortgleiche Dublette
  2025-bebb-lk-A1.2b.
- Der Bogenlängentyp (e3 k2) ist im Katalog Ermessen und verlangt den
  Rechner; wandert er, wandern die Zeilen mit.
- Kein LaTeX-Lauf; Grafiken (ksys mit \funktionab, \punkt,
  \asymptote) sind nur auf Bausteinname und Bereich geprüft.
