# Plan: Punkte und Werte (lineare Funktionen, Lerneinheit 3), ZLZ

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 8,
Oberschule, allein; sicher: f(x) = m·x + n lesen und zeichnen (E2, NKP),
negative Zahlen und Brüche malnehmen, lineare Gleichung zweischrittig
lösen (Blatt 0). Ziel P10. Heft 6 Seiten: Übersicht + vier Abschnitte
+ Probetest.

## 1 Rückwärts von den Zielaufgaben (P10, Katalog „Zielmarke“)

| Zielaufgabe | braucht |
|---|---|
| y = ½x + 1 an der Stelle −10 (2017-OS-K5b) | einsetzen mit Klammer, Bruch mal Zahl (A) |
| Punktprobe, Wertetabelle zuordnen (Funktionen allgemein) | Funktionswert mit y vergleichen; am Graphen nicht genau genug (B) |
| Nullstelle berechnen, x = 1,5 (2022-OS-K3a) | Term = Wert, nach x lösen (C), Sonderfall Wert 0 (D) |
| y = −0,2x + 40 → nach 200 min leer (2021-OS-K6d) | Nullstelle in der Sache mit Dezimalsteigung (D Ziel) |
| Nullstelle und Schnittpunkt am Graphen ablesen (2019-OS-K2a, 2023-OS-K4a) | Achsenschnittpunkte als Punkte schreiben, Schnittpunkt ablesen (D) |

Darunter liegt überall: lesen, ob x oder y gegeben ist → einsetzen
oder gleichsetzen → Ergebnis als Zahl oder Punkt → Frage beantworten.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Funktionswert berechnen | Grundhandgriff; erst ganz, dann negativ, dann Bruch, Wertetabelle |
| B | Liegt der Punkt auf der Geraden? | A plus Vergleich; Punkt außerhalb des Bildes zwingt zum Rechnen |
| C | x zum Funktionswert finden | Umkehrung von A; eigener Handgriff (−n, :m) |
| D | Nullstelle und Schnittpunkte mit den Achsen | Sonderfall von C (Wert 0); Achsenpunkte; Schnittpunkt ablesen |
| T | Probetest | je Abschnitt eine Aufgabe, Ziel vergleicht zwei Nullstellen |

Ziel je Abschnitt (Modell selbst finden, Antwortform wechselt):
A Akku: x selbst bestimmen (hin und zurück), reicht es? (ja/nein) ·
B Gerade in Worten, welcher Punkt liegt darauf? (ankreuzen) ·
C Sparen: wann reicht es? x ≈ 14,4 → 15 Wochen (aufrunden) ·
D Öltank: wann leer, wie viele Tage Reserve? (Unterschied) ·
T zwei Kerzen: welche brennt länger, um wie viel? (Vergleich).

## 3 Änderungen gegenüber Katalog und Thema-Weg

- Thema-Weg Punkt 3 ergänzt: Folge A–D, Rückwärtsrechnen vor der
  Nullstelle; Schnittpunkt zweier Geraden am Graphen ablesen schon hier
  (2023-OS-K4a), rechnerisch erst E4.
- Fehler finden (k5-s1) und Begründen ohne Rechnung (k5-s2) nicht
  genommen (Bauauftrag 4); Falle Nullstelle/n steht in der Fehlerliste.
- x als Dezimalzahl (k2-s3) nicht eigens: Dezimalzahlen stehen in m
  (C4, D2, Ziele), wie in den Originalen.
- Rechenplatz: höchstens zwei Bilder je Seite (B, D), damit Karo bleibt.

## 4 Feste Zahlen (sympy in `tmp/bau.py`, `pruef` je Zeile)

A: Bsp ½x + 4 bei −6 → 1; 3x − 2: 10, −2; −2x + 5: −1, 13; ¾x − 1: 5, −4;
Tabelle −2x + 1; Ziel −2,5x + 100 bei 36 → 10 %. B: Bsp −2x + 1, P(−2|5)
ja, Q(1|−2) nein; 2x − 3; −3x + 2; ⅔x − 1; Graph 2x + 1, P(10|20) nein
(21); Ziel 3x − 2 → B(5|13). C: Bsp −3x + 4 = 19 → −5; 2x + 3 = 11 → 4;
−4x + 1 = 13 → −3; ½x − 2 = 3 → 10; −0,4x + 1 = 5 → −10; Ziel
4,5x + 35 = 100 → 14,4 → 15 Wochen. D: Bsp 2x − 5 → 2,5; 4x − 8 → 2;
−2x + 7 → 3,5; Graph ½x − 1 und −x + 5: N 2, S(4|1); Ziel −7,5x + 1200
→ 160, Reserve 10. T: −⅓x + 2: 5, 0; ¾x + 2 bei −4 → −1 ja; −3x + 5 =
−10 → 5; 0,5x + 3 → −6; Kerzen 10 h und 12 h → B, 2 h.
