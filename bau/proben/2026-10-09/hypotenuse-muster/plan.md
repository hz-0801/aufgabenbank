# Plan: Hypotenuse berechnen (Pythagoras, Lerneinheit 1), zweigleisig

Prüfstein 09.10.2026: gebaut nach `bau/muster-auftrag.md`, nicht nach dem
Bauauftrag. Schüler Kl. 9, Oberschule Berlin, Ziel P10; sicher: Quadrat,
Quadratwurzel, Runden, rechtwinkliges Dreieck erkennen. Zeit normal,
allein.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe (Katalog, Prüfungsform) | braucht |
|---|---|
| Gleichung zum Dreieck ankreuzen, Buchstaben x, y, z oder u, v, w (2017-B1d, 2021-B1h, 2026-B1j) | Hypotenuse = Seite gegenüber dem rechten Winkel, in jeder Lage und mit jedem Buchstaben (A) |
| Satz in Worten unter drei Aussagen (2022-B1g) | Satz als „Kathetenquadrate zusammen = Hypotenusenquadrat“ (A, Formel) |
| Entfernung im Gelände, AB = √1300 ≈ 36,1 m (2020-K7a) | Zwischenergebnis c², Wurzel geht nicht auf, runden (B); die längere gegebene Seite ist nicht automatisch die Hypotenuse (C) |
| Rampe 170 cm / 16 cm ≈ 170,8 cm (2025-K4a) | Sachskizze lesen (C); Ergebnis fast gleich der langen Kathete ist richtig (C) |
| Stab im Becher mit Überstand (2022-K2c) | Überstand addieren (C); Radius → Durchmesser ist Lerneinheit 3, hier nicht |

Darunter liegt überall: rechten Winkel finden → gegenüber die Hypotenuse →
Gleichung → c² → Wurzel → runden → Einheit. Die Ergänzungen des Lehrers
verlangen zusätzlich am Ende jedes Abschnitts eine Aufgabe ohne
gezeichnetes Dreieck, in der der Schüler das rechtwinklige Dreieck selbst
erkennt und danach entscheidet oder vergleicht.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Hypotenuse finden und berechnen (Wurzel geht auf) | Kern: Seite gegenüber dem rechten Winkel; glatte Zahlen, damit nur das Finden neu ist |
| B | Wurzel geht nicht auf, Dezimalzahlen, Einheiten | die P10-Zahlen sind nie glatt; Zwischenergebnis c², erst am Ende runden; Diagonale im Rechteck |
| C | Sachaufgaben mit Skizze | Leiter, Rampe, Gelände, Überstand – die Kontextform der P10 |
| T | Probetest | gemischt, Ankreuzformen der P10 und zwei Entscheidungsaufgaben |

Ziel je Abschnitt (Entscheidung, Dreieck selbst finden):
A Schrank aufrichten (Diagonale der Seitenwand gegen Raumhöhe),
B Abkürzung quer durch den Park (Ersparnis),
C Reicht die Leiter? (um wie viel zu kurz),
T Passt die Stange flach in den Laderaum?

## 3 Änderungen gegenüber dem Katalog

- **Gestrichen:** Quadrate über den Seiten zeichnen, Kästchen zählen,
  Zerlegungsbeweis, Fehler finden, Rückwärts-Aufgaben (Lehrer 09.10.:
  keine Rätsel- oder Herleitungsaufgaben; erklären tut das Beispiel).
- **Satz in Worten** nur als P10-Ankreuzform im Probetest, nicht als
  Herleitung.
- **Gleichung mit fremden Buchstaben** in A (rechnen) und in T (ankreuzen,
  dort ist die Hypotenuse a – Falle „c ist immer die Hypotenuse“).
- **Diagonale im Rechteck** in B statt eigener Abschnitt: dieselbe Rechnung,
  nur das Dreieck muss im Rechteck gesehen werden.
- **Längere gegebene Seite ist Kathete** (C2, Muster 2020-K7a) eigens geübt,
  weil das der P10-Fehler dieser Marke ist.
- **Rampe** (C1) mit Ergebnis knapp über der langen Kathete (Muster
  2025-K4a); die Lösung sagt, warum das stimmt.
- Kein Vorher-Abschnitt: Quadrat, Wurzel, Runden und rechter Winkel sitzen.

## 4 Feste Zahlen (alle mit sympy geprüft, `pruef` in aufgaben.jsonl)

A: Beispiel 6/8 → 10; 9/12 → 15; 8/15 → 17; Schrank 240/70 → 250 > 245.
B: Beispiel 4/7 → √65 ≈ 8,1; 5/9 → √106 ≈ 10,3; 2,5/4,2 → √23,89 ≈ 4,9;
1,2 m / 50 cm → 130 cm; Handy 6,5/14 → √238,25 ≈ 15,4; Park 160/70 →
√30500 ≈ 174,6, spart ≈ 55,4 m.
C: Beispiel Leiter 1,2/3,5 → 3,7; Rampe 240/18 → √57924 ≈ 240,7 cm;
Teich 34/12 → √1300 ≈ 36,1 m; Seil 6/3 → √45 ≈ 6,71 + 0,5 ≈ 7,2 m;
Leiter 4,7/2,0 → √26,09 ≈ 5,11 m > 5 m, zu kurz um ≈ 11 cm.
T: Satz in Worten; a² = b² + c²; Fußballfeld 105/68 → √15649 ≈ 125,1 m;
Laderaum 2,20/1,30 → √6,53 ≈ 2,56 m < 2,60 m, passt nicht.

## 5 Form

Selbstlernfassung: Seite 1 Übersicht (Kennung, Name, Seite, „kann ich“,
Nutzung, Nachbestellen), Seite 2 Formel auf einen Blick, je Abschnitt eine
Seite (1–2 Zeilen, Formel, Beispiel in Schritten mit Skizze, Aufgaben),
Probetest. Tischblatt: dieselben Aufgaben ohne Beispiel und Formel,
kompakt. Lösungen je Fassung als eigenes PDF, Ergebnis fett, Schritte
knapp. Beide Fassungen werden aus `aufgaben.jsonl` gesetzt.
