# Plan: Baumdiagramm und Pfadregeln (Lerneinheit 3), Kennung 6KD

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 9
(Katalog: OS 8–10, P10 oft), allein, Ziel P10. Sicher: Einheit 2
(günstig durch möglich, Gegenereignis einstufig), Brüche multiplizieren
und kürzen. Neu: Baum, Pfad- und Summenregel, mehrstufiges Gegenereignis,
drei Stufen.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe | braucht |
|---|---|
| dreistufiger Baum, P(mindestens zwei Sechsen) (2020-OS-K6c, III) | Baum beschriften (A), drei Faktoren je Pfad, gleich viele Treffer = gleiche Wahrscheinlichkeit, „mindestens zwei“ = genau zwei + drei (D), Pfade addieren (B) |
| Baum zweier verschieden beschrifteter Würfel ergänzen, P(beide ungerade) (2026-FOR-K6b) | Astwahrscheinlichkeit je Gerät aus der Beschriftung, zweite Stufe anders als die erste (A, T1) |
| „nicht zweimal gerade“ (2026-FOR-K6c) | Gegenteil ist „zweimal“, nicht „zweimal ungerade“ (C) |
| P(12 oder 21), P(33) mit Behauptung (2025-OS-K3c, K3b) | Pfade zum Ereignis finden, je Pfad mal, dann plus (B) |
| zwei Scheiben zu P(13) = 25 % belegen (2025-OS-K3d) | Pfadregel rückwärts (A-Ziel, T5) |
| zweimal dieselbe Farbe, gleich gegen erst 6 (2014-OS-K6c, 2020-OS-K6b) | drei Pfade addieren, vergleichen (B) |
| Joker zwei Wochen, Zettel kommen zurück (2024-OS-K5b) | Pfadregel mit Zurücklegen (A) |

## 2 Lernweg

| Kennung | Abschnitt | Grund für die Stelle | Ziel (Modell selbst, Antwortform) |
|---|---|---|---|
| A | Baum und Pfadregel | Kern: Äste beschriften (Summe 1), Pfad mal; zwei Räder ohne Baum | Räder so belegen, dass P = 3/16 (eintragen) |
| B | Mehrere Pfade: plus | Summenregel; „34 oder 43“, „dieselbe Farbe“ | Ist das Spiel fair? (begründen) |
| C | Mindestens einmal: über das Gegenteil | „mindestens einmal“, „nicht zweimal“ | Ben: 1/6 + 1/6? Um wie viel daneben? (Unterschied) |
| D | Drei Stufen | Zielmarke der P10, verbindet A–C | Welches Spiel ist besser, A oder B? (vergleichen) |
| T | Probetest | je Rechenart eine Aufgabe: Baum ergänzen + Pfad (A), Summenregel (B, Ankreuzen), Gegenteil in Prozent (C), dreistufig mindestens zwei (D) | Wie viele rote Kugeln für 36 %? (Anzahl, Pfadregel rückwärts) |

Roter Faden: dasselbe Glücksrad (1 rot, 3 blau) in allen vier Beispielen –
zweimal Rot, genau einmal Rot, mindestens einmal Rot, dreimal genau
zweimal Rot. So ändert sich im Beispiel nur das Ereignis.

## 3 Änderungen gegenüber dem Katalog

- Gestrichen auf dem Blatt: Vorstufe „mit oder ohne Zurücklegen
  ankreuzen“ (gehört vor Einheit 4), Fehler finden, Begründen „warum die
  Äste zusammen 1 ergeben“ (steht im Satz von A), Baum → Zufallsversuch.
- Belegen (Katalog: vorletzte Sprosse) als Ziel von A: braucht nur die
  Pfadregel rückwärts.
- Behauptung prüfen als B-Ziel (fair?) und C-Ziel (Ben), nicht als eigene
  Stufe.
- Kein Fehlerkasten vor dem Probetest: jeder Hinweis steht einmal, im
  Satz des Abschnitts.

## 4 Zahlen

Alle mit Fraction gerechnet (Bauskript, 39 Rechnungen), dann
`werkzeuge/bank-pruef.py wahrscheinlichkeit`: 0 Abweichungen.
A: 1/16; 1/4; 6/25; 1/8; 3/16 = 3/4 · 1/4. B: 3/8; 0,48; 5/8; 19/50;
7/18 gegen 11/18. C: 7/16; 16/25; 5/9; 7/9; 11/36 statt 12/36.
D: 9/64; 1/64; 125/216; 0,384; 40 % gegen 44/125 = 35,2 %.
T: 1/9; 1/2; 39/64 ≈ 60,9 %; 13/125 = 10,4 %; 6 rote Kugeln.
