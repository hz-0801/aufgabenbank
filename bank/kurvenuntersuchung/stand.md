# Stand: kurvenuntersuchung

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719
(2026-09-28, aus dem Kopf von mappen/kurvenuntersuchung.md)
Datum: 2026-09-29 13:47 (date, UTC)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.9,
Vorlage auftrag-eintrag.md 2026-09-29c; Nachzug des Bestands vom
27./28.09. (Katalog 95b0f8b, Gegenlese 28.09.). Umbauskript:
werkzeuge/einmalig/nachzug-kurvenuntersuchung-2026-09-29.py.
Endstand: 0 Abweichungen, 0 Warnungen, mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      29         0        12      16        0       1
    e1.jsonl        39         4         5      15        6       9
    e2.jsonl       113        12        10      75        7       9
    e3.jsonl        63         4         5      39        6       9
    e4.jsonl        49         4         5      27        4       9
    e5.jsonl        52         4         5      27        4      12
    gesamt         345        28        42     199       27      49

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         29      0              0          0
    e1           25      0             14          0
    e2           89      7             17          0
    e3           51      0             12          0
    e4           32      3             14          0
    e5           36      0             16          0

Übernommen heißt: aufgabe, loesung, merkmal wortgleich; nachgezogen
nur quelle (126–131 → 124–129), sprosse, id, sprosse_text (drei
Vorstufen mit längerem Text, Aufgaben gleich) und hoehe (e2 k2 s10).
Umgeschrieben: Päckchen (je Verfahrenskette 5), merkmal und Form der
Pflichtzeilen, drei anwendung-Lösungen (Urteil zuerst).
Neu: e2 k1 s0 „Stelle, Wert oder Punkt?“ (4), e2 k2 s6 „Ändert sich
die Monotonie …“ (3), e4 s4 Übersichtstabelle (3).

## Originale je Einheit

- e1: 2026MgrundlegendBAnalysisWTR1-1a, 2024-bebb-gk-A1.7a,
  2021-be-gk-B2.1g (Prüfung), 2021-A-1c (Prüfung), 2024-C-1d
  (Prüfung)
- e2: 2025-C-1d, 2023-C-1c, 2025-bebb-gk-B2.2b, 2019-be-gk-B2.2b,
  2018-bb-ea-B2.1g, 2021-be-gk-B2.2d (Prüfung), 2026-C-1e
  (Prüfung), 2026MgrundlegendAAnalysis11-a,
  2020MgrundlegendAAnalysis11-a, 2022-bebb-gk-B2.1a,
  2025-bebb-lk-A1.1a, 2021-be-gk-B2.1f, 2026MgrundlegendAAnalysis11-b,
  2025-bebb-gk-B2.1b, 2023MgrundlegendBAnalysisWTR1-1a,
  2018MerhoehtBAnalysisCAS2-1d, 2017-be-gk-cas-B1.1e,
  2023MgrundlegendBAnalysisWTR1-1b
- e3: 2018MgrundlegendBAnalysisWTR-1a, 2024-B-1e, 2023-bebb-gk-B2.1f,
  2021-be-gk-B2.2e (Prüfung), 2026-C-1f (Prüfung), 2020-C-1d
  (Prüfung), 2021MgrundlegendBAnalysisWTR-1b, 2021-A-1d,
  2026MgrundlegendBAnalysisMMS2-1c, 2022MerhoehtBAnalysisWTR1-2c,
  2018MerhoehtAAnalysis12-b, 2017MerhoehtBAnalysisCAS2-2b,
  2018MerhoehtBAnalysisCAS3-2d
- e4: 2020-be-gk-B2.2d, 2023-bebb-lk-A1.1b, 2023-bebb-lk-A1.1a,
  2023MerhoehtAAnalysis11-a, 2024-bebb-gk-B2.1d (Prüfung),
  2023-bebb-gk-B2.2e (Prüfung)
- e5: 2022MgrundlegendBAnalysisWTR2-2c, 2023-C-2a, 2024-C-2d,
  2019-be-gk-B2.2c, 2018-be-gk-B1.1d, 2026-bb-gk-B2.1f,
  2024MgrundlegendBAnalysisWTR2-2c (Prüfung), 2021-B-2d (Prüfung),
  2017-be-gk-B1.1c, 2024MerhoehtBAnalysisWTR3-1c,
  2018MgrundlegendBAnalysisWTR-2e, 2018MerhoehtBAnalysisWTR1-2d

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 204 Abweichungen
  (e1 30, e2 70, e3 39, e4 31, e5 34), alle „sprosse_text nicht
  wortgleich in Zeile quelle“ (Katalogzeilen um zwei verschoben).
- Erster Wurf je Einheit: e1, e2, e3, e5 je 0; e4 2 Abweichungen
  (Sperre Zahlenpaar (2|0), (0|1), (1|2) aus Originalen in der
  neuen Sprosse s4); beim zweiten Wurf 0. Warnungen durchweg 0.
  Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 34–39 unverändert.
