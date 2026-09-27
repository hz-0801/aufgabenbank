# Gegenlese: uneigentliche-integrale

Datum: 2026-09-27 21:46 UTC
Modell: Claude Code, Web-Sitzung (Modellkennung nach Sitzungsregel nicht im Repo)
Geprüfte Zeilen: 59 (zone 16, e1 23, e2 20)
Korrekturen: 0
Verfahren: jede Lösung aus der Aufgabe neu gerechnet
(Stammfunktionen, Grenzwerte, Restflächen mit sympy); bank.md nur
für die Felder.

## Befunde

(2) uneigentliche-integrale-e1-k2-s1-v3: Die Aufgabe hat keinen Satz mit dem Gesuchten („Die Fläche zwischen … rechts der y-Achse.“) – „Gesucht ist der Inhalt der Fläche zwischen …“.
(4) uneigentliche-integrale-e1-k1-s2-v3: Die Lösung führt w und E(w) ein, die Aufgabe spricht nur von t – „Energie bis zur Zeit w: E(w) = …“ voranstellen.
(4) uneigentliche-integrale-e2-k1-s2-v1: Die Schranke „kleiner als 4e^{-6}“ kommt aus der Stammfunktion, nicht aus dem Abfallen des Graphen (Höhe 0,01 mal unbegrenzte Breite gibt keine Schranke); die Sprosse verlangt die Begründung über das Abfallen – Schranke streichen oder mit Rechnung ausweisen: ∫_6^w 4e^{-x} dx = 4e^{-6} − 4e^{-w} < 4e^{-6}.
(4) uneigentliche-integrale-e2-k1-s2-v2: wie v1, Schranke 4e^{-5} ohne Herleitung – streichen oder ∫_{10}^w 2e^{-0,5x} dx = 4e^{-5} − 4e^{-0,5w} ausweisen.
(4) uneigentliche-integrale-e2-k1-s2-v3: wie v1, Schranke 3e^{-6} ohne Herleitung – streichen oder ∫_3^w 6e^{-2x} dx = 3e^{-6} − 3e^{-2w} ausweisen.
(6) uneigentliche-integrale-e2-k2-s1-v3: Jans Fehler (F mit f verwechselt) ist wirklich falsch, aber keins der beiden Muster im merkmal („als Gleichheit von Stammfunktionen gelesen, Restfläche für null erklärt“) – merkmal um „F mit f verwechselt“ ergänzen oder die Aufgabe auf eines der beiden Muster umstellen.

Punkte 1, 3 und 5 ohne Befund: alle Lösungen rechnerisch richtig,
pruef passt; jede Ankreuzaufgabe hat genau eine richtige Option
(Restflächen der Vorstufe nachgerechnet: 0,02 zu 2,98; 5,5 zu 4,5;
0,005 zu 2; divergent).

Sauber: 53 Zeilen ohne Befund
