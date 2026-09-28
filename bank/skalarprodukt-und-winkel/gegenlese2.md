# Zweitlesung skalarprodukt-und-winkel

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 155 (zone 31, e1 26,
e2 38, e3 31, e4 29)

Prüfung: Jede Rechenlösung aus den Angaben der Aufgabe neu berechnet
(Skript nachrechnen.py im Scratchpad, sympy): alle Skalarprodukte,
Beträge, Differenzvektoren, Kreuzprodukt der Zone, alle Winkel
zwischen Vektoren (0–180°), Geraden und Ebenen (Betrag im Zähler,
0–90°), Gerade–Ebene (Sinus), Projektionen, Prozentneigungen,
Bogenlängen samt Kreisprobe der Punkte, die Parameterungleichungen
mit sympy gelöst, die Schnittpunkte der Geradenpaare (sie schneiden
sich), die Trapez-Parallelitäten, die Ecke des rechten Winkels über
alle drei Ecken, die Zeltpyramiden aus den zwei Ebenen rekonstruiert
(Spitze auf der Achse, beide Normalen zeigen nach außen, Innenwinkel
ist der Nebenwinkel), die Schattenpunkte der Pyramidenspitzen. Jedes
pruef ausgewertet und gegen die gerundete Lösung gehalten: kein
Rechenfehler, keine Abweichung. Alle 24 Originale aus Abschnitt 2 der
Mappe gegen die verfremdeten Zeilen gehalten: überall andere Zahlen
bei gleicher Form; Kasten-Zahlen des Eintrags nirgends übernommen.
`python3 werkzeuge/bank-pruef.py skalarprodukt-und-winkel`:
„Abweichungen: 0, Warnungen: 0". Geprüft: 23 Ankreuzen-Zeilen (je
genau eine richtige Option, Lösung wortgleich), 13 Fehler-finden-
Zeilen (zone 1, e1 3, e2 3, e3 3, e4 3; jeder eingebaute Fehler ist
falsch, jede angegebene Rechnung richtig).

## Befunde

e2-k2-s1-v3, e2-k2-s1-v5: „hat die Grundecken $K$, $L$ und $S$. S ist
die Spitze" (v5 „Bodenecken … und S") – S steht unter den Grundecken
und ist zugleich Spitze, der Text widerspricht sich – Vorschlag: „hat
die Grundecken $K(3 \mid 1 \mid 0)$ und $L(5 \mid 6 \mid 0)$ und die
Spitze $S(1 \mid 3 \mid 6)$" (v5 entsprechend „die Bodenecken K und L
und die Zeltspitze S"); Lösung und pruef unverändert.

e2-k2-s2-v1, e2-k2-s2-v2: Satzzeichenfehler „$D(2 \mid 3 \mid 2)$. ist
ein Trapez" (v2 „$T(2 \mid 5 \mid 3)$. ist ein Trapez") – Vorschlag:
den Punkt nach der Klammer streichen.

e1-k1-s1-v5: Die Aufgabe verlangt zweierlei (Skalarprodukt berechnen
und beurteilen, ob der Winkel kleiner als $90^\circ$ ist), das
antwort-Gerüst trägt nur das Skalarprodukt; die anderen s1-Zeilen
haben „Winkel: \leerfeld" – Vorschlag: „\quad kleiner als $90^\circ$:
\janein" anhängen.

e1-k1-s0-v3, e1-k1-s0-v4: Das Merkmal der Vorstufe ist „nur die Art
des Ergebnisses bestimmen", das der Sprosse 2 „verschachtelte
Ausdrücke von innen nach außen prüfen"; $(\vec a \circ \vec b) \cdot
\vec c$ und $\vec a \circ \vec b + \vec c$ sind schon verschachtelt und
nehmen Sprosse 2 vorweg (v4 ist zudem derselbe Fall Vektor plus Zahl
wie s2-v3 und k2-s1-v1) – Vorschlag: v3 „$\vec a \circ \vec a$"
(Zahl), v4 „$\vec a + 5$" (nicht definiert) – ungeschachtelt, die
Lösungen bleiben in der Folge Zahl, Vektor, Zahl, nicht definiert.

e3-k1-s1-v5: Ein „Hang", der mit $74{,}5^\circ$ gegen die Horizontale
steht, ist eine Felswand, keine Anwendung mit realistischer Größe (das
Original war eine Windradebene) – Vorschlag: Kontext behalten und die
Ebene flacher legen, etwa $E\colon x + 2y + 6z = 12$ ($\mathrm{cos}\,
\varphi = \frac{6}{\sqrt{41}}$, $\varphi \approx 20{,}4^\circ$; kein
Wert des Eintrags), oder die Ebene behalten und „eine schräge
Glasfront" daraus machen.

