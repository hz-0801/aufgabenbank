# Zweitlesung tangente-normale-schnittwinkel

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 247
(zone 26, e1 51, e2 51, e3 32, e4 48, e5 39)

Prüfung: Jede Zeile aller sechs jsonl-Dateien einzeln gelesen und aus
dem Aufgabentext nachgerechnet (Funktionswerte, Ableitungen,
Tangenten-, Normalen- und Lotgleichungen, Achsenabschnitte, Flächen,
Umfänge, Winkel über den Arkustangens im Gradmaß); mit sympy/Skript
eigens geprüft: die Faktorisierung und Wurzel in e2-k2-s1-v1
((u + 1)²(3u² − 2u − 15), u ≈ 2,59), die Berührbedingungen der
Kamera-Aufgaben e2-k1-s9-v1/v2 (a = −2 bzw. −6, 12), die Eindeutigkeit
der Lösung von f′(x) = tan(−30°) in [0; 2] in e4-k1-s9-v3 (f′ steigt
dort monoton von −8 auf 0, x ≈ 1,26), die Wandfläche 58 m² in
e5-k1-s2-v2, die Winkelhalbierenden-Stellen in e4-k1-s10-v1/v2 und
n(c) in e1-k2-s1-v1. Alle 247 Lösungen stimmen mit der eigenen
Rechnung überein; jede pruef-Zahl passt nach Rundung zur Lösung.
Die 20 Ankreuzzeilen (alle Vorstufen, keine Zahloptionen) haben je
eine richtige Option, die loesung nennt sie wortgleich. Die 16
Fehler-finden-Zeilen enthalten einen echten Fehler aus „Typische
Fehler“, die Richtigrechnung stimmt. Grafiken (ksys) passen zu den
Werten (Berührpunkte, Achsenschnitte und Ableseziele im Bereich).
`werkzeuge/bank-pruef.py tangente-normale-schnittwinkel`: 0
Abweichungen, 4 Warnungen (e1 k1 s10: die Pooldublette
2024-bebb-lk-A1.5b / 2024MerhoehtAAnalysis21-b je 1×, laut stand.md
Entscheidung 5 gewollt). Befunde nur zu Eindeutigkeit und Merkmal,
keine Rechenfehler.

## Befunde

e2-k1-s3-v2: [E] Die Rodelbahn wird „für 0 ≤ x ≤ 15“ durch h
beschrieben, soll aber schon im Punkt (10 | h(10)) geradlinig
fortgesetzt werden – Definitionsbereich und Fortsetzung widersprechen
sich – Bereich auf „0 ≤ x ≤ 10“ setzen.

e4-k1-s3-v3: [M] Sprosse „Tangentengleichung und Schnittwinkel mit der
x-Achse nebeneinander“; die Zeile fragt nur den Schnittwinkel von
e^(2x) mit der Geraden y = 2, keine Tangentengleichung und nicht die
x-Achse (das Original 2023MgrundlegendBAnalysisWTR1-1c steht auch
nicht in der Belegklammer der Sprosse) – Tangentengleichung im
Schnittpunkt mitfragen oder die Zeile zu e4-k1-s2 umhängen.

e4-k1-s5-v3: [M] Sprosse und Merkmal verlangen „einzeichnen und
deuten“; die Zeile (form text, ohne Grafik) lässt nur α und β
berechnen und deuten – Abbildung mit Podest und Rampe geben und α, β
einzeichnen lassen (wie v1, v2).

e4-k1-s6-v3: [M] Merkmal „zwei Steigungen an derselben Stelle“,
Sprosse „Schnittwinkel zweier Graphen“; die Zeile fragt den Winkel
zweier Tangenten desselben Graphen an verschiedenen Stellen (2 und 16),
also ein anderes Merkmal – als Typ ohne Kette oder mit zweitem Graphen
an derselben Stelle neu fassen.

Sauber: 243 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k1-s3-v2 – Definitionsbereich 0 ≤ x ≤ 15 widerspricht
der Fortsetzung bei x = 10 (beide: Bereich auf 0 ≤ x ≤ 10).
e4-k1-s3-v3 – keine Tangentengleichung, Winkel gegen y = 2 statt gegen
die x-Achse, Merkmal verfehlt. e4-k1-s5-v3 – ohne Grafik und
Zeichenauftrag, obwohl die Sprosse „einzeichnen“ verlangt.

