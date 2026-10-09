# Plan: Bruch als Anteil (Brüche und Dezimalzahlen, Lerneinheit 1)

Bau 10.10.2026 (Fable) nach `bau/bauauftrag.md`, Standardlage. Kennung
QG4. Erster Bau des Themas: Thema-Weg angelegt.

Lage: Klasse 7 Oberschule (Katalog nennt OS Kl. 5; die P10-Form fragt
fünf von neun Flächen-Originalen in Prozent, und Prozent als Hundertstel
ist Kl. 7 – darum Kl. 7, siehe bau/befunde-M3.md). Sicher: Teilen und
Vervielfachen im Kopf, Größen mit Komma. Allein, Ziel P10.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe | braucht |
|---|---|
| Kreis mit ungleichen Sektoren, Anteil ankreuzen, 3/12 statt 3/7 (2019-OS-B1c, Niveau II) | ungleiche Teile auf das kleinste Stück bringen (C); Zähler/Nenner (A) |
| halbe Kästchen, Mittenquadrat 1/2 (2024-OS-B1b) | in halben Kästchen zählen (C) |
| Kästchenfigur als Bruch und Prozent, 9/15 = 3/5 = 60 % (2014-OS-B1i) | Teil zum Ganzen, nicht zum Rest (A); Merkbrüche in Prozent (E) |
| 20 % von 15, 25 % von 24 Kästchen markieren (2022-OS-B1a, 2023-OS-B1d) | Prozent → Merkbruch (E); Ganzes : Nenner (B) |
| 6/7 von 28 schraffieren, 3/8 von 8 (2017-OS-B1a, 2021-OS-B1b) | Zähler ist Zahl der Teile, nicht der Kästchen (B) |
| Viertel im leeren Quadrat (2025-OS-B1c) | selbst gleich teilen (B) |
| 3/4 von 1,2 kg (2018-OS-B1a) | Ganzes : Nenner · Zähler mit Komma und Einheit (D) |
| Rest bei 2/3 von 600 l (2015-OS-B1h) | Rest = Ganzes − Bruchteil (D) |

## 2 Lernweg

| Abschnitt | Name | Grund für die Stelle |
|---|---|---|
| A | Anteil ablesen: Zähler und Nenner | Kern; Falle Teil-zu-Rest gleich in der zweiten Aufgabe |
| B | Anteil einzeichnen | Umkehrung von A; neu ist Ganzes : Nenner, wenn die Figur mehr Kästchen hat |
| C | Ungleiche Teile: erst gleich groß machen | das einzige Niveau-II-Original; halbe Kästchen und Sektoren |
| D | Bruchteil einer Zahl oder Größe berechnen | dieselbe Rechnung wie B ohne Bild, mit Komma, Einheit, Rest |
| E | Anteil in Prozent | P10-Form; Merkbrüche, dann wie B |
| T | Probetest | gemischt, alle P10-Formen |

Ziel je Abschnitt (Modell selbst erkennen, entscheiden/vergleichen):
A zwei Klassen, gleicher Anteil trotz anderer Zahlen; B Beet mit zwei
Bruchteilen, reicht es; C Pizza mit halbem Stück, genau ein Viertel;
D Saftflasche, bleibt ein Viertelliter; E Parkhaus 75 % < 80 %;
T Regentonne, läuft sie über.

## 3 Änderungen gegenüber dem Katalog

- Thema-Weg neu angelegt (fehlte).
- Gestrichen: Figur mit gegebenem Anteil auswählen (als eigener
  Abschnitt), Fehler finden, Begründen, Ganzes aus Bruchteil – nicht
  auf dem Blatt, Bank hält sie.
- Prozent als Anteil der Figur ist eigener Abschnitt E, weil fünf
  Originale so fragen; Umrechnen allgemein bleibt prozentrechnung.md.
- Kein Kürzen: Prozent über Merkbrüche (Figur : 4 = ein Viertel).

## 4 Zahlen (bank-pruef 0 Abweichungen; sympy-Kontrolle im Bau)

A 3/8, 1/6, 7/12, 4/10 und 6/10, 13/24, 1/2 = 1/2. B 9 von 12, 5, 4 von
6, 20 von 24, Viertel, 12 + 5 = 17 < 20, 3 frei. C 3/8, 5/16, 1/6, 3/8
(ankreuzen), 1/4, 3/12 = 1/4. D 2,1 kg, 15 min, 1,5 l, 32 l, 1750 m,
0,25 l. E 4 von 16, 50 %, 6 von 30, 75 %, 2 von 20, 75 % < 80 %.
T 40 %, 4/8, 15 von 25, 150 l, 2000 g, 290 l < 300 l.

## 5 Form

Sorten selbst (Übersicht, Formel auf einen Blick, je Abschnitt eine
Seite) und tisch-alt, aus den Bankzeilen mit werkzeuge/setzer.py
gesetzt. Grafiken ganz als TikZ in grafik (Gitter, Streifen, Kreis).
