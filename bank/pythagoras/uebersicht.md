# Übersicht: pythagoras

Stand 2026-09-27, Prüfstein (erste Fassung). Quelle: mappen/pythagoras.md
(Merkkasten Katalogzeile 42–67, Typische Fehler 69–83, Erkennungsschritte
34–40, Originale in Abschnitt 2) und die Ketten der Bank (bank/pythagoras/
e1–e3.jsonl, Feld kette und sprosse_text). Kein neuer Stoff: Beispielzahlen aus
dem Merkkasten, Zahlen der Fehlerzeilen aus „Typische Fehler“ und den dort
genannten Originalen, sonst aus dem Merkkasten – nie aus einer Bankzeile.

Jeder `tex`-Block ist Quelltext für mathblatt.sty mit den Bausteinen aus
mappen/_bausteine.md. `regel`, `beispiel` und `schritte` sind drei Fassungen
desselben Kastens einer Einheit; der Zusammenbau setzt eine davon.

## Einheit 1 · Satz und Hypotenuse

### regel

```tex
\uebersichtskasten{Die längste Seite im rechtwinkligen Dreieck (Hypotenuse, gegenüber dem rechten Winkel) bekommst du, wenn du die beiden anderen Seiten hoch zwei nimmst, addierst und dann die Wurzel ziehst.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: Katheten $a = 6$ cm, $b = 8$ cm \rechnung{c^2 &= 6^2 + 8^2 \\ c^2 &= 36 + 64 = 100 \\ c &= \sqrt{100} = 10 \text{ cm}}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Hypotenuse} \begin{schritte} \schritt Such den rechten Winkel; die Seite gegenüber ist die Hypotenuse. \schritt Schreib die Gleichung: Kathete$^2$ + Kathete$^2$ = Hypotenuse$^2$ – mit den Buchstaben der Skizze. \schritt Setz ein und rechne das Zwischenergebnis $c^2$ aus. \schritt Zieh die Wurzel; geht sie nicht auf, runde auf eine Stelle. \schritt Schreib die Einheit dazu – cm und m vorher angleichen. \end{schritte}}
```

## Einheit 2 · Kathete und Umkehrung

### regel

```tex
\uebersichtskasten{Suchst du eine kurze Seite (Kathete), ziehst du vom Quadrat der Hypotenuse das Quadrat der bekannten Kathete ab und dann die Wurzel – und ergeben bei drei Seiten die zwei kurzen hoch zwei zusammen die lange hoch zwei, ist das Dreieck rechtwinklig.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: Hypotenuse $c = 13$ cm, Kathete $b = 5$ cm; Seiten $9$ cm, $12$ cm, $15$ cm \rechnung{a^2 &= 13^2 - 5^2 = 169 - 25 = 144 \\ a &= \sqrt{144} = 12 \text{ cm} \\ 9^2 + 12^2 &= 81 + 144 = 225 = 15^2 && \Rightarrow \text{rechtwinklig}}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Kathete und Umkehrung} \begin{schritte} \schritt Lange oder kurze Seite gesucht? Kathete gesucht heißt minus. \schritt Stell um: $a^2 = c^2 - b^2$. \schritt Rechne $a^2$ aus, dann die Wurzel. \schritt Prüfe: Die Kathete ist kürzer als die Hypotenuse. \schritt Umkehrung: längste Seite als $c$; ist $a^2 + b^2 = c^2$, ist das Dreieck rechtwinklig. \end{schritte}}
```

## Einheit 3 · Figuren und Körper

### regel

