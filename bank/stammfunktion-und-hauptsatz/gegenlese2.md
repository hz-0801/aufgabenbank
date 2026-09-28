# Zweitlesung stammfunktion-und-hauptsatz

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 150 (zone 25, e1 32,
e2 27, e3 32, e4 34)

Prüfung: Jede Rechenlösung mit sympy nachgerechnet (Skript
nachrechnen.py im Scratchpad, 145 Einzelprüfungen an 135 Zeilen:
alle Stammfunktionsnachweise F' = f, Konstanten c und Faktoren r,
bestimmte Integrale und Hauptsatzdifferenzen, Periodenintegrale,
Kurvenlängen numerisch, Abweichungen in Prozent, Integralfunktionen
samt Nullstellen, Wendestellen und Werten, Vorzeichenwechsel und
Extremstellen der Graphenaufgaben, Fensterwerte der Grafiken) – kein
Rechenfehler; die 15 Zeilen ohne Zahl (Begründen, Vorstufe) von Hand
gelesen. Alle 45 Grafiken mit xelatex und mathblatt.sty gerendert und
angesehen. Alle 36 Zeilen mit original gegen Abschnitt 2 der Mappe
gehalten: überall andere Zahlen bei gleicher Form und Falle (eine
Ausnahme unten). `python3 werkzeuge/bank-pruef.py
stammfunktion-und-hauptsatz`: „Abweichungen: 0, Warnungen: 0".
Geprüft: 19 Ankreuzen-Zeilen (je genau eine richtige Option, Lösung
beginnt wortgleich mit ihr), 13 Fehler-finden-Zeilen (zone 1, e1 3,
e2 3, e3 3, e4 3; jeder eingebaute Fehler ist falsch, jede angegebene
Rechnung richtig).

## Befunde

e3-k1-s0-v4: Gerendert sind die Beschriftungen $u$ und $v$ am rechten
Fensterrand abgeschnitten (beide Kurven laufen bei $x = 3$ aus dem
Fenster, es bleibt je ein Strich) – ein Schüler kann die Graphen
nicht zuordnen, die Ankreuzaufgabe ist so nicht lösbar. Dazu ist das
Paar $u = -0{,}5x^2 + 2$, $v = -x^3/6 + 2x$ genau $f$ und die gesuchte
Stammfunktion $F$ des Grundfalls e3-k1-s1-v2 derselben Kette: die
Vorstufe zeigt die Skizze, die der Grundfall verlangt – Vorschlag:
`\begin{ksys}[xmin=-3,xmax=5,ymin=-3,ymax=3,ablesen]
\parabel{-0.5}{1}{2}{u} \funktionab{-(\x-1)^3/6+2*(\x-1)}{v}{-2.8}{4.8}
\end{ksys}` ($v' = u$, Nullstellen von $u$ bei $-1$ und $3$; am
Rendering geprüft, beide Beschriftungen sichtbar); Lösung
„$v$ – …, an den Nullstellen von $u$ hat $v$ seine Extrempunkte"
bleibt.

e3-k1-s6-v1: Derselbe Graph `\parabel{0.5}{1}{-2}{f'}` steht schon
in zone-f4-v3 (Blatt 0, Nullstelle mit Vorzeichenwechsel bei $3$, die
zweite bei $-1$ ablesbar); die Prüfungshöhe verlangt genau dieses
Paar $a = -1$, $b = 3$ – Vorschlag: `\begin{ksys}[xmin=-2,xmax=6,
ymin=-3,ymax=4,ablesen] \parabel{0.5}{2}{-2}{f'} \end{ksys}`,
Lösung „z. B. $a = 0$ und $b = 4$: $f'(4) - f'(0) = 0 - 0 = 0$",
pruef [0, 4].

e4-k1-s2-v3: Gleicher Integrand wie e4-k1-s2-v2 ($f(t) = -t + 2$,
`\gerade{-1}{2}{f}`), nur die untere Grenze und das Fenster sind
anders – zwei Varianten derselben Sprosse mit derselben Funktion –
Vorschlag: `\begin{ksys}[xmin=-3,xmax=5,ymin=-4,ymax=4,ablesen]
\gerade{-1}{1}{f} \end{ksys}`, untere Grenze $-2$; Lösung „$x = -2$
(gleiche Grenzen) und $x = 4$: das Dreieck von $-2$ bis $1$ über der
Achse hat den Inhalt $4{,}5$, das von $1$ bis $4$ darunter
ebenfalls", pruef [-2, 4].

