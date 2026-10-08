# Plan: Selbstlernheft „Geraden und Dreiecke im Koordinatensystem“ (Kl. 11, EP)

Start 2026-10-08. Schülerin allein, Test am Montag, sicher nur im P10-Stoff
(m und n ablesen, Steigungsdreieck, Gerade zeichnen).

## 1 Rückwärts von den Testaufgaben

Zwei Aufgabentypen tragen einen Test dieses Stoffs:

**Typ 1 – Dreieck ABC gegeben** („Seitenhalbierende, Mittelsenkrechte, Höhe,
Fläche, Innenwinkel“). Dafür braucht sie:

| Testfrage | braucht |
|---|---|
| Seitenhalbierende (Gleichung, Länge) | Mittelpunkt (A1), Gerade durch zwei Punkte (B3), Länge (A2) |
| Mittelsenkrechte | Mittelpunkt (A1), Steigung (B1), senkrechte Steigung (C1), Gerade durch Punkt mit Steigung (C3/B2) |
| Höhe, Lotfußpunkt | Seitengerade (B3), Senkrechte durch Punkt (C3), Schnittpunkt (C2) |
| Fläche | Koordinaten ablesen (Rechteckweg) oder Seite · Höhe (A2, D3) |
| Innenwinkel | Steigungswinkel (B6), Schnittwinkel-Gedanke (C4) |
| rechtwinklig? | m₁·m₂ = −1 (C1) |
| Schwerpunkt, Umkreismittelpunkt (Rand) | Schnittpunkt (C2) von zwei Seitenhalbierenden bzw. Mittelsenkrechten |

**Typ 2 – zwei Geraden** („Lage, Schnittpunkt, Schnittwinkel“): Steigungen
vergleichen (C1), gleichsetzen (C2), Steigungswinkel (B6) → Schnittwinkel (C4).

Darunter liegt überall: eine Gerade aus Angaben aufstellen (B1–B3), Punktprobe
(B4), Achsenschnittpunkte (B5).

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| V | Vorher: P10-Check | sie fängt mit etwas an, das sie kann |
| A1 | Mittelpunkt einer Strecke | nur Mittelwert, keine Gerade nötig |
| A2 | Länge einer Strecke | Pythagoras aus P10 |
| B1 | Steigung aus zwei Punkten | Steigungsdreieck als Rechnung |
| B2 | Gerade aus Punkt und Steigung | n durch Einsetzen |
| B3 | Gerade aus zwei Punkten, waagerecht/senkrecht | B1 + B2 |
| B4 | Punktprobe: auf, über, unter | Gleichung benutzen |
| B5 | Achsenschnittpunkte | Gleichung benutzen |
| B6 | Steigungswinkel | Grundlage für C4 und D5 |
| C1 | Lage zweier Geraden | nur Steigungen vergleichen |
| C2 | Schnittpunkt | Gleichsetzen |
| C3 | Parallele und Senkrechte durch einen Punkt | **neu**: Kern von Mittelsenkrechte, Höhe, Abstand |
| C4 | Schnittwinkel | aus B6 |
| D1 | Seitenhalbierende (+ Schwerpunkt) | A1 + B3 |
| D2 | Mittelsenkrechte (+ Umkreismittelpunkt) | A1 + C3 |
| D3 | Höhe, Lotfußpunkt, Abstand Punkt–Gerade | C3 + C2 + A2 |
| D4 | Flächeninhalt | Rechteckweg sicher, ½·g·h als Kontrolle |
| D5 | Innenwinkel | B6 + Kontrolle mit Skizze und Winkelsumme |
| T | Probetest (7 Aufgaben, ca. 45 min) | gemischt, neues Dreieck |

## 3 Änderungen gegenüber dem Vorschlag

- **C3 neu** (Parallele/Senkrechte durch einen Punkt): Mittelsenkrechte, Höhe
  und Abstand brauchen alle denselben Schritt „Steigung −1/m, dann n mit dem
  Punkt“. Einmal eigens geübt, sonst stolpert sie dreimal in D.
- **C2 Schnittpunkt direkt nach C1 Lage**: Testfrage lautet meist „Lage
  untersuchen, ggf. Schnittpunkt“.
- **Höhe und Abstand Punkt–Gerade zusammen (D3)**: dieselbe Rechnung
  (Lotgerade, Lotfußpunkt, Länge).
- **Schwerpunkt in D1, Umkreismittelpunkt in D2** als letzte Aufgabe (Rand).
- **Fläche (D4)**: Hauptweg umschließendes Rechteck minus drei rechtwinklige
  Dreiecke – nur Koordinatendifferenzen, keine Wurzeln, kein Lotfußpunkt;
  ½·g·h steht als zweiter Weg und als Kontrolle im Beispiel.
- **Innenwinkel (D5)**: Unterschied der Steigungswinkel, dann Kontrolle an der
  Skizze (spitz/stumpf) und Winkelsumme 180°.
- **Steigungswinkel** mit 0° ≤ α < 180° (m < 0: α = 180° + tan⁻¹ m), weil
  der Taschenrechner sonst negative Winkel liefert.
- **B4 Punktprobe** endet mit „auf der Geraden, aber auf der Strecke?“ (Lage
  Punkt–Gerade/Strecke).

## 4 Feste Zahlen

- Dreieck durch Teil D: **A(1|−4), B(7|2), C(−1|6)**. Seiten AB: y = x − 5,
  BC: y = −½x + 5,5, AC: y = −5x + 1; Mittelpunkte (4|−1), (3|4), (0|1);
  Lotfußpunkt von C auf AB: F(5|0); Fläche 36; Winkel 56,3°, 71,6°, 52,1°
  (bei B liefert der Unterschied der Steigungswinkel 108,4° → Falle sichtbar).
  Schon in A1, A2, B1, B3, B6 als letzte Aufgabe, damit sie es wiedererkennt.
- Umkreis-Dreieck (D2): P(−5|−4), Q(7|0), R(1|8), U(0|1), r = √50.
- Probetest-Dreieck: A(2|−4), B(6|0), C(0|4); s_c: y = −1,5x + 4,
  Mittelsenkrechte AB: y = −x + 2, F(5|−1), Fläche 20, α ≈ 59,0°.
- Alle Ergebnisse mit sympy nachgerechnet (Skript im Scratchpad, Werte im
  Lösungsheft).

## 5 Form je Abschnitt

Kennung, 1–2 Zeilen worum es geht, Formel, Beispiel in Schritten mit Skizze,
4–5 Aufgaben von leicht bis Testniveau (letzte grau als „Testniveau“
markiert). Rechnen auf einem extra Blatt; Lösungen mit Weg im Lösungsheft.
Seite 1 Übersicht mit Kästchen „kann ich“, Seite 2 Formelsammlung.
