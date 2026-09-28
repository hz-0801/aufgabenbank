# Sprachlauf rationale-zahlen

Stand 2026-09-28 (Gruppe 2). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py rationale-zahlen`: 0 Abweichungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 45 | 1 | 46 |
| e2.jsonl | 36 | 23 | 59 |
| e3.jsonl | 12 | 32 | 44 |
| e4.jsonl | 30 | 7 | 37 |
| zone.jsonl | 9 | 14 | 23 |
| gesamt | 132 | 77 | 209 |

Geänderte Sprossen: 48. Die 10 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1 …).

## Entscheidungen

- „:“ bleibt überall stehen, wo es vorkommt: Einmaleins-Division (Zone f1), Punkt vor Strich (Zone f4, e3 k1 s6), Teilen rationaler Zahlen (e3 k1 s0, s3, k3 s1) und der Term $(a + b) : c$ aus dem Original 2016-OS-B1i (e3 k1 s8, e2 k3 s8). Überall ist das Teilen selbst Thema oder die Form des Originals; ein Bruch würde die Punkt-vor-Strich-Falle und den Fehler in Mias Rechnung (Zone f4-v5) auflösen.
- „Berechne: <Term>“ gilt als ganzer Imperativsatz mit Doppelpunkt (Regel 3 der Kurzfassung) und bleibt unverändert; ebenso „Löse die Klammer auf und berechne: …“ und „Rechne geschickt: …“.
- „Ordne aufsteigend“ wird überall „Ordne die Zahlen der Größe nach, die kleinste zuerst: …“ (e1 k1 s5, die Originale s7 und die Fehlerzeile k5 s1 v2); „aufsteigend“ ist für schwache Schüler kein Alltagswort.
- „auf Zehntel/Ganze/Hundertstel runden“ wird „auf eine Stelle nach dem Komma“, „auf eine ganze Zahl“ und „auf zwei Stellen nach dem Komma“ (wie im Prozent-Lauf).
- Termwerte ohne Sachlage („… für $x = 4$ – welcher Wert?“) stehen einheitlich als „Setze … in den Term … ein. Berechne den Wert.“ (Zone f5, e4 k1 s5; e2 k3 s8 mit „Berechne nur die Klammer.“). Die Originale e3 k1 s7–s9 („Berechne den Wert von … für …“) sind ganze Sätze nah am Original und bleiben.
- e3 k2 s1 (Aussage prüfen, form ankreuzen ohne \kreuz): „Lies die Aussage: …“ löste im Prüfskript die Regel „Ablese-Auftrag ohne Grafik“ aus; daher „Prüfe, ob diese Aussage stimmt: „…““.
- Fachwort „Förderkorb/Sohle“ (e4 k1 s3 v2) ersetzt durch „Aufzug“ und „tiefster Gang“; das Ergebnis (Höhenunterschied $725$ m) bleibt.
- Die Preislisten der Originale e4 k1 s6 bleiben als Liste nach einem ganzen Einleitungssatz („Im Tierpark gelten diese Preise: …“); nur „Ermittle … und vergleiche …“ wurde in zwei kurze Sätze geteilt.

## 10 Beispiele

1. `rationale-zahlen-zone-f2-v1` – Zahlenstrahl

   vorher: Welche Zahl gehört zu A? Lies ab.

   nachher: Der Zahlenstrahl zeigt den Punkt A. Lies ab, welche Zahl zu A gehört.

2. `rationale-zahlen-zone-f5-v3` – Wert eines Terms mit Platzhalter berechnen (Vorzahl mal x pl

   vorher: $2 \cdot x + 1$ für $x = 2{,}5$ – welcher Wert?

   nachher: Setze $x = 2{,}5$ in den Term $2 \cdot x + 1$ ein. Berechne den Wert.

3. `rationale-zahlen-e1-k1-s3-v1` – zwei negative vergleichen

   vorher: $-15$ oder $-9$ – welche ist kleiner?

   nachher: Welche Zahl ist kleiner, $-15$ oder $-9$?

4. `rationale-zahlen-e1-k3-s1-v1` – runden

   vorher: $-3{,}47$ auf Zehntel runden

   nachher: Runde $-3{,}47$ auf eine Stelle nach dem Komma.

5. `rationale-zahlen-e1-k5-s4-v1` – Vergleichen und Ordnen von rationalen Zahlen

   vorher: Tiefste Punkte an Land: Kaspisches Meer $-28$ m, Totes Meer $-430$ m, Death Valley $-86$ m, Qattara-Senke $-133$ m. Welcher Ort liegt am tiefsten?

   nachher: Diese Orte an Land liegen unter dem Meeresspiegel: Kaspisches Meer $-28$ m, Totes Meer $-430$ m, Death Valley $-86$ m, Qattara-Senke $-133$ m. Welcher Ort liegt am tiefsten?

6. `rationale-zahlen-e2-k3-s5-v1` – Unterschied zweier Zahlen

   vorher: $-6$ und $5$ – wie weit auseinander?

   nachher: Wie weit liegen $-6$ und $5$ auf der Zahlengeraden auseinander?

7. `rationale-zahlen-e2-k7-s2-v1` – Begründen (warum minus minus plus ist)

   vorher: Setze fort: $4 - 2 = 2$, $4 - 1 = 3$, $4 - 0 = 4$. Begründe damit, warum $4 - (-3)$ dasselbe ist wie $4 + 3$.

   nachher: Setze die Reihe fort: $4 - 2 = 2$, $4 - 1 = 3$, $4 - 0 = 4$. Erkläre damit, warum $4 - (-3)$ dasselbe ist wie $4 + 3$.

8. `rationale-zahlen-e3-k3-s2-v1` – Begründen (Permanenzreihe oder Spiegelung)

   vorher: Setze fort: $2 \cdot (-4) = -8$, $1 \cdot (-4) = -4$, $0 \cdot (-4) = 0$. Begründe damit, warum $(-1) \cdot (-4)$ positiv ist.

   nachher: Setze die Reihe fort: $2 \cdot (-4) = -8$, $1 \cdot (-4) = -4$, $0 \cdot (-4) = 0$. Erkläre damit, warum $(-1) \cdot (-4)$ positiv ist.

9. `rationale-zahlen-e4-k1-s5-v1` – Termwert mit Klammer

   vorher: $3 \cdot (y + 4)$ für $y = -7$ – welcher Wert?

   nachher: Setze $y = -7$ in den Term $3 \cdot (y + 4)$ ein. Berechne den Wert.

10. `rationale-zahlen-e4-k3-s3-v1` – Addition als Zusammenfassung von mehreren Änderungen

   vorher: Lea hat $85$ € auf dem Konto. Sie zahlt $24{,}99$ € Handyrechnung und $49{,}90$ € für ein Konzertticket, bekommt $30$ € Taschengeld und zahlt $11{,}50$ € fürs Kino. Überziehen darf sie nicht. Kann sie danach noch ein Buch für $15$ € kaufen?

   nachher: Lea hat $85$ € auf dem Konto. Sie bezahlt ihre Handyrechnung über $24{,}99$ € und ein Konzertticket für $49{,}90$ €. Dann bekommt sie $30$ € Taschengeld. Danach zahlt sie $11{,}50$ € fürs Kino. Ihr Konto darf nicht ins Minus gehen. Kann sie danach noch ein Buch für $15$ € kaufen?
