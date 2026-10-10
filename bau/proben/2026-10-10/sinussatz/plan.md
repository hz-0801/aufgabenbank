# Plan: Sinussatz (Trigonometrie, Lerneinheit 4)

Bau 10.10.2026 nach `bau/bauauftrag.md`, Kennung XAD, Standardlage:
Klasse 10 (OS), sicher sind Lerneinheit 1–3 (Seite und Winkel im
rechtwinkligen Dreieck, Teildreieck in der Figur) und die Winkelsumme,
unsicher bei Neuem, allein, Ziel P10. Letzte P10-oft-Einheit des Themas:
Thema-Weg und Probetest des Themas endgültig.

## 1 Rückwärts von den Zielaufgaben (P10, alle mit Stern)

| Zielaufgabe (Katalog, Prüfungsform) | braucht |
|---|---|
| Seilbahn, stumpfer Winkel 108°, erst γ = 34° (2024-OS-K6d) | dritter Winkel (B), stumpfer Winkel bleibt (C) |
| Rampe, 141° nicht durch 39° ersetzen (2025-OS-K4c) | Nebenwinkel, stumpf im Sinussatz (C) |
| Nachweis Sichtlinie, Dreieck nicht rechtwinklig (2018-OS-K4c) | rechtwinklig oder nicht? (Vorgehen 1), Nachweis (D) |
| Viereck: 90° − 64°, dann 86° − 26° (2019-OS-K3c, Niveau III) | Teilwinkel (C) |
| DE mit Sinussatz, dann DP = DE − 10 (2020-OS-K7c) | dritter Winkel (B), Rest (D) |
| Wanderung JR + 2500 m (2014-OS-K2b) | Weg = Teil + Teil (D) |
| Aussage „BC = DC“ prüfen (2021-OS-K3c) | zwei Seiten vergleichen (B-Ziel, T4) |

Darunter überall: Paar aus Seite und Winkel gegenüber finden → fehlt
ein Winkel, ausrechnen → Sinussatz mit zwei Paaren → nach der Seite
umstellen → Ergebnis weitergeben. Falsche Paarung ist die Fehlerquelle
in sieben der neun Originale, darum zuerst und allein (A).

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Seite aus einem ganzen Paar | Kern: Paar finden, alle Winkel gegeben; erst ankreuzen, dann rechnen |
| B | Erst den dritten Winkel | in fast jedem Original fehlt der Winkel zum Paar |
| C | Winkel aus der Figur | Nebenwinkel (stumpf), Teilwinkel im Viereck: die Fallen 2019, 2024, 2025 |
| D | Ergebnis weitergeben | Weg, Rest, Nachweis nach rechtwinkligem Teildreieck |
| T | Probetest | je ein Stück aus A (ankreuzen), B (Brücke), C (Viereck, Niveau III), D (Umweg, Ziel) |

Ziele (Modell selbst finden, Antwortform wechselt): A Reicht die
Schnur? B Welcher Turm ist näher, um wie viel? C Stimmt das Schild?
D Wie viel spart sie? T Hat der Kapitän recht (höchstens 2 km)?

## 3 Änderungen gegenüber dem Katalog

- Nicht aufs Blatt: Kosinussatz, Winkel mit dem Sinussatz (kein
  P10-Original, nur RLP G), Herleitung, zweiter Weg über die Höhe,
  Fehler finden, Begründen; alles bleibt in der Bank.
- „Rechtwinklig oder nicht?“ nur als Schritt 1 im Vorgehen und als
  falsche Option in A1/T1; geübt in D3 (erst rechtwinkliges Dreieck,
  dann Sinussatz).
- Stumpfer Winkel kein eigener Abschnitt: im Nebenwinkel (C1, C2) und im
  Viereck (T3) mitgeübt, Satz einmal in C.

## 4 Feste Zahlen (sympy, `pruef` in der Bank)

A: 8 sin 45°/sin 70° ≈ 6,0; 10 sin 50°/sin 72° ≈ 8,1; 6 sin 80°/sin 55°
≈ 7,2; 9 sin 48°/sin 64° ≈ 7,4; Segel 5,4 sin 58°/sin 72° ≈ 4,82 > 4,5.
B: γ = 68°, 7 sin 48°/sin 68° ≈ 5,6; 10,1; 7,7; 85 sin 72°/sin 45° ≈
114,3; Türme 409,2 und 322,8, S um ≈ 86 m näher.
C: 140°, 15°, 30 sin 25°/sin 15° ≈ 49,0; 9,3; Seil 2,5 sin 110°/sin 32°
≈ 4,4; 10 sin 32°/sin 80° ≈ 5,4; Schild 800 sin 130°/sin 20° ≈ 1792 m.
D: 2,4 + 3,782 ≈ 6,2; 1,8 + 2,428 ≈ 4,2; 11,17 − 6 ≈ 5,2; AC ≈ 6,527,
CD ≈ 3,80; Feldweg 7,35 − 6,62 ≈ 0,7 km.
T: r/sin 41° = t/sin 77°; 140 sin 57°/sin 45° ≈ 166,0; 9 sin 115°/sin 35°
≈ 14,2; Umweg 5,6 + 7,60 − 11,48 ≈ 1,7 km ≤ 2 km.

## 5 Form

Gesetzt mit `werkzeuge/setzer.py trigonometrie 4` aus dem Lernweg-Block
XAD (Katalog, Form abschnitte), Sorten selbst und tisch-alt. Skizzen aus
einem Skript: Maße aus den Zahlen, Beschriftung außen neben der Linie,
nur gegebene Winkel mit Zahl, ein Winkel je Ecke.
