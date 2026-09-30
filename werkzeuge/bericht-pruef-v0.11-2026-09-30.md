# Bericht bank-pruef.py v0.11 (2026-09-30)

Auftrag: Formprobe P1–P8, Punktschreibweise (4; 1), Winkel „rund …°“, Urteilszählung. Modell: Claude Opus 5.5. Alle Zahlen aus Skriptausgaben (Lauf je Eintrag mit `--katalog`, Klon vom 30.09., Stand vor diesem Commit 0f1ee71).

## Gegenprobe mit bekannten Werten

```
v0.10: zahlenpaare('$Q(4; 1)$') = []; ergebnis_zahlen(T) = ['0.8']; vergleiche('36.87', T) = ['36.87 nicht an der Ergebnisstelle (nur im Text; Ergebnisstelle: 0.8)']
v0.11: zahlenpaare('$Q(4; 1)$') = [('Punkt', '4', '1')]; ergebnis_zahlen(T) = ['0.8', '37']; vergleiche('36.87', T) = []
T = '$\cos\varphi = 0{,}8$, der Winkel ist also rund $37^\circ$.'
```

`--selbsttest`: bestanden; `_basis`: Abweichungen 0, Warnungen 0 (wie v0.10).

## Summen über 72 Einträge

| | Abweichungen | Warnungen | Formprobe |
|---|---|---|---|
| v0.10 mit `--katalog` (Ausgangswert) | 315 | 2 | – |
| v0.11 mit `--katalog` (Endwert) | 439 | 2 | 882 |
| v0.10 ohne `--katalog` | 6 | 2 | – |
| v0.11 ohne `--katalog` | 130 | 2 | 882 |

Der Ausgangswert war nicht 0/0: Die Bank hat 72 Einträge (nicht 73), und v0.10 meldet ohne `--katalog` 6 Abweichungen und 2 Warnungen (binomische-formeln 4 × „grafik leer“, `weg.jsonl` in lineare-gleichungen und quadratische-funktionen als Dateiname, je 1 Mengenwarnung in punkte-und-strecken-im-koordinatensystem und zuordnungen), mit `--katalog` zusätzlich 309 Katalog-Abweichungen („sprosse_text nicht wortgleich“) in 9 Einträgen. Diese Werte sind in v0.11 unverändert; alle 124 neuen Abweichungen stammen aus (b), keine aus (c).

## Tabelle je Eintrag

Abw./Warn. mit `--katalog`, v0.10 → v0.11; Urteile aus v0.11.

| Eintrag | Abw. v0.10 | Abw. v0.11 | Warn. | Formprobe | ja | nein | richtig | falsch | offen | sonst |
|---|---|---|---|---|---|---|---|---|---|---|
| ableitung-und-aenderungsrate | 0 | 0 | 0 | 0 | 11 | 10 | 4 | 0 | 0 | 8 |
| ableitungsregeln | 0 | 0 | 0 | 0 | 5 | 7 | 3 | 0 | 0 | 2 |
| abstaende | 0 | 8 | 0 | 0 | 8 | 9 | 4 | 0 | 0 | 10 |
| bedingte-wahrscheinlichkeit-und-bayes | 12 | 12 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 14 |
| binomialverteilung | 0 | 0 | 0 | 0 | 14 | 12 | 5 | 0 | 0 | 9 |
| binomische-formeln | 4 | 4 | 0 | 0 | 9 | 9 | 3 | 0 | 0 | 4 |
| bruchrechnung | 0 | 0 | 0 | 0 | 18 | 19 | 5 | 0 | 0 | 2 |
| brueche-dezimalzahlen | 0 | 0 | 0 | 1 | 16 | 13 | 5 | 0 | 0 | 0 |
| daten | 0 | 0 | 0 | 40 | 5 | 9 | 0 | 0 | 0 | 25 |
| ebenen | 0 | 14 | 0 | 1 | 17 | 14 | 4 | 0 | 0 | 10 |
| einheiten | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 9 |
| extremalprobleme | 0 | 6 | 0 | 0 | 8 | 6 | 3 | 0 | 0 | 1 |
| flaechen | 0 | 0 | 0 | 30 | 1 | 4 | 0 | 0 | 0 | 6 |
| flaecheninhalt-durch-integration | 0 | 0 | 0 | 0 | 14 | 13 | 5 | 0 | 0 | 6 |
| flaecheninhalt-und-volumen-im-raum | 0 | 12 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 3 |
| funktionsklassen-und-eigenschaften | 0 | 2 | 0 | 1 | 16 | 18 | 7 | 2 | 0 | 11 |
| funktionsscharen-und-ortskurven | 0 | 0 | 0 | 27 | 0 | 0 | 0 | 0 | 0 | 0 |
| geraden | 0 | 33 | 0 | 0 | 9 | 12 | 4 | 0 | 0 | 16 |
| gleichungen-loesen | 21 | 21 | 0 | 21 | 0 | 1 | 0 | 0 | 0 | 0 |
| grenzwerte-und-verhalten-im-unendlichen | 12 | 12 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 |
| hypergeometrische-verteilung | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 |
| hypothesentests | 12 | 12 | 0 | 17 | 0 | 0 | 0 | 1 | 0 | 0 |
| integrationsregeln | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| kenngroessen-von-verteilungen | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 | 0 | 4 |
| koerper | 0 | 0 | 0 | 25 | 3 | 3 | 0 | 0 | 0 | 16 |
| kombinatorik | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 11 |
| konfidenzintervalle | 0 | 0 | 0 | 14 | 0 | 1 | 0 | 0 | 0 | 5 |
| kreis | 0 | 0 | 0 | 13 | 1 | 1 | 0 | 0 | 0 | 6 |
| kurvenuntersuchung | 0 | 0 | 0 | 4 | 13 | 10 | 5 | 0 | 0 | 6 |
| lagebeziehungen | 0 | 14 | 0 | 0 | 9 | 12 | 4 | 0 | 0 | 24 |
| lineare-funktionen | 0 | 0 | 0 | 20 | 8 | 11 | 0 | 0 | 0 | 10 |
| lineare-gleichungen | 1 | 1 | 0 | 0 | 5 | 12 | 4 | 0 | 0 | 14 |
| lineare-gleichungssysteme | 0 | 0 | 0 | 24 | 0 | 1 | 0 | 0 | 0 | 3 |
| linearkombination-und-lineare-abhaengigkeit | 0 | 0 | 0 | 5 | 3 | 2 | 0 | 0 | 0 | 11 |
| matrizen-und-uebergangsprozesse | 0 | 0 | 0 | 24 | 6 | 5 | 0 | 0 | 0 | 2 |
| normalverteilung-und-sigma-regeln | 0 | 0 | 0 | 15 | 0 | 2 | 0 | 1 | 0 | 4 |
| orthogonalitaet | 4 | 7 | 0 | 23 | 3 | 1 | 0 | 0 | 0 | 2 |
| potenz-exponentialfunktionen | 0 | 0 | 0 | 25 | 2 | 3 | 0 | 1 | 0 | 17 |
| potenzen-wurzeln | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| prozentrechnung | 0 | 0 | 0 | 4 | 17 | 12 | 5 | 0 | 0 | 2 |
| punkte-und-strecken-im-koordinatensystem | 0 | 0 | 1 | 25 | 0 | 0 | 0 | 0 | 0 | 9 |
| pyramide-kegel-kugel | 0 | 0 | 0 | 12 | 1 | 1 | 0 | 0 | 0 | 17 |
| pythagoras | 0 | 0 | 0 | 0 | 13 | 14 | 1 | 0 | 0 | 8 |
| quadratische-funktionen | 1 | 1 | 0 | 25 | 0 | 1 | 0 | 0 | 0 | 23 |
| quadratische-gleichungen | 195 | 195 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 17 |
| rationale-zahlen | 0 | 0 | 0 | 0 | 8 | 12 | 4 | 0 | 0 | 11 |
| reelle-zahlen | 0 | 0 | 0 | 18 | 2 | 1 | 0 | 0 | 0 | 16 |
| rekonstruktion-von-bestaenden | 0 | 0 | 0 | 17 | 1 | 1 | 0 | 0 | 0 | 3 |
| rekonstruktion-von-funktionsgleichungen | 0 | 11 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 7 |
| rotationsvolumen | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 4 |
| scharen-von-geraden-und-ebenen | 10 | 15 | 0 | 20 | 3 | 3 | 0 | 2 | 0 | 1 |
| schnittmengen | 0 | 4 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 3 |
| skalarprodukt-und-winkel | 0 | 2 | 0 | 0 | 6 | 10 | 4 | 0 | 0 | 13 |
| spiegelung | 4 | 5 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 2 |
| stammfunktion-und-hauptsatz | 0 | 0 | 0 | 0 | 11 | 9 | 4 | 0 | 0 | 0 |
| strahlensaetze | 0 | 0 | 0 | 15 | 0 | 2 | 0 | 0 | 0 | 16 |
| symmetrie-abbildungen | 39 | 39 | 0 | 18 | 1 | 2 | 0 | 0 | 0 | 0 |
| tangente-normale-schnittwinkel | 0 | 6 | 0 | 1 | 15 | 10 | 5 | 0 | 0 | 3 |
| terme | 0 | 0 | 0 | 0 | 11 | 10 | 4 | 0 | 0 | 0 |
| trigonometrie | 0 | 0 | 0 | 20 | 2 | 4 | 0 | 0 | 0 | 15 |
| trigonometrische-funktionen | 0 | 0 | 0 | 19 | 2 | 1 | 0 | 0 | 0 | 8 |
| umkehrfunktion | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 4 |
| unabhaengigkeit | 0 | 0 | 0 | 16 | 0 | 1 | 0 | 0 | 0 | 19 |
| uneigentliche-integrale | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| vektoren-und-rechenoperationen | 0 | 2 | 0 | 0 | 10 | 5 | 3 | 0 | 0 | 4 |
| vierfeldertafel | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| wahrscheinlichkeit | 0 | 0 | 0 | 21 | 5 | 7 | 0 | 0 | 0 | 5 |
| winkel-dreiecke | 0 | 0 | 0 | 27 | 0 | 7 | 0 | 0 | 0 | 0 |
| zinsrechnung | 0 | 0 | 0 | 8 | 1 | 4 | 0 | 0 | 0 | 0 |
| zufallsexperimente-und-pfadregeln | 0 | 1 | 0 | 1 | 21 | 17 | 8 | 0 | 0 | 10 |
| zufallsgroessen-und-verteilungen | 0 | 0 | 0 | 12 | 1 | 2 | 0 | 0 | 0 | 0 |
| zuordnungen | 0 | 0 | 1 | 20 | 2 | 8 | 0 | 0 | 0 | 14 |
| **Summe** | 315 | 439 | 2 | 882 | 337 | 364 | 103 | 7 | 0 | 505 |

