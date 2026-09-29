# Stand: vektoren-und-rechenoperationen

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719 (Mappe vom
29.09., 17:58 UTC)
Datum: 2026-09-29 21:54 CEST
Vorlage auftrag-eintrag.md 2026-09-29e; Nachzug des Bestands vom
27./28.09. Prüfskript v0.10 mit `--katalog`: alle Dateien
0 Abweichungen, 0 Warnungen.
Umbauskript: werkzeuge/einmalig/
nachzug-vektoren-und-rechenoperationen-2026-09-29.py.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     27 |        – |        12 |      14 |        – |       1 |
| e1    |     41 |        8 |         5 |      12 |        4 |      12 |
| e2    |     46 |        4 |         5 |      21 |        4 |      12 |
| e3    |     23 |        4 |         5 |       3 |        2 |       9 |

Vorstufen: e1 k1 Erkennungsschritt (4) und k2 s0 (4); e2 k1 s0;
e3 k1 s0. Keine Kette hat Vorstufen −1 oder −2.

## Nachzug je Einheit

| Datei | übernommen | neu | umgeschrieben | entfallen |
|-------|-----------:|----:|--------------:|----------:|
| zone  |         27 |   0 |             0 |         0 |
| e1    |         31 |   0 |            10 |         0 |
| e2    |         37 |   3 |             6 |         0 |
| e3    |         13 |   0 |            10 |         0 |

Übernommen: Aufgabe und Lösung wortgleich, nachgezogen quelle
(37 → 35, 80 → 78, 83–85 → 81–83), bei den Vorstufen der längere
sprosse_text, in e2 sprosse und id ab s3 (+1). Neu: e2 k1 s3
(zwei Kantenwege, ein Vektor). Umgeschrieben: die Päckchen e1 und
e3 (je 5) und die Pflichtzeilen, die eine fehlende Form herstellen.
ids mit original: 11 von 25 geändert (e2 k1 s3–s8 → s4–s9);
bank/_punkte.csv ist nicht angefasst.

## Originale je Einheit

- e1: 2025MerhoehtAAGLAA11-a, 2021MgrundlegendAAGLAA112-a,
  2025MerhoehtBAGLAA1WTR-2b, 2022MerhoehtBAGLAA2WTR2-1f;
  Prüfungshöhe 2024MgrundlegendBAGLAA1WTR-1e,
  2025MerhoehtBAGLAA1MMS-1a
- e2: 2021MgrundlegendAAGLAA12-b, 2026MgrundlegendBAGLAA2MMS2-1a,
  2021MgrundlegendAAGLAA12-a, 2026MerhoehtBAGLAA1WTR-1a,
  2022MerhoehtBAGLAA1WTR-1b, 2017MgrundlegendBAGLAA2WTR2-1c,
  2017MerhoehtBAGLAA2WTR1-1b, 2024MgrundlegendAAGLAA211-b,
  2019MerhoehtAAGLAA21-b, 2022MerhoehtAAGLAA221-b;
  Prüfungshöhe 2026MgrundlegendAAGLAA222-b, 2025MerhoehtAAGLAA223-b
- e3: 2019MgrundlegendBAGLAA2WTR2-1d; Prüfungshöhe
  2019MgrundlegendBAGLAA2WTR2-1e

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                |
|-------|-------------:|----------:|---------------------------------|
| zone  |            0 |         0 | –                               |
| e1    |            0 |         0 | –                               |
| e2    |            1 |         0 | pruef fehlt (Bruch in s3 v3)    |
| e3    |            0 |         0 | –                               |

Der alte Bestand gegen die neue Mappe: 86 Abweichungen, alle
„sprosse_text nicht wortgleich in Zeile quelle“ (Zeilen um zwei
verschoben). Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Päckchen e1 am festen Quader A(2 | 1 | 0) … H(2 | 4 | 3): A
   bleibt Fuß, die Zielecke wandert (C, F, G, H, B).
2. Päckchen e2 unverändert: der Bestand nutzt schon einen festen
   Quader (6 × 4 × 3), der Termweg wandert; übernommen.
3. Päckchen e3: dasselbe Eiscafé, Vanille 24 und Erdbeere 18
   bleiben, Schoko wandert je Wochentag.
4. Die neue Sprosse e2 s3 steht in der Kettenfolge der Mappe nach
   der Lagebeschreibung; die späteren Sprossen rücken um eins.
5. Der Erkennungsschritt „Faktor gesucht oder Richtung gesucht?“
   bleibt in e1 (fragt, was fehlt; die Vorstufe „Zahl oder Pfeil?“
   fragt, was eine Größe ist – kein gleicher Handgriff).
6. Umgeschrieben statt ergänzt: je Einheit die fehler- und
   begruenden-Zeilen, deren Form doppelt war; in e2 die erste
   anwendung zur P8-Entscheidung (Lampe über Kopfhöhe).
7. Urteile: P6 e1–e3 je „Ja“, P8 e1 und e2 „Nein“, e3 „Nein“ und
   „Ja“; P2 je „Richtig.“ – zusammen mit den Serien etwa halbe-halbe.
8. muster.md mit eigenen Punkten außerhalb der Päckchen und der
   Sperre (e2: Kante AB = 5, weil (4 | 0 | 0) gesperrt ist).

## Befunde

- Katalog: „Faktor gesucht oder Richtung gesucht?“ (Z. 35) und die
  Vorstufe „Zahl oder Pfeil?“ (Z. 81) liegen nah beieinander; ein
  Schüler übt zweimal das Ankreuzen Zahl gegen Richtung.
- Katalog: die Landeszeile 2018-bb-ea-B3.2c trägt keine eigene
  Sprosse; ihre Lage deckt e2 s2 über den iqb-Zwilling.
- Auftrag: die Schrittnamenpflicht gilt für neue und umgeschriebene
  Lösungen; Urteils- und Begründungslösungen haben keine
  Rechenzeilen, dort steht nur das Urteil vorn.
- Prüfskript: bei Tripeln aus Termwegen (Kantenfaktoren) prüft
  pruef nur Brüche; die Richtigkeit von u, v, w-Termen prüft kein
  Skript.

## Offene Punkte

- Die Gegenlese-Befunde vom 27./28.09. zu übernommenen Zeilen sind
  nicht eingearbeitet (e1 k3 s3 v2 „Pfeil zu“, e3 k2 s3 sprosse_text,
  e1 k3 s4 v2 Rundung, e3 k1 s3 v1 Kontext wie das Original).
- ksys3-Grafiken ungerendert (kein LaTeX in der Sitzung).
- bank/_punkte.csv braucht `werkzeuge/punkte-nachziehen.py` für die
  11 geänderten ids.
