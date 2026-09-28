# Zweitlesung vektoren-und-rechenoperationen

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 134 (zone 27, e1 41,
e2 43, e3 23)

Prüfung: Jede Zeile mit Zahl in der Lösung wurde mit einem eigenen
sympy-Skript (Scratchpad, nachrechnen.py) aus dem Aufgabentext neu
berechnet: Verbindungsvektoren, Beträge, Betragsgleichungen mit
Vorzeichenwahl, Kollinearitätsfaktor, Termpunkte am Quader 6×4×3,
Linearkombinationen, vierte Ecke samt Rechtwinkel- und Längenprobe,
Diagonalenschnittpunkt, Durchstoßpunkt-Term mit Abstandsverhältnis,
Normierung, Drehung (Senkrechtheit, Länge, Vorzeichen), Stumpf-Term,
Skalarprodukte und Mischungsansätze; die Blickrichtungen als
Projektionen der Stäbe. 109 von 109 Proben stimmen mit loesung und
pruef überein. `python3 werkzeuge/bank-pruef.py
vektoren-und-rechenoperationen`: „Abweichungen: 0, Warnungen: 0"
(je Datei 0/0). Die 20 Originale in Abschnitt 2 der Mappe wurden
gegen die Zeilen mit Feld original verglichen (Zahlen, Verfahren,
Kontext). Geprüft: 16 Ankreuzen-Zeilen (je genau eine Option
richtig, Lösung nennt sie wortgleich) und 10 Fehler-finden-Zeilen
(Fehler ist falsch, richtige Rechnung stimmt); Begründen- und
Textzeilen inhaltlich gelesen.

## Befunde

e1-k3-s3-v2: „Zeichne von $P$ aus einen Pfeil zu $(-2 | 3)$ ein"
liest sich als Pfeil zum Punkt $(-2 | 3)$, gemeint ist der Vektor;
ein Schüler zeichnet von $P(3 | -1)$ nach $(-2 | 3)$ – Vorschlag:
„Zeichne den Vektor $\vec v = (-2 | 3)$ mit Fuß in $P$ ein."

e1-k3-s4-v2: Lösung $\sqrt{369} \approx 19{,}21$ m, die Aufgabe
nennt keine Rundung – Vorschlag: Zahlen glatt wählen, etwa
$M(0 | 0 | 8)$ und $B(9 | 12 | 0)$ ergeben 17 m; sonst „auf cm
gerundet" in den Text.

e2-k1-s7-v1: „$L$ ist der Lotfußpunkt von $K$" nennt nicht, worauf
das Lot fällt; für den Term unerheblich, aber ein Schüler stockt –
Vorschlag: „Lotfußpunkt von $K$ auf der Ebene $E$".

e2-k2-s1-v1: „wie oben" setzt voraus, dass das Quaderbild auf dem
Blatt darüber steht; $F$ wird gebraucht, ist aber nicht genannt –
Vorschlag: „wie oben" streichen und $F(6 | 0 | 3)$ mit angeben.

e2-k1-s4-v1: Lösungszusatz „(mit $\overrightarrow{BC}$ läge $E$
außerhalb)" hat keinen Bezug – außerhalb wovon? Im Original liegt
$E$ auf einer Diagonale, hier nicht – Vorschlag: „(mit
$\overrightarrow{BC}$ entstünde ein überschlagenes Viereck, kein
Quadrat $BCDE$)".

zone-f1-v2: merkmal „positive Koordinaten", abgelesen wird aber
$A(-2 | 3)$; die negative Koordinate ist das Merkmal der mittleren
Zeile (v3) – Vorschlag: $A(2 | 3)$ oder $A(3 | 1)$ (Grafik
anpassen).

zone-f6-v4: die Fallstrick-Zeile „das Ergebnis ist eine Zahl, kein
Vektor" unterscheidet sich von den Zeilen f6-v1/v2 nur in den
Zahlen; die Falle ist am Text nicht sichtbar – Vorschlag: Frage
„Zahl oder Vektor? Berechne." mit Antwortgerüst „= __" oder
antwort „Zahl: __".

