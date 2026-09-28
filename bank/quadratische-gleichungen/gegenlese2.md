# Zweitlesung quadratische-gleichungen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 258
(zone 34, e1 63, e2 43, e3 79, e4 39)

Prüfung: Jede Zeile gelesen (Aufgabe, Antwortgerüst, Lösung, pruef,
Grafik, sprosse_text, merkmal). Von den 225 Zeilen mit pruef-Zahl
wurden 152 mit sympy aus dem Aufgabentext gelöst (alle
gleichungsraster-Zeilen direkt aus aufgabe, Text- und Sachaufgaben
über eine von Hand aufgestellte Gleichung); 134 stimmen unmittelbar
mit pruef überein, die übrigen 18 sind erwartete Abweichungen und von
Hand bestätigt (pruef trägt bei „keine Lösung“ den negativen Wert
unter der Wurzel bzw. von x², bei Schnittpunkten zusätzlich die
y-Werte, bei Sachaufgaben Breite und Länge statt beider Lösungen).
Die 73 weiteren pruef-Zeilen (Zone-Rechnungen, Einsetzproben,
Diskriminanten, p und q ablesen, Anzahl der Lösungen) von Hand
nachgerechnet, Rundungen auf zwei Stellen geprüft (√11, √7, √13,
√30, 3 ± √5, −5 ± √7, 1 ± √3, 5 ± √3, −2 ± √5, 2 ± √3, −1 ± √5,
Zylinderradien, Kreisradius): alles richtig. Die Graphen (\parabel
als a(x − d)² + e, \gerade) passen zu den Gleichungen, Scheitel und
Schnittstellen liegen im Achsenbereich. 28 Ankreuzzeilen: jede Option
einzeln geprüft, genau eine richtig, loesung wortgleich; bei
2025-OS-B1h-Verfremdungen ist die zweite echte Lösung (−2 bzw. −5)
keine Option. 13 Fehler-finden-Zeilen: eingebauter Fehler jeweils
wirklich falsch und konsistent durchgerechnet, Richtigrechnung
stimmt. `werkzeuge/bank-pruef.py quadratische-gleichungen`: 0
Abweichungen, 0 Warnungen.
Hinweis außerhalb der Zeilenzählung: Die Bank ist nach Katalog-Commit
99da689 gebaut (stand.md), die Mappe steht auf c651dc4. Dort ist die
Reihenfolge der Einheiten eine andere (Einheit 2 p-q-Formel, Einheit 3
Nullprodukt; in der Bank e2 Nullprodukt, e3 p-q-Formel), die
quelle-Zeilen (106–109 gegen 103–106) und mehrere sprosse_text passen
nicht mehr wortgleich (etwa die Vorstufe der Wurzelkette, im neuen
Katalog ausdrücklich „bei x² = c“, in der Bank an (x − d)² = c).
Das ist ein Nachzug des ganzen Eintrags, kein Zeilenbefund.

## Befunde

zone-f7-v2: [M] merkmal „sehr leicht: x mal Klammer ausmultiplizieren“,
die Aufgabe verlangt aber die Gegenrichtung (x²+7x – x ausklammern);
die zwei Grundfall-Varianten unterscheiden sich damit im Handgriff,
nicht nur in den Zahlen – Aufgabe auf Ausmultiplizieren umstellen
(etwa x·(x + 7)) oder merkmal beider Zeilen auf „ausmultiplizieren
oder ausklammern“ fassen.

e1-k2-s7-v2, e1-k2-s7-v3: [M] Die Sprosse verlangt die
Fallbetrachtung („nach dem Freistellen entscheidet das Vorzeichen“),
das Antwortgerüst nimmt den Fall aber vorweg: v2 „x = __“ (eine
Lösung), v3 leer (keine Lösung), v1 „x1, x2“ – einheitliches Gerüst
für alle drei („Lösungen: __“).

e3-k3-s6-v1, e3-k3-s6-v2, e3-k3-s6-v3: [E] Antwortgerüst „x1 = __,
x2 = __“, die Lösung ist „genau eine Lösung: x = …“; das Gerüst
verlangt zwei Werte, wo einer richtig ist – Gerüst wie in e1-k2-s10
und e2-k1-s4 („x = __“) oder neutral („Lösungen: __“).

e4-k1-s5-v2: [E] sprachlich: „Eine rechteckige Wiese … Wie breit ist
es?“ – „Wie breit ist sie?“.

Sauber: 251 Zeilen ohne Befund

## Abgleich

Beide Leser: zone-f7-v2 – Variante klammert aus, merkmal und v1
multiplizieren aus. e1-k2-s7-v2 und e1-k2-s7-v3 – das Antwortgerüst
verrät den Fall, den die Sprosse erst betrachten lassen will.
e3-k3-s6-v1 bis v3 – Gerüst mit zwei Lösungen bei genau einer Lösung.
e4-k1-s5-v2 – „Wiese … ist es“ statt „ist sie“.

Nur Erstleser:
- e1-k3-s4-v2 (R, Zwischenrundung): bestätigt – √0,95 ≈ 0,975 führt
  auf 0,97, die Lösung nennt den exakt gerechneten Wert 0,98
  (√(3/π) ≈ 0,977); den Zwischenwert genauer schreiben. Die drei
  Zylinderzeilen e1-k2-s6 habe ich daraufhin nachgesehen: dort passt
  der gerundete Zwischenwert zum Endwert.
- e1-k2-s0-v1 bis v4 (M, Vorstufe an quadrierter Klammer):
  bestätigt – im aktuellen Katalog heißt die Vorstufe ausdrücklich
  „bei x² = c“, und die quadrierte Klammer kommt erst in s8; die
  Trennung „Erkennung an x² = c, Vorstufe an (x − d)² = c“
  (stand.md Entscheidung 1) ist mit dem Streichen der
  Erkennungsschritte hinfällig. Ich hatte das nur als Hinweis zum
  Katalogstand geführt, nicht je Zeile.
- e1-k2-s13-v3 (M, andere Aufgabenart): bestätigt – „Zahl rechts
  ändern“ ist ein anderer Handgriff als „selbst angeben“, und die neue
  rechte Seite muss nicht negativ sein (jede Zahl unter 4), das
  merkmal „rechte Seite negativ“ trifft erst nach dem Freistellen zu.
  Von mir übersehen.
- e2-k2-s1-v3 (Schreibform, Formel vor ihrer Einheit): bestätigt für
  die Reihenfolge der Bank (Nullprodukt e2 vor p-q-Formel e3); die
  Richtigrechnung braucht die Lösungsformel. Im aktuellen Katalog
  steht die p-q-Formel vor dem Nullprodukt, dort entfiele der Befund
  – bis zum Nachzug Lösung bei x² + 2x − 24 = 0 enden lassen oder
  durch Probe bestätigen.

Nur Zweitleser: keine – alle meine Befunde hat auch der Erstleser;
zusätzlich nur der Hinweis außerhalb der Zählung, dass die Bank auf
Katalog-Commit 99da689 steht und Einheitenfolge, quelle-Zeilen und
sprosse_text dem Katalog der Mappe (c651dc4) nicht mehr folgen.

Widersprüche: keine.
