# Sprachlauf bruchrechnung

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Vergleich gegen den Bankstand a2e4f9f. Nur das Feld aufgabe ist geändert (Skriptprobe: alle anderen Felder gleich, keine Zahl verloren, keine neue Zahl). `python3 werkzeuge/bank-pruef.py bruchrechnung`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 49 | 10 | 59 |
| e2.jsonl | 28 | 7 | 35 |
| e3.jsonl | 49 | 10 | 59 |
| e4.jsonl | 39 | 3 | 42 |
| e5.jsonl | 33 | 9 | 42 |
| zone.jsonl | 17 | 9 | 26 |
| gesamt | 215 | 48 | 263 |

## 10 Beispiele

1. `bruchrechnung-e1-k1-s0-v1` – „Gleicher Nenner – ja oder nein?“ – ankreuzen, ob man sofort rechnen d

   vorher: $\frac{4}{11} + \frac{5}{11}$ – sofort rechnen? \janein

   nachher: Kreuze an, ob du $\frac{4}{11} + \frac{5}{11}$ sofort ausrechnen darfst. \janein

2. `bruchrechnung-e2-k1-s1-v1` – gleich viele Stellen

   vorher: $3{,}4 + 2{,}5$

   nachher: Berechne. $3{,}4 + 2{,}5$

3. `bruchrechnung-e3-k1-s0-v1` – „Von heißt mal“ – im Text das „von“ unterstreichen und die Malaufgabe 

   vorher: Unterstreiche „von“ und schreibe die Malaufgabe auf: Zwei Fünftel von 35 Kindern fahren mit dem Rad.

   nachher: Zwei Fünftel von 35 Kindern fahren mit dem Rad. Unterstreiche im Satz das Wort „von“. Schreibe dann die passende Malaufgabe auf.

4. `bruchrechnung-e4-k1-s0-v1` – „Wie viele Kommastellen hat das Ergebnis?“ – nur die Anzahl angeben (2

   vorher: $3{,}2 \cdot 0{,}4$ – wie viele Kommastellen hat das Ergebnis?

   nachher: Wie viele Stellen nach dem Komma hat das Ergebnis von $3{,}2 \cdot 0{,}4$?

5. `bruchrechnung-e5-k1-s0-v1` – Rechnung einkreisen

   vorher: $7 + 3 \cdot 5$ – kreise die Rechnung ein, die zuerst drankommt.

   nachher: Kreise in $7 + 3 \cdot 5$ die Rechnung ein, die du zuerst rechnen musst.

6. `bruchrechnung-zone-f1-v1` – Bruch als Anteil lesen, am Streifen einzeichnen (drei Achtel markieren

   vorher: Welcher Anteil ist gefärbt?

   nachher: Welcher Anteil des Streifens ist gefärbt?

7. `bruchrechnung-e1-k3-s6-v1` – gemischte Zahlen

   vorher: $2\frac{1}{5} + 1\frac{2}{5}$

   nachher: Berechne. $2\frac{1}{5} + 1\frac{2}{5}$

8. `bruchrechnung-e2-k4-s2-v1` – Begründen

   vorher: Warum schreibt man beim Addieren Komma unter Komma?

   nachher: Erkläre, warum man beim Addieren Komma unter Komma schreibt.

9. `bruchrechnung-e3-k3-s1-v1` – Bruch geteilt durch Zahl

   vorher: $\frac{2}{3} : 5$

   nachher: Berechne. $\frac{2}{3} : 5$

10. `bruchrechnung-e4-k2-s8-v1` – Prüfungshöhe: Menge mal Literpreis mit Wechsel zwischen Cent und Euro,

   vorher: Ein Lieferwagen braucht 8 l Diesel auf 100 km und fährt im Jahr $25\,000$ km. Ein Liter Diesel kostet $162{,}4$ ct. Berechne die Kraftstoffkosten für ein Jahr in Euro. (P10 2014 OS)

   nachher: Ein Lieferwagen braucht 8 l Diesel auf 100 km. Er fährt im Jahr $25\,000$ km. Ein Liter Diesel kostet $162{,}4$ ct. Berechne, wie viel Euro der Diesel für ein Jahr kostet. (P10 2014 OS)

## Wo die Regeln nicht reichten

# Wo die Regeln nicht reichten (bruchrechnung)

- Divisionszeichen (e3-k3-*, e3-k5-*, e4-k2-s2/s6/s7, e4-k3-s1-v3, e4-k3-s2-v3, e5-k1-*, e5-k4-*, zone-f5-v2): In diesem Eintrag ist das Teilen selbst Gegenstand (Bruch durch Zahl, Komma verschieben beim Teilen, Punkt vor Strich). „:“ blieb überall stehen; $\frac{\frac{2}{3}}{5}$ oder $\frac{63}{9}$ als Einmaleins-Aufgabe hätte die Sprosse verfälscht. Auch die Rabattterme in e5-k1-s7-v1/v2 („… : 100“) und der Originalterm $(a + b) : c$ (e5-k1-s6-v3/v4) blieben, weil gerade diese Terme geprüft bzw. aus dem Original übernommen werden.
- Reine Terme mit Ergebnisform (e1-k3-s2-*, e1-k3-s3-*, e5-k1-s5-*): Nur „Berechne.“ hätte die Lösung (gekürzt, gemischte Zahl, Umstellen) nicht verlangt. Entscheidung: Formhinweis als zweiter Satz („Kürze das Ergebnis so weit wie möglich.“, „Schreibe das Ergebnis als gemischte Zahl.“), bei Rechenvorteil „Rechne geschickt.“ wie in e5-k2. Bei „vorher kürzen“ (e3-k2-s3) kein Hinweis, weil das der Lösungsweg und keine Ergebnisform ist.
- Wahrscheinlichkeitsoriginale (e1-k3-s7-v1/v2, e3-k2-s5-v5/v6): Das Wort „Pfad“ (Baumdiagramm) übt die Sprosse nicht. Ersetzt durch „Die Wahrscheinlichkeit für zweimal rot ist …“; lange Sätze mit Semikolon (v3, v4, v7, v8, e3-k2-s6) in kurze Sätze zerlegt, Wortlaut sonst nahe am Original.
- „sofort rechnen“ (e1-k1-s0-*): Für schwache Schüler ungenau, eine Erklärung („ohne zu erweitern“) wäre aber eine Hilfe gewesen. Entschieden: „Kreuze an, ob du … sofort ausrechnen darfst.“ (Wort der Sprosse beibehalten).
- Fachwörter der Sprosse: „Kommastellen“ (e4-k1-s0, e4-k3-s2-v2) als „Stellen nach dem Komma“ geschrieben; „Überschlag“, „erweitern“, „Zähler/Nenner“, „ggT/kgV“ ausgeschrieben blieben, weil die Sprossen sie üben.
