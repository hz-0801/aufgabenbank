# Übersicht: ableitungsregeln

Stand 2026-09-27, Prüfstein (erste Fassung). Quelle: mappen/ableitungsregeln.md
(Merkkasten Katalogzeile 40–81, Typische Fehler 83–91, Typen je Lerneinheit
19–24 für die Fehler-finden-Muster, Erkennungsschritte 35–38) und die Ketten der
Bank (bank/ableitungsregeln/e1–e3.jsonl, Feld kette und sprosse_text). Kein
neuer Stoff: Beispiel- und Fehlerzahlen aus dem Merkkasten und aus „Typische
Fehler“ – nie aus einer Bankzeile. Nicht aufgenommen aus „Typische Fehler“: der
Punkt „Verhalten im Unendlichen“ (gehört laut Mappe zu
grenzwerte-und-verhalten-im-unendlichen.md) und aus „Anschluss an die
Kurvenuntersuchung“ alles außer dem Anstieg über f(0) (Stoff von
kurvenuntersuchung.md).

Jeder `tex`-Block ist Quelltext für mathblatt.sty mit den Bausteinen aus
mappen/_bausteine.md. `regel`, `beispiel` und `schritte` sind drei Fassungen
desselben Kastens einer Einheit; der Zusammenbau setzt eine davon.

## Einheit 1 · Potenz-, Faktor- und Summenregel

### regel

```tex
\uebersichtskasten{Du leitest jeden Summanden einzeln ab: Exponent nach vorn und mit dem Vorfaktor multiplizieren, Exponent um eins kleiner – eine Zahl ohne $x$ fällt weg.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: $f(x) = 2x^5 - 3x^2 + 7$ \rechnung{f'(x) &= 5 \cdot 2x^4 - 2 \cdot 3x + 0 \\ f'(x) &= 10x^4 - 6x \\ f''(x) &= 40x^3 - 6}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Potenz-, Faktor- und Summenregel} \begin{schritte} \schritt Zerleg $f$ in Summanden. \schritt Je Summand: Exponent nach vorn, mit dem Vorfaktor multiplizieren. \schritt Exponent um eins senken. \schritt Zahl ohne $x$ streichen; ein Parameter wie $k$ ist eine Zahl. \schritt Für $f''$ und $f'''$: dieselben Regeln noch einmal auf $f'$. \end{schritte}}
```

## Einheit 2 · Kettenregel

### regel

```tex
\uebersichtskasten{Bei einer Verkettung leitest du die äußere Funktion ab, lässt die innere darin stehen und multiplizierst mit der Ableitung der inneren.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: $f(x) = e^{3x}$ und $g(x) = (2x - 1)^4$ \rechnung{f'(x) &= e^{3x} \cdot 3 = 3 \cdot e^{3x} && \text{innen } 3x \\ g'(x) &= 4 \cdot (2x - 1)^3 \cdot 2 = 8 \cdot (2x - 1)^3 && \text{innen } 2x - 1}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Kettenregel} \begin{schritte} \schritt Bestimm innen und außen: Der Exponent oder die Klammer ist innen. \schritt Leite außen ab und lass innen stehen. \schritt Leite innen ab. \schritt Multipliziere beides, Zahlen nach vorn. \schritt Noch einmal ableiten: Bei $e^{3x}$ kommt der Faktor $3$ wieder dazu, $f''(x) = 9 \cdot e^{3x}$. \end{schritte}}
```

## Einheit 3 · Produktregel

### regel

```tex
\uebersichtskasten{Bei einem Produkt leitest du erst den einen Faktor ab und lässt den anderen stehen, dann umgekehrt, und addierst beides: $(u \cdot v)' = u' \cdot v + u \cdot v'$.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: $f(x) = x \cdot e^{-x}$ mit $u = x$ und $v = e^{-x}$ \rechnung{f'(x) &= 1 \cdot e^{-x} + x \cdot (-1) \cdot e^{-x} \\ f'(x) &= (1 - x) \cdot e^{-x}}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Produktregel} \begin{schritte} \schritt Benenn die Faktoren $u$ und $v$. \schritt Bilde $u'$ und $v'$ – beim e-Faktor mit der Kettenregel. \schritt Setz ein: $u' \cdot v + u \cdot v'$. \schritt Klammer den e-Term aus und fass den Rest zusammen. \schritt Vergleich mit der vorgegebenen Form. \end{schritte}}
```

## Übersicht

### tabelle

```tex
\sachtabelle{lll}{Verfahren & Wann nehme ich es? & Erkennungsmerkmal}{Potenzregel & Summe von $x$-Potenzen & $2x^5 - 3x^2 + 7$ \\ Kettenregel & $x$ steckt in etwas drin & $x$ im Exponenten, in $(\ldots)^n$ \\ Produktregel & zwei Faktoren mit $x$ & $x^2 \cdot e^x$ \\ Produkt- und Kettenregel & Faktor $e^{kx}$ mit $k \ne 1$ & $x \cdot e^{-x}$, $(x^2 + 1) \cdot e^{2x}$ \\ Regel am Graphen & nur Graphen gegeben & $f(x_0)$, $f'(x_0)$ ablesen}
```

### abbildung

```tex
\termbaum{\cdot}{\tb{+}{x^2}{1}}{e^{2x}}
Oberstes Rechenzeichen ist „$\cdot$“ und in beiden Faktoren steht $x$: Produktregel. Im rechten Faktor steckt $2x$ im Exponenten: Kettenregel dazu.
```

## Typische Fehler

### fehler

```tex
\sachtabelle{lll}{Achtung bei & falsch & richtig}{Exponent senken & $2x^5 \to 10x^5$ & $2x^5 \to 10x^4$ \\ Vorfaktor mal Exponent & $\frac{1}{4}x^4 \to \frac{1}{4}x^3$ & $\frac{1}{4} \cdot 4x^3 = x^3$ \\ Konstante & $-3x^2 + 7 \to -6x + 7$ & $-3x^2 + 7 \to -6x$ \\ Parameter & $(1 - ax)' = -ax$ & $(1 - ax)' = -a$ \\ Aufleiten & $2x^5 \to \frac{2}{5}x^5$ & $2x^5 \to \frac{2}{6}x^6 = \frac{1}{3}x^6$ \\ Anstieg & Anstieg in $0$ über $f(0)$ & Anstieg in $0$ über $f'(0)$ \\ innere Ableitung & $e^{-x^2/2} \to e^{-x^2/2}$ & $e^{-x^2/2} \to -x \cdot e^{-x^2/2}$ \\ äußere Ableitung & $(2x - 1)^4 \to 4x^3 \cdot 2$ & $4 \cdot (2x - 1)^3 \cdot 2$ \\ wiederholt ableiten & $2^{100} \cdot e^{2x}$: Streckung & Verschiebung: $2^{100} = e^{2d}$ \\ Produktregel & $x \cdot e^{-x} \to 1 \cdot (-e^{-x})$ & $(1 - x) \cdot e^{-x}$ \\ Produkt am Graphen & $h'(3) = f'(3) \cdot g'(3)$ & $f'(3) \cdot g(3) + f(3) \cdot g'(3)$ \\ vorgegebene Form & $2x \cdot e^{2x} + 2(x^2 + 1) \cdot e^{2x}$ & $2 \cdot (x^2 + x + 1) \cdot e^{2x}$ \\ Tiefpunkt am Graphen & $f'(3)$ am Graphen geschätzt & Tiefpunkt: $f'(3) = 0$}
```
