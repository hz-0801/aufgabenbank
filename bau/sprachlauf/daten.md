# Sprachlauf daten

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist geändert (Skriptprobe: alle anderen Felder gleich, keine Zahl verloren, keine neue Zahl). `python3 werkzeuge/bank-pruef.py daten`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 88 | 0 | 88 |
| e2.jsonl | 59 | 0 | 59 |
| e3.jsonl | 50 | 4 | 54 |
| e4.jsonl | 72 | 7 | 79 |
| e5.jsonl | 81 | 6 | 87 |
| e6.jsonl | 40 | 1 | 41 |
| e7.jsonl | 75 | 0 | 75 |
| zone.jsonl | 43 | 12 | 55 |
| gesamt | 508 | 30 | 538 |

## 10 Beispiele

1. `daten-e1-k1-s0-v1` – Ganzes unterstreichen (Vorstufe)

   vorher: Von $26$ Kindern fahren $8$ mit dem Bus. – Was ist das Ganze? Unterstreiche es.

   nachher: Von $26$ Kindern fahren $8$ mit dem Bus. Unterstreiche im Text das Ganze.

2. `daten-e2-k1-s0-v1` – „Wo fängt die Achse an?“ – bei Diagrammen ankreuzen, ob die y-Achse be

   vorher: Die y-Achse eines Säulendiagramms ist mit $0$, $20$, $40$, $60$, $80$ beschriftet. Beginnt die Achse bei null? Kreuze an.\\ \kreuz{ja, bei null} \\ \kreuz{nein, Startwert} \leerfeld

   nachher: Die y-Achse (senkrechte Achse) eines Säulendiagramms ist mit $0$, $20$, $40$, $60$, $80$ beschriftet. Kreuze an, ob die Achse bei null beginnt. Wenn nicht, trage den Startwert ein.\\ \kreuz{ja, bei null} \\ \kreuz{nein, Startwert} \leerfeld

3. `daten-e3-k1-s0-v1` – Prozent oder Grad ankreuzen (Vorstufe)

   vorher: Zu einem Kreisdiagramm heißt es: „Der Sektor Bus hat einen Mittelpunktswinkel von $54$.“ Was ist die Zahl $54$ hier? Kreuze an.\\ \kreuz{Anteil in \%} \\ \kreuz{Winkel in Grad}

   nachher: Zu einem Kreisdiagramm steht: „Der Sektor Bus hat einen Mittelpunktswinkel von $54$.“ Kreuze an, was die Zahl $54$ hier ist.\\ \kreuz{Anteil in \%} \\ \kreuz{Winkel in Grad}

4. `daten-e4-k1-s0-v1` – Kenngröße ankreuzen (Vorstufe)

   vorher: „Wie weit liegen der kleinste und der größte Wert auseinander?“ – Welche Kenngröße ist gefragt? Kreuze an.\\ \kreuz{Spannweite} \\ \kreuz{Modalwert} \\ \kreuz{Median} \\ \kreuz{Mittelwert}

   nachher: Jemand fragt: „Wie weit liegen der kleinste und der größte Wert auseinander?“ Kreuze an, welche Kenngröße gefragt ist.\\ \kreuz{Spannweite} \\ \kreuz{Modalwert} \\ \kreuz{Median} \\ \kreuz{Mittelwert}

5. `daten-e5-k1-s0-v1` – Achsenanfang ankreuzen (Vorstufe)

   vorher: Die y-Achse eines Säulendiagramms ist mit $0$, $50$, $100$, $150$ beschriftet. Wo beginnt sie? Kreuze an.\\ \kreuz{bei null} \\ \kreuz{nicht bei null}

   nachher: Die y-Achse eines Säulendiagramms ist mit $0$, $50$, $100$, $150$ beschriftet. Kreuze an, wo sie beginnt.\\ \kreuz{bei null} \\ \kreuz{nicht bei null}

