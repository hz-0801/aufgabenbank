# Stand: kurvenuntersuchung

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/kurvenuntersuchung.md)
Datum: 2026-09-30 08:58 (date, UTC)
Grundlage: bank.md Stand 2026-09-30b, werkzeuge/bank-pruef.py v0.9
(--katalog), Vorlage auftrag-eintrag.md 2026-09-29e; Nachzug des
Bestands vom 29.09. (Katalog 2a296e5, Bank-Commit 1c561b3) um die
Katalogänderung vom 30.09. (Zeile 151: Sprosse „Ändert sich die
Monotonie …“ ohne Pfeile), die Regel zu Erkennungsschritten (bank.md
30.09.b) und die Originale, die die Mappe seit dem 30.09. in
Abschnitt 2 führt.
Endstand: 0 Abweichungen, 0 Warnungen, Formprobe 0 Hinweise.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      29         0        12      16        0       1
    e1.jsonl        41         4         5      15        8       9
    e2.jsonl       114         8        10      75       12       9
    e3.jsonl        69         8         5      39        8       9
    e4.jsonl        49         4         5      27        4       9
    e5.jsonl        56         4         5      27        8      12
    gesamt         358        28        42     199       40      49

## Nachzug je Einheit (30.09.)

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         29      0              0          0
    e1           39      2              0          0
    e2          106      5              3          4
    e3           63      6              0          0
    e4           49      0              0          0
    e5           52      4              0          0

Übernommen heißt: aufgabe, loesung, merkmal wortgleich; nachgezogen
nur sprosse_text (e2 k2 s6, drei Zeilen: Doppelpunkte statt Pfeile)
und id samt kette_nr (e3: alle Ketten um eins verschoben, k1–k7 →
k2–k8, weil der Erkennungsschritt k1 wurde).
Neu: e1 k1 s7 v7–v8 (2023MgrundlegendBAnalysisWTR2-2d); e2 k1 s10
v5–v6 (2025-C-1d); e2 k2 s10 v4 (2020-C-1c), v5–v6 (2019-A-1c);
e3 k1 s0 v1–v4 (Erkennungsschritt „Gegeben oder gesucht?“, Zeile
41); e3 k2 s10 v7–v8 (2019MerhoehtAAnalysis2-b); e5 k1 s9 v5–v6
(2023MgrundlegendBAnalysisWTR2-2b), v7–v8 (2025MerhoehtBAnalysisMMS1-2b).
Umgeschrieben: e2 k2 s10 v1–v2 (nur original 2023-bebb-lk-A1.2b und
Prüfkennung nachgetragen, Aufgabe sonst gleich), v3 (auf 2020-C-1c
umgeschrieben: drei Aussagen und Rechnung).
Entfallen: e2 k2 s0 („gegeben oder gesucht“ ankreuzen, vier Zeilen)
– derselbe Handgriff wie e2 k1 s−1 (bank.md, Erkennungsschritte und
Vorstufen); k2 beginnt mit dem Grundfall.

## Originale je Einheit

- e1: 2026MgrundlegendBAnalysisWTR1-1a, 2024-bebb-gk-A1.7a,
  2021-be-gk-B2.1g (Prüfung), 2021-A-1c (Prüfung), 2024-C-1d
  (Prüfung), 2023MgrundlegendBAnalysisWTR2-2d (Prüfung)
- e2: 2025-C-1d (s4 und Prüfung), 2023-C-1c, 2025-bebb-gk-B2.2b,
  2019-be-gk-B2.2b, 2018-bb-ea-B2.1g, 2021-be-gk-B2.2d (Prüfung),
  2026-C-1e (Prüfung), 2026MgrundlegendAAnalysis11-a,
  2020MgrundlegendAAnalysis11-a, 2022-bebb-gk-B2.1a,
  2025-bebb-lk-A1.1a, 2023-bebb-lk-A1.2b (Prüfung), 2020-C-1c
  (Prüfung), 2019-A-1c (Prüfung), 2021-be-gk-B2.1f,
  2026MgrundlegendAAnalysis11-b, 2025-bebb-gk-B2.1b,
  2023MgrundlegendBAnalysisWTR1-1a, 2018MerhoehtBAnalysisCAS2-1d,
  2017-be-gk-cas-B1.1e, 2023MgrundlegendBAnalysisWTR1-1b
