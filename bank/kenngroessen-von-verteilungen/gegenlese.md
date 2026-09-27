# Gegenlese: kenngroessen-von-verteilungen

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 186 (zone 26, e1 43, e2 50, e3 38, e4 29)
Korrekturen: 0

Alle Lösungen nachgerechnet (Gleichungen, Binomialwerte mit
scipy.stats.binom, Lage der höchsten Säule jedes
\binomialverteilung-Diagramms, Kandidaten der Beschriftungsaufgaben
vollständig aufgezählt); keine rechnerische Abweichung.

## Punkt 1 – Lösung richtig

kenngroessen-von-verteilungen-e4-k2-s2-v2: „liegt das Maximum genau zwischen ihnen, und dort liegt auch der Erwartungswert“ stimmt nur für $p = 0{,}5$; allgemein liegt $\mu = np$ zwischen den Säulen, aber nicht in der Mitte (etwa $n = 9$, $p = 0{,}4$: gleich hohe Säulen bei 3 und 4, $\mu = 3{,}6$) – „der Erwartungswert liegt zwischen den beiden Säulen und ist nicht ganzzahlig; bei $p = 0{,}5$ genau in der Mitte“.

## Punkt 2 – eindeutig lösbar

kenngroessen-von-verteilungen-e4-k1-s1-v4, kenngroessen-von-verteilungen-e4-k1-s1-v5: Die höchste Säule ist am Diagramm kaum von der Nachbarsäule zu unterscheiden (n = 30, p = 0,2: 0,180 bei 6 gegen 0,172 bei 5; n = 40, p = 0,1: 0,206 bei 4 gegen 0,200 bei 3), und beide Nachbarn ergeben einen ganzzahligen Erwartungswert mit plausiblem $p$ – Parameter mit deutlicherem Maximum wählen, etwa n = 20, p = 0,3 bzw. n = 25, p = 0,2 (Verhältnis ≥ 1,1 wie in den übrigen Zeilen).

## Punkt 6 – Fehler finden

kenngroessen-von-verteilungen-e4-k2-s1-v3: Ben „rundet“ 29,6 auf 29 und 34,4 auf 35; das ist kein Runden, und gewöhnliches Runden (30 und 34) ergäbe hier zufällig das Richtige – das Muster „Grenzen gerundet statt eingeschlossene Werte“ zeigt sich nicht; Grenzen wählen, bei denen Runden nach außen führt, etwa $\mu = 32$, $\sigma = 4$, Faktor 0,65: $[29{,}4; 34{,}6]$, gerundet 29 bis 35, richtig 30 bis 34.

Sauber: 182 Zeilen ohne Befund
