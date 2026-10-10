# Plan: Winkel an Geradenkreuzungen und Parallelen (Winkel und Dreiecke, Lerneinheit 2)

Bau 10.10.2026 nach `bau/bauauftrag.md`, Kennung FP6, Standardlage:
Klasse 7 (Katalog: LS-AA Kl. 7, OS Kl. 6–7), sicher ist Lerneinheit 1
(Winkel benennen, Teilwinkel addieren und abziehen, Dezimalgrad), unsicher
bei Neuem, allein, Ziel P10 („P10 oft“).

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe (Katalog, Prüfungsform) | braucht |
|---|---|
| Scheitelwinkel an verlängerten Dreiecksseiten, 65° überflüssig (2019-OS-B1a) | Kreuzung in der Figur sehen; Scheitelwinkel; Angabe weglassen (A, B) |
| Kreuzung mit Teilwinkel 50° − 30° (2014-OS-B1f) | erst ganzer Winkel (Scheitel/Neben), dann Teil abziehen (A, B) |
| Wechselwinkel zu 74° (2020-OS-B1g) | Parallelen erkennen, Wechselwinkel (C) |
| Nebenwinkel des Stufenwinkels 180° − 53° (2015-OS-B1d) | Stufenwinkel, dann daneben 180° minus (A, C) |
| Parallelogramm 180° − 75° (2026-FOR-B1i); Trapez 180° − 107° mit überflüssigen Winkeln (2021-OS-B1i); Deich 180° − 56° (2023-OS-K2a) | Nachbarwinkel zwischen Parallelen; im Trapez nur an den Schenkeln (D) |

Darunter überall: zwei Geraden suchen, an denen der Winkel liegt → Lage
benennen → gleich oder 180° minus. Alles läuft auf Scheitel- und
Nebenwinkel zurück; Parallelen machen aus zwei Kreuzungen eine.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Scheitel- und Nebenwinkel | Kern jeder Aufgabe; alle vier Winkel aus einem |
| B | Kreuzungen in Figuren | verlängerte Seiten und Teilwinkel (2 P10-Typen); braucht nur A |
| C | Winkel an Parallelen | Stufen-, Wechselwinkel, daneben 180° minus (Falle 2015) |
| D | Parallelogramm und Trapez | dieselbe Regel in Vierecken; Trapez: nur an den Schenkeln |
| T | Probetest | Parallelogramm (ankreuzen), Teilwinkel, verlängerte Seiten, Nebenwinkel-Falle, Gitter |

Ziele (Modell selbst finden, Antwortform wechselt): A Schere – reicht die
Öffnung? (begründen) · B Radweg zwischen zwei Straßen – welcher Winkel
größer, um wie viel? (rechnen) · C Radweg über zwei Schienen – sicher?
(ankreuzen) · D Deich – Böschungswinkel eintragen, Vorschrift erfüllt?
(eintragen) · T Rankgitter – welche Winkel 65°, welche 115°? (zuordnen).

## 3 Schritt-Beispiel-Abgleich (vor dem Setzen)

| Aufgabe | Schritte | Beispiel |
|---|---|---|
| A1–A3 | Scheitel gleich; Neben 180° minus; gegenüber vom Neben | A1, A2, A3 |
| A4 Schere | Griffe/Klingen = zwei Geraden; Scheitelwinkel; vergleichen | A1 |
| B1 | Scheitel; Teil abziehen | B2, B3 |
| B2 | Neben 180° minus; Teil abziehen | A2, B3 |
| B3 Radweg | stumpfer = 180° − 70°; minus 52°; vergleichen | A2, B3 |
| C1 | Stufen- und Wechselwinkel | C2, C3 |
| C2 | Stufenwinkel, daneben 180° minus | C2, C4 |
| C3 Schienen | 180° − 118° (Neben); Stufenwinkel an Schiene 2; vergleichen | A2, C2 |
| D1 | Nachbar 180° minus; Gegenwinkel | D1–D3 |
| D2/D3 | Nachbar an den Seiten zwischen den Parallelen | D1, D2 |
| D4 Deich | Krone ∥ Boden: unten = 180° − oben; vergleichen | D1 |
| T1 | Nachbar im Parallelogramm | D2 |
| T2 | Scheitel; Teil abziehen | B2, B3 |
| T3 | Kreuzung an der Ecke; Scheitel; Angabe weglassen | B1, B2, B4 |
| T4 | Stufenwinkel; daneben 180° minus | C2, C4 |
| T5 Gitter | Stufenwinkel; Neben; Scheitel | C2, C4, A1 |

Kein Schritt ohne Beispiel. Teilwinkel abziehen ist Lerneinheit 1, steht
aber zusätzlich im Beispiel B.

## 4 Änderungen gegenüber dem Katalog

- **Gestrichen fürs Blatt:** Vorstufen „Sind die Geraden parallel?“ und
  „Winkelpaar benennen“ (die Beispiele benennen jede Lage), Fehler finden,
  Begründen, Parallelität prüfen (Lehrer 09.10.; bleibt Bank).
- **Teilwinkel und verlängerte Seiten als eigener Abschnitt B** vor den
  Parallelen: beides braucht nur Scheitel- und Nebenwinkel.
- **Trapez mit anders liegenden Parallelen** (AD ∥ BC) als eigene Stufe
  D3: der Schüler muss die Pfeile lesen, statt „oben/unten“ zu raten.
- Seite 1 nennt nur „gegenüber gleich, daneben 180°“; die Trapez-Regel steht
  nur in D, „nur bei Parallelen“ nur in C, „nicht maßstabsgerecht“ nur im
  Probetest.

## 5 Feste Zahlen (sympy, `pruef` in der Bank)

A: Bsp 65 → 115, 65, 115; 40 → 140, 40, 140; β = 128 → 52, 52, 128;
72,5 → 72,5, 107,5, 107,5; Schere 34 < 40.
B: Bsp 78 − 33 = 45 (62 überflüssig); 74 − 31 = 43;
180 − 114 − 28 = 38; Radweg 180 − 70 − 52 = 58, 58 − 52 = 6.
C: Bsp 62, 62, 118; 56 und 56; 180 − 48 = 132; Schienen 180 − 118 = 62 > 60.
D: Bsp 70 → 110, 70, 110; 58 → 122, 58, 122; 66/79 → δ 114, γ 101;
84/97 → β 96, δ 83; Deich 180 − 146 = 34 > 30, 180 − 152 = 28.
T: 68 → 112; 67 − 29 = 38; 39 (61 überflüssig); 180 − 57 = 123; Gitter 65/115.

## 6 Satz (nach Bildkontrolle)

Heft auf 6 Seiten mit Karo auf jeder Aufgabenseite nur mit drei Aufgaben in
B und C: verlängerte Seiten ohne Teilwinkel (früher B1, γ = 98°) und die
getrennten Stufen-/Wechselwinkel-Aufgaben stehen im Vorrat; C1 fragt
Stufen- und Wechselwinkel in einer Figur. Verlängerte Seiten übt das
Beispiel B und prüft T3.
