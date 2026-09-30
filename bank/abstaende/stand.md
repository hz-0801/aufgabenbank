# Stand: abstaende

Katalog-Commit: db8d2a3 (Katalogstand laut Auftrag 30.09.; der
Kopf der Mappe vom 30.09., 08:04 UTC, nennt 2a296e5 als letzten
Commit, der katalog/abstaende.md änderte – der Eintrag selbst ist
seit dem 29.09. unverändert)
Datum: 2026-09-30 09:05 (date, UTC)
Grundlage: bank.md Stand 2026-09-30b, Prüfskript v0.9 (--katalog),
Vorlage auftrag-eintrag.md 2026-09-29e. Nachzug des Stands vom 29.09.
(Commit 17:19 CEST, Umbauskript
werkzeuge/einmalig/nachzug-abstaende-2026-09-29.py) um die Regel zu
Erkennungsschritten (bank.md 30.09.b). Vorher wie nachher: alle
Dateien 0 Abweichungen, 0 Warnungen, Formprobe 0 Hinweise.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     31 |        – |        12 |      18 |        – |       1 |
| e1    |     41 |        8 |         5 |      15 |        4 |       9 |
| e2    |     37 |       12 |         5 |       9 |        2 |       9 |
| e3    |     39 |        4 |         5 |      15 |        6 |       9 |
| e4    |     34 |        4 |         5 |      12 |        4 |       9 |

Vorstufen: e1 k1 Erkennungsschritt „Hin oder zurück?“ s0 und k2
s0 „Abstand wovon zu was?“ (je 4); e2 k1 Erkennungsschritt
„Abstand wovon zu was?“ s0 (neu 30.09.), k2 s-1 „Hin oder
zurück?“ und s0 Abstand des Ursprungs (je 4); e3, e4 je s0.

## Nachzug 30.09. (Erkennungsschritte)

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         31      0              0          0
    e1           41      0              0          0
    e2           33      4              0          0
    e3           39      0              0          0
    e4           34      0              0          0

Neu: e2 k1 „Abstand wovon zu was?“, vier Zeilen, eigene Kette,
Sprosse 0, quelle 38 (Bereich „vor allen Einheiten“; in e1 hat die
Verfahrenskette eine Vorstufe mit demselben Handgriff, in e2 nicht).
Dadurch in e2 die Verfahrenskette k1 → k2 und die Pflichtkette
k2 → k3; alle 33 Bestandszeilen wortgleich, nachgezogen nur id und
kette_nr; muster.md-Abschnitt „e2 k1“ → „e2 k2“. Umbenannte ids
mit original (für _punkte.csv, nicht angefasst):
abstaende-e2-k1-s2-v1, -s3-v1, -s3-v2, -s3-v3, -s4-v1, -s5-v1,
-s5-v2 → jeweils abstaende-e2-k2-…; kein neues Urteil nötig, die
Zeilen sind unverändert. „Hin oder zurück?“ bleibt Erkennungsschritt
in e1 (dort hat keine Kette eine solche Vorstufe); e2 k2 s-1 bleibt
als Vorstufe der Katalogkette.

## Nachzug je Einheit

| Datei | übernommen | neu | umgeschrieben | entfallen |
|-------|-----------:|----:|--------------:|----------:|
| zone  |         31 |   0 |             0 |         0 |
| e1    |         32 |   0 |             9 |         0 |
| e2    |         20 |   4 |             9 |         0 |
| e3    |         30 |   0 |             9 |         0 |
| e4    |         24 |   0 |            10 |         0 |

Übernommen: Aufgabe und Lösung wortgleich, nachgezogen nur quelle
(105–108 → 103–106), bei e2 die alte Vorstufe s0 → s-1, bei e3
und e4 der längere sprosse_text der Vorstufe, bei e2 s2 v1 der
längere Sprossentext. Neu: e2 s0 (Abstand des Ursprungs).
Umgeschrieben: die vier Päckchen (je 5), e2 s2 v2 und v3 (jetzt
mit Lotfußpunkt und Probe) und je Einheit die Pflichtzeilen, die
eine fehlende Form herstellen (P1, P2, P4, P6, in e4 dazu P8).
Keine id einer Zeile mit original hat sich geändert.

## Originale je Einheit

- e1: 2018-be-gk-B2.1d, 2018-be-gk-B2.2a, 2020MerhoehtAAGLAA211-b,
  2023MgrundlegendBAGLAA1WTR-1c, 2026-bb-gk-A1.5b,
  2026-bb-ea-A1.7b, 2026MerhoehtBAGLAA2WTR1-1g; Prüfungshöhe
  2026-bb-ea-B3e, 2019MgrundlegendAAGLAA211-b
- e2: 2017-bb-ea-B3.2d, 2026-bb-ea-A1.3b, 2025-bebb-gk-A1.8b,
  2024-bebb-lk-A1.7b, 2018-bb-ea-B3.1f; Prüfungshöhe
  2018MerhoehtBAGLAA2WTR1-1g
- e3: 2026-bb-gk-B3c, 2022-bebb-gk-B3i, 2023-bebb-gk-B3h,
  2021-be-gk-B3g, 2022-bebb-lk-A1.5b,
  2021MgrundlegendBAGLAA2WTR2-1e; Prüfungshöhe
  2023MerhoehtBAGLAA2WTR2-1g, 2022MerhoehtBAGLAA2WTR2-1g,
  2026-bb-ea-A1.8b
