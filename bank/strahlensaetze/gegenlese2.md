# Zweitlesung strahlensaetze

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 226
(zone 39, e1 82, e2 54, e3 51)

Prüfung: Jede Zeile gelesen (Aufgabe, Antwortgerüst, Lösung,
pruef, Grafik, Lösungsgrafik, sprosse_text, merkmal). Für alle 172
Zeilen mit pruef-Zahl habe ich das Ergebnis aus dem Aufgabentext
selbst angesetzt (sympy, exakte Brüche, Wurzel für die Hypotenusen
in e2 k1 s9) und mit pruef verglichen: 172 von 172 stimmen, auch
nach Rundung; die übrigen 54 Zeilen (Begründen, Zeichnen,
Ankreuzen ohne Zahl) von Hand geprüft. Zentren und Bildpunkte der
zentrischen Streckungen (e2 k1 s1–s3, k2) aus den \punkt-Koordinaten
nachgerechnet. 38 Ankreuzzeilen: jede hat genau eine richtige
Option, die loesung nennt sie wortgleich (Maßstab-passt-ins-Feld
in e1 k3 s0 mit allen drei Optionen gegen das Feld gerechnet). 10
Fehler-finden-Zeilen: der eingebaute Fehler ist in allen falsch und
in sich folgerichtig gerechnet, die Richtigrechnung stimmt.
Zusätzlich geprüft: Größe der Zeichenfelder (ksys-Karo 8 mm nach
Anleitung_mathblatt.md, also 1 Einheit = 0,8 cm) gegen die zu
zeichnenden Maße und die Längen in \strahlensatz{ZA}{ZA′} gegen
die Werte im Text. bank-pruef.py v0.5: 0 Abweichungen, 0
Warnungen.

## Befunde

zone-f5-v4: [E] Der Kreis mit d = 7 cm passt nicht ins
Zeichenfeld (ksys 9 × 6 Karo = 7,2 cm × 4,8 cm) – Feld größer
(ymax=10, xmax=10) oder kleineren Durchmesser wählen.

e1-k3-s4-v1, e1-k3-s4-v2, e1-k3-s4-v3: [E] Die Kreise mit
d = 6 cm, 7 cm und 5 cm passen nicht ins Zeichenfeld (ksys 10 × 6
Karo = 8 cm × 4,8 cm) – ymax auf 10 setzen (8 cm hoch).

e1-k3-s6-v1, e1-k3-s6-v2: [E] Das Quadrat mit 6 cm und das
Rechteck 8 cm × 5 cm passen nicht ins Zeichenfeld (8 cm × 4,8 cm)
– Feld auf etwa xmax=12, ymax=9 vergrößern.

e1-k3-s7-v1, e1-k3-s7-v2, e1-k3-s7-v3: [E] Der Text nennt ein
Zeichenfeld von 15 cm × 9 cm, die Grafik ist aber 8 cm × 4,8 cm
(ksys 10 × 6); die Musterlösungen 10 × 5 und 14 × 8 cm passen
nicht in die Grafik, 8 × 4 cm nur randgenau, und der Schüler wählt den Maßstab nach
einem Feld, das es nicht gibt – Grafik auf etwa xmax=19, ymax=11
(15,2 cm × 8,8 cm) und die Maße im Text auf die Grafik abstimmen.

e1-k3-s3-v2, e1-k3-s3-v3: [E] Das Pronomen passt nicht zum Nomen:
„Ein Balkon … Zeichne es“, „Eine Garage … Zeichne es“ – „Zeichne
ihn“ bzw. „Zeichne sie“.

e1-k3-s4-v3: [E] Das Pronomen passt nicht zum Nomen: „Ein rundes
Beet … Zeichne ihn“ – „Zeichne es“ (zusätzlich zum Feldbefund
oben).

e3-k1-s1-v2, e3-k1-s1-v3, e3-k1-s1-v4, e3-k1-s1-v5: [E] Die Grafik
\strahlensatz{ZA}{ZA′} passt nicht zu den Werten im Text (v2 2 : 7
statt 2 : 8, v3 und v4 3 : 7 statt 1 : 3, v5 3 : 7 statt 1 : 4),
und der Text sagt nicht, dass die Figur nicht maßstabsgerecht ist;
wer nachmisst, findet einen anderen Faktor – Grafik proportional
setzen (v2 {2}{8}, v3 {2}{6}, v4 {2}{6}, v5 {1.75}{7}) oder
„(nicht maßstabsgerecht)“ ergänzen.

e3-k3-s1-v3: [E] Die Strecke von 11 cm passt nicht ins
Zeichenfeld (ksys 12 × 6 Karo = 9,6 cm breit) – xmax=15 oder eine
kürzere Strecke.

