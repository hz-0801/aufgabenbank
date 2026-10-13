# Blatt P Wahrscheinlichkeit, VRK1 (13.10.2026, aus Daten, pruefheft.py v0.11; Runde 8, Lehrer 13.10.)
Blatt 4 Seiten (Seite 4 halb: Zufallsgerät und Fundstellen), Lösung 2, Übersicht 1; 14 Nummern =
alle 11 Originale 2022–2026 (nur 2024, 2025, 2026 haben das Kapitel) und vier Anstöße (4, 7, 10, 12).
Ein Blatt statt zwei: „Wahrscheinlichkeit einstufig“ hat in fünf Jahren nur drei Originale und wird
Stufe (pruefung.md § 5, Grenze ≤ 4 Originale); Zuschnitt bleibt „Baumdiagramm und Pfadregeln“, Anzeige
„Wahrscheinlichkeit“, KWF nie gesetzt. Karo 0,75/0,5 spart keine Seite.
Stufen (Jahre im Kopf, keine „fast immer“):
- Ergebnisse aufzählen: 1 ’25-3a · Wahrscheinlichkeit angeben: 2 ’26-6a, 3 ’24-5a
- Baum ergänzen: 4 Anstoß „fehlender Ast = 1 − bekannter“, 5 ’26-6b, 6 ’24-5b
- Pfad- und Summenregel: 7 „mal oder plus?“, 8 a/b ’25-3b/3c, 9 ’26-6c (Gegenereignis, schwerste)
- ohne Zurücklegen: 10 „was liegt noch in der Dose?“, 11 ’24-5c
- Zufallsgerät entwerfen: 12 „3/16 als Produkt zweier Viertel“, 13 ’25-3d, 14 ’26-6d
Gegenereignis ist keine Stufe (ein Original, 2026-6c; Stufe braucht mehr als eins) – erster Schritt
dort ist der Gegen-Pfad mit der Pfadregel. Gliederung und Plätze nachgezogen.
Abbildungen als TikZ zu den neuen Zahlen: Scheiben (2,3,3,4 | 4,2,3,2), Würfelnetze (A 2,2,2,3,4,5,
B 1,3,3,4,5,6), Bäume mit nur den Vorgaben des Originals (4/6 und 2/6 bzw. 5/6), leere Scheiben/Netz.
Antwortzeilen je Größe (P(2), P(34), P(E) …); Lösung rechts mit Ansatz (Pfad, 1 − …, 5/6 · 1/5).
Zahlen mit sympy durch Auszählen nachgerechnet (1/8, 3/16, 2/9, 7/9, 1/6, 1/36, 12,5 %); mehr-pruef.py
ohne Meldung. 2025-3b: 34 ist doppelt so wahrscheinlich wie 24 (wie im Original 22 vs. 33).
Daten: gliederung/wahrscheinlichkeit.md, mehr-p10/wahrscheinlichkeit.csv, zuordnung-wahrscheinlichkeit.csv.
Offen (Lehrer):
- Vier Seiten statt zwei: Grenze „solange das Blatt zwei Seiten hält“ reißt schon ohne die einstufigen
  (Bäume und Sachtexte sind lang). Weg A ein Blatt mit 4 Seiten (so gesetzt), Weg B zwei Blätter wie
  bisher (einstufig 1 Seite, Baum 3 Seiten).
