# Zweitlesung potenz-exponentialfunktionen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 464
(e1 95, e2 74, e3 79, e4 43, e5 111, zone 62) · Stand: Commit 6ef64d5

Prüfung: Jede Zeile gelesen; jedes Zahlenergebnis aus dem Aufgabentext
eigens nachgerechnet (Python/sympy, unabhängig vom Feld pruef), dazu
eindeutige Lösbarkeit, Passung zu sprosse_text und merkmal, genau eine
richtige Option beim Ankreuzen, echter Fehler bei Fehler finden.
werkzeuge/bank-pruef.py meldet 0 Abweichungen, 0 Warnungen; die Befunde
unten liegen außerhalb dessen, was das Skript prüft (es vergleicht pruef
mit loesung, nicht mit der Aufgabe).

Befunde: 39 Zeilen, davon 6 rechnerisch [R].

## Befunde

zone-f4-v4: Fallstrick „erst am Ende runden“ läuft ins Leere, weil 7,25·1,4 = 10,15 exakt ist und nichts zu runden ist; ≈ steht vor einem exakten Wert – Zahlen wählen, die Rundung erfordern (z. B. 7,25 € · 1,37 = 9,9325 ≈ 9,93 €).
zone-f7-v2: Verlangt Bruch und Zahl, das Antwortfeld hat nur eine Lücke – Antwortfeld auf „__ = __“ erweitern oder „als Bruch“ streichen.
zone-f8-v3: „runde auf zwei Stellen“ ist mehrdeutig (Nachkommastellen oder gültige Ziffern: 2,07 oder 2,1) – „auf zwei Nachkommastellen“ schreiben.
zone-f8-v4: „runde auf zwei Stellen“ ist mehrdeutig (1,63 oder 1,6) – „auf zwei Nachkommastellen“ schreiben.
e1-k2-s6-v1: Graph h (500·1,2^t) überschreitet ymax 600 bereits bei t=1, ist also fast nur ein Stummel am Rand (oder wird über den Rahmen hinaus gezeichnet) – h mit kleinerem Faktor oder größerem ymax.
e1-k2-s6-v2: Grafik beschriftet die Zeitachse mit „t in Jahren“, die Aufgabe spricht von Minuten; außerdem verlässt h (60·1,1^t) das Fenster bei t≈5,4 (ymax 100) – xlabel auf „t in min“, ylabel „Temperaturdifferenz“, ymax anheben oder h flacher wählen.
e1-k2-s6-v3: Grafik beschriftet die Zeitachse mit „t in Jahren“, die Aufgabe spricht von Wochen; h (400·1,15^t) verlässt das Fenster schon bei t≈2,9 – xlabel auf „t in Wochen“ ändern, h so wählen, dass er im Fenster bleibt.
e1-k2-s7-v1: f (80·1,025^t) und die Gerade g (1,6t+80) liegen bis t=10 höchstens 6,4 auseinander, die Krümmung von f ist im Bild praktisch nicht zu sehen, „Kurve oder Gerade“ ist so kaum entscheidbar – g deutlich anders legen (z. B. Steigung 1) oder höheren Prozentsatz/längeren Zeitraum wählen.
e1-k2-s7-v2: dasselbe Problem: u (40·1,03^t) und v (1,2t+40) weichen bis t=10 nur um 1,8 ab, die Krümmung ist nicht erkennbar – v anders legen oder Zeitraum/Prozentsatz vergrößern.
e1-k3-s5-v3: [R] Tabellenwert für 6 km passt nicht zu 12 % Abnahme: 800·0,88^6 = 371,5, gerundet 372, nicht 371 – Tabellenwert auf 372 setzen.
e1-k4-s3-v1: Graph f (100·1,3^t) verlässt das Fenster ymax 400 ab t≈5,3 bei xmax 6 – ymax auf 500 anheben oder xmax 5.
e2-k2-s1-v1: Ergebnis 287,5 Mitglieder ist als Anzahl unsinnig – Startwert so wählen, dass eine ganze Zahl entsteht (z. B. 260 · 1,15 = 299) oder Größe ohne Stückzahl wählen.
e2-k2-s1-v4: Grammatikfehler „Die Guthaben in Euro ist“ – „Das Guthaben in Euro ist“.
e2-k2-s2-v2: Tabelle zeigt 187,5 Frösche – Zahlen so wählen, dass ganze Tiere entstehen (z. B. Start 128: 160; 200).
e2-k2-s7-v2: „drei Stellen“ ist mehrdeutig (Nachkommastellen oder gültige Ziffern: 2,28 hat nur zwei Nachkommastellen, 2,166 vier Ziffern) – „auf drei Nachkommastellen runden“ schreiben.
e2-k2-s8-v2: [R] 254,62 · 1,03 ≈ 262,26 geht vom gerundeten Wert aus, exakt ist 240 · 1,03³ ≈ 262,25 – beide Werte als richtig zulassen oder die Rechenvorschrift (vom Tabellenwert aus) in der Aufgabe nennen.
e2-k2-s8-v9: [R] Wert bei 6 km: 545 · 0,88³ ≈ 371 rechnet mit dem gerundeten Tabellenwert, exakt ist 800 · 0,88⁶ ≈ 371,52, also 372 – Lösung auf 372 setzen oder in der Aufgabe vorgeben, vom gerundeten Tabellenwert aus weiterzurechnen.
e2-k3-s1-v1: pruef [500,530,561.8] enthält mit 530 zufällig einen von Paul übernommenen Wert und lässt den vierten richtigen Wert 595,51 aus – pruef auf [500,530,561.8,595.51] vervollständigen.
e2-k3-s1-v3: [R] pruef enthält 840, den eingebauten falschen Wert, statt der richtigen Antwort 800 (in allen anderen Fehler-finden-Zeilen trägt pruef den richtigen Wert) – pruef auf 800 setzen.
e2-k3-s3-v2: sprosse_text nennt „Zerfall mit Faktor kleiner eins“, die Aufgabe ist ein Wachstum um 2 % – sprosse_text allgemein fassen (Wachstum oder Zerfall) oder Aufgabe auf Abnahme umstellen.
e2-k3-s3-v3: sprosse_text nennt „Zerfall mit Faktor kleiner eins“, die Aufgabe ist ein Wachstum um 30 % – wie bei k3-s3-v2 angleichen.
e3-k1-s5-v1: Die Aufgabe nennt keine Zeiteinheit für t, die Lösung setzt „Jahre“ voraus – „($t$ in Jahren)“ ergänzen.
e3-k1-s5-v2: Die Aufgabe nennt keine Einheit der Masse, die Lösung sagt „in mg“ – Einheit in der Aufgabe angeben („$m$ in mg“).
e3-k1-s5-v3: Die Aufgabe nennt keine Einheit der Höhe, die Lösung sagt „in cm“ – „$h$ in cm“ in der Aufgabe ergänzen.
e3-k2-s0-v1: „runde auf vier Stellen“ ist mehrdeutig (gültige Ziffern ergäben $1{,}217$) – „auf vier Nachkommastellen“ schreiben.
e3-k2-s0-v3: „runde auf zwei Stellen“ ist mehrdeutig (gültige Ziffern ergäben $41$) – „auf zwei Nachkommastellen“ schreiben.
e3-k2-s0-v4: „runde auf vier Stellen“ ist mehrdeutig (gültige Ziffern ergäben $1{,}218$) – „auf vier Nachkommastellen“ schreiben.
e3-k3-s3-v1: sprosse_text („Bestandteile einer gegebenen Gleichung deuten“) passt nicht zu merkmal und Aufgabe (Tabelle einer Gleichung zuordnen) – sprosse_text auf den Darstellungswechsel Tabelle/Gleichung/Text anpassen.
e3-k3-s3-v2: sprosse_text („Bestandteile … deuten“) passt nicht zur Aufgabe (Wertetabelle zu einer Gleichung anlegen) – sprosse_text wie bei k3-s3-v1 anpassen.
e3-k3-s3-v3: sprosse_text passt nur teilweise (verlangt ist ein Sachtext zur Gleichung, also ein Darstellungswechsel) – sprosse_text wie bei k3-s3-v1 anpassen.
e3-k3-s4-v1: sprosse_text verlangt einen Schwellenzeitpunkt durch schrittweises Multiplizieren, die Aufgabe fragt nur den Wert nach 2 Jahren ab – sprosse_text allgemeiner fassen (Anwendung modellieren) oder Aufgabe auf Schwellenzeitpunkt umbauen.
e3-k3-s4-v3: sprosse_text verlangt einen Schwellenzeitpunkt, die Aufgabe fragt den Wert nach 15 Jahren ab – wie bei k3-s4-v1 angleichen.
e4-k2-s1-v1: Leons Schluss von 130 nach 2 Jahren auf Verdopplungszeit 4 Jahre ist mit „doppelte Zeit, doppelter Wert“ nicht nachvollziehbar (er verdoppelt weder Bestand noch Zeit erkennbar), der eingebaute Fehler passt daher nicht klar zur Lösung „Zeit statt Bestand verdoppelt“ – Aussage eindeutig machen, z. B. „Nach 2 Jahren sind es 130, also nach 4 Jahren 160 – die Verdopplung dauert also 6,7 Jahre“ oder „der Bestand verdoppelt sich, wenn sich die Zeit verdoppelt“.
e4-k2-s1-v3: Der Fehler (Hälfte falsch eingeschätzt, Halbwertszeit liegt außerhalb der Tabelle) ist keiner der beiden im merkmal genannten Fehlertypen (Zeit statt Bestand, Achsen vertauscht) – Fehler auf „Zeit halbiert statt Menge“ umbauen oder merkmal erweitern.
e4-k2-s3-v3: [R] Gefragt ist, wann erstmals weniger als 10 mg übrig sind; bei stetigem Zerfall ist das schon nach etwa 26,1 Tagen (96·0,5^(t/8) < 10), nicht erst nach 32 Tagen – Frage auf „nach wie vielen ganzen Halbwertszeiten“ umstellen oder Lösung auf ≈ 26 Tage ändern.
e5-k1-s4-v2: Aufgabe verlangt, die Schrittweite der senkrechten Achse selbst zu wählen und zu beschriften, die Grafik gibt aber ystep=2 schon vor – entweder Achse unbeschriftet lassen oder Aufforderung streichen.
e5-k1-s11-v3: Im Bild ist g der Graph von x³, nicht von 2x³ (bei x = 1 ablesbar 1 statt 2), streng genommen passt also keiner; zudem heißt die Funktion h, im Bild ist h aber der Graph von x⁴ – Frage umformulieren („welcher Graph hat dieselbe Form/Symmetrie wie h“) oder Graph 2x³ ins Bild und die Funktion umbenennen (z. B. p).
e5-k2-s9-v3: [R] pruef trägt 9, das richtige Ergebnis ist aber h(−3) = −9 (loesung nennt −9 richtig) – pruef auf −9 setzen.
e5-k3-s2-v2: Sprosse und Merkmal verlangen „Quadrat gegen Zweierpotenz“ (x² und 2^x), die Aufgabe nimmt x³ und 3^x – Merkmal/Sprosse weiter fassen oder Aufgabe auf x² und 2^x umstellen.

Sauber: 425 Zeilen ohne Befund

## Abgleich

Kein Abgleich möglich: bank/potenz-exponentialfunktionen/gegenlese.md liegt beim Pull vor dem Commit (11:22 UTC, main 56e0bad) nicht im Repo, auch nicht in der Git-Geschichte. Alle Befunde oben sind damit Befunde nur dieses Lesers; der Abgleich folgt, sobald ein Erstleser gegenlese.md anlegt.
