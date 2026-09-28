# Zweitlesung wahrscheinlichkeit

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 244
(zone 22, e1 47, e2 70, e3 58, e4 47)

Prüfung: Jede Zeile wurde gelesen und die Lösung aus dem Aufgabentext
selbst nachgerechnet. Ein eigenes sympy-Skript hat 68 Zeilen unabhängig
modelliert: Abzählungen per Aufzählung (Permutationen, Würfelpaare,
Losnummern 201–700/201–800, Ziffernscheiben) und Pfadrechnungen mit
exakten Brüchen. Alle 68 stimmen mit pruef überein. Ein zweites Skript
prüft in allen Lösungen jede Gleichheitskette (Bruch = gekürzt =
Dezimal = Prozent, Toleranz bei ≈): kein Bruch in einer Kette. Die
übrigen Zeilen (Aufzählungen, Bäume, Begründungen) wurden von Hand
geprüft, auch jedes Feld in den \baumzwei- und \baumdrei-Grafiken gegen
die Anzahlen nach jeder Vorgeschichte. 193 Zeilen tragen eine
pruef-Zahl, alle stimmen (auch nach Rundung). 16 Ankreuzzeilen: jeweils
genau eine Option richtig, loesung wortgleich. 13 Fehler-finden-Zeilen:
Fehler ist jeweils echt falsch, Richtigrechnung stimmt. bank-pruef.py:
0 Abweichungen, 0 Warnungen.

## Befunde

e1-k1-s6-v3: [M] Münze und Glücksrad 1, 2, 3 haben keine gemeinsamen
Ergebnisse, es gibt kein vertauschtes Paar; das Merkmal „vertauschte
Paare zählen doppelt“ wird nicht geübt – zwei Geräte mit denselben
Ausgängen nehmen (zwei Glücksräder mit 1, 2, 3 oder zwei Münzen in
neuem Kontext).

e1-k3-s4-v1, e1-k3-s4-v2, e1-k3-s4-v3: [M] sprosse_text „Zählprinzip
„mal“ (Kombinationen aus zwei Auswahlen)“, alle drei Varianten haben
drei Auswahlen (Ringe; Sorte/Milch/Größe; Waffel/Sorte/Sahne) – eine
Variante auf zwei Auswahlen zurücknehmen oder den sprosse_text auf die
Typenzeile „Zählprinzip: Anzahl der Kombinationen als Produkt“ stellen.

e3-k4-s2-v3: [E] Kein Zufallsversuch genannt; die Lösung setzt „richtig
wären 2/5 und 3/5“, was nur bei Ziehen mit Zurücklegen (oder zwei
Geräten) folgt; welcher Punkt falsch ist, bleibt eindeutig – den
Versuch nennen („Glücksrad, zweimal gedreht“) oder den Richtigwert aus
der Lösung nehmen.

e4-k1-s1-v5, e4-k1-s5-v3: [E] Karten „nacheinander gezogen“, ohne zu
sagen, ob die Karte zurückkommt; bei Karten ist beides üblich, und die
Einheit übt gerade diese Unterscheidung – „ohne Zurücklegen“ oder „und
behält sie“ ergänzen.

Sauber: 237 Zeilen ohne Befund

## Abgleich

Beide Leser: e4-k1-s1-v5 und e4-k1-s5-v3 – bei den Karten fehlt die
Angabe „ohne Zurücklegen“.

Nur Erstleser:
- e1-k1-s6-v1 (zwei gleiche Spielsteine, 3 oder 4 Ergebnisse):
  nicht bestätigt als Befund – das Original 2017-OS-B1f stellt die
  Frage genauso („zwei gleiche Münzen gleichzeitig“, Lösung 4). Das
  Zusammenfassen zu 3 ist dort die gewollte Falle. Der Einwand gilt
  also dem Original; die Verfremdung übernimmt es richtig.
- e1-k1-s8-v1 (D liegt nicht auf der Geraden): bestätigt – liegt D
  auch darauf, gibt es 0 Dreiecke; v2 und v3 schließen das aus, v1
  nicht. Von mir übersehen.
- e4-k1-s1-v2 (Kekse „blind gegriffen“): bestätigt – derselbe Befund
  wie bei den Karten, von mir als noch eindeutig genug durchgelassen;
  zur Einheit, die genau diese Unterscheidung übt, passt die Ergänzung.
- e1-k2-s1-v3 („mindestens zweimal Rot“ unter der Sprosse „mindestens
  einmal“): bestätigt (M) – die Variante ändert die Schwelle, nicht nur
  Zahl und Kontext. Von mir übersehen.
- e2-k3-s6-v3 (60 Eier stehen direkt da): bestätigt (M) – das Merkmal
  „Gesamtzahl erst aus dem Text bilden“ trifft nicht zu. Die Falle des
  Originals 2016-OS-B1f (4/56) ist aber da; der Vorschlag „56 heile
  und 4 zerbrochene“ erfüllt beides.
- e1-k1-s8-v2 („20 Dreierauswahlen“ ohne Weg): nicht bestätigt als
  Befund – die Sprosse selbst verlangt „alle Dreierauswahlen“. v3 und
  das Original (10 aus 5 Punkten) setzen dasselbe Abzählen voraus. Ein
  Weg in der Lösung wäre eine Verbesserung, kein Fehler.
- e3-k3-s11-v1 und e3-k3-s11-v2 (Schreibweise „3 · …“): nicht bestätigt
  – die Rechnung ist richtig. Das Verfahren des Originals 2020-OS-K6c
  schreibt es genauso („3 · (1/6)² · 5/6“), und auf der Prüfungshöhe
  darf die Lösung bündeln.
- e1-k1-s8-v3 (Distraktoren ohne Fehlerbild): bestätigt als
  Qualitätsbefund, nicht als Ankreuzfehler – genau eine Option (9)
  ist richtig. 11 hat kein erkennbares Fehlerbild; 8 ist nur die Zahl
  des Originals. Die Hauptfalle (10, Kollineare mitgezählt) fehlt.

Nur Zweitleser:
- e1-k1-s6-v3: Münze und Glücksrad haben keine vertauschten Paare,
  das Merkmal wird nicht geübt.
- e1-k3-s4-v1, e1-k3-s4-v2, e1-k3-s4-v3: Sprossentext „aus zwei
  Auswahlen“, alle Varianten haben drei.
- e3-k4-s2-v3: Der Richtigwert „2/5 und 3/5“ folgt nicht aus dem Text,
  weil kein Versuch genannt ist.

Widersprüche: e1-k1-s6-v1 – der Erstleser meldet eine Mehrdeutigkeit,
der Zweitleser sieht die Formulierung durch das Original gedeckt.
Sonst keine: Beide finden alle Lösungen rechnerisch richtig und alle
eingebauten Fehler echt.
