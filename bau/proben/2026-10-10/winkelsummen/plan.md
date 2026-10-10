# Plan: Winkelsummen, Dreiecke und Vierecke (Winkel und Dreiecke, Lerneinheit 3)

Bau 10.10.2026 nach `bau/bauauftrag.md`, Kennung HDK, Standardlage:
Klasse 7 (Katalog: Kl. 7, Vierecke Kl. 5), sicher ist Lerneinheit 2
(Scheitel-, Neben-, Stufenwinkel, Nachbarwinkel im Trapez) und die
Vierecksarten (Zone), unsicher bei Neuem, allein, Ziel P10 („P10 oft“).

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe (Katalog, Prüfungsform) | braucht |
|---|---|
| dritter Winkel mit Dezimalgraden, Dach 180 − 62,8 − 34,9 (2017-OS-K4a) | Winkelsumme; Dezimal abziehen (A) |
| α = β = 70°, Seite und γ (2023-OS-B1g) | gleiche Winkel → gleiche Seiten; Spitze (B) |
| Trapez-/Parallelogramm-Eigenschaft ankreuzen (2026-FOR-B1c, 2016-OS-B1e) | Vierecksarten (C, Formel) |
| Drachen, Teildreieck 180 − 123 − 36 (2015-OS-K5b) | Drachen-Symmetrie, 360° (C), Teildreieck (D) |
| Teildreieck an der Höhe 180 − 90 − α (2022-OS-K5c) | Höhe: 90° am Fußpunkt (D) |
| δ = 55° an der Berghöhe über Nebenwinkel 120° (2018-OS-K4b) | Nebenwinkel aus E2 im Teildreieck (D) |
| rechten Winkel begründen über 45° + 45° (2025-OS-K2c, 2023-OS-K7a) | Basiswinkel bei Spitze 90° (B), Teilwinkel addieren (D) |

Darunter überall: Figur finden, in der der Winkel liegt → bekannte
Winkel sammeln (gleiche, Nebenwinkel) → von 180° oder 360° abziehen.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Winkelsumme im Dreieck | Kern; Dezimalgrade und rechter Winkel gleich mit |
| B | Gleichschenklige Dreiecke | braucht A; beide Richtungen (Basis → Spitze, Spitze → Basis), gleiche Winkel → gleiche Seiten |
| C | Winkelsumme im Viereck | 360° über zwei Dreiecke; Drachen (zwei gleiche Winkel); Vierecksarten |
| D | Winkel in Teildreiecken | mischt A, B und Nebenwinkel aus E2; rechten Winkel begründen |
| T | Probetest | Dezimal ankreuzen, Trapez (360° oder Nachbarwinkel aus E2), Außenwinkel, Drachen-Eigenschaft, Dächer vergleichen |

Ziele (Modell selbst finden, Antwortform wechselt): A Sonnensegel – hält
die Naht? (rechnen, entscheiden) · B Stehleiter – steht sie sicher?
(ankreuzen) · C Flugdrachen – stimmt der Bauplan? (eintragen) · D Zelt –
rechter Winkel oben? (begründen) · T zwei Satteldächer – welches steiler,
um wie viel? (vergleichen).

## 3 Schritt-Beispiel-Abgleich (vor dem Setzen)

| Aufgabe | Schritte | Beispiel |
|---|---|---|
| A1 | zwei Winkel addieren; von 180° abziehen | A1, A2 |
| A2 | dasselbe mit Dezimalgrad, gesucht bei B | A1, A2 |
| A3 | Bogen mit Punkt = 90°; abziehen | A3, A4 |
| A4 Segel | Dreieck sehen; dritte Ecke; mit 55° vergleichen | A1, A2 |
| B1 | Basiswinkel gleich; Spitze = 180 − 2·Basis | B1, B2 |
| B2 | Spitze gegeben → (180 − Spitze) : 2 | B3 |
| B3 | gleiche Winkel → Seiten gegenüber gleich; Spitze | B1 (umgekehrt, Satz), B2 |
| B4 Leiter | gleichschenklig sehen; Basis aus Spitze; vergleichen | B3 |
| C1 | drei Winkel addieren; von 360° abziehen | C1, C2 |
| C2 | Drachen: Seitenecken gleich; Rest halbieren | C3, C4 |
| C3 | Raute = vier gleiche Seiten | Formel C (Vierecksarten) |
| C4 Flugdrachen | Summe des Plans prüfen; Seitenecken neu | C1, C3, C4 |
| D1 | Teildreieck mit 90°; zweites Teildreieck; Teile addieren | D1, D3, D4 |
| D2 | Nebenwinkel bei D; Teildreieck | D2, D1 |
| D3 | gleichschenklig mit Spitze 90° → 45°; zweimal; addieren | B3, D1, D4 |
| D4 Zelt | Teildreiecke sehen; wie D3 | B3, D4 |
| T1 | Winkelsumme Dezimal | A1, A2 |
| T2 | 360° (oder Nachbarwinkel aus E2) | C1, C2 |
| T3 | Nebenwinkel außen; Winkelsumme | D2, A2 |
| T4 | Drachen: Diagonalen senkrecht | Formel C |
| T5 | gleichschenklig sehen; Basis aus Spitze; vergleichen | B3 |

Kein Rechenschritt ohne Beispiel; C3 und T4 sind Wissen aus der
Formelzeile C.

## 4 Änderungen gegenüber dem Katalog

- **Gestrichen fürs Blatt:** Vorstufen „Welches Dreieck?“ und „Welches
  Teildreieck?“ (die Beispiele benennen beides), Fehler finden, Beweis der
  Winkelsumme, Vielecke (Bank).
- **Gleichseitig** nur als Formelzeile B und Vorrat (kein eigener Typ).
- **Teildreieck mit Nebenwinkel** als Kern von D (Mischung mit E2), nicht
  nur Höhe; die Höhe ist der Sonderfall 90°.
- **Rechten Winkel begründen** in D statt eigener Abschnitt: braucht B
  (Spitze 90° → 45°) und D (Teile addieren).

## 5 Feste Zahlen (sympy, `pruef` in der Bank)

A: Bsp 52,4/71,3 → 56,3; 90/34 → 56; 38/95 → 47; 63,5/49,8 → 66,7;
90/27,5 → 62,5; Segel 66,5/59,5 → 54 < 55.
B: Bsp 68 → 44; 52 → 64; 69 → 42; 38 → 71; 65/65 → BC = 5 cm, 50;
Leiter 32 → 74 > 70.
C: Bsp 85/110/72 → 93; Drachen 64/100 → 98; 78/125/96 → 61;
Drachen 52/118 → 95; Flugdrachen 84 + 60 + 2·106 = 356, richtig 108.
D: Bsp 40/35 → 105, 75, 62 → 43, Probe 78; Höhe 63/48 → 27, 42, 69;
64 → 116, 38 → 26; 45 + 45 = 90.
T: 46,5/71,8 → 61,7; Trapez 71/64/116 → 109; außen 118, 47 → 62, 71;
Dächer 104 → 38, 38 − 35 = 3.

## 6 Satz (nach Bildkontrolle)

Heft 6 Seiten, Karo auf jeder Aufgabenseite (B und C nur drei Zeilen).
Winkelzahlen in \footnotesize auf der Winkelhalbierenden, frei von Linien
geprüft (Hilfsskript); Drachen ohne gezeichnete Achse, damit die Zahlen
an der Achse nicht in einer Linie stehen.
