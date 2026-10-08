# Stand: ableitungsgraph-und-funktionsgraph

Katalog-Commit: ae6c3fc63b3c02a4f91f338899f160063635aec6
(2026-10-07, aus dem Kopf von
mappen/ableitungsgraph-und-funktionsgraph.md)
Datum: 2026-10-08 03:52 (date, UTC)
Grundlage: bank.md Stand 2026-10-06 (zehnte Fassung),
werkzeuge/bank-pruef.py mit --katalog, Vorlage auftrag-eintrag.md
2026-09-29e. Erstbefüllung, kein Nachzug.
Endstand: 0 Abweichungen, 0 Warnungen, Formprobe 0 Hinweise;
Urteile ja 5, nein 6.

## Zahlen je Datei

    Datei     Zeilen  vorstufe grundfall sprosse pruefung pflicht
    e1.jsonl     102         0         0      48       42      12

Mit Grafik (Feld grafik nicht leer): 85 Zeilen; mit loesungsgrafik 5.

## Originale

e1 (21 Kennungen, je 2 Zeilen an der Prüfungssprosse ihres Typs):
2021-be-gk-A1.2a, 2021MerhoehtAAnalysis22-a, 2026-bb-gk-A1.7a,
2019MerhoehtAAnalysis12-b, 2020-be-gk-B2.1d, 2023-bebb-gk-B2.2f,
2022-bebb-gk-B2.1c, 2025-bebb-lk-A1.1b, 2019MerhoehtAAnalysis12-a,
2026MgrundlegendAAnalysis14-a, 2017MgrundlegendAAnalysis2-a,
2020-be-gk-B2.2e, 2025-bebb-lk-B2.2a,
2017MgrundlegendBAnalysisWTR-2c, 2022-bebb-lk-B2.1e,
2025-bebb-lk-B2.2i, 2024MerhoehtBAnalysisWTR1-1c,
2026MgrundlegendBAnalysisMMS1-1e, 2024MgrundlegendBAnalysisWTR1-2c,
2023-bebb-gk-B2.1h, 2026MerhoehtBAnalysisMMS2-2c.
Pooldubletten als ein Original mit der Kennung, die in der Mappe
zuerst steht: 2025-bebb-lk-A1.1b (= 2025MerhoehtAAnalysis12-b),
2026-bb-gk-A1.7a (= 2026MgrundlegendAAnalysis22-a).

## Prüfskript vor der Korrektur

e1.jsonl: 1 Abweichung, 0 Warnungen; Grund: Punkt mit \mid in der
Lösung wird nicht als Ergebnisstelle erkannt (pruef auf die Stelle
gekürzt).

## Entscheidungen

- Verweiseintrag ohne eigene Lerneinheit: eine Datei e1.jsonl
  (einheit 1), nicht e4 nach der Einheit des tragenden Eintrags.
- Jeder der 16 Haupttypen aus Prüfungsform (Zeilen 31, 32) ist eine
  eigene Kette: s1 hoehe sprosse (3 Zeilen, eigene Vorlage), s2
  hoehe pruefung (2 Zeilen je Original); kette und sprosse_text =
  Typname wortgleich. Grund: der Eintrag hat keine eigene Sprosse,
  die Originale brauchen eine Prüfungssprosse je Typ.
- Reihenfolge der Typketten vom Ablesen zum Begründen, nicht nach
  Häufigkeit; die Bank erfindet sonst keine Struktur.
- Keine Sprossenkette „Graph und Ableitungsgraph“, keine zone.jsonl:
  beide liegen in bank/kurvenuntersuchung (e4, zone), der Katalog
  verweist darauf; doppelt angelegt wären sie Dubletten.
- Pflichtelemente als Kette 17 „Graph und Ableitungsgraph“ (Name der
  Sprossenkette des tragenden Eintrags); sprosse_text aus Zeile 23
  (fehler), 31 (begruenden), 6 (darstellung), 32 (anwendung).
- Kein muster.md: keine Verfahrenskette, und bank.md legt seit
  05.10. keine neuen Musterbeispiele an.
- Prüfkennung: be-gk, bebb-gk, bb-gk, iqb grundlegend = GK;
  bebb-lk, iqb erhöht = LK.

## Befunde

- Verweiseintrag: Mappe und Auftragsvorlage setzen eigene
  Lerneinheiten, Sprossen und Voraussetzungen voraus; für
  Verweiseinträge fehlt in bank.md eine Regel (Ablage, Einheit,
  Zone).
- Die 23 Originale dieses Eintrags stehen nicht in der Mappe von
  kurvenuntersuchung; der Blattbau zu „Graph und Ableitungsgraph“
  muss beide Ordner lesen.
- bank-pruef.py erkennt „(2 \mid 1)“ nicht als Punkt (PUNKT kennt
  nur | und ;), obwohl andere Bankzeilen \mid schreiben.
- bank/_punkte.csv hat für die 42 Zeilen mit original noch keine
  Zeilen (Schreibbereich dieses Laufs nur der Eintragsordner).

## Offene Punkte

- _punkte.csv nachziehen (werkzeuge/punkte.py --lesestoff, Urteile).
- Grafiken nicht kompiliert (kein LaTeX); Sichtprobe im Render offen.
