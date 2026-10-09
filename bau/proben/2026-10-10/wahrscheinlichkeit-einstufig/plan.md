# Plan: Wahrscheinlichkeit einstufig (Lerneinheit 2), Kennung KUV

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 7
(Katalog: OS 6–7), allein, Ziel P10. Sicher: Brüche kürzen, Bruch –
Dezimalzahl – Prozent, Zählen (Einheit 1). Neu: alles Übrige.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe | braucht |
|---|---|
| Endziffer-Lose, P = 7/80, Behauptung (2016-OS-K5d, III) | eingeschränkte Grundmenge, Ausnahme abziehen, Nummernbereich zählen (D, B) |
| Pfannkuchen 2/14 statt 2/16 (2018-OS-K7b) | Grundmenge nach Entnahme (D) |
| Stifte 3/20 = 15 %, Lampen 5/100, Lose 20/100 (2019-OS-K6a, 2016-OS-B1f, 2014-OS-B1b) | alle mitzählen, Prozent (B) |
| Lose 101–900 → 1/800 (2016-OS-K5c) | von … bis …: plus 1 (B) |
| weder 1 noch 6 (2014-OS-B1d) | Gegenereignis (C) |
| Glücksrad 3/8, Würfel mit zwei Zweien (2014-OS-K6a, 2026-FOR-K6a) | Felder zählen, nicht Farben (A) |
| Topf mit P = 50 % (2015-OS-B1a) | Anteil statt Anzahl vergleichen (A-Ziel) |
| Glücksrad 40 % → 2 Felder; Kugeln zu P = 2/3 (2018-OS-B1j, 2019-OS-B1g) | rückwärts: Felder/Kugeln aus P (E) |
| relative Häufigkeit, erwartete Anzahl (RLP E) | Vorhersage „ungefähr“ (E) |

## 2 Lernweg

| Kennung | Abschnitt | Grund für die Stelle | Ziel (Modell selbst, entscheiden) |
|---|---|---|---|
| A | Günstig durch möglich | Kern; kleine Zahlen | Welcher Beutel? 3/8 gegen 4/12 |
| B | Alle mitzählen, in Prozent | P10-Form: Gesamtzahl aus dem Text, Prozent | Welche Losbude? 25 % gegen 22 % |
| C | Gegenereignis | vor D, weil Einheit 3 es braucht | Ist das Würfelspiel fair? |
| D | Wenn sich die Grundmenge ändert | Entnahme, eingeschränkt; bereitet E4 vor | Endziffer-Lose, > 10 %? (nach 2016-OS-K5d) |
| E | Zufallsgerät bauen und vorhersagen | Umkehrung und Vorhersage | Reichen 50 Teddys? |
| T | Probetest | gemischt, Ankreuzform mit Farbfalle | Glücksrad entwerfen, reichen 70 Preise? |

## 3 Änderungen gegenüber dem Katalog

- Gestrichen auf dem Blatt: Vorstufe „möglich/günstig unterstreichen“,
  Fehler finden, Begründen „warum Laplace“ (Bauauftrag: keine
  Fehler-finden-Aufgaben; erklären tut das Beispiel).
- „Topf mit 50 % auswählen“ als Vergleich zweier Beutel (A-Ziel).
- Relative Häufigkeit nur einmal (E3), weil die Prüfung sie hier selten
  verlangt (Katalog: Vorrat daten.md).

## 4 Zahlen

Alle mit Fraction/sympy gerechnet und gegen pruef geprüft (Bauskript),
dann `werkzeuge/bank-pruef.py wahrscheinlichkeit`: 0 Abweichungen.
