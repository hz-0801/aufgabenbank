# Stand: tangente-normale-schnittwinkel

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/tangente-normale-schnittwinkel.md)
Datum: 2026-09-30 08:53 (date, UTC)
Grundlage: bank.md 2026-09-30b, werkzeuge/bank-pruef.py v0.9,
Vorlage auftrag-eintrag.md 2026-09-29e; Nachzug 30.09. des Stands
vom 29.09. (Katalog f038ccb; Abschnitt „Nachzug 2026-09-30“ unten).
Endstand: 0 Abweichungen, 0 Warnungen, Formprobe 0, mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      26         0        12      13        0       1
    e1.jsonl        59         8         5      30       10       6
    e2.jsonl        51         4         5      30        6       6
    e3.jsonl        36         4         5      15        6       6
    e4.jsonl        52         8         5      27        6       6
    e5.jsonl        39         4         5      18        6       6
    gesamt         263        28        37     133       34      31

## Nachzug je Einheit (29.09., Katalog f038ccb)

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         26      0              0          0
    e1           40      8             11          0
    e2           40      0             11          0
    e3           19      4             13          0
    e4           37      4             11          0
    e5           28      0             11          0

Übernommen heißt: aufgabe, loesung, merkmal wortgleich; nachgezogen
nur quelle (120–124 → 117–121), sprosse (e1 und e4: s0 → s−1), id
und sprosse_text (Vorstufen jetzt mit dem ganzen Katalogtext).
Umgeschrieben: je Verfahrenskette die fünf Grundfallzeilen
(Päckchen), je Einheit zwei fehler- und zwei begruenden-Zeilen
(Formen), in e3 dazu merkmal der zwei Prüfungszeilen.
Neu: e1 s0 „nur den Anstieg“ (4), e1 s10 vier Originalzeilen, e3 s7
vier Originalzeilen, e4 s0 „Welcher Winkel?“ (4).
Die ids von Zeilen mit original sind unverändert (0 geändert); acht
neue Zeilen mit original (e1 s10 v7–v10, e3 s7 v3–v6) haben noch
keine Zeile in bank/_punkte.csv.

## Originale je Einheit

- e1: 2025-bebb-gk-A1.1a, 2020-A-1d, 2026-C-1d, 2021-B-2a,
  2026-bb-gk-B2.2b, 2019-be-gk-B2.2f, 2018MgrundlegendAAnalysis12-a,
  2018-bb-ea-cas-B2.2d, 2023-bebb-gk-B2.1c, 2024-bebb-lk-A1.5a,
  2025-bebb-lk-A1.6a, 2023-bebb-gk-A1.1a,
  2017MerhoehtBAnalysisWTR3-2e, 2018MerhoehtBAnalysisCAS3-1d,
  2017MerhoehtBAnalysisWTR2-1f; Prüfung: 2024-bebb-lk-A1.5b,
  2024MerhoehtAAnalysis21-b, 2017-bb-ea-B2.1c, 2019-C-1f, 2026-C-1d
- e2: 2026-B-1g, 2019-A-2b, 2018-be-gk-cas-B1.1e, 2023-bebb-gk-B2.2d,
  2025-C-1f, 2017MerhoehtBAnalysisCAS2-2c,
  2020MgrundlegendBAnalysisWTR2-1c, 2018-bb-ea-cas-B2.1f,
  2017MerhoehtBAnalysisCAS2-2d, 2018MerhoehtBAnalysisCAS1-4,
  2017MerhoehtBAnalysisWTR1-1c, 2018MerhoehtBAnalysisCAS3-2f;
  Prüfung: 2025MerhoehtBAnalysisMMS2-2d,
  2019MgrundlegendBAnalysisWTR1-2a, 2026-B-1g
- e3: 2022-B-1f, 2023-A-1c, 2025-A-1h, 2024MerhoehtBAnalysisWTR3-1d,
  2026-bb-ea-B2.2e; Prüfung: 2023MerhoehtBAnalysisWTR2-2d,
  2022-B-1f, 2025-A-1h
- e4: 2018MerhoehtBAnalysisWTR2-1f, 2017MerhoehtBAnalysisWTR3-2f,
  2020-be-gk-B2.1f, 2026MgrundlegendBAnalysisWTR1-1c,
  2023MgrundlegendBAnalysisWTR1-1c, 2026MerhoehtBAnalysisWTR2-2c,
  2023MerhoehtBAnalysisWTR2-1d, 2025MerhoehtBAnalysisMMS2-2b,
  2018-be-gk-B1.2b, 2022-bebb-gk-B2.1e, 2017-be-gk-B1.1e,
  2026-bb-ea-A1.2b, 2026MerhoehtAAnalysis11-b,
  2018MerhoehtBAnalysisCAS1-3b, 2017-be-gk-cas-B1.2f,
  2017MerhoehtBAnalysisWTR3-2g; Prüfung: 2026-bb-ea-B2.1d,
  2024-bebb-gk-B2.1i, 2025-bebb-gk-B2.1d
