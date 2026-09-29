# Stand: flaecheninhalt-durch-integration

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719
(2026-09-28, aus dem Kopf der Mappe
mappen/flaecheninhalt-durch-integration.md)
Datum: 2026-09-29 17:11 CEST (date)
Grundlage: bank.md fünfte Fassung (29b), werkzeuge/bank-pruef.py
v0.9 (--katalog aus der Mappe), Vorlage auftrag-eintrag.md 29d;
Nachzug des Bestands vom 27.09. (Katalog 95b0f8b). Umbauskript
in werkzeuge/einmalig/:
nachzug-flaecheninhalt-durch-integration-2026-09-29.py.
Endstand: 0 Abweichungen, 0 Warnungen, mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      26         0        12      13        0       1
    e1.jsonl        36         4         5      12        6       9
    e2.jsonl        37         4         5      15        4       9
    e3.jsonl        39         4         5      12        6      12
    e4.jsonl        34         4         5      12        4       9
    e5.jsonl        51         4         5      18       12      12
    gesamt         223        20        37      82       32      52

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         26      0              0          0
    e1           24      0             12          0
    e2           25      0             12          0
    e3           24      0             15          0
    e4           22      0             12          0
    e5           29      7             15          0

Übernommen heißt: aufgabe, loesung, merkmal wortgleich; nachgezogen
quelle (106–110 → 102–106), id, sprosse (e5 ab s3 um eins nach
hinten) und sprosse_text (Vorstufen bis „nichts rechnen“,
Prüfungssprossen mit dem Wortlaut der Mappe). Umgeschrieben: je
Verfahrenskette die fünf Päckchenzeilen, die Pflichtformen (P1, P2,
P4, P6, P8, in e3 und e5 die Rückrichtung P7) und die merkmal der
Pflichtzeilen. Neu: e5 s3 „Wert und Fläche nebeneinander“ (3) und
an der e5-Prüfungssprosse die Originale 2025MerhoehtBAnalysisMMS1-1c
und 2024MerhoehtBAnalysisWTR1-1f (je 2).

## Originale je Einheit

- e1: 2024-bebb-lk-B2.1k, 2017MerhoehtAAnalysis2-a, 2021-B-1f
- e2: 2025MerhoehtBAnalysisMMS1-1d, 2023-C-2d
- e3: 2024-bebb-gk-B2.2e, 2020-be-gk-B2.2g, 2025-C-2c
- e4: 2025MgrundlegendBAnalysisWTR1-1d, 2026MerhoehtBAnalysisMMS2-2e
- e5: 2025-bebb-lk-B2.1d, 2025MerhoehtBAnalysisMMS1-1c,
  2025MerhoehtBAnalysisWTR2-1d, 2019MgrundlegendBAnalysisWTR1-2e,
  2024-bebb-lk-B2.1j, 2024MerhoehtBAnalysisWTR1-1f

Alle an der letzten Sprosse der Kette (hoehe pruefung), je 2 Zeilen.

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 139 Abweichungen
  (e1 27, e2 28, e3 27, e4 25, e5 32), alle „sprosse_text nicht
  wortgleich in Zeile“ (Katalogzeilen um vier verschoben,
  Vorstufen- und Prüfungstexte länger).
- Erster Wurf je Einheit: zone, e1–e5 je 0 Abweichungen, 0
  Warnungen. Keine Einheit ist gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 34–39 unverändert.
2. Päckchen, fester Wert im merkmal: e1 der Faktor 3 vor x² (die
   Zahl dahinter wandert, Nullstellen ±1 … ±5), e2 f = 3x² + 2 und
   g = −2x (obere Grenze wandert), e3 Graph x² + 1 und Höhe 10
   (Breite des Rechtecks wandert), e4 Parabel 0,5x² (Inhalt
   wandert), e5 Graph x − 2 (obere Grenze wandert).
3. Die Kennungen der Prüfungssprossen, die nicht in Abschnitt 2 der
   Mappe stehen (neun, siehe Befunde), bekommen keine Zeile; die
   Sprosse trägt nur die Originale mit Kennung, keine Zeilen mit
   original null daneben.
4. P1 (Serie) in allen fünf Einheiten statt P3: keine Einheit übt
   eine Umformungskette von Gleichungen.
5. P7 nur in e3 und e5 (wie 27.09.): dort steht je eine
   Zeile Term → Bild und eine Bild → Term; e1, e2, e4 haben keine
   darstellung-Zeilen.
6. Urteile je Einheit: P2 „Richtig“, P6 und P8 je einmal Ja, einmal
   Nein (e1 Nein/Ja, e2 Ja/Nein, e3 Ja/Nein, e4 Ja/Nein, e5
   Nein/Ja); die bestehende P5-Zeile v1 bleibt ohne Urteil.
7. Schrittnamen nur in neuen und umgeschriebenen Zeilen; Integrale
   weiter in Worten („Integral von a bis b über …“), weil `\int`
   nicht in STANDARD steht.
8. e5 s3 trägt das Antwortgerüst „Wert: __ Fläche: __“, weil die
   Sprosse beide Ergebnisse nebeneinander verlangt.

## Befunde

- Mappe: Neun Kennungen der Prüfungssprossen fehlen in Abschnitt 2
  (2026-bb-gk-B2.2d, 2026MgrundlegendBAnalysisWTR2-1d,
  2025-bebb-lk-B2.1e, 2026MgrundlegendBAnalysisMMS2-1f,
  2020MgrundlegendBAnalysisWTR1-1f, 2022-bebb-gk-B2.2i,
  2025MerhoehtBAnalysisWTR2-1e, 2026MerhoehtBAnalysisWTR3-1c,
  2019MgrundlegendBAnalysisWTR1-3d) – wie am 27.09.
- Katalog: Z. 105 nennt die Vorstufe von e4 in der Klammer
  („Vorstufe: ist der Inhalt gegeben oder gesucht?“), die übrigen
  Vorstufen enden auf „nichts rechnen“; der Sprossentext bleibt dort
  unverändert.
- bank/_punkte.csv: 8 ids mit original ändern sich (e5 k1 s7 → s8);
  4 neue Zeilen mit original (e5 k1 s8 v9–v12) fehlen dort.
- Prüfskript: \int fehlt weiter in STANDARD; die Form der
  Pflichtzeilen (P1–P8) prüft es nicht.
- Katalog: Die Erkennungsschritte sind seit 27.09. gestrichen (Z. 40);
  nichts entfällt.

## Offene Punkte

- Keine Grafik ist kompiliert; \flaeche und \flaechezwischen in der
  Aufgabengrafik (e3 k2 s4 v3, e5 k2 s4 v3) beim Zusammenbau prüfen.
- Die neun Kennungen ohne Zeile nachziehen, sobald die Mappe sie
  führt.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27./28.09. und sind nicht nachgezogen.
- Übernommene Zeilen tragen keine Schrittnamen (Auftrag).
