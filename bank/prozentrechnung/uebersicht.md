# Übersicht: prozentrechnung

Stand 2026-09-27, Prüfstein (erste Fassung). Quelle: mappen/prozentrechnung.md
(Merkkasten Katalogzeile 44–79, Typische Fehler 81–93, Erkennungsschritte
37–42, Originale in Abschnitt 2) und die Ketten der Bank (bank/prozentrechnung/
e1–e5.jsonl, Feld kette und sprosse_text). Kein neuer Stoff: Beispielzahlen aus
dem Merkkasten, Zahlen der Fehlerzeilen aus „Typische Fehler“ und den dort
genannten Originalen – nie aus einer Bankzeile, damit die Übersicht keine
Lösung einer Aufgabe desselben Blatts zeigt.

Jeder `tex`-Block ist Quelltext für mathblatt.sty mit den Bausteinen aus
mappen/_bausteine.md. `regel`, `beispiel` und `schritte` sind drei Fassungen
desselben Kastens einer Einheit; der Zusammenbau setzt eine davon.

## Einheit 1 · Prozente als Anteile

### regel

```tex
\uebersichtskasten{Prozent heißt Hundertstel: Schreib den Anteil als Bruch mit dem Nenner $100$ – der Zähler ist die Prozentzahl.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: \rechnung{\frac{3}{4} &= \frac{75}{100} = 75\,\% \\ 0{,}08 &= \frac{8}{100} = 8\,\% \\ \text{„jeder Fünfte“} &= \frac{1}{5} = \frac{20}{100} = 20\,\%}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Anteil in Prozent} \begin{schritte} \schritt Schreib den Anteil als Bruch („jeder Fünfte“ ist $\frac{1}{5}$). \schritt Erweitere auf den Nenner $100$ – bei einer Dezimalzahl: Komma zwei Stellen nach rechts. \schritt Der Zähler ist die Prozentzahl. \schritt Fehlt ein Anteil, rechne $100\,\%$ minus alle anderen. \end{schritte}}
```

## Einheit 2 · Prozentsatz

### regel

```tex
\uebersichtskasten{Den Prozentsatz bekommst du, wenn du den Teil durch das Ganze teilst und das Ergebnis in Prozent schreibst.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: $14$ von $40$ – wie viel Prozent? \rechnung{14 : 40 &= 0{,}35 \\ 0{,}35 &= 35\,\%}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Prozentsatz} \begin{schritte} \schritt Such das Ganze und unterstreiche es. \schritt Rechne Teil : Ganzes. \schritt Schreib das Ergebnis in Prozent: Komma zwei Stellen nach rechts. \schritt Runde, wenn es verlangt ist, auf eine Stelle. \achtung{Teil durch Ganzes, nicht Teil durch Rest.} \end{schritte}}
```

## Einheit 3 · Prozentwert

### regel

```tex
\uebersichtskasten{Den Prozentwert bekommst du, wenn du erst $1\,\%$ ausrechnest (Ganzes : $100$) und das mal die Prozentzahl nimmst – oder gleich die Prozentzahl als Dezimalzahl mal das Ganze.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: $18\,\%$ von $40$ kg \rechnung{1\,\% &= 40 : 100 = 0{,}4 \text{ kg} \\ 18\,\% &= 18 \cdot 0{,}4 = 7{,}2 \text{ kg} \\ \text{kurz: } 0{,}18 \cdot 40 &= 7{,}2 \text{ kg}}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Prozentwert} \begin{schritte} \schritt Such das Ganze und den Prozentsatz. \schritt Rechne $1\,\%$: Ganzes : $100$. \schritt Nimm das mal die Prozentzahl. \schritt Kurzweg: Prozentzahl als Dezimalzahl mal Ganzes ($18\,\% = 0{,}18$). \schritt Lies die Frage noch einmal: Ersparnis oder neuer Preis? \end{schritte}}
```

## Einheit 4 · Grundwert

### regel

```tex
\uebersichtskasten{Das Ganze bekommst du, wenn du erst $1\,\%$ ausrechnest (Prozentwert : Prozentzahl) und das mal $100$ nimmst.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: $36\,€$ sind $45\,\%$ – wie viel ist das Ganze? \rechnung{1\,\% &= 36 : 45 = 0{,}80\,€ \\ 100\,\% &= 100 \cdot 0{,}80 = 80\,€}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Grundwert} \begin{schritte} \schritt Ordne zu: Was ist gegeben, was gesucht? Gesucht ist das Ganze. \schritt Rechne $1\,\%$: Prozentwert : Prozentzahl. \schritt Nimm das mal $100$. \schritt Prüfe: Das Ganze ist größer als der Teil. \end{schritte}}
```

