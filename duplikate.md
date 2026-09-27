# Duplikate und Zahlenkollisionen der Bank

Gebaut mit werkzeuge/duplikate.py; nicht von Hand ändern, nach jedem Bank-Auftrag neu bauen.
Quelle: bank/*/*.jsonl, 70 Einträge, 13606 Zeilen. Stand der Bank: 8c77e08 2026-09-27 (letzter Commit auf bank/).
Verglichen wird aufgabe samt grafik nach Normierung (LaTeX-Abstände und $ weg, {,} → Komma, Tausender zusammen, Dezimalpunkt → Komma, Endnullen weg, Leerzeichen neben Zeichen gestrichen); „bis auf Zahlen“ ersetzt jede Zahl durch #. Reichweite: über Einträge / im Eintrag (über Sprossen) / in der Sprosse (Varianten).

## Zahl je Befundart

| Befundart | Gruppen | Zeilen |
|---|--:|--:|
| A wortgleich, über Einträge | 13 | 29 |
| A wortgleich, im Eintrag | 0 | 0 |
| A wortgleich, in der Sprosse | 0 | 0 |
| B bis auf Zahlen gleich, über Einträge | 73 | 351 |
| B bis auf Zahlen gleich, im Eintrag | 155 | 465 |
| B bis auf Zahlen gleich, in der Sprosse | 580 | 1466 |
| C gleiches Ergebnis und gleiche Kontextwörter (> 3 Zeilen) | 5 | 22 |
| D Personennamen (verschiedene) | 71 | 924 |
| D Sachkontexte (Zeilen mit mindestens einem) | 18 | 3339 |
| E aufgabe kürzer als 20 Zeichen | – | 267 |
| E aufgabe länger als 600 Zeichen | – | 2 |

## A Wortgleich nach Normierung

- A-001 (über Einträge, 4 Zeilen): flaechen-zone-f5-v2, kreis-zone-f4-v2, pyramide-kegel-kugel-zone-f4-v2, quadratische-funktionen-zone-f7-v1  
  `\sqrt{64}–wie viel?`
- A-002 (über Einträge, 3 Zeilen): koerper-zone-f5-v2, kreis-zone-f4-v1, quadratische-gleichungen-zone-f1-v1  
  `7^2–wie viel?`
- A-003 (über Einträge, 2 Zeilen): bruchrechnung-zone-f3-v2, brueche-dezimalzahlen-zone-f4-v1  
  `Nenne alle Teiler von 10.`
- A-004 (über Einträge, 2 Zeilen): einheiten-e1-k2-s8-v1, koerper-zone-f3-v3  
  `2,35 m–wie viel cm?`
- A-005 (über Einträge, 2 Zeilen): flaechen-zone-f3-v1, kreis-zone-f2-v1  
  `0,5\cdot 8–wie viel?`
- A-006 (über Einträge, 2 Zeilen): flaechen-zone-f4-v1, koerper-zone-f4-v1  
  `P=q\cdot r–nach r umstellen?`
- A-007 (über Einträge, 2 Zeilen): flaechen-zone-f5-v4, quadratische-gleichungen-zone-f2-v2  
  `\sqrt{100}–wie viel?`
- A-008 (über Einträge, 2 Zeilen): funktionsklassen-und-eigenschaften-zone-f4-v3, tangente-normale-schnittwinkel-zone-f4-v3  
  `x^2-2x-8=0–Lösungen?`
- A-009 (über Einträge, 2 Zeilen): koerper-zone-f5-v4, quadratische-funktionen-zone-f1-v6  
  `2\cdot 5^2–wie viel?`
- A-010 (über Einträge, 2 Zeilen): lineare-gleichungen-e2-k3-s1-v1, quadratische-gleichungen-zone-f3-v1  
  `x+8=15`
- A-011 (über Einträge, 2 Zeilen): potenzen-wurzeln-e3-k2-s12-v3, pyramide-kegel-kugel-zone-f4-v5  
  `\sqrt[3]{343}–wie viel?`
- A-012 (über Einträge, 2 Zeilen): pythagoras-zone-f2-v1, quadratische-funktionen-zone-f7-v2  
  `\sqrt{121}–wie viel?`
- A-013 (über Einträge, 2 Zeilen): quadratische-funktionen-zone-f7-v4, quadratische-gleichungen-zone-f2-v4  
  `\sqrt{-16}–wie viel?`

## B Bis auf Zahlen gleich, über Einträge hinweg

- B-001 (5 Zeilen): brueche-dezimalzahlen-e4-k1-s8-v1, brueche-dezimalzahlen-e4-k1-s8-v2, brueche-dezimalzahlen-e5-k2-s9-v5, brueche-dezimalzahlen-e5-k2-s9-v6, potenzen-wurzeln-e3-k2-s13-v3  
  `Welche Aussage ist wahr?Kreuze an.(P# # OS)\\kreuz{#<\frac{#}{#}}\\kreuz{\frac{#}{#}>\frac{#}{#}}\\kreuz{\sqrt{#}>\frac{#}{#}}`
- B-002 (5 Zeilen): strahlensaetze-zone-f9-v1, strahlensaetze-zone-f9-v2, strahlensaetze-zone-f9-v3, trigonometrie-zone-f7-v1, trigonometrie-zone-f7-v4  
  `Ein Dreieck hat die Winkel #^\circ und #^\circ.Wie groß ist der dritte?`
- B-003 (3 Zeilen): bruchrechnung-zone-f1-v2, brueche-dezimalzahlen-e1-k1-s2-v1, brueche-dezimalzahlen-e1-k1-s2-v3  
  `Färbe\frac{#}{#}des Streifens.‖Grafik:\bruchrechteck{#}{#}`
- B-004 (2 Zeilen): bruchrechnung-zone-f1-v1, brueche-dezimalzahlen-e1-k1-s1-v3  
  `Welcher Anteil ist gefärbt?‖Grafik:\bruchrechteck{#}{#}`
- B-005 (2 Zeilen): abstaende-zone-f1-v1, punkte-und-strecken-im-koordinatensystem-zone-f3-v1  
  `A(#|#|#),B(#|#|#):\overrightarrow{AB}und seine Länge?`
- B-006 (2 Zeilen): abstaende-zone-f1-v7, punkte-und-strecken-im-koordinatensystem-zone-f3-v2  
  `C(#|#|#),D(#|#|#):\overrightarrow{CD}und seine Länge?`
- B-007 (11 Zeilen): bedingte-wahrscheinlichkeit-und-bayes-zone-f4-v1, brueche-dezimalzahlen-e3-k1-s1-v1, brueche-dezimalzahlen-e3-k1-s1-v2, brueche-dezimalzahlen-e3-k1-s1-v3, brueche-dezimalzahlen-e3-k1-s1-v4, brueche-dezimalzahlen-e3-k1-s1-v5, brueche-dezimalzahlen-e3-k1-s2-v1, brueche-dezimalzahlen-e3-k1-s2-v2, brueche-dezimalzahlen-e3-k1-s2-v3, brueche-dezimalzahlen-e3-k1-s4-v1, brueche-dezimalzahlen-e3-k1-s4-v2  
  `Welcher Bruch ist größer:\frac{#}{#}oder\frac{#}{#}?`
- B-008 (2 Zeilen): symmetrie-abbildungen-zone-f6-v1, trigonometrische-funktionen-zone-f5-v4  
  `Miss den Winkel\alpha.‖Grafik:\winkel{#}{\alpha}`
- B-009 (2 Zeilen): ebenen-zone-f4-v2, flaecheninhalt-und-volumen-im-raum-zone-f4-v3  
  `Stehen(#|-#|#)und(#|#|#)senkrecht aufeinander?`
- B-010 (2 Zeilen): strahlensaetze-zone-f4-v1, zuordnungen-e2-k4-s1-v4  
  `# Brötchen kosten #€.Was kosten # Brötchen?`
- B-011 (5 Zeilen): bruchrechnung-zone-f2-v4, bruchrechnung-zone-f2-v6, brueche-dezimalzahlen-e2-k1-s4-v1, brueche-dezimalzahlen-e2-k1-s4-v2, brueche-dezimalzahlen-e2-k1-s4-v3  
  `Schreibe\frac{#}{#}mit dem Nenner #.`
- B-012 (2 Zeilen): linearkombination-und-lineare-abhaengigkeit-zone-f4-v4, punkte-und-strecken-im-koordinatensystem-zone-f8-v4  
  `Ist(#|#|#)ein Vielfaches von(#|#|#)?`
- B-013 (3 Zeilen): punkte-und-strecken-im-koordinatensystem-zone-f4-v1, vektoren-und-rechenoperationen-zone-f2-v1, vektoren-und-rechenoperationen-zone-f2-v2  
  `Katheten # cm und # cm:Hypotenuse?`
- B-014 (2 Zeilen): abstaende-zone-f6-v1, tangente-normale-schnittwinkel-zone-f6-v1  
  `Katheten # cm und # cm–Hypotenuse?`
- B-015 (2 Zeilen): prozentrechnung-e2-k3-s2-v1, zinsrechnung-zone-f2-v2  
  `# von # Kindern–wie viel Prozent?`
- B-016 (3 Zeilen): potenzen-wurzeln-zone-f5-v1, potenzen-wurzeln-zone-f5-v5, reelle-zahlen-zone-f2-v2  
  `# oder #–welche Zahl ist größer?`
- B-017 (2 Zeilen): punkte-und-strecken-im-koordinatensystem-zone-f4-v2, vektoren-und-rechenoperationen-zone-f2-v3  
  `Katheten # m und # m:Hypotenuse?`
- B-018 (2 Zeilen): abstaende-zone-f3-v1, lagebeziehungen-zone-f1-v1  
  `E:#x+#y-z=#–ein Normalenvektor?`
- B-019 (2 Zeilen): kenngroessen-von-verteilungen-zone-f4-v2, kombinatorik-zone-f3-v2  
  `Wie viel Prozent sind # von #?`
- B-020 (11 Zeilen): brueche-dezimalzahlen-e4-k1-s1-v1, brueche-dezimalzahlen-e4-k1-s1-v2, brueche-dezimalzahlen-e4-k1-s1-v5, brueche-dezimalzahlen-e4-k1-s2-v1, brueche-dezimalzahlen-e4-k1-s2-v2, brueche-dezimalzahlen-e4-k1-s4-v1, brueche-dezimalzahlen-e4-k1-s4-v2, brueche-dezimalzahlen-e4-k1-s4-v3, reelle-zahlen-zone-f1-v1, reelle-zahlen-zone-f1-v2, reelle-zahlen-zone-f1-v3  
  `\frac{#}{#}–als Dezimalzahl?`
- B-021 (5 Zeilen): bedingte-wahrscheinlichkeit-und-bayes-zone-f3-v2, brueche-dezimalzahlen-e2-k1-s3-v1, brueche-dezimalzahlen-e2-k1-s3-v2, brueche-dezimalzahlen-e2-k1-s3-v3, kombinatorik-zone-f3-v1  
  `Kürze\frac{#}{#}vollständig.`
- B-022 (7 Zeilen): bruchrechnung-e3-k2-s2-v1, bruchrechnung-e3-k2-s2-v2, bruchrechnung-e3-k2-s2-v3, bruchrechnung-e3-k2-s3-v1, bruchrechnung-e3-k2-s3-v2, bruchrechnung-e3-k2-s3-v3, zufallsexperimente-und-pfadregeln-zone-f3-v1  
  `\frac{#}{#}\cdot\frac{#}{#}`
- B-023 (6 Zeilen): prozentrechnung-zone-f2-v1, prozentrechnung-zone-f2-v3, prozentrechnung-zone-f2-v4, trigonometrie-zone-f5-v1, trigonometrie-zone-f5-v2, trigonometrie-zone-f5-v3  
  `\frac{#}{#}als Dezimalzahl?`
- B-024 (2 Zeilen): flaechen-zone-f1-v4, pythagoras-zone-f4-v4  
  `# m und # cm–zusammen in m?`
- B-025 (2 Zeilen): funktionsklassen-und-eigenschaften-e2-k1-s3-v3, quadratische-funktionen-e4-k1-s5-v1  
  `f(x)=#x^#-#x-#–Nullstellen?`
- B-026 (2 Zeilen): potenzen-wurzeln-zone-f3-v6, quadratische-gleichungen-zone-f1-v5  
  `Wo ist der Fehler?(-#)^#=-#`
- B-027 (6 Zeilen): bruchrechnung-zone-f2-v1, brueche-dezimalzahlen-e2-k1-s1-v1, brueche-dezimalzahlen-e2-k1-s1-v2, brueche-dezimalzahlen-e2-k1-s1-v3, brueche-dezimalzahlen-e2-k1-s1-v4, brueche-dezimalzahlen-e2-k1-s1-v5  
  `Erweitere\frac{#}{#}mit #.`
- B-028 (2 Zeilen): funktionsklassen-und-eigenschaften-e2-k1-s3-v1, quadratische-funktionen-e4-k1-s3-v3  
  `f(x)=x^#-#x+#–Nullstellen?`
- B-029 (2 Zeilen): kreis-zone-f6-v2, vierfeldertafel-zone-f1-v2  
  `# von #–wie viel Prozent?`
- B-030 (3 Zeilen): bruchrechnung-zone-f3-v2, brueche-dezimalzahlen-zone-f4-v1, brueche-dezimalzahlen-zone-f4-v3  
  `Nenne alle Teiler von #.`
- B-031 (3 Zeilen): pyramide-kegel-kugel-zone-f7-v1, pythagoras-zone-f7-v1, pythagoras-zone-f7-v3  
  `Durchmesser # cm–Radius?`
- B-032 (11 Zeilen): bruchrechnung-e1-k3-s1-v1, bruchrechnung-e1-k3-s1-v3, bruchrechnung-e1-k3-s1-v5, bruchrechnung-e1-k3-s2-v1, bruchrechnung-e1-k3-s2-v3, bruchrechnung-e1-k3-s3-v1, bruchrechnung-e1-k3-s3-v2, bruchrechnung-e1-k3-s3-v3, bruchrechnung-e1-k3-s4-v1, bruchrechnung-e1-k3-s5-v1, zufallsexperimente-und-pfadregeln-zone-f3-v5  
  `\frac{#}{#}+\frac{#}{#}`
- B-033 (6 Zeilen): bruchrechnung-e3-k3-s3-v1, bruchrechnung-e3-k3-s3-v2, bruchrechnung-e3-k3-s3-v3, bruchrechnung-e3-k3-s4-v1, bruchrechnung-e3-k3-s4-v2, integrationsregeln-zone-f1-v3  
  `\frac{#}{#}:\frac{#}{#}`
- B-034 (6 Zeilen): brueche-dezimalzahlen-e4-k1-s5-v1, brueche-dezimalzahlen-e4-k1-s5-v2, brueche-dezimalzahlen-e4-k1-s5-v3, reelle-zahlen-e1-k2-s1-v1, reelle-zahlen-e1-k2-s1-v2, reelle-zahlen-e1-k2-s1-v3  
  `#–als gekürzter Bruch?`
- B-035 (4 Zeilen): binomische-formeln-zone-f6-v1, binomische-formeln-zone-f6-v2, quadratische-gleichungen-zone-f6-v1, quadratische-gleichungen-zone-f6-v2  
  `y=(x-#)^#+#–Scheitel?`
- B-036 (4 Zeilen): koerper-zone-f3-v4, pyramide-kegel-kugel-zone-f8-v1, pyramide-kegel-kugel-zone-f8-v3, pyramide-kegel-kugel-zone-f8-v4  
  `# cm³–wie viel Liter?`
- B-037 (4 Zeilen): potenzen-wurzeln-e3-k2-s12-v1, potenzen-wurzeln-e3-k2-s12-v2, potenzen-wurzeln-e3-k2-s12-v3, pyramide-kegel-kugel-zone-f4-v5  
  `\sqrt[#]{#}–wie viel?`
- B-038 (3 Zeilen): abstaende-zone-f5-v1, punkte-und-strecken-im-koordinatensystem-zone-f6-v1, punkte-und-strecken-im-koordinatensystem-zone-f6-v2  
  `(#|#|#)\circ(#|#|#)?`
- B-039 (3 Zeilen): lineare-funktionen-zone-f6-v1, terme-e2-k4-s1-v1, terme-e2-k4-s10-v1  
  `Fasse zusammen:#x+#x`
- B-040 (3 Zeilen): lineare-funktionen-zone-f6-v2, terme-e2-k4-s2-v1, terme-e2-k4-s7-v1  
  `Fasse zusammen:#x-#x`
- B-041 (2 Zeilen): lineare-funktionen-zone-f3-v3, terme-zone-f2-v4  
  `Rechne:(-#)\cdot(-#)`
- B-042 (4 Zeilen): brueche-dezimalzahlen-zone-f7-v2, brueche-dezimalzahlen-zone-f7-v3, prozentrechnung-e1-k1-s4-v1, prozentrechnung-e1-k1-s4-v3  
  `#–wie viel Prozent?`
- B-043 (2 Zeilen): prozentrechnung-e1-k1-s4-v2, zufallsexperimente-und-pfadregeln-zone-f5-v4  
  `#\%als Dezimalzahl?`
- B-044 (24 Zeilen): flaechen-zone-f3-v1, flaechen-zone-f3-v3, flaechen-zone-f3-v4, koerper-zone-f5-v1, kreis-zone-f2-v1, potenzen-wurzeln-e2-k1-s3-v1, potenzen-wurzeln-e2-k1-s3-v2, potenzen-wurzeln-e2-k1-s3-v3, potenzen-wurzeln-zone-f1-v1, potenzen-wurzeln-zone-f1-v2, potenzen-wurzeln-zone-f1-v3, potenzen-wurzeln-zone-f2-v1, potenzen-wurzeln-zone-f2-v2, potenzen-wurzeln-zone-f4-v1, potenzen-wurzeln-zone-f4-v3, potenzen-wurzeln-zone-f4-v4, potenzen-wurzeln-zone-f7-v1, potenzen-wurzeln-zone-f7-v2, potenzen-wurzeln-zone-f7-v4, potenzen-wurzeln-zone-f8-v1, potenzen-wurzeln-zone-f8-v3, potenzen-wurzeln-zone-f8-v4, strahlensaetze-zone-f1-v1, strahlensaetze-zone-f1-v3  
  `#\cdot #–wie viel?`
- B-045 (14 Zeilen): flaechen-zone-f5-v1, flaechen-zone-f5-v2, flaechen-zone-f5-v3, flaechen-zone-f5-v4, kreis-zone-f4-v2, potenzen-wurzeln-e3-k2-s9-v1, potenzen-wurzeln-e3-k2-s9-v3, pyramide-kegel-kugel-zone-f4-v2, pythagoras-zone-f2-v1, quadratische-funktionen-zone-f7-v1, quadratische-funktionen-zone-f7-v2, quadratische-funktionen-zone-f7-v5, quadratische-gleichungen-zone-f2-v1, quadratische-gleichungen-zone-f2-v2  
  `\sqrt{#}–wie viel?`
- B-046 (8 Zeilen): bruchrechnung-e3-k2-s1-v1, bruchrechnung-e3-k2-s1-v2, bruchrechnung-e3-k2-s1-v4, bruchrechnung-e3-k2-s1-v5, lineare-gleichungen-zone-f4-v1, lineare-gleichungen-zone-f4-v2, lineare-gleichungen-zone-f4-v3, lineare-gleichungen-zone-f4-v5  
  `\frac{#}{#}\cdot #`
- B-047 (3 Zeilen): lineare-funktionen-zone-f3-v1, terme-zone-f2-v1, terme-zone-f2-v3  
  `Rechne:(-#)\cdot #`
- B-048 (2 Zeilen): einheiten-e3-k1-s5-v3, pyramide-kegel-kugel-zone-f8-v2  
  `# m³–wie viel dm³?`
- B-049 (3 Zeilen): brueche-dezimalzahlen-e1-k2-s3-v1, prozentrechnung-zone-f6-v1, prozentrechnung-zone-f6-v5  
  `\frac{#}{#}von #€`
- B-050 (2 Zeilen): gleichungen-loesen-zone-f1-v1, grenzwerte-und-verhalten-im-unendlichen-zone-f5-v1  
  `Löse:(x-#)(x+#)=#`
- B-051 (10 Zeilen): potenzen-wurzeln-e1-k3-s5-v1, potenzen-wurzeln-e1-k3-s5-v2, potenzen-wurzeln-e1-k3-s5-v3, potenzen-wurzeln-e1-k6-s1-v2, potenzen-wurzeln-zone-f3-v4, potenzen-wurzeln-zone-f3-v7, quadratische-funktionen-zone-f1-v4, quadratische-gleichungen-zone-f1-v2, quadratische-gleichungen-zone-f1-v3, quadratische-gleichungen-zone-f1-v6  
  `(-#)^#–wie viel?`
- B-052 (5 Zeilen): einheiten-e1-k2-s3-v3, einheiten-e1-k2-s8-v1, einheiten-e1-k2-s8-v2, koerper-zone-f3-v3, pythagoras-zone-f4-v1  
  `# m–wie viel cm?`
- B-053 (2 Zeilen): einheiten-e1-k2-s3-v2, pythagoras-zone-f4-v2  
  `# cm–wie viel m?`
- B-054 (2 Zeilen): einheiten-e3-k1-s7-v1, koerper-zone-f3-v1  
  `# l–wie viel ml?`
- B-055 (2 Zeilen): funktionsklassen-und-eigenschaften-zone-f4-v4, tangente-normale-schnittwinkel-zone-f4-v1  
  `#x^#=#–Lösungen?`
- B-056 (3 Zeilen): funktionsklassen-und-eigenschaften-zone-f4-v1, quadratische-funktionen-zone-f8-v1, quadratische-funktionen-zone-f8-v2  
  `x^#=#–Lösungen?`
- B-057 (20 Zeilen): koerper-zone-f5-v2, kreis-zone-f4-v1, kreis-zone-f4-v4, potenzen-wurzeln-e1-k3-s3-v1, potenzen-wurzeln-e1-k3-s3-v2, potenzen-wurzeln-e1-k3-s3-v3, potenzen-wurzeln-e1-k3-s7-v1, potenzen-wurzeln-e1-k3-s7-v2, potenzen-wurzeln-e1-k3-s7-v3, potenzen-wurzeln-e1-k6-s1-v1, pyramide-kegel-kugel-zone-f4-v1, pyramide-kegel-kugel-zone-f4-v3, pyramide-kegel-kugel-zone-f4-v4, pythagoras-zone-f1-v1, pythagoras-zone-f1-v3, quadratische-funktionen-zone-f1-v1, quadratische-funktionen-zone-f1-v2, quadratische-funktionen-zone-f1-v3, quadratische-funktionen-zone-f1-v5, quadratische-gleichungen-zone-f1-v1  
  `#^#–wie viel?`
- B-058 (7 Zeilen): flaechen-zone-f3-v2, flaechen-zone-f3-v5, kreis-zone-f2-v2, potenzen-wurzeln-zone-f8-v2, potenzen-wurzeln-zone-f8-v5, strahlensaetze-zone-f1-v2, strahlensaetze-zone-f1-v4  
  `#:#–wie viel?`
- B-059 (4 Zeilen): kombinatorik-zone-f2-v1, kombinatorik-zone-f2-v2, kombinatorik-zone-f2-v4, matrizen-und-uebergangsprozesse-zone-f6-v1  
  `Berechne #^#.`
- B-060 (2 Zeilen): ableitung-und-aenderungsrate-zone-f5-v1, orthogonalitaet-zone-f3-v1  
  `Löse:#t-#=#`
- B-061 (2 Zeilen): ableitung-und-aenderungsrate-zone-f5-v2, gleichungen-loesen-zone-f2-v1  
  `Löse:#x+#=#`
- B-062 (3 Zeilen): bruchrechnung-e5-k1-s1-v1, bruchrechnung-e5-k1-s2-v1, lineare-gleichungen-zone-f1-v1  
  `#+#\cdot #`
- B-063 (3 Zeilen): bruchrechnung-e5-k1-s1-v5, bruchrechnung-e5-k1-s2-v2, lineare-gleichungen-zone-f1-v4  
  `#-#\cdot #`
- B-064 (4 Zeilen): ableitungsregeln-zone-f3-v2, einheiten-zone-f3-v1, einheiten-zone-f3-v3, einheiten-zone-f3-v4  
  `#\cdot #?`
- B-065 (4 Zeilen): lineare-gleichungen-e3-k1-s2-v2, lineare-gleichungen-e3-k1-s2-v3, lineare-gleichungen-e3-k2-s1-v2, quadratische-gleichungen-zone-f3-v4  
  `#x-#=#x+#`
- B-066 (19 Zeilen): bruchrechnung-e4-k2-s1-v1, bruchrechnung-e4-k2-s1-v2, bruchrechnung-e4-k2-s1-v3, bruchrechnung-e4-k2-s1-v4, bruchrechnung-e4-k2-s1-v5, bruchrechnung-e4-k2-s3-v1, bruchrechnung-e4-k2-s3-v2, bruchrechnung-e4-k2-s3-v3, bruchrechnung-e4-k2-s4-v1, bruchrechnung-e4-k2-s4-v2, bruchrechnung-e4-k2-s4-v3, bruchrechnung-e4-k2-s5-v1, bruchrechnung-e4-k2-s5-v2, bruchrechnung-e4-k2-s5-v3, bruchrechnung-zone-f5-v1, brueche-dezimalzahlen-zone-f1-v2, prozentrechnung-zone-f3-v2, prozentrechnung-zone-f3-v3, prozentrechnung-zone-f3-v5  
  `#\cdot #`
- B-067 (4 Zeilen): lineare-gleichungen-e3-k2-s1-v1, lineare-gleichungssysteme-zone-f4-v1, lineare-gleichungssysteme-zone-f4-v3, zufallsexperimente-und-pfadregeln-zone-f9-v1  
  `#x+#=#`
- B-068 (3 Zeilen): lineare-gleichungen-e3-k1-s1-v3, lineare-gleichungen-e3-k1-s1-v5, lineare-gleichungssysteme-zone-f4-v2  
  `#x=x+#`
- B-069 (5 Zeilen): lineare-gleichungen-e2-k3-s1-v1, lineare-gleichungen-e2-k3-s1-v3, lineare-gleichungen-e2-k3-s3-v1, lineare-gleichungen-e2-k3-s3-v3, quadratische-gleichungen-zone-f3-v1  
  `x+#=#`
- B-070 (2 Zeilen): lineare-gleichungen-e2-k3-s5-v1, quadratische-gleichungen-zone-f3-v3  
  `-#x=#`
- B-071 (3 Zeilen): lineare-gleichungen-e2-k3-s2-v1, lineare-gleichungen-e2-k3-s2-v3, quadratische-gleichungen-zone-f3-v2  
  `#x=#`
- B-072 (18 Zeilen): bruchrechnung-e4-k2-s2-v1, bruchrechnung-e4-k2-s2-v2, bruchrechnung-e4-k2-s2-v3, bruchrechnung-e4-k2-s6-v1, bruchrechnung-e4-k2-s6-v2, bruchrechnung-e4-k2-s6-v3, bruchrechnung-e4-k2-s7-v1, bruchrechnung-e4-k2-s7-v2, bruchrechnung-e4-k2-s7-v3, bruchrechnung-zone-f5-v2, brueche-dezimalzahlen-zone-f1-v1, brueche-dezimalzahlen-zone-f1-v3, brueche-dezimalzahlen-zone-f6-v1, brueche-dezimalzahlen-zone-f6-v2, brueche-dezimalzahlen-zone-f6-v3, brueche-dezimalzahlen-zone-f6-v4, prozentrechnung-zone-f3-v1, prozentrechnung-zone-f3-v4  
  `#:#`
- B-073 (6 Zeilen): bruchrechnung-e2-k1-s1-v2, bruchrechnung-e2-k1-s1-v4, bruchrechnung-e2-k1-s2-v2, bruchrechnung-e2-k1-s2-v3, bruchrechnung-e2-k1-s3-v2, lineare-gleichungen-zone-f2-v2  
  `#-#`

## B Bis auf Zahlen gleich, im selben Eintrag, über Sprossen hinweg

- B-074 (7 Zeilen): lineare-funktionen-e1-k1-s1-v1, lineare-funktionen-e1-k1-s1-v3, lineare-funktionen-e1-k1-s1-v4, lineare-funktionen-e1-k1-s1-v5, lineare-funktionen-e1-k1-s3-v1, lineare-funktionen-e1-k1-s3-v2, lineare-funktionen-e1-k1-s3-v3  
  `Wertepaare und Gerade:Berechne die y-Werte zu y=#x für x=# # # und zeichne die Ursprungsgerade.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\end{ksys}`
- B-075 (2 Zeilen): lineare-funktionen-e4-k1-s3-v3, lineare-funktionen-e4-k1-s5-v3  
  `Gleichung aus zwei Punkten:Bestimme die Gleichung der Geraden durch A(#|#)und B(#|-#).`
- B-076 (4 Zeilen): lineare-funktionen-e4-k1-s3-v1, lineare-funktionen-e4-k1-s4-v1, lineare-funktionen-e4-k1-s4-v3, lineare-funktionen-e4-k1-s5-v1  
  `Gleichung aus zwei Punkten:Bestimme die Gleichung der Geraden durch A(#|#)und B(#|#).`
- B-077 (2 Zeilen): normalverteilung-und-sigma-regeln-zone-f2-v4, normalverteilung-und-sigma-regeln-zone-f2-v7  
  `Die Zuflussrate ist # Liter pro Minute,# Minuten lang.Wie viel Wasser fließt zu?`
- B-078 (2 Zeilen): konfidenzintervalle-zone-f2-v3, konfidenzintervalle-zone-f2-v6  
  `X ist binomialverteilt mit n=# und p=#.Berechne P(X=#)auf Tausendstel.`
- B-079 (2 Zeilen): hypothesentests-zone-f2-v3, hypothesentests-zone-f2-v6  
  `X ist binomialverteilt mit n=# und p=#;P(X\le #)\approx #.P(X\ge #)?`
- B-080 (7 Zeilen): winkel-dreiecke-e3-k2-s1-v1, winkel-dreiecke-e3-k2-s1-v2, winkel-dreiecke-e3-k2-s1-v3, winkel-dreiecke-e3-k2-s1-v4, winkel-dreiecke-e3-k2-s1-v5, winkel-dreiecke-e3-k2-s2-v2, winkel-dreiecke-e3-k2-s2-v3  
  `Im Dreieck ABC ist\alpha=#^\circ und\beta=#^\circ.Wie groß ist γ?`
- B-081 (3 Zeilen): lineare-funktionen-e3-k2-s1-v3, lineare-funktionen-e3-k2-s1-v5, lineare-funktionen-e3-k2-s3-v2  
  `f(#)?Berechne den Funktionswert von f(x)=-#x+# an der Stelle x=#.`
- B-082 (4 Zeilen): lineare-funktionen-e3-k2-s1-v2, lineare-funktionen-e3-k2-s1-v4, lineare-funktionen-e3-k2-s3-v1, lineare-funktionen-e3-k2-s3-v3  
  `f(#)?Berechne den Funktionswert von f(x)=#x-# an der Stelle x=#.`
- B-083 (2 Zeilen): trigonometrie-e4-k1-s3-v3, trigonometrie-e4-k1-s5-v3  
  `Dreieck ABC:c=# cm,\gamma=#^\circ,\alpha=#^\circ.Wie lang ist b?`
- B-084 (2 Zeilen): trigonometrie-e4-k1-s3-v1, trigonometrie-e4-k1-s5-v1  
  `Dreieck ABC:a=# cm,\alpha=#^\circ,\beta=#^\circ.Wie lang ist c?`
- B-085 (2 Zeilen): pythagoras-e2-k2-s2-v2, pythagoras-e2-k2-s3-v3  
  `Hypotenuse c=# m,Kathete b=# m–Kathete a auf eine Dezimale?`
- B-086 (2 Zeilen): zufallsgroessen-und-verteilungen-zone-f1-v4, zufallsgroessen-und-verteilungen-zone-f1-v6  
  `Zwei Würfel werden geworfen–Wahrscheinlichkeit der Summe #?`
- B-087 (4 Zeilen): pyramide-kegel-kugel-e2-k2-s1-v1, pyramide-kegel-kugel-e2-k2-s1-v3, pyramide-kegel-kugel-e2-k2-s1-v5, pyramide-kegel-kugel-e2-k2-s3-v1  
  `Kegel:Radius # cm,Höhe # cm–Volumen?Runde auf eine Stelle.`
- B-088 (2 Zeilen): skalarprodukt-und-winkel-zone-f5-v1, skalarprodukt-und-winkel-zone-f5-v3  
  `Ein Winkel ist #^\circ groß.Wie groß ist sein Nebenwinkel?`
- B-089 (2 Zeilen): trigonometrische-funktionen-zone-f1-v1, trigonometrische-funktionen-zone-f1-v4  
  `Gegenkathete # cm,Hypotenuse # cm–wie groß ist sin\alpha?`
- B-090 (7 Zeilen): koerper-e4-k2-s1-v1, koerper-e4-k2-s1-v2, koerper-e4-k2-s1-v3, koerper-e4-k2-s1-v4, koerper-e4-k2-s1-v5, koerper-e4-k2-s3-v1, koerper-e4-k2-s3-v3  
  `Zylinder:Radius # cm,Höhe # cm–Volumen auf eine Stelle?`
- B-091 (2 Zeilen): pyramide-kegel-kugel-zone-f3-v2, pyramide-kegel-kugel-zone-f3-v3  
  `Rechtwinkliges Dreieck,Katheten # m und # m–Hypotenuse?`
- B-092 (2 Zeilen): wahrscheinlichkeit-zone-f4-v1, wahrscheinlichkeit-zone-f4-v6  
  `Lose tragen die Nummern # bis #.Wie viele Lose sind es?`
- B-093 (2 Zeilen): flaechen-zone-f7-v1, flaechen-zone-f7-v3  
  `Kreis mit Radius r=# m–Fläche?Runde auf zwei Stellen.`
- B-094 (2 Zeilen): pythagoras-e1-k2-s3-v2, pythagoras-e1-k2-s4-v3  
  `Katheten a=# m,b=# m–Hypotenuse c auf eine Dezimale?`
- B-095 (2 Zeilen): terme-e4-k1-s3-v3, terme-e4-k1-s4-v3  
  `Klammere den größten gemeinsamen Faktor aus:#y^#+#y`
- B-096 (3 Zeilen): brueche-dezimalzahlen-zone-f3-v1, brueche-dezimalzahlen-zone-f3-v2, brueche-dezimalzahlen-zone-f3-v3  
  `#^\circ von #^\circ–welcher Anteil vom Vollkreis?`
- B-097 (5 Zeilen): pyramide-kegel-kugel-e3-k1-s1-v1, pyramide-kegel-kugel-e3-k1-s1-v2, pyramide-kegel-kugel-e3-k1-s1-v4, pyramide-kegel-kugel-e3-k1-s3-v1, pyramide-kegel-kugel-e3-k1-s3-v3  
  `Kugel:Radius # cm–Volumen?Runde auf eine Stelle.`
- B-098 (2 Zeilen): terme-e4-k1-s1-v1, terme-e4-k1-s4-v1  
  `Klammere den größten gemeinsamen Faktor aus:#x+#`
- B-099 (6 Zeilen): brueche-dezimalzahlen-e2-k1-s5-v1, brueche-dezimalzahlen-e2-k1-s5-v2, brueche-dezimalzahlen-e2-k1-s5-v3, brueche-dezimalzahlen-e2-k1-s6-v1, brueche-dezimalzahlen-e2-k1-s6-v2, brueche-dezimalzahlen-e2-k1-s6-v3  
  `Mache gleichnamig:\frac{#}{#}und\frac{#}{#}.`
- B-100 (3 Zeilen): potenzen-wurzeln-zone-f9-v2, potenzen-wurzeln-zone-f9-v3, potenzen-wurzeln-zone-f9-v4  
  `#–auf zwei Stellen nach dem Komma gerundet?`
- B-101 (2 Zeilen): pythagoras-e2-k2-s1-v1, pythagoras-e2-k2-s3-v2  
  `Hypotenuse c=# cm,Kathete b=# cm–Kathete a?`
- B-102 (3 Zeilen): reelle-zahlen-e2-k1-s2-v1, reelle-zahlen-e2-k1-s2-v2, reelle-zahlen-e2-k1-s5-v1  
  `#^#\cdot #^#–als eine Potenz und als Zahl?`
- B-103 (2 Zeilen): potenzen-wurzeln-zone-f9-v1, potenzen-wurzeln-zone-f9-v5  
  `#–auf eine Stelle nach dem Komma gerundet?`
- B-104 (2 Zeilen): flaechen-e1-k2-s1-v1, flaechen-e1-k2-s2-v1  
  `Rechteck,a=# cm,b=# cm–Fläche und Umfang?`
- B-105 (2 Zeilen): pythagoras-e2-k2-s1-v5, pythagoras-e2-k2-s3-v1  
  `Hypotenuse c=# m,Kathete b=# m–Kathete a?`
- B-106 (2 Zeilen): einheiten-zone-f6-v2, einheiten-zone-f6-v4  
  `Schnittstellen bei x=-# und x=#–Abstand?`
- B-107 (2 Zeilen): flaecheninhalt-und-volumen-im-raum-zone-f6-v1, flaecheninhalt-und-volumen-im-raum-zone-f6-v3  
  `Löse\tfrac{#}{#}\cdot #\cdot h=# nach h.`
- B-108 (2 Zeilen): einheiten-zone-f11-v1, einheiten-zone-f11-v3  
  `Rechteck,# m lang und # m breit–Fläche?`
- B-109 (2 Zeilen): prozentrechnung-zone-f1-v2, prozentrechnung-zone-f1-v5  
  `\frac{#}{#}–erweitere auf den Nenner #.`
- B-110 (2 Zeilen): stammfunktion-und-hauptsatz-zone-f3-v2, stammfunktion-und-hauptsatz-zone-f3-v4  
  `Welche Funktion hat die Ableitung #x^#?`
- B-111 (2 Zeilen): zinsrechnung-zone-f3-v1, zinsrechnung-zone-f3-v3  
  `#\%sind #€–wie viel Euro ist das Ganze?`
- B-112 (2 Zeilen): ebenen-zone-f2-v1, ebenen-zone-f2-v6  
  `A(#|#|#),B(#|#|#):\overrightarrow{AB}?`
- B-113 (3 Zeilen): reelle-zahlen-e2-k1-s3-v1, reelle-zahlen-e2-k1-s5-v2, reelle-zahlen-e2-k1-s5-v3  
  `#^#:#^#–als eine Potenz und als Zahl?`
- B-114 (3 Zeilen): reelle-zahlen-zone-f7-v1, reelle-zahlen-zone-f7-v3, reelle-zahlen-zone-f7-v4  
  `\frac{#}{#}+\frac{#}{#}–ausgerechnet?`
- B-115 (3 Zeilen): spiegelung-zone-f5-v1, spiegelung-zone-f5-v2, spiegelung-zone-f5-v4  
  `Mittelpunkt von A(#|#|#)und B(#|#|#)?`
- B-116 (2 Zeilen): potenzen-wurzeln-zone-f4-v2, potenzen-wurzeln-zone-f4-v5  
  `\frac{#}{#}\cdot\frac{#}{#}–wie viel?`
- B-117 (4 Zeilen): potenzen-wurzeln-e1-k4-s1-v1, potenzen-wurzeln-e1-k4-s1-v2, potenzen-wurzeln-e1-k4-s1-v3, potenzen-wurzeln-e1-k6-s1-v3  
  `\left(\frac{#}{#}\right)^#–wie viel?`
- B-118 (3 Zeilen): prozentrechnung-e4-k2-s1-v1, prozentrechnung-e4-k2-s2-v1, prozentrechnung-e4-k2-s3-v1  
  `#\%sind # kg–wie viel ist das Ganze?`
- B-119 (3 Zeilen): pythagoras-e1-k2-s1-v1, pythagoras-e1-k2-s1-v3, pythagoras-e1-k2-s4-v2  
  `Katheten a=# cm,b=# cm–Hypotenuse c?`
- B-120 (2 Zeilen): flaechen-e2-k1-s1-v1, flaechen-e2-k1-s3-v1  
  `Parallelogramm,g=# cm,h=# cm–Fläche?`
- B-121 (2 Zeilen): flaechen-e2-k1-s1-v4, flaechen-e2-k1-s3-v3  
  `Parallelogramm,g=# dm,h=# dm–Fläche?`
- B-122 (2 Zeilen): zinsrechnung-zone-f5-v2, zinsrechnung-zone-f5-v3  
  `Pro Tag #€–wie viel Euro für # Tage?`
- B-123 (3 Zeilen): prozentrechnung-e4-k2-s1-v3, prozentrechnung-e4-k2-s2-v3, prozentrechnung-e4-k2-s3-v2  
  `#\%sind # m–wie viel ist das Ganze?`
- B-124 (2 Zeilen): flaechen-e4-k1-s1-v1, flaechen-e4-k1-s2-v1  
  `Trapez,a=# cm,c=# cm,h=# cm–Fläche?`
- B-125 (6 Zeilen): einheiten-e2-k1-s6-v1, einheiten-e2-k1-s6-v2, einheiten-e2-k1-s6-v3, einheiten-e2-k1-s7-v1, einheiten-e2-k1-s7-v2, einheiten-e2-k1-s7-v3  
  `Von #:# Uhr bis #:# Uhr–wie lange?`
- B-126 (3 Zeilen): prozentrechnung-e4-k2-s1-v2, prozentrechnung-e4-k2-s2-v2, prozentrechnung-e4-k2-s3-v3  
  `#\%sind #€–wie viel ist das Ganze?`
- B-127 (3 Zeilen): pythagoras-e1-k2-s1-v2, pythagoras-e1-k2-s1-v5, pythagoras-e1-k2-s4-v1  
  `Katheten a=# m,b=# m–Hypotenuse c?`
- B-128 (2 Zeilen): brueche-dezimalzahlen-e4-k1-s8-v4, brueche-dezimalzahlen-e5-k2-s9-v8  
  `Setze<,=oder>ein:# __ #\%(P# # OS)`
- B-129 (2 Zeilen): flaechen-e2-k1-s1-v2, flaechen-e2-k1-s3-v2  
  `Parallelogramm,g=# m,h=# m–Fläche?`
- B-130 (3 Zeilen): binomische-formeln-e1-k1-s7-v1, binomische-formeln-e2-k2-s3-v1, binomische-formeln-e2-k2-s3-v3  
  `Multipliziere aus:(x+#)\cdot(x-#)`
- B-131 (2 Zeilen): binomische-formeln-e1-k1-s7-v2, binomische-formeln-e2-k2-s3-v2  
  `Multipliziere aus:(x-#)\cdot(x+#)`
- B-132 (2 Zeilen): brueche-dezimalzahlen-e4-k1-s8-v3, brueche-dezimalzahlen-e5-k2-s9-v7  
  `Setze<,=oder>ein:#\%__ #(P# # OS)`
- B-133 (2 Zeilen): reelle-zahlen-zone-f2-v1, reelle-zahlen-zone-f2-v4  
  `-# oder-#–welche Zahl ist größer?`
- B-134 (2 Zeilen): zuordnungen-zone-f5-v1, zuordnungen-zone-f5-v4  
  `Wie viele Minuten sind # Stunden?`
- B-135 (7 Zeilen): brueche-dezimalzahlen-e5-k2-s1-v1, brueche-dezimalzahlen-e5-k2-s1-v2, brueche-dezimalzahlen-e5-k2-s1-v3, brueche-dezimalzahlen-e5-k2-s1-v4, brueche-dezimalzahlen-e5-k2-s1-v5, brueche-dezimalzahlen-e5-k2-s2-v1, brueche-dezimalzahlen-e5-k2-s2-v2  
  `Welche Zahl ist größer:# oder #?`
- B-136 (3 Zeilen): hypothesentests-zone-f3-v1, hypothesentests-zone-f3-v2, hypothesentests-zone-f3-v3  
  `n=# p=#:Erwartungswert n\cdot p?`
- B-137 (2 Zeilen): flaechen-e4-k1-s1-v2, flaechen-e4-k1-s2-v2  
  `Trapez,a=# m,c=# m,h=# m–Fläche?`
- B-138 (2 Zeilen): rationale-zahlen-zone-f5-v1, rationale-zahlen-zone-f5-v3  
  `#\cdot x+# für x=#–welcher Wert?`
- B-139 (2 Zeilen): wahrscheinlichkeit-zone-f5-v2, wahrscheinlichkeit-zone-f5-v4  
  `Berechne\frac{#}{#}+\frac{#}{#}.`
- B-140 (3 Zeilen): strahlensaetze-zone-f2-v1, strahlensaetze-zone-f2-v4, strahlensaetze-zone-f2-v7  
  `#\text{m}–wie viele Zentimeter?`
- B-141 (2 Zeilen): punkte-und-strecken-im-koordinatensystem-e2-k1-s1-v5, punkte-und-strecken-im-koordinatensystem-zone-f3-v7  
  `K(#|#|#),L(#|#|#):Länge von KL?`
- B-142 (2 Zeilen): pythagoras-e1-k2-s9-v2, pythagoras-e3-k2-s6-v1  
  `Rechteck # m mal # m–Diagonale?`
- B-143 (2 Zeilen): wahrscheinlichkeit-zone-f2-v2, wahrscheinlichkeit-zone-f2-v4  
  `Wie viel sind #\%von # Feldern?`
- B-144 (6 Zeilen): potenzen-wurzeln-e2-k1-s7-v1, potenzen-wurzeln-e2-k1-s7-v2, potenzen-wurzeln-e2-k1-s7-v3, potenzen-wurzeln-e2-k1-s11-v1, potenzen-wurzeln-e2-k1-s11-v2, potenzen-wurzeln-e2-k1-s11-v3  
  `#–in Zehnerpotenzschreibweise?`
- B-145 (2 Zeilen): einheiten-zone-f8-v1, einheiten-zone-f8-v4  
  `# cm zum Quadrat–wie viel cm²?`
- B-146 (6 Zeilen): prozentrechnung-e1-k1-s2-v1, prozentrechnung-e1-k1-s2-v2, prozentrechnung-e1-k1-s2-v3, prozentrechnung-e1-k1-s3-v1, prozentrechnung-e1-k1-s3-v2, prozentrechnung-e1-k1-s3-v3  
  `\frac{#}{#}–wie viel Prozent?`
- B-147 (3 Zeilen): flaechen-e3-k1-s1-v1, flaechen-e3-k1-s1-v4, flaechen-e3-k1-s4-v1  
  `Dreieck,g=# cm,h=# cm–Fläche?`
- B-148 (3 Zeilen): trigonometrie-zone-f4-v1, trigonometrie-zone-f4-v2, trigonometrie-zone-f4-v3  
  `\frac{x}{#}=#–wie groß ist x?`
- B-149 (2 Zeilen): trigonometrie-zone-f4-v4, trigonometrie-zone-f4-v6  
  `\frac{#}{x}=#–wie groß ist x?`
- B-150 (2 Zeilen): ableitungsregeln-zone-f3-v3, ableitungsregeln-zone-f3-v4  
  `\frac{#}{#}\cdot #–gekürzt?`
- B-151 (2 Zeilen): flaechen-e3-k1-s1-v2, flaechen-e3-k1-s4-v2  
  `Dreieck,g=# m,h=# m–Fläche?`
- B-152 (2 Zeilen): rationale-zahlen-zone-f3-v2, rationale-zahlen-zone-f3-v5  
  `Berechne:\frac{#}{#}\cdot #`
- B-153 (3 Zeilen): bruchrechnung-zone-f6-v1, bruchrechnung-zone-f6-v3, bruchrechnung-zone-f6-v4  
  `\frac{#}{#}als Dezimalzahl`
- B-154 (2 Zeilen): einheiten-zone-f8-v2, einheiten-zone-f8-v3  
  `# m hoch drei–wie viel m³?`
- B-155 (4 Zeilen): prozentrechnung-zone-f5-v1, prozentrechnung-zone-f5-v2, prozentrechnung-zone-f5-v4, prozentrechnung-zone-f5-v5  
  `#–auf eine Dezimalstelle?`
- B-156 (3 Zeilen): quadratische-funktionen-zone-f4-v1, quadratische-funktionen-zone-f4-v2, quadratische-funktionen-zone-f4-v6  
  `(x+#)^#–ausmultipliziert?`
- B-157 (2 Zeilen): lineare-gleichungssysteme-e1-k1-s2-v2, lineare-gleichungssysteme-zone-f2-v3  
  `#x+#y=#–nach y umstellen.`
- B-158 (2 Zeilen): potenzen-wurzeln-zone-f1-v4, potenzen-wurzeln-zone-f2-v3  
  `#\cdot #\cdot #–wie viel?`
- B-159 (2 Zeilen): rotationsvolumen-zone-f1-v1, rotationsvolumen-zone-f1-v7  
  `(x+#)^# ausmultipliziert?`
- B-160 (9 Zeilen): potenzen-wurzeln-e1-k3-s10-v1, potenzen-wurzeln-e1-k3-s10-v2, potenzen-wurzeln-e1-k3-s10-v3, potenzen-wurzeln-e1-k3-s11-v1, potenzen-wurzeln-e1-k3-s11-v2, potenzen-wurzeln-e1-k3-s11-v3, potenzen-wurzeln-e1-k3-s12-v1, potenzen-wurzeln-e1-k3-s12-v2, potenzen-wurzeln-e1-k3-s12-v3  
  `#^x=#–welche Zahl ist x?`
- B-161 (3 Zeilen): zinsrechnung-zone-f1-v1, zinsrechnung-zone-f1-v3, zinsrechnung-zone-f1-v6  
  `#\%von #€–wie viel Euro?`
- B-162 (7 Zeilen): bruchrechnung-e1-k3-s1-v2, bruchrechnung-e1-k3-s1-v4, bruchrechnung-e1-k3-s2-v2, bruchrechnung-e1-k3-s4-v2, bruchrechnung-e1-k3-s4-v3, bruchrechnung-e1-k3-s5-v2, bruchrechnung-e1-k3-s5-v3  
  `\frac{#}{#}-\frac{#}{#}`
- B-163 (2 Zeilen): vierfeldertafel-zone-f3-v1, vierfeldertafel-zone-f3-v3  
  `P(A)=#–P(\overline{A})?`
- B-164 (2 Zeilen): winkel-dreiecke-zone-f2-v4, winkel-dreiecke-zone-f2-v6  
  `#^\circ-#^\circ-#^\circ`
- B-165 (6 Zeilen): potenzen-wurzeln-e2-k1-s4-v1, potenzen-wurzeln-e2-k1-s4-v2, potenzen-wurzeln-e2-k1-s4-v3, potenzen-wurzeln-e2-k1-s5-v1, potenzen-wurzeln-e2-k1-s5-v2, potenzen-wurzeln-e2-k1-s5-v3  
  `#\cdot #^{#}–wie viel?`
- B-166 (3 Zeilen): einheiten-zone-f4-v1, einheiten-zone-f4-v2, einheiten-zone-f4-v4  
  `Größere Zahl:# oder #?`
- B-167 (2 Zeilen): binomische-formeln-e3-k1-s4-v2, binomische-formeln-e3-k1-s5-v2  
  `Faktorisiere:#x^#+#x+#`
- B-168 (2 Zeilen): binomische-formeln-e3-k1-s4-v3, binomische-formeln-e3-k1-s5-v3  
  `Faktorisiere:#x^#-#x+#`
- B-169 (3 Zeilen): reelle-zahlen-zone-f3-v1, reelle-zahlen-zone-f3-v2, reelle-zahlen-zone-f3-v5  
  `\sqrt{#}–welche Zahl?`
- B-170 (3 Zeilen): vektoren-und-rechenoperationen-zone-f6-v1, vektoren-und-rechenoperationen-zone-f6-v2, vektoren-und-rechenoperationen-zone-f6-v4  
  `(#|#|#)\circ(#|#|#)=?`
- B-171 (2 Zeilen): flaecheninhalt-durch-integration-zone-f2-v2, flaecheninhalt-durch-integration-zone-f2-v4  
  `x^#-#x=#–Nullstellen?`
- B-172 (3 Zeilen): lineare-gleichungen-e1-k2-s2-v1, lineare-gleichungen-e1-k2-s2-v3, lineare-gleichungen-e1-k2-s3-v1  
  `#x+#=#–ist # Lösung?`
- B-173 (3 Zeilen): terme-e2-k4-s2-v2, terme-e2-k4-s7-v2, terme-e2-k4-s10-v2  
  `Fasse zusammen:#a-#a`
- B-174 (2 Zeilen): brueche-dezimalzahlen-zone-f2-v1, brueche-dezimalzahlen-zone-f2-v4  
  `# kg–wie viel Gramm?`
- B-175 (2 Zeilen): koerper-zone-f6-v1, koerper-zone-f6-v3  
  `#\%von # l–wie viel?`
- B-176 (2 Zeilen): lineare-funktionen-zone-f3-v4, lineare-funktionen-zone-f3-v6  
  `Rechne:-#\cdot(-#)+#`
- B-177 (2 Zeilen): lineare-gleichungen-e1-k2-s2-v2, lineare-gleichungen-e1-k2-s3-v2  
  `#x-#=#–ist # Lösung?`
- B-178 (2 Zeilen): pythagoras-zone-f2-v2, pythagoras-zone-f2-v6  
  `\sqrt{#+#}–wie viel?`
- B-179 (2 Zeilen): terme-e2-k4-s1-v4, terme-e2-k4-s10-v3  
  `Fasse zusammen:#b+#b`
- B-180 (2 Zeilen): terme-e2-k4-s2-v3, terme-e2-k4-s7-v3  
  `Fasse zusammen:#b-#b`
- B-181 (2 Zeilen): binomische-formeln-e3-k1-s4-v1, binomische-formeln-e3-k1-s5-v1  
  `Faktorisiere:#x^#-#`
- B-182 (2 Zeilen): binomische-formeln-zone-f7-v1, binomische-formeln-zone-f7-v4  
  `#x+#–ausgeklammert?`
- B-183 (2 Zeilen): pyramide-kegel-kugel-zone-f5-v3, pyramide-kegel-kugel-zone-f5-v4  
  `Vier Drittel von #?`
- B-184 (2 Zeilen): rationale-zahlen-zone-f4-v1, rationale-zahlen-zone-f4-v3  
  `Berechne:#+#\cdot #`
- B-185 (5 Zeilen): einheiten-e2-k1-s1-v2, einheiten-e2-k1-s1-v4, einheiten-e2-k1-s4-v1, einheiten-e2-k1-s4-v2, einheiten-e2-k1-s4-v3  
  `# h–wie viele min?`
- B-186 (4 Zeilen): einheiten-e2-k1-s2-v2, einheiten-e2-k1-s5-v1, einheiten-e2-k1-s5-v2, einheiten-e2-k1-s5-v3  
  `# min–wie viele h?`
- B-187 (3 Zeilen): einheiten-e2-k1-s2-v1, einheiten-e2-k1-s2-v3, einheiten-e2-k5-s1-v2  
  `# s–wie viele min?`
- B-188 (2 Zeilen): brueche-dezimalzahlen-e4-k1-s1-v4, brueche-dezimalzahlen-e4-k1-s2-v3  
  `#–als Zehnerbruch?`
- B-189 (2 Zeilen): brueche-dezimalzahlen-zone-f7-v4, brueche-dezimalzahlen-zone-f7-v6  
  `#\%–als Kommazahl?`
- B-190 (7 Zeilen): quadratische-gleichungen-e2-k1-s1-v1, quadratische-gleichungen-e2-k1-s1-v2, quadratische-gleichungen-e2-k1-s1-v3, quadratische-gleichungen-e2-k1-s1-v4, quadratische-gleichungen-e2-k1-s1-v5, quadratische-gleichungen-e2-k1-s4-v1, quadratische-gleichungen-e2-k1-s4-v3  
  `(x-#)\cdot(x-#)=#`
- B-191 (3 Zeilen): reelle-zahlen-e2-k2-s1-v1, reelle-zahlen-zone-f6-v5, reelle-zahlen-zone-f6-v7  
  `#^{-#}–als Bruch?`
- B-192 (2 Zeilen): flaechen-zone-f1-v1, flaechen-zone-f1-v3  
  `# m–wie viele cm?`
- B-193 (2 Zeilen): reelle-zahlen-zone-f6-v2, reelle-zahlen-zone-f6-v4  
  `#^#–ausgerechnet?`
- B-194 (2 Zeilen): terme-zone-f4-v3, terme-zone-f4-v4  
  `Rechne:#-#\cdot #`
- B-195 (8 Zeilen): brueche-dezimalzahlen-e1-k2-s1-v1, brueche-dezimalzahlen-e1-k2-s1-v2, brueche-dezimalzahlen-e1-k2-s1-v3, brueche-dezimalzahlen-e1-k2-s1-v4, brueche-dezimalzahlen-e1-k2-s1-v5, brueche-dezimalzahlen-e1-k2-s2-v1, brueche-dezimalzahlen-e1-k2-s2-v2, brueche-dezimalzahlen-e1-k2-s2-v3  
  `\frac{#}{#}von #`
- B-196 (2 Zeilen): einheiten-e1-k2-s5-v3, einheiten-e1-k2-s8-v3  
  `# kg–wie viel g?`
- B-197 (3 Zeilen): grenzwerte-und-verhalten-im-unendlichen-zone-f1-v1, grenzwerte-und-verhalten-im-unendlichen-zone-f1-v2, grenzwerte-und-verhalten-im-unendlichen-zone-f1-v3  
  `Berechne:(-#)^#`
- B-198 (2 Zeilen): rationale-zahlen-e2-k3-s3-v1, rationale-zahlen-e2-k3-s6-v3  
  `Berechne:#-(-#)`
- B-199 (2 Zeilen): winkel-dreiecke-zone-f2-v1, winkel-dreiecke-zone-f2-v3  
  `#^\circ+#^\circ`
- B-200 (4 Zeilen): potenzen-wurzeln-e1-k3-s6-v1, potenzen-wurzeln-e1-k3-s6-v2, potenzen-wurzeln-e1-k3-s6-v3, potenzen-wurzeln-zone-f3-v5  
  `-#^#–wie viel?`
- B-201 (2 Zeilen): rationale-zahlen-zone-f4-v4, rationale-zahlen-zone-f4-v6  
  `Berechne:#-#:#`
- B-202 (6 Zeilen): bruchrechnung-e3-k3-s1-v1, bruchrechnung-e3-k3-s1-v2, bruchrechnung-e3-k3-s1-v3, bruchrechnung-e3-k3-s1-v4, bruchrechnung-e3-k3-s1-v5, bruchrechnung-e3-k3-s4-v3  
  `\frac{#}{#}:#`
- B-203 (4 Zeilen): rationale-zahlen-e2-k3-s1-v1, rationale-zahlen-e2-k3-s1-v2, rationale-zahlen-e2-k3-s1-v4, rationale-zahlen-e2-k3-s6-v1  
  `Berechne:-#+#`
- B-204 (2 Zeilen): rationale-zahlen-e2-k3-s1-v3, rationale-zahlen-e2-k3-s6-v2  
  `Berechne:-#-#`
- B-205 (2 Zeilen): winkel-dreiecke-zone-f3-v1, winkel-dreiecke-zone-f3-v3  
  `# km in Meter`
- B-206 (2 Zeilen): lineare-funktionen-zone-f5-v3, lineare-funktionen-zone-f5-v4  
  `Löse:#=-#x+#`
- B-207 (2 Zeilen): rationale-zahlen-zone-f1-v2, rationale-zahlen-zone-f1-v3  
  `Berechne:#:#`
- B-208 (2 Zeilen): rationale-zahlen-zone-f1-v4, rationale-zahlen-zone-f3-v3  
  `Berechne:#-#`
- B-209 (2 Zeilen): rationale-zahlen-zone-f3-v1, rationale-zahlen-zone-f3-v4  
  `Berechne:#+#`
- B-210 (3 Zeilen): prozentrechnung-e3-k1-s2-v1, prozentrechnung-e3-k1-s3-v3, prozentrechnung-e3-k1-s7-v1  
  `#\%von # kg`
- B-211 (2 Zeilen): terme-zone-f1-v2, terme-zone-f1-v3  
  `Rechne:-#+#`
- B-212 (2 Zeilen): terme-zone-f1-v4, terme-zone-f1-v6  
  `Rechne:-#-#`
- B-213 (10 Zeilen): quadratische-gleichungen-e3-k3-s1-v1, quadratische-gleichungen-e3-k3-s1-v2, quadratische-gleichungen-e3-k3-s1-v3, quadratische-gleichungen-e3-k3-s1-v4, quadratische-gleichungen-e3-k3-s1-v5, quadratische-gleichungen-e3-k3-s6-v2, quadratische-gleichungen-e3-k3-s6-v3, quadratische-gleichungen-e3-k3-s7-v1, quadratische-gleichungen-e3-k3-s7-v3, quadratische-gleichungen-e3-k3-s9-v2  
  `x^#+#x+#=#`
- B-214 (6 Zeilen): quadratische-gleichungen-e3-k3-s2-v3, quadratische-gleichungen-e3-k3-s5-v1, quadratische-gleichungen-e3-k3-s5-v3, quadratische-gleichungen-e3-k3-s6-v1, quadratische-gleichungen-e3-k3-s7-v2, quadratische-gleichungen-e3-k3-s9-v1  
  `x^#-#x+#=#`
- B-215 (3 Zeilen): prozentrechnung-e3-k1-s2-v3, prozentrechnung-e3-k1-s5-v3, prozentrechnung-e3-k1-s7-v3  
  `#\%von # m`
- B-216 (2 Zeilen): gleichungen-loesen-zone-f4-v1, gleichungen-loesen-zone-f4-v4  
  `Löse:x^#=#`
- B-217 (2 Zeilen): quadratische-gleichungen-e3-k3-s2-v1, quadratische-gleichungen-e3-k3-s9-v3  
  `x^#-#x-#=#`
- B-218 (2 Zeilen): quadratische-gleichungen-e3-k3-s2-v2, quadratische-gleichungen-e3-k3-s5-v2  
  `x^#+#x-#=#`
- B-219 (2 Zeilen): terme-zone-f1-v1, terme-zone-f3-v3  
  `Rechne:#-#`
- B-220 (2 Zeilen): terme-zone-f3-v1, terme-zone-f3-v4  
  `Rechne:#+#`
- B-221 (6 Zeilen): prozentrechnung-e3-k1-s2-v2, prozentrechnung-e3-k1-s3-v1, prozentrechnung-e3-k1-s3-v2, prozentrechnung-e3-k1-s5-v1, prozentrechnung-e3-k1-s5-v2, prozentrechnung-e3-k1-s7-v2  
  `#\%von #€`
- B-222 (5 Zeilen): quadratische-gleichungen-e1-k2-s9-v1, quadratische-gleichungen-e1-k2-s9-v2, quadratische-gleichungen-e1-k2-s9-v3, quadratische-gleichungen-e1-k2-s10-v2, quadratische-gleichungen-e1-k2-s10-v3  
  `(x+#)^#=#`
- B-223 (4 Zeilen): quadratische-gleichungen-e1-k2-s8-v1, quadratische-gleichungen-e1-k2-s8-v2, quadratische-gleichungen-e1-k2-s8-v3, quadratische-gleichungen-e1-k2-s10-v1  
  `(x-#)^#=#`
- B-224 (4 Zeilen): lineare-gleichungen-e3-k1-s1-v1, lineare-gleichungen-e3-k1-s1-v2, lineare-gleichungen-e3-k1-s1-v4, lineare-gleichungen-e3-k2-s1-v3  
  `#x=#x+#`
- B-225 (2 Zeilen): lineare-gleichungen-zone-f3-v4, lineare-gleichungen-zone-f3-v8  
  `#x+#+#x`
- B-226 (8 Zeilen): quadratische-gleichungen-e1-k2-s1-v1, quadratische-gleichungen-e1-k2-s1-v2, quadratische-gleichungen-e1-k2-s1-v3, quadratische-gleichungen-e1-k2-s1-v4, quadratische-gleichungen-e1-k2-s1-v5, quadratische-gleichungen-e1-k2-s3-v1, quadratische-gleichungen-e1-k2-s3-v2, quadratische-gleichungen-e1-k2-s3-v3  
  `x^#=#`
- B-227 (2 Zeilen): lineare-gleichungen-zone-f3-v2, lineare-gleichungen-zone-f3-v6  
  `#x-#x`
- B-228 (9 Zeilen): bruchrechnung-e2-k1-s1-v1, bruchrechnung-e2-k1-s1-v3, bruchrechnung-e2-k1-s1-v5, bruchrechnung-e2-k1-s2-v1, bruchrechnung-e2-k1-s3-v1, bruchrechnung-e2-k1-s3-v3, bruchrechnung-e2-k2-s1-v1, bruchrechnung-e2-k2-s1-v2, bruchrechnung-e2-k2-s1-v3  
  `#+#`

## B Bis auf Zahlen gleich, in derselben Sprosse (Varianten)

Nach bank.md unterscheiden sich Varianten einer Sprosse in Zahlen und Kontext; hier fehlt der andere Kontext (oder die Aufgabe hat keinen). Nur Kennung, Zeilen und Text gekürzt.

- B-229 (2): schnittmengen-e3-k1-s5-v1, schnittmengen-e3-k1-s5-v3 – `Die Abbildung zeigt den Quader mit A(#|#|#),B(#|#|#),C(#|#|#)und F(#|#|#),die Gerade h durch B und F sowie die Schnittfi …`
- B-230 (2): schnittmengen-e3-k1-s2-v1, schnittmengen-e3-k1-s2-v2 – `Ein Holzkörper ist eine Pyramide über dem Quadrat ABCD mit A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)und der Spitze E(#|#|#)sen …`
- B-231 (2): spiegelung-e2-k1-s5-v1, spiegelung-e2-k1-s5-v2 – `Die Abbildung zeigt die Punkte A,B und P in der x_#x_#-Ebene.g geht durch A und P,g^*durch B und P;g^*entsteht aus g dur …`
- B-232 (2): vektoren-und-rechenoperationen-e2-k2-s3-v1, vektoren-und-rechenoperationen-e2-k2-s3-v2 – `Gib\overrightarrow{AP}mit\vec u,\vec v,\vec w an.‖Grafik:\begin{ksys#}[x#max=#]\rquader{#}{#}{#}{#}\rpunkt*{#}{#}{#}{A}\ …`
- B-233 (3): punkte-und-strecken-im-koordinatensystem-e1-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e1-k1-s7-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s7-v3 – `Eine Pyramide hat den quadratischen Boden ABCD mit der Seite # cm;die Spitze S liegt # cm senkrecht über A.Im Gitter sin …`
- B-234 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v5, punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v6 – `Eine Pyramide hat den quadratischen Boden ABCD mit der Seite # in der x_#x_#-Ebene,A im Ursprung,B auf der x_#-Achse,D a …`
- B-235 (2): extremalprobleme-e1-k1-s5-v3, extremalprobleme-e1-k1-s5-v4 – `Gegeben ist f(x)=-#x^#+#x^#+#.Die Punkte O(#|#),P(#|#)und Q(#|f(#))bilden ein rechtwinkliges Dreieck.Zeichne es ein,bere …`
- B-236 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s7-v5, flaecheninhalt-und-volumen-im-raum-e1-k2-s7-v6 – `Der Flächeninhalt des Dreiecks PQR im Koordinatensystem wird mit dem Term #\cdot #-#\cdot\tfrac{#}{#}\cdot #\cdot #-\tfr …`
- B-237 (3): konfidenzintervalle-e1-k1-s2-v1, konfidenzintervalle-e1-k1-s2-v2, konfidenzintervalle-e1-k1-s2-v3 – `Vermutet wird ein Anteil von #\%.In einer Stichprobe vom Umfang n=# gibt es # Treffer.Lies das Konfidenzintervall zur Si …`
- B-238 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v7, punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v8 – `Ein Körper hat den rechteckigen Boden A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)und die Firstkante P(#|#|#),Q(#|#|#);die Dreiec …`
- B-239 (2): ableitung-und-aenderungsrate-e1-k1-s10-v3, ableitung-und-aenderungsrate-e1-k1-s10-v4 – `Die CO_#-Konzentration in einem Raum wird durch g(x)=-#\cdot\mathrm{e}^{-#x}+# beschrieben(x in Stunden,g(x)in ppm).Weis …`
- B-240 (2): lineare-funktionen-e5-k1-s5-v1, lineare-funktionen-e5-k1-s5-v2 – `Welches Mietauto?Angebot #:#€Miete pro Tag,# km insgesamt frei,jeder weitere km #€.Angebot #:einmalig #€für eine Woche,j …`
- B-241 (4): konfidenzintervalle-e1-k1-s1-v1, konfidenzintervalle-e1-k1-s1-v2, konfidenzintervalle-e1-k1-s1-v3, konfidenzintervalle-e1-k1-s1-v5 – `Die Grafik zeigt Grenzgraphen für Stichproben vom Umfang n=#(Sicherheitswahrscheinlichkeit #\%).In einer Stichprobe gibt …`
- B-242 (2): skalarprodukt-und-winkel-e4-k2-s1-v1, skalarprodukt-und-winkel-e4-k2-s1-v2 – `Eine gerade Pyramide hat ihre quadratische Grundfläche in der xy-Ebene,eine Ecke F(#\mid #\mid #)und die Spitze S(#\mid …`
- B-243 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s4-v1, flaecheninhalt-und-volumen-im-raum-e1-k2-s4-v2 – `Licht fällt in Richtung(#|#|-#)auf das Dreieck mit P(#|#|#),Q(#|#|#),R(#|#|#).Bestimme die Schattenpunkte in der x-y-Ebe …`
- B-244 (2): flaecheninhalt-durch-integration-e4-k1-s6-v3, flaecheninhalt-durch-integration-e4-k1-s6-v4 – `Für a># schließt der Graph von f_a(x)=x^#-a^# im vierten Quadranten mit den Koordinatenachsen eine Fläche ein.Das Dreiec …`
- B-245 (3): strahlensaetze-e2-k2-s1-v1, strahlensaetze-e2-k2-s1-v2, strahlensaetze-e2-k2-s1-v3 – `Das Dreieck A'B'C'ist das Bild von ABC bei einer zentrischen Streckung.Zeichne Geraden durch A und A',B und B',C und C'. …`
- B-246 (3): punkte-und-strecken-im-koordinatensystem-e5-k1-s6-v1, punkte-und-strecken-im-koordinatensystem-e5-k1-s6-v2, punkte-und-strecken-im-koordinatensystem-e5-k1-s6-v3 – `Ein Dachgeschoss hat einen rechteckigen Boden von # m mal # m.Die Dachflächen steigen von den beiden Traufwänden(Höhe # …`
- B-247 (3): kenngroessen-von-verteilungen-e3-k3-s1-v1, kenngroessen-von-verteilungen-e3-k3-s1-v2, kenngroessen-von-verteilungen-e3-k3-s1-v3 – `Die Diagramme zeigen die Verteilungen von X und Y,beide binomialverteilt mit n=#;die Erwartungswerte sind ganzzahlig.Lie …`
- B-248 (2): ableitung-und-aenderungsrate-e3-k1-s1-v3, ableitung-und-aenderungsrate-e3-k1-s1-v5 – `Gegeben ist f(x)=#x^# und der Punkt P(#|#)auf dem Graphen.Berechne die Steigung m der Sekante durch P und Q(#+h|f(#+h))f …`
- B-249 (2): lineare-funktionen-e2-k5-s6-v1, lineare-funktionen-e2-k5-s6-v2 – `Welche Gleichung gehört zu welcher Geraden?Ordne den Geraden f,g und h je eine der Gleichungen zu:y=-#x+#;y=-\frac{#}{#} …`
- B-250 (2): uneigentliche-integrale-e2-k1-s0-v2, uneigentliche-integrale-e2-k1-s0-v3 – `Die Fläche R rechts von x=# ist schraffiert.Fällt sie gegenüber der Fläche links davon ins Gewicht?\\kreuz{fällt ins Gew …`
- B-251 (2): symmetrie-abbildungen-e3-k1-s8-v1, symmetrie-abbildungen-e3-k1-s8-v2 – `Die Dreiecke ABC und DEF sind der Anfang eines Bandornaments.Zeichne die nächsten zwei Dreiecke und benenne die Abbildun …`
- B-252 (2): lineare-gleichungssysteme-e5-k1-s8-v1, lineare-gleichungssysteme-e5-k1-s8-v3 – `Aussage nachweisen:Eine Mischung aus drei Sorten hat die Anteile x,y und z;keiner ist negativ.Das zugehörige Gleichungss …`
- B-253 (2): normalverteilung-und-sigma-regeln-e3-k1-s1-v4, normalverteilung-und-sigma-regeln-e3-k1-s1-v5 – `Die Abbildung zeigt den Graphen der Verteilungsfunktion F einer normalverteilten Zufallsgröße X.Lies\mu und\sigma ab.(Ab …`
- B-254 (2): flaecheninhalt-durch-integration-e5-k1-s7-v3, flaecheninhalt-durch-integration-e5-k1-s7-v4 – `f(x)=x^# für #\le x\le #;sein Graph wird an der Geraden y=x gespiegelt.Begründe,dass der Term #\cdot # minus Integral vo …`
- B-255 (2): trigonometrische-funktionen-e2-k1-s0-v1, trigonometrische-funktionen-e2-k1-s0-v3 – `Wo ist die Welle zu Ende?Welcher Abschnitt ist genau eine ganze Wiederholung?\\kreuz{von A bis B}\\kreuz{von A bis C}‖Gr …`
- B-256 (2): zinsrechnung-e2-k2-s1-v2, zinsrechnung-e2-k2-s1-v3 – `Start #€,Zinssatz #\%.Am Ende jedes Jahres kommen erst die Zinsen,dann #€Einzahlung dazu.Fülle die Tabelle aus–Guthaben …`
- B-257 (2): flaecheninhalt-und-volumen-im-raum-e2-k3-s3-v1, flaecheninhalt-und-volumen-im-raum-e2-k3-s3-v3 – `Stelle für das Viereck PQRS im Koordinatensystem einen Flächenterm„Rechteck plus rechtwinkliges Dreieck“auf und berechne …`
- B-258 (2): punkte-und-strecken-im-koordinatensystem-e1-k1-s4-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s4-v3 – `Ein Quader hat eine Ecke im Ursprung O und die Kanten # # und # entlang der x_#-,x_#-und x_#-Achse.P(#|#|#)liegt auf ein …`
- B-259 (3): strahlensaetze-e2-k1-s2-v1, strahlensaetze-e2-k1-s2-v2, strahlensaetze-e2-k1-s2-v3 – `Das Zentrum Z liegt außerhalb des Dreiecks ABC.Zeichne Strahlen von Z durch die Ecken und strecke mit k=#.Gib die Bildpu …`
- B-260 (2): extremalprobleme-e3-k1-s8-v3, extremalprobleme-e3-k1-s8-v4 – `Die Zielfunktion A(x)=-#x^#+x^#+#x beschreibt für #<x<# den Flächeninhalt eines Dreiecks unter einem Graphen.Bestimme di …`
- B-261 (2): punkte-und-strecken-im-koordinatensystem-e2-k1-s9-v5, punkte-und-strecken-im-koordinatensystem-e2-k1-s9-v6 – `Ein Ball fliegt vereinfacht geradlinig:Nach t Sekunden ist er in\vec x=(#|#|#)+t\cdot(#|#|-#)(# LE=# m,Boden ist die x_# …`
- B-262 (2): symmetrie-abbildungen-e2-k3-s5-v1, symmetrie-abbildungen-e2-k3-s5-v3 – `Die Punkte A,B,C,D sind die halbe Figur,a ist die Symmetrieachse.Ergänze die Figur zur achsensymmetrischen.‖Grafik:\begi …`
- B-263 (2): ableitung-und-aenderungsrate-e2-k1-s8-v1, ableitung-und-aenderungsrate-e2-k1-s8-v2 – `Die Abbildung zeigt den Graphen einer Funktion f.Beurteile die Aussage:„Für #\le x\le # ist die Steigung des Graphen kle …`
- B-264 (2): trigonometrie-e4-k1-s16-v3, trigonometrie-e4-k1-s16-v4 – `Eine Rampe y führt auf eine Treppe.Im Dreieck aus Rampe,waagerechter Strecke(# cm)und der Verbindung Treppenfuß–obere St …`
- B-265 (3): winkel-dreiecke-e5-k1-s5-v1, winkel-dreiecke-e5-k1-s5-v2, winkel-dreiecke-e5-k1-s5-v3 – `Zeichne das Dreieck ABC und mit dem Geodreieck die Höhe von C auf die Seite AB,wenn nötig auf ihre Verlängerung.Gib den …`
- B-266 (3): symmetrie-abbildungen-e3-k1-s2-v1, symmetrie-abbildungen-e3-k1-s2-v2, symmetrie-abbildungen-e3-k1-s2-v3 – `Das Dreieck ABC wurde auf A'B'C'verschoben.Beschreibe die Verschiebung in Kästchen.‖Grafik:\begin{ksys}[xmin=#xmax=#ymin …`
- B-267 (2): flaecheninhalt-und-volumen-im-raum-e1-k3-s3-v1, flaecheninhalt-und-volumen-im-raum-e1-k3-s3-v3 – `Stelle für das Dreieck PQR im Koordinatensystem einen Flächenterm„Rechteck minus Randdreiecke“auf und berechne den Fläch …`
- B-268 (2): trigonometrie-e3-k1-s17-v3, trigonometrie-e3-k1-s17-v4 – `Ein rechtwinkliges Trapez hat die senkrechten Seiten # cm und # cm und die waagerechte Grundseite # cm.\alpha ist der Wi …`
- B-269 (2): flaecheninhalt-und-volumen-im-raum-e3-k1-s6-v4, flaecheninhalt-und-volumen-im-raum-e3-k1-s6-v5 – `Die Grundfläche der Pyramide PQRS ist ein rechtwinkliges Dreieck PQR mit der Hypotenuse|PQ|=#\mathrm{cm}und der Kathete| …`
- B-270 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s10-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s10-v2 – `Ein Quadrat liegt in der x_#x_#-Ebene;P(#|#|#)ist eine Ecke.Der Schnittpunkt seiner Diagonalen liegt auf der Geraden dur …`
- B-271 (4): strahlensaetze-e2-k1-s1-v1, strahlensaetze-e2-k1-s1-v2, strahlensaetze-e2-k1-s1-v4, strahlensaetze-e2-k1-s1-v5 – `Strecke das Dreieck ABC vom Zentrum Z=A aus mit dem Streckfaktor k=#.Zeichne das Bilddreieck und gib die Bildpunkte an.‖ …`
- B-272 (2): lineare-funktionen-e5-k2-s1-v1, lineare-funktionen-e5-k2-s1-v2 – `Welcher Graph passt zum Tarif?Tarif:#€Grundgebühr und #€je Stunde.Gib den passenden Graphen an.‖Grafik:\begin{ksys}[xmin …`
- B-273 (2): normalverteilung-und-sigma-regeln-e2-k1-s5-v1, normalverteilung-und-sigma-regeln-e2-k1-s5-v2 – `Die Abbildung zeigt die Dichte von X mit dem Erwartungswert #.Jemand rechnet:P(#\le X\le #)\approx #\cdot #=# somit P(|X …`
- B-274 (5): symmetrie-abbildungen-e3-k1-s1-v1, symmetrie-abbildungen-e3-k1-s1-v2, symmetrie-abbildungen-e3-k1-s1-v3, symmetrie-abbildungen-e3-k1-s1-v4, symmetrie-abbildungen-e3-k1-s1-v5 – `Der Verschiebungspfeil führt von P nach Q.Verschiebe das Dreieck ABC mit diesem Pfeil.‖Grafik:\begin{ksys}[xmin=#xmax=#y …`
- B-275 (4): flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v1, flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v2, flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v3, flaecheninhalt-und-volumen-im-raum-e4-k1-s1-v4 – `Ein Quader hat die Grundfläche PQRU mit P(#|#|#),Q(#|#|#),R(#|#|#),U(#|#|#)und die Höhe #.Die Ebene durch Q,U und T(#|#| …`
- B-276 (3): winkel-dreiecke-e2-k2-s5-v1, winkel-dreiecke-e2-k2-s5-v2, winkel-dreiecke-e2-k2-s5-v3 – `g\parallel h,g liegt oben,h unten,die Gerade k schneidet beide.An g liegt oberhalb von g rechts von k ein Winkel von #^\ …`
- B-277 (2): winkel-dreiecke-e2-k2-s6-v2, winkel-dreiecke-e2-k2-s6-v3 – `g\parallel h,g liegt oben,h unten,die Gerade k schneidet beide.An g liegt unterhalb von g links von k ein Winkel von #^\ …`
- B-278 (3): winkel-dreiecke-e2-k2-s7-v1, winkel-dreiecke-e2-k2-s7-v2, winkel-dreiecke-e2-k2-s7-v3 – `g\parallel h,g liegt oben,h unten,die Gerade k schneidet beide.An g liegt oberhalb von g rechts von k ein Winkel von #^\ …`
- B-279 (3): winkel-dreiecke-e5-k1-s2-v1, winkel-dreiecke-e5-k1-s2-v2, winkel-dreiecke-e5-k1-s2-v3 – `Zeichne das spitzwinklige Dreieck ABC.Konstruiere zwei Mittelsenkrechten und den Umkreis.Gib den Mittelpunkt U an.‖Grafi …`
- B-280 (2): geraden-e3-k1-s6-v1, geraden-e3-k1-s6-v2 – `Gegeben sind g\colon\vec x=(#|#|#)+r\cdot(#|#|#)und die dazu echt parallele Gerade p\colon\vec x=(#|#|#)+r\cdot(#|#|#).E …`
- B-281 (2): strahlensaetze-e2-k1-s3-v1, strahlensaetze-e2-k1-s3-v3 – `Verkleinere das Dreieck ABC vom Zentrum Z aus mit k=#.Zeichne das Bild und gib die Bildpunkte an.‖Grafik:\begin{ksys}[xm …`
- B-282 (2): uneigentliche-integrale-e2-k1-s2-v2, uneigentliche-integrale-e2-k1-s2-v3 – `Der Graph von f(x)=#e^{-#x}ist gezeichnet.Markiere die Restfläche zwischen x=# und einem großen w und begründe,warum sie …`
- B-283 (2): winkel-dreiecke-e5-k1-s7-v1, winkel-dreiecke-e5-k1-s7-v2 – `Zeichne eine Strecke AB von # cm Länge und darüber den Thaleskreis.Wähle einen Punkt C darauf und zeichne das Dreieck AB …`
- B-284 (2): binomialverteilung-e5-k1-s8-v1, binomialverteilung-e5-k1-s8-v2 – `X ist binomialverteilt mit # Versuchen und der Trefferwahrscheinlichkeit #;die Verteilung ist symmetrisch.Es gilt P(X\ge …`
- B-285 (2): tangente-normale-schnittwinkel-e2-k1-s9-v1, tangente-normale-schnittwinkel-e2-k1-s9-v2 – `Ein Hügelprofil wird für-#\le x\le # durch f(x)=-\frac{#}{#}x^#+# beschrieben(# LE=# m).Eine Kamera steht im Punkt K(#|# …`
- B-286 (2): winkel-dreiecke-e2-k2-s4-v2, winkel-dreiecke-e2-k2-s4-v3 – `Die Geraden g und h schneiden sich;zwischen ihnen liegt\alpha=#^\circ.Eine dritte Gerade durch den Schnittpunkt teilt de …`
- B-287 (2): binomialverteilung-e5-k2-s1-v1, binomialverteilung-e5-k2-s1-v2 – `X ist binomialverteilt mit # Versuchen und der Trefferwahrscheinlichkeit #.In einem Diagramm sind die Säulen von # bis z …`
- B-288 (5): trigonometrische-funktionen-e1-k1-s1-v1, trigonometrische-funktionen-e1-k1-s1-v2, trigonometrische-funktionen-e1-k1-s1-v3, trigonometrische-funktionen-e1-k1-s1-v4, trigonometrische-funktionen-e1-k1-s1-v5 – `Zeichne den Punkt P zum Winkel #°auf dem Einheitskreis ein.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#xstep=#ystep=# …`
- B-289 (3): zinsrechnung-e2-k1-s3-v1, zinsrechnung-e2-k1-s3-v2, zinsrechnung-e2-k1-s3-v3 – `Zinssatz #\%.Zinsen vom Guthaben der Zeile davor,neues Guthaben=altes Guthaben+Zinsen+Einzahlung.Ergänze Jahr #.‖Grafik: …`
- B-290 (3): pythagoras-e1-k3-s1-v1, pythagoras-e1-k3-s1-v2, pythagoras-e1-k3-s1-v3 – `Dreieck ABC,rechter Winkel bei A.Zeichne die Quadrate über allen drei Seiten.Wie viele Kästchen hat jedes?‖Grafik:\begin …`
- B-291 (3): strahlensaetze-e2-k1-s7-v1, strahlensaetze-e2-k1-s7-v2, strahlensaetze-e2-k1-s7-v3 – `Dreieck ABC hat die Seiten #\text{cm},#\text{cm}und #\text{cm},Dreieck DEF die Seiten #\text{cm},#\text{cm}und #\text{cm …`
- B-292 (2): trigonometrie-e3-k1-s17-v5, trigonometrie-e3-k1-s17-v6 – `Im Dreieck ABC liegt F auf AC,BF steht senkrecht auf AC.AB=# cm,der Winkel bei A ist #^\circ,\angle FBA=#^\circ,\angle C …`
- B-293 (5): winkel-dreiecke-e5-k1-s1-v1, winkel-dreiecke-e5-k1-s1-v2, winkel-dreiecke-e5-k1-s1-v3, winkel-dreiecke-e5-k1-s1-v4, winkel-dreiecke-e5-k1-s1-v5 – `Verbinde A und B und konstruiere mit dem Zirkel die Mittelsenkrechte der Strecke AB.In welchem Punkt schneidet sie AB?‖G …`
- B-294 (3): geraden-e4-k1-s3-v1, geraden-e4-k1-s3-v2, geraden-e4-k1-s3-v3 – `Ein Seil ist geradlinig zwischen zwei Masten gespannt;die Fußpunkte sind F_#(#|#|#)und F_#(#|#|#),befestigt ist es in # …`
- B-295 (2): trigonometrie-e4-k1-s16-v5, trigonometrie-e4-k1-s16-v6 – `Von einer Plattform aus werden zwei Sichtlinien gepeilt.Im Dreieck ACD ist CD=# m,der Winkel bei A zwischen den Sichtlin …`
- B-296 (2): winkel-dreiecke-e2-k2-s8-v2, winkel-dreiecke-e2-k2-s8-v3 – `Im Dreieck ABC ist der Winkel bei C #^\circ groß.Die Seiten AB und CB werden über B hinaus verlängert;zwischen den beide …`
- B-297 (3): symmetrie-abbildungen-e3-k1-s4-v1, symmetrie-abbildungen-e3-k1-s4-v2, symmetrie-abbildungen-e3-k1-s4-v3 – `Drehe das Dreieck ABC um den Punkt Z um eine Vierteldrehung gegen den Uhrzeigersinn.‖Grafik:\begin{ksys}[xmin=-#xmax=#ym …`
- B-298 (3): winkel-dreiecke-e5-k1-s4-v1, winkel-dreiecke-e5-k1-s4-v2, winkel-dreiecke-e5-k1-s4-v3 – `Zeichne das Dreieck ABC.Konstruiere zwei Winkelhalbierende und den Inkreis.Gib den Mittelpunkt I an.‖Grafik:\begin{ksys} …`
- B-299 (3): flaecheninhalt-und-volumen-im-raum-e2-k1-s6-v5, flaecheninhalt-und-volumen-im-raum-e2-k1-s6-v6, flaecheninhalt-und-volumen-im-raum-e2-k1-s6-v7 – `Der Flächeninhalt des Vierecks PQRS mit P(#|#|#),Q(#|#|#),R(#|#|#),S(#|#|#)wird mit dem Term #\cdot #+\tfrac{#}{#}\cdot …`
- B-300 (3): strahlensaetze-e2-k1-s9-v1, strahlensaetze-e2-k1-s9-v2, strahlensaetze-e2-k1-s9-v3 – `Die beiden rechtwinkligen Dreiecke sind ähnlich.Miss in beiden die Kathete a und die Hypotenuse c und berechne jeweils a …`
- B-301 (3): zuordnungen-e4-k2-s5-v1, zuordnungen-e4-k2-s5-v2, zuordnungen-e4-k2-s5-v3 – `Welcher Zuordnungstyp liegt in der Tabelle vor?Prüfe erst die Quotienten,dann die Produkte.\\kreuz{proportional}\\kreuz{ …`
- B-302 (2): orthogonalitaet-e2-k1-s3-v1, orthogonalitaet-e2-k1-s3-v2 – `Der Punkt Q liegt auf der Kante von A(#|#|#)nach D(#|#|#);außerdem sind R(#|#|#)und F(#|#|#)gegeben.Das Dreieck FQR soll …`
- B-303 (2): linearkombination-und-lineare-abhaengigkeit-e2-k1-s0-v1, linearkombination-und-lineare-abhaengigkeit-e2-k1-s0-v3 – `\vec{OX}=#\cdot\vec{OA}+#\cdot\vec{OB}.Ergeben die Koeffizienten zusammen # und liegen beide zwischen # und #?\\kreuz{Su …`
- B-304 (3): pyramide-kegel-kugel-e1-k5-s11-v1, pyramide-kegel-kugel-e1-k5-s11-v2, pyramide-kegel-kugel-e1-k5-s11-v3 – `Zeichne das Schrägbild einer quadratischen Pyramide mit Grundkante # cm und Höhe # cm(Tiefe halb so lang,schräg unter #° …`
- B-305 (3): zinsrechnung-e2-k1-s4-v1, zinsrechnung-e2-k1-s4-v2, zinsrechnung-e2-k1-s4-v3 – `Zinssatz #\%,jedes Jahr #€Einzahlung.Ergänze die zwei Felder und kontrolliere mit Jahr #.‖Grafik:\sachtabelle{lrrr}{Jahr …`
- B-306 (2): extremalprobleme-e1-k1-s1-v1, extremalprobleme-e1-k1-s1-v5 – `Der Punkt P(#|f(#))auf dem Graphen von f(x)=#-x^# ist eine Ecke eines Rechtecks;die gegenüberliegende Ecke liegt im Ursp …`
- B-307 (2): kenngroessen-von-verteilungen-e2-k7-s1-v2, kenngroessen-von-verteilungen-e2-k7-s1-v3 – `In einer Urne liegen vier Kugeln mit den Zahlen # # # und c.Zwei Kugeln werden ohne Zurücklegen gezogen;der Erwartungswe …`
- B-308 (2): lineare-funktionen-e2-k3-s0-v1, lineare-funktionen-e2-k3-s0-v3 – `Einen Schritt nach rechts–wie viel nach oben oder unten?Lies am Steigungsdreieck ab.‖Grafik:\begin{ksys}[xmin=-#xmax=#ym …`
- B-309 (2): lineare-funktionen-e2-k3-s0-v2, lineare-funktionen-e2-k3-s0-v4 – `Einen Schritt nach rechts–wie viel nach oben oder unten?Lies am Steigungsdreieck ab.‖Grafik:\begin{ksys}[xmin=-#xmax=#ym …`
- B-310 (2): extremalprobleme-e3-k1-s3-v1, extremalprobleme-e3-k1-s3-v2 – `Die Zielfunktion A(x)=-#x^#+#x^#+#x beschreibt für #<x<# den Flächeninhalt eines Dreiecks.Bestimme die Extremstelle im I …`
- B-311 (4): brueche-dezimalzahlen-e3-k1-s0-v1, brueche-dezimalzahlen-e3-k1-s0-v2, brueche-dezimalzahlen-e3-k1-s0-v3, brueche-dezimalzahlen-e3-k1-s0-v4 – `\frac{#}{#}und\frac{#}{#}–welcher Vergleichsweg ist am schnellsten?Kreuze an.\\kreuz{gleicher Nenner}\\kreuz{gleicher Zä …`
- B-312 (3): strahlensaetze-e3-k1-s8-v1, strahlensaetze-e3-k1-s8-v2, strahlensaetze-e3-k1-s8-v3 – `In einer V-Figur ist\overline{ZA}=#\text{cm},\overline{ZA'}=#\text{cm},\overline{ZB}=#\text{cm}und\overline{ZB'}=#\text{ …`
- B-313 (3): strahlensaetze-e3-k3-s1-v1, strahlensaetze-e3-k3-s1-v2, strahlensaetze-e3-k3-s1-v3 – `Zeichne eine Strecke von #\text{cm}Länge und teile sie mit einem Hilfsstrahl und Parallelen in # gleiche Teile.Wie lang …`
- B-314 (2): zinsrechnung-e1-k1-s11-v5, zinsrechnung-e1-k1-s11-v6 – `Auf ein Sparbuch werden jedes Jahr #€eingezahlt.Weise nach,dass die Bank #\%Zinsen pro Jahr zahlt.(P# # OS)‖Grafik:\sach …`
- B-315 (2): lineare-funktionen-e2-k5-s4-v2, lineare-funktionen-e2-k5-s4-v3 – `m?Lies die Steigung m der Geraden g ab.Gehe so weit nach rechts,bis du wieder auf einer Gitterlinie bist.‖Grafik:\begin{ …`
- B-316 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s6-v2, flaecheninhalt-und-volumen-im-raum-e1-k2-s6-v3 – `P(#|#|#),Q(#|#|#),R(#|#|#);für T gilt\overrightarrow{OT}=\overrightarrow{OR}-#\cdot\overrightarrow{PQ}.Bestimme T und da …`
- B-317 (3): winkel-dreiecke-e5-k1-s6-v1, winkel-dreiecke-e5-k1-s6-v2, winkel-dreiecke-e5-k1-s6-v3 – `Zeichne das Dreieck ABC und seine drei Seitenhalbierenden.Gib den Schwerpunkt S an.‖Grafik:\begin{ksys}[xmin=#xmax=#ymin …`
- B-318 (2): ableitungsregeln-e1-k2-s9-v3, ableitungsregeln-e1-k2-s9-v4 – `Gegeben ist f(x)=x^#-#x^#+#x^#.Bestimme die ersten drei Ableitungen und entscheide mit Rechnung,an welcher der Stellen x …`
- B-319 (2): schnittmengen-e3-k1-s3-v2, schnittmengen-e3-k1-s3-v3 – `Das ebene Viereck ABCD hat die Ecken A(#|#|#),B(#|#|#),C(#|#|#)und D(#|#|#).Die Ebene z=# schneidet das Viereck in einer …`
- B-320 (2): zuordnungen-e4-k2-s4-v1, zuordnungen-e4-k2-s4-v3 – `Welcher Zuordnungstyp gehört zum Graphen?\\kreuz{proportional}\\kreuz{antiproportional}\\kreuz{keins von beiden}‖Grafik: …`
- B-321 (2): kenngroessen-von-verteilungen-e4-k1-s1-v1, kenngroessen-von-verteilungen-e4-k1-s1-v2 – `Das Diagramm zeigt die Verteilung einer binomialverteilten Zufallsgröße X mit n=#;der Erwartungswert von X ist ganzzahli …`
- B-322 (4): winkel-dreiecke-e1-k1-s0-v1, winkel-dreiecke-e1-k1-s0-v2, winkel-dreiecke-e1-k1-s0-v3, winkel-dreiecke-e1-k1-s0-v4 – `Nicht ablesen:Gilt beim Messen von α am Geodreieck die kleinere oder die größere der beiden Zahlen?\\kreuz{die kleinere …`
- B-323 (3): lineare-funktionen-e2-k4-s4-v1, lineare-funktionen-e2-k4-s4-v2, lineare-funktionen-e2-k4-s4-v3 – `Mit n und Steigungsdreieck:Zeichne die Gerade zu f(x)=#x+#:Markiere n auf der y-Achse,gehe # nach rechts und m nach oben …`
- B-324 (2): trigonometrie-e4-k1-s16-v11, trigonometrie-e4-k1-s16-v12 – `Viereck ABCD mit rechtem Winkel bei A und der Diagonale BD.\angle ADB=#^\circ,\angle BDC=#^\circ,\angle ABC=#^\circ,DC=# …`
- B-325 (3): symmetrie-abbildungen-e3-k1-s3-v1, symmetrie-abbildungen-e3-k1-s3-v2, symmetrie-abbildungen-e3-k1-s3-v3 – `Drehe das Dreieck ABC um den Punkt Z um eine halbe Drehung.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\punkt{#}{#}{ …`
- B-326 (2): hypothesentests-e1-k1-s3-v2, hypothesentests-e1-k1-s3-v3 – `Getestet wird H_#\colon p\le # mit # Versuchen auf dem Signifikanzniveau #\%;X ist die Trefferzahl.Bestimme die Grenze d …`
- B-327 (2): strahlensaetze-e2-k1-s11-v2, strahlensaetze-e2-k1-s11-v3 – `Ein Quadermodell ist #\text{cm}lang,#\text{cm}breit und #\text{cm}hoch und wird mit k=# vergrößert.Wie lang ist die läng …`
- B-328 (2): trigonometrie-e3-k1-s17-v7, trigonometrie-e3-k1-s17-v8 – `Im Parallelogramm ABCD ist die Höhe h=CF\approx # cm bekannt;F liegt auf der Verlängerung von AB.Der Winkel CAB beträgt …`
- B-329 (3): zufallsgroessen-und-verteilungen-e2-k1-s0-v1, zufallsgroessen-und-verteilungen-e2-k1-s0-v2, zufallsgroessen-und-verteilungen-e2-k1-s0-v4 – `Kann das Diagramm die vollständige Verteilung einer Zufallsgröße zeigen?\kreuz{ja}\\kreuz{nein}‖Grafik:\saeulenab[ymax=# …`
- B-330 (2): kreis-e3-k1-s6-v1, kreis-e3-k1-s6-v3 – `Ein Kreisausschnitt hat den Radius r=# cm und den Mittelpunktswinkel\alpha=#^\circ.Wie groß ist der Umfang des Ausschnit …`
- B-331 (2): trigonometrie-e3-k1-s4-v2, trigonometrie-e3-k1-s4-v3 – `Rechtwinkliges Trapez:die senkrechten Seiten sind # m und # m lang und stehen # m auseinander.Wie groß ist der Winkel\al …`
- B-332 (5): konfidenzintervalle-e2-k1-s1-v1, konfidenzintervalle-e2-k1-s1-v2, konfidenzintervalle-e2-k1-s1-v3, konfidenzintervalle-e2-k1-s1-v4, konfidenzintervalle-e2-k1-s1-v5 – `In einer Stichprobe vom Umfang # gibt es # Treffer.Berechne mit der Grenzgleichung die Grenzen des Konfidenzintervalls z …`
- B-333 (4): symmetrie-abbildungen-e1-k1-s0-v1, symmetrie-abbildungen-e1-k1-s0-v2, symmetrie-abbildungen-e1-k1-s0-v3, symmetrie-abbildungen-e1-k1-s0-v4 – `Zeichne vom Ursprung aus nur den Weg zu(#|#)mit zwei Pfeilen ein:erst nach rechts,dann nach oben.Setze keinen Punkt.‖Gra …`
- B-334 (3): winkel-dreiecke-e4-k1-s10-v3, winkel-dreiecke-e4-k1-s10-v4, winkel-dreiecke-e4-k1-s10-v5 – `Konstruiere das Dreieck ABC mit c=# cm,\alpha=#^\circ und\beta=#^\circ und schreibe eine Konstruktionsbeschreibung.Miss …`
- B-335 (2): lineare-funktionen-e3-k2-s7-v1, lineare-funktionen-e3-k2-s7-v2 – `Graph und Nullstelle:Zeichne den Graphen der Funktion f mit f(x)=-#x+# und berechne die Nullstelle von f.(P# # OS)‖Grafi …`
- B-336 (2): quadratische-funktionen-e3-k1-s7-v1, quadratische-funktionen-e3-k1-s7-v3 – `f(x)=x^#-#x+#–lies den Scheitel ab,stelle die Scheitelpunktform auf und prüfe mit x=#.‖Grafik:\begin{ksys}[xmin=-#xmax=# …`
- B-337 (4): orthogonalitaet-e4-k1-s1-v1, orthogonalitaet-e4-k1-s1-v2, orthogonalitaet-e4-k1-s1-v3, orthogonalitaet-e4-k1-s1-v4 – `Gegeben sind P(#|#|#)und g\colon\vec x=(#|#|#)+\lambda\cdot(#|#|#).Bestimme den Punkt F von g,der P am nächsten liegt,un …`
- B-338 (3): zinsrechnung-e1-k1-s7-v1, zinsrechnung-e1-k1-s7-v2, zinsrechnung-e1-k1-s7-v3 – `Weise mit der Tabelle nach,dass die Bank #\%Zinsen im Jahr zahlt.‖Grafik:\sachtabelle{lrrr}{Buchung&Einzahlung&Zinsen&Gu …`
- B-339 (2): einheiten-e4-k2-s4-v1, einheiten-e4-k2-s4-v2 – `Aus einer # m langen Latte werden zwei Leisten gesägt,# und # Längeneinheiten lang;eine Längeneinheit entspricht # cm.Wi …`
- B-340 (3): symmetrie-abbildungen-e2-k3-s6-v1, symmetrie-abbildungen-e2-k3-s6-v2, symmetrie-abbildungen-e2-k3-s6-v3 – `Spiegle das Dreieck ABC an der schrägen Geraden a.‖Grafik:\begin{ksys}[xmin=#xmax=#ymin=#ymax=#]\gerade{#}{#}{a}\punkt{# …`
- B-341 (3): flaecheninhalt-durch-integration-e4-k1-s2-v1, flaecheninhalt-durch-integration-e4-k1-s2-v2, flaecheninhalt-durch-integration-e4-k1-s2-v3 – `Eine Fläche liegt über der x-Achse rechts der y-Achse:bis x=# unter der Geraden y=# danach unter der Strecke von(#|#)zum …`
- B-342 (3): zuordnungen-e4-k2-s2-v1, zuordnungen-e4-k2-s2-v2, zuordnungen-e4-k2-s2-v3 – `Ist die Zuordnung in der Tabelle antiproportional?Prüfe die Produkte x·y.\\kreuz{antiproportional}\\kreuz{nicht antiprop …`
- B-343 (3): strahlensaetze-e3-k1-s2-v1, strahlensaetze-e3-k1-s2-v2, strahlensaetze-e3-k1-s2-v3 – `In der V-Figur ist\overline{ZA}=#\text{cm},\overline{ZA'}=#\text{cm}und\overline{AB}=#\text{cm}.Berechne die Parallele\o …`
- B-344 (3): winkel-dreiecke-e1-k3-s1-v1, winkel-dreiecke-e1-k3-s1-v2, winkel-dreiecke-e1-k3-s1-v3 – `Schätze,ohne zu messen:Wie groß ist α im Vergleich zu einem rechten Winkel?\\kreuz{ein Viertel}\\kreuz{die Hälfte}\\kreu …`
- B-345 (2): kurvenuntersuchung-e3-k1-s9-v1, kurvenuntersuchung-e3-k1-s9-v2 – `Der Graph von f(x)=#x^#-x^#+#x ist punktsymmetrisch zum Ursprung.Weise nach,dass W(#|#)ein Wendepunkt ist,und gib ohne w …`
- B-346 (3): lineare-funktionen-e1-k1-s4-v1, lineare-funktionen-e1-k1-s4-v2, lineare-funktionen-e1-k1-s4-v3 – `Wertepaare und Gerade:Berechne die y-Werte zu y=\frac{#}{#}x für x=# # # und zeichne die Ursprungsgerade.‖Grafik:\begin{ …`
- B-347 (3): punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v2, punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v3 – `Dreieck OPQ mit dem Ursprung O,P(#|#|#)und Q(#|#|#).Gib einen Punkt T\ne P an,sodass das Dreieck OTQ denselben Flächenin …`
- B-348 (3): pyramide-kegel-kugel-e2-k2-s9-v1, pyramide-kegel-kugel-e2-k2-s9-v2, pyramide-kegel-kugel-e2-k2-s9-v3 – `Skizziere das Schrägbild eines Kegels mit dem Radius # cm und der Höhe # cm.Zeichne die Höhe gestrichelt ein und beschri …`
- B-349 (2): trigonometrie-e3-k1-s5-v1, trigonometrie-e3-k1-s5-v2 – `Parallelogramm ABCD:BC=# cm.F liegt auf der Verlängerung von AB über B hinaus,CF steht senkrecht darauf;der Winkel CBF b …`
- B-350 (3): winkel-dreiecke-e2-k2-s3-v1, winkel-dreiecke-e2-k2-s3-v2, winkel-dreiecke-e2-k2-s3-v3 – `An einer Geradenkreuzung ist\alpha=#^\circ;β und δ liegen neben α,γ liegt α gegenüber.Gib β,γ und δ an.‖Grafik:\geradenk …`
- B-351 (3): symmetrie-abbildungen-e2-k3-s2-v1, symmetrie-abbildungen-e2-k3-s2-v2, symmetrie-abbildungen-e2-k3-s2-v3 – `Spiegle das Dreieck ABC an der Geraden a.‖Grafik:\begin{ksys}[xmin=#xmax=#ymin=#ymax=#]\asymptote{x=#}{a}\punkt{#}{#}{A} …`
- B-352 (2): lineare-funktionen-e2-k4-s3-v1, lineare-funktionen-e2-k4-s3-v3 – `Gerade durch Punkte:Berechne zwei Punkte von f(x)=#x+# trage sie ein und zeichne die Gerade durch sie.‖Grafik:\begin{ksy …`
- B-353 (2): orthogonalitaet-e2-k1-s6-v2, orthogonalitaet-e2-k1-s6-v3 – `Gegeben sind A(#|#|#),B(#|#|#)und C(#|#|#).Der Punkt T liegt auf der Strecke AC so,dass das Dreieck ABT bei B rechtwinkl …`
- B-354 (5): symmetrie-abbildungen-e2-k3-s1-v1, symmetrie-abbildungen-e2-k3-s1-v2, symmetrie-abbildungen-e2-k3-s1-v3, symmetrie-abbildungen-e2-k3-s1-v4, symmetrie-abbildungen-e2-k3-s1-v5 – `Spiegle den Punkt P an der Geraden a.Zähle die Kästchen bis zur Achse.‖Grafik:\begin{ksys}[xmin=#xmax=#ymin=#ymax=#]\asy …`
- B-355 (3): symmetrie-abbildungen-e2-k3-s3-v1, symmetrie-abbildungen-e2-k3-s3-v2, symmetrie-abbildungen-e2-k3-s3-v3 – `Spiegle das Dreieck ABC an der Geraden a.‖Grafik:\begin{ksys}[xmin=#xmax=#ymin=-#ymax=#]\gerade{#}{#}{a}\punkt{#}{#}{A}\ …`
- B-356 (2): kreis-e3-k1-s4-v1, kreis-e3-k1-s4-v3 – `Ein Kreisausschnitt hat den Radius r=# cm und den Mittelpunktswinkel\alpha=#^\circ.Wie lang ist sein Bogen b?Rechne mit …`
- B-357 (2): kreis-e3-k1-s5-v1, kreis-e3-k1-s5-v3 – `Ein Kreisausschnitt hat den Radius r=# cm und den Mittelpunktswinkel\alpha=#^\circ.Wie groß ist seine Fläche?Rechne mit …`
- B-358 (2): normalverteilung-und-sigma-regeln-e1-k1-s2-v1, normalverteilung-und-sigma-regeln-e1-k1-s2-v2 – `Die Abbildung zeigt die Dichte einer normalverteilten Zufallsgröße X mit dem Erwartungswert #.Wie groß ist P(X=#)?(Abitu …`
- B-359 (2): quadratische-gleichungen-e3-k5-s3-v1, quadratische-gleichungen-e3-k5-s3-v3 – `Die Parabel y=x^#-#x+# ist gezeichnet.Lösungen von x^#-#x+#=# am Graphen?‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=# …`
- B-360 (2): trigonometrie-e4-k1-s16-v1, trigonometrie-e4-k1-s16-v2 – `Eine Seilbahn führt von A über die Stütze B nach C.AB=# m,der Winkel bei A ist #^\circ,der Winkel ABC ist #^\circ.Berech …`
- B-361 (5): zuordnungen-e4-k2-s1-v1, zuordnungen-e4-k2-s1-v2, zuordnungen-e4-k2-s1-v3, zuordnungen-e4-k2-s1-v4, zuordnungen-e4-k2-s1-v5 – `Ist die Zuordnung in der Tabelle proportional?Prüfe die Quotienten y:x.\\kreuz{proportional}\\kreuz{nicht proportional}‖ …`
- B-362 (3): lineare-funktionen-e2-k4-s8-v3, lineare-funktionen-e2-k4-s8-v4, lineare-funktionen-e2-k4-s8-v8 – `Graph zeichnen:Zeichne den Graphen der Funktion f mit f(x)=#x-# in das Koordinatensystem.(P# # OS)‖Grafik:\begin{ksys}[x …`
- B-363 (3): symmetrie-abbildungen-e3-k1-s6-v1, symmetrie-abbildungen-e3-k1-s6-v2, symmetrie-abbildungen-e3-k1-s6-v3 – `Spiegle das Dreieck ABC am Zentrum Z.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\punkt{#}{#}{A}\punkt{#}{#}{B}\punk …`
- B-364 (2): spiegelung-e2-k1-s4-v1, spiegelung-e2-k1-s4-v2 – `Zwei Flächen eines Körpers liegen symmetrisch zu einer Ebene H;W(#|#|#)ist das Spiegelbild von C(#|#|#),U(#|#|#)liegt au …`
- B-365 (2): lineare-funktionen-e1-k1-s5-v1, lineare-funktionen-e1-k1-s5-v2 – `Wertepaare und Gerade:Berechne die y-Werte zu y=-#x für x=# # # und zeichne die Ursprungsgerade.‖Grafik:\begin{ksys}[xmi …`
- B-366 (2): lineare-funktionen-e4-k2-s1-v1, lineare-funktionen-e4-k2-s1-v3 – `Gerade durch zwei Punkte:Trage A(-#|-#)und B(#|#)ein und zeichne die Gerade durch beide Punkte.‖Grafik:\begin{ksys}[xmin …`
- B-367 (2): lineare-gleichungssysteme-e3-k1-s9-v1, lineare-gleichungssysteme-e3-k1-s9-v2 – `I:#x+#y=# II:#x-#y=-#–Lösung?Löse mit dem Additionsverfahren,mache die Probe in beiden Gleichungen und begründe,warum da …`
- B-368 (3): lineare-funktionen-e1-k1-s2-v1, lineare-funktionen-e1-k1-s2-v2, lineare-funktionen-e1-k1-s2-v3 – `y-Wert bei x=#?Lies am Graphen von y=#x ab und prüfe mit der Rechnung.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#abl …`
- B-369 (3): rekonstruktion-von-funktionsgleichungen-e3-k1-s1-v1, rekonstruktion-von-funktionsgleichungen-e3-k1-s1-v2, rekonstruktion-von-funktionsgleichungen-e3-k1-s1-v3 – `Der Graph von f mit f(x)=a\cdot\mathrm{sin}(b\cdot x)und a,b># hat die direkt aufeinanderfolgenden Extrempunkte E_#(#|#) …`
- B-370 (2): ebenen-e1-k1-s5-v2, ebenen-e1-k1-s5-v3 – `Beschreiben E_#\colon\vec x=(#|#|#)+r\cdot(#|#|#)+s\cdot(#|#|#)und E_#\colon\vec x=(#|#|#)+r\cdot(#|#|#)+s\cdot(#|#|#),r …`
- B-371 (2): trigonometrische-funktionen-e3-k1-s6-v1, trigonometrische-funktionen-e3-k1-s6-v3 – `Lies die Periode ab und berechne b in y=sin(b·x).‖Grafik:\begin{ksys}[xmin=#xmax=#ymin=-#ymax=#xstep=#ystep=#ablesen]\fu …`
- B-372 (5): strahlensaetze-e3-k1-s1-v1, strahlensaetze-e3-k1-s1-v2, strahlensaetze-e3-k1-s1-v3, strahlensaetze-e3-k1-s1-v4, strahlensaetze-e3-k1-s1-v5 – `In der V-Figur ist\overline{ZA}=#\text{cm},\overline{ZA'}=#\text{cm}und\overline{ZB}=#\text{cm}.Berechne\overline{ZB'}.‖ …`
- B-373 (2): symmetrie-abbildungen-e2-k3-s0-v1, symmetrie-abbildungen-e2-k3-s0-v2 – `Punkt P liegt # Kästchen links von der Achse,sein Bildpunkt # Kästchen rechts,beide auf gleicher Höhe.Ist richtig gespie …`
- B-374 (2): brueche-dezimalzahlen-e1-k1-s4-v1, brueche-dezimalzahlen-e1-k1-s4-v3 – `Bei welcher Figur ist\frac{#}{#}gefärbt?Kreuze an.\\kreuz{P}\\kreuz{Q}\\kreuz{R}‖Grafik:P\bruchrechteck{#}{#}Q\bruchkrei …`
- B-375 (2): lineare-funktionen-e2-k5-s3-v1, lineare-funktionen-e2-k5-s3-v2 – `m?Lies die Steigung m der Geraden g mit einem Steigungsdreieck ab.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#ablesen …`
- B-376 (2): punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v3, punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v4 – `A(#|#|#)und M(#|#|#).Gib zwei Punkte B und C an,sodass A,B und C denselben Abstand zu M haben und ein gleichschenkliges …`
- B-377 (2): trigonometrie-e4-k1-s16-v7, trigonometrie-e4-k1-s16-v8 – `Ein Grundstück ABCD hat bei B einen rechten Winkel.AC=# m,\angle BAC=#^\circ,\angle BCD=#^\circ,\angle ADC=#^\circ.Berec …`
- B-378 (3): koerper-e3-k1-s7-v1, koerper-e3-k1-s7-v2, koerper-e3-k1-s7-v3 – `Dreiecksprisma:Das Dreieck hat einen rechten Winkel zwischen den Seiten # cm und # cm,die lange Seite ist # cm;das Prism …`
- B-379 (3): quadratische-gleichungen-e1-k3-s3-v1, quadratische-gleichungen-e1-k3-s3-v2, quadratische-gleichungen-e1-k3-s3-v3 – `Zeichne die Gerade y=# zur Normalparabel y=x^# ein.Lösungen von x^#=#?‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\p …`
- B-380 (2): lineare-funktionen-e2-k5-s2-v2, lineare-funktionen-e2-k5-s2-v3 – `m?Lies die Steigung m der Geraden g mit einem Steigungsdreieck ab.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#ablesen …`
- B-381 (3): trigonometrie-e3-k1-s6-v1, trigonometrie-e3-k1-s6-v2, trigonometrie-e3-k1-s6-v3 – `Parallelogramm ABCD mit der Höhe h=# cm von C auf die Verlängerung von AB.Die Diagonale AC bildet mit AB einen Winkel vo …`
- B-382 (2): pythagoras-e2-k3-s1-v1, pythagoras-e2-k3-s1-v3 – `Pythagoreisches Tripel:drei ganze Zahlen,bei denen die Quadrate der zwei kleineren zusammen das Quadrat der größten erge …`
- B-383 (4): winkel-dreiecke-e1-k2-s0-v1, winkel-dreiecke-e1-k2-s0-v2, winkel-dreiecke-e1-k2-s0-v3, winkel-dreiecke-e1-k2-s0-v4 – `Welche Winkelart hat α?Nicht messen.\\kreuz{spitz}\\kreuz{recht}\\kreuz{stumpf}\\kreuz{gestreckt}\\kreuz{überstumpf}‖Gra …`
- B-384 (2): kurvenuntersuchung-e4-k3-s1-v1, kurvenuntersuchung-e4-k3-s1-v3 – `Gegeben ist f(x)=#\cdot\mathrm{e}^{#x}.Weise nach,dass g(x)=\mathrm{ln}(f(x))eine lineare Funktion ist,und gib Steigung …`
- B-385 (2): lineare-funktionen-e4-k1-s1-v1, lineare-funktionen-e4-k1-s1-v5 – `Gleichung?Bestimme die Gleichung der Geraden g aus dem Graphen.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#ablesen]\g …`
- B-386 (2): symmetrie-abbildungen-e1-k2-s6-v1, symmetrie-abbildungen-e1-k2-s6-v2 – `Trage A(#|#),B(#|#),C(#|#),D(#|#)ein und verbinde sie der Reihe nach.Wie heißt die Figur?‖Grafik:\begin{ksys}[xmin=#xmax …`
- B-387 (3): koerper-e4-k2-s7-v1, koerper-e4-k2-s7-v2, koerper-e4-k2-s7-v3 – `Ein Zylinder hat den Radius # cm und die Höhe # cm.Welches Rechteck gehört zu seinem Netz?\\kreuz{# cm×# cm}\\kreuz{# cm …`
- B-388 (2): flaechen-e3-k1-s3-v1, flaechen-e3-k1-s3-v3 – `Stumpfwinkliges Dreieck,Grundseite # cm;die Höhe dazu liegt außerhalb und ist # cm lang–Fläche?‖Grafik:\dreieck{(#)}{(#) …`
- B-389 (2): lineare-gleichungssysteme-e1-k1-s8-v1, lineare-gleichungssysteme-e1-k1-s8-v3 – `Lösung durch Probieren?I:x+y=# II:#x+y=#.Setze in I nacheinander x=# # #\ldots ein,trage y ein und prüfe II.‖Grafik:\wer …`
- B-390 (5): reelle-zahlen-e1-k1-s1-v1, reelle-zahlen-e1-k1-s1-v2, reelle-zahlen-e1-k1-s1-v3, reelle-zahlen-e1-k1-s1-v4, reelle-zahlen-e1-k1-s1-v5 – `\frac{#}{#}–als Dezimalzahl,abbrechend oder periodisch?Schreibe periodische Zahlen mit Periodenstrich.\\kreuz{abbrechend …`
- B-391 (2): konfidenzintervalle-e2-k1-s2-v1, konfidenzintervalle-e2-k1-s2-v3 – `Die untere Grenze eines Konfidenzintervalls zur Sicherheitswahrscheinlichkeit #\%ist # der Umfang #.Bestimme die Treffer …`
- B-392 (2): binomialverteilung-e5-k1-s7-v1, binomialverteilung-e5-k1-s7-v2 – `X ist binomialverteilt mit # Versuchen und der Trefferwahrscheinlichkeit #;es gilt P(X\le #)\approx #.Bestimme ohne Rech …`
- B-393 (2): binomialverteilung-e5-k1-s8-v3, binomialverteilung-e5-k1-s8-v4 – `Y hat die Werte # bis # und eine symmetrische Verteilung.Es gilt P(Y\le #)\approx # und P(Y=#)\approx #.Bestimme damit P …`
- B-394 (3): winkel-dreiecke-e4-k1-s3-v1, winkel-dreiecke-e4-k1-s3-v2, winkel-dreiecke-e4-k1-s3-v3 – `Konstruiere das Dreieck ABC mit c=# cm,\alpha=#^\circ und\beta=#^\circ.Beginne mit der Seite c auf dem Strahl.‖Grafik:\w …`
- B-395 (3): trigonometrie-e4-k1-s9-v1, trigonometrie-e4-k1-s9-v2, trigonometrie-e4-k1-s9-v3 – `Viereck ABCD mit rechtem Winkel bei B und der Diagonale AC=# m.\angle BAC=#^\circ,\angle BCD=#^\circ,\angle ADC=#^\circ. …`
- B-396 (2): kurvenuntersuchung-e1-k1-s7-v5, kurvenuntersuchung-e1-k1-s7-v6 – `Bestimme Koordinaten und Art aller Extrempunkte des Graphen von f(x)=\frac{#}{#}x^#-#x+# und gib das Monotonieverhalten …`
- B-397 (3): strahlensaetze-e2-k1-s6-v1, strahlensaetze-e2-k1-s6-v2, strahlensaetze-e2-k1-s6-v3 – `Dreieck # hat die Winkel #^\circ und #^\circ,Dreieck # die Winkel #^\circ und #^\circ.Sind die Dreiecke ähnlich?\kreuz{j …`
- B-398 (3): reelle-zahlen-e1-k1-s5-v1, reelle-zahlen-e1-k1-s5-v2, reelle-zahlen-e1-k1-s5-v3 – `\sqrt{#}–markiere die Zahl auf dem Zahlenstrahl.Zwischen welchen Zehnteln liegt sie?‖Grafik:\zahlenstrahl[xmin=#xmax=#xs …`
- B-399 (3): winkel-dreiecke-e4-k1-s6-v1, winkel-dreiecke-e4-k1-s6-v2, winkel-dreiecke-e4-k1-s6-v3 – `Konstruiere ein rechtwinkliges Dreieck ABC mit dem rechten Winkel bei C und den Katheten a=# cm und b=# cm.‖Grafik:\wink …`
- B-400 (2): grenzwerte-und-verhalten-im-unendlichen-e3-k1-s2-v1, grenzwerte-und-verhalten-im-unendlichen-e3-k1-s2-v3 – `f(x)=#e^{-#x}-#.Begründe,dass f streng monoton fällt und der Graph durch den Ursprung verläuft.Grenzwert für x\to+\infty …`
- B-401 (2): uneigentliche-integrale-e1-k1-s3-v1, uneigentliche-integrale-e1-k1-s3-v2 – `Vergleiche∫_#^w\frac{#}{x^#}dx und∫_#^w\frac{#}{x}dx für w\to\infty:Welche der beiden unbegrenzten Flächen hat einen end …`
- B-402 (2): koerper-e4-k2-s11-v1, koerper-e4-k2-s11-v2 – `Zylinder A:Radius # cm,Höhe # cm.Zylinder B:Radius # cm,Höhe # cm.Wievielmal so groß ist das Volumen von B?Begründe mit …`
- B-403 (2): potenzen-wurzeln-e3-k2-s13-v1, potenzen-wurzeln-e3-k2-s13-v2 – `Welche Aussage ist wahr?Kreuze an.(P# # OS)\\kreuz{\sqrt{(-#)^#}=-#}\\kreuz{\sqrt{(-#)^#}=#}\\kreuz{\sqrt{(-#)^#}ist nic …`
- B-404 (2): spiegelung-e2-k1-s3-v1, spiegelung-e2-k1-s3-v2 – `g und h schneiden sich in S(#|#|#)und haben die Richtungsvektoren(#|#|#)und(#|#|#).Gib eine Ebene an,an der g auf h gesp …`
- B-405 (3): pyramide-kegel-kugel-e3-k1-s6-v1, pyramide-kegel-kugel-e3-k1-s6-v2, pyramide-kegel-kugel-e3-k1-s6-v3 – `Skizziere eine Kugel mit dem Radius # cm:Kreis,Äquator als Ellipse,Radius gestrichelt und beschriftet.‖Grafik:\rechenpla …`
- B-406 (2): skalarprodukt-und-winkel-e4-k1-s1-v1, skalarprodukt-und-winkel-e4-k1-s1-v2 – `Berechne den Winkel,unter dem die Gerade g\colon\vec x=(#\mid #\mid #)+t\cdot(#\mid #\mid #),t\in\mathbb{R},die xy-Ebene …`
- B-407 (3): winkel-dreiecke-e4-k1-s2-v1, winkel-dreiecke-e4-k1-s2-v2, winkel-dreiecke-e4-k1-s2-v3 – `Konstruiere das Dreieck ABC mit b=# cm,c=# cm und\alpha=#^\circ.Beginne mit der Seite c auf dem Strahl.‖Grafik:\winkelst …`
- B-408 (2): ebenen-e1-k1-s3-v1, ebenen-e1-k1-s3-v2 – `Die Ebene E enthält die Gerade g\colon\vec x=(#|#|#)+t\cdot(#|#|#),t\in\mathbb{R},und den Punkt P(#|#|#).Parametergleich …`
- B-409 (2): hypothesentests-e3-k1-s0-v1, hypothesentests-e3-k1-s0-v3 – `Getestet wird H_#\colon p\le #.Für welchen wahren Anteil p ist ein Fehler zweiter Art möglich?\\kreuz{p=#}\\kreuz{p=#}\\ …`
- B-410 (2): hypothesentests-e3-k1-s0-v2, hypothesentests-e3-k1-s0-v4 – `Getestet wird H_#\colon p\ge #.Für welchen wahren Anteil p ist ein Fehler zweiter Art möglich?\\kreuz{p=#}\\kreuz{p=#}\\ …`
- B-411 (2): lineare-funktionen-e2-k5-s1-v3, lineare-funktionen-e2-k5-s1-v4 – `n?Lies den y-Achsenabschnitt n der Geraden g ab.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#ablesen]\gerade{#}{-#}{g} …`
- B-412 (2): umkehrfunktion-e2-k1-s4-v1, umkehrfunktion-e2-k1-s4-v2 – `Die Punkte A(#|#)und B(#|#)werden an y=x gespiegelt.Begründe,dass A,B,B'und A'ein Trapez bilden,und berechne seinen Fläc …`
- B-413 (4): kreis-e3-k1-s0-v1, kreis-e3-k1-s0-v2, kreis-e3-k1-s0-v3, kreis-e3-k1-s0-v4 – `Welcher Teil des Kreises ist grau?Kreuze an.\\kreuz{\frac{#}{#}}\\kreuz{\frac{#}{#}}\\kreuz{\frac{#}{#}}‖Grafik:\kreisse …`
- B-414 (3): winkel-dreiecke-e4-k1-s4-v1, winkel-dreiecke-e4-k1-s4-v2, winkel-dreiecke-e4-k1-s4-v3 – `Konstruiere das Dreieck ABC mit b=# cm,c=# cm und\beta=#^\circ.Beginne mit der Seite c auf dem Strahl.‖Grafik:\winkelstr …`
- B-415 (2): normalverteilung-und-sigma-regeln-e3-k1-s1-v1, normalverteilung-und-sigma-regeln-e3-k1-s1-v2 – `Die Dichte von X ist f(x)=\frac{#}{#\sqrt{#\pi}}\mathrm{e}^{-\frac{#}{#}\left(\frac{x-#}{#}\right)^#}.\mu und\sigma?(Abi …`
- B-416 (2): punkte-und-strecken-im-koordinatensystem-e2-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e2-k1-s7-v3 – `A(#|#|#)und B(#|#|#)liegen auf einer Geraden g.Gib einen Punkt D\ne B auf g an,der von A so weit entfernt ist wie B.(Abi …`
- B-417 (2): ebenen-e2-k2-s3-v2, ebenen-e2-k2-s3-v3 – `Bestimme rechnerisch einen Normalenvektor der Ebene durch A(#|#|#),B(#|#|#)und C(#|#|#)und prüfe ihn mit beiden Skalarpr …`
- B-418 (3): extremalprobleme-e3-k1-s1-v3, extremalprobleme-e3-k1-s1-v4, extremalprobleme-e3-k1-s1-v5 – `Die Zielfunktion A(x)=#x-x^# #<x<\sqrt{#},beschreibt einen Flächeninhalt.Bestimme die Stelle mit A'(x)=# im Definitionsb …`
- B-419 (3): lineare-funktionen-e2-k4-s6-v1, lineare-funktionen-e2-k4-s6-v2, lineare-funktionen-e2-k4-s6-v3 – `Mit n und Steigungsdreieck:Zeichne die Gerade zu f(x)=\frac{#}{#}x+#.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\en …`
- B-420 (2): pythagoras-e3-k2-s5-v1, pythagoras-e3-k2-s5-v3 – `Dreieck ABC mit stumpfem Winkel bei B.Die Höhe von C trifft die Verlängerung von AB im Punkt D.CD=# cm,BC=# cm–wie lang …`
- B-421 (3): winkel-dreiecke-e5-k1-s3-v1, winkel-dreiecke-e5-k1-s3-v2, winkel-dreiecke-e5-k1-s3-v3 – `Konstruiere mit dem Zirkel die Winkelhalbierende von α.Wie groß ist jeder der beiden Teilwinkel?‖Grafik:\winkel[#]{#}{\a …`
- B-422 (2): pythagoras-e3-k2-s4-v2, pythagoras-e3-k2-s4-v3 – `Parallelogramm:schräge Seite # cm.Der Fußpunkt der Höhe liegt auf der Verlängerung der Grundseite,# cm hinter der Ecke–H …`
- B-423 (2): trigonometrie-e3-k1-s17-v9, trigonometrie-e3-k1-s17-v10 – `Im Dreieck ABC ist AD die Höhe auf BC(D zwischen B und C),AD=# m.\angle ACD=#^\circ,\angle CAB=#^\circ.Berechne BD.(P# # …`
- B-424 (5): winkel-dreiecke-e4-k1-s1-v1, winkel-dreiecke-e4-k1-s1-v2, winkel-dreiecke-e4-k1-s1-v3, winkel-dreiecke-e4-k1-s1-v4, winkel-dreiecke-e4-k1-s1-v5 – `Konstruiere das Dreieck ABC mit a=# cm,b=# cm und c=# cm.Beginne mit der Seite c auf dem Strahl.‖Grafik:\winkelstrahl[#] …`
- B-425 (5): winkel-dreiecke-e2-k2-s1-v1, winkel-dreiecke-e2-k2-s1-v2, winkel-dreiecke-e2-k2-s1-v3, winkel-dreiecke-e2-k2-s1-v4, winkel-dreiecke-e2-k2-s1-v5 – `An einer Geradenkreuzung ist\alpha=#^\circ.Wie groß ist der Scheitelwinkel von α?‖Grafik:\geradenkreuzung{#}{\alpha}{}{} …`
- B-426 (3): kreis-e3-k1-s1-v1, kreis-e3-k1-s1-v2, kreis-e3-k1-s1-v3 – `Ein Kreisausschnitt hat den Mittelpunktswinkel\alpha=#^\circ.Welcher Teil des Kreises ist das?Gib den Anteil als Bruch a …`
- B-427 (3): trigonometrie-e4-k1-s11-v1, trigonometrie-e4-k1-s11-v2, trigonometrie-e4-k1-s11-v3 – `Dreieck ABC:a=# cm,\alpha=#^\circ,\beta=#^\circ.Berechne b mit dem Sinussatz und noch einmal über die Höhe h von C auf A …`
- B-428 (3): kreis-e3-k1-s2-v1, kreis-e3-k1-s2-v2, kreis-e3-k1-s2-v3 – `Ein Kreisausschnitt hat den Mittelpunktswinkel\alpha=#^\circ.Wie viel Prozent des Kreises sind das?Runde auf eine Stelle …`
- B-429 (3): winkel-dreiecke-e1-k2-s6-v1, winkel-dreiecke-e1-k2-s6-v2, winkel-dreiecke-e1-k2-s6-v3 – `Die Winkel #^\circ und #^\circ liegen am selben Scheitel nebeneinander.Wie groß ist der Winkel,den beide zusammen bilden …`
- B-430 (3): winkel-dreiecke-e4-k1-s5-v1, winkel-dreiecke-e4-k1-s5-v2, winkel-dreiecke-e4-k1-s5-v3 – `Konstruiere ein gleichschenkliges Dreieck ABC mit der Basis c=# cm und den Schenkeln a=b=# cm.‖Grafik:\winkelstrahl[#][A …`
- B-431 (2): symmetrie-abbildungen-e3-k1-s5-v1, symmetrie-abbildungen-e3-k1-s5-v2 – `Spiegle den Punkt P am Zentrum Z.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\punkt{#}{#}{P}\punkt{#}{#}{Z}\end{ksys …`
- B-432 (3): winkel-dreiecke-e1-k2-s7-v1, winkel-dreiecke-e1-k2-s7-v2, winkel-dreiecke-e1-k2-s7-v3 – `Ein Winkel von #^\circ ist durch einen Strahl in zwei Teilwinkel geteilt.Der eine misst #^\circ.Wie groß ist der andere?`
- B-433 (2): flaecheninhalt-und-volumen-im-raum-e2-k1-s1-v1, flaecheninhalt-und-volumen-im-raum-e2-k1-s1-v2 – `P(#|#|#),Q(#|#|#),R(#|#|-#).Zeige,dass bei Q ein rechter Winkel liegt,und berechne den Flächeninhalt des Rechtecks PQRS.`
- B-434 (3): winkel-dreiecke-e2-k2-s2-v1, winkel-dreiecke-e2-k2-s2-v2, winkel-dreiecke-e2-k2-s2-v3 – `An einer Geradenkreuzung ist\alpha=#^\circ.Wie groß ist ein Nebenwinkel von α?‖Grafik:\geradenkreuzung{#}{\alpha}{}{}{}`
- B-435 (2): binomialverteilung-e4-k1-s9-v7, binomialverteilung-e4-k1-s9-v9 – `X ist binomialverteilt mit # Versuchen,und es gilt P(X=#)=P(X=#).Bestimme die Trefferwahrscheinlichkeit p ohne Rechner.`
- B-436 (2): strahlensaetze-e2-k1-s8-v2, strahlensaetze-e2-k1-s8-v3 – `Die Dreiecke ABC und DEF sind ähnlich,AB entspricht DE.Es ist AB=#\text{cm},DE=#\text{cm}und AC=#\text{cm}.Berechne DF.`
- B-437 (2): flaechen-e3-k2-s1-v1, flaechen-e3-k2-s1-v3 – `Dreieck ABC:AB=# cm,BC=# cm.Die Höhe auf AB ist # cm,die Höhe auf BC # cm.Fläche–rechne mit BC und der passenden Höhe.`
- B-438 (2): lineare-funktionen-e2-k4-s5-v1, lineare-funktionen-e2-k4-s5-v3 – `Mit n und Steigungsdreieck:Zeichne die Gerade zu f(x)=-#x+#.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\end{ksys}`
- B-439 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v3, punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v4 – `Quader ABCDEFGH(Boden ABCD,E über A,F über B,G über C,H über D)mit A(#|#|#),B(#|#|#),E(#|#|#),H(#|#|#):G?(Abitur # GK)`
- B-440 (3): flaechen-e2-k1-s0-v1, flaechen-e2-k1-s0-v2, flaechen-e2-k1-s0-v4 – `Zeichne die Höhe zur Grundseite g ein und markiere den rechten Winkel.‖Grafik:\parallelogramm[seiten={g,,,}]{#}{#}{#}`
- B-441 (3): rationale-zahlen-e1-k1-s0-v1, rationale-zahlen-e1-k1-s0-v2, rationale-zahlen-e1-k1-s0-v3 – `Schreibe an jeden Strich seine Zahl.Abstand zwischen zwei Strichen:#.‖Grafik:\zahlenstrahl[xmin=-#xmax=#xstep=#]{#/#}`
- B-442 (3): trigonometrie-e2-k1-s5-v1, trigonometrie-e2-k1-s5-v2, trigonometrie-e2-k1-s5-v3 – `Gegenkathete von\alpha:# cm,Hypotenuse # cm.Berechne\alpha,dann\beta als Ergänzung;kontrolliere\beta mit dem Kosinus.`
- B-443 (3): trigonometrie-e3-k1-s11-v1, trigonometrie-e3-k1-s11-v2, trigonometrie-e3-k1-s11-v3 – `Rechter Winkel bei D;B liegt zwischen D und C.Von A aus:\angle DAC=#^\circ,\angle BAC=#^\circ,AD=# m.Wie lang ist BD?`
- B-444 (2): lineare-funktionen-e2-k4-s7-v1, lineare-funktionen-e2-k4-s7-v2 – `Mit n und Steigungsdreieck:Zeichne die Gerade zu f(x)=#x-#.‖Grafik:\begin{ksys}[xmin=-#xmax=#ymin=-#ymax=#]\end{ksys}`
- B-445 (3): punkte-und-strecken-im-koordinatensystem-e5-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e5-k1-s7-v2, punkte-und-strecken-im-koordinatensystem-e5-k1-s7-v3 – `Der Punkt B(#|#|#)wird um die x_#-Achse gedreht.Gib drei Bildpunkte an,bei denen eine Koordinate # ist.(Abitur # LK)`
- B-446 (3): pythagoras-e3-k2-s1-v1, pythagoras-e3-k2-s1-v3, pythagoras-e3-k2-s1-v5 – `Gleichschenkliges Dreieck:Grundseite # cm,Schenkel # cm–Höhe h?‖Grafik:\dreieck{(#)}{(#)}{(#,#)}{# cm}{}{# cm}{}{}{}`
- B-447 (2): trigonometrie-e1-k5-s1-v1, trigonometrie-e1-k5-s1-v3 – `Gemessen:Gegenkathete # cm,Hypotenuse # cm,Winkel #^\circ.Verhältnis als Dezimalzahl–passt es zu\mathrm{sin}#^\circ?`
- B-448 (2): trigonometrische-funktionen-e1-k1-s11-v1, trigonometrische-funktionen-e1-k1-s11-v2 – `Welches Bogenmaß gehört zu #°?\\kreuz{\frac{\pi}{#}}\kreuz{\frac{\pi}{#}}\kreuz{\frac{\pi}{#}}\kreuz{\frac{#\pi}{#}}`
- B-449 (2): potenzen-wurzeln-e3-k2-s0-v3, potenzen-wurzeln-e3-k2-s0-v4 – `\sqrt{#}–zwischen welchen ganzen Zahlen?\\kreuz{zwischen # und #}\\kreuz{zwischen # und #}\\kreuz{zwischen # und #}`
- B-450 (2): flaechen-e3-k1-s0-v1, flaechen-e3-k1-s0-v4 – `Zeichne die Höhe zur Grundseite g ein und markiere den rechten Winkel.‖Grafik:\dreieck{(#)}{(#)}{(#)}{}{}{g}{}{}{}`
- B-451 (2): lineare-funktionen-e1-k1-s6-v1, lineare-funktionen-e1-k1-s6-v2 – `Proportional?Entscheide mit den Quotienten y:x.Wenn ja:Gib die Gleichung an.‖Grafik:\wertetabelle[#,#]{x}{y}{#,#}`
- B-452 (2): punkte-und-strecken-im-koordinatensystem-e3-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s7-v3 – `In der x_#x_#-Ebene liegen A(#|#),B(#|#)und C(#|#)auf einem Kreis.Koordinaten seines Mittelpunkts M?(Abitur # GK)`
- B-453 (2): kreis-e1-k2-s4-v1, kreis-e1-k2-s4-v2 – `Ein Kreis hat den Umfang u=# cm.Wie groß ist sein Durchmesser?Rechne mit der\pi-Taste und runde auf eine Stelle.`
- B-454 (2): trigonometrie-e4-k1-s16-v9, trigonometrie-e4-k1-s16-v10 – `Dreieck DEF:FE=# m,Winkel bei F #^\circ,Winkel bei E #^\circ.P liegt auf DE mit PE=# m.Wie lang ist DP?(P# # OS)`
- B-455 (3): koerper-e1-k1-s6-v1, koerper-e1-k1-s6-v2, koerper-e1-k1-s6-v3 – `Zeichne auf Kästchenpapier das Schrägbild eines Quaders:Länge # cm,Tiefe # cm,Höhe # cm.‖Grafik:\rechenplatz{#}`
- B-456 (2): bruchrechnung-e1-k5-s4-v2, bruchrechnung-e1-k5-s4-v3 – `Zeige\frac{#}{#}+\frac{#}{#}an einem Streifen mit # Teilen und gib das Ergebnis an.‖Grafik:\bruchrechteck{#}{#}`
- B-457 (4): prozentrechnung-e4-k2-s0-v1, prozentrechnung-e4-k2-s0-v2, prozentrechnung-e4-k2-s0-v3, prozentrechnung-e4-k2-s0-v4 – `Grau sind #\%,das sind # Kästchen–wie viele Kästchen hat der ganze Streifen?‖Grafik:\streifen[#]{#}{#\%}{#\%}`
- B-458 (3): koerper-e3-k1-s4-v1, koerper-e3-k1-s4-v2, koerper-e3-k1-s4-v3 – `Prisma mit Trapez als Grundfläche:parallele Seiten # cm und # cm,Abstand # cm;Höhe des Prismas # cm–Volumen?`
- B-459 (2): kreis-e2-k1-s6-v1, kreis-e2-k1-s6-v3 – `Ein Kreis hat die Fläche A=# cm².Wie groß ist sein Radius?Rechne mit der\pi-Taste und runde auf eine Stelle.`
- B-460 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s2-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s2-v3 – `Sind\vec{u}=(#|-#|#)und\vec{v}=(-#|#|-#)kollinear?Zeigen sie in dieselbe Richtung oder in die Gegenrichtung?`
- B-461 (2): brueche-dezimalzahlen-e3-k1-s5-v1, brueche-dezimalzahlen-e3-k1-s5-v2 – `Trage\frac{#}{#}und\frac{#}{#}am Zahlenstrahl ein.‖Grafik:\zahlenstrahl[xmin=#xmax=#xstep=#karo=#]{#/# #/#}`
- B-462 (2): funktionsklassen-und-eigenschaften-e2-k1-s9-v1, funktionsklassen-und-eigenschaften-e2-k1-s9-v2 – `f(x)=#x^#-#x^#+#–berechne die Koordinaten aller Schnittpunkte des Graphen mit den Koordinatenachsen(FHR #).`
- B-463 (2): kreis-e1-k4-s1-v1, kreis-e1-k4-s1-v3 – `Zeichne einen Kreis mit dem Radius # cm und markiere seinen Mittelpunkt mit M.‖Grafik:\rechenplatz[halb]{#}`
- B-464 (2): reelle-zahlen-e2-k1-s0-v1, reelle-zahlen-e2-k1-s0-v3 – `#^#\cdot #^#–welches Gesetz passt?\\kreuz{gleiche Basis}\\kreuz{gleicher Exponent}\\kreuz{keins:ausrechnen}`
- B-465 (3): koerper-e2-k5-s1-v1, koerper-e2-k5-s1-v2, koerper-e2-k5-s1-v3 – `Ein Aquarium ist innen # cm lang und # cm breit.Es werden # l Wasser eingefüllt.Wie hoch steht das Wasser?`
- B-466 (2): symmetrie-abbildungen-e2-k2-s1-v2, symmetrie-abbildungen-e2-k2-s1-v5 – `Zeichne die Symmetrieachse der Figur ein.‖Grafik:\dreieck{(#)}{(#)}{(#,#)}{a}{b}{c}{\alpha}{\beta}{\gamma}`
- B-467 (2): trigonometrie-e3-k1-s14-v1, trigonometrie-e3-k1-s14-v2 – `Hypotenuse # cm,\alpha=#^\circ.Berechne Gegenkathete und Ankathete und prüfe mit dem Satz des Pythagoras.`
- B-468 (2): uneigentliche-integrale-e1-k1-s1-v4, uneigentliche-integrale-e1-k1-s1-v5 – `f(x)=#e^{-#x}–Inhalt A(w)der Fläche zwischen dem Graphen von f und der x-Achse von # bis w als Term in w?`
- B-469 (3): winkel-dreiecke-e3-k2-s3-v1, winkel-dreiecke-e3-k2-s3-v2, winkel-dreiecke-e3-k2-s3-v3 – `Ein gleichschenkliges Dreieck hat zwei Basiswinkel von je #^\circ.Wie groß ist der Winkel an der Spitze?`
- B-470 (2): ableitungsregeln-e1-k2-s8-v2, ableitungsregeln-e1-k2-s8-v3 – `f(x)=\frac{#}{#}x^#-\frac{#}{#}x^#+#x.Weise nach:f'(x)=\frac{#}{#}\cdot(x-#)^#\cdot(x+#)^#.(Abitur # GK)`
- B-471 (2): punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e5-k1-s1-v5 – `Gerades Prisma ABCDEF(D über A,E über B,F über C)mit A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#):F?(Abitur # GK)`
- B-472 (2): uneigentliche-integrale-e1-k1-s1-v1, uneigentliche-integrale-e1-k1-s1-v3 – `f(x)=e^{-#x}–Inhalt A(w)der Fläche zwischen dem Graphen von f und der x-Achse von # bis w als Term in w?`
- B-473 (5): trigonometrie-e3-k1-s1-v1, trigonometrie-e3-k1-s1-v2, trigonometrie-e3-k1-s1-v3, trigonometrie-e3-k1-s1-v4, trigonometrie-e3-k1-s1-v5 – `Gleichschenkliges Dreieck:Schenkel # cm,Basiswinkel #^\circ.Wie lang ist die Höhe h auf die Grundseite?`
- B-474 (3): kenngroessen-von-verteilungen-e3-k1-s1-v1, kenngroessen-von-verteilungen-e3-k1-s1-v2, kenngroessen-von-verteilungen-e3-k1-s1-v3 – `X ist binomialverteilt mit n=# und dem Erwartungswert\mu=#.Bestimme p und die Standardabweichung\sigma.`
- B-475 (4): punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v2, punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v4, punkte-und-strecken-im-koordinatensystem-e3-k1-s1-v5 – `Zeige:Das Dreieck A(#|#|#),B(#|#|#),C(#|#|#)ist gleichschenklig.Nenne Basis und Schenkel.(Abitur # GK)`
- B-476 (3): winkel-dreiecke-e1-k2-s4-v1, winkel-dreiecke-e1-k2-s4-v2, winkel-dreiecke-e1-k2-s4-v3 – `Bestimme den überstumpfen Winkel α.Miss dazu den Rest bis zum Vollwinkel.‖Grafik:\winkel[#]{#}{\alpha}`
- B-477 (2): linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v1, linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v2 – `Forme\vec{OX}=p\cdot\vec{OA}+q\cdot\vec{OB}mit p+q=# für A(#|#|#)und B(#|#|#)in eine Parameterform um.`
- B-478 (4): lineare-funktionen-e1-k1-s0-v1, lineare-funktionen-e1-k1-s0-v2, lineare-funktionen-e1-k1-s0-v3, lineare-funktionen-e1-k1-s0-v4 – `Welcher Faktor?Mit welcher Zahl wird jeder x-Wert multipliziert?‖Grafik:\wertetabelle[#,#]{x}{y}{#,#}`
- B-479 (4): zuordnungen-e1-k2-s0-v1, zuordnungen-e1-k2-s0-v2, zuordnungen-e1-k2-s0-v3, zuordnungen-e1-k2-s0-v4 – `Auf einer Achse stehen die Zahlen # # und # je # Kästchen auseinander.Wie viel ist ein Kästchen wert?`
- B-480 (3): bruchrechnung-e2-k1-s0-v1, bruchrechnung-e2-k1-s0-v2, bruchrechnung-e2-k1-s0-v3 – `Welche Zahl steht in der Stellenwerttafel?‖Grafik:\sachtabelle{ccc}{Einer&Zehntel&Hundertstel}{#&#&#}`
- B-481 (3): trigonometrie-e3-k1-s12-v1, trigonometrie-e3-k1-s12-v2, trigonometrie-e3-k1-s12-v3 – `Dreieck ABC mit der Höhe h von C auf AB:AC=# cm,\alpha=#^\circ,\beta=#^\circ.Berechne erst h,dann BC.`
- B-482 (2): strahlensaetze-e1-k2-s0-v1, strahlensaetze-e1-k2-s0-v2 – `Maßstab #:#–ist die Zeichnung kleiner oder größer als die Wirklichkeit?\kreuz{kleiner}\\kreuz{größer}`
- B-483 (2): flaecheninhalt-durch-integration-e4-k1-s1-v1, flaecheninhalt-durch-integration-e4-k1-s1-v2 – `Für m># schließt die Gerade y=m\cdot x mit dem Graphen von f(x)=#x^# eine Fläche vom Inhalt # ein–m?`
- B-484 (3): strahlensaetze-e2-k1-s4-v1, strahlensaetze-e2-k1-s4-v2, strahlensaetze-e2-k1-s4-v3 – `\overline{AB}=#\text{cm},die Bildstrecke\overline{A'B'}=#\text{cm}–wie groß ist der Streckfaktor k?`
- B-485 (2): quadratische-funktionen-e1-k1-s6-v1, quadratische-funktionen-e1-k1-s6-v3 – `f(x)=-#x^#–\kreuz{nach oben}\kreuz{nach unten}\\kreuz{schmaler}\kreuz{breiter}als die Normalparabel`
- B-486 (2): kenngroessen-von-verteilungen-e2-k3-s1-v2, kenngroessen-von-verteilungen-e2-k3-s1-v3 – `Die Zufallsgröße X nimmt die Werte # # und # an,mit P(X=#)=# und E(X)=#.Bestimme P(X=#)und P(X=#).`
- B-487 (2): terme-e1-k3-s1-v1, terme-e1-k3-s1-v3 – `Erfinde eine Situation,zu der der Term #+#x passt.Wofür steht x?Was bedeutet der Termwert für x=#?`
- B-488 (3): winkel-dreiecke-e3-k2-s5-v1, winkel-dreiecke-e3-k2-s5-v2, winkel-dreiecke-e3-k2-s5-v3 – `Ein Dreieck hat einen rechten Winkel und einen Winkel von #^\circ.Wie groß ist der dritte Winkel?`
- B-489 (3): tangente-normale-schnittwinkel-e3-k1-s1-v1, tangente-normale-schnittwinkel-e3-k1-s1-v3, tangente-normale-schnittwinkel-e3-k1-s1-v5 – `Die Tangente an den Graphen von f im Punkt P(#|#)hat die Steigung #.Gleichung der Normalen in P?`
- B-490 (2): flaecheninhalt-und-volumen-im-raum-e3-k1-s1-v1, flaecheninhalt-und-volumen-im-raum-e3-k1-s1-v4 – `Pyramide mit der Grundfläche P(#|#|#),Q(#|#|#),R(#|#|#),T(#|#|#)und der Spitze S(#|#|#).Volumen?`
- B-491 (3): brueche-dezimalzahlen-e4-k1-s3-v1, brueche-dezimalzahlen-e4-k1-s3-v2, brueche-dezimalzahlen-e4-k1-s3-v3 – `Trage # und # am Zahlenstrahl ein.‖Grafik:\zahlenstrahl[xmin=#xmax=#xstep=#karo=#]{#/# #/# #/#}`
- B-492 (2): quadratische-gleichungen-e2-k1-s10-v1, quadratische-gleichungen-e2-k1-s10-v2 – `Welcher Wert erfüllt x\cdot(x+#)=-#?(P# # OS)\\kreuz{x=#}\\kreuz{x=#}\\kreuz{x=-#}\\kreuz{x=-#}`
- B-493 (2): trigonometrische-funktionen-e2-k1-s1-v1, trigonometrische-funktionen-e2-k1-s1-v5 – `Fülle die Wertetabelle für y=sin(x)aus(zwei Stellen).‖Grafik:\wertetabelle{x in°}{y}{#,#,#,#,#}`
- B-494 (3): winkel-dreiecke-e4-k1-s8-v1, winkel-dreiecke-e4-k1-s8-v2, winkel-dreiecke-e4-k1-s8-v3 – `Lässt sich aus den Seiten # cm,# cm und # cm ein Dreieck konstruieren?\\kreuz{ja}\\kreuz{nein}`
- B-495 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s0-v2, linearkombination-und-lineare-abhaengigkeit-e1-k1-s0-v4 – `\vec{a}=(#|#|#)und\vec{b}=(#|#|#).Ist einer ein Vielfaches des anderen?\\kreuz{ja}\kreuz{nein}`
- B-496 (3): zinsrechnung-e2-k1-s7-v1, zinsrechnung-e2-k1-s7-v2, zinsrechnung-e2-k1-s7-v3 – `#€zu #\%,# Jahre:einmal mit einfachen Zinsen,einmal mit Zinseszins.Wie viel Euro Unterschied?`
- B-497 (5): punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v3, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v4, punkte-und-strecken-im-koordinatensystem-e1-k1-s1-v5 – `A(#|#|#)und B(#|#|#)eintragen,C ablesen.‖Grafik:\begin{ksys#}\rpunkt{#}{#}{#}{C}\end{ksys#}`
- B-498 (3): kreis-e1-k2-s1-v1, kreis-e1-k2-s1-v2, kreis-e1-k2-s1-v4 – `Kreis mit d=# cm–wie lang ist der Umfang?Rechne mit der\pi-Taste und runde auf eine Stelle.`
- B-499 (3): kreis-e2-k1-s1-v1, kreis-e2-k1-s1-v3, kreis-e2-k1-s1-v5 – `Kreis mit r=# cm–wie groß ist die Fläche?Rechne mit der\pi-Taste und runde auf eine Stelle.`
- B-500 (3): matrizen-und-uebergangsprozesse-e5-k1-s1-v1, matrizen-und-uebergangsprozesse-e5-k1-s1-v2, matrizen-und-uebergangsprozesse-e5-k1-s1-v3 – `Es gilt v_{n+#}=M\cdot v_n;M=((#|#),(#|#)),Gesamtzahl #.Berechne die stationäre Verteilung.`
- B-501 (2): kreis-e2-k1-s3-v1, kreis-e2-k1-s3-v3 – `Kreis mit r=# m–wie groß ist die Fläche?Rechne mit der\pi-Taste und runde auf zwei Stellen.`
- B-502 (4): bruchrechnung-e1-k3-s0-v1, bruchrechnung-e1-k3-s0-v2, bruchrechnung-e1-k3-s0-v3, bruchrechnung-e1-k3-s0-v4 – `Färbe\frac{#}{#},dann weitere\frac{#}{#}–wie viel ist gefärbt?‖Grafik:\bruchrechteck{#}{#}`
- B-503 (2): kreis-e3-k1-s3-v1, kreis-e3-k1-s3-v3 – `Ein Kreisausschnitt ist\frac{#}{#}des ganzen Kreises.Wie groß ist sein Mittelpunktswinkel?`
- B-504 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s4-v2, punkte-und-strecken-im-koordinatensystem-e4-k1-s4-v3 – `Zeige:A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)bilden eine Raute,aber kein Quadrat.(Abitur # GK)`
- B-505 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s7-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s7-v2 – `Zeige:Das Viereck K(#|#|#),L(#|#|#),M(#|#|#),N(#|-#|#)ist ein Drachenviereck.(Abitur # GK)`
- B-506 (3): zinsrechnung-e2-k1-s2-v1, zinsrechnung-e2-k1-s2-v2, zinsrechnung-e2-k1-s2-v3 – `#€zu #\%,die Zinsen bleiben auf dem Konto.Rechne Jahr für Jahr–Guthaben nach zwei Jahren?`
- B-507 (2): lineare-funktionen-e4-k1-s2-v1, lineare-funktionen-e4-k1-s2-v3 – `Gleichung?Eine Gerade hat die Steigung m=# und geht durch P(#|#).Bestimme ihre Gleichung.`
- B-508 (2): rationale-zahlen-e2-k3-s0-v1, rationale-zahlen-e2-k3-s0-v4 – `Zeichne den Pfeil:Start bei-# # nach rechts.‖Grafik:\zahlenstrahl[xmin=-#xmax=#xstep=#]{}`
- B-509 (5): einheiten-e3-k2-s1-v1, einheiten-e3-k2-s1-v2, einheiten-e3-k2-s1-v3, einheiten-e3-k2-s1-v4, einheiten-e3-k2-s1-v5 – `Eine Fläche ist # Flächeneinheiten groß;eine Längeneinheit entspricht # cm.Wie viel cm²?`
- B-510 (2): lineare-gleichungssysteme-e3-k1-s4-v2, lineare-gleichungssysteme-e3-k1-s4-v3 – `I:#x+#y=# II:#x+#y=#–Lösung?Vervielfache beide Gleichungen und addiere oder subtrahiere.`
- B-511 (3): koerper-e3-k1-s3-v1, koerper-e3-k1-s3-v2, koerper-e3-k1-s3-v3 – `Dreiecksprisma:Dreieck mit Grundseite # cm und Höhe # cm;Höhe des Prismas # cm–Volumen?`
- B-512 (3): vektoren-und-rechenoperationen-e1-k2-s1-v1, vektoren-und-rechenoperationen-e1-k2-s1-v2, vektoren-und-rechenoperationen-e1-k2-s1-v3 – `A(#|#|#),B(#|#|#):\overrightarrow{AB},\overrightarrow{BA}und #\cdot\overrightarrow{AB}?`
- B-513 (3): winkel-dreiecke-e1-k2-s3-v1, winkel-dreiecke-e1-k2-s3-v2, winkel-dreiecke-e1-k2-s3-v3 – `Zeichne an den Strahl mit dem Scheitel S einen Winkel von #^\circ.‖Grafik:\winkelstrahl`
- B-514 (2): lineare-gleichungen-e1-k2-s5-v3, lineare-gleichungen-e1-k2-s5-v4 – `#-#x=#x-#–welche Zahl ist die Lösung?(P# # OS)\\kreuz{-#}\\kreuz{#}\\kreuz{#}\\kreuz{#}`
- B-515 (2): potenzen-wurzeln-e3-k2-s0-v1, potenzen-wurzeln-e3-k2-s0-v2 – `\sqrt{#}–geht die Wurzel im Kopf auf?\\kreuz{ja,Quadratzahl}\\kreuz{nein,Näherungswert}`
- B-516 (2): pyramide-kegel-kugel-e1-k5-s6-v1, pyramide-kegel-kugel-e1-k5-s6-v3 – `Quadratische Pyramide:Grundkante # cm,Seitenhöhe # cm–Flächeninhalt einer Seitenfläche?`
- B-517 (2): trigonometrische-funktionen-e1-k1-s7-v1, trigonometrische-funktionen-e1-k1-s7-v3 – `sin\alpha=#–welche beiden Winkel im ersten Vollkreis ab #°passen?Runde auf eine Stelle.`
- B-518 (3): winkel-dreiecke-e3-k2-s6-v1, winkel-dreiecke-e3-k2-s6-v2, winkel-dreiecke-e3-k2-s6-v3 – `Ein Viereck hat die Winkel #^\circ,#^\circ und #^\circ.Wie groß ist der vierte Winkel?`
- B-519 (2): symmetrie-abbildungen-e1-k2-s0-v2, symmetrie-abbildungen-e1-k2-s0-v3 – `Welche Koordinate ist bei(#|#)null?\\kreuz{die erste}\\kreuz{die zweite}\\kreuz{keine}`
- B-520 (5): reelle-zahlen-e3-k1-s1-v1, reelle-zahlen-e3-k1-s1-v2, reelle-zahlen-e3-k1-s1-v3, reelle-zahlen-e3-k1-s1-v4, reelle-zahlen-e3-k1-s1-v5 – `\sqrt{#\cdot #}–erst malnehmen,dann Wurzel;und die Wurzeln einzeln.Gleiches Ergebnis?`
- B-521 (3): punkte-und-strecken-im-koordinatensystem-e4-k1-s1-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s1-v2, punkte-und-strecken-im-koordinatensystem-e4-k1-s1-v5 – `Zeige:A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)bilden ein Parallelogramm ABCD.(Abitur # LK)`
- B-522 (2): rationale-zahlen-e3-k1-s7-v1, rationale-zahlen-e3-k1-s7-v2 – `Berechne ohne Taschenrechner den Wert von\frac{a+b}{c}für a=# b=-# und c=-#.(P# # OS)`
- B-523 (2): uneigentliche-integrale-e2-k1-s1-v3, uneigentliche-integrale-e2-k1-s1-v5 – `F ist eine Stammfunktion von f(x)=#e^{-#x}.Was bedeutet F(w)-F(#)für w># geometrisch?`
- B-524 (3): brueche-dezimalzahlen-e4-k1-s7-v1, brueche-dezimalzahlen-e4-k1-s7-v2, brueche-dezimalzahlen-e4-k1-s7-v3 – `\frac{#}{#}–als Dezimalzahl?Die Division geht nicht auf;schreibe mit Periodenstrich.`
- B-525 (2): lineare-funktionen-e2-k4-s1-v1, lineare-funktionen-e2-k4-s1-v4 – `Wertetabelle:Fülle die Tabelle zu f(x)=#x-# aus.‖Grafik:\wertetabelle{x}{f(x)}{-#,#}`
- B-526 (2): rotationsvolumen-zone-f5-v1, rotationsvolumen-zone-f5-v2 – `Kugel mit Radius # cm,ebener Schnitt # cm vom Mittelpunkt–Radius des Schnittkreises?`
- B-527 (2): pythagoras-e3-k2-s6-v2, pythagoras-e3-k2-s6-v3 – `Raute mit den Diagonalen # cm und # cm–Seitenlänge?‖Grafik:\raute[diagonalen]{#}{#}`
- B-528 (2): quadratische-funktionen-e2-k1-s0-v1, quadratische-funktionen-e2-k1-s0-v3 – `f(x)=(x-#)^#+#–kreise die Zahl in der Klammer ein.Bei welchem x liegt der Scheitel?`
- B-529 (3): zinsrechnung-e1-k1-s8-v1, zinsrechnung-e1-k1-s8-v2, zinsrechnung-e1-k1-s8-v3 – `#€zu #\%,die Zinsen werden jedes Jahr ausgezahlt.Wie viel Euro Zinsen in # Jahren?`
- B-530 (3): zinsrechnung-e2-k1-s5-v1, zinsrechnung-e2-k1-s5-v2, zinsrechnung-e2-k1-s5-v3 – `Rechne in einem Schritt mit dem Wachstumsfaktor:#€zu #\%–Guthaben nach einem Jahr?`
- B-531 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v5 – `Sind\vec{u}=(#|#|-#)und\vec{v}=(#|#|-#)kollinear?Gib gegebenenfalls den Faktor an.`
- B-532 (2): zinsrechnung-e1-k1-s11-v3, zinsrechnung-e1-k1-s11-v4 – `Ein Sparguthaben von #€bringt in einem Jahr #€Zinsen.Gib den Zinssatz an.(P# # OS)`
- B-533 (2): potenzen-wurzeln-e2-k1-s0-v3, potenzen-wurzeln-e2-k1-s0-v4 – `#–wandert das Komma so viele Stellen,wie Nullen dastehen?\\kreuz{ja}\\kreuz{nein}`
- B-534 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v3, linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v4 – `Sind\vec{u}=(#|#|#)und\vec{v}=(#|#|#)kollinear?Gib gegebenenfalls den Faktor an.`
- B-535 (2): pythagoras-e2-k2-s6-v2, pythagoras-e2-k2-s6-v3 – `Hypotenuse # m,Kathete # m.Weise nach,dass die andere Kathete etwa # m lang ist.`
- B-536 (2): quadratische-gleichungen-e2-k1-s0-v1, quadratische-gleichungen-e2-k1-s0-v3 – `(x-#)\cdot(x+#)=#–gilt der Satz vom Nullprodukt?\\kreuz{gilt}\\kreuz{gilt nicht}`
- B-537 (3): zufallsgroessen-und-verteilungen-e2-k1-s1-v1, zufallsgroessen-und-verteilungen-e2-k1-s1-v2, zufallsgroessen-und-verteilungen-e2-k1-s1-v3 – `X nimmt die Werte # bis # an,die Verteilung ist symmetrisch,P(X=#)=#–P(X\le #)?`
- B-538 (2): flaecheninhalt-und-volumen-im-raum-e1-k2-s1-v2, flaecheninhalt-und-volumen-im-raum-e1-k2-s1-v3 – `P(#|#|#),Q(#|#|#),R(#|-#|#),rechtwinklig bei Q.Flächeninhalt des Dreiecks PQR?`
- B-539 (2): lineare-funktionen-e2-k2-s0-v1, lineare-funktionen-e2-k2-s0-v3 – `Steigt oder fällt die Gerade f(x)=#x-#?Kreuze an.\\kreuz{steigt}\\kreuz{fällt}`
- B-540 (2): pythagoras-e3-k2-s10-v1, pythagoras-e3-k2-s10-v3 – `Kegel:Durchmesser # cm,Höhe # cm–Mantellinie s?‖Grafik:\kegel{#}{#}{}{# cm}{s}`
- B-541 (2): quadratische-gleichungen-e3-k3-s8-v1, quadratische-gleichungen-e3-k3-s8-v3 – `x^#-#x+#=#–Diskriminante D=\left(\frac{p}{#}\right)^#-q und Zahl der Lösungen?`
- B-542 (3): punkte-und-strecken-im-koordinatensystem-e3-k1-s2-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s2-v2, punkte-und-strecken-im-koordinatensystem-e3-k1-s2-v3 – `Prüfe,ob das Dreieck A(#|#|#),B(#|#|#),C(#|#|#)gleichseitig ist.(Abitur # GK)`
- B-543 (2): punkte-und-strecken-im-koordinatensystem-e4-k1-s3-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s3-v3 – `Zeige:A(#|#|#),B(#|#|#),C(#|#|#),D(#|#|#)bilden eine Raute ABCD.(Abitur # GK)`
- B-544 (5): ebenen-e1-k1-s1-v1, ebenen-e1-k1-s1-v2, ebenen-e1-k1-s1-v3, ebenen-e1-k1-s1-v4, ebenen-e1-k1-s1-v5 – `Punkt(#|#|#),Spannvektoren(#|#|#)und(#|#|#):Parametergleichung der Ebene E?`
- B-545 (3): winkel-dreiecke-e1-k2-s2-v1, winkel-dreiecke-e1-k2-s2-v2, winkel-dreiecke-e1-k2-s2-v3 – `Miss den stumpfen Winkel α mit dem Geodreieck.‖Grafik:\winkel[#]{#}{\alpha}`
- B-546 (3): potenzen-wurzeln-e3-k2-s3-v1, potenzen-wurzeln-e3-k2-s3-v2, potenzen-wurzeln-e3-k2-s3-v3 – `\sqrt{#}–zwischen welchen ganzen Zahlen?Prüfe dann mit dem Taschenrechner.`
- B-547 (2): trigonometrie-zone-f2-v1, trigonometrie-zone-f2-v2 – `Ein Winkel ist #^\circ groß.Spitz oder stumpf?\\kreuz{spitz}\kreuz{stumpf}`
- B-548 (3): potenzen-wurzeln-e3-k2-s2-v1, potenzen-wurzeln-e3-k2-s2-v2, potenzen-wurzeln-e3-k2-s2-v3 – `\sqrt{#}–mit dem Taschenrechner,auf zwei Stellen nach dem Komma gerundet?`
- B-549 (3): trigonometrie-e1-k3-s4-v1, trigonometrie-e1-k3-s4-v2, trigonometrie-e1-k3-s4-v3 – `Hypotenuse # cm,\alpha=#^\circ–wie lang ist die Gegenkathete x von\alpha?`
- B-550 (2): pythagoras-e3-k2-s11-v2, pythagoras-e3-k2-s11-v3 – `Kegel:Mantellinie # m,Radius # m–Höhe h?‖Grafik:\kegel{#}{#}{# m}{h}{# m}`
- B-551 (2): lineare-gleichungssysteme-e1-k1-s1-v2, lineare-gleichungssysteme-e1-k1-s1-v3 – `#x+y=#–Lösungspaare?Ergänze die Tabelle.‖Grafik:\wertetabelle{x}{y}{#,#}`
- B-552 (5): zinsrechnung-e2-k1-s1-v1, zinsrechnung-e2-k1-s1-v2, zinsrechnung-e2-k1-s1-v3, zinsrechnung-e2-k1-s1-v4, zinsrechnung-e2-k1-s1-v5 – `#€zu #\%,die Zinsen werden am Jahresende gutgeschrieben–neues Guthaben?`
- B-553 (3): reelle-zahlen-e1-k1-s2-v1, reelle-zahlen-e1-k1-s2-v2, reelle-zahlen-e1-k1-s2-v3 – `\sqrt{#}–rational oder irrational?\\kreuz{rational}\\kreuz{irrational}`
- B-554 (3): trigonometrie-e1-k3-s5-v1, trigonometrie-e1-k3-s5-v2, trigonometrie-e1-k3-s5-v3 – `Hypotenuse # cm,\alpha=#^\circ–wie lang ist die Ankathete x von\alpha?`
- B-555 (2): brueche-dezimalzahlen-e1-k1-s6-v11, brueche-dezimalzahlen-e1-k1-s6-v12 – `Schraffiere\frac{#}{#}der Fläche.(P# # OS)‖Grafik:\bruchrechteck{#}{#}`
- B-556 (2): brueche-dezimalzahlen-e1-k1-s6-v13, brueche-dezimalzahlen-e1-k1-s6-v14 – `Markiere\frac{#}{#}des Rechtecks.(P# # OS)‖Grafik:\bruchrechteck{#}{#}`
- B-557 (2): brueche-dezimalzahlen-e3-k1-s7-v1, brueche-dezimalzahlen-e3-k1-s7-v2 – `Gib eine Zahl an,die zwischen\frac{#}{#}und\frac{#}{#}liegt.(P# # OS)`
- B-558 (2): linearkombination-und-lineare-abhaengigkeit-e1-k1-s3-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s3-v2 – `Sind\vec{a}=(#|#|#),\vec{b}=(#|#|#)und\vec{c}=(#|#|#)linear abhängig?`
- B-559 (2): quadratische-gleichungen-e1-k2-s0-v1, quadratische-gleichungen-e1-k2-s0-v2 – `(x-#)^#=#–wie viele Lösungen?\\kreuz{zwei}\\kreuz{eine}\\kreuz{keine}`
- B-560 (2): reelle-zahlen-e1-k1-s0-v1, reelle-zahlen-e1-k1-s0-v2 – `\sqrt{#}–geht die Wurzel auf?\\kreuz{geht auf}\\kreuz{geht nicht auf}`
- B-561 (2): spiegelung-e2-k1-s1-v1, spiegelung-e2-k1-s1-v3 – `Q(#|#|#)ist das Spiegelbild von P(#|#|#).Bestimme die Spiegelebene E.`
- B-562 (3): potenzen-wurzeln-e1-k2-s0-v1, potenzen-wurzeln-e1-k2-s0-v2, potenzen-wurzeln-e1-k2-s0-v4 – `#^{-#}–Bruch oder negative Zahl?\\kreuz{Bruch}\\kreuz{negative Zahl}`
- B-563 (2): pyramide-kegel-kugel-e2-k2-s8-v1, pyramide-kegel-kugel-e2-k2-s8-v3 – `Kegel:Radius # cm,Mantellinie # cm–Oberfläche?Runde auf eine Stelle.`
- B-564 (3): quadratische-funktionen-e1-k1-s1-v2, quadratische-funktionen-e1-k1-s1-v4, quadratische-funktionen-e1-k1-s1-v5 – `Wertetabelle zu f(x)=x^#–fülle aus.\wertetabelle{x}{f(x)}{-#-#-#,#}`
- B-565 (3): zinsrechnung-e1-k1-s4-v1, zinsrechnung-e1-k1-s4-v2, zinsrechnung-e1-k1-s4-v3 – `#€Kapital bringen in einem Jahr #€Zinsen.Wie hoch ist der Zinssatz?`
- B-566 (2): flaechen-e2-k1-s2-v1, flaechen-e2-k1-s2-v3 – `Parallelogramm:Grundseite # cm,schräge Seite # cm,Höhe # cm–Fläche?`
- B-567 (2): matrizen-und-uebergangsprozesse-e2-k1-s2-v1, matrizen-und-uebergangsprozesse-e2-k1-s2-v2 – `Bestimme alle Vektoren v mit M\cdot v=#\cdot v für M=((#|#),(#|#)).`
- B-568 (5): winkel-dreiecke-e1-k2-s1-v1, winkel-dreiecke-e1-k2-s1-v2, winkel-dreiecke-e1-k2-s1-v3, winkel-dreiecke-e1-k2-s1-v4, winkel-dreiecke-e1-k2-s1-v5 – `Miss den Winkel α mit dem Geodreieck.‖Grafik:\winkel[#]{#}{\alpha}`
- B-569 (3): ebenen-e2-k1-s1-v1, ebenen-e2-k1-s1-v2, ebenen-e2-k1-s1-v3 – `Spannvektoren(#|#|#)und(#|#|#):ein Normalenvektor\vec n der Ebene?`
- B-570 (3): quadratische-funktionen-e1-k1-s5-v1, quadratische-funktionen-e1-k1-s5-v2, quadratische-funktionen-e1-k1-s5-v3 – `Wertetabelle zu f(x)=#x^#–fülle aus.\wertetabelle{x}{f(x)}{-#-#,#}`
- B-571 (3): quadratische-gleichungen-e4-k1-s3-v1, quadratische-gleichungen-e4-k1-s3-v2, quadratische-gleichungen-e4-k1-s3-v3 – `Das Produkt einer Zahl x mit ihrem Nachfolger ist #.Welche Zahlen?`
- B-572 (3): strahlensaetze-e1-k2-s8-v1, strahlensaetze-e1-k2-s8-v2, strahlensaetze-e1-k2-s8-v3 – `Karte im Maßstab #:# auf der Karte #\text{cm}–wie viele Kilometer?`
- B-573 (2): brueche-dezimalzahlen-e2-k1-s0-v3, brueche-dezimalzahlen-e2-k1-s0-v4 – `\frac{#}{#}\to\frac{#}{#}–erweitert oder gekürzt,mit welcher Zahl?`
- B-574 (2): lineare-gleichungen-e1-k3-s2-v1, lineare-gleichungen-e1-k3-s2-v3 – `Probiere eigene Zahlen:#x+#=#‖Grafik:\wertetabelleleer{x}{#x+#}{#}`
- B-575 (2): potenzen-wurzeln-e1-k3-s15-v5, potenzen-wurzeln-e1-k3-s15-v6 – `#^# #^# #^#–welche Zahl ist die größte?Unterstreiche sie.(P# # OS)`
- B-576 (2): rationale-zahlen-e1-k1-s1-v1, rationale-zahlen-e1-k1-s1-v2 – `Trage ein:-# # und-#.‖Grafik:\zahlenstrahl[xmin=-#xmax=#xstep=#]{}`
- B-577 (2): symmetrie-abbildungen-e2-k2-s1-v1, symmetrie-abbildungen-e2-k2-s1-v4 – `Zeichne die Symmetrieachse der Figur ein.‖Grafik:\drachen{#}{#}{#}`
- B-578 (2): kurvenuntersuchung-e3-k1-s1-v1, kurvenuntersuchung-e3-k1-s1-v3 – `Bilde die erste,zweite und dritte Ableitung von f(x)=x^#-#x^#+#x.`
- B-579 (2): linearkombination-und-lineare-abhaengigkeit-zone-f4-v1, linearkombination-und-lineare-abhaengigkeit-zone-f4-v2 – `Ist(#|#)ein Vielfaches von(#|#)?Gib gegebenenfalls den Faktor an.`
- B-580 (2): quadratische-funktionen-e1-k1-s1-v1, quadratische-funktionen-e1-k1-s1-v3 – `Wertetabelle zu f(x)=x^#–fülle aus.\wertetabelle{x}{f(x)}{-#-#,#}`
- B-581 (2): vektoren-und-rechenoperationen-e2-k1-s7-v2, vektoren-und-rechenoperationen-e2-k1-s7-v3 – `Q liegt von L(#|#|#)aus im Abstand # in Richtung\vec r=(#|#|#):Q?`
- B-582 (5): strahlensaetze-e1-k2-s1-v1, strahlensaetze-e1-k2-s1-v2, strahlensaetze-e1-k2-s1-v3, strahlensaetze-e1-k2-s1-v4, strahlensaetze-e1-k2-s1-v5 – `Maßstab #:#–wie viel ist #\text{cm}auf dem Plan in Wirklichkeit?`
- B-583 (3): koerper-e3-k1-s2-v1, koerper-e3-k1-s2-v2, koerper-e3-k1-s2-v3 – `Prisma mit rechteckiger Grundfläche # cm×# cm,Höhe # cm–Volumen?`
- B-584 (3): prozentrechnung-e1-k1-s1-v1, prozentrechnung-e1-k1-s1-v2, prozentrechnung-e1-k1-s1-v3 – `Wie viel Prozent sind grau?‖Grafik:\streifenfeld[#]{#}{#\%}{#\%}`
- B-585 (2): bruchrechnung-e5-k1-s6-v3, bruchrechnung-e5-k1-s6-v4 – `Berechne den Wert des Terms(a+b):c für a=# b=# und c=#.(P# # OS)`
- B-586 (2): pyramide-kegel-kugel-e2-k2-s7-v1, pyramide-kegel-kugel-e2-k2-s7-v3 – `Kegel:Radius # cm,Mantellinie # cm–Mantel?Runde auf eine Stelle.`
- B-587 (2): reelle-zahlen-e2-k3-s1-v1, reelle-zahlen-e2-k3-s1-v2 – `Finde den Fehler und rechne richtig:\rechnung{#^#\cdot #^#&=#^#}`
- B-588 (2): trigonometrie-e3-k1-s2-v1, trigonometrie-e3-k1-s2-v3 – `Trapez:Höhe # m,Basiswinkel #^\circ.Wie lang ist der Schenkel s?`
- B-589 (5): trigonometrie-e4-k1-s1-v1, trigonometrie-e4-k1-s1-v2, trigonometrie-e4-k1-s1-v3, trigonometrie-e4-k1-s1-v4, trigonometrie-e4-k1-s1-v5 – `Dreieck ABC:a=# cm,\alpha=#^\circ,\beta=#^\circ.Wie lang ist b?`
- B-590 (3): trigonometrie-e1-k3-s7-v1, trigonometrie-e1-k3-s7-v2, trigonometrie-e1-k3-s7-v3 – `Gegenkathete # cm,\alpha=#^\circ–wie lang ist die Hypotenuse x?`
- B-591 (3): zinsrechnung-e2-k1-s6-v1, zinsrechnung-e2-k1-s6-v2, zinsrechnung-e2-k1-s6-v3 – `#€zu #\%mit Zinseszins,# Jahre–Guthaben am Ende?Runde auf Cent.`
- B-592 (2): brueche-dezimalzahlen-e5-k2-s9-v9, brueche-dezimalzahlen-e5-k2-s9-v10 – `Welche Zahl liegt genau in der Mitte zwischen-# und-#?(P# # OS)`
- B-593 (2): pyramide-kegel-kugel-e1-k5-s8-v2, pyramide-kegel-kugel-e1-k5-s8-v3 – `Quadratische Pyramide:Grundkante # m,Seitenhöhe # m–Oberfläche?`
- B-594 (3): trigonometrie-e1-k3-s9-v1, trigonometrie-e1-k3-s9-v2, trigonometrie-e1-k3-s9-v3 – `Ankathete # cm,\alpha=#^\circ–wie lang ist die Gegenkathete x?`
- B-595 (3): trigonometrie-e1-k3-s10-v1, trigonometrie-e1-k3-s10-v2, trigonometrie-e1-k3-s10-v3 – `Gegenkathete # cm,\alpha=#^\circ–wie lang ist die Ankathete x?`
- B-596 (3): zinsrechnung-e2-k1-s8-v1, zinsrechnung-e2-k1-s8-v2, zinsrechnung-e2-k1-s8-v3 – `#€zu #\%mit Zinseszins,# Jahre–wie viel Euro Zinsen insgesamt?`
- B-597 (2): brueche-dezimalzahlen-e4-k1-s6-v1, brueche-dezimalzahlen-e4-k1-s6-v3 – `\frac{#}{#}–als Dezimalzahl?Teile den Zähler durch den Nenner.`
- B-598 (2): normalverteilung-und-sigma-regeln-zone-f1-v1, normalverteilung-und-sigma-regeln-zone-f1-v2 – `X nimmt # und # je mit Wahrscheinlichkeit # an.Erwartungswert?`
- B-599 (3): brueche-dezimalzahlen-e5-k2-s0-v1, brueche-dezimalzahlen-e5-k2-s0-v2, brueche-dezimalzahlen-e5-k2-s0-v3 – `Hänge Nullen an,bis beide gleich viele Stellen haben:# und #.`
- B-600 (3): potenzen-wurzeln-e3-k2-s8-v1, potenzen-wurzeln-e3-k2-s8-v2, potenzen-wurzeln-e3-k2-s8-v3 – `\sqrt{-#}und-\sqrt{#}–welcher Term hat einen Wert?Gib ihn an.`
- B-601 (2): prozentrechnung-e1-k1-s1-v4, prozentrechnung-e1-k1-s1-v5 – `Wie viel Prozent sind grau?‖Grafik:\streifenfeld{#}{#\%}{#\%}`
- B-602 (2): prozentrechnung-e1-k2-s1-v1, prozentrechnung-e1-k2-s1-v2 – `#;\frac{#}{#};#\%;\frac{#}{#}–der Größe nach,kleinste zuerst?`
- B-603 (2): pythagoras-e2-k2-s2-v1, pythagoras-e2-k2-s2-v3 – `Hypotenuse c=# cm,Kathete b=# cm–Kathete a auf eine Dezimale?`
- B-604 (2): pythagoras-e3-k2-s2-v1, pythagoras-e3-k2-s2-v3 – `Gleichschenkliges Dreieck:Grundseite # cm,Höhe # cm–Schenkel?`
- B-605 (4): matrizen-und-uebergangsprozesse-e2-k1-s1-v1, matrizen-und-uebergangsprozesse-e2-k1-s1-v2, matrizen-und-uebergangsprozesse-e2-k1-s1-v3, matrizen-und-uebergangsprozesse-e2-k1-s1-v5 – `Bestimme alle Vektoren v mit M\cdot v=v für M=((#|#),(#|#)).`
- B-606 (3): koerper-e4-k2-s2-v1, koerper-e4-k2-s2-v2, koerper-e4-k2-s2-v3 – `Zylinder:Durchmesser # cm,Höhe # cm–Volumen auf eine Stelle?`
- B-607 (3): lineare-gleichungen-e1-k3-s1-v1, lineare-gleichungen-e1-k3-s1-v3, lineare-gleichungen-e1-k3-s1-v5 – `Für welches x ist #x+#=#?‖Grafik:\wertetabelle{x}{#x+#}{#,#}`
- B-608 (3): trigonometrie-e1-k3-s8-v1, trigonometrie-e1-k3-s8-v2, trigonometrie-e1-k3-s8-v3 – `Ankathete # cm,\alpha=#^\circ–wie lang ist die Hypotenuse x?`
- B-609 (2): brueche-dezimalzahlen-e1-k1-s6-v7, brueche-dezimalzahlen-e1-k1-s6-v8 – `Markiere #\%der Fläche.(P# # OS)‖Grafik:\bruchrechteck{#}{#}`
- B-610 (2): flaechen-zone-f6-v1, flaechen-zone-f6-v2 – `Ist das ein rechter Winkel?\janein‖Grafik:\winkel{#}{\alpha}`
- B-611 (2): lineare-gleichungen-e1-k3-s1-v2, lineare-gleichungen-e1-k3-s1-v4 – `Für welches x ist #x-#=#?‖Grafik:\wertetabelle{x}{#x-#}{#,#}`
- B-612 (2): pythagoras-e2-k2-s4-v2, pythagoras-e2-k2-s4-v3 – `Hypotenuse c=# m,Kathete b=# m–Kathete a?Ist a kürzer als c?`
- B-613 (2): rationale-zahlen-e3-k1-s8-v1, rationale-zahlen-e3-k1-s8-v2 – `Berechne den Wert von(a+b):c für a=# b=-# und c=-#.(P# # OS)`
- B-614 (3): binomische-formeln-e3-k1-s0-v1, binomische-formeln-e3-k1-s0-v2, binomische-formeln-e3-k1-s0-v4 – `x^#+#x+#–Quadrate mit Wurzeln?Passt das Mittelglied?\janein`
- B-615 (3): zinsrechnung-e1-k1-s6-v1, zinsrechnung-e1-k1-s6-v2, zinsrechnung-e1-k1-s6-v3 – `#€Zinsen im Jahr sind #\%vom Kapital.Wie viel Euro Kapital?`
- B-616 (2): pyramide-kegel-kugel-e2-k2-s11-v1, pyramide-kegel-kugel-e2-k2-s11-v3 – `Kegel:Volumen # cm³,Radius # cm–Höhe?Runde auf eine Stelle.`
- B-617 (2): rotationsvolumen-e1-k1-s1-v2, rotationsvolumen-e1-k1-s1-v3 – `f(x)=#x+# rotiert über[#;#]um die x-Achse–Rotationsvolumen?`
- B-618 (2): trigonometrie-e4-k1-s12-v1, trigonometrie-e4-k1-s12-v2 – `Dreieck ABC:a=# cm,\alpha=#^\circ,b=# cm.Wie groß ist\beta?`
- B-619 (3): trigonometrische-funktionen-e1-k1-s9-v1, trigonometrische-funktionen-e1-k1-s9-v2, trigonometrische-funktionen-e1-k1-s9-v3 – `#°ins Bogenmaß–als Vielfaches von\pi und auf zwei Stellen?`
- B-620 (2): gleichungen-loesen-e2-k1-s2-v1, gleichungen-loesen-e2-k1-s2-v2 – `f(x)=#e^{#x}-#.Bestimme die Nullstelle exakt.(Abitur # LK)`
- B-621 (3): potenzen-wurzeln-e1-k3-s9-v1, potenzen-wurzeln-e1-k3-s9-v2, potenzen-wurzeln-e1-k3-s9-v3 – `#^# #^# #^#–welche Zahl ist die größte?Unterstreiche sie.`
- B-622 (2): flaecheninhalt-und-volumen-im-raum-zone-f5-v1, flaecheninhalt-und-volumen-im-raum-zone-f5-v2 – `Rechtwinkliges Dreieck,Katheten # cm und # cm.Hypotenuse?`
- B-623 (2): potenzen-wurzeln-e3-k2-s13-v5, potenzen-wurzeln-e3-k2-s13-v6 – `\sqrt{#};-\frac{#}{#};#;-#–aufsteigend geordnet?(P# # OS)`
- B-624 (3): koerper-e4-k2-s8-v1, koerper-e4-k2-s8-v2, koerper-e4-k2-s8-v3 – `Zylinder:Volumen # cm³,Radius # cm–Höhe auf eine Stelle?`
- B-625 (3): reelle-zahlen-e2-k1-s1-v1, reelle-zahlen-e2-k1-s1-v2, reelle-zahlen-e2-k1-s1-v4 – `#^#\cdot #^#–als Malkette,wie viele Faktoren,als Potenz?`
- B-626 (2): pyramide-kegel-kugel-e1-k5-s2-v1, pyramide-kegel-kugel-e1-k5-s2-v3 – `Quadratische Pyramide:Grundkante # cm,Höhe # cm–Volumen?`
- B-627 (2): trigonometrie-e4-k1-s13-v1, trigonometrie-e4-k1-s13-v2 – `Dreieck ABC:a=# cm,b=# cm,\gamma=#^\circ.Wie lang ist c?`
- B-628 (5): zinsrechnung-e1-k1-s1-v1, zinsrechnung-e1-k1-s1-v2, zinsrechnung-e1-k1-s1-v3, zinsrechnung-e1-k1-s1-v4, zinsrechnung-e1-k1-s1-v5 – `Sparbuch:#€zu #\%–wie viel Euro Zinsen nach einem Jahr?`
- B-629 (3): potenzen-wurzeln-e1-k1-s0-v1, potenzen-wurzeln-e1-k1-s0-v2, potenzen-wurzeln-e1-k1-s0-v4 – `(-#)^#–plus oder minus?\\kreuz{positiv}\\kreuz{negativ}`
- B-630 (3): zinsrechnung-e1-k3-s1-v1, zinsrechnung-e1-k3-s1-v2, zinsrechnung-e1-k3-s1-v3 – `Überschlage:#€zu #\%–etwa wie viel Euro Zinsen im Jahr?`
- B-631 (2): grenzwerte-und-verhalten-im-unendlichen-e2-k1-s1-v2, grenzwerte-und-verhalten-im-unendlichen-e2-k1-s1-v4 – `f(x)=e^{-#x}.Verhalten für x\to+\infty und x\to-\infty?`
- B-632 (2): wahrscheinlichkeit-zone-f1-v1, wahrscheinlichkeit-zone-f1-v2 – `Kürze\frac{#}{#}und schreibe den Bruch als Prozentsatz.`
- B-633 (3): brueche-dezimalzahlen-e5-k2-s5-v1, brueche-dezimalzahlen-e5-k2-s5-v2, brueche-dezimalzahlen-e5-k2-s5-v3 – `Welche Zahl liegt genau in der Mitte zwischen # und #?`
- B-634 (3): koerper-e4-k2-s5-v1, koerper-e4-k2-s5-v2, koerper-e4-k2-s5-v3 – `Zylinder:Radius # cm,Höhe # cm–Mantel auf eine Stelle?`
- B-635 (3): trigonometrische-funktionen-e1-k1-s6-v1, trigonometrische-funktionen-e1-k1-s6-v2, trigonometrische-funktionen-e1-k1-s6-v3 – `#°–welches Vorzeichen haben Sinuswert und Kosinuswert?`
- B-636 (3): zinsrechnung-e1-k1-s2-v1, zinsrechnung-e1-k1-s2-v2, zinsrechnung-e1-k1-s2-v3 – `Rechne über #\%:#€zu #\%–wie viel Euro Zinsen im Jahr?`
- B-637 (2): pythagoras-e1-k2-s3-v1, pythagoras-e1-k2-s3-v3 – `Katheten a=# cm,b=# cm–Hypotenuse c auf eine Dezimale?`
- B-638 (2): reelle-zahlen-e2-k1-s1-v3, reelle-zahlen-e2-k1-s1-v5 – `#\cdot #^#–als Malkette,wie viele Faktoren,als Potenz?`
- B-639 (2): trigonometrische-funktionen-e3-k1-s2-v1, trigonometrische-funktionen-e3-k1-s2-v2 – `y=#·sin(x)–zwischen welchen Werten schwingt die Welle?`
- B-640 (5): trigonometrie-e2-k1-s1-v1, trigonometrie-e2-k1-s1-v2, trigonometrie-e2-k1-s1-v3, trigonometrie-e2-k1-s1-v4, trigonometrie-e2-k1-s1-v5 – `Gegenkathete # cm,Hypotenuse # cm–wie groß ist\alpha?`
- B-641 (3): zinsrechnung-e1-k1-s5-v1, zinsrechnung-e1-k1-s5-v2, zinsrechnung-e1-k1-s5-v3 – `Guthaben #€,Zinsen in einem Jahr #€–welcher Zinssatz?`
- B-642 (2): binomische-formeln-e2-k2-s4-v1, binomische-formeln-e2-k2-s4-v3 – `Welche Formel passt?Multipliziere aus:(x+#)\cdot(x-#)`
- B-643 (2): brueche-dezimalzahlen-e5-k2-s9-v3, brueche-dezimalzahlen-e5-k2-s9-v4 – `Ordne aufsteigend:-\frac{#}{#};#;-#;\sqrt{#}(P# # OS)`
- B-644 (2): normalverteilung-und-sigma-regeln-zone-f5-v1, normalverteilung-und-sigma-regeln-zone-f5-v2 – `X binomialverteilt mit n=# p=#:P(X=#)mit dem Rechner?`
- B-645 (2): pyramide-kegel-kugel-e3-k1-s2-v1, pyramide-kegel-kugel-e3-k1-s2-v2 – `Kugel:Durchmesser # cm–Volumen?Runde auf eine Stelle.`
- B-646 (2): pyramide-kegel-kugel-e3-k1-s9-v1, pyramide-kegel-kugel-e3-k1-s9-v3 – `Kugel:Oberfläche # cm²–Radius?Runde auf zwei Stellen.`
- B-647 (2): tangente-normale-schnittwinkel-e4-k1-s1-v3, tangente-normale-schnittwinkel-e4-k1-s1-v5 – `Eine Gerade hat den Steigungswinkel #^\circ–Steigung?`
- B-648 (3): brueche-dezimalzahlen-e3-k2-s1-v1, brueche-dezimalzahlen-e3-k2-s1-v2, brueche-dezimalzahlen-e3-k2-s1-v3 – `Gib einen Bruch zwischen\frac{#}{#}und\frac{#}{#}an.`
- B-649 (3): trigonometrie-e2-k1-s3-v1, trigonometrie-e2-k1-s3-v2, trigonometrie-e2-k1-s3-v3 – `Gegenkathete # cm,Ankathete # cm–wie groß ist\alpha?`
- B-650 (3): trigonometrie-e4-k1-s14-v1, trigonometrie-e4-k1-s14-v2, trigonometrie-e4-k1-s14-v3 – `Dreieck ABC:a=# cm,b=# cm,c=# cm.Wie groß ist\gamma?`
- B-651 (2): pythagoras-e1-k4-s1-v1, pythagoras-e1-k4-s1-v3 – `Katheten # m und # m–Hypotenuse c,sinnvoll gerundet?`
- B-652 (2): rationale-zahlen-e3-k1-s9-v1, rationale-zahlen-e3-k1-s9-v2 – `Berechne den Wert von #\cdot(x-#)für x=-#.(P# # FOR)`
- B-653 (2): rationale-zahlen-e4-k1-s2-v1, rationale-zahlen-e4-k1-s2-v3 – `Kontostand #€;Buchungen-#€,-#€,+#€–neuer Kontostand?`
- B-654 (5): quadratische-gleichungen-e4-k1-s1-v1, quadratische-gleichungen-e4-k1-s1-v2, quadratische-gleichungen-e4-k1-s1-v3, quadratische-gleichungen-e4-k1-s1-v4, quadratische-gleichungen-e4-k1-s1-v5 – `Das Quadrat einer Zahl x ist #:x^#=#.Welche Zahlen?`
- B-655 (4): prozentrechnung-e2-k2-s0-v1, prozentrechnung-e2-k2-s0-v2, prozentrechnung-e2-k2-s0-v3, prozentrechnung-e2-k2-s0-v4 – `In #-\%-Schritte einteilen.‖Grafik:\streifenleer[#]`
- B-656 (2): bruchrechnung-e4-k2-s9-v1, bruchrechnung-e4-k2-s9-v2 – `Welcher Wert ist am kleinsten:#;#;#^#;#\%?(P# # OS)`
- B-657 (2): pyramide-kegel-kugel-e3-k1-s5-v1, pyramide-kegel-kugel-e3-k1-s5-v3 – `Kugel:Radius # cm–Oberfläche?Runde auf eine Stelle.`
- B-658 (2): trigonometrie-zone-f6-v1, trigonometrie-zone-f6-v2 – `Katheten # cm und # cm–wie lang ist die Hypotenuse?`
- B-659 (3): trigonometrie-e2-k1-s2-v1, trigonometrie-e2-k1-s2-v2, trigonometrie-e2-k1-s2-v3 – `Ankathete # cm,Hypotenuse # cm–wie groß ist\alpha?`
- B-660 (2): lagebeziehungen-zone-f2-v1, lagebeziehungen-zone-f2-v2 – `g:\vec{x}=(#|#|#)+t\cdot(#|#|#)–der Punkt für t=#?`
- B-661 (4): bruchrechnung-e4-k1-s0-v1, bruchrechnung-e4-k1-s0-v2, bruchrechnung-e4-k1-s0-v3, bruchrechnung-e4-k1-s0-v4 – `#\cdot #–wie viele Kommastellen hat das Ergebnis?`
- B-662 (3): koerper-e2-k1-s4-v1, koerper-e2-k1-s4-v2, koerper-e2-k1-s4-v3 – `Quader:# cm lang,# cm breit,# cm hoch–Oberfläche?`
- B-663 (3): vektoren-und-rechenoperationen-e1-k2-s2-v1, vektoren-und-rechenoperationen-e1-k2-s2-v2, vektoren-und-rechenoperationen-e1-k2-s2-v3 – `\vec u=(#|#|#),\vec v=(#|#|#):welcher ist länger?`
- B-664 (3): zinsrechnung-e1-k2-s2-v1, zinsrechnung-e1-k2-s2-v2, zinsrechnung-e1-k2-s2-v3 – `#€zu #\%für # Tage,Bankjahr–wie viel Euro Zinsen?`
- B-665 (2): koerper-e2-k1-s6-v1, koerper-e2-k1-s6-v2 – `Quader:Volumen # cm³,Länge # cm,Breite # cm–Höhe?`
- B-666 (2): quadratische-funktionen-e4-k1-s4-v1, quadratische-funktionen-e4-k1-s4-v3 – `f(x)=x^#-#x+#–Nullstellen?Runde auf zwei Stellen.`
- B-667 (2): zinsrechnung-e1-k2-s4-v1, zinsrechnung-e1-k2-s4-v3 – `#€bringen in # Monaten #€Zinsen.Welcher Zinssatz?`
- B-668 (3): koerper-e2-k1-s1-v1, koerper-e2-k1-s1-v2, koerper-e2-k1-s1-v5 – `Quader:Länge # cm,Breite # cm,Höhe # cm–Volumen?`
- B-669 (2): lineare-gleichungen-e2-k3-s8-v5, lineare-gleichungen-e2-k3-s8-v6 – `#\cdot(x+#)=#–löse und mache die Probe.(P# # OS)`
- B-670 (3): lineare-funktionen-e3-k1-s0-v1, lineare-funktionen-e3-k1-s0-v2, lineare-funktionen-e3-k1-s0-v4 – `Einsetzen:Setze x=# in #x-# ein und rechne aus.`
- B-671 (2): potenzen-wurzeln-e3-k2-s5-v1, potenzen-wurzeln-e3-k2-s5-v3 – `\sqrt{#};#;\frac{#}{#};-#–aufsteigend geordnet?`
- B-672 (2): tangente-normale-schnittwinkel-e4-k1-s1-v1, tangente-normale-schnittwinkel-e4-k1-s1-v2 – `Eine Gerade hat die Steigung #–Steigungswinkel?`
- B-673 (2): bruchrechnung-e1-k1-s0-v1, bruchrechnung-e1-k1-s0-v2 – `\frac{#}{#}+\frac{#}{#}–sofort rechnen?\janein`
- B-674 (2): bruchrechnung-e1-k1-s0-v3, bruchrechnung-e1-k1-s0-v4 – `\frac{#}{#}-\frac{#}{#}–sofort rechnen?\janein`
- B-675 (2): hypergeometrische-verteilung-zone-f4-v1, hypergeometrische-verteilung-zone-f4-v2 – `Berechne und kürze:\frac{#}{#}\cdot\frac{#}{#}`
- B-676 (2): potenzen-wurzeln-e2-k1-s17-v1, potenzen-wurzeln-e2-k1-s17-v2 – `#=#\cdot #^{\square}–welche Hochzahl?(P# # OS)`
- B-677 (2): rationale-zahlen-e1-k1-s7-v1, rationale-zahlen-e1-k1-s7-v2 – `Ordne aufsteigend:-\frac{#}{#};#;-#;#(P# # OS)`
- B-678 (4): brueche-dezimalzahlen-e4-k1-s0-v1, brueche-dezimalzahlen-e4-k1-s0-v2, brueche-dezimalzahlen-e4-k1-s0-v3, brueche-dezimalzahlen-e4-k1-s0-v4 – `\frac{#}{#}–wie viele Stellen nach dem Komma?`
- B-679 (3): rationale-zahlen-e4-k1-s1-v1, rationale-zahlen-e4-k1-s1-v4, rationale-zahlen-e4-k1-s1-v5 – `Kontostand-#€,Einzahlung #€–neuer Kontostand?`
- B-680 (2): binomische-formeln-e1-k1-s5-v1, binomische-formeln-e1-k1-s5-v2 – `Schreib die vier Produkte hin:(x+#)\cdot(x+#)`
- B-681 (2): bruchrechnung-e5-k3-s1-v1, bruchrechnung-e5-k3-s1-v3 – `Kann #\cdot #=# stimmen?Prüfe mit Überschlag.`
- B-682 (2): pyramide-kegel-kugel-e1-k5-s1-v1, pyramide-kegel-kugel-e1-k5-s1-v4 – `Pyramide:Grundfläche # cm²,Höhe # cm–Volumen?`
- B-683 (2): reelle-zahlen-e1-k1-s6-v1, reelle-zahlen-e1-k1-s6-v2 – `\sqrt{#};#;#\frac{#}{#}–aufsteigend geordnet?`
- B-684 (2): koerper-e3-k1-s9-v1, koerper-e3-k1-s9-v2 – `Prisma:Volumen # cm³,Grundfläche # cm²–Höhe?`
- B-685 (2): pyramide-kegel-kugel-e1-k5-s12-v2, pyramide-kegel-kugel-e1-k5-s12-v3 – `Pyramide:Volumen # m³,Grundfläche # m²–Höhe?`
- B-686 (2): reelle-zahlen-e2-k1-s6-v2, reelle-zahlen-e2-k1-s6-v3 – `#^#:#^#–mit Gesetz oder ausrechnen?Ergebnis?`
- B-687 (2): spiegelung-zone-f2-v1, spiegelung-zone-f2-v2 – `Verbindungsvektor von A(#|#|#)nach B(#|#|#)?`
- B-688 (3): bruchrechnung-e3-k3-s2-v1, bruchrechnung-e3-k3-s2-v2, bruchrechnung-e3-k3-s2-v3 – `#:\frac{#}{#}–wie oft passt\frac{#}{#}in #?`
- B-689 (2): abstaende-e2-k1-s1-v2, abstaende-e2-k1-s1-v3 – `Abstand von P(#|#|#)zur Ebene E:#x+#y+#z=#?`
- B-690 (2): koerper-e3-k1-s1-v1, koerper-e3-k1-s1-v2 – `Prisma:Grundfläche # cm²,Höhe # cm–Volumen?`
- B-691 (2): lineare-gleichungen-e2-k3-s8-v1, lineare-gleichungen-e2-k3-s8-v2 – `#(x+#)=#–löse und mache die Probe.(P# # OS)`
- B-692 (2): potenzen-wurzeln-e1-k3-s4-v1, potenzen-wurzeln-e1-k3-s4-v2 – `#^#–wie viel?Rechne mit dem Taschenrechner.`
- B-693 (2): punkte-und-strecken-im-koordinatensystem-zone-f8-v1, punkte-und-strecken-im-koordinatensystem-zone-f8-v2 – `Ist(#|#|#)ein Vielfaches von(#|#|#)?Faktor?`
- B-694 (2): pyramide-kegel-kugel-e1-k5-s1-v2, pyramide-kegel-kugel-e1-k5-s1-v5 – `Pyramide:Grundfläche # m²,Höhe # m–Volumen?`
- B-695 (2): quadratische-funktionen-e3-k1-s1-v1, quadratische-funktionen-e3-k1-s1-v3 – `f(x)=x^#+#x+#–Schnittpunkt mit der y-Achse?`
- B-696 (2): quadratische-funktionen-e3-k1-s1-v2, quadratische-funktionen-e3-k1-s1-v4 – `f(x)=x^#-#x+#–Schnittpunkt mit der y-Achse?`
- B-697 (5): zinsrechnung-e1-k2-s1-v1, zinsrechnung-e1-k2-s1-v2, zinsrechnung-e1-k2-s1-v3, zinsrechnung-e1-k2-s1-v4, zinsrechnung-e1-k2-s1-v5 – `#€zu #\%für # Monate–wie viel Euro Zinsen?`
- B-698 (3): pythagoras-e1-k2-s5-v1, pythagoras-e1-k2-s5-v2, pythagoras-e1-k2-s5-v3 – `Katheten a=# m,b=# cm–Hypotenuse c in cm?`
- B-699 (3): reelle-zahlen-e3-k1-s9-v1, reelle-zahlen-e3-k1-s9-v2, reelle-zahlen-e3-k1-s9-v3 – `\frac{#}{\sqrt{#}}–mit rationalem Nenner?`
- B-700 (2): binomische-formeln-e2-k3-s1-v1, binomische-formeln-e2-k3-s1-v2 – `#^#–mit einer binomischen Formel im Kopf?`
- B-701 (2): trigonometrische-funktionen-e1-k1-s10-v1, trigonometrische-funktionen-e1-k1-s10-v2 – `\frac{#}{#}\pi ins Gradmaß–wie viel Grad?`
- B-702 (3): gleichungen-loesen-e2-k1-s1-v1, gleichungen-loesen-e2-k1-s1-v3, gleichungen-loesen-e2-k1-s1-v5 – `Löse:#e^{#x}-#=#.Runde auf zwei Stellen.`
- B-703 (2): potenzen-wurzeln-e1-k3-s0-v3, potenzen-wurzeln-e1-k3-s0-v4 – `#^#–was ist die Basis,was der Exponent?`
- B-704 (2): potenzen-wurzeln-e2-k1-s17-v3, potenzen-wurzeln-e2-k1-s17-v4 – `#\cdot #^{-#}–als Dezimalzahl?(P# # OS)`
- B-705 (2): quadratische-funktionen-e3-k1-s10-v1, quadratische-funktionen-e3-k1-s10-v2 – `Weise nach:(x+#)^#-#=x^#+#x+#.(P# # OS)`
- B-706 (5): trigonometrische-funktionen-e3-k1-s1-v1, trigonometrische-funktionen-e3-k1-s1-v2, trigonometrische-funktionen-e3-k1-s1-v3, trigonometrische-funktionen-e3-k1-s1-v4, trigonometrische-funktionen-e3-k1-s1-v5 – `y=#·sin(x)–wie groß ist die Amplitude?`
- B-707 (2): brueche-dezimalzahlen-e2-k1-s7-v1, brueche-dezimalzahlen-e2-k1-s7-v3 – `Schreibe\frac{#}{#}als gemischte Zahl.`
- B-708 (3): potenzen-wurzeln-e1-k3-s13-v1, potenzen-wurzeln-e1-k3-s13-v2, potenzen-wurzeln-e1-k3-s13-v3 – `#^{-#}–als Bruch und als Dezimalzahl?`
- B-709 (3): potenzen-wurzeln-e2-k1-s6-v1, potenzen-wurzeln-e2-k1-s6-v2, potenzen-wurzeln-e2-k1-s6-v3 – `#\cdot #^{#}–ausgeschrieben?(P# # OS)`
- B-710 (3): potenzen-wurzeln-e2-k1-s8-v1, potenzen-wurzeln-e2-k1-s8-v2, potenzen-wurzeln-e2-k1-s8-v3 – `#=#\cdot #^{\square}–welche Hochzahl?`
- B-711 (3): reelle-zahlen-e2-k1-s4-v1, reelle-zahlen-e2-k1-s4-v2, reelle-zahlen-e2-k1-s4-v3 – `(#^#)^#–als eine Potenz und als Zahl?`
- B-712 (2): koerper-e2-k3-s1-v1, koerper-e2-k3-s1-v2 – `Würfel mit # cm³ Volumen–Kantenlänge?`
- B-713 (2): prozentrechnung-e5-k2-s3-v1, prozentrechnung-e5-k2-s3-v3 – `von # auf #–um wie viel Prozent mehr?`
- B-714 (2): quadratische-gleichungen-e3-k3-s10-v1, quadratische-gleichungen-e3-k3-s10-v3 – `Probe:Ist x=-# Lösung von x^#-#x-#=#?`
- B-715 (3): potenzen-wurzeln-e1-k3-s8-v1, potenzen-wurzeln-e1-k3-s8-v2, potenzen-wurzeln-e1-k3-s8-v3 – `#^# oder #^#–welche Zahl ist größer?`
- B-716 (2): trigonometrische-funktionen-e3-k1-s5-v1, trigonometrische-funktionen-e3-k1-s5-v3 – `y=sin(#·x)–wie lang ist die Periode?`
- B-717 (2): pythagoras-e2-k2-s8-v1, pythagoras-e2-k2-s8-v2 – `Seiten # cm,# cm,# cm–rechtwinklig?`
- B-718 (5): potenzen-wurzeln-e3-k2-s1-v1, potenzen-wurzeln-e3-k2-s1-v2, potenzen-wurzeln-e3-k2-s1-v3, potenzen-wurzeln-e3-k2-s1-v4, potenzen-wurzeln-e3-k2-s1-v5 – `\sqrt{#}–wie viel?Mache die Probe.`
- B-719 (3): potenzen-wurzeln-e1-k3-s2-v1, potenzen-wurzeln-e1-k3-s2-v2, potenzen-wurzeln-e1-k3-s2-v3 – `#^# und #\cdot #–wie viel jeweils?`
- B-720 (2): bruchrechnung-e2-k3-s1-v1, bruchrechnung-e2-k3-s1-v3 – `Erst überschlagen,dann rechnen:#+#`
- B-721 (2): bruchrechnung-e5-k2-s1-v1, bruchrechnung-e5-k2-s1-v3 – `Rechne geschickt:#\cdot #+#\cdot #`
- B-722 (2): brueche-dezimalzahlen-e5-k2-s3-v1, brueche-dezimalzahlen-e5-k2-s3-v2 – `Ordne von klein nach groß:#;#;#;#.`
- B-723 (2): brueche-dezimalzahlen-e5-k3-s1-v1, brueche-dezimalzahlen-e5-k3-s1-v2 – `Gib eine Zahl zwischen # und # an.`
- B-724 (2): integrationsregeln-e1-k1-s1-v1, integrationsregeln-e1-k1-s1-v5 – `Gib eine Stammfunktion an:f(x)=x^#`
- B-725 (2): potenzen-wurzeln-e1-k3-s15-v7, potenzen-wurzeln-e1-k3-s15-v8 – `#^{-#}\square #–<,=oder>?(P# # OS)`
- B-726 (2): spiegelung-e1-k3-s1-v1, spiegelung-e1-k3-s1-v2 – `Spiegle P(#|#|#)am Punkt Q(#|#|#).`
- B-727 (4): potenzen-wurzeln-e1-k3-s15-v1, potenzen-wurzeln-e1-k3-s15-v2, potenzen-wurzeln-e1-k3-s15-v3, potenzen-wurzeln-e1-k3-s15-v4 – `#^x=#–welche Zahl ist x?(P# # OS)`
- B-728 (3): potenzen-wurzeln-e3-k2-s6-v1, potenzen-wurzeln-e3-k2-s6-v2, potenzen-wurzeln-e3-k2-s6-v3 – `\left(\sqrt{#}\right)^#–wie viel?`
- B-729 (3): reelle-zahlen-e3-k1-s3-v1, reelle-zahlen-e3-k1-s3-v2, reelle-zahlen-e3-k1-s3-v3 – `\sqrt{#}–teilweise Wurzel ziehen?`
- B-730 (2): binomische-formeln-e1-k1-s6-v1, binomische-formeln-e1-k1-s6-v3 – `Multipliziere aus:(x+#)\cdot(x+#)`
- B-731 (2): binomische-formeln-e1-k1-s8-v1, binomische-formeln-e1-k1-s8-v2 – `Multipliziere aus:(x-#)\cdot(x-#)`
- B-732 (3): brueche-dezimalzahlen-e5-k2-s6-v1, brueche-dezimalzahlen-e5-k2-s6-v2, brueche-dezimalzahlen-e5-k2-s6-v3 – `Setze<,=oder>ein:\frac{#}{#}__ #`
- B-733 (2): binomische-formeln-e2-k2-s7-v1, binomische-formeln-e2-k2-s7-v3 – `Multipliziere aus:#\cdot(x+#)^#`
- B-734 (2): flaechen-e4-k1-s3-v2, flaechen-e4-k1-s3-v3 – `Trapez,A=# m²,a=# m,c=# m–Höhe?`
- B-735 (2): lineare-gleichungen-e2-k2-s0-v1, lineare-gleichungen-e2-k2-s0-v3 – `#x+#=#–welche Umformung zuerst?`
- B-736 (3): potenzen-wurzeln-e2-k1-s10-v1, potenzen-wurzeln-e2-k1-s10-v2, potenzen-wurzeln-e2-k1-s10-v3 – `#\cdot #^{-#}–als Dezimalzahl?`
- B-737 (2): prozentrechnung-e5-k2-s5-v2, prozentrechnung-e5-k2-s5-v3 – `brutto(mit #\%Steuer)#€–netto?`
- B-738 (2): rationale-zahlen-e2-k3-s5-v1, rationale-zahlen-e2-k3-s5-v3 – `-# und #–wie weit auseinander?`
- B-739 (2): rationale-zahlen-e1-k1-s3-v1, rationale-zahlen-e1-k1-s3-v2 – `-# oder-#–welche ist kleiner?`
- B-740 (2): reelle-zahlen-e3-k1-s2-v1, reelle-zahlen-e3-k1-s2-v2 – `\sqrt{\frac{#}{#}}–als Bruch?`
- B-741 (2): zuordnungen-zone-f3-v1, zuordnungen-zone-f3-v2 – `# ist das Wievielfache von #?`
- B-742 (2): bruchrechnung-e3-k2-s4-v1, bruchrechnung-e3-k2-s4-v2 – `#\frac{#}{#}\cdot\frac{#}{#}`
- B-743 (2): grenzwerte-und-verhalten-im-unendlichen-zone-f3-v1, grenzwerte-und-verhalten-im-unendlichen-zone-f3-v2 – `y=#^x:Werte für x=# x=# x=#?`
- B-744 (3): quadratische-funktionen-e4-k1-s1-v1, quadratische-funktionen-e4-k1-s1-v3, quadratische-funktionen-e4-k1-s1-v5 – `f(x)=(x-#)^#-#–Nullstellen?`
- B-745 (2): potenzen-wurzeln-e3-k2-s4-v1, potenzen-wurzeln-e3-k2-s4-v3 – `\sqrt{#}\square #–<,=oder>?`
- B-746 (2): quadratische-funktionen-e4-k1-s1-v2, quadratische-funktionen-e4-k1-s1-v4 – `f(x)=(x+#)^#-#–Nullstellen?`
- B-747 (2): reelle-zahlen-e2-k1-s9-v1, reelle-zahlen-e2-k1-s9-v3 – `#x^#\cdot #x^#–vereinfacht?`
- B-748 (2): zinsrechnung-zone-f6-v1, zinsrechnung-zone-f6-v2 – `„plus #\%“–mal welche Zahl?`
- B-749 (3): potenzen-wurzeln-e1-k3-s1-v1, potenzen-wurzeln-e1-k3-s1-v2, potenzen-wurzeln-e1-k3-s1-v5 – `#^# als Malkette–wie viel?`
- B-750 (3): quadratische-funktionen-e3-k1-s3-v1, quadratische-funktionen-e3-k1-s3-v2, quadratische-funktionen-e3-k1-s3-v3 – `f(x)=(x-#)^#+#–Normalform?`
- B-751 (2): binomische-formeln-e2-k2-s5-v1, binomische-formeln-e2-k2-s5-v3 – `Multipliziere aus:(#x+#)^#`
- B-752 (2): quadratische-funktionen-e3-k1-s4-v2, quadratische-funktionen-e3-k1-s4-v3 – `f(x)=(x+#)^#-#–Normalform?`
- B-753 (5): binomische-formeln-e2-k2-s1-v1, binomische-formeln-e2-k2-s1-v2, binomische-formeln-e2-k2-s1-v3, binomische-formeln-e2-k2-s1-v4, binomische-formeln-e2-k2-s1-v5 – `Multipliziere aus:(x+#)^#`
- B-754 (3): binomische-formeln-e2-k2-s2-v1, binomische-formeln-e2-k2-s2-v2, binomische-formeln-e2-k2-s2-v3 – `Multipliziere aus:(x-#)^#`
- B-755 (3): brueche-dezimalzahlen-e5-k2-s8-v1, brueche-dezimalzahlen-e5-k2-s8-v2, brueche-dezimalzahlen-e5-k2-s8-v3 – `Setze<,=oder>ein:#^# __ #`
- B-756 (3): potenzen-wurzeln-e1-k3-s14-v1, potenzen-wurzeln-e1-k3-s14-v2, potenzen-wurzeln-e1-k3-s14-v3 – `#^{-#}\square #–<,=oder>?`
- B-757 (3): quadratische-gleichungen-e1-k2-s4-v1, quadratische-gleichungen-e1-k2-s4-v2, quadratische-gleichungen-e1-k2-s4-v3 – `x^#=-#–Lösungen?Begründe.`
- B-758 (2): bruchrechnung-e1-k3-s6-v1, bruchrechnung-e1-k3-s6-v3 – `#\frac{#}{#}+#\frac{#}{#}`
- B-759 (2): brueche-dezimalzahlen-e5-k2-s7-v1, brueche-dezimalzahlen-e5-k2-s7-v3 – `Setze<,=oder>ein:# __ #\%`
- B-760 (2): lineare-funktionen-zone-f4-v1, lineare-funktionen-zone-f4-v2 – `Rechne:\frac{#}{#}\cdot #`
- B-761 (5): quadratische-funktionen-e2-k1-s1-v1, quadratische-funktionen-e2-k1-s1-v2, quadratische-funktionen-e2-k1-s1-v3, quadratische-funktionen-e2-k1-s1-v4, quadratische-funktionen-e2-k1-s1-v5 – `f(x)=(x-#)^#+#–Scheitel?`
- B-762 (2): lineare-gleichungssysteme-e1-k1-s2-v1, lineare-gleichungssysteme-e1-k1-s2-v3 – `#x+y=#–nach y umstellen.`
- B-763 (2): potenzen-wurzeln-e1-k5-s1-v1, potenzen-wurzeln-e1-k5-s1-v3 – `#^#\square #\%–<,=oder>?`
- B-764 (2): rationale-zahlen-e1-k1-s2-v1, rationale-zahlen-e1-k1-s2-v3 – `-#–Gegenzahl und Betrag?`
- B-765 (3): potenzen-wurzeln-e3-k2-s7-v1, potenzen-wurzeln-e3-k2-s7-v2, potenzen-wurzeln-e3-k2-s7-v3 – `\sqrt{(-#)^#}–wie viel?`
- B-766 (3): rationale-zahlen-e3-k1-s5-v1, rationale-zahlen-e3-k1-s5-v2, rationale-zahlen-e3-k1-s5-v3 – `Berechne:(-#)^# und-#^#`
- B-767 (2): lineare-gleichungen-e1-k2-s4-v1, lineare-gleichungen-e1-k2-s4-v3 – `#x-#=#x+#–ist # Lösung?`
- B-768 (3): brueche-dezimalzahlen-e2-k1-s2-v1, brueche-dezimalzahlen-e2-k1-s2-v2, brueche-dezimalzahlen-e2-k1-s2-v3 – `Kürze\frac{#}{#}mit #.`
- B-769 (3): rationale-zahlen-e3-k1-s2-v1, rationale-zahlen-e3-k1-s2-v2, rationale-zahlen-e3-k1-s2-v3 – `Berechne:(-#)\cdot(-#)`
- B-770 (2): koerper-e2-k1-s3-v1, koerper-e2-k1-s3-v3 – `# cm³–wie viele Liter?`
- B-771 (3): binomische-formeln-e3-k1-s2-v1, binomische-formeln-e3-k1-s2-v2, binomische-formeln-e3-k1-s2-v3 – `Faktorisiere:x^#+#x+#`
- B-772 (3): binomische-formeln-e3-k1-s3-v1, binomische-formeln-e3-k1-s3-v2, binomische-formeln-e3-k1-s3-v3 – `Faktorisiere:x^#-#x+#`
- B-773 (2): potenzen-wurzeln-e2-k1-s1-v1, potenzen-wurzeln-e2-k1-s1-v2 – `#^{#}–ausgeschrieben?`
- B-774 (2): reelle-zahlen-e3-k1-s7-v1, reelle-zahlen-e3-k1-s7-v3 – `\sqrt[#]{#}–Ergebnis?`
- B-775 (3): prozentrechnung-e2-k4-s1-v1, prozentrechnung-e2-k4-s1-v2, prozentrechnung-e2-k4-s1-v3 – `#\%–Teil und Ganzes?`
- B-776 (2): rationale-zahlen-e3-k1-s1-v2, rationale-zahlen-e3-k1-s1-v4 – `Berechne:(-#)\cdot #`
- B-777 (3): potenzen-wurzeln-e2-k1-s1-v3, potenzen-wurzeln-e2-k1-s1-v4, potenzen-wurzeln-e2-k1-s1-v5 – `#–als Zehnerpotenz?`
- B-778 (2): prozentrechnung-e3-k1-s9-v3, prozentrechnung-e3-k1-s9-v4 – `#\%von #€(P# # FOR)`
- B-779 (2): rationale-zahlen-e3-k1-s1-v1, rationale-zahlen-e3-k1-s1-v3 – `Berechne:#\cdot(-#)`
- B-780 (5): binomische-formeln-e3-k1-s1-v1, binomische-formeln-e3-k1-s1-v2, binomische-formeln-e3-k1-s1-v3, binomische-formeln-e3-k1-s1-v4, binomische-formeln-e3-k1-s1-v5 – `Faktorisiere:x^#-#`
- B-781 (3): einheiten-e2-k1-s1-v1, einheiten-e2-k1-s1-v3, einheiten-e2-k1-s1-v5 – `# min–wie viele s?`
- B-782 (2): einheiten-e3-k1-s2-v1, einheiten-e3-k1-s2-v3 – `# m²–wie viel cm²?`
- B-783 (2): prozentrechnung-e3-k1-s9-v1, prozentrechnung-e3-k1-s9-v2 – `#\%von #€(P# # OS)`
- B-784 (2): pyramide-kegel-kugel-zone-f5-v1, pyramide-kegel-kugel-zone-f5-v2 – `Ein Drittel von #?`
- B-785 (2): rationale-zahlen-e1-k2-s1-v2, rationale-zahlen-e1-k2-s1-v3 – `Mitte von-# und-#?`
- B-786 (2): zinsrechnung-zone-f7-v1, zinsrechnung-zone-f7-v2 – `#^{#}–welche Zahl?`
- B-787 (2): einheiten-e1-k2-s1-v2, einheiten-e1-k2-s1-v5 – `# cm–wie viel mm?`
- B-788 (2): einheiten-e3-k1-s6-v1, einheiten-e3-k1-s6-v3 – `# l–wie viel dm³?`
- B-789 (2): lineare-gleichungen-e3-k1-s5-v1, lineare-gleichungen-e3-k1-s5-v2 – `\frac{x}{#}+#=x-#`
- B-790 (2): quadratische-gleichungen-e2-k1-s2-v1, quadratische-gleichungen-e2-k1-s2-v3 – `(x+#)\cdot(x-#)=#`
- B-791 (2): terme-zone-f4-v1, terme-zone-f4-v2 – `Rechne:#+#\cdot #`
- B-792 (2): einheiten-e1-k2-s1-v1, einheiten-e1-k2-s1-v4 – `# m–wie viel dm?`
- B-793 (2): einheiten-e1-k2-s4-v1, einheiten-e1-k2-s4-v3 – `# km–wie viel m?`
- B-794 (2): lineare-gleichungen-e2-k3-s4-v2, lineare-gleichungen-e2-k3-s4-v3 – `#x-#=#–mit Probe`
- B-795 (2): rationale-zahlen-e2-k3-s3-v2, rationale-zahlen-e2-k3-s3-v3 – `Berechne:-#-(-#)`
- B-796 (2): einheiten-e1-k2-s6-v1, einheiten-e1-k2-s6-v3 – `#€–wie viel ct?`
- B-797 (2): rationale-zahlen-e2-k3-s2-v1, rationale-zahlen-e2-k3-s2-v3 – `Berechne:#+(-#)`
- B-798 (3): bruchrechnung-e1-k4-s1-v1, bruchrechnung-e1-k4-s1-v2, bruchrechnung-e1-k4-s1-v3 – `#+\frac{#}{#}`
- B-799 (2): lineare-gleichungen-e2-k3-s6-v1, lineare-gleichungen-e2-k3-s6-v2 – `\frac{x}{#}=#`
- B-800 (2): quadratische-gleichungen-e2-k1-s3-v1, quadratische-gleichungen-e2-k1-s3-v3 – `x\cdot(x+#)=#`
- B-801 (2): reelle-zahlen-e3-k1-s11-v1, reelle-zahlen-e3-k1-s11-v3 – `x^#=#–Lösung?`
- B-802 (2): lineare-funktionen-zone-f5-v1, lineare-funktionen-zone-f5-v2 – `Löse:#=#x-#`
- B-803 (2): lineare-gleichungen-zone-f5-v1, lineare-gleichungen-zone-f5-v2 – `#\cdot(x+#)`
- B-804 (2): quadratische-gleichungen-e2-k1-s8-v1, quadratische-gleichungen-e2-k1-s8-v2 – `#x^#-#x=#`
- B-805 (3): quadratische-gleichungen-e1-k2-s7-v1, quadratische-gleichungen-e1-k2-s7-v2, quadratische-gleichungen-e1-k2-s7-v3 – `#x^#+#=#`
- B-806 (3): quadratische-gleichungen-e2-k1-s6-v1, quadratische-gleichungen-e2-k1-s6-v2, quadratische-gleichungen-e2-k1-s6-v3 – `x^#+#x=#`
- B-807 (3): quadratische-gleichungen-e2-k1-s7-v1, quadratische-gleichungen-e2-k1-s7-v2, quadratische-gleichungen-e2-k1-s7-v3 – `x^#-#x=#`
- B-808 (3): lineare-gleichungen-e2-k3-s1-v2, lineare-gleichungen-e2-k3-s1-v4, lineare-gleichungen-e2-k3-s1-v5 – `x-#=#`

## C Gleiches Ergebnis und gleiche Kontextwörter (mehr als drei Zeilen)

Davon mit mindestens zwei gemeinsamen Kontextwörtern: 0. Ein einzelnes Kontextwort (ein Name, ein Glücksrad) mit kleinem Ergebnis ist ein schwacher Befund.

- C-001 (über Einträge, 5 Zeilen, 1 Kontextwort): Ergebnis `3`, Kontext `Ben`: ableitungsregeln-e1-k4-s1-v2, kurvenuntersuchung-e4-k4-s1-v2, lagebeziehungen-e2-k2-s1-v3, symmetrie-abbildungen-e2-k6-s1-v3, zuordnungen-e1-k4-s1-v2  
  `Ich finde den Fehler: Zu $g(x) = \frac{1}{2}x^6 + 5x$ schreibt Ben $g'(x) = \frac{1}{2}x^5 + 5$.`
- C-002 (über Einträge, 5 Zeilen, 1 Kontextwort): Ergebnis `3`, Kontext `Tim`: abstaende-e4-k2-s1-v3, ebenen-e4-k3-s1-v3, funktionsscharen-und-ortskurven-e1-k2-s1-v1, lineare-gleichungssysteme-e1-k3-s3-v1, vektoren-und-rechenoperationen-e1-k3-s1-v2  
  `Finde den Fehler. Eine senkrechte Tafel hat die Oberkante DE mit D(3 | −4 | 5) und E(3 | 4 | 5), der Mast steht auf der z-Achse. Tim schreibt: „Abstand der Tafel zum Mast = Abstand von D zur z-Achse = …`
- C-003 (über Einträge, 4 Zeilen, 1 Kontextwort): Ergebnis `3`, Kontext `Paul`: ableitung-und-aenderungsrate-e2-k4-s1-v1, lineare-funktionen-e2-k7-s1-v1, lineare-gleichungen-e3-k3-s3-v1, symmetrie-abbildungen-e3-k4-s1-v2  
  `Für $g(x) = 3\mathrm{e}^x - 3$ soll $g'(0)$ berechnet werden. Paul rechnet $g(0) = 3 - 3 = 0$ und antwortet: $g'(0) = 0$. Finde den Fehler.`
- C-004 (über Einträge, 4 Zeilen, 1 Kontextwort): Ergebnis `3`, Kontext `Sara`: ebenen-e4-k3-s1-v2, kenngroessen-von-verteilungen-e3-k4-s1-v2, lineare-funktionen-e3-k5-s1-v1, tangente-normale-schnittwinkel-e2-k1-s6-v1  
  `Sara sagt: „$E\colon x - y + 2z = 1$ und $F\colon 3x - 3y + 6z = 3$ haben keine gemeinsamen Punkte, weil ihre Normalenvektoren Vielfache sind.“ Finde den Fehler.`
- C-005 (über Einträge, 4 Zeilen, 1 Kontextwort): Ergebnis `[1, 2]`, Kontext `glücksrad`: kenngroessen-von-verteilungen-e2-k2-s1-v2, wahrscheinlichkeit-e2-k2-s0-v4, wahrscheinlichkeit-e2-k3-s2-v2, zufallsgroessen-und-verteilungen-e1-k3-s1-v1  
  `Ein Glücksrad hat Felder mit den Zahlen 2 und 1; die 2 erscheint mit der Wahrscheinlichkeit $q$. Es wird zweimal gedreht; die Punktzahl ist das Produkt der beiden Zahlen. Im Mittel soll sie 2{,}25 bet …`

## D Personennamen und Sachkontexte

Personennamen: 71 verschiedene in 924 Zeilen (gezählt je Zeile). Die zehn häufigsten:

| Rang | Name | Zeilen |
|--:|---|--:|
| 1 | Tom | 74 |
| 2 | Mia | 72 |
| 3 | Ben | 69 |
| 4 | Tim | 68 |
| 5 | Lea | 59 |
| 6 | Jonas | 41 |
| 7 | Ole | 41 |
| 8 | Paul | 41 |
| 9 | Jan | 37 |
| 10 | Lena | 31 |

Sachkontexte (Wortliste KONTEXTE im Skript; eine Zeile kann mehrere haben):

| Sachkontext | Zeilen |
|---|--:|
| Geld und Einkauf | 688 |
| Garten, Bau und Wohnen | 568 |
| Glücksspiel und Zufallsgeräte | 488 |
| Wasser und Behälter | 389 |
| Verkehr und Fahrt | 295 |
| Karte und Gelände | 278 |
| Sport und Spiel | 206 |
| Umfrage und Medizin | 189 |
| Natur und Tiere | 182 |
| Zinsen und Konto | 168 |
| Essen und Kochen | 167 |
| Freizeit und Veranstaltung | 141 |
| Schule | 118 |
| Produktion und Qualität | 116 |
| Temperatur und Wetter | 112 |
| Wachstum und Bestand | 108 |
| Handy und Technik | 72 |
| Tarife und Gebühren | 49 |
| ohne Sachkontext (innermathematisch) | 10267 |

## E Länge der aufgabe (unter 20 oder über 600 Zeichen)

Kürzer als 20 Zeichen: 267 Zeilen.

- ableitung-und-aenderungsrate-zone-f5-v1 (19): `Löse: $4t - 10 = 6$`
- ableitung-und-aenderungsrate-zone-f5-v2 (18): `Löse: $6x + 9 = 0$`
- ableitungsregeln-zone-f3-v2 (17): `$0{,}25 \cdot 8$?`
- ableitungsregeln-zone-f5-v4 (16): `Lies $f'(2)$ ab.`
- binomische-formeln-zone-f5-v1 (19): `$\sqrt{64}$ – Wert?`
- binomische-formeln-zone-f5-v2 (13): `$9^2$ – Wert?`
- binomische-formeln-zone-f5-v3 (16): `$(-6)^2$ – Wert?`
- bruchrechnung-e1-k4-s1-v1 (17): `$3 + \frac{2}{5}$`
- bruchrechnung-e1-k4-s1-v2 (17): `$5 + \frac{1}{6}$`
- bruchrechnung-e1-k4-s1-v3 (17): `$2 + \frac{7}{4}$`
- bruchrechnung-e2-k1-s1-v1 (15): `$3{,}4 + 2{,}5$`
- bruchrechnung-e2-k1-s1-v2 (15): `$6{,}8 - 4{,}3$`
- bruchrechnung-e2-k1-s1-v3 (17): `$1{,}25 + 3{,}42$`
- bruchrechnung-e2-k1-s1-v4 (17): `$7{,}86 - 2{,}51$`
- bruchrechnung-e2-k1-s1-v5 (16): `$12{,}3 + 5{,}6$`
- bruchrechnung-e2-k1-s2-v1 (16): `$5{,}6 + 1{,}23$`
- bruchrechnung-e2-k1-s2-v2 (16): `$8{,}79 - 3{,}4$`
- bruchrechnung-e2-k1-s2-v3 (16): `$9{,}58 - 2{,}3$`
- bruchrechnung-e2-k1-s3-v1 (17): `$2{,}68 + 3{,}57$`
- bruchrechnung-e2-k1-s3-v2 (16): `$5{,}3 - 2{,}76$`
- bruchrechnung-e2-k1-s3-v3 (18): `$14{,}85 + 7{,}49$`
- bruchrechnung-e2-k2-s1-v1 (12): `$4 + 2{,}35$`
- bruchrechnung-e2-k2-s1-v2 (12): `$7 + 0{,}08$`
- bruchrechnung-e2-k2-s1-v3 (12): `$12 + 3{,}9$`
- bruchrechnung-e3-k3-s1-v1 (17): `$\frac{2}{3} : 5$`
- bruchrechnung-e3-k3-s1-v2 (17): `$\frac{5}{7} : 3$`
- bruchrechnung-e3-k3-s1-v3 (17): `$\frac{3}{8} : 4$`
- bruchrechnung-e3-k3-s1-v4 (17): `$\frac{7}{9} : 2$`
- bruchrechnung-e3-k3-s1-v5 (17): `$\frac{4}{5} : 3$`
- bruchrechnung-e3-k3-s4-v3 (18): `$\frac{8}{15} : 4$`
- bruchrechnung-e4-k2-s1-v1 (17): `$3{,}72 \cdot 10$`
- bruchrechnung-e4-k2-s1-v2 (18): `$0{,}58 \cdot 100$`
- bruchrechnung-e4-k2-s1-v3 (17): `$4{,}5 \cdot 100$`
- bruchrechnung-e4-k2-s1-v4 (18): `$0{,}093 \cdot 10$`
- bruchrechnung-e4-k2-s1-v5 (17): `$12{,}6 \cdot 10$`
- bruchrechnung-e4-k2-s2-v1 (13): `$45{,}7 : 10$`
- bruchrechnung-e4-k2-s2-v2 (11): `$236 : 100$`
- bruchrechnung-e4-k2-s2-v3 (13): `$8{,}4 : 100$`
- bruchrechnung-e4-k2-s3-v1 (15): `$2{,}3 \cdot 3$`
- bruchrechnung-e4-k2-s3-v2 (16): `$0{,}45 \cdot 6$`
- bruchrechnung-e4-k2-s3-v3 (16): `$3{,}15 \cdot 7$`
- bruchrechnung-e4-k2-s4-v1 (19): `$1{,}2 \cdot 0{,}7$`
- bruchrechnung-e4-k2-s4-v2 (19): `$2{,}5 \cdot 1{,}3$`
- bruchrechnung-e4-k2-s4-v3 (19): `$0{,}6 \cdot 4{,}1$`
- bruchrechnung-e4-k2-s5-v1 (19): `$0{,}2 \cdot 0{,}4$`
- bruchrechnung-e4-k2-s6-v1 (11): `$8{,}4 : 4$`
- bruchrechnung-e4-k2-s6-v2 (11): `$3{,}6 : 9$`
- bruchrechnung-e4-k2-s6-v3 (13): `$12{,}75 : 5$`
- bruchrechnung-e4-k2-s7-v1 (15): `$5{,}6 : 0{,}7$`
- bruchrechnung-e4-k2-s7-v2 (17): `$1{,}44 : 0{,}12$`
- bruchrechnung-e4-k2-s7-v3 (16): `$3{,}5 : 0{,}05$`
- bruchrechnung-e5-k1-s1-v1 (15): `$5 + 4 \cdot 6$`
- bruchrechnung-e5-k1-s1-v2 (13): `$30 - 18 : 3$`
- bruchrechnung-e5-k1-s1-v4 (12): `$48 : 6 - 5$`
- bruchrechnung-e5-k1-s1-v5 (16): `$40 - 3 \cdot 7$`
- bruchrechnung-e5-k1-s2-v3 (19): `$1{,}6 : 4 + 0{,}9$`
- bruchrechnung-zone-f5-v1 (11): `$7 \cdot 8$`
- bruchrechnung-zone-f5-v2 (8): `$63 : 9$`
- bruchrechnung-zone-f6-v2 (17): `$0{,}9$ als Bruch`
- brueche-dezimalzahlen-zone-f1-v1 (8): `$56 : 7$`
- brueche-dezimalzahlen-zone-f1-v2 (11): `$6 \cdot 8$`
- brueche-dezimalzahlen-zone-f1-v3 (11): `$4{,}2 : 6$`
- brueche-dezimalzahlen-zone-f6-v1 (8): `$84 : 4$`
- brueche-dezimalzahlen-zone-f6-v2 (8): `$75 : 5$`
- brueche-dezimalzahlen-zone-f6-v3 (7): `$7 : 4$`
- brueche-dezimalzahlen-zone-f6-v4 (7): `$2 : 5$`
- einheiten-zone-f3-v1 (16): `$0{,}3 \cdot 4$?`
- einheiten-zone-f3-v2 (12): `$2{,}4 : 3$?`
- einheiten-zone-f3-v3 (17): `$1{,}25 \cdot 6$?`
- einheiten-zone-f3-v4 (17): `$0{,}15 \cdot 8$?`
- einheiten-zone-f10-v2 (17): `Löse: $x : 5 = 9$`
- extremalprobleme-zone-f5-v1 (19): `Löse $x^2 - 9 = 0$.`
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
- koerper-zone-f5-v2 (17): `$7^2$ – wie viel?`
- kombinatorik-zone-f2-v1 (15): `Berechne $2^5$.`
- kombinatorik-zone-f2-v2 (15): `Berechne $3^4$.`
- kombinatorik-zone-f2-v4 (15): `Berechne $6^3$.`
- kreis-zone-f4-v1 (17): `$7^2$ – wie viel?`
- kurvenuntersuchung-zone-f2-v1 (19): `Löse $3x - 12 = 0$.`
- lagebeziehungen-zone-f4-v1 (19): `$3k + 6 = 0$ – $k$?`
- lagebeziehungen-zone-f5-v2 (19): `$3a - 6 = 0$ – $a$?`
- lineare-funktionen-zone-f3-v2 (19): `Rechne: $(-20) : 5$`
- lineare-funktionen-zone-f5-v1 (18): `Löse: $0 = 2x - 8$`
- lineare-funktionen-zone-f5-v2 (19): `Löse: $0 = 5x - 15$`
- lineare-gleichungen-e2-k3-s1-v1 (12): `$x + 8 = 15$`
- lineare-gleichungen-e2-k3-s1-v2 (12): `$x - 5 = 12$`
- lineare-gleichungen-e2-k3-s1-v3 (13): `$x + 16 = 25$`
- lineare-gleichungen-e2-k3-s1-v4 (12): `$x - 11 = 3$`
- lineare-gleichungen-e2-k3-s1-v5 (12): `$x - 7 = 30$`
- lineare-gleichungen-e2-k3-s2-v1 (9): `$6x = 54$`
- lineare-gleichungen-e2-k3-s2-v2 (11): `$x : 3 = 8$`
- lineare-gleichungen-e2-k3-s2-v3 (9): `$7x = 84$`
- lineare-gleichungen-e2-k3-s3-v1 (12): `$x + 12 = 5$`
- lineare-gleichungen-e2-k3-s3-v2 (10): `$4x = -36$`
- lineare-gleichungen-e2-k3-s3-v3 (12): `$x + 20 = 8$`
- lineare-gleichungen-e2-k3-s5-v1 (10): `$-3x = 18$`
- lineare-gleichungen-e2-k3-s5-v2 (11): `$-6x = -42$`
- lineare-gleichungen-e2-k3-s5-v3 (9): `$-x = 11$`
- lineare-gleichungen-e2-k3-s6-v1 (17): `$\frac{x}{4} = 6$`
- lineare-gleichungen-e2-k3-s6-v2 (17): `$\frac{x}{7} = 3$`
- lineare-gleichungen-e2-k3-s6-v3 (18): `$\frac{x}{2} = -9$`
- lineare-gleichungen-e3-k1-s1-v1 (14): `$5x = 2x + 12$`
- lineare-gleichungen-e3-k1-s1-v2 (14): `$7x = 3x + 20$`
- lineare-gleichungen-e3-k1-s1-v3 (13): `$6x = x + 30$`
- lineare-gleichungen-e3-k1-s1-v4 (14): `$9x = 4x + 35$`
- lineare-gleichungen-e3-k1-s1-v5 (13): `$4x = x + 24$`
- lineare-gleichungen-e3-k1-s2-v1 (18): `$6x + 5 = 2x + 25$`
- lineare-gleichungen-e3-k1-s2-v2 (17): `$5x - 3 = 2x + 9$`
- lineare-gleichungen-e3-k1-s2-v3 (18): `$8x - 4 = 3x + 26$`
- lineare-gleichungen-e3-k1-s4-v1 (19): `$3(x + 2) = x + 14$`
- lineare-gleichungen-e3-k1-s4-v2 (19): `$4(x - 1) = 2x + 6$`
- lineare-gleichungen-e3-k1-s4-v3 (18): `$20 - (x + 4) = x$`
- lineare-gleichungen-e3-k1-s6-v1 (19): `$2(x + 3) = 2x + 6$`
- lineare-gleichungen-e3-k1-s6-v2 (17): `$3x + 4 = 3x - 2$`
- lineare-gleichungen-zone-f1-v1 (15): `$2 + 4 \cdot 5$`
- lineare-gleichungen-zone-f1-v2 (15): `$6 \cdot 3 - 8$`
- lineare-gleichungen-zone-f1-v3 (19): `$4 \cdot (-3) + 20$`
- lineare-gleichungen-zone-f1-v4 (16): `$15 - 2 \cdot 6$`
- lineare-gleichungen-zone-f2-v1 (8): `$-3 + 8$`
- lineare-gleichungen-zone-f2-v2 (7): `$4 - 9$`
- lineare-gleichungen-zone-f2-v3 (16): `$-2{,}5 - 1{,}5$`
- lineare-gleichungen-zone-f2-v4 (12): `$-21 : (-7)$`
- lineare-gleichungen-zone-f2-v5 (10): `$6 - (-4)$`
- lineare-gleichungen-zone-f3-v1 (9): `$4x + 3x$`
- lineare-gleichungen-zone-f3-v2 (9): `$9x - 5x$`
- lineare-gleichungen-zone-f3-v3 (17): `$2x + 5 + 3x - 1$`
- lineare-gleichungen-zone-f3-v4 (13): `$5x + 2 + 3x$`
- lineare-gleichungen-zone-f3-v5 (8): `$x + 5x$`
- lineare-gleichungen-zone-f3-v6 (9): `$3x - 7x$`
- lineare-gleichungen-zone-f3-v8 (13): `$6x + 4 + 3x$`
- lineare-gleichungen-zone-f5-v1 (17): `$4 \cdot (x + 3)$`
- lineare-gleichungen-zone-f5-v2 (17): `$2 \cdot (x + 5)$`
- lineare-gleichungen-zone-f5-v3 (18): `$-3 \cdot (x - 4)$`
- lineare-gleichungen-zone-f5-v4 (14): `$12 - (x + 5)$`
- lineare-gleichungen-zone-f5-v5 (17): `$5 \cdot (x - 2)$`
- lineare-gleichungssysteme-zone-f4-v1 (13): `$2x + 5 = 17$`
- lineare-gleichungssysteme-zone-f4-v2 (13): `$4x = x + 15$`
- lineare-gleichungssysteme-zone-f4-v4 (17): `$7 - 2x = 3x - 8$`
- matrizen-und-uebergangsprozesse-zone-f6-v1 (19): `Berechne $0{,}5^3$.`
- orthogonalitaet-zone-f3-v1 (19): `Löse: $3t - 12 = 0$`
- orthogonalitaet-zone-f3-v2 (18): `Löse: $2a + 6 = 0$`
- potenzen-wurzeln-e1-k3-s3-v1 (18): `$14^2$ – wie viel?`
- potenzen-wurzeln-e1-k3-s3-v2 (18): `$17^2$ – wie viel?`
- potenzen-wurzeln-e1-k3-s3-v3 (17): `$9^3$ – wie viel?`
- potenzen-wurzeln-e1-k3-s6-v1 (18): `$-8^2$ – wie viel?`
- potenzen-wurzeln-e1-k3-s6-v2 (18): `$-5^4$ – wie viel?`
- potenzen-wurzeln-e1-k3-s6-v3 (18): `$-1^8$ – wie viel?`
- potenzen-wurzeln-e1-k6-s1-v1 (17): `$8^0$ – wie viel?`
- potenzen-wurzeln-zone-f3-v5 (18): `$-5^2$ – wie viel?`
- prozentrechnung-zone-f2-v2 (18): `$0{,}9$ als Bruch?`
- prozentrechnung-zone-f3-v1 (11): `$600 : 100$`
- prozentrechnung-zone-f3-v2 (16): `$0{,}1 \cdot 70$`
- prozentrechnung-zone-f3-v3 (17): `$0{,}15 \cdot 60$`
- prozentrechnung-zone-f3-v4 (10): `$45 : 100$`
- prozentrechnung-zone-f3-v5 (17): `$0{,}06 \cdot 50$`
- pyramide-kegel-kugel-zone-f4-v1 (17): `$3^3$ – wie viel?`
- pyramide-kegel-kugel-zone-f4-v4 (17): `$6^3$ – wie viel?`
- pythagoras-zone-f1-v1 (18): `$11^2$ – wie viel?`
- pythagoras-zone-f9-v2 (19): `$7$ m – die Hälfte?`
- quadratische-funktionen-zone-f1-v1 (17): `$6^2$ – wie viel?`
- quadratische-funktionen-zone-f1-v2 (17): `$9^2$ – wie viel?`
- quadratische-funktionen-zone-f5-v2 (18): `$x - 7 = 5$ – $x$?`
- quadratische-gleichungen-e1-k2-s1-v1 (8): `x^2 = 81`
- quadratische-gleichungen-e1-k2-s1-v2 (8): `x^2 = 25`
- quadratische-gleichungen-e1-k2-s1-v3 (9): `x^2 = 100`
- quadratische-gleichungen-e1-k2-s1-v4 (9): `x^2 = 169`
- quadratische-gleichungen-e1-k2-s1-v5 (9): `x^2 = 196`
- quadratische-gleichungen-e1-k2-s3-v1 (8): `x^2 = 13`
- quadratische-gleichungen-e1-k2-s3-v2 (7): `x^2 = 7`
- quadratische-gleichungen-e1-k2-s3-v3 (8): `x^2 = 30`
- quadratische-gleichungen-e1-k2-s5-v1 (9): `3x^2 = 75`
- quadratische-gleichungen-e1-k2-s5-v2 (13): `x^2 + 11 = 60`
- quadratische-gleichungen-e1-k2-s5-v3 (12): `2x^2 - 8 = 0`
- quadratische-gleichungen-e1-k2-s7-v1 (13): `2x^2 + 5 = 37`
- quadratische-gleichungen-e1-k2-s7-v2 (14): `3x^2 + 10 = 10`
- quadratische-gleichungen-e1-k2-s7-v3 (13): `5x^2 + 12 = 2`
- quadratische-gleichungen-e1-k2-s8-v1 (14): `(x - 6)^2 = 16`
- quadratische-gleichungen-e1-k2-s8-v2 (14): `(x - 5)^2 = 49`
- quadratische-gleichungen-e1-k2-s8-v3 (15): `(x - 1)^2 = 100`
- quadratische-gleichungen-e1-k2-s9-v1 (15): `(x + 10)^2 = 25`
- quadratische-gleichungen-e1-k2-s9-v2 (14): `(x + 5)^2 = 81`
- quadratische-gleichungen-e1-k2-s9-v3 (14): `(x + 1)^2 = 64`
- quadratische-gleichungen-e1-k2-s10-v1 (13): `(x - 9)^2 = 0`
- quadratische-gleichungen-e1-k2-s10-v2 (13): `(x + 5)^2 = 0`
- quadratische-gleichungen-e1-k2-s10-v3 (14): `(x + 12)^2 = 0`
- quadratische-gleichungen-e2-k1-s3-v1 (19): `x \cdot (x + 6) = 0`
- quadratische-gleichungen-e2-k1-s6-v1 (12): `x^2 + 9x = 0`
- quadratische-gleichungen-e2-k1-s6-v2 (13): `x^2 + 11x = 0`
- quadratische-gleichungen-e2-k1-s6-v3 (13): `x^2 + 12x = 0`
- quadratische-gleichungen-e2-k1-s7-v1 (12): `x^2 - 3x = 0`
- quadratische-gleichungen-e2-k1-s7-v2 (13): `x^2 - 10x = 0`
- quadratische-gleichungen-e2-k1-s7-v3 (12): `x^2 - 8x = 0`
- quadratische-gleichungen-e2-k1-s8-v1 (13): `2x^2 - 6x = 0`
- quadratische-gleichungen-e2-k1-s8-v2 (14): `4x^2 - 10x = 0`
- quadratische-gleichungen-e2-k1-s8-v3 (14): `2x^2 + 14x = 0`
- quadratische-gleichungen-e3-k3-s1-v1 (16): `x^2 + 6x + 8 = 0`
- quadratische-gleichungen-e3-k3-s1-v2 (18): `x^2 + 10x + 16 = 0`
- quadratische-gleichungen-e3-k3-s1-v3 (18): `x^2 + 12x + 20 = 0`
- quadratische-gleichungen-e3-k3-s1-v4 (18): `x^2 + 14x + 24 = 0`
- quadratische-gleichungen-e3-k3-s1-v5 (18): `x^2 + 10x + 21 = 0`
- quadratische-gleichungen-e3-k3-s2-v1 (17): `x^2 - 4x - 12 = 0`
- quadratische-gleichungen-e3-k3-s2-v2 (16): `x^2 + 2x - 8 = 0`
- quadratische-gleichungen-e3-k3-s2-v3 (18): `x^2 - 10x + 21 = 0`
- quadratische-gleichungen-e3-k3-s3-v1 (12): `x^2 + 5 = 6x`
- quadratische-gleichungen-e3-k3-s3-v2 (13): `x^2 = 4x + 21`
- quadratische-gleichungen-e3-k3-s4-v1 (19): `5x^2 - 20x + 15 = 0`
- quadratische-gleichungen-e3-k3-s4-v2 (18): `-x^2 + 8x - 12 = 0`
- quadratische-gleichungen-e3-k3-s4-v3 (19): `4x^2 + 16x - 20 = 0`
- quadratische-gleichungen-e3-k3-s5-v1 (16): `x^2 - 3x + 2 = 0`
- quadratische-gleichungen-e3-k3-s5-v2 (17): `x^2 + 5x - 14 = 0`
- quadratische-gleichungen-e3-k3-s5-v3 (17): `x^2 - 7x + 12 = 0`
- quadratische-gleichungen-e3-k3-s6-v1 (18): `x^2 - 10x + 25 = 0`
- quadratische-gleichungen-e3-k3-s6-v2 (16): `x^2 + 4x + 4 = 0`
- quadratische-gleichungen-e3-k3-s6-v3 (18): `x^2 + 16x + 64 = 0`
- quadratische-gleichungen-e3-k3-s7-v1 (16): `x^2 + 2x + 5 = 0`
- quadratische-gleichungen-e3-k3-s7-v2 (17): `x^2 - 8x + 17 = 0`
- quadratische-gleichungen-e3-k3-s7-v3 (16): `x^2 + 4x + 7 = 0`
- quadratische-gleichungen-e3-k3-s9-v1 (16): `x^2 - 6x + 4 = 0`
- quadratische-gleichungen-e3-k3-s9-v2 (18): `x^2 + 10x + 18 = 0`
- quadratische-gleichungen-e3-k3-s9-v3 (16): `x^2 - 2x - 2 = 0`
- quadratische-gleichungen-e3-k3-s11-v1 (19): `(x + 2)^2 = 5x + 10`
- quadratische-gleichungen-e3-k3-s11-v3 (18): `(x - 1)^2 = x + 19`
- quadratische-gleichungen-zone-f1-v1 (17): `$7^2$ – wie viel?`
- quadratische-gleichungen-zone-f3-v1 (10): `x + 8 = 15`
- quadratische-gleichungen-zone-f3-v2 (7): `3x = 27`
- quadratische-gleichungen-zone-f3-v3 (8): `-2x = 14`
- quadratische-gleichungen-zone-f3-v4 (16): `5x - 3 = 2x + 12`
- rationale-zahlen-e2-k3-s1-v1 (18): `Berechne: $-5 + 8$`
- rationale-zahlen-e2-k3-s1-v2 (18): `Berechne: $-3 + 2$`
- rationale-zahlen-e2-k3-s1-v3 (18): `Berechne: $-4 - 3$`
- rationale-zahlen-e2-k3-s1-v4 (18): `Berechne: $-9 + 4$`
- rationale-zahlen-zone-f1-v2 (18): `Berechne: $63 : 9$`
- rationale-zahlen-zone-f1-v3 (19): `Berechne: $120 : 8$`
- rationale-zahlen-zone-f1-v4 (19): `Berechne: $73 - 38$`
- rekonstruktion-von-bestaenden-zone-f4-v1 (15): `3\,m³ in Liter?`
- rekonstruktion-von-bestaenden-zone-f4-v3 (16): `72\,km/h in m/s?`
- terme-e2-k2-s0-v1 (14): `$a$ – Vorzahl?`
- terme-e2-k2-s0-v2 (15): `$-b$ – Vorzahl?`
- terme-e2-k2-s0-v3 (19): `$1{,}5z$ – Vorzahl?`
- terme-e2-k2-s0-v4 (16): `$-4w$ – Vorzahl?`
- terme-zone-f1-v1 (15): `Rechne: $4 - 9$`
- terme-zone-f1-v2 (16): `Rechne: $-3 + 8$`
- terme-zone-f1-v4 (16): `Rechne: $-6 - 4$`
- terme-zone-f1-v6 (16): `Rechne: $-8 - 6$`
- vektoren-und-rechenoperationen-zone-f4-v1 (15): `$3r = 12$: $r$?`
- vektoren-und-rechenoperationen-zone-f4-v2 (17): `$s - 2 = 7$: $s$?`
- vierfeldertafel-zone-f1-v1 (18): `$25\,\%$ von $80$?`
- winkel-dreiecke-zone-f3-v1 (13): `3 km in Meter`
- winkel-dreiecke-zone-f3-v3 (15): `2,4 km in Meter`
- zufallsexperimente-und-pfadregeln-zone-f8-v1 (18): `$6!$ (6 Fakultät)?`

Länger als 600 Zeichen: 2 Zeilen.

- matrizen-und-uebergangsprozesse-e4-k1-s7-v5 (664): `Ein Kanuverleih hat drei Stationen; die Verteilung geht von Abend zu Abend mit M über. d ist die Verteilung am Montagabend vor einer Entnahme: am Montagabend we …`
- matrizen-und-uebergangsprozesse-e4-k1-s7-v6 (647): `E-Roller stehen in drei Zonen; die Verteilung geht von Abend zu Abend mit M über. d ist die Verteilung am Freitagabend vor dem Einsammeln: am Freitagabend werde …`
