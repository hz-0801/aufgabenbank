# Zweitlesung kenngroessen-von-verteilungen

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 186
(zone 26, e1 43, e2 50, e3 38, e4 29)

Prüfung: Jede Zeile wurde mit einem Skript ausgegeben und einzeln
gelesen. Für jede Zeile mit einer Zahl in pruef (152 Zeilen) wurde
die Lösung unabhängig aus dem Aufgabentext nachgerechnet
(Python/sympy im Scratchpad, nicht das Feld pruef ausgewertet):
Erwartungswerte aus Tabellen, Sachtexten und Pfaden (mit und ohne
Zurücklegen, hypergeometrisch mit comb), fehlende
Wahrscheinlichkeiten über die Summe 1, Fairness- und
Erwartungswertgleichungen (linear und quadratisch, mit Sieben der
Lösungen), Ungleichungen und Wertebereiche, Verhältnisse und
Maxima über k, Binomialformeln vorwärts und rückwärts
(p aus σ² = μ(1 − p), n = μ : p, n aus σ), Varianz-Summanden, Modus
der Binomialverteilung (höchste Säule) für jedes gezeichnete
Diagramm samt Prüfung auf Doppelmaxima, Säulenhöhen für die
Sigma-Intervalle, Rundung auf die Stellen der Lösung. 149 Zeilen
stimmen exakt; 2 Zeilen (e4-k1-s4-v1, e4-k1-s4-v2) summieren die im
Text gerundet vorgegebenen Säulenhöhen (0,384 statt exakt 0,383;
0,546 statt 0,5455), das ist gewollt; 3 Textzeilen (e1-k1-s5-v1,
e1-k1-s5-v2, e2-k8-s1-v2) tragen in pruef nur eine Kennzahl der
Deutung. 34 Zeilen ohne pruef (Ankreuzen, Begründen, Zeichnen)
wurden gelesen: bei jedem Ankreuzen ist genau eine Option richtig,
die Begründungen tragen den richtigen Kern. Alle 13
Fehler-finden-Zeilen: der Fehler reproduziert die vorgelegten
Zahlen, die Richtigrechnung stimmt (eine Ausnahme unten). Keine
unausgeglichenen $ oder Klammern, keine doppelte Aufgabe (aufgabe
und grafik zusammen). Nebenbei, kein Befund: dieselben
Zahlensätze kommen in verschiedener Richtung mehrfach vor
(e2-k1-s1-v1 und e2-k9-s1-v1: Einsatz 2 €, p = 0,25, a = 8;
e3-k1-s1-v1 und e3-k2-s1-v2: n = 100, p = 0,5, σ = 5; e3-k1-s1-v2
und e3-k4-s1-v2: n = 100, p = 0,1, σ = 3; e3-k2-s1-v1 und
e3-k4-s1-v1: p = 0,1, σ = 6, n = 400).
`python3 werkzeuge/bank-pruef.py kenngroessen-von-verteilungen`:
zone/e1/e2/e3/e4 je „Abweichungen 0, Warnungen 0", zuletzt
„Abweichungen: 0, Warnungen: 0".

## Befunde

e3-k3-s1-v1, e3-k3-s1-v2, e4-k1-s2-v1, e4-k1-s2-v2: zwei
Diagramme ohne Beschriftung, der Text sagt nicht, welches zu $X$
und welches zu $Y$ gehört; bei Vertauschung kippt das Verhältnis
(1,6 : 2,5 = 0,64 gegen 1,5625; 2,25 : 3 = 0,75 gegen 1,33) bzw.
die Zuordnung $p_X$/$p_Y$ – Vorschlag: „Das linke Diagramm gehört
zu $X$, das rechte zu $Y$" ergänzen, wie e4-k2-s3-v3 es tut
(e3-k3-s1-v3 hat Verhältnis 1, e4-k1-s2-v3 ist über n = 8 und
e4-k2-s1-v2 über Leas Satz eindeutig).
e2-k9-s1-v3: fraglich: Max' Rechnung enthält keinen falschen
Schritt, sie endet nur mit beiden Lösungen; „Finde den Fehler"
trifft eine Auslassung, keinen Fehler – Vorschlag: Max schließt
mit „also gibt es zwei mögliche Anzahlen" oder wählt $x = -8$.
e4-k2-s3-v1: fraglich: „auf zwei Stellen ablesen" verlangt vom
Stabdiagramm 0,02 statt 0,01 (exakt 0,0156) und 0,09 statt 0,10
(exakt 0,0938); das ist am Bild nicht sicher zu unterscheiden –
Vorschlag: p = 0,5 im Text nennen und die Werte berechnen lassen,
oder auf eine Stelle ablesen.

Sauber: 180 Zeilen ohne Befund

## Abgleich

Gezählt wird je Leser die Zeile im Befundteil (Erstleser: drei
Punkte mit je einer Zeile, 4 ids; Zweitleser: drei Zeilen, 6 ids).

- Beide Leser: keine gemeinsame id und kein gemeinsamer Befund.
- Nur Zweitleser: e3-k3-s1-v1, e3-k3-s1-v2, e4-k1-s2-v1,
  e4-k1-s2-v2 (Zuordnung X/Y der beiden Diagramme);
  e2-k9-s1-v3 (fraglich, kein falscher Schritt in Max' Rechnung);
  e4-k2-s3-v1 (fraglich, Ablesen auf zwei Stellen).
- Nur Erstleser: e4-k2-s2-v2 – nachgeprüft: bei zwei gleich hohen
  Säulen k und k + 1 ist μ = k + 1 − p, also nur für p = 0,5 genau
  in der Mitte (n = 9, p = 0,4: Säulen 3 und 4, μ = 3,6);
  Zustimmung, die Begründung sollte „zwischen" statt „genau
  zwischen" sagen oder p = 0,5 nennen. e4-k1-s1-v4, e4-k1-s1-v5 –
  nachgerechnet: 0,1795 gegen 0,1723 (n = 30) und 0,2059 gegen
  0,2003 (n = 40), die höchste Säule ist am Bild kaum von der
  Nachbarsäule zu trennen; Zustimmung, das habe ich übersehen.
  e4-k2-s1-v3 – nachgeprüft: 29,6 ≈ 29 und 34,4 ≈ 35 ist kein
  Runden, und richtiges Runden (30 und 34) träfe hier das
  Ergebnis; Zustimmung, der Vorschlag mit Faktor 0,65
  ([29,4; 34,6], gerundet 29 bis 35, richtig 30 bis 34) zeigt das
  Muster sauber.

Zahlen: Zweitleser 3 Befunde, Erstleser 3, gemeinsam 0, nur
Zweitleser 3. (Nach ids: Zweitleser 6, Erstleser 4, gemeinsam 0,
nur Zweitleser 6; zusammen 10 Zeilen mit Befund, 176 ohne.)
