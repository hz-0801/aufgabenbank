# Stand: stammfunktion-und-hauptsatz

Katalog-Commit: f038ccb61160c64df73f067abd6bee324e86bee1
(2026-09-29, aus dem Kopf von mappen/stammfunktion-und-hauptsatz.md)
Datum: 2026-09-29 17:17 CEST (date)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.9
(--katalog aus der Mappe), Vorlage auftrag-eintrag.md 2026-09-29d;
Nachzug des Bestands vom 27./28.09. (Katalog 95b0f8b, Commit
945b26c). Umbauskript:
werkzeuge/einmalig/nachzug-stammfunktion-und-hauptsatz-2026-09-29.py.
Endstand: 0 Abweichungen, 0 Warnungen, mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      25         0        10      14        0       1
    e1.jsonl        35         4         5      15        5       6
    e2.jsonl        28         4         5       9        4       6
    e3.jsonl        32         4         5      12        5       6
    e4.jsonl        34         4         5      15        4       6
    gesamt         154        16        30      65       18      25

Pflicht je Einheit: fehler 3, begruenden 3 (Typenzeilen 23–26
nennen nur diese); Zone fehler 1 (Paar).

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         25      0              0          0
    e1           21      3             11          0
    e2           16      1             11          0
    e3           21      0             11          0
    e4           23      0             11          0

Übernommen heißt: aufgabe, loesung, merkmal wortgleich; nachgezogen
nur quelle (97–100 → 94–97), sprosse, id und sprosse_text (drei
Vorstufen mit längerem Text); in e2 dazu hoehe der drei Zeilen, die
von der Sprosse „nur einsetzen“ zur Vorstufe 0 wurden.
Umgeschrieben: je Kette die fünf Grundfallzeilen (Päckchen) und je
Einheit die sechs Pflichtzeilen (bei v1 von fehler und begruenden
nur merkmal). Neu: e1 Sprosse 4 „drei verschiedene Stammfunktionen
…“ (3), e2 vierte Zeile der Vorstufe 0 (1).

## Originale je Einheit

- e1: 2022MerhoehtBAnalysisWTR3-2a, 2020-be-gk-A1.1a,
  2018-be-gk-B1.2c, 2020MgrundlegendBAnalysisWTR2-1e,
  2024MerhoehtBAnalysisWTR1-1d, 2025MgrundlegendAAnalysis12-a,
  2026MgrundlegendBAnalysisWTR1-1d, 2020-be-gk-B2.1h,
  2024MgrundlegendBAnalysisWTR1-1f, 2026MerhoehtAAnalysis12-b;
  Prüfungshöhe 2023-bebb-gk-B2.1l.
- e2: 2026MerhoehtBAnalysisWTR3-1b, 2025MerhoehtBAnalysisWTR3-2c
  (beide Vorstufe 0), 2023MgrundlegendAAnalysis13-a,
  2018MgrundlegendBAnalysisWTR-1d, 2021MgrundlegendAAnalysis13-a,
  2025-bebb-lk-B2.2b, 2017MerhoehtBAnalysisCAS1-2h,
  2018MerhoehtBAnalysisCAS1-3c; Prüfungshöhe 2025-bebb-gk-B2.2d,
  2022MgrundlegendBAnalysisWTR1-1f.
- e3: 2023-bebb-gk-A1.2b, 2021MgrundlegendAAnalysis2-b,
  2023MerhoehtAAnalysis21-b, 2022MerhoehtAAnalysis11-a,
  2021MgrundlegendAAnalysis11-a, 2026-bb-gk-B2.1b, 2026-bb-ea-B2.1e,
  2019MgrundlegendBAnalysisWTR2-1e, 2022-bebb-lk-B2.1k,
  2024-bebb-gk-B2.1f, 2025MerhoehtBAnalysisMMS2-1c;
  Prüfungshöhe 2020MgrundlegendBAnalysisWTR2-1h.