e4-k1-s0-v3: „Der Winkel, unter dem ein Lichtstrahl auf eine
Glasscheibe trifft" ist in der Optik der Einfallswinkel, gemessen zum
Lot – dafür stünde der Kosinus; die Aufgabe meint den Winkel zur
Scheibe (Sinus). Zwei Lesarten – Vorschlag: „Der Winkel zwischen
einem Lichtstrahl und dem Boden wird über …" (Lösung Sinus bleibt).
Ermessen: die Abitur-Formulierung „unter dem das Licht auf den
Untergrund trifft" (e4-k1-s1-v5) trägt keine Optik-Assoziation, die
Glasscheibe schon.

e3-k1-s0-v1, e3-k1-s0-v2: Beide Zeilen stehen fast wortgleich noch
einmal in e4 – v1 „Winkel zwischen zwei Ebenen über ihre
Normalenvektoren → Kosinus" ist e4-k1-s0-v4 („zwei Dachflächen"), v2
„Gerade und Ebene über Richtungs- und Normalenvektor → Sinus" ist
e4-k1-s0-v1 („Treppenkante und Boden") – über Ketten hinweg doppelt.
Der Katalog setzt „Kosinus oder Sinus?" vor Einheit 3 und 4, die
Zeilen müssen aber nicht dieselben sein – Vorschlag: in e3 die
E3-Falle abfragen: v1 „Der Winkel einer Ebene gegen die xy-Ebene wird
über ihren Normalenvektor und $(0 \mid 0 \mid 1)$ berechnet" (Kosinus),
v2 „Der Winkel zwischen dem Normalenvektor einer Ebene und der
xy-Ebene" (Sinus – Vektor gegen Ebene). Ermessen.

e3-k2-s1-v2: Ninas Aufgabe ($2x + y + 2z = 5$) hat dieselbe richtige
Lösung $48{,}2^\circ$ wie der Grundfall e3-k1-s1-v1 ($x + 2y + 2z = 8$)
derselben Einheit; kommen beide auf ein Blatt, steht die Lösung der
Fehler-finden-Zeile schon im Grundfall – Vorschlag: „$6x + 6y + 7z =
5$: $\lvert\vec n\rvert = \sqrt{36 + 36 + 7} = \sqrt{79}$, $\mathrm{cos}
\,\varphi = \frac{7}{\sqrt{79}}$, $\varphi \approx 38{,}0^\circ$";
richtig $\lvert\vec n\rvert = 11$, $\varphi \approx 50{,}5^\circ$
(pruef math.degrees(math.acos(7/11))).

e4-k3-s1-v1: Jonas' Richtungsvektor $(4 \mid 1 \mid 8)$ ist der
Normalenvektor von e3-k1-s1-v2 ($4x + y + 8z = 16$); sein falscher
Wert $27{,}3^\circ$ ist dort die richtige Lösung – auf einem
Übungsblatt über beide Einheiten verwirrend – Vorschlag: $(6 \mid 2
\mid 9)$, $\lvert\vec u\rvert = 11$, Jonas: $\mathrm{cos}\,\varphi =
\frac{9}{11}$, $\varphi \approx 35{,}1^\circ$; richtig $\mathrm{sin}\,
\varphi = \frac{9}{11}$, $\varphi \approx 54{,}9^\circ$ (pruef
math.degrees(math.asin(9/11))).

e4-k1-s4-v1, e4-k1-s4-v2, e4-k3-s1-v3: Die Rundungskette der Lösung
geht nicht auf. v1: mit dem gedruckten $\alpha \approx 73{,}7^\circ$
ergibt der Bogen $64{,}3$ m, gedruckt ist $64{,}4$ m (exakt
$64{,}350$, knapp). v2: „$\approx 46{,}4$ LE $\approx 92{,}7$ m", aber
$46{,}4 \cdot 2 = 92{,}8$. k3-s1-v3: mit $\alpha \approx 106{,}3^\circ$
kommt $18{,}55 \to 18{,}6$ m, gedruckt $18{,}5$ m. Ein Schüler, der
den gedruckten Zwischenwert weiterrechnet, landet neben der Lösung –
Vorschlag: den Zwischenwert zweistellig drucken ($\alpha \approx
73{,}74^\circ$, $106{,}26^\circ$) und in v2 „$\approx 46{,}36$ LE
$\approx 92{,}7$ m"; pruef bleibt.

e4-k2-s1-v2: „der Strahl durch S trifft die Seitenfläche" stimmt nicht:
der Strahl von S in Richtung $(2 \mid 2 \mid -3)$ läuft unterhalb der
Kante FS durch das Innere der Pyramide und erreicht den Boden in
$(2 \mid 2 \mid 0)$, innerhalb des Grundquadrats – Vorschlag: „das
Licht ist steiler als die Kante, der Strahl durch S bleibt unterhalb
von FS und träfe den Boden in $(2 \mid 2 \mid 0)$ innerhalb der
Grundfläche – der Schatten der Spitze fällt nicht neben die Pyramide".

e4-k2-s1-v1: $\varphi_K \approx 54{,}7^\circ$ ist der Ergebniswert des
Kastenbeispiels der Einheit (Lichtrichtung $(1 \mid -1 \mid -2)$,
$54{,}7^\circ$), zufällig über einen anderen Weg
($\mathrm{tan} = \sqrt 2$); bank.md sperrt Ergebnisse des Kastens –
Ermessen: $S(0 \mid 0 \mid 5)$ statt $(0 \mid 0 \mid 6)$ gibt
$\mathrm{tan}\,\varphi_K = \frac{5}{3\sqrt 2}$, $\varphi_K \approx
49{,}7^\circ$, die Kante bleibt steiler als das Licht ($35{,}3^\circ$).

e3-k1-s3-v3: Die Aufgabe verlangt am First „als Term in $\varphi$ und
als Zahl", das Gerüst hat dafür ein Feld „am First \leerfeld" (3 cm) –
Vorschlag: „am First: \leerfeld $\approx$ \leerfeld[$^\circ$]".

e1-k1-s3-v1, e1-k1-s3-v2, e1-k1-s3-v3, e1-k1-s5-v1, e1-k1-s5-v2,
e1-k2-s1-v3: Variablen im Fließtext ohne Mathemodus – „Werte von r",
„alle r", „Seitenlänge s und die Höhe h", „nur von s abhängt", in der
Lösung „h kommt nicht vor" – Vorschlag: $r$, $s$, $h$ setzen, wie
sonst im Eintrag.

Sauber: 130 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k2-s1-v3, e2-k2-s1-v5 (S unter den Grundecken und
zugleich Spitze); e2-k2-s2-v1, e2-k2-s2-v2 (Punkt mitten im Satz);
e1-k1-s0-v3, e1-k1-s0-v4 (Vorstufe schon verschachtelt, nimmt s2
vorweg – gleicher Vorschlag: eine Rechenart); e4-k1-s4-v1,
e4-k1-s4-v2, e4-k3-s1-v3 (Rundungskette des Bogens; der Erstleser
ergänzt „mit ungerundetem α", ich drucke α zweistellig – beides
verträglich); e4-k1-s0-v3 (Glasscheibe: Einfallswinkel zum Lot als
zweite Lesart).
Nur Erstleser: e3-k1-s4-v1, e3-k1-s4-v3 (mit dem gedruckten Winkel
2,9° bzw. 20,6° kommt 5,1 % bzw. 37,6 % statt 5,0 % und 37,5 %) –
richtig, übersehen; dieselbe Rundungskette wie beim Bogen, der
Vorschlag (Tangens exakt als 1/20 und 3/8) ist der bessere.
e4-k2-s1-v3 („also parallel zu einer Diagonalen" setzt achsenparallele
Grundseiten voraus) – richtig, ich hatte die Lage stillschweigend
angenommen; die Ergänzung kostet nichts. e3-k1-s2-v3 (F ist x = 0,
eine Koordinatenebene, gegen das merkmal „keine davon eine
Koordinatenebene") – richtig, übersehen; die Variante folgt dem
Original, das merkmal muss weicher werden. e2-k2-s6-v3, e2-k2-s6-v4
(Normalenrechnung in e2, der Kasten dazu kommt erst in e3) –
richtig, Katalogbefund; ich hatte nur die Geometrie geprüft.
e3-k1-s0-v2 (Sinusformel in e3 unbekannt) – richtig; damit fällt auch
mein Vorschlag für diese Zeile („Normalenvektor gegen xy-Ebene →
Sinus"), der den Sinus ebenso voraussetzt; mein Vorschlag für v1
bleibt. e4-k1-s2-v3 (Richtungsvektor steht schon in der
Geradengleichung, merkmal „Richtungsvektor erst bilden" fehlt) –
Beobachtung geteilt, Vorschlag nicht: siehe Widerspruch.
Nur Zweitleser: e1-k1-s1-v5 (kein Feld für die Beurteilung);
e3-k1-s1-v5 (Hang mit 74,5°); e3-k1-s0-v1 (wortgleich zu
e4-k1-s0-v4); e3-k2-s1-v2 (gleiche Lösung 48,2° wie der Grundfall
e3-k1-s1-v1); e4-k3-s1-v1 (Vektor und 27,3° aus e3-k1-s1-v2);
e4-k2-s1-v2 („trifft die Seitenfläche"); e4-k2-s1-v1 (54,7° ist das
Kastenergebnis, Ermessen); e3-k1-s3-v3 (ein Feld für Term und Zahl);
e1-k1-s3-v1 bis v3, e1-k1-s5-v1, e1-k1-s5-v2, e1-k2-s1-v3 (Variablen
ohne Mathemodus).
Widerspruch: e4-k1-s2-v3 – der Erstleser will die Dachkante über zwei
Punkte geben, damit die Variante das merkmal erfüllt; der Zweitleser
hält die Geradengleichung für die Form des Originals 2017-bb-ea-B3.2a,
das der Sprossentext nennt, und würde das merkmal weiten („Richtungs-
vektor aus zwei Punkten oder aus der Kantengleichung ablesen") statt
die Verfremdung zu ändern.
