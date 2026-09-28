# Zweitlesung ableitungsregeln

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 138 (zone 30, e1 47,
e2 29, e3 32)

Prüfung: Jede Rechenlösung mit sympy nachgerechnet (Skript
nachrechnen.py im Scratchpad: alle Ableitungen bis f''', alle
Stammfunktionen, Faktorisierungen, Grenzwerte, Punktproben,
Ableitungswerte an Stellen, die Verschiebungen d = n/k · ln k, die
Sinus-Ableitungen bis zur 102., die Graphenwerte der sechs
ksys-Aufgaben) – kein Rechenfehler. Die sechs Grafiken mit pdflatex
und mathblatt.sty gerendert und angesehen. Alle Originale aus
Abschnitt 2 der Mappe gegen die verfremdeten Zeilen gehalten:
überall andere Zahlen bei gleicher Form und Falle.
`python3 werkzeuge/bank-pruef.py ableitungsregeln`:
„Abweichungen: 0, Warnungen: 0". Geprüft: 16 Ankreuzen-Zeilen
(je genau eine richtige Option, Lösung wortgleich), 10
Fehler-finden-Zeilen (zone 1, e1 3, e2 3, e3 3; jeder eingebaute
Fehler ist falsch, jede angegebene Rechnung richtig).

## Befunde

zone-f7-v4: Die Frage „Streckung oder Verschiebung?" lässt
„Streckung" als richtige Antwort zu (der Graph ist auch eine
Streckung in y-Richtung), die Lösung verlangt „Beides" – Vorschlag:
„Um wie viel ist der Graph von $y = e^x$ dabei in $x$-Richtung
verschoben?" (Lösung „3 nach links", pruef 3 bleibt).

e3-k1-s5-v1, e3-k1-s5-v2, e3-k1-s5-v3: „folgere daraus etwas über
die Krümmung des Graphen" – „etwas" ist kein Operator, ein Schüler
weiß nicht, was verlangt ist (Vorzeichen? Wendestelle?) –
Vorschlag: „Was folgt daraus für die Krümmung des Graphen?
Begründe." (Lösung unverändert).

e1-k2-s6-v3: Merkmal ist „ableiten und ausklammern"; v3 klammert
nicht aus, sondern faktorisiert mit der dritten binomischen Formel
(der Handgriff von Sprosse 8) und bringt mit $c^2$ statt $c$ einen
zweiten Twist – Vorschlag: $h_c(x) = x^5 - c \cdot x^3$, Nachweis
$h_c'(x) = x^2 \cdot (5x^2 - 3c)$ (pruef 5).

e2-k1-s5-v1: Gerendert sind f und g zwei nach oben geöffnete
Parabeln, die sich in $(0|-1)$ schneiden und rechts oben dicht
nebeneinander aus dem Fenster laufen; die Beschriftungen f und g
liegen dort übereinander, ein Schüler kann die Graphen nicht
zuordnen – Vorschlag: f nach unten öffnen,
`\funktion{-0.5*\x^2+3}{f}` (f(2) = 1 bleibt, Lösung und pruef
unverändert; f und g trennen sich dann sichtbar wie in v2).

zone-f5-v1: `\tangentean` ohne Stern zeichnet ein Steigungsdreieck
mit den Zahlen 1 und 1 (am Rendering geprüft) – die gesuchte
Steigung steht damit in der Grafik – Vorschlag: `\tangentean*`,
die Tangente läuft durch die Gitterpunkte $(1|0)$ und $(2|1)$,
Ablesen bleibt Blatt-0-leicht. Ermessen: wer das beschriftete
Dreieck auf Blatt 0 als Hilfe will, lässt es.

e1-k2-s9-v1, e1-k2-s9-v2, e1-k2-s9-v3, e1-k2-s9-v4, e1-k3-s1-v1,
e1-k3-s1-v2, e1-k3-s1-v3: Das antwort-Gerüst trägt nur die drei
Ableitungen, die Lösung hat einen zweiten Teil ohne Platz auf dem
Blatt (Punktprobe und Extrempunkt, Anstiegsvergleich,
Grenzverhalten) – Vorschlag: Gerüst ergänzen um „P auf dem Graphen:
☐ ja ☐ nein, Extrempunkt: ☐ ja ☐ nein" (s9-v1, v2), „größerer
Anstieg bei x = __" (s9-v3, v4), „x → +∞: __, x → −∞: __"
(k3-s1-v1 bis v3).

e2-k3-s1-v3, e2-k3-s2-v1, e2-k3-s2-v2: Dieselbe Funktion steht in
einer Grundfall- und einer Pflichtzeile derselben Einheit –
$e^{5x}$ in k1-s1-v1 und k3-s1-v3, $e^{4x}$ in k1-s4-v1 und
k3-s2-v1, $e^{-2x}$ in k1-s1-v2 und k3-s2-v2; kommen beide auf ein
Blatt, steht die Lösung der Pflichtzeile schon im Grundfall –
Vorschlag: k3-s1-v3 auf $e^{9x}$, k3-s2-v1 auf $e^{10x}$, k3-s2-v2
auf $e^{-9x}$ (alle drei weder im Kasten noch sonst im Eintrag).

e2-k3-s1-v3: Die Fehlerbenennung „als wäre der Exponent ein
Vorfaktor" trifft Kims Rechnung $5x \cdot e^{5x - 1}$ nicht (sie
ist die Potenzregel auf $e^{5x}$) – Vorschlag: „Kim hat die
Potenzregel angewendet (Exponent nach vorn, um eins gesenkt); bei
$e^{kx}$ bleibt der Exponent stehen, es kommt der Faktor $k$ dazu;
richtig: …".

e2-k2-s1-v1, e2-k2-s1-v2, e2-k2-s1-v3: Der Hinweis „Es gilt
sin' = cos und cos' = −sin" steht hinter der Prüfkennung, die das
Ende des Fragesatzes markieren soll – Vorschlag: Hinweis vor die
Frage ziehen („Es gilt … . $f(x) = \mathrm{sin}(2x)$ – Term der
fünften Ableitung? (Abitur 2017 LK)").

Sauber: 118 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k3-s1-v3 (Fehlerbenennung „als wäre der Exponent
ein Vorfaktor" trifft Kims Rechnung nicht; beide schlagen die
Benennung als Potenzregel auf $e^{5x}$ vor).
Nur Zweitleser: zone-f7-v4 (Frage lässt „Streckung" zu);
e3-k1-s5-v1 bis v3 („folgere etwas" ohne Operator); e1-k2-s6-v3
(binomische Formel statt Ausklammern, $c^2$); e2-k1-s5-v1
(Beschriftungen f und g liegen übereinander, am Rendering
geprüft); zone-f5-v1 (Steigungsdreieck zeigt die Antwort);
e1-k2-s9-v1 bis v4 und e1-k3-s1-v1 bis v3 (antwort-Gerüst ohne
den zweiten Teil); e2-k3-s1-v3, e2-k3-s2-v1, e2-k3-s2-v2 (gleiche
Funktion wie eine Grundfallzeile); e2-k2-s1-v1 bis v3 (Hinweis
hinter der Prüfkennung).
Nur Erstleser: e3-k2-s2-v3 (f, g, a nicht eingeführt) – richtig
nach der Buchstabenregel von bank.md, übersehen; zum Lösen reicht
zwar die gegebene Gleichung, der vorgeschlagene Vorsatz kostet
aber nichts. e1-k2-s9-v2 (Tiefpunkt braucht das f''-Kriterium) –
richtig, übersehen; ich hatte die Variante mit $f'(2) = 0$ als
Gegenstück zu v1 gutgeheißen, der f''-Schritt liegt aber außerhalb
der Sprosse; der zweite Vorschlag des Erstlesers (nur fragen, ob P
als Extrempunkt in Frage kommt) hält die Variante. e2-k1-s4-v3
(f aus f' und f(1) rekonstruieren) – nicht geteilt: genau diese
Form (f' und ein Funktionswert gegeben) ist die des Originals
2024MerhoehtAAnalysis23, das der Sprossentext nennt; v1/v2 sind
die vereinfachten Varianten, v3 die Verfremdung; die Rekonstruktion
ist ein Ablesen ($f' = 6e^{6x}$, $f(1) = e^6$), kein eigener
Handgriff. e3-k1-s3-v3 (Extrempunkt zusätzlich) – nicht geteilt:
der Sprossentext nennt das Original ausdrücklich „mit
anschließendem Extrempunkt", die Variante folgt ihm; allenfalls
das Merkmal um „oder mit anschließendem Extrempunkt" ergänzen.
Widerspruch: e2-k1-s4-v3 – der Erstleser sieht in der
Rekonstruktion von f einen Schritt außerhalb von Merkmal und
Kette, der Zweitleser die vom Sprossentext genannte Form des
Originals. e3-k1-s3-v3 – der Erstleser hält den Extrempunkt für
einen Zusatz gegenüber Merkmal und v1/v2, der Zweitleser für den
im Sprossentext genannten Anschluss des Originals.