„sonst“: Urteilsfrage, deren loesung nicht mit einem Urteilswort beginnt (meist Rechnung zuerst, Urteil am Ende). P4 zählt je Aussage (wahr = ja, falsch = nein).

## Neue Abweichungen aus (b) Punktschreibweise

124 Zeilen in 16 Einträgen, alle „Sperre“. Ursache: Die Mappen schreiben Punkte der Originale (vor allem IQB und Landesabitur) mit Semikolon – 1 156 Stellen in mappen/ –, die v0.10 nicht las; die Sperre auf diese Originale war bisher blind. Aus (c) keine neue Abweichung (189 Zeilen haben einen Winkel-Treffer in loesung; keine davon wich in v0.10 ab).

Zwei Fehltreffer im ersten Anlauf wurden im Skript behoben: Matrizen zeilenweise „((2; 2), (3; 0))“ (27 Zeilen in matrizen-und-uebergangsprozesse) und Punkte nur aus 0, 1, −1 wie (0|0|1), (0|1|1) (26 weitere Treffer). Danach 124.

| id | Befund | Urteil |
|---|---|---|
| abstaende-zone-f1-v1 | Sperre: Tripel (1|2|3) (Original 2022-bebb-lk-A1.5b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|2|3) |
| abstaende-zone-f5-v1 | Sperre: Tripel (1|2|3) (Original 2022-bebb-lk-A1.5b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|2|3) |
| abstaende-e1-k3-s1-v1 | Sperre: Tripel (1|2|3) (Original 2022-bebb-lk-A1.5b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|2|3) |
| abstaende-e2-k2-s1-v3 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1g) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| abstaende-e3-k1-s1-v4 | Sperre: Tripel (2|0|3) (Original 2018MerhoehtBAGLAA2WTR3-1c) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|0|3) |
| abstaende-e3-k1-s4-v2 | Sperre: Tripel (0|2|1) (Original 2026-bb-ea-A1.8b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 0|2|1) |
| abstaende-e3-k1-s7-v2 | Sperre: Tripel (1|3|0) (Original 2017MgrundlegendAAGLAA22-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|3|0) |
| abstaende-e4-k1-s6-v1 | Sperre: Tripel (0|2|1) (Original 2026-bb-ea-A1.8b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 0|2|1) |
| ebenen-e1-k1-s1-v1 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| ebenen-e1-k1-s1-v2 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| ebenen-e1-k1-s1-v3 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| ebenen-e1-k1-s1-v4 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| ebenen-e1-k1-s1-v5 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| ebenen-e1-k1-s2-v1 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1d) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| ebenen-e1-k1-s3-v3 | Sperre: Tripel (2|1|2) (Original 2022MerhoehtAAGLAA222-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|1|2) |
| ebenen-e1-k1-s5-v3 | Sperre: Tripel (2|1|1) (Original 2022MerhoehtAAGLAA222-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|1|1) |
| ebenen-e2-k1-s4-v2 | Sperre: Tripel (2|6|1) (Original 2017MgrundlegendBAGLAA2WTR2-1d) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|6|1) |
| ebenen-e2-k2-s4-v2 | Sperre: Tripel (2|1|1) (Original 2022MerhoehtAAGLAA222-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|1|1) |
| ebenen-e2-k2-s5-v2 | Sperre: Tripel (2|1|1) (Original 2022MerhoehtAAGLAA222-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|1|1) |
| ebenen-e3-k1-s8-v1 | Sperre: Tripel (2|6|1) (Original 2017MgrundlegendBAGLAA2WTR2-1d) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|6|1) |
| ebenen-e4-k1-s1-v3 | Sperre: Tripel (2|1|2) (Original 2022MerhoehtAAGLAA222-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|1|2) |
| ebenen-e4-k3-s1-v1 | Sperre: Tripel (2|1|1) (Original 2022MerhoehtAAGLAA222-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|1|1) |
| extremalprobleme-zone-f2-v4 | Sperre: Zahlenpaar (2|0) (Original 2023-A-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| extremalprobleme-e1-k1-s2-v2 | Sperre: Zahlenpaar (2|0) (Original 2023-A-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| extremalprobleme-e1-k1-s4-v3 | Sperre: Zahlenpaar (2|0) (Original 2023-A-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| extremalprobleme-e1-k1-s5-v3 | Sperre: Zahlenpaar (2|0) (Original 2023-A-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| extremalprobleme-e1-k1-s5-v4 | Sperre: Zahlenpaar (2|0) (Original 2023-A-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| extremalprobleme-e3-k2-s1-v1 | Sperre: Zahlenpaar (2|0) (Original 2023-A-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e1-k2-s1-v2 | Sperre: Tripel (2|0|1) (Original 2024MgrundlegendAAGLAA221) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|0|1) |
| flaecheninhalt-und-volumen-im-raum-e1-k2-s1-v3 | Sperre: Tripel (0|0|3) (Original 2026MgrundlegendAAGLAA213-c) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|3); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e1-k2-s5-v3 | Sperre: Tripel (0|0|5) (Original 2017MgrundlegendBAGLAA2CAS1-1d); Sperre: Tripel (6|0|0) (Original 2026MgrundlegendAAGLAA213-c) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|5, 6|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e2-k1-s2-v3 | Sperre: Tripel (6|0|3) (Original 2026MerhoehtAAGLAA212-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 6|0|3) |
| flaecheninhalt-und-volumen-im-raum-e2-k1-s5-v2 | Sperre: Tripel (2|0|1) (Original 2024MgrundlegendAAGLAA221) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|0|1) |
| flaecheninhalt-und-volumen-im-raum-e2-k3-s4-v3 | Sperre: Tripel (0|0|5) (Original 2017MgrundlegendBAGLAA2CAS1-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|5); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e3-k1-s1-v1 | Sperre: Tripel (5|5|0) (Original 2017MgrundlegendBAGLAA2CAS2-1c) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 5|5|0) |
| flaecheninhalt-und-volumen-im-raum-e3-k1-s2-v1 | Sperre: Tripel (6|0|0) (Original 2026MgrundlegendAAGLAA213-c) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (6|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e3-k1-s3-v1 | Sperre: Tripel (0|0|5) (Original 2017MgrundlegendBAGLAA2CAS1-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|5); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e4-k1-s7-v1 | Sperre: Tripel (0|0|5) (Original 2017MgrundlegendBAGLAA2CAS1-1d); Sperre: Tripel (6|0|0) (Original 2026MgrundlegendAAGLAA213-c) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|5, 6|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e4-k1-s7-v2 | Sperre: Tripel (0|0|10) (Original 2026MgrundlegendAAGLAA111-b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|10); ob frei wie der Ursprung, entscheidet der Chat |
| flaecheninhalt-und-volumen-im-raum-e4-k1-s7-v3 | Sperre: Tripel (0|0|3) (Original 2026MgrundlegendAAGLAA213-c) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|3); ob frei wie der Ursprung, entscheidet der Chat |
| funktionsklassen-und-eigenschaften-e1-k1-s8-v2 | Sperre: Zahlenpaar (2|5) (Original 2017MgrundlegendBAnalysisWTR-2b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|5) |
| funktionsklassen-und-eigenschaften-e5-k2-s1-v2 | Sperre: Zahlenpaar (2|5) (Original 2017MgrundlegendBAnalysisWTR-2b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|5) |
| geraden-zone-f2-v4 | Sperre: Tripel (1|2|2) (Original 2023MerhoehtAAGLAA212-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|2|2) |
| geraden-zone-f3-v2 | Sperre: Tripel (3|-1|2) (Original 2022MgrundlegendAAGLAA213-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|-1|2) |
| geraden-zone-f3-v4 | Sperre: Tripel (2|-3|1) (Original 2021MerhoehtAAGLAA112-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-3|1) |
| geraden-zone-f5-v2 | Sperre: Tripel (2|4|-2) (Original 2025MgrundlegendBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|4|-2) |
| geraden-zone-f5-v4 | Sperre: Tripel (2|-3|1) (Original 2021MerhoehtAAGLAA112-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-3|1) |
| geraden-e1-k2-s3-v2 | Sperre: Tripel (2|3|1) (Original 2021MerhoehtAAGLAA112-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|3|1) |
| geraden-e1-k2-s5-v1 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e2-k1-s1-v1 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e2-k1-s1-v2 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e2-k1-s1-v3 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e2-k1-s1-v4 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e2-k1-s1-v5 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e2-k1-s4-v3 | Sperre: Tripel (1|2|2) (Original 2023MerhoehtAAGLAA212-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|2|2) |
| geraden-e2-k1-s6-v1 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e2-k1-s8-v1 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e2-k2-s1-v3 | Sperre: Tripel (1|2|2) (Original 2023MerhoehtAAGLAA212-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|2|2) |
| geraden-e3-k1-s-1-v1 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s-1-v2 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s-1-v3 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s-1-v4 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s1-v1 | Sperre: Tripel (4|3|0) (Original 2025-bebb-gk-A1.2a); Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 4|3|0) |
| geraden-e3-k1-s1-v2 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s1-v3 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s1-v4 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s1-v5 | Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (5|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s2-v1 | Sperre: Tripel (2|-1|3) (Original 2025-bebb-lk-A1.7a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|3) |
| geraden-e3-k1-s4-v1 | Sperre: Tripel (5|5|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f); Sperre: Tripel (5|0|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f); Sperre: Tripel (0|5|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 5|5|0) |
| geraden-e3-k1-s4-v3 | Sperre: Tripel (0|5|0) (Original 2017MgrundlegendBAGLAA2CAS2-1f) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|5|0); ob frei wie der Ursprung, entscheidet der Chat |
| geraden-e3-k1-s5-v2 | Sperre: Tripel (3|-1|2) (Original 2022MgrundlegendAAGLAA213-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|-1|2) |
| geraden-e3-k1-s6-v1 | Sperre: Tripel (2|0|1) (Original 2022MgrundlegendAAGLAA213-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|0|1) |
| geraden-e3-k2-s1-v2 | Sperre: Tripel (2|0|1) (Original 2022MgrundlegendAAGLAA213-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|0|1) |
| geraden-e3-k2-s1-v3 | Sperre: Tripel (2|3|1) (Original 2021MerhoehtAAGLAA112-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|3|1) |
| geraden-e4-k1-s2-v2 | Sperre: Tripel (2|6|1) (Original 2017MgrundlegendBAGLAA2WTR2-1f) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|6|1) |
| lagebeziehungen-e1-k2-s1-v1 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| lagebeziehungen-e1-k2-s1-v2 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| lagebeziehungen-e1-k2-s1-v3 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| lagebeziehungen-e1-k2-s1-v4 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| lagebeziehungen-e1-k2-s1-v5 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| lagebeziehungen-e1-k2-s4-v1 | Sperre: Tripel (2|5|3) (Original 2025-bebb-gk-A1.5b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|5|3) |
| lagebeziehungen-e1-k2-s4-v3 | Sperre: Tripel (1|3|1) (Original 2025-bebb-gk-A1.5b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|3|1) |
| lagebeziehungen-e1-k2-s5-v1 | Sperre: Tripel (5|0|3) (Original 2026-bb-gk-A1.2a); Sperre: Tripel (5|0|0) (Original 2023MgrundlegendAAGLAA22-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 5|0|3) |
| lagebeziehungen-e1-k2-s6-v1 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| lagebeziehungen-e1-k2-s6-v2 | Sperre: Tripel (3|2|4) (Original 2017MerhoehtBAGLAA2WTR1-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|2|4) |
| lagebeziehungen-e2-k1-s2-v2 | Sperre: Tripel (0|0|5) (Original 2017MerhoehtBAGLAA2WTR1-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|5); ob frei wie der Ursprung, entscheidet der Chat |
| lagebeziehungen-e2-k1-s2-v3 | Sperre: Tripel (0|3|0) (Original 2023MgrundlegendAAGLAA22-a) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3|0); ob frei wie der Ursprung, entscheidet der Chat |
| lagebeziehungen-e3-k1-s4-v3 | Sperre: Tripel (0|2|0) (Original 2024MgrundlegendBAGLAA2WTR1-1d) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|2|0); ob frei wie der Ursprung, entscheidet der Chat |
| lagebeziehungen-e4-k3-s1-v1 | Sperre: Tripel (0|0|5) (Original 2017MerhoehtBAGLAA2WTR1-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|5); ob frei wie der Ursprung, entscheidet der Chat |
| orthogonalitaet-zone-f2-v5 | Sperre: Tripel (2|3|1) (Original 2021MerhoehtAAGLAA112-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|3|1) |
| orthogonalitaet-e2-k2-s3-v2 | Sperre: Tripel (4|0|3) (Original 2023MerhoehtAAGLAA221) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 4|0|3) |
| orthogonalitaet-e4-k2-s1-v1 | Sperre: Tripel (1|3|0) (Original 2017MgrundlegendAAGLAA22-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|3|0) |
| rekonstruktion-von-funktionsgleichungen-zone-f2-v1 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e1-k1-s5-v1 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e1-k1-s6-v3 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e1-k1-s8-v1 | Sperre: Zahlenpaar (2|-6) (Original 2023-A-2a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-6) |
| rekonstruktion-von-funktionsgleichungen-e1-k1-s8-v2 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e2-k1-s1-v2 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e2-k1-s1-v3 | Sperre: Zahlenpaar (4|3) (Original 2017MerhoehtBAnalysisCAS2-4) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 4|3) |
| rekonstruktion-von-funktionsgleichungen-e2-k1-s8-v4 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e2-k1-s8-v6 | Sperre: Zahlenpaar (0|0.5) (Original 2022MgrundlegendAAnalysis12-a) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0.5); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e3-k1-s6-v1 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| rekonstruktion-von-funktionsgleichungen-e3-k3-s1-v1 | Sperre: Zahlenpaar (0|3) (Original 2023-C-2b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|3); ob frei wie der Ursprung, entscheidet der Chat |
| scharen-von-geraden-und-ebenen-zone-f1-v3 | Sperre: Tripel (1|1|2) (Original 2026MerhoehtBAGLAA2MMS2-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|1|2) |
| scharen-von-geraden-und-ebenen-e1-k2-s0-v1 | Sperre: Tripel (1|1|2) (Original 2026MerhoehtBAGLAA2MMS2-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|1|2) |
| scharen-von-geraden-und-ebenen-e2-k1-s6-v1 | Sperre: Tripel (1|1|2) (Original 2026MerhoehtBAGLAA2MMS2-1e) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|1|2) |
| scharen-von-geraden-und-ebenen-e4-k1-s1-v5 | Sperre: Tripel (5|5|0) (Original 2017MerhoehtBAGLAA2CAS2-1f) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 5|5|0) |
| scharen-von-geraden-und-ebenen-e4-k1-s3-v3 | Sperre: Tripel (5|5|0) (Original 2017MerhoehtBAGLAA2CAS2-1f) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 5|5|0) |
| schnittmengen-zone-f1-v2 | Sperre: Tripel (0|1|2) (Original 2025-bebb-lk-A1.3b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 0|1|2) |
| schnittmengen-e1-k2-s0-v4 | Sperre: Tripel (0|1|2) (Original 2025-bebb-lk-A1.3b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 0|1|2) |
| schnittmengen-e1-k2-s1-v4 | Sperre: Tripel (1|1|-2) (Original 2018MerhoehtBAGLAA2CAS2-1g) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 1|1|-2) |
| schnittmengen-e1-k2-s2-v3 | Sperre: Tripel (0|2|0) (Original 2025-bebb-lk-A1.3b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|2|0); ob frei wie der Ursprung, entscheidet der Chat |
| skalarprodukt-und-winkel-e2-k2-s5-v1 | Sperre: Tripel (2|-1|2) (Original 2024MerhoehtAAGLAA211-b) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-1|2) |
| skalarprodukt-und-winkel-e4-k1-s2-v1 | Sperre: Tripel (0|0|5) (Original 2017MerhoehtBAGLAA2CAS1-1e) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (0|0|5); ob frei wie der Ursprung, entscheidet der Chat |
| spiegelung-e1-k3-s2-v1 | Sperre: Tripel (2|-3|4) (Original 2017MerhoehtBAGLAA2WTR1-1c) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|-3|4) |
| tangente-normale-schnittwinkel-zone-f3-v3 | Sperre: Zahlenpaar (4|1) (Original 2025-bebb-gk-A1.1a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 4|1) |
| tangente-normale-schnittwinkel-e2-k1-s8-v1 | Sperre: Zahlenpaar (2|0) (Original 2024-bebb-lk-A1.5a) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| tangente-normale-schnittwinkel-e2-k4-s1-v3 | Sperre: Zahlenpaar (3|1) (Original 2025-bebb-lk-A1.6a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 3|1) |
| tangente-normale-schnittwinkel-e3-k1-s3-v1 | Sperre: Zahlenpaar (4|1) (Original 2025-bebb-gk-A1.1a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 4|1) |
| tangente-normale-schnittwinkel-e4-k1-s10-v5 | Sperre: Zahlenpaar (2|0) (Original 2024-bebb-lk-A1.5a) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| tangente-normale-schnittwinkel-e4-k1-s10-v6 | Sperre: Zahlenpaar (2|0) (Original 2024-bebb-lk-A1.5a) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0); ob frei wie der Ursprung, entscheidet der Chat |
| vektoren-und-rechenoperationen-e2-k1-s6-v1 | Sperre: Tripel (2|4|5) (Original 2021MgrundlegendAAGLAA112-a) | Zeile falsch nach Wortlaut der Sperre (Punkt/Tripel des Originals übernommen: 2|4|5) |
| vektoren-und-rechenoperationen-e2-k1-s9-v3 | Sperre: Tripel (2|0|0) (Original 2026MgrundlegendAAGLAA222-b) | offen: nur Achsenpunkt mit einer Koordinate ≠ 0 (2|0|0); ob frei wie der Ursprung, entscheidet der Chat |
| zufallsexperimente-und-pfadregeln-e2-k1-s0-v4 | Sperre: Zahlenpaar (5|2) (Merkkasten, Zeile 70); Sperre: Zahlenpaar (2|5) (Merkkasten, Zeile 70) | offen: Würfelpaar (2; 5)/(5; 2) aus dem Merkkasten, das die Aufgabe als Gegenstand braucht |

