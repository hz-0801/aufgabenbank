# Musterbeispiele: abstaende

Je Verfahrenskette ein vorgerechnetes Beispiel am Grundfall, mit
eigenen Zahlen (nicht aus dem Päckchen). Reine Daten; die Form auf
dem Blatt setzt der Zusammenbau (layout-befunde 55).

## e1 k2 Abstand zweier Punkte

Aufgabe: Berechne den Abstand der Punkte $A(1 | 2 | 0)$ und
$B(3 | 5 | 6)$.

| Schritt | Zeile |
|---|---|
| Verbindungsvektor | $\overrightarrow{AB} = (3 \| 5 \| 6) - (1 \| 2 \| 0) = (2 \| 3 \| 6)$ |
| Betrag | $d = \sqrt{2^2 + 3^2 + 6^2} = \sqrt{49}$ |
| Ergebnis | $d = 7$ |

## e2 k1 Abstand Punkt–Ebene

Aufgabe: Berechne den Abstand des Punktes $P(3 | 1 | 3)$ von der
Ebene $E\colon 2x + y + 2z = 4$ mit der Hesseschen Normalform.

| Schritt | Zeile |
|---|---|
| Normalenvektor | $\vec n = (2 \| 1 \| 2)$, $\|\vec n\| = \sqrt{4 + 1 + 4} = 3$ |
| HNF | $\tfrac{2x + y + 2z - 4}{3} = 0$ |
| einsetzen | $\tfrac{6 + 1 + 6 - 4}{3} = 3$ |
| Vorzeichen | positiv: $P$ liegt auf der dem Ursprung abgewandten Seite |
| Ergebnis | $d = 3$ |

## e3 k1 Lotfußpunkt

Aufgabe: Berechne den Lotfußpunkt $F$ von $P(4 | 1 | 2)$ auf
$g\colon \vec x = (0 | 1 | 1) + t \cdot (2 | 2 | 1)$ und den
Abstand von $P$ zu $g$.

| Schritt | Zeile |
|---|---|
| Laufpunkt | $F_t(2t \| 1 + 2t \| 1 + t)$ |
| Verbindungsvektor | $\overrightarrow{PF_t} = (2t - 4 \| 2t \| t - 1)$ |
| Lotbedingung | $\overrightarrow{PF_t} \circ (2 \| 2 \| 1) = 9t - 9 = 0$ |
| Parameter | $t = 1$ |
| Lotfußpunkt | $F(2 \| 3 \| 2)$ |
| Abstand | $\|\overrightarrow{PF}\| = \|(-2 \| 2 \| 0)\| = \sqrt{8}$ |
| Ergebnis | $F(2 \| 3 \| 2)$, $d \approx 2{,}83$ |

## e4 k1 Abstand als Argument

Aufgabe: $P(1 | 1 | 1)$ liegt in $E_1\colon 2x + y + 2z = 5$,
$Q(0 | 0 | -2)$ in der parallelen Ebene
$E_2\colon 2x + y + 2z = -4$. Ist $PQ$ kleiner, größer oder genauso
groß wie der Abstand der Ebenen? Begründe.

| Schritt | Zeile |
|---|---|
| Richtung | $\overrightarrow{PQ} = (-1 \| -1 \| -3)$, kein Vielfaches von $(2 \| 1 \| 2)$ |
| Lage | $PQ$ steht schräg zu den Ebenen |
| Regel | das Lot ist die kürzeste Verbindung |
| Kontrolle | $\|\overrightarrow{PQ}\| = \sqrt{11} \approx 3{,}32$, Abstand $\tfrac{9}{3} = 3$ |
| Ergebnis | $PQ$ ist größer als der Abstand der Ebenen |
