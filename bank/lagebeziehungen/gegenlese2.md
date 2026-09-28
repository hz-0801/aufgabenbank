# Zweitlesung lagebeziehungen

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 146 (zone 27, e1 36,
e2 26, e3 31, e4 26)

Prüfung: Jede Rechenlösung mit sympy nachgerechnet (Skript
nachrechnen.py im Scratchpad: Normalenvektoren, Geradenpunkte,
Skalarprodukte, alle Punktproben an Koordinaten- und Parameterform,
Parameterwerte k, c, r/s, a, die Punkte mit gleichen Koordinaten,
Einsetzen des allgemeinen Geradenpunkts, Kreismittelpunkte, die
Schar-Fallunterscheidungen samt S_a, die Pyramidenschranken über
alle Ecken, alle Schatten- und Durchstoßpunkte, Netzhöhen,
Auftreffzeiten aus den quadratischen Gleichungen, die
Schattenlänge √3) – kein Rechenfehler; jedes Feld pruef gegen die
Lösung gehalten, `python3 werkzeuge/bank-pruef.py lagebeziehungen`:
„Abweichungen: 0, Warnungen: 0". Alle 42 Originale aus Abschnitt 2
der Mappe und die drei Kastenbeispiele gegen die Zeilen gehalten:
überall andere Zahlen bei gleicher Form und Falle. Geprüft: 25
Ankreuzen-Zeilen (zone 5, e1 8, e2 4, e3 4, e4 4; je genau eine
richtige Option, Lösung beginnt wortgleich mit ihr), 13
Fehler-finden-Zeilen (zone 1, je Einheit 3; jeder eingebaute Fehler
ist falsch, jede angegebene Rechnung richtig). Wortdoppelungen von
Aufgaben: keine.

## Befunde

e1-k2-s5-v1: $E$ ist in Einheit 1 überall die Ebene, hier heißt der
Endpunkt der Kante $E(5 | 0 | 3)$ (Regel: ein Buchstabe je Einheit
für eine Sache) – Vorschlag: Kante $AH$ mit $H(5 | 0 | 3)$, im
Lösungsweg und in der Lösung ebenso.

e1-k2-s6-v2: Die Ebenen heißen $S$ und $T$; in derselben Einheit
sind $S$ (k1-s0-v4, k2-s2-v1) und $T$ (k2-s0-v4, k2-s6-v1) Punkte –
Vorschlag: $F_1: x - 2y = 0$ und $F_2: x + 2y = 0$ (Lösung
entsprechend).

e1-k2-s7-v1, e1-k2-s7-v2: „Das Dreieck $ABC$" – die Ecken $A$, $B$,
$C$ werden nirgends angegeben, das Dreieck ist nur über die Ebene
und die Vorzeichen bestimmt – Vorschlag: „Das Dreieck $D$ ist der
Teil der Ebene … mit nichtnegativen Koordinaten" und „im Innern von
$D$" (Lösung unverändert).

e1-k2-s4-v1: „Eine Lärmschutzwand steht auf der Fahrbahn" – dann
stünde sie mitten auf der Straße; gemeint ist die Fahrbahnebene –
Vorschlag: „Eine Lärmschutzwand steht neben einer Fahrbahn, die in
der xy-Ebene liegt, und liegt in der Ebene $W$ …".

e2-k1-s0-v3, e2-k1-s5-v1, e2-k1-s5-v2, e2-k2-s1-v3: Der Buchstabe
$a$ steht in Einheit 2 für drei Sachen: Koeffizient der Ebene
(s0-v3, s3-v2), Scharparameter (s4-v1 bis v3) und die gemeinsame
Koordinate (s5-v1, s5-v2, k2-s1-v3) – Vorschlag: in s0-v3 $k$ wie in
den übrigen Ebenengleichungen der Einheit, in s5 und k2-s1-v3 $m$
für die gemeinsame Koordinate ($m - 4m + 6m = 3m = 9$); $a$ bleibt
der Schar (s4) und der Originalform $a \cdot x - a \cdot z = b$
(s3-v2).

e2-k2-s1-v3: Ergibt denselben Punkt $(3 | 3 | 3)$ wie die
Prüfungszeile k1-s5-v2; auf einem Blatt steht die richtige Antwort
der Fehlerzeile schon oben – Vorschlag: $E: 4x + y + 3z = 16$, Ben
rechnet $16 : 4 = 4$ und nennt $(4 | 4 | 4)$; richtig $8a = 16$,
$a = 2$, Punkt $(2 | 2 | 2)$ (pruef 2).

e3-k1-s4-v1, e3-k1-s4-v2, e3-k1-s4-v3, e3-k1-s5-v1, e3-k1-s5-v2,
e3-k1-s5-v3: Auch in Einheit 3 trägt $a$ drei Sachen: die Drehachse
(s4), die Koordinate der Punkte $(a | a | 0)$ (s5) und den
Scharparameter $g_a$ (s6, Originalform) – Vorschlag: Achse $d$ in
s4, Punkte $(m | m | 0)$, $(m | -m | m)$, $(2m | m | m)$ in s5; $a$
bleibt der Schar.

