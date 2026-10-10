# Plan: Dezimalzahlen (Brüche und Dezimalzahlen, Lerneinheit 4)

Bau 10.10.2026 (Opus) nach `bau/bauauftrag.md`, Standardlage. Kennung
DXZ (reserviert). Thema-Weg von E1–E3 (QG4, A5D, FS9) übernommen und
für E4 ergänzt.

Lage: Klasse 6 Oberschule (Katalog: OS Kl. 5, GYM Kl. 5–6; Serie wie
A5D, FS9). Sicher: Bruch als Anteil, Kürzen, Erweitern, Brüche am
Zahlenstrahl (E1–E3); Größen mit Komma (Vorher). Allein, Ziel P10 (E4
ohne eigenen Typ; Umwandeln ist Nebenleistung).

## 1 Rückwärts von den Zielaufgaben

| Zielaufgabe | braucht |
|---|---|
| Zahlen in verschiedenen Darstellungen vergleichen (2015-OS-B1c 3/2, 2018-OS-B1d 5 % gegen 0,5, 2023-OS-B1f) – Typ in E5 | Bruch → Dezimalzahl sicher: Zehnerbruch (A), erweitern (C), teilen (D) |
| Zahl zwischen 1/2 und 4/5 (2014-OS-B1c) | 1/2 = 0,5, 4/5 = 0,8 (C); Lage am Strahl (B) |
| 3/4 von 1,2 kg (2018-OS-B1a) | Dezimalgrößen lesen, kg ↔ g (A, C) |
| Mitte zweier Zahlen (2020-OS-B1f) – E5 | Hundertstel zwischen zwei Zehnteln (B) |

## 2 Lernweg (Heft 6 Seiten: Übersicht, A–D, Probetest)

| Abschnitt | Name | Grund für die Stelle |
|---|---|---|
| A | Zehntel, Hundertstel, Tausendstel | Stellenwert und Zehnerbruch zuerst; Nullen sind der häufigste Fehler |
| B | Am Zahlenstrahl: ablesen, eintragen, weiterzählen | Lage sichtbar; Nachbarzehntel und Weiterzählen über die Einerstelle (2,9 → 3,0) |
| C | Bruch und Dezimalzahl: erweitern und kürzen | braucht A und Erweitern (E2); beide Richtungen |
| D | Teilen: Zähler durch Nenner, auch periodisch | wo kein Zehnerbruch passt (Achtel, Drittel, Sechstel) |
| T | Probetest | jede Fertigkeit aus A–D, P10-Ankreuzform |

Ziele (Antwortform wechselt): A Sprint 12,07 s gegen 12,7 s – Anzeige
ankreuzen, wer schneller (ankreuzen); B Weitsprung 3,46 m – zwischen
welchen Strichen, welcher näher (zuordnen); C Waage 3/4 kg gegen 0,7 kg
– wie viel Gramm fehlen (rechnen); D Band 5 m in 8 Stücke – reicht ein
Stück für 60 cm (begründen); T Mehl 3/8 kg gegen 0,4 kg – zu viel oder
zu wenig, um wie viel (rechnen).

## 3 Änderungen gegenüber dem Katalog

- Stellenwerttafel steht im Beispiel A und in A3, nicht als eigener
  Abschnitt; „Stellen einzeln gegeben“ (k1-s2) entfällt, die Tafel
  zeigt dasselbe.
- Achtel über Division (D), nicht über Erweitern auf 1000 (zu viel für
  Kl. 6 allein).
- Vergleichen und Ordnen bleiben in E5; in E4 nur, wo die Sache es
  verlangt (Zeiten, Gramm), über Stellenwert oder Einheit.
- Nicht auf dem Blatt: Fehler finden, Begründen (Bank k4-s1/s2);
  Prozent (E5, prozentrechnung.md).
- Formelkasten S. 1 nur Erweitern und Kürzen (Vorwissen); die zwei
  Fehler (Bruchstrich als Komma, Nullen) stehen nur dort.

## 4 Zahlen (Fraction-Prüfung im Bauskript, 39 Prüfungen, alle richtig)

A 23/1000 = 0,023; 0,3 0,9 0,47 0,81; 0,06 0,006 0,052 0,09; 4,058;
7/10 13/100 8/100 2019/1000; 12,07 s, Ben.
B A = 2,6; 0,4 0,9 1,3; 0,43 0,49 0,56; 3,4|3,5 0,7|0,8 5,0|5,1
1,9|2,0; 2,9 3,0 3,1 / 1,0 1,2 1,4 / 4,99 5,00 5,01; 3,4–3,5 m, näher 3,5.
C 7/20 = 0,35; 0,5 0,6 0,8 1,5; 0,75 0,45 0,24 0,14; 2/5 1/4 13/20 6/5;
Paare; 50 g. D 3/8 = 0,375; 0,25 0,75 0,125 0,875; 2,25 1,375 2,625;
0,‾3 0,‾6 0,‾5 0,1‾6; ja ja nein ja; ja, 62,5 cm.
T 0,9 0,09 0,045; 1,26 1,35; 0,6 0,85 9/20; 0,875 0,‾6; 7/20 = 0,35;
25 g zu viel.

## 5 Form

Sorten selbst (6 Seiten, Lösungen 2 Seiten) und tisch-alt, mit
werkzeuge/setzer.py aus den Bankzeilen. Grafiken TikZ (Zahlenstrahl)
und \sachtabelle (Stellenwerttafel). Ankreuzoptionen mit Brüchen als
\dfrac (T5), damit sie lesbar bleiben.
