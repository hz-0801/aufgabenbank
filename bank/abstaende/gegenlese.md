# Gegenlese: abstaende

Datum: 2026-09-27  
Modell: Claude in Claude Code (Web-Sitzung); die genaue Modellkennung darf laut Sitzungsvorgabe nicht ins Repo, sie steht im Chatbericht  
Geprüfte Zeilen: 174  
Korrekturen: 0

## Festlegungen dieser Gegenlese

- Jede Zeile einzeln nachgerechnet (Python mit sympy/scipy), aus dem Aufgabentext; bank.md nur für die Felder, stand.md nicht gelesen.
- Korrigiert wird nur, wenn loesung selbst rechnerisch falsch ist und die Korrektur eindeutig in loesung/pruef liegt. Ein unvollständiges pruef bei richtiger loesung ist ein Befund unter Punkt 1, keine Korrektur.
- Widerspricht die Lösung einer Grafik oder dem Aufgabentext und ließe sich das an Aufgabe, Grafik oder Lösung beheben, ist die Korrektur nicht eindeutig: Befund, keine Änderung.
- Korrigierte Zeilen stehen unter Punkt 1 mit „korrigiert“ und zählen nicht als sauber. Eine Zeile mit mehreren Befunden steht unter jedem Punkt einmal.

## Befunde

### 1 Lösung und pruef

- abstaende-e1-k3-s3-v1: pruef liefert Strecke (1921 m) und Sekunden (384 s), nicht die im Antwortgerüst gefragten 6,4 min – pruef um math.sqrt(3690000)/300 ergänzen oder Antwortgerüst auf Sekunden umstellen
- abstaende-e4-k1-s5-v3: pruef liefert nur z ≈ 2,10, Antwortgerüst und Lösung verlangen R(2 | 2 | 2,10); anders als v1 ([[5,3,7/3]]) – pruef: [[2,2,(6-0.5*math.sqrt(13))/2]]

### 2 Eindeutig lösbar

- abstaende-e1-k2-s3-v3: Keine Rundungsangabe für die Entfernung zum Startplatz (√312500 ≈ 559,02 m) – „Runde auf ganze Meter.“ ergänzen
- abstaende-e1-k3-s3-v1: Keine Rundungsangabe für die Fahrzeit in Minuten (6,40 min) – „Runde auf Zehntel Minuten.“ ergänzen
- abstaende-e1-k3-s3-v2: Bezugspunkt der Funkreichweite nicht genannt; die Lösung misst stillschweigend vom Startpunkt S – „Die Fernsteuerung bleibt in S; ihre Funkreichweite beträgt 500 m.“
- abstaende-e2-k1-s3-v2: Jeder Punkt mit Abstand 7 zu E erfüllt die Bedingung; die Lösung nennt nur zwei Punkte auf dem Lot durch (2 | 1 | 0) – P auf der Lotgeraden durch (2 | 1 | 0) verlangen oder Lösung mit „z. B.“ als Beispiel kennzeichnen
- abstaende-e3-k1-s2-v1: Frage „Welche Bedeutung hat Q für diesen Wert?“ ist unklar formuliert; A, B, E nicht als Punkte eingeführt (E steht sonst für Ebenen) – „A, B, E sind Punkte des Gestänges … Welche Bedeutung hat der Punkt Q, der sich mit diesem r ergibt?“
- abstaende-e3-k1-s2-v3: „Welcher Punkt ist F?“ lässt offen, ob Deutung oder Koordinaten gefragt sind; Lösung und pruef verlangen Koordinaten – Fragen: „Was beschreibt II? Deute F und berechne seine Koordinaten.“

### 3 Sprosse und Merkmal

- abstaende-zone-f1-v2: Variante fragt nur den Betrag eines gegebenen Vektors; das Bilden des Verbindungsvektors (Merkmal, v1) entfällt – Zwei Punkte vorgeben und Verbindungsvektor samt Länge fragen, z. B. A(1 | 0 | 2), B(1 | 3 | 6)
- abstaende-zone-f5-v1: Variante fragt nur das Skalarprodukt; der Test auf senkrecht aus Merkmal und v2 fehlt – „– senkrecht?“ ergänzen, Antwort „__ \janein“, Lösung „5 – nein“
- abstaende-e3-k1-s4-v3: Variante verlangt Erläutern eines vorgelegten Rechenwegs, v1/v2 eigenes Rechnen; Tätigkeit ändert sich, Form „teil“ passt nicht zur Erläuterung – Als Rechenaufgabe wie v1/v2 fassen oder form „text“ und Erläutern-Charakter der Sprosse einheitlich festlegen

### 4 Schreibform

- keine

### 5 Ankreuzen

- keine

### 6 Fehler finden

- keine

Sauber: 164 Zeilen ohne Befund