Nur Erstleser:
- e2-k2-s1-v3: Lösung nennt nur die Berührpunkte, gefragt sind die
  Tangenten – bestätigt, nachgerechnet: y = 6x − 4 in (2 | 8) und
  y = −2x − 4 in (−2 | 0); von mir übersehen (loesung unvollständig).
- e2-k1-s4-v3 und e2-k2-s1-v1: Glasbereich reicht über die Hochpunkte
  (±√6 bzw. ±2√2) hinaus, das Profil fällt wieder auf 0 – bestätigt
  als Sachplausibilität (f(√12) = 0 bzw. f(4) = 0); die Rechnung und
  die Ergebnisse bleiben richtig, die Kürzung des Bereichs ändert sie
  nicht.
- Rundungsangabe fehlt (rund 55 Zeilen, vor allem e3-k1-s4/s5 und die
  Winkelzeilen in e4) – teilweise bestätigt: formal richtig, die
  Stellenzahl steht nur in der Lösung; das Ergebnis ist aber nicht
  mehrdeutig, und eine \anweisung je Einheit beim Zusammenbau genügt.
  Ich zähle es nicht als Befund je Zeile.
- e1-k1-s10-v5/v6: merkmal nennt Punktprobe, die Zeilen geben nur die
  Stelle – teilweise bestätigt: die Zeilen folgen treu dem Original
  2019-C-1f (dort ebenfalls nur „berührt an der Stelle x = −1“, keine
  Punktprobe); der Widerspruch liegt im merkmal- bzw. Katalogtext
  („nach Punktprobe und Anstieg“), nicht in der Aufgabe – merkmal
  anpassen.
- e5-k1-s8-v5/v6: merkmal „Parameter statt Zahlen“ passt nicht zur
  fhr-Zielmarke; v6 ohne Skizze – für v6 bestätigt (Original
  2024-C-1g verlangt „Skizze von t und des Dreiecks“, v6 hat weder
  Grafik noch Zeichenauftrag; M); für v5 nur merkmal-Wortlaut.
- e5-k1-s6-v2: Lösung setzt ohne Begründung nur −1 an – nicht als
  Fehler bestätigt: die Lösung ist richtig und +1 ist wegen
  f′(u) < 0 ausgeschlossen; eine Ergänzung „±1, wegen f′ < 0 nur −1“
  verbessert die Lösungsschrift, ist aber kein Befund.
- e2-k2-s1-v1, e4-k1-s9-v3: ohne Rechner/CAS kaum lösbar, Hilfsmittel
  nicht genannt – bestätigt als Hinweis: e4-k1-s9-v3 ist nur
  numerisch lösbar (Lösung sagt „mit dem Rechner“, die Aufgabe nicht),
  e2-k2-s1-v1 ist ohne den Hinweis auf die doppelte Lösung u = −1 eine
  Gleichung 4. Grades; die Einheit ist Sek II mit Rechner, daher kein
  Rechenbefund, sondern Hilfsmittelangabe ergänzen.
- e4-k1-s0-v2 und e4-k1-s0-v4: „Was ist gegeben?“, obwohl der Winkel
  gesucht ist – bestätigt: der Katalog (Voraussetzung/Erkennungsschritt,
  Mappe Z. 56) ordnet „Winkel gegeben oder gesucht“ dem Winkel-Weg zu,
  damit sind „ein Punkt“ und „ein Winkel“ beide vertretbar; ich hatte
  die Frage wörtlich gelesen und nur „ein Punkt“ gelten lassen – A.

Nur Zweitleser:
- e4-k1-s6-v3: Winkel zweier Tangenten desselben Graphen an
  verschiedenen Stellen statt Schnittwinkel zweier Graphen an derselben
  Stelle – Merkmal verfehlt (das Original 2017-be-gk-B1.1e steht nicht
  in der Belegklammer der Sprosse); der Erstleser hat die Zeile nur aus
  dem Rundungsbefund herausgenommen.

Widersprüche: keine in der Sache. Der Erstleser zählt 185 saubere
Zeilen, ich 243 – der Unterschied kommt fast ganz aus dem
Rundungsbefund, den ich nicht je Zeile zähle; nach Abgleich kämen bei
mir e2-k2-s1-v3 (R), e2-k1-s4-v3 und e2-k2-s1-v1 (E), e5-k1-s8-v6 (M)
und e4-k1-s0-v2/v4 (A) hinzu.
