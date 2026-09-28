# Zweitlesung winkel-dreiecke

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 273
(zone 22, e1 50, e2 53, e3 56, e4 50, e5 42)

Prüfung: Jede Zeile gelesen (Aufgabe, Antwortgerüst, Lösung, pruef, Grafik, Lösungsgrafik). Die 159 Zeilen mit pruef-Zahl aus dem Aufgabentext selbst nachgerechnet; alle stimmen mit loesung und pruef überein, auch nach Rundung. Mit eigenem Skript (Python/sympy) nachgerechnet: alle Konstruktionen in e4 (SSS-, SWS-, WSW-, SsW-Kontrollwerte und Lösungsgrafik-Koordinaten von C, Hypotenusen), alle Umkreis- und Inkreismittelpunkte, Höhenfußpunkte, Schwerpunkte und Mittelpunkte in e5 samt Spitzwinkligkeit, dazu die Winkel der Grafiken in zone-f1-v4 (84,3° und 95,7° neben den beiden rechten Winkeln), e2-k2-s9-v2 (Trapez mit 73°/58°), e2-k2-s9-v3 (Deich 52°) und e3-k2-s0-v2 (stumpf, 108°). 47 Ankreuzzeilen Option für Option geprüft, auch auf Sonderfälle; 16 Fehler-finden-Zeilen: Jeder eingebaute Fehler ist falsch, und jede Richtigrechnung stimmt. `werkzeuge/bank-pruef.py winkel-dreiecke`: 0 Abweichungen, 0 Warnungen. Bemerkung ohne Zählung: Knapp über den 4 cm Freiraum der Grafik `\winkelstrahl` ragen außerdem e4-k1-s1-v1 (4,2 cm), e4-k1-s3-v1 (4,3 cm), e4-k1-s5-v3 (4,5 cm), e4-k1-s10-v3 (4,2 cm) und e5-k1-s7-v3 (Halbkreis 4,5 cm).

## Befunde

e3-k2-s0-v4: [A] Das Dreieck mit a = b = c = 5 cm ist gleichseitig und damit auch gleichschenklig (mindestens zwei gleich lange Seiten); zwei Optionen stimmen. – Option „gleichschenklig“ ersetzen, etwa durch „rechtwinklig“, oder fragen: „Welche Bezeichnung ist die genaueste?“

e3-k1-s0-v1, e3-k1-s0-v2, e3-k1-s0-v3, e3-k1-s0-v4: [E] „Fahre in einer Skizze das Dreieck nach“, aber es gibt keine Grafik; der Schüler müsste die Figur erst selbst zeichnen, der Erkennungsschritt verlangt aber das Nachfahren in einer Figur. – Grafik ergänzen (`\viereck[diagonalen]` für v3/v4, ein Dreieck mit eingezeichneter Höhe für v1/v2) oder den Auftrag in „Zeichne eine Skizze und fahre … nach“ ändern.

e4-k1-s1-v3, e4-k1-s1-v5, e4-k1-s2-v3, e4-k1-s3-v2, e4-k1-s3-v3, e4-k1-s4-v1, e4-k1-s4-v2, e4-k1-s4-v3, e4-k1-s5-v2, e4-k1-s6-v2, e4-k1-s10-v5: [E] Die Grafik `\winkelstrahl[9][…]` lässt über dem Strahl 4 cm frei; das fertige Dreieck ist aber 4,7 bis 8,0 cm hoch (C nach der Lösungsgrafik; s6-v2: Kathete mindestens 5 cm senkrecht; s2-v3 liegt C außerdem 1,55 cm links vom Scheitel A). Die Zeichnung passt nicht in den Platz der Grafik. – Seiten so wählen, dass C höchstens 4 cm über dem Strahl liegt, oder statt des Strahls ein leeres Koordinatensystem mit genug Höhe setzen.

