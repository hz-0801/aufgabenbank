# Musterbeispiele: ableitungsregeln

Je Verfahrenskette ein vorgerechnetes Beispiel am Grundfall, mit
eigenen Zahlen (nicht aus dem Päckchen). Reine Daten; die Form auf
dem Blatt setzt der Zusammenbau (layout-befunde 55).

## e1 k2 Potenz-, Faktor- und Summenregel

Aufgabe: $f(x) = 4x^3 + 5x^2 - 3x + 1$ – $f'(x)$?

| Schritt | Zeile |
|---|---|
| Summanden einzeln ableiten | $f'(x) = 3 \cdot 4x^2 + 2 \cdot 5x - 3 + 0$ |
| Konstante fällt weg | $1$ wird $0$ |
| zusammenfassen | $f'(x) = 12x^2 + 10x - 3$ |
| Ergebnis | $f'(x) = 12x^2 + 10x - 3$ |

## e2 k1 Kettenregel

Aufgabe: $f(x) = e^{-8x}$ – $f'(x)$?

| Schritt | Zeile |
|---|---|
| innere Funktion | $v(x) = -8x$ |
| äußere Funktion | $u(z) = e^z$ |
| innere Ableitung | $v'(x) = -8$ |
| äußere Ableitung | $u'(z) = e^z$ |
| zusammensetzen | $f'(x) = u'(v(x)) \cdot v'(x) = e^{-8x} \cdot (-8)$ |
| Ergebnis | $f'(x) = -8 \cdot e^{-8x}$ |

## e3 k1 Produktregel

Aufgabe: $f(x) = 5x^2 \cdot e^x$ – $f'(x)$, $e^x$ ausgeklammert?

| Schritt | Zeile |
|---|---|
| Faktoren ableiten | $u(x) = 5x^2$, $u'(x) = 10x$; $v(x) = e^x$, $v'(x) = e^x$ |
| Produktregel | $f'(x) = 10x \cdot e^x + 5x^2 \cdot e^x$ |
| $e^x$ ausklammern | $f'(x) = (5x^2 + 10x) \cdot e^x$ |
| Ergebnis | $f'(x) = (5x^2 + 10x) \cdot e^x$ |
