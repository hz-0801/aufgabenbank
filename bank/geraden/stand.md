# Stand: geraden

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719 (Mappe vom
29.09., 12:26 UTC)
Datum: 2026-09-29 15:09 CEST
Vorlage auftrag-eintrag.md 2026-09-29c; Nachzug des Bestands vom
27./28.09. (samt Gegenlese-Korrekturen). Prüfskript v0.9 mit
`--katalog`: alle Dateien 0 Abweichungen, 0 Warnungen.
Umbauskript: werkzeuge/einmalig/nachzug-geraden-2026-09-29.py.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     30 |        – |        14 |      15 |        – |       1 |
| e1    |     47 |       16 |         5 |      12 |        2 |      12 |
| e2    |     44 |        4 |         5 |      24 |        2 |       9 |
| e3    |     33 |        8 |         5 |      12 |        2 |       6 |
| e4    |     31 |        4 |         5 |       9 |        4 |       9 |

Vorstufen: e1 k2 s-2, s-1, s0 (je 4) und der Erkennungsschritt
k1 (4); e3 k1 s-1, s0 (je 4); e2, e4 je s0.

## Nachzug je Einheit

| Datei | übernommen | neu | umgeschrieben | entfallen |
|-------|-----------:|----:|--------------:|----------:|
| zone  |         30 |   0 |             0 |         0 |
| e1    |         29 |   8 |            10 |         0 |
| e2    |         34 |   0 |            10 |         0 |
| e3    |         20 |   4 |             9 |         0 |
| e4    |         21 |   0 |            10 |         0 |

Übernommen: Aufgabe und Lösung wortgleich, nachgezogen nur quelle
(40 → 39, 101 → 102, 103–106 → 104–107), sprosse, id und bei den
alten Vorstufen der längere sprosse_text. Neu: e1 s-1 Wertetafel,
e1 s0 Quaderkante, e3 s-1 Lagen am Quader. Umgeschrieben: die vier
Päckchen (je 5) und je Einheit die Pflichtzeilen, die eine fehlende
Form herstellen (P1, P2, P4, P6, P8).

## Originale je Einheit

- e1: 2023MgrundlegendAAGLAA213-a, 2021MerhoehtAAGLAA112-a,
  2019-be-gk-A1.3a, 2022MgrundlegendAAGLAA213-b,
  2021-be-gk-A1.5b (Prüfungshöhe)
- e2: 2023-bebb-gk-A1.4a, 2019MgrundlegendAAGLAA211-a,
  2019MgrundlegendAAGLAA22-a, 2018-be-gk-B2.2d, 2020-be-gk-A1.3a,
  2023MgrundlegendAAGLAA213-b, 2026MgrundlegendBAGLAA2MMS2-1d,
  2017MerhoehtBAGLAA2WTR1-1f, 2017MerhoehtBAGLAA2WTR3-1g,
  2017MgrundlegendBAGLAA2CAS1-1f, 2025-bebb-lk-A1.7a (Prüfungshöhe)
- e3: 2022MgrundlegendAAGLAA213-a, 2021-be-gk-B3b, 2018-be-gk-B2.1c,
  2019-be-gk-A1.3b (Prüfungshöhe)
- e4: 2022MgrundlegendBAGLAA2WTR1-1f, 2022MgrundlegendBAGLAA2WTR1-1e,
  2017MgrundlegendBAnalysisWTR-1g, 2018-be-gk-B2.2e und
  2025MgrundlegendBAGLAA2WTR1-1e (Prüfungshöhe)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund               |
|-------|-------------:|----------:|--------------------------------|
| zone  |            0 |         0 | –                              |
| e1    |           16 |         0 | Sperre: Tripel des Quaders     |
| e2    |            3 |         0 | merkmal uneinheitlich (Pflicht) |
| e3    |            5 |         0 | Sperre: Tripel aus der Mappe   |
| e4    |            5 |         0 | merkmal uneinheitlich (Pflicht) |

