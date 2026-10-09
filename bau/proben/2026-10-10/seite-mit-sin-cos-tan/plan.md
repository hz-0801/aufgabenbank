# Plan: Seite berechnen mit sin, cos und tan (Trigonometrie, Lerneinheit 1)

Bau 10.10.2026 nach `bau/bauauftrag.md`, Kennung N9M, Standardlage:
Klasse 10 (OS), sicher sind die Voraussetzungen aus dem Katalog
(Pythagoras, rechter Winkel, Bruch umstellen, Taschenrechner), unsicher
bei Neuem, allein, Ziel P10. Erster Bau des Themas: Thema-Weg angelegt.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe (Katalog, Prüfungsform) | braucht |
|---|---|
| sin γ = u/w als Bruch eintragen, Gleichung unter vier ankreuzen, Buchstaben r, s, t oder u, v, w (2025-B1g, 2020-B1c, 2018-B1g, 2017-B1j, 2019-B1h) | Seiten vom markierten Winkel aus benennen, in jeder Lage; Hypotenuse ist nicht immer der letzte Buchstabe (A, T) |
| sin 30° = 7/x nach x umstellen (2020-B1j) | x im Nenner: mal x, dann geteilt (C) |
| AB ≈ 614 m im Viereck mit Diagonale nachweisen, AD mit cos (2021-K3a/b) | rechtwinkliges Dreieck in der Figur sehen, Funktion selbst wählen (D, T) |
| Seite im Dreieck mit gezeichneter Höhe, geteilt durch den Sinus (2022-K5d) | Teildreieck mit Höhe, x im Nenner (D) |
| PB = 1,20 : tan 34,9° an der Dachwand (2017-K4b, Hauptmarke) | Ankathete gesucht beim Tangens: geteilt (C, T) |

Darunter liegt überall: rechter Winkel → Hypotenuse; vom Winkel aus G und
A → Funktion aus den zwei beteiligten Seiten → Gleichung → x oben: mal,
x unten: geteilt → Taschenrechner (DEG) → am Ende runden, Einheit.
Jeder Abschnitt endet mit einer Aufgabe ohne Figur, in der der Schüler
das Dreieck selbst skizziert und dann entscheidet.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Seiten vom Winkel aus benennen | ohne sichere Namen bricht alles; die P10-Basisaufgabe ist genau das |
| B | Kathete berechnen: mal | x im Zähler, kein Umstellen; sin → cos → tan, je eine Änderung |
| C | Seite im Nenner: geteilt | der P10-Fehler der Einheit (mal statt geteilt); erst wenn mal sitzt |
| D | Welche Funktion? Figuren und Sachen | P10 sagt nie, welche Funktion; Viereck mit Diagonale, Höhe, Schatten |
| T | Probetest | P10-Formen gemischt: Ankreuzen, Gleichung ohne Figur, Nachweis, Entscheidung |

Ziele (Modell selbst finden, dann entscheiden): A sin α = cos β?
B reicht die Leiter bis zum Sims? C ist die Rampe lang genug?
D fliegt der Drachen höher als der Mast? T reicht das Seil der
Seilrutsche?

## 3 Änderungen gegenüber dem Katalog

- **Gestrichen fürs Blatt:** H/G/A-Beschriften als eigene Stufe (steht
  im Beispiel A und im Vorrat), Taschenrechner-Werte als eigene Stufe
  (Hinweis DEG in Formel B und auf Seite 1), Rückwärts-Sprosse, Fehler
  finden, Begründen (Lehrer 09.10.: keine Rätsel- und Fehleraufgaben).
- **Mal vor geteilt getrennt** (B, C) statt nach Funktion sortiert wie
  die Kette (sin, cos, sin geteilt …): der Schüler lernt eine
  Rechenregel je Abschnitt, die Funktion wechselt innerhalb.
- **Anderer Winkel markiert** (A2) im selben Dreieck, damit das
  Tauschen von Gegen- und Ankathete sichtbar wird; Ziel A fragt es ohne
  Figur ab (sin α = cos β).
- **Hypotenuse nicht der letzte Buchstabe** (T1: s, nicht t) als Falle
  der Ankreuzform.
- **Nachweis** nur im Probetest (P10-Form), mit voller Rechnung.

## 4 Feste Zahlen (alle mit sympy geprüft, `pruef` in der Bank)

A: Brüche ohne Zahlen. B: Beispiel 10·sin 35° ≈ 5,7; 6·sin 52° ≈ 4,7;
9·cos 38° ≈ 7,1; 7·tan 33° ≈ 4,5; 8,5·cos 41° ≈ 6,4; Leiter 5·sin 70°
≈ 4,70 > 4,50. C: Beispiel 7 : sin 36° ≈ 11,9; 4 : sin 30° = 8;
7 : cos 50° ≈ 10,9; 5 : tan 42° ≈ 5,6; 4,5 : cos 60° = 9; Rampe
0,60 : sin 20° ≈ 1,75 > 1,60. D: Beispiel 50·sin 37° ≈ 30,1;
4,2 : sin 35° ≈ 7,3; 12,4·tan 38,5° ≈ 9,9; 620·cos 52° ≈ 382; Drachen
60·sin 50° ≈ 46,0 > 45. T: cos β = r/s; 8 : tan 40° ≈ 9,5;
1,40 : tan 36° ≈ 1,93; Seil 85 : cos 12° ≈ 86,9 < 90.

## 5 Form

Gesetzt mit `werkzeuge/setzer.py trigonometrie 1` aus dem Lernweg-Block
N9M (Katalog, Form abschnitte) in den Sorten selbst und tisch-alt.
Vorrat je Abschnitt in der Bank (Katalogzeile, Spalte Vorrat).