Zählung der Urteile: Zeile falsch nach Wortlaut der Sperre 75, offen 49.

## Merkmale je Form (Bestandsaufnahme Schritt 2)

Bestand: 2 571 Pflichtzeilen in 857 Gruppen zu je 3 (fehler 813, begruenden 810, anwendung 570, darstellung 378), gesammelt mit `werkzeuge/einmalig/pflichtzeilen-2026-09-30.py`. Treffer = Zeilen der jeweiligen Sorte.

| Sorte | Form | Merkmal im Skript | Treffer |
|---|---|---|---|
| fehler | P1 | aufgabe enthält „nicht stimmen“ | 99 |
| fehler | P3 | aufgabe „Setze … ein“ und „Zeile“ | 5 |
| fehler | P2m (Mehrzahl) | aufgabe „Genau eine Rechnung/Umformung/… ist falsch“ | 2 |
| fehler | P2 | loesung beginnt mit „Richtig.“ (mit Punkt; „Richtig:“ ist die Korrektur einer Fehlerzeile) | 102 |
| fehler | F (Schülerrechnung mit Fehler) | alles andere (262 × „Finde den Fehler“, 40 × „Ich finde den Fehler“) | 605 |
| begruenden | P4 | aufgabe enthält „wahr oder falsch“ | 103 |
| begruenden | P6 | aufgabe „recht hat“ oder „<Name> sagt …: „“ | 129 |
| begruenden | B („Begründe, warum …“) | alles andere | 578 |
| begruenden | „ohne genau zu rechnen“ | „ohne (genau) zu rechnen“, „ohne (vollständige) Rechnung“, „ohne … zu (be)rechnen“, „ohne den Rechner“ | 127 |
| anwendung | P8 | letzte Frage beginnt mit Verb (Reicht, Ist, Passt, Kann, Stimmt, Darf, Hält … – Liste aus dem Bestand) oder „Prüfe/Entscheide/Begründe/Beurteile/Untersuche …, ob“ oder loesung beginnt mit ja/nein | 207 (Verbfrage 189, „…, ob“ 13, ja/nein-Anfang 101; überlappend) |
| anwendung | A (ohne Entscheidung) | alles andere | 363 |
| darstellung | Ziel Bild | Zeichne, Skizziere, Markiere, Beschrifte, Färbe, Trage/Teile … ein, Stelle … dar, Zeige … an, Erstelle/Übertrage … Baum/Diagramm/Koordinatensystem | 135 |
| darstellung | Ziel Symbol | Schreibe, Gib, Lies, Stelle … auf, Welche(r/s) Term/Gleichung/Bruch/Zahl | 144 |
| darstellung | Ziel Wort | Beschreibe, Formuliere, Deute, Nenne, Sage, Erfinde, „in Worten“, „Was bedeutet“ | 36 |
| darstellung | Ziel Tabelle | Ergänze/Fülle/Vervollständige/Übertrage/Lege … Tabelle/tafel | 15 |
| darstellung | nicht erkannt | – | 48 |

