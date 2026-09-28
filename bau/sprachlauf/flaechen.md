# Sprachlauf flaechen

Stand 2026-09-28 (Gruppe 2). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py flaechen`: 0 Abweichungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 54 | 0 | 54 |
| e2.jsonl | 36 | 0 | 36 |
| e3.jsonl | 44 | 0 | 44 |
| e4.jsonl | 38 | 0 | 38 |
| e5.jsonl | 41 | 0 | 41 |
| zone.jsonl | 31 | 0 | 31 |
| gesamt | 244 | 0 | 244 |

Geänderte Sprossen: 91. Die 10 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1 …).

## Entscheidungen

- Alle 244 Zeilen neu gefasst; auch die schon ganzen Sätze (Originale, Sachaufgaben) wurden an Semikolon und Kommaketten in kurze Sätze geteilt und auf die einheitliche Satzform der Sprosse gebracht.
- Maßangaben „$6$ m × $4$ m“ sind jetzt „mit den Seiten $6$ m und $4$ m“; bei zwei oder drei Rechtecken „Das erste Rechteck hat die Seiten … Das zweite hat die Seiten …“. „L-förmig“ und „T-förmig“ heißen „hat die Form eines L/T“.
- „:“ bleibt nur in der Zone f3 (`$96 : 3$`, `$24\,000 : 600$`), weil die Sprosse das Teilen selbst übt („Multiplizieren und Dividieren mit Dezimalzahlen“). In den \rechnung-Blöcken der Fehler-finden-Aufgaben (e1-k5-s1-v2, e3-k4-s1-v2/v3, e4-k4-s1-v3, e5-k4-s1-v2) und in den Termen `$A = m \cdot n : 2$`, `$A = 5 \cdot z : 2$` (e3-k4-s4) steht jetzt ein Bruch. Die Lösungen behalten ihr „:“ (nur aufgabe geändert).
- Grafikzeilen nennen die Figur: „Die Figur zeigt ein Parallelogramm/Dreieck mit der Grundseite $g$.“ (Höhe einzeichnen), „Die Figur zeigt ein Viereck.“ (Formel ankreuzen, Teilflächen benennen, Ergänzen), bei e2-k1-s6 „Die Skizze zeigt …“, weil die Aufgabe selbst „in der Skizze“ sagt. Zeilen mit \rechenplatz (e1-k5-s4, e3-k4-s4) haben keine Figur und nennen keine.
- e1-k1-s0 („Was ist gesucht? Kreise es … ein“): Die Frage hatte kein Ziel. Neu: „Kreise in der Formel … die Größe ein, die du noch nicht kennst.“ – verrät die gesuchte Größe nicht.
- Begründen-Zeilen mit Ja/Nein-Frage wurden „Begründe, ob …“, Erklär-Zeilen „Erkläre, warum …“. e4-k4-s2-v3 behält zwei Fragen (Figur benennen und Formel prüfen), weil die Lösung beide Antworten gibt.
- e4-k1-s0: Die Klammerlegende „($a$, $c$ parallele Seiten, …)“ ist ein Satz geworden („In den Formeln sind $a$ und $c$ parallele Seiten …“); die \kreuz-Optionen sind wortgleich aus der alten Zeile übernommen.
- Originale (e1-k2-s9, e3-k1-s7, e4-k1-s6, e5-k1-s7) folgen weiter den Angaben der Mappe; „Weise es über die Tiefe (Höhe) nach“ heißt jetzt „Zeige mit der Tiefe (Höhe) …, ob …“. Keine Sperre ausgelöst.

## 10 Beispiele

1. `flaechen-zone-f1-v1` – Längeneinheiten umrechnen (mm, cm, m), gemischte Angaben ang

   vorher: $3$ m – wie viele cm?

   nachher: Rechne $3$ m in cm um.

2. `flaechen-zone-f3-v4` – Multiplizieren und Dividieren mit Dezimalzahlen (Kommazahl m

   vorher: $0{,}3 \cdot 0{,}4$ – wie viel?

   nachher: Berechne. $0{,}3 \cdot 0{,}4$

3. `flaechen-zone-f6-v4` – Rechten Winkel erkennen und einzeichnen (Geodreieck)

   vorher: An welcher Ecke ist ein rechter Winkel? Prüfe mit dem Geodreieck und markiere ihn.

   nachher: Die Figur zeigt ein Dreieck. Eine Ecke hat einen rechten Winkel. Finde diese Ecke mit dem Geodreieck und markiere den Winkel.

4. `flaechen-e1-k2-s5-v1` – Seite aus A

   vorher: Rechteck, $A = 56$ cm², $a = 8$ cm – wie lang ist $b$?

   nachher: Ein Rechteck hat die Fläche $A = 56$ cm² und die Länge $a = 8$ cm. Wie lang ist die Breite $b$ des Rechtecks?

5. `flaechen-e1-k5-s4-v1` – Term zu Figur (Fläche oder Umfang mit Variablen)

   vorher: Zeichne ein Rechteck, dessen Fläche $A = 3 \cdot x$ ist, und beschrifte die Seiten.

   nachher: Ein Rechteck hat die Fläche $A = 3 \cdot x$. Zeichne das Rechteck und beschrifte die Seiten.

6. `flaechen-e2-k3-s2-v1` – Begründen (Dreieck abschneiden und anlegen)

   vorher: Warum ist die Fläche eines Parallelogramms Grundseite mal Höhe? Begründe mit Abschneiden und Anlegen.

   nachher: Erkläre, warum die Fläche eines Parallelogramms Grundseite mal Höhe ist. Schneide dazu in Gedanken ein Dreieck ab und lege es an.

7. `flaechen-e3-k2-s1-v1` – Höhe zur passenden Grundseite wählen (drei Höhen)

   vorher: Dreieck ABC: $AB = 8$ cm, $BC = 7{,}5$ cm. Die Höhe auf AB ist $6$ cm, die Höhe auf BC $6{,}4$ cm. Fläche – rechne mit BC und der passenden Höhe.

   nachher: Im Dreieck ABC ist $AB = 8$ cm und $BC = 7{,}5$ cm. Die Höhe auf AB ist $6$ cm. Die Höhe auf BC ist $6{,}4$ cm. Berechne die Fläche mit der Seite BC und der passenden Höhe.

8. `flaechen-e4-k1-s4-v1` – Drachen aus e und f

   vorher: Drachenviereck mit den Diagonalen $e = 7$ cm und $f = 6$ cm – Fläche?

   nachher: Ein Drachenviereck hat die Diagonalen $e = 7$ cm und $f = 6$ cm. Berechne die Fläche des Drachenvierecks.

9. `flaechen-e5-k1-s2-v1` – Rechteck und Dreieck

   vorher: Eine Giebelwand: unten ein Rechteck, $8$ m breit und $3$ m hoch, darauf ein Dreieck mit derselben Grundseite und $2{,}5$ m Höhe. Fläche der Wand?

   nachher: Eine Giebelwand ist unten ein Rechteck. Es ist $8$ m breit und $3$ m hoch. Darauf sitzt ein Dreieck mit derselben Grundseite und $2{,}5$ m Höhe. Berechne die Fläche der Wand.

10. `flaechen-e5-k4-s3-v1` – Berechnen in Sachkontexten mit verschiedenen Einheiten

   vorher: Ein L-förmiges Zimmer besteht aus den Rechtecken $5$ m × $4$ m und $2{,}5$ m × $2$ m. Es bekommt Parkett für $32$ € je m²; für Verschnitt kauft man $5\,\%$ mehr. Was kostet das Parkett?

   nachher: Ein Zimmer hat die Form eines L. Es besteht aus zwei Rechtecken. Das erste Rechteck hat die Seiten $5$ m und $4$ m. Das zweite hat die Seiten $2{,}5$ m und $2$ m. Parkett kostet $32$ € je m². Für Verschnitt kauft man $5\,\%$ mehr. Wie viel kostet das Parkett?