- e5: 2026-B-1h, 2018-bb-ea-B2.2b, 2017-be-gk-B1.2e,
  2022-bebb-gk-B2.1g, 2017-bb-ea-cas-B2.1c, 2017-bb-ea-A1.1b,
  2018-bb-ea-A1.1b, 2019MgrundlegendAAnalysis2-b, 2021-be-gk-B2.2f,
  2022MerhoehtBAnalysisWTR1-1d; Prüfung: 2024MerhoehtAAnalysis22,
  2024-bebb-lk-B2.1f, 2024-C-1g

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 169 Abweichungen
  (e1 35, e2 36, e3 26, e4 39, e5 33), alle „sprosse_text nicht
  wortgleich in Zeile quelle“ (Katalogzeilen um drei verschoben);
  4 Warnungen in e1 (2024-bebb-lk-A1.5b und
  2024MerhoehtAAnalysis21-b je 1× statt 2×).
- Erster Wurf je Einheit: 0 Abweichungen, 0 Warnungen. Die eigene
  Punktprobe (Punkte mit Semikolon aus den Originalen) fand im
  ersten Wurf von e3 den Grundfallpunkt (4 | 1) aus
  2025-bebb-gk-A1.1a; e3 neu geschrieben mit P(4 | 3), dann 0.
  Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 34–39 unverändert.
2. Päckchen, fester Wert im merkmal: e1 Stelle 1 an x³ + c·x² − 2
   (c wandert), e2 Stelle 1 an x³ + c·x − 1 (c wandert, 3 Ja,
   2 Nein), e3 Punkt P(4 | 3) (Tangentensteigung wandert), e4 Punkt
   P(1 | 2) (spitz, stumpf, 90° nach den Urteilen vom 28.09.), e5
   y-Achsenabschnitt 6 (Steigung wandert).
3. e1 s0 „nur den Anstieg“ nutzt denselben Term wie der Grundfall an
   der Stelle −1 (Körperregel: derselbe Term trägt Vorstufe und
   Grundfall).
4. Die Prüfungssprosse von e1 trägt jetzt alle fünf Originale der
   Katalogzeile je zweimal; die Pooldublette 2024-bebb-lk-A1.5b /
   2024MerhoehtAAnalysis21-b zählt als zwei Kennungen (Entscheidung
   5 vom 27.09. aufgehoben, weil das Prüfskript je Kennung 2 will).
5. e3 s7 trägt die fhr-Zielmarken 2022-B-1f und 2025-A-1h je zweimal
   (neu), obwohl beide auch an s2 stehen – bank.md: alle Originale
   der Katalogzeile an der einen Prüfungssprosse.
6. Pflichtformen je Einheit: fehler v1 Schülerrechnung (Bestand), v2
   P2 fehlerfrei, v3 P1 Serie; begruenden v1 „Begründe, warum“
   (Bestand), v2 P4 Aussagenserie, v3 P6 Personenaussage. P3
   entfällt, weil keine Einheit eine Umformungskette übt.
7. Urteile der P6-Zeilen: e1, e2, e4 Nein, e3, e5 Ja.
8. darstellung und anwendung gibt es weiter nicht: „Typen je
   Lerneinheit“ nennt als Pflicht nur Fehler finden und Begründen.
9. \tan bleibt \mathrm{tan}, \iff bleibt \Leftrightarrow.

## Befunde

- Katalog: Die Vorstufe s−1 von e1 und e4 („Was ist gegeben?“) ist
  wortgleich dieselbe; die Ankreuzzeilen sind verschieden, aber der
  Handgriff ist derselbe.
- Katalog: e2 bis e5 bleiben bei einer Vorstufe; nur e1 hat die
  Anstiegsvorstufe, obwohl e3 (Normale) denselben Schritt f'(x₀)
  vor dem negativen Kehrwert braucht.
- Prüfskript: Die Sperre erkennt Punkte in der Schreibweise der
  Originale „(4; 1)“ nicht, nur „(4 | 1)“; die eigene Probe fand
  (4 | 1) aus 2025-bebb-gk-A1.1a im ersten Wurf von e3. Im Bestand
  stehen weiter (2 | 0) (e2 s8 v1, e4 s10 v5–v6), (3 | 1) (e2 k4
  v3) und (4 | 1) (e3 s3 v1) – übernommene Zeilen, nicht geändert.
- Prüfskript: \tan fehlt in STANDARD.
- bank.md: tan fehlt in der Regel „sin, cos, ln als \mathrm{…}“.

## Offene Punkte

- bank/_punkte.csv: acht neue Zeilen mit original ohne Urteil
  (e1 s10 v7–v10, e3 s7 v3–v6).
- Kein LaTeX-Lauf; Grafiken nur auf Bausteinname und Bereich
  geprüft.
