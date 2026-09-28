# Zweitlesung binomische-formeln

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 170
(zone 30, e1 48, e2 50, e3 42)

Prüfung: Jede Zeile mit sympy nachgerechnet (Skript im Scratchpad,
nicht im Repo). 105 Zeilen mit Termumformung (Zusammenfassen,
Ausmultiplizieren, Faktorisieren, Zone-Rechnungen) generisch: der
Aufgabenterm ist zu jedem Glied der Gleichungskette in loesung
gleichwertig (simplify(a − b) == 0). Die übrigen 65 Zeilen einzeln:
Termwerte durch Einsetzen, Scheitel über die Ableitung, Gleichungen
der Prüfungshöhe e2 s10 durch Umformen, Lösungen von e3 s8 mit
solve, Kopfrechnen numerisch, bei Fehler-finden die falsche Zeile
als ungleich und die richtige als gleich, bei „kein Binom" mit
factor. Alle 170 Rechnungen stimmen. pruef je Zeile ausgewertet
und gegen die Lösungszahl gehalten; `python3 werkzeuge/bank-pruef.py
binomische-formeln` (v0.5): 0 Abweichungen, 0 Warnungen in allen
vier Dateien. Ankreuzen-Zeilen geprüft: 8 (e2 k1 s0, e3 k1 s0);
Fehler-finden-Zeilen geprüft: 10 (zone f4 v5, e1 k3 s1, e2 k4 s1,
e3 k2 s1). Dubletten: keine Aufgabe doppelt; Sperre gegen Kasten,
Typische Fehler, Originale und die Beispiele aus Voraussetzungen und
Erkennungsschritten von Hand gegengelesen, kein Treffer.

## Befunde

e3-k1-s0-v1, -v2, -v3: Die Aufgabe stellt zwei Fragen („Quadrate mit
Wurzeln? Passt das Mittelglied?"), hat aber nur ein `\janein`. Bei
v2 ($x^2 + 18x + 36$) ist die erste Frage mit ja, die zweite mit
nein zu beantworten; mit einem Kästchenpaar nicht eindeutig
ankreuzbar, und die loesung „nein – …" antwortet auf die zweite
Frage, während „nein" in v4 auf die erste antwortet. Dazu ist
„Quadrate mit Wurzeln?" kein verständlicher Fragesatz. – Vorschlag:
zwei Zeilen mit je einem `\janein`: „Sind das erste und das letzte
Glied Quadrate? \janein \\ Passt das Mittelglied? \janein", loesung
je Frage „ja"/„nein" mit Wurzeln und doppeltem Produkt.

e3-k1-s0-v4: antwort „Wurzeln __ und __", aber $20$ hat keine
ganzzahlige Wurzel; das Gerüst verlangt einen Eintrag, den es nicht
gibt. – Vorschlag: antwort „Wurzeln __ und __ (oder: keine)" oder die
Zeile mit dem Vorschlag oben umbauen.

zone-f1-v2, zone-f3-v2, zone-f7-v2: Die zwei Grundfall-Zeilen einer
Fertigkeit teilen einen merkmal-Text, der nur v1 beschreibt: f1-v2
($9 - 2 \cdot 4$) hat kein Produkt negativer Zahlen; f3-v2 ($9x - x$)
fasst mit Minus und Vorzahl eins zusammen, nicht „mit Plus"; f7-v2
($x^2 - 4x$) klammert die Variable aus, nicht eine „gemeinsame Zahl".
– Vorschlag: merkmal je Paar weiter fassen („Vorzeichenprodukt oder
Punkt vor Strich, je eins"; „gleichartige Glieder mit Plus oder
Minus, Vorzahl eins"; „gemeinsame Zahl oder Variable ausklammern")
oder v2 an das merkmal anpassen.

e1-k1-s4-v3: Sprosse „Zahl mal Klammer mit zwei Variablen", Aufgabe
$2x \cdot (x + 4y)$: der Faktor ist ein Term mit Variable, das
Ergebnis hat $x^2$ und $xy$. Die Variante ändert das Merkmal, nicht
nur die Zahlen. – Vorschlag: Zahl als Faktor, etwa
$5 \cdot (2a - 3b)$.

e2-k2-s6-v3: merkmal „b ist ein Glied mit y, Mittelglied mit xy",
Aufgabe $(x + 2y) \cdot (x - 2y)$ nach der dritten Formel hat kein
Mittelglied. – Vorschlag: merkmal „b ist ein Glied mit y" (ohne
Mittelglied) oder v3 als Quadrat, etwa $(3x + y)^2$.

e3-k2-s2-v3: Sprosse „Begründen, warum eine Summe zweier Quadrate
keine binomische Formel ist"; die Aufgabe fragt nach $-x^2 + 64$,
einer Differenz, zu der die dritte Formel passt. Die Variante kehrt
das Merkmal um (Ermessen: als Kontrollfrage sinnvoll, nach bank.md
aber nicht die Sprosse). – Vorschlag: eine Summe, etwa $4x^2 + 25$,
oder die Zeile behalten und im merkmal „auch Gegenprobe" nennen.