- e4: 2023-bebb-gk-B3c, 2023MgrundlegendBAGLAA2WTR2-1e,
  2021-be-gk-B2.2h (Grundfall), 2018MerhoehtBAGLAA2WTR3-1d,
  2023MerhoehtBAGLAA2WTR1-1c, 2017-bb-ea-B3.1e, 2017-bb-ea-B3.1c,
  2019MgrundlegendAAGLAA22-b; Prüfungshöhe 2024-bebb-lk-B3d,
  2022-bebb-gk-B3g

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                 |
|-------|-------------:|----------:|----------------------------------|
| zone  |            0 |         0 | –                                |
| e1    |            0 |         0 | –                                |
| e2    |            0 |         0 | –                                |
| e3    |            1 |         0 | Sperre: Tripel des Merkkastens   |
| e4    |            2 |         0 | Sperre: Tripel aus Kasten, Orig. |

Der alte Bestand gegen die neue Mappe: 103 Abweichungen, alle
„sprosse_text nicht wortgleich in Zeile quelle“ (Zeilen um zwei
verschoben, zwei Vorstufen länger). Keine Einheit ist zweimal
gescheitert.

## Entscheidungen

1. Grundfälle tragen original null, außer e4 v1–v3, die wie im
   Bestand ein Original verfremden (der Sprossentext nennt sie).
2. Sek-II-Päckchen: e1 am Quader A(2 | 1 | 1) … G(4 | 4 | 7), A
   bleibt, die Gegenecke wandert; e2 dieselbe Ebene
   2x − y + 2z = 6, der Punkt wandert; e3 dieselbe Gerade, der
   Punkt wandert; e4 dieselben Scheibenebenen und P, Q wandert.
3. Die neue Vorstufe e2 s0 nutzt denselben Normalenvektor wie der
   Grundfall; spätere Sprossen bleiben wortgleich übernommen.
4. e2 s2 v1 (Original 2017-bb-ea-B3.2d) bleibt wortgleich, obwohl
   die Sprosse jetzt Lotfußpunkt und Probe nennt; v2, v3 sind
   umgeschrieben und verlangen beides, die Probe als eigene Zeile.
5. HNF mit Vorzeichen als Schreibform im Grundfall e2 und im
   Muster (Hinweis Sek II); die Seite heißt „Seite des Ursprungs“.
6. merkmal der Pflichtsprossen bleibt je Sprosse einheitlich (das
   Skript verlangt es); die Form steht nur in aufgabe und loesung.
7. Keine Einheit hat darstellung (wie im Bestand; „Dazu“ nennt sie
   nicht); P8 steht in e1, e2, e3 schon im Bestand, in e4 v3
   umgeschrieben.
8. Urteilsfragen: P6 in e1 und e3 „Nein“, in e2 und e4 „Ja“; die
   P4-Serien mischen wahr und falsch.
9. muster.md: je Verfahrenskette eigene Zahlen außerhalb von
   Päckchen und Sperre; e4 als Vergleich mit Kontrollzeile.
10. Die vier neuen e2-Zeilen tragen zwei Punkt–Ebene-, eine
    Punkt–Punkt- und eine Punkt–Gerade-Vorlage mit Kontexten, die in
    e1 k2 s0 nicht vorkommen; Ankreuzoptionen wortgleich wie dort.

## Befunde

- Katalog: „Abstand wovon zu was?“ (38, vor allen Einheiten) ist
  zugleich Vorstufe der Kette e1 (103); „Hin oder zurück?“ (39, vor
  Einheit 1 und 2) zugleich Vorstufe der Kette e2 (104). Nach
  bank.md 30.09.b steht jeder Erkennungsschritt einmal, in der
  ersten Einheit seines Bereichs ohne gleiche Kettenvorstufe:
  „Abstand wovon zu was?“ in e2 (k1, seit 30.09.), „Hin oder
  zurück?“ in e1 (k1). Der Katalog bleibt unverändert.
- bank.md: Die Regel sagt nicht, ob ein in e1 angelegter
  Erkennungsschritt („Hin oder zurück?“) und die gleichnamige
  Kettenvorstufe e2 k2 s-1 als „zwei Ketten mit Vorstufen desselben
  Handgriffs“ zählen; hier sind beide belassen, weil der
  Erkennungsschritt keine Kettenvorstufe ist und der Auftrag es so
  vorgibt.
- Katalog: die Sprossenzeilen nennen den Grundfall „viermal“,
  bank.md fünf Zeilen; bank.md angewandt.
- bank.md: das Päckchen passt schlecht auf e4, dessen Grundfall
  drei Vergleichsarten mischt; gelöst über denselben Körper.
- _punkte.csv: e4-k1-s1-v1 bis v3 sind inhaltlich umgeschrieben
  (ids gleich); das Urteil umfang sollte neu gelesen werden.
- Prüfskript: die Sperre trifft Achsen- und Einheitstripel wie
  (0 | 1 | 0) und kleine Normalenvektoren wie (1 | 2 | 2); für die
  Raumgeometrie eng, aber regelgerecht.

## Offene Punkte

- e3 ist nach den Marken LK-Zusatz; für GK-Blätter sind nur
  Vorstufe, Deutung (s2, s3) und die Pflichtelemente Mindeststoff.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27.09.; die umgeschriebenen Zeilen sind ungelesen.
