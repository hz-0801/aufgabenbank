# Stand: binomialverteilung

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/binomialverteilung.md)
Datum: 2026-09-30 08:58 UTC (date)
Grundlage: bank.md Stand 2026-09-30b, werkzeuge/bank-pruef.py v0.12
(--katalog aus der Mappe); Nachzug des Stands vom 29.09. (Katalog
f56cace) nach der Katalogänderung vom 30.09. (Zeile 152: Einheit 3
mit eigener Vorstufe „Mit oder ohne Gegenereignis?“) und der Mappe
mit den Kennungen der Sprossenketten in Abschnitt 2 (134 Originale
statt 77).

## Zeilen je Datei und hoehe

    Datei  Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone       37         0        16      20        0       1
    e1         40         4         5      15        4      12
    e2         51         4         5      24        6      12
    e3         64         8         5      27       12      12
    e4         50         4         5      24        8       9
    e5         52         4         5      21       10      12

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         37      0              0          0
    e1           38      0              2          0
    e2           47      0              4          0
    e3           54      4              6          0
    e4           43      0              7          1
    e5           43      2              7          0

Umgeschrieben heißt fast immer: nur das Feld original gesetzt und
die Prüfkennung ans Ende des Fragesatzes gestellt (bank.md, 3.6),
Aufgabe und Lösung sonst wortgleich (e1 2, e2 4, e3 2, e4 7, e5 7
Zeilen). Wirklich umgeschrieben sind die vier Vorstufenzeilen e3 k2
s0 (neue Vorstufe, Zeile 126, statt der wortgleichen Kopie von e2).
Neu: e3 k2 s9 v9–v12 (2021-be-gk-B4d,
2023MgrundlegendBStochastikWTR1-2a), e5 k1 s8 v9–v10
(2021MgrundlegendBStochastikWTR1-1c). Entfallen: e4 k1 s9 v9 (dritte
Zeile „p aus zwei Einzelwahrscheinlichkeiten“; die Sprosse trägt
jetzt 2019MerhoehtAStochastik11-b mit zwei Zeilen v7, v8). Keine id
umbenannt; punkte-nachziehen.py nicht nötig.

## Originale je Einheit

- e1: 2024-bebb-lk-A1.9a (neu, s3), 2023-bebb-lk-A1.8a,
  2022-bebb-gk-B4a, 2018-be-gk-B3.2g; Prüfungshöhe
  2018MgrundlegendBStochastikWTR3-2d, 2024MerhoehtAStochastik23-b.
- e2: 2017-be-gk-B3.1e, 2018-bb-ea-B4.2b (neu, s5),
  2026MgrundlegendAStochastik12-a, 2021MgrundlegendAStochastik2-a,
  2025-bebb-lk-B4a (neu, s8); Prüfungshöhe 2022-bebb-gk-B4b,
  2019-be-gk-B4.1a, 2018-bb-ea-B4.2c.
- e3: 2020MgrundlegendBStochastikWTR1-1a (neu, s3 v1),
  2022-bebb-lk-B4k (neu, s3 v2), 2018-be-gk-B3.2a,
  2018MerhoehtBStochastikWTR1-1a, 2023-bebb-gk-B4.1d,
  2017MerhoehtBStochastikCAS2-2, 2017MerhoehtBStochastikCAS1-1b,
  2023MgrundlegendBStochastikWTR2-2b (k3); Prüfungshöhe
  2022-bebb-lk-B4m, 2023MerhoehtBStochastikWTR3-1c,
  2024MgrundlegendAStochastik21-b, 2020MgrundlegendAStochastik2-b,
  2021-be-gk-B4d (neu), 2023MgrundlegendBStochastikWTR1-2a (neu) –
  alle sechs Kennungen der Katalogzeile, zwölf Zeilen.
- e4: 2017-bb-ea-B4.2b, 2018-be-gk-B3.2d, 2023-bebb-lk-B4h (neu,
  s5), 2021MgrundlegendBStochastikWTR2-1d (neu, s7 v1),
  2022MgrundlegendBStochastikWTR2-2b (neu, s7 v2), 2018-be-gk-B3.2c
  (neu, s8 v1), 2019MgrundlegendBStochastikWTR1-1b,
  2017-be-gk-cas-B3.2d (k2); Prüfungshöhe 2025MerhoehtAStochastik21,
  2022-bebb-lk-B4f, 2022MerhoehtBStochastikWTR1-1f,
  2019MerhoehtAStochastik11-b (neu) – alle vier Kennungen, acht
  Zeilen.
- e5: 2017-be-gk-cas-B3.1e, 2025-bebb-gk-B4c (neu, s3),
  2023-bebb-gk-A1.7b, 2026-bb-gk-B4c (neu, s5 v1),
  2024MerhoehtAStochastik23-a (neu, s5 v2),
  2019MerhoehtAStochastik11-a (neu, s6 v2),
  2021MerhoehtAStochastik12-b (neu, s7); Prüfungshöhe
  2025-bebb-gk-A1.9b, 2021MgrundlegendAStochastik2-b,
  2022MgrundlegendBStochastikWTR2-3a, 2022-bebb-lk-A1.8b,
  2021MgrundlegendBStochastikWTR1-1c (neu) – alle fünf Kennungen,
  zehn Zeilen.

