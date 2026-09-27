# Gegenlese: vierfeldertafel

Datum: 2026-09-27 21:51 UTC
Modell: Claude Code, Web-Sitzung (Modellkennung nach Sitzungsregel nicht im Repo)
Geprüfte Zeilen: 78 (zone 22, e1 33, e2 23)
Korrekturen: 17 (e1 15, e2 2)
Verfahren: jede Lösung aus der Aufgabe neu gerechnet; jede Tafel
(grafik, loesungsgrafik) nach der Lesart des Bausteins gegen den
Aufgabentext und auf Zeilen- und Spaltensummen geprüft; bank.md nur
für die Felder.

## Entscheidung

`\vierfeldertafel{A}{B}{…}` nimmt laut blattbau (mathblatt.sty,
Z. 1731; Anleitung_mathblatt.md, Z. 256) A als Spalte und B als
Zeile; die neun Werte stehen zeilenweise: Zeile B (A, nicht A,
Summe), Zeile nicht B, Summenzeile. Der Eintrag hat alle Tafeln
umgekehrt gefüllt (erstes Merkmal als Zeile). Gerendert zeigte die
Aufgabentafel die Ränder vertauscht zum Text, die Lösungstafel
falsche Felder, und in e2 k1-s4 passte die Lösung nicht mehr zur
gezeigten Tafel. Korrektur je Zeile: die beiden Merkmalsnamen im
Bausteinaufruf getauscht (grafik und loesungsgrafik), Werte, loesung
und pruef unverändert. Das ist die eindeutige Korrektur, die die
Rechnung des Autors erhält; eine Änderung der Lösung hätte in
e2 k1-s4-v1 das Urteil verschoben (22/51 ≈ 0,43 statt 27/51).
Danach stimmen alle Ränder mit dem Text, alle Summen gehen auf,
Prüfskript 0 Abweichungen.

## Befunde

(1) vierfeldertafel-e1-k2-s1-v1: Tafel transponiert (Z = 40 stand als Zeilenrand S) – korrigiert: {Z}{S} → {S}{Z} in grafik und loesungsgrafik.
(1) vierfeldertafel-e1-k2-s1-v2: Tafel transponiert – korrigiert: {E}{L} → {L}{E}.
(1) vierfeldertafel-e1-k2-s1-v3: Tafel transponiert – korrigiert: {M}{J} → {J}{M}.
(1) vierfeldertafel-e1-k2-s1-v4: Tafel transponiert – korrigiert: {W}{K} → {K}{W}.
(1) vierfeldertafel-e1-k2-s1-v5: Tafel transponiert – korrigiert: {J}{A} → {A}{J}.
(1) vierfeldertafel-e1-k2-s2-v1: Lösungstafel transponiert (Aufgabentafel leer) – korrigiert: {S}{R} → {R}{S}.
(1) vierfeldertafel-e1-k2-s2-v2: Tafel transponiert – korrigiert: {E}{V} → {V}{E}.
(1) vierfeldertafel-e1-k2-s2-v3: Tafel transponiert – korrigiert: {F}{S} → {S}{F}.
(1) vierfeldertafel-e1-k2-s3-v1: Tafel transponiert – korrigiert: {B}{L} → {L}{B}.
(1) vierfeldertafel-e1-k2-s3-v2: Tafel transponiert – korrigiert: {I}{V} → {V}{I}.
(1) vierfeldertafel-e1-k2-s3-v3: Tafel transponiert – korrigiert: {V}{D} → {D}{V}.
(1) vierfeldertafel-e1-k2-s4-v2: Tafel transponiert (Frauen 120 stand als Rand T) – korrigiert: {F}{T} → {T}{F}.
(1) vierfeldertafel-e1-k2-s4-v3: Tafel transponiert – korrigiert: {J}{S} → {S}{J}.
(1) vierfeldertafel-e1-k2-s6-v1: Termtafel transponiert (A∩notB zeigte p statt 5p an notA∩B) – korrigiert: {A}{B} → {B}{A}.
(1) vierfeldertafel-e1-k2-s6-v2: Termtafel transponiert – korrigiert: {A}{B} → {B}{A}.
(1) vierfeldertafel-e2-k1-s4-v1: Lösung passte nicht zur gerenderten Tafel (dort P(S ∩ nicht H) = 22 %, S ∪ nicht H = 73 %) – korrigiert: grafik {S}{H} → {H}{S}, damit gilt die Lösung (27 %, 51 %, 78 %).
(1) vierfeldertafel-e2-k1-s4-v2: wie v1 (gerendert A ∩ nicht B = 28 %, A ∪ nicht B = 62 %) – korrigiert: grafik {A}{B} → {B}{A}, damit gilt die Lösung (38 %, 34 %, 72 %).
(2) vierfeldertafel-e2-k1-s1-v4: Dass alle 1 000 Lose verkauft wurden und alle übrigen am Nachmittag, steht nicht im Text – „Alle 1 000 Lose wurden verkauft, 400 davon am Vormittag, der Rest am Nachmittag.“

Punkte 3 bis 6 ohne Befund: Varianten ändern nur das Merkmal, die
Lösungen sind in der Schreibform der Sprosse, jede Ankreuzaufgabe
hat genau eine richtige Option, jeder eingebaute Fehler ist falsch
und trifft das genannte Muster.

Hinweis über den Eintrag hinaus: `\vierfeldertafel` steht auch in
bedingte-wahrscheinlichkeit-und-bayes (zone, e1, e2) und
zufallsexperimente-und-pfadregeln (e1, e6); dort nicht geprüft.
unabhaengigkeit nutzt die richtige Lesart.

Sauber: 60 Zeilen ohne Befund
