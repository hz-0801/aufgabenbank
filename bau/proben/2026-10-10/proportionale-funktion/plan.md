# Plan: Proportionale Funktion (lineare Funktionen, Lerneinheit 1), VUC

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 8,
Oberschule, allein; sicher: Dreisatz, proportionale Zuordnung,
Koordinaten in vier Quadranten, Dezimalzahlen mal und durch. Ziel P10.

## 1 Rückwärts von den Zielaufgaben

Kein P10-Original für Einheit 1. Zielmarke (Katalog, RLP F, LISUM-PH
Jg. 8): zu einem Sachverhalt die Gleichung aufstellen, die
Ursprungsgerade zeichnen, m als Wert je Einheit deuten. Dazu die
P10-Formen, die Einheit 1 vorbereitet: Gleichung zu einem Tarif
ankreuzen (2021-OS-K7a, dort mit n), Wertetabelle einer Funktion
zuordnen, Graph einer Geraden lesen.

| Zielaufgabe | braucht |
|---|---|
| Sachverhalt → Gleichung, Graph, Deutung | m als Wert je Einheit (D), Ursprungsgerade zeichnen (B) |
| Gleichung zu Text ankreuzen | y = m·x von y = x + m unterscheiden (A, T) |
| Gleichung zu einem Graphen | Gitterpunkt ablesen, m = y : x (C) |
| Entscheiden: reicht es, wo billiger | x aus y (x = y : m), zwei m vergleichen (C, D) |

Darunter liegt überall: y : x gleich? → m → y = m·x → Werte, Graph,
rückwärts rechnen.

## 2 Lernweg

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Proportional? Gleichung aus der Tabelle | Quotient y : x ist der Kern; aus ihm kommt m; Falle „fester Zuwachs“ |
| B | Den Graphen zeichnen | Wertetabelle → Punkte → Gerade durch (0\|0); m ganz, Dezimal, Bruch, negativ |
| C | Gleichung am Graphen ablesen | Umkehrung von B; steiler = größeres m; zwei Geraden vergleichen |
| D | Sachaufgaben: m deuten, vorwärts und rückwärts | m = Wert je Einheit; x = y : m; Dreisatz als Kontrolle |
| T | Probetest | gemischt, Ankreuzform, Zeichnen, Tabelle ergänzen, Entscheidung |

Ziel je Abschnitt (Modell selbst finden, entscheiden):
A Lohnt der 10-kg-Sack? (nicht proportional), B Ist Jana vor 13 Uhr an
der Hütte? (Graph selbst anlegen), C Erdnüsse: Graph gegen 600 g für
2,70 €, D Reicht der Tank bis Hamburg?, T Schafft Lisa 7 km in 40 min?

## 3 Änderungen gegenüber dem Katalog

- Fehler finden (Differenz statt Quotient, k1-s7) gestrichen; die Falle
  steht als Erkennen in A3 (Tabelle mit festem Zuwachs) und als Fehler-
  zeile im Kopf.
- Dreisatz als Kontrolle nicht eigener Abschnitt, sondern Schritt in D.
- Neu: x aus y (x = y : m) in D; bereitet Einheit 3 (Argument) vor.
- Neu: zwei Geraden vergleichen (C4) nach LISUM-PH („Vergleichen von
  Graphen mit verschiedenen Steigungen, auch an Bewegungsgraphen“).
- Steigungsdreieck nur als Satz in C (1 nach rechts, m nach oben);
  geübt wird es in Einheit 2.

## 4 Feste Zahlen (sympy, Skript `pruef` je Zeile)

A: Bsp 8/2 = 12/3 = 20/5 = 4; 7; 1,5; Tabelle 2 → 2,5; Sack 13 € statt
15 €. B: Bsp y = 3x; 2x; 0,5x; ⅔x; −1,5x; Jana 18 : 4 = 4,5 h → 13:30.
C: Bsp (2|5) → 2,5; 3; 0,75; −1,5; Anna 45 − 30 = 15 km; Erdnüsse 5 €
gegen 4,50 € je kg. D: Bsp 25 l/min, 150 l, 16 min; 4,50 €; 15 min;
8,50 €/m → 27,20 €; 0,06 · 380 = 22,8 l > 21 l. T: 1,2x; 1,25; −0,5x;
3,5 (17,5; 8; 42); 6 · 7 = 42 min > 40.
