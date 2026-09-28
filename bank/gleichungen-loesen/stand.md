# Stand: gleichungen-loesen

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
(2026-09-26T16:47:30+02:00)
Datum: 2026-09-27 14:44 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen,
0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|---|---|---|---|---|---|---|
| zone | 38 | – | 16 | 21 | – | 1 |
| e1 | 56 | 4 | 5 | 33 | 2 | 12 |
| e2 | 50 | 4 | 5 | 30 | 2 | 9 |
| e3 | 47 | 4 | 5 | 24 | 2 | 12 |
| e4 | 32 | 4 | 5 | 9 | 2 | 12 |

## Originale je Einheit

- e1: 2025-A-2c, 2024-C-2f, 2021-A-1e,
  2019MgrundlegendAAnalysis12-a, 2021-A-2b, 2020-A-2a, 2022-B-2a,
  2018-be-gk-B1.1f, 2022-C-2d, 2023-C-2c, 2019-be-gk-A1.2a,
  2020MgrundlegendBAnalysisWTR1-1a, 2019MgrundlegendBAnalysisWTR1-3b,
  2020-be-gk-B2.2b, 2019-C-2c (Prüfungshöhe),
  2017MerhoehtBAnalysisCAS2-2a (Typ ohne Kette)
- e2: 2017-bb-ea-A1.1a, 2017MerhoehtAAnalysis11-a,
  2022MerhoehtBAnalysisWTR3-1a, 2024MerhoehtBAnalysisWTR1-2b,
  2018MerhoehtBAnalysisWTR2-1b, 2021-be-gk-B2.2g,
  2022-bebb-gk-B2.1d, 2026-bb-ea-A1.1a, 2026MerhoehtAAnalysis14-a,
  2025-bebb-lk-B2.2d, 2018MerhoehtAAnalysis11-a,
  2026MerhoehtAAnalysis13-a, 2023MgrundlegendAAnalysis2-b
  (Prüfungshöhe), 2018-be-gk-cas-B1.2b (Typ ohne Kette)
- e3: 2019MgrundlegendBAnalysisWTR1-2d, 2023MerhoehtBAnalysisWTR2-2b,
  2025-bebb-gk-B2.2g, 2025MgrundlegendBAnalysisWTR2-2c,
  2026MerhoehtBAnalysisMMS2-1b, 2025MerhoehtBAnalysisWTR3-2a,
  2022MerhoehtBAnalysisWTR3-3b, 2025-bebb-gk-A1.7a,
  2025MgrundlegendAAnalysis22-a, 2023-bebb-lk-B2.1i (Prüfungshöhe),
  2018-bb-ea-cas-B2.2f (Typ ohne Kette)
- e4: 2023-bebb-gk-B2.2g, 2022-bebb-lk-B2.1m, 2019-be-gk-B2.2g,
  2024-bebb-gk-B2.2h (Prüfungshöhe), 2017MgrundlegendBAnalysisCAS-1d,
  2018-be-gk-cas-B1.1g (Typ ohne Kette)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund |
|---|---|---|---|
| zone | 13 | 0 | merkmal uneinheitlich (8) |
| e1 | 6 | 0 | pruef fehlt (3) |
| e2 | 0 | 0 | – |
| e3 | 2 | 0 | Sperre k(x) − g(x) = 0 (2) |
| e4 | 0 | 0 | – |

Keine Einheit scheiterte zweimal. Nach dem Commit von e3 fand die
Gegenprobe die Kastenzahl 100 in e3-k1-s1-v4 (1 LE = 100 m); die
Zeile trägt jetzt 1 LE = 50 m und geht mit diesem Commit ein.

## Entscheidungen

- Zone: Fertigkeitszeilen ohne Doppelpunkt (Z. 33, 35, 36, 38)
  tragen als kette den Text bis zum ersten Gedankenstrich.
- Zone: Fertigkeit 3 ohne Polynomdivision, weil sie als Verfahren
  in Einheit 1 steht und die Zone nichts Neues lehrt.
- Zone-Paar in Fertigkeit 2 (durch x geteilt, Lösung null
  verloren) als Sprossen 5 und 6: häufigstes Muster „Lösungen
  verloren".