e3-k1-s6-v3, e3-k1-s6-v4, e3-k2-s1-v3: LaTeX `$S_t$$(\frac{t}{2} |
…)$` – zwei Formeln stoßen mit `$$` aneinander, das ist fragil (in
anderen Umgebungen der Beginn einer abgesetzten Formel) und
uneinheitlich zu `$B_t(t | 0 | 0)$` in derselben Zeile – Vorschlag:
`$S_t(\frac{t}{2} | \frac{t}{2} | 1)$` in einer Formel.

e3-k1-s6-v3, e3-k1-s6-v4: Das Antwortgerüst „$t \ge$ __" verrät auf
Prüfungshöhe die Form der Lösungsmenge (eine Schranke nach unten),
die der Schüler aus dem Vergleich der Ecken selbst finden soll –
Vorschlag: antwort „__" oder „für $t$ __".

e3-k2-s1-v3: Dieselbe Pyramide (Spitze in Höhe 1) mit derselben
Ebenenfamilie $y + z = c$ wie die Prüfungszeile k1-s6-v3 (dort
$c = 6$, hier $c = 5$); deren Lösung „die Grundfläche erreicht $E$
zuerst" nennt Toms Fehler vorweg – Vorschlag: Spitze in Höhe 2 und
$E: x + z = 5$: Tom prüft nur die Spitze, $\frac{t}{2} + 2 \ge 5$,
also $t \ge 6$; richtig liefern $B_t$ und $C_t$ den Wert $t$,
gemeinsame Punkte für $t \ge 5$ (pruef 5 bleibt).

e4-k3-s2-v1: Die Begründung „der Strahl, der an $P$ vorbeigestreift
wäre, trifft dort auf die Wand" ist schief – der Strahl streift
nicht vorbei, er wird von $P$ aufgehalten – Vorschlag: „Licht läuft
geradlinig; der Strahl durch $P$ wird von $P$ aufgehalten und fehlt
genau dort auf der Wand, wo die Lichtgerade durch $P$ die Wandebene
schneidet."

e4-k2-s1-v3: Der Typ heißt „Länge eines Schattens … beschreiben",
v1 und v2 beschreiben, v3 sagt „Berechne" und verlangt den Betrag
$\sqrt{3}$ – ein anderer Operator als in den Schwesterzeilen.
Ermessen: als Rechenfassung des Typs tragbar, weil das Merkmal
„bestimmen" sagt; wer den Typ als Deutungstyp halten will, fragt
„Beschreibe, wie man die Länge berechnet, und führe es aus".

Sauber: 126 Zeilen ohne Befund

## Abgleich

Beide Leser: e4-k2-s1-v3 (v3 sagt „Berechne", der Typ heißt
„beschreiben"); der Erstleser trägt den stärkeren Grund nach – der
Vektorbetrag steht nicht unter den Voraussetzungen des Eintrags –,
damit kippt mein Ermessen zu seinem Vorschlag (v3 als
Beschreibungsaufgabe mit eigenem Kontext).
Nur Zweitleser: e1-k2-s5-v1 ($E$ als Punkt); e1-k2-s6-v2 ($S$, $T$
als Ebenen neben den Punkten $S$, $T$ der Einheit); e1-k2-s7-v1, v2
($ABC$ ohne Ecken); e1-k2-s4-v1 (Wand „auf der Fahrbahn");
e2-k1-s0-v3, e2-k1-s5-v1, v2, e2-k2-s1-v3 ($a$ für drei Sachen in
Einheit 2); e2-k2-s1-v3 (Punkt $(3 | 3 | 3)$ wie k1-s5-v2);
e3-k1-s4-v1 bis v3, e3-k1-s5-v1 bis v3 ($a$ für drei Sachen in
Einheit 3); e3-k1-s6-v3, v4, e3-k2-s1-v3 (`$S_t$$(`); e3-k1-s6-v3,
v4 (Gerüst „$t \ge$ __"); e3-k2-s1-v3 (Pyramide und Ebenenfamilie
der Prüfungszeile); e4-k3-s2-v1 („vorbeigestreift").
Nur Erstleser: e3-k1-s4-v2 (Normalenvektor „gleich" Richtungsvektor)
– vom Erstleser bereits korrigiert, die jsonl trägt heute „ist ein
Vielfaches", ich habe die berichtigte Fassung geprüft. zone-f5-v2
($3a - 6 = 0$ fast gleich zone-f4-v1 $3k + 6 = 0$) – richtig,
übersehen; die Nähe zu f4-v1 trägt den Befund, das merkmal selbst
lässt Term und Gleichung ausdrücklich beide zu. e2-k2-s1-v1 ($Q$
steht nur in Janas Rechnung, nicht in den Angaben) – richtig,
übersehen; ohne $Q$ in den Angaben ist „falscher Punkt" kein
Schülerfehler, sondern ein Fremdkörper. e3-k1-s3-v3 ($t$ aus
$t + 1 = 5$ statt Entscheidung) – nicht geteilt: der Kasten sagt
„ein Parameter in einer anderen Koordinate ändert daran nichts",
genau das prüft v3; die Auflösung $t + 1 = 5$ ist Blatt-0-Stoff.
Widerspruch: e3-k1-s3-v3 – der Erstleser sieht im Bestimmen von $t$
einen anderen Schritt mit anderer Antwortform als in v1/v2, der
Zweitleser die Kastenaussage über den Parameter in einer anderen
Koordinate, geprüft am selben Merkmal (gleiche z-Koordinate).
