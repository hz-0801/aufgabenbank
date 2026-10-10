# Plan: Wachstumsfaktor und Wachstumstabelle (potenz-exponentialfunktionen, Lerneinheit 2), SLM

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 10
(Katalog: OS Kl. 10, GYM Kl. 10), allein; sicher: Prozentrechnung mit
Wachstumsfaktor (Prozentrechnung E5), linear/exponentiell unterscheiden
(E1, TCQ). Ziel P10. Heft 6 Seiten: Übersicht + A–D + T.

## 1 Rückwärts von den Zielaufgaben (P10, Katalog „Zielmarke“)

| Zielaufgabe | braucht |
|---|---|
| Faktor als Quotient an einer Bakterientabelle nachweisen (2025-OS-K7b) | Quotient neu : alt, alle Quotienten, Faktor (B) |
| Prozentsatz an einer Umsatztabelle nachweisen (2018-OS-K2a) | Quotient → Faktor → Prozentsatz (A, B) |
| zwei Felder ergänzen, eines der Anfangswert (2026-FOR-K7a, 2020-OS-K4a) | Faktor aus %, Startwert in Schritt 0, mal q (A, C) |
| drei Werte, einer über mehrere Schritte mit Potenz (2019-OS-K7a, 2017-OS-K7a) | Schritte zählen, mal qⁿ, runden (C) |
| Wert und fehlende Zeitangabe in einer Zerfallstabelle (2016-OS-K4a) | q < 1, durch q zurück, mal q bis der Wert passt (D) |

Darunter liegt überall: Prozentsatz ↔ Faktor (A). Ohne den Faktor gibt
es keine Tabelle; darum A zuerst, dann der Faktor aus der Tabelle (B),
dann vorwärts (C), dann rückwärts und die fehlende Zeit (D).

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Faktor und Prozentsatz | Werkzeug für alles; Fallen 1,019 / 0,875 / 1,25 ≠ 1,025 |
| B | Faktor aus der Tabelle | Nachweis-Form der P10; Umkehrung von A am Material |
| C | Tabelle fortschreiben | Kern der P10 (5 Originale): Startwert, Lücke, Potenz |
| D | Zurückrechnen und fehlende Zeit | Umkehrrichtung von C; 2016-K4a |
| T | Probetest | Nachweis, Faktor, Tabelle (roter Faden Miete), Luftdruck |

Ziele (Modell selbst, Antwortform wechselt): A Angebote ankreuzen ·
B Behauptung an einer Tabelle prüfen (begründen) · C Tabelle ergänzen
und Zunahme angeben (eintragen) · D Startwert, fehlende Zeit, Behauptung
„weniger als ein Viertel“ (rechnen, entscheiden) · T Luftdruck:
Meereshöhe, fehlende Höhe, „24 % in 2 km“ prüfen (begründen).

Rundung einheitlich (Kasten „Achtung“, einmal): erst beim Eintragen
runden – Geld auf Cent, Anzahlen ganz, sonst eine Stelle nach dem Komma;
mit dem genauen Wert weiterrechnen. Alle Zahlen so gewählt, dass auch
das Weiterrechnen mit dem gerundeten Tabellenwert dasselbe Ergebnis gibt
(in `bau.py` geprüft, nicht im Repo).

## 3 Schritte je Aufgabe → Beispielschritt

- A-Bsp: 1 Zunahme oder Abnahme? · 2 Zunahme: q = 1 + p/100 (auch
  1,9 % → 1,019: Komma zwei Stellen nach links) · 3 Abnahme:
  q = 1 − p/100 · 4 vom Faktor zum Prozentsatz: Abstand zu 1 (0,85 →
  −15 %; 1,2 → +20 %).
  A1 (1–3) · A2 Kommaprozente, „halbiert“ (1–3; Hälfte = 50 % aus E1) ·
  A3 Faktor → Prozent (4) · A4 Ziel: 2,5 % → 1,025 (2), 1,25 und
  0,975 deuten (4).
