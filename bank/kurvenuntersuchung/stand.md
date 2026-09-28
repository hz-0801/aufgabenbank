# Stand: kurvenuntersuchung

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26)
Datum: 2026-09-27 14:56 UTC
Prüfskript: bank-pruef.py v0.5, am Ende 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     29 |        – |        12 |      16 |        – |       1 |
| e1    |     39 |        4 |         5 |      15 |        6 |       9 |
| e2    |    106 |        8 |        10 |      75 |        4 |       9 |
| e3    |     63 |        4 |         5 |      39 |        6 |       9 |
| e4    |     46 |        4 |         5 |      24 |        4 |       9 |
| e5    |     52 |        4 |         5 |      27 |        4 |      12 |
| Summe |    335 |       24 |        42 |     196 |       24 |      49 |

## Originale je Einheit

- E1: 2026MgrundlegendBAnalysisWTR1-1a, 2024-bebb-gk-A1.7a,
  2021-be-gk-B2.1g (Prüfung), 2021-A-1c (Prüfung),
  2024-C-1d (Prüfung)
- E2: 2025-C-1d, 2023-C-1c, 2025-bebb-gk-B2.2b, 2019-be-gk-B2.2b,
  2018-bb-ea-B2.1g, 2021-be-gk-B2.2d (Prüfung), 2026-C-1e (Prüfung),
  2026MgrundlegendAAnalysis11-a, 2020MgrundlegendAAnalysis11-a,
  2022-bebb-gk-B2.1a, 2025-bebb-lk-A1.1a, 2021-be-gk-B2.1f,
  2026MgrundlegendAAnalysis11-b, 2025-bebb-gk-B2.1b,
  2023MgrundlegendBAnalysisWTR1-1a, 2018MerhoehtBAnalysisCAS2-1d,
  2017-be-gk-cas-B1.1e, 2023MgrundlegendBAnalysisWTR1-1b
- E3: 2018MgrundlegendBAnalysisWTR-1a, 2024-B-1e, 2023-bebb-gk-B2.1f,
  2021-be-gk-B2.2e (Prüfung), 2026-C-1f (Prüfung),
  2020-C-1d (Prüfung), 2021MgrundlegendBAnalysisWTR-1b, 2021-A-1d,
  2026MgrundlegendBAnalysisMMS2-1c, 2022MerhoehtBAnalysisWTR1-2c,
  2018MerhoehtAAnalysis12-b, 2017MerhoehtBAnalysisCAS2-2b,
  2018MerhoehtBAnalysisCAS3-2d
- E4: 2020-be-gk-B2.2d, 2023-bebb-lk-A1.1b, 2023-bebb-lk-A1.1a,
  2023MerhoehtAAnalysis11-a, 2024-bebb-gk-B2.1d (Prüfung),
  2023-bebb-gk-B2.2e (Prüfung)
- E5: 2022MgrundlegendBAnalysisWTR2-2c, 2023-C-2a, 2024-C-2d,
  2019-be-gk-B2.2c, 2018-be-gk-B1.1d, 2026-bb-gk-B2.1f,
  2024MgrundlegendBAnalysisWTR2-2c (Prüfung), 2021-B-2d (Prüfung),
  2017-be-gk-B1.1c, 2024MerhoehtBAnalysisWTR3-1c,
  2018MgrundlegendBAnalysisWTR-2e, 2018MerhoehtBAnalysisWTR1-2d

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                 |
|-------|-------------:|----------:|----------------------------------|
| zone  |            0 |         0 | –                                |
| e1    |            0 |         0 | –                                |
| e2    |            1 |         0 | pruef nicht an Ergebnisstelle    |
| e3    |            7 |         0 | Sperre Zahlenpaar, Baustein \tan |
| e4    |            5 |         0 | Sperre Zahlenpaar                |
| e5    |            1 |         0 | Sperre Zahlenpaar                |

E3: je 3 Sperrtreffer und 3 × \tan, dazu 1 Ergebnisstelle. E4 brauchte
drei Läufe: die erste Korrektur erzeugte 2 neue Sperrtreffer.

## Entscheidungen

- Zone: Fertigkeitszeilen ohne Doppelpunkt (36–39) enden für kette und
  sprosse_text am Gedankenstrich; Folge nach erster Verwendung, bei
  gleicher Einheit in der Folge des Eintrags.
