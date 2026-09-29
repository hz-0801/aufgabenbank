# Stand: ableitung-und-aenderungsrate

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719
(2026-09-28, aus dem Kopf von mappen/ableitung-und-aenderungsrate.md)
Datum: 2026-09-29 19:06 (date, UTC)
Grundlage: bank.md fünfte Fassung (29b), werkzeuge/bank-pruef.py
v0.10, Vorlage auftrag-eintrag.md 2026-09-29e; Nachzug des Bestands
vom 27./28.09. (Katalog 95b0f8b, Gegenlese 28.09.). Umbauskript:
werkzeuge/einmalig/nachzug-ableitung-und-aenderungsrate-2026-09-29.py.
Endstand: 0 Abweichungen, 0 Warnungen, mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      30         0        14      15        0       1
    e1.jsonl        49         4         5      24        4      12
    e2.jsonl        49         4         5      24        4      12
    e3.jsonl        44         4         5      21        2      12
    e4.jsonl        47         4         5      21        5      12
    gesamt         219        16        34     105       15      49

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         30      0              0          0
    e1           35      0             14          0
    e2           35      0             14          0
    e3           27      3             14          2
    e4           33      0             14          2

Übernommen heißt: aufgabe, loesung, merkmal wortgleich; nachgezogen
nur sprosse_text (e1 s10, e2 s8, e4 s9: Prüfungssprossen mit dem
ganzen Katalogtext), sprosse, id und variante (e3 ab s2 eine Sprosse
höher, e4 s9), quelle (e3 k2: 112 → 25).
Umgeschrieben: je Verfahrenskette die fünf Grundfallzeilen
(Päckchen, Lösung mit Schrittnamen), je Einheit alle drei fehler- und
begruenden-Zeilen (merkmal; v2, v3 in neuer Form), eine bis zwei
anwendung-Zeilen (P8), e4 eine darstellung-Zeile (rückwärts), dazu
sechs Zeilen nur im Feld original (Dubletten, unten).
Neu: e3 s2 „Tangente mit dem Lineal anlegen …“ (3, mit grafik).
Entfallen: je zwei Prüfungszeilen in e3 s8 und e4 s9 (Dubletten).
ids von Zeilen mit original: 9 geändert (e3 s2–s7 → s3–s8 sieben,
e3 s7 v4 → s8 v2, e4 s9 v7 → v5), 4 Zeilen mit original entfallen,
6 Zeilen tragen eine andere Kennung; bank/_punkte.csv nicht
angefasst (punkte-nachziehen.py).

## Originale je Einheit

- e1: 2024-bebb-lk-B2.2f, 2025-bebb-gk-B2.2f (s2);
  2019-be-gk-B2.2d, 2017MerhoehtAAnalysis12-a,
  2019MgrundlegendBAnalysisWTR1-1d (s3); 2025-bebb-lk-B2.2h,
  2026MgrundlegendBAnalysisWTR1-2c (s4); 2018-be-gk-B1.2e,
  2024-bebb-lk-B2.1e (s5); 2018-be-gk-B1.2g (s6); 2026-bb-gk-B2.1i
  (s7); 2026MgrundlegendBAnalysisMMS1-1b (s8);
  2024MerhoehtBAnalysisWTR3-1b (s9); Prüfung:
  2018MgrundlegendBAnalysisWTR-2c, 2019MgrundlegendBAnalysisWTR2-2d
- e2: 2026MgrundlegendAAnalysis21-a (s2); 2024-bebb-gk-A1.4a (s3);
  2023-bebb-lk-B2.2b (s5); 2021MgrundlegendBAnalysisWTR-2a (s6);
  2021-be-gk-B2.1i (s7); Prüfung: 2023MerhoehtAAnalysis13-a,
  2020MgrundlegendBAnalysisWTR1-1c; Typen ohne Kette:
  2017MerhoehtBAnalysisWTR1-1b, 2017MerhoehtBAnalysisWTR2-2b
- e3: 2024MerhoehtBAnalysisWTR1-1b (s3); 2026-bb-gk-B2.2h (s4);
  2022-bebb-gk-B2.2c (s5); 2024MgrundlegendAAnalysis22 (s6);
  2022-bebb-lk-B2.2e (s7); Prüfung: 2025-bebb-lk-A1.6b; Typ ohne
  Kette: 2018MerhoehtBAnalysisCAS2-2c
