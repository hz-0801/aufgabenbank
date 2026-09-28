# Sprachlauf lineare-funktionen

Stand 2026-09-28 (Gruppe 2). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py lineare-funktionen`: 0 Abweichungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 45 | 0 | 45 |
| e2.jsonl | 79 | 3 | 82 |
| e3.jsonl | 58 | 0 | 58 |
| e4.jsonl | 40 | 1 | 41 |
| e5.jsonl | 54 | 0 | 54 |
| zone.jsonl | 13 | 13 | 26 |
| gesamt | 289 | 17 | 306 |

Geänderte Sprossen: 82. Die 10 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1 …).

## Entscheidungen

- Das Etikett „Ich finde den Fehler:“ vor Fehler-Aufgaben ist gestrichen; alle
  Fehler-Zeilen haben die feste Form „<Name> soll … <Name> rechnet so / schreibt …
  Finde den Fehler und …“. Wo loesung eine Gleichung, einen Punkt oder m nennt,
  heißt der Schluss „… und gib die richtige Gleichung / den richtigen Punkt / m
  richtig an“ statt „rechne richtig“.
- „:“ als Division wird Bruch: Quotient $\frac{y}{x}$ (Proportionalität) und die
  Steigungsrechnungen in \rechnung (e4 k4 s1). „:“ bleibt nur in „Rechne:
  $(-20) : 5$“ (Zone, die Sprosse übt das Teilen negativer Zahlen). loesung
  schreibt weiter „:“ (nicht angefasst).
- „Rechne: …“ und „Fasse zusammen: …“ (Zone) bleiben als Imperativsatz;
  „Löse: …“ wird „Löse die Gleichung. …“ (loesung zeigt x = …, keine Menge).
- G-Zeilen nennen ihre Darstellung („Das Koordinatensystem zeigt …“, „Die
  Tabelle zeigt …“), Zeichenaufträge nennen „in das Koordinatensystem“.
- „y ist der Preis in €, x die Anzahl der Einheiten“ wird je Sachlage konkret
  („Für x Stunden zahlt man y Euro.“); das ändert keine Lösung.
- Das Zahlwerkzeug verlangt, dass jede Zahl so oft stehen bleibt wie vorher.
  Wo ein Stichwort-Kopf eine Zahl doppelte („Preis für 5 kg? … 5 kg?“), steht
  sie jetzt in einem Lage-Satz („Tim kauft 5 kg Äpfel. Wie viel kosten die 5 kg?“).
- Fachwörter bleiben, wo die Sprosse sie übt (Steigung m, y-Achsenabschnitt n,
  Steigungsdreieck, Nullstelle, Quotient, proportional, Dreisatz, Anstieg im
  Original 2019); „Kostenvoranschlag“ und „Vieltelefonierer“ sind umschrieben,
  „Weise nach“ wird „Zeige mit einer Rechnung“.
- Unverändert: 17 Zeilen (Zone „Rechne:“/„Fasse zusammen:“, e2 k7 s2 „Welche
  Gerade ist steiler: … oder …? Begründe ohne Rechnung.“, e4 k4 s2 v1).

## 10 Beispiele

1. `lineare-funktionen-zone-f1-v1` – Koordinaten lesen und eintragen, 4 Quadranten, (x|y)-Reihenf

   vorher: Punkt A – welche Koordinaten? Lies ab.

   nachher: Das Koordinatensystem zeigt den Punkt A. Lies die Koordinaten von A ab.

2. `lineare-funktionen-zone-f5-v4` – Lineare Gleichung zweischrittig lösen (null gleich einem zwe

   vorher: Löse: $0 = -0{,}2x + 6$

   nachher: Löse die Gleichung. $0 = -0{,}2x + 6$

3. `lineare-funktionen-e1-k1-s8-v1` – zu einem Sachverhalt die Gleichung aufstellen, den Graphen z

   vorher: Wasser im Becken: In ein leeres Becken laufen je Minute 12 Liter Wasser. Stelle eine Gleichung für die Wassermenge y (in Litern) nach x Minuten auf, zeichne den Graphen für 0 bis 5 Minuten und erkläre, was der Faktor im Sachzusammenhang bedeutet.

   nachher: In ein leeres Becken laufen in jeder Minute 12 Liter Wasser. Nach x Minuten sind y Liter im Becken. Stelle eine Gleichung für y auf. Zeichne den Graphen für 0 bis 5 Minuten in das Koordinatensystem. Erkläre, was der Faktor in deiner Gleichung für das Becken bedeutet.

4. `lineare-funktionen-e2-k4-s1-v1` – Wertetabelle aus Gleichung

   vorher: Wertetabelle: Fülle die Tabelle zu $f(x) = 3x - 2$ aus.

   nachher: Fülle die Wertetabelle zu $f(x) = 3x - 2$ aus.

5. `lineare-funktionen-e2-k5-s2-v1` – m ablesen ganzzahlig

   vorher: m? Lies die Steigung m der Geraden g mit einem Steigungsdreieck ab.

   nachher: Das Koordinatensystem zeigt die Gerade g. Lies ihre Steigung m mit einem Steigungsdreieck ab.

6. `lineare-funktionen-e3-k2-s1-v1` – x positiv ganz

   vorher: $f(4)$? Berechne den Funktionswert von $f(x) = 2x + 5$ an der Stelle $x = 4$.

   nachher: Setze $x = 4$ in $f(x) = 2x + 5$ ein. Berechne so den Funktionswert $f(4)$.

7. `lineare-funktionen-e3-k5-s1-v1` – Fehler finden

   vorher: Ich finde den Fehler: Sara soll die Nullstelle von $f(x) = 2x - 6$ angeben und schreibt: Die Nullstelle ist $-6$. Benenne den Fehler und rechne richtig.

   nachher: Sara soll die Nullstelle von $f(x) = 2x - 6$ angeben. Sie schreibt: „Die Nullstelle ist $-6$.“ Finde den Fehler und rechne richtig.

8. `lineare-funktionen-e4-k1-s6-v1` – Prüfungshöhe: zwei Punkte mit Bruch-m

   vorher: Gerade durch A und B: Zeichne die Gerade f durch $A(-2|8)$ und $B(4|-1)$, entscheide für jede Aussage, ob sie wahr oder falsch ist, und gib eine Gleichung von f an. (P10 2025 OS) \\ \kreuz{wahr}\kreuz{falsch} f verläuft monoton steigend. \\ \kreuz{wahr}\kreuz{falsch} f schneidet die y-Achse in $(0|5)$.

   nachher: Zeichne die Gerade f durch $A(-2|8)$ und $B(4|-1)$ in das Koordinatensystem. Kreuze bei jeder Aussage an, ob sie wahr oder falsch ist. Gib dann eine Gleichung von f an. (P10 2025 OS) \\ \kreuz{wahr}\kreuz{falsch} f verläuft monoton steigend. \\ \kreuz{wahr}\kreuz{falsch} f schneidet die y-Achse in $(0|5)$.

9. `lineare-funktionen-e5-k1-s2-v1` – Gleichung aufstellen

   vorher: Stelle eine Gleichung auf: Ein Kino-Abo kostet einmalig 10 € und 6 € je Film. y sind die Kosten in €, x die Anzahl der Filme.

   nachher: Ein Kino-Abo kostet einmalig 10 € und dazu 6 € je Film. Für x Filme zahlt man y Euro. Stelle eine Gleichung für y auf.

10. `lineare-funktionen-e5-k4-s4-v1` – Endwert berechnen

   vorher: Wie weit reicht das Geld? Für die Klassenfahrt kostet ein Bus 180 € Grundpreis und 1{,}90 € je km. Die Klasse hat 600 € für den Bus. Wie viele Kilometer (hin und zurück) sind höchstens drin?

   nachher: Für die Klassenfahrt kostet ein Bus 180 € Grundpreis und 1{,}90 € je km. Die Klasse hat 600 € für den Bus. Wie viele Kilometer kann der Bus höchstens fahren, hin und zurück zusammen?
