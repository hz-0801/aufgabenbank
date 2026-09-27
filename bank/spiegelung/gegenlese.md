# Gegenlese – spiegelung

Datum: 2026-09-27 21:50 UTC
Modell: claude-opus-5-5
Geprüfte Zeilen: 117
Korrekturen: 0

## Entscheidungen

- Befunde stehen je Prüfpunkt unter einer Überschrift, eine Zeile je id; derselbe
  Befund an mehreren Zeilen steht je id einmal.
- Korrekturen stehen unter Punkt 1 mit „korrigiert:“ statt eines Vorschlags.
- Nachgerechnet mit sympy (Skripte zone.py, e1.py, e2.py, e3.py im Scratch-Ordner):
  jede Spiegelung auch als Gegenprobe über die Lotgerade, jede Symmetrieebene durch
  Spiegeln aller Ecken, Scharaufgaben für allgemeines t. Keine Rechnung ist falsch.
- Q steht in Einheit 1 für das Spiegelzentrum (k3 s1), den Ausgangspunkt (s3) und das
  Bild (s5). Der Merkkasten der Einheit macht es genauso, jede Aufgabe erklärt den
  Buchstaben: kein Befund je Zeile.
- Spiegelebene zweier Geraden (e2 s3) und Winkelhalbierende (e2 s5): Auch die Ebene
  mit dem Normalenvektor u − v bzw. die äußere Winkelhalbierende spiegelt g auf h. Die
  Aufgaben fragen nach „einer“ Ebene bzw. „einer Geraden“ wie das Original, und das
  Raute-Verfahren liefert die gegebene Lösung: kein Befund. Wer die andere angibt,
  hat auch recht.
- pruef-Werte bei Begründen- und Scharaufgaben (etwa 0, 1, [4, 2] für
  x₂ = (4t − 1)/2) sind nur Platzhalter an der Ergebnisstelle. Das Prüfskript nimmt sie
  an, deshalb kein Befund.
- Die doppelte Vorstufe über Einheitsgrenzen hinweg nennt stand.md als Katalogbefund.
  Befund hier ist nur, dass e2 dieselben vier Situationen wie e1 bringt, bloß anders
  formuliert.

## 1 Lösung und pruef

- keine

## 2 Eindeutig lösbar

- spiegelung-e2-k2-s1-v2: Die Schülerrechnung benutzt $\vec{u}$, $\vec{v}$, der Text
  führt sie nicht ein – im Text „$\vec{u} = (2 | 1 | 2)$ und $\vec{v} = (2 | 2 | 1)$“
  schreiben.
- spiegelung-e3-k1-s1-v2: Grundecken in der Folge A, B, C, D ergeben ein überschlagenes
  Viereck (A(−3|0), B(3|0), C(−2|4), D(2|4)) – C und D tauschen: C(2|4|1), D(−2|4|1).
- spiegelung-e3-k1-s6-v2: Für t = 1,5 ist die Grundfläche ein Quadrat 6 × 6. Die
  Pyramide hat dann vier Symmetrieebenen, nicht „die beiden“ – Zahlen so wählen, dass nie
  ein Quadrat entsteht, etwa A_t(3|4t + 5|0), B_t(−3|4t + 5|0), S_t(0|2t + 2|4)
  (Länge 4t + 6 > 6), oder t ≠ 1,5 verlangen.
- spiegelung-e3-k2-s1-v3: Für t = 3/4 ist die Grundfläche ein Quadrat 4 × 4, dann gibt es
  keine eindeutige „zweite Symmetrieebene“ – t > 1 verlangen.

## 3 Sprosse und Merkmal

- spiegelung-e2-k1-s0-v1: Inhaltlich gleich wie spiegelung-e1-k1-s0-v2 (Ebene aus
  Punkt und Spiegelpunkt), nur anders formuliert – eine neue Situation nehmen, etwa zwei
  Seitenflächen symmetrisch zu H.
- spiegelung-e2-k1-s0-v2: Inhaltlich gleich wie spiegelung-e1-k1-s0-v1 (Punkt an Ebene
  spiegeln) – eine neue Situation nehmen, etwa ein Dreieck an einer Ebene spiegeln.
- spiegelung-e2-k1-s0-v3: Inhaltlich gleich wie spiegelung-e1-k1-s0-v3 (Bildgerade
  angeben) – eine neue Situation nehmen, etwa den Spiegelpunkt über den Lotfußpunkt.
- spiegelung-e2-k1-s0-v4: Inhaltlich gleich wie spiegelung-e1-k1-s0-v4 (Ebene, die g
  auf h spiegelt) – eine neue Situation nehmen, etwa die Symmetrieebene eines Körpers
  aus einem Eckenpaar.
- spiegelung-e3-k1-s4-v1: s4 bringt gegenüber s3 kein neues Merkmal. Den Mittelwert
  verlangt schon s3 (x₁ = 2, x₂ = 2, x₁ = 2,5), dessen merkmal „über Mittelwerte“ nennt –
  s3 auf das Einzeichnen beschränken (Ebene nennen oder Körper ab dem Ursprung als halbe
  Kante). Sonst Reihenfolge s3/s4 als Katalogbefund in stand.md.
- spiegelung-e3-k1-s4-v2: wie e3-k1-s4-v1, kein neues Merkmal gegenüber s3.
- spiegelung-e3-k1-s4-v3: wie e3-k1-s4-v1. Hier liegt der Körper zudem wie in s3 am
  Ursprung (0 … 6, 0 … 4), der Mittelwert ist also nur die halbe Kante.

## 4 Schreibform

- spiegelung-e1-k3-s4-v2: Die Lösung nimmt den Weg über P − 2 · d · n⁰ mit der
  Seitenprüfung ohne Rechnung. Das steht nicht im Merkkasten, und die Sprosse heißt „über
  die Lotgerade“ – den Lotgeraden-Weg zeigen: (5 + 2λ | −1 − λ | 4 + 2λ) einsetzen,
  19 + 9λ = 1, λ = −2, bei 2λ = −4: P'(−3 | 3 | −4).

## 5 Ankreuzen

- keine

## 6 Fehler finden

- keine

Sauber: 105 Zeilen ohne Befund
