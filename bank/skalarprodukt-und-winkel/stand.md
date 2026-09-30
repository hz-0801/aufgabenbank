# Stand – skalarprodukt-und-winkel

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19 (Mappe
vom 30.09., 08:13 UTC)
Datum: 2026-09-30 08:54 UTC
Vorlage auftrag-eintrag.md 2026-09-29e, bank.md 2026-09-30b;
Nachzug des Stands vom 29.09. (Katalog 2a296e5) nach der
Katalogänderung vom 30.09. (Zeile 95: Prüfungshöhe der Einheit 2
ohne den Zeltwinkel) und der neuen Regel zu Erkennungsschritten.
Prüfskript v0.10 mit `--katalog`: alle Dateien 0 Abweichungen,
0 Warnungen, Formprobe 0 Hinweise.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     31 |      – |      12 |      18 |      – |       1 |
| e1    |     30 |      8 |       5 |       9 |      2 |       6 |
| e2    |     38 |      8 |       5 |      12 |      4 |       9 |
| e3    |     35 |      8 |       5 |       9 |      4 |       9 |
| e4    |     29 |      4 |       5 |       9 |      2 |       9 |
| Summe |    163 |     28 |      32 |      57 |     12 |      34 |

Vorstufen: e1 k1 s-1 („Zahl oder Vektor?“) und s0 (Quader ohne
Koordinaten), je 4; e2 k1 Erkennungsschritt „Der Formelwinkel oder
sein Nachbar?“ und k2 s0 („Welche zwei Richtungen …“ als Vorstufe
der Kette); e3 k1 Erkennungsschritt „Welche zwei Richtungen bilden
den Winkel?“ (neu, 30.09.) und k2 s0 („Kosinus oder Sinus?“);
e4 k1 s0.

## Nachzug je Einheit (30.09.)

| Datei | übernommen | neu | umgeschrieben | entfallen |
|-------|-----------:|----:|--------------:|----------:|
| zone  |         31 |   0 |             0 |         0 |
| e1    |         30 |   0 |             0 |         0 |
| e2    |         36 |   2 |             0 |         2 |
| e3    |         31 |   4 |             0 |         0 |
| e4    |         29 |   0 |             0 |         0 |

Übernommen: Aufgabe und Lösung wortgleich; nachgezogen in e2 der
sprosse_text und das merkmal der Prüfungssprosse s6 (v1, v2), in
e3 id und kette_nr aller Zeilen (k1 → k2, k2 → k3). Neu: e2 s6 v3
und v4 mit dem Trapezwinkel 2019-be-gk-B3.2c (Würfel und Quader,
Innenwinkel bei N bzw. X); e3 k1 s0 v1–v4, der Erkennungsschritt
als eigene Kette (Ebene gegen xy-Ebene, zwei Seitenflächen, Gerade
gegen Ebene, Kante gegen Grundfläche). Entfallen: e2 s6 v3 und v4
mit dem Zeltwinkel 2017-bb-ea-B3.1b (liegt in e3 s5 v3, v4).
Zeilen mit original: 31 vorher, 31 nachher; ids geändert: alle 31
Zeilen von e3 (Kettennummer), dazu e2 s6 v3, v4 mit neuem Original
bei gleicher id.
Ältere Nachzüge: 29.09. (Umbauskript
werkzeuge/einmalig/nachzug-skalarprodukt-und-winkel-2026-09-29.py),
Nachbesserung 30.09. früh (Antwortgerüst `__`, 70 Zeilen;
e1-k1-s1-v5 mit Urteil „Nein“).

## Originale je Einheit

- e1: 2024MerhoehtAAGLAA211-b, 2025MerhoehtAAGLAA211-a,
  2025MerhoehtAAGLAA211-b, 2024MgrundlegendBAGLAA1WTR-1f,
  2021MgrundlegendAAGLAA12-c (Prüfungshöhe)
- e2: 2026-bb-gk-B3b, 2019-be-gk-B3.2c (s2), 2018-bb-ea-B3.1c,
  2024-bebb-gk-B3b, 2021MgrundlegendBAGLAA2WTR2-1d,
  2023MerhoehtBAGLAA1WTR-2a und 2019-be-gk-B3.2c (Prüfungshöhe)
- e3: 2025-bebb-gk-B3c, 2024-bebb-gk-B3e, 2018-be-gk-B2.2c,
  2024MgrundlegendBAGLAA2WTR1-1c, 2022MerhoehtBAGLAA2WTR2-1d,
  2020MgrundlegendBAGLAA2WTR-1b, 2026MgrundlegendBAGLAA2WTR1-1e und
  2017-bb-ea-B3.1b (Prüfungshöhe)
- e4: 2023MgrundlegendBAGLAA2WTR1-1f, 2017-bb-ea-B3.2a,
  2023MerhoehtBAGLAA2WTR1-1d, 2018MerhoehtBAGLAA2CAS2-1f,
  2023MerhoehtBAnalysisWTR2-2e (Prüfungshöhe)

## Prüfskript vor der Korrektur (30.09.)