6. `daten-e6-k1-s0-v1` – „Gewichtet oder ungewichtet?“ und „Wert oder Klasse?“ ankreuzen (Vorst

   vorher: Für den Mittelwert der Tabelle: Wie zählt jeder Wert? Kreuze an.\\ \kreuz{jeder Wert zählt einmal (ungewichtet)} \\ \kreuz{jeder Wert zählt mit seiner Häufigkeit (gewichtet)}

   nachher: Die Tabelle zeigt, wie oft jede Note vorkommt. Du willst den Mittelwert berechnen. Kreuze an, wie jeder Wert dabei zählt.\\ \kreuz{jeder Wert zählt einmal (ungewichtet)} \\ \kreuz{jeder Wert zählt mit seiner Häufigkeit (gewichtet)}

7. `daten-e7-k1-s0-v1` – „Welche zwei Merkmale?“ und „Feld oder Rand?“ ankreuzen (Vorstufe)

   vorher: „In der Klasse 9b haben $14$ von $27$ Kindern ein Haustier; $11$ der Kinder sind Jungen, $5$ Jungen haben ein Haustier.“ Welche zwei Merkmale mit je zwei Ausprägungen gehören in Kopfzeile und Kopfspalte der Tafel? Trage nur die Namen ein, keine Zahl.

   nachher: Ein Text lautet: „In der Klasse 9b haben $14$ von $27$ Kindern ein Haustier. $11$ der Kinder sind Jungen, $5$ Jungen haben ein Haustier.“ Trage in die Kopfzeile und die Kopfspalte der Vierfeldertafel die zwei Merkmale ein. Jedes Merkmal hat zwei Ausprägungen (Möglichkeiten). Trage nur die Namen ein, keine Zahl.

8. `daten-zone-f1-v1` – Prozentsatz berechnen (Teil geteilt durch Ganzes), Prozent ↔ Dezimalza

   vorher: $7$ von $10$ Kindern – wie viel Prozent?

   nachher: $7$ von $10$ Kindern haben ein Haustier. Wie viel Prozent der Kinder haben ein Haustier?

9. `daten-e1-k1-s8-v1` – aus einem Diagramm (Anzahl und Gesamtzahl ablesen)

   vorher: Lies ab: Wie viele Kinder nannten Fußball, wie viele wurden insgesamt befragt? Relative Häufigkeit von Fußball als Dezimalzahl.

   nachher: Das Säulendiagramm zeigt die Lieblingssportarten von Kindern. Lies ab, wie viele Kinder Fußball nannten und wie viele Kinder insgesamt befragt wurden. Gib dann die relative Häufigkeit von Fußball als Dezimalzahl an.

10. `daten-e2-k2-s7-v1` – Säule mit gegebenem Wert ergänzen

   vorher: Zeichne die Säule für Donnerstag: $140$ Besucher.

   nachher: Am Donnerstag kamen $140$ Besucher. Zeichne dafür die Säule in das Säulendiagramm ein.

## Wo die Regeln nicht reichten

# Sprachlauf daten: Wo die Regeln nicht reichten

- Fachwörter der Kenngrößen (e4, e5, e6: Modalwert, Median, Quartil, Standardabweichung, Mittelpunktswinkel in e3): Regel 7 verlangt ein Alltagswort daneben. Das hätte aber die Lösung verraten, zum Beispiel bei `daten-e4-k1-s3-v1` „Bestimme den Modalwert (den häufigsten Wert)“, und die Vorstufen `e4-k1-s0` fragen genau nach diesen Begriffen. Entscheidung: Diese Begriffe bleiben ohne Erklärung stehen. Erklärt habe ich nur Wörter, die keine Lösung vorwegnehmen: „Minimum (kleinster Wert)“, „y-Achse (senkrechte Achse)“, „Ausprägungen (Möglichkeiten)“, „Reklamationen (Beschwerden)“.
- Zahlwörter: Regel 8 verbietet neue Zahlen. Offen blieb, ob auch ein neues Zahlwort als neue Zahl zählt, das apply.py gar nicht prüft. Beispiele sind „Vier Städte“ (`e2-k2-s9-v2`), „Drei Läufe“ (`e2-k3-s1-v3`) und „drei Möglichkeiten“ (`zone-f12-v3`). Entscheidung: Diese Zahlwörter habe ich wieder entfernt. Zahlwörter aus dem alten Text („fünf Packungen“, „sechs Wochen“) bleiben stehen. Uhrzeitschreibweisen wie „3:45“ (`zone-f6-v4`, `e4-k2-s3-v1` bis `v3`) sind keine Division und bleiben ebenfalls.
- Gedankenstrich in wörtlicher Rede: apply.py weist jedes „ – “ zurück, auch innerhalb eines Zitats. Betroffen waren `e5-k1-s8-v3`, `e5-k1-s10-v2` und `e5-k4-s4-v1`. Entscheidung: Das Zitat habe ich in zwei Sätze geteilt. In `e5-k1-s8-v3` habe ich zusätzlich die Redewendung „platzt aus allen Nähten“ durch „wird zu klein“ ersetzt. Die geprüfte Zahlenaussage („über 800“) bleibt gleich.
- Formen „Aussage: … Stimmt das? Prüfe am Diagramm.“ (e5-k1-s1 bis s4, e5-k2-s3, e7-k2-s7): Diese Aufgaben habe ich in die feste Satzform „<Name> sagt: „…“ Begründe mit dem Säulendiagramm (bzw. Boxplot, Vierfeldertafel), ob <Name> recht hat.“ gebracht und dafür Namen erfunden. Bei Zeitungs- und Werbeaussagen (e5-k1-s10, e5-k4-s4) blieb „Eine Zeitung schreibt / Jemand behauptet“ stehen, weil der Sprecher dort Teil der Sachlage ist.
- Ergänzte Lage bei unvollständigem Text: In `daten-e1-k2-s5-v2` (FHR 2023) fehlte, dass die übrigen Zuschauer eine Stehplatzkarte haben. Die Lösung nennt Stehplätze, und die Frage nach „vier Kartenarten“ setzt sie voraus. Entscheidung: Ich habe den Satz „Die anderen haben eine Stehplatzkarte.“ ergänzt. In `e2-k1-s0-v1`/`v2` habe ich wie in `v3`/`v4` den Satz „Wenn nicht, trage den Startwert ein.“ ergänzt, weil die Bausteine ein \leerfeld für den Startwert haben.
