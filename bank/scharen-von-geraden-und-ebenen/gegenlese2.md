# Zweitlesung scharen-von-geraden-und-ebenen

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 157 (zone 28, e1 43,
e2 32, e3 23, e4 31)

Prüfung: Jede Rechenzeile mit sympy nachgerechnet (Skript
nachrechnen.py im Scratchpad, 132 Checks: Punktproben mit
herausfallendem Parameter, Zugehörigkeit über den Vielfachen-Ansatz,
Identität und Parallelität der Geradenscharen, Nichtparallelität
allgemein, windschiefe Lage, Parameter aus Skalarprodukt,
Kollinearität, Gerade-in-Ebene, Durchstoßpunkte mit Bereichs- und
Ganzzahligkeitsbedingung, Ebenen aus drei Punkten, Winkel- und
Abstandsgleichungen mit beiden Lösungen, das Flächenminimum auch
über die Ableitung der Zielfunktion, Schnittpolygone der Körper
kantenweise mit Eckenzahl je Bereich, Kantenbereiche der
N_k-Prismen, Spurgeraden, Achsenabschnitte mit Vorzeichenfällen) –
kein Rechenfehler; jedes pruef-Feld gegen die Lösung gehalten. Alle
44 Originale der Mappe gegen die verfremdeten Zeilen gehalten
(Zahlen, Form, Falle), ebenso die Zahlen des Merkkastens. Grafiken
gegen die Bausteinsyntax und die ksys3-Bereiche geprüft (Punkte auf
den Geraden, Parameterbereiche innerhalb der Achsen).
`python3 werkzeuge/bank-pruef.py scharen-von-geraden-und-ebenen`:
„Abweichungen: 0, Warnungen: 0". Geprüft: 23 Ankreuzen-Zeilen (je
genau eine richtige Option, Lösung wortgleich), 13
Fehler-finden-Zeilen (zone 1, e1 3, e2 3, e3 3, e4 3; jeder
eingebaute Fehler ist falsch, jede angegebene Rechnung richtig).

## Befunde

e2-k1-s5-v2: „im Quadrat mit $0 \le x_1 \le 3$ und $0 \le x_2 \le 4$"
ist ein Rechteck 3 × 4, kein Quadrat – Vorschlag: „im Quadrat mit
$0 \le x_1, x_2 \le 3$" (der Durchstoßpunkt hat $x_2 = 3$, Lösung
$k = -1; 0; 1; 2$ und pruef bleiben). Dazu trägt das antwort-Gerüst
„$k = $ __" nur einen Wert, gesucht sind vier – Vorschlag:
„$k = $ __, __, __, __".

e2-k1-s6-v1, e2-k1-s6-v2, e2-k1-s6-v3: Verlangt sind die
Koordinatengleichung und $k$, das antwort-Gerüst hat nur „$k = $ __";
die Ebenengleichung hat keinen Platz auf dem Blatt – Vorschlag:
„$E$: __, $k = $ __".

e4-k1-s1-v1, e4-k1-s1-v2, e4-k1-s1-v3, e4-k1-s1-v4, e4-k1-s1-v5:
„Gib $E_2$ an" (v5: $F_2$) ohne Gerüst, antwort ist leer; die
Gleichung hat nur die Zeichnung als Ort – Vorschlag: antwort
„$E_2$: __" (v5 „$F_2$: __"), wie es die Bank bei zeichnen-Zeilen
mit Rechenanteil sonst hält.

e1-k2-s8-v3: Der Richtungsvektor $(1 | k | 0)$ von $h_k$ ist der des
Originals 2023-bebb-lk-A1.5b, $(1; a; 0)$; die Verfremdung ändert
nur $g$ und den Stützvektor – Vorschlag: $h_k: \vec{x} = (1 | 0 | 2)
+ s \cdot (2 | k | 0)$; die Rechnung bleibt ($x_3$: $r = 0$, $x_1$:
$s = 0$, $x_2$: $3 = 0$), Lösung und pruef unverändert.