- Übernommene Zeilen tragen keine Schrittnamen (Auftrag).
- Die Gegenlese vom 28.09. galt dem alten Bestand; die neuen und
  umgeschriebenen Zeilen (73) sind ungelesen.
- Ohne Zeile bleiben weiter die Originale, die nur außerhalb von
  „Prüfungsform“ stehen (Mappe, Abschnitt 2, Schluss).

## Nachbesserung 2026-09-30

- Teil 3, „Begründe, ohne genau zu rechnen“ – P6-Zeile umgeschrieben
  (bank.md: eine begruenden-Zeile je Einheit ohne Rechnung
  entscheidbar); P6 bleibt, Urteil unverändert.
  - tangente-normale-schnittwinkel-e4-k3-s2-v3: Urteil über die
    Größenordnung (beide Winkel zwischen 45° und 90°) statt über
    $\mathrm{tan}^{-1}$-Werte.

## Nachzug 2026-09-30 (Katalog db8d2a3)

Anlass: Katalogzeile „Änderungen 2026-09-30“ – Einheit 4 nur noch
mit der Vorstufe „Welcher Winkel?“, Einheit 3 mit der zweiten
Vorstufe „nur die Normalensteigung“; dazu mehr Originale in
Abschnitt 2 der Mappe (146).

Prüfskript vorher, Bestand vom 29.09. gegen die neue Mappe mit
`--katalog`: 11 Abweichungen, 0 Warnungen, Formprobe 0 – e4 4×
„sprosse_text nicht wortgleich in Zeile 120“ (die gestrichene
Vorstufe), 7× Sperre gegen Terme aus neu aufgenommenen Originalen
(zone 1, e1 1, e2 2, e3 1, e4 1, e5 1: x² − 2x − 8 aus
2025MgrundlegendAAnalysis11-b, x³ − 4x aus 2024-bebb-lk-B2.2c,
−x² + 4x − 1 aus 2025-bebb-gk-A1.7b, ½x² aus
2024MgrundlegendAAnalysis21-a). Nachher: 0 / 0 / 0.

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         25      0              1          0
    e1           58      0              1          0
    e2           49      0              2          0
    e3           35      4              1          0
    e4           47      0              1          4
    e5           38      0              1          0

Umgeschrieben heißt hier: nur die Zahlen (Term, Punkt, Ergebnis),
Sprosse, Form und Rechenweg unverändert. Neu: e3 s0 „nur die
Normalensteigung“ (4 Zeilen, derselbe Punkt P(4 | 3) und dieselben
Tangentensteigungen 2, −2, 4, −1 wie im Grundfall v1–v4); die alte
Vorstufe „Tangente oder Normale?“ ist jetzt s−1 (ids e3-k1-s0-v1–4
→ e3-k1-s-1-v1–4, ohne original). Entfallen: e4 s−1 „Was ist
gegeben?“ (4 Zeilen); die Kette beginnt mit s0 „Welcher Winkel?“.
Grundfälle, muster.md und die Pflichtformen unverändert.

Entscheidungen 30.09.:
10. Die neue Vorstufe e3 s0 trägt den Punkt des Grundfalls und
    fragt nur die Steigung (Antwortgerüst m_n = __), form teil,
    pruef die Zahl – Vorstufe und Grundfall am selben Körper.
11. Zwei Zeilen mit original sind nur in den Zahlen umgeschrieben
    (e3-k1-s6-v1 mit 2026-bb-ea-B2.2e, e4-k1-s10-v6 mit
    2025-bebb-gk-B2.1d); `punkte-nachziehen.py 1c561b3` würde ihre
    Zeilen in bank/_punkte.csv als „Aufgabe geändert“ streichen
    (umbenannt 0, weil keine id mit original umbenannt wurde).
    bank/_punkte.csv ist nicht geändert: Umfang und Handlung sind
    dieselben, das Urteil „ganz“ gilt sachlich weiter; ob die zwei
    Zeilen neu beurteilt werden, entscheidet der Chat.

Befunde 30.09.:
- Der Katalogbefund vom 29.09. (Vorstufe „Was ist gegeben?“ in e1
  und e4 wortgleich) ist mit db8d2a3 erledigt; e4 hat nur noch
  „Welcher Winkel?“. Der zweite Befund (Anstiegsvorstufe fehlte
  in e3) ist mit „nur die Normalensteigung“ ebenfalls erledigt.
- Sperre: Die vier Terme aus neu aufgenommenen Originalen trafen
  Zeilen, die vor dem 30.09. sauber waren; jeder Mappenbau mit
  mehr Originalen kann so Bestandszeilen kippen. Kein Fehler, aber
  ein Grund, das Prüfskript nach jedem Mappenbau zu laufen.

Offen 30.09.: bank/_punkte.csv für die zwei umgeschriebenen
Originalzeilen (Entscheidung 11); die acht Zeilen ohne Urteil vom
29.09. bleiben.
