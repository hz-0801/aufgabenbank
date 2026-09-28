# Zweitlesung extremalprobleme

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 134 (zone 26, e1 31,
e2 34, e3 43)

Prüfung: Jede Rechen- und Nachweiszeile mit sympy nachgerechnet
(Skript nachrechnen.py im Scratchpad): Funktionswerte, Terme
ausmultipliziert, Ableitungen, Nullstellen, zweite Ableitungen,
Substitutionen, Rand- und Extremwerte, bei den Trapezen zusätzlich
die Symmetrie f(B − u) = f(u) und die Mittelparallele, bei den
ksys-Grafiken die Lage der Lösungspunkte im Achsenbereich. Alle
Werte stimmen mit loesung und pruef überein, auch die gerundeten
(P(3 | 1,34), √13 ≈ 3,61, r ≈ 5,42). Begründen- und Textzeilen
inhaltlich gelesen; die 22 Originale in Abschnitt 2 der Mappe
gegen Zahlen, Form und Kontext der verfremdeten Zeilen gehalten.
`python3 werkzeuge/bank-pruef.py extremalprobleme`: Abweichungen 0,
Warnungen 0 (je Datei 0/0). Ankreuzen-Zeilen geprüft: 12 (je vier
in e1, e2, e3), in jeder genau eine Option richtig und in loesung
wortgleich. Fehler-finden-Zeilen geprüft: 10 (zone 1, e1 3, e2 3,
e3 3), jeder eingebaute Fehler ist wirklich falsch, jede
Korrekturrechnung richtig. Rundung auf zwei Dezimalen steht
nirgends im Text, ist aber die durchgehende Konvention der Bank –
nicht als Befund gezählt.

## Befunde

e2-k1-s3-v1, e2-k1-s3-v2, e2-k1-s3-v3: Vorlagentext nicht
ausgefüllt und Grammatik – „Für ein rechteckiger Spielplatz an
einem Bach stehen für die drei Seiten ohne Bach, Mauer oder Stall
70 m Zaun …", ebenso „Parkplatz an einer Mauer … ohne Bach, Mauer
oder Stall" und „Pferch an einem Stall … ohne Bach, Mauer oder
Stall"; auch „senkrecht dazu" hat keinen Bezug – je Variante nur
das eigene Hindernis nennen: „Für einen rechteckigen Spielplatz am
Bach stehen für die drei Seiten ohne Bachufer 70 m Zaun zur
Verfügung, die vollständig verwendet werden; a ist die Seite
senkrecht zum Bach, b die Seite parallel dazu." (v2 mit Mauer, v3
mit Stall).

e1-k1-s0-v4: „wenn sich die Stelle u ändert" – u ist im Text
nicht erklärt, C und D haben keine Koordinaten – „die Ecken C und
D auf dem Graphen an den Stellen u und −u" schreiben.

e3-k1-s2-v3: die Lösung sagt „x = 2 (im Bereich)", die Aufgabe
nennt keinen Bereich; die zweite Lösung x = −2 muss der Schüler
selbst verwerfen – „0 < x < √12" (oder „x > 0") in den
Aufgabentext.

e3-k1-s5-v1: gleicher Kontext wie das Original 2018-be-gk-B1.1g
(Skispringer, Flugbahn, Aufsprunghang), bank.md verlangt beim
Verfremden „anderer Kontext" – Kontext tauschen, etwa Drohne über
einem Hang, Wasserstrahl einer Fontäne über einer Rampe oder
Brückenbogen über einem Tal; Zahlen können bleiben.

zone-f2-v4, e1-k2-s3-v1: dieselbe Aufgabe mit anderen Worten –
f(x) = 8 − x², Rechteck mit Ecke (2 | f(2)), Höhe 4, Fläche 8, auf
Blatt 0 und Blatt 1; ebenso zone-f5-v4, e3-k1-s8-v4: dieselbe
Substitutionsgleichung x⁴ − 3x² − 4 = 0 (z = 4, z = −1, x = ±2) als
Fallstrick auf Blatt 0 und als A'(x) = 0 auf Prüfungshöhe; ebenso
e1-k2-s1-v2, e2-k1-s4-v2: dieselbe Figur an f(x) = 9 − x² mit
demselben Zielterm 18x − 2x³, einmal als Korrektur der
Fehler-finden-Zeile, einmal als Nachweis – je ein Glied auf andere
Zahlen setzen, etwa zone-f2-v4 auf f(x) = 7 − x² mit Stelle 2
(Höhe 3, Fläche 6), zone-f5-v4 auf x⁴ − 8x² − 9 = 0 (z = 9, z = −1,
x = ±3), e2-k1-s4-v2 auf f(x) = 25 − x², 0 < x < 5, Nachweis
A(x) = 50x − 2x³. Die Wiederkehr von 4 − x² (fünfmal) und 9 − x²
(sechsmal) über die Blätter ist kein Verstoß, aber eintönig.

Sauber: 122 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k1-s0-v4 (u unerklärt); e2-k1-s3-v1, e2-k1-s3-v2,
e2-k1-s3-v3 (Schablonenrest „ohne Bach, Mauer oder Stall",
Grammatik).
Nur Zweitleser: e3-k1-s2-v3 (Definitionsbereich fehlt im Text);
e3-k1-s5-v1 (gleicher Kontext wie das Original, Skisprung);
zone-f2-v4 / e1-k2-s3-v1, zone-f5-v4 / e3-k1-s8-v4, e1-k2-s1-v2 /
e2-k1-s4-v2 (Zahlendoppel über Blätter hinweg).
Nur Erstleser: e3-k2-s1-v2 („dort ist d² maximal" gilt nur lokal)
– richtig, übersehen, d² wächst für große |x| unbeschränkt,
„lokales Maximum" genügt. e1-k1-s5-v1, e1-k1-s5-v2 (A für Punkt
A_k und Flächeninhalt A(u)) – richtig, übersehen, bank.md verlangt
einen Buchstaben je Sache; P_k, Q_k ist der kleinere Eingriff.
e3-k1-s6-v2 (Gerüst „u = __" ohne den gefragten Inhalt) – richtig,
übersehen, „u = __, T = __". e2-k1-s1-v3 (Nebenbedingung steht
schon umgestellt, Merkmal fällt weg) – richtig, übersehen; ich
hatte es als zulässige Variante gelesen, aber die Regel „Varianten
ändern nur Zahlen und Kontext" greift, 2x + y = 6 heilt es.
e1-k2-s2-v2 (Zerlegung des Trapezes ohne Schnittlinie) – im Kern
richtig, die Schnittlinie fehlt; der vorgeschlagene Satz ist aber
zu lang für „Kern in einem Satz", ein Halbsatz „längs der
Senkrechten durch die Schenkelmitte" genügt. e3-k3-s3-v2,
e3-k3-s3-v3 (Minimum nicht nachgewiesen) – richtig, übersehen;
v1 derselben Sprosse führt V'', die Lösungsdatei sollte in allen
drei gleich verfahren. e2-k1-s0-v4 (Distraktor „nach A" schwach)
– nicht geteilt: eine offensichtlich falsche Option stört auf einer
Vorstufe niemanden, und „nach 2y" wäre selbst keine übliche
Umstellung; kein Befund im Sinn des Auftrags.
Widerspruch: keiner (der Erstleser zählt neun Fehler-finden-Zeilen,
ich zehn mit zone-f1-v5; das ist Zählung, kein Urteil).
