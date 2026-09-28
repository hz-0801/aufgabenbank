# Sprachlauf quadratische-funktionen

Stand 2026-09-28 (Gruppe 4). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 2384be4. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py quadratische-funktionen`: Abweichungen: 1, Warnungen: 0

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 49 | 0 | 49 |
| e2.jsonl | 58 | 2 | 60 |
| e3.jsonl | 36 | 6 | 42 |
| e4.jsonl | 56 | 4 | 60 |
| zone.jsonl | 46 | 0 | 46 |
| gesamt | 245 | 12 | 257 |

Geänderte Sprossen: 102. Die Beispiele sind je Sprosse
die erste geänderte Zeile, gleichmäßig über die Sprossen verteilt.

## Entscheidungen

- Stichwortfragen („$f(x) = …$ – Scheitel?“, „– Nullstellen?“, „– Schnittpunkt?“)
  sind Sätze mit Verb: „Gib den Scheitel der Parabel … an.“, „Berechne die
  Nullstellen von …“, „Gegeben sind … Berechne ihren Schnittpunkt.“
- Wo die Zeile eine Grafik hat, nennt der erste Satz sie: „Das
  Koordinatensystem zeigt …“ (Regel 5).
- Wertetabellen, \kreuz- und \rechnung-Bausteine stehen unverändert hinter
  dem neuen Satz; bei den Ankreuz-Wertetabellen (e1-k1-s6) entfällt das
  nachgestellte „als die Normalparabel“, weil der Satz davor es nennt.
- Klammerlegenden ($x$: Entfernung in m, …) sind eigene Sätze „Dabei ist $x$ …“.
- Fehler finden: „<Name> soll … Er/Sie rechnet so: … Finde den Fehler und
  rechne richtig.“; wo nur abgelesen oder hingeschrieben wird, „… und schreibe
  den Scheitel/die Gleichung/den Punkt richtig.“
- Lösungsmenge: Die quadratischen Gleichungen in zone-f8 heißen „Löse die
  Gleichung … Gib die Lösungsmenge an.“ (Nachtrag, gleich wie in
  quadratische-gleichungen); loesung zeigt weiter $x_1 = …$, $x_2 = …$. Die
  linearen in zone-f5 heißen nur „Löse die Gleichung.“ Nullstellen bleiben
  „Berechne die Nullstellen …“.
- „Runde auf zwei Stellen.“ wird „Runde auf zwei Stellen nach dem Komma.“,
  auch in den Originalen e4-k1-s14.
- Fachwörter Scheitel, Normalparabel, Normalform, Scheitelpunktform,
  Nullstelle, Wertetabelle bleiben, weil die Sprossen sie üben.
- weg.jsonl hat kein Feld aufgabe und bleibt unberührt; seine eine
  Abweichung im Prüfskript („Dateiname“) bestand schon vor dem Lauf.

## 10 Beispiele

1. `quadratische-funktionen-e1-k1-s0-v1` – Gerade oder Parabel ankreuzen (Vorstufe)

   vorher: $f(x) = 4x - 1$ – Gerade oder Parabel? \kreuz{Gerade} \kreuz{Parabel}

   nachher: Kreuze an, ob der Graph von $f(x) = 4x - 1$ eine Gerade oder eine Parabel ist. \kreuz{Gerade} \kreuz{Parabel}

2. `quadratische-funktionen-e1-k1-s11-v1` – die Gleichung zum fallenden Bogen des Fallschirmsprungs aus vier Terme

   vorher: Ein Stein fällt von einer $45\,$m hohen Brücke. Der Graph zeigt seine Höhe $h$ (in m) nach $t$ Sekunden. Welche Gleichung passt? Kreuze an und begründe. \\ \kreuz{$h(t) = 5t^2 + 45$} \\ \kreuz{$h(t) = 5t^2 - 45$} \\ \kreuz{$h(t) = -5t^2 + 45$} \\ \kreuz{$h(t) = -5t^2 - 45$} (P10 2015 OS)

   nachher: Ein Stein fällt von einer $45\,$m hohen Brücke. Der Graph zeigt seine Höhe $h$ (in m) nach $t$ Sekunden. Kreuze die passende Gleichung an. Begründe deine Wahl. \\ \kreuz{$h(t) = 5t^2 + 45$} \\ \kreuz{$h(t) = 5t^2 - 45$} \\ \kreuz{$h(t) = -5t^2 + 45$} \\ \kreuz{$h(t) = -5t^2 - 45$} (P10 2015 OS)

3. `quadratische-funktionen-e2-k1-s6-v1` – Gleichung aus dem Graphen aufstellen (Scheitel ablesen, Öffnung prüfen

   vorher: Gleichung der Parabel?

   nachher: Das Koordinatensystem zeigt eine Parabel. Stelle ihre Gleichung auf.

4. `quadratische-funktionen-e2-k2-s4-v1` – Modellieren mit Wurfparabel und Bauwerk

   vorher: Beim Kugelstoßen gilt für die Flugbahn $h(x) = -0{,}05(x - 6)^2 + 3{,}8$ ($x$: Entfernung in m, $h$: Höhe in m). Wie hoch fliegt die Kugel höchstens, und in welcher Entfernung?

   nachher: Beim Kugelstoßen fliegt die Kugel auf der Bahn $h(x) = -0{,}05(x - 6)^2 + 3{,}8$. Dabei ist $x$ die Entfernung in m und $h$ die Höhe in m. Das Koordinatensystem zeigt die Bahn. Wie hoch fliegt die Kugel höchstens? In welcher Entfernung ist das?

5. `quadratische-funktionen-e3-k2-s2-v1` – Begründen (warum q der y-Achsenabschnitt ist; warum die Öffnung bei x²

   vorher: Der Graph von $f(x) = x^2 - 7x + 4$ schneidet die $y$-Achse im Punkt $(0|4)$. Warum?

   nachher: Der Graph von $f(x) = x^2 - 7x + 4$ schneidet die $y$-Achse im Punkt $(0|4)$. Erkläre, warum.

6. `quadratische-funktionen-e4-k1-s10-v1` – Punktprobe als Schnittpunkt-Nachweis in beiden Funktionen

   vorher: $f(x) = x^2 - 5$, $g(x) = 2x + 3$ – ist $P(4|11)$ ein Schnittpunkt?

   nachher: Gegeben sind die Parabel $f(x) = x^2 - 5$ und die Gerade $g(x) = 2x + 3$. Prüfe, ob $P(4|11)$ ein Schnittpunkt der beiden Graphen ist.

7. `quadratische-funktionen-zone-f1-v5` – Quadrieren auch negativer Zahlen und Dezimalzahlen, Quadrat vor Punkt 

   vorher: $0{,}3^2$ – wie viel?

   nachher: Berechne. $0{,}3^2$

8. `quadratische-funktionen-zone-f3-v6` – Lineare Funktion f(x) = m·x + n: Gerade zeichnen, Funktionswert, Punkt

   vorher: $g(x) = 2x - 8$ – Nullstelle? Gib auch den Punkt an.

   nachher: Berechne die Nullstelle von $g(x) = 2x - 8$. Gib auch den Punkt auf der $x$-Achse an.

9. `quadratische-funktionen-zone-f6-v3` – Schnittpunkt zweier Geraden durch Gleichsetzen

   vorher: $g(x) = 3x + 4$ und $h(x) = x - 2$ – Schnittpunkt?

   nachher: Gegeben sind die Geraden $g(x) = 3x + 4$ und $h(x) = x - 2$. Berechne ihren Schnittpunkt.

10. `quadratische-funktionen-zone-f8-v6` – Quadratische Gleichung durch Wurzelziehen lösen und Normalform mit der

   vorher: $x^2 + 4x + 9 = 0$ – Lösungen?

   nachher: Löse die Gleichung $x^2 + 4x + 9 = 0$. Gib die Lösungsmenge an.
