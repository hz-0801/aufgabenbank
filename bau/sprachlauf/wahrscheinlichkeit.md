# Sprachlauf wahrscheinlichkeit

Stand 2026-09-28 (Gruppe 4). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand daba0d1. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py wahrscheinlichkeit`: Abweichungen: 0, Warnungen: 0

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 19 | 28 | 47 |
| e2.jsonl | 40 | 30 | 70 |
| e3.jsonl | 32 | 26 | 58 |
| e4.jsonl | 15 | 32 | 47 |
| zone.jsonl | 6 | 16 | 22 |
| gesamt | 112 | 132 | 244 |

Geänderte Sprossen: 47. Die Beispiele sind je Sprosse
die erste geänderte Zeile, gleichmäßig über die Sprossen verteilt.

## Entscheidungen

- Der Eintrag war schon weitgehend in ganzen Sätzen; geändert wurden vor
  allem Gedankenstriche als Satzersatz (e1-k1-s0, e1-k1-s5), Semikolonketten
  (in Sätze geteilt), „Frage? Kreuze an.“ (zu „Kreuze an, …“) und die Formen
  aus Regel 6.
- „Stimmt das? Begründe.“ und „Hat er Recht? Begründe.“ werden „Begründe, ob
  <Name> recht hat.“ (auch in Originalen; die Prüfkennung bleibt am Ende).
  „Begründe, warum das stimmt/falsch ist.“ wird ebenso „Begründe, ob <Name>
  recht hat.“, weil die alte Form die Antwort vorwegnahm.
- „Finde den Fehler.“ wird „… und rechne richtig.“ bzw. bei einer Aussage
  ohne Rechnung „… und schreibe die Aussage richtig.“
- Glücksräder mit Grafik heißen „Das Glücksrad im Bild …“ (Regel 5).
- Zahlen stehen in diesem Eintrag teils ohne $…$ (so im Bestand); das ist
  nicht Gegenstand des Sprachlaufs und blieb.
- Fachwörter Stufe, Pfad, Ereignis, Gegenereignis, relative Häufigkeit,
  mit/ohne Zurücklegen, möglich/günstig bleiben (Sprossen üben sie).

## 10 Beispiele

1. `wahrscheinlichkeit-e1-k1-s0-v1` – Möglichkeiten in Ordnung auflisten (Vorstufe: erst alle mit dem ersten

   vorher: Paul hat zwei Mützen (grau, grün) und zwei Schals (gelb, weiß). Schreibe alle Paare aus Mütze und Schal auf – erst alle mit der grauen Mütze.

   nachher: Paul hat zwei Mützen, eine graue und eine grüne. Er hat zwei Schals, einen gelben und einen weißen. Schreibe alle Paare aus Mütze und Schal auf. Beginne mit den Paaren mit der grauen Mütze.

2. `wahrscheinlichkeit-e1-k1-s9-v1` – Prüfungshöhe: die Zahl der möglichen dreistelligen Nummern aus drei ve

   vorher: Ein Fahrradschloss hat einen dreistelligen Code aus den Ziffern 2, 4 und 8; jede Ziffer kommt genau einmal vor. Wie viele Codes sind möglich? (P10 2017 OS)

   nachher: Ein Fahrradschloss hat einen dreistelligen Code aus den Ziffern 2, 4 und 8. Jede Ziffer kommt genau einmal vor. Wie viele Codes sind möglich? (P10 2017 OS)

3. `wahrscheinlichkeit-e2-k2-s0-v1` – bei Glücksrad und Urne prüfen, ob alle Felder gleich groß sind, und Fe

   vorher: Das Glücksrad hat fünf gleich große Felder. Welcher Anteil der Felder ist rot? Kreuze an. \\ \kreuz{$\frac{1}{3}$} \\ \kreuz{$\frac{3}{5}$}

   nachher: Das Glücksrad im Bild hat fünf gleich große Felder. Kreuze an, welcher Anteil der Felder rot ist. \\ \kreuz{$\frac{1}{3}$} \\ \kreuz{$\frac{3}{5}$}

4. `wahrscheinlichkeit-e2-k3-s7-v2` – Gegenereignis („weder … noch“)

   vorher: In einer Urne liegen 4 rote, 3 blaue und 2 grüne Kugeln. Wie groß ist die Wahrscheinlichkeit für weder Rot noch Blau?

   nachher: In einer Urne liegen 4 rote, 3 blaue und 2 grüne Kugeln. Eine Kugel wird gezogen. Wie groß ist die Wahrscheinlichkeit für weder Rot noch Blau?

5. `wahrscheinlichkeit-e2-k3-s13-v1` – Prüfungshöhe: Lose mit fester Endziffer als eingeschränkte Grundmenge,

   vorher: Bei einem Schulfest gibt es Lose mit den Nummern 201 bis 700. Einen Trostpreis gibt es für jedes Los, dessen Nummer auf 45 endet, außer für das Los 445 (Hauptgewinn). Timo hat ein Los und sieht nur die letzte Ziffer: 5. Er sagt: „Die Wahrscheinlichkeit für einen Trostpreis ist $\frac{4}{50}$.“ Hat er Recht? Begründe. (P10 2016 OS)

   nachher: Bei einem Schulfest gibt es Lose mit den Nummern 201 bis 700. Einen Trostpreis gibt es für jedes Los, dessen Nummer auf 45 endet, außer für das Los 445 (Hauptgewinn). Timo hat ein Los und sieht nur die letzte Ziffer: 5. Er sagt: „Die Wahrscheinlichkeit für einen Trostpreis ist $\frac{4}{50}$.“ Begründe, ob Timo recht hat. (P10 2016 OS)

6. `wahrscheinlichkeit-e3-k2-s0-v1` – das Ereignis in eigenen Worten umschreiben und das Gegenereignis nenne

   vorher: Ein Würfel wird zweimal geworfen. Ereignis: „mindestens eine Sechs“. Nenne das Gegenereignis.

   nachher: Ein Würfel wird zweimal geworfen. Das Ereignis heißt „mindestens eine Sechs“. Nenne das Gegenereignis.

7. `wahrscheinlichkeit-e3-k3-s9-v1` – Behauptung prüfen (P(22) = P(33)?)

   vorher: Zwei Glücksräder haben je vier gleich große Felder: links 5, 6, 5, 7, rechts 6, 7, 6, 5. Beide werden gedreht; gelesen wird erst links, dann rechts. Eva behauptet: „66 ist genauso wahrscheinlich wie 77.“ Hat Eva Recht? Begründe. (P10 2025 OS)

   nachher: Zwei Glücksräder haben je vier gleich große Felder: links 5, 6, 5, 7, rechts 6, 7, 6, 5. Beide werden gedreht. Man liest erst die linke, dann die rechte Ziffer. Eva behauptet: „66 ist genauso wahrscheinlich wie 77.“ Begründe, ob Eva recht hat. (P10 2025 OS)

8. `wahrscheinlichkeit-e3-k4-s3-v1` – Baum zeichnen und ergänzen (Äste an einem Punkt ergeben 1; gleiche Äst

   vorher: Der Baum zeigt einen zweistufigen Zufallsversuch. Beschreibe einen Zufallsversuch, der zu diesem Baum passt (Gerät, Beschriftung, wie oft).

   nachher: Der Baum zeigt einen zweistufigen Zufallsversuch. Beschreibe einen Zufallsversuch, der zu diesem Baum passt. Nenne das Gerät, die Beschriftung und wie oft es benutzt wird.

9. `wahrscheinlichkeit-e4-k2-s3-v1` – Ereignis zu einer gegebenen Rechnung in Worten

   vorher: In einem Beutel liegen 5 rote und 3 blaue Kugeln; zwei werden ohne Zurücklegen gezogen. Welches Ereignis gehört zur Rechnung $\frac{5}{8} \cdot \frac{3}{7}$?

   nachher: In einem Beutel liegen 5 rote und 3 blaue Kugeln. Zwei werden ohne Zurücklegen gezogen. Welches Ereignis gehört zur Rechnung $\frac{5}{8} \cdot \frac{3}{7}$?

10. `wahrscheinlichkeit-zone-f4-v5` – Anzahl der Zahlen in einem Bereich (101 bis 900 sind 800 Lose; Endziff

   vorher: Ben berechnet die Zahl der Lose mit den Nummern 301 bis 700 so: $700 - 301 = 399$. Finde den Fehler und rechne richtig.

   nachher: Ben soll zählen, wie viele Lose die Nummern 301 bis 700 tragen. Er rechnet so: $700 - 301 = 399$. Finde den Fehler und rechne richtig.
