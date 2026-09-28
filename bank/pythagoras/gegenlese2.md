# Zweitlesung pythagoras

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 236
(zone 38, e1 65, e2 58, e3 75)

Prüfung: Jede Zeile gelesen. 145 Zeilen mit Zahlergebnis habe ich aus dem Aufgabentext unabhängig nachgerechnet (sympy, exakte Wurzeln aus Hypotenuse und Kathete, Überstände und Teilstrecken dazu), und zwar mit eigenen Formeln, nicht aus pruef. Die übrigen Zahlzeilen (Umkehrung, Tripel, Knotenschnur, Radius, Rechenweg mit Radius) habe ich im Kopf geprüft. Alle Ergebnisse und Rundungen stimmen mit loesung und pruef überein. Die 32 Ankreuzzeilen haben je genau eine richtige Option, und loesung nennt sie wortgleich. Bei den 10 Fehler-finden-Zeilen ist der eingebaute Fehler wirklich falsch und die Richtigrechnung stimmt. Für die Grafiken habe ich die Seitenverhältnisse von \dreieck, \dreieckrw, \trapez, \raute, \kegel, \pyramide, \quader und \zylinder gegen die Werte gerechnet, dazu die Winkel der \dreieck-Figuren und die ksys-Bereiche beim Kästchenzählen. `bank-pruef.py pythagoras`: 0 Abweichungen, 0 Warnungen.

## Befunde

e1-k1-s0-v2: [E] Die Winkelangaben 62°, 48° und 70° passen nicht zur Figur: gezeichnet sind etwa 62°, 43° und 75°. – C auf (1.67,3.14) setzen.

e1-k2-s2-v2: [E] Die Grafik passt nicht zu den Werten: AB : BC = 2,48 : 3,5 = 0,71, verlangt sind 33 : 56 = 0,59. – \dreieck{(0,0)}{(2.06,0)}{(2.06,3.5)}… mit sonst gleichen Argumenten.

e1-k2-s11-v2: [E] Der Stab liegt auf dem Boden einer Kiste und soll an einer Ecke 5 cm hinausragen. Bei einer Kiste mit Wänden geht das nicht. – Kontext ändern, z. B. Stab diagonal auf einer rechteckigen Tischplatte, der über die Ecke hinausragt.

e3-k2-s13-v1, e3-k2-s13-v2, e3-k2-s16-v1, e3-k2-s16-v2: [E] Die Grafik \zylinder zeigt nur den Zylinder ohne das Kegeldach, nach dem gefragt ist, und ist nicht nach den Werten skaliert. An ihr wird nichts abgelesen. – Grafik weglassen oder den Turm aus Zylinder und Kegel zeigen (dafür gibt es keinen Baustein; dann als Befund an die Vorlage).

e3-k2-s13-v3: [E] In \zylinder{1.25}{2.25} ist der Radius im Maßstab des Durchmessers gezeichnet: r : h = 0,56 statt 2,5 : 9 = 0,28. – \zylinder{0.63}{2.25}{}{}.

e3-k4-s4-v3: [E] \pyramide{4}{4}{1.5} zeigt die Höhe im Maßstab 1,5 : 4, das entspricht 0,9 m statt 0,5 m bei 2,4 m Grundkante. Das Stützdreieck erscheint damit fast doppelt so steil. – \pyramide{4}{4}{0.83}{…}.

Hinweise (keine Kennzeichen, nicht gezählt):
- Innerhalb einer Einheit kommt dieselbe Rechnung mehrfach vor. In e1 verrät die Vorstufe die Lösung späterer Zeilen, wenn beide auf einem Blatt stehen: e1-k2-s0-v1 (9, 40, 41) ↔ s1-v2 ↔ k5-s1-v3; s0-v2 (28, 45, 53) ↔ s2-v1; s0-v3 (11, 60, 61) ↔ s1-v4 ↔ s10-v1; s0-v4 (33, 56, 65) ↔ s2-v2 ↔ k5-s1-v1. Weitere Paare mit derselben Rechnung: e1-k2-s1-v5 ↔ s11-v2 (40, 42 → 58); e1-k2-s9-v1 ↔ k5-s1-v2 (24, 45 → 51); e1-k2-s9-v2 ↔ s10-v2 (1,2 und 3,5 → 3,7); e3-k2-s1-v2 ↔ s4-v2 (61, 11 → 60); e3-k2-s3-v1 ↔ s9-v1 (9, 40 → 41); e3-k2-s6-v2 ↔ s10-v1 (33, 56 → 65). Keine Aufgabe ist wortgleich doppelt, aber die Regel „keine Aufgabe doppelt“ ist dem Sinn nach berührt. Vorschlag: In den Vorstufen andere Tripel nehmen und in jeder Einheit jedes Tripel nur einmal.
- Bei den Anwendungszeilen passt der Sprossentext nicht ganz: e1-k5-s3 (Sprosse „mit gegebener Skizze“) hat keine Grafik, und e3-k4-s3-v1 und v3 (Sprosse „mit Überstand“) haben keinen Überstand. Das merkmal „echte Frage aus dem Alltag“ erfüllen alle.

