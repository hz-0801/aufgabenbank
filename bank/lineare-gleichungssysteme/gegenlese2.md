# Zweitlesung lineare-gleichungssysteme

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 294
(zone 42, e1 50, e2 44, e3 57, e4 65, e5 36)

Prüfung: Jede Zeile gelesen (aufgabe, antwort, grafik, loesung,
pruef gegen sprosse_text und merkmal). Ein sympy-Skript hat die
Gleichungen mit Kennung I/II/III aus aufgabe gezogen und in 168
Zeilen das System gelöst (auch mit Parameter a, Schar und
unterbestimmten Systemen); alle übrigen Zeilen (Zone-Terme,
Tabellen, Sachaufgaben ohne Kennung, Mischungen, Parameterfälle)
von Hand nachgerechnet, dazu die Zulässigkeit der Mischungsanteile
(u, v, w ≥ 0 lösbar) und die Lage aller Lösungspunkte im
Koordinatensystem. Alle 234 Zeilen mit pruef-Zahl stimmen mit
loesung und eigener Rechnung überein (keine Rundungsfälle). 32
Ankreuzzeilen: jede Option einzeln geprüft, je genau eine richtig,
loesung wortgleich. 16 Fehler-finden-Zeilen: jeder eingebaute
Fehler ist wirklich falsch und die Richtigrechnung stimmt.
bank-pruef.py: 0 Abweichungen, 0 Warnungen in allen sechs Dateien.
Kein rechnerischer Fehler gefunden.

## Befunde

e1-k1-s6-v1, e1-k1-s6-v2, e1-k1-s6-v3: [E] „Die Geraden I und II
gehören zu den Gleichungen I und II“ verweist auf Gleichungen, die
nirgends stehen; lösbar ist die Aufgabe am Bild, der Satz schickt
den Schüler aber auf die Suche – Satz streichen oder „Die Geraden
I und II gehören zu einem Gleichungssystem“.

e2-k3-s4-v2, e2-k3-s4-v3: [M] Die Sprosse verlangt zu begründen,
warum nach dem Einsetzen nur eine Variable übrig ist; v2 fragt,
warum man überhaupt einsetzen darf (II wird dabei nicht genannt),
v3, warum Einsetzen in dieselbe Gleichung eine wahre Aussage
liefert – beides andere Begründungen als v1 – Fragen auf den
Sprossenkern zurückführen (z. B. v2: „I: x = 4y − 1, II: 3x + 2y
= 11 – warum steht nach dem Einsetzen nur noch y in II?“) oder v3
zum Fehler-finden-Muster „Term in dieselbe Gleichung“ stellen.

e4-k6-s1-v1: [M] merkmal „Anzahl und Gesamtbetrag vertauscht“
beschreibt den eingebauten Fehler ungenau: vertauscht sind die
beiden Gesamtbeträge zwischen I und II (so auch die loesung) –
merkmal zu „die zwei Gesamtbeträge vertauscht“ ändern.

Außerhalb der Kennzeichen, nicht gezählt: e3-k1-s9-v1 bis v3 –
die Begründung in loesung hat verdrehte Wortstellung nach „weil“
(„weil keine Variable steht allein“, „weil keine Gleichung ist
aufgelöst“, „weil keine Variable hat die Vorzahl 1“); richtig
„weil keine Variable allein steht“ usw.

Sauber: 288 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k3-s4-v2 und v3 fragen etwas anderes als die
Sprosse (warum man einsetzen darf; warum Einsetzen in dieselbe
Gleichung eine wahre Aussage gibt), v2 nennt dabei ein II, das
nicht dasteht. e4-k6-s1-v1: merkmal nennt „Anzahl und
Gesamtbetrag“, vertauscht sind aber die zwei Gesamtbeträge.
e3-k1-s9-v1 bis v3: Wortstellung im weil-Satz (Erstleser als
Schreibform-Befund, hier außerhalb der Kennzeichen notiert).

Nur Erstleser: e4-k1-s7-v1 bis v3 und e4-k3-s1-v1 bis v3 – die
loesung stellt I und II auf, ohne x und y zu benennen – bestätigt:
Die Aufgaben selbst sind eindeutig (der Schüler benennt), aber die
Musterlösung einer Sprosse „aufstellen, lösen, zuordnen“ sollte die
Benennung zeigen, wie e4-k1-s8-v7 und v8 es tun; ein Mangel der
Lösungsform, kein Rechenfehler (in der Zweitlesung gesehen, aber
nicht als Befund geführt).

Nur Zweitleser: e1-k1-s6-v1 bis v3 – der Satz „Die Geraden I und
II gehören zu den Gleichungen I und II“ verweist auf Gleichungen,
die nicht dastehen.

Widersprüche: e1-k1-s6-v1 bis v3 – der Erstleser hat den Satz
gesehen und bewusst nicht als Befund geführt, weil die Aufgabe am
Bild lösbar ist; die Zweitlesung führt ihn als [E], weil der Satz
auf nicht vorhandene Gleichungen verweist. Lösbarkeit ist
unstrittig; zu entscheiden ist nur, ob der Satz bleibt.
