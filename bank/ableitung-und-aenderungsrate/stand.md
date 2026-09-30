# Stand: ableitung-und-aenderungsrate

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/ableitung-und-aenderungsrate.md)
Datum: 2026-09-30 09:08 (date, UTC)
Grundlage: bank.md Stand 2026-09-30b (Erkennungsschritte und
Vorstufen), werkzeuge/bank-pruef.py v0.12, Vorlage auftrag-eintrag.md
2026-09-29e; Nachzug des Stands vom 29.09. (Katalog 2a296e5), Anlass
Katalogänderung 30.09. („Mittel oder Moment?“ vor Einheit 1 und 3) und
neu aufgenommene Originale in Abschnitt 2 der Mappe (68 statt 61).
Endstand: 0 Abweichungen, 0 Warnungen, mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      30         0        14      15        0       1
    e1.jsonl        49         4         5      24        4      12
    e2.jsonl        49         4         5      24        4      12
    e3.jsonl        40         0         5      21        2      12
    e4.jsonl        46         4         5      21        4      12
    gesamt         214        12        34     105       14      49

## Nachzug je Einheit (30.09.)

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         30      0              0          0
    e1           47      0              2          0
    e2           48      0              1          0
    e3           40      0              0          4
    e4           39      0              7          1

Umgeschrieben in e1: s2 v2 und k2 s1 v2 (Uhrzeiten und Werte, weil die
Sperre „15:00“ aus dem neuen Original 2024-bebb-lk-B2.2h meldete;
Verfahren und Ergebnisform gleich). In e2 und e4 nur das Feld original:
e2 s4 v1 (2017MerhoehtAAnalysis12-b), e4 s2 v2 und v3
(2023-bebb-lk-B2.2c), e4 s7 v3 (2026MgrundlegendBAnalysisMMS1-1d),
e4 s8 v1 und v2 (2024-bebb-lk-B2.2h), e4 s9 v1 und v2
(2019-be-gk-B2.1e) – alle waren am 29.09. auf diese Originale
geschrieben und trugen null, weil die Kennungen in der Mappe fehlten.
Entfallen: e3 k1 s0 v1–v4 (Vorstufe „Mittel oder Moment?“, steht in
e1 k1 s0); e4 s9 v1 alt (dritte Zeile ohne Original an der
Prüfungssprosse, Kontext Bäume wie das Original).
ids: e4 s9 v2–v5 → v1–v4; Zeilen mit original, die ein neues Urteil
brauchen: e2-k1-s4-v1, e4-k1-s2-v2, e4-k1-s2-v3, e4-k1-s7-v3,
e4-k1-s8-v1, e4-k1-s8-v2, e4-k1-s9-v1, e4-k1-s9-v2; umbenannt mit
Urteil: e4-k1-s9-v4 → v3, e4-k1-s9-v5 → v4. bank/_punkte.csv nicht
angefasst.

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
  2017MerhoehtAAnalysis12-b (s4); 2023-bebb-lk-B2.2b (s5);
  2021MgrundlegendBAnalysisWTR-2a (s6); 2021-be-gk-B2.1i (s7);
  Prüfung: 2023MerhoehtAAnalysis13-a, 2020MgrundlegendBAnalysisWTR1-1c;
  Typen ohne Kette: 2017MerhoehtBAnalysisWTR1-1b,
  2017MerhoehtBAnalysisWTR2-2b
- e3: 2024MerhoehtBAnalysisWTR1-1b (s3); 2026-bb-gk-B2.2h (s4);
  2022-bebb-gk-B2.2c (s5); 2024MgrundlegendAAnalysis22 (s6);
  2022-bebb-lk-B2.2e (s7); Prüfung: 2025-bebb-lk-A1.6b; Typ ohne
  Kette: 2018MerhoehtBAnalysisCAS2-2c
- e4: 2021MerhoehtAAnalysis13-b, 2023-bebb-lk-B2.2c (s2);
  2019MgrundlegendAAnalysis12-b, 2018-be-gk-B1.2f (s3);
  2019-be-gk-B2.1b, 2026MgrundlegendBAnalysisMMS1-1c (s4);
  2026MerhoehtBAnalysisMMS1-1f, 2026MerhoehtBAnalysisMMS2-1c,
  2025-bebb-lk-B2.1f (s5); 2025MerhoehtBAnalysisMMS1-2a (s6);
  2022-bebb-gk-B2.1m, 2022MgrundlegendBAnalysisWTR2-2d,
  2026MgrundlegendBAnalysisMMS1-1d (s7); 2024-bebb-lk-B2.2h (s8);
  Prüfung: 2019-be-gk-B2.1e, 2026-bb-gk-B2.2i

