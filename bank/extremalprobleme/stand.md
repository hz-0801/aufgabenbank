# Stand: extremalprobleme

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719
(2026-09-28, aus dem Kopf von mappen/extremalprobleme.md)
Datum: 2026-09-29 18:14 (date, CEST)
Grundlage: bank.md fünfte Fassung (29b), werkzeuge/bank-pruef.py
v0.9, Vorlage auftrag-eintrag.md 2026-09-29d; Nachzug des Bestands
vom 27./28.09. (Katalog 95b0f8b, Gegenlese 28.09.). Umbauskript:
werkzeuge/einmalig/nachzug-extremalprobleme-2026-09-29.py.
Endstand: 0 Abweichungen, 0 Warnungen, mit `--katalog`.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     26 |        – |        12 |      13 |        – |       1 |
| e1    |     31 |        4 |         5 |       9 |        4 |       9 |
| e2    |     37 |        4 |         5 |      15 |        4 |       9 |
| e3    |     46 |        4 |         5 |      24 |        4 |       9 |

## Nachzug je Einheit

| Datei | übernommen | neu | umgeschrieben | entfallen |
|-------|-----------:|----:|--------------:|----------:|
| zone  |         26 |   0 |             0 |         0 |
| e1    |         20 |   0 |            11 |         0 |
| e2    |         22 |   3 |            12 |         0 |
| e3    |         31 |   3 |            12 |         0 |

Übernommen: aufgabe und loesung wortgleich; nachgezogen quelle
(79 → 76, 81–83 → 78–80), sprosse (e2 ab s2 um eins, e3 ab s4 um
eins), id und der Vorstufentext (Katalog: Text nach dem Namen).
Umgeschrieben: Päckchen (je Kette 5), merkmal aller fehler- und
begruenden-Zeilen, je Einheit zwei fehler- und zwei
begruenden-Zeilen (Form), e2 und e3 je eine anwendung (P8).
Neu: e2 s2 „eine feste Nebenbedingung, wechselnde Zielfunktion
ohne Figur“ (3), e3 s4 „Randmaximum“ (3).

## Originale je Einheit

- e1: 2020-C-2c, 2023-A-1e, 2019MgrundlegendBAnalysisWTR2-1f,
  2020MerhoehtAAnalysis11-a, 2019MgrundlegendBAnalysisWTR2-1h;
  Prüfung 2017-bb-ea-B2.2c, 2023-A-1e
- e2: 2025-A-2d, 2025-A-2e, 2022-bebb-gk-B2.1h; Prüfung
  2020MerhoehtAAnalysis11-a, 2020-A-1f
- e3: 2023-A-1f, 2022-bebb-gk-B2.1h, 2018-be-gk-B1.1g,
  2021-be-gk-B2.2i, 2024-bebb-gk-B2.2g,
  2019MgrundlegendBAnalysisWTR2-1i, 2021-be-gk-A1.3b,
  2018-bb-ea-cas-B2.2i (Typ ohne Kette); Prüfung
  2024MerhoehtBAnalysisWTR3-2f, 2023-A-1f

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund              |
|-------|-------------:|----------:|-------------------------------|
| zone  |            0 |         0 | –                             |
| e1    |           25 |         0 | sprosse_text nicht wortgleich |
| e2    |           25 |         0 | sprosse_text nicht wortgleich |
| e3    |           31 |         0 | sprosse_text nicht wortgleich |

Das ist der Bestand gegen die neue Mappe (quelle um drei Zeilen
verschoben). Erster Wurf des Nachzugs: alle Dateien 0. Keine
Einheit ist zweimal gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten (Zeilen 28–33) unverändert.
2. Päckchen: e1 f(x) = 16 − x² fest, die Stelle wandert; e2 Beet
   an der Mauer mit drei Seiten Zaun fest, die Zaunlänge wandert;
   e3 kx − x³ fest, k wandert (Sek-II-Form: derselbe Term).
3. Grundfall-Päckchen und neue Lösungen tragen Schrittnamen
   („Ableitung bilden:“, „Bedingung A'(x) = 0:“, „Randwerte:“).
4. P1-Serie statt P3 in allen Einheiten: keine Einheit übt eine
   Umformungskette von Gleichungen.
5. Randmaximum (e3 s4) ohne original, hoehe sprosse; es steht vor
   den Sprossen mit Original, weil der Katalog es dort nennt.
6. Die Prüfungshöhen bleiben mit 4 Zeilen (je Original 2) wie im
   Bestand; die ids der Zeilen mit original ändern sich in e2 (13)
   und e3 (16), weil davor je eine Sprosse neu ist.
7. Urteile: P6 e1 und e2 „Nein“, e3 „Ja“; P8 e2 „Ja“, e3 „Nein“;
   P2 je Einheit „Richtig.“
8. e1 hat keine anwendung, e2 und e3 keine darstellung (wie im
   Bestand); P8 daher nur in e2 und e3.
9. muster.md: eigene Zahlen außerhalb der Päckchen (20 − x²,
   26 m, 147x − x³).

## Befunde

- Katalog: die Vorstufentexte schließen mit „(Vorstufe)“ bzw.
  „(Vorstufe, Grundvorstellung)“; der sprosse_text endet vor der
  Klammer.
- Katalog: die Sprossen nennen 2020-C-2d, 2020-C-2e, 2025-A-2f,
  2019MgrundlegendBAnalysisWTR2-1g und 2020MerhoehtAAnalysis11-b;
  die Mappe führt sie nicht in Abschnitt 2 (wie 27.09.).
- Katalog: 2023-A-1f, 2022-bebb-gk-B2.1h und
  2020MerhoehtAAnalysis11-a stehen an zwei Sprossen, einmal davon
  auf einer Prüfungshöhe (wie 27.09.).
- bank/_punkte.csv: 29 ids von Zeilen mit original sind
  verschoben (e2 k1 s2–s6 → s3–s7, e3 k1 s4–s8 → s5–s9); die
  Datei ist nicht angefasst.
- Prüfskript: prüft die Form der Pflichtzeilen (P1–P8) nicht; die
  drei Formen je Einheit sind nur durch Durchsicht gesichert.

## Offene Punkte

- Keine Grafik ist kompiliert (LaTeX nicht verfügbar).
- Die Gegenlese vom 28.09. galt dem alten Bestand; die neuen und
  umgeschriebenen Zeilen (41) sind ungelesen.
- Übernommene Zeilen tragen keine Schrittnamen (Auftrag).
