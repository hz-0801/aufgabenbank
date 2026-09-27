# Gegenlese: ableitung-und-aenderungsrate

Datum: 2026-09-27  
Modell: Claude in Claude Code (Web-Sitzung); die genaue Modellkennung darf laut Sitzungsvorgabe nicht ins Repo, sie steht im Chatbericht  
Geprüfte Zeilen: 220  
Korrekturen: 2

## Festlegungen dieser Gegenlese

- Jede Zeile einzeln nachgerechnet (Python mit sympy/scipy), aus dem Aufgabentext; bank.md nur für die Felder, stand.md nicht gelesen.
- Korrigiert wird nur, wenn loesung selbst rechnerisch falsch ist und die Korrektur eindeutig in loesung/pruef liegt. Ein unvollständiges pruef bei richtiger loesung ist ein Befund unter Punkt 1, keine Korrektur.
- Widerspricht die Lösung einer Grafik oder dem Aufgabentext und ließe sich das an Aufgabe, Grafik oder Lösung beheben, ist die Korrektur nicht eindeutig: Befund, keine Änderung.
- Korrigierte Zeilen stehen unter Punkt 1 mit „korrigiert“ und zählen nicht als sauber. Eine Zeile mit mehreren Befunden steht unter jedem Punkt einmal.

## Befunde

### 1 Lösung und pruef

- ableitung-und-aenderungsrate-e1-k1-s6-v2: korrigiert – Vergleich der Beträge: |−4,42| > |−3|, also größer bei A, nicht B (loesung)
- ableitung-und-aenderungsrate-e1-k2-s4-v1: korrigiert – w(3) = 2 + 4,5 + 1,5 = 8, nicht 7; Sekantensteigung (8 − 3)/2 = 2,5 cm je Stunde (loesung, pruef)
- ableitung-und-aenderungsrate-zone-f1-v3: pruef prüft nur m = 2, nicht den y-Achsenabschnitt −1 der gefragten Gleichung – pruef: [2, -1]
- ableitung-und-aenderungsrate-zone-f1-v4: pruef prüft nur −3; der Achsenabschnitt 7, um den es im Fallstrick geht, bleibt ungeprüft – pruef: [-3, 7]
- ableitung-und-aenderungsrate-e1-k1-s5-v1: pruef enthält den Achsenabschnitt 2,277 der gefragten Geradengleichung nicht – pruef um f(1)-m ≈ 2.2769 ergänzen
- ableitung-und-aenderungsrate-e1-k1-s5-v3: pruef enthält den Achsenabschnitt −4 der gefragten Sekantengleichung nicht – pruef: [-1, 8, 3, -4]
- ableitung-und-aenderungsrate-e2-k1-s7-v1: „Schaufel läuft dort ohne Knick weiter“ trifft nicht zu: f(0) = 0, p(0,5) = 0,75; verschiedene Punkte, kein Anschluss – Deutung auf „beide Begrenzungslinien verlaufen dort in gleicher Richtung (parallele Tangenten)“ beschränken
- ableitung-und-aenderungsrate-e2-k1-s7-v2: f(5) = −3,75, g(5) = −2,5: Graphen treffen sich bei x = 5 nicht; „knickfreier Übergang, gleiche Tangente“ ist falsch – g(x) = −0,5x − 1,25 und f für x ≤ 5 setzen; dann ist g die Tangente in (5 | −3,75)
- ableitung-und-aenderungsrate-e2-k2-s1-v1: Grafik 5t²: Punkt ist (2 | 20), nicht (2 | 40); da f(2) = f'(2) = 20, greift der Hinweis „nicht der Wert“ nicht. Nicht korrigiert, weil der Fehler ebenso in der Grafik liegen kann – Grafik auf \funktion{5*\x^2+20}{f} ändern: f(2) = 40, f'(2) = 20, Lösung stimmt dann
- ableitung-und-aenderungsrate-e2-k4-s4-v3: pruef enthält nur x = 1, die Lösung nennt auch x = −1 – pruef: [9, -3, 9, 1, -1]

### 2 Eindeutig lösbar

