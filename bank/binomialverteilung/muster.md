# Musterbeispiele: binomialverteilung

Je Verfahrenskette ein vorgerechnetes Beispiel zum Grundfall, mit
eigenen Zahlen (nicht aus dem Päckchen). Reine Daten; die Form auf
dem Blatt setzt der Zusammenbau (layout-befunde 55).

## e1 k1 Modell erkennen

Ein Spielwürfel hat die Form eines Tetraeders mit den Zahlen 1 bis 4;
er wird einmal geworfen. Treffer ist „4“. Mit welcher
Wahrscheinlichkeit tritt der Treffer ein?

| Schritt | Zeile |
|---|---|
| zwei Ausgänge | Treffer „4“, Niete „1, 2 oder 3“ |
| günstige Seiten | 1 von 4 Seiten |
| Ergebnis | p = 1/4 = 0,25 |

## e2 k1 Bernoulli-Formel

Eine Basketballspielerin trifft einen Freiwurf mit der
Wahrscheinlichkeit 0,7 und wirft 5-mal; X ist die Anzahl der Treffer.
Gib den Term für P(X = 3) an, ohne ihn auszurechnen.

| Schritt | Zeile |
|---|---|
| Anordnungen | (5 über 3) = 10 Pfade mit 3 Treffern |
| Treffer | 0,7³ |
| Nieten | 0,3² |
| Ergebnis | P(X = 3) = (5 über 3) · 0,7³ · 0,3² |

## e3 k2 Kumulierte Wahrscheinlichkeiten

Ein Würfel wird 25-mal geworfen; X ist die Anzahl der Sechsen.
Übersetze „mehr als 8 Sechsen“ in einen Ansatz mit P(X ≤ …).

| Schritt | Zeile |
|---|---|
| Bedingung | X > 8 |
| ganze Zahl | X ≥ 9 |
| Gegenereignis | X ≤ 8 |
| Ansatz | P(X > 8) = 1 − P(X ≤ 8) |
| Ergebnis | Grenze k = 8 |

## e4 k1 Umkehraufgaben

5 % der Lose einer Tombola gewinnen. Stelle den Ansatz auf: Wie viele
Lose muss man kaufen, damit mit mindestens 80 % Wahrscheinlichkeit
mindestens ein Gewinn dabei ist?

| Schritt | Zeile |
|---|---|
| Niete | kein Gewinn mit 1 − 0,05 = 0,95 |
| Gegenereignis | kein Gewinn bei n Losen: 0,95ⁿ |
| mindestens ein Gewinn | 1 − 0,95ⁿ |
| Ergebnis | 1 − 0,95ⁿ ≥ 0,8 |

## e5 k1 Verteilung im Diagramm

Ein Säulendiagramm zeigt die Verteilung der Anzahl X der Treffer
(Werte gerundet): P(X = 0) ≈ 17 %, P(X = 1) ≈ 38 %, P(X = 2) ≈ 32 %,
P(X = 3) ≈ 12 %, P(X = 4) ≈ 2 %. Mit welcher Wahrscheinlichkeit liegt
X zwischen 1 und 3, beide eingeschlossen?

| Schritt | Zeile |
|---|---|
| ablesen | P(X = 1) ≈ 38 %, P(X = 2) ≈ 32 %, P(X = 3) ≈ 12 % |
| addieren | 38 % + 32 % + 12 % = 82 % |
| Ergebnis | P(1 ≤ X ≤ 3) ≈ 82 % |
