# Sprachlauf terme

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Vergleich gegen den Bankstand 3edb7ad. Nur das Feld aufgabe ist geändert (Skriptprobe: alle anderen Felder gleich, keine Zahl verloren, keine neue Zahl). `python3 werkzeuge/bank-pruef.py terme`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 33 | 6 | 39 |
| e2.jsonl | 20 | 61 | 81 |
| e3.jsonl | 18 | 18 | 36 |
| e4.jsonl | 6 | 23 | 29 |
| zone.jsonl | 1 | 17 | 18 |
| gesamt | 78 | 125 | 203 |

## 10 Beispiele

1. `terme-e1-k1-s1-v1` – passenden Term ankreuzen (3×) [INKL]

   vorher: Das Vierfache einer Zahl $x$, um 1 vermindert – welcher Term passt? \\ \kreuz{$4x - 1$} \\ \kreuz{$4 \cdot (x - 1)$} \\ \kreuz{$1 - 4x$}

   nachher: Das Vierfache einer Zahl $x$ wird um 1 vermindert. Kreuze den Term an, der dazu passt. \\ \kreuz{$4x - 1$} \\ \kreuz{$4 \cdot (x - 1)$} \\ \kreuz{$1 - 4x$}

2. `terme-e2-k2-s0-v1` – Vorzahl lesen: „Welche Vorzahl hat x? −t? 0,5y?" (x = 1x, −t = −1t)

   vorher: $a$ – Vorzahl?

   nachher: Welche Vorzahl hat $a$?

3. `terme-e3-k1-s0-v1` – Zeichen vor der Klammer feststellen: „Steht vor der Klammer + oder − o

   vorher: $7 + (a - 2)$ – was steht vor der Klammer?

   nachher: Was steht im Term $7 + (a - 2)$ direkt vor der Klammer?

4. `terme-e4-k1-s7-v1` – Fehler finden: Faktor nur aus einem Glied gezogen

   vorher: Finde den Fehler und rechne richtig: \rechnung{5x + 20 &= 5 \cdot (x + 20)}

   nachher: Nora soll im Term $5x + 20$ den größten gemeinsamen Faktor ausklammern. Sie rechnet so: \rechnung{5x + 20 &= 5 \cdot (x + 20)} Finde den Fehler und rechne richtig.

5. `terme-zone-f1-v5` – Addieren und Subtrahieren negativer Zahlen (3 − 7, −2 − 5)

   vorher: Finde den Fehler und rechne richtig: \rechnung{-7 - 5 &= -2}

   nachher: Tim soll $-7 - 5$ berechnen. Er rechnet so: \rechnung{-7 - 5 &= -2} Finde den Fehler und rechne richtig.

6. `terme-e1-k3-s1-v1` – Situation zu Term angeben

   vorher: Erfinde eine Situation, zu der der Term $12 + 3x$ passt. Wofür steht $x$? Was bedeutet der Termwert für $x = 2$?

   nachher: Erfinde eine Situation aus dem Alltag, zu der der Term $12 + 3x$ passt. Schreibe auf, wofür $x$ steht. Berechne den Term für $x = 2$ und erkläre, was das Ergebnis bedeutet.

7. `terme-e2-k6-s2-v1` – Begründen (zusammenfassbar oder nicht)

   vorher: Kann man $4x + 4y$ zusammenfassen? Begründe.

   nachher: Begründe, ob man den Term $4x + 4y$ zusammenfassen kann.

8. `terme-e3-k3-s1-v1` – Fehler finden

   vorher: Finde den Fehler und rechne richtig: \rechnung{12 - (a - 5) &= 12 - a - 5 \\ &= 7 - a}

   nachher: Jan soll die Klammer in $12 - (a - 5)$ auflösen. Er rechnet so: \rechnung{12 - (a - 5) &= 12 - a - 5 \\ &= 7 - a} Finde den Fehler und rechne richtig.

9. `terme-e4-k2-s1-v1` – Fehler finden

   vorher: Finde den Fehler und rechne richtig: \rechnung{12x - 8 &= 4 \cdot (3x + 2)}

   nachher: Finn soll im Term $12x - 8$ den größten gemeinsamen Faktor ausklammern. Er rechnet so: \rechnung{12x - 8 &= 4 \cdot (3x + 2)} Finde den Fehler und rechne richtig.

10. `terme-e1-k2-s1-v1` – Termwert berechnen (auch negative Einsetzung)

   vorher: $4x - 3$ für $x = 5$ – Termwert?

   nachher: Berechne den Wert des Terms $4x - 3$ für $x = 5$.

## Wo die Regeln nicht reichten

# Wo die Regeln nicht reichten (terme)

- terme-e1-k1-s1-v3, e1-k1-s6-v3, e1-k1-s7-v1/v2: Divisionen als „$x : 2 + 5$“ bzw. „$(4x + 9) : 2$“ stehen in \kreuz-Optionen und in loesung. Regel 4 verlangt \frac, der Auftrag lässt Bausteine aber unverändert (Ausnahme nur \rechnung), und loesung darf sich nicht ändern. Entschieden: „:“ in \kreuz stehen gelassen; bei den Originalen (2023-OS-B1h) ist „:“ ohnehin der Wortlaut. Sollte das Blatt \frac wollen, müssen kreuz und loesung gemeinsam geändert werden.
- Reine Rechenaufgaben mit Verb und Doppelpunkt („Fasse zusammen: $…$“, „Multipliziere: $…$“, „Löse die Klammer auf: $…$“, „Rechne: $…$“, „Klammere … aus: $…$“, zusammen über 100 Zeilen): Regel 3 zeigt „Berechne.“ mit Punkt, Regel 1 erlaubt den Doppelpunkt vor einer Rechnung. Entschieden: als gute Zeilen unverändert gelassen, kein Punkt-Umbau nur der Form wegen.
- terme-e1-k3-s1-v1..v3 (Situation zu Term): Die Sprosse verlangt drei Ergebnisse (Situation, Bedeutung von $x$, Bedeutung des Werts). Regel 2 erlaubt zwei Fragen nur bei zwei Ergebnissen. Entschieden: drei kurze Aufforderungen statt Fragen; „Termwert“ durch „Berechne den Term für $x = …$“ ersetzt.
- terme-e3-k2-s6/s7: Text sagte nur „Löse die Klammer auf“, loesung ist aber zusammengefasst (Sprosse „auflösen und zusammenfassen“). Entschieden: „und fasse zusammen“ ergänzt (bei s7 „Klammern“ im Plural) – keine Hilfe, sondern der Auftrag, den die Lösung schon voraussetzt.
- Fehler-finden-Zeilen ohne Namen (e2-k6-s1, e3-k3-s1, e4-k1-s7, e4-k2-s1, zone-f1-v5): Die feste Satzform braucht einen Namen und ein „soll …“. Entschieden: Namen ergänzt, Auftrag aus dem linken Term der \rechnung abgeleitet; bei e4 „den größten gemeinsamen Faktor ausklammern“, weil die Sprosse das Ausklammern übt.