## Einheit 5 · Veränderung

### regel

```tex
\uebersichtskasten{Der alte Wert ist immer $100\,\%$: Für den neuen Wert nimmst du ihn mal $1{,}\ldots$ (mehr) oder mal $0{,}\ldots$ (weniger), und die Veränderung in Prozent ist der Unterschied geteilt durch den alten Wert.}
```

### beispiel

```tex
\uebersichtskasten{Beispiel: $250\,€$ um $12\,\%$ erhöht; von $60$ auf $69$ – um wie viel Prozent? \rechnung{250 \cdot 1{,}12 &= 280\,€ \\ (69 - 60) : 60 &= 9 : 60 = 0{,}15 = 15\,\%}}
```

### schritte

```tex
\uebersichtskasten{\textbf{Veränderung} \begin{schritte} \schritt Markiere den alten Wert – er ist $100\,\%$. \schritt „um“ oder „auf“? Um $12\,\%$ mehr: mal $1{,}12$; um $12\,\%$ weniger: mal $0{,}88$; auf $70\,\%$: mal $0{,}7$. \schritt Neuer Wert: alter Wert mal Faktor. \schritt Veränderung in Prozent: (neu $-$ alt) : alt. \schritt Alter Wert gesucht: neuer Wert : Faktor. \end{schritte}}
```

## Übersicht

### tabelle

```tex
\sachtabelle{lll}{Verfahren & Wann nehme ich es? & Erkennungsmerkmal}{Umwandeln & Anteil als Prozent schreiben & Bruch, Dezimalzahl, „jeder Fünfte“ \\ Prozentsatz & Teil und Ganzes gegeben & „Wie viel Prozent …?“ \\ Prozentwert & Ganzes und Prozentsatz gegeben & „$18\,\%$ von $40$ kg“ \\ Grundwert & Teil und Prozentsatz gegeben & „$36\,€$ sind $45\,\%$“ \\ neuer Wert & alter Wert und Prozentsatz & „um … erhöht“, „auf … gesenkt“ \\ Veränderung in \% & alter und neuer Wert & „um wie viel Prozent?“ \\ alter Wert & neuer Wert und Prozentsatz & „vorher“, „ohne Steuer“}
```

### abbildung

```tex
\streifenwertreihe{a/35/14/40, b/18/7{,}2\,kg/40\,kg, c/45/36\,€/80\,€}
a) Prozentsatz: $14$ von $40$ sind $35\,\%$. \quad b) Prozentwert: $18\,\%$ von $40$ kg sind $7{,}2$ kg. \\ c) Grundwert: $36\,€$ sind $45\,\%$, das Ganze sind $80\,€$.
```

## Typische Fehler

### fehler

```tex
\sachtabelle{lll}{Achtung bei & falsch & richtig}{Teil und Ganzes & $1{,}25$ von $7{,}8$: $7{,}8 : 1{,}25$ & $1{,}25 : 7{,}8 \approx 16{,}0\,\%$ \\ Prozent als Dezimalzahl & $30\,\%$ von $70\,€$: $0{,}03 \cdot 70$ & $0{,}3 \cdot 70 = 21\,€$ \\ Ganzes gesucht & $25\,\%$ sind $200\,€$: $0{,}25 \cdot 200$ & $200 \cdot 4 = 800\,€$ \\ Ersparnis oder Preis & $20\,\%$ Rabatt auf $550\,€$: $440\,€$ & Ersparnis $550 \cdot 0{,}2 = 110\,€$ \\ Nenner als Prozent & „jeder Fünfte“ $= 5\,\%$ & $\frac{1}{5} = \frac{20}{100} = 20\,\%$ \\ alter Wert ist $100\,\%$ & $470$ auf $400$: $70 : 400$ & $70 : 470 \approx 14{,}9\,\%$ \\ Prozentpunkte & $72\,\%$ auf $95\,\%$ von $1\,200$: $23$ & $0{,}23 \cdot 1\,200 = 276$ \\ Teil zu Rest & $2$ mit Senf, $14$ ohne: $2 : 14$ & $2 : 16 = 12{,}5\,\%$ \\ „um“ und „auf“ & „auf $70\,\%$ gesenkt“: $70\,\%$ Rabatt & $30\,\%$ Rabatt \\ Brutto und Netto & Brutto $- 19\,\%$ vom Brutto & Brutto $: 1{,}19$ \\ Steigung & Höhe : Rampenlänge & $16 : 170 \approx 9{,}4\,\%$ (waagerecht) \\ Prozentzeichen & $35\,\%$ von $40$: $35 \cdot 40$ & $0{,}35 \cdot 40 = 14$}
```
