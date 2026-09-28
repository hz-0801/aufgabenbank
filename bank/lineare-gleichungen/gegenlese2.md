# Zweitlesung lineare-gleichungen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 199
(zone 28, e1 48, e2 47, e3 36, e4 40)

Prüfung: Jede Zeile von zone.jsonl und e1–e4.jsonl gelesen (weg.jsonl
enthält Lösungswege, keine Aufgaben, und ist nicht Gegenstand).
Alle 42 Umformaufgaben (form gleichungsraster) mit sympy aus dem
Aufgabentext gelöst, einschließlich der Sonderfälle (jede Zahl /
keine Lösung); alle 11 Ankreuzzeilen (e1 4, e4 7) je Option mit sympy
gelöst bzw. eingesetzt – je genau eine Option richtig, loesung nennt
sie wortgleich. Die übrigen Rechen-, Einsetz-, Tabellen- und
Sachzeilen von Hand und per Skript nachgerechnet (Tabellenwerte,
Proben, Reste in den Sachtabellen, Tarifaufgaben). 184 Zeilen tragen
eine pruef-Zahl, alle stimmen mit der eigenen Rechnung und der
Ergebnisstelle der loesung; 15 Zeilen haben pruef "" (Begründen,
Formel umstellen, Deutung). 13 Fehler-finden-Zeilen (zone 1, e1–e4
je 3): der eingebaute Fehler ist jeweils wirklich falsch, die
Richtigrechnung stimmt. Originale gegen Abschnitt 2 der Mappe
gehalten (Verfahren, Falle, Form übernommen, Zahlen fremd). Keine
Aufgabe doppelt (aufgabe + grafik). bank-pruef.py: zone, e1–e4 je 0
Abweichungen, 0 Warnungen (die eine Abweichung betrifft nur den
Dateinamen weg.jsonl).

## Befunde

e2-k4-s4-v3: [E] Die loesung „die Gleichung verliert ihre Lösung“
ist schief: Nach dem Malnehmen mit 0 steht 0 = 0, das gilt für jede
Zahl – die Gleichung gewinnt Lösungen hinzu, die Umformung lässt sich
nicht rückgängig machen. – loesung etwa: „Dann steht 0 = 0 da, das
gilt für jede Zahl; die Lösung der ursprünglichen Gleichung ginge
verloren, weil man mal 0 nicht rückgängig machen kann.“

e2-k4-s4-v2: [M] Die Frage „warum zuerst −3 und nicht zuerst :5?“
ist eine Reihenfolgefrage (Kette Reihenfolge bestimmen), nicht das
Merkmal der Sprosse „warum die gleiche Umformung auf beiden Seiten
die Lösung nicht ändert“; zudem unterstellt die Frage eine Pflicht,
die die loesung selbst verneint („beides ist erlaubt“). – durch eine
Begründung zum Merkmal ersetzen, z. B. „Warum darf man bei
3x = 12 beide Seiten durch 3 teilen?“

Sauber: 197 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e2-k4-s4-v3: Die Lösung „die Gleichung verliert ihre Lösung“ ist schief; nach mal 0 steht 0 = 0, jede Zahl ist Lösung (beide als Lösungs- bzw. Eindeutigkeitsbefund, gleiche Richtung der Korrektur).
- e2-k4-s4-v2: Reihenfolgefrage statt Begründung zum Merkmal „gleiche Umformung auf beiden Seiten“; beide schlagen eine Begründungsfrage zum Teilen beider Seiten vor.

Nur Erstleser:
- e2-k1-s0-v2: bestätigt – bei x/3 ist auch 1/3 als „was steht bei x“ richtig (die Kette nennt die Sprosse „Vorzahl als Bruch“); die loesung sollte beides gelten lassen.
- e4-k2-s1-v1: bestätigt – A, a, b werden nicht erklärt, während v2 und v3 ihre Buchstaben erklären; bank.md verlangt die Erklärung.
- e2-k3-s7-v3: bestätigt, geringes Gewicht – die Variante verlangt nur eine einschrittige Gleichung und ist damit leichter als v1/v2; das Merkmal (Umkehrung) bleibt, der Anspruch nicht.
- e3-k2-s1-v1: bestätigt, geringes Gewicht – x nur links, v2/v3 x beidseitig; in einer Einheit „x beidseitig“ sollte auch v1 beidseitig sein.
- e4-k1-s6-v5 bis v8: bestätigt als Befund am Merkmal, nicht an den Aufgaben – die Zeilen folgen ihren Originalen (Gleichung angeben bzw. ankreuzen), das gemeinsame Merkmal „… und lösen“ passt auf sie nicht. Ich hatte den Punkt gesehen und verworfen, weil die Aufgaben originaltreu sind; die Merkmalsformulierung ist aber tatsächlich zu weit.
- e4-k1-s5-v1 bis v3: teilweise bestätigt – kein Verstoß gegen bank.md (Sachaufgabe: Ergebnis mit Zwischenergebnis, die eingesetzte Formel steht da), aber weil die Aufgabe ausdrücklich gegeben/gesucht/Formel/Rechnung verlangt, wäre die Formelzeile in der loesung sinnvoll.
- e1-k4-s2-v1: bestätigt – „Eine Probe macht sie nicht.“ verrät den Fehler, und die Aufgabe hat keine Rechnung in der Schreibform (\rechnung), wie 2.3 c sie für Fehler finden verlangt.

Nur Zweitleser: keine.

Widersprüche: keine. Die Entscheidungen des Erstlesers (pruef bei Ankreuzen mit Gleichungen, e1-k2-s5-v3/v4 mit positiver Lösung, Klammer in e2-k3-s8, x je Aufgabe erklärt) teile ich.