e1-k4-s3-v3: [M] Minutenzeiger von 3:00 bis 3:20 Uhr ist ein Anteil am Vollwinkel (360° : 3); Merkmal und Sprosse verlangen Teilwinkel oder Teilstrecken mit Summe oder Differenz. – Durch einen Kontext mit Teilwinkeln ersetzen (etwa eine Schranke oder Tür, die sich um zwei Teildrehungen öffnet, gesucht der Rest bis 90° oder die Summe).

e5-k1-s8-v3: [M] Gezeigt wird mit der Umkehrung des Thales, dass die Ecken eines Rechtecks auf einem Kreis liegen; Sprosse und Merkmal verlangen, einen rechten Winkel mit Thales zu begründen. Die Umkehrung ist im Katalog Vorrat. – Durch eine Aufgabe ersetzen, in der ein rechter Winkel aus „C liegt auf dem Kreis über dem Durchmesser AB“ zu begründen ist.

e5-k1-s4-v2: [R] Genau liegt der Inkreismittelpunkt bei I(5 | 7/3); die Lösung schreibt „I(5|2,3)“ ohne ≈ (anders als e5-k1-s2-v3), der Radius 4/3 steht als „≈ 1,3“. – „I ≈ (5|2,3)“ schreiben, dazu der Hinweis auf den periodischen Wert, oder C so wählen, dass I ganzzahlig liegt.

Sauber: 254 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e3-k2-s0-v4: Das gleichseitige Dreieck ist auch gleichschenklig, damit sind zwei Optionen richtig.
- e1-k4-s3-v3: Die Uhr-Aufgabe verlangt einen Anteil am Vollwinkel, keine Summe oder Differenz von Teilwinkeln.
- e5-k1-s8-v3: Verlangt wird die Umkehrung des Thales (Vorrat), nicht die Begründung eines rechten Winkels.
- e5-k1-s4-v2: I = (5 | 7/3) ist periodisch und steht ohne ≈ und ohne Rundungshinweis (Erstleser unter „Eindeutig“, Zweitleser unter R).

