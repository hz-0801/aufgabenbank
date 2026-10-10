# Plan: Kreisfläche (Kreis, Lerneinheit 2), E69

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 8 (Katalog:
OS und GYM Kl. 7–8, „im Lehrwerk Kl. 8, im Fahrplan Kl. 8“), allein,
Taschenrechner mit $\pi$; sicher: Quadrat und Wurzel, Dezimalzahlen,
Runden, Flächeneinheiten. Ziel P10. Erster Bau des Themas: Thema-Weg
und Lernweg in `katalog/kreis.md` neu angelegt. Kreisumfang (E1) ist
nicht gebaut: Radius, Durchmesser, $\pi$ zeigt Beispiel A, $u = \pi
\cdot d$ Beispiel D. Heft 6 Seiten: Übersicht, A–D, T.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe | braucht |
|---|---|
| Kreisfläche aus d = 2,14 m, zwei Stellen (2016-OS-K3b) | Durchmesser erkennen, halbieren, $\pi r^2$, runden (A) |
| Grundfläche eines Körpers aus r (2024-OS-K4a) | Kreis im Körper sehen, $\pi r^2$ statt $2\pi r$ (A, D) |
| Fehlerquelle u/A vertauscht (2024-OS-K4a, 2023-OS-K5a, 2022-OS-K2a) | Rand oder Fläche entscheiden (D) |
| Nebenleistung Rechteck mit zwei Halbkreisen (2017-OS-K3b) | Halbkreis, zwei Halbkreise = Kreis, Teilflächen addieren (B) |
| r aus A (2022-OS-K2d, Katalog „Wurzel vergessen“) | durch $\pi$, Wurzel, d = 2r (C) |

## 2 Lernweg

| Kennung | Abschnitt | Grund |
|---|---|---|
| A | Fläche aus Radius oder Durchmesser | Kern, mit Radius/Durchmesser und $\pi$ (E1 fehlt) |
| B | Halbkreis und Viertelkreis | Teilflächen; zwei Halbkreise, Rechteck dazu |
| C | Radius aus der Fläche | Umkehrung mit Wurzel |
| D | Fläche oder Umfang? | häufigster P10-Fehler; Tabelle r, d, u, A |
| T | Probetest | Formel wählen, P10-Form (d mit Dezimalzahl), r aus A, Entscheidung u und A |

Ziele (Modell selbst, Antwortform wechselt): A Pizza – eine große oder
zwei kleine, um wie viel (rechnen, Unterschied) · B Sprenger an der Hecke
– reicht eine Tüte (begründen) · C Ziege – kürzester Strick (ankreuzen) ·
D Teich – Anzahl Steine und Säcke (eintragen) · T Tischdecke – reichen
Stoff und Borte (zwei Urteile).

## 3 Schritte je Aufgabe → Beispiel

Beispielschritte: A1 Radius ablesen, A2 $\pi \cdot r^2$ mit Taste,
erst am Ende runden, A3 Durchmesser halbieren, A4 Dezimalzahl, zwei
Stellen, A5 vergleichen/Differenz · B1 gerade Seite = Durchmesser,
halbieren, B2 ganzer Kreis : 2, B3 Sache → Kreis, Ecke = Viertel, B4
ganzer Kreis : 4, B5 zwei Halbkreise = Kreis, Rechteck extra, addieren ·
C1 Formel mit A, C2 durch $\pi$ (nicht runden), C3 Wurzel, C4 d = 2r, C5
Probe · D1 Rand → $u = \pi d$, D2 innen → halbieren, $\pi r^2$, D3
Einheit umrechnen, teilen, D4 Anzahl aufrunden.

A1 (A2) · A2 (A1, A3, A2) · A3 (A2–A4, zwei Stellen) · A4 Ziel (A3, A2,
mal 2, A5). B1 (B2; B1–B2; B4) · B2 (B4 mit Buchstaben, Formelzeile) · B3
(B5, A3) · B4 Ziel (B3: gerade Hecke = halber Kreis, B2, A5). C1 (C2–C3)
· C2 (C2–C4) · C3 (C2–C4, zwei Stellen) · C4 Ziel (B3: Reichweite =
Radius, C2–C3, A5 vergleichen mit 3/4/5 m). D1 (D1, D2, Satz: Rad rollt
ab) · D2 (A3, D1, A2; $u = 2\pi r$ aus der Formelzeile) · D3 (D1, D2,
Formelzeile) · D4 Ziel (D1, D3, D4, D2, D3, D4). T1 (D1) · T2 (A3, A4) ·
T3 (C2–C3) · T4 (D2, D1, A5).

## 4 Nicht genommen

Fehler finden, Begründen (Tortenstücke) nach Bauauftrag 4; Umfang
rückwärts (E1); Kegel (Kl. 8 kennt ihn nicht, die Prüfungsform
2024-OS-K4a steht als Dose im Vorrat). Zahlen mit sympy in
`/root/work/w7c/tmp/bau.py` gerechnet und in die Lösungen geschrieben;
bank-pruef kreis: 0 Abweichungen (16 Mengenwarnungen e2, wie bei allen
Bauten Zusatzzeilen); Skizzen aus den Zahlen gezeichnet.

## 5 Ids

Blatt: A kreis-e2-k1-s2-v4 | kreis-e2-k1-s1-v6, kreis-e2-k1-s2-v5, kreis-e2-k1-s3-v6, kreis-e2-k3-s1-v4
B kreis-e2-k1-s4-v4 | kreis-e2-k1-s4-v5, kreis-e2-k2-s1-v4, kreis-e2-k1-s4-v6, kreis-e2-k5-s3-v4
C kreis-e2-k1-s6-v4 | kreis-e2-k1-s6-v5, kreis-e2-k1-s6-v6, kreis-e2-k1-s6-v7, kreis-e2-k1-s6-v8
D kreis-e2-k4-s1-v4 | kreis-e2-k4-s1-v5, kreis-e2-k1-s5-v6, kreis-e2-k1-s7-v4, kreis-e2-k5-s3-v6
T kreis-e2-k1-s0-v5, kreis-e2-k1-s8-v5, kreis-e2-k1-s6-v13, kreis-e2-k5-s3-v8
Vorrat: kreis-e2-k1-s1-v7, kreis-e2-k1-s2-v6, kreis-e2-k1-s3-v7, kreis-e2-k3-s1-v5, kreis-e2-k1-s4-v7, kreis-e2-k1-s4-v8, kreis-e2-k2-s1-v5, kreis-e2-k1-s4-v9, kreis-e2-k5-s3-v5, kreis-e2-k1-s6-v9, kreis-e2-k1-s6-v10, kreis-e2-k1-s6-v11, kreis-e2-k1-s6-v12, kreis-e2-k4-s1-v6, kreis-e2-k1-s5-v7, kreis-e2-k1-s7-v5, kreis-e2-k5-s3-v7, kreis-e2-k1-s8-v6, kreis-e2-k1-s0-v6, kreis-e2-k5-s3-v9
