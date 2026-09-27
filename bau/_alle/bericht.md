# Zusammenbau über alle Einträge

Stand 2026-09-27, zusammenbau.py v0.1 (mit den zwei Änderungen unten),
Bank beim Commit 8c77e08 („trigonometrie: Gegenlese“).

## Läufe

    lernblatt/  zusammenbau.py <eintrag>             alle 70 Einträge
    schwach/    zusammenbau.py <eintrag> --schwach   27 Einträge Sek I

Sek I heißt: die erste Marken-Zeile der Mappe beginnt mit „OS Kl.“ –
dasselbe Merkmal, nach dem das Skript `\weit` setzt. schwach ohne
`--klasse` (der Auftrag nennt keine). Vorlage: mathblatt.sty
„Version 2026-09-28a“ aus bau/prozentrechnung/2026-09-27/lernblatt/
(blattbau ist in der Sitzung nicht geklont; dieselbe Fassung wie in
den Prüfsteinen). Ausgabe je Lauf unter bau/_alle/<eintrag>/<lauf>/,
Einzelheiten in der zusammenbau.log dort.

## Ergebnis

- 97 Läufe, 70 Einträge; **67 Einträge ohne Strukturfehler**, 3 mit (56 Fehler in 6 Läufen).
- Alle 56 verbliebenen Fehler liegen in der Bank (Zeile ändern).
- Ohne die Skript-Änderung 2 hätte die Prüfung 0 Fehler gemeldet: die
  alte Prüfung sah keinen Mathe-Modus. Ohne Änderung 1 wären es 15
  Fehler mehr (Zusammenbau).
- Summe über alle Läufe: 2068 Hauptnummern, 7378 Teilaufgaben, 6851 TODO-Zeilen, 227 WARNUNG (Halbseitenmaß) in 76 Läufen.

## Änderungen am Skript

1. `klar()` statt `pct()` für Klartext: Kettennamen als Titel und in der
   Abhakseite, Einheitentitel im Verzeichnis, Merkkasten aus der Mappe,
   Text vor und nach den Lücken im Antwortgerüst. Wörter mit `_` oder `^`
   außerhalb `$…$` kommen in Mathe, `^(…)` wird `^{(…)}`. Grund: diese
   Felder sind Klartext (bank.md: kette wortgleich aus dem Katalog,
   antwort „wie auf dem Blatt“; das Skript setzt dort schon `<`, `>` in
   Mathe), der Zusammenbau reichte `e^x`, `P_A(B)`, `S_1(`, `h_s` roh an
   LaTeX weiter – Kompilierfehler „Missing $ inserted“.
2. Strukturprüfung um den Mathe-Modus erweitert (`modusfehler`): `_`, `^`,
   `#` außerhalb Mathe, `&` außerhalb einer Ausrichtung, `$` in einem
   Mathe-Argument (`\gl`, `\rechnung`), `\rechnung` in Mathe oder `\text`.
   Grafik- und Rahmenbausteine werden samt Argumenten übergangen. Grund:
   die Prüfung soll den Lauf bis zum ersten Render ersetzen, übersah aber
   genau diese Fehlerklasse (vorher 0 Meldungen in allen 97 Läufen).

Nachweis Prüfsteine: die drei Läufe unter bau/prozentrechnung/2026-09-27/
(lernblatt, schwach-7 mit `--klasse 7 --schwach`, fokus-prozentsatz mit
`--fokus Prozentsatz`) vor und nach den Änderungen neu gebaut und mit
`diff -r` verglichen: alle 56 Dateien byteidentisch, sha256 über alle 56 Dateien
vorher und nachher 46491c4d…3f16. VERSION bleibt deshalb „v0.1“ – sie
steht in jedem Quelltext und in der log. werkzeuge/zusammenbau.md ist
nicht nachgezogen (Auftrag: nur bau/_alle/ und das Skript); fehlt dort
im Abschnitt Strukturprüfung ein Satz zu Änderung 2.

