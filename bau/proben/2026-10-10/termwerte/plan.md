# Plan: Termwerte berechnen (Terme, Lerneinheit 5)

Bau 10.10.2026 (Opus) nach `bau/bauauftrag.md`, Standardlage. Kennung
MZE (reserviert). Erster Bau des Themas: Thema-Weg und Lernweg im
Katalog neu angelegt.

Lage: Klasse 7 Oberschule (Katalog: OS Kl. 6–7, GYM Kl. 6–7; negative
Zahlen sind Kl. 7). Sicher: Rechnen mit negativen Zahlen, Punkt vor
Strich. Allein, Ziel P10 (Termwert „oft“, Aufgabe 1).

## 1 Rückwärts von den Zielaufgaben

| Zielaufgabe | braucht |
|---|---|
| 5 · (x − 3) für x = −2 (2026-FOR-B1g) | negative Zahl einsetzen, Klammer zuerst (B) |
| (a + b) : c mit negativen Zahlen (2016-OS-B1i, 2021-OS-B1g, Ergebnis −3,5) | jede Variable ihre Zahl, Bruchstrich, Teilen mit Vorzeichen, Komma (D) |
| (a − 3)² − 2(a + 4,5) − a, a = −2 (2022-GYM-B2a) | Quadrat bei negativer Einsetzung (C) |
| Formel in einer Sache (Tarif, Anhalteweg) | Zahl aus dem Text, einsetzen, vergleichen (A-Ziel, T-Ziel) |

## 2 Lernweg (Heft 6 Seiten)

A Zahl einsetzen und ausrechnen · B Negative Zahlen einsetzen ·
C Quadrate · D Zwei Variablen und Bruchstrich · T Probetest.
Ziele (Antwortform wechselt): A Fahrradverleih, reicht das Geld
(rechnen/entscheiden) · B welcher Term ist größer, um wie viel
(rechnen/vergleichen) · C Wertetabelle, wo negativ (eintragen) ·
D größter Termwert (ankreuzen) · T Anhalteweg 30/50 km/h gegen 20 m
(rechnen/entscheiden).

## 3 Schritte je Aufgabe → Beispiel

| Aufgabe | Schritte | gezeigt in |
|---|---|---|
| A1 5x − 4 | einsetzen mit Malpunkt; Punkt vor Strich | Bsp A 1, 3 |
| A2 a–d | Klammer zuerst; x zweimal | Bsp A 1, 2 |
| A3 Tabelle 3x − 2 | wie A1, fünfmal | Bsp A |
| A4 Ziel 4 + 3h | h aus Text; einsetzen; mit 20 € vergleichen | Bsp A; Aufgabe sagt, was zu vergleichen ist |
| B1, B2 | Klammer um negative Zahl; Vorzeichen; Minus vor Minus | Formel B (drei Zeilen), Bsp B 3–4, S. 1 |
| B3 | Klammer im Term mit negativer Zahl | Bsp B 1–4 |
| B4 Ziel | zwei Termwerte, Differenz | Bsp B |
| C1–C3 | negative Zahl beim Quadrat in Klammern; Hoch vor Punkt | Formel C, Bsp C 1–4, S. 1 |
| C4 Ziel | Tabelle mit Quadrat; Vorzeichen ablesen | Bsp C, Bsp A (Tabelle A3) |
| D1 | zwei Variablen; Produkt mit Vorzeichen | Bsp D 1, S. 1 |
| D2, D3 | Bruchstrich: oben, unten, teilen; Komma | Bsp D 1–3 |
| D4 Ziel | vier Terme werten, größten wählen | D1, Bsp D |
| T1 | B | Bsp B |
| T2 4 · (x − 2), x = −3 | B | Bsp B |
| T3 2x² + x | C | Bsp C |
| T4 (a − b)/c | D | Bsp D |
| T5 a² − b | C + D | Bsp C, D |
| T6 Anhalteweg | v/10 (Bruchstrich), Quadrat, Punkt, Strich, mit 20 m vergleichen | Bsp D, C, A; A4 |

Kein Schritt ohne Beispiel.

## 4 Änderungen gegenüber dem Katalog

- Neu in der Kette Termwert (Sprossen 7–13): Klammer im Term,
  Wertetabelle, negative Zahl mit Klammer im Term, Werte vergleichen,
  zwei Variablen mit negativen Zahlen, Bruchstrich (P10 ’16, ’21),
  Formel aus einer Sache. Der Bruchstrich fehlte, obwohl zwei
  P10-Originale ihn verlangen.
- Nicht auf dem Blatt: negative Brüche als Einsetzung (s4, s5) und
  Quadrat einer Klammer mit zwei Variablen (s6): über der P10-Höhe der
  Oberschule; bleiben in der Bank.
- Merkkasten-Zahl (3x² für x = −2) gemieden.

## 5 Zahlen

Alle 46 Zeilen mit sympy geprüft (Bauskript, Ausdruck, Einsetzung,
Soll): A 18; 6 11 46; 13 20 11 8; 1 4 7 10 13; 22 €, fehlen 2 €.
B 16; 4 −5 7; 11 6 17 −9; 2 18; 11 gegen 8, um 3. C 44; 25 25 1 100;
16 8 6; 1 −3; 8 3 0 −1 0 3, negativ bei x = 1. D 3; 1 11 −12 −7; −2;
−2,5; b − a = 6. T 14; −20; 15; 1,5; 14; 18 m ja, 40 m nein.
