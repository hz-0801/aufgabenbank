# Sprachlauf brueche-dezimalzahlen

Stand 2026-09-28 (Sprachlauf Gruppe 3). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand e32024f. Nur das Feld aufgabe ist geändert;
`python3 werkzeuge/bank-pruef.py brueche-dezimalzahlen`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 69 | 10 | 79 |
| e2.jsonl | 21 | 26 | 47 |
| e3.jsonl | 14 | 27 | 41 |
| e4.jsonl | 34 | 15 | 49 |
| e5.jsonl | 21 | 44 | 65 |
| zone.jsonl | 26 | 4 | 30 |
| gesamt | 185 | 126 | 311 |

Geänderte Sprossen: 68. Die 10 Beispiele sind je Sprosse die erste
geänderte Zeile, gleichmäßig über die Sprossen verteilt (Zone zuerst).

## 10 Beispiele vorher/nachher

1. `brueche-dezimalzahlen-zone-f1-v1` – Teilen und Vervielfachen im Kopf (vierundzwanzig geteilt dur

   vorher: $56 : 7$

   nachher: Berechne. $56 : 7$

2. `brueche-dezimalzahlen-zone-f3-v3` – Kreissektor als Anteil vom Vollkreis (120° von 360°)

   vorher: $45^\circ$ von $360^\circ$ – welcher Anteil vom Vollkreis?

   nachher: Ein Kreissektor (ein Kreisstück) hat einen Winkel von $45^\circ$. Der ganze Kreis hat $360^\circ$. Welcher Anteil des ganzen Kreises ist der Sektor?

3. `brueche-dezimalzahlen-zone-f6-v4` – Schriftlich oder mit Taschenrechner dividieren (drei geteilt

   vorher: $2 : 5$

   nachher: Berechne. $2 : 5$

4. `brueche-dezimalzahlen-e1-k1-s1-v1` – Anteil an gleich geteilter Figur ablesen

   vorher: Welcher Anteil des Streifens ist gefärbt?

   nachher: Der Streifen ist in gleich große Teile geteilt. Welcher Anteil des Streifens ist gefärbt? Gib ihn als Bruch an.

5. `brueche-dezimalzahlen-e1-k2-s2-v1` – Zähler größer als eins (Ganzes : Nenner · Zähler)

   vorher: $\frac{3}{4}$ von $36$

   nachher: Berechne $\frac{3}{4}$ von $36$.

6. `brueche-dezimalzahlen-e1-k4-s3-v1` – Übersetzen von gebrochenen Zahlen (gemeine Brüche und Dezima

   vorher: Schreibe als Bruch: fünf Neuntel.

   nachher: Schreibe fünf Neuntel als Bruch.

7. `brueche-dezimalzahlen-e2-k4-s2-v1` – Begründen (warum Erweitern den Bruch nicht größer macht)

   vorher: Erweitert man $\frac{1}{2}$ mit $3$, stehen größere Zahlen da. Ist der Bruch größer geworden? Begründe.

   nachher: Man erweitert $\frac{1}{2}$ mit $3$. Dann stehen dort größere Zahlen. Ist der Bruch größer geworden? Begründe.

8. `brueche-dezimalzahlen-e4-k1-s1-v1` – Zehnerbruch ↔ Dezimalzahl

   vorher: $\frac{6}{10}$ – als Dezimalzahl?

   nachher: Schreibe $\frac{6}{10}$ als Dezimalzahl.

9. `brueche-dezimalzahlen-e4-k4-s3-v1` – Übersetzen von gebrochenen Zahlen (gemeine Brüche und Dezima

   vorher: Welche Dezimalzahl zeigt der gefärbte Teil des Streifens?

   nachher: Der Streifen ist in gleich große Teile geteilt. Welche Dezimalzahl zeigt der gefärbte Teil?

10. `brueche-dezimalzahlen-e5-k6-s4-v1` – runden auf Zehntel und Hundertstel (auch Größen mit Einheit)

   vorher: Beim 100-m-Lauf brauchen Ali $13{,}4$ s, Ben $13{,}38$ s und Can $13{,}45$ s. Wer ist am schnellsten, wer wird Dritter?

   nachher: Ali, Ben und Can laufen $100$ m. Ali braucht $13{,}4$ s, Ben $13{,}38$ s und Can $13{,}45$ s. Wer ist am schnellsten? Wer wird Dritter?

## Fälle, in denen die Regeln nicht reichten

1. `zone-f1-v1..v4`, `zone-f6-v1..v4` (Teilen im Kopf, schriftlich dividieren): Die Regel sagt
   „Division als Bruch“, das Muster prozentrechnung (zone-f3) hat „$600 : 100$“ zu
   „Berechne. $\frac{600}{100}$“ gemacht. Hier ist das Teilen selbst die geübte Fertigkeit
   („drei geteilt durch acht“), und in einem Bruch-Eintrag würde aus „$7 : 4$“ als
   $\frac{7}{4}$ eine Umwandlungsaufgabe (Schüler antworten dann $1\frac{3}{4}$); bei f1-v4
   (Reihenfolge beim Teilen) und f6-v4 (kleinere durch größere Zahl) ist das Zeichen der
   Fallstrick. Entscheidung: „:“ bleibt, nur „Berechne.“ davor. Ebenso bleibt „:“ in e2-k3
   (Bruch als Geteilt-Aufgabe).
2. Zeilen mit Grafik ohne Angabe, was die Grafik genau ist (`\bruchrechteck`, `\kreisdiagramm`):
   Ob `\bruchrechteck` als Streifen oder als Kästchenrechteck gezeichnet wird, steht nicht in der
   Zeile. Entscheidung: in Kette 1/4 „Streifen“ wie im Bestand (e1-k1-s1-v1), bei den
   Originalformen (e1-k1-s6, e2-k1-s8, e1-k4-s1-v1) „Die Figur besteht aus gleich großen
   Kästchen.“, weil die loesung dort in Kästchen zählt. Sollte die Vorlage `\bruchrechteck`
   anders zeichnen, lohnt ein Blick auf diese Sätze.
3. Fehler-finden-Zeilen, deren Fehler eine Aussage statt einer Rechnung ist (e3-k3-s1,
   e5-k6-s1-v1): feste Form „… und schreibe die Aussage richtig.“ gewählt; bei reinen
   Umwandlungen (zone-f7-v5, e4-k4-s1, e2-k4-s1) „Finde den Fehler und rechne richtig.“, bei
   e5-k6-s1-v3 (Ordnen) „Finde den Fehler und ordne richtig.“ – die Regel kennt nur die ersten
   beiden Formen.
