# Zweitlesung rotationsvolumen

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 87 (e1 31, e2 31,
zone 25)

Prüfung: Jede Zeile gelesen; jede Lösung mit sympy nachgerechnet
(Integrale exakt, Ergebnis als π-Vielfaches und als Dezimalzahl,
dazu Massen, Umrechnungen, Nullstellen, Definitionsbereiche und die
Auflösung nach x² bei Rotation um die y-Achse); das Feld pruef gegen
die Lösung geprüft. Bei den Füllhöhengleichungen die Gleichung
gelöst, um die Sachlage zu prüfen (Kugel unter Wasser). Sperre gegen
Merkkasten, Typische Fehler und die 17 Originale der Mappe von Hand
verglichen. `python3 werkzeuge/bank-pruef.py rotationsvolumen`:
Abweichungen 0, Warnungen 0 (zone, e1, e2 je 0/0). Alle 87
Lösungszahlen stimmen mit der Nachrechnung überein; die Befunde
unten betreffen Sachlage, Verfremdung, Formulierung und Form.

## Befunde

rotationsvolumen-e1-k1-s5-v2: Die Daten sind nicht verträglich.
Die Gleichung $\pi \cdot$ Integral von t bis t + 2 über
$(2x + 16)\,dx = 150$ ist $4\pi(t + 9) = 150$ und ergibt
$t \approx 2{,}94$ cm; die Kugel mit Durchmesser 4 cm reicht bis
$x = 4$ und wäre dann nicht „ganz unter Wasser“, wie die Aufgabe
sagt (die Lösung verlangt $t \ge 4$). Zum Vergleich: v1 ergibt
$t \approx 17{,}7 \ge 6$, das Original $t \approx 10{,}6 \ge 10$,
e2-k2-s1-v3 $t \approx 15{,}4 \ge 4$ – alle verträglich. –
Vorschlag: „200 cm³ Wasser heben den Wasserstand um 2 cm“ (dann
$t \approx 6{,}9$) oder „220 cm³“ ($t \approx 8{,}5$); Lösung und
pruef entsprechend (200 bzw. 220).

rotationsvolumen-e1-k1-s0-v3, -v4: Der Aufgabentext nennt die
Achse wörtlich („um die y-Achse gedreht“, „um die x-Achse gedreht“),
die richtige Option beginnt mit denselben Worten – das Ankreuzen ist
Ablesen, kein Erkennen. v1 („senkrechte Achse“) und v2
(„waagerechte Achse“) verlangen den Schritt; damit unterscheiden
sich die vier Varianten im Merkmal, nicht nur in Zahlen und Kontext.
– Vorschlag: v3 „Ein Trichter steht mit der Öffnung nach oben; sein
Rand ist der Graph von $f(x) = 2\sqrt{x}$ über [0; 4], er dreht sich
um die senkrechte Achse.“; v4 „Eine Spielzeugrakete liegt
waagerecht; ihre Hülle ist der Graph von $f(x) = \sqrt{8 - x}$ über
[0; 8], gedreht um die waagerechte Achse.“

rotationsvolumen-e1-k1-s4-v2: Die Verfremdung nimmt dem Original
2017MerhoehtBAnalysisWTR2-2e die Falle. Dort ist die Dichte als
2700 kg/m³ gegeben und muss auf dm³ gebracht werden (Fehlerquelle
„dm³ nicht in m³ umgerechnet“); hier steht „Ein Kubikdezimeter Stein
hat die Masse 2,5 kg“, die Umrechnung entfällt. Rechnung stimmt:
$40\pi - 22{,}5\pi = 17{,}5\pi \approx 54{,}98$ dm³, Masse
$\approx 137{,}4$ kg. – Vorschlag: „Ein Kubikmeter Stein hat die
Masse 2\,500 kg“; Lösung mit dem Zwischenschritt
„2\,500 kg/m³ = 2,5 kg/dm³“, Ergebnis unverändert.

