# Gegenlese umkehrfunktion

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 91
Korrekturen: 0

## 1 Lösung und pruef

- umkehrfunktion-e2-k1-s3-v1: Aufgabe verlangt „gib den Berührpunkt an“, die Lösung nennt nur „Spiegelpunkt von Q“, obwohl f konkret ist – Berührpunkt ergänzen: Q(2 ln 3 | 0), Berührpunkt mit g $(0 | 2\,\mathrm{ln}\,3) \approx (0 | 2{,}20)$, oder allgemein $(f(x_Q) | x_Q)$
- umkehrfunktion-e2-k1-s4-v2: Aufgabe verlangt „Begründe, dass … ein Trapez bilden“, die Lösung enthält nur die Rechnung – Satz wie in v1 ergänzen: „AA' und BB' stehen senkrecht auf y = x, sind also parallel“

## 2 Eindeutig lösbar

- umkehrfunktion-e2-k1-s3-v3: „Berührt sie auch den Graphen der Umkehrfunktion?“ hat ohne f keine eindeutige Antwort, und die Lösung „nur dieses Spiegelbild berührt den Graphen der Umkehrfunktion“ stimmt so nicht (die Gerade kann g an anderer Stelle berühren) – fragen „Muss sie … berühren?“, Lösung „nicht zwangsläufig: im Spiegelpunkt hat g die Steigung −1/2, dort berührt sie nicht“
- umkehrfunktion-e1-k1-s4-v1, umkehrfunktion-e1-k1-s4-v2: h steht in Einheit 1 für die eingeschränkte Funktion, in e1-k2 (Glas, Schale, Vase) für die Füllhöhe – die eingeschränkte Funktion umbenennen (z. B. k)

## 3 Sprosse und Merkmal

- umkehrfunktion-e1-k1-s2-v3: $\sqrt{x} + 1$ auf $[0;\, 9]$ hat nur geschlossene Grenzen, das Merkmal „nicht angenommene Grenze bleibt offen“ fehlt – Funktion mit Grenzwert wählen, z. B. $f(x) = \frac{1}{x} + 1$ auf $[1;\, \infty[$ (Definitionsbereich von g $]1;\, 2]$)
- umkehrfunktion-e1-k1-s3-v3: „Bestimme“ statt „weise nach“ und kein Faktor vor dem ln ($2e^x + 5$ → $\mathrm{ln}\frac{x-5}{2}$), damit Grundfall-Niveau statt Merkmal von v1/v2 – wie v1/v2 negativen Exponentenfaktor und vorgegebenen Term, z. B. $f(x) = 2e^{-3x} + 5$, $g(x) = -\frac{1}{3}\,\mathrm{ln}\left(\frac{x - 5}{2}\right)$ nachweisen
- umkehrfunktion-e2-k1-s3-v3: Gegenfall Steigung −2 statt des Sonderfalls Steigung −1 – ändert das Merkmal der Sprosse; als Begründen-Aufgabe (e2-k2-s2) führen oder durch einen dritten Sonderfall mit Steigung −1 ersetzen
- umkehrfunktion-e1-k3-s3-v1, umkehrfunktion-e1-k3-s3-v2, umkehrfunktion-e1-k3-s3-v3: sprosse_text verlangt den Definitionsbereich der Umkehrfunktion, keine Variante fragt ihn – je eine Frage nach dem sinnvollen Bereich ergänzen (z. B. Tee: für welche Temperaturen gilt t(T)? $]20;\, 80]$)
- umkehrfunktion-e2-k2-s3-v1, umkehrfunktion-e2-k2-s3-v2: „Tage je Zentimeter“ bzw. „Zeit je Meter“ ist eine eingekleidete Kehrwertrechnung, keine im Kontext sinnvolle Frage – nach einer Dauer fragen, z. B. „Wie lange braucht sie etwa für den nächsten halben Zentimeter?“ bzw. „für die nächsten 10 m?“
- umkehrfunktion-zone-f5-v4, umkehrfunktion-zone-f5-v5: gleiche Frage wie die Vorstufe von Einheit 2 (e2-k1-s0 v2 und v3, nur andere Zahl), die Zone nimmt die Vorstufe vorweg – in der Zone die Steigung über das Umstellen einer Geradengleichung nach x fragen (z. B. $y = 3x$ → $x = \frac{1}{3}y$), nicht als Spiegelfrage

## 4 Schreibform

- keiner

## 5 Ankreuzen

- keiner

## 6 Fehler finden

- umkehrfunktion-e1-k3-s1-v3: der eingebaute Fehler ist keiner – $g(y) = \frac{y}{4} + 2$ ist dieselbe Funktion wie $g(x) = 0{,}25x + 2$, und mit der Eingabe nach rechts gezeichnet ist der Graph richtig – Paul die Gleichung $x = \frac{y}{4} + 2$ als Graph von g ins xy-System zeichnen lassen (er erhält wieder die Gerade von f)
- umkehrfunktion-e2-k2-s1-v2: Bens Fehler (Gegenzahl statt Kehrwert) ist nicht das genannte Muster „Tangente neu berechnet statt gespiegelt“, und Steigung 4 → 1/4 ist das Beispiel des Merkkastens – eigene Zahlen und das Muster der Mappe, z. B. Ben berechnet die Steigung von g in (b | a) als f'(b) statt 1/f'(a)
- umkehrfunktion-e2-k2-s1-v3: dieselben Punkte A(0 | 4), B(1 | 7) wie e2-k1-s4-v1, die Höhe $2\sqrt{2}$ steht dort schon in der Lösung – eigene Punkte wählen, z. B. A(0 | 3), B(2 | 7)

## Entscheidungen

- Verweise auf andere Zeilen in Kurzform (ohne volle id) zählen nicht als Befund dieser Zeilen; die Zählung „Sauber“ geht nach vollen ids.
- Merkkasten-Funktion $x^2$/$\sqrt{x}$ in der Grafik von e2-k2-s4-v2 nicht beanstandet (Grundfunktion, nur Grafik).

Sauber: 74 Zeilen ohne Befund
