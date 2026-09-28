# Sprachlauf binomische-formeln

Stand 2026-09-28 (Gruppe 2). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py binomische-formeln`: 0 Abweichungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 16 | 32 | 48 |
| e2.jsonl | 22 | 28 | 50 |
| e3.jsonl | 17 | 25 | 42 |
| zone.jsonl | 30 | 0 | 30 |
| gesamt | 85 | 85 | 170 |

Geänderte Sprossen: 41. Die 10 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1 …).

## Entscheidungen

- Reine Rechenzeilen mit „– Ergebnis?“, „– Wert?“, „– zusammengefasst?“
  bekommen ein Verb vorn („Berechne.“, „Fasse zusammen:“); „– ohne
  Klammer?“ wird einheitlich „Schreibe den Term ohne Klammer:“, auch
  für $-(x + 8)$ und $(5x)^2$, wo „Multipliziere aus“ schief wäre.
- Zone f7 „– ausgeklammert?“ wird „Klammere den gemeinsamen Faktor
  aus:“; der bestimmte Artikel deckt $4x \cdot (x - 2)$ als volle
  Lösung ab (nicht nur $4$ oder $x$).
- Fehler-finden-Zeilen ohne Namen bekommen eine Person und einen
  Auftrag ohne Zahlen („Lena soll die Klammern ausmultiplizieren.“),
  damit der Term nicht doppelt steht; die \rechnung bleibt
  zeichengleich. Bei e3 k2 s1 v1/v2 („lässt sich nicht
  faktorisieren“) bleibt die feste Schlussformel „rechne richtig“,
  obwohl die richtige Antwort „geht nicht“ ist.
- „Begründe am Flächenbild“ (e1 k3 s2, e2 k4 s2 v2) wird „Ein
  Rechteck/Quadrat hat die Seiten … Seine Fläche ist … Erkläre mit
  einer Skizze …“; das Wort „Flächenbild“ und das unklare „obwohl
  außen nur $x^2$ und eine Zahl stehen“ (e1 k3 s2 v3) entfallen.
- Ja/Nein-Vorstufen (e2 k1 s0, e3 k1 s0) werden „Kreuze an, ob …“
  bzw. drei kurze Sätze; \janein bleibt am Ende.
- Originale: 2017-OS-K5d (e2 k2 s10 v1/v2) bleiben unverändert, sie
  sind schon ganze Sätze; 2022-OS-K3c (v3/v4) nur aus dem Passiv
  „werden gleichgesetzt“ in „Setze $p(x)$ und $g(x)$ gleich.“ gelöst.
- Unverändert bleiben alle Zeilen „Multipliziere aus:“, „Fasse
  zusammen:“, „Faktorisiere:“, „Löse durch Faktorisieren:“ (Lösung
  zeigt $x_1$/$x_2$, Sprosse ist Formelverfahren), e3 k1 s10 und
  e3 k2 s2 v2/v3. Kein „:“ als Division im Eintrag.

## 10 Beispiele

1. `binomische-formeln-zone-f1-v1` – Multiplizieren mit Vorzeichen und Punkt vor Strich

   vorher: $(-4) \cdot (-8)$ – Ergebnis?

   nachher: Berechne. $(-4) \cdot (-8)$

2. `binomische-formeln-zone-f2-v3` – Termwert berechnen, auch mit negativer Zahl, als Probe einer

   vorher: $2x^2 - 3x$ für $x = -2$ – Termwert?

   nachher: Setze $x = -2$ in den Term $2x^2 - 3x$ ein. Berechne den Wert.

3. `binomische-formeln-zone-f4-v1` – Zahl mal Klammer und Minusklammer (Distributivgesetz, alle V

   vorher: $4 \cdot (x + 2)$ – ohne Klammer?

   nachher: Schreibe den Term ohne Klammer: $4 \cdot (x + 2)$

4. `binomische-formeln-zone-f4-v6` – Zahl mal Klammer und Minusklammer (Distributivgesetz, alle V

   vorher: $-(2x - 5)$ – ohne Klammer?

   nachher: Schreibe den Term ohne Klammer: $-(2x - 5)$

5. `binomische-formeln-zone-f6-v3` – Scheitelpunktform lesen

   vorher: $y = (x - 6)^2 - 7$ – Scheitel?

   nachher: Eine Parabel hat die Gleichung $y = (x - 6)^2 - 7$. Gib ihren Scheitelpunkt an.

6. `binomische-formeln-zone-f7-v4` – Ausklammern eines gemeinsamen Zahlfaktors oder einer Variabl

   vorher: $7x + 7$ – ausgeklammert?

   nachher: Klammere den gemeinsamen Faktor aus: $7x + 7$

7. `binomische-formeln-e1-k3-s2-v1` – Begründen (warum vier Produkte entstehen – Flächenbild eines

   vorher: Warum entstehen bei $(x + 2) \cdot (y + 5)$ vier Produkte? Begründe am Flächenbild eines Rechtecks.

   nachher: Ein Rechteck hat die Seiten $x + 2$ und $y + 5$. Seine Fläche ist $(x + 2) \cdot (y + 5)$. Erkläre mit einer Skizze des Rechtecks, warum beim Ausmultiplizieren vier Produkte entstehen.

8. `binomische-formeln-e2-k2-s10-v3` – Prüfungshöhe: Scheitelpunktform einer verschobenen Normalpar

   vorher: Die Parabel $p(x) = (x - 4)^2 - 3$ und die Gerade $g(x) = -2x + 5$ werden gleichgesetzt. Multipliziere aus und bringe die Gleichung in die Form „… $= 0$“. (P10 2022 OS)

   nachher: Eine Parabel hat die Gleichung $p(x) = (x - 4)^2 - 3$. Eine Gerade hat die Gleichung $g(x) = -2x + 5$. Setze $p(x)$ und $g(x)$ gleich. Multipliziere aus und bringe die Gleichung in die Form „… $= 0$“. (P10 2022 OS)

9. `binomische-formeln-e3-k1-s6-v1` – kein Binom erkennen und begründen (Mittelglied passt nicht,

   vorher: Lässt sich $x^2 + 64$ mit einer binomischen Formel faktorisieren? Begründe.

   nachher: Lässt sich $x^2 + 64$ mit einer binomischen Formel faktorisieren? Begründe deine Antwort.

10. `binomische-formeln-e3-k2-s2-v1` – Begründen (warum eine Summe zweier Quadrate keine binomische

   vorher: Warum lässt sich $x^2 + 16$ nicht mit einer binomischen Formel faktorisieren? Begründe.

   nachher: Erkläre, warum sich $x^2 + 16$ nicht mit einer binomischen Formel faktorisieren lässt.
