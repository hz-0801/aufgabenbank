# Zweitlesung funktionsscharen-und-ortskurven

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 222
(zone 30, e1 40, e2 37, e3 36, e4 42, e5 37)

Prüfung: Jede Zeile aus dem Aufgabentext neu gerechnet; alle Rechnungen mit Parameter (Ableitungen, Extrem- und Wendestellen, Diskriminanten, Integrale mit Parametergrenzen, Ortskurven, Streckungsidentitäten f_a(x) = f_1(ax)/a, Trapezflächen für k = 4 … 9) mit einem sympy-Skript im Scratchpad bestätigt, die Zahlaufgaben der Zone und von e1 von Hand. Alle 175 Zeilen mit pruef-Zahl stimmen mit loesung und pruef überein (Rundung eingeschlossen); keine Zeile ist rechnerisch falsch. Die 16 Ankreuzzeilen (je vier Vorstufen in e1, e2, e4, e5) haben genau eine richtige Option, loesung nennt sie wortgleich. Die 16 Fehler-finden-Zeilen (zone-f1-v5 und je drei in e1–e5) enthalten einen echten Fehler aus „Typische Fehler“, die Richtigrechnung stimmt. Grafiken gegen die Aufgabenwerte gehalten (Zuordnungen in e1-k1-s5 und e1-k1-s8, Ablesegrafiken e3-k1-s8-v3/v4, Lösungsgrafiken e1-k1-s7 und e4-k1-s8-v5/v6): passen. Originale gegen Abschnitt 2 der Mappe gehalten. `werkzeuge/bank-pruef.py funktionsscharen-und-ortskurven`: 0 Abweichungen, 0 Warnungen.

## Befunde

e1-k1-s2-v3: [E] Der Text spricht von „ein abgebildeter Graph“, die Zeile hat aber keine Grafik (aus dem Original übernommen) – „Ein Graph der Schar geht durch (0 | 12)“ schreiben.

e1-k1-s8-v3, e1-k1-s8-v4, e2-k1-s8-v3, e2-k1-s8-v4, e3-k1-s8-v3, e3-k1-s8-v4, e4-k1-s8-v3, e4-k1-s8-v4, e4-k1-s8-v5, e4-k1-s8-v6, e5-k1-s8-v3, e5-k1-s8-v4: [M] sprosse_text gibt nur die erste Aufgabe der Prüfungshöhe des Katalogs wieder („Bestimmungsgleichungen … deuten“, „Folgerungen … übersetzen“, „über die Diskriminante“, „Vierecksinhalt …“, „Ortsgerade y = x …“), die Zeilen üben aber die zweite oder dritte (Graphen über das Grenzverhalten zuordnen; Nullstellen und Tangente am faktorisierten Term; waagerechte Tangente am Bild; Achsendreieck als Term; Stammfunktionen nach Vorzeichen; Trapezflächen für k und k + 1) – sprosse_text auf die ganze Prüfungshöhe des Katalogs erweitern oder je Original eine eigene Sprosse mit passendem Text führen.

e3-k1-s7-v3: [M] merkmal „Punkte in Parameterkoordinaten, Abstand mit Pythagoras“, die Aufgabe verlangt aber den Parameter aus der Differenz der Extremstellen (rückwärts, ohne Punkte und ohne Pythagoras; Typ „Scharparameter aus dem Abstand der Extremstellen berechnen“) – durch eine Abstandsaufgabe mit Punkten ersetzen oder merkmal/Sprosse anpassen.

e3-k2-s3-v2, e3-k2-s3-v3: [M] sprosse_text „Einzigen Wendepunkt einer Schar nachweisen und angeben“, beide Aufgaben fragen nur nach dem Hochpunkt (Maximum der Konzentration, höchster Punkt des Wasserstrahls), kein Wendepunkt – je eine Frage nach der stärksten Ab- bzw. Zunahme (Wendestelle) ergänzen, wie in v1.

e4-k1-s1-v2, e4-k1-s1-v4: [M] merkmal „Nullstellen als Terme sind die Integrationsgrenzen“, hier sind die Nullstellen parameterfrei (±2 bzw. 0 und 3), der Parameter steht nur als Faktor – Terme so wählen, dass die Nullstellen vom Parameter abhängen (wie v1, v3, v5).

e5-k1-s3-v2, e5-k1-s3-v3: [M] merkmal „Ortskurve ist eine Gerade: Steigung aus zwei Punkten“, beide Aufgaben verlangen die Elimination wie der Grundfall s1 und keine Steigung aus zwei Punkten – als Zwei-Punkte-Aufgabe fassen (zwei Hochpunkte angeben lassen) oder merkmal auf „Ortsgerade über die Elimination“ ändern.

