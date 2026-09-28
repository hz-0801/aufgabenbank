# Sprachlauf trigonometrische-funktionen

Stand 2026-09-28 (Gruppe 2). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py trigonometrische-funktionen`: 0 Abweichungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 51 | 3 | 54 |
| e2.jsonl | 43 | 17 | 60 |
| e3.jsonl | 52 | 5 | 57 |
| e4.jsonl | 47 | 4 | 51 |
| zone.jsonl | 45 | 1 | 46 |
| gesamt | 238 | 30 | 268 |

Geänderte Sprossen: 100. Die 10 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1 …).

## Entscheidungen

- Schreibweise der Zeilen beibehalten: sin, cos, Gradzahlen und Dezimalzahlen stehen in diesem Eintrag meist außerhalb von $…$ („sin 50° ≈ 0,8“). Das bleibt so; eine Umstellung auf $…{,}…$ würde die Zahlprobe brechen und ist keine Sprachfrage.
- Sinussatz (e1-k1-s13, Originale): Der Divisions-Doppelpunkt ist ersetzt. In v2/v3 steht ein Bruch, $\frac{x}{\text{sin } 104^\circ} = \frac{9}{\text{sin } 38^\circ}$ (\sin ist kein zugelassener Baustein, also \text{sin }). In v1 steht „5,3“ im Term. Im Bruch wäre das $5{,}3$ geworden, eine neue Zahlmarke, die die Probe sperrt. Deshalb steht die Rechnung dort in Worten: „e ist 5,3 cm mal sin 128°, geteilt durch sin 31°“. Der „:“ in Uhrzeiten (3:00 Uhr) bleibt.
- Grafikzeilen nennen die Darstellung einheitlich: „Das Koordinatensystem zeigt …“ (ksys), „Das Bild zeigt einen Punkt P auf dem Einheitskreis“ (\einheitskreis), „Die Tabelle zeigt …“ (\sachtabelle), „Das Diagramm zeigt …“ (e4-k1-s2-v2 mit Zeitachse). Bei zwei Systemen (e3-k1-s14) heißt es „das erste/zweite Koordinatensystem“.
- Stellenangaben „(eine Stelle)“ und „(zwei Stellen)“ heißen jetzt immer „Runde auf eine/zwei Stellen nach dem Komma.“ und stehen als eigener Satz, auch beim Ablesen.
- Fehler finden: Wo eine Rechnung oder ein Wert falsch ist, steht „Finde den Fehler und rechne richtig.“, wo es um eine Aussage geht, „… und schreibe die Aussage richtig.“ Bei der gezeichneten Dachspitze (e2-k2-s1-v1) steht „… und beschreibe, wie die Kurve richtig aussieht.“, weil es dort weder Rechnung noch Aussage gibt.
- Fachwörter der Sprossen bleiben (Amplitude, Periode, Mittellinie, periodisch, Funktionstyp, Spannweite, Rechts-/Hochachse). Buchstaben ohne Erklärung bekommen eine: „c“ als Form „y = sin(x + c)“, „a“ als Form „y = a · sin(x)“, „t“ und „y“ als Sätze („Dabei ist t die Zeit in Stunden …“).
- Unverändert (30 Zeilen): die Begründe-Zeilen mit ganzem Satz (e1-k2-s2, e2-k2-s2, e3-k3-s2 und e4-k2-s2 v1/v2), gute Fragesätze (e2-k1-s7 v1/v2, e2-k1-s8, e2-k1-s9, e2-k1-s10 v1/v3, e2-k1-s12 v1/v2, e2-k1-s13 v2/v3, e3-k1-s10 v2/v3, e4-k1-s2 v1/v3) und zone-f5-v1.
- e2-k2-s3-v3 hat die Form ankreuzen, aber kein \kreuz (Tabelle ausfüllen). Ich habe nur die Sprache geglättet und die Form nicht angefasst. Das ist ein Befund für die Korrektur.

## 10 Beispiele

1. `trigonometrische-funktionen-zone-f1-v1` – Sinus, Kosinus und Tangens als Seitenverhältnisse im rechtwi

   vorher: Gegenkathete 2 cm, Hypotenuse 5 cm – wie groß ist sin $\alpha$?

   nachher: In einem rechtwinkligen Dreieck ist die Gegenkathete von $\alpha$ 2 cm lang. Die Hypotenuse ist 5 cm lang. Berechne sin $\alpha$.

2. `trigonometrische-funktionen-zone-f4-v1` – Kreis mit Mittelpunkt und Radius zeichnen, Umfang mit Pi ber

   vorher: Radius 3 cm – wie lang ist der Umfang? Gib ihn mit $\pi$ und gerundet an.

   nachher: Ein Kreis hat den Radius 3 cm. Gib seinen Umfang mit $\pi$ an und auch gerundet.

3. `trigonometrische-funktionen-zone-f7-v4` – Wertetabelle anlegen, Wertepaare als Punkte eintragen, den G

   vorher: Zeichne den Graphen von $y = x^2 - 2$ aus der Tabelle als durchgehende Linie.

   nachher: Die Tabelle gehört zu $y = x^2 - 2$. Zeichne den Graphen als durchgehende Linie in das Koordinatensystem.

4. `trigonometrische-funktionen-zone-f11-v3` – Größtwert, Kleinstwert und Spannweite einer Tabelle entnehme

   vorher: −2, 5, 3, −1, 4 (in °C) – wie groß ist der Mittelwert?

   nachher: Gemessen wurden die Temperaturen −2 °C, 5 °C, 3 °C, −1 °C und 4 °C. Berechne den Mittelwert.

5. `trigonometrische-funktionen-e1-k1-s9-v1` – Winkel vom Gradmaß ins Bogenmaß umrechnen

   vorher: 40° ins Bogenmaß – als Vielfaches von $\pi$ und auf zwei Stellen?

   nachher: Rechne 40° ins Bogenmaß um. Schreibe das Ergebnis als Vielfaches von $\pi$. Runde es außerdem auf zwei Stellen nach dem Komma.

6. `trigonometrische-funktionen-e2-k1-s4-v1` – Funktionswert zu einem Winkel ablesen

   vorher: Lies sin 135° am Graphen ab (eine Stelle).

   nachher: Das Koordinatensystem zeigt den Graphen von y = sin(x). Lies sin 135° am Graphen ab. Runde auf eine Stelle nach dem Komma.

7. `trigonometrische-funktionen-e2-k2-s3-v1` – Wertetabelle einem Graphen zuordnen

   vorher: Gehört die Wertetabelle zu f oder zu g?\\ \kreuz{f}\kreuz{g}

   nachher: Das Koordinatensystem zeigt die Graphen f und g. Kreuze an, zu welchem Graphen die Wertetabelle gehört.\\ \kreuz{f}\kreuz{g}

8. `trigonometrische-funktionen-e3-k1-s10-v1` – die Wirkung eines Parameters in Worten beschreiben

   vorher: Der Faktor vor sin steigt von 1 auf 4. Beschreibe, was mit der Welle passiert.

   nachher: Der Faktor a in y = a · sin(x) steigt von 1 auf 4. Beschreibe, was mit der Welle passiert.

9. `trigonometrische-funktionen-e4-k1-s4-v1` – Mittellinie und Amplitude daraus bestimmen

   vorher: Größtwert 27 °C, Kleinstwert 13 °C – Mittellinie und Amplitude?

   nachher: Eine Temperatur hat den Größtwert 27 °C und den Kleinstwert 13 °C. Bestimme die Mittellinie und die Amplitude.

10. `trigonometrische-funktionen-e4-k2-s2-v3` – Begründen (warum ein Wachstumsvorgang keine Sinuskurve ergib

   vorher: Begründe, warum man für die Höhe einer Riesenradgondel eine Sinuskurve nehmen kann, für die Höhe eines geworfenen Balls aber nicht.

   nachher: Für die Höhe einer Gondel im Riesenrad kann man eine Sinuskurve nehmen. Für die Höhe eines geworfenen Balls geht das nicht. Begründe, warum.