- e4: 2018MerhoehtBAnalysisWTR1-1d, 2017MerhoehtBAnalysisWTR2-1k,
  2017MerhoehtBAnalysisWTR2-1j; Prüfungshöhe 2026MerhoehtAAnalysis23,
  2026MerhoehtBAnalysisMMS1-1h.

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 92 Abweichungen
  (e1 26, e2 18, e3 26, e4 22), alle „sprosse_text nicht wortgleich
  in Zeile“ (Katalogzeilen um drei verschoben). Zone 0.
- e1.jsonl: 1 / 0 – pruef nicht an der Ergebnisstelle (Grundfall
  v5, Rechenzeile mit Zahl vor dem Ergebnis); korrigiert.
- e2.jsonl, e3.jsonl, e4.jsonl: 0 / 0.
- Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 30–35 unverändert.
2. Päckchen, fester Wert im merkmal: e1 die Form r² − (r − x)²
   (r wandert; v5 ist die übernommene Kugelschale derselben Form),
   e2 f(x) = 3x² + a · x auf [−1; 2] (a wandert), e3 die Parabel
   f(x) = ½(x − 1)² + e mit P(0 | 1) (e wandert), e4 f(t) = t² − 2t
   (die untere Grenze wandert).
3. Grundfall-Originale bleiben auf ihren Varianten (e2 v4, v5; e3
   v3–v5), die Aufgabe ist jetzt die Päckchenzeile mit Prüfkennung.
4. e2: die drei alten Zeilen „nur einsetzen“ sind Vorstufe 0 (Aufgabe
   gleich), eine vierte zeigt F(a) negativ, wie der Sprossentext
   verlangt.
5. Neue Sek-II-Lösungen des Hauptsatzes tragen die Klammer
   [F(x)] mit Grenzen als eigene Zeile (Hinweis Sek II,
   regeln.md 12); übernommene Zeilen bleiben ohne.
6. P1 (Serie) in allen Einheiten statt P3, weil keine Einheit
   Gleichungen umformt; Kennzeichen: Exponent, Vorzeichen, Schranke,
   Nullstelle der unteren Grenze.
7. Urteile je Einheit: P2 „Richtig.“, P6 „Nein;“ – je ein Ja und ein
   Nein.
8. Neue Sprosse e1 s4 als form zeichnen mit leerem ksys; die
   Lösungsgrafik zeigt die drei Graphen mit c = 0, 2, −2.

## Befunde

- Katalog: Die Erkennungsschritte sind seit 27.09. gestrichen
  (Zeile 36); die drei Vorstufen tragen jetzt den vollen Text.
- Katalog: Die Vorstufe e2 nennt 2025-bebb-lk-B2.2b, das Original
  steht aber als Gegenstück an Sprosse 3 (Ableitung); die Vorstufe
  trägt die beiden iqb-Originale.
- Prüfskript: prüft die Form der Pflichtzeilen (P1–P6) nicht; die
  drei Formen je Einheit sind nur durch Durchsicht gesichert.
- bank/_punkte.csv: 17 Zeilen mit original haben eine neue id
  (e1 s4–s6 → s5–s7, e2 s2–s5 → s0–s4); die Datei ist nicht
  nachgezogen (nicht Schreibbereich).

## Offene Punkte

- Ohne Zeile wie 27.09.: 2017-be-gk-B1.2d, 2022-bebb-gk-B2.2d,
  2023-bebb-lk-B2.1k, 2024-bebb-gk-B2.1e, 2020MerhoehtAAnalysis21-a,
  2026-bb-gk-A1.7b, 2026MgrundlegendAAnalysis22-b,
  2017MerhoehtBAnalysisWTR2-1i.
- Grundvorstellung (Zeile 92) steht nicht in der Bank.
- Punkte-Urteile für die umgeschriebenen Grundfallzeilen mit
  original (e2 v4, v5; e3 v3–v5) sind neu zu fällen.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27./28.09. und sind nicht nachgezogen.