2. Päckchen, fester Wert im merkmal: e1 die Ableitung 2x − 6 (das
   Intervall wandert), e2 k1 x³/3 − 2x² (Faktor vor x wandert,
   Lösungen 2 ± r), e2 k2 Stelle 2 und x³ − 12x (Faktor davor
   wandert), e3 x³ und −5x (Faktor vor x² wandert), e4 dieselbe
   Kurve dritten Grades (verschoben), e5 Raumtemperatur 20 °C
   (Anfangstemperatur wandert).
3. e2 k2: die letzte Katalogsprosse (Logarithmus, allgemeine
   Aussagen) ist jetzt hoehe pruefung, original null, 3 Zeilen –
   bank.md verlangt je Verfahrenskette eine Prüfungshöhe; die
   Kennungen der Sprosse stehen nicht in Abschnitt 2 der Mappe.
4. Die neue Katalogsprosse e2 k2 „Ändert sich die Monotonie …“ steht
   als Sprosse 6 mit 3 Zeilen: Ankreuzen am Graphen, aber mitten in
   der Kette, also keine Vorstufe.
5. Neue Sek-II-Lösungen tragen Schrittnamen („Ableitung bilden:“,
   „Bedingung f''(x) = 0:“); das Urteil steht vorn, die Einsetzung
   in derselben Zeile.
6. P1 (Serie) in allen Einheiten statt P3, weil keine Einheit eine
   Umformungskette von Gleichungen übt.
7. P8 je Einheit eine Grenzwert-Entscheidung (Werbeaktion 7 Wochen,
   Mast unter Kabel, Achterbahn 3 m, Rampe 30°, Rutsche 45°); e4 hat
   kein anwendung, dort entfällt P8.
8. e4 darstellung: v1 vorwärts (f → f'), v2 und v3 rückwärts
   (f' → f); e5 darstellung: v1/v2 Graph → Bereich, v3 Worte → Graph.
9. Urteile (erstes Wort der Pflichtlösungen): 5 Ja, 5 Nein, 5
   Richtig (P2), 1 wahr, 1 falsch; P6 viermal Nein, einmal Ja,
   P8 viermal Ja, einmal Nein.

## Befunde

- Katalog: „Gegeben oder gesucht?“ (Z. 41) verlangt denselben
  Handgriff wie die Vorstufen s−1 von e2 k1 und s0 von e2 k2; der
  Erkennungsschritt entfällt, der Katalog führt beide.
- Katalog: Die Sprosse „Ändert sich die Monotonie …“ enthält „→“,
  das zugleich die Sprossen der Kette trennt; wer die Kette an „→“
  teilt, zerschneidet sie in drei Stücke.
- Katalog: Die Prüfungshöhe von „Extrempunkte nachweisen“ nennt nur
  Kennungen, die nicht in Abschnitt 2 der Mappe stehen.
- Prüfskript: Die Sperre trifft kleine Punkte wie (2|0), (0|1),
  (1|2) aus Originalen; bei Übersichten einfacher Kubiken sind das
  die natürlichen Werte – eigene Zahlen gewählt, ohne Verbiegung.
- Prüfskript: \tan fehlt in STANDARD; weiter \mathrm{tan} verwendet.

## Offene Punkte

- Keine Grafik ist kompiliert; \sachtabelle in aufgabe (e4 s4) und
  \funktionab mit exp beim Zusammenbau prüfen.
- LK-Aufgaben (Sinus, ln, Punktsymmetrie, Mindestgrad) tragen keine
  Niveaumarke; die Auswahl fürs Blatt muss sie aussortieren.
- Die Gegenlese vom 28.09. galt dem alten Bestand; die neuen und
  umgeschriebenen Zeilen (69) sind ungelesen.
- Übernommene Zeilen tragen keine Schrittnamen (Auftrag).

## Nachbesserung 2026-09-30

- Teil 1, Antwortgerüst: 14 Zeilen (zone.jsonl 14) –
  im Feld antwort `\leerfeld[X]` → `__ X` und `\leerfeld` → `__`,
  weil bank.md (Feld antwort) das Gerüst „__“ vorschreibt; alle
  Zeilen dieser Dateien mit `\leerfeld` in antwort, ids über
  `git show` des Commits oder das Skript
  werkzeuge/einmalig/leerfeld-antwort-2026-09-30.py.
- Teil 3, „Begründe, ohne genau zu rechnen“ – je Einheit die
  P6-Zeile umgeschrieben
  (bank.md: eine begruenden-Zeile je Einheit ohne Rechnung
  entscheidbar); P6 bleibt, Urteil unverändert.
  - kurvenuntersuchung-e2-k12-s2-v3: $f'(x) = 3(x-2)^2$ vorgegeben, Urteil
    über das Vorzeichen des Quadrats.
  - kurvenuntersuchung-e3-k7-s2-v3: Urteil über das Vorzeichen von $f''$
    (Vielfaches von $x^2$), ohne $f''$ auszurechnen.
  - kurvenuntersuchung-e4-k4-s2-v3: Hochpunkt $H(2 | 4)$ von $f'$
    vorgegeben, Urteil über $f'(2) > 0$.
  - kurvenuntersuchung-e5-k4-s2-v3: Zuwächse 12, 8, 5 cm und $h$, $t$
    erklärt, Urteil über Monotonie der Zuwächse.
