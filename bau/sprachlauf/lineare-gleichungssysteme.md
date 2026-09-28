# Sprachlauf lineare-gleichungssysteme

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Vergleich gegen den Bankstand ba59b59. Nur das Feld aufgabe ist geändert (Skriptprobe: alle anderen Felder gleich, keine Zahl verloren, keine neue Zahl). `python3 werkzeuge/bank-pruef.py lineare-gleichungssysteme`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 50 | 0 | 50 |
| e2.jsonl | 44 | 0 | 44 |
| e3.jsonl | 57 | 0 | 57 |
| e4.jsonl | 65 | 0 | 65 |
| e5.jsonl | 36 | 0 | 36 |
| zone.jsonl | 42 | 0 | 42 |
| gesamt | 294 | 0 | 294 |

## 10 Beispiele

1. `lineare-gleichungssysteme-e1-k1-s0-v1` – Zahlenpaar prüfen – Lösung von I, II, beiden (Vorstufe)

   vorher: $(2|6)$ – Lösung von welcher Gleichung? I: $x + y = 8$, II: $3x - y = 0$. Kreuze an.\\ \kreuz{nur von I}\\ \kreuz{nur von II}\\ \kreuz{von beiden}\\ \kreuz{von keiner}

   nachher: Gegeben sind die Gleichungen I: $x + y = 8$ und II: $3x - y = 0$. Kreuze an, von welcher Gleichung das Zahlenpaar $(2|6)$ eine Lösung ist.\\ \kreuz{nur von I}\\ \kreuz{nur von II}\\ \kreuz{von beiden}\\ \kreuz{von keiner}

2. `lineare-gleichungssysteme-e2-k1-s0-v1` – Gleichung mit Vorzahl 1 ankreuzen (Vorstufe)

   vorher: Welche Gleichung ist fast fertig? I: $3x + 7y = 17$, II: $x + 4y = 9$. Kreuze die Gleichung an, die du umstellst und in die andere einsetzt.\\ \kreuz{Gleichung I}\\ \kreuz{Gleichung II}

   nachher: Gegeben sind I: $3x + 7y = 17$ und II: $x + 4y = 9$. Du willst eine Gleichung umstellen und in die andere einsetzen. Kreuze an, welche Gleichung dafür schon fast fertig ist.\\ \kreuz{Gleichung I}\\ \kreuz{Gleichung II}

3. `lineare-gleichungssysteme-e3-k1-s0-v1` – gleiche Vorzahl oder Gegenzahl ankreuzen (Vorstufe)

   vorher: Gleiche Vorzahl oder Gegenzahl bei $y$? I: $2x + 3y = 9$, II: $5x - 3y = 14$. Kreuze an.\\ \kreuz{gleiche Vorzahl}\\ \kreuz{Gegenzahlen}\\ \kreuz{weder noch}

   nachher: Gegeben sind I: $2x + 3y = 9$ und II: $5x - 3y = 14$. Kreuze an, was für die Vorzahlen bei $y$ gilt.\\ \kreuz{gleiche Vorzahl}\\ \kreuz{Gegenzahlen}\\ \kreuz{weder noch}

4. `lineare-gleichungssysteme-e4-k1-s0-v1` – Unbekannte benennen, Anzahlen und Beträge markieren (Vorstufe)

   vorher: Bäckerei: $3$ Brötchen und $2$ Brezeln kosten $3{,}10\,€$; $1$ Brötchen und $4$ Brezeln kosten $3{,}70\,€$. Was ist unbekannt? Benenne die gesuchten Größen mit $x$ und $y$ und schreib heraus, welche Zahlen rechts vom Gleichheitszeichen und welche vor $x$ und $y$ stehen.

   nachher: In einer Bäckerei kosten $3$ Brötchen und $2$ Brezeln zusammen $3{,}10\,€$. $1$ Brötchen und $4$ Brezeln kosten $3{,}70\,€$. Überlege, was unbekannt ist, und benenne die gesuchten Größen mit $x$ und $y$. Schreibe dann heraus, welche Zahlen rechts vom Gleichheitszeichen stehen und welche vor $x$ und $y$.

