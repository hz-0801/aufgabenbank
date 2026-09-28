# Zweitlesung rekonstruktion-von-funktionsgleichungen

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 146 (zone 27, e1 37,
e2 42, e3 40)

Prüfung: Jede Rechenzeile mit sympy aus dem Aufgabentext neu
aufgestellt und gelöst (Skript nachrechnen.py im Scratchpad: alle
Gleichungssysteme auf Eindeutigkeit und auf die Zahl Bedingungen =
Unbekannte geprüft, die angegebene Funktion in jede Bedingung
eingesetzt, Hoch-/Tiefpunkt mit f'' bestätigt, Tangenten- und
Knickbedingungen, Integrationskonstanten, Steigungswinkel über den
Tangens, Sinusparameter an beiden Extrempunkten, Flächen als
Integral, die drei Kettenlinien mit nsolve, die vierten Bedingungen
der Existenzfragen, die Ableitungen der Unmöglichkeitszeilen) – kein
Rechenfehler; jede pruef-Zahl gegen die Lösung gehalten. Die acht
Grafiken der e1 mit pdflatex und mathblatt.sty gerendert und
angesehen. Alle Originale aus Abschnitt 2 der Mappe gegen die
verfremdeten Zeilen gehalten: überall andere Zahlen bei gleicher
Form und Falle; die Zahlenbeispiele der Merkkästen kommen in keiner
Zeile vor. `python3 werkzeuge/bank-pruef.py
rekonstruktion-von-funktionsgleichungen`: „Abweichungen: 0,
Warnungen: 0". Geprüft: 16 Ankreuzen-Zeilen (zone 4, e1 4, e2 4,
e3 4; je genau eine richtige Option, Lösung wortgleich), 10
Fehler-finden-Zeilen (zone 1, e1 3, e2 3, e3 3; jeder eingebaute
Fehler ist falsch, jede angegebene Rechnung richtig).

## Befunde