rotationsvolumen-e1-k1-s5-v3: Der gezeigte Zwischenschritt
„$0{,}0775 \cdot 0{,}9 \approx 0{,}0697$ t“ stimmt nicht mit sich
selbst: $0{,}0775 \cdot 0{,}9 = 0{,}06975$, gerundet 0,0698 t =
69,8 kg; das genannte Endergebnis 69,7 kg folgt nur aus dem
ungerundeten Volumen ($\tfrac{74}{3}\pi/1000 \cdot 0{,}9 \approx
0{,}06974$). – Vorschlag: „Masse $\approx 0{,}07749 \cdot 0{,}9
\approx 0{,}0697$ t $\approx 69{,}7$ kg“.

rotationsvolumen-e1-k2-s1-v3: Der Maßstab „1 LE = 2 cm, 1 VE =
$2^3 = 8$ cm³“ steht dreimal im Eintrag: zone-f4-v4 (5 VE →
40 cm³), hier (20π VE, Fehler Faktor 2 statt 8) und in e2-k1-s5-v2,
Schritt (2) (Fehler Faktor 2 statt 8). Zwei Fehler-finden-Stellen
mit demselben Maßstab und demselben falschen Faktor sind derselbe
Fehlerbaustein zweimal. – Vorschlag: hier „1 LE = 5 cm“, Rechnung
$V = 20\pi \cdot 5$ cm³ $\approx 314{,}16$ cm³; richtig 1 VE
$= 125$ cm³, $V = 2\,500\pi \approx 7\,853{,}98$ cm³; pruef
[125,2500*math.pi].

rotationsvolumen-e1-k2-s3-v2: Alle drei Anwendungen (v1 Fass, v2
Eimer, v3 Kreisel) enden mit „ja“; der Maßstab (2.4 b) will bei
Ja/Nein-Entscheidungen richtig und falsch etwa halbe-halbe. Rechnung
stimmt: $5{,}49\pi \approx 17{,}25$ l. – Vorschlag: „Passen 20 l
Wasser hinein?“ – nein, es fassen nur etwa 17,25 l; pruef bleibt
5.49*math.pi.

rotationsvolumen-e2-k1-s0-v2, -v4: In allen vier Zeilen der
Vorstufe steht die richtige Option an erster Stelle ($f(2)$, $f(3)$,
„der x-Wert zur Höhe y …“, $h(x)$); das Muster ist ratbar. In e1-s0
wechselt die Stelle (2, 1, 2, 1). – Vorschlag: v2 in der Folge „der
Kugelradius / $f(3)$ / die Stelle $x = 3$“, v4 in der Folge „$g(x)$ /
$g(x) - h(x)$ / $h(x)$“; loesung unverändert.

rotationsvolumen-e2-k1-s1-v3: Dieselbe Funktion und derselbe
Gegenstand wie e2-k1-s0-v3: dort „Glas, Kurve $y = x^2$, Drehung um
die y-Achse, Radius in der Höhe y“, hier „Sektglas, Längsschnitt
$y = x^2$, Drehung um die y-Achse, Integrand $\pi y$“ – zwei Sprossen
derselben Einheit am selben Beispiel; dazu ist der Sektkelch
$y = 2x^2$ in e2-k2-s3-v2 ein dritter Sektglas-Kontext. Rechnung
stimmt. – Vorschlag: hier $y = 4x^2$ mit Füllvolumen $\pi \cdot$
Integral von 0 bis h über $\tfrac{y}{4}\,dy$ und der Frage nach dem
Integranden $\tfrac{\pi}{4}y$ (Radiusquadrat $x^2 = \tfrac{y}{4}$);
Gegenstand etwa „Trinkglas“.

rotationsvolumen-e2-k1-s2-v2: x trägt zwei Bedeutungen – Koordinate
der Innenseite ($q(x)$, $1 \le x \le 5$) und Füllhöhe (Argument von
$s(x)$). Die Lösung mischt beide in einem Satz: „[0; 4] (Boden bei
$x = 1$, Rand bei 5); s(x) ist das Wasservolumen … bei der Füllhöhe x
dm“. Das Original macht es ebenso, bank.md verlangt aber einen
Buchstaben je Sache. Werte stimmen (Definitionsbereich [0; 4]). –
Vorschlag: $s(h) = \pi \cdot$ Integral von 1 bis $1 + h$ über
$(q(t))^2\,dt$, Definitionsbereich für h; Lösung „Boden bei $x = 1$,
Rand bei $x = 5$, also $0 \le h \le 4$“.

