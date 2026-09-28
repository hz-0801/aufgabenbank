# Sprachlauf trigonometrie

Stand 2026-09-28 (Sprachlauf Gruppe 3). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 2384be4. Nur das Feld aufgabe ist geändert;
`python3 werkzeuge/bank-pruef.py trigonometrie`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 91 | 0 | 91 |
| e2.jsonl | 63 | 0 | 63 |
| e3.jsonl | 78 | 0 | 78 |
| e4.jsonl | 72 | 0 | 72 |
| zone.jsonl | 36 | 2 | 38 |
| gesamt | 340 | 2 | 342 |

Geänderte Sprossen: 112. Die 10 Beispiele sind je Sprosse die erste
geänderte Zeile, gleichmäßig über die Sprossen verteilt (Zone zuerst).

## 10 Beispiele vorher/nachher

1. `trigonometrie-zone-f1-v1` – Rechtwinkliges Dreieck erkennen, Rechtwinkelmarke (Bogen mit

   vorher: Das Dreieck hat bei $C$ einen rechten Winkel. Welche Seite ist die Hypotenuse?

   nachher: Die Figur zeigt ein Dreieck. Es hat bei $C$ einen rechten Winkel. Welche Seite ist die Hypotenuse?

2. `trigonometrie-zone-f4-v6` – Gleichung mit einem Bruch nach einer Größe umstellen, Größe

   vorher: $\frac{9}{x} = 0{,}6$ – wie groß ist $x$?

   nachher: Löse die Gleichung. $\frac{9}{x} = 0{,}6$

3. `trigonometrie-zone-f9-v1` – Höhe, Diagonale, Überstand am Trapez, Fußpunkt auf der Verlä

   vorher: Gleichschenkliges Trapez: untere Seite $10$ cm, obere Seite $6$ cm. Wie lang ist ein Überstand?

   nachher: Ein gleichschenkliges Trapez hat unten eine Seite von $10$ cm. Die obere Seite ist $6$ cm lang. Die untere Seite steht links und rechts gleich weit über. Wie lang ist ein Überstand?

4. `trigonometrie-e1-k3-s7-v1` – Hypotenuse gesucht: geteilt durch den Sinus

   vorher: Gegenkathete $6$ cm, $\alpha = 44^\circ$ – wie lang ist die Hypotenuse $x$?

   nachher: Ein rechtwinkliges Dreieck hat den Winkel $\alpha = 44^\circ$. Die Gegenkathete von $\alpha$ ist $6$ cm lang. Wie lang ist die Hypotenuse $x$?

5. `trigonometrie-e1-k6-s1-v1` – Ergebnis prüfen: Kathete kürzer als Hypotenuse

   vorher: Lea rechnet zur Hypotenuse $6$ cm eine Gegenkathete von $7{,}3$ cm aus. Kann das stimmen?

   nachher: Die Hypotenuse eines rechtwinkligen Dreiecks ist $6$ cm lang. Lea berechnet die Gegenkathete und erhält $7{,}3$ cm. Begründe, ob das stimmen kann.

6. `trigonometrie-e2-k1-s9-v1` – Winkel im Teildreieck mit gezeichneter Höhe

   vorher: Im Dreieck $ABC$ ist die Höhe von $C$ auf $AB$ $4{,}5$ cm lang, $AC = 7{,}2$ cm. Wie groß ist $\alpha$ bei $A$?

   nachher: Im Dreieck $ABC$ geht die Höhe von $C$ auf die Seite $AB$. Sie ist $4{,}5$ cm lang. Die Seite $AC$ ist $7{,}2$ cm lang. Wie groß ist der Winkel $\alpha$ bei $A$?

7. `trigonometrie-e3-k1-s4-v1` – rechtwinkliges Trapez: Hilfsdreieck mit der Differenz der Hö

   vorher: Rechtwinkliges Trapez: die senkrechten Seiten sind $9$ cm und $4$ cm lang und stehen $8$ cm auseinander. Wie groß ist der Winkel $\alpha$ zwischen der schrägen Seite und der Waagerechten?

   nachher: Ein rechtwinkliges Trapez hat zwei senkrechte Seiten. Sie sind $9$ cm und $4$ cm lang. Sie stehen $8$ cm auseinander. Wie groß ist der Winkel $\alpha$ zwischen der schrägen Seite und der Waagerechten?

8. `trigonometrie-e3-k1-s16-v1` – Stützdreieck in Pyramide oder Kegel mit Neigungswinkel, Seit

   vorher: Quadratische Pyramide: Grundkante $6$ m, die Seitenflächen sind um $57^\circ$ gegen die Grundfläche geneigt. Wie lang ist die Seitenhöhe $h_s$?

   nachher: Eine Pyramide hat eine quadratische Grundfläche mit $6$ m langen Kanten. Die Seitenflächen sind um $57^\circ$ gegen die Grundfläche geneigt. Wie lang ist die Seitenhöhe $h_s$?

9. `trigonometrie-e4-k1-s7-v1` – Nachweis mit vorgegebenem Ergebnis

   vorher: Dreieck $ABC$: $a = 9$ cm, $\alpha = 77^\circ$, $\beta = 44^\circ$. Zeige rechnerisch, dass $b \approx 6{,}4$ cm ist.

   nachher: Im Dreieck $ABC$ ist $a = 9$ cm, $\alpha = 77^\circ$ und $\beta = 44^\circ$. Zeige mit einer Rechnung, dass $b \approx 6{,}4$ cm ist.

10. `trigonometrie-e4-k2-s3-v1` – nach der Seite umstellen und mit dem Taschenrechner berechne

   vorher: Über einen Fluss soll ein Seil von $A$ zu einem Baum $C$ am anderen Ufer gespannt werden. Am eigenen Ufer ist $AB = 80$ m abgesteckt, der Winkel bei $A$ ist $72^\circ$, der bei $B$ $63^\circ$. Reicht eine $100$ m lange Seilrolle?

   nachher: Über einen Fluss soll ein Seil gespannt werden. Es soll von $A$ bis zu einem Baum $C$ am anderen Ufer reichen. Am eigenen Ufer ist die Strecke $AB = 80$ m abgesteckt. Der Winkel bei $A$ ist $72^\circ$ groß, der Winkel bei $B$ ist $63^\circ$ groß. Reicht eine Seilrolle mit $100$ m Seil?

## Fälle, in denen die Regeln nicht reichten

1. e1-k3-s1-v1…v5, e1-k3-s16-v11/v12 („Rechter Winkel bei C. Trage den
   Bruch ein.“): Die Aufgabe nannte die Funktion nicht, die loesung
   verlangt aber genau eine (z. B. sin β = e/f). Entscheidung: die
   Funktion aus der loesung in den Auftrag geschrieben, gleicher Satzbau
   wie die Tangens-Zeilen s16-v13/v14: „Die Figur zeigt ein Dreieck mit
   rechtem Winkel bei $C$. Schreibe $\mathrm{sin}\,\beta$ als Bruch aus
   zwei Seiten.“ Das Verlangte ist damit erst eindeutig; keine neue Zahl.
2. Gleichungen ohne Sachlage (zone-f4, e1-k3-s12, e1-k3-s16-v9/v10,
   vorher „… – wie groß ist $x$?“): Die loesung steht nicht als
   Lösungsmenge da, also nach Regel „Löse die Gleichung. $…$“; die
   Prüfkennung steht bei s16-v9/v10 hinter dem Term.
3. Fehler-finden mit Sinussatz (e4-k2-s1-v1/v2): Die Division in der
   \rechnung stand als „:“; nach Regel 4 als \frac umgeschrieben. Die
   loesung derselben Zeilen (und fast alle loesung-Felder des Eintrags)
   schreiben weiter „8 · sin 43° : sin 71°“ – aufgabe und loesung sind
   dort jetzt uneinheitlich; loesung durfte nicht angefasst werden.
   Ebenfalls offen: Ankreuz-Optionen mit Stichwort-Doppelpunkt
   („Seite: Gleichung umstellen“, „im Zähler: mal“) mussten wörtlich
   bleiben.