Der alte Bestand gegen die neue Mappe: 104 Abweichungen, alle
„sprosse_text nicht wortgleich in Zeile quelle“ (Zeilen
verschoben). e1 brauchte einen zweiten Quader (der erste traf
nach der Verschiebung drei Tripel der Mappe). Keine Einheit ist
zweimal gescheitert.

## Entscheidungen

1. Grundfälle tragen original null, auch wo die Sprosse eine
   Kennung nennt (wie im Bestand).
2. Sek-II-Päckchen: e1 und e3 am Quader mit festen Ecken (e1
   A(1 | 3 | 0) … G(6 | 7 | 3), e3 A(1 | 0 | 0) … G(5 | 3 | 4)),
   eine Ecke bleibt, die zweite wandert; e2 dieselbe Gerade, der
   Punkt wandert; e4 dieselbe Mastspitze, der Anker wandert.
3. Der Quader von e1 trägt die ganze Vorstufenkette s-1, s0, s1;
   die späteren Sprossen bleiben wortgleich übernommen und nutzen
   ihn nicht – die Übernahme geht vor der Körperregel.
4. merkmal der Pflichtsprossen bleibt je Sprosse einheitlich (das
   Skript verlangt es); die Form steht nur in aufgabe und loesung.
5. e3 hat keine anwendung und keine darstellung, e2 und e4 keine
   darstellung (wie im Bestand; die Typen tragen sie nicht).
6. e2 k2 und e4 k2 (Typen ohne Kette) bleiben wie im Bestand.
7. Urteilsfragen: P6 je Einheit mit „Nein“, P8 mit „Ja“; die P4-
   Serien mischen wahr und falsch.
8. muster.md: je Verfahrenskette eigene Punkte außerhalb der
   Päckchen und der Sperre.

## Befunde

- Katalog: die Erkennungsschritte „Punkt, Richtung, Parameter?“,
  „Aus welcher Koordinate …“ und „Identisch, parallel …“ stehen
  nicht mehr als eigene Schritte, sind aber als Vorstufen in den
  Ketten geblieben – der Befund vom 27.09. ist erledigt.
- Katalog: „Gerade oder Strecke?“ steht als Erkennungsschritt vor
  e1 und e4 und zugleich als Vorstufe von e4; er steht nur in e1.
- Katalog: Sprossen nennen 2019-be-gk-B3.1c und
  2018MgrundlegendBAGLAA2WTR2-1e, die Mappe führt beide nicht in
  Abschnitt 2 – für diese Sprossen ist kein original möglich.
- bank.md: „dieselben Körper durch die ganze Kette“ kollidiert mit
  der Übernahme wortgleicher Zeilen im Nachzug; der Auftrag regelt
  nicht, welche Regel vorgeht.
- Prüfskript: die Sperre zählt jede Ecke des Quaders einzeln; bei
  kleinen Koordinaten treffen viele Quader Tripel der Mappe, obwohl
  kein Original dieselbe Figur hat.

## Offene Punkte

- Die ksys3-Grafiken (e1 darstellung, Quader in e1 s0 und e3 s-1)
  sind nicht gerendert; LaTeX ist in der Sitzung nicht verfügbar.
- e4 s4 v4: der vorgelegte Ansatz hat keine Lösung mit t zwischen
  null und eins; gefragt ist nur die Deutung.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27.09. (alte ids); die umgeschriebenen Zeilen sind ungelesen.

## Nachbesserung 2026-09-30

- Teil 2, geraden-e3-k1-s4-v1: Würfel mit Kantenlänge 3 statt 5
  (A(3|0|0), B(3|3|0), C(0|3|0), G(0|3|3)), Geradengleichung,
  Richtungen und pruef nachgerechnet – die Ecken fielen mit dem Boden
  des Originals 2017MgrundlegendBAGLAA2CAS2-1f zusammen (Sperre).
  Kantenlänge 4 und 6 gingen nicht: 4 trifft A, B, C eines Quaders im
  Original, 6 trifft E(6|0|0), F(0|6|0) der Kletteranlage.