Quelle einer darstellung-Zeile: Bild bei „Lies“ oder Bild-Baustein in grafik (ksys, saeulen, baum, zahlenstrahl, …), Tabelle bei Tabellen-Baustein, Symbol bei Formel mit „=“ oder „(x)“, sonst Wort. Richtungen im Bestand: Bild→Symbol 84, Wort→Bild 69, Wort→Symbol 42, Symbol→Bild 41, Tabelle→Bild 19, Wort→Wort 17, Wort→Tabelle 11, Tabelle→Symbol 10, Bild→Wort 9, Symbol→Symbol 8, Symbol→Wort 8, Bild→Bild 6, Symbol→Tabelle 3, Tabelle→Wort 2, Bild→Tabelle 1, nicht erkannt 48. „Rückwärts“ prüft das Skript nicht.

Regeln der Formprobe je Einheit: fehler – P2 oder P2m fehlt; eine Form doppelt (F doppelt heißt: weder P1/P3 noch zweite Sonderform). begruenden – P4 fehlt, P6 fehlt, „ohne genau zu rechnen“ fehlt; P4 oder P6 doppelt (B doppelt folgt schon aus fehlendem P4/P6 und wird nicht eigens gemeldet). anwendung – P8 fehlt (keine Doppelprüfung: bank.md verlangt „eine der drei“). darstellung – mindestens zwei Zeilen erkannt und nur eine Richtung. P1 oder P4 mit pruef nicht "": 0 Treffer.

## Urteile (Rohstoff für die Entscheidung im Chat)

Summen über 72 Einträge: ja 337, nein 364, richtig 103, falsch 7, offen 0, sonst 505.

Nach Form (alle Zeilen mit Urteilsfrage):

| Form | ja | nein | richtig | falsch | sonst |
|---|---|---|---|---|---|
| begruenden P4 (je Aussage) | 185 | 124 | – | – | – |
| begruenden P6 | 24 | 95 | – | 1 | 7 |
| begruenden B | 3 | 18 | – | – | 4 |
| fehler P2 | – | – | 102 | – | – |
| fehler F (mit „Prüfe, ob“) | – | – | – | 3 | 1 |
| anwendung P8 | 58 | 38 | – | 1 | 105 |
| darstellung | – | – | – | – | 7 |
| andere Höhen | 67 | 89 | 1 | 2 | 381 |

Einträge mit nein ≥ 3 × ja oder ja ≥ 3 × nein (bei mindestens einem Urteil): 12 – flaechen (ja 1, nein 4), gleichungen-loesen (0, 1), konfidenzintervalle (0, 1), lineare-gleichungssysteme (0, 1), normalverteilung-und-sigma-regeln (0, 2), orthogonalitaet (3, 1), quadratische-funktionen (0, 1), strahlensaetze (0, 2), unabhaengigkeit (0, 1), winkel-dreiecke (0, 7), zinsrechnung (1, 4), zuordnungen (2, 8). „offen“ („Das kann man nicht entscheiden“) kommt als erstes Wort nicht vor. 105 der P8-Urteile stehen nicht am Anfang der loesung (bank.md: „Urteil zuerst, dann die Rechnung“).

## Formprobe-Hinweise je Eintrag (vollständig)

Summe 882. Nach Art: fehler P2 fehlt 167, fehler Form F doppelt 167, begruenden P4 fehlt 167, begruenden „ohne genau zu rechnen“ fehlt 154, begruenden P6 fehlt 143, anwendung P8 fehlt 62, darstellung nur eine Richtung 20, begruenden P6 doppelt 2.

### ableitung-und-aenderungsrate (0)

keine

### ableitungsregeln (0)

keine

### abstaende (0)

keine

### bedingte-wahrscheinlichkeit-und-bayes (16)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (bedingte-wahrscheinlichkeit-und-bayes-e1-k2-s1-v1, bedingte-wahrscheinlichkeit-und-bayes-e1-k2-s1-v2, bedingte-wahrscheinlichkeit-und-bayes-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (bedingte-wahrscheinlichkeit-und-bayes-e2-k2-s1-v1, bedingte-wahrscheinlichkeit-und-bayes-e2-k2-s1-v2, bedingte-wahrscheinlichkeit-und-bayes-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (bedingte-wahrscheinlichkeit-und-bayes-e3-k2-s1-v1, bedingte-wahrscheinlichkeit-und-bayes-e3-k2-s1-v2, bedingte-wahrscheinlichkeit-und-bayes-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### binomialverteilung (0)

