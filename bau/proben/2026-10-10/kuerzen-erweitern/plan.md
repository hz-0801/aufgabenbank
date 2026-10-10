# Plan: Kürzen und Erweitern (Brüche und Dezimalzahlen, Lerneinheit 2)

Bau 10.10.2026 (Opus) nach `bau/bauauftrag.md`, Standardlage. Kennung
A5D (reserviert). Thema-Weg von E1 (QG4) übernommen und ergänzt.

Lage: Klasse 6 Oberschule (Katalog: OS Kl. 5–6, GYM Kl. 5). Sicher:
Bruch als Anteil (E1), Einmaleins, Teiler und Vielfache. Allein, Ziel
P10 (E2 hat keinen eigenen Typ; Nebenleistung in 2014-OS-B1i).

## 1 Rückwärts von den Zielaufgaben

| Zielaufgabe | braucht |
|---|---|
| Kästchenfigur als Bruch, gekürzt, in Prozent (2014-OS-B1i) | vollständig kürzen (B); auf 100 erweitern (C) |
| Brüche vergleichen, Zahl dazwischen (E3, 2014-OS-B1c) | gleichnamig machen (C) |
| Zehnerbruch → Dezimalzahl (E4) | auf 10, 100 erweitern (C) |
| Anteile in Sachen beurteilen (gleich viel? hat er recht?) | Erweitern als Verfeinern (A), kürzen (B) |
| Geteilt-Aufgabe, Zeit in Stunden | Bruch > 1, gemischte Zahl (D) |

## 2 Lernweg (Heft 6 Seiten: Übersicht, A–D, Probetest)

| Abschnitt | Name | Grund für die Stelle |
|---|---|---|
| A | Erweitern und kürzen | Streifen zuerst (Verfeinern), dann Faktor erkennen, dann rechnen |
| B | Vollständig kürzen | P10-Nebenleistung; Größen (min, g, cm) als Bruchteil |
| C | Auf einen gemeinsamen Nenner bringen | gegebener Nenner, Nenner 100 → Prozent, gleichnamig |
| D | Brüche größer als 1: gemischte Zahlen | Bruch als Geteilt-Aufgabe, Ganze abspalten, zurück |
| T | Probetest | jede Rechenart aus A–D, P10-Form, Ziel |

Ziele (Antwortform wechselt): A Schokoriegel – wer hat mehr? (gleich
viel); B Test 21/28 – hat er recht? (ja); C Elfmeter 21/25 gegen 17/20
– wer trifft besser? (Prozent); D 14 Baguettes auf 4 Tische – wie viele,
wie schneiden?; T Urkunde ab drei Viertel – wer bekommt eine?

## 3 Änderungen gegenüber dem Katalog

- Nicht auf dem Blatt: Fehler finden, Begründen (Bank k4-s1/s2 hält sie).
- Prozent über Nenner 100 in C, weil die P10 „kürzen, dann Prozent“
  fragt; Hilfe „1/100 = 1 %“ in der Aufgabe (Kl. 6).
- Thema-Weg: Bau-Satz an Einheit 2 ergänzt.

## 4 Zahlen (64 Kontrollen mit sympy/Fraction, alle richtig)

A 6/8, 4/10, mal 5 · durch 7 · mal 8, 12/20 15/18 70/90, 5/6 3/7 4/7,
gleich viel. B 5/7; 3/4 2/3 2/5; 3/4 3/5 2/3; 16/24 = 2/3; 5/6 3/4
7/20; ja. C 9/12 10/12; 16/24 15/24 14/24; 30 % 35 % 48 %; 6/9 3/12
12/20; Nenner 12, 15, 24; 84 % < 85 %. D 3 2/5; 3 1/2 3 2/3 5 3/4;
7/4 17/6 38/9; 5/8, 2 1/4, 3 1/3; 2 1/4 h; 3 1/2. T 15 5 7; 3/4 3/5
2/3; Nenner 18, 20; 4 5/6, 27/8, 2 3/5; 7/20 = 35 %; nur Ole.

## 5 Form

Sorten selbst (6 Seiten) und tisch-alt, mit werkzeuge/setzer.py aus
den Bankzeilen. Grafiken als TikZ in grafik (Streifen, Gitter).
Päckchen-Brüche als \dfrac nach \par (sonst zu klein für Kl. 6).
