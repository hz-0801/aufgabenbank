# Plan: Dreieck (Flächen, Lerneinheit 3), SC4

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 7 (Katalog
OS Kl. 7–8, GYM bis 7), allein; sicher: Rechteck, Einmaleins, Teilen,
Flächeneinheiten. Ziel P10. Heft 6 Seiten: Übersicht, A–D, T.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe | braucht |
|---|---|
| Grundseite aus Dreiecksfläche, Faktor 2 (2020-OS-K7b) | Teildreieck rechtwinklig sehen (A), rückwärts mal 2, durch h (C) |
| Flächeninhalt Dreieck (2015-OS-K6c, 2022-OS-K5e) | Höhe zur Grundseite, nicht die schräge Seite (A), Höhe außen, passende Seite (B) |
| Term zu Figur: Umfang 3·a, Fläche rechtwinklig (2024-OS-B1c, 2022-OS-B1e) | Umfang alle Seiten, Höhe zählt nicht; Buchstaben statt Zahlen (D) |

## 2 Lernweg

| Kennung | Abschnitt | Grund |
|---|---|---|
| A | Fläche aus Grundseite und Höhe | Kern; rechtwinklig: Katheten sind g und h |
| B | Die passende Höhe finden | Höhe außen, Höhe zu einer schrägen Seite, Höhe = Abstand |
| C | Grundseite oder Höhe rückwärts | P10-Zielmarke (Faktor 2) |
| D | Umfang und Terme | Umfang gegen Fläche; Term zu Figur (Kl. 7 kennt Variablen) |
| T | Probetest | Ankreuzen, P10-Form ohne Figur, Term, Fläche und Umfang in einer Sache |

Ziele (Modell selbst, Antwortform wechselt): A welcher Wimpel größer,
um wie viel · B hat Tom recht? (gleich groß) · C passt das Schild?
(ja, Luft) · D wessen Seite länger, um wie viel · T reicht Kante,
reicht Rasen (je ja/nein).

Der Thema-Weg setzt das Parallelogramm (E2, ungebaut) vor das Dreieck;
die Höhe wird darum in A und B selbst eingeführt, nicht vorausgesetzt.

## 3 Schritte je Aufgabe → Beispiel

Beispielschritte: A1 Höhe finden, A2 g·h:2, A3 rechtwinklig, A4
vergleichen/Differenz · B1 Höhe außen, gehört zu ihrer Seite, B2 schräge
Seite weglassen, B3 rechnen · C1 Formel mit Zahlen, C2 mal 2, C3 durch
h, C4 Probe · D1 Umfang alle Seiten (Höhe nicht), D2 u = 3·a, D3 a = u:3,
D4 Fläche mit Buchstaben.
A1 (A1–2), A2 (A2), A3 (A3), A4 (A2–4). B1 (B1–3), B2 (B1, Höhe zu BC),
B3 (B1, Abstand = Höhe), B4 (B1, A2, A4). C1 (C1–3), C2 (C1–3), C3 (A3,
C1–3), C4 (C1–3, A4). D1 (D1–2), D2 (D1, D4), D3 (D4), D4 (D3, Quadrat
u:4 aus E1, A4). T1 (A1–2), T2 (A3, C), T3 (D1, D4), T4 (D1, A3, A4).

## 4 Nicht genommen

Fehler finden, Begründen (halbes Parallelogramm) nach Bauauftrag 4;
Rechenweg beschreiben (2015-OS-K5d) und Seiten aus Pythagoras/Sinus
(gehören zu pythagoras/trigonometrie). Zahlen mit Python/sympy in
`tmp/bau.py` geprüft (check je Zeile), bank-pruef 0 Abweichungen;
Skizzen aus den Koordinaten gerechnet (Seitenlängen nachgeprüft).
