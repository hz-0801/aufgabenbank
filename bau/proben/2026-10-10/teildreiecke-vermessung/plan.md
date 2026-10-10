# Plan: Teildreiecke in Figuren und Vermessung (Trigonometrie, Lerneinheit 3)

Bau 10.10.2026 nach `bau/bauauftrag.md`, Kennung 56N, Standardlage:
Klasse 10 (OS), sicher sind Lerneinheit 1 und 2 (Seite mit mal oder
geteilt, Winkel mit der Umkehrtaste) und Pythagoras 3 (Dreieck in der
Figur finden), unsicher bei Neuem, allein, Ziel P10.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe (Katalog, Prüfungsform) | braucht |
|---|---|
| Teilwinkel, dann Seite mit tan (2016-OS-K7c, Niveau III) | Teilwinkel als Unterschied (D) |
| Berghöhe mit Gerätehöhe und Plattform (2018-OS-K4d) | Dreieck beginnt am Gerät, Höhe addieren (C) |
| Kathete als Unterschied, nicht die ganze Seite (2023-OS-K7b) | Hilfslinie (B) |
| Winkel im Hilfsdreieck des rechtwinkligen Trapezes (2020-OS-K5b) | Unterschied der Höhen als Kathete (B) |
| Strecke aus der Höhe berechnen (2026-FOR-K4c) | zwei Dreiecke an derselben Höhe (D) |
| Höhe für die Fläche, Schenkel für den Umfang (2015-OS-K5d, 2022-OS-K5e) | Teildreieck in der Figur, Ergebnis weitergeben (A) |

Darunter: Teildreieck finden (rechter Winkel oder Höhe einzeichnen) →
vom Winkel aus benennen → fehlende Kathete zuerst ausrechnen → rechnen
wie in 1 und 2 → Ergebnis weitergeben. Neu gegenüber 1 und 2 ist nur
das Finden und das Weitergeben.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Teildreieck in der Figur | Höhe, Diagonale: das Dreieck liegt in der Figur, alle Seiten sind da; Fläche als Weitergabe |
| B | Hilfslinie: Kathete als Unterschied | jetzt fehlt eine Kathete; Hilfslinie gegeben → selbst → Überstand |
| C | Vermessung: Höhenwinkel und Gerätehöhe | Dreieck im Gelände, Zusatzstück addieren; sin bei schräger Länge; rückwärts |
| D | Zwei Schritte | Teilwinkel und zwei Dreiecke an derselben Höhe; Plan in Worten |
| T | Probetest | je ein Stück aus B (Überstand, cos⁻¹), C (Gerätehöhe), A+D (Fläche aus zwei Dreiecken), C mit Fenster (Ziel) |

Ziele (Modell selbst finden, Antwortform wechselt): A Reicht das Holz?
B Welches Dach ist steiler, um wie viel? C Stimmt die Angabe im
Prospekt? D Ist der Abstand größer als der Turm? T Um wie viel
verschätzt sie sich?

## 3 Änderungen gegenüber dem Katalog

- Gestrichen fürs Blatt: Parallelogramm (Fußpunkt auf der Verlängerung),
  zweiter Weg mit Pythagoras, Stützdreieck in Pyramide und Kegel (kein
  P10-Original), Fehler finden, Begründen; Parallelogramm und Stützdreieck
  bleiben im Bestand der Bank.
- Höhenwinkel wird in C eingeführt (Satz), weil kein früherer Abschnitt
  ihn erklärt.
- Teilwinkel in D statt am Anfang: er braucht ein sicheres Teildreieck.

## 4 Feste Zahlen (sympy, `pruef` in der Bank)

A: 6 tan 40° ≈ 5,03, A ≈ 30,2; 9 sin 55° ≈ 7,4; 5 sin 60° ≈ 4,3,
A ≈ 41,1; 2 · 6 sin 35° ≈ 6,9; Giebel 4,5 tan 38° ≈ 3,52, A ≈ 15,8 < 16.
B: tan⁻¹(0,9/4) ≈ 12,7°; tan⁻¹(3/6) ≈ 26,6°; tan⁻¹(3,5/3) ≈ 49,4°;
3 : cos 56° ≈ 5,4; Dächer 8,5° und 11,3°, Unterschied 2,8°.
C: 25 tan 32° + 1,6 ≈ 17,2; 40 tan 38° + 1,5 ≈ 32,8; 60 sin 35° + 1,2 ≈
35,6; 34,4 : tan 40° ≈ 41,0; 50 tan 33° + 1,4 ≈ 33,9 (1,1 m weniger).
D: 9 sin 40° : sin 65° ≈ 6,4; 8 sin 50° : tan 35° ≈ 8,8; 80 tan 22° ≈
32,3; AB ≈ 8,01 + 4,68 ≈ 12,7; Turm 49,93 − 23,44 ≈ 26,5 < 30.
T: cos⁻¹(2/3) ≈ 48,2°; 45 tan 37° + 1,55 ≈ 35,5; Fläche ≈ 34,6;
18 tan 24° + 6,5 ≈ 14,5 (1,5 m zu hoch geschätzt).

## 5 Form

Gesetzt mit `werkzeuge/setzer.py trigonometrie 3` aus dem Lernweg-Block
56N (Katalog, Form abschnitte), Sorten selbst und tisch-alt. Skizzen aus
einem Skript (Maße aus den Zahlen, Beschriftung neben der Linie,
Zahlen nur an einer Strecke).