rotationsvolumen-e2-k1-s4-v1: Ergebnis wie im Original
2017-bb-ea-B2.1d. Dort Radius 1,5 LE · 4 cm = 6 cm, Grundfläche
12 cm × 12 cm; hier 1,2 LE · 5 cm = 6 cm, 12 cm × 12 cm – Radius und
Kantenlänge sind die Zahlen des Originals, obwohl LE und Maßstab
geändert wurden; Ergebnisse sind nach „Regeln für den Inhalt“
gesperrt. Dazu wiederholt „größter Radius 1,2“ die Zahl von s4-v2.
– Vorschlag: „größter Radius 1,4 LE, Höhe 2,5 LE, 1 LE = 5 cm“:
Radius 7 cm, Fach 14 cm × 14 cm × 12,5 cm; pruef [14,12.5].

rotationsvolumen-e2-k1-s4-v3: Die Aufgabe fragt nach Maßen und
Volumen, antwort trägt nur die Maße („__ dm × __ dm × __ dm“); die
Lösung nennt 54 dm³. – Vorschlag: antwort „__ dm × __ dm × __ dm,
V = __ dm³“.

rotationsvolumen-e2-k2-s3-v3: Der Text nennt die Füllhöhe x („x die
Füllhöhe in dm“), antwort und Lösung rechnen mit h („h = __ dm“,
$A(h) = \pi(h + 9)$) – h ist nirgends eingeführt (Buchstabenregel).
Außerdem fehlt der Nachweis-Schritt, den sprosse_text und merkmal
verlangen („als Term nachweisen … mit einer Folgefrage“); v1 und v2
haben ihn. Rechnung stimmt: $h = \tfrac{50}{\pi} - 9 \approx 6{,}92$.
– Vorschlag: „… x-Achse ist die senkrechte Rotationsachse, der Boden
liegt bei $x = 0$; 1 LE = 1 dm. Zeige, dass die Wasseroberfläche bei
der Füllhöhe h den Inhalt $A(h) = \pi(h + 9)$ hat. Bei welcher
Füllhöhe ist er 50 dm²?“; antwort „h = __ dm“.

rotationsvolumen-zone-f4-v3: „Erde, Dichte 0,8 t/m³“ ist die
Zahl-Kontext-Paarung des Originals 2019-A-2d („ein Kubikmeter
Pflanzerde wiegt 0,8 Tonnen“). Nach dem Buchstaben der Regel frei
(Zahl unter 10), dem Sinn der Sperre nach eine Übernahme. –
Vorschlag: „0,5 m³ Kies, Dichte 1,6 t/m³ – Masse in kg?“, Lösung
$0{,}5 \cdot 1{,}6 = 0{,}8$ t $= 800$ kg, pruef [0.8,800].

Hinweis ohne Befund: In neun Deutungs- und Aufstellzeilen trägt pruef
eine Zahl aus der Aufgabe statt einer Lösungszahl (e1-s5-v1 „250“,
e1-s5-v2 „150“, e2-s1-v1 „40“, e2-s1-v4 „0.001“, e2-s2-v1 „4“,
e2-s2-v3 „500“, e2-k2-s1-v2 „6“, e2-k2-s1-v3 „200“, e2-s5-v3 „0.61“).
Das Skript findet die Zahl und meldet OK, prüft damit aber nichts.
bank.md erlaubt "" bei Begründen; ob leeres pruef oder Pseudozahl
gewollt ist, entscheidet der Chat. Keine Änderung nötig.

Sauber: 72 Zeilen ohne Befund (alle 87 Lösungszahlen und alle
pruef-Ausdrücke rechnerisch richtig; Sperre und Originalkennungen in
Ordnung; Fehler-finden-Zeilen tragen echte Fehler aus „Typische
Fehler“ mit eigenen Zahlen; Ankreuzzeilen haben genau eine richtige
Option, wortgleich in loesung; keine Dublette gleicher Rechnung. Ein
harter Befund (s5-v2, Sachlage), der Rest Verfremdung, Formulierung
und Form.)