e3-k4-s3-v3: [E] „Der Schatten fällt auf eine Wand 2 m hinter der
Lampe“: hinter der Lampe liegt die Wand auf der falschen Seite,
dort fällt kein Schatten der Figur hin; die Lösung rechnet mit
2 m Abstand Lampe–Wand auf der Seite der Figur – „auf eine Wand,
die 2 m von der Lampe entfernt hinter der Figur steht“.

Sauber: 209 Zeilen ohne Befund

## Abgleich

Beide Leser: zone-f5-v4, e1-k3-s4-v1 bis v3 und e1-k3-s6-v1, v2 –
die verlangte Zeichnung passt nicht ins Zeichenfeld (Karo 8 mm).
e1-k3-s7-v1 bis v3 – Feldmaße im Text (15 cm × 9 cm) und Grafik
(8 cm × 4,8 cm) widersprechen sich. e3-k1-s1-v2 bis v5 – das
Verhältnis ZA′ : ZA der Grafik weicht vom Text ab. e3-k3-s1-v3 –
die 11-cm-Strecke passt nicht ins Feld. e3-k4-s3-v3 – „Wand 2 m
hinter der Lampe“ liegt auf der falschen Seite.

Nur Erstleser:
e3-k1-s8-v2 und e3-k2-s1-v2 („In einer V-Figur“, Antwort „nicht
parallel“ bzw. „nein“): bestätigt, aber weich – nach dem Merkkasten
gehören die Parallelen zur V-Figur, die Frage setzt also voraus,
was sie prüfen soll; „zwei Geraden schneiden sich in Z“ ist sauberer.
e3-k3-s1-v1 (7 : 3 periodisch ohne Hinweis in der Aufgabe):
bestätigt – der Hinweis steht nur in der Lösung, bank.md verlangt
ihn an der Aufgabe; von mir übersehen.
e3-k4-s2-v2 (gemeinsames Schattenende nicht in der Aufgabe):
teilweise bestätigt – die Aufgabe ist lösbar, aber der Lösungskern
sollte die parallelen Sonnenstrahlen nennen, wie es der
Katalogtext dieser Pflicht tut.
e1-k1-s0-v1 und e1-k1-s0-v3 (Einkreisen der umzurechnenden Einheit
fehlt): bestätigt – die Sprosse verlangt es, die Aufgabe nicht.
e2-k1-s5-v3 (drei Seitenverhältnisse statt Eigenschaft prüfen):
bestätigt – die Variante verlangt die Rechnung von s7 und ändert
damit mehr als das Merkmal ihrer Sprosse.
e3-k1-s2-v3, e3-k1-s3-v2, e3-k1-s3-v3 (Dezimalzahlen vor s4):
bestätigt – s4 führt Dezimalzahlen als Merkmal ein, die drei
Varianten nehmen es vorweg.
e1-k3-s0-v1 bis v4 („Welcher Maßstab passt?“, der winzige Maßstab
passt auch ins Feld): bestätigt – der Katalog meint „passend“
gegen „winzig“, das Wort „passt“ trennt das nicht; von mir
übersehen.
e3-k1-s0-v3 und e3-k1-s0-v4 (Lösung am Namen ablesbar): nicht
bestätigt – genau eine Option ist richtig, und am Namen zu sehen,
dass eine Strecke bei Z beginnt, ist der Handgriff der Vorstufe
(„nichts rechnen“); allenfalls eine Anregung für die Form.
e3-k4-s1-v1 (gleicher Fehler wie v2): nicht bestätigt – Jan
ersetzt ZA′ durch AA′ (Abschnitt nicht vom Zentrum), Mia mischt
AA′ mit ZA′ neben der Parallelen; das sind die zwei getrennt
genannten Muster aus „Typische Fehler“.
e3-k4-s1-v2 (Zahlen wie e3-k1-s2-v2: 3, 5, 6 → 10 cm): bestätigt
– über AA′ = 2 dieselbe Rechnung mit demselben Ergebnis; auf einem
Blatt verrät die eine Zeile die andere.
e3-k4-s1-v3 (Zahlen wie e3-k1-s1-v2: 2, 8, 5 → 20 cm; Lösungssatz
„ZB′ wird mit 5 malgenommen“ unklar): bestätigt, beides.

Nur Zweitleser: e1-k3-s3-v2, e1-k3-s3-v3 und e1-k3-s4-v3 – das
Pronomen passt nicht zum Nomen („Balkon … es“, „Garage … es“,
„Beet … ihn“).

Widersprüche: keine; nur bei e1-k3-s7-v2 ist die Musterlösung
8 cm × 4 cm randgenau im Feld 8 cm × 4,8 cm (Erstleser genauer,
oben angeglichen), der Befund bleibt wegen des Widerspruchs zum
Text.