## Je Eintrag

HN Hauptnummern, TA Teilaufgaben (gleich der Zahl der Lösungsbuchstaben),
TODO Zeilen „%% TODO“, F Strukturfehler; „–“ kein Lauf (Sek II).

| Eintrag | Lernblatt HN | TA | TODO | F | schwach HN | TA | TODO | F |
| --- | --: | --: | --: | --: | --: | --: | --: | --: |
| ableitung-und-aenderungsrate | 20 | 73 | 53 | 0 | – | – | – | – |
| ableitungsregeln | 18 | 49 | 46 | 0 | – | – | – | – |
| abstaende | 17 | 56 | 47 | 0 | – | – | – | – |
| bedingte-wahrscheinlichkeit-und-bayes | 13 | 39 | 36 | 0 | – | – | – | – |
| binomialverteilung | 24 | 88 | 64 | 0 | – | – | – | – |
| binomische-formeln | 18 | 59 | 43 | 0 | 18 | 74 | 101 | 0 |
| bruchrechnung | 29 | 85 | 72 | 0 | 29 | 115 | 143 | 0 |
| brueche-dezimalzahlen | 30 | 96 | 74 | **3** | 30 | 126 | 148 | **3** |
| ebenen | 19 | 70 | 54 | 0 | – | – | – | – |
| einheiten | 38 | 120 | 96 | 0 | 38 | 155 | 207 | 0 |
| extremalprobleme | 15 | 46 | 40 | 0 | – | – | – | – |
| flaechen | 29 | 83 | 69 | 0 | 29 | 108 | 140 | 0 |
| flaecheninhalt-durch-integration | 18 | 68 | 52 | 0 | – | – | – | – |
| flaecheninhalt-und-volumen-im-raum | 18 | 61 | 53 | 0 | – | – | – | – |
| funktionsklassen-und-eigenschaften | 22 | 93 | 65 | 0 | – | – | – | – |
| funktionsscharen-und-ortskurven | 19 | 73 | 54 | 0 | – | – | – | – |
| geraden | 20 | 60 | 53 | 0 | – | – | – | – |
| gleichungen-loesen | 22 | 77 | 57 | 0 | – | – | – | – |
| grenzwerte-und-verhalten-im-unendlichen | 16 | 47 | 42 | 0 | – | – | – | – |
| hypergeometrische-verteilung | 10 | 23 | 27 | 0 | – | – | – | – |
| hypothesentests | 15 | 39 | 41 | 0 | – | – | – | – |
| integrationsregeln | 8 | 20 | 23 | 0 | – | – | – | – |
| kenngroessen-von-verteilungen | 28 | 64 | 73 | 0 | – | – | – | – |
| koerper | 28 | 96 | 67 | 0 | 28 | 121 | 134 | 0 |
| kombinatorik | 13 | 46 | 36 | 0 | – | – | – | – |
| konfidenzintervalle | 15 | 34 | 40 | 0 | – | – | – | – |
| kreis | 22 | 60 | 51 | 0 | 22 | 75 | 99 | 0 |
| kurvenuntersuchung | 37 | 107 | 93 | 0 | – | – | – | – |
| lagebeziehungen | 18 | 50 | 49 | 0 | – | – | – | – |
| lineare-funktionen | 31 | 87 | 77 | 0 | 31 | 117 | 112 | 0 |
| lineare-gleichungen | 21 | 68 | 57 | 0 | 21 | 93 | 107 | 0 |
| lineare-gleichungssysteme | 30 | 112 | 81 | 0 | 30 | 152 | 168 | 0 |
| linearkombination-und-lineare-abhaengigkeit | 9 | 21 | 25 | 0 | – | – | – | – |
| matrizen-und-uebergangsprozesse | 19 | 68 | 54 | 0 | – | – | – | – |
| normalverteilung-und-sigma-regeln | 14 | 35 | 42 | 0 | – | – | – | – |
| orthogonalitaet | 20 | 55 | 53 | 0 | – | – | – | – |
| potenzen-wurzeln | 23 | 80 | 53 | 0 | 23 | 95 | 128 | 0 |
| prozentrechnung | 25 | 88 | 61 | 0 | 25 | 113 | 117 | 0 |
| punkte-und-strecken-im-koordinatensystem | 20 | 78 | 56 | 0 | – | – | – | – |
| pyramide-kegel-kugel | 22 | 81 | 51 | 0 | 22 | 96 | 117 | 0 |
| pythagoras | 24 | 85 | 55 | 0 | 24 | 100 | 101 | 0 |
| quadratische-funktionen | 18 | 87 | 45 | **2** | 18 | 107 | 106 | **2** |
| quadratische-gleichungen | 23 | 84 | 55 | **19** | 23 | 104 | 132 | **27** |
| rationale-zahlen | 25 | 72 | 59 | 0 | 25 | 92 | 108 | 0 |
| reelle-zahlen | 18 | 67 | 43 | 0 | 18 | 82 | 96 | 0 |
| rekonstruktion-von-bestaenden | 15 | 42 | 40 | 0 | – | – | – | – |
| rekonstruktion-von-funktionsgleichungen | 18 | 49 | 46 | 0 | – | – | – | – |
| rotationsvolumen | 11 | 30 | 29 | 0 | – | – | – | – |
| scharen-von-geraden-und-ebenen | 17 | 52 | 47 | 0 | – | – | – | – |
| schnittmengen | 17 | 44 | 45 | 0 | – | – | – | – |
| skalarprodukt-und-winkel | 18 | 51 | 49 | 0 | – | – | – | – |
| spiegelung | 16 | 41 | 42 | 0 | – | – | – | – |
| stammfunktion-und-hauptsatz | 18 | 48 | 49 | 0 | – | – | – | – |
| strahlensaetze | 22 | 78 | 54 | 0 | 22 | 98 | 89 | 0 |
| symmetrie-abbildungen | 25 | 77 | 60 | 0 | 25 | 97 | 77 | 0 |
| tangente-normale-schnittwinkel | 24 | 79 | 64 | 0 | – | – | – | – |
| terme | 21 | 67 | 54 | 0 | 21 | 92 | 115 | 0 |
| trigonometrie | 27 | 104 | 63 | 0 | 27 | 124 | 148 | 0 |
| trigonometrische-funktionen | 22 | 94 | 53 | 0 | 22 | 114 | 109 | 0 |
| umkehrfunktion | 12 | 32 | 31 | 0 | – | – | – | – |
| unabhaengigkeit | 15 | 41 | 40 | 0 | – | – | – | – |
| uneigentliche-integrale | 9 | 20 | 25 | 0 | – | – | – | – |
| vektoren-und-rechenoperationen | 15 | 46 | 40 | 0 | – | – | – | – |
| vierfeldertafel | 12 | 29 | 35 | 0 | – | – | – | – |
| wahrscheinlichkeit | 22 | 82 | 53 | 0 | 22 | 102 | 112 | 0 |
| winkel-dreiecke | 24 | 88 | 59 | 0 | 24 | 113 | 88 | 0 |
| zinsrechnung | 18 | 57 | 44 | 0 | 18 | 72 | 94 | 0 |
| zufallsexperimente-und-pfadregeln | 30 | 121 | 85 | 0 | – | – | – | – |
| zufallsgroessen-und-verteilungen | 10 | 25 | 29 | 0 | – | – | – | – |
| zuordnungen | 27 | 82 | 69 | 0 | 27 | 112 | 113 | 0 |