- B-Bsp: 1 Quotienten neu : alt · 2 alle gleich → q; einer anders →
  nicht derselbe Prozentsatz · 3 q → Prozentsatz (A-Bsp 4) · 4 Antwort.
  B1 (1–4) · B2 Abnahme 0,8 (1–4) · B3 Nachweis 4 % mit Jahren (1–4) ·
  B4 Ziel: ein Quotient anders → Behauptung falsch (1, 2, 3).
- C-Bsp: 1 Faktor aus % (A) · 2 Startwert in Schritt 0 · 3 Lücke: mal q,
  Probe mit dem nächsten Wert · 4 Schritte zählen (6 − 3 = 3), mal q³,
  runden.
  C1 Guthaben, mal q dreimal, Cent (1, 3) · C2 Abnahme, Startwert (1–3) ·
  C3 Jahre zählen 2030 − 2020, Potenz, ganze Zahl (1–4) · C4 Ziel:
  Startwert, Lücke, Potenz, Zunahme bilden (1–4; Differenz ist Vorwissen).
- D-Bsp: 1 Faktor, Probe am Quotienten · 2 zurück: durch q (zwei Schritte:
  durch q²) · 3 fehlende Zeit: mal q, bis der Wert passt, Schritte zählen ·
  4 späterer Wert mit Potenz (C-Bsp 4).
  D1 einen Schritt zurück, zu und ab (1, 2) · D2 zwei Schritte zurück
  (2) · D3 fehlende Zeit (1, 3) · D4 Ziel: alle vier, Vergleich mit einem
  Viertel (Vorwissen).
- T1 → B-Bsp 1–4 · T2 → A-Bsp 2 (1,8 % → 1,018) · T3 → C-Bsp 1–4 (2026
  ist Schritt 0, 2031 sind 5 Schritte) · T4 → D-Bsp 2 (q²), 3; „24 %?“ →
  0,88² = 0,7744 (C-Bsp 4) und Abstand zu 1 (A-Bsp 4).

## 4 Abweichungen vom Katalog

- Vorstufen („mehr oder weniger“, „Differenz oder Quotient“) nicht als
  eigene Aufgabe: A-Bsp Schritt 1 und E1 decken sie.
- Wachstumsrate aus nicht benachbarten Werten (k1-s6, braucht eine
  Wurzel) nicht auf dem Blatt; zwei Schritte nur vorwärts/rückwärts mit
  q² (D2, T4). Gehört zu Einheit 3 (Gleichung), Zeile in befunde-M3.
- Fehler finden und Begründen (k3) nicht auf dem Blatt (Bauauftrag 4);
  die Fallen stehen im Beispiel und im Fehlerkasten.
- Zerfallstabelle (k2-s7) ohne eigene Aufgabe: C2, D-Bsp, D4, T4 sind
  Abnahmen.

## 5 Zahlen

Alle in `bau.py` (nicht im Repo) mit sympy geprüft (pruef = Rechenausdruck).
A: 1,03; 1,019; 0,96; 0,85 → −15 %; 1,2 → +20 % · 1,07; 0,93; 1,4; 0,98 ·
1,019; 0,875; 1,005; 0,5 · +8 %; −8 %; +35 %; −40 % · A und B (1,025).
B: 200·1,3ⁿ (439,4) · 50·1,2ⁿ (86,4) · 1500·0,8ⁿ (768) · 1250·1,04ⁿ
(1352) · 2400, 3000, 3750, 4500 (1,25; 1,25; 1,2).
C: 50·1,2ⁿ, Woche 6 ≈ 149,3 · 2000·1,05ⁿ (2315,25) · 640·0,75ⁿ (202,5) ·
40000·1,02¹⁰ ≈ 48 760 · 40·1,15ⁿ: 52,9; 70,0; 122,4; +82,4 kg.
D: 200·0,9ⁿ (Stunde 4; ≈ 106,3) · 520 : 1,04 = 500; 17 000 : 0,85 =
20 000 · 45 : 1,5² = 20 · 500·1,2ⁿ = 1036,8 bei n = 4 · 50·0,8ⁿ:
Stunde 4; ≈ 13,1 > 12,5.
T: 450 000·1,08ⁿ · 1,018 · 700·1,018ⁿ · 1000·0,88ⁿ: 774,4; 527,7 bei
5 km; 1 − 0,7744 = 22,56 % ≠ 24 %.
