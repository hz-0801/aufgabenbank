# Gegenlese: funktionsscharen-und-ortskurven

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung), unabhängige Gegenlese
Geprüfte Zeilen: 222 (zone 30, e1 40, e2 37, e3 36, e4 42, e5 37)
Korrekturen: 0

Alle Lösungen mit Python/sympy aus der Aufgabe nachgerechnet;
bank-pruef.py: 0 Abweichungen. Keine Lösung ist rechnerisch falsch.

## Entscheidungen

- Korrigiert wird nur eine falsche Zahl mit eindeutiger Korrektur.
  Ein pruef, der eine richtige Lösung nur teilweise abdeckt, steht
  als Befund unter Punkt 1; die Zeile bleibt unverändert.
- Leeres pruef bei zone-f1-v4 bis v6 (Ziffern nur im Exponenten) ist
  nach bank.md zulässig und kein Befund.
- Das Antwortgerüst `\_\_` (unten) gehört zu keinem der Punkte 1–6
  und steht deshalb gesondert am Ende.

## Befunde

### Punkt 1 – Lösung rechnerisch richtig

- funktionsscharen-und-ortskurven-e1-k1-s6-v1: Lösung stimmt, das Gerüst hat drei Lücken, pruef [3, 2] prüft den y-Achsenabschnitt nicht – pruef [3, 2, 3].
- funktionsscharen-und-ortskurven-e2-k1-s5-v2: Lösung nennt drei Punkte, pruef lässt $(0 | 0)$ weg – pruef [[-1, -1], [0, 0], [1, 1]].
- funktionsscharen-und-ortskurven-e4-k2-s3-v3: Lösung stimmt (Breite 8 m), pruef 0.5625 prüft die Breite nicht – pruef [0.5625, 8], dafür „Breite am Boden $2r = 8$ m“ in der Lösung.

### Punkt 2 – eindeutig lösbar

- funktionsscharen-und-ortskurven-e1-k1-s2-v3: Text nennt einen „abgebildeten Graphen“, grafik ist leer – „abgebildeter“ streichen oder Grafik ergänzen.
- funktionsscharen-und-ortskurven-e3-k1-s8-v1: „Bestimme ihn“ kann den Wert von $a$ oder den Punkt meinen, die Lösung gibt nur $a$ – „Bestimme diesen Wert von $a$.“
- funktionsscharen-und-ortskurven-e3-k1-s8-v2: wie s8-v1 – wie s8-v1.

### Punkt 3 – passt zu sprosse_text und merkmal

- funktionsscharen-und-ortskurven-e1-k1-s2-v2: führt auf die quadratische Gleichung $-8a^2 + 24a = 0$, die Sprosse verlangt „lineare Gleichung lösen“ – in $a$ linearen Ansatz wählen (etwa $a x^3 + 6x^2$, Nullstelle $-2$).
- funktionsscharen-und-ortskurven-e1-k1-s8-v3: reines Zuordnen von Graphen ohne Sachzusammenhang, die Sprosse ist „Bestimmungsgleichungen im Sachzusammenhang deuten und auswerten“ – in einen Sachkontext mit Bestimmungsgleichungen einbetten oder zur Zuordnen-Sprosse verlegen.
- funktionsscharen-und-ortskurven-e1-k1-s8-v4: wie s8-v3 – wie s8-v3.
- funktionsscharen-und-ortskurven-e2-k1-s4-v3: wegen $b > 0$ keine Fallunterscheidung, die Sprosse verlangt sie nach Vorzeichen oder Parität – Bereich auf $b \ne 0$ öffnen und nach dem Vorzeichen unterscheiden lassen.
- funktionsscharen-und-ortskurven-e3-k1-s2-v1: gefragt ist nur die parameterfreie x-Koordinate, kein Extrempunkt als Term – auch die y-Koordinate verlangen ($H(6 | 432k)$).
- funktionsscharen-und-ortskurven-e3-k1-s7-v3: Umkehraufgabe (Parameter aus dem x-Abstand), ohne Pythagoras und Abstand als Term – Abstandsaufgabe wie v1/v2 stellen.
- funktionsscharen-und-ortskurven-e3-k2-s3-v2: verlangt nur das Maximum, keinen Wendepunkt – Wendestellenfrage ergänzen (stärkste Abnahme, $t = 8$).
- funktionsscharen-und-ortskurven-e3-k2-s3-v3: Parabel, hat keinen Wendepunkt – Scharfunktion mit Wendestelle im Sachkontext nehmen.
- funktionsscharen-und-ortskurven-e4-k1-s1-v2: Nullstellen $\pm 2$ parameterfrei, Merkmal ist „Nullstellen als Terme“ – Funktion mit parameterabhängigen Nullstellen nehmen.
- funktionsscharen-und-ortskurven-e4-k1-s1-v4: Nullstellen 0 und 3 parameterfrei – etwa $a x (x - 3a)$.
- funktionsscharen-und-ortskurven-e4-k1-s6-v2: kein Parameter wird bestimmt, nur für jedes $p$ nachgewiesen (v1/v3 bestimmen ihn) – Parameter aus den Übergangsbedingungen bestimmen lassen.
- funktionsscharen-und-ortskurven-e4-k1-s8-v3: Dreieck aus Achsenschnittpunkten, sprosse_text ist „Vierecksinhalt aus Hochpunkt und Achsenpunkten“ – sprosse_text auf alle Originale der Prüfungshöhe abstimmen oder Zeile passend zuordnen.
- funktionsscharen-und-ortskurven-e4-k1-s8-v4: wie s8-v3 – wie s8-v3.
- funktionsscharen-und-ortskurven-e4-k1-s8-v5: fragt, ob Stammfunktionen nur negative Werte haben, nicht den Vierecksinhalt – wie s8-v3.
- funktionsscharen-und-ortskurven-e4-k1-s8-v6: wie s8-v5 – wie s8-v3.
- funktionsscharen-und-ortskurven-e5-k1-s8-v3: Trapezflächen, sprosse_text ist „Ortsgerade y = x über Sonderfall und Streckung begründen“ – sprosse_text auf beide Originale abstimmen oder Zeile passend zuordnen.
- funktionsscharen-und-ortskurven-e5-k1-s8-v4: wie s8-v3 – wie s8-v3.

### Punkt 4 – Schreibform

- funktionsscharen-und-ortskurven-e2-k1-s7-v3: Lösung braucht die Quotientenregel, die weder Zone noch Kette davor einführen – als Schar ohne Bruch stellen, etwa $g_a(x) = 2x \cdot e^{a x^2}$.

### Punkt 5 – Ankreuzen

keine

### Punkt 6 – Fehler finden

- funktionsscharen-und-ortskurven-e4-k2-s1-v3: eingebauter Fehler $(2a)^3 = 2a^3$ ist ein Klammerfehler, nicht das Muster „Parametergrenzen als Zahlen behandelt“ bzw. „Vorzeichenbedingung“ der Sprosse – Fehler nach dem genannten Muster bauen.

Sauber: 197 Zeilen ohne Befund

## Außerhalb der Punkte 1–6

- 88 Zeilen (zone 19, e1 18, e2 5, e3 12, e4 25, e5 9) schreiben die Lücke in antwort als `\_\_`; werkzeuge/zusammenbau.py (`antwortfeld`) trennt nur an `__`, es entsteht kein `\leerfeld`, auf dem Blatt stehen wörtliche Unterstriche – `\_\_` durch `__` ersetzen (Zeilen nicht als Befund gezählt).