## Abgleich mit gegenlese.md

Befundzeilen: Erstleser (claude-opus-5-5) 7 Zeilen, Zweitleser 15
Zeilen; 4 Zeilen bei beiden, 3 nur beim Erstleser, 11 nur beim
Zweitleser. Die Entscheidung des Erstlesers, die zwei Zielmarken je
Prüfungshöhe (v1/v2, v3/v4) nicht als Merkmalswechsel zu werten,
teile ich.

Beide: e1-k1-s5-v2 (Daten unverträglich, $t \approx 2{,}94 < 4$;
beide schlagen 200 cm³ vor); e1-k1-s5-v3 (Rundungskette
$0{,}0775 \cdot 0{,}9$, gleiche Zahlen); e2-k1-s4-v3 (Antwortgerüst
ohne Volumenfeld); e1-k1-s4-v2 – dieselbe Zeile, verschiedener
Befund: der Erstleser rügt die Rundungskette „$54{,}98 \cdot 2{,}5
\approx 137{,}4$“ ($= 137{,}45$, gerundet 137,5; zutreffend, von mir
übersehen), ich die entfallene Falle des Originals (kg/m³ statt
kg/dm³); beides gilt, sein Vorschlag $43{,}75\pi \approx 137{,}4$ kg
und mein Vorschlag „2\,500 kg/m³“ lassen sich verbinden.

Nur Erstleser: e2-k1-s4-v2 (Rundungskette $4{,}99 \cdot 4 = 19{,}96$
statt 19,95) – zutreffend, nachgerechnet, von mir übersehen.
e2-k2-s1-v3 (Maßstab „1 LE = 1 cm“ fehlt, Kugel und Wassermenge in
cm) – zutreffend, übersehen; ohne Maßstab ist die Gleichung nicht
eindeutig. e2-k1-s0-v3 (Rotation um die y-Achse ist ein anderes
Merkmal als „Radius am Ort x als Funktionswert“) – zutreffend als
Merkmalsurteil; der Merkkasten der Einheit nennt die Achsprüfung
zwar, das merkmal der Zeile aber nicht. Wird v3 wie vorgeschlagen
auf die x-Achse umgestellt, entfällt zugleich meine Doppelung
$y = x^2$/Glas zwischen s0-v3 und s1-v3 – dann genügt es, s1-v3
stehen zu lassen.

Nur Zweitleser: e1-k1-s0-v3/-v4 (Achse im Text genannt, Ankreuzen
wird Ablesen); e1-k2-s1-v3 (Maßstab 1 LE = 2 cm mit Faktor 8 zum
dritten Mal, Fehlerbaustein doppelt mit e2-k1-s5-v2);
e1-k2-s3-v2 (alle drei Anwendungen „ja“); e2-k1-s0-v2/-v4 (richtige
Option stets zuerst); e2-k1-s1-v3 (gleiche Funktion und Gegenstand
wie s0-v3); e2-k1-s2-v2 (x doppelt belegt); e2-k1-s4-v1 (Ergebnis
6 cm / 12 cm × 12 cm wie das Original); e2-k2-s3-v3 (h nicht
eingeführt, Nachweis fehlt); zone-f4-v3 (Erde 0,8 t/m³ aus dem
Original). Der Erstleser hat Rechnung, Eindeutigkeit und Merkmal
geprüft und Verfremdung, Sperre im Sinn und Formmuster (Optionsfolge,
Ja/Nein-Verteilung) nicht angesehen; dort liegen meine Zusatzfunde.

Widersprüche: keine. Der Erstleser zählt 80 saubere Zeilen, ich 72;
der Unterschied sind die 11 Zeilen mit Befunden nur bei mir, abzüglich
der 3 nur bei ihm. Zusammen: 18 Zeilen mit mindestens einem Befund,
69 ohne.