e1-k1-s0-v1, e1-k1-s0-v2, e1-k1-s0-v3, e1-k1-s0-v4: der
Sprossentext verlangt auch „welche Bedingung sie liefert"; die
Aufgabe fragt nur „Was fehlt?", die Lösung antwortet trotzdem auf
beides („die Länge liefert sie") – Vorschlag: Frage ergänzen
„Was fehlt, und was liefert es?" oder die Lösung auf die Option
kürzen.

e1-k3-s3-v1: „Lies $\overrightarrow{AB}$ ab", die Grafik zeigt aber
nur die Punkte $A$ und $B$, keinen Pfeil (ksys kennt keinen
2D-Pfeil); merkmal „zwischen Pfeil … und Koordinaten wechseln" ist
so nicht getroffen – Vorschlag: „Lies $A$ und $B$ ab und gib
$\overrightarrow{AB}$ an."

e3-k1-s3-v1: gleicher Kontext wie das Original
2019MgrundlegendBAGLAA2WTR2-1e (Farben mischen, Preis je Liter,
Verhältnis, Gesamtpreis); bank.md verlangt „anderer Kontext" –
Vorschlag: andere Mischung, etwa Beton (Zement : Sand : Kies) oder
Teemischung; Farben stehen außerdem in zone-f5-v3 und
e3-k2-s1-v2 (dort regelfrei, aber dreimal dieselbe Einkleidung).

e1-k2-s6-v1: „600 Leihräder auf drei Stationen" ist der Kontext des
Originals (900 E-Scooter auf Stationen) mit anderem Fahrzeug, kein
anderer Kontext – Vorschlag: Verteilung anderer Art, etwa Paletten
auf drei Lager oder Bücher auf drei Filialen; v2 (Stimmen) ist
sauber.

e3-k1-s2-v1, e3-k1-s3-v1, e3-k1-s3-v2: Buchstabenregel („ein
Buchstabe je Einheit für eine Sache"): $w$ ist in s2-v1 die Zahl
der Wasserkisten, in s3-v1 die Liter Weiß; $k$ für Cola-Kisten
liest sich als „Kisten"; $c$ für Rosinen in s3-v2 ist unerklärt –
Vorschlag: s2-v1 Cola, Saft, Limo als $(c | s | l)$; s3-v2
Datteln statt Rosinen, $(h | n | d)$.

e2-k1-s6-v3: $P_2(-2 | 3 | -3)$ liegt genau in der Ecke des
Achsenbereichs (x1min=−2 Voreinstellung, x3min=−3 gesetzt); Punkt
und Gerade enden am Rand, das Label hat keinen Platz – Vorschlag:
`[x1min=-3,x3min=-4]` in Grafik und Lösungsgrafik.

e1-k2-s5-v3: die Draufsicht ist die Strecke von $(0 | 0)$ nach
$(0 | 4)$, sie liegt auf der $x_2$-Achse am Rand des Gitters
(xmin=0); ein Schüler zeichnet auf die Achsenlinie – Vorschlag:
Stäbe in die Ebene $x_1 = 2$ legen (Endpunkte $(2 | 0 | 0)$,
$(2 | 4 | 4)$, $(2 | 4 | 0)$, $(2 | 0 | 4)$), dann liegt die
Strecke im Gitter.

Sauber: 116 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k3-s3-v2 (Pfeil zum Punkt statt Vektor),
e2-k2-s1-v1 („wie oben", $F$ fehlt), zone-f1-v2 (merkmal „positive
Koordinaten" bei $A(-2 | 3)$).
Nur Zweitleser: e1-k3-s4-v2 (Rundung), e2-k1-s7-v1 (Lot ohne
Ebene), e2-k1-s4-v1 („außerhalb" ohne Bezug), zone-f6-v4
(Fallstrick unsichtbar), e1-k1-s0-v1 bis v4 (Bedingung gefragt oder
nicht), e1-k3-s3-v1 (kein Pfeil in der Grafik), e3-k1-s3-v1
(Kontext des Originals), e1-k2-s6-v1 (Kontext des Originals),
e3-k1-s2-v1/e3-k1-s3-v1/e3-k1-s3-v2 (Buchstaben $w$, $k$, $c$),
e2-k1-s6-v3 (Punkt in der Ecke des Achsenbereichs), e1-k2-s5-v3
(Draufsicht auf der Achse).
Nur Erstleser: e2-k2-s1-v2 (kein Körper genannt, $DH = \vec w$
folgt erst im Quader $ABCDEFGH$) – richtig, übersehen: die Zeile hat
keine Grafik, der Quader gehört in den Text; e3-k2-s3-v1
(Lösung nutzt $\vec m \circ \vec p$, ohne dass die Aufgabe $\vec m$
und $\vec p$ einführt) – richtig, übersehen, leicht: entweder die
Vektoren im Text nennen oder „$\vec m \circ \vec p =$" in der
Lösung streichen; e3-k2-s3-v1, v2, v3 (sprosse_text „Tupel in Form
von Punkten und Vektoren angeben" passt nicht zur Aufgabe) – nicht
geteilt: der sprosse_text der Anwendungszeilen ist in allen drei
Einheiten die GK-Kern-Zeile der Einheit (e1 „Betrag eines Vektors
bzw. Länge einer Strecke", e2 „Vektoraddition"), das Feld steht
nicht auf dem Blatt, und der Gesamtpreis ist das Skalarprodukt aus
genau dieser Kernzeile; wer es ändert, ändert alle drei Einheiten.
Widerspruch: Der Erstleser hält den sprosse_text von e3-k2-s3 für
einen Befund, der Zweitleser für die regelkonforme Etikettierung der
Pflichtzeilen; sonst keiner.
