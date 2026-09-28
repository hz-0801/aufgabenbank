# Sprachlauf pyramide-kegel-kugel

Stand 2026-09-28 (Sprachlauf Gruppe 3). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 73c3d55. Nur das Feld aufgabe ist geändert;
`python3 werkzeuge/bank-pruef.py pyramide-kegel-kugel`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 76 | 1 | 77 |
| e2.jsonl | 61 | 2 | 63 |
| e3.jsonl | 53 | 5 | 58 |
| zone.jsonl | 48 | 0 | 48 |
| gesamt | 238 | 8 | 246 |

Geänderte Sprossen: 99. Die 10 Beispiele sind je Sprosse die erste
geänderte Zeile, gleichmäßig über die Sprossen verteilt (Zone zuerst).

## 10 Beispiele vorher/nachher

1. `pyramide-kegel-kugel-zone-f1-v1` – Flächeninhalt von Quadrat, Rechteck, Dreieck (Seitenflächen)

   vorher: Quadrat mit der Seite $7$ cm – Flächeninhalt?

   nachher: Ein Quadrat hat die Seitenlänge $7$ cm. Berechne seinen Flächeninhalt.

2. `pyramide-kegel-kugel-zone-f4-v1` – Quadrieren und hoch drei, Wurzel und Kubikwurzel mit dem Tas

   vorher: $3^3$ – wie viel?

   nachher: Berechne. $3^3$

3. `pyramide-kegel-kugel-zone-f6-v4` – Formel aus der Formelsammlung entnehmen und nach einer Größe

   vorher: Dreieck: $A = \frac{1}{2} \cdot g \cdot h$ mit $A = 18$ cm² und der Grundseite $g = 4{,}5$ cm. Wie groß ist die Höhe $h$?

   nachher: Für ein Dreieck gilt $A = \frac{1}{2} \cdot g \cdot h$. Der Flächeninhalt ist $A = 18$ cm². Die Grundseite ist $g = 4{,}5$ cm lang. Wie lang ist die Höhe $h$?

4. `pyramide-kegel-kugel-zone-f8-v6` – Volumeneinheiten cm³ → dm³ = l mit 1000, m³; Masse aus Volum

   vorher: Ein Aluminiumteil wiegt $540$ g, Aluminium hat die Dichte $2{,}7$ g/cm³. Welches Volumen hat das Teil?

   nachher: Ein Teil aus Aluminium wiegt $540$ g. Aluminium hat die Dichte $2{,}7$ g/cm³. Wie groß ist das Volumen des Teils?

5. `pyramide-kegel-kugel-e1-k5-s1-v1` – V aus gegebener Grundfläche und Höhe mit ganzen Zahlen

   vorher: Pyramide: Grundfläche $27$ cm², Höhe $8$ cm – Volumen?

   nachher: Eine Pyramide hat die Grundfläche $27$ cm² und die Höhe $8$ cm. Berechne ihr Volumen.

6. `pyramide-kegel-kugel-e1-k5-s11-v1` – Schrägbild zeichnen und Höhe einzeichnen

   vorher: Zeichne das Schrägbild einer quadratischen Pyramide mit Grundkante $4$ cm und Höhe $5$ cm (Tiefe halb so lang, schräg unter 45°). Zeichne die Höhe gestrichelt ein und beschrifte sie.

   nachher: Eine Pyramide hat ein Quadrat als Grundfläche. Die Grundkante ist $4$ cm lang, die Höhe ist $5$ cm. Zeichne ihr Schrägbild. Zeichne die Kanten nach hinten halb so lang und schräg unter 45° ein. Zeichne die Höhe gestrichelt ein und beschrifte sie.

7. `pyramide-kegel-kugel-e2-k2-s2-v1` – aus d

   vorher: Kegel: Durchmesser $8$ cm, Höhe $9$ cm – Volumen? Runde auf eine Stelle.

   nachher: Der Grundkreis eines Kegels hat den Durchmesser $8$ cm. Der Kegel ist $9$ cm hoch. Berechne sein Volumen. Runde auf eine Stelle nach dem Komma.

8. `pyramide-kegel-kugel-e2-k2-s13-v2` – Kegel gegen Zylinder mit gleichem r und h: ein Drittel, begr

   vorher: Ein kegelförmiges und ein zylinderförmiges Messglas haben innen beide den Radius $4$ cm und die Höhe $7$ cm. Berechne beide Volumen. Wie oft musst du das Kegelglas füllen, bis das Zylinderglas voll ist?

   nachher: Ein Messglas hat innen die Form eines Kegels. Ein zweites Messglas hat innen die Form eines Zylinders. Beide haben den Radius $4$ cm und die Höhe $7$ cm. Berechne beide Volumen. Wie oft musst du das Kegelglas füllen, bis das Zylinderglas voll ist?

9. `pyramide-kegel-kugel-e3-k1-s6-v1` – Kugel skizzieren (Kreis mit Äquatorellipse, Radius gestriche

   vorher: Skizziere eine Kugel mit dem Radius $2$ cm: Kreis, Äquator als Ellipse, Radius gestrichelt und beschriftet.

   nachher: Skizziere eine Kugel mit dem Radius $2$ cm. Zeichne einen Kreis und den Äquator als flache Ellipse. Zeichne den Radius gestrichelt ein und beschrifte ihn.

10. `pyramide-kegel-kugel-e3-k2-s4-v1` – Sachaufgabe (Silo oder Turm mit Halbkugeldach, Eiskugel in d

   vorher: Die Kuppel eines Turms ist eine Halbkugel mit dem Radius $2{,}8$ m. Sie wird außen zweimal gestrichen; ein Eimer Farbe reicht für $15$ m². Wie viele Eimer braucht man?

   nachher: Die Kuppel eines Turms ist eine Halbkugel mit dem Radius $2{,}8$ m. Die Kuppel wird außen zweimal gestrichen. Ein Eimer Farbe reicht für $15$ m². Wie viele Eimer Farbe braucht man?

## Fälle, in denen die Regeln nicht reichten

1. „quadratische Pyramide“ (e1, rund 40 Zeilen): Fachwort, das die Sprossen
   nicht selbst üben, aber in fast jeder Pyramidenzeile stand. Entschieden:
   einheitlich „Eine Pyramide hat ein Quadrat als Grundfläche.“ bzw. „… mit
   einem Quadrat als Grundfläche“; „Grundkante“, „Seitenhöhe“, „Mantel“,
   „Mantellinie“ bleiben (Sprossenwörter).
2. e1-k1-s0-v3 (Globus, „Färbe die Grundfläche“): Die Kugel hat laut loesung
   keine Grundfläche; ein Zusatz „wenn es eine gibt“ hätte die Lösung
   verraten. Entschieden: gleicher Satzbau wie die anderen Varianten
   („Färbe dann die Grundfläche.“), Falle bleibt.
3. e2-k2-s14-v1/v2 (Original 2026-FOR-K2d): Die Behauptung in wörtlicher Rede
   bleibt ein langer Wenn-Satz (über 12 Wörter), weil sie als Aussage zu
   prüfen ist und dem Original folgt; nur die Aufforderung ist zu „Prüfe mit
   einer Rechnung, ob … recht hat“ vereinheitlicht. Ebenso e1-k6-s1-v3: die
   Division „30 \cdot 8 : 2“ in der Fehlerrechnung ist nach Regel 4 als
   Bruch \frac{30 \cdot 8}{2} gesetzt.
