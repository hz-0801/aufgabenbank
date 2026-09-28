# Sprachlauf quadratische-gleichungen

Stand 2026-09-28 (Gruppe 4). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand dae7f7e. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py quadratische-gleichungen`: Abweichungen: 0, Warnungen: 0

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 62 | 1 | 63 |
| e2.jsonl | 43 | 0 | 43 |
| e3.jsonl | 79 | 0 | 79 |
| e4.jsonl | 37 | 2 | 39 |
| zone.jsonl | 34 | 0 | 34 |
| gesamt | 255 | 3 | 258 |

Geänderte Sprossen: 92. Die Beispiele sind je Sprosse
die erste geänderte Zeile, gleichmäßig über die Sprossen verteilt.

## Entscheidungen

- Reine Gleichungen ohne Auftrag („$x^2 = 81$“) heißen „Löse die Gleichung
  $x^2 = 81$. Gib die Lösungsmenge an.“ (Regel Lösungsmenge des Auftrags).
  Das gilt für die Übungszeilen in e1-k2, e2-k1 und e3-k3; wo die Lösungen
  gerundet werden, steht „Runde auf zwei Stellen nach dem Komma.“ davor.
  Die unveränderliche loesung zeigt weiter $x_1 = …$, $x_2 = …$ – der Inhalt
  stimmt, die Form nicht; siehe Bericht.
- Die Aufgaben der zone (Vorwissen, lineare Gleichungen) heißen nur „Löse die
  Gleichung.“ ohne Lösungsmenge, weil dort eine Zahl die Lösung ist.
- „Satz vom Nullprodukt“ (e2-k1-s0) wird in der Aufgabe selbst erklärt, weil
  die Optionen „gilt/gilt nicht“ wortgleich bleiben müssen: „Der Satz vom
  Nullprodukt sagt: Ein Produkt ist null, wenn ein Faktor null ist. Kreuze
  an, ob der Satz für die Gleichung … gilt.“
- „p und q?“ wird „Die Gleichung … hat die Form $x^2 + px + q = 0$. Gib $p$
  und $q$ an.“; „welcher Weg, welche Lösungen?“ wird „Löse die Gleichung …
  Wähle dafür einen passenden Weg und schreibe ihn dazu.“ (keine Frage nach
  einem Verfahrensnamen).
- Fehler finden ohne Lage („Wo ist der Fehler? \rechnung{…}“) bekommt eine
  Person und den Auftrag: „Ben soll die Gleichung … lösen. Er rechnet so: …
  Finde den Fehler und rechne richtig.“ (Namen neu, Zahlen gleich).
- Faustregel Bremsweg: „$(v : 10)^2 : 2$“ steht als Bruch.
- Die Ankreuz-Optionen „reinquadratisch – Wurzelziehen“ usw. enthalten einen
  Gedankenstrich; sie bleiben wortgleich, weil loesung sie so nennt.

## 10 Beispiele

1. `quadratische-gleichungen-e1-k1-s0-v1` – „Quadratisch oder linear?“ – zu Gleichungen ankreuzen, ob x² oder eine

   vorher: $5x - 2 = x^2$ – quadratisch oder linear?\\ \kreuz{quadratisch} \\ \kreuz{linear}

   nachher: Kreuze an, ob die Gleichung $5x - 2 = x^2$ quadratisch oder linear ist.\\ \kreuz{quadratisch} \\ \kreuz{linear}

2. `quadratische-gleichungen-e1-k2-s9-v1` – d negativ (Plus in der Klammer)

   vorher: $(x + 10)^2 = 25$

   nachher: Löse die Gleichung $(x + 10)^2 = 25$. Gib die Lösungsmenge an.

3. `quadratische-gleichungen-e2-k1-s0-v1` – „Steht rechts eine Null?“ ankreuzen (Vorstufe)

   vorher: $(x - 2) \cdot (x + 7) = 0$ – gilt der Satz vom Nullprodukt?\\ \kreuz{gilt} \\ \kreuz{gilt nicht}

   nachher: Der Satz vom Nullprodukt sagt: Ein Produkt ist null, wenn ein Faktor null ist. Kreuze an, ob der Satz für die Gleichung $(x - 2) \cdot (x + 7) = 0$ gilt.\\ \kreuz{gilt} \\ \kreuz{gilt nicht}

4. `quadratische-gleichungen-e2-k1-s10-v1` – Prüfungshöhe und zugleich Einstiegsaufgabe: unter vier Werten den ankr

   vorher: Welcher Wert erfüllt $x \cdot (x + 9) = -14$? (P10 2025 OS)\\ \kreuz{$x = 2$} \\ \kreuz{$x = 7$} \\ \kreuz{$x = -7$} \\ \kreuz{$x = -14$}

   nachher: Kreuze an, welcher Wert die Gleichung $x \cdot (x + 9) = -14$ erfüllt. (P10 2025 OS)\\ \kreuz{$x = 2$} \\ \kreuz{$x = 7$} \\ \kreuz{$x = -7$} \\ \kreuz{$x = -14$}

5. `quadratische-gleichungen-e3-k3-s5-v1` – p ungerade: Dezimalzahl unter der Wurzel

   vorher: $x^2 - 3x + 2 = 0$

   nachher: Löse die Gleichung $x^2 - 3x + 2 = 0$. Gib die Lösungsmenge an.

6. `quadratische-gleichungen-e3-k5-s2-v1` – Begründen (warum die Formel nur für die Normalform gilt; warum bei neg

   vorher: Begründe, warum du bei $3x^2 + 9x - 12 = 0$ vor der Formel durch $3$ teilen musst.

   nachher: Erkläre, warum du bei $3x^2 + 9x - 12 = 0$ vor der Formel durch $3$ teilen musst.

7. `quadratische-gleichungen-e4-k1-s7-v1` – Probe im Sachzusammenhang

   vorher: Lukas sagt: Ein Rechteck, das $3$ cm länger als breit ist und $70\,\text{cm}^2$ Fläche hat, ist $7$ cm breit. Stimmt das?

   nachher: Ein Rechteck ist $3$ cm länger als breit und hat $70\,\text{cm}^2$ Fläche. Lukas sagt: „Das Rechteck ist $7$ cm breit.“ Begründe, ob Lukas recht hat.

8. `quadratische-gleichungen-zone-f2-v1` – Quadratwurzel ziehen

   vorher: $\sqrt{49}$ – wie viel?

   nachher: Berechne. $\sqrt{49}$

9. `quadratische-gleichungen-zone-f5-v3` – Klammer zuerst und Punkt vor Strich mit negativen Zahlen

   vorher: $(-4) \cdot (-4 + 9)$ – wie viel?

   nachher: Berechne. $(-4) \cdot (-4 + 9)$

10. `quadratische-gleichungen-zone-f8-v4` – Terme ordnen und zusammenfassen, x² zuerst, dann x-Glieder, dann Zahle

   vorher: $2x - x^2 + 7 - 5x$ – ordnen und zusammenfassen?

   nachher: Ordne den Term: zuerst $x^2$, dann $x$, zuletzt die Zahl. Fasse dabei zusammen. $2x - x^2 + 7 - 5x$