keine

### binomische-formeln (0)

keine

### bruchrechnung (0)

keine

### brueche-dezimalzahlen (1)

- e5.jsonl darstellung: nur eine Richtung (Wort → Symbol) in 3 erkannten Zeilen

### daten (40)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (daten-e1-k7-s1-v1, daten-e1-k7-s1-v2, daten-e1-k7-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (daten-e2-k4-s1-v1, daten-e2-k4-s1-v2, daten-e2-k4-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (daten-e3-k3-s1-v1, daten-e3-k3-s1-v2, daten-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (daten-e4-k4-s1-v1, daten-e4-k4-s1-v2, daten-e4-k4-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (daten-e5-k4-s1-v1, daten-e5-k4-s1-v2, daten-e5-k4-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e6.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e6.jsonl fehler: Form F doppelt (daten-e6-k2-s1-v1, daten-e6-k2-s1-v2, daten-e6-k2-s1-v3)
- e6.jsonl begruenden: P4 fehlt [B, B, B]
- e6.jsonl begruenden: P6 fehlt [B, B, B]
- e6.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e6.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e7.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e7.jsonl fehler: Form F doppelt (daten-e7-k3-s1-v1, daten-e7-k3-s1-v2, daten-e7-k3-s1-v3)
- e7.jsonl begruenden: P4 fehlt [B, B, B]
- e7.jsonl begruenden: P6 fehlt [B, B, B]
- e7.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e7.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### ebenen (1)

- e2.jsonl darstellung: nur eine Richtung (Symbol → Symbol) in 2 erkannten Zeilen

