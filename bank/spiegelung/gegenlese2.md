# Zweitlesung spiegelung

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 117 (zone 26, e1 34,
e2 26, e3 31)

Prüfung: Jede Lösungszahl wurde mit sympy aus dem Aufgabentext neu
gerechnet (Skript im Scratchpad): Spiegelpunkte an Punkt, an
Koordinatenebenen, an Ebenen über Lotfußpunkt und Lotgerade,
Abstände, Verbindungsvektoren, Mittelpunkte, Beträge, Schnittpunkte
Gerade–Ebene, Ebenengleichungen aus Normalenvektor und Mittelpunkt
(Probe mit dem Mittelpunkt und dem Kantenpunkt U), Rautenpunkte der
Winkelhalbierenden, Symmetrieebenen der Körper (alle Ecken an jedem
Kandidaten gespiegelt und mit der Eckenmenge verglichen), Mittel-
werte mit Parameter, Drachen- und Rautenseiten, die Ecken der
ksys3-Bausteine gegen die Aufgabenmaße und den Achsenbereich. Alle
Zahlen stimmen; kein Rechenfehler. Die Tripel der Aufgaben wurden
zusätzlich gegen alle Tripel der Mappe verglichen, auch gegen die
mit Semikolon geschriebenen der IQB-Originale. bank-pruef.py v0.5:
0 Abweichungen, 0 Warnungen in allen vier Dateien. Ankreuzen: 20
Zeilen (e1 12, e2 4, e3 4), in jeder genau eine Option richtig und
in loesung wortgleich genannt. Fehler finden: 10 Zeilen (zone 1,
je Einheit 3), der eingebaute Fehler ist überall falsch und die
richtige Rechnung überall richtig; alle bestanden.

## Befunde

e3-k1-s6-v1: $C(-1 | -1 | 0)$ ist wortgleich die Ecke C des
verfremdeten Originals 2026MerhoehtAAGLAA223 („C(−1; −1; 0)“); die
Sperre des Prüfskripts greift nicht, weil zahlenpaare() nur Tupel
mit senkrechtem Strich liest, die IQB-Originale der Mappe aber mit
Semikolon schreiben. Gleicher Zufallstreffer in e1-k3-s2-v1:
$P(2 | -3 | 4)$ ist E(2; −3; 4) aus 2017MerhoehtBAGLAA2WTR1-1c
(anderes Verfahren). – Vorschlag: in e3-k1-s6-v1 C und D
verschieben, etwa $C(-1 | -3 | 0)$, $D(3 | -3 | 0)$,
$S_t(1 | t + 1 | 5)$ (Mittelwert $(5 + 2t - 3)/2 = t + 1$); in
e1-k3-s2-v1 eine Koordinate ändern, etwa $P(2 | -3 | 6)$; als
Skriptbefund in stand.md: Sperre auch für Tupel mit Semikolon.

e3-k1-s4-v3: Die Grundfläche ist das Merkkasten-Beispiel der
Einheit 3 (Zeile 68: B(4|0|0), C(4|6|0), D(0|6|0), Antwort x = 2,
y = 3) mit vertauschten Achsen – B(6|0|0), C(6|4|0), D(0|4|0),
Antwort x1 = 3, x2 = 2; zugleich die Zahlen des Originals
2025MerhoehtAAGLAA223-a. – Vorschlag: andere Maße, etwa
$B(8 | 0 | 0)$, $C(8 | 6 | 0)$, $D(0 | 6 | 0)$ und Abstand 3;
Lösung $x_1 = 4$ oder $x_2 = 3$, pruef [4, 3].

e1-k3-s4-v2: Die Sprosse heißt „über die Lotgerade: aufstellen,
schneiden, Parameter verdoppeln“, die loesung rechnet aber über den
gegebenen Abstand und den Einheitsnormalenvektor
($P - 4\vec{n}$); die Lotgerade kommt nicht vor, und der Abstand 6
macht sie überflüssig. – Vorschlag: loesung über die Lotgerade
$(5 + 2\lambda | -1 - \lambda | 4 + 2\lambda)$: $19 + 9\lambda = 1$,
$\lambda = -2$, Spiegelpunkt bei $2\lambda = -4$: $P'(-3 | 3 | -4)$;
den Abstand als Gegenprobe nennen oder aus der Aufgabe streichen.

e2-k1-s4-v3, e3-k1-s2-v1, e3-k1-s3-v3: Kontext und Buchstaben des
Originals sind übernommen, nur die Zahlen sind neu – Dachfläche
TUVW und Seitenfläche BUVC mit C, W, U (2026-bb-gk-B3e), Turmdach
mit Giebelspitzen E–H und Spitze S (2022-bebb-gk-B3e,
„Kirchturmdach“), Haus mit Satteldach (2019MgrundlegendBAGLAA2WTR2-
1b). bank.md verlangt „andere Zahlen, anderer Kontext“. –
Vorschlag: anderen Sachkontext (Pavillon, Zeltdach, Vitrine,
Lagerhalle) und andere Punktnamen.

e1-k3-s3-v1, e1-k3-s3-v2: antwort nennt $R$, die aufgabe führt R
nicht ein („Spiegle $Q$ an $E$.“); nur v3 sagt „Q und R liegen
symmetrisch“. – Vorschlag: „Bestimme den Spiegelpunkt $R$ von $Q$
an $E$.“ (Geringer, weil konventionell: e2-k1-s3-v1 und -v2
nennen $E$ nur in antwort.)