Hinweise ohne Kennzeichen (nicht gezählt): e4-k1-s6-v1 übernimmt die Flugkurve p_a(x) = −ax² + bx + 2 wörtlich aus dem Original 2018MerhoehtBAnalysisWTR2-1d (Sperre; das Prüfskript fängt es nicht) – etwa −ax² + bx + 3 mit angepasstem f. e3-k2-s3-v1 und e4-k1-s4-v3 behalten den Kontext der Originale 2017MgrundlegendBAnalysisCAS-2d/-2c (Temperatur einer Flüssigkeit, t · e^(−kt)); die Verfremdung verlangt einen anderen Kontext. e5-k1-s8-v4 ist e5-k1-s8-v3 um 2 verschoben (alle Werte und Seitenlängen gleich).

Sauber: 202 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e1-k1-s2-v3: „abgebildeter Graph“ ohne Grafik.
- e1-k1-s8-v3/v4, e4-k1-s8-v3 bis v6, e5-k1-s8-v3/v4: sprosse_text nennt nur die erste Aufgabe der Prüfungshöhe, die Zeilen üben eine andere.
- e3-k1-s7-v3: Umkehraufgabe aus der x-Differenz statt Abstand mit Pythagoras.
- e3-k2-s3-v2/v3: Sprosse verlangt den einzigen Wendepunkt, die Aufgaben fragen nur nach dem Maximum.
- e4-k1-s1-v2/v4: Nullstellen parameterfrei, obwohl das Merkmal Nullstellen als Terme verlangt.

Nur Erstleser:
- e1-k1-s6-v1, e2-k1-s5-v2, e4-k2-s3-v3 (pruef deckt nicht jede Ergebniszahl ab): bestätigt als Lücke im pruef; die Lösungen stimmen, rechnerisch kein Fehler, deshalb in meiner Liste nicht gezählt.
- e3-k1-s8-v1/v2 („Bestimme ihn“ kann Wert oder Punkt meinen): bestätigt – „ihn“ bezieht sich grammatisch auf „Wert“ wie auf „Punkt“; das hatte ich übersehen.
- e1-k1-s2-v2 (quadratische statt lineare Gleichung): als Unstimmigkeit bestätigt, aber kein Fehler der Bank – die Zeile verfremdet genau 2022-bebb-lk-A1.3a, das der Katalog auf diese Sprosse legt und das selbst auf a² führt; Katalogbefund (Sprossentext zu eng).
- e2-k1-s4-v3 (keine Fallunterscheidung wegen b > 0): nicht bestätigt als Fehler der Bank – das Original 2025MerhoehtBAnalysisMMS2-1a hat ebenfalls b > 0 und steht im Katalog auf dieser Sprosse; höchstens ein Katalogbefund.
- e3-k1-s2-v1 (nur die parameterfreie x-Koordinate gefragt): bestätigt – merkmal „Extremstelle und Art hängen vom Parameter ab“ trifft nicht zu, auch wenn die Zeile dem Original 2020MerhoehtAAnalysis13-a folgt; die y-Koordinate 432k mitzufragen behebt es.
- e4-k1-s6-v2 (kein Parameter bestimmt): nicht bestätigt – das Original 2022MerhoehtBAnalysisWTR1-1e verlangt genau die zwei Übergangsbedingungen, der Katalog legt es auf diese Sprosse.
- e2-k1-s7-v3 (Quotientenregel nicht eingeführt): nicht bestätigt – die Ableitungsregeln sind Voraussetzung aus dem Nachbarthema ableitungsregeln.md, die Zone muss nicht jede Regel üben.
- e4-k2-s1-v3 (Klammerfehler statt Muster der Sprosse): nicht bestätigt – „Parameterpotenzen beim Einsetzen der Grenzen falsch“ steht in „Typische Fehler“ (Katalogzeile 106), und das verlangt bank.md für Fehler-finden-Zeilen.
- `\_\_` in antwort (88 Zeilen): bestätigt – zusammenbau.py trennt mit `antwort.split("__")`, die Zeichenfolge `\_\_` enthält kein `__`.

Nur Zweitleser:
- e2-k1-s8-v3/v4, e3-k1-s8-v3/v4: dasselbe Muster wie die gemeinsamen s8-Befunde – sprosse_text nennt nur die erste Aufgabe der Prüfungshöhe; der Erstleser hat es in e2 und e3 nicht gemeldet.
- e5-k1-s3-v2/v3: Merkmal „Steigung aus zwei Punkten“, die Aufgaben verlangen die Elimination wie der Grundfall.
- Hinweise ohne Zählung: e4-k1-s6-v1 übernimmt p_a(x) = −ax² + bx + 2 wörtlich aus 2018MerhoehtBAnalysisWTR2-1d (Sperre); e3-k2-s3-v1 und e4-k1-s4-v3 behalten den Kontext Flüssigkeitstemperatur der Originale; e5-k1-s8-v4 ist v3 um 2 verschoben.

Widersprüche: keine in der Sache; beide Leser rechnen jede Lösung richtig. Die Leser urteilen verschieden, wo eine Zeile ein Original treu verfremdet, das zum Sprossentext nicht ganz passt (e1-k1-s2-v2, e2-k1-s4-v3, e4-k1-s6-v2): Der Erstleser meldet die Zeile, ich sehe den Befund beim Katalog.
