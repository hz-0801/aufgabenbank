# Gegenlese: geraden

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung), unabhängige Gegenlese
Geprüfte Zeilen: 173 (zone 30, e1 39, e2 44, e3 29, e4 31)
Korrekturen: 0

Alle Lösungszahlen und pruef-Werte mit Python/sympy aus der Aufgabe
nachgerechnet; bank-pruef.py: 0 Abweichungen.

## Entscheidungen

- Korrigiert wird nur eine falsche Zahl mit eindeutiger Korrektur.
  Ein pruef, der eine richtige Lösung nur teilweise abdeckt, und
  eine schiefe Aussage in einer Beschreiben-/Begründen-Lösung
  stehen als Befund unter Punkt 1.
- Eine Zeile mit Befunden unter mehreren Punkten steht unter jedem.

## Befunde

### Punkt 1 – Lösung rechnerisch richtig

- geraden-e2-k2-s1-v1: Lösung (Verhältnis 3 : 2) stimmt, pruef [0.6, 3] prüft den zweiten Teil nicht – pruef [0.6, 3, 2].
- geraden-e4-k1-s4-v1: Zusatz „eine Höhendifferenz, kein Lotabstand zu einer Ebene“ ist irreführend, beim waagerechten Dach ($x_3 = 4$) ist die Höhendifferenz genau der Lotabstand – Zusatz streichen, in aufgabe „wie hoch über dem Dach“ wie in v2.

### Punkt 2 – eindeutig lösbar

- geraden-e1-k1-s0-v1: Lösung deutet $r = 0$ als „am Boden“, die Aufgabe sagt nicht, dass die $x_1x_2$-Ebene der Boden ist – in der Aufgabe ergänzen oder Lösung auf „$r = 0$ Anfang, $r = 1$ Ende“ beschränken.
- geraden-e2-k3-s3-v3: Ergebnis ≈ 140,2 m nicht ganzzahlig, die Aufgabe nennt keine Rundung – „Runde auf 0,1 m.“ ergänzen.

### Punkt 3 – passt zu sprosse_text und merkmal

- geraden-zone-f2-v2: fragt einen Betrag, das Merkmal ist „Verbindungsvektor als Differenz Ende minus Anfang“ – durch einen Verbindungsvektor ersetzen.
- geraden-zone-f6-v2: fragt den Anstieg aus zwei Punkten, das Merkmal ist „Anstieg und Achsenabschnitt aus der Gleichung“ – durch Ablesen von $m$ und $n$ aus einer Gleichung ersetzen.
- geraden-zone-f7-v2: fragt eine Maßstabsumrechnung, das Merkmal ist „Steigung in Prozent aus glatten Längen“ – durch eine Steigungsaufgabe ersetzen.
- geraden-e1-k2-s2-v2: Gleichung ist vorgegeben, das „schreiben“ der Sprosse fällt weg (v1 stellt sie aus zwei Punkten auf) – Start- und Zielpunkt geben, Gleichung aufstellen und deuten lassen.
- geraden-e1-k2-s2-v3: wie v2, Gleichung vorgegeben – wie v2.
- geraden-e1-k3-s3-v2: Sprosse verlangt „Gleichung … angeben“, die Aufgabe fragt nur die Höhe – „Gib eine Gleichung der Bahn der Last an und …“ ergänzen.
- geraden-e2-k3-s3-v1: umgekehrte Richtung (aus der Höhe den Punkt), die Sprosse verlangt Höhe aus der Entfernung – umdrehen: Entfernung geben, Höhe erfragen.
- geraden-e2-k3-s3-v3: umgekehrte Richtung (aus der Höhe die Entfernung) – umdrehen wie v1.
- geraden-e3-k1-s0-v3: fragt direkt „Welche Lage?“, das Merkmal verlangt den nächsten Prüfschritt (so v1) – als Frage nach dem nächsten Prüfschritt stellen.
- geraden-e3-k1-s0-v4: fragt die Endentscheidung statt des nächsten Prüfschritts – etwa „Gemeinsamer Stützpunkt – was ist noch zu prüfen?“.
- geraden-e4-k1-s4-v1: Sprosse und Merkmal verlangen Weg beschreiben und vorgelegten Ansatz deuten, v1 enthält nur das Beschreiben – jede Variante mit beiden Teilen bauen.
- geraden-e4-k1-s4-v2: nur Beschreiben – wie v1.
- geraden-e4-k1-s4-v3: nur Deuten, kein mehrschrittiger Weg – wie v1.
- geraden-e4-k1-s4-v4: nur Deuten – wie v1.
- geraden-e4-k3-s1-v1: Merkmal „eigene Zahlen“, die Aufgabe hat weder Zahlen noch Geraden, daher keine richtige Rechnung in der Lösung – konkrete $g$, $h$ mit Janas falschem Wert vorgeben, richtigen senkrechten Abstand ausrechnen.
- geraden-e4-k3-s1-v3: ohne eigene Zahlen (anders als v2) – konkrete Schiene, Richtung und Zielpunkt einsetzen.

### Punkt 4 – Schreibform

- geraden-e2-k3-s3-v3: Lösung nennt $|\overrightarrow{EF}| \approx 200{,}2$ m und rechnet mit $200{,}25$ weiter (mit $200{,}2$ käme $140{,}1$) – einheitlich $\approx 200{,}25$ m oder ungerundet $0{,}7 \cdot \sqrt{40\,100}$.

### Punkt 5 – Ankreuzen

keine

### Punkt 6 – Fehler finden

- geraden-e3-k2-s1-v3: Tims Ergebnis „windschief“ stimmt, falsch ist nur die Begründung; wer nachrechnet, findet kein falsches Ergebnis (anders als v1/v2) – $h$ so wählen, dass sich $g$ und $h$ schneiden, etwa $h\colon \vec x = (2 | 1 | -1) + t \cdot (0 | 1 | 1)$ (Schnitt in $(2 | 3 | 1)$), loesung und pruef anpassen.

Sauber: 153 Zeilen ohne Befund