## Strukturfehler mit Datei und Zeile

**brueche-dezimalzahlen/lernblatt** (3)

- e5_a.tex:26: _ außerhalb Mathe ← bank/brueche-dezimalzahlen/e5.jsonl:26 (brueche-dezimalzahlen-e5-k2-s6-v1)
- e5_a.tex:27: _ außerhalb Mathe ← bank/brueche-dezimalzahlen/e5.jsonl:29 (brueche-dezimalzahlen-e5-k2-s7-v1)
- e5_a.tex:28: _ außerhalb Mathe ← bank/brueche-dezimalzahlen/e5.jsonl:32 (brueche-dezimalzahlen-e5-k2-s8-v1)

**brueche-dezimalzahlen/schwach** (3)

- e5_a.tex:41: _ außerhalb Mathe ← bank/brueche-dezimalzahlen/e5.jsonl:26 (brueche-dezimalzahlen-e5-k2-s6-v1)
- e5_a.tex:43: _ außerhalb Mathe ← bank/brueche-dezimalzahlen/e5.jsonl:29 (brueche-dezimalzahlen-e5-k2-s7-v1)
- e5_a.tex:45: _ außerhalb Mathe ← bank/brueche-dezimalzahlen/e5.jsonl:32 (brueche-dezimalzahlen-e5-k2-s8-v1)

