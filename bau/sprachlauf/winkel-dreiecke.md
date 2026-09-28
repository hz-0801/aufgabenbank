# Sprachlauf winkel-dreiecke

Stand 2026-09-28 (Sprachlauf Gruppe 3). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 214afea. Nur das Feld aufgabe ist geändert;
`python3 werkzeuge/bank-pruef.py winkel-dreiecke`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 23 | 27 | 50 |
| e2.jsonl | 40 | 13 | 53 |
| e3.jsonl | 21 | 35 | 56 |
| e4.jsonl | 33 | 17 | 50 |
| e5.jsonl | 36 | 6 | 42 |
| zone.jsonl | 12 | 10 | 22 |
| gesamt | 165 | 108 | 273 |

Geänderte Sprossen: 62. Die 10 Beispiele sind je Sprosse die erste
geänderte Zeile, gleichmäßig über die Sprossen verteilt (Zone zuerst).

## 10 Beispiele vorher/nachher

1. `winkel-dreiecke-zone-f2-v1` – Addieren und Subtrahieren im Bereich bis zum Vollwinkel, auc

   vorher: $38^\circ + 29^\circ$

   nachher: Berechne. $38^\circ + 29^\circ$

2. `winkel-dreiecke-zone-f4-v3` – Vierecksarten kennen

   vorher: Welche Seiten des Vierecks sind parallel? Wie heißt das Viereck?

   nachher: Die Figur zeigt ein Viereck. Welche Seiten des Vierecks sind parallel? Wie heißt das Viereck?

3. `winkel-dreiecke-e1-k3-s1-v1` – Winkel schätzen (Viertel-, halber, Dreiviertel-Rechter)

   vorher: Schätze, ohne zu messen: Wie groß ist α im Vergleich zu einem rechten Winkel? \\ \kreuz{ein Viertel} \\ \kreuz{die Hälfte} \\ \kreuz{drei Viertel}

   nachher: Die Figur zeigt einen Winkel α. Vergleiche α ohne Messen mit einem rechten Winkel. Kreuze an, welcher Teil eines rechten Winkels α ist. \\ \kreuz{ein Viertel} \\ \kreuz{die Hälfte} \\ \kreuz{drei Viertel}

4. `winkel-dreiecke-e2-k2-s4-v1` – Teilwinkel an der Kreuzung (Scheitelwinkel minus Teil)

   vorher: Die Geraden g und h schneiden sich; zwischen ihnen liegt $\alpha = 64^\circ$. Eine dritte Gerade durch den Schnittpunkt teilt den Scheitelwinkel von α in zwei Teile, der untere misst $23^\circ$. Wie groß ist der obere Teil β? (P10 2014 OS)

   nachher: Die Geraden g und h schneiden sich. Zwischen ihnen liegt der Winkel $\alpha = 64^\circ$. Eine dritte Gerade geht durch den Schnittpunkt. Sie teilt den Scheitelwinkel von α in zwei Teile. Der untere Teil misst $23^\circ$. Wie groß ist der obere Teil β? (P10 2014 OS)

5. `winkel-dreiecke-e2-k3-s1-v1` – Parallelität aus gleichen Stufenwinkeln prüfen

   vorher: Die Gerade k schneidet die Geraden g (oben) und h (unten). An g liegt oberhalb von g rechts von k ein Winkel von $73^\circ$, an h oberhalb von h rechts von k ebenfalls $73^\circ$. Sind g und h parallel? \\ \kreuz{ja} \\ \kreuz{nein}

   nachher: Die Gerade k schneidet zwei Geraden g und h. Die Gerade g liegt oben, h liegt unten. An g liegt oberhalb von g und rechts von k ein Winkel von $73^\circ$. An h liegt oberhalb von h und rechts von k auch ein Winkel von $73^\circ$. Kreuze an, ob g und h parallel sind. \\ \kreuz{ja} \\ \kreuz{nein}

6. `winkel-dreiecke-e3-k2-s10-v1` – Vierecks-Eigenschaft ankreuzen

   vorher: Ergänze richtig: „In jedem Drachenviereck …“ (P10 2026 FOR) \\ \kreuz{sind alle Winkel gleich groß} \\ \kreuz{gibt es zwei Paare gleich langer Nachbarseiten} \\ \kreuz{sind alle Seiten gleich lang}

   nachher: Ein Satz beginnt so: „In jedem Drachenviereck …“ Kreuze an, wie er richtig weitergeht. (P10 2026 FOR) \\ \kreuz{sind alle Winkel gleich groß} \\ \kreuz{gibt es zwei Paare gleich langer Nachbarseiten} \\ \kreuz{sind alle Seiten gleich lang}

