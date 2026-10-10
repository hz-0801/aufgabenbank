# Plan: Säulen-, Balken- und Liniendiagramme (daten, Lerneinheit 2), T74

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 6 (Katalog:
OS Kl. 5–6, GYM 5), allein; sicher: Zahlen ordnen, Skalen ablesen,
Grundrechnen (Blatt 0). Ziel P10. Heft 6 Seiten: Übersicht + A–D + T;
Lösungen 2 Seiten.

## 1 Rückwärts von den Zielaufgaben (Katalog „Zielmarke“)

| Zielaufgabe | braucht |
|---|---|
| Achse ohne Zahlen: Kästchenwert aus Säule mit bekanntem Wert, Säule zuordnen, dritte zeichnen (2023-OS-K6d, 2018-OS-K3a) | Kästchenwert (A), Höhe ↔ Wert in beide Richtungen (A, D) |
| Wert mit „in Tausend“ vollständig (2016-OS-K2b) | Achsenbeschriftung lesen (A) |
| Werte über einer Schwelle, Grenzwert (Typische Fehler) | alle Werte ablesen, „mehr als“ (B) |
| Liniendiagramm: Anstieg, Rückgang | Änderung = später − früher, steilste Strecke (C) |

## 2 Lernweg

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Säulen ablesen | Grundhandgriff: Kästchenwert, dann Wert; „in Tausend“ |
| B | Werte vergleichen und auswählen | A auf mehrere Werte; Balken als neue Lage |
| C | Liniendiagramme lesen | Ablesen plus Änderung zwischen Punkten |
| D | Säulen zeichnen und Achse einteilen | Umkehrung von A; Achse ohne Zahlen = Prüfungshöhe |
| T | Probetest | je Abschnitt eine Aufgabe, Ziel: zeichnen und Unterschied |

Ziele (Modell selbst, Antwortform wechselt): A Freibad-Preis (ja/nein mit
Wert) · B Kino-Zuschlag (Anzahl Tage → Betrag) · C Wassertank (welcher
Monat?) · D Verein (zuordnen und zeichnen) · T Kiosk (zeichnen und um wie
viel).

## 3 Abweichungen

- Fehler finden (k4-s1) und Begründen (k4-s2) nicht genommen
  (Bauauftrag 4); „Diagramm aus Tabelle zeichnen“ (k3-s1) nur im Vorrat D,
  weil die Seite sonst keinen Rechenplatz hat; der Probetest verlangt es
  nicht.
- Balkendiagramme als eigenes TikZ (erste Kategorie oben, 0,55 cm je
  Zeile); `\balkenab` ist mit mindestens 0,73 cm je Zeile für die rechte
  Spalte zu hoch.
- Säulen und Linien mit `\saeulenab`/`\liniendia`, Höhe 1,9 cm, höchstens
  12 Hilfslinien, jede Hauptlinie beziffert.

## 4 Zahlen

Alle in `bau.py` (Bauskript, nicht im Repo) mit sympy/Asserts geprüft:
jeder Wert liegt auf einer Hilfslinie, Schwellen und Steilstellen
eindeutig. A: 45; 10/25/0,1; 6, 14; 35 000/120 000/2 500; Juli 13 000.
B: 220−80=140; 50; Mo, Fr; 3·50=150 €. C: März 30 €; 6 °C, +7; 2022 −10;
Juni (30 cm, Mai genau 20). D: 7 Kästchen; 9 Kästchen; 15 je Kästchen →
105, 75; 30 je Kästchen → Schwimmen, Tennis 3. T: 2 500; Di, Do, 40;
März 3 kg; 15 je Kästchen → Sa 8, 45 €.