**quadratische-funktionen/lernblatt** (2)

- e3_a.tex:55: \rechnung in Mathe oder \text (Absatz im Argument) ← bank/quadratische-funktionen/e3.jsonl:37 (quadratische-funktionen-e3-k2-s1-v1)
- e4_a.tex:45: \rechnung in Mathe oder \text (Absatz im Argument) ← bank/quadratische-funktionen/e4.jsonl:49 (quadratische-funktionen-e4-k2-s1-v1)

**quadratische-funktionen/schwach** (2)

- e3_a.tex:50: \rechnung in Mathe oder \text (Absatz im Argument) ← bank/quadratische-funktionen/e3.jsonl:37 (quadratische-funktionen-e3-k2-s1-v1)
- e4_a.tex:54: \rechnung in Mathe oder \text (Absatz im Argument) ← bank/quadratische-funktionen/e4.jsonl:49 (quadratische-funktionen-e4-k2-s1-v1)

**quadratische-gleichungen/lernblatt** (19)

- e1_a.tex:23: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:9 (quadratische-gleichungen-e1-k2-s1-v1)
- e1_a.tex:29: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:17 (quadratische-gleichungen-e1-k2-s3-v1)
- e1_a.tex:35: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:18 (quadratische-gleichungen-e1-k2-s3-v2)
- e1_a.tex:41: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:29 (quadratische-gleichungen-e1-k2-s7-v1)
- e1_a.tex:42: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:32 (quadratische-gleichungen-e1-k2-s8-v1)
- e1_a.tex:43: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:35 (quadratische-gleichungen-e1-k2-s9-v1)
- e1_a.tex:44: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:38 (quadratische-gleichungen-e1-k2-s10-v1)
- e2_a.tex:24: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e2.jsonl:22 (quadratische-gleichungen-e2-k1-s6-v1)
- e2_a.tex:25: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e2.jsonl:25 (quadratische-gleichungen-e2-k1-s7-v1)
- e2_a.tex:26: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e2.jsonl:28 (quadratische-gleichungen-e2-k1-s8-v1)
- e3_a.tex:31: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:13 (quadratische-gleichungen-e3-k3-s1-v1)
- e3_a.tex:32: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:18 (quadratische-gleichungen-e3-k3-s2-v1)
- e3_a.tex:33: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:21 (quadratische-gleichungen-e3-k3-s3-v1)
- e3_a.tex:34: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:24 (quadratische-gleichungen-e3-k3-s4-v1)
- e3_a.tex:35: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:27 (quadratische-gleichungen-e3-k3-s5-v1)
- e3_a.tex:36: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:30 (quadratische-gleichungen-e3-k3-s6-v1)
- e3_a.tex:37: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:33 (quadratische-gleichungen-e3-k3-s7-v1)
- e3_a.tex:43: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:39 (quadratische-gleichungen-e3-k3-s9-v1)
- e3_a.tex:49: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:45 (quadratische-gleichungen-e3-k3-s11-v1)