7. `winkel-dreiecke-e4-k1-s6-v1` – rechtwinkliges Dreieck aus den Katheten

   vorher: Konstruiere ein rechtwinkliges Dreieck ABC mit dem rechten Winkel bei C und den Katheten a = 4 cm und b = 6 cm.

   nachher: Konstruiere ein rechtwinkliges Dreieck ABC. Der rechte Winkel liegt bei C. Die Katheten sind a = 4 cm und b = 6 cm.

8. `winkel-dreiecke-e4-k3-s1-v1` – Fehler finden (WWW als Kongruenzsatz; Winkel an der falschen

   vorher: Sina sagt: „Mit $\alpha = 52^\circ$, $\beta = 64^\circ$ und $\gamma = 64^\circ$ ist das Dreieck eindeutig festgelegt – das ist der Kongruenzsatz WWW.“ Finde den Fehler.

   nachher: Sina sagt: „Mit $\alpha = 52^\circ$, $\beta = 64^\circ$ und $\gamma = 64^\circ$ ist das Dreieck eindeutig festgelegt. Das ist der Kongruenzsatz WWW.“ Finde den Fehler.

9. `winkel-dreiecke-e5-k1-s4-v1` – Inkreis

   vorher: Zeichne das Dreieck ABC. Konstruiere zwei Winkelhalbierende und den Inkreis. Gib den Mittelpunkt I an.

   nachher: Die Figur zeigt die Ecken eines Dreiecks ABC im Koordinatensystem. Zeichne das Dreieck. Konstruiere zwei Winkelhalbierende und den Inkreis. Gib den Mittelpunkt I an.

10. `winkel-dreiecke-e5-k2-s3-v1` – Mittelsenkrechte und Umkreis

   vorher: Drei Dörfer A, B und C wollen einen gemeinsamen Funkmast, der von allen drei Dörfern gleich weit entfernt ist (1 Kästchen = 1 km). Konstruiere den Standort. Gib seine Koordinaten und die Entfernung zu den Dörfern an.

   nachher: Das Koordinatensystem zeigt drei Dörfer A, B und C. Dabei steht 1 Kästchen für 1 km. Die Dörfer wollen einen gemeinsamen Funkmast. Er soll von allen drei Dörfern gleich weit entfernt sein. Konstruiere den Standort. Gib seine Koordinaten und die Entfernung zu den Dörfern an.

## Fälle, in denen die Regeln nicht reichten

1. e3-k1-s0-v1 bis v4 (Teildreieck ankreuzen, keine grafik): Mein
   erster Text „Zeichne eine Skizze. Fahre darin …“ löste in
   bank-pruef die Abweichung „grafik leer (Zeichenauftrag)“ aus, weil
   der Imperativ „Zeichne“ eine Grafik verlangt. Entscheidung: die
   Bestandsform „Fahre in einer Skizze das Dreieck nach …“ behalten,
   nur den Doppelpunkt vor den Kreuzen durch „Kreuze dieses Dreieck
   an.“ ersetzt. Regel fehlt: Bei Zeilen ohne grafik ist „Zeichne“ im
   neuen Text tabu.
2. e5-k2-s3-v1/v2 („(1 Kästchen = 1 km)“): Die Zahlprobe verlangt
   jede Ziffer wieder, also auch die „1“ in „1 Kästchen“. Das
   natürlichere „Ein Kästchen steht für …“ fällt durch. Entscheidung:
   „Dabei steht 1 Kästchen für 1 km.“ Die Regel „Zahlwörter erlaubt“
   gilt nur in eine Richtung (Ziffer → Wort ist verboten).
3. e2-k2-s0/s5–s7/s10 und e2-k3-s1 (Lage an Parallelen): Die Lage
   „oberhalb von g rechts von k“ ist von Natur aus lang und lässt
   sich ohne Figurbezeichnung nicht kürzer sagen. Entscheidung: ein
   fester Vorspann in drei kurzen Sätzen („Die Figur zeigt zwei
   parallele Geraden g und h. Die Gerade g liegt oben, h liegt unten.
   Die Gerade k schneidet beide.“), $g \parallel h$ durch Worte
   ersetzt; Sätze mit der Lageangabe bleiben bei etwa 15 Wörtern.
   Ebenso bleiben Angabesätze mit Maßlisten („Konstruiere das
   Dreieck ABC mit a = 6 cm, b = 5 cm und c = 7 cm.“) über 12
   Zählwörtern, weil „=“ und „cm“ mitzählen.
