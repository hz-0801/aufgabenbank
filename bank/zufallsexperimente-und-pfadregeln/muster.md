# Musterbeispiele: zufallsexperimente-und-pfadregeln

Je Verfahrenskette ein vorgerechnetes Beispiel am Grundfall, mit
eigenen Zahlen (nicht aus dem Päckchen). Reine Daten; die Form auf
dem Blatt setzt der Zusammenbau (layout-befunde 55).

## e1 k1 Ereignisse als Mengen

Aufgabe: Eine Münze wird geworfen (K = Kopf, Z = Zahl), danach wird
ein Würfel mit den Seiten A, B, C, A, B, C geworfen. Gib die
Ergebnismenge als Tupel an. Prüfe, ob ein Laplace-Experiment vorliegt.

| Schritt | Zeile |
|---|---|
| erste Stufe | K oder Z |
| zweite Stufe | A, B oder C |
| Tupel aufschreiben | (K; A), (K; B), (K; C), (Z; A), (Z; B), (Z; C) |
| Anzahl | $2 \cdot 3 = 6$ |
| Laplace prüfen | jede Münzseite $\frac{1}{2}$, jeder Buchstabe $\frac{2}{6} = \frac{1}{3}$, jedes Tupel $\frac{1}{6}$ |
| Ergebnis | $\Omega$ hat 6 Tupel; ja, ein Laplace-Experiment |

## e2 k1 Laplace-Experimente

Aufgabe: Ein Glücksrad hat 16 gleich große Sektoren, 6 davon sind
grün. Wie groß ist die Wahrscheinlichkeit für Grün?

| Schritt | Zeile |
|---|---|
| alle Ergebnisse zählen | 16 Sektoren |
| günstige Ergebnisse zählen | 6 grüne Sektoren |
| günstige durch alle | $P = \frac{6}{16}$ |
| kürzen | $P = \frac{3}{8}$ |
| Ergebnis | $P(\text{grün}) = \frac{3}{8} = 0{,}375$ |

## e3 k1 Pfadregeln bei unabhängigen Stufen

Aufgabe: Ein Schütze trifft mit 70 %, sonst verfehlt er. Er schießt
zweimal. Beschrifte den Baum. Wie groß ist die Wahrscheinlichkeit für
erst verfehlt, dann getroffen?

| Schritt | Zeile |
|---|---|
| Äste der ersten Stufe | T $0{,}7$, V $0{,}3$ |
| Äste der zweiten Stufe | dieselben: T $0{,}7$, V $0{,}3$ |
| Pfad wählen | erst V, dann T |
| Pfad multiplizieren | $P = 0{,}3 \cdot 0{,}7$ |
| Ergebnis | $P = 0{,}21$ |

## e4 k1 Ohne Zurücklegen und Umlegen

Aufgabe: In einer Schale liegen 3 Zitronen- und 5 Orangenbonbons.
Zwei werden ohne Zurücklegen genommen. Wie groß ist die
Wahrscheinlichkeit für zwei verschiedene Sorten?

| Schritt | Zeile |
|---|---|
| Pfade finden | Zitrone–Orange und Orange–Zitrone |
| erster Pfad | $\frac{3}{8} \cdot \frac{5}{7} = \frac{15}{56}$ |
| zweiter Pfad | $\frac{5}{8} \cdot \frac{3}{7} = \frac{15}{56}$ |
| Pfade addieren | $P = \frac{15}{56} + \frac{15}{56} = \frac{30}{56}$ |
| Ergebnis | $P = \frac{15}{28}$ |

## e5 k1 Mammutbäume

Aufgabe: Ein Spieler verwandelt einen Freiwurf mit $0{,}6$. Er wirft
dreimal. Wie groß ist die Wahrscheinlichkeit für genau einen Fehlwurf?

| Schritt | Zeile |
|---|---|
| ein Pfad | $0{,}4 \cdot 0{,}6 \cdot 0{,}6 = 0{,}144$ |
| Positionen zählen | der Fehlwurf steht an Stelle 1, 2 oder 3: 3 Pfade |
| mal Anzahl | $P = 3 \cdot 0{,}144$ |
| Ergebnis | $P = 0{,}432$ |

## e6 k1 Situationsbäume

Aufgabe: 45 % der Mitglieder eines Vereins sind Jugendliche (J), die
übrigen Erwachsene (E). Unter den Jugendlichen fahren 70 % mit dem
Rad (R), unter den Erwachsenen 30 %. A heißt anders. Beschrifte den
Baum.

| Schritt | Zeile |
|---|---|
| erste Stufe Gruppe | J $0{,}45$, E $0{,}55$ |
| zweite Stufe unter J | R $0{,}7$, A $0{,}3$ |
| zweite Stufe unter E | R $0{,}3$, A $0{,}7$ |
| Kontrolle | an jedem Knoten ergeben die Äste 1 |
| Ergebnis | Baum mit J/E oben, R/A unten, sechs Äste beschriftet |

## e7 k1 Term und Ereignis

Aufgabe: Ein Würfel wird viermal geworfen. Welches Ereignis hat die
Wahrscheinlichkeit $\left(\frac{5}{6}\right)^3 \cdot \frac{1}{6}$?

| Schritt | Zeile |
|---|---|
| Faktoren zählen | vier Faktoren: vier Würfe |
| Basis $\frac{5}{6}$ lesen | keine Sechs, dreimal |
| Basis $\frac{1}{6}$ lesen | eine Sechs, einmal |
| Reihenfolge | kein Vorfaktor: feste Reihenfolge |
| Ergebnis | erst dreimal keine Sechs, dann eine Sechs |

## e8 k1 Rückwärts

Aufgabe: 40 % der Gäste eines Hotels sind Geschäftsreisende, von
ihnen buchen 25 % Frühstück. Insgesamt buchen 55 % Frühstück. Wie
groß ist der Anteil a unter den übrigen Gästen?

| Schritt | Zeile |
|---|---|
| Bedingung Pfadsumme = 0,55 | $0{,}4 \cdot 0{,}25 + 0{,}6a = 0{,}55$ |
| Pfad ausrechnen | $0{,}1 + 0{,}6a = 0{,}55$ |
| minus $0{,}1$ | $0{,}6a = 0{,}45$ |
| durch $0{,}6$ | $a = 0{,}75$ |
| Probe | $0{,}1 + 0{,}6 \cdot 0{,}75 = 0{,}55$ |
| Ergebnis | $a = 0{,}75$, also 75 % |