## Prüfskript vor der Korrektur

- Bestand vor dem Nachzug (v0.12 --katalog): 4 Abweichungen, alle
  e3 k2 s0 „sprosse_text nicht wortgleich in Zeile 126“ (die alte
  Vorstufe); 0 Warnungen, Formprobe 0.
- zone, e1, e2, e4: 0 / 0. e3: 1 / 0 (ein Zwischenwert der
  Prüfplan-Lösung stand nach „·“, nicht an einer Ergebnisstelle; aus
  pruef genommen). e5: 2 / 0 („pruef fehlt“ bei den zwei
  Beurteilungszeilen mit Ziffern in der Lösung; die Säulensumme als
  „P(X ≤ 1) ≈ …“ in die Lösung gestellt, pruef gesetzt).
- Danach 0 / 0 in allen Dateien, Formprobe 0. Keine Einheit
  scheiterte zweimal.

## Entscheidungen

- Zone bleibt: Fertigkeiten (Zeilen 34–41) unverändert.
- Neue Vorstufe e3: vier Ankreuzzeilen mit je drei Optionen der Form
  „direkt: P(X ≤ k)“ / „Gegenereignis: 1 − P(X ≤ k)“; die Lösung
  nennt die Option wortgleich, pruef leer. Die vier alten Zeilen
  (Kopie von e2 s0) sind ersetzt, nicht ergänzt.
- Originale mitten in der Kette: wo die vorhandenen Zeilen v1/v2
  einer Sprosse dasselbe Verfahren und dieselbe Falle wie die erste
  Kennung der Katalogzeile tragen, ist das Feld original gesetzt und
  die Prüfkennung angehängt – Übernahme statt Neuschreiben (22
  Zeilen). Nicht gesetzt, wo die Falle fehlt (e3 s2 „höchstens“
  gegen 2026-bb-gk-B4b „weniger als“; e4 s4 v1 „≥“ gegen
  2025-bebb-gk-B4d „mehr als“) oder das Verfahren nur teils passt
  (e2 s9, e4 s8 v2, e5 s6 v1). Zwei Sprossen tragen je Zeile ein
  anderes Original (e3 s3, e4 s7), weil jede Zeile genau einem
  entspricht.
- e2 s4 behält 2017-be-gk-B3.1e (kein Treffer als Potenz), obwohl
  die Katalogzeile 2018-bb-ea-B4.2b und 2020-be-gk-B4.1a nennt; die
  Zeilen verfremden das Berliner Original, das in der Mappe steht.
- Prüfungssprosse e4: 2019MerhoehtAStochastik11-b an die zwei
  vorhandenen Zeilen v7, v8 (Gleichung zweier
  Einzelwahrscheinlichkeiten ohne Rechner); v9 entfällt (zwei Zeilen
  je Original).
- Erkennungsschritt „Treffer oder Niete gezählt?“ (Zeile 43) bleibt
  als eigene Kette e3 k1; die gleichnamige Vorstufe e5 k1 s0 bleibt
  auch. Lesart von bank.md 30.09.b: der Erkennungsschritt füllt die
  Einheit ohne solche Vorstufe (e3), die Einheit mit Vorstufe (e5)
  behält sie; die Regel „zwei Ketten mit Vorstufen desselben
  Handgriffs“ lese ich als Regel für zwei Verfahrensketten, nicht
  für Erkennungsschritt gegen Vorstufe.
- Neue Lösungen mit Schrittnamen (regeln.md 12): „Erfolg einer
  Spielerin:“, „erster Schritt:“, „zweiter Schritt:“, „Ergebnis:“;
  in den Beurteilungszeilen das Urteil vorn („falsch (I): …; wahr
  (II): …“), je eine Aussage wahr und eine falsch.
- muster.md unverändert (Grundfälle unverändert).

## Befunde

- Katalog: Erkennungsschritt Zeile 43 und Vorstufe e5 (Zeile 128)
  sind derselbe Handgriff an derselben Vorlage (Diagramm); nach
  bank.md 30.09.b gehört der Fall hierher (beide Stellen: Zeile 43,
  Zeile 128). Ob die Vorstufe in e5 entfallen soll, muss der Chat
  entscheiden; hier bleibt sie.
- bank.md: für ein Original mitten in der Kette ist keine Zeilenzahl
  festgelegt (Prüfungshöhe: zwei je Original); hier tragen es ein
  oder zwei Zeilen je Sprosse.
- Prüfskript: „pruef fehlt“ trifft auch Beurteilungszeilen, deren
  Lösung nur Vergleichszahlen nennt (Säulensumme, Erwartungswert);
  die Lösung musste eine Ergebnisstelle bekommen.
- Prüfskript: prüft die Pflichtformen P1–P8 nicht (unverändert).
- bank/_punkte.csv: 28 Zeilen dieses Eintrags mit original haben
  kein Urteil (22 nachgetragene, 6 neue); punkte.py meldet sie als
  „ohne Urteil“. Nicht angefasst (außerhalb des Ordners).

## Offene Punkte

- Grundvorstellung (Zeile 122) steht nur als darstellung-Pflicht e1.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27./28.09. und sind nicht nachgezogen.
- Urteile für die 28 Zeilen in bank/_punkte.csv (Lesestoff über
  `punkte.py --lesestoff DIR --nur-neu`).
