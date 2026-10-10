# Plan: Anwendungen (lineare Funktionen, Lerneinheit 5), PRC

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 8,
Oberschule, allein; sicher: f(x) = m·x + n lesen und zeichnen (E2, NKP),
einsetzen und rückwärts rechnen (E3, ZLZ), Schnittpunkt am Graphen
ablesen (E3 D), proportional oder mit Grundgebühr (E1, VUC). E4
(Gleichung bestimmen, Gleichsetzen) ist noch nicht gebaut; das
Gleichsetzen in der Sache wird darum hier in D vollständig vorgerechnet.
Ziel P10. Heft 6 Seiten: Übersicht + vier Abschnitte + Probetest.

## 1 Rückwärts von den Zielaufgaben (P10, Katalog „Zielmarke“)

| Zielaufgabe | braucht |
|---|---|
| Gleichung zu Tarif ankreuzen, Cent und Euro (2021-OS-K7a) | n = Startwert, m = je Einheit, Cent → € (A) |
| Gleichung aufstellen (2016-OS-K6c), aus Tabelle (2021-OS-K6a) | dasselbe, auch abnehmend, Startwert bei x = 0 (A) |
| Graph zu Tarif zuordnen und begründen (2016-OS-K6a, 2023-OS-K3a) | n und m im Sachgraphen mit Achseneinteilung, Ursprung, waagerecht (B) |
| Endwert (2022-OS-K6a), Mindestzahl aufgerundet (2022-OS-K6b) | einsetzen; Gleichung = Wert lösen; Runden nach der Sache (C) |
| Tarife vergleichen, Freimenge, günstigeren wählen (2023-OS-K3b, 2016-OS-K6b) | beide für eine Menge rechnen; ab wann: gleichsetzen (D) |

Darunter liegt überall: x und y mit Einheit benennen → Gleichung →
einsetzen, rückwärts oder gleichsetzen → Antwort in der Sache.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Gleichung aus dem Text | Grundhandgriff aller Sachaufgaben; erst ankreuzen, dann aufstellen, abnehmend, aus Tabelle |
| B | Graph und Sache | dieselbe Gleichung im Bild; Achseneinteilung; Zuordnen; Schnittpunkt ablesen bereitet D vor |
| C | Endwert und rückwärts | E3 A und C in der Sache, neu: Runden nach der Sache |
| D | Tarife vergleichen | mischt A–C; neu: zwei Terme gleichsetzen (x auf beiden Seiten) |
| T | Probetest | je Abschnitt eine Aufgabe, Ziel wie D |

Ziel je Abschnitt (Modell selbst finden, Antwortform wechselt):
A zwei Studios: Gleichungen, wo steigen die Kosten stärker, um wie viel?
(Unterschied) · B Kletterhalle: welche Gerade ist das Abo, ab wie vielen
Besuchen lohnt es? (ablesen, Entscheidung) · C E-Bike: reicht es nach
18 Monaten, wie viele Monate länger? (ja/nein, Unterschied) · D
Handwerker: wer ist bei 4 h günstiger, ab wann der andere? (Entscheidung,
gleichsetzen) · T Fahrradverleih: dasselbe ohne Beispiel.

## 3 Änderungen gegenüber Katalog und Thema-Weg

- Kette Anwendung (Katalog) läuft markieren → ankreuzen → aufstellen →
  Endwert → vergleichen → ab wann. Heft folgt ihr, schiebt aber den
  Sachgraphen (Graph zu Tarif zuordnen) als B vor das Rechnen, weil der
  Schnittpunkt am Graphen das Gleichsetzen in D anschaulich vorbereitet.
- Rückwärtsrechnen mit Runden (2022-OS-K6b) als eigener Schritt in C;
  „mindestens → aufrunden, höchstens → abrunden“ nur dort.
- Gleichsetzen in der Sache (eigentlich E4) hier vollständig im
  Beispiel D, weil E4 noch nicht gebaut ist.
- Nicht genommen: Fehler finden (k4-s1), Situation zu Gleichung
  beschreiben (k3-s1) – Bauauftrag 4 bzw. kein Platz auf 6 Seiten.

## 4 Feste Zahlen (sympy in `tmp/bau5.py`, pruef je Zeile)

A: Bsp 2,5x + 5; Strom 0,3x + 9; Umzug 0,25x + 39; Fass −12x + 160;
Tabelle 35x + 250; Ziel 24x + 19,9 / 29x → 5 €. B: Bsp Parkhaus 1,5x + 2;
Taxi 2x + 4; Boote 3x, 1,5x + 6, 15; Ziel 9x / 4x + 30 → 6, ab 7.
C: Bsp 35x + 240: 660, 21,7 → 22; Taxi 29,10 €; Kerze 12 cm; Handwerker
3,5 h; Kletterpark 26,5 → 26; Ziel 45x + 380: 1190 < 1450, 23,8 → 24,
6 Monate länger. D: Bsp 0,4x = 0,25x + 12 → 80 km; Strom 88/84; Boot
4x + 15 = 7x → 5; Mietwagen 97/94; Ziel 42x + 60 / 49x + 25: 228/221,
x = 5. T: 0,8x + 4,5; −25x + 200 → 8 min; 350x + 600: 1650, 5 h;
3x + 10 = 5x: 22/20, 5 h.
