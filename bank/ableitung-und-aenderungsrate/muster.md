# Musterbeispiele: ableitung-und-aenderungsrate

Je Verfahrenskette ein vorgerechnetes Beispiel am Grundfall, mit
eigenen Zahlen (nicht aus dem Päckchen). Reine Daten; die Form auf
dem Blatt setzt der Zusammenbau (layout-befunde 55).

## e1 k1 Mittlere Änderungsrate

Aufgabe: Um 7 Uhr liegen $350$ Pakete im Lager, um 12 Uhr $600$.
Berechne die mittlere Änderungsrate der Paketzahl in diesem Zeitraum.

| Schritt | Zeile |
|---|---|
| Differenz | $600 - 350 = 250$ |
| Länge des Zeitraums | $12 - 7 = 5$ Stunden |
| durch die Länge teilen | $\frac{250}{5} = 50$ |
| Ergebnis | $50$ Pakete je Stunde |

## e2 k1 Ableitung an einer Stelle

Aufgabe: Die Temperatur in einem Gewächshaus wird durch
$T(t) = -t^2 + 8t + 12$ beschrieben ($t$ in Stunden, $T(t)$ in °C).
Berechne $T'(2)$ und gib an, was die Zahl bedeutet.

| Schritt | Zeile |
|---|---|
| ableiten | $T'(t) = -2t + 8$ |
| Stelle einsetzen | $T'(2) = -4 + 8 = 4$ |
| deuten | die Temperatur steigt in diesem Moment um $4$ °C je Stunde |
| Ergebnis | $T'(2) = 4$ °C je Stunde |

## e3 k1 Von der Sekante zur Tangente

Aufgabe: Gegeben ist $f(x) = x^2 + 2x$ mit dem Punkt $P(1 | 3)$.
Berechne die Steigung der Sekante durch $P$ und $Q(1 + h | f(1 + h))$
für $h = 1$; $0{,}1$; $0{,}01$ und gib die Tangentensteigung $f'(1)$
an.

| Schritt | Zeile |
|---|---|
| aufstellen | $m = \frac{f(1 + h) - f(1)}{h}$ |
| umformen | $m = \frac{2h + h^2 + 2h}{h} = 4 + h$ |
| einsetzen | $m = 5$; $4{,}1$; $4{,}01$ |
| Grenzwert | für $h \to 0$ strebt $m$ gegen $4$ |
| Ergebnis | $f'(1) = 4$ |

## e4 k1 Die Rate als Funktion

Aufgabe: Die Verkaufsrate eines Spiels wird durch $v$ beschrieben ($t$
in Wochen, $v(t)$ in Stück je Woche); es gilt
$v'(t) = (7 - t) \cdot \mathrm{e}^{-0{,}2t}$. Gib an, zu welchem
Zeitpunkt die Verkaufsrate am größten ist.

| Schritt | Zeile |
|---|---|
| Bedingung | $v'(t) = 0$: $(7 - t) \cdot \mathrm{e}^{-0{,}2t} = 0$ |
| Nullprodukt | der e-Faktor ist nie null, also $t = 7$ |
| Vorzeichenwechsel | $v'$ wechselt bei $7$ von plus nach minus |
| Ergebnis | nach $7$ Wochen ist die Verkaufsrate am größten |
