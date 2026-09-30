# Musterbeispiele: ebenen

Je Verfahrenskette ein vorgerechnetes Beispiel am Grundfall, mit
eigenen Zahlen (nicht aus dem Päckchen). Reine Daten; die Form auf
dem Blatt setzt der Zusammenbau (layout-befunde 55).

## e1 k1 Parameterform

Aufgabe: Gib eine Parametergleichung der Ebene mit dem Stützpunkt
$P(2 | 1 | 4)$ und den Spannvektoren $(3 | 1 | 0)$ und $(0 | 2 | 1)$
an.

| Schritt | Zeile |
|---|---|
| Stützvektor | $\overrightarrow{OP} = (2 \| 1 \| 4)$ |
| Spannvektoren | $\vec u = (3 \| 1 \| 0)$, $\vec v = (0 \| 2 \| 1)$ |
| nicht parallel? | $(0 \| 2 \| 1)$ ist kein Vielfaches von $(3 \| 1 \| 0)$ ✓ |
| einsetzen | $\vec x = (2 \| 1 \| 4) + r \cdot (3 \| 1 \| 0) + s \cdot (0 \| 2 \| 1)$ |
| Ergebnis | $E\colon \vec x = (2 \| 1 \| 4) + r \cdot (3 \| 1 \| 0) + s \cdot (0 \| 2 \| 1)$, $r, s \in \mathbb{R}$ |

## e2 k1 Koordinatengleichung bestimmen

Aufgabe: Bestimme einen Normalenvektor der Ebene mit den
Spannvektoren $\vec u = (1 | 2 | 1)$ und $\vec v = (4 | 0 | 1)$.

| Schritt | Zeile |
|---|---|
| Skalarprodukt mit $\vec u$ | $n_1 + 2n_2 + n_3 = 0$ |
| Skalarprodukt mit $\vec v$ | $4n_1 + n_3 = 0$, also $n_3 = -4n_1$ |
| Komponente wählen | $n_1 = 2$, also $n_3 = -8$ |
| ausrechnen | $2 + 2n_2 - 8 = 0$, also $n_2 = 3$ |
| Probe | $2 + 6 - 8 = 0$ ✓ und $8 + 0 - 8 = 0$ ✓ |
| Ergebnis | $\vec n = (2 \| 3 \| -8)$ (jedes Vielfache ebenso) |

## e2 k2 Normalenvektor und Nachweise

Aufgabe: Gib zwei Normalenvektoren von $E\colon 4x - 2y + 5z = 20$
an.

| Schritt | Zeile |
|---|---|
| ablesen | Zahlen vor $x$, $y$, $z$: $(4 \| -2 \| 5)$ |
| Vielfaches bilden | $2 \cdot (4 \| -2 \| 5) = (8 \| -4 \| 10)$ |
| Ergebnis | $\vec n = (4 \| -2 \| 5)$ und $\vec n = (8 \| -4 \| 10)$ |

## e3 k1 Besondere Lagen

Aufgabe: Die Punkte $(2 | 5 | 1)$, $(4 | 5 | 3)$ und $(0 | 5 | 7)$
liegen in einer Ebene. Gib ihre Gleichung an und beschreibe ihre Lage.

| Schritt | Zeile |
|---|---|
| gleiche Koordinate suchen | alle drei Punkte haben $y = 5$ |
| Gleichung | $y = 5$ |
| fehlende Variablen | $x$ und $z$ fehlen: parallel zur $xz$-Ebene |
| Ursprung prüfen | $0 \ne 5$: keine Koordinatenebene |
| Ergebnis | $E\colon y = 5$, parallel zur $xz$-Ebene, 5 Einheiten daneben |

## e4 k2 Parallele Ebenen

Aufgabe: Gib eine Gleichung der Ebene $F$ an, die parallel zu
$E\colon x + 3y - 2z = 5$ ist und durch $P(2 | 4 | 1)$ geht.

| Schritt | Zeile |
|---|---|
| Normalenvektor übernehmen | $F\colon x + 3y - 2z = e$ |
| Punkt einsetzen | $e = 2 + 3 \cdot 4 - 2 \cdot 1 = 12$ |
| Probe | $12 \ne 5$: $F$ ist echt parallel, nicht identisch |
| Ergebnis | $F\colon x + 3y - 2z = 12$ |
