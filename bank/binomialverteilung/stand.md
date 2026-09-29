# Stand: binomialverteilung

Katalog-Commit: f56cacecc590f51abf34cf81948a0d2b751d7d33
(2026-09-28, aus dem Kopf von mappen/binomialverteilung.md)
Datum: 2026-09-29 23:09 CEST (date)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.10
(--katalog aus der Mappe); Nachzug des Bestands vom 27./28.09.
(Katalog 95b0f8b). Umbauskript:
werkzeuge/einmalig/nachzug-binomialverteilung-2026-09-29.py.

## Zeilen je Datei und hoehe

    Datei  Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone       37         0        16      20        0       1
    e1         40         4         5      15        4      12
    e2         51         4         5      24        6      12
    e3         60         8         5      27        8      12
    e4         51         4         5      24        9       9
    e5         50         4         5      21        8      12

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         37      0              0          0
    e1           35      0              5          0
    e2           38      3             10          0
    e3           46      4             10          0
    e4           41      0             10          0
    e5           40      0             10          0

Umgeschrieben: die fünf Grundfallzeilen (e2–e5, Päckchen) und die
fehler- und begruenden-Zeilen v2, v3 sowie eine anwendung je Einheit
(Pflichtformen). Nachgezogen in allen übernommenen Zeilen: quelle
(125 → 122, 127–131 → 124–128), sprosse_text der Vorstufen (längerer
Sprossentext bis „nichts rechnen“), in e2 sprosse (ab 2 um eins
verschoben), in e3 kette_nr (um eins verschoben), dazu die id.
Zeilen mit original und neuer id: 32 (e2 12, e3 20); bank/_punkte.csv
nicht angefasst.

## Originale je Einheit

- e1: 2023-bebb-lk-A1.8a, 2022-bebb-gk-B4a, 2018-be-gk-B3.2g;
  Prüfungshöhe 2018MgrundlegendBStochastikWTR3-2d,
  2024MerhoehtAStochastik23-b.
- e2: 2017-be-gk-B3.1e, 2026MgrundlegendAStochastik12-a,
  2021MgrundlegendAStochastik2-a; Prüfungshöhe 2022-bebb-gk-B4b,
  2019-be-gk-B4.1a, 2018-bb-ea-B4.2c.
- e3: 2018-be-gk-B3.2a, 2018MerhoehtBStochastikWTR1-1a,
  2023-bebb-gk-B4.1d, 2017MerhoehtBStochastikCAS2-2,
  2017MerhoehtBStochastikCAS1-1b, 2023MgrundlegendBStochastikWTR2-2b;
  Prüfungshöhe 2022-bebb-lk-B4m, 2023MerhoehtBStochastikWTR3-1c,
  2024MgrundlegendAStochastik21-b, 2020MgrundlegendAStochastik2-b.
- e4: 2017-bb-ea-B4.2b, 2018-be-gk-B3.2d,
  2019MgrundlegendBStochastikWTR1-1b, 2017-be-gk-cas-B3.2d;
  Prüfungshöhe 2025MerhoehtAStochastik21, 2022-bebb-lk-B4f,
  2022MerhoehtBStochastikWTR1-1f.
- e5: 2017-be-gk-cas-B3.1e, 2023-bebb-gk-A1.7b; Prüfungshöhe
  2025-bebb-gk-A1.9b, 2021MgrundlegendAStochastik2-b,
  2022MgrundlegendBStochastikWTR2-3a, 2022-bebb-lk-A1.8b.

## Prüfskript vor der Korrektur

- Bestand vor dem Nachzug (v0.10 --katalog): 179 Abweichungen, alle
  „sprosse_text nicht wortgleich in Zeile“ (Zeilen verschoben).
- zone 0 / 0 (unverändert); e1 0 / 0; e2 0 / 0; e3 0 / 0; e4 0 / 0.
- e5 1 / 0: grafik leer bei einem Ableseauftrag („liest … ab“ in
  einer Fehler-Vorlage ohne Diagramm); Aufgabe umformuliert.
- Keine Einheit scheiterte zweimal.

## Entscheidungen

- Zone bleibt: Fertigkeiten (Zeilen 34–41) unverändert.
- Päckchen: e2 n = 6, p = 0,4 fest, k wandert; e3 n = 40 und die
  Zahl 12 fest, das Wort wandert; e4 p = 0,08 fest, die Schranke
  wandert; e5 dasselbe Diagramm (B(8; 0,35) gerundet), das Ereignis
  wandert.
- e1 Grundfall bleibt übernommen: die Katalogzeile verlangt vier
  Kontexte (Münze, Würfel, Glücksrad, Bevölkerung), ein festes p über
  fünf Kontexte trüge nicht.
- Erkennungsschritt „Treffer oder Niete gezählt?“ (Zeile 43) steht
  als eigene Kette e3 k1 (erste Einheit seines Bereichs, bank.md);
  in e5 bleibt die gleichnamige Vorstufe der Kette.
- Neue Sprosse e2 s2 „die ganze Verteilung für kleines n“ mit
  „k = 0:“ … als Zeilenkopf und „Kontrolle:“ als eigener Zeile.
- Schrittnamen (regeln.md 12) nur in neuen und umgeschriebenen
  Rechenzeilen; Anordnungsfaktor vorn mit Begründung (n über k).
- Pflichtformen: fehler v1 Schülerrechnung/-aussage, v2 fehlerfreie
  Vorlage (P2), v3 Serie (P1), in e4 Prüfzahl (P3); begruenden v1
  Warum-Frage, v2 Aussagenserie (P4), v3 Personenaussage (P6).
- Urteile: P6 zweimal Ja (e1, e5), dreimal Nein; P8 zweimal Ja
  (e3, e4), dreimal Nein.

## Befunde

- Katalog: die drei gestrichenen Erkennungsschritte (alt Zeilen
  43–45) stehen jetzt wortgleich als Vorstufen der Ketten; der vierte
  (Zeile 43) wiederholt die Vorstufe von e5 und steht vor e3 ohne
  Vorstufe – er bleibt dort als eigene Kette.
- Katalog: „Genau, höchstens oder mindestens?“ ist weiter Vorstufe
  von zwei Ketten (e2 und e3).
- Mappe: 2024-bebb-lk-A1.9a, 2021-be-gk-B4d,
  2023MgrundlegendBStochastikWTR1-2a und weitere Kennungen der
  Sprossen stehen nicht in Abschnitt 2; sie bleiben original null.
- Prüfskript: prüft die Pflichtformen P1–P8 nicht; die Formen sind
  nur durch Durchsicht gesichert.
- Prüfskript: „liest … ab“ in einer Fehler-Vorlage verlangt eine
  Grafik, auch wenn nur das Vorgehen einer Person geschildert wird.

## Offene Punkte

- e3: der zweistufige Prüfplan (Original nicht in der Mappe) hat
  keine eigene Zeile.
- Grundvorstellung (Zeile 122) steht nur als darstellung-Pflicht e1.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27./28.09. und sind nicht nachgezogen.
- bank/_punkte.csv braucht punkte-nachziehen.py für 32 ids.