5. `lineare-gleichungssysteme-e5-k1-s0-v1` – „Wie viele Lösungen?“ und „Parameter im Koeffizienten?“ ankreuzen (Vor

   vorher: Wie viele Lösungen? Beim Lösen eines Systems mit drei Variablen steht am Ende $0 = 0$. Kreuze an.\\ \kreuz{genau eine}\\ \kreuz{keine}\\ \kreuz{unendlich viele}

   nachher: Beim Lösen eines Systems mit drei Variablen steht am Ende $0 = 0$. Kreuze an, wie viele Lösungen das System hat.\\ \kreuz{genau eine}\\ \kreuz{keine}\\ \kreuz{unendlich viele}

6. `lineare-gleichungssysteme-zone-f1-v1` – Lösung durch Einsetzen prüfen, Ergebnis mit (wA)/(fA)

   vorher: $x = 4$ – Lösung von $x + 5 = 9$? Setze ein.

   nachher: Prüfe durch Einsetzen, ob $x = 4$ eine Lösung der Gleichung $x + 5 = 9$ ist.

7. `lineare-gleichungssysteme-e1-k1-s8-v1` – systematisches Probieren mit Tabelle

   vorher: Lösung durch Probieren? I: $x + y = 8$, II: $3x + y = 14$. Setze in I nacheinander $x = 0, 1, 2, \ldots$ ein, trage $y$ ein und prüfe II.

   nachher: Finde die Lösung von I: $x + y = 8$ und II: $3x + y = 14$ durch Probieren. Setze in I nacheinander $x = 0, 1, 2, \ldots$ ein und trage $y$ in die Tabelle ein. Prüfe dann jedes Paar mit II.

8. `lineare-gleichungssysteme-e2-k1-s8-v1` – Gleichsetzen bei zwei Gleichungen y = …

   vorher: I: $y = 3x - 4$, II: $y = x + 2$ – Lösung? Setze die rechten Seiten gleich.

   nachher: Löse das Gleichungssystem I: $y = 3x - 4$ und II: $y = x + 2$. Setze dazu die rechten Seiten gleich.

9. `lineare-gleichungssysteme-e3-k1-s8-v1` – Verfahren wählen und begründen

   vorher: I: $y = 3x - 2$, II: $y = -x + 6$ – welches Verfahren passt? Entscheide und begründe.

   nachher: Gegeben ist das Gleichungssystem I: $y = 3x - 2$ und II: $y = -x + 6$. Entscheide und begründe, welches Lösungsverfahren hier am besten passt.

10. `lineare-gleichungssysteme-e4-k1-s8-v1` – Prüfungshöhe: Rosen und Tulpen – System aus „zusammen 3,80 €“ und „sec

   vorher: Café: Ein Croissant und ein Muffin kosten zusammen $4{,}10\,€$. Fünf Croissants und zwei Muffins kosten $13{,}60\,€$. $x$ ist der Preis eines Croissants, $y$ der Preis eines Muffins in Euro. Stelle ein Gleichungssystem auf. (P10 2024 OS)

   nachher: In einem Café kosten ein Croissant und ein Muffin zusammen $4{,}10\,€$. Fünf Croissants und zwei Muffins kosten $13{,}60\,€$. $x$ ist der Preis eines Croissants in Euro, $y$ der Preis eines Muffins in Euro. Stelle ein Gleichungssystem auf. (P10 2024 OS)

## Wo die Regeln nicht reichten

# Wo die Regeln nicht reichten (lineare-gleichungssysteme)

- Lösungsmenge (z. B. e2-k1-s1-v1, e3-k1-s1-v1): Die Regel „Lösungsmenge statt Lösung“ passt hier nicht. `loesung` gibt „$x = 3$, $y = 7$; Lösung $(3|7)$“ an, nicht $L = \{(3|7)\}$. Deshalb steht dort überall „Löse das Gleichungssystem …“, ohne Lösungsmenge. „Lösungsmenge“ bleibt nur, wo sie schon im Text stand (e5-k1-s5, e5-k1-s8, zone-f10-v3).
- Bezeichner „I: $…$“ (fast alle Zeilen): Die Regel verbietet Stichwörter mit Doppelpunkt, aber „I:“/„II:“ ist die übliche Schreibweise für die Gleichungen eines Systems und steht auch in `loesung`. Sie bleibt. Die Gleichungen stehen jetzt in ganzen Sätzen („Löse das Gleichungssystem I: $…$ und II: $…$.“), und reine Stichwort-Anfänge wie „Schar und Auswahl:“, „Probe im Text:“ oder „Bäckerei:“ sind gestrichen.
- Fehler finden bei Aufstellen, Ablesen und Zuordnen (e4-k6-s1-v1, e4-k6-s2-v1, e1-k3-s1-v1): Die feste Form „rechne richtig“ passt nicht überall. Wo nichts gerechnet wird, habe ich sie angepasst: „stelle die Gleichungen richtig auf“ bzw. „schreibe die Antwort richtig“. Bei e5-k2-s1-v1 ist Jans Satz der Fehler, darum steht dort „schreibe die Aussage richtig“.
- Vorstufen „Was ist unbekannt?“ (e4-k1-s0-v1–v4): Ein Satz wie „Der Preis ist unbekannt“ hätte die Lösung vorweggenommen. Der Text sagt deshalb nur „Überlege, was unbekannt ist, und benenne die gesuchten Größen mit $x$ und $y$.“
- Fachwörter aus der Oberstufe (e4-k2-s3 „Interpretiere … im Sachzusammenhang“, e1-k3-s6 „nicht äquivalent“, e4-k6-s5 „Bilanz“): Den Operator habe ich durch „Erkläre, was die beiden Gleichungen für die Mischung bedeuten“ ersetzt. „Äquivalent“ bekommt „(nicht gleichwertig)“ dazu, weil die Sprosse das Wort nennt. „Bilanz“ bleibt ohne Erklärung, weil eine Erklärung die Antwort vorwegnähme.