## Prüfskript vor der Korrektur

- Bestand vom 29.09. gegen die neue Mappe mit `--katalog`:
  2 Abweichungen (e1 2, beide Sperre „15:00“ und „Zahlenpaar 15 von 0“
  aus Original 2024-bebb-lk-B2.2h), 0 Warnungen.
- Nach dem Umbau: 0 Abweichungen, 0 Warnungen in jeder Datei. Keine
  Einheit ist zweimal gescheitert.

## Entscheidungen

1. „Mittel oder Moment?“ (Katalog Z. 39, jetzt „Vor Einheit 1 und 3“)
   steht als Vorstufe in beiden Ketten (Z. 110, 112); nach bank.md
   30.09.b entfällt er als eigene Kette, und die Vorstufenzeilen
   stehen einmal bei der ersten Kette in der Reihenfolge der Datei:
   e1 k1 s0 bleibt, e3 k1 s0 entfällt; e3 k1 beginnt mit dem
   Grundfall s1, keine Nachnummerierung, muster.md unverändert.
2. Die vier e3-Vorstufen fragten an einem Term oder einer Geraden
   (Sekanten- oder Tangentensteigung), die e1-Vorstufen am
   Aufgabentext (Zeitraum oder Zeitpunkt). Gewertet als derselbe
   Handgriff, weil der Katalog beide Ketten auf denselben
   Erkennungsschritt verweist („zu Aufgabentexten ankreuzen“); die
   Termform war eine Abweichung der Bank vom Katalog.
3. Sperre gegen Uhrzeiten (15:00 aus 2024-bebb-lk-B2.2h): die zwei
   e1-Zeilen tragen jetzt andere Uhrzeiten und Werte (9:00 als
   Bezug, 11:00 und 13:00; 13:30 und 17:00); 08:00, 10:00, 14:00 und
   16:00 sind ebenfalls gesperrt und wurden gemieden.
4. Pooldubletten (bank.md 29.09.): 2023-bebb-lk-B2.2c vor
   2023MerhoehtBAnalysisWTR1-1c, 2024-bebb-lk-B2.2h vor
   2024MerhoehtBAnalysisWTR2-2c – die Kennung, die in der Mappe zuerst
   steht.
5. Prüfungssprosse e4 s9 zu 2019-be-gk-B2.1e: von den drei Zeilen ohne
   Original entfällt die erste (zwei Bäume – derselbe Kontext wie das
   Original, keine Verfremdung); die Zeilen Fahrzeuge und Verkaufszahlen
   tragen das Original, die letzte mit Randextremum.
6. Originale mitten in der Kette (e2 s4, e4 s2, s7, s8) nur dort
   gesetzt, wo die Zeile am 29.09. auf dieses Original geschrieben war
   (Verfahren und Falle gleich); e4 s8 v3 (Urteil „Nein“) und e4 s2 v1
   bleiben null.
7. Übernommene Zeilen bleiben wortgleich und ohne Schrittnamen; die
   zwei umgeschriebenen e1-Zeilen behalten ihre Form (Ablesen, P2).

## Befunde

- Prüfskript: Uhrzeiten aus Originaltexten („nach 15:00 Uhr“) werden
  als Gleichung und als Zahlenpaar „15 von 0“ gesperrt; eine Uhrzeit
  ist kein Term. Umgangen durch andere Uhrzeiten.
- Katalog: „Mittel oder Moment?“ ist Vorstufe von E1 (Z. 110) und E3
  (Z. 112); nach bank.md 30.09.b stehen die Zeilen nur bei E1 – der
  Katalog bleibt unverändert (Katalogbefund mit beiden Stellen).
- Katalog: Die Prüfungssprossen von E1, E2, E4 fassen zwei Originale in
  einem Satz; der sprosse_text ist dadurch über 250 Zeichen lang.
- Prüfskript: Die Dublettenregel (bank.md 29.09.) prüft es nicht; eine
  Pooldublette mit beiden Kennungen gäbe weiter keine Warnung.
- Katalog (erledigt): Die am 29.09. fehlenden Kennungen stehen jetzt in
  Abschnitt 2 der Mappe.

## Offene Punkte

- bank/_punkte.csv: acht Zeilen ohne Urteil, zwei umbenannte ids
  (oben) mit werkzeuge/punkte-nachziehen.py nachziehen.
- Kein LaTeX-Lauf; Grafiken nur auf Bausteinname und Bereich geprüft.
- Die Gegenlese vom 28.09. galt dem alten Bestand; die seither neuen
  und umgeschriebenen Zeilen sind ungelesen.
- E3 s4 und E4 s4–s7 verlangen den Rechner; der Text sagt es nicht.