Sauber: 227 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k2-s11-v2: Der Stab kann nicht aus einer Kiste mit Wänden hinausragen; der Vorschlag ist bei beiden die Tischplatte. e3-k2-s13-v1, s13-v2, s16-v1, s16-v2: Die Grafik zeigt nur den Zylinder ohne das Kegeldach. e3-k2-s13-v3: Die Grafik ist falsch skaliert, der Becher erscheint breiter als hoch; beide Korrekturvorschläge treffen das Verhältnis 2,5 : 9. Die Zahlwiederholungen in e1 (Vorstufe s0-v1 bis v4 gegen s1-v2, s1-v4, s2-v1, s2-v2; s1-v4 gegen s10-v1; s9-v2 gegen s10-v2; s1-v5 gegen s11-v2) haben beide gefunden. Der Erstleser führt sie als Merkmalsbefund, ich als Hinweis ohne Kennzeichen.

Nur Erstleser:
- zone-f3-v4: bestätigt. Der Text nennt nur einen Winkel mit 88°, damit ist ein rechter Winkel an einer anderen Ecke nicht ausgeschlossen, und die Lösung begründet nur für diesen einen Winkel. Das hatte ich übersehen.
- e1-k2-s12-v1 und e1-k2-s12-v2: bestätigt. Laut mathblatt.sty setzt \dreieckrw die Ecken A oben, B rechts und C unten links und beschriftet #3 an CB und #4 an CA. Damit trägt CB 39 m bzw. 47 m, der Text sagt aber BC = 14 m bzw. CB = 22 m. Ich hatte die Eckbuchstaben nicht geprüft; die Korrektur des Erstlesers stimmt.
- e2-k4-s3-v2: bestätigt. Aus der Bildschirmdiagonale und der Gerätebreite folgt keine Höhe; beide Maße gehören zu derselben Fläche.
- e3-k4-s4-v3 (pruef leer): nicht bestätigt als Fehler. Die Form ist zeichnen, und dafür erlaubt bank.md pruef "". Die Zahl 1,3 m stimmt; pruef 1.69**0.5 zu setzen wäre trotzdem eine sinnvolle Absicherung. Ich habe an derselben Zeile die Grafik bemängelt, nicht pruef.
- e1-k5-s4-v1: bestätigt, aber leicht. Die Sprosse verlangt eine Gleichung, die Aufgabe nur Skizze und H. Ich hatte das merkmal „zwischen Text, Skizze und Gleichung wechseln“ für erfüllt gehalten und die Zeile nicht aufgenommen.
- e3-k2-s4-v3: bestätigt als Zahlwiederholung (7,5 und 4,5 → 6 wie e2-k2-s4-v1), über zwei Einheiten hinweg. Bei mir fällt das unter den Hinweis, dort ist es aber nicht aufgeführt.
- e1-k2-s1-v4, e1-k2-s2-v1 (Wiederholung aus zone-f2-v5 und zone-f2-v6): bestätigt, nur Summe unter der Wurzel, mit geringem Gewicht.
- zone-f8-v3 (form ankreuzen ohne Optionen): nicht bestätigt. Die Zeile trägt im heutigen Stand form teil; der Befund ist erledigt oder betraf eine ältere Fassung.

Nur Zweitleser:
- e1-k1-s0-v2: Die Winkelangaben 62°, 48° und 70° passen nicht zur gezeichneten Figur (≈ 62°, 43°, 75°).
- e1-k2-s2-v2: Das Seitenverhältnis der Grafik passt nicht zu 33 : 56.
- e3-k4-s4-v3: Die Pyramide ist fast doppelt so hoch gezeichnet, wie es der Höhe von 0,5 m entspricht.
- Hinweise ohne Kennzeichen: die Zahlwiederholungen in e3 (s1-v2 gegen s4-v2, s3-v1 gegen s9-v1, s6-v2 gegen s10-v1), in e1 (s9-v1 gegen k5-s1-v2) und in e1-k5-s1-v1 und v3 gegen die Vorstufe; dazu die Sprossentexte der Anwendungszeilen e1-k5-s3 und e3-k4-s3.

Widersprüche: Keine in der Sache. Unterschiedlich sind nur die Einordnung (Zahlwiederholungen: Merkmal beim Erstleser, Hinweis ohne Kennzeichen bei mir) und der Stand: zone-f8-v3 widerspricht der heutigen Datei.
