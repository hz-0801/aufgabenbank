# Gegenlese trigonometrische-funktionen

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 268
Korrekturen: 0

## 1 Lösung und pruef

- keiner

## 2 Eindeutig lösbar

- trigonometrische-funktionen-zone-f4-v1: „gerundet“ ohne Stellenzahl, die Lösung rundet auf 18,85 – „auf zwei Stellen“ ergänzen
- trigonometrische-funktionen-e1-k1-s13-v3: z ist nicht erklärt („Bei einer Rampe gilt z : …“) – sagen, welche Strecke z ist, z. B. „die Länge z der Rampe“
- trigonometrische-funktionen-e4-k1-s5-v2: „Start auf Höhe der Mitte“ ohne Richtung; fährt die Gondel abwärts, wäre a = −20 richtig – „… und steigt“ ergänzen wie in e4-k1-s13-v2
- trigonometrische-funktionen-e4-k1-s5-v1, trigonometrische-funktionen-e4-k1-s5-v2, trigonometrische-funktionen-e4-k1-s5-v3, trigonometrische-funktionen-e4-k1-s6-v1: t (und y) ohne Erklärung und Einheit, obwohl b von der Zeiteinheit abhängt – „(t in h, y in °C)“ bzw. passend ergänzen wie in e4-k1-s6-v2
- trigonometrische-funktionen-e4-k1-s7-v1, trigonometrische-funktionen-e4-k1-s7-v2, trigonometrische-funktionen-e4-k1-s7-v3, trigonometrische-funktionen-e4-k1-s13-v1, trigonometrische-funktionen-e4-k1-s13-v2, trigonometrische-funktionen-e4-k1-s13-v3: Winkelmodus nicht genannt; die Gleichungen rechnen in Grad (b = 360 : Periode), im RAD-Modus kommt ein falscher Wert heraus (z. B. 1,6 · sin 270 + 3 ≈ 2,72 statt 1,4) – „Rechne im Grad-Modus.“ ergänzen

## 3 Sprosse und Merkmal

- trigonometrische-funktionen-zone-f1-v4, trigonometrische-funktionen-zone-f4-v4: Fallstrick-Zeile gleicht der leichten Zeile derselben Fertigkeit (zone-f1-v1, zone-f4-v1) bis auf die Zahlen, der Fallstrick wird nicht provoziert – Angabe so wählen, dass der Fehler naheliegt (f1: erst Hypotenuse, dann Gegenkathete nennen; f4: Radius gegeben, dazu der Hinweis „u = π · d“)
- trigonometrische-funktionen-zone-f2-v2: dieselbe Aufgabe wie zone-f1-v3 (Sinuswert mit dem Rechner im Grad-Modus auf zwei Stellen), dort „mittel“, hier „sehr leicht, im Kopf“ – durch eine Kopfaufgabe ersetzen (z. B. Modus zu „sin 30°“ ankreuzen)
- trigonometrische-funktionen-e1-k1-s7-v2: der negative Sinuswert verlangt zusätzlich, den Rechnerwert −23,6° in den dritten und vierten Quadranten zu bringen; das haben v1 und v3 nicht – positiven Sinuswert nehmen oder als eigene Sprosse führen
- trigonometrische-funktionen-e2-k1-s7-v3: der eingeschränkte Winkelbereich (0° bis 180°) ist ein neues Merkmal gegenüber v1 und v2 – ohne Einschränkung stellen, z. B. „Kann sin x = −1,5 sein?“
- trigonometrische-funktionen-e3-k1-s7-v3, trigonometrische-funktionen-e3-k1-s8-v3: negatives a (s7-v3 zudem ohne b) ist ein Zusatzmerkmal gegenüber den Schwestervarianten – positives a und b ≠ 1 wie in v1 und v2
- trigonometrische-funktionen-e3-k1-s11-v1, trigonometrische-funktionen-e3-k1-s11-v2, trigonometrische-funktionen-e3-k1-s11-v3: die Varianten teilen das Merkmal auf (v2 nur c, v1 und v3 nur d) – jede Variante c und d zusammen geben, z. B. y = sin(x − 30°) + 1
- trigonometrische-funktionen-e4-k1-s11-v1, trigonometrische-funktionen-e4-k1-s11-v2, trigonometrische-funktionen-e4-k1-s11-v3: v1 nur Tabelle, v2 und v3 nur Auswahl zu einem Sachverhalt – jede Variante mit beiden Teilen der Sprosse (Tabelle, dann Sachverhalt zuordnen)
- trigonometrische-funktionen-e2-k1-s15-v2, trigonometrische-funktionen-e2-k1-s15-v3: Tabelle und Zeichenauftrag wiederholen e2-k1-s1-v5 (Sinus in 40°-Schritten) bzw. e2-k1-s2-v3 (zwei Wellen, 90°-Schritte, 0° bis 720°) – andere Schrittweite oder anderen Bereich wählen (z. B. 30°-Schritte, −360° bis 360°)

## 4 Schreibform

- trigonometrische-funktionen-e2-k1-s8-v3, trigonometrische-funktionen-e2-k1-s11-v3: negative Winkel (−540° bis 0°, −80° bis 80°) vor der Symmetrie-Sprosse s12, die sie erst einführt; Einheit 1 kennt nur 0° bis 360° – Bereich ins Positive legen (z. B. 720° bis 1260°, 280° bis 440°)
- trigonometrische-funktionen-e3-k3-s1-v2: Fehler finden setzt die Verschiebung d voraus (Welle 2 · sin(x) + 1), die in Einheit 3 nur Vorrat (GYM) ist; in der EBR/FOR-Fassung fehlt der Schüler der Begriff – als GYM-Zeile kennzeichnen oder erst nach s11 einsetzen

## 5 Ankreuzen

- keiner

## 6 Fehler finden

- keiner

## Entscheidungen

- \funktion zeichnet über TikZ/pgfmath, dort rechnen sin und cos in Grad (mathblatt.sty; \sinus und \kosinus setzen dafür deg()); alle Graphen haben eine Gradachse und wurden so nachgerechnet – sie passen.
- Die Gradrechnung in Einheit 4 (b = 360 : Periode) gilt als Konvention der Kette; beanstandet ist nur der fehlende Modus-Hinweis beim Rechnen.
- Eine Variante gilt als abweichend im Merkmal, wenn sie einen Schritt verlangt, den die Schwestervarianten nicht verlangen; ein Wechsel zwischen Text und Bild innerhalb einer Sprosse, die beides nennt, gilt nicht als Abweichung.
- e4-k1-s12-v3 (Sinuskurve statt Kurve ab Ursprung im Kandidatenfeld) nicht beanstandet: das Merkmal „auswählen und zwei ausschließen“ bleibt, stand.md begründet die Wahl.

Sauber: 238 Zeilen ohne Befund