Nur Erstleser:
- zone-f5-v4: bestätigt – die Zeichenfläche ist 6 Einheiten hoch (bei Karo 8 mm nur 4,8 cm), ein Kreis mit 9 cm Durchmesser passt nicht. Aus demselben Grund passt wohl auch der Kreis mit Radius 3 cm in zone-f5-v1 nicht (6 cm Durchmesser); das haben beide Leser übersehen.
- e2-k4-s3-v2: schwach bestätigt – die Strebe endet am oberen Boden, gemeint kann also nur der Winkel zwischen den Böden sein. Die Lösung spricht aber selbst vom Stufenwinkel oberhalb; die vorgeschlagene Schärfung schadet nicht.
- e5-k1-s2-v3: schwach bestätigt – die Lösung trägt zwar ≈, aber die Aufgabe nennt keine Genauigkeit, und U ist periodisch; aus der Konstruktion lässt sich ein Wert auf eine Dezimale kaum sicher ablesen.
- e2-k3-s1-v3: bestätigt – an h ist statt des Stufenwinkels sein Nebenwinkel gegeben, ein Zusatzschritt, den v1 und v2 nicht haben.
- e2-k4-s2-v2: bestätigt – „Nebenwinkel sind immer gleich groß“ zu widerlegen ist nicht die Sprosse „warum Scheitelwinkel gleich groß sind“.
- e3-k2-s4-v3: schwach bestätigt – die Frage nach zwei Winkeln zusammen ist ein kleiner Zusatzschritt; das Merkmal bleibt aber gleich.
- e3-k2-s7-v2: nicht bestätigt – die Zeile verfremdet das Original 2018-OS-K4b, das der Katalog dieser Sprosse zuordnet (Nebenwinkel vergessen, Teildreieck); Originale dürfen an jeder Höhe stehen, und ihre Schrittzahl gibt das Original vor.
- e3-k2-s8-v3: nicht bestätigt – das ist die Verfremdung von 2023-OS-K7a (Begründung über 45° und 45°), die zur Sprosse gehört; der Rechenschritt über die Winkelsumme steht auch im Original.
- e3-k2-s9-v3: bestätigt – γ = 90° folgt allein aus γ = α + β; gleiche Basiswinkel werden nicht gebraucht, das Merkmal wird verfehlt.
- e3-k3-s1-v3: schwach bestätigt – der gesuchte fünfte Winkel ist ein Zusatzschritt gegenüber v1 und v2; als Anwendung der Winkelsumme vertretbar.
- e4-k3-s2-v2: bestätigt – begründet wird, warum SWS reicht, nicht, warum drei Winkel nicht reichen.
- e4-k3-s2-v3: bestätigt – der SsW-Sonderfall ist eine andere Aussage als die Sprosse und deutlich schwerer.
- e4-k3-s3-v2: bestätigt – die zweiseitige Abschätzung mit der Differenz 8 − 5 ist im Eintrag nicht eingeführt; v1 und v3 prüfen nur ja oder nein.
- e5-k1-s4-v3: bestätigt – A(2|1), B(8|1), C(2|9) ist das Dreieck aus v1, um 1 nach rechts verschoben; der Sache nach doppelt.
- e5-k1-s5-v1: nicht bestätigt – die Sprosse heißt „Höhe im spitzwinkligen, dann im stumpfwinkligen Dreieck“ und nennt den spitzwinkligen Fall selbst; v1 deckt ihn ab, v2 und v3 den stumpfen.
- e5-k1-s7-v3: schwach bestätigt – die Kathete a als zusätzliche Vorgabe ist ein Schritt mehr als in v1 und v2.
- e5-k2-s2-v2: bestätigt – die Begründung stützt sich auf die Umkehrung des Thales (Vorrat) statt auf gleiche Abstände am Schnittpunkt besonderer Linien.
- e5-k2-s3-v3: bestätigt – A(2|2), B(8|2), C(4|6) ist das Dreieck aus e5-k1-s2-v1, um (1|1) verschoben; der Sache nach doppelt.
- e2-k2-s9-v2: nicht bestätigt – die Klammer mit dem Weg über 360° ist ein zusätzlicher Weg, den auch das Original 2021-OS-B1i nennt; sie schadet der Lösung nicht (höchstens eine Stilfrage).
- zone-f2-v5: Befund bestätigt, Vorschlag falsch – dass der Fehler nur am Endergebnis zu sehen ist, stimmt. Die vorgeschlagene Zwischenzeile „133,2°; 133,2° − 37,5° = 96,3°“ ist aber selbst falsch gerechnet (133,2 − 37,5 = 95,7). Zum Endwert 96,3° passt der Übertragsfehler 180° − 46,8° = 133,8°, dann 133,8° − 37,5° = 96,3°; so sollte die Rechnung auf dem Blatt stehen.

Nur Zweitleser:
- e3-k1-s0-v1 bis e3-k1-s0-v4: Aufgetragen ist, in einer Skizze nachzufahren, aber es gibt keine Grafik.
- e4-k1-s1-v3, s1-v5, s2-v3, s3-v2, s3-v3, s4-v1, s4-v2, s4-v3, s5-v2, s6-v2, s10-v5: Das fertige Dreieck ist höher als die 4 cm, die `\winkelstrahl` über dem Strahl freilässt; in s2-v3 liegt C zudem links vom Scheitel.

Widersprüche:
- e3-k2-s7-v2, e3-k2-s8-v3, e5-k1-s5-v1, e2-k2-s9-v2: Der Erstleser führt sie als Befund, der Zweitleser hält sie für richtig (Verfremdung eines Originals der Sprosse, Sprosse nennt den Fall selbst, bzw. zusätzlicher Weg).
- zone-f2-v5: Befund gleich gesehen, aber der Korrekturvorschlag des Erstlesers ist rechnerisch falsch.
