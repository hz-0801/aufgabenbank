# Zweitlesung funktionsklassen-und-eigenschaften

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 296
(zone 28, e1 51, e2 48, e3 30, e4 39, e5 49, e6 51)

Prüfung: Jede Zeile aus Aufgabentext und Grafikaufruf selbst nachgerechnet; mit sympy geprüft wurden alle Polynomdivisionen und Faktorisierungen (e1 Prüfungshöhe, e2 S5, S7, S9), die Nullstellen der biquadratischen und quadratischen Aufgaben (e2 S4, Anwendung), die Extremstellen hinter den Ablesegrafiken (e1 K2, e6 S2, S3, S8, S10), die Ablesestellen der ksys-Funktionen (e1 S5, S9 v5/v6) und alle e- und ln-Werte mit Rundung (e1 S4, e3 S6, e3 Anwendung, e6 S4); der Rest im Kopf mit Gegenrechnung. Alle 218 Zeilen mit pruef-Zahl stimmen mit meiner Rechnung überein, keine Rundungsabweichung. Die 28 Ankreuzzeilen (zone f5, e1 S0, e2 S0, e4 S0, e5 S0, e6 S0, e6 S5, e6 K2 S3 v2) haben je genau eine richtige Option, auch bei den Graphenzuordnungen (jede Nebenoption scheitert an einem Merkmal); die 19 Fehler-finden-Zeilen enthalten jeweils einen echten Fehler, die Richtigrechnung stimmt. Grafiken passen zu den Werten (Scheitel, Extrempunkte und Ablesepunkte im Achsenbereich). `werkzeuge/bank-pruef.py`: 0 Abweichungen, 0 Warnungen. Hinweis ohne Kennzeichen (nicht gezählt): e3-k1-s6-v3 benutzt $G(x) = x - \mathrm{ln}(e^x + 1)$; die Mappe nennt den Term von F im Original 2024MerhoehtBAnalysisWTR1-1e nicht („F wie in d“), das Verfahren „ln(e^x + 1) gegen x abschätzen“ legt aber nahe, dass es genau dieser Term ist – dann wäre die Zeile nicht verfremdet (v4 ist es). Am Originalheft prüfen.

## Befunde

e5-k1-s2-v3: [E] $g(x) = x^2 - x$ geht aus $f(x) = x^2 + x$ nicht nur durch Spiegelung an der y-Achse hervor, sondern ebenso durch Verschiebung um $1$ nach rechts ($f(x - 1) = x^2 - x$); die Frage „wie geht … hervor?“ hat zwei richtige Antworten, die Lösung nennt eine – Frage auf die Spiegelung festlegen („Zeige: g entsteht durch Spiegelung an der y-Achse“) oder ein Termpaar ohne Parabelform wählen (etwa $x^3 + x^2$ und $-x^3 + x^2$).

e5-k2-s4-v1, e5-k2-s4-v2, e5-k2-s4-v3: [M] sprosse_text (Typ) verlangt „Periode … deuten und Stelle stärkster Zunahme am Graphen angeben“; die Aufgaben fragen Periode und größten/kleinsten Wert, keine Stelle stärkster Zunahme und keinen Graphen – je Aufgabe die Frage nach dem Zeitpunkt des stärksten Anstiegs ergänzen (mit Graph) oder merkmal und sprosse_text angleichen.

Sauber: 292 Zeilen ohne Befund

## Abgleich

Beide Leser: e5-k2-s4-v1 bis v3 – der Typ im sprosse_text verlangt die Stelle stärkster Zunahme am Graphen, die Aufgaben fragen stattdessen Extremwerte (Erstleser unter Punkt 3, Zweitleser als [M]).

Nur Erstleser: keine.

Nur Zweitleser: e5-k1-s2-v3 – $x^2 - x$ entsteht aus $x^2 + x$ auch durch Verschiebung um $1$ nach rechts, die Frage hat zwei richtige Antworten. Dazu der ungezählte Hinweis zu e3-k1-s6-v3 (möglicherweise der unverfremdete Term des Originals 2024MerhoehtBAnalysisWTR1-1e; die Mappe zeigt den Term nicht).

Widersprüche: e5-k1-s2-v3 – der Erstleser zählt die Zeile als sauber (Sauber 293), der Zweitleser nicht (Sauber 292); sonst keine.