- sprosse_text ist der Sprossentext ohne Klammerzusatz (Kennung,
  Niveau); die Kennungen stehen im Feld original.
- Pflichtkette: Sprosse 1 fehler, 2 begruenden, 3 anwendung,
  4 darstellung; sprosse_text „Fehler finden", „Begründen",
  „Anwendung", „Darstellungswechsel"; quelle ist die Typenzeile.
- Darstellung in e1, e3, e4 (Gleichung oder Ungleichung und
  Graph), nicht in e2, dessen Typen rein algebraisch sind.
- Typ ohne Kette: kette ist der Typname aus „Typen je
  Lerneinheit", Sprosse 1, mit dem CAS-Original des Typs.
- e1: Prüfungshöhe nur 2019-C-2c; die fhr-Zielmarke 2022-B-2a
  steht verfremdet an Sprosse 5, „an der Abbildung prüfen" als
  Textbedingung (nächster Schnittpunkt rechts von Q).
- Rechneraufgaben: pruef aus geschlossener Form oder numerischer
  Nullstelle; e3 Sprosse 5 so gewählt, dass r(t) = r(t − c) die
  geschlossene Lösung t = c · e/(e − 1) hat.
- Termergebnisse und Termnachweise: pruef ist die erste Zahl der
  Lösung, weil das Skript nur dort eine Ergebnisstelle sieht.

## Befunde

- Katalog: Alle drei Erkennungsschritte (Z. 40–42) verlangen den
  Handgriff der Vorstufen (Z. 106–109); sie entfallen, der Katalog
  führt beide.
- Katalog Z. 27 nennt Nachzüge vom 28. und 29.09.2026, der
  Katalog-Commit ist vom 26.09.2026.
- bank.md: Die Regel „Fertigkeit bis zum Doppelpunkt" greift bei
  Z. 33, 35, 36, 38 nicht; Z. 38 hat erst im Ermessen-Vermerk
  einen.
- Prüfskript: Bei Termen gilt nur die erste Zahl als
  Ergebnisstelle; pruef prüft dort einen Koeffizienten, nicht den
  Term.
- Prüfskript: Grenzen einer Ungleichung („x > 0") sind keine
  Ergebnisstelle; die Lösungen nennen sie zusätzlich als „x = …".
- Prüfskript: Die Sperre meldet k(x) − g(x) = 0, obwohl die
  Sprosse (Z. 108) diese Form selbst nennt; Funktion umbenannt.

## Offene Punkte

- Grafiken mit \funktion und exp (e3 Sprosse 5, e4 Darstellung)
  sind nicht kompiliert; Achsenbereiche nur rechnerisch geprüft.
- Einheit 4 steht ohne Planzeile (Katalog-Ermessen); die Zeilen
  taugen nur für Abitur Teil B.

## Nachbesserung Gegenlese 2026-09-28

- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- gleichungen-loesen-e1-k1-s7-v2: unterer Bogen g lag zwischen x = 4 und x = 6 unter dem Boden (g(5) = −0,5) → f(x) = −0,5x² + 5x − 2, g(x) = 0,5x² − 5x + 14 (Minimum 1,5), S₁(2 | 6), S₂(8 | 6), Platte 6 m × 6 m, 36 m², 1 080 € (Regel a).
- gleichungen-loesen-e1-k3-s3-v1: pruef [2, 8] prüfte die Antwortzahlen nicht → pruef [2, 8, 200, 800], Lösung „von 2 · 100 = 200 bis 8 · 100 = 800 Stück“ (Regel b).
- gleichungen-loesen-e1-k3-s3-v3: pruef [4, 8] prüfte die Uhrzeiten nicht → pruef [4, 8, 10, 14], Lösung „um 6 + 4 = 10 Uhr und um 6 + 8 = 14 Uhr“ (Regel b).
- gleichungen-loesen-e3-k3-s1-v1: pruef [0, 4] nahm die Zahlen der falschen Schülergleichung → pruef [4, 30], Lösung ergänzt „also p(x + 4) − p(x) = 30“ (Regel a).
- Prüfskript: Abweichungen 0.
