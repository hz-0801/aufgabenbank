# Sprachlauf prozentrechnung

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Skript:
bau/sprachlauf/sprachlauf_prozentrechnung.py (alle neuen Texte
stehen dort). Vergleich gegen den Bankstand d86851d. Nur das Feld
aufgabe ist geändert; `python3 werkzeuge/bank-pruef.py
prozentrechnung`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 43 | 4 | 47 |
| e2.jsonl | 56 | 1 | 57 |
| e3.jsonl | 45 | 3 | 48 |
| e4.jsonl | 37 | 4 | 41 |
| e5.jsonl | 48 | 4 | 52 |
| zone.jsonl | 32 | 0 | 32 |
| gesamt | 261 | 16 | 277 |

Geänderte Sprossen: 97. Die 25 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1–e5).

## 25 Beispiele

1. `prozentrechnung-zone-f1-v1` – Bruch als Anteil lesen und kürzen (drei von zwölf, gekürzt e

   vorher: $6$ von $10$ Bonbons sind rot – welcher Anteil? Kürze.

   nachher: In einer Tüte sind $10$ Bonbons. $6$ davon sind rot. Schreibe den Anteil der roten Bonbons als Bruch und kürze ihn.

2. `prozentrechnung-zone-f2-v1` – Bruch ↔ Dezimalzahl (ein Viertel, drei Fünftel)

   vorher: $\frac{1}{2}$ als Dezimalzahl?

   nachher: Schreibe $\frac{1}{2}$ als Dezimalzahl.

3. `prozentrechnung-zone-f3-v1` – Durch hundert teilen, mit Dezimalzahlen multiplizieren (Komm

   vorher: $600 : 100$

   nachher: Berechne. $\frac{600}{100}$

4. `prozentrechnung-zone-f4-v1` – Hoch- und Runterrechnen in einer Tabelle (Dreisatz, proporti

   vorher: $2$ Kinokarten kosten $18\,€$ – wie viel kosten $5$ Karten?

   nachher: $2$ Kinokarten kosten $18\,€$. Berechne mit der Tabelle, wie viel $5$ Kinokarten kosten.

5. `prozentrechnung-zone-f5-v1` – Runden auf eine Dezimalstelle

   vorher: $4{,}73$ – auf eine Dezimalstelle?

   nachher: Runde $4{,}73$ auf eine Stelle nach dem Komma.

6. `prozentrechnung-zone-f6-v1` – Bruchteil einer Größe (zwei Drittel von 60 €)

   vorher: $\frac{1}{4}$ von $20\,€$

   nachher: Berechne $\frac{1}{4}$ von $20\,€$.

7. `prozentrechnung-zone-f6-v6` – Bruchteil einer Größe (zwei Drittel von 60 €)

   vorher: Von $40\,€$ ist ein Fünftel ausgegeben – wie viel ist übrig? Ben rechnet: $40 : 5 = 8$, übrig sind $8\,€$. Wo ist der Fehler?

   nachher: Von $40\,€$ ist ein Fünftel ausgegeben. Ben soll ausrechnen, wie viel Euro übrig sind. Er rechnet: $\frac{40}{5} = 8$. Dann sagt er: „Übrig sind $8\,€$.“ Finde den Fehler und rechne richtig.

8. `prozentrechnung-e1-k1-s3-v1` – Nenner, der in hundert aufgeht, erweitern

   vorher: $\frac{11}{20}$ – wie viel Prozent?

   nachher: Schreibe den Bruch $\frac{11}{20}$ in Prozent.

9. `prozentrechnung-e1-k1-s7-v1` – Prüfungshöhe: zu einer Prozentangabe die passende Anteilsaus

   vorher: $5\,\%$ der Pakete kommen zu spät – welche Aussage passt? Kreuze an. (P10 2020 OS)\\ \kreuz{$5$ von $10$ Paketen kommen zu spät.}\\ \kreuz{Jedes 5. Paket kommt zu spät.}\\ \kreuz{$5$ von $100$ Paketen kommen zu spät.}

   nachher: $5\,\%$ der Pakete kommen zu spät. Kreuze die Aussage an, die dazu passt. (P10 2020 OS)\\ \kreuz{$5$ von $10$ Paketen kommen zu spät.}\\ \kreuz{Jedes 5. Paket kommt zu spät.}\\ \kreuz{$5$ von $100$ Paketen kommen zu spät.}

10. `prozentrechnung-e1-k3-s1-v1` – Fehler finden (Nenner als Prozent gelesen)

   vorher: Tom: „Jede fünfundzwanzigste Schraube ist fehlerhaft, das sind $25\,\%$.“ – Fehler? Wie heißt es richtig?

   nachher: Tom sagt: „Jede fünfundzwanzigste Schraube ist fehlerhaft, das sind $25\,\%$.“ Finde den Fehler und schreibe die Aussage richtig.

11. `prozentrechnung-e2-k2-s0-v1` – Streifen einteilen: „Teile den Streifen in 10 %-Schritte“ (a

   vorher: In $10$-\%-Schritte einteilen.

   nachher: Teile den Streifen in gleiche Teile ein. Jeder Teil soll $10\,\%$ sein.

12. `prozentrechnung-e2-k3-s3-v1` – Teil : Ganzes als Dezimalzahl mit Taschenrechner

   vorher: $27$ von $60$ Minuten Training sind Laufen – wie viel Prozent?

   nachher: Ein Training dauert $60$ Minuten. Davon läuft Mia $27$ Minuten. Wie viel Prozent der Trainingszeit läuft Mia?

13. `prozentrechnung-e2-k3-s7-v2` – Prüfungshöhe: Anteil aus zwei Zahlen eines Sachtextes, das G

   vorher: Auf dem Blech liegen $11$ Muffins mit Blaubeeren und $4$ mit Kirschen. Wie viel Prozent sind Kirschmuffins? Runde auf eine Stelle. (P10 2018 OS)

   nachher: Auf dem Blech liegen $11$ Muffins mit Blaubeeren und $4$ mit Kirschen. Wie viel Prozent der Muffins sind mit Kirschen? Runde auf eine Stelle nach dem Komma. (P10 2018 OS)

14. `prozentrechnung-e2-k5-s1-v1` – Fehler finden (G und W vertauscht; Teil zu Rest statt Teil z

   vorher: Kim, „$12$ von $48$ Kindern“: \rechnung{48 : 12 &= 4 = 400\,\%} Fehler? Wie heißt es richtig?

   nachher: Kim soll ausrechnen, wie viel Prozent $12$ von $48$ Kindern sind. Kim rechnet so: \rechnung{\frac{48}{12} &= 4 = 400\,\%} Finde den Fehler und rechne richtig.

15. `prozentrechnung-e3-k1-s1-v1` – 50 %, 25 %, 10 % vom Ganzen am Streifen (4×)

   vorher: $50\,\%$ von $80\,€$ – wie viel?

   nachher: Der ganze Streifen steht für $80\,€$. Wie viel Euro sind $50\,\%$ davon?

16. `prozentrechnung-e3-k1-s5-v1` – Grundwert mit Komma

   vorher: $20\,\%$ von $4{,}50\,€$

   nachher: Berechne $20\,\%$ von $4{,}50\,€$.

17. `prozentrechnung-e3-k1-s9-v1` – dazu der Prozentwert ohne Kontext (2014-OS-B1a, 2026-FOR-B1a

   vorher: $17\,\%$ von $60\,€$ (P10 2014 OS)

   nachher: Berechne $17\,\%$ von $60\,€$. (P10 2014 OS)

18. `prozentrechnung-e3-k3-s2-v1` – Begründen (warum erst 1 %)

   vorher: $1\,\%$ von $500\,€$ sind $5\,€$. Warum?

   nachher: $1\,\%$ von $500\,€$ sind $5\,€$. Erkläre, warum.

19. `prozentrechnung-e4-k2-s0-v1` – Streifen: zwanzig Prozent sind vier Kästchen, wie viel ist d

   vorher: Grau sind $30\,\%$, das sind $6$ Kästchen – wie viele Kästchen hat der ganze Streifen?

   nachher: Der graue Teil des Streifens ist $30\,\%$. Er hat $6$ Kästchen. Wie viele Kästchen hat der ganze Streifen?

20. `prozentrechnung-e4-k2-s4-v1` – Sachtext („das sind 60 %“)

   vorher: $21$ Kinder fahren mit dem Rad, das sind $75\,\%$ der Klasse – wie viele Kinder hat die Klasse?

   nachher: $21$ Kinder fahren mit dem Rad. Das sind $75\,\%$ der Klasse. Wie viele Kinder hat die Klasse?

21. `prozentrechnung-e4-k3-s3-v1` – aus Prozentwert und Prozentsatz auf das Ganze schließen

   vorher: Grau sind $40\,\%$, das sind $18$ kg. Trage die Werte an den Streifen, lies das Ganze ab.

   nachher: Der graue Teil des Streifens ist $40\,\%$. Das sind $18$ kg. Trage die Werte am Streifen ein und lies das Ganze ab.

22. `prozentrechnung-e5-k2-s1-v1` – Prozentwert berechnen und dazu oder weg (4×)

   vorher: $80\,€$ um $10\,\%$ erhöht – neuer Preis?

   nachher: Ein Preis von $80\,€$ wird um $10\,\%$ erhöht. Wie hoch ist der neue Preis?

23. `prozentrechnung-e5-k2-s5-v1` – Brutto/Netto

   vorher: netto (ohne Steuer) $200\,€$, $19\,\%$ Mehrwertsteuer – brutto?

   nachher: Ein Gerät kostet ohne Mehrwertsteuer (netto) $200\,€$. Dazu kommen $19\,\%$ Mehrwertsteuer. Wie viel kostet das Gerät mit Mehrwertsteuer (brutto)?

24. `prozentrechnung-e5-k2-s10-v1` – der Preis nach Rabatt über den Faktor (2015-OS-K2b)

   vorher: Kletterhalle: Erwachsene $14\,€$, Jugendliche (bis $17$ Jahre) $9\,€$. Familie Demir: Mutter, Vater, Tochter ($15$ Jahre), Sohn ($12$ Jahre). Montags gibt es $15\,\%$ Rabatt. Wie viel zahlt die Familie am Montag? (P10 2015 OS)

   nachher: In einer Kletterhalle zahlen Erwachsene $14\,€$ und Jugendliche bis $17$ Jahre $9\,€$. Familie Demir kommt mit Mutter, Vater, Tochter ($15$ Jahre) und Sohn ($12$ Jahre). Montags gibt es $15\,\%$ Rabatt. Wie viel zahlt die Familie am Montag? (P10 2015 OS)

25. `prozentrechnung-e5-k3-s3-v1` – Wert nach Erhöhung oder Senkung (Wachstumsfaktor)

   vorher: Zwei Angebote für ein Fahrrad zu $600\,€$: A gibt $10\,\%$ Rabatt und auf den neuen Preis nochmals $10\,\%$; B gibt einmal $20\,\%$ Rabatt. Welches Angebot ist günstiger?

   nachher: Ein Fahrrad kostet $600\,€$. Bei Angebot A gibt es $10\,\%$ Rabatt. Auf den neuen Preis gibt es noch einmal $10\,\%$. Bei Angebot B gibt es einmal $20\,\%$ Rabatt. Welches Angebot ist günstiger?
