# Zweitlesung potenzen-wurzeln

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 257
(zone 46, e1 79, e2 68, e3 64)

Prüfung: Jede Zeile aller vier Dateien gelesen (Aufgabe, Antwortgerüst,
Lösung, pruef, Sprossentext, Merkmal, Original). Alle Ergebnisse mit
eigenem Rechenweg nachgerechnet, die nicht trivialen mit einem
sympy-Skript mit exakter Arithmetik und kaufmännischer Rundung
(Potenzwerte mit Taschenrechner, Exponenten über log, negative
Hochzahlen als Bruch, Vergleiche und Ordnungen, Rundung in
Zehnerpotenzschreibweise, Sachaufgaben Mikrowelt/Astronomie, alle
Wurzel-Näherungswerte, Kathete, Zylinderradius, p-q-Formel mit
solve). Alle 222 Zeilen mit pruef-Zahl stimmen mit loesung überein,
auch nach Rundung; keine rechnerische Abweichung. 35 Ankreuzzeilen
einzeln gegen jede Option geprüft (auch Gleichheitsfälle wie
2,25 < 9/4 und 1,75 > 7/4): je genau eine Option richtig, loesung
nennt sie wortgleich. 10 Fehler-finden-Zeilen: der eingebaute Fehler
ist jeweils falsch und entspricht einem Muster aus „Typische Fehler“,
die Richtigrechnung stimmt. Verfremdung der Originale gegen Abschnitt
2 der Mappe abgeglichen (Form, Falle, andere Zahlen). bank-pruef.py:
Abweichungen 0, Warnungen 0.

## Befunde

zone-f6-v4: [M] Die Fertigkeit nennt ausdrücklich „√ mit Klammer für
den Term darunter“, EXP und Anzeige mit E; der Klammer-Fallstrick ist
hier nur als $(18 + 42) : 6$ geübt, keine Zone-Zeile berührt eine
der genannten Tasten – Fallstrick an der Wurzeltaste stellen, etwa
$\sqrt{(19 + 30)}$ mit dem Taschenrechner (ohne Klammer 34,36 statt 7).

e2-k1-s0-v3, e2-k1-s0-v4: [E] „wandert das Komma so viele Stellen, wie
Nullen dastehen?“ sagt nicht, wohin das Komma wandert (in die Form
a · 10ⁿ); ohne diesen Bezug ist die Frage für eine ganze Zahl ohne
Komma unklar – ergänzen: „Beim Schreiben als $6{,}3 \cdot 10^{\square}$:
wandert das Komma …“ bzw. „als $5 \cdot 10^{\square}$“.

e2-k1-s13-v3: [E] „welche Tasten tippst du?“ hängt vom Rechnermodell
ab (EXP, EE oder ×10ˣ); loesung nennt nur EXP – in loesung „EXP (oder
×10ˣ/EE)“ aufnehmen, wie es Sprosse und Voraussetzungen tun.

e3-k3-s2-v2: [E] Die Begründung „66 liegt nur 2 über 64, aber 15 unter
81“ trägt nicht allgemein (für 72,3 läge die Zahl näher an 64 als an
81, die Wurzel aber näher an 9, weil 8,5² = 72,25); Ergebnis stimmt
– Kern ersetzen durch „8,5² = 72,25 und 66 < 72,25, also
√66 < 8,5“.

Sauber: 252 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k1-s0-v3 und e2-k1-s0-v4 – die Frage nach dem wandernden Komma nennt die Zielform a · 10ⁿ nicht; beide schlagen denselben Zusatz „= 6,3 · 10^□“ bzw. „= 5 · 10^□“ vor.

Nur Erstleser: e2-k1-s16-v3 (Vorfaktoren 2 · 4 als zusätzlicher Schritt gegenüber v1/v2) – bestätigt, aber leicht: die Variante ändert mehr als das Merkmal „Hochzahlen addieren oder subtrahieren“; ich hatte sie übersehen, weil das Original 2015-OS-K3c genau mit Vorfaktoren rechnet – sauberer wäre, v3 durch eine reine Zehnerpotenz zu ersetzen und die Vorfaktor-Form der Prüfungshöhe oder einer eigenen Sprosse zu lassen.
Nur Erstleser: e2-k1-s15-v3 (1,7 · 10²¹ · 100 verlangt das Addieren der Hochzahlen, das erst in s16 kommt) – teilweise bestätigt: „mal 100 heißt Hochzahl um zwei größer“ lässt sich über Kommaverschiebung begründen, die Lösung schreibt aber 10²¹ · 10² = 10²³ und greift damit s16 vor; Tausch der Zeile hinter s16 oder eine Sachaufgabe ohne Hochzahladdition ist die bessere Lösung.

Nur Zweitleser: zone-f6-v4 – der Taschenrechner-Fallstrick übt die Klammer ohne Wurzeltaste, obwohl die Fertigkeit „√ mit Klammer“ nennt (M).
Nur Zweitleser: e2-k1-s13-v3 – loesung nennt nur die Taste EXP, nicht ×10ˣ/EE (E).
Nur Zweitleser: e3-k3-s2-v2 – die Begründung über den Abstand zu 64 und 81 trägt nicht allgemein, tragfähig ist 8,5² = 72,25 > 66 (E).

Widersprüche: keine
