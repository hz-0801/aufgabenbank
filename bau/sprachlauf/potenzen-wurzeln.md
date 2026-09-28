# Sprachlauf potenzen-wurzeln

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Vergleich gegen den Bankstand 1917549. Nur das Feld aufgabe ist geändert (Skriptprobe: alle anderen Felder gleich, keine Zahl verloren, keine neue Zahl). `python3 werkzeuge/bank-pruef.py potenzen-wurzeln`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 76 | 3 | 79 |
| e2.jsonl | 61 | 7 | 68 |
| e3.jsonl | 61 | 3 | 64 |
| zone.jsonl | 46 | 0 | 46 |
| gesamt | 244 | 13 | 257 |

## 10 Beispiele

1. `potenzen-wurzeln-e1-k1-s0-v1` – „Plus oder minus?“ – zu Potenzen mit negativer Basis und mit Minus vor

   vorher: $(-5)^4$ – plus oder minus?\\ \kreuz{positiv} \\ \kreuz{negativ}

   nachher: Kreuze an, ob $(-5)^4$ positiv oder negativ ist.\\ \kreuz{positiv} \\ \kreuz{negativ}

2. `potenzen-wurzeln-e2-k1-s0-v1` – „groß oder klein“ und „Stellen oder Nullen“ ankreuzen (Vorstufe)

   vorher: $4{,}7 \cdot 10^{8}$ – größer oder kleiner als eins?\\ \kreuz{größer als eins} \\ \kreuz{kleiner als eins}

   nachher: Kreuze an, ob $4{,}7 \cdot 10^{8}$ größer oder kleiner als eins ist.\\ \kreuz{größer als eins} \\ \kreuz{kleiner als eins}

3. `potenzen-wurzeln-e3-k1-s0-v1` – „Was zuerst?“ – bei Termen mit Wurzel und Quadrat markieren, was zuers

   vorher: $\sqrt{(-7)^2}$ – was zuerst?\\ \kreuz{erst die Wurzel} \\ \kreuz{erst das Quadrat}

   nachher: Kreuze an, was du bei $\sqrt{(-7)^2}$ zuerst rechnest.\\ \kreuz{erst die Wurzel} \\ \kreuz{erst das Quadrat}

4. `potenzen-wurzeln-zone-f1-v1` – Kleines Einmaleins und Malnehmen mehrstelliger Zahlen im Kopf oder hal

   vorher: $7 \cdot 8$ – wie viel?

   nachher: Berechne $7 \cdot 8$.

5. `potenzen-wurzeln-e1-k3-s6-v1` – Minus vor der Potenz ohne Klammer

   vorher: $-8^2$ – wie viel?

   nachher: Berechne $-8^2$.

6. `potenzen-wurzeln-e2-k1-s8-v1` – fehlende Hochzahl eintragen (P10-Form)

   vorher: $64\,000 = 6{,}4 \cdot 10^{\square}$ – welche Hochzahl?

   nachher: Setze die fehlende Hochzahl in das Kästchen ein. $64\,000 = 6{,}4 \cdot 10^{\square}$

7. `potenzen-wurzeln-e3-k2-s7-v1` – Wurzel eines Quadrats mit negativer Basis: erst das Quadrat

   vorher: $\sqrt{(-8)^2}$ – wie viel?

   nachher: Berechne $\sqrt{(-8)^2}$.

8. `potenzen-wurzeln-zone-f9-v1` – Runden von Dezimalzahlen auf eine und zwei Stellen, Näherungswert mit 

   vorher: $4{,}372$ – auf eine Stelle nach dem Komma gerundet?

   nachher: Runde $4{,}372$ auf eine Stelle nach dem Komma.

9. `potenzen-wurzeln-e1-k3-s14-v1` – Potenz mit negativer Hochzahl gegen Dezimalzahl vergleichen (P10-Form)

   vorher: $4^{-3} \;\square\; 0{,}02$ – $<$, $=$ oder $>$?

   nachher: Setze das passende Zeichen $<$, $=$ oder $>$ ein. $4^{-3} \;\square\; 0{,}02$

10. `potenzen-wurzeln-e2-k1-s16-v1` – Zehnerpotenzen multiplizieren und dividieren (Vorrat)

   vorher: $10^{4} \cdot 10^{3}$ – als Zehnerpotenz?

   nachher: Schreibe $10^{4} \cdot 10^{3}$ als eine Zehnerpotenz.

## Wo die Regeln nicht reichten

# Wo die Regeln nicht reichten (potenzen-wurzeln)

- e1-k3-s10/s11/s12 und s15-v1..v4 (Exponent gesucht, $5^x = 625$): Das sind Gleichungen, aber loesung schreibt „also $x = 4$“ und nicht die Lösungsmenge. Entscheidung: keine Frage nach der Lösungsmenge, sondern „Welche Zahl muss für $x$ stehen, damit $5^x = 625$ stimmt?“.
- e2-k2-s1-v1..v3 (Fehler finden beim Umschreiben in und aus der Zehnerpotenzschreibweise): Die feste Form „rechne richtig“ passt nur halb, weil die Kinder eine Zahl umschreiben und nicht rechnen. Entscheidung: feste Form beibehalten („Er schreibt so: … Finde den Fehler und rechne richtig.“), damit die Satzform überall gleich bleibt.
- e1-k7-s1-v3 und e3-k3-s1-v3 (falsche Aussage statt falscher Rechnung): Die Form „Fehler finden“ passte vom Inhalt her, „Begründe, ob … recht hat“ ebenfalls. Entscheidung: Fehler-finden-Form mit „… und schreibe die Aussage richtig.“, weil die Sprosse „Fehler finden“ heißt. „nicht definiert“ (Nils) wurde zu „hat keinen Wert“, passend zur Lösung und zu e3-k2-s8.
- e2-k1-s14 (Runden in Zehnerpotenzschreibweise): „Faktor“ übt die Sprosse nicht, und „vor $\cdot 10$“ hätte eine neue Zahl gebracht. Entscheidung: „Runde die Zahl vor dem Malpunkt auf … Stellen nach dem Komma.“
- e3-k2-s13-v11/v12 (Nullstellen mit der p-q-Formel, Original 2025-OS-K5c): Das Original fragt nach „Schnittpunkten mit der x-Achse“, die Lösung gibt $x_1$, $x_2$. Entscheidung: „Berechne die Nullstellen von … mit der p-q-Formel.“; Fachwort und Verfahrensname bleiben, weil die Aufgabe ohne sie nicht lösbar gestellt ist. Division „:“ wurde in aufgabe als \frac geschrieben (e3-k2-s11-v3, e2-k1-s16-v2, zone-f6-v2/v4, zone-f8-v2/v5); in loesung steht weiter „:“ (nicht angefasst).