- e3: 2018MgrundlegendBAnalysisWTR-1a, 2024-B-1e, 2023-bebb-gk-B2.1f,
  2021-be-gk-B2.2e (Prüfung), 2026-C-1f (Prüfung), 2020-C-1d
  (Prüfung), 2019MerhoehtAAnalysis2-b (Prüfung),
  2021MgrundlegendBAnalysisWTR-1b, 2021-A-1d,
  2026MgrundlegendBAnalysisMMS2-1c, 2022MerhoehtBAnalysisWTR1-2c,
  2018MerhoehtAAnalysis12-b, 2017MerhoehtBAnalysisCAS2-2b,
  2018MerhoehtBAnalysisCAS3-2d
- e4: 2020-be-gk-B2.2d, 2023-bebb-lk-A1.1b, 2023-bebb-lk-A1.1a,
  2023MerhoehtAAnalysis11-a, 2024-bebb-gk-B2.1d (Prüfung),
  2023-bebb-gk-B2.2e (Prüfung)
- e5: 2022MgrundlegendBAnalysisWTR2-2c, 2023-C-2a, 2024-C-2d,
  2019-be-gk-B2.2c, 2018-be-gk-B1.1d, 2026-bb-gk-B2.1f,
  2024MgrundlegendBAnalysisWTR2-2c (Prüfung), 2021-B-2d (Prüfung),
  2023MgrundlegendBAnalysisWTR2-2b (Prüfung),
  2025MerhoehtBAnalysisMMS1-2b (Prüfung), 2017-be-gk-B1.1c,
  2024MerhoehtBAnalysisWTR3-1c, 2018MgrundlegendBAnalysisWTR-2e,
  2018MerhoehtBAnalysisWTR1-2d

## Prüfskript vor der Korrektur

- Bestand gegen die Mappe db8d2a3 mit `--katalog`: 3 Abweichungen
  (e2 3, alle „sprosse_text nicht wortgleich in Zeile 126“ – die
  Sprosse mit den Doppelpunkten), 0 Warnungen, Formprobe 0.
- Erster Wurf je Einheit: e1 0, e2 0, e3 1 („pruef fehlt“ bei der
  Nein-Antwort v8, Lösung ohne Ergebniszahl; zweiter Wurf 0), e5 0.
  Warnungen durchweg 0. Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 34–39 unverändert.
2. Der Erkennungsschritt „Gegeben oder gesucht?“ (Z. 41, „vor
   Einheit 2 und 3“) steht in e3 als k1 s0 mit vier Zeilen: e2 hat
   Vorstufen mit demselben Handgriff (k1 s−1), e3 nur „welcher
   Nachweis“ (bank.md 30.09.b). Die Texte fragen nach Wendepunkten
   und einem Sachzusammenhang, damit der Schritt in e3 trägt.
3. e2 k2 s0 („gegeben oder gesucht“ ankreuzen) entfällt: derselbe
   Handgriff wie e2 k1 s−1; nach bank.md stehen die Zeilen einmal,
   bei der ersten Kette, die zweite beginnt mit dem Grundfall.
4. 2025-C-1d durchläuft e1 (Monotonie-Anhang) und e2 (Extrempunkte
   mit Sattelpunkt): die zwei Prüfungszeilen stehen in e2 k1 s10,
   in e1 nicht (bank.md, Original über zwei Einheiten); die Zeile
   e2 k1 s4 v1 mit demselben Original bleibt (Verfremdung mitten in
   der Kette).
5. e2 k2 s10: die drei Originale der Katalogzeile stehen jetzt in
   Abschnitt 2 der Mappe; die zwei ln-Zeilen sind übernommen und
   tragen 2023-bebb-lk-A1.2b, die Aussagenzeile wurde zu 2020-C-1c
   (drei Aussagen plus Rechnung an eigener Funktion), 2019-A-1c neu
   mit zwei Funktionen (einmal Sattelstelle, einmal nicht).
