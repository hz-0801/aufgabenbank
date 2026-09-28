# Sprachlauf pythagoras

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Vergleich gegen den Bankstand 405a7c4. Nur das Feld aufgabe ist geändert (Skriptprobe: alle anderen Felder gleich, keine Zahl verloren, keine neue Zahl). `python3 werkzeuge/bank-pruef.py pythagoras`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 65 | 0 | 65 |
| e2.jsonl | 53 | 5 | 58 |
| e3.jsonl | 72 | 3 | 75 |
| zone.jsonl | 38 | 0 | 38 |
| gesamt | 228 | 8 | 236 |

## 10 Beispiele

1. `pythagoras-e1-k1-s0-v1` – Gilt der Satz hier?

   vorher: Gilt der Satz des Pythagoras? \janein

   nachher: Gilt für das Dreieck in der Figur der Satz des Pythagoras? \janein

2. `pythagoras-e2-k1-s0-v1` – Welche Seite ist die längste?

   vorher: Welche Seite kann die Hypotenuse sein? \\ \kreuz{$4$ cm} \\ \kreuz{$8{,}5$ cm} \\ \kreuz{$7{,}5$ cm}

   nachher: Ein rechtwinkliges Dreieck hat diese drei Seiten. Kreuze an, welche Seite die Hypotenuse sein kann. \\ \kreuz{$4$ cm} \\ \kreuz{$8{,}5$ cm} \\ \kreuz{$7{,}5$ cm}

3. `pythagoras-e3-k1-s0-v1` – Ganz oder halb?

   vorher: Kegel mit Durchmesser $18$ cm – welche Länge gehört ins Teildreieck aus Höhe, Radius und Mantellinie? \\ \kreuz{$18$ cm} \\ \kreuz{$9$ cm}

   nachher: Die Figur zeigt einen Kegel. Sein Durchmesser ist $18$ cm lang. Höhe, Radius und Mantellinie bilden ein rechtwinkliges Dreieck. Kreuze an, welche Länge in dieses Dreieck gehört. \\ \kreuz{$18$ cm} \\ \kreuz{$9$ cm}

4. `pythagoras-zone-f1-v1` – Quadrieren mit dem Taschenrechner, auch Dezimalzahlen; Quadratzahlen b

   vorher: $11^2$ – wie viel?

   nachher: Berechne $11^2$.

5. `pythagoras-e1-k2-s7-v1` – Satz in Worten unter drei Aussagen ankreuzen

   vorher: Welche Aussage gilt im rechtwinkligen Dreieck? \\ \kreuz{Die Hypotenuse ist die kürzeste Seite.} \\ \kreuz{Das Quadrat über der Hypotenuse ist so groß wie die zwei Quadrate über den Katheten zusammen.} \\ \kreuz{Die zwei Katheten sind zusammen so lang wie die Hypotenuse.}

   nachher: Kreuze an, welche Aussage im rechtwinkligen Dreieck gilt. \\ \kreuz{Die Hypotenuse ist die kürzeste Seite.} \\ \kreuz{Das Quadrat über der Hypotenuse ist so groß wie die zwei Quadrate über den Katheten zusammen.} \\ \kreuz{Die zwei Katheten sind zusammen so lang wie die Hypotenuse.}

6. `pythagoras-e2-k2-s8-v1` – Umkehrung: drei Seiten, längste als c, a² + b² mit c² vergleichen, Ent

   vorher: Seiten $33$ cm, $56$ cm, $65$ cm – rechtwinklig?

   nachher: Ein Dreieck hat die Seiten $33$ cm, $56$ cm und $65$ cm. Prüfe mit einer Rechnung, ob das Dreieck rechtwinklig ist.

7. `pythagoras-e3-k2-s7-v1` – Strecke aus Koordinaten mit positiven Koordinaten

   vorher: $P(1 | 1)$ und $Q(4 | 5)$ – Länge der Strecke PQ?

   nachher: Gegeben sind die Punkte $P(1 | 1)$ und $Q(4 | 5)$. Berechne die Länge der Strecke PQ.

