# Stand: funktionsklassen-und-eigenschaften

Katalog-Commit: f56cacecc590f51abf34cf81948a0d2b751d7d33
(2026-09-28, aus dem Kopf von mappen/funktionsklassen-und-
eigenschaften.md)
Datum: 2026-09-29 18:31 CEST (date)
Grundlage: bank.md fünfte Fassung (29b), werkzeuge/bank-pruef.py
v0.9 (--katalog aus der Mappe), Vorlage auftrag-eintrag.md 29d;
Nachzug des Bestands vom 27.09. (Katalog 95b0f8b). Umbauskript:
werkzeuge/einmalig/nachzug-funktionsklassen-und-eigenschaften-
2026-09-29.py. Endstand: 0 Abweichungen, 0 Warnungen.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      28         0        12      15        0       1
    e1.jsonl        51         4         5      24        6      12
    e2.jsonl        53         4         5      27        8       9
    e3.jsonl        30         0         5      12        4       9
    e4.jsonl        39         4         5      18        6       6
    e5.jsonl        53         8         5      24        4      12
    e6.jsonl        51         4         5      24        6      12
    gesamt         305        24        42     144       34      61

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         28      0              0          0
    e1           37      0             14          0
    e2           36      5             12          0
    e3           18      0             12          0
    e4           28      0             11          0
    e5           34      4             15          0
    e6           38      0             13          0

Übernommen: aufgabe, loesung, merkmal wortgleich; nachgezogen nur
quelle (139–144 → 135–140), id, sprosse und bei den Vorstufen
sprosse_text (Katalogtext länger, Aufgabe gleich).
Umgeschrieben: je Verfahrenskette die fünf Grundfallzeilen
(Päckchen), die sechs fehler- und begruenden-Zeilen (v1 nur
merkmal), dazu Lösungen und Aufgaben einzelner anwendung- und
darstellung-Zeilen (P7, P8).
Neu: e2 s6 „rückwärts“ (3), e2 Prüfungshöhe 2023-A-2d (2), e5 s0
„im Argument ausklammern“ (4).

## Originale je Einheit

- e1: 2025-A-1d, 2024-bebb-lk-B2.2g, 2025MerhoehtBAnalysisWTR1-2b
  (alle Prüfung)
- e2: 2026-B-1b, 2023-bebb-gk-B2.2a, 2023MerhoehtBAnalysisWTR1-1a,
  2023-A-2d (alle Prüfung)
- e3: 2017-bb-ea-B2.1a, 2024MerhoehtBAnalysisWTR1-1e (Prüfung)
- e4: 2026-B-1a, 2022-bebb-lk-B2.2a, 2021MerhoehtAAnalysis21-b
  (Prüfung)
- e5: 2026-bb-ea-A1.5b, 2026MerhoehtBAnalysisMMS1-1d (Prüfung)
- e6: 2023-C-1e, 2026MgrundlegendAAnalysis12-a,
  2023MgrundlegendAAnalysis13-b (Prüfung)

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 190 Abweichungen
  (e1 30, e2 30, e3 21, e4 33, e5 37, e6 39), alle „sprosse_text
  nicht wortgleich in Zeile quelle“ (Katalogzeilen um vier
  verschoben).
- Erster Wurf: e1 2 (Sperre: „8 − 4 = 4“ aus dem Merkkasten,
  „e⁰ = 0“ aus Typische Fehler), e5 5 (grafik verlangt: „Zeichne
  nichts“ als Zeichenauftrag gelesen, 4×; pruef fehlt, 1×), e6 1
  (Sperre: x³ − 4x aus 2024-bebb-gk-A1.1a); e2, e3, e4 je 0.
  Zweiter Wurf: 0. Warnungen durchweg 0. Keine Einheit ist zweimal
  gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten (Zeilen 37–42) unverändert.
2. Päckchen: e1 x³ − 4x² + 6 (Stelle wandert), e2 Faktor (x − 3)
   (zweiter Faktor wandert), e3 ln(bx − 6) (Faktor b wandert), e4
   −6x² + 1 (erster Summand wandert), e5 Faktor 3 (Summand wandert),
   e6 x³ − ax an −2 … 2 (a wandert).
3. Vorstufen-sprosse_text: Katalogtext bis „nichts rechnen“, ohne
   die Klammer „(Vorstufe …)“ (wie ableitungsregeln).
4. e5: die alte Vorstufe „Innen oder außen?“ ist jetzt Sprosse
   −1, die neue Katalogvorstufe „im Argument ausklammern“
   Sprosse 0.
5. e2: neue Sprosse 6 „rückwärts“, die alten Sprossen 6–9
   rücken auf 7–10; 2023-A-2d (Katalog nennt es an der
   Prüfungshöhe, bisher ohne Zeile) mit zwei Zeilen an der
   Prüfungssprosse.
6. P1-Serie statt P3 in allen Einheiten: keine Kette übt eine
   Umformungskette; die Ungleichung in e3 ist ein Schritt.
7. e5 anwendung: alle drei neu mit Periode, Stelle stärkster
   Zunahme am Graphen und Grenzwert-Entscheidung, weil der
   Typtext es verlangt (Befund beider Gegenleser 27./28.09.).
8. Urteile der Pflichtzeilen: P2 sechsmal „Richtig“, P6 viermal
   Nein und zweimal Ja, P8 viermal Ja und sechsmal Nein
   (e3 v3 übernommen mit „nein:“).
9. Typen ohne Kette (e1 k2, e2 k2) bleiben mit quelle 27/28.

## Befunde

- Prüfskript: „Zeichne nichts“ gilt als Zeichenauftrag und verlangt
  eine Grafik; nur „ohne zu zeichnen“ ist ausgenommen.
- Prüfskript: prüft die Pflichtformen P1–P8 nicht; die Formen je
  Einheit sind nur durch Durchsicht gesichert.
- Mappe: Die Prüfungshöhen nennen viele Kennungen, die Abschnitt 2
  nicht aufnimmt (etwa 2023MerhoehtBAnalysisWTR2-2c); sie bekommen
  keine Zeile.
- Mappe: 30 Originale in Abschnitt 2 (CAS-Nachtrag 2017/2018) stehen
  an keiner Sprosse der Ketten und haben keine Bankzeile.
- Katalog: Die Ketten nennen den Grundfall „viermal“, bank.md
  verlangt 5 Zeilen; geschrieben sind 5.

## Offene Punkte

- bank/_punkte.csv: 6 ids mit original haben sich geändert (e2
  s9 → s10), 2 neue Zeilen mit original (2023-A-2d) haben noch
  keine Punktezeile.
- e5-k1-s2-v3 (Zweitleser 28.09.): x² − x entsteht aus x² + x auch
  durch Verschiebung; übernommen, weil wortgleich zu halten.
- e3-k1-s6-v3: möglicherweise der unverfremdete Term von
  2024MerhoehtBAnalysisWTR1-1e; am Originalheft prüfen.
- Schrittnamen nur in neuen und umgeschriebenen Zeilen.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27./28.09.; nicht kompiliert (kein LaTeX in der Sitzung).