e3-k1-s1-v5: $f(x) = x^2 e^{-x}$ ist im Fenster zu flach – der
Hochpunkt $(2 \mid 0{,}54)$ ist bei 8-mm-Karo gut 4 mm hoch, die
Kurve liegt von $1$ bis $5$ fast auf der Achse; die Lösung verlangt
den Wendepunkt von $F$ bei $2$, den ein Schüler am Bild nicht
verorten kann – Vorschlag: $f(x) = 2x^2 e^{-x}$ (Hochpunkt
$(2 \mid 1{,}08)$), Fenster `ymax=5`, `\funktionab{2*\x^2*exp(-\x)}
{f}{-0.7}{5} \punkt{0}{1}{P}`; Lösungsgrafik
`\funktionab{5-2*(\x^2+2*\x+2)*exp(-\x)}{F}{-0.9}{4.8}` ($F(0) = 1$,
$F' = f$ geprüft); Lösung und pruef unverändert.

e3-k1-s3-v3: Derselbe Graph $x^3/3 - x$ steht in e3-k1-s5-v2 als $f$
mit eingezeichnetem $f'$; dort ist $f'(0) = -1$ ablesbar, genau die
hier gesuchte Tangentensteigung, beide Zeilen in Einheit 3 –
Vorschlag: `\funktionab{\x^3/3-2*\x}{F}{-2.9}{2.9}` (Fenster
unverändert), Lösungsgrafik mit `\tangentean*{\x^3/3-2*\x}{0}{t}`,
Lösung „$f(0) = -2$ – die Tangente im Ursprung hat die Steigung
$-2$", pruef -2 (gerendert: die Tangente läuft durch $(1 \mid -2)$).

e1-k1-s6-v2: Der Faktor $(6x - 3)$ ist der Polynomfaktor des
Originals 2020-be-gk-B2.1h ($f(x) = (6x - 3) \cdot e^{-x}$, in
e1-k1-s4-v3 schon verfremdet zu $(2x + 3)$); die Variante trägt kein
original – Vorschlag: $f(x) = (4x - 2) \cdot e^{2x}$, Ansatz
unverändert, Lösung „$r = 2$, denn $F'(x) = r \cdot (2x - 1) \cdot
e^{2x}$", pruef 2.

e1-k1-s5-v1: Die Lösung nennt zwei verschiedene Funktionen beide
$G$ („$G(x) = x^2 - 2x + 3$ und $G(x) = x^2 - 2x - 3$") –
Vorschlag: wie in v2 nur die Terme, „also $x^2 - 2x + 3$ und
$x^2 - 2x - 3$".

e3-k1-s6-v5: Das Gerüst verlangt „$H(x) = $ __", die Lösung endet
mit „$H(x) = F(x) + 3$" ohne Term (v4 schreibt ihn aus) –
Vorschlag: „$H(x) = \frac{1}{2} \cdot (-x^2 + 6x - 6) \cdot e^{x}
+ 3$".

e4-k1-s5-v3, e4-k1-s5-v4: $D(x)$ ist über $x$ definiert, die Frage
sagt „bei $t = 4$" bzw. „bei $t = 6$" – zwei Buchstaben für
dieselbe Zeit – Vorschlag: „dass $D$ bei $x = 4$ sein Maximum hat"
(bzw. $x = 6$), Lösung entsprechend „Maximum bei $x = 4$".

zone-f1-v2: Merkmal des Grundfalls ist „Bruch mal Potenz, im Kopf",
die Aufgabe ist eine Bruchaddition $\frac{1}{3} + \frac{1}{6}$ ohne
Potenz – die zweite Variante ändert das Merkmal, nicht nur die
Zahlen – Vorschlag: $\frac{1}{2} \cdot 4^2$ (Lösung $8$, pruef 8);
Ermessen: wer die Bruchaddition auf Blatt 0 will (die Fertigkeit
nennt sie), weitet das Merkmal auf „Bruch mal Potenz oder Brüche
addieren, im Kopf".

e3-k1-s2-v2, e3-k1-s2-v3, e3-k1-s1-v3: Beschriftung $F$ am
Fensterrand abgeschnitten (gerendert: in s2-v2 bleibt von $F$ bei
$(6 \mid 4)$ ein Strich, in s2-v3 sitzt $F$ auf der Zahl $4$ der
x-Achse, in der Lösungsgrafik von s1-v3 ist $F$ bei $(4 \mid 3{,}65)$
halb weg) – bei einem einzigen Graphen unschädlich – Vorschlag:
s2-v2 `xmax=7`, s2-v3 `xmax=5` (die Parabel verlässt das Fenster dann
oben bzw. unten, die Beschriftung steht innen; gerendert), s1-v3
`\funktionab{2*atan(\x)*3.14159/180+1}{F}{-4}{3.7}`.

Sauber: 136 Zeilen ohne Befund

## Abgleich

Beide Leser: e3-k1-s0-v4 (Bildpaar ist f und die Lösung F von
e3-k1-s1-v2; der Erstleser führt dafür beide ids, der Zweitleser
ändert nur die Vorstufe und sieht zusätzlich die abgeschnittenen
Beschriftungen u und v); e4-k1-s5-v3, e4-k1-s5-v4 (D über x erklärt,
gefragt „bei t = 4"; der Erstleser will zusätzlich x im Text
erklären); zone-f1-v2 (Bruchaddition unter dem Merkmal „Bruch mal
Potenz"; beide nennen als Ausweg auch das weitere Merkmal).
Nur Zweitleser: e3-k1-s6-v1 (gleicher f'-Graph wie zone-f4-v3, dort
sind −1 und 3 ablesbar); e4-k1-s2-v3 (gleicher Integrand wie v2);
e3-k1-s1-v5 (f zu flach, Wendepunkt bei 2 nicht verortbar, am
Rendering geprüft); e3-k1-s3-v3 (gleicher Graph wie e3-k1-s5-v2, wo
f'(0) = −1 abzulesen ist); e1-k1-s6-v2 (Faktor 6x − 3 aus
2020-be-gk-B2.1h); e1-k1-s5-v1 (zweimal G); e3-k1-s6-v5 (H ohne
Term); e3-k1-s2-v2, e3-k1-s2-v3, e3-k1-s1-v3 (Beschriftung F am
Fensterrand abgeschnitten).
Nur Erstleser: zone-f3-v4 (pruef "" trotz Ziffer 5) – richtig nach
dem Wortlaut von bank.md; das Prüfskript lässt es durch, deshalb
übersehen. zone-f3-v1 bis v5 („Welche Funktion …?" legt eine
einzige Antwort nahe) – geteilt, kostet nichts. zone-f1-v6 (nur
ungerade Potenzen, das Merkmal nennt gerade und ungerade) – richtig,
übersehen. e1-k1-s3-v2 ((x − 2)² · e^x ist f_0 aus
2025-bebb-lk-B2.2b) – richtig, übersehen: ich hatte jede Zeile nur
gegen ihr eigenes Original gehalten, nicht gegen alle 50.
e2-k2-s1-v3 (Startpunkt des Balls fehlt; ab dem Boden wäre der Weg
9,17 m) – richtig, übersehen, die Grenze 0 steht nur in der Lösung.
e2-k1-s2-v2 (Satz „Energie ist das Integral der Leistung" fehlt) –
geteilt; die Einheit kWh im Gerüst deutet es an, der Satz des
Originals macht es eindeutig.
e4-k1-s1-v1 bis v4 („eine Nullstelle" lässt auch die gerechnete zu)
– geteilt in der Sache: jede Nullstelle ist eine richtige Antwort,
die Zeile ist damit lösbar, aber die Lösung nennt nur die untere
Grenze; die Umformulierung des Erstlesers zielt auf den Handgriff der
Sprosse. e2-k3-s2-v3 (cos über [0; π] ist keine volle Periode) –
geteilt: Lösung und Symmetrieargument stimmen, der Gegenstand weicht
vom Sprossentext ab. e1-k1-s6-v5 (Stammfunktion −e^(−x) wird
nirgends geübt) – nicht geteilt: der Kasten setzt „Stammfunktionen
elementarer Funktionen" als Auswendigstoff, und die Formelsammlung
führt das Paar; ein Hinweissatz schadet aber nicht.
Widerspruch: e1-k1-s6-v5 – der Erstleser sieht in −e^(−x) einen
Schritt, den keine Sprosse trägt, der Zweitleser den Auswendigstoff
des Kastens (elementare Stammfunktionen) und die Formelsammlung.
Sonst kein Widerspruch: kein Befund des einen hält der andere für
falsch.
