# Gegenlese binomische-formeln

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 170
Korrekturen: 0

## 1 Lösung und pruef
binomische-formeln-e2-k2-s9-v3: pruef "-16" prüft den Zwischenwert, das Ergebnis x² − 10x + 64 hat −10 (Lösung selbst richtig) – pruef "-10"; das Skript wertet aber nur die erste Zahl (−16) als Ergebnisstelle, daher nicht korrigiert: Lösung als „$x^2 - 10x + 64$, aus …" umstellen oder Skriptbefund in stand.md
## 2 Eindeutigkeit
binomische-formeln-e3-k1-s0-v4: antwort „Wurzeln __ und __" ist nicht ausfüllbar, weil 20 keine Quadratzahl ist (pruef 20 ist keine Wurzel) – Gerüst für den Nein-Fall öffnen oder Aufgabe mit Quadratzahl und falschem Mittelglied
## 3 Sprosse und Merkmal
binomische-formeln-zone-f1-v2: Aufgabe 9 − 2 · 4 enthält kein Produkt negativer Zahlen, merkmal „Produkt zweier negativer Zahlen" passt nicht – Aufgabe mit Produkt zweier negativer Zahlen oder merkmal der Fertigkeit anpassen
binomische-formeln-zone-f3-v2: 9x − x zieht ab und hat Vorzahl eins, merkmal „gleichartige Glieder mit Plus zusammenfassen" – Aufgabe mit Plus (etwa 6x + 2x) oder merkmal anpassen
binomische-formeln-zone-f7-v2: x² − 4x klammert eine Variable aus, merkmal „gemeinsame Zahl ausklammern" – Aufgabe mit Zahlfaktor (etwa 6x − 18)
binomische-formeln-e1-k1-s1-v1: Glied y mit Vorzahl eins nimmt das Merkmal von Sprosse 2 („Vorzahl eins") vorweg – y durch 2y o. ä. ersetzen
binomische-formeln-e1-k1-s1-v3: Glied x mit Vorzahl eins nimmt das Merkmal von Sprosse 2 vorweg – x durch 2x o. ä. ersetzen
binomische-formeln-e1-k1-s1-v5: Glied a mit Vorzahl eins nimmt das Merkmal von Sprosse 2 vorweg – a durch 3a o. ä. ersetzen
binomische-formeln-e1-k1-s4-v3: Faktor 2x statt Zahl, es entsteht x² – Sprosse heißt „Zahl mal Klammer"; Zahl als Faktor (etwa 5 · (3x + y))
binomische-formeln-e2-k2-s6-v3: dritte Formel ohne Mittelglied, merkmal verlangt „Mittelglied mit xy" – erste oder zweite Formel mit y-Glied (etwa (3x + y)²)
binomische-formeln-e3-k2-s2-v3: −x² + 64 ist Differenz, eine Formel passt; Sprosse verlangt Begründung, warum eine Summe zweier Quadrate keine Formel hat – Aufgabe mit echter Summe zweier Quadrate
## 4 Schreibform
binomische-formeln-e3-k1-s10-v1: Probe multipliziert nur 3 · (x² − 16) aus und prüft den Formelschritt (x + 4)(x − 4) nicht – Probe vom Endergebnis aus: 3 · (x² − 4x + 4x − 16) = 3x² − 48
binomische-formeln-e3-k1-s10-v2: Probe startet bei 2 · (x² + 12x + 36), nicht beim Endergebnis 2 · (x + 6)² – Probe: 2 · (x + 6)² = 2 · (x² + 12x + 36) = 2x² + 24x + 72
binomische-formeln-e3-k1-s10-v3: Probe startet bei 7 · (x² − 4x + 4), nicht beim Endergebnis 7 · (x − 2)² – Probe: 7 · (x − 2)² = 7 · (x² − 4x + 4) = 7x² − 28x + 28
## 5 Ankreuzen
binomische-formeln-e3-k1-s0-v2: zwei Fragen („Quadrate?", „Mittelglied?"), aber nur ein \janein; hier wäre die erste Frage ja, die zweite nein – je Frage ein \janein oder eine Frage „Ist das ein Binom-Quadrat?"
binomische-formeln-e3-k1-s0-v4: zwei Fragen, ein \janein; die erste Frage ist schon nein, die zweite ist nicht entscheidbar – wie v2
## 6 Fehler finden
keine

## Entscheidungen
e2-k2-s9-v3: pruef nicht korrigiert, weil "-10" im Prüfskript eine Abweichung erzeugt (Ergebnisstelle = erste Zahl −16) und die richtige Lösung nicht umgeschrieben werden darf; als Befund unter 1 geführt.
pruef mit Zahl bei \janein (e2-k1-s0-v1, -v3; e3-k1-s0-v1 bis -v4): bank.md verlangt bei Ankreuzen ohne Zahloptionen pruef "", aber auch pruef mit Ziffer, wenn die Lösung eine Ziffer trägt; Regelkonflikt, nicht als Befund gezählt.
pruef als bloßer Vorfaktor (e2-k2-s7, e3-k1-s5, e3-k1-s10): passt zum Ergebnis (Leitkoeffizient), prüft aber wenig; nicht als Befund gezählt.
Varianten mit negativem Faktor oder gemischten Formeln innerhalb einer Sprosse (e1-k1-s4-v2, e3-k1-s4) gelten als Zahlunterschied, da die vorigen Sprossen das schon trainieren.

Sauber: 155 Zeilen ohne Befund