- ableitung-und-aenderungsrate-zone-f1-v3: \steigungsdreieck{1}{1}{1} zeichnet 1 nach oben (Beschriftung 1) und erreicht die Gerade nicht; Lösung nennt 2 nach oben – Grafik: \steigungsdreieck{1}{1}{2}
- ableitung-und-aenderungsrate-zone-f6-v4: Optionen sprechen von t = 4, t = 8, t = 0, die Achse ist aber mit x beschriftet (ksys ohne xlabel); t ist nicht erklärt – xlabel=t ergänzen oder Optionen mit x formulieren
- ableitung-und-aenderungsrate-e1-k1-s9-v1: Graph 0,1x³ läuft bis x ≈ 3,42 (Rand y = 4), Endpunkt x = 3 nicht erkennbar; mit sichtbarem Ende wäre Sekante steiler als 45°, Urteil kippt – \funktionab{0.1*\x^3}{f}{0}{3} statt \funktion
- ableitung-und-aenderungsrate-e1-k1-s9-v2: Graph 0,75x² läuft bis x ≈ 2,31 (Rand y = 4), Endpunkt (2|3) der Lösung nicht erkennbar – \funktionab{0.75*\x^2}{f}{0}{2} statt \funktion
- ableitung-und-aenderungsrate-e1-k1-s9-v3: Graph läuft bis x = 5, Lösung nimmt Endpunkt (4|2); Anfangs-/Endpunkt des Wegs nicht festgelegt – \funktionab{…}{w}{0}{4} statt \funktion
- ableitung-und-aenderungsrate-e1-k2-s4-v1: Der Punkt (3|8) liegt genau auf dem oberen Rand (ymax = 8), schlecht ablesbar – ymax=10 setzen
- ableitung-und-aenderungsrate-e2-k4-s4-v3: „an welcher Stelle“ im Singular, es gibt aber zwei Stellen mit waagerechter Tangente (x = −1 und x = 1) – „an welchen Stellen“ schreiben
- ableitung-und-aenderungsrate-e4-k1-s1-v1: Sprachfehler im Arbeitsauftrag: „nenne den Zeitpunkt … an“ – „an“ am Satzende streichen: „… und nenne den Zeitpunkt der größten …rate.“
- ableitung-und-aenderungsrate-e4-k1-s1-v2: Sprachfehler im Arbeitsauftrag: „nenne den Zeitpunkt … an“ – „an“ am Satzende streichen: „… und nenne den Zeitpunkt der größten …rate.“
- ableitung-und-aenderungsrate-e4-k1-s1-v3: Sprachfehler im Arbeitsauftrag: „nenne den Zeitpunkt … an“ – „an“ am Satzende streichen: „… und nenne den Zeitpunkt der größten …rate.“
- ableitung-und-aenderungsrate-e4-k1-s1-v4: Sprachfehler im Arbeitsauftrag: „nenne den Zeitpunkt … an“ – „an“ am Satzende streichen: „… und nenne den Zeitpunkt der größten …rate.“
- ableitung-und-aenderungsrate-e4-k1-s1-v5: Sprachfehler im Arbeitsauftrag: „nenne den Zeitpunkt … an“ – „an“ am Satzende streichen: „… und nenne den Zeitpunkt der größten …rate.“
- ableitung-und-aenderungsrate-e4-k2-s3-v2: „In welchem Monat“: t = 10 ist genau die Grenze zwischen 10. und 11. Monat, beide Antworten vertretbar – „Nach wie vielen Monaten …“ fragen; Lösung „nach 10 Monaten“
- ableitung-und-aenderungsrate-e4-k2-s3-v3: „An welchem Tag“: t = 10 ist genau die Grenze zwischen 10. und 11. Tag, beide Antworten vertretbar – „Nach wie vielen Tagen …“ fragen; Lösung „nach 10 Tagen“
- ableitung-und-aenderungsrate-e4-k2-s4-v3: Unteres System ymin2 = −4, aber f'(6) = −12: der Graph von f' verlässt ab x ≈ 4,83 den Bereich, Skizze nicht vollständig möglich – ymin2=-12 setzen (oder Intervall auf 0 ≤ x ≤ 4,5 begrenzen)

### 3 Sprosse und Merkmal

