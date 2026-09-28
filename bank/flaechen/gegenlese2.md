# Zweitlesung flaechen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 244
(zone 31, e1 54, e2 36, e3 44, e4 38, e5 41)

Prüfung: Jede Zeile gelesen (Aufgabe, Antwortgerüst, Lösung, pruef,
Grafik). 193 Zeilen tragen eine pruef-Zahl; für 117 davon (alle mit
Dezimalzahlen, π, Umkehrungen, Sachkontext, Rundung) habe ich das
Ergebnis aus dem Aufgabentext mit sympy selbst gerechnet und mit
pruef verglichen – 117 von 117 stimmen, auch in der Rundung der
Lösung; die übrigen Ganzzahl-Einschritter von Hand nachgerechnet, alle
richtig. Geometrie der Grafiken nachgemessen: Seitenverhältnisse der
\dreieckrw (15-8-17, 24-7-25, 20-21-29), stumpfwinklige Dreiecke
(Höhenfußpunkt außerhalb, Verhältnis g : h), Viereck-Skizzen in e5,
rechte Winkel in zone-f6; Verträglichkeit der Angaben (Höhe ≤
Nachbarseite beim Parallelogramm, beide Höhen im Dreieck ergeben
dieselbe Fläche, Schenkel und Höhe im Trapez). 10 Ankreuzzeilen: je
genau eine Option richtig, Lösung wortgleich. 16 Fehler-finden-Zeilen:
der eingebaute Fehler ist jeweils falsch und rechnerisch so
ausgeführt, die Richtigrechnung stimmt. `bank-pruef.py flaechen`: 0
Abweichungen, 0 Warnungen.

## Befunde

e1-k2-s4-v2: [E] Die Skizze passt nicht zu den Maßen: die mit 31 m
beschriftete Seite CD ist kürzer gezeichnet (≈ 4,0) als die mit 24 m
beschriftete Seite AB (5,0) – Ecken so wählen, dass die Seiten grob
im Verhältnis 24 : 17 : 31 : 19 stehen, oder Beschriftung tauschen.

e1-k2-s8-v1, e1-k2-s8-v2, e1-k2-s8-v3, e3-k1-s6-v1, e3-k1-s6-v2,
e3-k1-s6-v3: [M] Sprosse „Term zu Figur“ (Katalog: „Term zu einer
beschrifteten Figur“, P10-Originale alle mit Bild), die Varianten
beschreiben die Figur nur in Worten, grafik leer – je eine beschriftete
Skizze ergänzen (\rechteck, \dreieck, \dreieckrw mit Variablen) und
den Text auf die Frage kürzen.

e4-k4-s2-v2: [E] Lösungstext sachlich ungenau: „Die Diagonalen teilen
es in acht Dreiecke“ – die Diagonalen teilen das Rechteck in vier
Rechtecke, erst die Drachenseiten halbieren jedes in zwei Dreiecke –
so umformulieren.

e5-k1-s0-v4: [E] Der Aufgabentext nennt die Teilflächen schon
(„unten rechteckig … oben sitzt ein Halbkreis“), zu erkennen bleibt
nichts – Figur als Skizze geben (Rechteck mit aufgesetztem Halbkreis)
und nur fragen, woraus die Glasfläche besteht.

e5-k2-s1-v2: [E] „Kann er den Flur ganz bedecken?“ ist ohne „in einem
Stück“ nicht eindeutig; zugeschnitten reicht der Rest (4,2 m² > 3,96
m²), die Lösung „nein“ gilt nur für ein Stück – „in einem Stück“
ergänzen.

Sauber: 234 Zeilen ohne Befund

## Abgleich

Beide Leser: e5-k2-s1-v2 – „ganz bedecken“ ohne „in einem Stück“,
zerschnitten reicht der Rest; beide schlagen „in einem Stück“ vor.
e4-k4-s2-v2 – „Die Diagonalen teilen es in acht Dreiecke“ ist
sachlich falsch; beide schlagen dieselbe Umformulierung vor (vier
Rechtecke, von den Drachenseiten halbiert).

Nur Erstleser: e4-k1-s0-v3 [A] – bestätigt: die Raute ist ein
Parallelogramm, nach der Legende ist $A = a \cdot h$ ebenso richtig
wie $A = \frac{e \cdot f}{2}$; damit sind zwei Optionen richtig. Ich
habe das übersehen; Vorschlag des Erstlesers (Option $a \cdot h$
durch $a \cdot c$ ersetzen) übernehmen. e1-k2-s8-v3 [E] – bestätigt,
aber leicht: „$x$ breit und 3 cm länger“ mischt einheitenlose
Variable und cm; mir aufgefallen, von mir als zu gering nicht
aufgenommen; „$x$ cm breit“ ist die einfache Lösung (gleiches Muster
in e3-k1-s6-v3, „Grundseite $y$ und Höhe $8$ cm“).

Nur Zweitleser: e1-k2-s4-v2 – Viereck-Skizze widerspricht den
Maßen (31-m-Seite kürzer gezeichnet als 24-m-Seite).
e1-k2-s8-v1–v3 und e3-k1-s6-v1–v3 – Sprosse „Term zu Figur“ ohne
Figur, die Figur steht nur im Text. e5-k1-s0-v4 – der Text verrät
die Teilflächen (Rechteck und Halbkreis), der Erkennungsschritt
entfällt.

Widersprüche: Punkt 3 (Sprosse und Merkmal) – der Erstleser meldet
keine Befunde, ich sehe bei den sechs Term-zu-Figur-Zeilen die
fehlende Figur als Merkmalsabweichung; Sachfrage, keine Rechenfrage.
Sonst keine.
