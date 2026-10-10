# Plan: Normalform und p-q-Formel (quadratische Gleichungen, E2), 2TB

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 9
(Katalog: OS Kl. 9–10, GYM Kl. 9), Oberschule, Ziel P10, allein.
Sicher (E1 und Terme): x² = c lösen, beide Lösungen; Klammern
ausmultiplizieren, binomische Formeln; Terme aus Text aufstellen.
Neu: Normalform, p-q-Formel. Abgrenzung zu quadratische Funktionen E4
(GHD): dort Nullstellen und Schnittpunkte am Graphen; hier nur die
Gleichung, ohne Graph, und Sachgleichungen (Zahlenrätsel, Automat,
Rechteck).

Bank: Die Bankdateien tragen die Folge vor dem Tausch vom 27.09.
(`bank/quadratische-gleichungen/stand.md`): die p-q-Kette liegt in
`e3.jsonl` (k3, k4), die Rechteck-Sprossen in `e4.jsonl` (k1). Die neuen
Zeilen stehen dort als neue Varianten; `e2.jsonl` (Nullprodukt) bleibt
unberührt.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe | braucht |
|---|---|
| x² − 6x + 7 = 0, Lösung 3 ± √2 und gerundet (2025-OS-K5c) | p, q mit Vorzeichen, −p/2 (A); Wurzel stehen lassen, am Ende runden (B) |
| 2x² + 8x + 6 = 0 erst durch 2 teilen (2020-OS-K3e) | durch die Zahl vor x² teilen (C) |
| −x² − 2x + 5 = −10 ordnen (2023-OS-K4c) | Zahl hinüber (A), durch −1 teilen (C) |
| x² + 2x − 1 = 3x + 1 gleichsetzen (2021-OS-K2c, 2024-OS-K3d) | x-Glieder auf beiden Seiten ordnen (C); p ungerade (B) |
| (x + 3)² − 2 = 0 bzw. Klammer zuerst (2017-OS-K5d, 2022-OS-K3c) | Klammer auflösen (C) |
| zwei, eine, keine Lösung | Wert unter der Wurzel (B) |
| Rechteck mit Seitenbeziehung und Fläche (Katalog E4, RLP G) | Gleichung selbst aufstellen, negative Länge streichen (D) |

## 2 Lernweg

| Kennung | Abschnitt | Grund für die Stelle | Ziel (Modell selbst, Antwortform) |
|---|---|---|---|
| A | Die p-q-Formel | Kern: p und q ablesen, einsetzen; Wurzel geht auf; nur „Zahl nach links“ als Ordnen | Bens Zahlenrätsel: ist 7 die einzige Zahl? (begründen) |
| B | Wurzel geht nicht auf – eine oder keine Lösung | p ungerade, runden am Ende, Wert unter der Wurzel entscheidet | Leas Zahlenrätsel: keine, eine, zwei Zahlen? (ankreuzen) |
| C | Erst in Normalform bringen | ordnen mit x auf beiden Seiten, teilen (auch −1), Klammer zuerst – die Formen der P10 | zwei Zahlenautomaten: wo gleich, wo größer, um wie viel? (vergleichen) |
| D | Sachgleichungen | Gleichung selbst aufstellen, Länge nie negativ, Antwort | Spielplatz: reicht der Zaun, wie viel fehlt? (entscheiden) |
| T | Probetest | je Form der P10 einmal, gemischt | Fenster: passt es in die Öffnung, um wie viel nicht? (entscheiden) |

## 3 Schritte je Ziel- und T-Aufgabe → Beispielschritt

Beispielschritte: A1 Zahl nach links, A2 p und q, A3 einsetzen, A4 Wurzel
und x₁, x₂, A5 Probe; B1 p ungerade, B2 nicht glatt, erst am Ende runden,
B3 negativ: keine, B4 null: eine; C1 Klammer, C2 alles nach links, C3
teilen, C4 Formel; D1 x nennen, Gleichung, D2 ordnen, D3 Formel, D4
negative Länge streichen, D5 Antwort und Probe.

| Aufgabe | Schritte | Beispielschritte |
|---|---|---|
| A4 Ben | Text → x² − 2x = 35 (Terme, Vorwissen); −35; p, q; einsetzen; x₁ = 7, x₂ = −5; Probe mit −5 | A1, A2, A3, A4, A5 |
| B4 Lea | Text → x² + 10x = −25; +25; p, q; unter der Wurzel 0 | A1, A2, A3, B4 |
| C5 Automaten | Text → 2x² − 3x = x + 6; alles nach links; durch 2; Formel; Werte einsetzen, Unterschied | C2, C3, C4, A5 |
| D4 Spielplatz | x, x + 10; x(x + 10) = 600; ordnen; Formel; −30 streichen; Umfang (Formel des Abschnitts); vergleichen | D1–D5 |
| T1 | p, q; einsetzen; √3 stehen lassen, runden | A2, A3, B2 |
| T2 | durch 4; Formel | C3, C4 |
| T3 | Zahl nach links; durch −1; Formel | A1, C3, C4 |
| T4 | Terme gleichsetzen; alles nach links; p ungerade; einsetzen | C2, B1, A5 |
| T5 | je Gleichung nur unter der Wurzel rechnen | B3, B4 |
| T6 Fenster | x, x + 0,5; Gleichung; ordnen; p = 0,5 (Dezimalzahl); −1,5 streichen; Maße vergleichen | D1–D5, B1 |

Lücke im ersten Entwurf: Teilen durch −1 kam in keinem Beispiel vor
(nur als Merksatz) – darum hat das Beispiel C die Zahl −2 vor x².
Binomische Formel: Beispiel C beginnt mit (x + 2)²; ohne das hätte C3b
keinen Beispielschritt.

## 4 Änderungen gegenüber dem Katalog

- Gestrichen: Vorstufe „einkreisen“ als Ankreuzaufgabe (A1 fragt p, q
  direkt), Fehler finden, Begründen als eigene Aufgabe, Vieta,
  grafisches Lösen, „Diskriminante“ als Wort (GYM, Niveau H), Rückwärts
  (Zahl so wählen) – bleiben im Bestand.
- Ordnen in zwei Stufen: „Zahl nach links“ schon in A (kleinster
  Schritt, P10 2023), x-Glieder beidseitig und Teilen in C.
- Sachgleichungen als D, weil die Ziele das Aufstellen ohnehin
  verlangen; Zahlenrätsel und Nachfolger dort nur einmal, die Einheit 4
  (Sachaufgaben) vertieft.

## 5 Zahlen

Alle mit sympy im Bauskript (`/root/work/w7e/tmp/bau.py`, nicht im
Repo): Lösungen jeder Gleichung, Normalform nach dem Ordnen, Rundung,
Seiten und Umfang. Glatte Lösungen außer B2, T1 und deren Vorrat.
Keine Normalform doppelt auf dem Blatt; keine Terme der Originale.