- e4: 2021MerhoehtAAnalysis13-b (s2); 2019MgrundlegendAAnalysis12-b,
  2018-be-gk-B1.2f (s3); 2019-be-gk-B2.1b,
  2026MgrundlegendBAnalysisMMS1-1c (s4); 2026MerhoehtBAnalysisMMS1-1f,
  2026MerhoehtBAnalysisMMS2-1c, 2025-bebb-lk-B2.1f (s5);
  2025MerhoehtBAnalysisMMS1-2a (s6); 2022-bebb-gk-B2.1m,
  2022MgrundlegendBAnalysisWTR2-2d (s7); Prüfung: 2026-bb-gk-B2.2i,
  dazu 3 Zeilen ohne original zu 2019-be-gk-B2.1e

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 18 Abweichungen
  (e1 4, e2 4, e3 3, e4 7), alle „sprosse_text nicht wortgleich in
  Zeile quelle“ (Prüfungssprossen mit zwei Originalen, e3 k2 mit
  quelle 112).
- Erster Wurf des Umbaus: e3 3 Abweichungen (dieselbe e3-k2-Ursache,
  quelle), e1, e2, e4 0; keine Warnung. Keine Einheit ist zweimal
  gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 31–37 unverändert.
2. Päckchen, fester Wert im merkmal: e1 Anfang 120 Liter und
   4 Stunden (Endmenge wandert, einmal fallend), e2 w(t) = t³ − 6t² +
   c·t + 40 an der Stelle 3 (c wandert, Rate positiv, null, negativ),
   e3 x² + c·x an der Stelle 2 (c wandert), e4 r'(t) = (a − t) ·
   e^(−0,5t) (a wandert).
3. e3 Grundfall mit den Schrittnamen aufstellen, umformen, Grenzwert
   (Hinweis des Auftrags); e3 s2 nutzt x² + c·x wie der Grundfall
   (Körperregel), an der Stelle 1.
4. Pooldubletten (bank.md 29.09.): an den Prüfungssprossen e3 s8 und
   e4 s9 ein Original mit zwei Zeilen statt zwei mit je zwei; an
   e1 s2, e2 s3, e2 s5, e3 s4 trägt die Poolzeile die Kennung, die
   in der Mappe zuerst steht.
5. e3 k2 (Typ ohne Kette) trägt quelle 25, weil der Typname nur in
   „Typen je Lerneinheit“ steht (vorher 112).
6. Pflichtformen: fehler v1 Schülerrechnung (Bestand), v2 P2, v3 P1
   (e3: v1 P1, v2 P2, v3 Schülerrechnung); begruenden v1 „Begründe,
   warum“ (Bestand), v2 P4, v3 P6 (e3 und e4: v2 P6, v3 P4). P3
   entfällt: keine Einheit übt eine Umformungskette.
7. Urteile P6: e1 Ja, e2 Nein, e3 Ja, e4 Nein; P8 anwendung: e1 v1,
   v2 Nein, e2 v1 Ja, e3 v1 Nein, e4 v3 Ja.
8. e4 darstellung v1 jetzt rückwärts (Term → Graph); v2, v3 bleiben
   Graph → Punkt und Bestand → Rate.
9. Übernommene Zeilen bleiben ohne Schrittnamen (Auftrag); e1 s1 bis
   e4 s1 und e3 s2 tragen sie.

## Befunde

- Katalog: Die Sprossen von E2 und E4 nennen weiter Originale, die in
  Abschnitt 2 der Mappe fehlen (2019-be-gk-B2.1e, 2023-bebb-lk-B2.2c,
  2023MerhoehtBAnalysisWTR1-1c, 2024-bebb-lk-B2.2h,
  2024MerhoehtBAnalysisWTR2-2c, 2026MgrundlegendBAnalysisMMS1-1d,
  2017MerhoehtAAnalysis12-b); ihre Zeilen tragen original null.
- Katalog: „Mittel oder Moment?“ (Z. 39: „Vor Einheit 1 und 2“) ist
  Vorstufe von E1 und E3 (Z. 110, 112), nicht von E2.
- Katalog: Die Prüfungssprossen von E1, E2, E4 fassen zwei
  Originale in einem Satz; der sprosse_text ist dadurch über 250
  Zeichen lang.
- Prüfskript: Die Dublettenregel (bank.md 29.09.) prüft es nicht;
  eine Pooldublette mit beiden Kennungen gäbe weiter keine Warnung.
- Prüfskript: Ein Typ ohne Kette mit quelle der Kettenzeile fiel erst
  mit `--katalog` auf (e3 k2); ohne den Schalter bleibt es still.

## Offene Punkte

- bank/_punkte.csv: ids nachziehen (9 umbenannt, 4 entfallen,
  6 mit neuer Kennung) mit werkzeuge/punkte-nachziehen.py.
- Kein LaTeX-Lauf; Grafiken nur auf Bausteinname und Bereich
  geprüft.
- Die Gegenlese vom 28.09. galt dem alten Bestand; die neuen und
  umgeschriebenen Zeilen (59) sind ungelesen.
- E3 s4 und E4 s4–s7 verlangen den Rechner; der Text sagt es nicht.
