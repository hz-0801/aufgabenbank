# Stand: ebenen

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     30 |        – |        14 |      15 |        – |       1 |
| e1    |     37 |        4 |         5 |      12 |        4 |      12 |
| e2    |     63 |        8 |        10 |      31 |        2 |      12 |
| e3    |     46 |        4 |         5 |      21 |        4 |      12 |
| e4    |     32 |        4 |         5 |      12 |        2 |       9 |
| Summe |    208 |       20 |        39 |      91 |       12 |      46 |

## Originale je Einheit

- e1: 2018-bb-ea-B3.2a, 2022MgrundlegendBAGLAA2WTR2-1a,
  2018MgrundlegendAAGLAA211-b, 2022-bebb-gk-B3b
- e2: 2020MgrundlegendBAGLAA2WTR-1a, 2024-bebb-gk-B3d,
  2025-bebb-gk-B3b, 2021MgrundlegendBAGLAA2WTR1-1b, 2020-be-gk-B3.1a,
  2023MerhoehtBAGLAA2WTR2-1a, 2024MgrundlegendBAGLAA2WTR2-1c,
  2020-be-gk-B3.2b, 2018-be-gk-B2.1a, 2018MerhoehtAAGLAA212-b,
  2022-bebb-lk-B3c, 2017-bb-ea-A1.2b, 2021-be-gk-A1.4a,
  2025MgrundlegendBAGLAA2WTR1-1c, 2017-bb-ea-B3.2c, 2025-bebb-lk-B3b
- e3: 2020MerhoehtAAGLAA22-a, 2022-bebb-gk-A1.4b,
  2023MerhoehtBAGLAA2WTR1-1f, 2018MerhoehtBAGLAA2WTR3-1f,
  2026MerhoehtBAGLAA2WTR1-1f, 2018-bb-ea-A1.2a,
  2022MgrundlegendBAGLAA2WTR1-1b, 2026MerhoehtBAGLAA2WTR1-1c,
  2022MerhoehtAAGLAA222-b
- e4: 2019-be-gk-B3.2e, 2023-bebb-gk-B3b, 2020-be-gk-B3.2c,
  2020MgrundlegendAAGLAA211-b, 2017MgrundlegendBAGLAA2WTR1-1f

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund              |
|-------|-------------:|----------:|-------------------------------|
| zone  |           34 |         0 | pruef als Zahl statt Ausdruck |
| e1    |           10 |         0 | Sperre: Tripel                |
| e2    |           12 |         5 | Sperre: Tripel                |
| e3    |            4 |         0 | Sperre: Tripel                |
| e4    |            1 |         0 | Sperre: Tripel                |

Sperre: Tripel heißt ein Tripel aus Merkkasten oder Original.

Nach der Korrektur bleibt eine Warnung: e2 k1 s8, 4 Zeilen statt 3
(siehe Entscheidungen). Keine Einheit scheiterte zweimal.

## Entscheidungen

- Einheit 2 hat zwei Verfahrensketten mit derselben Vorstufe; jede
  Kette trägt ihre eigene Vorstufe mit vier verschiedenen Zeilen.
- In Einheit 2 trägt nur die letzte Kette hoehe pruefung; die
  Prüfungshöhe der ersten Kette steht als hoehe sprosse mit Original,
  4 Zeilen (2 je Original), daher die Warnung „Menge sprosse = 3“.
- Wortgleiche Dubletten aus Landesheft und Pool zählen als ein
  Original: 2 Zeilen je Paar, Kennung der Landesfassung.
- An Kettensprossen (hoehe sprosse) trägt je verfremdetes Original
  eine Variante das Feld original, die übrigen Varianten null.
- Zone: kette und sprosse_text sind die Fertigkeit bis zum „ – “
  (die Sek-II-Zeilen haben keinen Doppelpunkt), bei Fertigkeit 7
  bis zum Doppelpunkt.
- Variablen x, y, z wie im Merkkasten; Schrägbilder mit
  \begin{ksys3}[xyz].
- Anwendung und Darstellung: sprosse_text selbst formuliert (der
  Katalog nennt nur Fehler finden und Begründen), quelle ist die
  Kettenzeile; Pflicht-Sprossen fehler 1, begruenden 2, anwendung 3,
  darstellung 4.
- Einheit 4 ohne Darstellung, weil kein Typ der Einheit einen
  Darstellungswechsel trägt.
- Typ ohne Kette in Einheit 4: kette und sprosse_text sind der
  Typname ohne Klammerzusatz, quelle Zeile 26.
- Schrägbild-Sonderfall (e3 Prüfungshöhe): die Verkürzung der
  x-Achse steht im Aufgabentext, weil keine Abbildung vorliegt.

## Befunde

- Katalogbefund: Alle vier Erkennungsschritte verlangen denselben
  Handgriff wie die Vorstufe der Kette ihrer Einheit („Was legt die
  Ebene fest?“ E1, „Welche Form, welcher Weg?“ E2, „Welche
  Koordinate fehlt?“ E3, „Parallel, identisch oder schneidend?“ E4);
  sie entfallen, die Vorstufen bleiben.
- Katalogbefund: „Was legt die Ebene fest?“ steht „vor Einheit 1
  und 4“; nach bank.md steht ein Erkennungsschritt nur einmal.
- Katalogbefund: Einheit 2 hat in beiden Ketten eine Prüfungshöhe,
  bank.md erlaubt eine Sprosse mit hoehe pruefung je Einheit.
- Katalogbefund: 2024MerhoehtBAGLAA2WTR1-1c,
  2026MgrundlegendBAGLAA2WTR1-1c und 2026MerhoehtBAGLAA2MMS2-1b
  stehen in Sprossen, fehlen aber in Abschnitt 2 der Mappe und sind
  daher nicht als original nutzbar.
- bank.md: „Prüfungshöhe 2 je Original“ klärt nicht, ob wortgleiche
  Dubletten eins oder zwei Originale sind; das Prüfskript zählt je
  Kennung.
- bank.md: „Fertigkeit bis zum Doppelpunkt“ passt nicht zu den
  Sek-II-Fertigkeitszeilen (Form „was – wofür“).
- Prüfskript: „im Koordinatensystem“ im Wortlaut des Originals
  2022-bebb-gk-A1.4b („Beschreibe die Lage … im Koordinatensystem“)
  gilt als Zeichenauftrag und verlangt eine Grafik.

## Offene Punkte

- Die Schrägbild-Konvention von ksys3 (Verkürzung der x-Achse) ist
  in _bausteine.md nicht belegt; e3 k1 s9 v3/v4 mit der Vorlage
  abgleichen.
- e3 k2 s4 v2 (Spurpunkte am \rebene ablesen) setzt bezifferte
  Achsen im Schrägbild voraus.