| Datei | Abw. | Warn. | häufigster Grund                          |
|-------|-----:|------:|-------------------------------------------|
| zone  |    0 |     0 | –                                         |
| e1    |    0 |     0 | –                                         |
| e2    |    4 |     0 | sprosse_text s6 nicht wortgleich in Z. 95 |
| e3    |    0 |     0 | –                                         |
| e4    |    0 |     0 | –                                         |

Nach dem ersten Wurf jeder Einheit 0 Abweichungen; keine Einheit
ist zweimal gescheitert.

## Entscheidungen

1. Sek-II-Päckchen (29.09.): e1 Quader A(1 | 2 | 0) … H(1 | 4 | 2),
   AG bleibt; e2 Zelt mit Spitze S(1 | 2 | 6), Kante SA bleibt; e3
   Pavillondach mit Spitze S(0 | 0 | 6), die xy-Ebene bleibt; e4
   Mastspitze S(2 | 3 | 8), der Boden bleibt; die zweite Größe
   wandert. Die Körper tragen nur Vorstufe s0 und Grundfall;
   spätere Sprossen bleiben wortgleich (Übernahme vor Körperregel).
2. 2019-be-gk-B3.2c steht zweimal: verfremdet an s2 v3 (der
   Katalog nennt es an der Trapezsprosse weiter) und mit zwei
   Zeilen an der Prüfungssprosse s6, weil die Katalogzeile 95 es
   dort als zweites Original nennt; die Aufgaben sind verschieden
   (Würfel 7 mit I–L; Würfel 6 mit M–P; Quader 8·6·5 mit U–X).
3. Der Erkennungsschritt „Welche zwei Richtungen …“ steht nach
   bank.md 30.09.b in e3 (Bereich „vor Einheit 2 bis 4“; e2 hat ihn
   als Vorstufe k2 s0, e3 und e4 haben „Kosinus oder Sinus?“, ein
   anderer Handgriff); die vier Zeilen decken die Fälle der
   Katalogzeile, die e2 nicht übt (Normale gegen Normale zweimal,
   Richtung gegen Normale zweimal), nicht noch einmal Kanten vom
   Scheitel weg.
4. „Der Formelwinkel oder sein Nachbar?“ bleibt in e2 als k1: e3
   hat den Handgriff in seiner Vorstufe („dazu … ankreuzen“), e2
   nicht – das ist die Regel vom 30.09.b.
5. Winkel als „Ergebnis: $\varphi \approx …^\circ$“, nicht „rund“;
   neue Lösungen tragen Schrittnamen (Vektoren, Skalarprodukt,
   Beträge, Kosinus, Ergebnis), übernommene bleiben ohne.
6. Pflichtformen (29.09.): e1 P2 und P3, e2–e4 P1 und P2;
   begruenden je Einheit „Begründe, warum …“, P4, P6; keine
   darstellung, e1 keine anwendung (die Typen tragen sie nicht).
7. bank/_punkte.csv nach dem letzten Bank-Commit mit
   `punkte-nachziehen.py 1c561b3 skalarprodukt-und-winkel`
   nachgezogen: 10 ids umbenannt (e3), 2 entfernt (e2 s6 v3, v4,
   neue Aufgabe bei gleicher id), keine Zeile eines anderen
   Eintrags berührt (am Diff geprüft).

## Befunde

- Katalog, Zeile 95 gegen Zeile 38: der Erkennungsschritt „Welche
  zwei Richtungen …“ und die Vorstufe der e2-Kette sind derselbe
  Handgriff; die Zeilen stehen einmal in e2 (k2 s0), der Schritt
  selbst nach der Regel 30.09.b in e3 (Katalogbefund nach bank.md:
  Erkennungsschritt Zeile 38; Vorstufe Zeile 95).
- Katalog, Zeile 39 gegen Zeile 96: „Der Formelwinkel …“ und die
  e3-Vorstufe („dazu … ankreuzen“) sind derselbe Handgriff; der
  Schritt steht in e2 (k1), in e3 entfällt er.
- Katalog, Zeile 95: 2019-be-gk-B3.2c steht an der Trapezsprosse
  und an der Prüfungshöhe derselben Kette; die Bank hält es an
  beiden Stellen (Entscheidung 2). Ist nur eine Stelle gemeint,
  ist die Prüfungshöhe die mit den zwei Zeilen.
- Prüfskript: „rund“ zählt nicht als Ergebnisstelle.
- Prüfskript: die Sperre zählt jede Körperecke einzeln; kleine
  Koordinaten treffen Tripel der Mappe, obwohl keine Figur gleich
  ist (29.09.; am 30.09. kein Treffer).
- werkzeuge/punkte-nachziehen.py entfernt jede csv-Zeile, deren id
  in der ganzen Bank fehlt, nicht nur bei den genannten Einträgen;
  bei parallelen Nachzügen kann das Zeilen anderer Einträge
  treffen, deren Skriptlauf noch aussteht – vor dem Commit den
  Diff prüfen.

## Offene Punkte

- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27.09.; die seit 29.09. umgeschriebenen und neuen Zeilen sind
  ungelesen.
- bank/_punkte.csv: e2 s6 v3 und v4 (2019-be-gk-B3.2c) brauchen
  ein neues Urteil; die vier Päckchenzeilen v5 (29.09.) ebenso.
- Sachbild-Aufgaben (e3 s3) stehen weiter ohne Grafik.