6. Nur Prüfungssprossen (hoehe pruefung) erhalten neue Originale;
   Sprossen mitten in der Kette, deren Original neu in der Mappe
   steht, bleiben ohne Feld original (Auftrag: Prüfungssprossen).
7. Neue Lösungen tragen Schrittnamen („Ableitung bilden:“, „Bedingung
   f''(x₀) ≠ 0:“, „Kettenregel:“); Urteile stehen vorn (Ja/Nein,
   wahr/falsch je Aussage).
8. Frühere Entscheidungen vom 29.09. (Päckchen, P1 statt P3, P8 je
   Einheit, Urteilsverteilung) gelten fort; siehe git-Stand 1c561b3.

## Befunde

- Katalog: „Gegeben oder gesucht?“ (Z. 41) und die Vorstufen e2 k1
  s−1 (Z. 125) und e2 k2 s0 (Z. 126) verlangen denselben Handgriff;
  die Bank hält ihn in e2 einmal (k1 s−1) und legt den
  Erkennungsschritt in e3 an – dort, wo er am wenigsten gebraucht
  wird, weil e3 keine „gegeben oder gesucht“-Vorstufe hat. Ob die
  Regel „erste Einheit ohne solche Vorstufe“ hier das Richtige trifft,
  entscheidet der Chat; der Katalog bleibt unverändert.
- Katalog: e1 (Z. 124) und e2 (Z. 125) nennen beide 2025-C-1d als
  Zielmarke; die Bank führt es einmal an der Prüfungssprosse von e2.
- Katalog: e2 k1 s−1 (Z. 125) bündelt zwei Handgriffe („gegeben oder
  gesucht“ und „welcher Nachweis“) in einer Vorstufe; „welcher
  Nachweis“ steht in e3 (Z. 127) noch einmal als Vorstufe.
- Prüfskript: eine Nein-Antwort ohne Ergebniszahl („hat keinen
  Wendepunkt“) verlangt pruef; gelöst mit „Anzahl 0“ in der Lösung.
- Prüfskript: \tan fehlt in STANDARD; weiter \mathrm{tan} verwendet.

## Offene Punkte

- Keine Grafik ist kompiliert; \sachtabelle in aufgabe (e4 s4),
  \funktionab mit exp und die neuen Grafiken e3 k2 s10 v7–v8 beim
  Zusammenbau prüfen.
- LK-Aufgaben (Sinus, ln, Punktsymmetrie, Mindestgrad, e^g) tragen
  keine Niveaumarke; die Auswahl fürs Blatt muss sie aussortieren.
- Die neuen und umgeschriebenen Zeilen (vom 29.09.: 69; vom 30.09.:
  20) sind ungelesen; Gegenlese offen.
- Übernommene Zeilen tragen keine Schrittnamen (Auftrag).
- bank/_punkte.csv: Zeilen mit ids aus e3 sind umbenannt
  (punkte-nachziehen.py); die neuen Zeilen mit original brauchen ein
  Urteil (punkte.py --lesestoff --nur-neu).

## Nachbesserung 2026-09-30 (vor dem Nachzug)

- Teil 1, Antwortgerüst: 14 Zeilen (zone.jsonl 14) –
  im Feld antwort `\leerfeld[X]` → `__ X` und `\leerfeld` → `__`
  (bank.md, Feld antwort); Skript
  werkzeuge/einmalig/leerfeld-antwort-2026-09-30.py.
- Teil 3, „Begründe, ohne genau zu rechnen“ – je Einheit die
  P6-Zeile umgeschrieben; P6 bleibt, Urteil unverändert:
  kurvenuntersuchung-e2-k12-s2-v3, kurvenuntersuchung-e3-k8-s2-v3
  (vor dem Nachzug e3-k7-s2-v3), kurvenuntersuchung-e4-k4-s2-v3,
  kurvenuntersuchung-e5-k4-s2-v3.