e2-k2-s1-v1, e2-k2-s1-v2, e2-k2-s1-v3: „Eine Suppe wird vom Herd
genommen und kühlt ab. Ab $t = 5$ wird ihre Temperatur durch …
beschrieben. Zu Beginn des Abkühlens beträgt die Temperatur 80 °C"
– der Text bindet den Beginn des Abkühlens nicht an $t = 5$; wer
das Herdnehmen als $t = 0$ liest, hat eine zweite Lesart, in der
das Modell an der genannten Stelle gar nicht gilt (im Original
2017MgrundlegendBAnalysisCAS-1e macht die Geschichte $t = 20$
eindeutig: Steuerung nach 20 Minuten abgeschaltet). Gleiches in
v2 („Ab $t = 2$ … Zu Beginn des Erwärmens") und v3 („Ab $t = 4$ …
Zu Beginn des Abkühlens") – Vorschlag: den Zeitpunkt in die
Geschichte nehmen:
„Eine Suppe wird zum Zeitpunkt $t = 5$ ($t$ in Minuten seit
dem Anrichten) vom Herd genommen; ab dann wird ihre Temperatur
durch … beschrieben. Zu Beginn des Abkühlens …" – die Falle des
Originals (nicht $t = 0$ einsetzen) bleibt, die Lesart wird eine.
Lösung und pruef unverändert.

e2-k1-s5-v3: Merkmal ist „Randbedingung mit Steigungswinkel über
den Tangens"; mit $0^\circ$ ist $\mathrm{tan}(0^\circ) = 0$ und die
Bedingung dieselbe waagerechte Tangente wie in Sprosse 1 – der
Handgriff der Sprosse fehlt. Dazu die Größe: eine 4 m lange,
1,6 m hohe „Bodenwelle" auf einer Rollerbahn hat bis zu $51^\circ$
Gefälle (nachgerechnet), das ist eine Schanze – Vorschlag: „Eine
Mulde ist am Boden 4 m breit und wird durch eine zur $y$-Achse
symmetrische Parabel $p$ beschrieben, deren Nullstellen die Ränder
sind (Angaben in m). An den Rändern hat sie die Steigungswinkel
$-45^\circ$ und $45^\circ$. Bestimme eine Gleichung von $p$ und die
Tiefe der Mulde." Lösung $p(2) = 4a + c = 0$, $p'(2) = 4a =
\mathrm{tan}(45^\circ) = 1$, $a = 0{,}25$, $c = -1$,
$p(x) = 0{,}25x^2 - 1$, Tiefe 1 m; pruef [0.25, -1]; antwort
„p(x) = __, Tiefe __". Die Variante öffnet als einzige nach oben.

e2-k1-s5-v1: Ein „Rundbogen über einem Gartenweg" mit 4 m
Spannweite und 1 m Höhe – unter dem Bogen kommt niemand hindurch;
die Höhe folgt aus den $45^\circ$ und lässt sich nicht heben, ohne
die Zahlen zu verderben – Vorschlag: den Gegenstand tauschen, etwa
„Ein Bogen aus Weidenruten über einem Blumenbeet"; Zahlen, Lösung
und pruef unverändert.

e2-k1-s1-v4: „eine Koordinateneinheit entspricht 5 m", Befestigung
$A(0|5{,}5)$, Tiefpunkt $T(3|1)$ – das Seil der „kleinen
Hängebrücke" hängt auf 15 m Horizontale um 22,5 m durch –
Vorschlag: „eine Koordinateneinheit entspricht 1 m", $A(0|2{,}5)$,
$T(5|1)$; Lösung $c = 2{,}5$; $25a + 5b + 2{,}5 = 1$ und
$10a + b = 0$; $a = 0{,}06$, $b = -0{,}6$, also
$f(x) = 0{,}06x^2 - 0{,}6x + 2{,}5$; pruef [2.5, 0.06, -0.6]
(Durchhang 1,5 m auf 5 m).

e2-k1-s2-v1: Merkmal „vier Koeffizienten", die Variante gibt aber
den Ansatz $h(t) = a \cdot t^3 + b \cdot t^2$ mit zwei Unbekannten
vor (wie das Original 2019-be-gk-B2.1c); v2 und v3 haben vier. Die
Variante ändert damit nicht nur die Zahlen – Vorschlag: Merkmal auf
„dritter Grad: Wert- und Steigungsbedingungen an verschiedenen
Stellen, zwei bis vier Koeffizienten" weiten; oder v1 ohne
vorgegebenen Ansatz: „ganzrationale Funktion dritten Grades; zu
Beginn ($t = 0$) sind Höhe und Wachstumsrate null" – dann vier
Bedingungen, Lösung und pruef unverändert.

e1-k1-s3-v2: „Der untere Bogen einer Gartenpforte", Punkte
$P(0|4)$ und $R(6|4)$ – eine Pforte ist die Fußgängertür; 6 m breit
und 4 m hoch ist ein Hoftor (so auch das Original 2023-C-2b) –
Vorschlag: „Der untere Bogen eines Hoftors"; sonst nichts.

e1-k1-s5-v2: Gerendert liegt die Marke $P$ von $\punkt{1}{-1.5}{P}$
auf dem Kurvenstück, das rechts neben dem Tiefpunkt (bei
$x \approx 0{,}85$) ansteigt; der Punkt selbst ist erkennbar, die
Beschriftung schneidet den Graphen. Zudem läuft die Kurve links
oben aus dem Fenster (ymax 2, $f(-0{,}5) \approx 2{,}8$; geclippt)
– Vorschlag: $P(3|1{,}5)$ statt $P(1|-1{,}5)$ – dort steht das
Label frei; Lösung „$f(3) = -3a = 1{,}5$, also $a = -0{,}5$",
Aufgabentext „verläuft durch $P(3|1{,}5)$", Grafik
`\punkt{3}{1.5}{P}`, pruef unverändert; ymax auf 3.

e3-k1-s5-v1, e3-k1-s5-v2, e3-k1-s5-v3: Die Aufgabe hat zwei
Operatoren (Begründe den Ansatz; bestimme $a$ und $c$), das
antwort-Gerüst trägt nur „a = __, c = __" – für die Begründung
ist kein Platz vorgesehen – Vorschlag: „Begründung: __; a = __,
c = __". Ermessen: wer die Begründung auf den Schreibzeilen des
Teils sieht, lässt es.

Sauber: 134 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k2-s1-v1, e2-k2-s1-v2, e2-k2-s1-v3 („Zu Beginn des
Abkühlens" nicht an die Startstelle des Modells gebunden; beide
schlagen vor, den Zeitpunkt in den Text zu nehmen); e2-k1-s2-v1
(Ansatz mit zwei statt vier Koeffizienten; der Erstleser will v1
auf vier Koeffizienten weiten, ich biete das oder das weitere
Merkmal an); e2-k1-s5-v3 (Steigungswinkel 0° macht den
Tangens-Schritt überflüssig; der Erstleser sieht zusätzlich, dass
der vierte Grad die Prüfungssprosse s8 vorwegnimmt – richtig, mein
Vorschlag der Mulde zweiten Grades erfüllt beides).
Nur Zweitleser: e2-k1-s5-v1 (Rundbogen 1 m hoch über einem Weg);
e2-k1-s1-v4 (Hängebrücke mit 22,5 m Durchhang auf 15 m);
e1-k1-s3-v2 (Gartenpforte 6 m breit); e1-k1-s5-v2 (Marke $P$ auf
dem Graphen, am Rendering geprüft); e3-k1-s5-v1 bis v3
(antwort-Gerüst ohne Platz für die Begründung).
Nur Erstleser: e3-k1-s4-v1, e3-k1-s5-v1 bis v3, e3-k3-s1-v1 bis v3
($p$ ist in Einheit 3 die Periode und zugleich Funktionsname) und
e3-k1-s4-v3 ($b$ Parameter und Funktionsname) – richtig nach der
Regel „ein Buchstabe je Einheit für eine Sache", von mir übersehen;
die Umbenennung kostet nichts. e3-k1-s5-v1 bis v3 (Flächenformel
$\frac{2}{3} c \cdot x_0$ ohne das Integral, aus dem sie folgt) –
richtig, die Lösung springt dort; der Zwischenschritt gehört hinein.
Widerspruch: keiner – kein Befund, den der eine Leser für richtig
und der andere für falsch hält.