8. `pythagoras-zone-f9-v1` – Strecke halbieren, halbe Differenz zweier Seiten bilden (Überstand am 

   vorher: $18$ cm – die Hälfte?

   nachher: Berechne die Hälfte von $18$ cm.

9. `pythagoras-e1-k4-s1-v1` – Ergebnis mit sinnvoller Genauigkeit angeben

   vorher: Katheten $2{,}3$ m und $3{,}1$ m – Hypotenuse $c$, sinnvoll gerundet?

   nachher: Die Katheten eines rechtwinkligen Dreiecks sind $2{,}3$ m und $3{,}1$ m lang. Berechne die Länge der Hypotenuse $c$. Runde das Ergebnis sinnvoll.

10. `pythagoras-e2-k4-s3-v1` – Kathete im Sachzusammenhang (Höhenunterschied der Seilbahn, Abstand au

   vorher: Eine Drehleiter der Feuerwehr ist $30$ m lang ausgefahren. Ihr unteres Ende sitzt $3$ m über dem Boden, $14$ m waagerecht vom Haus entfernt. Reicht sie bis zu einem Fenster in $28$ m Höhe?

   nachher: Eine Drehleiter der Feuerwehr ist $30$ m lang ausgefahren. Ihr unteres Ende ist $3$ m über dem Boden. Es ist waagerecht $14$ m vom Haus entfernt. Ein Fenster liegt in $28$ m Höhe. Reicht die Leiter bis zu diesem Fenster?

## Wo die Regeln nicht reichten

# Wo die Regeln nicht reichten (pythagoras)

- pythagoras-e2-k2-s0-v1 bis -v4: Der Stamm „… gesucht ist die Höhe an der Wand. Plus oder minus?“ ist Stichwortsprache, aber die Kreuzfelder enthalten selbst einen Gedankenstrich („\kreuz{Hypotenuse gesucht – plus}“). Bausteine dürfen inhaltlich nicht geändert werden, apply.py lehnt jeden Text mit „ – “ ab. Entscheidung: die vier Zeilen unverändert gelassen. Vorschlag für den Auftraggeber: Kreuzfelder auf „Hypotenuse gesucht, also plus“ ändern (loesung mitziehen), dann Stamm umschreiben.
- „auf eine Dezimale“ (24 Zeilen, auch die Originale 2020-OS-K7a, 2024-OS-K6a, 2025-OS-K4a, 2026-FOR-K2c, 2022-OS-K2c, 2019-OS-K2d): nicht ausdrücklich geregelt. Entscheidung: einheitlich als eigener Satz „Runde auf eine Stelle nach dem Komma.“ nach Regel 2; die Prüfkennung steht danach am Textende wie im Muster prozentrechnung.
- Darstellung nennen (Regel 5) bei Sachskizzen ohne eigenen Inhalt (z. B. e1-k2-s10, e1-k2-s11, e2-k2-s7, e3-k3-s1): Ein Satz wie „Die Skizze zeigt das Dreieck aus Wand, Boden und Leiter“ wäre schon eine Lösungshilfe. Entscheidung: neutral „Die Skizze zeigt die Lage.“; bei Körpern und Figuren „Die Figur zeigt …“ mit dem Namen des Körpers.
- e3-k2-s7-v3, e3-k2-s8-v2 (Strecke aus Koordinaten, Lösung ≈ 6,7 bzw. ≈ 8,1) und e1-k4-s1 („sinnvoll gerundet“): Die Aufgaben nennen keine Rundung, die Lösungen sind gerundet. Entscheidung: keine Rundungsvorgabe ergänzt (wäre neue Information); bei e1-k4-s1 „Runde das Ergebnis sinnvoll.“, weil das die Sprosse ist.
- e3-k4-s4-v3 („Stützdreieck“) und e3-k1-s0 („Teildreieck aus Höhe und Seitenhöhe“): Fachwort ohne Einführung. Entscheidung: umschrieben als „rechtwinkliges Dreieck aus Höhe und Seitenhöhe“, ohne die halbe Grundkante zu nennen, damit die Aufgabe nicht leichter wird.
