# Duplikate und Zahlenkollisionen der Bank

Gebaut mit werkzeuge/duplikate.py; nicht von Hand ändern, nach jedem Bank-Auftrag neu bauen.
Quelle: bank/*/*.jsonl, 72 Einträge, 16119 Zeilen. Stand der Bank: fc42b51 2026-10-02 (letzter Commit auf bank/).
Verglichen wird aufgabe samt grafik nach Normierung (LaTeX-Abstände und $ weg, {,} → Komma, Tausender zusammen, Dezimalpunkt → Komma, Endnullen weg, Leerzeichen neben Zeichen gestrichen); „bis auf Zahlen“ ersetzt jede Zahl durch #. Reichweite: über Einträge / im Eintrag (über Sprossen) / in der Sprosse (Varianten).

## Zahl je Befundart

| Befundart | Gruppen | Zeilen |
|---|--:|--:|
| A wortgleich, über Einträge | 30 | 64 |
| A wortgleich, im Eintrag | 0 | 0 |
| A wortgleich, in der Sprosse | 0 | 0 |
| B bis auf Zahlen gleich, über Einträge | 110 | 534 |
| B bis auf Zahlen gleich, im Eintrag | 157 | 450 |
| B bis auf Zahlen gleich, in der Sprosse | 733 | 1995 |
| C gleiches Ergebnis und gleiche Kontextwörter (> 3 Zeilen) | 6 | 29 |
| D Personennamen (verschiedene) | 72 | 1176 |
| D Sachkontexte (Zeilen mit mindestens einem) | 18 | 4263 |
| E aufgabe kürzer als 20 Zeichen | – | 106 |
| E aufgabe länger als 600 Zeichen | – | 2 |

## A Wortgleich nach Normierung

- A-001 (über Einträge, 5 Zeilen): binomische-formeln-zone-f5-v1, flaechen-zone-f5-v2, kreis-zone-f4-v2, pyramide-kegel-kugel-zone-f4-v2, quadratische-funktionen-zone-f7-v1  
  `Berechne.\sqrt{64}`
- A-002 (über Einträge, 3 Zeilen): koerper-zone-f5-v2, kreis-zone-f4-v1, quadratische-gleichungen-zone-f1-v1  
  `Berechne.7^2`
- A-003 (über Einträge, 2 Zeilen): binomische-formeln-zone-f3-v1, lineare-gleichungen-zone-f3-v1  
  `Fasse zusammen:4x+3x`
- A-004 (über Einträge, 2 Zeilen): binomische-formeln-zone-f3-v2, terme-e1-k4-s6-v3  
  `Fasse zusammen:9x-x`
- A-005 (über Einträge, 2 Zeilen): binomische-formeln-zone-f5-v2, quadratische-funktionen-zone-f1-v2  
  `Berechne.9^2`
- A-006 (über Einträge, 2 Zeilen): bruchrechnung-zone-f3-v2, brueche-dezimalzahlen-zone-f4-v1  
  `Nenne alle Teiler von 10.`
- A-007 (über Einträge, 2 Zeilen): bruchrechnung-zone-f6-v2, prozentrechnung-zone-f2-v2  
  `Schreibe 0,9 als Bruch.`
- A-008 (über Einträge, 2 Zeilen): bruchrechnung-zone-f6-v3, potenzen-wurzeln-zone-f5-v2  
  `Schreibe\frac{3}{5}als Dezimalzahl.`
- A-009 (über Einträge, 2 Zeilen): brueche-dezimalzahlen-e4-k1-s3-v1, prozentrechnung-zone-f2-v4  
  `Schreibe\frac{7}{100}als Dezimalzahl.`
- A-010 (über Einträge, 2 Zeilen): brueche-dezimalzahlen-e4-k1-s5-v3, prozentrechnung-zone-f2-v3  
  `Schreibe\frac{3}{25}als Dezimalzahl.`
- A-011 (über Einträge, 2 Zeilen): einheiten-e1-k2-s8-v1, koerper-zone-f3-v3  
  `Rechne 2,35 m in cm um.`
- A-012 (über Einträge, 2 Zeilen): flaechen-zone-f1-v1, pythagoras-zone-f4-v1  
  `Rechne 3 m in cm um.`
- A-013 (über Einträge, 2 Zeilen): flaechen-zone-f3-v1, kreis-zone-f2-v1  
  `Berechne.0,5\cdot 8`
- A-014 (über Einträge, 2 Zeilen): flaechen-zone-f4-v1, koerper-zone-f4-v1  
  `Stelle die Formel P=q\cdot r nach r um.`
- A-015 (über Einträge, 2 Zeilen): flaechen-zone-f5-v4, quadratische-gleichungen-zone-f2-v2  
  `Berechne.\sqrt{100}`
- A-016 (über Einträge, 2 Zeilen): koerper-e2-k1-s3-v1, pyramide-kegel-kugel-zone-f8-v4  
  `Rechne 4500 cm³ in Liter um.`
- A-017 (über Einträge, 2 Zeilen): koerper-e2-k1-s3-v3, pyramide-kegel-kugel-zone-f8-v3  
  `Rechne 750 cm³ in Liter um.`
- A-018 (über Einträge, 2 Zeilen): koerper-e4-k2-s1-v2, pyramide-kegel-kugel-zone-f2-v3  
  `Ein Zylinder hat den Radius 2 cm und die Höhe 9 cm.Berechne sein Volumen.Runde auf eine Stelle nach dem Komma.`
- A-019 (über Einträge, 2 Zeilen): koerper-zone-f2-v5, pyramide-kegel-kugel-zone-f7-v6  
  `Ein Kreis hat den Durchmesser 14 cm.Berechne seinen Flächeninhalt.Runde auf eine Stelle nach dem Komma.`
- A-020 (über Einträge, 2 Zeilen): koerper-zone-f5-v4, quadratische-funktionen-zone-f1-v6  
  `Berechne.2\cdot 5^2`
- A-021 (über Einträge, 2 Zeilen): potenz-exponentialfunktionen-e5-k1-s0-v1, potenzen-wurzeln-e1-k1-s0-v1  
  `Kreuze an,ob(-5)^4 positiv oder negativ ist.\\kreuz{positiv}\\kreuz{negativ}`
- A-022 (über Einträge, 2 Zeilen): potenz-exponentialfunktionen-e5-k1-s1-v2, potenzen-wurzeln-e1-k3-s5-v1  
  `Berechne(-4)^3.`
- A-023 (über Einträge, 2 Zeilen): potenz-exponentialfunktionen-zone-f10-v3, quadratische-funktionen-e1-k1-s1-v1  
  `Fülle die Wertetabelle zu f(x)=x^2 aus.\wertetabelle{x}{f(x)}{-2-1,1,2}`
- A-024 (über Einträge, 2 Zeilen): potenzen-wurzeln-e3-k2-s12-v1, reelle-zahlen-e3-k1-s7-v1  
  `Berechne\sqrt[3]{64}.`
- A-025 (über Einträge, 2 Zeilen): potenzen-wurzeln-zone-f4-v2, wahrscheinlichkeit-zone-f5-v1  
  `Berechne\frac{1}{2}\cdot\frac{1}{3}.`
- A-026 (über Einträge, 2 Zeilen): pyramide-kegel-kugel-zone-f3-v1, trigonometrie-zone-f6-v1  
  `Ein rechtwinkliges Dreieck hat die Katheten 3 cm und 4 cm.Wie lang ist die Hypotenuse?`
- A-027 (über Einträge, 2 Zeilen): quadratische-funktionen-zone-f4-v3, quadratische-gleichungen-zone-f7-v3  
  `Multipliziere aus.(x-6)^2`
- A-028 (über Einträge, 2 Zeilen): quadratische-funktionen-zone-f7-v4, quadratische-gleichungen-zone-f2-v4  
  `Berechne.\sqrt{-16}`
- A-029 (über Einträge, 2 Zeilen): quadratische-funktionen-zone-f8-v2, quadratische-gleichungen-e1-k2-s1-v3  
  `Löse die Gleichung x^2=100.Gib die Lösungsmenge an.`
- A-030 (über Einträge, 2 Zeilen): trigonometrie-zone-f8-v1, winkel-dreiecke-zone-f3-v1  
  `Rechne 3 km in Meter um.`

## B Bis auf Zahlen gleich, über Einträge hinweg

- B-001 (8 Zeilen): koerper-e4-k2-s1-v1, koerper-e4-k2-s1-v2, koerper-e4-k2-s1-v3, koerper-e4-k2-s1-v4, koerper-e4-k2-s1-v5, koerper-e4-k2-s3-v1, koerper-e4-k2-s3-v3, pyramide-kegel-kugel-zone-f2-v3  
  `Ein Zylinder hat den Radius # cm und die Höhe # cm.Berechne sein Volumen.Runde auf eine Stelle nach dem Komma.`
- B-002 (2 Zeilen): lineare-funktionen-zone-f1-v2, quadratische-funktionen-zone-f2-v2  
  `Trage den Punkt B(#|#)in das Koordinatensystem ein.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\end{ksys}`
- B-003 (2 Zeilen): extremalprobleme-zone-f1-v3, koerper-zone-f2-v3  
  `Ein Trapez hat die parallelen Seiten # cm und # cm und die Höhe # cm.Berechne seinen Flächeninhalt.`
- B-004 (3 Zeilen): pyramide-kegel-kugel-zone-f3-v1, trigonometrie-zone-f6-v1, trigonometrie-zone-f6-v2  
  `Ein rechtwinkliges Dreieck hat die Katheten # cm und # cm.Wie lang ist die Hypotenuse?`
- B-005 (3 Zeilen): pyramide-kegel-kugel-zone-f3-v2, pyramide-kegel-kugel-zone-f3-v3, trigonometrie-zone-f6-v3  
  `Ein rechtwinkliges Dreieck hat die Katheten # m und # m.Wie lang ist die Hypotenuse?`
- B-006 (2 Zeilen): koerper-zone-f2-v4, pyramide-kegel-kugel-zone-f1-v4  
  `Ein Dreieck hat die Grundseite # cm und die Höhe # cm.Berechne seinen Flächeninhalt.`
- B-007 (2 Zeilen): daten-zone-f1-v1, prozentrechnung-e2-k3-s2-v1  
  `# von # Kindern haben ein Haustier.Wie viel Prozent der Kinder haben ein Haustier?`
- B-008 (5 Zeilen): strahlensaetze-zone-f9-v1, strahlensaetze-zone-f9-v2, strahlensaetze-zone-f9-v3, trigonometrie-zone-f7-v1, trigonometrie-zone-f7-v4  
  `Ein Dreieck hat die Winkel #^\circ und #^\circ.Wie groß ist der dritte Winkel?`
- B-009 (4 Zeilen): potenzen-wurzeln-e3-k2-s2-v1, potenzen-wurzeln-e3-k2-s2-v2, potenzen-wurzeln-e3-k2-s2-v3, reelle-zahlen-zone-f4-v1  
  `Berechne\sqrt{#}mit dem Taschenrechner.Runde auf zwei Stellen nach dem Komma.`
- B-010 (3 Zeilen): koerper-e3-k1-s1-v1, koerper-e3-k1-s1-v2, pyramide-kegel-kugel-zone-f2-v1  
  `Ein Prisma hat die Grundfläche # cm² und die Höhe # cm.Berechne sein Volumen.`
- B-011 (6 Zeilen): potenz-exponentialfunktionen-e5-k1-s0-v1, potenz-exponentialfunktionen-e5-k1-s0-v3, potenz-exponentialfunktionen-e5-k2-s0-v1, potenzen-wurzeln-e1-k1-s0-v1, potenzen-wurzeln-e1-k1-s0-v2, potenzen-wurzeln-e1-k1-s0-v4  
  `Kreuze an,ob(-#)^# positiv oder negativ ist.\\kreuz{positiv}\\kreuz{negativ}`
- B-012 (3 Zeilen): potenz-exponentialfunktionen-e5-k1-s0-v2, potenz-exponentialfunktionen-e5-k2-s0-v2, potenzen-wurzeln-e1-k1-s0-v3  
  `Kreuze an,ob-#^# positiv oder negativ ist.\\kreuz{positiv}\\kreuz{negativ}`
- B-013 (4 Zeilen): rationale-zahlen-basis-k3-v4, rationale-zahlen-basis-k3-v9, brueche-dezimalzahlen-e3-k1-s7-v1, brueche-dezimalzahlen-e3-k1-s7-v2  
  `Gib eine Zahl an,die zwischen\frac{#}{#}und\frac{#}{#}liegt.(P# # OS)`
- B-014 (4 Zeilen): potenz-exponentialfunktionen-e5-k1-s2-v1, potenz-exponentialfunktionen-zone-f10-v3, quadratische-funktionen-e1-k1-s1-v1, quadratische-funktionen-e1-k1-s1-v3  
  `Fülle die Wertetabelle zu f(x)=x^# aus.\wertetabelle{x}{f(x)}{-#-#,#}`
- B-015 (2 Zeilen): potenz-exponentialfunktionen-zone-f5-v4, prozentrechnung-e2-k3-s8-v3  
  `Von # Losen sind # Gewinne.Wie viel Prozent der Lose gewinnen?`
- B-016 (4 Zeilen): prozentrechnung-e4-k2-s3-v2, prozentrechnung-e4-k2-s5-v3, zinsrechnung-zone-f3-v1, zinsrechnung-zone-f3-v3  
  `#\%eines Betrags sind #€.Wie viel Euro ist der ganze Betrag?`
- B-017 (2 Zeilen): symmetrie-abbildungen-zone-f6-v1, trigonometrische-funktionen-zone-f5-v4  
  `Miss den Winkel\alpha im Bild.‖Grafik:\winkel{#}{\alpha}`
- B-018 (3 Zeilen): kreis-zone-f4-v3, quadratische-funktionen-zone-f7-v3, quadratische-gleichungen-zone-f2-v3  
  `Berechne\sqrt{#}.Runde auf zwei Stellen nach dem Komma.`
- B-019 (10 Zeilen): quadratische-funktionen-zone-f8-v6, quadratische-gleichungen-e3-k3-s1-v1, quadratische-gleichungen-e3-k3-s1-v2, quadratische-gleichungen-e3-k3-s1-v3, quadratische-gleichungen-e3-k3-s1-v4, quadratische-gleichungen-e3-k3-s1-v5, quadratische-gleichungen-e3-k3-s6-v2, quadratische-gleichungen-e3-k3-s6-v3, quadratische-gleichungen-e3-k3-s7-v1, quadratische-gleichungen-e3-k3-s7-v3  
  `Löse die Gleichung x^#+#x+#=#.Gib die Lösungsmenge an.`
- B-020 (6 Zeilen): quadratische-funktionen-zone-f8-v5, quadratische-gleichungen-e3-k3-s2-v3, quadratische-gleichungen-e3-k3-s5-v1, quadratische-gleichungen-e3-k3-s5-v3, quadratische-gleichungen-e3-k3-s6-v1, quadratische-gleichungen-e3-k3-s7-v2  
  `Löse die Gleichung x^#-#x+#=#.Gib die Lösungsmenge an.`
- B-021 (3 Zeilen): quadratische-funktionen-zone-f8-v3, quadratische-gleichungen-e3-k3-s2-v2, quadratische-gleichungen-e3-k3-s5-v2  
  `Löse die Gleichung x^#+#x-#=#.Gib die Lösungsmenge an.`
- B-022 (2 Zeilen): daten-zone-f8-v5, pythagoras-zone-f2-v3  
  `Berechne\sqrt{#}.Runde auf eine Stelle nach dem Komma.`
- B-023 (2 Zeilen): abstaende-zone-f1-v1, punkte-und-strecken-im-koordinatensystem-zone-f3-v1  
  `A(#|#|#),B(#|#|#):\overrightarrow{AB}und seine Länge?`
- B-024 (2 Zeilen): abstaende-zone-f1-v7, punkte-und-strecken-im-koordinatensystem-zone-f3-v2  
  `C(#|#|#),D(#|#|#):\overrightarrow{CD}und seine Länge?`
- B-025 (11 Zeilen): bedingte-wahrscheinlichkeit-und-bayes-zone-f4-v1, brueche-dezimalzahlen-e3-k1-s1-v1, brueche-dezimalzahlen-e3-k1-s1-v2, brueche-dezimalzahlen-e3-k1-s1-v3, brueche-dezimalzahlen-e3-k1-s1-v4, brueche-dezimalzahlen-e3-k1-s1-v5, brueche-dezimalzahlen-e3-k1-s2-v1, brueche-dezimalzahlen-e3-k1-s2-v2, brueche-dezimalzahlen-e3-k1-s2-v3, brueche-dezimalzahlen-e3-k1-s4-v1, brueche-dezimalzahlen-e3-k1-s4-v2  
  `Welcher Bruch ist größer:\frac{#}{#}oder\frac{#}{#}?`
- B-026 (6 Zeilen): quadratische-funktionen-zone-f8-v4, quadratische-gleichungen-e1-k2-s9-v1, quadratische-gleichungen-e1-k2-s9-v2, quadratische-gleichungen-e1-k2-s9-v3, quadratische-gleichungen-e1-k2-s10-v2, quadratische-gleichungen-e1-k2-s10-v3  
  `Löse die Gleichung(x+#)^#=#.Gib die Lösungsmenge an.`
- B-027 (7 Zeilen): quadratische-funktionen-zone-f8-v1, quadratische-funktionen-zone-f8-v2, quadratische-gleichungen-e1-k2-s1-v1, quadratische-gleichungen-e1-k2-s1-v2, quadratische-gleichungen-e1-k2-s1-v3, quadratische-gleichungen-e1-k2-s1-v4, quadratische-gleichungen-e1-k2-s1-v5  
  `Löse die Gleichung x^#=#.Gib die Lösungsmenge an.`
- B-028 (2 Zeilen): binomische-formeln-zone-f2-v1, rationale-zahlen-zone-f5-v4  
  `Setze x=# in den Term #x+# ein.Berechne den Wert.`
- B-029 (2 Zeilen): ebenen-zone-f4-v2, flaecheninhalt-und-volumen-im-raum-zone-f4-v3  
  `Stehen(#|-#|#)und(#|#|#)senkrecht aufeinander?`
- B-030 (2 Zeilen): strahlensaetze-zone-f4-v1, zuordnungen-e2-k4-s1-v4  
  `# Brötchen kosten #€.Was kosten # Brötchen?`
- B-031 (7 Zeilen): kombinatorik-zone-f2-v3, potenzen-wurzeln-e2-k1-s7-v1, potenzen-wurzeln-e2-k1-s7-v2, potenzen-wurzeln-e2-k1-s7-v3, potenzen-wurzeln-e2-k1-s11-v1, potenzen-wurzeln-e2-k1-s11-v2, potenzen-wurzeln-e2-k1-s11-v3  
  `Schreibe # in Zehnerpotenzschreibweise.`
- B-032 (6 Zeilen): potenzen-wurzeln-zone-f9-v1, potenzen-wurzeln-zone-f9-v5, prozentrechnung-zone-f5-v1, prozentrechnung-zone-f5-v2, prozentrechnung-zone-f5-v4, prozentrechnung-zone-f5-v5  
  `Runde # auf eine Stelle nach dem Komma.`
- B-033 (2 Zeilen): bruchrechnung-zone-f4-v2, einheiten-zone-f2-v3  
  `Schreibe # Hundertstel als Dezimalzahl.`
- B-034 (3 Zeilen): daten-zone-f1-v2, prozentrechnung-e1-k1-s4-v1, prozentrechnung-e1-k1-s4-v3  
  `Schreibe die Dezimalzahl # in Prozent.`
- B-035 (5 Zeilen): bruchrechnung-zone-f2-v4, bruchrechnung-zone-f2-v6, brueche-dezimalzahlen-e2-k1-s4-v1, brueche-dezimalzahlen-e2-k1-s4-v2, brueche-dezimalzahlen-e2-k1-s4-v3  
  `Schreibe\frac{#}{#}mit dem Nenner #.`
- B-036 (4 Zeilen): potenz-exponentialfunktionen-zone-f8-v1, potenz-exponentialfunktionen-zone-f8-v2, potenzen-wurzeln-e1-k3-s4-v1, potenzen-wurzeln-e1-k3-s4-v2  
  `Berechne #^# mit dem Taschenrechner.`
- B-037 (3 Zeilen): potenzen-wurzeln-zone-f4-v2, potenzen-wurzeln-zone-f4-v5, wahrscheinlichkeit-zone-f5-v1  
  `Berechne\frac{#}{#}\cdot\frac{#}{#}.`
- B-038 (2 Zeilen): linearkombination-und-lineare-abhaengigkeit-zone-f4-v4, punkte-und-strecken-im-koordinatensystem-zone-f8-v4  
  `Ist(#|#|#)ein Vielfaches von(#|#|#)?`
- B-039 (20 Zeilen): bruchrechnung-zone-f6-v1, bruchrechnung-zone-f6-v3, bruchrechnung-zone-f6-v4, brueche-dezimalzahlen-e4-k1-s1-v1, brueche-dezimalzahlen-e4-k1-s1-v2, brueche-dezimalzahlen-e4-k1-s1-v3, brueche-dezimalzahlen-e4-k1-s1-v4, brueche-dezimalzahlen-e4-k1-s1-v5, brueche-dezimalzahlen-e4-k1-s3-v1, brueche-dezimalzahlen-e4-k1-s3-v2, brueche-dezimalzahlen-e4-k1-s5-v1, brueche-dezimalzahlen-e4-k1-s5-v2, brueche-dezimalzahlen-e4-k1-s5-v3, potenzen-wurzeln-zone-f5-v2, prozentrechnung-zone-f2-v1, prozentrechnung-zone-f2-v3, prozentrechnung-zone-f2-v4, trigonometrie-zone-f5-v1, trigonometrie-zone-f5-v2, trigonometrie-zone-f5-v3  
  `Schreibe\frac{#}{#}als Dezimalzahl.`
- B-040 (3 Zeilen): bedingte-wahrscheinlichkeit-und-bayes-zone-f3-v3, strahlensaetze-zone-f1-v2, strahlensaetze-zone-f1-v4  
  `Berechne\frac{#}{#}als Dezimalzahl.`
- B-041 (4 Zeilen): brueche-dezimalzahlen-e5-k2-s4-v1, brueche-dezimalzahlen-e5-k2-s4-v2, daten-zone-f2-v1, daten-zone-f2-v3  
  `Ordne von klein nach groß:#;#;#;#.`
- B-042 (3 Zeilen): potenzen-wurzeln-zone-f5-v4, rationale-zahlen-e1-k1-s3-v1, rationale-zahlen-e1-k1-s3-v2  
  `Welche Zahl ist kleiner,-# oder-#?`
- B-043 (3 Zeilen): punkte-und-strecken-im-koordinatensystem-zone-f4-v1, vektoren-und-rechenoperationen-zone-f2-v1, vektoren-und-rechenoperationen-zone-f2-v2  
  `Katheten # cm und # cm:Hypotenuse?`
- B-044 (2 Zeilen): abstaende-zone-f6-v1, tangente-normale-schnittwinkel-zone-f6-v1  
  `Katheten # cm und # cm–Hypotenuse?`
- B-045 (10 Zeilen): bruchrechnung-e1-k3-s1-v1, bruchrechnung-e1-k3-s1-v2, bruchrechnung-e1-k3-s1-v3, bruchrechnung-e1-k3-s1-v4, bruchrechnung-e1-k3-s1-v5, reelle-zahlen-zone-f7-v1, reelle-zahlen-zone-f7-v3, reelle-zahlen-zone-f7-v4, wahrscheinlichkeit-zone-f5-v2, wahrscheinlichkeit-zone-f5-v4  
  `Berechne\frac{#}{#}+\frac{#}{#}.`
- B-046 (8 Zeilen): brueche-dezimalzahlen-e5-k2-s1-v1, brueche-dezimalzahlen-e5-k2-s1-v2, brueche-dezimalzahlen-e5-k2-s1-v3, brueche-dezimalzahlen-e5-k2-s1-v4, brueche-dezimalzahlen-e5-k2-s1-v5, brueche-dezimalzahlen-e5-k2-s3-v1, brueche-dezimalzahlen-e5-k2-s3-v2, daten-zone-f2-v2  
  `Welche Zahl ist größer:# oder #?`
- B-047 (8 Zeilen): einheiten-zone-f10-v2, lineare-gleichungen-e2-k3-s2-v2, lineare-gleichungen-e2-k3-s7-v1, lineare-gleichungen-e2-k3-s7-v2, strahlensaetze-zone-f8-v1, trigonometrie-zone-f4-v1, trigonometrie-zone-f4-v2, trigonometrie-zone-f4-v3  
  `Löse die Gleichung.\frac{x}{#}=#`
- B-048 (6 Zeilen): einheiten-zone-f4-v1, einheiten-zone-f4-v2, einheiten-zone-f4-v4, potenzen-wurzeln-zone-f5-v1, potenzen-wurzeln-zone-f5-v5, reelle-zahlen-zone-f2-v2  
  `Welche Zahl ist größer,# oder #?`
- B-049 (3 Zeilen): einheiten-zone-f10-v4, trigonometrie-zone-f4-v4, trigonometrie-zone-f4-v6  
  `Löse die Gleichung.\frac{#}{x}=#`
- B-050 (2 Zeilen): punkte-und-strecken-im-koordinatensystem-zone-f4-v2, vektoren-und-rechenoperationen-zone-f2-v3  
  `Katheten # m und # m:Hypotenuse?`
- B-051 (2 Zeilen): abstaende-zone-f3-v1, lagebeziehungen-zone-f1-v1  
  `E:#x+#y-z=#–ein Normalenvektor?`
- B-052 (3 Zeilen): kenngroessen-von-verteilungen-zone-f4-v2, kombinatorik-zone-f3-v2, kreis-zone-f6-v2  
  `Wie viel Prozent sind # von #?`
- B-053 (2 Zeilen): einheiten-zone-f10-v3, strahlensaetze-zone-f8-v2  
  `Löse die Gleichung.#\cdot x=#`
- B-054 (5 Zeilen): bedingte-wahrscheinlichkeit-und-bayes-zone-f3-v2, brueche-dezimalzahlen-e2-k1-s3-v1, brueche-dezimalzahlen-e2-k1-s3-v2, brueche-dezimalzahlen-e2-k1-s3-v3, kombinatorik-zone-f3-v1  
  `Kürze\frac{#}{#}vollständig.`
- B-055 (5 Zeilen): lineare-gleichungen-e3-k2-s2-v2, lineare-gleichungen-e3-k2-s2-v3, lineare-gleichungen-e3-k3-s1-v2, quadratische-funktionen-zone-f5-v4, quadratische-gleichungen-zone-f3-v4  
  `Löse die Gleichung.#x-#=#x+#`
- B-056 (3 Zeilen): daten-zone-f1-v5, potenzen-wurzeln-zone-f5-v3, prozentrechnung-e1-k1-s4-v2  
  `Schreibe #\%als Dezimalzahl.`
- B-057 (6 Zeilen): bruchrechnung-zone-f2-v1, brueche-dezimalzahlen-e2-k1-s1-v1, brueche-dezimalzahlen-e2-k1-s1-v2, brueche-dezimalzahlen-e2-k1-s1-v3, brueche-dezimalzahlen-e2-k1-s1-v4, brueche-dezimalzahlen-e2-k1-s1-v5  
  `Erweitere\frac{#}{#}mit #.`
- B-058 (3 Zeilen): brueche-dezimalzahlen-e1-k2-s3-v1, prozentrechnung-zone-f6-v1, prozentrechnung-zone-f6-v5  
  `Berechne\frac{#}{#}von #€.`
- B-059 (6 Zeilen): koerper-e2-k1-s3-v1, koerper-e2-k1-s3-v3, koerper-zone-f3-v4, pyramide-kegel-kugel-zone-f8-v1, pyramide-kegel-kugel-zone-f8-v3, pyramide-kegel-kugel-zone-f8-v4  
  `Rechne # cm³ in Liter um.`
- B-060 (4 Zeilen): quadratische-funktionen-zone-f4-v1, quadratische-funktionen-zone-f4-v2, quadratische-funktionen-zone-f4-v6, quadratische-gleichungen-zone-f7-v4  
  `Multipliziere aus.(x+#)^#`
- B-061 (3 Zeilen): daten-zone-f9-v1, lineare-gleichungen-e3-k3-s1-v1, quadratische-funktionen-zone-f5-v1  
  `Löse die Gleichung.#x+#=#`
- B-062 (3 Zeilen): quadratische-gleichungen-e1-k2-s16-v1, reelle-zahlen-e3-k1-s13-v1, reelle-zahlen-e3-k1-s13-v3  
  `Löse die Gleichung x^#=#.`
- B-063 (8 Zeilen): lineare-gleichungen-e2-k3-s1-v1, lineare-gleichungen-e2-k3-s1-v2, lineare-gleichungen-e2-k3-s1-v3, lineare-gleichungen-e2-k3-s1-v4, lineare-gleichungen-e2-k3-s1-v5, lineare-gleichungen-e2-k3-s3-v1, lineare-gleichungen-e2-k3-s3-v3, quadratische-gleichungen-zone-f3-v1  
  `Löse die Gleichung.x+#=#`
- B-064 (3 Zeilen): bruchrechnung-zone-f3-v2, brueche-dezimalzahlen-zone-f4-v1, brueche-dezimalzahlen-zone-f4-v3  
  `Nenne alle Teiler von #.`
- B-065 (3 Zeilen): trigonometrie-zone-f8-v1, winkel-dreiecke-zone-f3-v1, winkel-dreiecke-zone-f3-v3  
  `Rechne # km in Meter um.`
- B-066 (2 Zeilen): lineare-gleichungen-e2-k3-s6-v1, quadratische-gleichungen-zone-f3-v3  
  `Löse die Gleichung.-#x=#`
- B-067 (3 Zeilen): lineare-gleichungen-e2-k3-s2-v1, lineare-gleichungen-e2-k3-s2-v3, quadratische-gleichungen-zone-f3-v2  
  `Löse die Gleichung.#x=#`
- B-068 (2 Zeilen): einheiten-e3-k1-s1-v2, flaechen-zone-f2-v1  
  `Rechne # cm² in mm² um.`
- B-069 (2 Zeilen): einheiten-e3-k1-s1-v4, flaechen-zone-f2-v6  
  `Rechne # dm² in cm² um.`
- B-070 (2 Zeilen): potenzen-wurzeln-e3-k2-s11-v1, reelle-zahlen-e3-k1-s5-v2  
  `Berechne\sqrt{#^#+#^#}.`
- B-071 (3 Zeilen): brueche-dezimalzahlen-zone-f7-v2, brueche-dezimalzahlen-zone-f7-v3, potenz-exponentialfunktionen-zone-f5-v3  
  `Schreibe # in Prozent.`
- B-072 (3 Zeilen): einheiten-e3-k1-s2-v1, einheiten-e3-k1-s2-v3, flaechen-zone-f2-v4  
  `Rechne # m² in cm² um.`
- B-073 (3 Zeilen): lineare-gleichungen-zone-f3-v4, lineare-gleichungen-zone-f3-v8, terme-e1-k4-s4-v1  
  `Fasse zusammen:#x+#+#x`
- B-074 (2 Zeilen): einheiten-e3-k1-s1-v1, flaechen-zone-f2-v2  
  `Rechne # m² in dm² um.`
- B-075 (2 Zeilen): einheiten-e3-k1-s5-v3, pyramide-kegel-kugel-zone-f8-v2  
  `Rechne # m³ in dm³ um.`
- B-076 (5 Zeilen): einheiten-zone-f9-v1, prozentrechnung-e3-k1-s2-v3, prozentrechnung-e3-k1-s4-v1, prozentrechnung-e3-k1-s8-v1, zinsrechnung-zone-f1-v2  
  `Berechne #\%von # kg.`
- B-077 (2 Zeilen): einheiten-e1-k2-s2-v1, flaechen-zone-f1-v2  
  `Rechne # mm in cm um.`
- B-078 (2 Zeilen): einheiten-zone-f9-v3, koerper-zone-f6-v2  
  `Berechne #\%von # m³.`
- B-079 (9 Zeilen): binomische-formeln-zone-f3-v1, lineare-funktionen-zone-f6-v1, lineare-gleichungen-zone-f3-v1, terme-e1-k4-s1-v1, terme-e1-k4-s1-v2, terme-e1-k4-s1-v3, terme-e1-k4-s1-v4, terme-e1-k4-s1-v5, terme-e1-k4-s11-v1  
  `Fasse zusammen:#x+#x`
- B-080 (7 Zeilen): einheiten-e1-k2-s3-v3, einheiten-e1-k2-s8-v1, einheiten-e1-k2-s8-v2, flaechen-zone-f1-v1, flaechen-zone-f1-v3, koerper-zone-f3-v3, pythagoras-zone-f4-v1  
  `Rechne # m in cm um.`
- B-081 (6 Zeilen): potenz-exponentialfunktionen-zone-f14-v2, potenzen-wurzeln-e3-k2-s12-v1, potenzen-wurzeln-e3-k2-s12-v2, potenzen-wurzeln-e3-k2-s12-v3, reelle-zahlen-e3-k1-s7-v1, reelle-zahlen-e3-k1-s7-v3  
  `Berechne\sqrt[#]{#}.`
- B-082 (5 Zeilen): daten-zone-f5-v2, einheiten-zone-f3-v2, kreis-zone-f2-v2, prozentrechnung-zone-f3-v1, prozentrechnung-zone-f3-v4  
  `Berechne.\frac{#}{#}`
- B-083 (5 Zeilen): lineare-funktionen-zone-f6-v2, lineare-gleichungen-zone-f3-v2, lineare-gleichungen-zone-f3-v6, terme-e1-k4-s2-v1, terme-e1-k4-s7-v1  
  `Fasse zusammen:#x-#x`
- B-084 (4 Zeilen): einheiten-zone-f9-v2, prozentrechnung-e3-k1-s4-v3, prozentrechnung-e3-k1-s6-v3, prozentrechnung-e3-k1-s8-v3  
  `Berechne #\%von # m.`
- B-085 (3 Zeilen): abstaende-zone-f5-v1, punkte-und-strecken-im-koordinatensystem-zone-f6-v1, punkte-und-strecken-im-koordinatensystem-zone-f6-v2  
  `(#|#|#)\circ(#|#|#)?`
- B-086 (3 Zeilen): lineare-funktionen-zone-f3-v3, terme-zone-f2-v4, terme-zone-f2-v5  
  `Rechne:(-#)\cdot(-#)`
- B-087 (2 Zeilen): einheiten-e1-k2-s3-v2, pythagoras-zone-f4-v2  
  `Rechne # cm in m um.`
- B-088 (2 Zeilen): einheiten-e3-k1-s7-v1, koerper-zone-f3-v1  
  `Rechne # l in ml um.`
- B-089 (2 Zeilen): funktionsklassen-und-eigenschaften-zone-f4-v3, tangente-normale-schnittwinkel-zone-f4-v3  
  `x^#-#x-#=#–Lösungen?`
- B-090 (9 Zeilen): prozentrechnung-e3-k1-s2-v1, prozentrechnung-e3-k1-s2-v2, prozentrechnung-e3-k1-s4-v2, prozentrechnung-e3-k1-s6-v1, prozentrechnung-e3-k1-s6-v2, prozentrechnung-e3-k1-s8-v2, zinsrechnung-zone-f1-v1, zinsrechnung-zone-f1-v3, zinsrechnung-zone-f1-v6  
  `Berechne #\%von #€.`
- B-091 (3 Zeilen): binomische-formeln-zone-f1-v2, bruchrechnung-e5-k1-s2-v2, lineare-gleichungen-zone-f1-v4  
  `Berechne.#-#\cdot #`
- B-092 (3 Zeilen): pythagoras-zone-f2-v2, pythagoras-zone-f2-v6, reelle-zahlen-e3-k1-s5-v1  
  `Berechne\sqrt{#+#}.`
- B-093 (2 Zeilen): bruchrechnung-e5-k1-s2-v1, lineare-gleichungen-zone-f1-v1  
  `Berechne.#+#\cdot #`
- B-094 (27 Zeilen): bruchrechnung-e4-k2-s1-v1, bruchrechnung-e4-k2-s1-v2, bruchrechnung-e4-k2-s1-v3, bruchrechnung-e4-k2-s1-v4, bruchrechnung-e4-k2-s1-v5, potenz-exponentialfunktionen-zone-f4-v1, potenz-exponentialfunktionen-zone-f4-v2, potenz-exponentialfunktionen-zone-f4-v3, potenzen-wurzeln-e2-k1-s3-v1, potenzen-wurzeln-e2-k1-s3-v2, potenzen-wurzeln-e2-k1-s3-v3, potenzen-wurzeln-zone-f1-v1, potenzen-wurzeln-zone-f1-v2, potenzen-wurzeln-zone-f1-v3, potenzen-wurzeln-zone-f2-v1, potenzen-wurzeln-zone-f2-v2, potenzen-wurzeln-zone-f4-v1, potenzen-wurzeln-zone-f4-v3, potenzen-wurzeln-zone-f4-v4, potenzen-wurzeln-zone-f7-v1, potenzen-wurzeln-zone-f7-v2, potenzen-wurzeln-zone-f7-v4, potenzen-wurzeln-zone-f8-v1, potenzen-wurzeln-zone-f8-v3, potenzen-wurzeln-zone-f8-v4, strahlensaetze-zone-f1-v1, strahlensaetze-zone-f1-v3  
  `Berechne #\cdot #.`
- B-095 (3 Zeilen): lineare-funktionen-zone-f3-v1, terme-zone-f2-v1, terme-zone-f2-v3  
  `Rechne:(-#)\cdot #`
- B-096 (22 Zeilen): bruchrechnung-e4-k2-s3-v1, bruchrechnung-e4-k2-s3-v2, bruchrechnung-e4-k2-s3-v3, bruchrechnung-e4-k2-s4-v1, bruchrechnung-e4-k2-s4-v2, bruchrechnung-e4-k2-s4-v3, bruchrechnung-e4-k2-s5-v1, bruchrechnung-e4-k2-s5-v2, bruchrechnung-e4-k2-s5-v3, bruchrechnung-zone-f5-v1, brueche-dezimalzahlen-zone-f1-v2, einheiten-zone-f3-v1, einheiten-zone-f3-v3, einheiten-zone-f3-v4, flaechen-zone-f3-v1, flaechen-zone-f3-v3, flaechen-zone-f3-v4, koerper-zone-f5-v1, kreis-zone-f2-v1, prozentrechnung-zone-f3-v2, prozentrechnung-zone-f3-v3, prozentrechnung-zone-f3-v5  
  `Berechne.#\cdot #`
- B-097 (13 Zeilen): binomische-formeln-zone-f5-v1, daten-zone-f8-v2, flaechen-zone-f5-v1, flaechen-zone-f5-v2, flaechen-zone-f5-v3, flaechen-zone-f5-v4, kreis-zone-f4-v2, pyramide-kegel-kugel-zone-f4-v2, quadratische-funktionen-zone-f7-v1, quadratische-funktionen-zone-f7-v2, quadratische-funktionen-zone-f7-v5, quadratische-gleichungen-zone-f2-v1, quadratische-gleichungen-zone-f2-v2  
  `Berechne.\sqrt{#}`
- B-098 (6 Zeilen): kenngroessen-von-verteilungen-zone-f6-v2, potenz-exponentialfunktionen-zone-f14-v1, potenzen-wurzeln-e3-k2-s9-v1, potenzen-wurzeln-e3-k2-s9-v3, potenzen-wurzeln-e3-k2-s9-v4, pythagoras-zone-f2-v1  
  `Berechne\sqrt{#}.`
- B-099 (2 Zeilen): gleichungen-loesen-zone-f1-v1, grenzwerte-und-verhalten-im-unendlichen-zone-f5-v1  
  `Löse:(x-#)(x+#)=#`
- B-100 (2 Zeilen): funktionsklassen-und-eigenschaften-zone-f4-v4, tangente-normale-schnittwinkel-zone-f4-v1  
  `#x^#=#–Lösungen?`
- B-101 (14 Zeilen): potenz-exponentialfunktionen-e5-k1-s1-v1, potenz-exponentialfunktionen-e5-k1-s1-v2, potenz-exponentialfunktionen-e5-k1-s1-v3, potenz-exponentialfunktionen-e5-k1-s1-v4, potenz-exponentialfunktionen-e5-k1-s1-v5, potenz-exponentialfunktionen-zone-f9-v2, potenz-exponentialfunktionen-zone-f9-v3, potenzen-wurzeln-e1-k3-s5-v1, potenzen-wurzeln-e1-k3-s5-v2, potenzen-wurzeln-e1-k3-s5-v3, potenzen-wurzeln-e1-k6-s1-v2, potenzen-wurzeln-zone-f3-v4, potenzen-wurzeln-zone-f3-v7, reelle-zahlen-zone-f6-v3  
  `Berechne(-#)^#.`
- B-102 (5 Zeilen): binomische-formeln-zone-f5-v3, quadratische-funktionen-zone-f1-v4, quadratische-gleichungen-zone-f1-v2, quadratische-gleichungen-zone-f1-v3, quadratische-gleichungen-zone-f1-v6  
  `Berechne.(-#)^#`
- B-103 (15 Zeilen): kombinatorik-zone-f2-v1, kombinatorik-zone-f2-v2, kombinatorik-zone-f2-v4, matrizen-und-uebergangsprozesse-zone-f6-v1, potenzen-wurzeln-e1-k3-s3-v1, potenzen-wurzeln-e1-k3-s3-v2, potenzen-wurzeln-e1-k3-s3-v3, potenzen-wurzeln-e1-k3-s7-v1, potenzen-wurzeln-e1-k3-s7-v2, potenzen-wurzeln-e1-k3-s7-v3, potenzen-wurzeln-e1-k6-s1-v1, pythagoras-zone-f1-v1, pythagoras-zone-f1-v3, reelle-zahlen-zone-f6-v2, reelle-zahlen-zone-f6-v4  
  `Berechne #^#.`
- B-104 (2 Zeilen): lineare-gleichungen-zone-f2-v1, lineare-gleichungssysteme-zone-f6-v2  
  `Berechne.-#+#`
- B-105 (18 Zeilen): bruchrechnung-e4-k2-s2-v1, bruchrechnung-e4-k2-s2-v2, bruchrechnung-e4-k2-s2-v3, bruchrechnung-e4-k2-s6-v1, bruchrechnung-e4-k2-s6-v2, bruchrechnung-e4-k2-s6-v3, bruchrechnung-e4-k2-s7-v1, bruchrechnung-e4-k2-s7-v2, bruchrechnung-e4-k2-s7-v3, bruchrechnung-zone-f5-v2, brueche-dezimalzahlen-zone-f1-v1, brueche-dezimalzahlen-zone-f1-v3, brueche-dezimalzahlen-zone-f6-v1, brueche-dezimalzahlen-zone-f6-v2, brueche-dezimalzahlen-zone-f6-v3, brueche-dezimalzahlen-zone-f6-v4, flaechen-zone-f3-v2, flaechen-zone-f3-v5  
  `Berechne.#:#`
- B-106 (12 Zeilen): binomische-formeln-zone-f5-v2, koerper-zone-f5-v2, kreis-zone-f4-v1, kreis-zone-f4-v4, pyramide-kegel-kugel-zone-f4-v1, pyramide-kegel-kugel-zone-f4-v3, pyramide-kegel-kugel-zone-f4-v4, quadratische-funktionen-zone-f1-v1, quadratische-funktionen-zone-f1-v2, quadratische-funktionen-zone-f1-v3, quadratische-funktionen-zone-f1-v5, quadratische-gleichungen-zone-f1-v1  
  `Berechne.#^#`
- B-107 (7 Zeilen): bruchrechnung-e2-k1-s2-v1, bruchrechnung-e2-k1-s3-v1, bruchrechnung-e2-k1-s3-v3, bruchrechnung-e2-k2-s1-v1, bruchrechnung-e2-k2-s1-v2, bruchrechnung-e2-k2-s1-v3, daten-zone-f5-v5  
  `Berechne.#+#`
- B-108 (4 Zeilen): bruchrechnung-e2-k1-s2-v2, bruchrechnung-e2-k1-s2-v3, bruchrechnung-e2-k1-s3-v2, lineare-gleichungen-zone-f2-v2  
  `Berechne.#-#`
- B-109 (2 Zeilen): ableitung-und-aenderungsrate-zone-f5-v1, orthogonalitaet-zone-f3-v1  
  `Löse:#t-#=#`
- B-110 (2 Zeilen): ableitung-und-aenderungsrate-zone-f5-v2, gleichungen-loesen-zone-f2-v1  
  `Löse:#x+#=#`

## B Bis auf Zahlen gleich, im selben Eintrag, über Sprossen hinweg

- B-111 (7 Zeilen): lineare-funktionen-e1-k1-s1-v1, lineare-funktionen-e1-k1-s1-v3, lineare-funktionen-e1-k1-s1-v4, lineare-funktionen-e1-k1-s1-v5, lineare-funktionen-e1-k1-s3-v1, lineare-funktionen-e1-k1-s3-v2, lineare-funktionen-e1-k1-s3-v3  
  `Berechne die y-Werte zu y=#x für x=# # #.Zeichne dann die Gerade durch diese Punkte in das Koordinatensystem.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\end{ksys}`
- B-112 (2 Zeilen): lineare-funktionen-e4-k1-s1-v2, lineare-funktionen-e4-k4-s3-v1  
  `Das Koordinatensystem zeigt die Gerade g.Bestimme die Gleichung von g.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#ablesen]\gerade{-#}{#}{g}\end{ksys}`
- B-113 (2 Zeilen): pythagoras-e2-k3-s2-v2, pythagoras-e2-k3-s3-v3  
  `In einem rechtwinkligen Dreieck ist c=# m die Hypotenuse und b=# m eine Kathete.Berechne die Länge der Kathete a.Runde auf eine Stelle nach dem Komma.`
- B-114 (2 Zeilen): pythagoras-e1-k2-s3-v2, pythagoras-e1-k2-s4-v3  
  `In einem rechtwinkligen Dreieck sind a=# m und b=# m die Katheten.Berechne die Länge der Hypotenuse c.Runde auf eine Stelle nach dem Komma.`
- B-115 (3 Zeilen): brueche-dezimalzahlen-zone-f3-v1, brueche-dezimalzahlen-zone-f3-v2, brueche-dezimalzahlen-zone-f3-v3  
  `Ein Kreissektor(ein Kreisstück)hat einen Winkel von #^\circ.Der ganze Kreis hat #^\circ.Welcher Anteil des ganzen Kreises ist der Sektor?`
- B-116 (3 Zeilen): quadratische-funktionen-e4-k1-s4-v2, quadratische-funktionen-e4-k1-s5-v2, quadratische-funktionen-e4-k1-s5-v3  
  `Die Parabel f(x)=x^#+#x+# hat den Scheitel S(-#|#).Berechne ihre Nullstellen mit der p-q-Formel.Wie passt das Ergebnis zum Scheitel?`
- B-117 (2 Zeilen): quadratische-funktionen-e4-k1-s4-v1, quadratische-funktionen-e4-k1-s5-v1  
  `Die Parabel f(x)=x^#-#x+# hat den Scheitel S(#|#).Berechne ihre Nullstellen mit der p-q-Formel.Wie passt das Ergebnis zum Scheitel?`
- B-118 (4 Zeilen): brueche-dezimalzahlen-e4-k1-s9-v1, brueche-dezimalzahlen-e4-k1-s9-v2, brueche-dezimalzahlen-e5-k2-s10-v5, brueche-dezimalzahlen-e5-k2-s10-v6  
  `Kreuze die Aussage an,die wahr ist.(P# # OS)\\kreuz{#<\frac{#}{#}}\\kreuz{\frac{#}{#}>\frac{#}{#}}\\kreuz{\sqrt{#}>\frac{#}{#}}`
- B-119 (2 Zeilen): trigonometrische-funktionen-zone-f1-v1, trigonometrische-funktionen-zone-f1-v4  
  `In einem rechtwinkligen Dreieck ist die Gegenkathete von\alpha # cm lang.Die Hypotenuse ist # cm lang.Berechne sin\alpha.`
- B-120 (2 Zeilen): quadratische-funktionen-e2-k1-s4-v3, quadratische-funktionen-e2-k1-s14-v5  
  `Skizziere die Parabel zu f(x)=(x-#)^#-# im Koordinatensystem.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\end{ksys}`
- B-121 (2 Zeilen): potenz-exponentialfunktionen-e2-k2-s4-v3, potenz-exponentialfunktionen-e3-k2-s2-v2  
  `Ein Guthaben von #€wächst jedes Jahr um #\%.Berechne das Guthaben nach # Jahren mit einer Potenz.Runde auf Cent.`
- B-122 (2 Zeilen): flaechen-e4-k1-s1-v1, flaechen-e4-k1-s2-v1  
  `Ein Trapez hat die parallelen Seiten a=# cm und c=# cm.Die Höhe ist h=# cm.Berechne die Fläche des Trapezes.`
- B-123 (4 Zeilen): pyramide-kegel-kugel-e2-k2-s1-v1, pyramide-kegel-kugel-e2-k2-s1-v3, pyramide-kegel-kugel-e2-k2-s1-v5, pyramide-kegel-kugel-e2-k2-s3-v1  
  `Ein Kegel hat den Radius # cm und die Höhe # cm.Berechne sein Volumen.Runde auf eine Stelle nach dem Komma.`
- B-124 (2 Zeilen): flaechen-e1-k2-s1-v1, flaechen-e1-k2-s2-v1  
  `Ein Rechteck hat die Länge a=# cm und die Breite b=# cm.Berechne die Fläche und den Umfang des Rechtecks.`
- B-125 (2 Zeilen): flaechen-e2-k1-s1-v1, flaechen-e2-k1-s3-v1  
  `Ein Parallelogramm hat die Grundseite g=# cm und die Höhe h=# cm.Berechne die Fläche des Parallelogramms.`
- B-126 (2 Zeilen): flaechen-e2-k1-s1-v4, flaechen-e2-k1-s3-v3  
  `Ein Parallelogramm hat die Grundseite g=# dm und die Höhe h=# dm.Berechne die Fläche des Parallelogramms.`
- B-127 (2 Zeilen): flaechen-e4-k1-s1-v2, flaechen-e4-k1-s2-v2  
  `Ein Trapez hat die parallelen Seiten a=# m und c=# m.Die Höhe ist h=# m.Berechne die Fläche des Trapezes.`
- B-128 (2 Zeilen): flaechen-e2-k1-s1-v2, flaechen-e2-k1-s3-v2  
  `Ein Parallelogramm hat die Grundseite g=# m und die Höhe h=# m.Berechne die Fläche des Parallelogramms.`
- B-129 (2 Zeilen): potenz-exponentialfunktionen-e2-k2-s4-v1, potenz-exponentialfunktionen-e3-k2-s2-v1  
  `Ein Bestand von # wächst jedes Jahr mit dem Faktor #.Berechne den Wert nach # Jahren mit einer Potenz.`
- B-130 (2 Zeilen): flaechen-zone-f7-v1, flaechen-zone-f7-v3  
  `Ein Kreis hat den Radius r=# m.Berechne die Fläche des Kreises.Runde auf zwei Stellen nach dem Komma.`
- B-131 (2 Zeilen): brueche-dezimalzahlen-e1-k1-s2-v2, brueche-dezimalzahlen-e1-k4-s3-v3  
  `Der Kreis ist in gleich große Teile geteilt.Färbe\frac{#}{#}des Kreises.‖Grafik:\bruchkreis{#}{#}`
- B-132 (2 Zeilen): quadratische-funktionen-e2-k1-s6-v2, quadratische-funktionen-e2-k1-s14-v3  
  `Eine Normalparabel ist nach oben geöffnet.Ihr Scheitel ist S(-#|#).Stelle ihre Gleichung auf.`
- B-133 (3 Zeilen): flaechen-e3-k1-s1-v1, flaechen-e3-k1-s1-v4, flaechen-e3-k1-s4-v1  
  `Ein Dreieck hat die Grundseite g=# cm und die Höhe h=# cm.Berechne die Fläche des Dreiecks.`
- B-134 (2 Zeilen): trigonometrische-funktionen-zone-f1-v3, trigonometrische-funktionen-zone-f2-v2  
  `Berechne sin #°mit dem Taschenrechner im Grad-Modus.Runde auf zwei Stellen nach dem Komma.`
- B-135 (5 Zeilen): pyramide-kegel-kugel-e3-k1-s1-v1, pyramide-kegel-kugel-e3-k1-s1-v2, pyramide-kegel-kugel-e3-k1-s1-v4, pyramide-kegel-kugel-e3-k1-s3-v1, pyramide-kegel-kugel-e3-k1-s3-v3  
  `Eine Kugel hat den Radius # cm.Berechne ihr Volumen.Runde auf eine Stelle nach dem Komma.`
- B-136 (2 Zeilen): flaechen-e3-k1-s1-v2, flaechen-e3-k1-s4-v2  
  `Ein Dreieck hat die Grundseite g=# m und die Höhe h=# m.Berechne die Fläche des Dreiecks.`
- B-137 (2 Zeilen): trigonometrie-e4-k1-s3-v3, trigonometrie-e4-k1-s5-v3  
  `Im Dreieck ABC ist c=# cm,\gamma=#^\circ und\alpha=#^\circ.Wie lang ist die Seite b?`
- B-138 (2 Zeilen): trigonometrie-e4-k1-s3-v1, trigonometrie-e4-k1-s5-v1  
  `Im Dreieck ABC ist a=# cm,\alpha=#^\circ und\beta=#^\circ.Wie lang ist die Seite c?`
- B-139 (3 Zeilen): einheiten-basis-k1-v1, einheiten-basis-k1-v9, einheiten-e2-k1-s10-v1  
  `Ein Zug fährt um #:# Uhr ab und ist # h # min unterwegs.Wann kommt er an?(P# # OS)`
- B-140 (2 Zeilen): normalverteilung-und-sigma-regeln-zone-f2-v4, normalverteilung-und-sigma-regeln-zone-f2-v7  
  `Die Zuflussrate ist # Liter pro Minute,# Minuten lang.Wie viel Wasser fließt zu?`
- B-141 (2 Zeilen): trigonometrische-funktionen-zone-f6-v3, trigonometrische-funktionen-zone-f6-v4  
  `Welcher Anteil des Vollkreises sind #°?Gib ihn als Bruch und als Dezimalzahl an.`
- B-142 (6 Zeilen): daten-e3-k1-s5-v1, daten-e3-k1-s5-v2, daten-e3-k1-s5-v3, daten-e3-k1-s6-v1, daten-e3-k1-s6-v2, daten-e3-k1-s6-v3  
  `Ein Sektor im Kreisdiagramm steht für #\%.Wie groß ist sein Mittelpunktswinkel?`
- B-143 (2 Zeilen): quadratische-funktionen-e4-k1-s12-v1, quadratische-funktionen-e4-k1-s13-v1  
  `Berechne die gemeinsamen Punkte der Parabel f(x)=x^#+# und der Geraden g(x)=#x.`
- B-144 (2 Zeilen): einheiten-zone-f6-v2, einheiten-zone-f6-v4  
  `Zwei Schnittstellen liegen bei x=-# und x=#.Wie weit liegen sie auseinander?`
- B-145 (2 Zeilen): lineare-funktionen-e4-k1-s3-v3, lineare-funktionen-e4-k1-s5-v3  
  `Eine Gerade geht durch die Punkte A(#|#)und B(#|-#).Bestimme ihre Gleichung.`
- B-146 (4 Zeilen): lineare-funktionen-e4-k1-s3-v1, lineare-funktionen-e4-k1-s4-v1, lineare-funktionen-e4-k1-s4-v3, lineare-funktionen-e4-k1-s5-v1  
  `Eine Gerade geht durch die Punkte A(#|#)und B(#|#).Bestimme ihre Gleichung.`
- B-147 (2 Zeilen): trigonometrie-zone-f3-v1, trigonometrie-zone-f3-v3  
  `Berechne mit dem Taschenrechner.Tippe den Nenner in Klammern.\frac{#}{#+#}`
- B-148 (2 Zeilen): konfidenzintervalle-zone-f2-v3, konfidenzintervalle-zone-f2-v6  
  `X ist binomialverteilt mit n=# und p=#.Berechne P(X=#)auf Tausendstel.`
- B-149 (2 Zeilen): daten-zone-f3-v2, daten-zone-f3-v4  
  `Zeichne einen Winkel von #^\circ an den Strahl.‖Grafik:\winkelstrahl`
- B-150 (2 Zeilen): hypothesentests-zone-f2-v3, hypothesentests-zone-f2-v6  
  `X ist binomialverteilt mit n=# und p=#;P(X\le #)\approx #.P(X\ge #)?`
- B-151 (7 Zeilen): winkel-dreiecke-e3-k2-s1-v1, winkel-dreiecke-e3-k2-s1-v2, winkel-dreiecke-e3-k2-s1-v3, winkel-dreiecke-e3-k2-s1-v4, winkel-dreiecke-e3-k2-s1-v5, winkel-dreiecke-e3-k2-s2-v2, winkel-dreiecke-e3-k2-s2-v3  
  `Im Dreieck ABC ist\alpha=#^\circ und\beta=#^\circ.Wie groß ist γ?`
- B-152 (8 Zeilen): brueche-dezimalzahlen-basis-k3-v1, brueche-dezimalzahlen-basis-k3-v2, brueche-dezimalzahlen-basis-k3-v4, brueche-dezimalzahlen-basis-k3-v5, brueche-dezimalzahlen-basis-k3-v9, brueche-dezimalzahlen-basis-k3-v10, brueche-dezimalzahlen-e5-k2-s10-v9, brueche-dezimalzahlen-e5-k2-s10-v10  
  `Welche Zahl liegt genau in der Mitte zwischen-# und-#?(P# # OS)`
- B-153 (3 Zeilen): lineare-funktionen-e3-k2-s1-v3, lineare-funktionen-e3-k2-s1-v5, lineare-funktionen-e3-k2-s3-v2  
  `Setze x=# in f(x)=-#x+# ein.Berechne so den Funktionswert f(#).`
- B-154 (4 Zeilen): lineare-funktionen-e3-k2-s1-v2, lineare-funktionen-e3-k2-s1-v4, lineare-funktionen-e3-k2-s3-v1, lineare-funktionen-e3-k2-s3-v3  
  `Setze x=# in f(x)=#x-# ein.Berechne so den Funktionswert f(#).`
- B-155 (3 Zeilen): reelle-zahlen-e2-k1-s2-v1, reelle-zahlen-e2-k1-s2-v2, reelle-zahlen-e2-k1-s5-v1  
  `Schreibe #^#\cdot #^# als eine Potenz und berechne ihren Wert.`
- B-156 (2 Zeilen): einheiten-zone-f11-v1, einheiten-zone-f11-v3  
  `Ein Rechteck ist # m lang und # m breit.Berechne seine Fläche.`
- B-157 (7 Zeilen): quadratische-gleichungen-e2-k1-s1-v1, quadratische-gleichungen-e2-k1-s1-v2, quadratische-gleichungen-e2-k1-s1-v3, quadratische-gleichungen-e2-k1-s1-v4, quadratische-gleichungen-e2-k1-s1-v5, quadratische-gleichungen-e2-k1-s4-v1, quadratische-gleichungen-e2-k1-s4-v3  
  `Löse die Gleichung(x-#)\cdot(x-#)=#.Gib die Lösungsmenge an.`
- B-158 (4 Zeilen): potenz-exponentialfunktionen-e5-k2-s8-v1, potenz-exponentialfunktionen-zone-f15-v1, potenz-exponentialfunktionen-zone-f15-v2, potenz-exponentialfunktionen-zone-f15-v3  
  `Ein Würfel hat die Kante #\mathrm{cm}.Berechne sein Volumen.`
- B-159 (2 Zeilen): pythagoras-zone-f7-v1, pythagoras-zone-f7-v3  
  `Ein Kreis hat den Durchmesser # cm.Wie lang ist sein Radius?`
- B-160 (2 Zeilen): zufallsgroessen-und-verteilungen-zone-f1-v4, zufallsgroessen-und-verteilungen-zone-f1-v6  
  `Zwei Würfel werden geworfen–Wahrscheinlichkeit der Summe #?`
- B-161 (2 Zeilen): skalarprodukt-und-winkel-zone-f5-v1, skalarprodukt-und-winkel-zone-f5-v3  
  `Ein Winkel ist #^\circ groß.Wie groß ist sein Nebenwinkel?`
- B-162 (4 Zeilen): reelle-zahlen-e2-k1-s3-v1, reelle-zahlen-e2-k1-s3-v2, reelle-zahlen-e2-k1-s5-v2, reelle-zahlen-e2-k1-s5-v3  
  `Schreibe #^#:#^# als eine Potenz und berechne ihren Wert.`
- B-163 (2 Zeilen): prozentrechnung-e4-k2-s3-v1, prozentrechnung-e4-k2-s5-v1  
  `#\%einer Menge sind # kg.Wie viel kg ist die ganze Menge?`
- B-164 (2 Zeilen): prozentrechnung-e4-k2-s3-v3, prozentrechnung-e4-k2-s5-v2  
  `#\%einer Strecke sind # m.Wie lang ist die ganze Strecke?`
- B-165 (3 Zeilen): quadratische-gleichungen-e5-k2-s3-v1, quadratische-gleichungen-e5-k2-s3-v2, quadratische-gleichungen-e5-k2-s5-v3  
  `Löse die Wurzelgleichung\sqrt{#x+#}=x+#.Mache die Probe.`
- B-166 (2 Zeilen): rationale-zahlen-zone-f5-v1, rationale-zahlen-zone-f5-v3  
  `Setze x=# in den Term #\cdot x+# ein.Berechne den Wert.`
- B-167 (2 Zeilen): wahrscheinlichkeit-zone-f4-v1, wahrscheinlichkeit-zone-f4-v6  
  `Lose tragen die Nummern # bis #.Wie viele Lose sind es?`
- B-168 (2 Zeilen): quadratische-gleichungen-e5-k2-s4-v3, quadratische-gleichungen-e5-k2-s5-v2  
  `Löse die Wurzelgleichung\sqrt{#x+#}=x.Mache die Probe.`
- B-169 (6 Zeilen): brueche-dezimalzahlen-e2-k1-s5-v1, brueche-dezimalzahlen-e2-k1-s5-v2, brueche-dezimalzahlen-e2-k1-s5-v3, brueche-dezimalzahlen-e2-k1-s6-v1, brueche-dezimalzahlen-e2-k1-s6-v2, brueche-dezimalzahlen-e2-k1-s6-v3  
  `Mache die Brüche\frac{#}{#}und\frac{#}{#}gleichnamig.`
- B-170 (2 Zeilen): einheiten-zone-f8-v1, einheiten-zone-f8-v4  
  `Berechne # cm zum Quadrat.Gib das Ergebnis in cm² an.`
- B-171 (2 Zeilen): quadratische-gleichungen-e5-k2-s1-v3, quadratische-gleichungen-e5-k2-s5-v1  
  `Löse die Wurzelgleichung\sqrt{x-#}=#.Mache die Probe.`
- B-172 (7 Zeilen): rationale-zahlen-basis-k1-v1, rationale-zahlen-basis-k1-v2, rationale-zahlen-basis-k1-v3, rationale-zahlen-basis-k1-v7, rationale-zahlen-basis-k1-v10, rationale-zahlen-e3-k1-s7-v5, rationale-zahlen-e3-k1-s7-v6  
  `Berechne den Wert von #\cdot(x-#)für x=-#.(P# # FOR)`
- B-173 (4 Zeilen): quadratische-gleichungen-e1-k2-s8-v1, quadratische-gleichungen-e1-k2-s8-v2, quadratische-gleichungen-e1-k2-s8-v3, quadratische-gleichungen-e1-k2-s10-v1  
  `Löse die Gleichung(x-#)^#=#.Gib die Lösungsmenge an.`
- B-174 (2 Zeilen): brueche-dezimalzahlen-basis-k4-v1, brueche-dezimalzahlen-e5-k2-s10-v1  
  `Welcher Wert ist der kleinste:#;#;#^#;#\%?(P# # OS)`
- B-175 (2 Zeilen): potenz-exponentialfunktionen-e3-k2-s0-v3, potenz-exponentialfunktionen-zone-f8-v3  
  `Berechne #^#.Runde auf zwei Stellen nach dem Komma.`
- B-176 (2 Zeilen): terme-e4-k2-s3-v3, terme-e4-k2-s4-v3  
  `Klammere den größten gemeinsamen Faktor aus:#y^#+#y`
- B-177 (9 Zeilen): potenzen-wurzeln-e1-k3-s10-v1, potenzen-wurzeln-e1-k3-s10-v2, potenzen-wurzeln-e1-k3-s10-v3, potenzen-wurzeln-e1-k3-s11-v1, potenzen-wurzeln-e1-k3-s11-v2, potenzen-wurzeln-e1-k3-s11-v3, potenzen-wurzeln-e1-k3-s12-v1, potenzen-wurzeln-e1-k3-s12-v2, potenzen-wurzeln-e1-k3-s12-v3  
  `Welche Zahl muss für x stehen,damit #^x=# stimmt?`
- B-178 (2 Zeilen): einheiten-zone-f8-v2, einheiten-zone-f8-v3  
  `Berechne # m hoch drei.Gib das Ergebnis in m³ an.`
- B-179 (6 Zeilen): terme-e4-k2-s1-v1, terme-e4-k2-s1-v2, terme-e4-k2-s1-v3, terme-e4-k2-s1-v4, terme-e4-k2-s1-v5, terme-e4-k2-s4-v1  
  `Klammere den größten gemeinsamen Faktor aus:#x+#`
- B-180 (3 Zeilen): brueche-dezimalzahlen-basis-k2-v1, brueche-dezimalzahlen-basis-k2-v9, brueche-dezimalzahlen-e1-k2-s6-v4  
  `Wie viel Gramm sind\frac{#}{#}von # kg?(P# # OS)`
- B-181 (2 Zeilen): rationale-zahlen-basis-k3-v1, rationale-zahlen-e1-k1-s6-v1  
  `Gib eine Zahl an,die größer ist als-#.(P# # OS)`
- B-182 (2 Zeilen): prozentrechnung-zone-f1-v2, prozentrechnung-zone-f1-v5  
  `Erweitere den Bruch\frac{#}{#}auf den Nenner #.`
- B-183 (3 Zeilen): reelle-zahlen-zone-f1-v1, reelle-zahlen-zone-f1-v2, reelle-zahlen-zone-f1-v3  
  `Schreibe den Bruch\frac{#}{#}als Dezimalzahl.`
- B-184 (2 Zeilen): potenz-exponentialfunktionen-zone-f11-v1, potenz-exponentialfunktionen-zone-f11-v3  
  `Die Gleichung lautet y=#x.Berechne y für x=#.`
- B-185 (6 Zeilen): einheiten-e2-k1-s6-v1, einheiten-e2-k1-s6-v2, einheiten-e2-k1-s6-v3, einheiten-e2-k1-s7-v1, einheiten-e2-k1-s7-v2, einheiten-e2-k1-s7-v3  
  `Wie lange dauert es von #:# Uhr bis #:# Uhr?`
- B-186 (3 Zeilen): quadratische-funktionen-e4-k1-s1-v2, quadratische-funktionen-e4-k1-s1-v4, quadratische-funktionen-e4-k1-s18-v1  
  `Berechne die Nullstellen von f(x)=(x+#)^#-#.`
- B-187 (2 Zeilen): potenz-exponentialfunktionen-e5-k2-s2-v1, potenz-exponentialfunktionen-zone-f10-v2  
  `Die Funktion lautet f(x)=x^#.Berechne f(-#).`
- B-188 (4 Zeilen): potenz-exponentialfunktionen-e5-k2-s1-v1, potenz-exponentialfunktionen-e5-k2-s1-v3, potenz-exponentialfunktionen-e5-k2-s1-v5, potenz-exponentialfunktionen-zone-f10-v1  
  `Die Funktion lautet f(x)=x^#.Berechne f(#).`
- B-189 (2 Zeilen): quadratische-funktionen-e4-k1-s3-v3, quadratische-funktionen-e4-k1-s17-v3  
  `Berechne die Nullstellen von f(x)=x^#-#x+#.`
- B-190 (4 Zeilen): quadratische-funktionen-e3-k1-s3-v1, quadratische-funktionen-e3-k1-s3-v2, quadratische-funktionen-e3-k1-s3-v3, quadratische-funktionen-e3-k1-s9-v1  
  `Schreibe f(x)=(x-#)^#+# in der Normalform.`
- B-191 (3 Zeilen): quadratische-funktionen-e3-k1-s4-v2, quadratische-funktionen-e3-k1-s4-v3, quadratische-funktionen-e3-k1-s9-v2  
  `Schreibe f(x)=(x+#)^#-# in der Normalform.`
- B-192 (6 Zeilen): prozentrechnung-e1-k1-s2-v1, prozentrechnung-e1-k1-s2-v2, prozentrechnung-e1-k1-s2-v3, prozentrechnung-e1-k1-s3-v1, prozentrechnung-e1-k1-s3-v2, prozentrechnung-e1-k1-s3-v3  
  `Schreibe den Bruch\frac{#}{#}in Prozent.`
- B-193 (3 Zeilen): potenzen-wurzeln-zone-f9-v2, potenzen-wurzeln-zone-f9-v3, potenzen-wurzeln-zone-f9-v4  
  `Runde # auf zwei Stellen nach dem Komma.`
- B-194 (2 Zeilen): binomische-formeln-zone-f7-v1, binomische-formeln-zone-f7-v4  
  `Klammere den gemeinsamen Faktor aus:#x+#`
- B-195 (2 Zeilen): brueche-dezimalzahlen-e4-k1-s9-v3, brueche-dezimalzahlen-e5-k2-s10-v7  
  `Setze<,=oder>ein:#\%\leerfeld #(P# # OS)`
- B-196 (2 Zeilen): brueche-dezimalzahlen-e4-k1-s9-v4, brueche-dezimalzahlen-e5-k2-s10-v8  
  `Setze<,=oder>ein:#\leerfeld #\%(P# # OS)`
- B-197 (2 Zeilen): flaecheninhalt-und-volumen-im-raum-zone-f6-v1, flaecheninhalt-und-volumen-im-raum-zone-f6-v3  
  `Löse\tfrac{#}{#}\cdot #\cdot h=# nach h.`
- B-198 (2 Zeilen): lineare-gleichungssysteme-e1-k1-s2-v2, lineare-gleichungssysteme-zone-f2-v3  
  `Stelle die Gleichung #x+#y=# nach y um.`
- B-199 (2 Zeilen): stammfunktion-und-hauptsatz-zone-f3-v2, stammfunktion-und-hauptsatz-zone-f3-v4  
  `Welche Funktion hat die Ableitung #x^#?`
- B-200 (2 Zeilen): ebenen-zone-f2-v1, ebenen-zone-f2-v6  
  `A(#|#|#),B(#|#|#):\overrightarrow{AB}?`
- B-201 (3 Zeilen): lineare-gleichungen-e1-k2-s2-v1, lineare-gleichungen-e1-k2-s2-v3, lineare-gleichungen-e1-k2-s3-v1  
  `Prüfe,ob # die Gleichung #x+#=# löst.`
- B-202 (3 Zeilen): spiegelung-zone-f5-v1, spiegelung-zone-f5-v2, spiegelung-zone-f5-v4  
  `Mittelpunkt von A(#|#|#)und B(#|#|#)?`
- B-203 (2 Zeilen): lineare-gleichungen-e1-k2-s2-v2, lineare-gleichungen-e1-k2-s3-v2  
  `Prüfe,ob # die Gleichung #x-#=# löst.`
- B-204 (6 Zeilen): bruchrechnung-e3-k1-s3-v1, bruchrechnung-e3-k1-s3-v2, bruchrechnung-e3-k1-s3-v3, bruchrechnung-e3-k1-s4-v1, bruchrechnung-e3-k1-s4-v2, bruchrechnung-e3-k1-s4-v3  
  `Berechne.\frac{#}{#}\cdot\frac{#}{#}`
- B-205 (4 Zeilen): potenzen-wurzeln-e1-k4-s1-v1, potenzen-wurzeln-e1-k4-s1-v2, potenzen-wurzeln-e1-k4-s1-v3, potenzen-wurzeln-e1-k6-s1-v3  
  `Berechne\left(\frac{#}{#}\right)^#.`
- B-206 (3 Zeilen): binomische-formeln-e1-k1-s7-v1, binomische-formeln-e2-k2-s3-v1, binomische-formeln-e2-k2-s3-v3  
  `Multipliziere aus:(x+#)\cdot(x-#)`
- B-207 (3 Zeilen): strahlensaetze-zone-f2-v1, strahlensaetze-zone-f2-v4, strahlensaetze-zone-f2-v7  
  `Rechne #\text{m}in Zentimeter um.`
- B-208 (2 Zeilen): binomische-formeln-e1-k1-s7-v2, binomische-formeln-e2-k2-s3-v2  
  `Multipliziere aus:(x-#)\cdot(x+#)`
- B-209 (2 Zeilen): reelle-zahlen-zone-f2-v1, reelle-zahlen-zone-f2-v4  
  `Welche Zahl ist größer,-# oder-#?`
- B-210 (2 Zeilen): zuordnungen-zone-f5-v1, zuordnungen-zone-f5-v4  
  `Wie viele Minuten sind # Stunden?`
- B-211 (5 Zeilen): bruchrechnung-e3-k2-s4-v1, bruchrechnung-e3-k2-s4-v2, bruchrechnung-e3-k2-s4-v3, bruchrechnung-e3-k2-s5-v1, bruchrechnung-e3-k2-s5-v2  
  `Berechne.\frac{#}{#}:\frac{#}{#}`
- B-212 (4 Zeilen): bruchrechnung-e1-k3-s4-v2, bruchrechnung-e1-k3-s4-v3, bruchrechnung-e1-k3-s6-v2, bruchrechnung-e1-k3-s6-v3  
  `Berechne.\frac{#}{#}-\frac{#}{#}`
- B-213 (3 Zeilen): hypothesentests-zone-f3-v1, hypothesentests-zone-f3-v2, hypothesentests-zone-f3-v3  
  `n=# p=#:Erwartungswert n\cdot p?`
- B-214 (2 Zeilen): bruchrechnung-e1-k3-s4-v1, bruchrechnung-e1-k3-s6-v1  
  `Berechne.\frac{#}{#}+\frac{#}{#}`
- B-215 (2 Zeilen): daten-zone-f9-v2, daten-zone-f9-v3  
  `Löse die Gleichung.#\cdot #+#x=#`
- B-216 (2 Zeilen): quadratische-gleichungen-e5-k3-s3-v1, quadratische-gleichungen-e5-k3-s5-v2  
  `Löse die Ungleichung x^#-#x-#<#.`
- B-217 (2 Zeilen): winkel-dreiecke-zone-f2-v4, winkel-dreiecke-zone-f2-v6  
  `Berechne.#^\circ-#^\circ-#^\circ`
- B-218 (2 Zeilen): punkte-und-strecken-im-koordinatensystem-e2-k1-s1-v5, punkte-und-strecken-im-koordinatensystem-zone-f3-v7  
  `K(#|#|#),L(#|#|#):Länge von KL?`
- B-219 (2 Zeilen): pyramide-kegel-kugel-zone-f5-v3, pyramide-kegel-kugel-zone-f5-v4  
  `Berechne vier Drittel von #.`
- B-220 (4 Zeilen): einheiten-e2-k1-s2-v2, einheiten-e2-k1-s5-v1, einheiten-e2-k1-s5-v2, einheiten-e2-k1-s5-v3  
  `Rechne # min in Stunden um.`
- B-221 (4 Zeilen): lineare-gleichungen-zone-f4-v1, lineare-gleichungen-zone-f4-v2, lineare-gleichungen-zone-f4-v3, lineare-gleichungen-zone-f4-v5  
  `Berechne.\frac{#}{#}\cdot #`
- B-222 (3 Zeilen): quadratische-gleichungen-e5-k3-s2-v1, quadratische-gleichungen-e5-k3-s2-v2, quadratische-gleichungen-e5-k3-s5-v1  
  `Löse die Ungleichung x^#>#.`
- B-223 (2 Zeilen): ableitungsregeln-zone-f3-v3, ableitungsregeln-zone-f3-v4  
  `\frac{#}{#}\cdot #–gekürzt?`
- B-224 (2 Zeilen): rationale-zahlen-zone-f3-v2, rationale-zahlen-zone-f3-v5  
  `Berechne:\frac{#}{#}\cdot #`
- B-225 (6 Zeilen): lineare-gleichungen-e3-k2-s1-v1, lineare-gleichungen-e3-k2-s1-v2, lineare-gleichungen-e3-k2-s1-v3, lineare-gleichungen-e3-k2-s1-v4, lineare-gleichungen-e3-k2-s1-v5, lineare-gleichungen-e3-k3-s1-v3  
  `Löse die Gleichung.#x=#x+#`
- B-226 (2 Zeilen): brueche-dezimalzahlen-zone-f7-v4, brueche-dezimalzahlen-zone-f7-v6  
  `Schreibe #\%als Kommazahl.`
- B-227 (2 Zeilen): lineare-funktionen-zone-f5-v3, lineare-funktionen-zone-f5-v4  
  `Löse die Gleichung.#=-#x+#`
- B-228 (2 Zeilen): lineare-gleichungssysteme-zone-f4-v1, lineare-gleichungssysteme-zone-f4-v3  
  `Löse die Gleichung #x+#=#.`
- B-229 (2 Zeilen): wahrscheinlichkeit-zone-f2-v2, wahrscheinlichkeit-zone-f2-v4  
  `Berechne #\%von # Feldern.`
- B-230 (8 Zeilen): brueche-dezimalzahlen-e1-k2-s1-v1, brueche-dezimalzahlen-e1-k2-s1-v2, brueche-dezimalzahlen-e1-k2-s1-v3, brueche-dezimalzahlen-e1-k2-s1-v4, brueche-dezimalzahlen-e1-k2-s1-v5, brueche-dezimalzahlen-e1-k2-s2-v1, brueche-dezimalzahlen-e1-k2-s2-v2, brueche-dezimalzahlen-e1-k2-s2-v3  
  `Berechne\frac{#}{#}von #.`
- B-231 (5 Zeilen): einheiten-e2-k1-s1-v2, einheiten-e2-k1-s1-v4, einheiten-e2-k1-s4-v1, einheiten-e2-k1-s4-v2, einheiten-e2-k1-s4-v3  
  `Rechne # h in Minuten um.`
- B-232 (3 Zeilen): einheiten-e2-k1-s2-v1, einheiten-e2-k1-s2-v3, einheiten-e2-k5-s1-v2  
  `Rechne # s in Minuten um.`
- B-233 (3 Zeilen): reelle-zahlen-e2-k2-s1-v1, reelle-zahlen-zone-f6-v5, reelle-zahlen-zone-f6-v7  
  `Schreibe #^{-#}als Bruch.`
- B-234 (2 Zeilen): potenzen-wurzeln-zone-f1-v4, potenzen-wurzeln-zone-f2-v3  
  `Berechne #\cdot #\cdot #.`
- B-235 (2 Zeilen): rotationsvolumen-zone-f1-v1, rotationsvolumen-zone-f1-v7  
  `(x+#)^# ausmultipliziert?`
- B-236 (3 Zeilen): reelle-zahlen-zone-f3-v1, reelle-zahlen-zone-f3-v2, reelle-zahlen-zone-f3-v5  
  `Welche Zahl ist\sqrt{#}?`
- B-237 (2 Zeilen): brueche-dezimalzahlen-zone-f2-v1, brueche-dezimalzahlen-zone-f2-v4  
  `Rechne # kg in Gramm um.`
- B-238 (2 Zeilen): winkel-dreiecke-zone-f2-v1, winkel-dreiecke-zone-f2-v3  
  `Berechne.#^\circ+#^\circ`
- B-239 (2 Zeilen): vierfeldertafel-zone-f3-v1, vierfeldertafel-zone-f3-v3  
  `P(A)=#–P(\overline{A})?`
- B-240 (6 Zeilen): potenzen-wurzeln-e2-k1-s4-v1, potenzen-wurzeln-e2-k1-s4-v2, potenzen-wurzeln-e2-k1-s4-v3, potenzen-wurzeln-e2-k1-s5-v1, potenzen-wurzeln-e2-k1-s5-v2, potenzen-wurzeln-e2-k1-s5-v3  
  `Berechne #\cdot #^{#}.`
- B-241 (2 Zeilen): binomische-formeln-e3-k1-s5-v2, binomische-formeln-e3-k1-s6-v2  
  `Faktorisiere:#x^#+#x+#`
- B-242 (2 Zeilen): binomische-formeln-e3-k1-s5-v3, binomische-formeln-e3-k1-s6-v3  
  `Faktorisiere:#x^#-#x+#`
- B-243 (3 Zeilen): vektoren-und-rechenoperationen-zone-f6-v1, vektoren-und-rechenoperationen-zone-f6-v2, vektoren-und-rechenoperationen-zone-f6-v4  
  `(#|#|#)\circ(#|#|#)=?`
- B-244 (2 Zeilen): flaecheninhalt-durch-integration-zone-f2-v2, flaecheninhalt-durch-integration-zone-f2-v4  
  `x^#-#x=#–Nullstellen?`
- B-245 (3 Zeilen): terme-e1-k4-s2-v2, terme-e1-k4-s7-v2, terme-e1-k4-s11-v2  
  `Fasse zusammen:#a-#a`
- B-246 (2 Zeilen): einheiten-e1-k2-s5-v3, einheiten-e1-k2-s8-v3  
  `Rechne # kg in g um.`
- B-247 (2 Zeilen): koerper-zone-f6-v1, koerper-zone-f6-v3  
  `Berechne #\%von # l.`
- B-248 (2 Zeilen): lineare-funktionen-zone-f3-v4, lineare-funktionen-zone-f3-v6  
  `Rechne:-#\cdot(-#)+#`
- B-249 (2 Zeilen): potenzen-wurzeln-zone-f8-v2, potenzen-wurzeln-zone-f8-v5  
  `Berechne\frac{#}{#}.`
- B-250 (2 Zeilen): terme-e1-k4-s2-v3, terme-e1-k4-s7-v3  
  `Fasse zusammen:#b-#b`
- B-251 (2 Zeilen): binomische-formeln-e3-k1-s5-v1, binomische-formeln-e3-k1-s6-v1  
  `Faktorisiere:#x^#-#`
- B-252 (2 Zeilen): rationale-zahlen-zone-f4-v1, rationale-zahlen-zone-f4-v3  
  `Berechne:#+#\cdot #`
- B-253 (2 Zeilen): terme-zone-f4-v3, terme-zone-f4-v4  
  `Rechne:#-#\cdot #`
- B-254 (3 Zeilen): grenzwerte-und-verhalten-im-unendlichen-zone-f1-v1, grenzwerte-und-verhalten-im-unendlichen-zone-f1-v2, grenzwerte-und-verhalten-im-unendlichen-zone-f1-v3  
  `Berechne:(-#)^#`
- B-255 (2 Zeilen): rationale-zahlen-e2-k3-s4-v1, rationale-zahlen-e2-k3-s7-v3  
  `Berechne:#-(-#)`
- B-256 (2 Zeilen): rationale-zahlen-zone-f4-v4, rationale-zahlen-zone-f4-v6  
  `Berechne:#-#:#`
- B-257 (4 Zeilen): potenzen-wurzeln-e1-k3-s6-v1, potenzen-wurzeln-e1-k3-s6-v2, potenzen-wurzeln-e1-k3-s6-v3, potenzen-wurzeln-zone-f3-v5  
  `Berechne-#^#.`
- B-258 (4 Zeilen): rationale-zahlen-e2-k3-s1-v1, rationale-zahlen-e2-k3-s1-v2, rationale-zahlen-e2-k3-s1-v4, rationale-zahlen-e2-k3-s7-v1  
  `Berechne:-#+#`
- B-259 (3 Zeilen): rationale-zahlen-e2-k3-s1-v3, rationale-zahlen-e2-k3-s1-v5, rationale-zahlen-e2-k3-s7-v2  
  `Berechne:-#-#`
- B-260 (2 Zeilen): rationale-zahlen-zone-f1-v2, rationale-zahlen-zone-f1-v3  
  `Berechne:#:#`
- B-261 (2 Zeilen): rationale-zahlen-zone-f1-v4, rationale-zahlen-zone-f3-v3  
  `Berechne:#-#`
- B-262 (2 Zeilen): rationale-zahlen-zone-f3-v1, rationale-zahlen-zone-f3-v4  
  `Berechne:#+#`
- B-263 (3 Zeilen): terme-zone-f1-v4, terme-zone-f1-v7, terme-zone-f3-v5  
  `Rechne:-#-#`
- B-264 (2 Zeilen): terme-zone-f1-v2, terme-zone-f1-v3  
  `Rechne:-#+#`
- B-265 (2 Zeilen): gleichungen-loesen-zone-f4-v1, gleichungen-loesen-zone-f4-v4  
  `Löse:x^#=#`
- B-266 (2 Zeilen): terme-zone-f1-v1, terme-zone-f3-v3  
  `Rechne:#-#`
- B-267 (2 Zeilen): terme-zone-f3-v1, terme-zone-f3-v4  
  `Rechne:#+#`

## B Bis auf Zahlen gleich, in derselben Sprosse (Varianten)

Nach bank.md unterscheiden sich Varianten einer Sprosse in Zahlen und Kontext; hier fehlt der andere Kontext (oder die Aufgabe hat keinen). Nur Kennung, Zeilen und Text gekürzt.

- B-268 (2): schnittmengen-e3-k1-s5-v1, schnittmengen-e3-k1-s5-v3 – `Die Abbildung zeigt den Quader mit A(#|#|#),B(#|#|#),C(#|#|#)und F(#|#|#),die Gerade h durch B und F sowie die Schnittfi …`
- B-269 (2): schnittmengen-e3-k1-s2-v1, schnittmengen-e3-k1-s2-v2 – `Ein Holzkörper ist eine Pyramide über dem Quadrat ABCD mit A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)und der Spitze E(#|#|#)sen …`
- B-270 (2): lineare-funktionen-e5-k1-s5-v1, lineare-funktionen-e5-k1-s5-v2 – `Jana will ein Auto mieten.Bei Angebot # kostet die Miete #€pro Tag.# km sind insgesamt frei,jeder weitere km kostet #€.B …`
- B-271 (2): spiegelung-e2-k1-s5-v1, spiegelung-e2-k1-s5-v2 – `Die Abbildung zeigt die Punkte A,B und P in der x_#x_#-Ebene.g geht durch A und P,g^*durch B und P;g^*entsteht aus g dur …`
- B-272 (2): vektoren-und-rechenoperationen-e2-k2-s3-v1, vektoren-und-rechenoperationen-e2-k2-s3-v2 – `Gib\overrightarrow{AP}mit\vec u,\vec v,\vec w an.‖Grafik:\begin{ksys#}[x#max=#]\rquader{#}{#}{#}{#}\rpunkt*{#}{#}{#}{A}\ …`
- B-273 (3): strahlensaetze-e2-k2-s1-v1, strahlensaetze-e2-k2-s1-v2, strahlensaetze-e2-k2-s1-v3 – `Das Koordinatensystem zeigt zwei Dreiecke.Das Dreieck A'B'C'ist das Bild von ABC bei einer zentrischen Streckung.Zeichne …`
- B-274 (3): punkte-und-strecken-im-koordinatensystem-e1-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e1-k1-s7-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s7-v3 – `Eine Pyramide hat den quadratischen Boden ABCD mit der Seite # cm;die Spitze S liegt # cm senkrecht über A.Im Gitter sin …`
- B-275 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v5, punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v6 – `Eine Pyramide hat den quadratischen Boden ABCD mit der Seite # in der x_#x_#-Ebene,A im Ursprung,B auf der x_#-Achse,D a …`
- B-276 (2): extremalprobleme-e1-k1-s5-v3, extremalprobleme-e1-k1-s5-v4 – `Gegeben ist f(x)=-#x^#+#x^#+#.Die Punkte O(#|#),P(#|#)und Q(#|f(#))bilden ein rechtwinkliges Dreieck.Zeichne es ein,bere …`
- B-277 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s7-v5, flaecheninhalt-und-volumen-im-raum-e1-k2-s7-v6 – `Der Flächeninhalt des Dreiecks PQR im Koordinatensystem wird mit dem Term #\cdot #-#\cdot\tfrac{#}{#}\cdot #\cdot #-\tfr …`
- B-278 (2): trigonometrie-e4-k1-s17-v3, trigonometrie-e4-k1-s17-v4 – `Eine Rampe y führt zu einer Treppe.Die Rampe,eine waagerechte Strecke und eine Hilfslinie bilden ein Dreieck.Die waagere …`
- B-279 (5): winkel-dreiecke-e5-k2-s1-v1, winkel-dreiecke-e5-k2-s1-v2, winkel-dreiecke-e5-k2-s1-v3, winkel-dreiecke-e5-k2-s1-v4, winkel-dreiecke-e5-k2-s1-v5 – `Die Punkte A,B und C liegen auf einem Kreis mit dem Mittelpunkt M;C liegt nicht auf dem Bogen AB unter dem Mittelpunktsw …`
- B-280 (3): konfidenzintervalle-e1-k1-s2-v1, konfidenzintervalle-e1-k1-s2-v2, konfidenzintervalle-e1-k1-s2-v3 – `Vermutet wird ein Anteil von #\%.In einer Stichprobe vom Umfang n=# gibt es # Treffer.Lies das Konfidenzintervall zur Si …`
- B-281 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v7, punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v8 – `Ein Körper hat den rechteckigen Boden A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)und die Firstkante P(#|#|#),Q(#|#|#);die Dreiec …`
- B-282 (2): ableitung-und-aenderungsrate-e1-k1-s10-v3, ableitung-und-aenderungsrate-e1-k1-s10-v4 – `Die CO_#-Konzentration in einem Raum wird durch g(x)=-#\cdot\mathrm{e}^{-#x}+# beschrieben(x in Stunden,g(x)in ppm).Weis …`
- B-283 (4): konfidenzintervalle-e1-k1-s1-v1, konfidenzintervalle-e1-k1-s1-v2, konfidenzintervalle-e1-k1-s1-v3, konfidenzintervalle-e1-k1-s1-v5 – `Die Grafik zeigt Grenzgraphen für Stichproben vom Umfang n=#(Sicherheitswahrscheinlichkeit #\%).In einer Stichprobe gibt …`
- B-284 (3): pythagoras-e2-k4-s4-v1, pythagoras-e2-k4-s4-v2, pythagoras-e2-k4-s4-v3 – `Ein Rechteck ist # cm lang und # cm breit.Verwandle es mit dem Höhensatz in ein flächengleiches Quadrat:Lege beide Seite …`
- B-285 (2): skalarprodukt-und-winkel-e4-k2-s1-v1, skalarprodukt-und-winkel-e4-k2-s1-v2 – `Eine gerade Pyramide hat ihre quadratische Grundfläche in der xy-Ebene,eine Ecke F(#\mid #\mid #)und die Spitze S(#\mid …`
- B-286 (3): strahlensaetze-e2-k1-s2-v1, strahlensaetze-e2-k1-s2-v2, strahlensaetze-e2-k1-s2-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und das Zentrum Z.Das Zentrum liegt außerhalb des Dreiecks.Zeichne Strahlen …`
- B-287 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s4-v1, flaecheninhalt-und-volumen-im-raum-e1-k2-s4-v2 – `Licht fällt in Richtung(#|#|-#)auf das Dreieck mit P(#|#|#),Q(#|#|#),R(#|#|#).Bestimme die Schattenpunkte in der x-y-Ebe …`
- B-288 (2): symmetrie-abbildungen-e3-k1-s8-v1, symmetrie-abbildungen-e3-k1-s8-v2 – `Im Koordinatensystem sind die Dreiecke ABC und DEF der Anfang eines Bandornaments.Zeichne die nächsten zwei Dreiecke.Nen …`
- B-289 (2): kenngroessen-von-verteilungen-e3-k3-s1-v1, kenngroessen-von-verteilungen-e3-k3-s1-v2 – `Die Diagramme zeigen die Verteilungen von X und Y,beide binomialverteilt mit n=#;die Erwartungswerte sind ganzzahlig.Das …`
- B-290 (3): winkel-dreiecke-e5-k1-s5-v1, winkel-dreiecke-e5-k1-s5-v2, winkel-dreiecke-e5-k1-s5-v3 – `Die Figur zeigt die Ecken eines Dreiecks ABC im Koordinatensystem.Zeichne das Dreieck.Zeichne mit dem Geodreieck die Höh …`
- B-291 (2): strahlensaetze-e2-k2-s3-v1, strahlensaetze-e2-k2-s3-v3 – `Das Dreieck A'B'C'ist das Bild des Dreiecks ABC bei einer zentrischen Streckung.Konstruiere das Zentrum Z und gib seine …`
- B-292 (2): trigonometrische-funktionen-e1-k1-s3-v1, trigonometrische-funktionen-e1-k1-s3-v2 – `Das Koordinatensystem zeigt einen Punkt P auf dem Einheitskreis.Lies sin\alpha und cos\alpha für P ab.Runde auf eine Ste …`
- B-293 (2): zinsrechnung-e2-k2-s1-v2, zinsrechnung-e2-k2-s1-v3 – `Auf einem Konto liegen am Start #€.Der Zinssatz ist #\%.Am Ende jedes Jahres kommen erst die Zinsen dazu,dann #€Einzahlu …`
- B-294 (2): flaecheninhalt-durch-integration-e4-k1-s6-v3, flaecheninhalt-durch-integration-e4-k1-s6-v4 – `Für a># schließt der Graph von f_a(x)=x^#-a^# im vierten Quadranten mit den Koordinatenachsen eine Fläche ein.Das Dreiec …`
- B-295 (2): symmetrie-abbildungen-e2-k3-s5-v1, symmetrie-abbildungen-e2-k3-s5-v3 – `Im Koordinatensystem ist die halbe Figur mit den Punkten A,B,C,D gezeichnet.Die Gerade a ist die Symmetrieachse.Ergänze …`
- B-296 (3): kurvenuntersuchung-e5-k1-s1-v1, kurvenuntersuchung-e5-k1-s1-v2, kurvenuntersuchung-e5-k1-s1-v4 – `Ein Getränk wird in einen Raum mit #°C gebracht.Die Abbildung zeigt seine Temperatur T(in°C)t Minuten danach.Beschreibe …`
- B-297 (2): kurvenuntersuchung-e5-k1-s1-v3, kurvenuntersuchung-e5-k1-s1-v5 – `Ein Getränk wird in einen Raum mit #°C gebracht.Die Abbildung zeigt seine Temperatur T(in°C)t Minuten danach.Beschreibe …`
- B-298 (3): pythagoras-e1-k3-s1-v1, pythagoras-e1-k3-s1-v2, pythagoras-e1-k3-s1-v3 – `Im Kästchengitter sind die Punkte A,B und C eingezeichnet.Sie bilden ein Dreieck mit einem rechten Winkel bei A.Zeichne …`
- B-299 (3): zinsrechnung-e2-k1-s3-v1, zinsrechnung-e2-k1-s3-v2, zinsrechnung-e2-k1-s3-v3 – `Die Tabelle zeigt ein Sparkonto mit #\%Zinsen im Jahr.Die Zinsen werden vom Guthaben der Zeile davor berechnet.Es gilt:n …`
- B-300 (2): ableitung-und-aenderungsrate-e3-k1-s1-v4, ableitung-und-aenderungsrate-e3-k1-s1-v5 – `Gegeben ist f(x)=x^#-#x mit dem Punkt P(#|-#)auf dem Graphen.Q(#+h|f(#+h))ist ein zweiter Punkt des Graphen.Berechne für …`
- B-301 (2): strahlensaetze-e2-k1-s3-v1, strahlensaetze-e2-k1-s3-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und das Zentrum Z.Verkleinere das Dreieck vom Zentrum Z aus mit k=#.Zeichne …`
- B-302 (3): punkte-und-strecken-im-koordinatensystem-e5-k1-s6-v1, punkte-und-strecken-im-koordinatensystem-e5-k1-s6-v2, punkte-und-strecken-im-koordinatensystem-e5-k1-s6-v3 – `Ein Dachgeschoss hat einen rechteckigen Boden von # m mal # m.Die Dachflächen steigen von den beiden Traufwänden(Höhe # …`
- B-303 (2): trigonometrische-funktionen-e2-k1-s0-v1, trigonometrische-funktionen-e2-k1-s0-v3 – `Das Koordinatensystem zeigt eine Welle.Kreuze an,welcher Abschnitt genau eine ganze Wiederholung ist.\\kreuz{von A bis B …`
- B-304 (3): winkel-dreiecke-e5-k1-s2-v1, winkel-dreiecke-e5-k1-s2-v2, winkel-dreiecke-e5-k1-s2-v3 – `Die Figur zeigt die Ecken eines spitzwinkligen Dreiecks ABC im Koordinatensystem.Zeichne das Dreieck.Konstruiere zwei Mi …`
- B-305 (3): zinsrechnung-e2-k1-s4-v1, zinsrechnung-e2-k1-s4-v2, zinsrechnung-e2-k1-s4-v3 – `Die Tabelle zeigt ein Sparkonto mit #\%Zinsen im Jahr.Jedes Jahr werden #€eingezahlt.Ergänze die zwei leeren Felder.Kont …`
- B-306 (2): pyramide-kegel-kugel-e3-k1-s17-v1, pyramide-kegel-kugel-e3-k1-s17-v2 – `Von einer Kugel mit dem Radius # cm wird # cm vom Mittelpunkt entfernt eine Kappe abgeschnitten.Bestimme die Höhe h der …`
- B-307 (3): winkel-dreiecke-e2-k2-s5-v1, winkel-dreiecke-e2-k2-s5-v2, winkel-dreiecke-e2-k2-s5-v3 – `Die Figur zeigt zwei parallele Geraden g und h.Die Gerade g liegt oben,h liegt unten.Die Gerade k schneidet beide.An g l …`
- B-308 (2): lineare-funktionen-e2-k3-s0-v1, lineare-funktionen-e2-k3-s0-v3 – `Das Koordinatensystem zeigt eine Gerade mit einem Steigungsdreieck.Das Dreieck geht einen Schritt nach rechts.Lies ab,wi …`
- B-309 (2): lineare-funktionen-e2-k3-s0-v2, lineare-funktionen-e2-k3-s0-v4 – `Das Koordinatensystem zeigt eine Gerade mit einem Steigungsdreieck.Das Dreieck geht einen Schritt nach rechts.Lies ab,wi …`
- B-310 (2): prozentrechnung-e1-k1-s5-v1, prozentrechnung-e1-k1-s5-v2 – `Fülle die Tabelle aus.In jeder Spalte steht dieselbe Zahl in vier Schreibweisen.Kürze die Brüche so weit wie möglich.‖Gr …`
- B-311 (2): trigonometrie-e4-k1-s17-v11, trigonometrie-e4-k1-s17-v12 – `Das Viereck ABCD hat bei A einen rechten Winkel.Die Diagonale BD teilt es in zwei Dreiecke.Es gilt\angle ADB=#^\circ,\an …`
- B-312 (2): winkel-dreiecke-e2-k2-s6-v2, winkel-dreiecke-e2-k2-s6-v3 – `Die Figur zeigt zwei parallele Geraden g und h.Die Gerade g liegt oben,h liegt unten.Die Gerade k schneidet beide.An g l …`
- B-313 (3): winkel-dreiecke-e2-k2-s7-v1, winkel-dreiecke-e2-k2-s7-v2, winkel-dreiecke-e2-k2-s7-v3 – `Die Figur zeigt zwei parallele Geraden g und h.Die Gerade g liegt oben,h liegt unten.Die Gerade k schneidet beide.An g l …`
- B-314 (2): flaechen-e2-k1-s6-v1, flaechen-e2-k1-s6-v3 – `Die Skizze zeigt ein Parallelogramm.Die Grundseite ist g=# cm,die Höhe ist h=# cm.Zeichne in der Skizze die Höhe zu g ei …`
- B-315 (2): lineare-funktionen-e2-k5-s6-v1, lineare-funktionen-e2-k5-s6-v2 – `Das Koordinatensystem zeigt die Geraden f,g und h.Ordne jeder Geraden eine dieser Gleichungen zu:y=-#x+#;y=-\frac{#}{#}x …`
- B-316 (2): uneigentliche-integrale-e2-k1-s0-v2, uneigentliche-integrale-e2-k1-s0-v3 – `Die Fläche R rechts von x=# ist schraffiert.Fällt sie gegenüber der Fläche links davon ins Gewicht?\\kreuz{fällt ins Gew …`
- B-317 (4): strahlensaetze-e2-k1-s1-v1, strahlensaetze-e2-k1-s1-v2, strahlensaetze-e2-k1-s1-v4, strahlensaetze-e2-k1-s1-v5 – `Das Koordinatensystem zeigt das Dreieck ABC.Strecke es vom Zentrum Z=A aus mit dem Streckfaktor k=#.Zeichne das Bilddrei …`
- B-318 (2): strahlensaetze-e3-k3-s3-v1, strahlensaetze-e3-k3-s3-v2 – `Zeichne einen Punkt Z und einen Punkt A mit\overline{ZA}=#\text{cm}.Konstruiere den Bildpunkt A'der Streckung von Z aus …`
- B-319 (2): normalverteilung-und-sigma-regeln-e3-k1-s1-v4, normalverteilung-und-sigma-regeln-e3-k1-s1-v5 – `Die Abbildung zeigt den Graphen der Verteilungsfunktion F einer normalverteilten Zufallsgröße X.Lies\mu und\sigma ab.(Ab …`
- B-320 (3): winkel-dreiecke-e5-k1-s4-v1, winkel-dreiecke-e5-k1-s4-v2, winkel-dreiecke-e5-k1-s4-v3 – `Die Figur zeigt die Ecken eines Dreiecks ABC im Koordinatensystem.Zeichne das Dreieck.Konstruiere zwei Winkelhalbierende …`
- B-321 (2): flaecheninhalt-durch-integration-e5-k1-s8-v3, flaecheninhalt-durch-integration-e5-k1-s8-v4 – `f(x)=x^# für #\le x\le #;sein Graph wird an der Geraden y=x gespiegelt.Begründe,dass der Term #\cdot # minus Integral vo …`
- B-322 (2): lineare-gleichungssysteme-e5-k1-s12-v1, lineare-gleichungssysteme-e5-k1-s12-v3 – `Eine Mischung aus drei Sorten hat die Anteile x,y und z.Keiner der Anteile ist negativ.Das zugehörige Gleichungssystem h …`
- B-323 (2): lineare-funktionen-e5-k2-s1-v1, lineare-funktionen-e5-k2-s1-v2 – `Ein Tarif kostet #€Grundgebühr und #€je Stunde.Das Koordinatensystem zeigt die Graphen A,B und C.Gib den Graphen an,der …`
- B-324 (2): trigonometrie-e3-k1-s19-v5, trigonometrie-e3-k1-s19-v6 – `Im Dreieck ABC liegt der Punkt F auf AC.Die Strecke BF steht senkrecht auf AC.Es gilt AB=# cm,und der Winkel bei A ist # …`
- B-325 (5): flaecheninhalt-durch-integration-e5-k1-s1-v1, flaecheninhalt-durch-integration-e5-k1-s1-v2, flaecheninhalt-durch-integration-e5-k1-s1-v3, flaecheninhalt-durch-integration-e5-k1-s1-v4, flaecheninhalt-durch-integration-e5-k1-s1-v5 – `Die Abbildung zeigt den Graphen von f(x)=x-#;die Gitterlinien haben den Abstand #.Bestimme den Wert des Integrals von # …`
- B-326 (3): pyramide-kegel-kugel-e1-k5-s12-v1, pyramide-kegel-kugel-e1-k5-s12-v2, pyramide-kegel-kugel-e1-k5-s12-v3 – `Eine Pyramide hat ein Quadrat als Grundfläche.Die Grundkante ist # cm lang,die Höhe ist # cm.Zeichne ihr Schrägbild.Zeic …`
- B-327 (2): flaecheninhalt-und-volumen-im-raum-e2-k3-s3-v1, flaecheninhalt-und-volumen-im-raum-e2-k3-s3-v3 – `Stelle für das Viereck PQRS im Koordinatensystem einen Flächenterm„Rechteck plus rechtwinkliges Dreieck“auf und berechne …`
- B-328 (5): winkel-dreiecke-e5-k1-s1-v1, winkel-dreiecke-e5-k1-s1-v2, winkel-dreiecke-e5-k1-s1-v3, winkel-dreiecke-e5-k1-s1-v4, winkel-dreiecke-e5-k1-s1-v5 – `Die Figur zeigt die Punkte A und B im Koordinatensystem.Verbinde A und B.Konstruiere mit dem Zirkel die Mittelsenkrechte …`
- B-329 (3): binomialverteilung-e5-k1-s1-v2, binomialverteilung-e5-k1-s1-v4, binomialverteilung-e5-k1-s1-v5 – `Das Säulendiagramm zeigt die Verteilung der Anzahl X der Treffer bei # Versuchen(Werte gerundet).Mit welcher Wahrscheinl …`
- B-330 (3): symmetrie-abbildungen-e3-k1-s2-v1, symmetrie-abbildungen-e3-k1-s2-v2, symmetrie-abbildungen-e3-k1-s2-v3 – `Im Koordinatensystem wurde das Dreieck ABC auf A'B'C'verschoben.Beschreibe die Verschiebung in Kästchen.‖Grafik:\begin{k …`
- B-331 (2): trigonometrische-funktionen-e3-k1-s0-v1, trigonometrische-funktionen-e3-k1-s0-v4 – `Das Koordinatensystem zeigt die Wellen f und g.Kreuze an,was bei g anders ist als bei f.\\kreuz{die Höhe(a)}\kreuz{die B …`
- B-332 (2): trigonometrische-funktionen-e3-k1-s0-v2, trigonometrische-funktionen-e3-k1-s0-v3 – `Das Koordinatensystem zeigt die Wellen f und g.Kreuze an,was bei g anders ist als bei f.\\kreuz{die Höhe(a)}\kreuz{die B …`
- B-333 (5): trigonometrische-funktionen-e1-k1-s1-v1, trigonometrische-funktionen-e1-k1-s1-v2, trigonometrische-funktionen-e1-k1-s1-v3, trigonometrische-funktionen-e1-k1-s1-v4, trigonometrische-funktionen-e1-k1-s1-v5 – `Das Koordinatensystem zeigt den Einheitskreis.Zeichne auf dem Kreis den Punkt P zum Winkel #°ein.‖Grafik:\begin{ksys}[xm …`
- B-334 (3): symmetrie-abbildungen-e3-k1-s4-v1, symmetrie-abbildungen-e3-k1-s4-v2, symmetrie-abbildungen-e3-k1-s4-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und den Punkt Z.Drehe das Dreieck um Z um eine Vierteldrehung gegen den Uhrz …`
- B-335 (2): punkte-und-strecken-im-koordinatensystem-e1-k1-s4-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s4-v3 – `Ein Quader hat eine Ecke im Ursprung O und die Kanten # # und # entlang der x_#-,x_#-und x_#-Achse.P(#|#|#)liegt auf ein …`
- B-336 (3): winkel-dreiecke-e5-k1-s6-v1, winkel-dreiecke-e5-k1-s6-v2, winkel-dreiecke-e5-k1-s6-v3 – `Die Figur zeigt die Ecken eines Dreiecks ABC im Koordinatensystem.Zeichne das Dreieck und seine drei Seitenhalbierenden. …`
- B-337 (3): strahlensaetze-e2-k1-s9-v1, strahlensaetze-e2-k1-s9-v2, strahlensaetze-e2-k1-s9-v3 – `Die Grafik zeigt zwei ähnliche rechtwinklige Dreiecke.Miss in beiden Dreiecken die Kathete a und die Hypotenuse c.Berech …`
- B-338 (2): trigonometrische-funktionen-e3-k1-s8-v1, trigonometrische-funktionen-e3-k1-s8-v2 – `Das Koordinatensystem zeigt eine Welle.Stelle ihre Gleichung in der Form y=a·sin(b·x)auf.Bestimme erst die Amplitude,dan …`
- B-339 (5): extremalprobleme-e2-k1-s1-v1, extremalprobleme-e2-k1-s1-v2, extremalprobleme-e2-k1-s1-v3, extremalprobleme-e2-k1-s1-v4, extremalprobleme-e2-k1-s1-v5 – `An einer Mauer wird ein rechteckiges Beet an den drei übrigen Seiten mit # m Zaun eingefasst;a steht senkrecht zur Mauer …`
- B-340 (3): rationale-zahlen-e2-k3-s2-v1, rationale-zahlen-e2-k3-s2-v2, rationale-zahlen-e2-k3-s2-v3 – `Rechne-#+# nicht aus.Zeichne den Pfeil von-# um # nach rechts.Ist die Summe größer oder kleiner als null?Kreuze an und b …`
- B-341 (3): strahlensaetze-e2-k1-s7-v1, strahlensaetze-e2-k1-s7-v2, strahlensaetze-e2-k1-s7-v3 – `Dreieck ABC hat die Seiten #\text{cm},#\text{cm}und #\text{cm}.Dreieck DEF hat die Seiten #\text{cm},#\text{cm}und #\tex …`
- B-342 (2): extremalprobleme-e3-k1-s9-v3, extremalprobleme-e3-k1-s9-v4 – `Die Zielfunktion A(x)=-#x^#+x^#+#x beschreibt für #<x<# den Flächeninhalt eines Dreiecks unter einem Graphen.Bestimme di …`
- B-343 (2): trigonometrie-e3-k1-s19-v3, trigonometrie-e3-k1-s19-v4 – `Ein rechtwinkliges Trapez hat die senkrechten Seiten # cm und # cm.Die waagerechte Grundseite ist # cm lang.Der Winkel\a …`
- B-344 (2): punkte-und-strecken-im-koordinatensystem-e2-k1-s9-v5, punkte-und-strecken-im-koordinatensystem-e2-k1-s9-v6 – `Ein Ball fliegt vereinfacht geradlinig:Nach t Sekunden ist er in\vec x=(#|#|#)+t\cdot(#|#|-#)(# LE=# m,Boden ist die x_# …`
- B-345 (3): zuordnungen-e4-k2-s5-v1, zuordnungen-e4-k2-s5-v2, zuordnungen-e4-k2-s5-v3 – `Die Tabelle zeigt eine Zuordnung.Prüfe erst die Quotienten\frac{y}{x},dann die Produkte x·y.Kreuze an,welcher Zuordnungs …`
- B-346 (4): winkel-dreiecke-e1-k1-s0-v1, winkel-dreiecke-e1-k1-s0-v2, winkel-dreiecke-e1-k1-s0-v3, winkel-dreiecke-e1-k1-s0-v4 – `Die Figur zeigt den Winkel α.Du willst α mit dem Geodreieck messen.An jedem Strich stehen zwei Zahlen.Kreuze an,welche Z …`
- B-347 (2): trigonometrie-e1-k5-s1-v1, trigonometrie-e1-k5-s1-v3 – `In einem rechtwinkligen Dreieck ist ein Winkel #^\circ groß.Gemessen sind die Gegenkathete # cm und die Hypotenuse # cm. …`
- B-348 (3): kurvenuntersuchung-e4-k1-s1-v1, kurvenuntersuchung-e4-k1-s1-v3, kurvenuntersuchung-e4-k1-s1-v4 – `Die Abbildung zeigt den Graphen von f.Gib die Nullstellen von f'an und trage das Vorzeichen von f'in jedem Abschnitt daz …`
- B-349 (2): kurvenuntersuchung-e4-k1-s1-v2, kurvenuntersuchung-e4-k1-s1-v5 – `Die Abbildung zeigt den Graphen von f.Gib die Nullstellen von f'an und trage das Vorzeichen von f'in jedem Abschnitt daz …`
- B-350 (5): symmetrie-abbildungen-e3-k1-s1-v1, symmetrie-abbildungen-e3-k1-s1-v2, symmetrie-abbildungen-e3-k1-s1-v3, symmetrie-abbildungen-e3-k1-s1-v4, symmetrie-abbildungen-e3-k1-s1-v5 – `Im Koordinatensystem führt ein Verschiebungspfeil von P nach Q.Verschiebe das Dreieck ABC mit diesem Pfeil.‖Grafik:\begi …`
- B-351 (2): ableitung-und-aenderungsrate-e2-k1-s8-v1, ableitung-und-aenderungsrate-e2-k1-s8-v2 – `Die Abbildung zeigt den Graphen einer Funktion f.Beurteile die Aussage:„Für #\le x\le # ist die Steigung des Graphen kle …`
- B-352 (3): trigonometrie-e2-k1-s5-v1, trigonometrie-e2-k1-s5-v2, trigonometrie-e2-k1-s5-v3 – `Ein rechtwinkliges Dreieck hat die spitzen Winkel\alpha und\beta.Die Gegenkathete von\alpha ist # cm lang,die Hypotenuse …`
- B-353 (2): winkel-dreiecke-e2-k2-s4-v2, winkel-dreiecke-e2-k2-s4-v3 – `Die Geraden g und h schneiden sich.Zwischen ihnen liegt der Winkel\alpha=#^\circ.Eine dritte Gerade geht durch den Schni …`
- B-354 (2): flaecheninhalt-und-volumen-im-raum-e1-k3-s3-v1, flaecheninhalt-und-volumen-im-raum-e1-k3-s3-v3 – `Stelle für das Dreieck PQR im Koordinatensystem einen Flächenterm„Rechteck minus Randdreiecke“auf und berechne den Fläch …`
- B-355 (2): flaechen-e3-k1-s3-v1, flaechen-e3-k1-s3-v3 – `Die Figur zeigt ein stumpfwinkliges Dreieck mit der Grundseite # cm.Die Höhe zu dieser Seite liegt außerhalb des Dreieck …`
- B-356 (2): flaecheninhalt-und-volumen-im-raum-e3-k1-s6-v4, flaecheninhalt-und-volumen-im-raum-e3-k1-s6-v5 – `Die Grundfläche der Pyramide PQRS ist ein rechtwinkliges Dreieck PQR mit der Hypotenuse|PQ|=#\mathrm{cm}und der Kathete| …`
- B-357 (3): zuordnungen-e4-k2-s2-v1, zuordnungen-e4-k2-s2-v2, zuordnungen-e4-k2-s2-v3 – `Die Tabelle zeigt eine Zuordnung.Berechne für jedes Wertepaar das Produkt x·y.Kreuze dann an,ob die Zuordnung antipropor …`
- B-358 (3): symmetrie-abbildungen-e3-k1-s3-v1, symmetrie-abbildungen-e3-k1-s3-v2, symmetrie-abbildungen-e3-k1-s3-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und den Punkt Z.Drehe das Dreieck um Z um eine halbe Drehung.‖Grafik:\begin{ …`
- B-359 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s10-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s10-v2 – `Ein Quadrat liegt in der x_#x_#-Ebene;P(#|#|#)ist eine Ecke.Der Schnittpunkt seiner Diagonalen liegt auf der Geraden dur …`
- B-360 (5): zuordnungen-e4-k2-s1-v1, zuordnungen-e4-k2-s1-v2, zuordnungen-e4-k2-s1-v3, zuordnungen-e4-k2-s1-v4, zuordnungen-e4-k2-s1-v5 – `Die Tabelle zeigt eine Zuordnung.Berechne für jedes Wertepaar den Quotienten\frac{y}{x}.Kreuze dann an,ob die Zuordnung …`
- B-361 (3): winkel-dreiecke-e1-k3-s1-v1, winkel-dreiecke-e1-k3-s1-v2, winkel-dreiecke-e1-k3-s1-v3 – `Die Figur zeigt einen Winkel α.Vergleiche α ohne Messen mit einem rechten Winkel.Kreuze an,welcher Teil eines rechten Wi …`
- B-362 (2): lineare-funktionen-e2-k5-s4-v2, lineare-funktionen-e2-k5-s4-v3 – `Das Koordinatensystem zeigt die Gerade g.Lies ihre Steigung m ab.Gehe dazu nach rechts,bis die Gerade wieder durch eine …`
- B-363 (2): quadratische-funktionen-e3-k1-s7-v1, quadratische-funktionen-e3-k1-s7-v3 – `Das Koordinatensystem zeigt die Parabel f(x)=x^#-#x+#.Lies ihren Scheitel ab.Stelle damit die Scheitelpunktform auf.Prüf …`
- B-364 (5): zufallsexperimente-und-pfadregeln-e6-k1-s1-v1, zufallsexperimente-und-pfadregeln-e6-k1-s1-v2, zufallsexperimente-und-pfadregeln-e6-k1-s1-v3, zufallsexperimente-und-pfadregeln-e6-k1-s1-v4, zufallsexperimente-und-pfadregeln-e6-k1-s1-v5 – `#\%der Haushalte eines Orts haben einen Hund(H),die übrigen nicht(N).Unter den Hundehaltern haben #\%auch eine Katze(K), …`
- B-365 (2): zinsrechnung-e1-k1-s12-v5, zinsrechnung-e1-k1-s12-v6 – `Auf ein Sparbuch werden jedes Jahr #€eingezahlt.Die Tabelle zeigt das Guthaben.Weise nach,dass die Bank #\%Zinsen pro Ja …`
- B-366 (2): zuordnungen-e4-k2-s4-v1, zuordnungen-e4-k2-s4-v3 – `Der Graph zeigt eine Zuordnung.Kreuze an,zu welchem Zuordnungstyp sie gehört.\\kreuz{proportional}\\kreuz{antiproportion …`
- B-367 (2): normalverteilung-und-sigma-regeln-e2-k1-s5-v1, normalverteilung-und-sigma-regeln-e2-k1-s5-v2 – `Die Abbildung zeigt die Dichte von X mit dem Erwartungswert #.Jemand rechnet:P(#\le X\le #)\approx #\cdot #=# somit P(|X …`
- B-368 (4): flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v1, flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v2, flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v3, flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v4 – `Ein Quader hat die Grundfläche PQRU mit P(#|#|#),Q(#|#|#),R(#|#|#),U(#|#|#)und die Höhe #.Die Ebene durch Q,U und T(#|#| …`
- B-369 (2): koerper-e4-k2-s12-v1, koerper-e4-k2-s12-v2 – `Ergänze die fehlenden Größen der drei Zylinder(auf eine Stelle nach dem Komma runden).\Zylinder #:r=# cm,h=# cm;gesucht …`
- B-370 (2): winkel-dreiecke-e5-k1-s7-v1, winkel-dreiecke-e5-k1-s7-v2 – `Zeichne eine Strecke AB von # cm Länge.Zeichne darüber den Thaleskreis.Wähle einen Punkt C darauf und zeichne das Dreiec …`
- B-371 (3): winkel-dreiecke-e2-k2-s3-v1, winkel-dreiecke-e2-k2-s3-v2, winkel-dreiecke-e2-k2-s3-v3 – `Zwei Geraden kreuzen sich.Dabei entstehen die Winkel α,β,γ und δ.Es ist\alpha=#^\circ.Die Winkel β und δ liegen neben α, …`
- B-372 (3): strahlensaetze-e3-k3-s2-v1, strahlensaetze-e3-k3-s2-v2, strahlensaetze-e3-k3-s2-v3 – `Zeichne eine Strecke AB von #\text{cm}Länge.Teile sie mit einem Hilfsstrahl und einer Parallelen im Verhältnis #:#.Wie l …`
- B-373 (2): geraden-e3-k1-s6-v1, geraden-e3-k1-s6-v2 – `Gegeben sind g\colon\vec x=(#|#|#)+r\cdot(#|#|#)und die dazu echt parallele Gerade p\colon\vec x=(#|#|#)+r\cdot(#|#|#).E …`
- B-374 (3): symmetrie-abbildungen-e3-k1-s6-v1, symmetrie-abbildungen-e3-k1-s6-v2, symmetrie-abbildungen-e3-k1-s6-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und das Zentrum Z.Spiegle das Dreieck am Zentrum Z.‖Grafik:\begin{ksys}[xmin …`
- B-375 (2): uneigentliche-integrale-e2-k1-s2-v2, uneigentliche-integrale-e2-k1-s2-v3 – `Der Graph von f(x)=#e^{-#x}ist gezeichnet.Markiere die Restfläche zwischen x=# und einem großen w und begründe,warum sie …`
- B-376 (2): binomialverteilung-e5-k1-s8-v1, binomialverteilung-e5-k1-s8-v2 – `X ist binomialverteilt mit # Versuchen und der Trefferwahrscheinlichkeit #;die Verteilung ist symmetrisch.Es gilt P(X\ge …`
- B-377 (2): tangente-normale-schnittwinkel-e2-k1-s9-v1, tangente-normale-schnittwinkel-e2-k1-s9-v2 – `Ein Hügelprofil wird für-#\le x\le # durch f(x)=-\frac{#}{#}x^#+# beschrieben(# LE=# m).Eine Kamera steht im Punkt K(#|# …`
- B-378 (3): symmetrie-abbildungen-e2-k3-s6-v1, symmetrie-abbildungen-e2-k3-s6-v2, symmetrie-abbildungen-e2-k3-s6-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und die schräge Gerade a.Spiegle das Dreieck an a.‖Grafik:\begin{ksys}[xmin= …`
- B-379 (2): binomialverteilung-e5-k2-s1-v1, binomialverteilung-e5-k2-s1-v2 – `X ist binomialverteilt mit # Versuchen und der Trefferwahrscheinlichkeit #.In einem Diagramm sind die Säulen von # bis z …`
- B-380 (2): trigonometrie-e4-k1-s17-v5, trigonometrie-e4-k1-s17-v6 – `Von einer Plattform aus peilt man zwei Sichtlinien an.Im Dreieck ACD ist CD=# m.Der Winkel bei A zwischen den Sichtlinie …`
- B-381 (5): flaecheninhalt-durch-integration-e3-k1-s1-v1, flaecheninhalt-durch-integration-e3-k1-s1-v2, flaecheninhalt-durch-integration-e3-k1-s1-v3, flaecheninhalt-durch-integration-e3-k1-s1-v4, flaecheninhalt-durch-integration-e3-k1-s1-v5 – `Eine Fläche liegt über der x-Achse zwischen der y-Achse und der Geraden x=#.Oben wird sie für #\le x\le # vom Graphen vo …`
- B-382 (2): trigonometrie-e3-k1-s5-v1, trigonometrie-e3-k1-s5-v2 – `Im Parallelogramm ABCD ist BC=# cm.Der Punkt F liegt auf der Verlängerung von AB über B hinaus.Die Strecke CF steht senk …`
- B-383 (2): daten-e2-k1-s0-v1, daten-e2-k1-s0-v2 – `Die y-Achse(senkrechte Achse)eines Säulendiagramms ist mit # # # # # beschriftet.Kreuze an,ob die Achse bei null beginnt …`
- B-384 (3): symmetrie-abbildungen-e2-k3-s2-v1, symmetrie-abbildungen-e2-k3-s2-v2, symmetrie-abbildungen-e2-k3-s2-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und die Gerade a.Spiegle das Dreieck an a.‖Grafik:\begin{ksys}[xmin=#xmax=#y …`
- B-385 (3): symmetrie-abbildungen-e2-k3-s3-v1, symmetrie-abbildungen-e2-k3-s3-v2, symmetrie-abbildungen-e2-k3-s3-v3 – `Das Koordinatensystem zeigt das Dreieck ABC und die Gerade a.Spiegle das Dreieck an a.‖Grafik:\begin{ksys}[xmin=#xmax=#y …`
- B-386 (3): geraden-e4-k1-s3-v1, geraden-e4-k1-s3-v2, geraden-e4-k1-s3-v3 – `Ein Seil ist geradlinig zwischen zwei Masten gespannt;die Fußpunkte sind F_#(#|#|#)und F_#(#|#|#),befestigt ist es in # …`
- B-387 (2): trigonometrische-funktionen-e3-k1-s6-v1, trigonometrische-funktionen-e3-k1-s6-v3 – `Das Koordinatensystem zeigt den Graphen von y=sin(b·x).Lies die Periode ab.Berechne dann den Faktor b.‖Grafik:\begin{ksy …`
- B-388 (2): winkel-dreiecke-e2-k2-s8-v2, winkel-dreiecke-e2-k2-s8-v3 – `Im Dreieck ABC ist der Winkel bei C #^\circ groß.Die Seiten AB und CB werden über B hinaus verlängert.Zwischen den beide …`
- B-389 (2): brueche-dezimalzahlen-e2-k1-s8-v1, brueche-dezimalzahlen-e2-k1-s8-v2 – `Die Figur besteht aus gleich großen Kästchen.Einige Kästchen sind grau.Welcher Anteil der Fläche ist grau?Gib ihn als vo …`
- B-390 (2): einheiten-e4-k2-s4-v1, einheiten-e4-k2-s4-v2 – `Aus einer # m langen Latte werden zwei Leisten gesägt.Sie sind # und # Längeneinheiten lang.Eine Längeneinheit entsprich …`
- B-391 (3): flaecheninhalt-und-volumen-im-raum-e2-k1-s6-v5, flaecheninhalt-und-volumen-im-raum-e2-k1-s6-v6, flaecheninhalt-und-volumen-im-raum-e2-k1-s6-v7 – `Der Flächeninhalt des Vierecks PQRS mit P(#|#|#),Q(#|#|#),R(#|#|#),S(#|#|#)wird mit dem Term #\cdot #+\tfrac{#}{#}\cdot …`
- B-392 (5): symmetrie-abbildungen-e2-k3-s1-v1, symmetrie-abbildungen-e2-k3-s1-v2, symmetrie-abbildungen-e2-k3-s1-v3, symmetrie-abbildungen-e2-k3-s1-v4, symmetrie-abbildungen-e2-k3-s1-v5 – `Das Koordinatensystem zeigt den Punkt P und die Gerade a.Spiegle P an a.Zähle dazu die Kästchen bis zur Achse.‖Grafik:\b …`
- B-393 (2): orthogonalitaet-e2-k1-s3-v1, orthogonalitaet-e2-k1-s3-v2 – `Der Punkt Q liegt auf der Kante von A(#|#|#)nach D(#|#|#);außerdem sind R(#|#|#)und F(#|#|#)gegeben.Das Dreieck FQR soll …`
- B-394 (5): binomialverteilung-e4-k1-s1-v1, binomialverteilung-e4-k1-s1-v2, binomialverteilung-e4-k1-s1-v3, binomialverteilung-e4-k1-s1-v4, binomialverteilung-e4-k1-s1-v5 – `In #\%der Überraschungseier einer Sorte steckt eine Sonderfigur.Stelle den Ansatz auf:Wie viele Eier muss man öffnen,dam …`
- B-395 (3): zinsrechnung-e2-k1-s7-v1, zinsrechnung-e2-k1-s7-v2, zinsrechnung-e2-k1-s7-v3 – `Auf einem Konto liegen #€für # Jahre.Die Bank zahlt #\%Zinsen im Jahr.Rechne einmal mit einfachen Zinsen und einmal mit …`
- B-396 (2): linearkombination-und-lineare-abhaengigkeit-e2-k1-s0-v1, linearkombination-und-lineare-abhaengigkeit-e2-k1-s0-v3 – `\vec{OX}=#\cdot\vec{OA}+#\cdot\vec{OB}.Ergeben die Koeffizienten zusammen # und liegen beide zwischen # und #?\\kreuz{Su …`
- B-397 (2): quadratische-funktionen-basis-k1-v7, quadratische-funktionen-basis-k1-v10 – `Welche Wertetabelle gehört zu y=-#x^#?(P# # FOR)\\kreuz{A}\\kreuz{B}\\kreuz{C}‖Grafik:A:\wertetabelle[#,#]{x}{y}{-#-#,#} …`
- B-398 (2): pyramide-kegel-kugel-e1-k5-s10-v1, pyramide-kegel-kugel-e1-k5-s10-v2 – `Eine quadratische Pyramide hat die Grundkante a=# cm und die Seitenkante # cm.Berechne nacheinander die Seitenhöhe h_s,d …`
- B-399 (3): lineare-funktionen-e1-k1-s2-v1, lineare-funktionen-e1-k1-s2-v2, lineare-funktionen-e1-k1-s2-v3 – `Das Koordinatensystem zeigt den Graphen von y=#x.Lies den y-Wert bei x=# ab.Prüfe dein Ergebnis mit einer Rechnung.‖Graf …`
- B-400 (2): stammfunktion-und-hauptsatz-e3-k1-s1-v1, stammfunktion-und-hauptsatz-e3-k1-s1-v2 – `Das Bild zeigt den Graphen von f.Skizziere den Graphen der Stammfunktion F von f,die durch P(#|#)geht.‖Grafik:\begin{ksy …`
- B-401 (5): extremalprobleme-e1-k1-s1-v1, extremalprobleme-e1-k1-s1-v2, extremalprobleme-e1-k1-s1-v3, extremalprobleme-e1-k1-s1-v4, extremalprobleme-e1-k1-s1-v5 – `Der Punkt P(#|f(#))auf dem Graphen von f(x)=#-x^# ist eine Ecke eines Rechtecks;die gegenüberliegende Ecke liegt im Ursp …`
- B-402 (2): lineare-gleichungssysteme-e1-k1-s10-v1, lineare-gleichungssysteme-e1-k1-s10-v3 – `Finde die Lösung von I:x+y=# und II:#x+y=# durch Probieren.Setze in I nacheinander x=# # #\ldots ein und trage y in die …`
- B-403 (2): kenngroessen-von-verteilungen-e2-k7-s1-v2, kenngroessen-von-verteilungen-e2-k7-s1-v3 – `In einer Urne liegen vier Kugeln mit den Zahlen # # # und c.Zwei Kugeln werden ohne Zurücklegen gezogen;der Erwartungswe …`
- B-404 (5): ableitung-und-aenderungsrate-e4-k1-s1-v1, ableitung-und-aenderungsrate-e4-k1-s1-v2, ableitung-und-aenderungsrate-e4-k1-s1-v3, ableitung-und-aenderungsrate-e4-k1-s1-v4, ableitung-und-aenderungsrate-e4-k1-s1-v5 – `Die Zuflussrate in ein Becken wird durch r beschrieben(t in Stunden,r(t)in Litern je Stunde);es gilt r'(t)=(#-t)\cdot\ma …`
- B-405 (3): strahlensaetze-e3-k1-s9-v1, strahlensaetze-e3-k1-s9-v2, strahlensaetze-e3-k1-s9-v3 – `In einer V-Figur ist\overline{ZA}=#\text{cm},\overline{ZA'}=#\text{cm},\overline{ZB}=#\text{cm}und\overline{ZB'}=#\text{ …`
- B-406 (5): pythagoras-e3-k2-s1-v1, pythagoras-e3-k2-s1-v2, pythagoras-e3-k2-s1-v3, pythagoras-e3-k2-s1-v4, pythagoras-e3-k2-s1-v5 – `Die Figur zeigt ein gleichschenkliges Dreieck.Die Grundseite ist # cm lang,die Schenkel sind je # cm lang.Berechne die H …`
- B-407 (5): reelle-zahlen-e1-k1-s1-v1, reelle-zahlen-e1-k1-s1-v2, reelle-zahlen-e1-k1-s1-v3, reelle-zahlen-e1-k1-s1-v4, reelle-zahlen-e1-k1-s1-v5 – `Schreibe den Bruch\frac{#}{#}als Dezimalzahl.Benutze bei einer Periode den Periodenstrich.Kreuze dann an,ob die Dezimalz …`
- B-408 (3): lineare-funktionen-e2-k4-s4-v1, lineare-funktionen-e2-k4-s4-v2, lineare-funktionen-e2-k4-s4-v3 – `Zeichne die Gerade zu f(x)=#x+# in das Koordinatensystem.Markiere dazu n auf der y-Achse.Gehe von dort # nach rechts und …`
- B-409 (2): brueche-dezimalzahlen-basis-k1-v1, brueche-dezimalzahlen-basis-k1-v3 – `Bei welcher Figur ist genau\frac{#}{#}grau?(P# # FOR)\\kreuz{P}\\kreuz{Q}\\kreuz{R}\\kreuz{S}‖Grafik:P\bruchkreis[#]{#}{ …`
- B-410 (2): brueche-dezimalzahlen-basis-k1-v4, brueche-dezimalzahlen-basis-k1-v8 – `Bei welcher Figur ist genau\frac{#}{#}grau?(P# # FOR)\\kreuz{P}\\kreuz{Q}\\kreuz{R}\\kreuz{S}‖Grafik:P\kreissektor[#]{#} …`
- B-411 (2): binomialverteilung-e5-k1-s1-v1, binomialverteilung-e5-k1-s1-v3 – `Das Säulendiagramm zeigt die Verteilung der Anzahl X der Treffer bei # Versuchen(Werte gerundet).Lies P(X=#)ab.‖Grafik:\ …`
- B-412 (2): extremalprobleme-e3-k1-s3-v1, extremalprobleme-e3-k1-s3-v2 – `Die Zielfunktion A(x)=-#x^#+#x^#+#x beschreibt für #<x<# den Flächeninhalt eines Dreiecks.Bestimme die Extremstelle im I …`
- B-413 (4): symmetrie-abbildungen-e1-k1-s0-v1, symmetrie-abbildungen-e1-k1-s0-v2, symmetrie-abbildungen-e1-k1-s0-v3, symmetrie-abbildungen-e1-k1-s0-v4 – `Zeichne im Koordinatensystem den Weg vom Ursprung zu(#|#)mit zwei Pfeilen ein.Gehe erst nach rechts,dann nach oben.Setze …`
- B-414 (4): winkel-dreiecke-e1-k2-s0-v1, winkel-dreiecke-e1-k2-s0-v2, winkel-dreiecke-e1-k2-s0-v3, winkel-dreiecke-e1-k2-s0-v4 – `Die Figur zeigt einen Winkel α.Kreuze an,welche Winkelart α hat.Miss dabei nicht.\\kreuz{spitz}\\kreuz{recht}\\kreuz{stu …`
- B-415 (2): quadratische-funktionen-basis-k1-v2, quadratische-funktionen-basis-k1-v3 – `Welche Wertetabelle gehört zu y=#x^#?(P# # FOR)\\kreuz{A}\\kreuz{B}\\kreuz{C}‖Grafik:A:\wertetabelle[#,#]{x}{y}{-#-#,#}B …`
- B-416 (2): quadratische-funktionen-e1-k1-s7-v1, quadratische-funktionen-e1-k1-s7-v3 – `Kreuze an,wie die Parabel zu f(x)=-#x^# geöffnet ist.Kreuze auch an,ob sie schmaler oder breiter als die Normalparabel i …`
- B-417 (5): zufallsexperimente-und-pfadregeln-e3-k1-s1-v1, zufallsexperimente-und-pfadregeln-e3-k1-s1-v2, zufallsexperimente-und-pfadregeln-e3-k1-s1-v3, zufallsexperimente-und-pfadregeln-e3-k1-s1-v4, zufallsexperimente-und-pfadregeln-e3-k1-s1-v5 – `Ein Glücksrad zeigt Rot(R)mit #\%,sonst Blau(B).Es wird zweimal gedreht.Beschrifte den Baum.Wie groß ist die Wahrscheinl …`
- B-418 (5): kreis-basis-k1-v1, kreis-basis-k1-v3, kreis-basis-k1-v5, kreis-basis-k1-v7, kreis-basis-k1-v9 – `Im Bild ist ein Kreisausschnitt grau gefärbt.Der Mittelpunktswinkel des grauen Teils beträgt #^\circ.Wie viel Prozent de …`
- B-419 (4): brueche-dezimalzahlen-e3-k1-s0-v1, brueche-dezimalzahlen-e3-k1-s0-v2, brueche-dezimalzahlen-e3-k1-s0-v3, brueche-dezimalzahlen-e3-k1-s0-v4 – `Du willst\frac{#}{#}und\frac{#}{#}vergleichen.Kreuze den schnellsten Weg an.\\kreuz{gleicher Nenner}\\kreuz{gleicher Zäh …`
- B-420 (3): trigonometrie-e3-k1-s11-v1, trigonometrie-e3-k1-s11-v2, trigonometrie-e3-k1-s11-v3 – `Das Dreieck ADC hat bei D einen rechten Winkel.Der Punkt B liegt auf der Strecke DC.Es gilt\angle DAC=#^\circ und\angle …`
- B-421 (2): brueche-dezimalzahlen-e1-k1-s4-v1, brueche-dezimalzahlen-e1-k1-s4-v3 – `Die Grafik zeigt drei Figuren P,Q und R.Kreuze die Figur an,bei der\frac{#}{#}gefärbt ist.\\kreuz{P}\\kreuz{Q}\\kreuz{R} …`
- B-422 (2): trigonometrie-e3-k1-s14-v1, trigonometrie-e3-k1-s14-v2 – `Ein rechtwinkliges Dreieck hat den Winkel\alpha=#^\circ.Die Hypotenuse ist # cm lang.Berechne die Gegenkathete und die A …`
- B-423 (2): trigonometrie-e4-k1-s17-v1, trigonometrie-e4-k1-s17-v2 – `Eine Seilbahn führt von A über die Stütze B nach C.Die Strecke AB ist # m lang.Der Winkel bei A ist #^\circ groß.Der Win …`
- B-424 (3): strahlensaetze-e3-k3-s1-v1, strahlensaetze-e3-k3-s1-v2, strahlensaetze-e3-k3-s1-v3 – `Zeichne eine Strecke von #\text{cm}Länge.Teile sie mit einem Hilfsstrahl und Parallelen in # gleiche Teile.Wie lang ist …`
- B-425 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s6-v2, flaecheninhalt-und-volumen-im-raum-e1-k2-s6-v3 – `P(#|#|#),Q(#|#|#),R(#|#|#);für T gilt\overrightarrow{OT}=\overrightarrow{OR}-#\cdot\overrightarrow{PQ}.Bestimme T und da …`
- B-426 (2): lineare-funktionen-e2-k4-s3-v1, lineare-funktionen-e2-k4-s3-v3 – `Berechne zwei Punkte der Geraden f(x)=#x+#.Trage die Punkte in das Koordinatensystem ein.Zeichne die Gerade durch beide …`
- B-427 (2): trigonometrie-e3-k1-s4-v2, trigonometrie-e3-k1-s4-v3 – `Ein rechtwinkliges Trapez hat zwei senkrechte Seiten.Sie sind # m und # m lang.Sie stehen # m auseinander.Wie groß ist d …`
- B-428 (2): trigonometrie-e3-k1-s19-v7, trigonometrie-e3-k1-s19-v8 – `Im Parallelogramm ABCD ist die Höhe h=CF\approx # cm bekannt.Der Punkt F liegt auf der Verlängerung von AB.Der Winkel CA …`
- B-429 (3): koerper-e3-k1-s8-v1, koerper-e3-k1-s8-v2, koerper-e3-k1-s8-v3 – `Die Grundfläche eines Prismas ist ein Dreieck.Es hat einen rechten Winkel zwischen den Seiten # cm und # cm.Die lange Se …`
- B-430 (2): kreis-e3-k1-s6-v1, kreis-e3-k1-s6-v3 – `Ein Kreisausschnitt hat den Radius r=# cm und den Mittelpunktswinkel\alpha=#^\circ.Wie groß ist der Umfang des Ausschnit …`
- B-431 (2): ableitungsregeln-e1-k2-s9-v3, ableitungsregeln-e1-k2-s9-v4 – `Gegeben ist f(x)=x^#-#x^#+#x^#.Bestimme die ersten drei Ableitungen und entscheide mit Rechnung,an welcher der Stellen x …`
- B-432 (2): koerper-e4-k2-s14-v1, koerper-e4-k2-s14-v2 – `Zylinder A hat den Radius # cm und die Höhe # cm.Zylinder B hat den Radius # cm und die Höhe # cm.Wie viel Mal so groß i …`
- B-433 (2): schnittmengen-e3-k1-s3-v2, schnittmengen-e3-k1-s3-v3 – `Das ebene Viereck ABCD hat die Ecken A(#|#|#),B(#|#|#),C(#|#|#)und D(#|#|#).Die Ebene z=# schneidet das Viereck in einer …`
- B-434 (2): kenngroessen-von-verteilungen-e4-k1-s1-v1, kenngroessen-von-verteilungen-e4-k1-s1-v2 – `Das Diagramm zeigt die Verteilung einer binomialverteilten Zufallsgröße X mit n=#;der Erwartungswert von X ist ganzzahli …`
- B-435 (4): kurvenuntersuchung-e1-k1-s1-v1, kurvenuntersuchung-e1-k1-s1-v2, kurvenuntersuchung-e1-k1-s1-v4, kurvenuntersuchung-e1-k1-s1-v5 – `Gegeben ist die Ableitung f'(x)=#x-#.Bestimme das Vorzeichen von f'(x)auf dem Intervall[#;#]und kreuze an.\\kreuz{f stei …`
- B-436 (2): trigonometrie-e4-k1-s17-v7, trigonometrie-e4-k1-s17-v8 – `Ein Grundstück ABCD hat bei B einen rechten Winkel.Die Diagonale AC ist # m lang.Es gilt\angle BAC=#^\circ,\angle BCD=#^ …`
- B-437 (3): pyramide-kegel-kugel-e3-k1-s6-v1, pyramide-kegel-kugel-e3-k1-s6-v2, pyramide-kegel-kugel-e3-k1-s6-v3 – `Skizziere eine Kugel mit dem Radius # cm.Zeichne einen Kreis und den Äquator als flache Ellipse.Zeichne den Radius gestr …`
- B-438 (2): brueche-dezimalzahlen-e1-k1-s6-v5, brueche-dezimalzahlen-e1-k1-s6-v6 – `Die Figur besteht aus gleich großen Kästchen.Einige Kästchen sind grau.Welcher Anteil der Fläche ist grau?Gib ihn als Br …`
- B-439 (2): strahlensaetze-e2-k1-s11-v2, strahlensaetze-e2-k1-s11-v3 – `Ein Quadermodell ist #\text{cm}lang,#\text{cm}breit und #\text{cm}hoch.Es wird mit k=# vergrößert.Wie lang ist die längs …`
- B-440 (4): funktionsklassen-und-eigenschaften-e6-k1-s1-v2, funktionsklassen-und-eigenschaften-e6-k1-s1-v3, funktionsklassen-und-eigenschaften-e6-k1-s1-v4, funktionsklassen-und-eigenschaften-e6-k1-s1-v5 – `Fülle die Wertetabelle von f(x)=x^#-#x aus und übertrage die Punkte ins Koordinatensystem.‖Grafik:\wertetabelle{x}{f(x)} …`
- B-441 (5): binomialverteilung-e2-k1-s1-v1, binomialverteilung-e2-k1-s1-v2, binomialverteilung-e2-k1-s1-v3, binomialverteilung-e2-k1-s1-v4, binomialverteilung-e2-k1-s1-v5 – `Ein Glücksrad bleibt mit der Wahrscheinlichkeit # auf Blau stehen und wird #-mal gedreht;X ist die Anzahl der Drehungen …`
- B-442 (3): lineare-funktionen-e1-k1-s4-v1, lineare-funktionen-e1-k1-s4-v2, lineare-funktionen-e1-k1-s4-v3 – `Berechne die y-Werte zu y=\frac{#}{#}x für x=# # #.Zeichne dann die Gerade durch diese Punkte in das Koordinatensystem.‖ …`
- B-443 (3): trigonometrie-e3-k1-s6-v1, trigonometrie-e3-k1-s6-v2, trigonometrie-e3-k1-s6-v3 – `Im Parallelogramm ABCD geht die Höhe h von C auf die Verlängerung von AB.Sie ist # cm lang.Die Diagonale AC bildet mit A …`
- B-444 (2): lineare-funktionen-e3-k2-s7-v1, lineare-funktionen-e3-k2-s7-v2 – `Zeichne den Graphen der Funktion f mit f(x)=-#x+# in das Koordinatensystem.Berechne dann die Nullstelle von f.(P# # OS)‖ …`
- B-445 (2): hypothesentests-e1-k1-s3-v2, hypothesentests-e1-k1-s3-v3 – `Getestet wird H_#\colon p\le # mit # Versuchen auf dem Signifikanzniveau #\%;X ist die Trefferzahl.Bestimme die Grenze d …`
- B-446 (2): pythagoras-e2-k5-s1-v1, pythagoras-e2-k5-s1-v3 – `Ein pythagoreisches Tripel sind drei ganze Zahlen.Dabei ergeben die Quadrate der zwei kleineren Zahlen zusammen das Quad …`
- B-447 (2): symmetrie-abbildungen-e2-k3-s0-v1, symmetrie-abbildungen-e2-k3-s0-v2 – `Punkt P liegt # Kästchen links von der Achse.Sein Bildpunkt liegt # Kästchen rechts davon,beide auf gleicher Höhe.Kreuze …`
- B-448 (2): trigonometrische-funktionen-e3-k1-s3-v2, trigonometrische-funktionen-e3-k1-s3-v3 – `Das Koordinatensystem zeigt eine Welle.Lies ihre Amplitude am Graphen ab.‖Grafik:\begin{ksys}[xmin=#xmax=#ymin=-#ymax=#x …`
- B-449 (5): zufallsexperimente-und-pfadregeln-e8-k2-s1-v1, zufallsexperimente-und-pfadregeln-e8-k2-s1-v2, zufallsexperimente-und-pfadregeln-e8-k2-s1-v3, zufallsexperimente-und-pfadregeln-e8-k2-s1-v4, zufallsexperimente-und-pfadregeln-e8-k2-s1-v5 – `#\%der Kunden eines Geschäfts sind Frauen,unter ihnen sind #\%Stammkunden.Insgesamt sind #\%der Kunden Stammkunden.Wie g …`
- B-450 (4): lineare-funktionen-e1-k1-s0-v1, lineare-funktionen-e1-k1-s0-v2, lineare-funktionen-e1-k1-s0-v3, lineare-funktionen-e1-k1-s0-v4 – `Die Tabelle zeigt x-Werte und y-Werte.Jeder x-Wert wird mit demselben Faktor multipliziert.So entsteht der y-Wert.Wie gr …`
- B-451 (2): trigonometrie-e4-k1-s17-v9, trigonometrie-e4-k1-s17-v10 – `Im Dreieck DEF ist FE=# m.Der Winkel bei F ist #^\circ groß,der Winkel bei E ist #^\circ groß.Der Punkt P liegt auf DE,u …`
- B-452 (3): quadratische-gleichungen-e1-k3-s3-v1, quadratische-gleichungen-e1-k3-s3-v2, quadratische-gleichungen-e1-k3-s3-v3 – `Das Bild zeigt die Normalparabel y=x^#.Zeichne die Gerade y=# ein.Lies die Lösungen von x^#=# ab.‖Grafik:\begin{ksys}[xm …`
- B-453 (3): strahlensaetze-e3-k1-s2-v1, strahlensaetze-e3-k1-s2-v2, strahlensaetze-e3-k1-s2-v3 – `In der V-Figur ist\overline{ZA}=#\text{cm},\overline{ZA'}=#\text{cm}und\overline{AB}=#\text{cm}.Berechne die Länge der P …`
- B-454 (2): lineare-funktionen-e2-k5-s3-v1, lineare-funktionen-e2-k5-s3-v2 – `Das Koordinatensystem zeigt die Gerade g.Lies ihre Steigung m mit einem Steigungsdreieck ab.‖Grafik:\begin{ksys}[xmin=-# …`
- B-455 (5): reelle-zahlen-e3-k1-s1-v1, reelle-zahlen-e3-k1-s1-v2, reelle-zahlen-e3-k1-s1-v3, reelle-zahlen-e3-k1-s1-v4, reelle-zahlen-e3-k1-s1-v5 – `Berechne\sqrt{#\cdot #}auf zwei Wegen.Nimm zuerst mal und ziehe dann die Wurzel.Ziehe beim zweiten Weg die Wurzeln einze …`
- B-456 (3): winkel-dreiecke-e4-k1-s12-v3, winkel-dreiecke-e4-k1-s12-v4, winkel-dreiecke-e4-k1-s12-v5 – `Konstruiere das Dreieck ABC mit c=# cm,\alpha=#^\circ und\beta=#^\circ.Schreibe eine Konstruktionsbeschreibung dazu.Miss …`
- B-457 (3): zufallsgroessen-und-verteilungen-e2-k1-s0-v1, zufallsgroessen-und-verteilungen-e2-k1-s0-v2, zufallsgroessen-und-verteilungen-e2-k1-s0-v4 – `Kann das Diagramm die vollständige Verteilung einer Zufallsgröße zeigen?\kreuz{ja}\\kreuz{nein}‖Grafik:\saeulenab[ymax=# …`
- B-458 (2): lineare-funktionen-e2-k5-s2-v2, lineare-funktionen-e2-k5-s2-v3 – `Das Koordinatensystem zeigt die Gerade g.Lies ihre Steigung m mit einem Steigungsdreieck ab.‖Grafik:\begin{ksys}[xmin=-# …`
- B-459 (5): konfidenzintervalle-e2-k1-s1-v1, konfidenzintervalle-e2-k1-s1-v2, konfidenzintervalle-e2-k1-s1-v3, konfidenzintervalle-e2-k1-s1-v4, konfidenzintervalle-e2-k1-s1-v5 – `In einer Stichprobe vom Umfang # gibt es # Treffer.Berechne mit der Grenzgleichung die Grenzen des Konfidenzintervalls z …`
- B-460 (3): trigonometrie-e4-k1-s9-v1, trigonometrie-e4-k1-s9-v2, trigonometrie-e4-k1-s9-v3 – `Das Viereck ABCD hat bei B einen rechten Winkel.Die Diagonale AC ist # m lang.Es gilt\angle BAC=#^\circ,\angle BCD=#^\ci …`
- B-461 (2): winkel-dreiecke-basis-k4-v3, winkel-dreiecke-basis-k4-v7 – `Ein Parallelogramm hat links unten einen Winkel von #^\circ.Wie groß ist der Winkel\gamma rechts oben?(P# # FOR)‖Grafik: …`
- B-462 (4): winkel-dreiecke-basis-k4-v1, winkel-dreiecke-basis-k4-v4, winkel-dreiecke-basis-k4-v6, winkel-dreiecke-basis-k4-v9 – `Ein Parallelogramm hat links unten einen Winkel von #^\circ.Wie groß ist der Winkel\beta rechts unten?(P# # FOR)‖Grafik: …`
- B-463 (2): winkel-dreiecke-basis-k4-v2, winkel-dreiecke-basis-k4-v8 – `Ein Parallelogramm hat links unten einen Winkel von #^\circ.Wie groß ist der Winkel\delta links oben?(P# # FOR)‖Grafik:\ …`
- B-464 (2): kreis-e3-k1-s4-v1, kreis-e3-k1-s4-v3 – `Ein Kreisausschnitt hat den Radius r=# cm und den Mittelpunktswinkel\alpha=#^\circ.Wie lang ist sein Bogen b?Rechne mit …`
- B-465 (2): kreis-e3-k1-s5-v1, kreis-e3-k1-s5-v3 – `Ein Kreisausschnitt hat den Radius r=# cm und den Mittelpunktswinkel\alpha=#^\circ.Wie groß ist seine Fläche?Rechne mit …`
- B-466 (2): quadratische-gleichungen-e2-k1-s0-v1, quadratische-gleichungen-e2-k1-s0-v3 – `Der Satz vom Nullprodukt sagt:Ein Produkt ist null,wenn ein Faktor null ist.Kreuze an,ob der Satz für die Gleichung(x-#) …`
- B-467 (2): quadratische-gleichungen-e3-k6-s3-v1, quadratische-gleichungen-e3-k6-s3-v3 – `Das Bild zeigt die Parabel y=x^#-#x+#.Lies am Graphen die Lösungen von x^#-#x+#=# ab.‖Grafik:\begin{ksys}[xmin=-#xmax=#y …`
- B-468 (3): rationale-zahlen-e1-k1-s0-v1, rationale-zahlen-e1-k1-s0-v2, rationale-zahlen-e1-k1-s0-v3 – `Auf der Zahlengeraden steht schon die Null.Von Strich zu Strich wächst die Zahl um #.Schreibe an jeden Strich seine Zahl …`
- B-469 (2): symmetrie-abbildungen-e3-k1-s5-v1, symmetrie-abbildungen-e3-k1-s5-v2 – `Das Koordinatensystem zeigt den Punkt P und das Zentrum Z.Spiegle P am Zentrum Z.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin= …`
- B-470 (4): orthogonalitaet-e4-k1-s1-v1, orthogonalitaet-e4-k1-s1-v2, orthogonalitaet-e4-k1-s1-v3, orthogonalitaet-e4-k1-s1-v4 – `Gegeben sind P(#|#|#)und g\colon\vec x=(#|#|#)+\lambda\cdot(#|#|#).Bestimme den Punkt F von g,der P am nächsten liegt,un …`
- B-471 (3): zinsrechnung-e1-k1-s7-v1, zinsrechnung-e1-k1-s7-v2, zinsrechnung-e1-k1-s7-v3 – `Weise mit der Tabelle nach,dass die Bank #\%Zinsen im Jahr zahlt.‖Grafik:\sachtabelle{lrrr}{Buchung&Einzahlung&Zinsen&Gu …`
- B-472 (2): lineare-funktionen-e1-k1-s5-v1, lineare-funktionen-e1-k1-s5-v2 – `Berechne die y-Werte zu y=-#x für x=# # #.Zeichne dann die Gerade durch diese Punkte in das Koordinatensystem.‖Grafik:\b …`
- B-473 (2): pythagoras-e3-k2-s4-v2, pythagoras-e3-k2-s4-v3 – `In einem Parallelogramm ist die schräge Seite # cm lang.Der Fußpunkt der Höhe liegt auf der Verlängerung der Grundseite. …`
- B-474 (4): kreis-e3-k1-s0-v1, kreis-e3-k1-s0-v2, kreis-e3-k1-s0-v3, kreis-e3-k1-s0-v4 – `Im Bild ist ein Teil des Kreises grau.Kreuze an,welcher Teil des Kreises das ist.\\kreuz{\frac{#}{#}}\\kreuz{\frac{#}{#} …`
- B-475 (3): flaecheninhalt-durch-integration-e4-k1-s2-v1, flaecheninhalt-durch-integration-e4-k1-s2-v2, flaecheninhalt-durch-integration-e4-k1-s2-v3 – `Eine Fläche liegt über der x-Achse rechts der y-Achse:bis x=# unter der Geraden y=# danach unter der Strecke von(#|#)zum …`
- B-476 (2): lineare-gleichungssysteme-e3-k1-s11-v1, lineare-gleichungssysteme-e3-k1-s11-v2 – `Löse das Gleichungssystem I:#x+#y=# und II:#x-#y=-# mit dem Additionsverfahren.Mache die Probe in beiden Gleichungen.Beg …`
- B-477 (2): symmetrie-abbildungen-e1-k2-s6-v1, symmetrie-abbildungen-e1-k2-s6-v2 – `Trage A(#|#),B(#|#),C(#|#),D(#|#)in das Koordinatensystem ein.Verbinde sie der Reihe nach.Wie heißt die Figur?‖Grafik:\b …`
- B-478 (2): trigonometrie-e3-k1-s19-v9, trigonometrie-e3-k1-s19-v10 – `Im Dreieck ABC ist AD die Höhe auf BC.Der Punkt D liegt zwischen B und C,und es gilt AD=# m.Außerdem ist\angle ACD=#^\ci …`
- B-479 (3): pyramide-kegel-kugel-e2-k2-s9-v1, pyramide-kegel-kugel-e2-k2-s9-v2, pyramide-kegel-kugel-e2-k2-s9-v3 – `Ein Kegel hat den Radius # cm und die Höhe # cm.Skizziere sein Schrägbild.Zeichne die Höhe gestrichelt ein.Beschrifte de …`
- B-480 (3): trigonometrie-e2-k1-s3-v1, trigonometrie-e2-k1-s3-v2, trigonometrie-e2-k1-s3-v3 – `Ein rechtwinkliges Dreieck hat den spitzen Winkel\alpha.Die Gegenkathete von\alpha ist # cm lang.Die Ankathete von\alpha …`
- B-481 (2): lineare-funktionen-e1-k1-s6-v1, lineare-funktionen-e1-k1-s6-v2 – `Die Tabelle zeigt eine Zuordnung.Entscheide mit den Quotienten\frac{y}{x},ob sie proportional ist.Wenn ja,gib ihre Gleic …`
- B-482 (2): trigonometrische-funktionen-e1-k1-s5-v2, trigonometrische-funktionen-e1-k1-s5-v3 – `Am Einheitskreis im Bild wurde cos #°≈# abgelesen.Prüfe den Wert mit dem Taschenrechner im Grad-Modus.Runde auf zwei Ste …`
- B-483 (5): pythagoras-e2-k4-s1-v1, pythagoras-e2-k4-s1-v2, pythagoras-e2-k4-s1-v3, pythagoras-e2-k4-s1-v4, pythagoras-e2-k4-s1-v5 – `Im Dreieck ABC liegt bei C ein rechter Winkel.Die Höhe h auf die Hypotenuse teilt sie in die Abschnitte p=# cm und q=# c …`
- B-484 (2): kurvenuntersuchung-e3-k2-s9-v1, kurvenuntersuchung-e3-k2-s9-v2 – `Der Graph von f(x)=#x^#-x^#+#x ist punktsymmetrisch zum Ursprung.Weise nach,dass W(#|#)ein Wendepunkt ist,und gib ohne w …`
- B-485 (3): lineare-funktionen-e2-k4-s6-v1, lineare-funktionen-e2-k4-s6-v2, lineare-funktionen-e2-k4-s6-v3 – `Zeichne die Gerade zu f(x)=\frac{#}{#}x+# in das Koordinatensystem.Nutze dazu n und ein Steigungsdreieck.‖Grafik:\begin{ …`
- B-486 (3): punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v2, punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v3 – `Dreieck OPQ mit dem Ursprung O,P(#|#|#)und Q(#|#|#).Gib einen Punkt T\ne P an,sodass das Dreieck OTQ denselben Flächenin …`
- B-487 (2): quadratische-funktionen-e1-k1-s5-v1, quadratische-funktionen-e1-k1-s5-v3 – `Fülle die Wertetabelle zu g(x)=x^#+# aus.\wertetabelle{x}{g(x)}{-#-#,#}Vergleiche mit f(x)=x^#:Um wie viel unterscheidet …`
- B-488 (3): reelle-zahlen-e1-k1-s5-v1, reelle-zahlen-e1-k1-s5-v2, reelle-zahlen-e1-k1-s5-v3 – `Markiere\sqrt{#}auf dem Zahlenstrahl.Zwischen welchen zwei Zahlen mit einer Stelle nach dem Komma liegt\sqrt{#}?‖Grafik: …`
- B-489 (3): flaechen-e2-k1-s0-v1, flaechen-e2-k1-s0-v2, flaechen-e2-k1-s0-v4 – `Die Figur zeigt ein Parallelogramm mit der Grundseite g.Zeichne die Höhe zu g ein und markiere den rechten Winkel.‖Grafi …`
- B-490 (3): koerper-e3-k1-s4-v1, koerper-e3-k1-s4-v2, koerper-e3-k1-s4-v3 – `Die Grundfläche eines Prismas ist ein Trapez.Seine parallelen Seiten sind # cm und # cm lang,ihr Abstand ist # cm.Das Pr …`
- B-491 (2): pythagoras-e2-k4-s2-v1, pythagoras-e2-k4-s2-v3 – `Im Dreieck ABC liegt bei C ein rechter Winkel.Die Hypotenuse ist c=# cm lang,der an a anliegende Hypotenusenabschnitt is …`
- B-492 (2): pythagoras-e3-k2-s5-v1, pythagoras-e3-k2-s5-v3 – `Das Dreieck ABC hat bei B einen stumpfen Winkel.Die Höhe von C trifft die Verlängerung von AB im Punkt D.Es gilt CD=# cm …`
- B-493 (2): lineare-funktionen-e4-k2-s1-v1, lineare-funktionen-e4-k2-s1-v3 – `Trage die Punkte A(-#|-#)und B(#|#)in das Koordinatensystem ein.Zeichne die Gerade durch beide Punkte.‖Grafik:\begin{ksy …`
- B-494 (2): orthogonalitaet-e2-k1-s6-v2, orthogonalitaet-e2-k1-s6-v3 – `Gegeben sind A(#|#|#),B(#|#|#)und C(#|#|#).Der Punkt T liegt auf der Strecke AC so,dass das Dreieck ABT bei B rechtwinkl …`
- B-495 (3): strahlensaetze-e2-k1-s6-v1, strahlensaetze-e2-k1-s6-v2, strahlensaetze-e2-k1-s6-v3 – `Dreieck # hat die Winkel #^\circ und #^\circ.Dreieck # hat die Winkel #^\circ und #^\circ.Kreuze an,ob die beiden Dreiec …`
- B-496 (2): normalverteilung-und-sigma-regeln-e1-k1-s2-v1, normalverteilung-und-sigma-regeln-e1-k1-s2-v2 – `Die Abbildung zeigt die Dichte einer normalverteilten Zufallsgröße X mit dem Erwartungswert #.Wie groß ist P(X=#)?(Abitu …`
- B-497 (2): lineare-funktionen-basis-k4-v4, lineare-funktionen-basis-k4-v8 – `Schnittpunkt mit der y-Achse:Markiere ihn an der Geraden y=-#x-#.(P# # OS)‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax= …`
- B-498 (2): lineare-funktionen-e2-k5-s1-v3, lineare-funktionen-e2-k5-s1-v4 – `Das Koordinatensystem zeigt die Gerade g.Lies ihren y-Achsenabschnitt n ab.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax …`
- B-499 (5): ableitung-und-aenderungsrate-e1-k1-s1-v1, ableitung-und-aenderungsrate-e1-k1-s1-v2, ableitung-und-aenderungsrate-e1-k1-s1-v3, ableitung-und-aenderungsrate-e1-k1-s1-v4, ableitung-und-aenderungsrate-e1-k1-s1-v5 – `Zu Beginn einer Messung sind # Liter Wasser in einem Becken,# Stunden später # Liter.Berechne die mittlere Änderungsrate …`
- B-500 (5): trigonometrie-e2-k1-s1-v1, trigonometrie-e2-k1-s1-v2, trigonometrie-e2-k1-s1-v3, trigonometrie-e2-k1-s1-v4, trigonometrie-e2-k1-s1-v5 – `Ein rechtwinkliges Dreieck hat den spitzen Winkel\alpha.Die Gegenkathete von\alpha ist # cm lang.Die Hypotenuse ist # cm …`
- B-501 (3): winkel-dreiecke-e5-k1-s3-v1, winkel-dreiecke-e5-k1-s3-v2, winkel-dreiecke-e5-k1-s3-v3 – `Die Figur zeigt einen Winkel α.Konstruiere mit dem Zirkel die Winkelhalbierende von α.Wie groß ist jeder der beiden Teil …`
- B-502 (3): zinsrechnung-e2-k1-s2-v1, zinsrechnung-e2-k1-s2-v2, zinsrechnung-e2-k1-s2-v3 – `Auf einem Konto liegen #€.Die Bank zahlt #\%Zinsen im Jahr.Die Zinsen bleiben auf dem Konto.Rechne Jahr für Jahr,wie hoc …`
- B-503 (2): binomische-formeln-e3-k1-s2-v1, binomische-formeln-e3-k1-s2-v2 – `Im Term x^#+#x+# sind x^# und # Quadrate.Schreibe ihre Wurzeln auf,bilde das doppelte Produkt und vergleiche es mit dem …`
- B-504 (2): terme-e6-k2-s1-v1, terme-e6-k2-s1-v3 – `Erfinde eine Situation aus dem Alltag,zu der der Term #+#x passt.Schreibe auf,wofür x steht.Berechne den Term für x=# un …`
- B-505 (2): spiegelung-e2-k1-s4-v1, spiegelung-e2-k1-s4-v2 – `Zwei Flächen eines Körpers liegen symmetrisch zu einer Ebene H;W(#|#|#)ist das Spiegelbild von C(#|#|#),U(#|#|#)liegt au …`
- B-506 (2): strahlensaetze-e2-k1-s8-v2, strahlensaetze-e2-k1-s8-v3 – `Die Dreiecke ABC und DEF sind ähnlich.Die Seite AB gehört zur Seite DE.Es ist AB=#\text{cm},DE=#\text{cm}und AC=#\text{c …`
- B-507 (2): tangente-normale-schnittwinkel-e1-k1-s10-v1, tangente-normale-schnittwinkel-e1-k1-s10-v7 – `Für a># ist f_a(x)=a\cdot x^#.Weise nach,dass die Tangente an den Graphen von f_a im Punkt(u|f_a(u))die y-Achse im Punkt …`
- B-508 (3): lineare-funktionen-basis-k4-v1, lineare-funktionen-basis-k4-v3, lineare-funktionen-basis-k4-v9 – `Schnittpunkt mit der y-Achse:Markiere ihn an der Geraden y=#x+#.(P# # OS)‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=# …`
- B-509 (3): koerper-e4-k2-s8-v1, koerper-e4-k2-s8-v2, koerper-e4-k2-s8-v3 – `Ein Zylinder hat den Radius # cm und die Höhe # cm.Kreuze an,welches Rechteck zu seinem Netz gehört.\\kreuz{# cm×# cm}\\ …`
- B-510 (2): lineare-funktionen-e2-k4-s5-v1, lineare-funktionen-e2-k4-s5-v3 – `Zeichne die Gerade zu f(x)=-#x+# in das Koordinatensystem.Nutze dazu n und ein Steigungsdreieck.‖Grafik:\begin{ksys}[xmi …`
- B-511 (3): strahlensaetze-e2-k1-s4-v1, strahlensaetze-e2-k1-s4-v2, strahlensaetze-e2-k1-s4-v3 – `Die Strecke\overline{AB}ist #\text{cm}lang.Sie wird zentrisch gestreckt.Die Bildstrecke\overline{A'B'}ist #\text{cm}lang …`
- B-512 (3): trigonometrie-e2-k1-s2-v1, trigonometrie-e2-k1-s2-v2, trigonometrie-e2-k1-s2-v3 – `Ein rechtwinkliges Dreieck hat den spitzen Winkel\alpha.Die Ankathete von\alpha ist # cm lang.Die Hypotenuse ist # cm la …`
- B-513 (3): trigonometrische-funktionen-e1-k1-s2-v1, trigonometrische-funktionen-e1-k1-s2-v2, trigonometrische-funktionen-e1-k1-s2-v3 – `Das Bild zeigt einen Punkt P auf dem Einheitskreis.Miss den Winkel\alpha zum Punkt P.Beginne an der positiven Rechtsachs …`
- B-514 (2): lineare-funktionen-e2-k4-s7-v1, lineare-funktionen-e2-k4-s7-v2 – `Zeichne die Gerade zu f(x)=#x-# in das Koordinatensystem.Nutze dazu n und ein Steigungsdreieck.‖Grafik:\begin{ksys}[xmin …`
- B-515 (2): pythagoras-e3-k2-s6-v2, pythagoras-e3-k2-s6-v3 – `Die Figur zeigt eine Raute mit ihren Diagonalen.Die Diagonalen sind # cm und # cm lang.Wie lang ist eine Seite der Raute …`
- B-516 (2): binomialverteilung-e5-k1-s7-v1, binomialverteilung-e5-k1-s7-v2 – `X ist binomialverteilt mit # Versuchen und der Trefferwahrscheinlichkeit #;es gilt P(X\le #)\approx #.Bestimme ohne Rech …`
- B-517 (2): lineare-funktionen-e4-k1-s1-v1, lineare-funktionen-e4-k1-s1-v5 – `Das Koordinatensystem zeigt die Gerade g.Bestimme die Gleichung von g.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#abl …`
- B-518 (2): pythagoras-e2-k3-s2-v1, pythagoras-e2-k3-s2-v3 – `In einem rechtwinkligen Dreieck ist c=# cm die Hypotenuse und b=# cm eine Kathete.Berechne die Länge der Kathete a.Runde …`
- B-519 (3): rekonstruktion-von-funktionsgleichungen-e3-k1-s1-v1, rekonstruktion-von-funktionsgleichungen-e3-k1-s1-v2, rekonstruktion-von-funktionsgleichungen-e3-k1-s1-v3 – `Der Graph von f mit f(x)=a\cdot\mathrm{sin}(b\cdot x)und a,b># hat die direkt aufeinanderfolgenden Extrempunkte E_#(#|#) …`
- B-520 (2): ebenen-e1-k1-s5-v2, ebenen-e1-k1-s5-v3 – `Beschreiben E_#\colon\vec x=(#|#|#)+r\cdot(#|#|#)+s\cdot(#|#|#)und E_#\colon\vec x=(#|#|#)+r\cdot(#|#|#)+s\cdot(#|#|#),r …`
- B-521 (2): flaechen-e3-k1-s0-v1, flaechen-e3-k1-s0-v4 – `Die Figur zeigt ein Dreieck mit der Grundseite g.Zeichne die Höhe zu g ein und markiere den rechten Winkel.‖Grafik:\drei …`
- B-522 (5): ableitung-und-aenderungsrate-e2-k1-s1-v1, ableitung-und-aenderungsrate-e2-k1-s1-v2, ableitung-und-aenderungsrate-e2-k1-s1-v3, ableitung-und-aenderungsrate-e2-k1-s1-v4, ableitung-und-aenderungsrate-e2-k1-s1-v5 – `Der Wasserstand in einem Hafenbecken wird durch w(t)=t^#-#t^#+#t+# beschrieben(t in Stunden,w(t)in cm).Berechne w'(#)und …`
- B-523 (5): strahlensaetze-e3-k1-s1-v1, strahlensaetze-e3-k1-s1-v2, strahlensaetze-e3-k1-s1-v3, strahlensaetze-e3-k1-s1-v4, strahlensaetze-e3-k1-s1-v5 – `In der V-Figur ist\overline{ZA}=#\text{cm},\overline{ZA'}=#\text{cm}und\overline{ZB}=#\text{cm}.Berechne\overline{ZB'}.‖ …`
- B-524 (3): zinsrechnung-e1-k1-s8-v1, zinsrechnung-e1-k1-s8-v2, zinsrechnung-e1-k1-s8-v3 – `Auf einem Konto liegen #€.Die Bank zahlt #\%Zinsen im Jahr.Die Zinsen werden jedes Jahr ausgezahlt.Wie viel Euro Zinsen …`
- B-525 (2): flaechen-e3-k2-s1-v1, flaechen-e3-k2-s1-v3 – `Im Dreieck ABC ist AB=# cm und BC=# cm.Die Höhe auf AB ist # cm.Die Höhe auf BC ist # cm.Berechne die Fläche mit der Sei …`
- B-526 (2): punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v3, punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v4 – `A(#|#|#)und M(#|#|#).Gib zwei Punkte B und C an,sodass A,B und C denselben Abstand zu M haben und ein gleichschenkliges …`
- B-527 (3): koerper-e3-k1-s3-v1, koerper-e3-k1-s3-v2, koerper-e3-k1-s3-v3 – `Die Grundfläche eines Prismas ist ein Dreieck.Das Dreieck hat die Grundseite # cm und die Höhe # cm.Das Prisma ist # cm …`
- B-528 (2): zufallsexperimente-und-pfadregeln-e5-k1-s1-v4, zufallsexperimente-und-pfadregeln-e5-k1-s1-v5 – `Eine Urne enthält # Kugeln,# davon sind rot.Es wird dreimal ohne Zurücklegen gezogen.Wie groß ist die Wahrscheinlichkeit …`
- B-529 (3): zufallsexperimente-und-pfadregeln-e5-k1-s1-v1, zufallsexperimente-und-pfadregeln-e5-k1-s1-v2, zufallsexperimente-und-pfadregeln-e5-k1-s1-v3 – `Eine Urne enthält # Kugeln,# davon sind rot.Es wird dreimal mit Zurücklegen gezogen.Wie groß ist die Wahrscheinlichkeit …`
- B-530 (2): funktionsklassen-und-eigenschaften-e5-k1-s0-v1, funktionsklassen-und-eigenschaften-e5-k1-s0-v3 – `Gegeben ist g(x)=f(#x+#).Klammere im Argument den Faktor vor x aus und gib an,um wie viel der Graph in x-Richtung versch …`
- B-531 (2): funktionsklassen-und-eigenschaften-e5-k1-s0-v2, funktionsklassen-und-eigenschaften-e5-k1-s0-v4 – `Gegeben ist g(x)=f(#x-#).Klammere im Argument den Faktor vor x aus und gib an,um wie viel der Graph in x-Richtung versch …`
- B-532 (2): pythagoras-e2-k3-s4-v2, pythagoras-e2-k3-s4-v3 – `In einem rechtwinkligen Dreieck ist c=# m die Hypotenuse und b=# m eine Kathete.Berechne die Länge der Kathete a.Prüfe d …`
- B-533 (3): bruchrechnung-e1-k3-s5-v1, bruchrechnung-e1-k3-s5-v2, bruchrechnung-e1-k3-s5-v3 – `Gegeben sind\frac{#}{#}und\frac{#}{#}.Gib den Hauptnenner an und die Zahl,mit der du jeden der beiden Brüche erweitern m …`
- B-534 (2): kurvenuntersuchung-e4-k3-s1-v1, kurvenuntersuchung-e4-k3-s1-v3 – `Gegeben ist f(x)=#\cdot\mathrm{e}^{#x}.Weise nach,dass g(x)=\mathrm{ln}(f(x))eine lineare Funktion ist,und gib Steigung …`
- B-535 (2): pyramide-kegel-kugel-e1-k5-s6-v1, pyramide-kegel-kugel-e1-k5-s6-v3 – `Eine Pyramide hat ein Quadrat als Grundfläche.Die Grundkante ist # cm lang,die Seitenhöhe ist # cm.Berechne den Flächeni …`
- B-536 (3): trigonometrie-e4-k1-s11-v1, trigonometrie-e4-k1-s11-v2, trigonometrie-e4-k1-s11-v3 – `Im Dreieck ABC ist a=# cm,\alpha=#^\circ und\beta=#^\circ.Berechne b mit dem Sinussatz.Berechne b dann noch einmal über …`
- B-537 (4): potenz-exponentialfunktionen-e2-k2-s0-v1, potenz-exponentialfunktionen-e2-k2-s0-v2, potenz-exponentialfunktionen-e2-k2-s0-v3, potenz-exponentialfunktionen-e2-k2-s0-v4 – `Die Tabelle zeigt Werte.Kreuze an,was von Wert zu Wert gleich bleibt.\wertetabelle[#,#]{t}{Wert}{#,#}\kreuz{die Differen …`
- B-538 (2): potenzen-wurzeln-e2-k1-s0-v3, potenzen-wurzeln-e2-k1-s0-v4 – `Die Zahl # soll in Zehnerpotenzschreibweise stehen.Kreuze an,ob das Komma so viele Stellen wandert,wie Nullen dastehen.\ …`
- B-539 (4): bruchrechnung-e1-k3-s0-v1, bruchrechnung-e1-k3-s0-v2, bruchrechnung-e1-k3-s0-v3, bruchrechnung-e1-k3-s0-v4 – `Färbe am Streifen zuerst\frac{#}{#}.Färbe dann noch\frac{#}{#}dazu.Welcher Anteil des Streifens ist jetzt gefärbt?‖Grafi …`
- B-540 (3): zinsrechnung-e1-k1-s2-v1, zinsrechnung-e1-k1-s2-v2, zinsrechnung-e1-k1-s2-v3 – `Auf einem Konto liegen #€.Die Bank zahlt #\%Zinsen im Jahr.Wie viel Euro Zinsen gibt es in einem Jahr?Rechne zuerst aus, …`
- B-541 (2): pythagoras-e3-k2-s11-v1, pythagoras-e3-k2-s11-v3 – `Die Figur zeigt einen Kegel.Sein Durchmesser ist # cm,seine Höhe ist # cm.Berechne die Länge der Mantellinie s.‖Grafik:\ …`
- B-542 (5): trigonometrie-e3-k1-s1-v1, trigonometrie-e3-k1-s1-v2, trigonometrie-e3-k1-s1-v3, trigonometrie-e3-k1-s1-v4, trigonometrie-e3-k1-s1-v5 – `Ein Dreieck ist gleichschenklig.Seine Schenkel sind # cm lang.Seine Basiswinkel sind #^\circ groß.Wie lang ist die Höhe …`
- B-543 (5): zinsrechnung-e2-k1-s1-v1, zinsrechnung-e2-k1-s1-v2, zinsrechnung-e2-k1-s1-v3, zinsrechnung-e2-k1-s1-v4, zinsrechnung-e2-k1-s1-v5 – `Auf einem Konto liegen #€.Die Bank zahlt #\%Zinsen im Jahr.Am Jahresende kommen die Zinsen auf das Konto.Wie hoch ist da …`
- B-544 (3): abstaende-e2-k2-s0-v1, abstaende-e2-k2-s0-v3, abstaende-e2-k2-s0-v4 – `Welchen Abstand hat der Ursprung von der Ebene E\colon #x-y+#z=#?Teile nur den Betrag der rechten Seite durch den Betrag …`
- B-545 (3): lineare-funktionen-e2-k4-s8-v3, lineare-funktionen-e2-k4-s8-v4, lineare-funktionen-e2-k4-s8-v8 – `Zeichne den Graphen der Funktion f mit f(x)=#x-# in das Koordinatensystem.(P# # OS)‖Grafik:\begin{ksys}[xmin=-#xmax=#ymi …`
- B-546 (2): pythagoras-e1-k2-s3-v1, pythagoras-e1-k2-s3-v3 – `In einem rechtwinkligen Dreieck sind a=# cm und b=# cm die Katheten.Berechne die Länge der Hypotenuse c.Runde auf eine S …`
- B-547 (2): konfidenzintervalle-e2-k1-s2-v1, konfidenzintervalle-e2-k1-s2-v3 – `Die untere Grenze eines Konfidenzintervalls zur Sicherheitswahrscheinlichkeit #\%ist # der Umfang #.Bestimme die Treffer …`
- B-548 (2): binomialverteilung-e5-k1-s8-v3, binomialverteilung-e5-k1-s8-v4 – `Y hat die Werte # bis # und eine symmetrische Verteilung.Es gilt P(Y\le #)\approx # und P(Y=#)\approx #.Bestimme damit P …`
- B-549 (2): pythagoras-e2-k3-s6-v2, pythagoras-e2-k3-s6-v3 – `In einem rechtwinkligen Dreieck ist die Hypotenuse # m lang.Eine Kathete ist # m lang.Weise nach,dass die andere Kathete …`
- B-550 (3): zinsrechnung-e2-k1-s5-v1, zinsrechnung-e2-k1-s5-v2, zinsrechnung-e2-k1-s5-v3 – `Auf einem Konto liegen #€.Die Bank zahlt #\%Zinsen im Jahr.Berechne das Guthaben nach einem Jahr in einem Schritt mit de …`
- B-551 (5): brueche-dezimalzahlen-e1-k1-s1-v1, brueche-dezimalzahlen-e1-k1-s1-v2, brueche-dezimalzahlen-e1-k1-s1-v3, brueche-dezimalzahlen-e1-k1-s1-v4, brueche-dezimalzahlen-e1-k1-s1-v5 – `Der Streifen ist in gleich große Teile geteilt.Welcher Anteil des Streifens ist gefärbt?Gib ihn als Bruch an.‖Grafik:\br …`
- B-552 (3): winkel-dreiecke-e4-k1-s3-v1, winkel-dreiecke-e4-k1-s3-v2, winkel-dreiecke-e4-k1-s3-v3 – `Konstruiere das Dreieck ABC mit c=# cm,\alpha=#^\circ und\beta=#^\circ.Beginne mit der Seite c auf dem Strahl.‖Grafik:\w …`
- B-553 (3): zinsrechnung-e1-k2-s2-v1, zinsrechnung-e1-k2-s2-v2, zinsrechnung-e1-k2-s2-v3 – `Auf einem Konto liegen #€für # Tage.Die Bank zahlt #\%Zinsen im Jahr.Rechne mit dem Bankjahr.Wie viel Euro Zinsen gibt e …`
- B-554 (2): strahlensaetze-e1-k2-s0-v1, strahlensaetze-e1-k2-s0-v2 – `Eine Zeichnung hat den Maßstab #:#.Kreuze an,ob die Zeichnung kleiner oder größer als die Wirklichkeit ist.\kreuz{kleine …`
- B-555 (5): prozentrechnung-e1-k1-s1-v1, prozentrechnung-e1-k1-s1-v2, prozentrechnung-e1-k1-s1-v3, prozentrechnung-e1-k1-s1-v4, prozentrechnung-e1-k1-s1-v5 – `Der Streifen zeigt ein Ganzes.Ein Teil davon ist grau.Wie viel Prozent des ganzen Streifens sind grau?‖Grafik:\streifenf …`
- B-556 (4): prozentrechnung-e4-k2-s0-v1, prozentrechnung-e4-k2-s0-v2, prozentrechnung-e4-k2-s0-v3, prozentrechnung-e4-k2-s0-v4 – `Der graue Abschnitt ist #\%des Ganzen.Trage den Abschnitt so oft ab,bis du bei #\%bist.Markiere das Ganze.‖Grafik:\strei …`
- B-557 (3): kreis-e3-k1-s2-v1, kreis-e3-k1-s2-v2, kreis-e3-k1-s2-v3 – `Ein Kreisausschnitt hat den Mittelpunktswinkel\alpha=#^\circ.Wie viel Prozent des Kreises sind das?Runde auf eine Stelle …`
- B-558 (3): winkel-dreiecke-e4-k1-s6-v1, winkel-dreiecke-e4-k1-s6-v2, winkel-dreiecke-e4-k1-s6-v3 – `Konstruiere ein rechtwinkliges Dreieck ABC.Der rechte Winkel liegt bei C.Die Katheten sind a=# cm und b=# cm.‖Grafik:\wi …`
- B-559 (2): kurvenuntersuchung-e1-k1-s7-v5, kurvenuntersuchung-e1-k1-s7-v6 – `Bestimme Koordinaten und Art aller Extrempunkte des Graphen von f(x)=\frac{#}{#}x^#-#x+# und gib das Monotonieverhalten …`
- B-560 (2): geraden-e4-k1-s1-v3, geraden-e4-k1-s1-v5 – `Von der Spitze M(#|#|#)eines Masts führt ein gespanntes Seil zum Bodenanker X(#|-#|#)(# LE=# m).Gib eine Gleichung der S …`
- B-561 (2): grenzwerte-und-verhalten-im-unendlichen-e3-k1-s2-v1, grenzwerte-und-verhalten-im-unendlichen-e3-k1-s2-v3 – `f(x)=#e^{-#x}-#.Begründe,dass f streng monoton fällt und der Graph durch den Ursprung verläuft.Grenzwert für x\to+\infty …`
- B-562 (2): pyramide-kegel-kugel-e1-k5-s8-v2, pyramide-kegel-kugel-e1-k5-s8-v3 – `Eine Pyramide hat ein Quadrat als Grundfläche.Die Grundkante ist # m lang,die Seitenhöhe ist # m.Berechne die Oberfläche …`
- B-563 (2): uneigentliche-integrale-e1-k1-s3-v1, uneigentliche-integrale-e1-k1-s3-v2 – `Vergleiche∫_#^w\frac{#}{x^#}dx und∫_#^w\frac{#}{x}dx für w\to\infty:Welche der beiden unbegrenzten Flächen hat einen end …`
- B-564 (10): potenzen-wurzeln-basis-k2-v1, potenzen-wurzeln-basis-k2-v2, potenzen-wurzeln-basis-k2-v3, potenzen-wurzeln-basis-k2-v4, potenzen-wurzeln-basis-k2-v5, potenzen-wurzeln-basis-k2-v6, potenzen-wurzeln-basis-k2-v7, potenzen-wurzeln-basis-k2-v8, potenzen-wurzeln-basis-k2-v9, potenzen-wurzeln-basis-k2-v10 – `Welche Aussage ist wahr?Kreuze an.(P# # OS)\\kreuz{\sqrt{(-#)^#}=-#}\\kreuz{\sqrt{(-#)^#}=#}\\kreuz{\sqrt{(-#)^#}ist nic …`
- B-565 (2): lineare-gleichungssysteme-e3-k1-s4-v2, lineare-gleichungssysteme-e3-k1-s4-v3 – `Löse das Gleichungssystem I:#x+#y=# und II:#x+#y=#.Vervielfache dazu beide Gleichungen.Addiere oder subtrahiere dann die …`
- B-566 (2): terme-e3-k2-s2-v1, terme-e3-k2-s2-v2 – `Rechne #-(#+#)auf zwei Wegen:erst die Klammer ausrechnen und dann abziehen;dann Glied für Glied abziehen.Vergleiche beid …`
- B-567 (5): prozentrechnung-e2-k3-s1-v1, prozentrechnung-e2-k3-s1-v2, prozentrechnung-e2-k3-s1-v3, prozentrechnung-e2-k3-s1-v4, prozentrechnung-e2-k3-s1-v5 – `In einer Schule wurden # Kinder befragt.# davon spielen ein Instrument.Wie viel Prozent der befragten Kinder spielen ein …`
- B-568 (2): spiegelung-e2-k1-s3-v1, spiegelung-e2-k1-s3-v2 – `g und h schneiden sich in S(#|#|#)und haben die Richtungsvektoren(#|#|#)und(#|#|#).Gib eine Ebene an,an der g auf h gesp …`
- B-569 (2): abstaende-e3-k1-s1-v1, abstaende-e3-k1-s1-v4 – `Die Gerade g\colon\vec x=(#|#|#)+t\cdot(#|#|-#)ist gegeben.Berechne den Lotfußpunkt F von P(#|#|#)auf g und den Abstand …`
- B-570 (2): pyramide-kegel-kugel-e2-k2-s7-v1, pyramide-kegel-kugel-e2-k2-s7-v3 – `Ein Kegel hat den Radius # cm und die Mantellinie # cm.Berechne den Flächeninhalt des Mantels.Runde auf eine Stelle nach …`
- B-571 (2): rationale-zahlen-e2-k3-s0-v1, rationale-zahlen-e2-k3-s0-v4 – `Ein Pfeil startet auf der Zahlengeraden bei-#.Er geht # nach rechts.Zeichne den Pfeil.‖Grafik:\zahlenstrahl[xmin=-#xmax= …`
- B-572 (3): winkel-dreiecke-e4-k1-s2-v1, winkel-dreiecke-e4-k1-s2-v2, winkel-dreiecke-e4-k1-s2-v3 – `Konstruiere das Dreieck ABC mit b=# cm,c=# cm und\alpha=#^\circ.Beginne mit der Seite c auf dem Strahl.‖Grafik:\winkelst …`
- B-573 (2): ebenen-e1-k1-s3-v1, ebenen-e1-k1-s3-v2 – `Die Ebene E enthält die Gerade g\colon\vec x=(#|#|#)+t\cdot(#|#|#),t\in\mathbb{R},und den Punkt P(#|#|#).Parametergleich …`
- B-574 (2): hypothesentests-e3-k1-s0-v1, hypothesentests-e3-k1-s0-v3 – `Getestet wird H_#\colon p\le #.Für welchen wahren Anteil p ist ein Fehler zweiter Art möglich?\\kreuz{p=#}\\kreuz{p=#}\\ …`
- B-575 (2): hypothesentests-e3-k1-s0-v2, hypothesentests-e3-k1-s0-v4 – `Getestet wird H_#\colon p\ge #.Für welchen wahren Anteil p ist ein Fehler zweiter Art möglich?\\kreuz{p=#}\\kreuz{p=#}\\ …`
- B-576 (2): umkehrfunktion-e2-k1-s4-v1, umkehrfunktion-e2-k1-s4-v2 – `Die Punkte A(#|#)und B(#|#)werden an y=x gespiegelt.Begründe,dass A,B,B'und A'ein Trapez bilden,und berechne seinen Fläc …`
- B-577 (4): winkel-dreiecke-basis-k1-v2, winkel-dreiecke-basis-k1-v4, winkel-dreiecke-basis-k1-v8, winkel-dreiecke-basis-k1-v10 – `Aus welchen drei Stäben kann man ein Dreieck legen?(P# # OS)\\kreuz{# cm,# cm,# cm}\\kreuz{# cm,# cm,# cm}\\kreuz{# cm,# …`
- B-578 (3): winkel-dreiecke-e4-k1-s4-v1, winkel-dreiecke-e4-k1-s4-v2, winkel-dreiecke-e4-k1-s4-v3 – `Konstruiere das Dreieck ABC mit b=# cm,c=# cm und\beta=#^\circ.Beginne mit der Seite c auf dem Strahl.‖Grafik:\winkelstr …`
- B-579 (2): lineare-funktionen-basis-k3-v6, lineare-funktionen-basis-k3-v10 – `Gegeben ist f(x)=-#x+#.Welcher Punkt liegt nicht auf der Geraden?Kreuze an.(P# # OS)\\kreuz{(#|-#)}\\kreuz{(-#|#)}\\kreu …`
- B-580 (2): normalverteilung-und-sigma-regeln-e3-k1-s1-v1, normalverteilung-und-sigma-regeln-e3-k1-s1-v2 – `Die Dichte von X ist f(x)=\frac{#}{#\sqrt{#\pi}}\mathrm{e}^{-\frac{#}{#}\left(\frac{x-#}{#}\right)^#}.\mu und\sigma?(Abi …`
- B-581 (2): potenzen-wurzeln-e3-k2-s0-v3, potenzen-wurzeln-e3-k2-s0-v4 – `Kreuze an,zwischen welchen ganzen Zahlen\sqrt{#}liegt.\\kreuz{zwischen # und #}\\kreuz{zwischen # und #}\\kreuz{zwischen …`
- B-582 (2): punkte-und-strecken-im-koordinatensystem-e2-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e2-k1-s7-v3 – `A(#|#|#)und B(#|#|#)liegen auf einer Geraden g.Gib einen Punkt D\ne B auf g an,der von A so weit entfernt ist wie B.(Abi …`
- B-583 (2): pythagoras-e1-k4-s1-v1, pythagoras-e1-k4-s1-v3 – `Die Katheten eines rechtwinkligen Dreiecks sind # m und # m lang.Berechne die Länge der Hypotenuse c.Runde das Ergebnis …`
- B-584 (2): pythagoras-e3-k2-s12-v2, pythagoras-e3-k2-s12-v3 – `Die Figur zeigt einen Kegel.Die Mantellinie ist # m lang,der Radius ist # m.Berechne die Höhe h.‖Grafik:\kegel{#}{#}{# m …`
- B-585 (2): ebenen-e2-k2-s4-v2, ebenen-e2-k2-s4-v3 – `Bestimme rechnerisch einen Normalenvektor der Ebene durch A(#|#|#),B(#|#|#)und C(#|#|#)und prüfe ihn mit beiden Skalarpr …`
- B-586 (2): flaechen-e2-k1-s2-v1, flaechen-e2-k1-s2-v3 – `Ein Parallelogramm hat die Grundseite # cm und die schräge Seite # cm.Die Höhe ist # cm.Berechne die Fläche des Parallel …`
- B-587 (5): extremalprobleme-e3-k1-s1-v1, extremalprobleme-e3-k1-s1-v2, extremalprobleme-e3-k1-s1-v3, extremalprobleme-e3-k1-s1-v4, extremalprobleme-e3-k1-s1-v5 – `Die Zielfunktion A(x)=#x-x^# #<x<\sqrt{#},beschreibt einen Flächeninhalt.Bestimme die Stelle mit A'(x)=# im Definitionsb …`
- B-588 (3): trigonometrie-e1-k3-s7-v1, trigonometrie-e1-k3-s7-v2, trigonometrie-e1-k3-s7-v3 – `Ein rechtwinkliges Dreieck hat den Winkel\alpha=#^\circ.Die Gegenkathete von\alpha ist # cm lang.Wie lang ist die Hypote …`
- B-589 (2): lineare-funktionen-basis-k3-v1, lineare-funktionen-basis-k3-v9 – `Gegeben ist f(x)=#x-#.Welcher Punkt liegt nicht auf der Geraden?Kreuze an.(P# # OS)\\kreuz{(#|#)}\\kreuz{(#|#)}\\kreuz{( …`
- B-590 (2): lineare-funktionen-basis-k3-v5, lineare-funktionen-basis-k3-v7 – `Gegeben ist f(x)=#x-#.Welcher Punkt liegt nicht auf der Geraden?Kreuze an.(P# # OS)\\kreuz{(#|#)}\\kreuz{(-#|-#)}\\kreuz …`
- B-591 (2): potenzen-wurzeln-e3-k2-s15-v1, potenzen-wurzeln-e3-k2-s15-v2 – `Kreuze die wahre Aussage an.(P# # OS)\\kreuz{\sqrt{(-#)^#}=-#}\\kreuz{\sqrt{(-#)^#}=#}\\kreuz{\sqrt{(-#)^#}ist nicht def …`
- B-592 (2): pyramide-kegel-kugel-e1-k5-s2-v1, pyramide-kegel-kugel-e1-k5-s2-v3 – `Eine Pyramide hat ein Quadrat als Grundfläche.Die Grundkante ist # cm lang,die Höhe ist # cm.Berechne das Volumen der Py …`
- B-593 (2): pyramide-kegel-kugel-e2-k2-s8-v1, pyramide-kegel-kugel-e2-k2-s8-v3 – `Ein Kegel hat den Radius # cm und die Mantellinie # cm.Berechne die Oberfläche des Kegels.Runde auf eine Stelle nach dem …`
- B-594 (5): zufallsexperimente-und-pfadregeln-e2-k1-s1-v1, zufallsexperimente-und-pfadregeln-e2-k1-s1-v2, zufallsexperimente-und-pfadregeln-e2-k1-s1-v3, zufallsexperimente-und-pfadregeln-e2-k1-s1-v4, zufallsexperimente-und-pfadregeln-e2-k1-s1-v5 – `In einer Lostrommel liegen # Lose,# davon sind Gewinne.Tom zieht ein Los.Wie groß ist die Wahrscheinlichkeit für einen G …`
- B-595 (3): trigonometrie-e1-k3-s9-v1, trigonometrie-e1-k3-s9-v2, trigonometrie-e1-k3-s9-v3 – `Ein rechtwinkliges Dreieck hat den Winkel\alpha=#^\circ.Die Ankathete von\alpha ist # cm lang.Wie lang ist die Gegenkath …`
- B-596 (3): trigonometrie-e1-k3-s10-v1, trigonometrie-e1-k3-s10-v2, trigonometrie-e1-k3-s10-v3 – `Ein rechtwinkliges Dreieck hat den Winkel\alpha=#^\circ.Die Gegenkathete von\alpha ist # cm lang.Wie lang ist die Ankath …`
- B-597 (3): zinsrechnung-e2-k1-s6-v1, zinsrechnung-e2-k1-s6-v2, zinsrechnung-e2-k1-s6-v3 – `Auf einem Konto liegen #€für # Jahre.Die Bank zahlt #\%Zinsen mit Zinseszins.Wie hoch ist das Guthaben am Ende?Runde auf …`
- B-598 (2): reelle-zahlen-e2-k1-s0-v1, reelle-zahlen-e2-k1-s0-v3 – `Kreuze an,welches Potenzgesetz zu #^#\cdot #^# passt.\\kreuz{gleiche Basis}\\kreuz{gleicher Exponent}\\kreuz{keins:ausre …`
- B-599 (5): pythagoras-e2-k3-s1-v1, pythagoras-e2-k3-s1-v2, pythagoras-e2-k3-s1-v3, pythagoras-e2-k3-s1-v4, pythagoras-e2-k3-s1-v5 – `In einem rechtwinkligen Dreieck ist die Hypotenuse c=# cm lang.Eine Kathete ist b=# cm lang.Berechne die Länge der Kathe …`
- B-600 (3): strahlensaetze-e1-k2-s8-v1, strahlensaetze-e1-k2-s8-v2, strahlensaetze-e1-k2-s8-v3 – `Eine Karte hat den Maßstab #:#.Auf der Karte ist ein Weg #\text{cm}lang.Wie viele Kilometer ist der Weg in Wirklichkeit …`
- B-601 (2): trigonometrische-funktionen-e1-k1-s11-v1, trigonometrische-funktionen-e1-k1-s11-v2 – `Kreuze an,welches Bogenmaß zu #°gehört.\\kreuz{\frac{\pi}{#}}\kreuz{\frac{\pi}{#}}\kreuz{\frac{\pi}{#}}\kreuz{\frac{#\pi …`
- B-602 (3): trigonometrie-e1-k3-s8-v1, trigonometrie-e1-k3-s8-v2, trigonometrie-e1-k3-s8-v3 – `Ein rechtwinkliges Dreieck hat den Winkel\alpha=#^\circ.Die Ankathete von\alpha ist # cm lang.Wie lang ist die Hypotenus …`
- B-603 (5): winkel-dreiecke-e4-k1-s1-v1, winkel-dreiecke-e4-k1-s1-v2, winkel-dreiecke-e4-k1-s1-v3, winkel-dreiecke-e4-k1-s1-v4, winkel-dreiecke-e4-k1-s1-v5 – `Konstruiere das Dreieck ABC mit a=# cm,b=# cm und c=# cm.Beginne mit der Seite c auf dem Strahl.‖Grafik:\winkelstrahl[#] …`
- B-604 (4): brueche-dezimalzahlen-e5-k2-s0-v1, brueche-dezimalzahlen-e5-k2-s0-v2, brueche-dezimalzahlen-e5-k2-s0-v3, brueche-dezimalzahlen-e5-k2-s0-v4 – `Die Zahlen # und # haben gleich viele Stellen.An welcher Stelle unterscheiden sie sich zuerst?Setze kein Vergleichszeich …`
- B-605 (3): kreis-e1-k2-s1-v1, kreis-e1-k2-s1-v2, kreis-e1-k2-s1-v4 – `Ein Kreis hat den Durchmesser d=# cm.Wie lang ist sein Umfang?Rechne mit der\pi-Taste.Runde auf eine Stelle nach dem Kom …`
- B-606 (2): kreis-e1-k2-s4-v1, kreis-e1-k2-s4-v2 – `Ein Kreis hat den Umfang u=# cm.Wie groß ist sein Durchmesser?Rechne mit der\pi-Taste.Runde auf eine Stelle nach dem Kom …`
- B-607 (5): winkel-dreiecke-e2-k2-s1-v1, winkel-dreiecke-e2-k2-s1-v2, winkel-dreiecke-e2-k2-s1-v3, winkel-dreiecke-e2-k2-s1-v4, winkel-dreiecke-e2-k2-s1-v5 – `An einer Geradenkreuzung ist\alpha=#^\circ.Wie groß ist der Scheitelwinkel von α?‖Grafik:\geradenkreuzung{#}{\alpha}{}{} …`
- B-608 (3): kreis-e3-k1-s1-v1, kreis-e3-k1-s1-v2, kreis-e3-k1-s1-v3 – `Ein Kreisausschnitt hat den Mittelpunktswinkel\alpha=#^\circ.Welcher Teil des Kreises ist das?Gib den Anteil als Bruch a …`
- B-609 (3): trigonometrie-e3-k1-s12-v1, trigonometrie-e3-k1-s12-v2, trigonometrie-e3-k1-s12-v3 – `Im Dreieck ABC geht die Höhe h von C auf AB.Es gilt AC=# cm,\alpha=#^\circ und\beta=#^\circ.Berechne zuerst h und dann B …`
- B-610 (3): winkel-dreiecke-e1-k2-s6-v1, winkel-dreiecke-e1-k2-s6-v2, winkel-dreiecke-e1-k2-s6-v3 – `Die Winkel #^\circ und #^\circ liegen am selben Scheitel nebeneinander.Wie groß ist der Winkel,den beide zusammen bilden …`
- B-611 (3): winkel-dreiecke-e4-k1-s5-v1, winkel-dreiecke-e4-k1-s5-v2, winkel-dreiecke-e4-k1-s5-v3 – `Konstruiere ein gleichschenkliges Dreieck ABC.Die Basis ist c=# cm.Die Schenkel sind a=b=# cm.‖Grafik:\winkelstrahl[#][A …`
- B-612 (2): winkel-dreiecke-basis-k3-v1, winkel-dreiecke-basis-k3-v6 – `Die beiden waagerechten Geraden sind parallel.Wie groß ist\alpha?(P# # OS)‖Grafik:\parallelenpaar{#}{#^\circ}{}{}{\alpha …`
- B-613 (3): winkel-dreiecke-e1-k2-s7-v1, winkel-dreiecke-e1-k2-s7-v2, winkel-dreiecke-e1-k2-s7-v3 – `Ein Winkel von #^\circ ist durch einen Strahl in zwei Teilwinkel geteilt.Der eine misst #^\circ.Wie groß ist der andere?`
- B-614 (2): flaecheninhalt-durch-integration-e4-k1-s1-v2, flaecheninhalt-durch-integration-e4-k1-s1-v5 – `Für m># schließen die Gerade y=m\cdot x und der Graph von f(x)=#x^# eine Fläche mit dem Inhalt\frac{#}{#}ein.Bestimme m.`
- B-615 (2): flaecheninhalt-und-volumen-im-raum-e2-k1-s1-v1, flaecheninhalt-und-volumen-im-raum-e2-k1-s1-v2 – `P(#|#|#),Q(#|#|#),R(#|#|-#).Zeige,dass bei Q ein rechter Winkel liegt,und berechne den Flächeninhalt des Rechtecks PQRS.`
- B-616 (2): lineare-gleichungen-e1-k3-s2-v1, lineare-gleichungen-e1-k3-s2-v3 – `Trage in die Tabelle eigene Zahlen für x ein.Welche Zahl löst die Gleichung #x+#=#?‖Grafik:\wertetabelleleer{x}{#x+#}{#}`
- B-617 (2): prozentrechnung-e5-k2-s1-v2, prozentrechnung-e5-k2-s1-v4 – `Ein Preis von #€wird um #\%gesenkt.Der Streifen zeigt die #\%.Wie hoch ist der neue Preis?‖Grafik:\streifen[#]{#}{#}{#€}`
- B-618 (4): potenz-exponentialfunktionen-e2-k1-s0-v1, potenz-exponentialfunktionen-e2-k1-s0-v2, potenz-exponentialfunktionen-e2-k1-s0-v3, potenz-exponentialfunktionen-e2-k1-s0-v4 – `Ein Wert wird jedes Jahr mit # multipliziert.Kreuze an,ob der Wert mehr oder weniger wird.\\kreuz{mehr}\\kreuz{weniger}`
- B-619 (3): kreis-e2-k1-s1-v1, kreis-e2-k1-s1-v3, kreis-e2-k1-s1-v5 – `Ein Kreis hat den Radius r=# cm.Wie groß ist seine Fläche?Rechne mit der\pi-Taste.Runde auf eine Stelle nach dem Komma.`
- B-620 (3): prozentrechnung-e5-k2-s1-v1, prozentrechnung-e5-k2-s1-v3, prozentrechnung-e5-k2-s1-v5 – `Ein Preis von #€wird um #\%erhöht.Der Streifen zeigt die #\%.Wie hoch ist der neue Preis?‖Grafik:\streifen[#]{#}{#}{#€}`
- B-621 (3): trigonometrische-funktionen-e1-k1-s9-v1, trigonometrische-funktionen-e1-k1-s9-v2, trigonometrische-funktionen-e1-k1-s9-v3 – `Rechne #°ins Bogenmaß um.Schreibe das Ergebnis als Vielfaches von\pi.Runde es außerdem auf zwei Stellen nach dem Komma.`
- B-622 (3): winkel-dreiecke-e2-k2-s2-v1, winkel-dreiecke-e2-k2-s2-v2, winkel-dreiecke-e2-k2-s2-v3 – `An einer Geradenkreuzung ist\alpha=#^\circ.Wie groß ist ein Nebenwinkel von α?‖Grafik:\geradenkreuzung{#}{\alpha}{}{}{}`
- B-623 (2): kreis-e2-k1-s3-v1, kreis-e2-k1-s3-v3 – `Ein Kreis hat den Radius r=# m.Wie groß ist seine Fläche?Rechne mit der\pi-Taste.Runde auf zwei Stellen nach dem Komma.`
- B-624 (2): kreis-e2-k1-s6-v1, kreis-e2-k1-s6-v3 – `Ein Kreis hat die Fläche A=# cm².Wie groß ist sein Radius?Rechne mit der\pi-Taste.Runde auf eine Stelle nach dem Komma.`
- B-625 (2): quadratische-gleichungen-e2-k1-s12-v1, quadratische-gleichungen-e2-k1-s12-v2 – `Kreuze an,welcher Wert die Gleichung x\cdot(x+#)=-# erfüllt.(P# # OS)\\kreuz{x=#}\\kreuz{x=#}\\kreuz{x=-#}\\kreuz{x=-#}`
- B-626 (2): trigonometrische-funktionen-e2-k1-s1-v1, trigonometrische-funktionen-e2-k1-s1-v5 – `Fülle die Wertetabelle für y=sin(x)aus.Runde auf zwei Stellen nach dem Komma.‖Grafik:\wertetabelle{x in°}{y}{#,#,#,#,#}`
- B-627 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v3, punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v4 – `Quader ABCDEFGH(Boden ABCD,E über A,F über B,G über C,H über D)mit A(#|#|#),B(#|#|#),E(#|#|#),H(#|#|#):G?(Abitur # GK)`
- B-628 (5): zinsrechnung-e1-k2-s1-v1, zinsrechnung-e1-k2-s1-v2, zinsrechnung-e1-k2-s1-v3, zinsrechnung-e1-k2-s1-v4, zinsrechnung-e1-k2-s1-v5 – `Auf einem Konto liegen #€für # Monate.Die Bank zahlt #\%Zinsen im Jahr.Wie viel Euro Zinsen gibt es für die # Monate?`
- B-629 (4): abstaende-e2-k2-s1-v1, abstaende-e2-k2-s1-v2, abstaende-e2-k2-s1-v4, abstaende-e2-k2-s1-v5 – `Die Ebene E\colon #x-y+#z=# ist gegeben.Berechne den Abstand des Punktes P(#|#|#)von E mit der Hesseschen Normalform.`
- B-630 (3): trigonometrie-e1-k3-s4-v1, trigonometrie-e1-k3-s4-v2, trigonometrie-e1-k3-s4-v3 – `Ein rechtwinkliges Dreieck hat den Winkel\alpha=#^\circ.Die Hypotenuse ist # cm lang.Wie lang ist die Gegenkathete x?`
- B-631 (2): quadratische-gleichungen-e3-k3-s10-v1, quadratische-gleichungen-e3-k3-s10-v3 – `Berechne für x^#-#x+#=# die Diskriminante D=\left(\frac{p}{#}\right)^#-q.Gib an,wie viele Lösungen die Gleichung hat.`
- B-632 (2): zufallsexperimente-und-pfadregeln-e7-k1-s1-v1, zufallsexperimente-und-pfadregeln-e7-k1-s1-v2 – `Eine Münze zeigt Kopf mit # und Zahl mit #.Sie wird dreimal geworfen.Welches Ereignis hat die Wahrscheinlichkeit #^#?`
- B-633 (3): punkte-und-strecken-im-koordinatensystem-e5-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e5-k1-s7-v2, punkte-und-strecken-im-koordinatensystem-e5-k1-s7-v3 – `Der Punkt B(#|#|#)wird um die x_#-Achse gedreht.Gib drei Bildpunkte an,bei denen eine Koordinate # ist.(Abitur # LK)`
- B-634 (3): zinsrechnung-e2-k1-s8-v1, zinsrechnung-e2-k1-s8-v2, zinsrechnung-e2-k1-s8-v3 – `Auf einem Konto liegen #€für # Jahre.Die Bank zahlt #\%Zinsen mit Zinseszins.Wie viel Euro Zinsen gibt es insgesamt?`
- B-635 (2): lineare-gleichungssysteme-e1-k1-s1-v2, lineare-gleichungssysteme-e1-k1-s1-v3 – `Die Tabelle gehört zur Gleichung #x+y=#.Ergänze zu jedem x den passenden Wert für y.‖Grafik:\wertetabelle{x}{y}{#,#}`
- B-636 (3): koerper-e1-k1-s6-v1, koerper-e1-k1-s6-v2, koerper-e1-k1-s6-v3 – `Ein Quader ist # cm lang,# cm tief und # cm hoch.Zeichne sein Schrägbild auf Kästchenpapier.‖Grafik:\rechenplatz{#}`
- B-637 (3): koerper-e4-k2-s2-v1, koerper-e4-k2-s2-v2, koerper-e4-k2-s2-v3 – `Ein Zylinder hat den Durchmesser # cm und die Höhe # cm.Berechne sein Volumen.Runde auf eine Stelle nach dem Komma.`
- B-638 (2): brueche-dezimalzahlen-e1-k1-s6-v11, brueche-dezimalzahlen-e1-k1-s6-v12 – `Die Figur besteht aus gleich großen Kästchen.Schraffiere\frac{#}{#}der Fläche.(P# # OS)‖Grafik:\bruchrechteck{#}{#}`
- B-639 (2): potenz-exponentialfunktionen-e1-k1-s0-v3, potenz-exponentialfunktionen-e1-k1-s0-v4 – `Die Werte sind # # # und #.Kreuze an,was von Wert zu Wert gleich bleibt.\\kreuz{die Differenz}\\kreuz{der Quotient}`
- B-640 (3): trigonometrie-e1-k3-s5-v1, trigonometrie-e1-k3-s5-v2, trigonometrie-e1-k3-s5-v3 – `Ein rechtwinkliges Dreieck hat den Winkel\alpha=#^\circ.Die Hypotenuse ist # cm lang.Wie lang ist die Ankathete x?`
- B-641 (3): winkel-dreiecke-e5-k2-s2-v1, winkel-dreiecke-e5-k2-s2-v2, winkel-dreiecke-e5-k2-s2-v3 – `Ein Umfangswinkel über dem Bogen AB ist #^\circ groß.Wie groß ist der Mittelpunktswinkel AMB über demselben Bogen?`
- B-642 (2): symmetrie-abbildungen-e2-k2-s1-v2, symmetrie-abbildungen-e2-k2-s1-v5 – `Zeichne die Symmetrieachse der Figur im Bild ein.‖Grafik:\dreieck{(#)}{(#)}{(#,#)}{a}{b}{c}{\alpha}{\beta}{\gamma}`
- B-643 (5): flaecheninhalt-durch-integration-e2-k1-s1-v1, flaecheninhalt-durch-integration-e2-k1-s1-v2, flaecheninhalt-durch-integration-e2-k1-s1-v3, flaecheninhalt-durch-integration-e2-k1-s1-v4, flaecheninhalt-durch-integration-e2-k1-s1-v5 – `Gegeben sind f(x)=#x^#+# und g(x)=-#x.Berechne den Inhalt der Fläche zwischen den beiden Graphen von x=# bis x=#.`
- B-644 (3): zinsrechnung-e1-k3-s1-v1, zinsrechnung-e1-k3-s1-v2, zinsrechnung-e1-k3-s1-v3 – `Auf einem Konto liegen #€.Die Bank zahlt #\%Zinsen im Jahr.Überschlage,wie viel Euro Zinsen es etwa im Jahr gibt.`
- B-645 (2): punkte-und-strecken-im-koordinatensystem-e3-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s7-v3 – `In der x_#x_#-Ebene liegen A(#|#),B(#|#)und C(#|#)auf einem Kreis.Koordinaten seines Mittelpunkts M?(Abitur # GK)`
- B-646 (2): trigonometrische-funktionen-e1-k1-s7-v1, trigonometrische-funktionen-e1-k1-s7-v3 – `Es gilt sin\alpha=#.Finde die beiden Winkel\alpha im ersten Vollkreis ab #°.Runde auf eine Stelle nach dem Komma.`
- B-647 (3): flaecheninhalt-durch-integration-e4-k1-s1-v1, flaecheninhalt-durch-integration-e4-k1-s1-v3, flaecheninhalt-durch-integration-e4-k1-s1-v4 – `Für m># schließen die Gerade y=m\cdot x und der Graph von f(x)=#x^# eine Fläche mit dem Inhalt # ein.Bestimme m.`
- B-648 (2): brueche-dezimalzahlen-e1-k1-s6-v13, brueche-dezimalzahlen-e1-k1-s6-v14 – `Die Figur besteht aus gleich großen Kästchen.Markiere\frac{#}{#}der Fläche.(P# # OS)‖Grafik:\bruchrechteck{#}{#}`
- B-649 (2): potenz-exponentialfunktionen-e5-k3-s0-v2, potenz-exponentialfunktionen-e5-k3-s0-v4 – `Kreuze an,wo die Variable im Term #^x steht.\\kreuz{in der Basis}\\kreuz{im Exponenten}\\kreuz{in einem Produkt}`
- B-650 (2): pyramide-kegel-kugel-e2-k2-s11-v1, pyramide-kegel-kugel-e2-k2-s11-v3 – `Ein Kegel hat das Volumen # cm³ und den Radius # cm.Wie hoch ist der Kegel?Runde auf eine Stelle nach dem Komma.`
- B-651 (3): koerper-e4-k2-s6-v1, koerper-e4-k2-s6-v2, koerper-e4-k2-s6-v3 – `Ein Zylinder hat den Radius # cm und die Höhe # cm.Berechne seinen Mantel.Runde auf eine Stelle nach dem Komma.`
- B-652 (2): bruchrechnung-e1-k5-s4-v2, bruchrechnung-e1-k5-s4-v3 – `Zeige\frac{#}{#}+\frac{#}{#}an einem Streifen mit # Teilen und gib das Ergebnis an.‖Grafik:\bruchrechteck{#}{#}`
- B-653 (2): flaechen-e4-k1-s3-v2, flaechen-e4-k1-s3-v3 – `Ein Trapez hat die Fläche A=# m².Die parallelen Seiten sind a=# m und c=# m.Wie lang ist die Höhe des Trapezes?`
- B-654 (2): tangente-normale-schnittwinkel-e3-k1-s0-v1, tangente-normale-schnittwinkel-e3-k1-s0-v3 – `Die Tangente an den Graphen von f im Punkt P(#|#)hat die Steigung #.Gib nur die Steigung der Normalen in P an.`
- B-655 (2): tangente-normale-schnittwinkel-e3-k1-s0-v2, tangente-normale-schnittwinkel-e3-k1-s0-v4 – `Die Tangente an den Graphen von f im Punkt P(#|#)hat die Steigung-#.Gib nur die Steigung der Normalen in P an.`
- B-656 (5): pythagoras-e1-k2-s1-v1, pythagoras-e1-k2-s1-v2, pythagoras-e1-k2-s1-v3, pythagoras-e1-k2-s1-v4, pythagoras-e1-k2-s1-v5 – `In einem rechtwinkligen Dreieck sind die Katheten a=# cm und b=# cm lang.Berechne die Länge der Hypotenuse c.`
- B-657 (3): pythagoras-e1-k2-s5-v1, pythagoras-e1-k2-s5-v2, pythagoras-e1-k2-s5-v3 – `In einem rechtwinkligen Dreieck sind a=# m und b=# cm die Katheten.Berechne die Länge der Hypotenuse c in cm.`
- B-658 (3): tangente-normale-schnittwinkel-e3-k1-s1-v1, tangente-normale-schnittwinkel-e3-k1-s1-v3, tangente-normale-schnittwinkel-e3-k1-s1-v5 – `Die Tangente an den Graphen von f im Punkt P(#|#)hat die Steigung #.Bestimme die Gleichung der Normalen in P.`
- B-659 (2): binomische-formeln-e2-k2-s4-v1, binomische-formeln-e2-k2-s4-v3 – `Gib an,welche binomische Formel passt.Wenn keine passt,schreibe„keine“.Multipliziere dann aus:(x+#)\cdot(x-#)`
- B-660 (2): tangente-normale-schnittwinkel-e3-k1-s1-v2, tangente-normale-schnittwinkel-e3-k1-s1-v4 – `Die Tangente an den Graphen von f im Punkt P(#|#)hat die Steigung-#.Bestimme die Gleichung der Normalen in P.`
- B-661 (10): winkel-dreiecke-basis-k2-v1, winkel-dreiecke-basis-k2-v2, winkel-dreiecke-basis-k2-v3, winkel-dreiecke-basis-k2-v4, winkel-dreiecke-basis-k2-v5, winkel-dreiecke-basis-k2-v6, winkel-dreiecke-basis-k2-v7, winkel-dreiecke-basis-k2-v8, winkel-dreiecke-basis-k2-v9, winkel-dreiecke-basis-k2-v10 – `Im Dreieck ABC ist\alpha=\beta=#^\circ und AC=# cm.Gib die Länge von BC und die Größe von\gamma an.(P# # OS)`
- B-662 (3): koerper-e3-k1-s2-v1, koerper-e3-k1-s2-v2, koerper-e3-k1-s2-v3 – `Die Grundfläche eines Prismas ist ein Rechteck mit # cm×# cm.Das Prisma ist # cm hoch.Berechne sein Volumen.`
- B-663 (3): koerper-e4-k2-s10-v1, koerper-e4-k2-s10-v2, koerper-e4-k2-s10-v3 – `Ein Zylinder hat das Volumen # cm³ und den Radius # cm.Wie hoch ist er?Runde auf eine Stelle nach dem Komma.`
- B-664 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s2-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s2-v3 – `Sind\vec{u}=(#|-#|#)und\vec{v}=(-#|#|-#)kollinear?Zeigen sie in dieselbe Richtung oder in die Gegenrichtung?`
- B-665 (5): zinsrechnung-e1-k1-s1-v1, zinsrechnung-e1-k1-s1-v2, zinsrechnung-e1-k1-s1-v3, zinsrechnung-e1-k1-s1-v4, zinsrechnung-e1-k1-s1-v5 – `Auf einem Sparbuch liegen #€.Die Bank zahlt #\%Zinsen im Jahr.Wie viel Euro Zinsen gibt es nach einem Jahr?`
- B-666 (3): winkel-dreiecke-e4-k1-s8-v1, winkel-dreiecke-e4-k1-s8-v2, winkel-dreiecke-e4-k1-s8-v3 – `Kreuze an,ob sich aus den Seiten # cm,# cm und # cm ein Dreieck konstruieren lässt.\\kreuz{ja}\\kreuz{nein}`
- B-667 (2): brueche-dezimalzahlen-e3-k1-s5-v1, brueche-dezimalzahlen-e3-k1-s5-v2 – `Trage\frac{#}{#}und\frac{#}{#}am Zahlenstrahl ein.‖Grafik:\zahlenstrahl[xmin=#xmax=#xstep=#karo=#]{#/# #/#}`
- B-668 (2): funktionsklassen-und-eigenschaften-e2-k1-s10-v1, funktionsklassen-und-eigenschaften-e2-k1-s10-v2 – `f(x)=#x^#-#x^#+#–berechne die Koordinaten aller Schnittpunkte des Graphen mit den Koordinatenachsen(FHR #).`
- B-669 (2): pythagoras-e3-k2-s2-v1, pythagoras-e3-k2-s2-v3 – `Ein gleichschenkliges Dreieck hat eine # cm lange Grundseite.Seine Höhe ist # cm.Wie lang ist ein Schenkel?`
- B-670 (5): einheiten-e3-k2-s1-v1, einheiten-e3-k2-s1-v2, einheiten-e3-k2-s1-v3, einheiten-e3-k2-s1-v4, einheiten-e3-k2-s1-v5 – `Eine Fläche ist # Flächeneinheiten groß.Eine Längeneinheit entspricht # cm.Wie groß ist die Fläche in cm²?`
- B-671 (3): koerper-e2-k5-s1-v1, koerper-e2-k5-s1-v2, koerper-e2-k5-s1-v3 – `Ein Aquarium ist innen # cm lang und # cm breit.Es werden # l Wasser eingefüllt.Wie hoch steht das Wasser?`
- B-672 (4): brueche-dezimalzahlen-e1-k1-s6-v7, brueche-dezimalzahlen-e1-k1-s6-v8, brueche-dezimalzahlen-e1-k1-s6-v9, brueche-dezimalzahlen-e1-k1-s6-v10 – `Die Figur besteht aus gleich großen Kästchen.Markiere #\%der Fläche.(P# # OS)‖Grafik:\bruchrechteck{#}{#}`
- B-673 (2): brueche-dezimalzahlen-e1-k1-s2-v1, brueche-dezimalzahlen-e1-k1-s2-v3 – `Der Streifen ist in gleich große Teile geteilt.Färbe\frac{#}{#}des Streifens.‖Grafik:\bruchrechteck{#}{#}`
- B-674 (2): potenzen-wurzeln-e3-k2-s0-v1, potenzen-wurzeln-e3-k2-s0-v2 – `Kreuze an,ob du\sqrt{#}im Kopf genau ausrechnen kannst.\\kreuz{ja,Quadratzahl}\\kreuz{nein,Näherungswert}`
- B-675 (2): uneigentliche-integrale-e1-k1-s1-v4, uneigentliche-integrale-e1-k1-s1-v5 – `f(x)=#e^{-#x}–Inhalt A(w)der Fläche zwischen dem Graphen von f und der x-Achse von # bis w als Term in w?`
- B-676 (5): lineare-gleichungen-e1-k3-s1-v1, lineare-gleichungen-e1-k3-s1-v2, lineare-gleichungen-e1-k3-s1-v3, lineare-gleichungen-e1-k3-s1-v4, lineare-gleichungen-e1-k3-s1-v5 – `Rechne mit der Tabelle aus,für welches x die Gleichung #x+#=# stimmt.‖Grafik:\wertetabelle{x}{#x+#}{#,#}`
- B-677 (3): brueche-dezimalzahlen-e4-k1-s8-v1, brueche-dezimalzahlen-e4-k1-s8-v2, brueche-dezimalzahlen-e4-k1-s8-v3 – `Schreibe\frac{#}{#}als Dezimalzahl.Die Division geht nicht auf.Schreibe das Ergebnis mit Periodenstrich.`
- B-678 (3): winkel-dreiecke-e3-k2-s3-v1, winkel-dreiecke-e3-k2-s3-v2, winkel-dreiecke-e3-k2-s3-v3 – `Ein gleichschenkliges Dreieck hat zwei Basiswinkel von je #^\circ.Wie groß ist der Winkel an der Spitze?`
- B-679 (2): ableitungsregeln-e1-k2-s8-v2, ableitungsregeln-e1-k2-s8-v3 – `f(x)=\frac{#}{#}x^#-\frac{#}{#}x^#+#x.Weise nach:f'(x)=\frac{#}{#}\cdot(x-#)^#\cdot(x+#)^#.(Abitur # GK)`
- B-680 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v5 – `Gerades Prisma ABCDEF(D über A,E über B,F über C)mit A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#):F?(Abitur # GK)`
- B-681 (2): tangente-normale-schnittwinkel-e1-k1-s1-v2, tangente-normale-schnittwinkel-e1-k1-s1-v4 – `Gegeben ist f(x)=x^#+#x^#-#.Bestimme die Gleichung der Tangente an den Graphen von f im Punkt P(#|f(#)).`
- B-682 (2): uneigentliche-integrale-e1-k1-s1-v1, uneigentliche-integrale-e1-k1-s1-v3 – `f(x)=e^{-#x}–Inhalt A(w)der Fläche zwischen dem Graphen von f und der x-Achse von # bis w als Term in w?`
- B-683 (3): kenngroessen-von-verteilungen-e3-k1-s1-v1, kenngroessen-von-verteilungen-e3-k1-s1-v2, kenngroessen-von-verteilungen-e3-k1-s1-v3 – `X ist binomialverteilt mit n=# und dem Erwartungswert\mu=#.Bestimme p und die Standardabweichung\sigma.`
- B-684 (3): tangente-normale-schnittwinkel-e5-k1-s1-v1, tangente-normale-schnittwinkel-e5-k1-s1-v2, tangente-normale-schnittwinkel-e5-k1-s1-v4 – `Die Gerade g(x)=-#x+# schließt mit den Koordinatenachsen ein Dreieck ein.Berechne seinen Flächeninhalt.`
- B-685 (2): kreis-e1-k4-s1-v1, kreis-e1-k4-s1-v3 – `Zeichne einen Kreis mit dem Radius # cm.Markiere seinen Mittelpunkt mit M.‖Grafik:\rechenplatz[halb]{#}`
- B-686 (2): pythagoras-e2-k3-s8-v1, pythagoras-e2-k3-s8-v2 – `Ein Dreieck hat die Seiten # cm,# cm und # cm.Prüfe mit einer Rechnung,ob das Dreieck rechtwinklig ist.`
- B-687 (2): symmetrie-abbildungen-e1-k2-s0-v2, symmetrie-abbildungen-e1-k2-s0-v3 – `Kreuze an,welche Koordinate beim Punkt(#|#)null ist.\\kreuz{die erste}\\kreuz{die zweite}\\kreuz{keine}`
- B-688 (4): kurvenuntersuchung-e2-k1-s1-v2, kurvenuntersuchung-e2-k1-s1-v3, kurvenuntersuchung-e2-k1-s1-v4, kurvenuntersuchung-e2-k1-s1-v5 – `Berechne die Stellen,an denen der Graph von f(x)=\frac{#}{#}x^#-#x^#-#x eine waagerechte Tangente hat.`
- B-689 (4): punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v2, punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v4, punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v5 – `Zeige:Das Dreieck A(#|#|#),B(#|#|#),C(#|#|#)ist gleichschenklig.Nenne Basis und Schenkel.(Abitur # GK)`
- B-690 (3): winkel-dreiecke-e1-k2-s4-v1, winkel-dreiecke-e1-k2-s4-v2, winkel-dreiecke-e1-k2-s4-v3 – `Bestimme den überstumpfen Winkel α.Miss dazu den Rest bis zum Vollwinkel.‖Grafik:\winkel[#]{#}{\alpha}`
- B-691 (2): linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v1, linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v2 – `Forme\vec{OX}=p\cdot\vec{OA}+q\cdot\vec{OB}mit p+q=# für A(#|#|#)und B(#|#|#)in eine Parameterform um.`
- B-692 (2): potenzen-wurzeln-e2-k1-s17-v1, potenzen-wurzeln-e2-k1-s17-v3 – `Schreibe die Zahl in der anderen Schreibweise:#\cdot #^{-#}.Entscheide selbst,wohin das Komma wandert.`
- B-693 (2): trigonometrie-e3-k1-s2-v1, trigonometrie-e3-k1-s2-v3 – `Ein Trapez ist # m hoch.Ein Basiswinkel ist #^\circ groß.Wie lang ist der Schenkel s an diesem Winkel?`
- B-694 (2): trigonometrie-zone-f2-v1, trigonometrie-zone-f2-v2 – `Ein Winkel ist #^\circ groß.Kreuze an,ob der Winkel spitz oder stumpf ist.\\kreuz{spitz}\kreuz{stumpf}`
- B-695 (4): brueche-dezimalzahlen-e4-k1-s0-v1, brueche-dezimalzahlen-e4-k1-s0-v2, brueche-dezimalzahlen-e4-k1-s0-v3, brueche-dezimalzahlen-e4-k1-s0-v4 – `Der Bruch\frac{#}{#}soll als Dezimalzahl geschrieben werden.Wie viele Stellen nach dem Komma hat sie?`
- B-696 (4): zuordnungen-e1-k2-s0-v1, zuordnungen-e1-k2-s0-v2, zuordnungen-e1-k2-s0-v3, zuordnungen-e1-k2-s0-v4 – `Auf einer Achse stehen die Zahlen # # und # je # Kästchen auseinander.Wie viel ist ein Kästchen wert?`
- B-697 (3): bruchrechnung-e2-k1-s0-v1, bruchrechnung-e2-k1-s0-v2, bruchrechnung-e2-k1-s0-v3 – `Welche Zahl steht in der Stellenwerttafel?‖Grafik:\sachtabelle{ccc}{Einer&Zehntel&Hundertstel}{#&#&#}`
- B-698 (2): flaechen-zone-f6-v1, flaechen-zone-f6-v2 – `Die Figur zeigt einen Winkel.Kreuze an,ob er ein rechter Winkel ist.\janein‖Grafik:\winkel{#}{\alpha}`
- B-699 (2): lineare-gleichungen-e1-k2-s6-v3, lineare-gleichungen-e1-k2-s6-v4 – `Kreuze an,welche Zahl die Gleichung #-#x=#x-# löst.(P# # OS)\\kreuz{-#}\\kreuz{#}\\kreuz{#}\\kreuz{#}`
- B-700 (2): brueche-dezimalzahlen-e2-k1-s0-v3, brueche-dezimalzahlen-e2-k1-s0-v4 – `Aus dem Bruch\frac{#}{#}wird\frac{#}{#}.Gib an,ob erweitert oder gekürzt wurde und mit welcher Zahl.`
- B-701 (2): rationale-zahlen-e4-k1-s2-v1, rationale-zahlen-e4-k1-s2-v3 – `Ein Konto steht bei #€.Danach gibt es drei Buchungen:-#€,-#€und+#€.Wie hoch ist der neue Kontostand?`
- B-702 (2): tangente-normale-schnittwinkel-e4-k1-s1-v3, tangente-normale-schnittwinkel-e4-k1-s1-v4 – `Die Gerade g geht durch den Punkt P(#|#)und hat den Steigungswinkel #^\circ.Berechne ihre Steigung.`
- B-703 (5): funktionsklassen-und-eigenschaften-e1-k1-s1-v1, funktionsklassen-und-eigenschaften-e1-k1-s1-v2, funktionsklassen-und-eigenschaften-e1-k1-s1-v3, funktionsklassen-und-eigenschaften-e1-k1-s1-v4, funktionsklassen-und-eigenschaften-e1-k1-s1-v5 – `Gegeben ist f(x)=x^#-#x^#+#.Berechne den Funktionswert an der Stelle # und schreibe den Punkt auf.`
- B-704 (3): stammfunktion-und-hauptsatz-e4-k1-s1-v1, stammfunktion-und-hauptsatz-e4-k1-s1-v3, stammfunktion-und-hauptsatz-e4-k1-s1-v5 – `J(x)ist das Integral von # bis x über f(t)=t^#-#t.Gib eine Nullstelle von J und den Term von J'an.`
- B-705 (2): kenngroessen-von-verteilungen-e2-k3-s1-v2, kenngroessen-von-verteilungen-e2-k3-s1-v3 – `Die Zufallsgröße X nimmt die Werte # # und # an,mit P(X=#)=# und E(X)=#.Bestimme P(X=#)und P(X=#).`
- B-706 (2): pyramide-kegel-kugel-e3-k1-s10-v1, pyramide-kegel-kugel-e3-k1-s10-v3 – `Eine Kugel hat die Oberfläche # cm².Wie groß ist ihr Radius?Runde auf zwei Stellen nach dem Komma.`
- B-707 (2): stammfunktion-und-hauptsatz-e4-k1-s1-v2, stammfunktion-und-hauptsatz-e4-k1-s1-v4 – `J(x)ist das Integral von-# bis x über f(t)=t^#-#t.Gib eine Nullstelle von J und den Term von J'an.`
- B-708 (3): brueche-dezimalzahlen-e5-k2-s2-v1, brueche-dezimalzahlen-e5-k2-s2-v2, brueche-dezimalzahlen-e5-k2-s2-v3 – `Hänge bei # und # Nullen an.Danach sollen beide Zahlen gleich viele Stellen nach dem Komma haben.`
- B-709 (3): winkel-dreiecke-e3-k2-s5-v1, winkel-dreiecke-e3-k2-s5-v2, winkel-dreiecke-e3-k2-s5-v3 – `Ein Dreieck hat einen rechten Winkel und einen Winkel von #^\circ.Wie groß ist der dritte Winkel?`
- B-710 (2): ebenen-e4-k2-s1-v4, ebenen-e4-k2-s1-v5 – `Gib eine Gleichung der Ebene F an,die parallel zu E\colon #x-y+#z=# ist und durch P(#|-#|#)geht.`
- B-711 (2): flaecheninhalt-und-volumen-im-raum-e3-k1-s1-v1, flaecheninhalt-und-volumen-im-raum-e3-k1-s1-v4 – `Pyramide mit der Grundfläche P(#|#|#),Q(#|#|#),R(#|#|#),T(#|#|#)und der Spitze S(#|#|#).Volumen?`
- B-712 (2): quadratische-gleichungen-e1-k2-s0-v1, quadratische-gleichungen-e1-k2-s0-v2 – `Kreuze an,wie viele Lösungen die Gleichung(x-#)^#=# hat.\\kreuz{zwei}\\kreuz{eine}\\kreuz{keine}`
- B-713 (5): quadratische-gleichungen-basis-k1-v1, quadratische-gleichungen-basis-k1-v2, quadratische-gleichungen-basis-k1-v4, quadratische-gleichungen-basis-k1-v6, quadratische-gleichungen-basis-k1-v9 – `Welcher Wert erfüllt x\cdot(x+#)=-#?(P# # OS)\\kreuz{x=#}\\kreuz{x=#}\\kreuz{x=-#}\\kreuz{x=-#}`
- B-714 (3): brueche-dezimalzahlen-e4-k1-s4-v1, brueche-dezimalzahlen-e4-k1-s4-v2, brueche-dezimalzahlen-e4-k1-s4-v3 – `Trage # und # am Zahlenstrahl ein.‖Grafik:\zahlenstrahl[xmin=#xmax=#xstep=#karo=#]{#/# #/# #/#}`
- B-715 (3): ebenen-e4-k2-s1-v1, ebenen-e4-k2-s1-v2, ebenen-e4-k2-s1-v3 – `Gib eine Gleichung der Ebene F an,die parallel zu E\colon #x-y+#z=# ist und durch P(#|#|#)geht.`
- B-716 (3): rationale-zahlen-e1-k1-s1-v2, rationale-zahlen-e1-k1-s1-v3, rationale-zahlen-e1-k1-s1-v5 – `Trage die Zahlen-# und-# an der Zahlengeraden ein.‖Grafik:\zahlenstrahl[xmin=-#xmax=#xstep=#]{}`
- B-717 (2): binomische-formeln-e1-k1-s5-v1, binomische-formeln-e1-k1-s5-v2 – `Multipliziere aus und schreibe alle vier Produkte auf.Fasse noch nicht zusammen.(x+#)\cdot(x+#)`
- B-718 (2): quadratische-funktionen-e1-k1-s10-v1, quadratische-funktionen-e1-k1-s10-v3 – `Die Parabel zu f(x)=a\cdot x^# geht durch den Punkt P(#|#).Bestimme a und gib die Gleichung an.`
- B-719 (2): rationale-zahlen-e1-k1-s1-v1, rationale-zahlen-e1-k1-s1-v4 – `Trage die Zahlen-# und # an der Zahlengeraden ein.‖Grafik:\zahlenstrahl[xmin=-#xmax=#xstep=#]{}`
- B-720 (3): kurvenuntersuchung-e2-k2-s1-v2, kurvenuntersuchung-e2-k2-s1-v4, kurvenuntersuchung-e2-k2-s1-v5 – `Zeige,dass f'(#)=# gilt,der Graph von f(x)=#x^#-#x also bei x=# eine waagerechte Tangente hat.`
- B-721 (2): quadratische-gleichungen-basis-k1-v5, quadratische-gleichungen-basis-k1-v10 – `Welcher Wert erfüllt x\cdot(x-#)=#?(P# # OS)\\kreuz{x=#}\\kreuz{x=#}\\kreuz{x=-#}\\kreuz{x=-#}`
- B-722 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s0-v2, linearkombination-und-lineare-abhaengigkeit-e1-k1-s0-v4 – `\vec{a}=(#|#|#)und\vec{b}=(#|#|#).Ist einer ein Vielfaches des anderen?\\kreuz{ja}\kreuz{nein}`
- B-723 (2): pyramide-kegel-kugel-e3-k1-s2-v1, pyramide-kegel-kugel-e3-k1-s2-v2 – `Eine Kugel hat den Durchmesser # cm.Berechne ihr Volumen.Runde auf eine Stelle nach dem Komma.`
- B-724 (3): ebenen-e2-k2-s1-v1, ebenen-e2-k2-s1-v2, ebenen-e2-k2-s1-v5 – `Gegeben ist E\colon #x-#y+#z=#.Gib den Normalenvektor von E an,dessen erste Komponente # ist.`
- B-725 (3): potenzen-wurzeln-e1-k2-s0-v1, potenzen-wurzeln-e1-k2-s0-v2, potenzen-wurzeln-e1-k2-s0-v4 – `Kreuze an,ob #^{-#}ein Bruch oder eine negative Zahl ist.\\kreuz{Bruch}\\kreuz{negative Zahl}`
- B-726 (2): pyramide-kegel-kugel-e3-k1-s5-v1, pyramide-kegel-kugel-e3-k1-s5-v3 – `Eine Kugel hat den Radius # cm.Berechne ihre Oberfläche.Runde auf eine Stelle nach dem Komma.`
- B-727 (5): punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v3, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v4, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v5 – `A(#|#|#)und B(#|#|#)eintragen,C ablesen.‖Grafik:\begin{ksys#}\rpunkt{#}{#}{#}{C}\end{ksys#}`
- B-728 (3): matrizen-und-uebergangsprozesse-e5-k1-s1-v1, matrizen-und-uebergangsprozesse-e5-k1-s1-v2, matrizen-und-uebergangsprozesse-e5-k1-s1-v3 – `Es gilt v_{n+#}=M\cdot v_n;M=((#|#),(#|#)),Gesamtzahl #.Berechne die stationäre Verteilung.`
- B-729 (2): lineare-gleichungssysteme-e1-k1-s12-v1, lineare-gleichungssysteme-e1-k1-s12-v2 – `Prüfe,ob der Punkt(#|#)das Ungleichungssystem I:y\geq # II:y\leq x+# III:x+y\leq # erfüllt.`
- B-730 (5): prozentrechnung-e3-k1-s1-v1, prozentrechnung-e3-k1-s1-v2, prozentrechnung-e3-k1-s1-v3, prozentrechnung-e3-k1-s1-v4, prozentrechnung-e3-k1-s1-v5 – `Der ganze Streifen steht für #€.Wie viel Euro sind #\%davon?‖Grafik:\streifen[#]{#}{#}{#€}`
- B-731 (3): reelle-zahlen-e2-k1-s1-v1, reelle-zahlen-e2-k1-s1-v2, reelle-zahlen-e2-k1-s1-v4 – `Schreibe #^#\cdot #^# als Malkette.Zähle die Faktoren.Schreibe dann alles als eine Potenz.`
- B-732 (2): kreis-e3-k1-s3-v1, kreis-e3-k1-s3-v3 – `Ein Kreisausschnitt ist\frac{#}{#}des ganzen Kreises.Wie groß ist sein Mittelpunktswinkel?`
- B-733 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s4-v2, punkte-und-strecken-im-koordinatensystem-e4-k1-s4-v3 – `Zeige:A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)bilden eine Raute,aber kein Quadrat.(Abitur # GK)`
- B-734 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s7-v2 – `Zeige:Das Viereck K(#|#|#),L(#|#|#),M(#|#|#),N(#|-#|#)ist ein Drachenviereck.(Abitur # GK)`
- B-735 (2): quadratische-gleichungen-e1-k2-s11-v1, quadratische-gleichungen-e1-k2-s11-v3 – `Schreibe die linke Seite von x^#+#x+#=# als Quadrat einer Klammer.Löse dann die Gleichung.`
- B-736 (5): flaecheninhalt-durch-integration-e1-k1-s1-v1, flaecheninhalt-durch-integration-e1-k1-s1-v2, flaecheninhalt-durch-integration-e1-k1-s1-v3, flaecheninhalt-durch-integration-e1-k1-s1-v4, flaecheninhalt-durch-integration-e1-k1-s1-v5 – `Der Graph von f(x)=#x^#-# schließt mit der x-Achse eine Fläche ein.Berechne ihren Inhalt.`
- B-737 (3): zinsrechnung-e1-k1-s5-v1, zinsrechnung-e1-k1-s5-v2, zinsrechnung-e1-k1-s5-v3 – `Auf einem Konto liegen #€.In einem Jahr gibt es dafür #€Zinsen.Wie hoch ist der Zinssatz?`
- B-738 (2): koerper-e2-k1-s6-v1, koerper-e2-k1-s6-v2 – `Ein Quader hat das Volumen # cm³.Er ist # cm lang und # cm breit.Wie hoch ist der Quader?`
- B-739 (2): lineare-funktionen-e4-k1-s2-v1, lineare-funktionen-e4-k1-s2-v3 – `Eine Gerade hat die Steigung m=#.Sie geht durch den Punkt P(#|#).Bestimme ihre Gleichung.`
- B-740 (5): prozentrechnung-e4-k2-s1-v1, prozentrechnung-e4-k2-s1-v2, prozentrechnung-e4-k2-s1-v3, prozentrechnung-e4-k2-s1-v4, prozentrechnung-e4-k2-s1-v5 – `Ein Händler hat # kg Äpfel verkauft.Das sind #\%seiner Äpfel.Wie viel kg Äpfel hatte er?`
- B-741 (4): prozentrechnung-e2-k2-s0-v1, prozentrechnung-e2-k2-s0-v2, prozentrechnung-e2-k2-s0-v3, prozentrechnung-e2-k2-s0-v4 – `Teile den Streifen in gleiche Teile ein.Jeder Teil soll #\%sein.‖Grafik:\streifenleer[#]`
- B-742 (3): flaechen-basis-k1-v1, flaechen-basis-k1-v6, flaechen-basis-k1-v9 – `Ein Rechteck hat den Umfang # cm und die Seite a=# cm.Wie lang ist die Seite b?(P# # OS)`
- B-743 (2): reelle-zahlen-e2-k1-s1-v3, reelle-zahlen-e2-k1-s1-v5 – `Schreibe #\cdot #^# als Malkette.Zähle die Faktoren.Schreibe dann alles als eine Potenz.`
- B-744 (2): tangente-normale-schnittwinkel-e1-k1-s0-v2, tangente-normale-schnittwinkel-e1-k1-s0-v4 – `Gegeben ist f(x)=x^#+#x^#-#.Berechne den Anstieg des Graphen von f an der Stelle x_#=-#.`
- B-745 (3): quadratische-gleichungen-e1-k2-s3-v1, quadratische-gleichungen-e1-k2-s3-v2, quadratische-gleichungen-e1-k2-s3-v3 – `Löse die Gleichung x^#=#.Runde auf zwei Stellen nach dem Komma.Gib die Lösungsmenge an.`
- B-746 (3): winkel-dreiecke-e1-k2-s3-v1, winkel-dreiecke-e1-k2-s3-v2, winkel-dreiecke-e1-k2-s3-v3 – `Zeichne an den Strahl mit dem Scheitel S einen Winkel von #^\circ.‖Grafik:\winkelstrahl`
- B-747 (5): potenz-exponentialfunktionen-e2-k1-s1-v1, potenz-exponentialfunktionen-e2-k1-s1-v2, potenz-exponentialfunktionen-e2-k1-s1-v3, potenz-exponentialfunktionen-e2-k1-s1-v4, potenz-exponentialfunktionen-e2-k1-s1-v5 – `Ein Wert steigt jedes Jahr um #\%.Mit welchem Faktor wird er jedes Jahr multipliziert?`
- B-748 (3): winkel-dreiecke-e3-k2-s6-v1, winkel-dreiecke-e3-k2-s6-v2, winkel-dreiecke-e3-k2-s6-v3 – `Ein Viereck hat die Winkel #^\circ,#^\circ und #^\circ.Wie groß ist der vierte Winkel?`
- B-749 (3): zinsrechnung-e1-k1-s6-v1, zinsrechnung-e1-k1-s6-v2, zinsrechnung-e1-k1-s6-v3 – `Die Zinsen für ein Jahr sind #€.Das sind #\%vom Kapital.Wie viel Euro ist das Kapital?`
- B-750 (2): pyramide-kegel-kugel-e1-k5-s13-v2, pyramide-kegel-kugel-e1-k5-s13-v3 – `Eine Pyramide hat das Volumen # m³ und die Grundfläche # m².Wie hoch ist die Pyramide?`
- B-751 (2): quadratische-funktionen-e2-k1-s0-v1, quadratische-funktionen-e2-k1-s0-v3 – `Kreise in f(x)=(x-#)^#+# die Zahl in der Klammer ein.Bei welchem x liegt der Scheitel?`
- B-752 (3): punkte-und-strecken-im-koordinatensystem-e4-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s1-v2, punkte-und-strecken-im-koordinatensystem-e4-k1-s1-v5 – `Zeige:A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)bilden ein Parallelogramm ABCD.(Abitur # LK)`
- B-753 (3): reelle-zahlen-e1-k1-s2-v1, reelle-zahlen-e1-k1-s2-v2, reelle-zahlen-e1-k1-s2-v3 – `Kreuze an,ob\sqrt{#}rational oder irrational ist.\\kreuz{rational}\\kreuz{irrational}`
- B-754 (2): rationale-zahlen-e3-k1-s7-v1, rationale-zahlen-e3-k1-s7-v2 – `Berechne ohne Taschenrechner den Wert von\frac{a+b}{c}für a=# b=-# und c=-#.(P# # OS)`
- B-755 (2): uneigentliche-integrale-e2-k1-s1-v3, uneigentliche-integrale-e2-k1-s1-v5 – `F ist eine Stammfunktion von f(x)=#e^{-#x}.Was bedeutet F(w)-F(#)für w># geometrisch?`
- B-756 (2): prozentrechnung-basis-k3-v4, prozentrechnung-basis-k3-v8 – `Ein Guthaben von #€bringt in einem Jahr #€Zinsen.Wie hoch ist der Zinssatz?(P# # OS)`
- B-757 (2): lineare-funktionen-e2-k2-s0-v1, lineare-funktionen-e2-k2-s0-v3 – `Kreuze an,ob die Gerade zu f(x)=#x-# steigt oder fällt.\\kreuz{steigt}\\kreuz{fällt}`
- B-758 (2): potenz-exponentialfunktionen-e4-k1-s1-v2, potenz-exponentialfunktionen-e4-k1-s1-v4 – `Eine Menge startet bei #\mathrm{mg}.Welchen Wert hat sie,wenn sie sich halbiert hat?`
- B-759 (2): rotationsvolumen-zone-f5-v1, rotationsvolumen-zone-f5-v2 – `Kugel mit Radius # cm,ebener Schnitt # cm vom Mittelpunkt–Radius des Schnittkreises?`
- B-760 (5): trigonometrie-e4-k1-s1-v1, trigonometrie-e4-k1-s1-v2, trigonometrie-e4-k1-s1-v3, trigonometrie-e4-k1-s1-v4, trigonometrie-e4-k1-s1-v5 – `Im Dreieck ABC ist a=# cm,\alpha=#^\circ und\beta=#^\circ.Wie lang ist die Seite b?`
- B-761 (3): koerper-e2-k1-s1-v1, koerper-e2-k1-s1-v2, koerper-e2-k1-s1-v5 – `Ein Quader ist # cm lang,# cm breit und # cm hoch.Berechne das Volumen des Quaders.`
- B-762 (3): trigonometrische-funktionen-e1-k1-s6-v1, trigonometrische-funktionen-e1-k1-s6-v2, trigonometrische-funktionen-e1-k1-s6-v3 – `Ein Winkel ist #°groß.Welches Vorzeichen haben sein Sinuswert und sein Kosinuswert?`
- B-763 (2): koerper-e3-k1-s10-v1, koerper-e3-k1-s10-v2 – `Ein Prisma hat das Volumen # cm³ und die Grundfläche # cm².Wie hoch ist das Prisma?`
- B-764 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v5 – `Sind\vec{u}=(#|#|-#)und\vec{v}=(#|#|-#)kollinear?Gib gegebenenfalls den Faktor an.`
- B-765 (2): zinsrechnung-e1-k1-s12-v3, zinsrechnung-e1-k1-s12-v4 – `Ein Sparguthaben von #€bringt in einem Jahr #€Zinsen.Gib den Zinssatz an.(P# # OS)`
- B-766 (5): strahlensaetze-e1-k2-s1-v1, strahlensaetze-e1-k2-s1-v2, strahlensaetze-e1-k2-s1-v3, strahlensaetze-e1-k2-s1-v4, strahlensaetze-e1-k2-s1-v5 – `Ein Plan hat den Maßstab #:#.Wie lang ist #\text{cm}auf dem Plan in Wirklichkeit?`
- B-767 (3): quadratische-gleichungen-e4-k1-s3-v1, quadratische-gleichungen-e4-k1-s3-v2, quadratische-gleichungen-e4-k1-s3-v3 – `Das Produkt einer Zahl x mit ihrem Nachfolger ist #.Welche Zahlen können es sein?`
- B-768 (3): rationale-zahlen-e4-k1-s1-v1, rationale-zahlen-e4-k1-s1-v2, rationale-zahlen-e4-k1-s1-v4 – `Ein Konto steht bei-#€.Dann werden #€eingezahlt.Wie hoch ist der neue Kontostand?`
- B-769 (2): prozentrechnung-e1-k2-s1-v1, prozentrechnung-e1-k2-s1-v2 – `Ordne die Zahlen der Größe nach,die kleinste zuerst.#;\frac{#}{#};#\%;\frac{#}{#}`
- B-770 (2): quadratische-funktionen-e4-k1-s6-v1, quadratische-funktionen-e4-k1-s6-v3 – `Berechne die Nullstellen von f(x)=x^#-#x+#.Runde auf zwei Stellen nach dem Komma.`
- B-771 (2): trigonometrie-e4-k1-s12-v1, trigonometrie-e4-k1-s12-v2 – `Im Dreieck ABC ist a=# cm,\alpha=#^\circ und b=# cm.Wie groß ist der Winkel\beta?`
- B-772 (3): quadratische-gleichungen-e5-k1-s1-v1, quadratische-gleichungen-e5-k1-s1-v2, quadratische-gleichungen-e5-k1-s1-v4 – `Löse die Bruchgleichung\frac{x}{#}=\frac{#}{x}.Gib zuerst die verbotene Zahl an.`
- B-773 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v3, linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v4 – `Sind\vec{u}=(#|#|#)und\vec{v}=(#|#|#)kollinear?Gib gegebenenfalls den Faktor an.`
- B-774 (2): quadratische-gleichungen-e5-k1-s1-v3, quadratische-gleichungen-e5-k1-s1-v5 – `Löse die Bruchgleichung\frac{#}{x}=\frac{x}{#}.Gib zuerst die verbotene Zahl an.`
- B-775 (2): rationale-zahlen-e1-k1-s6-v3, rationale-zahlen-e1-k1-s6-v4 – `Ordne die Zahlen der Größe nach,die kleinste zuerst:-\frac{#}{#};#;-#;#(P# # OS)`
- B-776 (2): rationale-zahlen-e4-k1-s1-v3, rationale-zahlen-e4-k1-s1-v5 – `Ein Konto steht bei-#€.Dann werden #€abgebucht.Wie hoch ist der neue Kontostand?`
- B-777 (5): quadratische-gleichungen-e4-k1-s1-v1, quadratische-gleichungen-e4-k1-s1-v2, quadratische-gleichungen-e4-k1-s1-v3, quadratische-gleichungen-e4-k1-s1-v4, quadratische-gleichungen-e4-k1-s1-v5 – `Das Quadrat einer Zahl x ist #.Es gilt also x^#=#.Welche Zahlen können es sein?`
- B-778 (3): funktionsklassen-und-eigenschaften-e5-k1-s1-v1, funktionsklassen-und-eigenschaften-e5-k1-s1-v3, funktionsklassen-und-eigenschaften-e5-k1-s1-v5 – `Beschreibe,wie der Graph von g(x)=#\cdot f(x)+# aus dem Graphen von f entsteht.`
- B-779 (3): potenzen-wurzeln-e3-k2-s3-v1, potenzen-wurzeln-e3-k2-s3-v2, potenzen-wurzeln-e3-k2-s3-v3 – `Zwischen welchen ganzen Zahlen liegt\sqrt{#}?Prüfe dann mit dem Taschenrechner.`
- B-780 (3): prozentrechnung-e2-k4-s1-v1, prozentrechnung-e2-k4-s1-v2, prozentrechnung-e2-k4-s1-v3 – `Der Teil soll #\%vom Ganzen sein.Gib dafür ein Beispiel mit Teil und Ganzem an.`
- B-781 (3): zufallsgroessen-und-verteilungen-e2-k1-s1-v1, zufallsgroessen-und-verteilungen-e2-k1-s1-v2, zufallsgroessen-und-verteilungen-e2-k1-s1-v3 – `X nimmt die Werte # bis # an,die Verteilung ist symmetrisch,P(X=#)=#–P(X\le #)?`
- B-782 (2): brueche-dezimalzahlen-e4-k1-s2-v1, brueche-dezimalzahlen-e4-k1-s2-v2 – `Eine Zahl hat # Einer,# Zehntel und # Hundertstel.Schreibe sie als Dezimalzahl.`
- B-783 (2): funktionsklassen-und-eigenschaften-e5-k1-s1-v2, funktionsklassen-und-eigenschaften-e5-k1-s1-v4 – `Beschreibe,wie der Graph von g(x)=#\cdot f(x)-# aus dem Graphen von f entsteht.`
- B-784 (2): pyramide-kegel-kugel-e1-k5-s1-v1, pyramide-kegel-kugel-e1-k5-s1-v4 – `Eine Pyramide hat die Grundfläche # cm² und die Höhe # cm.Berechne ihr Volumen.`
- B-785 (2): reelle-zahlen-e1-k1-s0-v1, reelle-zahlen-e1-k1-s0-v2 – `Kreuze an,ob die Wurzel\sqrt{#}aufgeht.\\kreuz{geht auf}\\kreuz{geht nicht auf}`
- B-786 (2): zinsrechnung-e1-k2-s4-v1, zinsrechnung-e1-k2-s4-v3 – `Ein Konto mit #€bringt in # Monaten #€Zinsen.Wie hoch ist der Zinssatz im Jahr?`
- B-787 (2): zinsrechnung-zone-f6-v1, zinsrechnung-zone-f6-v2 – `Ein Wert steigt um #\%.Mit welcher Zahl musst du den alten Wert multiplizieren?`
- B-788 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s1-v2, flaecheninhalt-und-volumen-im-raum-e1-k2-s1-v3 – `P(#|#|#),Q(#|#|#),R(#|-#|#),rechtwinklig bei Q.Flächeninhalt des Dreiecks PQR?`
- B-789 (2): potenzen-wurzeln-e1-k3-s0-v3, potenzen-wurzeln-e1-k3-s0-v4 – `Gib an,welche Zahl in #^# die Basis ist und welche der Exponent(die Hochzahl).`
- B-790 (3): punkte-und-strecken-im-koordinatensystem-e3-k1-s2-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s2-v2, punkte-und-strecken-im-koordinatensystem-e3-k1-s2-v3 – `Prüfe,ob das Dreieck A(#|#|#),B(#|#|#),C(#|#|#)gleichseitig ist.(Abitur # GK)`
- B-791 (3): reelle-zahlen-e3-k1-s4-v1, reelle-zahlen-e3-k1-s4-v2, reelle-zahlen-e3-k1-s4-v3 – `Ziehe aus\sqrt{#}teilweise die Wurzel.Suche dazu eine Quadratzahl als Faktor.`
- B-792 (2): potenz-exponentialfunktionen-e5-k2-s0-v3, potenz-exponentialfunktionen-e5-k2-s0-v4 – `Kreuze an,ob(-#)^{#}positiv oder negativ ist.\\kreuz{positiv}\\kreuz{negativ}`
- B-793 (2): potenzen-wurzeln-e2-k1-s18-v1, potenzen-wurzeln-e2-k1-s18-v2 – `Setze die fehlende Hochzahl in das Kästchen ein.#=#\cdot #^{\square}(P# # OS)`
- B-794 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s3-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s3-v3 – `Zeige:A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)bilden eine Raute ABCD.(Abitur # GK)`
- B-795 (2): pyramide-kegel-kugel-e1-k5-s1-v2, pyramide-kegel-kugel-e1-k5-s1-v5 – `Eine Pyramide hat die Grundfläche # m² und die Höhe # m.Berechne ihr Volumen.`
- B-796 (2): reelle-zahlen-e1-k1-s8-v1, reelle-zahlen-e1-k1-s8-v4 – `Berechne\sqrt{#}\cdot\sqrt{#}genau.Ist das Ergebnis rational oder irrational?`
- B-797 (2): trigonometrische-funktionen-e3-k1-s2-v1, trigonometrische-funktionen-e3-k1-s2-v2 – `Eine Welle hat die Gleichung y=#·sin(x).Zwischen welchen Werten schwingt sie?`
- B-798 (3): koerper-e2-k1-s4-v1, koerper-e2-k1-s4-v2, koerper-e2-k1-s4-v3 – `Ein Quader ist # cm lang,# cm breit und # cm hoch.Berechne seine Oberfläche.`
- B-799 (3): potenzen-wurzeln-e3-k2-s8-v1, potenzen-wurzeln-e3-k2-s8-v2, potenzen-wurzeln-e3-k2-s8-v3 – `Welcher der beiden Terme\sqrt{-#}und-\sqrt{#}hat einen Wert?Gib den Wert an.`
- B-800 (2): lineare-funktionen-e2-k4-s1-v1, lineare-funktionen-e2-k4-s1-v4 – `Fülle die Wertetabelle zu f(x)=#x-# aus.‖Grafik:\wertetabelle{x}{f(x)}{-#,#}`
- B-801 (2): trigonometrie-e4-k1-s13-v1, trigonometrie-e4-k1-s13-v2 – `Im Dreieck ABC ist a=# cm,b=# cm und\gamma=#^\circ.Wie lang ist die Seite c?`
- B-802 (5): daten-e3-k1-s1-v1, daten-e3-k1-s1-v2, daten-e3-k1-s1-v3, daten-e3-k1-s1-v4, daten-e3-k1-s1-v5 – `Färbe #\%des Streifens.Wie lang ist der gefärbte Teil?‖Grafik:\streifenleer`
- B-803 (3): winkel-dreiecke-e1-k2-s2-v1, winkel-dreiecke-e1-k2-s2-v2, winkel-dreiecke-e1-k2-s2-v3 – `Miss den stumpfen Winkel α mit dem Geodreieck.‖Grafik:\winkel[#]{#}{\alpha}`
- B-804 (2): terme-basis-k1-v1, terme-basis-k1-v4 – `Vereinfache den Term #x-#x^#-#x und berechne seinen Wert für x=#.(P# # GYM)`
- B-805 (2): potenzen-wurzeln-e1-k3-s16-v5, potenzen-wurzeln-e1-k3-s16-v6 – `Hier stehen drei Zahlen:#^# #^# #^#.Unterstreiche die größte Zahl.(P# # OS)`
- B-806 (2): potenzen-wurzeln-e3-k2-s15-v5, potenzen-wurzeln-e3-k2-s15-v6 – `Ordne diese Zahlen von klein nach groß:\sqrt{#};-\frac{#}{#};#;-#.(P# # OS)`
- B-807 (3): potenz-exponentialfunktionen-e4-k1-s1-v1, potenz-exponentialfunktionen-e4-k1-s1-v3, potenz-exponentialfunktionen-e4-k1-s1-v5 – `Ein Bestand startet bei #.Welchen Wert hat er,wenn er sich verdoppelt hat?`
- B-808 (3): trigonometrie-e4-k1-s14-v1, trigonometrie-e4-k1-s14-v2, trigonometrie-e4-k1-s14-v3 – `Im Dreieck ABC ist a=# cm,b=# cm und c=# cm.Wie groß ist der Winkel\gamma?`
- B-809 (2): brueche-dezimalzahlen-e4-k1-s7-v1, brueche-dezimalzahlen-e4-k1-s7-v3 – `Schreibe\frac{#}{#}als Dezimalzahl.Teile dazu den Zähler durch den Nenner.`
- B-810 (2): reelle-zahlen-e1-k1-s6-v1, reelle-zahlen-e1-k1-s6-v2 – `Ordne die Zahlen von der kleinsten bis zur größten:\sqrt{#};#;#\frac{#}{#}`
- B-811 (2): symmetrie-abbildungen-e2-k2-s1-v1, symmetrie-abbildungen-e2-k2-s1-v4 – `Zeichne die Symmetrieachse der Figur im Bild ein.‖Grafik:\drachen{#}{#}{#}`
- B-812 (3): bruchrechnung-e1-k3-s3-v1, bruchrechnung-e1-k3-s3-v2, bruchrechnung-e1-k3-s3-v3 – `Berechne.Schreibe das Ergebnis als gemischte Zahl.\frac{#}{#}+\frac{#}{#}`
- B-813 (4): funktionsklassen-und-eigenschaften-e3-k1-s1-v1, funktionsklassen-und-eigenschaften-e3-k1-s1-v2, funktionsklassen-und-eigenschaften-e3-k1-s1-v4, funktionsklassen-und-eigenschaften-e3-k1-s1-v5 – `Gib den größtmöglichen Definitionsbereich von f(x)=\mathrm{ln}(#x-#)an.`
- B-814 (3): quadratische-funktionen-e1-k1-s1-v2, quadratische-funktionen-e1-k1-s1-v4, quadratische-funktionen-e1-k1-s1-v5 – `Fülle die Wertetabelle zu f(x)=x^# aus.\wertetabelle{x}{f(x)}{-#-#-#,#}`
- B-815 (2): bruchrechnung-e1-k3-s2-v1, bruchrechnung-e1-k3-s2-v3 – `Berechne.Kürze das Ergebnis so weit wie möglich.\frac{#}{#}+\frac{#}{#}`
- B-816 (2): lineare-gleichungen-e2-k2-s0-v1, lineare-gleichungen-e2-k2-s0-v3 – `Du willst die Gleichung #x+#=# lösen.Welche Umformung machst du zuerst?`
- B-817 (2): potenz-exponentialfunktionen-e5-k1-s3-v2, potenz-exponentialfunktionen-e5-k1-s3-v3 – `Fülle die Wertetabelle zu g(x)=x^# aus.\wertetabelle{x}{g(x)}{-#-#,#,#}`
- B-818 (3): bruchrechnung-e3-k2-s2-v1, bruchrechnung-e3-k2-s2-v2, bruchrechnung-e3-k2-s2-v3 – `Berechne\frac{#}{#}:#.Kontrolliere dein Ergebnis mit einer Malaufgabe.`
- B-819 (3): quadratische-funktionen-e1-k1-s6-v1, quadratische-funktionen-e1-k1-s6-v2, quadratische-funktionen-e1-k1-s6-v3 – `Fülle die Wertetabelle zu f(x)=#x^# aus.\wertetabelle{x}{f(x)}{-#-#,#}`
- B-820 (2): binomische-formeln-zone-f6-v1, binomische-formeln-zone-f6-v2 – `Eine Parabel hat die Gleichung y=(x-#)^#+#.Gib ihren Scheitelpunkt an.`
- B-821 (2): bruchrechnung-e1-k1-s0-v1, bruchrechnung-e1-k1-s0-v2 – `Kreuze an,ob du\frac{#}{#}+\frac{#}{#}sofort ausrechnen darfst.\janein`
- B-822 (2): bruchrechnung-e1-k1-s0-v3, bruchrechnung-e1-k1-s0-v4 – `Kreuze an,ob du\frac{#}{#}-\frac{#}{#}sofort ausrechnen darfst.\janein`
- B-823 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s3-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s3-v2 – `Sind\vec{a}=(#|#|#),\vec{b}=(#|#|#)und\vec{c}=(#|#|#)linear abhängig?`
- B-824 (2): spiegelung-e2-k1-s1-v1, spiegelung-e2-k1-s1-v3 – `Q(#|#|#)ist das Spiegelbild von P(#|#|#).Bestimme die Spiegelebene E.`
- B-825 (3): potenzen-wurzeln-e2-k1-s8-v1, potenzen-wurzeln-e2-k1-s8-v2, potenzen-wurzeln-e2-k1-s8-v3 – `Setze die fehlende Hochzahl in das Kästchen ein.#=#\cdot #^{\square}`
- B-826 (3): zinsrechnung-e1-k1-s4-v1, zinsrechnung-e1-k1-s4-v2, zinsrechnung-e1-k1-s4-v3 – `#€Kapital bringen in einem Jahr #€Zinsen.Wie hoch ist der Zinssatz?`
- B-827 (2): matrizen-und-uebergangsprozesse-e2-k1-s2-v1, matrizen-und-uebergangsprozesse-e2-k1-s2-v2 – `Bestimme alle Vektoren v mit M\cdot v=#\cdot v für M=((#|#),(#|#)).`
- B-828 (5): winkel-dreiecke-e1-k2-s1-v1, winkel-dreiecke-e1-k2-s1-v2, winkel-dreiecke-e1-k2-s1-v3, winkel-dreiecke-e1-k2-s1-v4, winkel-dreiecke-e1-k2-s1-v5 – `Miss den Winkel α mit dem Geodreieck.‖Grafik:\winkel[#]{#}{\alpha}`
- B-829 (4): koerper-basis-k3-v1, koerper-basis-k3-v2, koerper-basis-k3-v6, koerper-basis-k3-v10 – `Ein Würfel hat die Kantenlänge # cm.Gib sein Volumen an.(P# # FOR)`
- B-830 (3): bruchrechnung-e3-k2-s3-v1, bruchrechnung-e3-k2-s3-v2, bruchrechnung-e3-k2-s3-v3 – `Berechne #:\frac{#}{#}.Überlege dazu,wie oft\frac{#}{#}in # passt.`
- B-831 (3): potenzen-wurzeln-e1-k3-s9-v1, potenzen-wurzeln-e1-k3-s9-v2, potenzen-wurzeln-e1-k3-s9-v3 – `Hier stehen drei Zahlen:#^# #^# #^#.Unterstreiche die größte Zahl.`
- B-832 (3): reelle-zahlen-e3-k1-s10-v1, reelle-zahlen-e3-k1-s10-v2, reelle-zahlen-e3-k1-s10-v3 – `Schreibe\frac{#}{\sqrt{#}}so um,dass im Nenner keine Wurzel steht.`
- B-833 (2): quadratische-funktionen-e3-k1-s1-v1, quadratische-funktionen-e3-k1-s1-v3 – `Gib den Schnittpunkt der Parabel f(x)=x^#+#x+# mit der y-Achse an.`
- B-834 (2): quadratische-funktionen-e3-k1-s1-v2, quadratische-funktionen-e3-k1-s1-v4 – `Gib den Schnittpunkt der Parabel f(x)=x^#-#x+# mit der y-Achse an.`
- B-835 (3): kurvenuntersuchung-e3-k2-s1-v1, kurvenuntersuchung-e3-k2-s1-v3, kurvenuntersuchung-e3-k2-s1-v5 – `Bilde die erste,zweite und dritte Ableitung von f(x)=x^#+#x^#-#x.`
- B-836 (2): kurvenuntersuchung-e3-k2-s1-v2, kurvenuntersuchung-e3-k2-s1-v4 – `Bilde die erste,zweite und dritte Ableitung von f(x)=x^#-#x^#-#x.`
- B-837 (2): linearkombination-und-lineare-abhaengigkeit-zone-f4-v1, linearkombination-und-lineare-abhaengigkeit-zone-f4-v2 – `Ist(#|#)ein Vielfaches von(#|#)?Gib gegebenenfalls den Faktor an.`
- B-838 (2): potenzen-wurzeln-e3-k2-s5-v1, potenzen-wurzeln-e3-k2-s5-v3 – `Ordne diese Zahlen von klein nach groß:\sqrt{#};#;\frac{#}{#};-#.`
- B-839 (2): vektoren-und-rechenoperationen-e2-k1-s8-v2, vektoren-und-rechenoperationen-e2-k1-s8-v3 – `Q liegt von L(#|#|#)aus im Abstand # in Richtung\vec r=(#|#|#):Q?`
- B-840 (2): bruchrechnung-e5-k1-s6-v3, bruchrechnung-e5-k1-s6-v4 – `Berechne den Wert des Terms(a+b):c für a=# b=# und c=#.(P# # OS)`
- B-841 (4): bruchrechnung-e4-k1-s0-v1, bruchrechnung-e4-k1-s0-v2, bruchrechnung-e4-k1-s0-v3, bruchrechnung-e4-k1-s0-v4 – `Wie viele Stellen nach dem Komma hat das Ergebnis von #\cdot #?`
- B-842 (3): reelle-zahlen-e1-k2-s1-v1, reelle-zahlen-e1-k2-s1-v2, reelle-zahlen-e1-k2-s1-v3 – `Schreibe die Dezimalzahl # als Bruch.Kürze so weit wie möglich.`
- B-843 (2): brueche-dezimalzahlen-basis-k3-v3, brueche-dezimalzahlen-basis-k3-v7 – `Welche Zahl liegt genau in der Mitte zwischen # und #?(P# # OS)`
- B-844 (2): brueche-dezimalzahlen-basis-k3-v6, brueche-dezimalzahlen-basis-k3-v8 – `Welche Zahl liegt genau in der Mitte zwischen-# und #?(P# # OS)`
- B-845 (2): normalverteilung-und-sigma-regeln-zone-f1-v1, normalverteilung-und-sigma-regeln-zone-f1-v2 – `X nimmt # und # je mit Wahrscheinlichkeit # an.Erwartungswert?`
- B-846 (2): potenzen-wurzeln-e1-k3-s16-v7, potenzen-wurzeln-e1-k3-s16-v8 – `Setze das passende Zeichen<,=oder>ein.#^{-#}\square #(P# # OS)`
- B-847 (2): stammfunktion-und-hauptsatz-e2-k1-s1-v1, stammfunktion-und-hauptsatz-e2-k1-s1-v2 – `Berechne den Wert des Integrals von-# bis # über f(x)=#x^#+#x.`
- B-848 (2): brueche-dezimalzahlen-e5-k2-s10-v3, brueche-dezimalzahlen-e5-k2-s10-v4 – `Ordne von klein nach groß:-\frac{#}{#};#;-#;\sqrt{#}(P# # OS)`
- B-849 (2): potenz-exponentialfunktionen-e5-k2-s5-v1, potenz-exponentialfunktionen-e5-k2-s5-v2 – `Die Funktion lautet f(x)=x^#.Für welche Zahlen x gilt f(x)=#?`
- B-850 (2): potenz-exponentialfunktionen-e5-k2-s7-v1, potenz-exponentialfunktionen-e5-k2-s7-v3 – `Die Funktion lautet g(x)=x^#.Für welche Zahlen x gilt g(x)=#?`
- B-851 (2): quadratische-gleichungen-e3-k3-s13-v1, quadratische-gleichungen-e3-k3-s13-v3 – `Prüfe durch Einsetzen,ob x=-# eine Lösung von x^#-#x-#=# ist.`
- B-852 (2): reelle-zahlen-e2-k1-s6-v2, reelle-zahlen-e2-k1-s6-v3 – `Berechne #^#:#^#.Entscheide vorher,ob ein Potenzgesetz hilft.`
- B-853 (4): matrizen-und-uebergangsprozesse-e2-k1-s1-v1, matrizen-und-uebergangsprozesse-e2-k1-s1-v2, matrizen-und-uebergangsprozesse-e2-k1-s1-v3, matrizen-und-uebergangsprozesse-e2-k1-s1-v5 – `Bestimme alle Vektoren v mit M\cdot v=v für M=((#|#),(#|#)).`
- B-854 (2): quadratische-gleichungen-e2-k1-s2-v1, quadratische-gleichungen-e2-k1-s2-v3 – `Löse die Gleichung(x+#)\cdot(x-#)=#.Gib die Lösungsmenge an.`
- B-855 (2): rationale-zahlen-e3-k1-s7-v3, rationale-zahlen-e3-k1-s7-v4 – `Berechne den Wert von(a+b):c für a=# b=-# und c=-#.(P# # OS)`
- B-856 (2): binomische-formeln-e3-k1-s0-v1, binomische-formeln-e3-k1-s0-v4 – `Kreuze an,ob #x^# ein Quadrat ist.Rechne nichts aus.\janein`
- B-857 (2): funktionsklassen-und-eigenschaften-e4-k1-s1-v3, funktionsklassen-und-eigenschaften-e4-k1-s1-v5 – `Untersuche f(x)=#x^#-#x^#+# auf Symmetrie.Begründe am Term.`
- B-858 (2): rotationsvolumen-e1-k1-s1-v2, rotationsvolumen-e1-k1-s1-v3 – `f(x)=#x+# rotiert über[#;#]um die x-Achse–Rotationsvolumen?`
- B-859 (4): potenzen-wurzeln-e1-k3-s16-v1, potenzen-wurzeln-e1-k3-s16-v2, potenzen-wurzeln-e1-k3-s16-v3, potenzen-wurzeln-e1-k3-s16-v4 – `Welche Zahl muss für x stehen,damit #^x=# stimmt?(P# # OS)`
- B-860 (3): funktionsklassen-und-eigenschaften-e4-k1-s1-v1, funktionsklassen-und-eigenschaften-e4-k1-s1-v2, funktionsklassen-und-eigenschaften-e4-k1-s1-v4 – `Untersuche f(x)=x^#-#x^#+# auf Symmetrie.Begründe am Term.`
- B-861 (2): gleichungen-loesen-e2-k1-s2-v1, gleichungen-loesen-e2-k1-s2-v2 – `f(x)=#e^{#x}-#.Bestimme die Nullstelle exakt.(Abitur # LK)`
- B-862 (2): rationale-zahlen-e2-k3-s6-v1, rationale-zahlen-e2-k3-s6-v3 – `Wie weit liegen-# und # auf der Zahlengeraden auseinander?`
- B-863 (3): potenzen-wurzeln-e2-k1-s6-v1, potenzen-wurzeln-e2-k1-s6-v2, potenzen-wurzeln-e2-k1-s6-v3 – `Schreibe #\cdot #^{#}als Zahl ohne Zehnerpotenz.(P# # OS)`
- B-864 (2): flaecheninhalt-und-volumen-im-raum-zone-f5-v1, flaecheninhalt-und-volumen-im-raum-zone-f5-v2 – `Rechtwinkliges Dreieck,Katheten # cm und # cm.Hypotenuse?`
- B-865 (2): koerper-e2-k3-s1-v1, koerper-e2-k3-s1-v2 – `Ein Würfel hat das Volumen # cm³.Wie lang ist eine Kante?`
- B-866 (2): quadratische-gleichungen-e2-k1-s3-v1, quadratische-gleichungen-e2-k1-s3-v3 – `Löse die Gleichung x\cdot(x+#)=#.Gib die Lösungsmenge an.`
- B-867 (2): reelle-zahlen-e3-k1-s2-v1, reelle-zahlen-e3-k1-s2-v2 – `Berechne\sqrt{\frac{#}{#}}.Gib das Ergebnis als Bruch an.`
- B-868 (3): reelle-zahlen-e2-k1-s4-v1, reelle-zahlen-e2-k1-s4-v2, reelle-zahlen-e2-k1-s4-v3 – `Schreibe(#^#)^# als eine Potenz und berechne ihren Wert.`
- B-869 (2): lineare-gleichungen-e2-k3-s8-v1, lineare-gleichungen-e2-k3-s8-v2 – `Löse die Gleichung und mache die Probe.#(x+#)=#(P# # OS)`
- B-870 (2): grenzwerte-und-verhalten-im-unendlichen-e2-k1-s1-v2, grenzwerte-und-verhalten-im-unendlichen-e2-k1-s1-v4 – `f(x)=e^{-#x}.Verhalten für x\to+\infty und x\to-\infty?`
- B-871 (2): potenzen-wurzeln-e3-k2-s4-v1, potenzen-wurzeln-e3-k2-s4-v3 – `Setze das passende Zeichen<,=oder>ein.\sqrt{#}\square #`
- B-872 (2): terme-e5-k1-s4-v1, terme-e5-k1-s4-v3 – `Berechne den Wert des Terms #x^#+#x für x=-\frac{#}{#}.`
- B-873 (2): wahrscheinlichkeit-zone-f1-v1, wahrscheinlichkeit-zone-f1-v2 – `Kürze\frac{#}{#}und schreibe den Bruch als Prozentsatz.`
- B-874 (3): brueche-dezimalzahlen-e5-k2-s6-v1, brueche-dezimalzahlen-e5-k2-s6-v2, brueche-dezimalzahlen-e5-k2-s6-v3 – `Welche Zahl liegt genau in der Mitte zwischen # und #?`
- B-875 (2): bruchrechnung-e5-k3-s1-v1, bruchrechnung-e5-k3-s1-v3 – `Prüfe mit einem Überschlag,ob #\cdot #=# stimmen kann.`
- B-876 (2): rationale-zahlen-e1-k2-s1-v2, rationale-zahlen-e1-k2-s1-v3 – `Welche Zahl liegt genau in der Mitte zwischen-# und-#?`
- B-877 (2): reelle-zahlen-e2-k1-s11-v1, reelle-zahlen-e2-k1-s11-v2 – `Berechne #^#\cdot #^#.Fasse zuerst die Basen zusammen.`
- B-878 (3): potenzen-wurzeln-e1-k3-s14-v1, potenzen-wurzeln-e1-k3-s14-v2, potenzen-wurzeln-e1-k3-s14-v3 – `Setze das passende Zeichen<,=oder>ein.#^{-#}\square #`
- B-879 (2): rationale-zahlen-basis-k3-v3, rationale-zahlen-basis-k3-v7 – `Gib eine Zahl an,die zwischen-# und-# liegt.(P# # OS)`
- B-880 (2): normalverteilung-und-sigma-regeln-zone-f5-v1, normalverteilung-und-sigma-regeln-zone-f5-v2 – `X binomialverteilt mit n=# p=#:P(X=#)mit dem Rechner?`
- B-881 (2): quadratische-gleichungen-e2-k1-s8-v1, quadratische-gleichungen-e2-k1-s8-v2 – `Löse die Gleichung #x^#-#x=#.Gib die Lösungsmenge an.`
- B-882 (2): quadratische-gleichungen-e5-k2-s1-v1, quadratische-gleichungen-e5-k2-s1-v5 – `Löse die Wurzelgleichung\sqrt{x+#}=#.Mache die Probe.`
- B-883 (4): trigonometrie-basis-k1-v1, trigonometrie-basis-k1-v4, trigonometrie-basis-k1-v9, trigonometrie-basis-k1-v10 – `\mathrm{sin}#^\circ=\frac{#}{x}–berechne x.(P# # OS)`
- B-884 (3): rationale-zahlen-basis-k1-v4, rationale-zahlen-basis-k1-v6, rationale-zahlen-basis-k1-v8 – `Berechne den Wert von #\cdot(x+#)für x=-#.(P# # FOR)`
- B-885 (3): brueche-dezimalzahlen-e3-k2-s1-v1, brueche-dezimalzahlen-e3-k2-s1-v2, brueche-dezimalzahlen-e3-k2-s1-v3 – `Gib einen Bruch zwischen\frac{#}{#}und\frac{#}{#}an.`
- B-886 (3): quadratische-gleichungen-e1-k2-s7-v1, quadratische-gleichungen-e1-k2-s7-v2, quadratische-gleichungen-e1-k2-s7-v3 – `Löse die Gleichung #x^#+#=#.Gib die Lösungsmenge an.`
- B-887 (3): quadratische-gleichungen-e2-k1-s6-v1, quadratische-gleichungen-e2-k1-s6-v2, quadratische-gleichungen-e2-k1-s6-v3 – `Löse die Gleichung x^#+#x=#.Gib die Lösungsmenge an.`
- B-888 (3): quadratische-gleichungen-e2-k1-s7-v1, quadratische-gleichungen-e2-k1-s7-v2, quadratische-gleichungen-e2-k1-s7-v3 – `Löse die Gleichung x^#-#x=#.Gib die Lösungsmenge an.`
- B-889 (2): trigonometrie-basis-k1-v2, trigonometrie-basis-k1-v5 – `\mathrm{cos}#^\circ=\frac{#}{x}–berechne x.(P# # OS)`
- B-890 (2): potenzen-wurzeln-e1-k5-s1-v1, potenzen-wurzeln-e1-k5-s1-v3 – `Setze das passende Zeichen<,=oder>ein.#^#\square #\%`
- B-891 (5): trigonometrische-funktionen-e3-k1-s1-v1, trigonometrische-funktionen-e3-k1-s1-v2, trigonometrische-funktionen-e3-k1-s1-v3, trigonometrische-funktionen-e3-k1-s1-v4, trigonometrische-funktionen-e3-k1-s1-v5 – `Wie groß ist die Amplitude der Funktion y=#·sin(x)?`
- B-892 (3): potenz-exponentialfunktionen-e3-k2-s0-v1, potenz-exponentialfunktionen-e3-k2-s0-v2, potenz-exponentialfunktionen-e3-k2-s0-v4 – `Berechne #^#.Runde auf vier Stellen nach dem Komma.`
- B-893 (2): bruchrechnung-e4-k2-s8-v5, bruchrechnung-e4-k2-s8-v6 – `Welcher Wert ist am kleinsten:#;#;#^#;#\%?(P# # OS)`
- B-894 (2): potenzen-wurzeln-e3-k2-s13-v1, potenzen-wurzeln-e3-k2-s13-v2 – `Welche Zahl steht unter der Wurzel?\sqrt{\square}=#`
- B-895 (2): binomische-formeln-e2-k3-s1-v1, binomische-formeln-e2-k3-s1-v2 – `Berechne #^# im Kopf mit einer binomischen Formel.`
- B-896 (2): lagebeziehungen-zone-f2-v1, lagebeziehungen-zone-f2-v2 – `g:\vec{x}=(#|#|#)+t\cdot(#|#|#)–der Punkt für t=#?`
- B-897 (3): lineare-funktionen-e3-k1-s0-v1, lineare-funktionen-e3-k1-s0-v2, lineare-funktionen-e3-k1-s0-v4 – `Setze x=# in den Term #x-# ein.Berechne den Wert.`
- B-898 (3): vektoren-und-rechenoperationen-e1-k2-s2-v1, vektoren-und-rechenoperationen-e1-k2-s2-v2, vektoren-und-rechenoperationen-e1-k2-s2-v3 – `\vec u=(#|#|#),\vec v=(#|#|#):welcher ist länger?`
- B-899 (2): trigonometrische-funktionen-e1-k1-s10-v1, trigonometrische-funktionen-e1-k1-s10-v2 – `Rechne\frac{#}{#}\pi vom Bogenmaß ins Gradmaß um.`
- B-900 (2): brueche-dezimalzahlen-basis-k2-v4, brueche-dezimalzahlen-basis-k2-v5 – `\frac{#}{#}von # kg–wie viel Kilogramm?(P# # OS)`
- B-901 (5): quadratische-funktionen-e2-k1-s1-v1, quadratische-funktionen-e2-k1-s1-v2, quadratische-funktionen-e2-k1-s1-v3, quadratische-funktionen-e2-k1-s1-v4, quadratische-funktionen-e2-k1-s1-v5 – `Gib den Scheitel der Parabel f(x)=(x-#)^#+# an.`
- B-902 (4): stammfunktion-und-hauptsatz-e1-k1-s1-v1, stammfunktion-und-hauptsatz-e1-k1-s1-v2, stammfunktion-und-hauptsatz-e1-k1-s1-v3, stammfunktion-und-hauptsatz-e1-k1-s1-v4 – `Gib eine Stammfunktion F von f(x)=#-(#-x)^# an.`
- B-903 (2): potenzen-wurzeln-e2-k1-s18-v3, potenzen-wurzeln-e2-k1-s18-v4 – `Schreibe #\cdot #^{-#}als Dezimalzahl.(P# # OS)`
- B-904 (10): potenzen-wurzeln-basis-k3-v1, potenzen-wurzeln-basis-k3-v2, potenzen-wurzeln-basis-k3-v3, potenzen-wurzeln-basis-k3-v4, potenzen-wurzeln-basis-k3-v5, potenzen-wurzeln-basis-k3-v6, potenzen-wurzeln-basis-k3-v7, potenzen-wurzeln-basis-k3-v8, potenzen-wurzeln-basis-k3-v9, potenzen-wurzeln-basis-k3-v10 – `#=#\cdot #^{\square}–welche Hochzahl?(P# # OS)`
- B-905 (2): hypergeometrische-verteilung-zone-f4-v1, hypergeometrische-verteilung-zone-f4-v2 – `Berechne und kürze:\frac{#}{#}\cdot\frac{#}{#}`
- B-906 (3): funktionsklassen-und-eigenschaften-e2-k1-s1-v1, funktionsklassen-und-eigenschaften-e2-k1-s1-v3, funktionsklassen-und-eigenschaften-e2-k1-s1-v5 – `Berechne die Nullstellen von f(x)=(x-#)(x+#).`
- B-907 (3): potenzen-wurzeln-e1-k3-s1-v1, potenzen-wurzeln-e1-k3-s1-v2, potenzen-wurzeln-e1-k3-s1-v5 – `Schreibe #^# als Malkette und rechne sie aus.`
- B-908 (3): potenzen-wurzeln-e1-k3-s13-v1, potenzen-wurzeln-e1-k3-s13-v2, potenzen-wurzeln-e1-k3-s13-v3 – `Schreibe #^{-#}als Bruch und als Dezimalzahl.`
- B-909 (2): funktionsklassen-und-eigenschaften-e2-k1-s1-v2, funktionsklassen-und-eigenschaften-e2-k1-s1-v4 – `Berechne die Nullstellen von f(x)=(x-#)(x-#).`
- B-910 (2): lineare-gleichungen-e2-k3-s4-v2, lineare-gleichungen-e2-k3-s4-v3 – `Löse die Gleichung und mache die Probe.#x-#=#`
- B-911 (2): trigonometrische-funktionen-e3-k1-s5-v1, trigonometrische-funktionen-e3-k1-s5-v3 – `Berechne die Periode der Funktion y=sin(#·x).`
- B-912 (3): quadratische-funktionen-e4-k1-s1-v1, quadratische-funktionen-e4-k1-s1-v3, quadratische-funktionen-e4-k1-s1-v5 – `Berechne die Nullstellen von f(x)=(x-#)^#-#.`
- B-913 (2): lineare-gleichungen-basis-k1-v4, lineare-gleichungen-basis-k1-v10 – `Löse die Gleichung #\cdot(x-#)+#=#.(P# # OS)`
- B-914 (2): bruchrechnung-e2-k3-s1-v1, bruchrechnung-e2-k3-s1-v3 – `Überschlage zuerst.Rechne dann genau aus.#+#`
- B-915 (2): quadratische-gleichungen-zone-f6-v1, quadratische-gleichungen-zone-f6-v2 – `Gib den Scheitel der Parabel y=(x-#)^#+# an.`
- B-916 (2): spiegelung-zone-f2-v1, spiegelung-zone-f2-v2 – `Verbindungsvektor von A(#|#|#)nach B(#|#|#)?`
- B-917 (3): ableitungsregeln-e3-k1-s1-v1, ableitungsregeln-e3-k1-s1-v2, ableitungsregeln-e3-k1-s1-v4 – `f(x)=#x^#\cdot e^x–f'(x),e^x ausgeklammert?`
- B-918 (3): quadratische-gleichungen-e1-k2-s4-v1, quadratische-gleichungen-e1-k2-s4-v2, quadratische-gleichungen-e1-k2-s4-v3 – `Hat die Gleichung x^#=-# Lösungen?Begründe.`
- B-919 (2): brueche-dezimalzahlen-basis-k2-v3, brueche-dezimalzahlen-basis-k2-v8 – `\frac{#}{#}von # l–wie viel Liter?(P# # OS)`
- B-920 (2): potenz-exponentialfunktionen-e5-k2-s1-v2, potenz-exponentialfunktionen-e5-k2-s1-v4 – `Die Funktion lautet g(x)=x^#.Berechne g(#).`
- B-921 (2): punkte-und-strecken-im-koordinatensystem-zone-f8-v1, punkte-und-strecken-im-koordinatensystem-zone-f8-v2 – `Ist(#|#|#)ein Vielfaches von(#|#|#)?Faktor?`
- B-922 (4): lineare-gleichungen-basis-k1-v1, lineare-gleichungen-basis-k1-v2, lineare-gleichungen-basis-k1-v5, lineare-gleichungen-basis-k1-v6 – `Löse die Gleichung #\cdot(x-#)=#.(P# # OS)`
- B-923 (2): lineare-gleichungen-basis-k1-v3, lineare-gleichungen-basis-k1-v9 – `Löse die Gleichung #\cdot(x+#)=#.(P# # OS)`
- B-924 (2): rationale-zahlen-e1-k1-s2-v1, rationale-zahlen-e1-k1-s2-v3 – `Gib die Gegenzahl und den Betrag von-# an.`
- B-925 (2): terme-e5-k1-s2-v1, terme-e5-k1-s2-v3 – `Berechne den Wert des Terms #x+# für x=-#.`
- B-926 (5): terme-e5-k1-s1-v1, terme-e5-k1-s1-v2, terme-e5-k1-s1-v3, terme-e5-k1-s1-v4, terme-e5-k1-s1-v5 – `Berechne den Wert des Terms #x-# für x=#.`
- B-927 (3): gleichungen-loesen-e2-k1-s1-v1, gleichungen-loesen-e2-k1-s1-v3, gleichungen-loesen-e2-k1-s1-v5 – `Löse:#e^{#x}-#=#.Runde auf zwei Stellen.`
- B-928 (2): lineare-gleichungen-e1-k2-s4-v1, lineare-gleichungen-e1-k2-s4-v3 – `Prüfe,ob # die Gleichung #x-#=#x+# löst.`
- B-929 (3): brueche-dezimalzahlen-e5-k2-s7-v1, brueche-dezimalzahlen-e5-k2-s7-v2, brueche-dezimalzahlen-e5-k2-s7-v3 – `Setze<,=oder>ein:\frac{#}{#}\leerfeld #`
- B-930 (2): quadratische-funktionen-e3-k1-s13-v1, quadratische-funktionen-e3-k1-s13-v2 – `Weise nach:(x+#)^#-#=x^#+#x+#.(P# # OS)`
- B-931 (3): potenzen-wurzeln-e2-k1-s10-v1, potenzen-wurzeln-e2-k1-s10-v2, potenzen-wurzeln-e2-k1-s10-v3 – `Schreibe #\cdot #^{-#}als Dezimalzahl.`
- B-932 (2): brueche-dezimalzahlen-e2-k1-s7-v1, brueche-dezimalzahlen-e2-k1-s7-v3 – `Schreibe\frac{#}{#}als gemischte Zahl.`
- B-933 (2): lineare-gleichungssysteme-e1-k1-s2-v1, lineare-gleichungssysteme-e1-k1-s2-v3 – `Stelle die Gleichung #x+y=# nach y um.`
- B-934 (2): bruchrechnung-e3-k1-s5-v1, bruchrechnung-e3-k1-s5-v2 – `Berechne.#\frac{#}{#}\cdot\frac{#}{#}`
- B-935 (2): potenzen-wurzeln-e2-k1-s1-v1, potenzen-wurzeln-e2-k1-s1-v2 – `Schreibe #^{#}als Zahl ohne Hochzahl.`
- B-936 (5): lineare-gleichungen-e1-k2-s1-v1, lineare-gleichungen-e1-k2-s1-v2, lineare-gleichungen-e1-k2-s1-v3, lineare-gleichungen-e1-k2-s1-v4, lineare-gleichungen-e1-k2-s1-v5 – `Prüfe,ob # die Gleichung x+#=# löst.`
- B-937 (3): potenzen-wurzeln-e1-k3-s8-v1, potenzen-wurzeln-e1-k3-s8-v2, potenzen-wurzeln-e1-k3-s8-v3 – `Welche Zahl ist größer,#^# oder #^#?`
- B-938 (2): lineare-gleichungen-e3-k2-s5-v1, lineare-gleichungen-e3-k2-s5-v2 – `Löse die Gleichung.\frac{x}{#}+#=x-#`
- B-939 (3): bruchrechnung-e3-k1-s2-v1, bruchrechnung-e3-k1-s2-v2, bruchrechnung-e3-k1-s2-v3 – `Berechne\frac{#}{#}von\frac{#}{#}.`
- B-940 (2): bruchrechnung-e1-k3-s7-v1, bruchrechnung-e1-k3-s7-v3 – `Berechne.#\frac{#}{#}+#\frac{#}{#}`
- B-941 (2): bruchrechnung-e5-k2-s1-v1, bruchrechnung-e5-k2-s1-v3 – `Rechne geschickt:#\cdot #+#\cdot #`
- B-942 (2): brueche-dezimalzahlen-e5-k3-s1-v1, brueche-dezimalzahlen-e5-k3-s1-v2 – `Gib eine Zahl zwischen # und # an.`
- B-943 (2): integrationsregeln-e1-k1-s1-v1, integrationsregeln-e1-k1-s1-v5 – `Gib eine Stammfunktion an:f(x)=x^#`
- B-944 (2): spiegelung-e1-k3-s1-v1, spiegelung-e1-k3-s1-v2 – `Spiegle P(#|#|#)am Punkt Q(#|#|#).`
- B-945 (10): potenzen-wurzeln-basis-k1-v1, potenzen-wurzeln-basis-k1-v2, potenzen-wurzeln-basis-k1-v3, potenzen-wurzeln-basis-k1-v4, potenzen-wurzeln-basis-k1-v5, potenzen-wurzeln-basis-k1-v6, potenzen-wurzeln-basis-k1-v7, potenzen-wurzeln-basis-k1-v8, potenzen-wurzeln-basis-k1-v9, potenzen-wurzeln-basis-k1-v10 – `#^x=#–welche Zahl ist x?(P# # OS)`
- B-946 (5): potenzen-wurzeln-e3-k2-s1-v1, potenzen-wurzeln-e3-k2-s1-v2, potenzen-wurzeln-e3-k2-s1-v3, potenzen-wurzeln-e3-k2-s1-v4, potenzen-wurzeln-e3-k2-s1-v5 – `Berechne\sqrt{#}.Mache die Probe.`
- B-947 (2): binomische-formeln-e1-k1-s6-v1, binomische-formeln-e1-k1-s6-v3 – `Multipliziere aus:(x+#)\cdot(x+#)`
- B-948 (2): binomische-formeln-e1-k1-s8-v1, binomische-formeln-e1-k1-s8-v2 – `Multipliziere aus:(x-#)\cdot(x-#)`
- B-949 (3): potenzen-wurzeln-e3-k2-s6-v1, potenzen-wurzeln-e3-k2-s6-v2, potenzen-wurzeln-e3-k2-s6-v3 – `Berechne\left(\sqrt{#}\right)^#.`
- B-950 (2): lineare-gleichungen-zone-f5-v1, lineare-gleichungen-zone-f5-v2 – `Löse die Klammer auf:#\cdot(x+#)`
- B-951 (3): brueche-dezimalzahlen-e4-k1-s6-v1, brueche-dezimalzahlen-e4-k1-s6-v2, brueche-dezimalzahlen-e4-k1-s6-v3 – `Schreibe # als gekürzten Bruch.`
- B-952 (3): brueche-dezimalzahlen-e5-k2-s9-v1, brueche-dezimalzahlen-e5-k2-s9-v2, brueche-dezimalzahlen-e5-k2-s9-v3 – `Setze<,=oder>ein:#^#\leerfeld #`
- B-953 (2): binomische-formeln-e2-k2-s7-v1, binomische-formeln-e2-k2-s7-v3 – `Multipliziere aus:#\cdot(x+#)^#`
- B-954 (2): brueche-dezimalzahlen-e5-k2-s8-v1, brueche-dezimalzahlen-e5-k2-s8-v3 – `Setze<,=oder>ein:#\leerfeld #\%`
- B-955 (5): terme-e3-k2-s1-v1, terme-e3-k2-s1-v2, terme-e3-k2-s1-v3, terme-e3-k2-s1-v4, terme-e3-k2-s1-v5 – `Löse die Klammer auf:#a+(#b-#)`
- B-956 (2): prozentrechnung-e3-k1-s11-v7, prozentrechnung-e3-k1-s11-v8 – `Berechne #\%von #€.(P# # FOR)`
- B-957 (2): zuordnungen-zone-f3-v1, zuordnungen-zone-f3-v2 – `# ist das Wievielfache von #?`
- B-958 (3): einheiten-e2-k1-s1-v1, einheiten-e2-k1-s1-v3, einheiten-e2-k1-s1-v5 – `Rechne # min in Sekunden um.`
- B-959 (3): potenzen-wurzeln-e2-k1-s1-v3, potenzen-wurzeln-e2-k1-s1-v4, potenzen-wurzeln-e2-k1-s1-v5 – `Schreibe # als Zehnerpotenz.`
- B-960 (2): grenzwerte-und-verhalten-im-unendlichen-zone-f3-v1, grenzwerte-und-verhalten-im-unendlichen-zone-f3-v2 – `y=#^x:Werte für x=# x=# x=#?`
- B-961 (2): prozentrechnung-e3-k1-s11-v5, prozentrechnung-e3-k1-s11-v6 – `Berechne #\%von #€.(P# # OS)`
- B-962 (5): bruchrechnung-e3-k1-s1-v1, bruchrechnung-e3-k1-s1-v2, bruchrechnung-e3-k1-s1-v3, bruchrechnung-e3-k1-s1-v4, bruchrechnung-e3-k1-s1-v5 – `Berechne\frac{#}{#}\cdot #.`
- B-963 (5): quadratische-gleichungen-e5-k3-s1-v1, quadratische-gleichungen-e5-k3-s1-v2, quadratische-gleichungen-e5-k3-s1-v3, quadratische-gleichungen-e5-k3-s1-v4, quadratische-gleichungen-e5-k3-s1-v5 – `Löse die Ungleichung x^#<#.`
- B-964 (2): pyramide-kegel-kugel-zone-f5-v1, pyramide-kegel-kugel-zone-f5-v2 – `Berechne ein Drittel von #.`
- B-965 (2): reelle-zahlen-e2-k1-s9-v1, reelle-zahlen-e2-k1-s9-v3 – `Vereinfache #x^#\cdot #x^#.`
- B-966 (5): binomische-formeln-e1-k1-s1-v1, binomische-formeln-e1-k1-s1-v2, binomische-formeln-e1-k1-s1-v3, binomische-formeln-e1-k1-s1-v4, binomische-formeln-e1-k1-s1-v5 – `Fasse zusammen:#x+#y+#x+#y`
- B-967 (3): potenzen-wurzeln-e1-k3-s2-v1, potenzen-wurzeln-e1-k3-s2-v2, potenzen-wurzeln-e1-k3-s2-v3 – `Berechne #^# und #\cdot #.`
- B-968 (2): ableitungsregeln-e1-k2-s1-v1, ableitungsregeln-e1-k2-s1-v3 – `f(x)=#x^#+#x^#-#x+#–f'(x)?`
- B-969 (2): ableitungsregeln-e1-k2-s1-v2, ableitungsregeln-e1-k2-s1-v5 – `f(x)=#x^#-#x^#-#x+#–f'(x)?`
- B-970 (2): binomische-formeln-e2-k2-s5-v1, binomische-formeln-e2-k2-s5-v3 – `Multipliziere aus:(#x+#)^#`
- B-971 (5): binomische-formeln-e2-k2-s1-v1, binomische-formeln-e2-k2-s1-v2, binomische-formeln-e2-k2-s1-v3, binomische-formeln-e2-k2-s1-v4, binomische-formeln-e2-k2-s1-v5 – `Multipliziere aus:(x+#)^#`
- B-972 (3): binomische-formeln-e2-k2-s2-v1, binomische-formeln-e2-k2-s2-v2, binomische-formeln-e2-k2-s2-v3 – `Multipliziere aus:(x-#)^#`
- B-973 (2): lineare-funktionen-zone-f4-v1, lineare-funktionen-zone-f4-v2 – `Rechne:\frac{#}{#}\cdot #`
- B-974 (2): lineare-funktionen-zone-f5-v1, lineare-funktionen-zone-f5-v2 – `Löse die Gleichung.#=#x-#`
- B-975 (3): lineare-gleichungen-e2-k3-s5-v1, lineare-gleichungen-e2-k3-s5-v2, lineare-gleichungen-e2-k3-s5-v3 – `Löse die Gleichung.#-x=#`
- B-976 (5): terme-e2-k1-s1-v1, terme-e2-k1-s1-v2, terme-e2-k1-s1-v3, terme-e2-k1-s1-v4, terme-e2-k1-s1-v5 – `Multipliziere:#\cdot #x`
- B-977 (3): rationale-zahlen-e3-k1-s5-v1, rationale-zahlen-e3-k1-s5-v2, rationale-zahlen-e3-k1-s5-v3 – `Berechne:(-#)^# und-#^#`
- B-978 (5): bruchrechnung-e3-k2-s1-v1, bruchrechnung-e3-k2-s1-v2, bruchrechnung-e3-k2-s1-v3, bruchrechnung-e3-k2-s1-v4, bruchrechnung-e3-k2-s1-v5 – `Berechne\frac{#}{#}:#.`
- B-979 (4): potenzen-wurzeln-e3-k2-s7-v1, potenzen-wurzeln-e3-k2-s7-v2, potenzen-wurzeln-e3-k2-s7-v3, potenzen-wurzeln-e3-k2-s7-v4 – `Berechne\sqrt{(-#)^#}.`
- B-980 (3): bruchrechnung-e1-k4-s1-v1, bruchrechnung-e1-k4-s1-v2, bruchrechnung-e1-k4-s1-v3 – `Berechne.#+\frac{#}{#}`
- B-981 (3): brueche-dezimalzahlen-e2-k1-s2-v1, brueche-dezimalzahlen-e2-k1-s2-v2, brueche-dezimalzahlen-e2-k1-s2-v3 – `Kürze\frac{#}{#}mit #.`
- B-982 (3): rationale-zahlen-e3-k1-s2-v1, rationale-zahlen-e3-k1-s2-v2, rationale-zahlen-e3-k1-s2-v3 – `Berechne:(-#)\cdot(-#)`
- B-983 (3): binomische-formeln-e3-k1-s3-v1, binomische-formeln-e3-k1-s3-v2, binomische-formeln-e3-k1-s3-v3 – `Faktorisiere:x^#+#x+#`
- B-984 (3): binomische-formeln-e3-k1-s4-v1, binomische-formeln-e3-k1-s4-v2, binomische-formeln-e3-k1-s4-v3 – `Faktorisiere:x^#-#x+#`
- B-985 (2): einheiten-e1-k2-s1-v2, einheiten-e1-k2-s1-v5 – `Rechne # cm in mm um.`
- B-986 (2): einheiten-e3-k1-s6-v1, einheiten-e3-k1-s6-v3 – `Rechne # l in dm³ um.`
- B-987 (5): bruchrechnung-e5-k1-s1-v1, bruchrechnung-e5-k1-s1-v2, bruchrechnung-e5-k1-s1-v3, bruchrechnung-e5-k1-s1-v4, bruchrechnung-e5-k1-s1-v5 – `Berechne #+#\cdot #.`
- B-988 (2): einheiten-e1-k2-s1-v1, einheiten-e1-k2-s1-v4 – `Rechne # m in dm um.`
- B-989 (2): einheiten-e1-k2-s4-v1, einheiten-e1-k2-s4-v3 – `Rechne # km in m um.`
- B-990 (10): prozentrechnung-basis-k4-v1, prozentrechnung-basis-k4-v2, prozentrechnung-basis-k4-v3, prozentrechnung-basis-k4-v4, prozentrechnung-basis-k4-v5, prozentrechnung-basis-k4-v6, prozentrechnung-basis-k4-v7, prozentrechnung-basis-k4-v8, prozentrechnung-basis-k4-v9, prozentrechnung-basis-k4-v10 – `#\%von #€(P# # FOR)`
- B-991 (5): rationale-zahlen-e3-k1-s1-v1, rationale-zahlen-e3-k1-s1-v2, rationale-zahlen-e3-k1-s1-v3, rationale-zahlen-e3-k1-s1-v4, rationale-zahlen-e3-k1-s1-v5 – `Berechne:#\cdot(-#)`
- B-992 (2): ableitungsregeln-e2-k1-s1-v2, ableitungsregeln-e2-k1-s1-v4 – `f(x)=e^{-#x}–f'(x)?`
- B-993 (5): binomische-formeln-e3-k1-s1-v1, binomische-formeln-e3-k1-s1-v2, binomische-formeln-e3-k1-s1-v3, binomische-formeln-e3-k1-s1-v4, binomische-formeln-e3-k1-s1-v5 – `Faktorisiere:x^#-#`
- B-994 (3): ableitungsregeln-e2-k1-s1-v1, ableitungsregeln-e2-k1-s1-v3, ableitungsregeln-e2-k1-s1-v5 – `f(x)=e^{#x}–f'(x)?`
- B-995 (2): einheiten-e1-k2-s6-v1, einheiten-e1-k2-s6-v3 – `Rechne #€in ct um.`
- B-996 (2): terme-zone-f4-v1, terme-zone-f4-v2 – `Rechne:#+#\cdot #`
- B-997 (2): rationale-zahlen-e2-k3-s4-v2, rationale-zahlen-e2-k3-s4-v3 – `Berechne:-#-(-#)`
- B-998 (2): rationale-zahlen-e2-k3-s3-v1, rationale-zahlen-e2-k3-s3-v3 – `Berechne:#+(-#)`
- B-999 (2): zinsrechnung-zone-f7-v1, zinsrechnung-zone-f7-v2 – `Berechne.#^{#}`
- B-1000 (5): bruchrechnung-e2-k1-s1-v1, bruchrechnung-e2-k1-s1-v2, bruchrechnung-e2-k1-s1-v3, bruchrechnung-e2-k1-s1-v4, bruchrechnung-e2-k1-s1-v5 – `Berechne #+#.`

## C Gleiches Ergebnis und gleiche Kontextwörter (mehr als drei Zeilen)

Davon mit mindestens zwei gemeinsamen Kontextwörtern: 0. Ein einzelnes Kontextwort (ein Name, ein Glücksrad) mit kleinem Ergebnis ist ein schwacher Befund.

- C-001 (über Einträge, 7 Zeilen, 1 Kontextwort): Ergebnis `2`, Kontext `vereinfache`: terme-basis-k1-v1, terme-basis-k1-v3, funktionsscharen-und-ortskurven-zone-f1-v3, reelle-zahlen-e2-k1-s9-v2, reelle-zahlen-e2-k1-s14-v2, reelle-zahlen-e3-k1-s16-v1, terme-e2-k1-s10-v1  
  `Vereinfache den Term $7x - 2x^2 - 3x$ und berechne seinen Wert für $x = 1$. (P10 2025 GYM)`
- C-002 (über Einträge, 5 Zeilen, 1 Kontextwort): Ergebnis `[1, 2]`, Kontext `glücksrad`: bruchrechnung-basis-k1-v3, kenngroessen-von-verteilungen-e2-k2-s1-v2, wahrscheinlichkeit-e2-k2-s0-v4, wahrscheinlichkeit-e2-k3-s2-v2, zufallsgroessen-und-verteilungen-e1-k3-s1-v1  
  `Ein Glücksrad hat 8 gleich große Felder mit den Zahlen 1 bis 8. Wie groß ist die Wahrscheinlichkeit für eine gerade Zahl? (P10 2014 OS)`
- C-003 (in der Sprosse, 5 Zeilen, 1 Kontextwort): Ergebnis `0.92`, Kontext `eier`: binomialverteilung-e4-k1-s1-v1, binomialverteilung-e4-k1-s1-v2, binomialverteilung-e4-k1-s1-v3, binomialverteilung-e4-k1-s1-v4, binomialverteilung-e4-k1-s1-v5  
  `In 8\,\% der Überraschungseier einer Sorte steckt eine Sonderfigur. Stelle den Ansatz auf: Wie viele Eier muss man öffnen, damit mit mindestens 90\,\% Wahrscheinlichkeit mindestens eine Sonderfigur da …`
- C-004 (über Einträge, 4 Zeilen, 1 Kontextwort): Ergebnis `11`, Kontext `glücksrad`: binomialverteilung-e3-k2-s1-v2, binomialverteilung-e3-k2-s1-v3, binomialverteilung-e3-k2-s1-v5, kenngroessen-von-verteilungen-e2-k1-s5-v2  
  `Ein Glücksrad wird 40-mal gedreht; X ist die Anzahl der Treffer. Übersetze „weniger als 12 Treffer“ in einen Ansatz mit $P(X \le \ldots)$.`
- C-005 (über Einträge, 4 Zeilen, 1 Kontextwort): Ergebnis `0`, Kontext `positiv`: funktionsklassen-und-eigenschaften-e6-k1-s7-v2, orthogonalitaet-e1-k4-s3-v2, scharen-von-geraden-und-ebenen-e4-k1-s6-v4, skalarprodukt-und-winkel-e1-k1-s0-v1  
  `Lies am Graphen $f(2)$ ab und entscheide mit Begründung, ob $f'(2)$ positiv oder negativ ist.`
- C-006 (im Eintrag, 4 Zeilen, 1 Kontextwort): Ergebnis `4`, Kontext `bestand`: potenz-exponentialfunktionen-e2-k2-s6-v2, potenz-exponentialfunktionen-e4-k1-s2-v3, potenz-exponentialfunktionen-e4-k1-s6-v1, potenz-exponentialfunktionen-e4-k1-s7-v1  
  `Ein Bestand wächst jedes Jahr mit dem Faktor $1{,}4$. In der Zeile der Jahre fehlt eine Angabe. Welches Jahr gehört dorthin? Prüfe mit dem Faktor. \wertetabelle[50,70,98,192{,}08]{Jahr}{Anzahl}{0,1,2, …`

## D Personennamen und Sachkontexte

Personennamen: 72 verschiedene in 1176 Zeilen (gezählt je Zeile). Die zehn häufigsten:

| Rang | Name | Zeilen |
|--:|---|--:|
| 1 | Tom | 94 |
| 2 | Mia | 87 |
| 3 | Tim | 80 |
| 4 | Ben | 79 |
| 5 | Lea | 68 |
| 6 | Jonas | 58 |
| 7 | Ole | 53 |
| 8 | Paul | 52 |
| 9 | Lena | 46 |
| 10 | Jan | 44 |

Sachkontexte (Wortliste KONTEXTE im Skript; eine Zeile kann mehrere haben):

| Sachkontext | Zeilen |
|---|--:|
| Geld und Einkauf | 872 |
| Garten, Bau und Wohnen | 646 |
| Glücksspiel und Zufallsgeräte | 529 |
| Wasser und Behälter | 459 |
| Verkehr und Fahrt | 378 |
| Karte und Gelände | 324 |
| Sport und Spiel | 282 |
| Schule | 276 |
| Umfrage und Medizin | 265 |
| Zinsen und Konto | 248 |
| Natur und Tiere | 225 |
| Essen und Kochen | 197 |
| Freizeit und Veranstaltung | 185 |
| Wachstum und Bestand | 177 |
| Produktion und Qualität | 136 |
| Temperatur und Wetter | 133 |
| Handy und Technik | 99 |
| Tarife und Gebühren | 58 |
| ohne Sachkontext (innermathematisch) | 11856 |

## E Länge der aufgabe (unter 20 oder über 600 Zeichen)

Kürzer als 20 Zeichen: 106 Zeilen.

- ableitung-und-aenderungsrate-zone-f5-v1 (19): `Löse: $4t - 10 = 6$`
- ableitung-und-aenderungsrate-zone-f5-v2 (18): `Löse: $6x + 9 = 0$`
- ableitungsregeln-zone-f3-v2 (17): `$0{,}25 \cdot 8$?`
- ableitungsregeln-zone-f5-v4 (16): `Lies $f'(2)$ ab.`
- binomische-formeln-zone-f5-v2 (15): `Berechne. $9^2$`
- binomische-formeln-zone-f5-v3 (18): `Berechne. $(-6)^2$`
- bruchrechnung-zone-f5-v2 (18): `Berechne. $63 : 9$`
- brueche-dezimalzahlen-zone-f1-v1 (18): `Berechne. $56 : 7$`
- brueche-dezimalzahlen-zone-f6-v1 (18): `Berechne. $84 : 4$`
- brueche-dezimalzahlen-zone-f6-v2 (18): `Berechne. $75 : 5$`
- brueche-dezimalzahlen-zone-f6-v3 (17): `Berechne. $7 : 4$`
- brueche-dezimalzahlen-zone-f6-v4 (17): `Berechne. $2 : 5$`
- extremalprobleme-zone-f5-v1 (19): `Löse $x^2 - 9 = 0$.`
- flaechen-zone-f3-v2 (18): `Berechne. $96 : 3$`
- funktionsscharen-und-ortskurven-zone-f3-v1 (17): `Löse: $x^2 = 25$.`
- geraden-zone-f4-v1 (19): `Löse $4 + 2t = 10$.`
- geraden-zone-f4-v2 (18): `Löse $7 - 3s = 1$.`
- geraden-zone-f4-v3 (18): `Löse $2 - 4r = 8$.`
- gleichungen-loesen-zone-f1-v4 (17): `Löse: $2x^2 = 32$`
- gleichungen-loesen-zone-f2-v1 (19): `Löse: $3x + 4 = 19$`
- gleichungen-loesen-zone-f2-v2 (19): `Löse: $5 - 2x = 11$`
- gleichungen-loesen-zone-f2-v4 (16): `Löse: $x^2 = 6x$`
- gleichungen-loesen-zone-f2-v5 (16): `Löse: $-3x > 12$`
- gleichungen-loesen-zone-f2-v7 (18): `Löse: $x^3 = 5x^2$`
- gleichungen-loesen-zone-f4-v1 (15): `Löse: $x^3 = 8$`
- gleichungen-loesen-zone-f4-v3 (17): `Löse: $x^5 = -32$`
- gleichungen-loesen-zone-f4-v4 (16): `Löse: $x^4 = 81$`
- grenzwerte-und-verhalten-im-unendlichen-zone-f1-v1 (18): `Berechne: $(-2)^4$`
- grenzwerte-und-verhalten-im-unendlichen-zone-f1-v2 (18): `Berechne: $(-3)^3$`
- hypothesentests-zone-f4-v1 (15): `Lies $f(2)$ ab.`
- integrationsregeln-zone-f1-v2 (17): `$2 : \frac{1}{3}$`
- kenngroessen-von-verteilungen-zone-f5-v1 (19): `Löse $3x + 2 = 14$.`
- koerper-zone-f5-v2 (15): `Berechne. $7^2$`
- kombinatorik-zone-f2-v1 (15): `Berechne $2^5$.`
- kombinatorik-zone-f2-v2 (15): `Berechne $3^4$.`
- kombinatorik-zone-f2-v4 (15): `Berechne $6^3$.`
- kreis-zone-f4-v1 (15): `Berechne. $7^2$`
- kreis-zone-f4-v4 (19): `Berechne. $3{,}5^2$`
- kurvenuntersuchung-zone-f2-v1 (19): `Löse $3x - 12 = 0$.`
- lagebeziehungen-zone-f4-v1 (19): `$3k + 6 = 0$ – $k$?`
- lagebeziehungen-zone-f5-v2 (19): `$3a - 6 = 0$ – $a$?`
- lineare-funktionen-zone-f3-v2 (19): `Rechne: $(-20) : 5$`
- lineare-gleichungen-zone-f2-v1 (18): `Berechne. $-3 + 8$`
- lineare-gleichungen-zone-f2-v2 (17): `Berechne. $4 - 9$`
- lineare-gleichungssysteme-zone-f6-v2 (18): `Berechne. $-4 + 9$`
- matrizen-und-uebergangsprozesse-zone-f6-v1 (19): `Berechne $0{,}5^3$.`
- orthogonalitaet-zone-f3-v1 (19): `Löse: $3t - 12 = 0$`
- orthogonalitaet-zone-f3-v2 (18): `Löse: $2a + 6 = 0$`
- potenz-exponentialfunktionen-e5-k1-s1-v1 (18): `Berechne $(-2)^4$.`
- potenz-exponentialfunktionen-e5-k1-s1-v2 (18): `Berechne $(-4)^3$.`
- potenz-exponentialfunktionen-e5-k1-s1-v3 (18): `Berechne $(-1)^5$.`
- potenz-exponentialfunktionen-e5-k1-s1-v5 (19): `Berechne $(-10)^3$.`
- potenz-exponentialfunktionen-zone-f9-v2 (18): `Berechne $(-3)^2$.`
- potenzen-wurzeln-e1-k3-s3-v1 (16): `Berechne $14^2$.`
- potenzen-wurzeln-e1-k3-s3-v2 (16): `Berechne $17^2$.`
- potenzen-wurzeln-e1-k3-s3-v3 (15): `Berechne $9^3$.`
- potenzen-wurzeln-e1-k3-s5-v1 (18): `Berechne $(-4)^3$.`
- potenzen-wurzeln-e1-k3-s5-v2 (18): `Berechne $(-2)^6$.`
- potenzen-wurzeln-e1-k3-s5-v3 (18): `Berechne $(-9)^3$.`
- potenzen-wurzeln-e1-k3-s6-v1 (16): `Berechne $-8^2$.`
- potenzen-wurzeln-e1-k3-s6-v2 (16): `Berechne $-5^4$.`
- potenzen-wurzeln-e1-k3-s6-v3 (16): `Berechne $-1^8$.`
- potenzen-wurzeln-e1-k3-s7-v1 (19): `Berechne $0{,}6^2$.`
- potenzen-wurzeln-e1-k3-s7-v2 (19): `Berechne $0{,}2^3$.`
- potenzen-wurzeln-e1-k3-s7-v3 (19): `Berechne $1{,}1^2$.`
- potenzen-wurzeln-e1-k6-s1-v1 (15): `Berechne $8^0$.`
- potenzen-wurzeln-e1-k6-s1-v2 (18): `Berechne $(-6)^0$.`
- potenzen-wurzeln-zone-f3-v4 (18): `Berechne $(-7)^2$.`
- potenzen-wurzeln-zone-f3-v5 (16): `Berechne $-5^2$.`
- potenzen-wurzeln-zone-f3-v7 (19): `Berechne $(-15)^2$.`
- pyramide-kegel-kugel-zone-f4-v1 (15): `Berechne. $3^3$`
- pyramide-kegel-kugel-zone-f4-v3 (19): `Berechne. $1{,}5^3$`
- pyramide-kegel-kugel-zone-f4-v4 (15): `Berechne. $6^3$`
- pythagoras-zone-f1-v1 (16): `Berechne $11^2$.`
- pythagoras-zone-f1-v3 (19): `Berechne $1{,}4^2$.`
- quadratische-funktionen-zone-f1-v1 (15): `Berechne. $6^2$`
- quadratische-funktionen-zone-f1-v2 (15): `Berechne. $9^2$`
- quadratische-funktionen-zone-f1-v3 (19): `Berechne. $1{,}2^2$`
- quadratische-funktionen-zone-f1-v4 (18): `Berechne. $(-8)^2$`
- quadratische-funktionen-zone-f1-v5 (19): `Berechne. $0{,}3^2$`
- quadratische-gleichungen-zone-f1-v1 (15): `Berechne. $7^2$`
- quadratische-gleichungen-zone-f1-v2 (18): `Berechne. $(-3)^2$`
- quadratische-gleichungen-zone-f1-v6 (19): `Berechne. $(-13)^2$`
- rationale-zahlen-e2-k3-s1-v1 (18): `Berechne: $-7 + 3$`
- rationale-zahlen-e2-k3-s1-v2 (18): `Berechne: $-7 + 9$`
- rationale-zahlen-e2-k3-s1-v3 (18): `Berechne: $-7 - 2$`
- rationale-zahlen-e2-k3-s1-v4 (18): `Berechne: $-7 + 7$`
- rationale-zahlen-e2-k3-s1-v5 (18): `Berechne: $-7 - 4$`
- rationale-zahlen-zone-f1-v2 (18): `Berechne: $63 : 9$`
- rationale-zahlen-zone-f1-v3 (19): `Berechne: $120 : 8$`
- rationale-zahlen-zone-f1-v4 (19): `Berechne: $73 - 38$`
- reelle-zahlen-zone-f6-v2 (15): `Berechne $4^3$.`
- reelle-zahlen-zone-f6-v3 (18): `Berechne $(-2)^3$.`
- reelle-zahlen-zone-f6-v4 (15): `Berechne $7^0$.`
- rekonstruktion-von-bestaenden-zone-f4-v1 (15): `3\,m³ in Liter?`
- rekonstruktion-von-bestaenden-zone-f4-v3 (16): `72\,km/h in m/s?`
- terme-zone-f1-v1 (15): `Rechne: $4 - 9$`
- terme-zone-f1-v2 (16): `Rechne: $-3 + 8$`
- terme-zone-f1-v4 (16): `Rechne: $-6 - 4$`
- terme-zone-f1-v7 (16): `Rechne: $-8 - 6$`
- vektoren-und-rechenoperationen-zone-f4-v1 (15): `$3r = 12$: $r$?`
- vektoren-und-rechenoperationen-zone-f4-v2 (17): `$s - 2 = 7$: $s$?`
- vierfeldertafel-zone-f1-v1 (18): `$25\,\%$ von $80$?`
- zinsrechnung-zone-f7-v1 (17): `Berechne. $2^{6}$`
- zinsrechnung-zone-f7-v2 (17): `Berechne. $5^{3}$`
- zufallsexperimente-und-pfadregeln-zone-f8-v1 (18): `$6!$ (6 Fakultät)?`

Länger als 600 Zeichen: 2 Zeilen.

- matrizen-und-uebergangsprozesse-e4-k1-s7-v5 (664): `Ein Kanuverleih hat drei Stationen; die Verteilung geht von Abend zu Abend mit M über. d ist die Verteilung am Montagabend vor einer Entnahme: am Montagabend we …`
- matrizen-und-uebergangsprozesse-e4-k1-s7-v6 (647): `E-Roller stehen in drei Zonen; die Verteilung geht von Abend zu Abend mit M über. d ist die Verteilung am Freitagabend vor dem Einsammeln: am Freitagabend werde …`
