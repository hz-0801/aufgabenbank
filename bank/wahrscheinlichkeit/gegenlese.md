# Gegenlese: wahrscheinlichkeit

Datum: 2026-09-27 21:54 UTC
Modell: Claude Code, Web-Sitzung (Modellkennung nach Sitzungsregel nicht im Repo)
Geprüfte Zeilen: 244 (zone 22, e1 47, e2 70, e3 58, e4 47)
Korrekturen: 0
Verfahren: jede Lösung aus der Aufgabe neu gerechnet (Brüche,
Pfadregeln und Zählungen mit Python), jeder Baum mit Vorgabewerten
Ast für Ast nachgezählt; bank.md nur für die Felder.

## Befunde

(2) wahrscheinlichkeit-e1-k1-s6-v1: „Zwei gleiche Spielsteine … gleichzeitig geworfen – wie viele verschiedene Ergebnisse?“ lässt auch 3 zu (rot–rot, rot–blau, blau–blau als beobachtbare Ergebnisse); die Lösung 4 verlangt unterscheidbare Steine – „Ein Stein ist markiert“ ergänzen oder nach gleich wahrscheinlichen Ergebnissen fragen.
(2) wahrscheinlichkeit-e1-k1-s8-v1: Dass D nicht auf der Geraden durch A, B, C liegt, steht nicht da (v2 und v3 sagen es) – „D liegt nicht auf dieser Geraden“ ergänzen.
(2) wahrscheinlichkeit-e4-k1-s1-v2: „blind gegriffen“ sagt nicht, dass der erste Keks nicht zurückkommt – „… und nicht zurückgelegt“ ergänzen.
(2) wahrscheinlichkeit-e4-k1-s1-v5: „nacheinander gezogen“ ohne Angabe zum Zurücklegen – „ohne Zurücklegen“ ergänzen.
(2) wahrscheinlichkeit-e4-k1-s5-v3: „nacheinander gezogen“ ohne Angabe zum Zurücklegen – „ohne Zurücklegen“ ergänzen.
(3) wahrscheinlichkeit-e1-k2-s1-v3: Sprosse „mindestens einmal …“, gefragt ist „mindestens zweimal Rot“ – auf „mindestens einmal“ umstellen oder als eigene Sprosse führen.
(3) wahrscheinlichkeit-e2-k3-s6-v3: Merkmal „Gesamtzahl erst aus dem Text bilden“ fehlt, die 60 Eier stehen direkt da – Gesamtzahl aus Teilen geben (etwa 56 heile und 4 zerbrochene Eier).
(4) wahrscheinlichkeit-e1-k1-s8-v2: „20 Dreierauswahlen“ ohne Weg; die Kette kennt bis dahin nur geordnete Produkte (s4), nicht das Teilen durch die Reihenfolgen – den Weg zeigen (6 · 5 · 4 : 6 = 20 oder geordnete Liste) oder mit fünf Punkten arbeiten.
(4) wahrscheinlichkeit-e3-k3-s11-v1: „3 · ¼ · ¼ · ¾“ bündelt drei gleich wahrscheinliche Pfade; die Kette addiert bis dahin nur einzeln (s4, s5) – die drei Pfade einzeln schreiben oder „drei Pfade mit je …“ voranstellen.
(4) wahrscheinlichkeit-e3-k3-s11-v2: wie v1, „3 · ⅓ · ⅓ · ⅔“ ohne Hinweis auf die drei Pfade – wie v1.
(5) wahrscheinlichkeit-e1-k1-s8-v3: Distraktoren 8 und 11 haben kein erkennbares Fehlerbild (10 fehlt nach stand.md, Entscheidung 7, als Kastenzahl) – etwa 7 (drei Auswahlen gestrichen statt einer) und 60 (geordnet 5 · 4 · 3) nehmen.

Punkte 1 und 6 ohne Befund: alle Lösungen rechnerisch richtig, pruef
passt; jeder eingebaute Fehler ist falsch und trifft das genannte
Muster.

Sauber: 233 Zeilen ohne Befund