e2-k1-s1-v5: Der Richtungsvektor $(1 | 0 | -1)$ ist das Negative des
Richtungsvektors $(-1 | 0 | 1)$ aus Original 2024-bebb-lk-A1.3a und
Merkkasten Einheit 2 – dieselbe Richtung, die der Schüler aus dem
Kasten kennt – Vorschlag: $g: \vec{x} = (1 | 2 | 0) + r \cdot
(1 | 1 | -2)$, dann $3k + 5 - 2(k + 6) = 0$, also $k = 7$ (pruef 7;
Stützpunkt liegt nicht in $E_7$, die Gerade ist echt parallel).
Ermessen: Form und Falle sind gewahrt, nur die Zahl wiederholt.

e4-k1-s5-v1: Die Schar $E_k: k x_1 + x_2 + 2x_3 = 4$ steht
wortgleich schon in e1-k1-s0-v3 (Ankreuzen) und e1-k2-s6-v3
(Verfremdung des Originals 2022MerhoehtAAGLAA222-a) – dieselbe
Gleichung in drei Einheiten – Vorschlag: $E_k: k x_1 + 2x_2 + x_3 =
6$, Lösung $g_k: \vec{x} = (0 | 3 | 0) + r \cdot (2 | -k | 0)$,
pruef [0, 3, 0]. Ermessen: keine Aufgabe ist doppelt, nur die Schar.

Sauber: 145 Zeilen ohne Befund

## Abgleich

Beide Leser: kein Befund deckungsgleich. e4-k1-s5-v1 nennen beide,
aber mit anderem Inhalt (Erstleser: Merkmal-Aufteilung v1/v2 gegen
v3; Zweitleser: dieselbe Schar wie e1-k1-s0-v3 und e1-k2-s6-v3).
Die Korrektur des Erstlesers an e4-k1-s3-v2 (Eckenzahl bei k = 2,
4, 6) ist in der jsonl umgesetzt und vom Zweitleser als richtig
nachgerechnet (3, 3, 5, 4, 5, 3, 3 Ecken für k = 1 … 7).
Nur Erstleser: zone-f3-v2 (Grundfall-Variante trägt schon den
Fallstrick von f3-v4: Faktor aus x_1 und x_2, Widerspruch erst in
x_3) – richtig, übersehen; die Zahlen sind korrekt, aber v4 bringt
danach nichts Neues. e3-k1-s4-v1, e3-k1-s4-v2 (Lösung springt von
„kleinste Höhe MQ_k" zu „F_k senkrecht zu SC") – richtig; ich hatte
die Äquivalenz nachgerechnet (MQ_k ⊥ BD für jedes k, BD ⊥ SC) und
die Lösung als „knapper Weg" durchgehen lassen, der Halbsatz kostet
nichts. e4-k1-s5-v1 bis v3 (Varianten ändern das Merkmal:
Spurgerade ohne Lotfußpunkt gegen Lotfußpunkt ohne Spurgerade) –
gesehen und nicht geführt, siehe Widerspruch.
Nur Zweitleser: e2-k1-s5-v2 (Rechteck 3 × 4 heißt „Quadrat";
Gerüst für vier Werte); e2-k1-s6-v1 bis v3 (kein Gerüst für die
Ebenengleichung); e4-k1-s1-v1 bis v5 (kein Gerüst für E_2 bzw.
F_2); e1-k2-s8-v3 (Richtungsvektor (1 | k | 0) des Originals
übernommen); e2-k1-s1-v5 (Richtungsvektor aus Original und
Merkkasten, nur das Vorzeichen gedreht); e4-k1-s5-v1 (Schar
k x_1 + x_2 + 2x_3 = 4 zum dritten Mal).
Widerspruch: e4-k1-s5-v1 bis v3 – der Erstleser hält die
Aufteilung des Sprossentexts auf v1/v2 (Spurgerade) und v3
(Lotfußpunkte) für einen Merkmalwechsel, der zu beheben ist; der
Zweitleser hält sie für tragbar, weil die Sprosse zwei Originale
mit je einem Handgriff bündelt (2022-bebb-lk-A1.6b Teil A,
2024-bebb-lk-B3g) und der Lotfußpunkt auf g_k für allgemeines k
keine glatten Koordinaten hat – die Regel „Varianten unterscheiden
sich nicht im Merkmal" spricht für den Erstleser, der Preis wäre
eine Sprossenteilung im Katalog.
