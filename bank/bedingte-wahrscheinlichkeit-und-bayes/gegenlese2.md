# Zweitlesung bedingte-wahrscheinlichkeit-und-bayes

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 115 (zone 27, e1 27,
e2 32, e3 29)

Prüfung: Jede Zeile gelesen; jede Lösung unabhängig nachgerechnet
(alle Quotienten Feld durch Rand, alle Bayes-Brüche, die Terme mit
Parameter samt Proben, die Ungleichungen in e3-k1-s5 und e3-k2-s3
von Hand aufgelöst, r = 7 und n = 14 in e2-k1-s5 aus den Termen
zurückgerechnet); alle 13 Vierfeldertafeln nach der Konvention der
Bausteine (Zeilen B, nicht B, Summe; Spalten A, nicht A, Summe)
auf Zeilen- und Spaltensummen und auf die abgelesenen Felder
geprüft – alle stimmen; die Bäume (\baumzwei) gegen die Pfade der
Lösungen; die Graphen in e3-k1-s3 an beiden Rändern ausgerechnet
(A: 1 → 0,18; C: 0 → 0,69; B: 1 → 0,19), die Ablesestellen in
e3-k1-s4 exakt (a = 0,5, p = 0,9, x = 0,15). Ankreuzen: in allen
12 Zeilen genau eine Option richtig. Fehler finden: in allen 10
Zeilen ist der eingebaute Fehler wirklich falsch (Lisas
Zahlenwerte 0,375 und 0,545 stimmen, ihr Fehler ist der
Beweisgang). Die Originale in Abschnitt 2 der Mappe mit den
Aufgaben verglichen: Kontexte und Zahlen sind gewechselt.
`python3 werkzeuge/bank-pruef.py bedingte-wahrscheinlichkeit-und-bayes`:
0 Abweichungen, 0 Warnungen.

## Befunde

e1-k1-s1-v5: Das richtige Ergebnis $\frac{0{,}14}{0{,}4} = 0{,}35$
ist zugleich der im Text genannte Anteil „35 % im Fahrdienst" –
Fahrdienst und Frau sind in diesen Zahlen unabhängig. Wer den
Anteil nur abliest statt zu teilen, hat die richtige Zahl; die
Zeile prüft den Grundfall damit nicht (im Original 2023-bebb-gk
ist 15/72 ≈ 0,21 ≠ 0,25, dort tritt das nicht auf). – Vorschlag:
„12 % der Beschäftigten sind Frauen und arbeiten im Fahrdienst"
→ 0,3; pruef `0.12/0.4`.

e1-k1-s0-v1: „der Anteil der Mädchen unter den Vereinsmitgliedern,
die Fußball spielen" – der Relativsatz kann sich auf die Mädchen
beziehen (dann wäre durch alle Mitglieder zu teilen) oder auf die
Mitglieder (gemeint). Die Lösung setzt die zweite Lesart voraus. –
Vorschlag: „Unter den Fußball spielenden Vereinsmitgliedern:
Anteil der Mädchen."

e3-k1-s2-v3: „Weiterhin sind 60 % der Besucher …" – „Weiterhin"
verweist auf einen Vortext („ein Jahr später" im Original), den
die Zeile nicht hat. – Vorschlag: „Weiterhin" streichen: „60 % der
Besucher eines Museums sind Erwachsene …; der Anteil a … ist seit
dem letzten Jahr gestiegen."

e2-k1-s4-v3: Die Figur „Frage A: verlassen? / Frage B: bleiben?,
Ja-Antwort, gesucht: will verlassen" ist die des Originals
2021MgrundlegendBStochastikWTR3-1g; gewechselt sind Zahlen (70/30
→ 90/10) und Verein statt Unternehmen. Als Verfremdung knapp, aber
vertretbar (gleiche Falle ist verlangt). – Vorschlag: hinnehmen.

Sauber: 111 Zeilen ohne Befund

## Abgleich

Beide Leser: e3-k1-s2-v3 („Weiterhin" ohne Vortext).

Nur Zweitleser: e1-k1-s1-v5 (richtiges Ergebnis 0,35 fällt mit
dem genannten Randanteil zusammen); e1-k1-s0-v1 (Relativsatz
zweideutig); e2-k1-s4-v3 (Figur des Originals, knapp verfremdet).

Nur Erstleser: e3-k2-s3-v1/v2 – die Höchstwerte sind aufgerundet
(w ≤ 0,0096 gibt 0,4999 < 0,5; k ≤ 0,0066 gibt 1,0001 % > 1 %),
bei einer oberen Schranke ist abzurunden. Richtig, und der
gewichtigste Befund des Eintrags: ich habe die Ungleichungen
aufgelöst (w ≤ 0,009596, k ≤ 0,006599), die Rundungsrichtung in
der Lösung aber nicht geprüft – in e3-k1-s5 (untere Schranke,
aufgerundet) stimmt sie, in e3-k2-s3 nicht. Ferner: e1-k2-s2-v3
(Gleichheit auch bei P(A ∩ B) = 0 – richtig, klein); e2-k2-s3-v1
(Ränder fehlen in der Lösung, die Lösungsgrafik hat sie –
richtig); zone-f5-v3 (0,8 zwischen den Gitterlinien – richtig);
zone-f2-v2 und zone-f5-v2 (Grundfall greift dem Fallstrick vor –
richtig, ein Sprossenbefund); e3-k1-s1-v5 (kein Bayes-Baum mit
Parameter, sondern Gegenereignis und Schnitt, anderes Merkmal –
richtig; ich habe die Rechnung geprüft und das Merkmal
durchgelassen).

Widerspruch: keiner. Zusammen: 3 Zeilen nur Zweitleser, 9 nur
Erstleser, 1 gemeinsam; 102 Zeilen bei beiden ohne Befund.