### einheiten (20)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (einheiten-e1-k9-s1-v1, einheiten-e1-k9-s1-v2, einheiten-e1-k9-s2-v1)
- e1.jsonl begruenden: P4 fehlt [B, B, P6]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (einheiten-e2-k6-s1-v1, einheiten-e2-k6-s1-v2, einheiten-e2-k6-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl darstellung: nur eine Richtung (Wort → Tabelle) in 3 erkannten Zeilen
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (einheiten-e3-k5-s1-v1, einheiten-e3-k5-s1-v2, einheiten-e3-k5-s2-v1)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (einheiten-e4-k5-s1-v1, einheiten-e4-k5-s1-v2, einheiten-e4-k5-s2-v1)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### extremalprobleme (0)

keine

### flaechen (30)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (flaechen-e1-k5-s1-v1, flaechen-e1-k5-s1-v2, flaechen-e1-k5-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl darstellung: nur eine Richtung (Symbol → Bild) in 3 erkannten Zeilen
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (flaechen-e2-k3-s1-v1, flaechen-e2-k3-s1-v2, flaechen-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (flaechen-e3-k4-s1-v1, flaechen-e3-k4-s1-v2, flaechen-e3-k4-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl darstellung: nur eine Richtung (Symbol → Bild) in 3 erkannten Zeilen
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (flaechen-e4-k4-s1-v1, flaechen-e4-k4-s1-v2, flaechen-e4-k4-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (flaechen-e5-k4-s1-v1, flaechen-e5-k4-s1-v2, flaechen-e5-k4-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### flaecheninhalt-durch-integration (0)

keine

### flaecheninhalt-und-volumen-im-raum (23)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (flaecheninhalt-und-volumen-im-raum-e1-k3-s1-v1, flaecheninhalt-und-volumen-im-raum-e1-k3-s1-v2, flaecheninhalt-und-volumen-im-raum-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (flaecheninhalt-und-volumen-im-raum-e2-k3-s1-v1, flaecheninhalt-und-volumen-im-raum-e2-k3-s1-v2, flaecheninhalt-und-volumen-im-raum-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (flaecheninhalt-und-volumen-im-raum-e3-k2-s1-v1, flaecheninhalt-und-volumen-im-raum-e3-k2-s1-v2, flaecheninhalt-und-volumen-im-raum-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (flaecheninhalt-und-volumen-im-raum-e4-k2-s1-v1, flaecheninhalt-und-volumen-im-raum-e4-k2-s1-v2, flaecheninhalt-und-volumen-im-raum-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### funktionsklassen-und-eigenschaften (1)

- e1.jsonl darstellung: nur eine Richtung (Bild → Symbol) in 2 erkannten Zeilen

### funktionsscharen-und-ortskurven (27)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (funktionsscharen-und-ortskurven-e1-k2-s1-v1, funktionsscharen-und-ortskurven-e1-k2-s1-v2, funktionsscharen-und-ortskurven-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (funktionsscharen-und-ortskurven-e2-k2-s1-v1, funktionsscharen-und-ortskurven-e2-k2-s1-v2, funktionsscharen-und-ortskurven-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (funktionsscharen-und-ortskurven-e3-k2-s1-v1, funktionsscharen-und-ortskurven-e3-k2-s1-v2, funktionsscharen-und-ortskurven-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (funktionsscharen-und-ortskurven-e4-k2-s1-v1, funktionsscharen-und-ortskurven-e4-k2-s1-v2, funktionsscharen-und-ortskurven-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (funktionsscharen-und-ortskurven-e5-k2-s1-v1, funktionsscharen-und-ortskurven-e5-k2-s1-v2, funktionsscharen-und-ortskurven-e5-k2-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### geraden (0)

keine

### gleichungen-loesen (21)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (gleichungen-loesen-e1-k3-s1-v1, gleichungen-loesen-e1-k3-s1-v2, gleichungen-loesen-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (gleichungen-loesen-e2-k3-s1-v1, gleichungen-loesen-e2-k3-s1-v2, gleichungen-loesen-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (gleichungen-loesen-e3-k3-s1-v1, gleichungen-loesen-e3-k3-s1-v2, gleichungen-loesen-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (gleichungen-loesen-e4-k3-s1-v1, gleichungen-loesen-e4-k3-s1-v2, gleichungen-loesen-e4-k3-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### grenzwerte-und-verhalten-im-unendlichen (17)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (grenzwerte-und-verhalten-im-unendlichen-e1-k3-s1-v1, grenzwerte-und-verhalten-im-unendlichen-e1-k3-s1-v2, grenzwerte-und-verhalten-im-unendlichen-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (grenzwerte-und-verhalten-im-unendlichen-e2-k2-s1-v1, grenzwerte-und-verhalten-im-unendlichen-e2-k2-s1-v2, grenzwerte-und-verhalten-im-unendlichen-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (grenzwerte-und-verhalten-im-unendlichen-e3-k2-s1-v1, grenzwerte-und-verhalten-im-unendlichen-e3-k2-s1-v2, grenzwerte-und-verhalten-im-unendlichen-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### hypergeometrische-verteilung (11)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (hypergeometrische-verteilung-e1-k2-s1-v1, hypergeometrische-verteilung-e1-k2-s1-v2, hypergeometrische-verteilung-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (hypergeometrische-verteilung-e2-k2-s1-v1, hypergeometrische-verteilung-e2-k2-s1-v2, hypergeometrische-verteilung-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### hypothesentests (17)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (hypothesentests-e1-k3-s1-v1, hypothesentests-e1-k3-s1-v2, hypothesentests-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (hypothesentests-e2-k2-s1-v1, hypothesentests-e2-k2-s1-v2, hypothesentests-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (hypothesentests-e3-k3-s1-v1, hypothesentests-e3-k3-s1-v2, hypothesentests-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### integrationsregeln (4)

- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (integrationsregeln-e2-k2-s1-v1, integrationsregeln-e2-k2-s1-v2, integrationsregeln-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]

### kenngroessen-von-verteilungen (21)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (kenngroessen-von-verteilungen-e1-k5-s1-v1, kenngroessen-von-verteilungen-e1-k5-s1-v2, kenngroessen-von-verteilungen-e1-k5-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, P6]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (kenngroessen-von-verteilungen-e2-k9-s1-v1, kenngroessen-von-verteilungen-e2-k9-s1-v2, kenngroessen-von-verteilungen-e2-k9-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (kenngroessen-von-verteilungen-e3-k4-s1-v1, kenngroessen-von-verteilungen-e3-k4-s1-v2, kenngroessen-von-verteilungen-e3-k4-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (kenngroessen-von-verteilungen-e4-k2-s1-v1, kenngroessen-von-verteilungen-e4-k2-s1-v2, kenngroessen-von-verteilungen-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### koerper (25)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (koerper-e1-k5-s1-v1, koerper-e1-k5-s1-v2, koerper-e1-k5-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (koerper-e2-k6-s1-v1, koerper-e2-k6-s1-v2, koerper-e2-k6-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, P6, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (koerper-e3-k2-s1-v1, koerper-e3-k2-s1-v2, koerper-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, P6]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl darstellung: nur eine Richtung (Wort → Bild) in 2 erkannten Zeilen
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (koerper-e4-k3-s1-v1, koerper-e4-k3-s1-v2, koerper-e4-k3-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, P6, P6]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl begruenden: Form P6 doppelt (koerper-e4-k3-s2-v2, koerper-e4-k3-s2-v3)
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (koerper-e5-k4-s1-v1, koerper-e5-k4-s1-v2, koerper-e5-k4-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl darstellung: nur eine Richtung (Wort → Symbol) in 2 erkannten Zeilen

### kombinatorik (16)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (kombinatorik-e1-k2-s1-v1, kombinatorik-e1-k2-s1-v2, kombinatorik-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (kombinatorik-e2-k2-s1-v1, kombinatorik-e2-k2-s1-v2, kombinatorik-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (kombinatorik-e3-k2-s1-v1, kombinatorik-e3-k2-s1-v2, kombinatorik-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### konfidenzintervalle (14)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (konfidenzintervalle-e1-k2-s1-v1, konfidenzintervalle-e1-k2-s1-v2, konfidenzintervalle-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, P6, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (konfidenzintervalle-e2-k3-s1-v1, konfidenzintervalle-e2-k3-s1-v2, konfidenzintervalle-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (konfidenzintervalle-e3-k2-s1-v1, konfidenzintervalle-e3-k2-s1-v2, konfidenzintervalle-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### kreis (13)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (kreis-e1-k6-s1-v1, kreis-e1-k6-s1-v2, kreis-e1-k6-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, P6]
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (kreis-e2-k5-s1-v1, kreis-e2-k5-s1-v2, kreis-e2-k5-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (kreis-e3-k3-s1-v1, kreis-e3-k3-s1-v2, kreis-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, P6]
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### kurvenuntersuchung (4)

- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### lagebeziehungen (0)

keine

### lineare-funktionen (20)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (lineare-funktionen-e1-k3-s1-v1, lineare-funktionen-e1-k3-s1-v2, lineare-funktionen-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (lineare-funktionen-e2-k7-s1-v1, lineare-funktionen-e2-k7-s1-v2, lineare-funktionen-e2-k7-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (lineare-funktionen-e3-k5-s1-v1, lineare-funktionen-e3-k5-s1-v2, lineare-funktionen-e3-k5-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (lineare-funktionen-e4-k4-s1-v1, lineare-funktionen-e4-k4-s1-v2, lineare-funktionen-e4-k4-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (lineare-funktionen-e5-k4-s1-v1, lineare-funktionen-e5-k4-s1-v2, lineare-funktionen-e5-k4-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, P6]

### lineare-gleichungen (0)

keine

### lineare-gleichungssysteme (24)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (lineare-gleichungssysteme-e1-k3-s1-v1, lineare-gleichungssysteme-e1-k3-s2-v1, lineare-gleichungssysteme-e1-k3-s3-v1)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (lineare-gleichungssysteme-e2-k3-s1-v1, lineare-gleichungssysteme-e2-k3-s2-v1, lineare-gleichungssysteme-e2-k3-s3-v1)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (lineare-gleichungssysteme-e3-k4-s1-v1, lineare-gleichungssysteme-e3-k4-s2-v1, lineare-gleichungssysteme-e3-k4-s3-v1)
- e3.jsonl begruenden: P4 fehlt [B, P6, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (lineare-gleichungssysteme-e4-k6-s1-v1, lineare-gleichungssysteme-e4-k6-s2-v1, lineare-gleichungssysteme-e4-k6-s3-v1)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (lineare-gleichungssysteme-e5-k2-s1-v1, lineare-gleichungssysteme-e5-k2-s2-v1, lineare-gleichungssysteme-e5-k2-s3-v1)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### linearkombination-und-lineare-abhaengigkeit (5)

- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (linearkombination-und-lineare-abhaengigkeit-e2-k2-s1-v1, linearkombination-und-lineare-abhaengigkeit-e2-k2-s1-v2, linearkombination-und-lineare-abhaengigkeit-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### matrizen-und-uebergangsprozesse (24)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (matrizen-und-uebergangsprozesse-e1-k2-s1-v1, matrizen-und-uebergangsprozesse-e1-k2-s1-v2, matrizen-und-uebergangsprozesse-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (matrizen-und-uebergangsprozesse-e2-k2-s1-v1, matrizen-und-uebergangsprozesse-e2-k2-s1-v2, matrizen-und-uebergangsprozesse-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (matrizen-und-uebergangsprozesse-e3-k2-s1-v1, matrizen-und-uebergangsprozesse-e3-k2-s1-v2, matrizen-und-uebergangsprozesse-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (matrizen-und-uebergangsprozesse-e4-k2-s1-v1, matrizen-und-uebergangsprozesse-e4-k2-s1-v2, matrizen-und-uebergangsprozesse-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (matrizen-und-uebergangsprozesse-e5-k3-s1-v1, matrizen-und-uebergangsprozesse-e5-k3-s1-v2, matrizen-und-uebergangsprozesse-e5-k3-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### normalverteilung-und-sigma-regeln (15)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (normalverteilung-und-sigma-regeln-e1-k2-s1-v1, normalverteilung-und-sigma-regeln-e1-k2-s1-v2, normalverteilung-und-sigma-regeln-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (normalverteilung-und-sigma-regeln-e2-k2-s1-v1, normalverteilung-und-sigma-regeln-e2-k2-s1-v2, normalverteilung-und-sigma-regeln-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (normalverteilung-und-sigma-regeln-e3-k3-s1-v1, normalverteilung-und-sigma-regeln-e3-k3-s1-v2, normalverteilung-und-sigma-regeln-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### orthogonalitaet (23)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (orthogonalitaet-e1-k5-s1-v1, orthogonalitaet-e1-k5-s1-v2, orthogonalitaet-e1-k5-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (orthogonalitaet-e2-k2-s1-v1, orthogonalitaet-e2-k2-s1-v2, orthogonalitaet-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (orthogonalitaet-e3-k2-s1-v1, orthogonalitaet-e3-k2-s1-v2, orthogonalitaet-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (orthogonalitaet-e4-k3-s1-v1, orthogonalitaet-e4-k3-s1-v2, orthogonalitaet-e4-k3-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### potenz-exponentialfunktionen (25)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (potenz-exponentialfunktionen-e1-k4-s1-v1, potenz-exponentialfunktionen-e1-k4-s1-v2, potenz-exponentialfunktionen-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (potenz-exponentialfunktionen-e2-k3-s1-v1, potenz-exponentialfunktionen-e2-k3-s1-v2, potenz-exponentialfunktionen-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (potenz-exponentialfunktionen-e3-k3-s1-v1, potenz-exponentialfunktionen-e3-k3-s1-v2, potenz-exponentialfunktionen-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, P6]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (potenz-exponentialfunktionen-e4-k2-s1-v1, potenz-exponentialfunktionen-e4-k2-s1-v2, potenz-exponentialfunktionen-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, P6, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (potenz-exponentialfunktionen-e5-k4-s1-v1, potenz-exponentialfunktionen-e5-k4-s1-v2, potenz-exponentialfunktionen-e5-k4-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### potenzen-wurzeln (15)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (potenzen-wurzeln-e1-k7-s1-v1, potenzen-wurzeln-e1-k7-s1-v2, potenzen-wurzeln-e1-k7-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (potenzen-wurzeln-e2-k2-s1-v1, potenzen-wurzeln-e2-k2-s1-v2, potenzen-wurzeln-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (potenzen-wurzeln-e3-k3-s1-v1, potenzen-wurzeln-e3-k3-s1-v2, potenzen-wurzeln-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### prozentrechnung (4)

- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl darstellung: nur eine Richtung (Wort → Bild) in 3 erkannten Zeilen
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### punkte-und-strecken-im-koordinatensystem (25)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (punkte-und-strecken-im-koordinatensystem-e1-k2-s1-v1, punkte-und-strecken-im-koordinatensystem-e1-k2-s1-v2, punkte-und-strecken-im-koordinatensystem-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (punkte-und-strecken-im-koordinatensystem-e2-k2-s1-v1, punkte-und-strecken-im-koordinatensystem-e2-k2-s1-v2, punkte-und-strecken-im-koordinatensystem-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (punkte-und-strecken-im-koordinatensystem-e3-k2-s1-v1, punkte-und-strecken-im-koordinatensystem-e3-k2-s1-v2, punkte-und-strecken-im-koordinatensystem-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (punkte-und-strecken-im-koordinatensystem-e4-k2-s1-v1, punkte-und-strecken-im-koordinatensystem-e4-k2-s1-v2, punkte-und-strecken-im-koordinatensystem-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (punkte-und-strecken-im-koordinatensystem-e5-k2-s1-v1, punkte-und-strecken-im-koordinatensystem-e5-k2-s1-v2, punkte-und-strecken-im-koordinatensystem-e5-k2-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### pyramide-kegel-kugel (12)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (pyramide-kegel-kugel-e1-k6-s1-v1, pyramide-kegel-kugel-e1-k6-s1-v2, pyramide-kegel-kugel-e1-k6-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, P6, B]
- e1.jsonl darstellung: nur eine Richtung (Wort → Bild) in 3 erkannten Zeilen
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (pyramide-kegel-kugel-e2-k3-s1-v1, pyramide-kegel-kugel-e2-k3-s1-v2, pyramide-kegel-kugel-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, P6]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (pyramide-kegel-kugel-e3-k2-s1-v1, pyramide-kegel-kugel-e3-k2-s1-v2, pyramide-kegel-kugel-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, P6]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### pythagoras (0)

keine

### quadratische-funktionen (25)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (quadratische-funktionen-e1-k2-s1-v1, quadratische-funktionen-e1-k2-s1-v2, quadratische-funktionen-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl darstellung: nur eine Richtung (Bild → Symbol) in 2 erkannten Zeilen
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (quadratische-funktionen-e2-k2-s1-v1, quadratische-funktionen-e2-k2-s1-v2, quadratische-funktionen-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (quadratische-funktionen-e3-k2-s1-v1, quadratische-funktionen-e3-k2-s1-v2, quadratische-funktionen-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (quadratische-funktionen-e4-k2-s1-v1, quadratische-funktionen-e4-k2-s1-v2, quadratische-funktionen-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl darstellung: nur eine Richtung (Bild → Symbol) in 3 erkannten Zeilen
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### quadratische-gleichungen (23)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (quadratische-gleichungen-e1-k3-s1-v1, quadratische-gleichungen-e1-k3-s1-v2, quadratische-gleichungen-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl darstellung: nur eine Richtung (Bild → Bild) in 3 erkannten Zeilen
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (quadratische-gleichungen-e2-k2-s1-v1, quadratische-gleichungen-e2-k2-s1-v2, quadratische-gleichungen-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (quadratische-gleichungen-e3-k5-s1-v1, quadratische-gleichungen-e3-k5-s1-v2, quadratische-gleichungen-e3-k5-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl darstellung: nur eine Richtung (Bild → Symbol) in 3 erkannten Zeilen
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (quadratische-gleichungen-e4-k3-s1-v1, quadratische-gleichungen-e4-k3-s1-v2, quadratische-gleichungen-e4-k3-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### rationale-zahlen (0)

keine

### reelle-zahlen (18)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (reelle-zahlen-e1-k4-s1-v1, reelle-zahlen-e1-k4-s1-v2, reelle-zahlen-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl darstellung: nur eine Richtung (Wort → Bild) in 2 erkannten Zeilen
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (reelle-zahlen-e2-k3-s1-v1, reelle-zahlen-e2-k3-s1-v2, reelle-zahlen-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (reelle-zahlen-e3-k2-s1-v1, reelle-zahlen-e3-k2-s1-v2, reelle-zahlen-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl darstellung: nur eine Richtung (Wort → Symbol) in 3 erkannten Zeilen

### rekonstruktion-von-bestaenden (17)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (rekonstruktion-von-bestaenden-e1-k3-s1-v1, rekonstruktion-von-bestaenden-e1-k3-s1-v2, rekonstruktion-von-bestaenden-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (rekonstruktion-von-bestaenden-e2-k3-s1-v1, rekonstruktion-von-bestaenden-e2-k3-s1-v2, rekonstruktion-von-bestaenden-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (rekonstruktion-von-bestaenden-e3-k2-s1-v1, rekonstruktion-von-bestaenden-e3-k2-s1-v2, rekonstruktion-von-bestaenden-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### rekonstruktion-von-funktionsgleichungen (15)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (rekonstruktion-von-funktionsgleichungen-e1-k2-s1-v1, rekonstruktion-von-funktionsgleichungen-e1-k2-s1-v2, rekonstruktion-von-funktionsgleichungen-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (rekonstruktion-von-funktionsgleichungen-e2-k3-s1-v1, rekonstruktion-von-funktionsgleichungen-e2-k3-s1-v2, rekonstruktion-von-funktionsgleichungen-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (rekonstruktion-von-funktionsgleichungen-e3-k5-s1-v1, rekonstruktion-von-funktionsgleichungen-e3-k5-s1-v2, rekonstruktion-von-funktionsgleichungen-e3-k5-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### rotationsvolumen (10)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (rotationsvolumen-e1-k2-s1-v1, rotationsvolumen-e1-k2-s1-v2, rotationsvolumen-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (rotationsvolumen-e2-k2-s1-v1, rotationsvolumen-e2-k2-s1-v2, rotationsvolumen-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### scharen-von-geraden-und-ebenen (20)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (scharen-von-geraden-und-ebenen-e1-k3-s1-v1, scharen-von-geraden-und-ebenen-e1-k3-s1-v2, scharen-von-geraden-und-ebenen-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (scharen-von-geraden-und-ebenen-e2-k2-s1-v1, scharen-von-geraden-und-ebenen-e2-k2-s1-v2, scharen-von-geraden-und-ebenen-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (scharen-von-geraden-und-ebenen-e3-k2-s1-v1, scharen-von-geraden-und-ebenen-e3-k2-s1-v2, scharen-von-geraden-und-ebenen-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (scharen-von-geraden-und-ebenen-e4-k2-s1-v1, scharen-von-geraden-und-ebenen-e4-k2-s1-v2, scharen-von-geraden-und-ebenen-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### schnittmengen (15)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (schnittmengen-e1-k4-s1-v1, schnittmengen-e1-k4-s1-v2, schnittmengen-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (schnittmengen-e2-k3-s1-v1, schnittmengen-e2-k3-s1-v2, schnittmengen-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (schnittmengen-e3-k2-s1-v1, schnittmengen-e3-k2-s1-v2, schnittmengen-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### skalarprodukt-und-winkel (0)

keine

### spiegelung (15)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (spiegelung-e1-k4-s1-v1, spiegelung-e1-k4-s1-v2, spiegelung-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (spiegelung-e2-k2-s1-v1, spiegelung-e2-k2-s1-v2, spiegelung-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (spiegelung-e3-k2-s1-v1, spiegelung-e3-k2-s1-v2, spiegelung-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### stammfunktion-und-hauptsatz (0)

keine

### strahlensaetze (15)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (strahlensaetze-e1-k4-s1-v1, strahlensaetze-e1-k4-s1-v2, strahlensaetze-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl darstellung: nur eine Richtung (Wort → Symbol) in 2 erkannten Zeilen
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (strahlensaetze-e2-k3-s1-v1, strahlensaetze-e2-k3-s1-v2, strahlensaetze-e2-k3-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (strahlensaetze-e3-k4-s1-v1, strahlensaetze-e3-k4-s1-v2, strahlensaetze-e3-k4-s1-v3)
- e3.jsonl begruenden: P4 fehlt [P6, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### symmetrie-abbildungen (18)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (symmetrie-abbildungen-e1-k6-s1-v1, symmetrie-abbildungen-e1-k6-s1-v2, symmetrie-abbildungen-e1-k6-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (symmetrie-abbildungen-e2-k6-s1-v1, symmetrie-abbildungen-e2-k6-s1-v2, symmetrie-abbildungen-e2-k6-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (symmetrie-abbildungen-e3-k4-s1-v1, symmetrie-abbildungen-e3-k4-s1-v2, symmetrie-abbildungen-e3-k4-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### tangente-normale-schnittwinkel (1)

- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### terme (0)

keine

### trigonometrie (20)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (trigonometrie-e1-k7-s1-v1, trigonometrie-e1-k7-s1-v2, trigonometrie-e1-k7-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (trigonometrie-e2-k4-s1-v1, trigonometrie-e2-k4-s1-v2, trigonometrie-e2-k4-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (trigonometrie-e3-k3-s1-v1, trigonometrie-e3-k3-s1-v2, trigonometrie-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (trigonometrie-e4-k2-s1-v1, trigonometrie-e4-k2-s1-v2, trigonometrie-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### trigonometrische-funktionen (19)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (trigonometrische-funktionen-e1-k2-s1-v1, trigonometrische-funktionen-e1-k2-s1-v2, trigonometrische-funktionen-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (trigonometrische-funktionen-e2-k2-s1-v1, trigonometrische-funktionen-e2-k2-s1-v2, trigonometrische-funktionen-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (trigonometrische-funktionen-e3-k3-s1-v1, trigonometrische-funktionen-e3-k3-s1-v2, trigonometrische-funktionen-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (trigonometrische-funktionen-e4-k2-s1-v1, trigonometrische-funktionen-e4-k2-s1-v2, trigonometrische-funktionen-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### umkehrfunktion (12)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (umkehrfunktion-e1-k3-s1-v1, umkehrfunktion-e1-k3-s1-v2, umkehrfunktion-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (umkehrfunktion-e2-k2-s1-v1, umkehrfunktion-e2-k2-s1-v2, umkehrfunktion-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### unabhaengigkeit (16)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (unabhaengigkeit-e1-k3-s1-v1, unabhaengigkeit-e1-k3-s1-v2, unabhaengigkeit-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (unabhaengigkeit-e2-k2-s1-v1, unabhaengigkeit-e2-k2-s1-v2, unabhaengigkeit-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (unabhaengigkeit-e3-k2-s1-v1, unabhaengigkeit-e3-k2-s1-v2, unabhaengigkeit-e3-k2-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### uneigentliche-integrale (10)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (uneigentliche-integrale-e1-k2-s1-v1, uneigentliche-integrale-e1-k2-s1-v2, uneigentliche-integrale-e1-k2-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (uneigentliche-integrale-e2-k2-s1-v1, uneigentliche-integrale-e2-k2-s1-v2, uneigentliche-integrale-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### vektoren-und-rechenoperationen (0)

keine

### vierfeldertafel (10)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (vierfeldertafel-e1-k3-s1-v1, vierfeldertafel-e1-k3-s1-v2, vierfeldertafel-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (vierfeldertafel-e2-k2-s1-v1, vierfeldertafel-e2-k2-s1-v2, vierfeldertafel-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt

### wahrscheinlichkeit (21)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (wahrscheinlichkeit-e1-k3-s1-v1, wahrscheinlichkeit-e1-k3-s1-v2, wahrscheinlichkeit-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, P6]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (wahrscheinlichkeit-e2-k6-s1-v1, wahrscheinlichkeit-e2-k6-s1-v2, wahrscheinlichkeit-e2-k6-s1-v3)
- e2.jsonl begruenden: P4 fehlt [P6, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl darstellung: nur eine Richtung (Wort → Symbol) in 3 erkannten Zeilen
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (wahrscheinlichkeit-e3-k4-s1-v1, wahrscheinlichkeit-e3-k4-s1-v2, wahrscheinlichkeit-e3-k4-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl darstellung: nur eine Richtung (Bild → Wort) in 3 erkannten Zeilen
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (wahrscheinlichkeit-e4-k2-s1-v1, wahrscheinlichkeit-e4-k2-s1-v2, wahrscheinlichkeit-e4-k2-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, P6]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### winkel-dreiecke (27)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (winkel-dreiecke-e1-k4-s1-v1, winkel-dreiecke-e1-k4-s1-v2, winkel-dreiecke-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, P6, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (winkel-dreiecke-e2-k4-s1-v1, winkel-dreiecke-e2-k4-s1-v2, winkel-dreiecke-e2-k4-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, P6, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (winkel-dreiecke-e3-k4-s1-v1, winkel-dreiecke-e3-k4-s1-v2, winkel-dreiecke-e3-k4-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (winkel-dreiecke-e4-k3-s1-v1, winkel-dreiecke-e4-k3-s1-v2, winkel-dreiecke-e4-k3-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e5.jsonl fehler: Form F doppelt (winkel-dreiecke-e5-k2-s1-v1, winkel-dreiecke-e5-k2-s1-v2, winkel-dreiecke-e5-k2-s1-v3)
- e5.jsonl begruenden: P4 fehlt [B, B, B]
- e5.jsonl begruenden: P6 fehlt [B, B, B]
- e5.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e5.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### zinsrechnung (8)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (zinsrechnung-e1-k4-s1-v1, zinsrechnung-e1-k4-s1-v2, zinsrechnung-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, P6]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (zinsrechnung-e2-k4-s1-v1, zinsrechnung-e2-k4-s1-v2, zinsrechnung-e2-k4-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, P6, P6]
- e2.jsonl begruenden: Form P6 doppelt (zinsrechnung-e2-k4-s2-v2, zinsrechnung-e2-k4-s2-v3)

### zufallsexperimente-und-pfadregeln (1)

- e5.jsonl darstellung: nur eine Richtung (Wort → Symbol) in 2 erkannten Zeilen

### zufallsgroessen-und-verteilungen (12)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (zufallsgroessen-und-verteilungen-e1-k3-s1-v1, zufallsgroessen-und-verteilungen-e1-k3-s1-v2, zufallsgroessen-und-verteilungen-e1-k3-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, B]
- e1.jsonl begruenden: P6 fehlt [B, B, B]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (zufallsgroessen-und-verteilungen-e2-k2-s1-v1, zufallsgroessen-und-verteilungen-e2-k2-s1-v2, zufallsgroessen-und-verteilungen-e2-k2-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e2.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt

### zuordnungen (20)

- e1.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e1.jsonl fehler: Form F doppelt (zuordnungen-e1-k4-s1-v1, zuordnungen-e1-k4-s1-v2, zuordnungen-e1-k4-s1-v3)
- e1.jsonl begruenden: P4 fehlt [B, B, P6]
- e1.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e1.jsonl anwendung: P8 (Entscheidung am Grenzwert) fehlt
- e2.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e2.jsonl fehler: Form F doppelt (zuordnungen-e2-k8-s1-v1, zuordnungen-e2-k8-s1-v2, zuordnungen-e2-k8-s1-v3)
- e2.jsonl begruenden: P4 fehlt [B, B, B]
- e2.jsonl begruenden: P6 fehlt [B, B, B]
- e2.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e3.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e3.jsonl fehler: Form F doppelt (zuordnungen-e3-k3-s1-v1, zuordnungen-e3-k3-s1-v2, zuordnungen-e3-k3-s1-v3)
- e3.jsonl begruenden: P4 fehlt [B, B, B]
- e3.jsonl begruenden: P6 fehlt [B, B, B]
- e3.jsonl begruenden: „ohne genau zu rechnen“ fehlt
- e4.jsonl fehler: P2 (fehlerfreie Vorlage) fehlt [F, F, F]
- e4.jsonl fehler: Form F doppelt (zuordnungen-e4-k5-s1-v1, zuordnungen-e4-k5-s1-v2, zuordnungen-e4-k5-s1-v3)
- e4.jsonl begruenden: P4 fehlt [B, B, B]
- e4.jsonl begruenden: P6 fehlt [B, B, B]
- e4.jsonl begruenden: „ohne genau zu rechnen“ fehlt

## Annahmen und Abweichungen vom Auftrag

- Ausgangswert nicht 0/0 und 72 statt 73 Einträge (siehe Summen); Maßstab der Gegenprobe war daher „unverändert gegenüber v0.10“.
- „(4, 1)“ mit Komma erkannte auch v0.10 nicht; v0.11 lässt das so (Verwechslung mit Dezimalkomma; 0 Vorkommen in bank/).
- Zwei Skriptkorrekturen nach der Gegenprobe (Matrizen, Punkte nur aus 0/1/−1): neue Ausnahmen der Sperre. Die zweite ist eine Regelentscheidung in Analogie zum Ursprung und im Chat zu bestätigen.
- Urteile-Zeile trägt zusätzlich „falsch“ und „sonst“, sonst gingen Zeilen verloren; Urteilsfrage = \janein, „recht hat“, „Prüfe, ob“, „wahr oder falsch“ oder Entscheidungsfrage (Verbfrage bzw. „…, ob“); bloßes „reicht/darf/stimmt“ im Text zählt nicht.
- Formprobe und Urteile nur für e<n>.jsonl, nicht für zone.jsonl und _basis.
- Die Ausgabe von FORMPROBE, „Formprobe:“ und „Urteile:“ steht vor den Dateisummen; letzte Zeile bleibt „Abweichungen: n, Warnungen: m“.
- bank.md nennt im Abschnitt „Prüfung“ v0.5; nicht geändert, weil der Text dort den Stand v0.5 beschreibt und eine bloße Zahl ihn falsch machen würde.
- Die Bestandsaufnahme (610 KB) wurde über Häufigkeiten und die vollständige Durchsicht aller Zeilen gelesen, die kein Merkmal traf (Restlisten je Sorte), nicht Zeile für Zeile.


## Nachtrag v0.12 (Körperregel, 30.09.)

Entscheidung des Lehrers 30.09.: Ein einzelner Punkt (Zahlenpaar oder Tripel als Koordinaten) ist frei; gesperrt sind zwei oder mehr verschiedene Punkte derselben Quelle in einer Zeile. Quelle ist ein Original (Kennung) oder der Kasten (Merkkasten und Typische Fehler der Mappe zusammen). Die Ausnahme „Punkte nur aus 0, 1, −1“ aus v0.11 ist entfernt; Ursprung frei, Matrizen ((a; b), (c; d)) kein Punkt, Anteil und Produkt unverändert. Lauf je Eintrag mit `--katalog` über 72 Einträge (ohne _basis).

| | Abweichungen | Warnungen | Formprobe |
|---|---|---|---|
| v0.11 | 439 | 2 | 882 |
| v0.12 | 317 | 2 | 882 |

122 der 124 Punkt-Abweichungen aus v0.11 entfallen (15 Einträge); keine neue Zeile, keine der 315 übrigen verändert. Zwei Zeilen bleiben:

| id | Befund | Urteil |
|---|---|---|
| geraden-e3-k1-s4-v1 | Sperre: Punkte (0\|5\|0), (5\|0\|0), (5\|5\|0) derselben Quelle (Original 2017MgrundlegendBAGLAA2CAS2-1f) | Treffer nach Regel, inhaltlich kein Körper des Originals: Die Zeile baut einen Würfel der Kantenlänge 5 (mit G(0\|5\|5)) nach 2021-be-gk-B3b; die drei Ecken decken sich zufällig mit dem Bodenquadrat der Zeltpyramide (Spitze S(2,5; 2,5; 3,9)). Entscheidung Chat. |
| zufallsexperimente-und-pfadregeln-e2-k1-s0-v4 | Sperre: Punkte (2\|5), (5\|2) derselben Quelle (Kasten: Merkkasten, Zeile 70) | Kein Körper: Würfelergebnisse (2; 5)/(5; 2), keine Koordinaten; die Zeile übernimmt aber das Beispiel des Kastens wörtlich als Gegenstand. Das Skript unterscheidet Ergebnispaar und Punkt nicht. Entscheidung Chat. |
