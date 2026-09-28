# Zweitlesung trigonometrische-funktionen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 268
(zone 46, e1 54, e2 60, e3 57, e4 51)

Prüfung: Alle 268 Zeilen einzeln gelesen (Aufgabe, Grafik, Antwortgerüst,
Lösung, pruef, Merkmal gegen sprosse_text). Jede Zahl der Lösungen aus dem
Aufgabentext neu gerechnet (Python/math): Seitenverhältnisse, Taschenrechnerwerte
in DEG und RAD (auch die Fehlerwerte sin 25 und 8 · sin 35 im Bogenmaß),
Umrechnungen Grad/Bogenmaß, beide Winkel zu sin α = c, Wertetabellen,
Sinussatz-Rechnungen der drei P10-Formen (8,11 cm; 14,2 m; 343,8 cm),
Perioden 360° : b, Null- und Extremstellen, Mittellinie/Amplitude, alle
Sachmodelle y = a · sin(b · t) + d einschließlich der Ungleichung
1,5 · sin(60 · t) + 4 < 3 (t ≈ 3,7 h); alle 179 Zeilen mit pruef-Zahl stimmen
nach Rundung. Die Grafiken wurden gegen die Werte gehalten (Achsenbereich,
Periode im Raster, Lage der markierten Punkte). Ankreuzzeilen (43) je Option
geprüft: überall genau eine richtige Option je Gruppe, Lösung wortgleich; auch
die Zuordnungen mit Scheinoptionen (sin(−2 · x), 3 · sin(2,5 · x), b = 8 statt 45,
72 h statt 5 h) sind eindeutig falsch. Fehler-finden-Zeilen (13, davon eine im Zone-Paar)
geprüft: eingebauter Fehler jeweils wirklich falsch, Richtigrechnung stimmt.
bank-pruef.py: 0 Abweichungen, 0 Warnungen.

## Befunde

e4-k1-s5-v2: [E] „Start auf Höhe der Mitte“ legt die Richtung nicht fest;
y = −20 · sin(36 · t) + 25 erfüllt den Text ebenso – „(Start auf Höhe der Mitte,
die Gondel steigt)“ ergänzen, wie in e4-k1-s13-v2.

Sauber: 267 Zeilen ohne Befund

## Abgleich

Beide Leser: e4-k1-s5-v2 – „Start auf Höhe der Mitte“ ohne Richtung, a = −20
wäre ebenso richtig; „und steigt“ ergänzen.

Nur Erstleser:
- zone-f4-v1 (E): „gerundet“ ohne Stellenzahl – bestätigt, die Lösung 18,85 ist
  aus dem Text nicht festgelegt.
- e1-k1-s13-v3 (E): z ist nicht erklärt – bestätigt, die Regel „Buchstaben nur,
  wenn im Text erklärt“ greift; bei mir übersehen.
- e4-k1-s5-v1, s5-v2, s5-v3, s6-v1 (E): t und y ohne Erklärung und Einheit,
  obwohl b von der Zeiteinheit abhängt – bestätigt, leicht (die Einheit der
  Periode legt t nahe, erklärt ist es nicht).
- e4-k1-s7-v1..v3, s13-v1..v3 (E): Grad-Modus nicht genannt – bestätigt und
  wichtiger, als ich es gelesen habe: e1-k1-s12-v3 lehrt „Winkel ohne
  Gradzeichen → RAD“, und sin(15 · 4) steht ohne Gradzeichen; nach der eigenen
  Regel des Eintrags wäre RAD richtig und das Ergebnis falsch.
- zone-f1-v4, zone-f4-v4 (M): Fallstrick nicht provoziert, Aufgabe gleicht der
  leichten Zeile – bestätigt als Schwäche; die Aufgaben sind richtig, der
  Fallstrick steht nur in der Lösung.
- zone-f2-v2 (M): gleicher Aufgabentyp wie zone-f1-v3, dort „mittel“, hier
  „sehr leicht, im Kopf“ – bestätigt, sin 64° auf zwei Stellen geht nicht im Kopf.
- e1-k1-s7-v2 (M): negativer Sinuswert verlangt die Umlegung von −23,6° in den
  dritten und vierten Quadranten – bestätigt, ein Schritt mehr als v1 und v3.
- e2-k1-s7-v3 (M): eingeschränkter Winkelbereich als Zusatzmerkmal –
  bestätigt; ich hatte es gesehen und als zulässig durchgehen lassen.
- e3-k1-s7-v3, e3-k1-s8-v3 (M): negatives a (s7-v3 ohne b) – bestätigt für
  s7-v3 (verlangt b gar nicht, also etwas anderes als v1/v2); für s8-v3 nur
  leicht, das Vorzeichen ist seit s4 eingeführt, aber ein Schritt mehr als die
  Schwestern.
- e3-k1-s11-v1..v3 (M): Varianten teilen das Merkmal c/d auf – bestätigt,
  leicht (Vorratssprosse).
- e4-k1-s11-v1..v3 (M): Varianten teilen die Sprosse in Tabelle und Auswahl
  auf – bestätigt, leicht.
- e2-k1-s15-v2, s15-v3 (M): Tabelle wiederholt e2-k1-s1-v5 bzw. den Bereich von
  e2-k1-s2-v3 – bestätigt, die Wertetabelle von s15-v2 ist argumentgleich mit
  s1-v5.
- e2-k1-s8-v3, e2-k1-s11-v3: negative Winkel vor der Symmetrie-Sprosse –
  bestätigt als leichte Merkmalsabweichung (neuer Winkelbereich), kein
  Rechenfehler.
- e3-k3-s1-v2: Fehler finden setzt d (Vorrat GYM) voraus – nicht bestätigt:
  der Schüler liest Hoch- und Tiefpunkt ab und halbiert den Abstand, den
  Parameter d braucht er dafür nicht; der Fehler „Höhe über der Achse“ lässt
  sich nur an einer verschobenen Welle zeigen.

Nur Zweitleser: keine.

Widersprüche: e3-k3-s1-v2 – der Erstleser beanstandet die Voraussetzung d, ich
halte die Zeile für ohne d lösbar. Sonst keine; die übrigen Unterschiede sind
Befunde, die ich übersehen oder zu milde gelesen habe.
