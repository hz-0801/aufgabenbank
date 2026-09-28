# Stand: tangente-normale-schnittwinkel

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5

## Zeilen je Datei und hoehe

| Datei| Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone |     26 |        0 |        12 |      13 |        0 |       1 |
| e1   |     51 |        4 |         5 |      30 |        6 |       6 |
| e2   |     51 |        4 |         5 |      30 |        6 |       6 |
| e3   |     32 |        4 |         5 |      15 |        2 |       6 |
| e4   |     48 |        4 |         5 |      27 |        6 |       6 |
| e5   |     39 |        4 |         5 |      18 |        6 |       6 |
| gesamt|    247 |       20 |        37 |     133 |       26 |      31 |

## Originale je Einheit

- e1: 2025-bebb-gk-A1.1a, 2020-A-1d, 2026-C-1d, 2021-B-2a,
  2026-bb-gk-B2.2b, 2019-be-gk-B2.2f, 2018MgrundlegendAAnalysis12-a,
  2018-bb-ea-cas-B2.2d, 2023-bebb-gk-B2.1c, 2024-bebb-lk-A1.5a,
  2025-bebb-lk-A1.6a, 2023-bebb-gk-A1.1a,
  2017MerhoehtBAnalysisWTR3-2e, 2018MerhoehtBAnalysisCAS3-1d,
  2017MerhoehtBAnalysisWTR2-1f; Prüfungshöhe: 2024-bebb-lk-A1.5b,
  2024MerhoehtAAnalysis21-b, 2017-bb-ea-B2.1c, 2019-C-1f
- e2: 2026-B-1g, 2019-A-2b, 2018-be-gk-cas-B1.1e, 2023-bebb-gk-B2.2d,
  2025-C-1f, 2017MerhoehtBAnalysisCAS2-2c,
  2020MgrundlegendBAnalysisWTR2-1c, 2018-bb-ea-cas-B2.1f,
  2017MerhoehtBAnalysisCAS2-2d, 2018MerhoehtBAnalysisCAS1-4,
  2017MerhoehtBAnalysisWTR1-1c, 2018MerhoehtBAnalysisCAS3-2f;
  Prüfungshöhe: 2025MerhoehtBAnalysisMMS2-2d,
  2019MgrundlegendBAnalysisWTR1-2a, 2026-B-1g
- e3: 2022-B-1f, 2023-A-1c, 2025-A-1h, 2024MerhoehtBAnalysisWTR3-1d,
  2026-bb-ea-B2.2e; Prüfungshöhe: 2023MerhoehtBAnalysisWTR2-2d
- e4: 2018MerhoehtBAnalysisWTR2-1f, 2017MerhoehtBAnalysisWTR3-2f,
  2020-be-gk-B2.1f, 2026MgrundlegendBAnalysisWTR1-1c,
  2023MgrundlegendBAnalysisWTR1-1c, 2026MerhoehtBAnalysisWTR2-2c,
  2023MerhoehtBAnalysisWTR2-1d, 2025MerhoehtBAnalysisMMS2-2b,
  2018-be-gk-B1.2b, 2022-bebb-gk-B2.1e, 2017-be-gk-B1.1e,
  2026-bb-ea-A1.2b, 2026MerhoehtAAnalysis11-b,
  2018MerhoehtBAnalysisCAS1-3b, 2017-be-gk-cas-B1.2f,
  2017MerhoehtBAnalysisWTR3-2g; Prüfungshöhe: 2026-bb-ea-B2.1d,
  2024-bebb-gk-B2.1i, 2025-bebb-gk-B2.1d
- e5: 2026-B-1h, 2018-bb-ea-B2.2b, 2017-be-gk-B1.2e,
  2022-bebb-gk-B2.1g, 2017-bb-ea-cas-B2.1c, 2017-bb-ea-A1.1b,
  2018-bb-ea-A1.1b, 2019MgrundlegendAAnalysis2-b, 2021-be-gk-B2.2f,
  2022MerhoehtBAnalysisWTR1-1d; Prüfungshöhe: 2024MerhoehtAAnalysis22,
  2024-bebb-lk-B2.1f, 2024-C-1g

## Prüfskript vor der Korrektur

| Datei | Abweichungen | häufigster Grund                | Warnungen |
|-------|-------------:|---------------------------------|----------:|
| zone  |            4 | Baustein \tan (4)               |         0 |
| e1    |           12 | Baustein \iff (10)              |         4 |
| e2    |            1 | Sperre g(x) = x + 1 (1)         |         0 |
| e3    |            0 | –                               |         0 |
| e4    |            2 | Ergebnisstelle, Sperre (je 1)   |         0 |
| e5    |            0 | –                               |         0 |

Die vier Warnungen in e1 bleiben (Entscheidung 5). In e3 wurden zwei
Grundfall-Lösungen nach eigener Durchsicht berichtigt (Befund 5).

## Entscheidungen