e3-k2-s1-v3: pruef [4, 2] trifft die Lösung $2t - \tfrac{1}{2}$
nicht; das Skript liest den Bruch $\tfrac{4t - 1}{2}$ als 4/2 und
meldet OK. Eine Lösung mit Parameter kennt bank.md nicht („"" nur
bei Begründen, Zeichnen oder ohne Ziffer“). Ähnlich e3-k1-s0-v2:
pruef 3 bei Ankreuzen mit Textoptionen, bank.md verlangt dort "".
– Vorschlag: beide pruef auf "" setzen; in stand.md als Befund:
bank.md und Skript regeln parametrische Lösungen nicht.

e3-k1-s4-v1: Der Quader 6 × 4 × 4 hat quadratische Querschnitte
senkrecht zu x1 und damit zwei weitere, schräge Symmetrieebenen
($x_2 - x_3 = 3$, $x_2 + x_3 = 7$). „Die beiden senkrechten“ bleibt
eindeutig, lädt aber zur Nachfrage ein. – Vorschlag: Höhe 5, dann
sind es genau drei Symmetrieebenen.

e3-k1-s1-v2: Die Grundecken in der genannten Reihenfolge A, B, C,
D bilden ein überschlagenes Viereck (BC und DA kreuzen sich); als
Trapez läuft es A, B, D, C. – Vorschlag: C und D tauschen:
$C(2 | 4 | 1)$, $D(-2 | 4 | 1)$.

e3-k1-s0-v3: $E$ bezeichnet hier eine Ebene, in e3-k1-s1-v1,
e3-k1-s1-v4 und e3-k1-s6-v3/v4 ($E_t$) einen Eckpunkt – bank.md:
ein Buchstabe je Einheit für eine Sache. – Vorschlag: in s0-v3
„die Ebene $L$“ (L ist in e3-k1-s5-v3 schon eine Ebene).

e2-k2-s1-v2: Im \rechnung-Block fehlt das & vor dem
Gleichheitszeichen (alle anderen Blöcke haben es). e2-k1-s5-v1,
e2-k1-s5-v2: Die Aufgabe spricht von der $x_1x_2$-Ebene, das ksys
beschriftet die Achsen x und y. – Vorschlag: „\vec{u} + \vec{v} &=
(4 | 3 | 3)“; im ksys xlabel=x_1, ylabel=x_2.

Sauber: 100 Zeilen ohne Befund

## Abgleich

Beide Leser: e3-k1-s1-v2 (Grundecken A, B, C, D überschlagen, C und
D tauschen); e1-k3-s4-v2 (loesung über Abstand statt über die
Lotgerade der Sprosse).
Nur Zweitleser: e3-k1-s6-v1 und e1-k3-s2-v1 (Tripel wortgleich aus
Originalen der Mappe, Sperre liest kein Semikolon); e3-k1-s4-v3
(Merkkasten-Zahlen mit vertauschten Achsen); e2-k1-s4-v3,
e3-k1-s2-v1, e3-k1-s3-v3 (Kontext und Buchstaben des Originals);
e1-k3-s3-v1, e1-k3-s3-v2 (R nicht eingeführt); e3-k2-s1-v3 und
e3-k1-s0-v2 (pruef ohne Bezug zur Lösung); e3-k1-s4-v1 (Quader mit
quadratischem Querschnitt); e3-k1-s0-v3 (E als Ebene und Eckpunkt
in einer Einheit); e2-k2-s1-v2 (& im \rechnung-Block); e2-k1-s5-v1,
e2-k1-s5-v2 (Achsenbeschriftung x, y statt x1, x2).
Nur Erstleser: e2-k2-s1-v2 ($\vec{u}$, $\vec{v}$ im Text nicht
eingeführt) – richtig, übersehen. e3-k1-s6-v2 (bei t = 1,5 ist die
Grundfläche ein Quadrat, dann vier Symmetrieebenen statt „der
beiden“) – richtig, übersehen, und der wichtigste Befund an der
Prüfungshöhe; v1 ist frei davon (Breite 4, Tiefe 6 + 2t). e3-k2-s1-
v3 (bei t = 3/4 Quadrat, „zweite Symmetrieebene“ nicht eindeutig) –
richtig, übersehen. e2-k1-s0-v1 bis v4 (dieselben vier Situationen
wie e1-k1-s0) – zustimmen, nachrangig: die Vorstufe gewinnt durch
neue Situationen, ein Fehler ist es nicht. e3-k1-s4-v1 bis v3 (kein
neues Merkmal gegenüber s3) – nur teils: v1 und v2 legen den Körper
weg vom Ursprung (1 … 7, −2 … 4), der Mittelwert ist dort nicht die
halbe Kante, das ist gegenüber s3 neu; für v3 (0 … 6, 0 … 4) und für
das merkmal von s3, das „über Mittelwerte“ schon vorwegnimmt,
zustimmen. Die Reihenfolge s3 vor s4 ist die des Katalogs (Zeile
89), also Katalogbefund, nicht Bankbefund.
Widerspruch: Der Erstleser nimmt Platzhalter-pruef (0, 1, [4, 2])
hin, weil das Skript sie annimmt; ich halte [4, 2] für keinen
Prüfwert, weil der Treffer nur durch das Lesen von (4t − 1)/2 als
4/2 entsteht, und schlage "" samt Regelbefund vor. Der Erstleser
sieht in e3-k1-s4-v1/v2 kein neues Merkmal, ich sehe es in der Lage
weg vom Ursprung.