e3-k2-s1-v1, -v2: „Finde den Fehler und rechne richtig", aber die
richtige Antwort ist „lässt sich nicht faktorisieren"; es gibt keine
richtige Rechnung. – Vorschlag: „Finde den Fehler und begründe" für
diese beiden Muster.

e1-k3-s2-v3: „obwohl außen nur $x^2$ und eine Zahl stehen" – „außen"
ist ohne Erklärung nicht verständlich. – Vorschlag: „obwohl Erstes
mal Erstes nur $x^2$ und Letztes mal Letztes nur eine Zahl ergibt".

e2-k1-s0-v1, -v3: „Wenn ja: schreib es als Klammer mal Klammer", aber
antwort ist leer; kein Platz für den Term. – Vorschlag: antwort
„__ · __".

Häufung (kein Regelverstoß, Hinweis): Die Zahl 9/81 trägt elf
Aufgaben (e2-k1-s0-v1, e2-k2-s1-v2, e2-k2-s2-v1, e2-k2-s4-v1,
e2-k2-s8-v1, e2-k4-s2-v2, e3-k1-s1-v2, e3-k1-s3-v1, e3-k1-s7-v2,
e3-k1-s8-v2, e3-k2-s2-v2), die Zahl 4/16 dreizehn (u. a. e2-k2-s1-v1,
e2-k2-s7-v1, e2-k2-s7-v2, e2-k4-s1-v3, e2-k4-s2-v1, e3-k1-s0-v3,
e3-k1-s2-v1, e3-k1-s5-v3, e3-k1-s9-v1, e3-k1-s9-v2, e3-k2-s1-v2);
e2-k2-s9-v1 und e3-k1-s9-v3 sind Hin- und Rückweg derselben Zahlen
($(x + 1)^2 - 6$ ↔ $x^2 + 2x - 5$). – Vorschlag: bei der nächsten
Änderung Zahlen streuen (2, 5, 7, 10, 12, 13, 15).

Sauber: 155 Zeilen ohne Befund (15 Zeilen in 10 Befunden; die
Häufung zählt nicht als Befund)

## Abgleich

Beide Leser: e3-k1-s0-v2: zwei Fragen, ein \janein · e3-k1-s0-v4:
antwort „Wurzeln __ und __" nicht ausfüllbar · zone-f1-v2,
zone-f3-v2, zone-f7-v2: merkmal passt nur zu v1 · e1-k1-s4-v3:
Faktor 2x statt Zahl · e2-k2-s6-v3: dritte Formel ohne Mittelglied ·
e3-k2-s2-v3: Differenz statt Summe zweier Quadrate. (8 Zeilen)

Nur Erstleser: e2-k2-s9-v3: pruef −16 prüft den Zwischenwert, das
Ergebnis hat −10 – bestätigt (v1 und v2 derselben Sprosse haben
Zwischen- und Endwert gleich, nur v3 nicht; Lösung wie in e2 s10
umstellen: „$x^2 - 10x + 64$, aus …", pruef −10) · e1-k1-s1-v1, -v3,
-v5: Glied mit Vorzahl eins im Grundfall „lauter Plus" – bestätigt,
das ist das Merkmal von Sprosse 2 („Vorzahl eins mitzählen"), drei
von fünf Grundfall-Zeilen nehmen es vorweg · e3-k1-s10-v1, -v2, -v3:
Probe startet nicht beim faktorisierten Endergebnis – bestätigt,
die Prüfungshöhe verlangt „die Probe führen", v1 prüft nur das
Ausklammern, v2 und v3 nur den zweiten Schritt. (7 Zeilen)

Nur Zweitleser: e3-k1-s0-v1, -v3: dieselbe \janein-Doppelfrage wie
v2 und v4, dazu der Fragesatz „Quadrate mit Wurzeln?" · e3-k2-s1-v1,
-v2: „rechne richtig" ohne mögliche richtige Rechnung · e1-k3-s2-v3:
„außen" unerklärt · e2-k1-s0-v1, -v3: antwort leer trotz „schreib
es als Klammer mal Klammer" · Hinweis Häufung 9/81 und 4/16 sowie
Hin- und Rückweg e2-k2-s9-v1 ↔ e3-k1-s9-v3. (7 Zeilen und ein
Hinweis)

Widersprüche: keine in der Sache. Gewichtung bei e3-k2-s2-v3: der
Erstleser will die Aufgabe ersetzen, der Zweitleser hält sie als
Kontrollfrage für vertretbar, wenn das merkmal sie nennt; beide
sehen, dass sie nicht die Sprosse trifft.
