# Stand: extremalprobleme

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, alle Dateien 0 Abweichungen,
0 Warnungen.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     26 |        – |        12 |      13 |        – |       1 |
| e1    |     31 |        4 |         5 |       9 |        4 |       9 |
| e2    |     34 |        4 |         5 |      12 |        4 |       9 |
| e3    |     43 |        4 |         5 |      21 |        4 |       9 |

## Originale je Einheit

- e1: 2020-C-2c, 2023-A-1e, 2019MgrundlegendBAnalysisWTR2-1f,
  2020MerhoehtAAnalysis11-a, 2019MgrundlegendBAnalysisWTR2-1h;
  Prüfungshöhe 2017-bb-ea-B2.2c und 2023-A-1e
- e2: 2025-A-2d, 2025-A-2e, 2022-bebb-gk-B2.1h; Prüfungshöhe
  2020MerhoehtAAnalysis11-a und 2020-A-1f
- e3: 2023-A-1f, 2022-bebb-gk-B2.1h, 2018-be-gk-B1.1g,
  2021-be-gk-B2.2i, 2024-bebb-gk-B2.2g,
  2019MgrundlegendBAnalysisWTR2-1i, 2021-be-gk-A1.3b,
  2018-bb-ea-cas-B2.2i (Typ ohne Kette); Prüfungshöhe
  2024MerhoehtBAnalysisWTR3-2f und 2023-A-1f

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund             |
|-------|-------------:|----------:|------------------------------|
| zone  |            0 |         0 | –                            |
| e1    |            0 |         0 | –                            |
| e2    |            1 |         0 | pruef nicht an Ergebnisstelle |
| e3    |            0 |         0 | –                            |

Keine Einheit scheiterte zweimal.

## Entscheidungen

1. Grundfälle tragen original null; Zwischensprossen mit einer
   Kennung aus Abschnitt 2 tragen sie, nennt eine Sprosse mehrere
   (e1 s2, e3 s5), trägt jede Variante eine andere.
2. Prüfungshöhen mit Abitur-Original und fhr-Zielmarke: eine Sprosse,
   4 Zeilen, je Original 2; sprosse_text ist die ganze Katalogspanne.
3. e2 s4 trägt original null: 2020-C-2d fehlt in Abschnitt 2, und
   2020-A-1f (Umfang) steht bereits auf der Prüfungshöhe; die
   Varianten üben nur die Symmetriefaktoren.
4. e3 s2 trägt original null, weil 2025-A-2f und 2020-C-2e nicht in
   Abschnitt 2 stehen.
5. Zone: kette ist die Fertigkeit bis zum Gedankenstrich; Folge
   Flächen, Punkte (e1), Terme (e2), Ableiten, Gleichungen,
   Extrempunkte (e3, in der Folge des Verfahrens).
6. Zone-Paar bei den Flächenformeln: Faktor ein halb vergessen – Teil
   des häufigsten Musters „Faktoren der Figur verloren“.
7. Pflichtelemente: fehler und begruenden je Einheit, darstellung nur
   in e1 (quelle 79, Grundvorstellung), anwendung in e2 und e3; die
   Anwendungen in e3 lösen die Zielfunktionen aus e2.
8. Typ ohne Kette in e3: „Kleinsten Abstand eines Punktes zu einem
   Graphen …“ mit dem Original 2018-bb-ea-cas-B2.2i.
9. Der FHR-Umfang heißt U(x), weil u in e2 die Stelle bezeichnet.
10. e3 s8 v3 setzt die Zielfunktion aus e1 s5 v3 fort (FHR-Kette
    Dreieck, Nachweis, Maximum); die Zahlen sind rechnertypisch krumm.

## Befunde

- Katalog: alle drei Erkennungsschritte verlangen denselben Handgriff
  wie die Vorstufe ihrer Kette und entfallen; der Katalog führt beide.
- Katalog: die Sprossen nennen 2020-C-2d, 2020-C-2e, 2025-A-2f,
  2019MgrundlegendBAnalysisWTR2-1g und 2020MerhoehtAAnalysis11-b; die
  Mappe führt sie nicht in Abschnitt 2.
- Katalog: 2023-A-1f, 2022-bebb-gk-B2.1h und
  2020MerhoehtAAnalysis11-a stehen jeweils an zwei Sprossen, einmal
  davon auf einer Prüfungshöhe.
- Katalog: e1 s2 heißt „Rechteck oder Dreieck … einzeichnen“, nennt
  mit 2019MgrundlegendBAnalysisWTR2-1f aber ein Trapez.
- bank.md: „Fertigkeit bis zum Doppelpunkt“ passt nicht; die Zeilen
  trennen mit Gedankenstrich, und „Ableitungen bilden:“ und
  „Gleichungen lösen:“ haben den Doppelpunkt mitten in der
  Fertigkeit.
- Prüfskript: pruef "" ist nur bei pflicht begruenden erlaubt;
  Begründungs- und Deutungssprossen (e1 s3–s4, e2 s6, e3 s8) tragen
  deshalb eine Kontrollzahl.

## Offene Punkte

- Die ksys-Grafiken (e1) sind nicht gesetzt worden; LaTeX ist in der
  Sitzung nicht verfügbar.