- Zone-Paar zum Fallstrick „x = 0 beim Ausklammern verloren“ in der
  Fertigkeit „Gleichungen lösen“ (häufigstes Muster mit
  Nullprodukt-Belegen).
- E2 hat zwei Verfahrensketten, aber eine Prüfungshöhe: sie steht in
  „Extrempunkte berechnen“ (Originale der Zielmarke); die letzte
  Katalogsprosse von „Extrempunkte nachweisen“ ist dort hoehe sprosse.
- Prüfungshöhe: 2 Zeilen je Original aus Abschnitt 2, das die
  Prüfungssprosse samt fhr-Zielmarke nennt; 2025-C-1d steht schon an
  E2 s4 und wird nicht wiederholt.
- Nennt eine Kettensprosse ein Original aus Abschnitt 2, trägt eine
  Variante es im Feld original; Kennungen außerhalb bleiben null.
- Jeder Haupttyp aus „Typen je Lerneinheit“, den keine Sprosse und
  kein Pflichtelement abdeckt, ist eine Kette ohne Sprossen mit 3
  Zeilen (E2 neun, E3 fünf, E4 zwei, E5 zwei).
- Pflichtelemente: fehler und begruenden überall, anwendung in E1–E3
  und E5, darstellung in E4 und E5; sprosse_text von anwendung und
  darstellung ist ein Typ der Einheit, der damit abgedeckt ist.
- E4 darstellung übt die Rückrichtung (Graph von f' zu Graph von f),
  weil die Kette nur von f nach f' geht.
- pruef bei Term-, Intervall- und Deutungsantworten: die Zahlen an der
  Ergebnisstelle (erste Zahl, nach „=“ oder „≈“), nicht jedes Glied.
- Fehlerregel „zweimal scheitern“ gelesen als: dieselbe Abweichung nach
  zwei Korrekturen; das trat nirgends ein.

## Befunde

- Katalog: Die Erkennungsschritte „Gegeben oder gesucht?“, „Welcher
  Nachweis?“ (E2) und „Was heißt das mathematisch?“ (E5) verlangen
  denselben Handgriff wie die Vorstufen; sie entfallen, der Katalog
  führt beide.
- Katalog: Beide Ketten von E2 haben die Vorstufe „gegeben oder
  gesucht“; beide stehen, mit verschiedenen Aufgaben.
- Katalog: Die Prüfungshöhe von „Extrempunkte nachweisen“ nennt nur
  Kennungen, die nicht in Abschnitt 2 der Mappe stehen.
- Gegenprobe: „Mehrstellige Kastenzahlen in keiner aufgabe“ trifft in
  Sek II Koeffizienten (0,5; 12; 16; 18; 24; 48): 80 Stellen; ohne
  verbogene Aufgaben nicht einhaltbar, die Sperrprobe meldet 0.
- Prüfskript: \tan ist kein erlaubter Befehl, bank.md nennt tan nicht
  bei \mathrm; verwendet ist \mathrm{tan}.
- Prüfskript: Zahlen hinter einem Term oder in einem zweiten Intervall
  liegen nicht an der Ergebnisstelle; pruef deckt dort nur die ersten
  Zahlen.
- Sprossentexte E2 s3 und E5 s1 enden als wortgleicher Ausschnitt mit
  geöffneter Klammer („(ganzrational vierten Grades“).

## Offene Punkte

- Keine Grafik ist kompiliert; \funktionab mit exp und sin (Grad) beim
  Zusammenbau prüfen.
- LK-Aufgaben (Sinus, ln, Punktsymmetrie, Mindestgrad) tragen keine
  Niveaumarke; die Auswahl fürs Blatt muss sie aussortieren.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- e3-k5-s1-v1: pruef gerundet [4.71] → ungerundet [3*math.pi/2] (Regel a).
- e3-k5-s1-v2: pruef gerundet [2.09] → ungerundet [2*math.pi/3] (Regel a).
- e3-k5-s1-v3: pruef gerundet [1.57] → ungerundet [math.pi/2] (Regel a).
- e4-k4-s1-v2: loesung behauptete „ist dort am steilsten“ (aus W und f'(1) = 3 folgt nur ein Extremum von f', möglich auch ein Minimum) → „Der Graph steigt durch $W$ und wechselt dort die Krümmung.“ (Regel a).
- Prüfskript: Abweichungen 0.
