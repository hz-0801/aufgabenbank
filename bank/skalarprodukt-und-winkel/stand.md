# Stand – skalarprodukt-und-winkel

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719 (Mappe
vom 29.09., 17:58 UTC)
Datum: 2026-09-29 20:51 CEST
Vorlage auftrag-eintrag.md 2026-09-29e; Nachzug des Bestands vom
27.09. Prüfskript v0.10 mit `--katalog`: alle Dateien 0
Abweichungen, 0 Warnungen.
Umbauskript:
werkzeuge/einmalig/nachzug-skalarprodukt-und-winkel-2026-09-29.py

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     31 |      – |      12 |      18 |      – |       1 |
| e1    |     30 |      8 |       5 |       9 |      2 |       6 |
| e2    |     38 |      8 |       5 |      12 |      4 |       9 |
| e3    |     31 |      4 |       5 |       9 |      4 |       9 |
| e4    |     29 |      4 |       5 |       9 |      2 |       9 |
| Summe |    159 |     24 |      32 |      57 |     12 |      34 |

Vorstufen: e1 k1 s-1 („Zahl oder Vektor?“) und s0 (Quader ohne
Koordinaten), je 4; e2 k1 Erkennungsschritt und k2 s0; e3, e4 je s0.

## Nachzug je Einheit

| Datei | übernommen | neu | umgeschrieben | entfallen |
|-------|-----------:|----:|--------------:|----------:|
| zone  |         31 |   0 |             0 |         0 |
| e1    |         17 |   4 |             9 |         0 |
| e2    |         29 |   0 |             9 |         0 |
| e3    |         22 |   0 |             9 |         0 |
| e4    |         20 |   0 |             9 |         0 |

Übernommen: Aufgabe und Lösung wortgleich; nachgezogen quelle
(96 → 94, 97 → 95, 98 → 96, 99 → 97, 41 → 39), bei e1 die alte
Vorstufe s0 → s-1, und der längere sprosse_text der Vorstufen und
Prüfungssprossen. Neu: e1 s0. Umgeschrieben: die vier Päckchen (je
5) und je Einheit vier Pflichtzeilen für die fehlenden Formen.
Zeilen mit original: 31 vorher, 31 nachher, keine id geändert; die
vier Päckchenzeilen v5 tragen eine neue Aufgabe.

## Originale je Einheit

- e1: 2024MerhoehtAAGLAA211-b, 2025MerhoehtAAGLAA211-a,
  2025MerhoehtAAGLAA211-b, 2024MgrundlegendBAGLAA1WTR-1f,
  2021MgrundlegendAAGLAA12-c (Prüfungshöhe)
- e2: 2026-bb-gk-B3b, 2019-be-gk-B3.2c, 2018-bb-ea-B3.1c,
  2024-bebb-gk-B3b, 2021MgrundlegendBAGLAA2WTR2-1d,
  2023MerhoehtBAGLAA1WTR-2a und 2017-bb-ea-B3.1b (Prüfungshöhe)
- e3: 2025-bebb-gk-B3c, 2024-bebb-gk-B3e, 2018-be-gk-B2.2c,
  2024MgrundlegendBAGLAA2WTR1-1c, 2022MerhoehtBAGLAA2WTR2-1d,
  2020MgrundlegendBAGLAA2WTR-1b, 2026MgrundlegendBAGLAA2WTR1-1e und
  2017-bb-ea-B3.1b (Prüfungshöhe)
- e4: 2023MgrundlegendBAGLAA2WTR1-1f, 2017-bb-ea-B3.2a,
  2023MerhoehtBAGLAA2WTR1-1d, 2018MerhoehtBAGLAA2CAS2-1f,
  2023MerhoehtBAnalysisWTR2-2e (Prüfungshöhe)

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                     |
|-------|-----:|------:|--------------------------------------|
| zone  |    0 |     0 | –                                    |
| e1    |    5 |     0 | Sperre: Quaderecke (5, 1, 0)         |
| e2    |    5 |     0 | Sperre: Zeltecke (0, 4, 0)           |
| e3    |    0 |     0 | –                                    |
| e4    |    0 |     0 | –                                    |

Der alte Bestand gegen die neue Mappe: 97 Abweichungen, alle
„sprosse_text nicht wortgleich in Zeile quelle“ (Zeilen um zwei
verschoben). e1 und e2 brauchten je einen zweiten Körper. Keine
Einheit ist zweimal gescheitert.

## Entscheidungen

1. Sek-II-Päckchen: e1 Quader A(1 | 2 | 0) … H(1 | 4 | 2), AG bleibt;
   e2 Zelt mit Spitze S(1 | 2 | 6), Kante SA bleibt; e3 Pavillondach
   mit Spitze S(0 | 0 | 6), die xy-Ebene bleibt; e4 Mastspitze
   S(2 | 3 | 8), der Boden bleibt; die zweite Größe wandert.
2. Die Körper tragen nur Vorstufe s0 (e1, ohne Koordinaten, dieselben
   Kantenlängen) und Grundfall; spätere Sprossen bleiben wortgleich
   übernommen (Übernahme vor Körperregel).
3. Winkel als „Ergebnis: $\varphi \approx …^\circ$“, nicht „rund“:
   das Prüfskript erkennt „rund“ nicht als Ergebnisstelle.
4. Neu geschriebene Lösungen tragen Schrittnamen (Vektoren,
   Skalarprodukt, Beträge, Kosinus/Sinus, Ergebnis); übernommene
   Lösungen bleiben ohne.
5. Pflichtformen: e1 P2 und P3 (Parameterungleichung), e2–e4 P1 und
   P2; begruenden je Einheit „Begründe, warum …“, P4, P6.
6. Urteile: P6 je Einheit „Nein“, P2 „Richtig“, P8 e2 und e4 „ja“,
   e3 „nein“; die P4-Serien mischen wahr und falsch.
7. Keine darstellung, e1 keine anwendung (wie im Bestand; die Typen
   tragen sie nicht).
8. Grundfall-Zeile v5 trägt weiter das Original der Sprosse.

## Befunde

- Katalog: Erkennungsschritt „Welche zwei Richtungen …“ wiederholt
  die Vorstufe von e2 und „Der Formelwinkel …“ die von e3; beide
  entfallen dort (bank.md), „Der Formelwinkel …“ steht nur in e2.
- Katalog: 2017-bb-ea-B3.1b ist Prüfungshöhe in e2 und e3; in e2
  verlangt es Ebenen-Normalen, die erst e3 einführt.
- Prüfskript: „rund“ zählt nicht als Ergebnisstelle; der Hinweis des
  Auftrags („Ergebnis: … rund …°“) lässt sich so nicht umsetzen.
- Prüfskript: die Sperre zählt jede Körperecke einzeln; kleine
  Koordinaten treffen Tripel der Mappe, obwohl keine Figur gleich ist.

## Offene Punkte

- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27.09.; die umgeschriebenen Zeilen sind ungelesen.
- bank/_punkte.csv: die vier Päckchenzeilen v5 haben eine neue
  Aufgabe bei gleicher id; ihr Urteil ist neu zu fällen.
- Sachbild-Aufgaben (e3 s3) stehen weiter ohne Grafik.
