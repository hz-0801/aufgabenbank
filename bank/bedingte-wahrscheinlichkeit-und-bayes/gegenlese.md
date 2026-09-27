# Gegenlese: bedingte-wahrscheinlichkeit-und-bayes

Datum: 2026-09-27  
Modell: Claude in Claude Code (Web-Sitzung); die genaue Modellkennung darf laut Sitzungsvorgabe nicht ins Repo, sie steht im Chatbericht  
Geprüfte Zeilen: 115  
Korrekturen: 0

## Festlegungen dieser Gegenlese

- Jede Zeile einzeln nachgerechnet (Python mit sympy/scipy), aus dem Aufgabentext; bank.md nur für die Felder, stand.md nicht gelesen.
- Korrigiert wird nur, wenn loesung selbst rechnerisch falsch ist und die Korrektur eindeutig in loesung/pruef liegt. Ein unvollständiges pruef bei richtiger loesung ist ein Befund unter Punkt 1, keine Korrektur.
- Widerspricht die Lösung einer Grafik oder dem Aufgabentext und ließe sich das an Aufgabe, Grafik oder Lösung beheben, ist die Korrektur nicht eindeutig: Befund, keine Änderung.
- Korrigierte Zeilen stehen unter Punkt 1 mit „korrigiert“ und zählen nicht als sauber. Eine Zeile mit mehreren Befunden steht unter jedem Punkt einmal.
- Aufgerundete Höchstwerte (e3-k2-s3-v1/v2) nicht korrigiert: Die Korrektur ist nicht eindeutig (abrunden auf 4 Stellen oder mehr Stellen angeben), und pruef müsste dann abweichend vom Rundungsprinzip des Prüfskripts gesetzt werden.

## Befunde

### 1 Lösung und pruef

- bedingte-wahrscheinlichkeit-und-bayes-e1-k2-s2-v3: „Gleich nur, wenn A und B gleich wahrscheinlich“ stimmt nicht: bei P(A ∩ B) = 0 sind beide Werte 0 – Zusatz „(bei P(A ∩ B) > 0)“
- bedingte-wahrscheinlichkeit-und-bayes-e2-k2-s3-v1: Lösung nennt nur die vier inneren Felder; die Ränder der Tafel (0,05; 0,95; 0,14; 0,86; 1) fehlen – Randwerte in der Lösung ergänzen
- bedingte-wahrscheinlichkeit-und-bayes-e3-k2-s3-v1: Höchstwert aufgerundet: w = 0,0096 ergibt 0,4999 < 0,5, erfüllt die Bedingung nicht – Abrunden (w ≤ 0,0095 bzw. ≤ 0,00959); Rundung im pruef entsprechend
- bedingte-wahrscheinlichkeit-und-bayes-e3-k2-s3-v2: Höchstwert aufgerundet: k = 0,0066 ergibt 1,0001 % > 1 %, erfüllt die Bedingung nicht – Abrunden (k ≤ 0,0065 bzw. ≤ 0,00659); Rundung im pruef entsprechend

### 2 Eindeutig lösbar

- bedingte-wahrscheinlichkeit-und-bayes-zone-f5-v3: h(4) = 0,8 liegt zwischen Gitterlinien (y-Karo 1), am Graphen nicht sicher ablesbar – Bereich 0 ≤ x ≤ 3 (h(3) = 1) oder feinere y-Einteilung (ystep=0.2)
- bedingte-wahrscheinlichkeit-und-bayes-e3-k1-s2-v3: Text beginnt mit „Weiterhin“ und verweist auf einen Vorlauf, den es nicht gibt – „Weiterhin“ streichen

### 3 Sprosse und Merkmal

- bedingte-wahrscheinlichkeit-und-bayes-zone-f2-v2: Grundfall-Variante verlangt die Summe über zwei Pfade; das ist das Merkmal der Sprosse 4 (f2-v5); v1 fragt nur einen Pfad – Auch hier nur einen Pfad (Produkt) erfragen
- bedingte-wahrscheinlichkeit-und-bayes-zone-f5-v2: Fragt schon die Stelle zu einem Funktionswert; genau der Fallstrick der Sprosse 3 (f5-v4), die dann nichts Neues bringt – Wie v1 einen Funktionswert zu einer Stelle erfragen
- bedingte-wahrscheinlichkeit-und-bayes-e3-k1-s1-v5: Kein Bayes-Baum mit Parameter, sondern dreistufiges Experiment mit Gegenereignis und Schnitt „mindestens eines, nicht alle“; anderes Merkmal, deutlich schwerer als v1–v4 – Auf höhere Sprosse verschieben oder durch einen Bayes-Term mit Parameter ersetzen

### 4 Schreibform

- keine

### 5 Ankreuzen

- keine

### 6 Fehler finden

- keine

Sauber: 106 Zeilen ohne Befund
