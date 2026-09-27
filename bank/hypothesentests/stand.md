# Stand: hypothesentests

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     22 |        – |        10 |      11 |        – |       1 |
| e1    |     29 |        4 |         5 |       9 |        2 |       9 |
| e2    |     23 |        4 |         5 |       3 |        2 |       9 |
| e3    |     39 |        4 |         5 |      12 |        6 |      12 |
| Summe |    113 |       12 |        25 |      35 |       10 |      31 |

## Originale je Einheit

- e1: 2018-bb-ea-B4.2d, 2023-bebb-lk-B4i,
  2026MerhoehtBStochastikWTR2-2a, 2025-bebb-lk-B4e, 2024-bebb-lk-B4e,
  2017MerhoehtBStochastikCAS2-3b
- e2: 2018MerhoehtBStochastikWTR1-1d, 2024-bebb-lk-B4d,
  2022-bebb-lk-B4h
- e3: 2023-bebb-lk-B4j, 2018MerhoehtBStochastikCAS2-4b,
  2024-bebb-lk-B4f, 2025-bebb-lk-B4f, 2022-bebb-lk-B4g,
  2022MerhoehtBStochastikWTR1-2a, 2023MerhoehtBStochastikWTR2-2c,
  2017MerhoehtBStochastikCAS2-3a

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                |
|-------|-------------:|----------:|---------------------------------|
| zone  |            5 |         0 | Sperre: n oder p aus Original   |
| e1    |            0 |         0 | –                               |
| e2    |            0 |         0 | –                               |
| e3    |            1 |         0 | Zahl nicht an der Ergebnisstelle|

Keine Einheit scheiterte zweimal.

## Entscheidungen

- Wortgleiche Dubletten aus Landesheft und Pool zählen als ein
  Original: 2 Zeilen je Paar, Kennung der Landesfassung.
- An Kettensprossen (hoehe sprosse, grundfall) trägt je
  verfremdetes Original eine Variante das Feld original.
- e3 Prüfungshöhe: drei Originale, weil 2022-bebb-lk-B4g eine
  abgewandelte, keine wortgleiche Poolzeile ist; 6 Zeilen.
- e3 „am Graphen ablesen“: die genannte Kennung fehlt in der Mappe;
  v1 verfremdet 2018MerhoehtBStochastikCAS2-4b (gleicher Typ).
- Zone: kette und sprosse_text sind die Fertigkeit bis zum „ – “,
  bei Fertigkeit 3 (ohne Gedankenstrich) bis zum Punkt.
- Darstellung nur in Einheit 3 (Gütekurve, Tabelle); Einheit 1 und
  2 tragen keinen Darstellungswechsel. Anwendung und Darstellung:
  sprosse_text selbst formuliert, quelle ist die Kettenzeile.
- pruef trägt die mit Python exakt berechneten Binomialwerte als
  Zahl; Binomialsummen sind ohne Hilfsfunktion kein kurzer Ausdruck.
- Gütekurven als \funktion (Polynom) oder \funktionab in
  exp-ln-Form, weil Binomialkoeffizienten über 16384 pgf sprengen.
- e2 k1 s2 v1 verfremdet 2024-bebb-lk-B4d im Sinn der Sprosse als
  laufende Maßnahme, die nur bei nachgewiesenem Rückgang endet.
- Sperre: Stichprobenumfänge und Anteile aus Kasten und Originalen
  (n = 100, 200, 600, 800; p = 0,6; p = 0,7; p ≤ 0,3 …) sind im
  ganzen Eintrag vermieden.

## Befunde

- Katalogbefund: Alle drei Erkennungsschritte verlangen denselben
  Handgriff wie die Vorstufe der Kette ihrer Einheit („Welche
  Richtung?“ E1, „Welcher Fehler?“ E2, „Wo darf p liegen?“ E3); sie
  entfallen, die Vorstufen bleiben.
- Katalogbefund: „Welcher Fehler?“ steht „vor Einheit 2 und 3“;
  nach bank.md steht ein Erkennungsschritt nur einmal.
- Katalogbefund: Die Sprossen nennen 2018MerhoehtBStochastikWTR1-1c,
  2025MerhoehtBStochastikWTR2-2c, 2024MerhoehtBStochastikWTR1-2a,
  2024MerhoehtBStochastikWTR1-2b, 2024MerhoehtBStochastikWTR1-2c,
  2025MerhoehtBStochastikWTR2-2d und 2026MerhoehtBStochastikWTR2-2b;
  sie fehlen in Abschnitt 2 der Mappe und sind nicht nutzbar.
- Katalogbefund: 2024-bebb-lk-B4d (dauerhafter Einsatz nur bei
  gestiegener Zufriedenheit) passt eher zur Figur „teurer Wechsel“
  als zur Sprosse „Abschalten nur bei nachgewiesenem Einbruch“.
- bank.md: „Fertigkeit bis zum Doppelpunkt“ passt nicht zu den
  Sek-II-Fertigkeitszeilen (Form „was – wofür“).

## Offene Punkte

- Die pgf-Ausdrücke der Gütekurven sind nicht kompiliert (kein
  LaTeX); vor dem Blattbau einmal setzen und prüfen.
- e3 k1 s5 v3/v4 nennen den abgelesenen Wert dreistellig im Text,
  weil eine Abbildung benachbarte Umfänge nicht trennt.