1. Zone: kette endet am Doppelpunkt, sonst vor „ – “; je Fertigkeit
   ein Fallstrick; das Zone-Paar steht bei „Ableitungswert als
   Tangentensteigung deuten“, weil „Funktionswert statt
   Ableitungswert“ laut Typische Fehler das häufigste Muster ist.
2. sprosse_text von Vorstufe und Grundfall ohne die Klammer
   „(Vorstufe …)“ bzw. „(Grundfall …)“, alle übrigen Sprossen
   wortgleich samt Belegklammer.
3. Typ ohne Kette nur dort, wo ein Original aus Abschnitt 2 der Mappe
   keine passende Kettensprosse hat (e1 zwei, e2 drei, e4 einer).
4. Pflichtelemente nur fehler und begruenden, weil „Typen je
   Lerneinheit“ nur diese nennt.
5. Die wortgleiche Pooldublette 2024-bebb-lk-A1.5b und
   2024MerhoehtAAnalysis21-b zählt als ein Original, je eine Zeile.
6. fhr-Zielmarken, deren Original schon an einer Kettensprosse steht
   (2026-C-1d, 2022-B-1f, 2025-A-1h), bekommen keine eigene
   Prüfungszeile; e3 hat daher nur zwei.
7. Originale, die der Katalog nur als Typ führt, stehen an der
   inhaltlich passenden Sprosse (etwa 2019-A-2b an e2 s3,
   2017-be-gk-cas-B1.2f und 2018MerhoehtBAnalysisCAS1-3b an e4 s9).
8. \tan und \iff sind keine Bausteine: Winkel mit \mathrm{tan},
   Äquivalenzen mit \Leftrightarrow.
9. Die mehrstelligen Kastenzahlen 0,5, 1,5, 4,47, 10,5, 18,4, 20,
   26,6, 45 und 90 kommen in keiner aufgabe vor („senkrecht“ statt
   90°, Winkelvorgaben ohne 45°).
10. In e3 heißt die Normale n(x); den y-Achsenabschnitt nennt e3
    deshalb nicht n.

## Befunde

1. Katalog: Alle vier Erkennungsschritte wiederholen die Vorstufe
   ihrer Einheit (e1 und e4 „Was ist gegeben?“, e2 „Berühren oder
   schneiden?“, e3 „Tangente oder Normale?“, e5 „Welches Dreieck?“)
   und entfallen; die Vorstufen bleiben.
2. Katalog: Viele Sprossen belegen nur mit Originalen, die die Mappe
   nicht aufnimmt (e1 s5, s7; e2 s2, s3, s6, s8; e3 s3, s5; e4 s8;
   e5 s5); sie tragen original null oder ein Ersatzoriginal (E. 7).
3. Katalog: Die Prüfungshöhen von e1, e2, e4 und e5 bündeln drei bis
   vier Teilziele in einer Sprosse; verfremdet sind nur die
   Originale aus Abschnitt 2.
4. Prüfskript: Ein Achsenabschnitt in „t(x) = 10x − 16“ ist keine
   Ergebnisstelle; pruef trägt daher oft die Steigung, n nur, wo die
   Lösung „n = …“ schreibt.
5. Prüfskript: Zwei falsch zusammengesetzte Grundfall-Lösungen in e3
   (Klammer im Bruch, „+ 0“) meldete es nicht; es prüft Zahlen,
   nicht die Form.
6. Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die eigene
   Probe fand 0 Treffer.
7. bank.md: tan fehlt in der Regel „sin, cos, ln als \mathrm{…}“.

## Offene Punkte

- Ohne Zeile: 2017MgrundlegendAAnalysis11-a und
  2025MgrundlegendBAnalysisWTR1-1b (e1 s4 hat nur drei Varianten),
  2018MerhoehtBAnalysisCAS3-1e, 2023-bebb-gk-B2.1j; dazu die
  Dubletten 2017-be-gk-cas-B1.2e, 2018-bb-ea-cas-B2.2b,
  2026MgrundlegendBAnalysisWTR2-1b.
- Kein LaTeX-Lauf; die Grafiken (ksys mit \funktion, \funktionab,
  \tangentean*, \gerade, \punkt) sind nur auf Bausteinname und
  Bereich geprüft.
- Typen ohne Original, die keine Sprosse deckt, haben keine Zeile.
- e4, Kette Winkel, Grundfall (Urteile vom 28.09., quer Sek II):
  die fünf Zeilen als Päckchen um einen festen Punkt, Winkel aus
  allen Lagen (spitz, stumpf, 90°); die 90°-Variante begründet
  „keine Steigung“. Umsetzung beim nächsten Bank-Auftrag des
  Eintrags.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- tangente-normale-schnittwinkel-e2-k2-s1-v3: Lösung nannte nur die Berührpunkte, gefragt sind die Tangenten → Tangenten $y = 6x - 4$ und $y = -2x - 4$ ergänzt, pruef um 6, −4, −2, −4 erweitert (Regel a).
- Prüfskript: Abweichungen 0.
