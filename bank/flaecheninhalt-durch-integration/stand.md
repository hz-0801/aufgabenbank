# Stand: flaecheninhalt-durch-integration

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf der Mappe
mappen/flaecheninhalt-durch-integration.md)
Datum: 2026-09-30 08:58 UTC (date)
Grundlage: bank.md Stand 2026-09-30b, werkzeuge/bank-pruef.py
(--katalog aus der Mappe), Vorlage auftrag-eintrag.md 29e; Nachzug
des Stands vom 29.09. (Katalog 2a296e5) nach den Katalogänderungen
vom 30.09. (Zeile 127: Vorstufe der Einheit 4 in der Form der
Nachbarketten) und der Mappe mit 148 Originalen.
Endstand: 0 Abweichungen, 0 Warnungen, Formprobe 0, mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      26         0        12      13        0       1
    e1.jsonl        36         4         5      12        6       9
    e2.jsonl        41         4         5      15        8       9
    e3.jsonl        47         4         5      12       14      12
    e4.jsonl        36         4         5      12        6       9
    e5.jsonl        53         4         5      18       14      12
    gesamt         239        20        37      82       48      52

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         26      0              0          0
    e1           36      0              0          0
    e2           37      4              0          0
    e3           39      8              0          0
    e4           30      2              4          0
    e5           51      2              0          0

Übernommen heißt: Zeile wortgleich, auch quelle und sprosse_text
(die Katalogzeilen 102–106 sind unverändert). Umgeschrieben: die
vier Vorstufenzeilen der Einheit 4 (sprosse_text nach Zeile 105,
drei Ankreuzoptionen statt zwei, merkmal). Neu: je zwei Zeilen zu
den Originalen, die die Mappe seit dem 30.09. führt, alle an der
Prüfungssprosse der Kette (e2 s7 v5–v8, e3 s6 v7–v14, e4 s6 v5–v6,
e5 s8 v13–v14). Keine id ist umbenannt.

## Originale je Einheit

- e1: 2024-bebb-lk-B2.1k, 2017MerhoehtAAnalysis2-a, 2021-B-1f
- e2: 2025MerhoehtBAnalysisMMS1-1d, 2023-C-2d, 2026-bb-gk-B2.2d
  (Pooldublette von 2026MgrundlegendBAnalysisWTR2-1d, Kennung der
  Mappe zuerst), 2025-bebb-lk-B2.1e
- e3: 2024-bebb-gk-B2.2e, 2020-be-gk-B2.2g, 2025-C-2c,
  2026MgrundlegendBAnalysisMMS2-1f, 2020MgrundlegendBAnalysisWTR1-1f,
  2022-bebb-gk-B2.2i, 2025MerhoehtBAnalysisWTR2-1e
- e4: 2025MgrundlegendBAnalysisWTR1-1d, 2026MerhoehtBAnalysisMMS2-2e,
  2026MerhoehtBAnalysisWTR3-1c
- e5: 2025-bebb-lk-B2.1d, 2025MerhoehtBAnalysisMMS1-1c,
  2025MerhoehtBAnalysisWTR2-1d, 2019MgrundlegendBAnalysisWTR1-2e,
  2024-bebb-lk-B2.1j, 2024MerhoehtBAnalysisWTR1-1f,
  2019MgrundlegendBAnalysisWTR1-3d

Alle an der letzten Sprosse der Kette (hoehe pruefung), je 2 Zeilen.
Die neun Kennungen, die am 29.09. ohne Zeile blieben, sind jetzt
alle in der Mappe und in der Bank.

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 4 Abweichungen
  (e4 4), alle „sprosse_text nicht wortgleich in Zeile 105“ (die
  Vorstufe der Einheit 4 ist neu gefasst); 0 Warnungen.
- Erster Wurf der neuen Zeilen: 6 Abweichungen (e2 2, e3 4), fünf
  „pruef-Zahl nicht an der Ergebnisstelle“ (Urteil oder Ergebnis
  stand hinter anderen Zahlen), eine Sperre (die Gleichung
  „f(x) = −1“ aus dem Original 2026MgrundlegendBAnalysisMMS2-1f in
  der Aufgabe, ersetzt durch die ausgeschriebene Gleichung). Nach
  einer Korrektur 0. Keine Einheit ist gescheitert.

## Entscheidungen

1. Zone, Grundfälle, Päckchen und muster.md bleiben: die Ketten
   sind unverändert, nur die Vorstufe der Einheit 4 und die
   Originale kamen dazu.
2. Vorstufe e4: Die vier Zeilen waren schon Ankreuzaufgaben; weil
   der neue Sprossentext drei Fälle nennt (Inhalt gesucht; Inhalt
   gegeben und Parameter gesucht; Inhalt gegeben und Grenze
   gesucht), tragen sie jetzt drei Optionen statt zwei; die vier
   Situationen (v1 und v4 vorwärts, v2 Grenze, v3 Parameter) sind
   geblieben.
3. Pooldublette 2026-bb-gk-B2.2d / 2026MgrundlegendBAnalysisWTR2-1d:
   ein Original, zwei Zeilen, Kennung 2026-bb-gk-B2.2d (steht in der
   Mappe zuerst).
4. 2025MerhoehtBAnalysisWTR2-1e („als Anschluss“ in Zeile 104) gilt
   als Original der Prüfungssprosse e3 und bekommt zwei Zeilen.
5. Nachweis-Aufgaben mit Term als Ergebnis (2 − 2e^u) tragen in
   pruef den Zahlanteil des Terms an der Ergebnisstelle (wie „6k“
   in e5 v11); Begründungen tragen die erste Zahl der Lösung.
6. Das Original 2026MerhoehtBAnalysisWTR3-1c („genau ein k > 0“)
   ist mit einer oberen Schranke für k gestellt (0 < k ≤ 4 bzw.
   4 < k ≤ 6), weil bei einer ganzrationalen Funktion der Inhalt
   unter der Achse hinter der nächsten Nullstelle wieder abnimmt
   und die Gleichung sonst eine zweite Lösung hätte.
7. Urteile: e2 v7 richtig, v8 falsch; e3 v11 größer, v12 kleiner.

## Befunde

- bank/_punkte.csv: 16 neue Zeilen mit original (e2 k1 s7 v5–v8,
  e3 k1 s6 v7–v14, e4 k1 s6 v5–v6, e5 k1 s8 v13–v14) fehlen dort;
  keine id ist umbenannt, punkte-nachziehen.py war nicht nötig.
- Prüfskript: \int fehlt weiter in STANDARD; Integrale stehen in
  Worten.
- Katalog: Zeile 105 nennt die Vorstufe jetzt wie die Nachbarketten;
  der Befund vom 29.09. (Klammerform) ist erledigt.

## Offene Punkte

- Keine Grafik ist kompiliert; \funktionab mit zwei Ästen der
  Hyperbel (e5 s8 v13, v14) und \flaeche, \flaechezwischen (e3 k2
  s4 v3, e5 k2 s4 v3) beim Zusammenbau prüfen.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27./28.09. und sind nicht nachgezogen.
- Übernommene Zeilen tragen keine Schrittnamen (Auftrag).