```tex
\uebersichtskasten{Such in der Figur oder im Körper das rechtwinklige Dreieck, fahr es nach und rechne darin mit Pythagoras – oft ist eine Seite nur die halbe Seite, die halbe Diagonale oder der Radius.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: gleichschenkliges Dreieck, Grundseite $16$ cm, Schenkel $17$ cm – Höhe $h$? \rechnung{\text{halbe Grundseite} &= 8 \text{ cm} \\ h^2 &= 17^2 - 8^2 = 289 - 64 = 225 \\ h &= \sqrt{225} = 15 \text{ cm}}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Teildreieck} \begin{schritte} \schritt Fahr das rechtwinklige Teildreieck farbig nach. \schritt Benenn seine Seiten neu: Hypotenuse gegenüber dem rechten Winkel. \schritt Ganz oder halb? Trag halbe Seite, halbe Diagonale oder Radius ein. \schritt Rechne mit plus (Hypotenuse gesucht) oder minus (Kathete gesucht). \schritt Addiere Teilstrecke oder Überstand, wenn die Aufgabe sie hat. \end{schritte}}
```

## Übersicht

### tabelle

```tex
\sachtabelle{lll}{Verfahren & Wann nehme ich es? & Erkennungsmerkmal}{Hypotenuse & beide Katheten bekannt & längste Seite gesucht: plus \\ Kathete & Hypotenuse und Kathete bekannt & kurze Seite gesucht: minus \\ Umkehrung & drei Seiten bekannt & „Ist das Dreieck rechtwinklig?“ \\ Teildreieck & Figur mit Höhe oder Diagonale & Höhe, Schenkel, Seite gesucht \\ Koordinaten & zwei Punkte gegeben & Länge der Strecke gesucht \\ Körper & Kegel, Pyramide, Quader & Mantellinie, Höhe, Diagonale}
```

### abbildung

```tex
\dreieckrw{4}{3}{$a$ Kathete}{$b$ Kathete}{$c$ Hypotenuse}
```

```tex
\kegel{1.5}{3}{$r$}{$h$}{$s$}
Im Kegel bilden Radius $r$, Höhe $h$ und Mantellinie $s$ ein rechtwinkliges Dreieck; $s$ ist die Hypotenuse: $s^2 = r^2 + h^2$.
```

## Typische Fehler

### fehler

```tex
\sachtabelle{lll}{Achtung bei & falsch & richtig}{Kathete gesucht & $BC^2 = 9^2 + 4^2$, $9{,}85$ m & $BC^2 = 9^2 - 4^2$, $BC \approx 8{,}06$ m \\ Hypotenuse finden & $\sqrt{34^2 - 12^2} \approx 31{,}8$ m & $\sqrt{34^2 + 12^2} \approx 36{,}1$ m \\ Wurzel vergessen & $z = x^2 + y^2$ & $z = \sqrt{x^2 + y^2}$ \\ Längen addiert & $c = 6 + 8 = 14$ cm & $c^2 = 6^2 + 8^2$, $c = 10$ cm \\ Wurzel aus Summe & $\sqrt{6^2 + 8^2} = 6 + 8$ & $\sqrt{6^2 + 8^2} = \sqrt{100} = 10$ \\ Becher: Durchmesser & Radius $3{,}2$ cm als Kathete & Durchmesser $6{,}4$ cm \\ ganz oder halb & $h^2 = 17^2 - 16^2$ & $h^2 = 17^2 - 8^2$, $h = 15$ cm \\ Schräge als Höhe & $r = 20$, $s = 29$: $h = 29$ cm & $h^2 = 29^2 - 20^2$, $h = 21$ cm \\ Überstand & Turmhöhe = Kegelhöhe & Zylinderhöhe + Kegelhöhe \\ kein rechter Winkel & Satz im stumpfen Dreieck & erst Höhe, dann Teildreieck \\ Koordinaten & $0 - (-2) = -2$ & $0 - (-2) = 2$ \\ Umkehrung & $9$, $12$, $15$ mit $c = 12$: nein & $c = 15$: $81 + 144 = 225$, ja \\ zu früh gerundet & $c^2$ runden, weiterrechnen & erst am Ende runden \\ Buchstaben & Hypotenuse $x$: $z^2 = x^2 + y^2$ & $z^2 = x^2 - y^2$}
```