**quadratische-gleichungen/schwach** (27)

- e1_a.tex:22: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:9 (quadratische-gleichungen-e1-k2-s1-v1)
- e1_a.tex:24: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:10 (quadratische-gleichungen-e1-k2-s1-v2)
- e1_a.tex:26: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:11 (quadratische-gleichungen-e1-k2-s1-v3)
- e1_a.tex:28: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:12 (quadratische-gleichungen-e1-k2-s1-v4)
- e1_a.tex:30: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:13 (quadratische-gleichungen-e1-k2-s1-v5)
- e1_a.tex:35: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:17 (quadratische-gleichungen-e1-k2-s3-v1)
- e1_a.tex:39: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:18 (quadratische-gleichungen-e1-k2-s3-v2)
- e1_a.tex:43: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:29 (quadratische-gleichungen-e1-k2-s7-v1)
- e1_a.tex:45: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:32 (quadratische-gleichungen-e1-k2-s8-v1)
- e1_a.tex:47: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:35 (quadratische-gleichungen-e1-k2-s9-v1)
- e1_a.tex:49: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e1.jsonl:38 (quadratische-gleichungen-e1-k2-s10-v1)
- e2_a.tex:33: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e2.jsonl:22 (quadratische-gleichungen-e2-k1-s6-v1)
- e2_a.tex:35: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e2.jsonl:25 (quadratische-gleichungen-e2-k1-s7-v1)
- e2_a.tex:37: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e2.jsonl:28 (quadratische-gleichungen-e2-k1-s8-v1)
- e3_a.tex:30: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:13 (quadratische-gleichungen-e3-k3-s1-v1)
- e3_a.tex:32: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:14 (quadratische-gleichungen-e3-k3-s1-v2)
- e3_a.tex:34: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:15 (quadratische-gleichungen-e3-k3-s1-v3)
- e3_a.tex:36: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:16 (quadratische-gleichungen-e3-k3-s1-v4)
- e3_a.tex:38: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:17 (quadratische-gleichungen-e3-k3-s1-v5)
- e3_a.tex:41: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:18 (quadratische-gleichungen-e3-k3-s2-v1)
- e3_a.tex:43: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:21 (quadratische-gleichungen-e3-k3-s3-v1)
- e3_a.tex:45: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:24 (quadratische-gleichungen-e3-k3-s4-v1)
- e3_a.tex:47: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:27 (quadratische-gleichungen-e3-k3-s5-v1)
- e3_a.tex:49: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:30 (quadratische-gleichungen-e3-k3-s6-v1)
- e3_a.tex:51: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:33 (quadratische-gleichungen-e3-k3-s7-v1)
- e3_a.tex:55: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:39 (quadratische-gleichungen-e3-k3-s9-v1)
- e3_a.tex:59: ^ außerhalb Mathe ← bank/quadratische-gleichungen/e3.jsonl:45 (quadratische-gleichungen-e3-k3-s11-v1)

## Fehlerarten

Die Prüfung ergibt sechs Fehlerarten, nicht zehn; weitere gibt sie in
den 97 Läufen nicht her. Gezählt sind Fehlerzeilen über alle Läufe;
die Arten 3 bis 5 vor Änderung 1 (danach 0).

1. **`^` außerhalb Mathe – Gleichung im Gleichungsraster ohne `$`** (46)
   - quadratische-gleichungen/lernblatt/e1_a.tex:23 `\gl{\text{x^2 = 81}}` ← e1.jsonl:9
   - quadratische-gleichungen/lernblatt/e2_a.tex:24 `\gl{\text{x^2 + 9x = 0}}` ← e2.jsonl:22
   - quadratische-gleichungen/schwach/e3_a.tex:30 `\swz{$\text{x^2 + 6x + 8 = 0}$}{}` ← e3.jsonl:13

   Bank: aufgabe als `$x^2 = 81$` schreiben wie in lineare-gleichungen;
   betrifft alle 79 gleichungsraster-Zeilen des Eintrags.
