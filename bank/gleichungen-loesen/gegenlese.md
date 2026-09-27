# Gegenlese: gleichungen-loesen

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung), unabhängige Gegenlese
Geprüfte Zeilen: 223 (zone 38, e1 56, e2 50, e3 47, e4 32)
Korrekturen: 0

Alle Lösungen und pruef-Werte mit Python/sympy aus der Aufgabe
nachgerechnet, Rechnerwerte numerisch; bank-pruef.py: 0 Abweichungen.

## Entscheidungen

- Korrigiert wird nur eine falsche Zahl mit eindeutiger Korrektur.
  Ein pruef, der eine richtige Lösung nicht oder nur teilweise an
  ihrer Ergebniszahl prüft, steht als Befund unter Punkt 1.
- Ein Sachkontext, der den Werten widerspricht, steht unter Punkt 2.
- Eine Zeile mit Befunden unter mehreren Punkten steht unter jedem.

## Befunde

### Punkt 1 – Lösung rechnerisch richtig

- gleichungen-loesen-e1-k3-s3-v1: Lösung stimmt, pruef [2, 8] prüft nur $x_1$, $x_2$, nicht die Gerüstzahlen 200 und 800 – pruef [2, 8, 200, 800].
- gleichungen-loesen-e1-k3-s3-v3: Lösung stimmt, pruef [4, 8] prüft nur $t_1$, $t_2$, nicht die Uhrzeiten 10 und 14 – pruef [4, 8, 10, 14].
- gleichungen-loesen-e3-k3-s1-v1: pruef [0, 4] nimmt die Zahlen der falschen Schülergleichung, nicht der richtigen $p(x + 4) = p(x) + 30$ – pruef [4, 30].

### Punkt 2 – eindeutig lösbar

- gleichungen-loesen-e1-k1-s7-v2: unterer Bogen $g$ liegt zwischen $x = 4$ und $x = 6$ unter dem Boden ($g(5) = -0{,}5$), obwohl „Boden bei $y = 0$“ – etwa $f(x) = -0{,}5x^2 + 5x - 2$, $g(x) = 0{,}5x^2 - 5x + 14$ (dann $S_1(2 | 6)$, $S_2(8 | 6)$, 36 m², 1080 €).
- gleichungen-loesen-e1-k1-s9-v1: Funktionsname $u$ neben der Substitution $u = x^2$ derselben Einheit (ein Buchstabe je Einheit für eine Sache) – $u$, $v$ in $f$, $g$ umbenennen, auch in der Lösung.
- gleichungen-loesen-e1-k1-s9-v2: wie s9-v1 – wie s9-v1.
- gleichungen-loesen-e1-k1-s9-v3: wie s9-v1 – wie s9-v1.
- gleichungen-loesen-e3-k2-s1-v3: $f - g$ hat bei $x \approx -1{,}44$ ein Minimum von nur $\approx 0{,}006$; am Rechnerbild wirkt das wie ein dritter Schnitt- oder Berührpunkt (Lösung mit zwei Punkten stimmt) – Zahlen ändern, etwa $g(x) = 0{,}5x + 1$.
- gleichungen-loesen-e3-k3-s1-v1: „4 Stunden später um 30 cm höher“ ohne Bezugszeitpunkt; bei der Lesart „ab jetzt“ ist $p(4) = p(0) + 30$ nicht falsch – „Zu jedem Zeitpunkt $x$ gilt: 4 Stunden später ist der Pegel um 30 cm höher als zum Zeitpunkt $x$.“

### Punkt 3 – passt zu sprosse_text und merkmal

- gleichungen-loesen-zone-f5-v2: fragt „Hat $e^x = 0$ eine Lösung?“, das Merkmal ist „e hoch null direkt“ – durch eine $e^0$-Aufgabe ersetzen (etwa $g(x) = 5e^x$, $g(0)$).
- gleichungen-loesen-e1-k1-s6-v1: sprosse_text verlangt „Lösung an der Abbildung prüfen“, grafik ist leer – Grafik mit $f$, $g$ und den Schnittpunkten ergänzen.
- gleichungen-loesen-e1-k1-s6-v2: wie s6-v1 – wie s6-v1.
- gleichungen-loesen-e1-k1-s6-v3: wie s6-v1 – wie s6-v1.
- gleichungen-loesen-e2-k1-s6-v2: „Zeige“-Aufgabe mit genannter Stelle und leerem Gerüst, v1/v3 fragen den Abstand der Schnittstellen – wie v1/v3 fassen (zwei Schnittstellen, Abstand, antwort „__ dm“).
- gleichungen-loesen-e3-k1-s0-v4: die Vorstufe („nichts rechnen“) verlangt schon die Maßstabsumrechnung (Merkmal von s3) – Maßstab weglassen (1 LE = 1 m).
- gleichungen-loesen-e4-k1-s1-v5: als einzige Grundfall-Variante mit ≥, dadurch kommt die isolierte Lösung $x = -6$ (doppelte Nullstelle) hinzu – auf > umstellen oder den ≥-Fall als eigene Sprosse führen.
- gleichungen-loesen-e4-k2-s1-v2: v1/v3 lösen mit dem Rechner auf zwei Stellen, v2 ist biquadratisch und von Hand lösbar, ohne Rechner- und Rundungsangabe – Methode und Rundung angleichen.

### Punkt 4 – Schreibform

keine

### Punkt 5 – Ankreuzen

- gleichungen-loesen-e1-k1-s0-v1: bei $x^4 - 10x^2 + 9 = 0$ führt auch „Polynomdivision“ zum Ziel ($x = 1$, $x = 3$ ratbar), also nicht genau eine richtige Option – Distraktor durch „Ausklammern“ oder „n-te Wurzel“ ersetzen.
- gleichungen-loesen-e3-k1-s0-v2: „2 Stunden später um 30 cm höher“ ohne Bezugszeitpunkt; bei der Lesart „ab jetzt“ ist auch $w(2) = w(0) + 30$ richtig – Bedingung schärfen wie bei e3-k3-s1-v1.

### Punkt 6 – Fehler finden

- gleichungen-loesen-e2-k3-s1-v1: Benennung „Vorfaktor 3 beim Logarithmieren mitgezogen“ trifft den eingebauten Fehler nicht, die 3 wurde übergangen ($\mathrm{ln}(3e^{2x}) = \mathrm{ln}(3) + 2x$) – „den Vorfaktor 3 beim Logarithmieren übergangen“.
- gleichungen-loesen-e3-k3-s1-v1: wegen der Mehrdeutigkeit (Punkt 2) ist der eingebaute Fehler nicht eindeutig falsch – Bedingung schärfen wie unter Punkt 2.

Sauber: 204 Zeilen ohne Befund
