# Musterbeispiele: flaecheninhalt-durch-integration

Je Verfahrenskette ein vorgerechnetes Beispiel am Grundfall, mit
eigenen Zahlen (nicht aus dem Päckchen). Reine Daten; die Form auf
dem Blatt setzt der Zusammenbau (layout-befunde 55).

## e1 k1 Fläche zwischen Graph und x-Achse

Aufgabe: Der Graph von $f(x) = 2x^2 - 8$ schließt mit der x-Achse
eine Fläche ein. Berechne ihren Inhalt.

| Schritt | Zeile |
|---|---|
| Nullstellen | $2x^2 - 8 = 0$, $x = -2$ oder $x = 2$ |
| Grenzen | $-2$ und $2$ |
| Stammfunktion | $F(x) = \frac{2}{3}x^3 - 8x$ |
| Integral | $F(2) - F(-2) = -\frac{32}{3} - \frac{32}{3} = -\frac{64}{3}$ |
| Betrag | $A = \left|-\frac{64}{3}\right| = \frac{64}{3}$ |
| Ergebnis | $A = \frac{64}{3} \approx 21{,}33$ |

## e2 k1 Fläche zwischen zwei Graphen

Aufgabe: Gegeben sind $f(x) = x^2 + 1$ und $g(x) = -x$. Berechne
den Inhalt der Fläche zwischen den Graphen von $x = 0$ bis $x = 3$.

| Schritt | Zeile |
|---|---|
| Differenz | $f(x) - g(x) = x^2 + x + 1$ |
| Lage | $x^2 + x + 1 > 0$ für alle $x$, $f$ liegt oben |
| Stammfunktion | $D(x) = \frac{1}{3}x^3 + \frac{1}{2}x^2 + x$ |
| Integral | $D(3) - D(0) = 9 + 4{,}5 + 3 - 0 = 16{,}5$ |
| Ergebnis | $A = 16{,}5$ |

## e3 k1 Zusammensetzen, Maßstab, Volumen

Aufgabe: Eine Fläche liegt über der x-Achse zwischen der y-Achse und
der Geraden $x = 5$. Oben wird sie für $0 \le x \le 2$ vom Graphen
von $f(x) = 0{,}5x^2$ begrenzt, danach von der waagerechten Strecke
in Höhe $2$. Berechne ihren Inhalt.

| Schritt | Zeile |
|---|---|
| Zerlegen | Integral von $0$ bis $2$ und Rechteck von $2$ bis $5$ |
| Integral | $\left[\frac{1}{6}x^3\right]_0^2 = \frac{8}{6} = \frac{4}{3}$ |
| Rechteck | $2 \cdot 3 = 6$ |
| Zusammensetzen | $A = \frac{4}{3} + 6$ |
| Ergebnis | $A = \frac{22}{3} \approx 7{,}33$ |

## e4 k1 Flächenbedingungen

Aufgabe: Für $m > 0$ schließen die Gerade $y = m \cdot x$ und der
Graph von $f(x) = x^2$ eine Fläche mit dem Inhalt $\frac{4}{3}$
ein. Bestimme $m$.

| Schritt | Zeile |
|---|---|
| Schnittstellen | $x^2 = m x$, $x = 0$ oder $x = m$ |
| Flächenterm | Integral von $0$ bis $m$ über $(m x - x^2) = \frac{1}{2}m^3 - \frac{1}{3}m^3 = \frac{1}{6}m^3$ |
| Bedingung | $\frac{1}{6}m^3 = \frac{4}{3}$ |
| umformen | $m^3 = 8$ |
| Ergebnis | $m = 2$ |

## e5 k1 Flächenbilanz

Aufgabe: Die Abbildung zeigt den Graphen von $f(x) = x - 1$; die
Gitterlinien haben den Abstand $1$. Bestimme den Wert des Integrals
von $0$ bis $3$ über $f(x)$, indem du Kästchen zählst.

| Schritt | Zeile |
|---|---|
| über der Achse | Dreieck von $1$ bis $3$: $2$ Kästchen |
| unter der Achse | Dreieck von $0$ bis $1$: $0{,}5$ Kästchen |
| Bilanz | $2 - 0{,}5 = 1{,}5$ |
| Ergebnis | Wert $= 1{,}5$ |