2. **`_` außerhalb Mathe – Lücke „__“ im Aufgabentext** (6)
   - brueche-dezimalzahlen/lernblatt/e5_a.tex:26 `$\frac{3}{5}$ __ $0{,}65$` ← e5.jsonl:26
   - brueche-dezimalzahlen/lernblatt/e5_a.tex:27 ← e5.jsonl:29
   - brueche-dezimalzahlen/schwach/e5_a.tex:45 ← e5.jsonl:32

   Bank: Lücke im Lückensatz als `\leerfeld` (bank.md, Feld antwort);
   13 Bankzeilen tragen „__“ in aufgabe, auch e4.jsonl:30, 31.
3. **`^`/`_` im Kettennamen als Titel und Abhakzeile** (6, behoben)
   - ableitungsregeln/lernblatt/blatt0_a.tex:34 „e^(kx) … e^x ist nie null“
   - grenzwerte-und-verhalten-im-unendlichen/lernblatt/abhaken.tex:10 „e^x“
   - zufallsexperimente-und-pfadregeln/lernblatt/blatt0_a.tex:34 „P_A(B)“

   Zusammenbau: kette ist Klartext, das Skript maskierte nur `%` –
   behoben mit Änderung 1.
4. **`^`/`_` im Antwortgerüst** (5, behoben)
   - pythagoras/lernblatt/e3_a.tex:42 „h_s = __ cm“
   - quadratische-funktionen/lernblatt/e4_a.tex:55 „S_1(__|__), S_2(__|__)“
   - schnittmengen/lernblatt/e3_a.tex:14 „S_x( __ |0|0)“

   Zusammenbau: antwort ist Klartext, das Skript setzte nur `<`, `>` in
   Mathe – behoben mit Änderung 1.
5. **`^`/`_` im Merkkasten aus der Mappe** (4, behoben)
   - potenzen-wurzeln/schwach/e1_a.tex:97 „5^x = 125“
   - reelle-zahlen/schwach/e3_a.tex:56 „√a = a^(1/2)“
   - zinsrechnung/schwach/e2_a.tex:63 „K_n = K_0 · qⁿ“

   Zusammenbau: Mappentext ist Klartext – behoben mit Änderung 1.
6. **`\rechnung` in `\gl{\text{…}}` bzw. `\swz{$\text{…}$}`** (4)
   - quadratische-funktionen/lernblatt/e3_a.tex:55 „Nina rechnet: \rechnung{…}“ ← e3.jsonl:37
   - quadratische-funktionen/lernblatt/e4_a.tex:45 „Lina berechnet …“ ← e4.jsonl:49
   - quadratische-funktionen/schwach/e3_a.tex:50 ← e3.jsonl:37

   Bank: Fehler-finden mit Rechnung ist keine Gleichung fürs Raster;
   form „teil“ statt „gleichungsraster“ (auch e4.jsonl:50, 51).

## Weitere Befunde (keine Strukturfehler)

- WARNUNG Halbseitenmaß (2.3 g): 227 Hauptnummern in 76 Läufen –
  Zusammenbau, bekannte Grenze von v0.1 (teilt nur im Fokus).
- Grafik im Gleichungsraster fällt weg: quadratische-funktionen-e4-k2-s4-v1
  (e4.jsonl:58) steht im Lernblatt ohne seine Grafik, ohne Eintrag in
  der log; ebenso wären v2, v3 und zufallsexperimente-und-pfadregeln-
  e8-k2-s4-v2 betroffen. Liegt in der Bank (form passt nicht zur
  Grafik); das Skript sollte es mindestens melden – offen.
- bank-pruef.py kennt die Arten 1, 2 und 6 nicht; mit der Modusprüfung
  aus dem Skript fielen sie schon beim Schreiben der Bank auf.