- ableitung-und-aenderungsrate-zone-f3-v2: v1 prüft nur Uhrzeit→Stunden, v2 nur Einheit „je“: die Varianten tragen verschiedene Teile des Merkmals, nicht austauschbar – Je Variante beide Teile oder Merkmal/Sprosse aufteilen
- ableitung-und-aenderungsrate-e1-k1-s1-v3: „am ersten und am 15. Tag“ verlangt, die Länge (14) erst zu erschließen; Zaunpfahl-Fallstrick im Grundfall, anders als die übrigen Varianten – Zeitraum direkt nennen, z. B. „nach 14 Tagen“
- ableitung-und-aenderungsrate-e1-k1-s8-v2: Gleichung hat nur eine Lösung (c = 4); das Merkmal „kleinere Lösung wählen“ fehlt in dieser Variante – Kubischen Term wählen, der zwei Lösungen liefert
- ableitung-und-aenderungsrate-e1-k1-s10-v3: v1–v2 prüfen nur die Zusatzkosten-Aussage, v3–v4 nur Termnachweis und Schranke; die Varianten sind nicht gleichwertig zur Sprosse – Je Variante beide Teile als a)/b) stellen
- ableitung-und-aenderungsrate-e1-k2-s2-v3: Begründung zur Umrechnung von Uhrzeiten gehört weder zu sprosse_text (Sekante, Einheiten) noch zum Merkmal – Durch Begründung zu Sekante oder Einheit ersetzen
- ableitung-und-aenderungsrate-e1-k2-s3-v1: sprosse_text verlangt Rate „aus dem Funktionsterm“; hier nur zwei Messwerte, kein Term – Verlauf durch Funktionsterm vorgeben
- ableitung-und-aenderungsrate-e1-k2-s3-v3: sprosse_text verlangt Rate „aus dem Funktionsterm“; hier nur Messwerte, kein Term – Verlauf durch Funktionsterm vorgeben
- ableitung-und-aenderungsrate-e1-k2-s4-v1: sprosse_text verlangt die Sekantengleichung; keine der drei Varianten fragt nach ihr, nur nach der Steigung – Gleichung der Sekante mit erfragen oder sprosse_text prüfen
- ableitung-und-aenderungsrate-e2-k1-s0-v1: Merkmal verlangt, die Einheit zu nennen; v1–v4 fragen nicht danach, v3/v4 haben ohne Sachkontext gar keine Einheit – Auftrag „und nenne die Einheit“ ergänzen; v3/v4 mit Sachkontext und Einheiten versehen
- ableitung-und-aenderungsrate-e2-k1-s3-v3: g'(0) = 0: waagerechte Tangente, ein Steigungsdreieck entfällt; das Merkmal (Tangente mit Steigungsdreieck) wird nicht geübt – Stelle oder Term so wählen, dass g'(x₀) ≠ 0, und Steigungsdreieck verlangen
- ableitung-und-aenderungsrate-e4-k1-s5-v2: Nur eine Nullstelle von w', kein Kandidat zu verwerfen, keine Uhrzeit; Merkmal der Sprosse (Kandidatenwahl, Uhrzeit) fehlt; Niveau wie Sprosse 1/2 – Zeit ab Uhrzeit zählen und einen Kandidaten (Rand oder negative Lösung) verwerfen lassen
- ableitung-und-aenderungsrate-e4-k1-s7-v2: Beide Lösungen (2 und 6) liegen in der Phase; das Verwerfen einer Lösung außerhalb der Phase entfällt. Zudem Tippfehler „ist $= 4$ Minuten“ – Zahlen so wählen, dass eine Lösung außerhalb 0–8 liegt; „ist $= 4$“ zu „ist 4“
- ableitung-und-aenderungsrate-e4-k1-s9-v4: Varianten teilen die Sprosse: v1–v3 nur Differenz zweier Raten, v4–v7 nur Proportionalität f − c = k·f'; Varianten prüfen verschiedene Merkmale – Jede Variante mit beiden Teilen versehen oder die Sprosse in zwei Teilaufgaben/Varianten-Gruppen trennen
- ableitung-und-aenderungsrate-e4-k2-s2-v3: Begründung zum Randvergleich steht nicht in der Sprosse (nur Wendestelle und negative Rate bei Anzahl) – Durch Begründung zu einem der beiden Katalogthemen ersetzen oder Sprossentext erweitern

### 4 Schreibform

- ableitung-und-aenderungsrate-e2-k1-s6-v3: Lösung begründet mit „Weg wäre die Fläche unter dem Graphen“; Integral ist in dieser Kette nicht verfügbar – Begründen über die Einheit: 24 km je Stunde ist eine Geschwindigkeit (Rate), kein Weg in km
- ableitung-und-aenderungsrate-e2-k4-s2-v3: Lösung nutzt „Grenzwert von Differenzenquotienten“; der Grenzwertbegriff kommt erst in Einheit 3 – Über das Steigungsdreieck der Tangente begründen: Höhenunterschied in m durch Zeitunterschied in s

### 5 Ankreuzen

- keine

### 6 Fehler finden

- ableitung-und-aenderungsrate-e4-k2-s1-v3: Mehrere Fehler vermischt (Maximum statt Minimum, Stelle statt Wert, Rand nicht geprüft); Leas „4“ stimmt zufällig mit z(0) = 4 überein; „den Fehler“ nicht eindeutig – Auf ein Muster beschränken, z. B. Lea gibt z(4) = 20 ohne Randvergleich an; Zahlen so wählen, dass z(0) ≠ 4

Sauber: 182 Zeilen ohne Befund
