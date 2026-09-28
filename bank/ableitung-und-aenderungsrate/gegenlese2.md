# Zweitlesung ableitung-und-aenderungsrate

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 220
(zone 30, e1 49, e2 49, e3 43, e4 49)

Prüfung: Alle 220 Zeilen wurden mit einem Skript kompakt ausgegeben
und einzeln gelesen. Jede Lösung wurde nachgerechnet: die 54 Zeilen
mit e-Funktion, Wurzel, Kreisbogen oder Näherungswert mit sympy bzw.
Python (Funktionswerte, Ableitungen, Nullstellen, Grenzwerte,
Differenzenquotienten), die übrigen Rechen- und Ablesezeilen im
Kopf, dazu bei den 53 Zeilen mit Grafik die Lage der Lösungspunkte
im Achsenbereich und die Werte der Funktion an den genannten
Stellen. Die 22
Ankreuzzeilen wurden auf genau eine richtige Option und wortgleiche
Nennung in loesung geprüft, die 13 Fehler-finden-Zeilen darauf, ob
der eingebaute Fehler falsch und die Richtigrechnung richtig ist.
Nebenprüfung mit Skript: $-Zeichen, geschweifte und runde Klammern
paarig in allen Feldern, keine Aufgabe doppelt (aufgabe und grafik
zusammen). werkzeuge/bank-pruef.py ableitung-und-aenderungsrate:
0 Abweichungen, 0 Warnungen in allen fünf Dateien.

## Befunde

ableitung-und-aenderungsrate-e1-k1-s9-v1: Der Endpunkt des
Skateparks ist nicht bestimmt – der Text nennt keinen
Definitionsbereich, und \funktion{0.1*\x^3} verlässt das Fenster
(ymax 4) oben bei x ≈ 3,42. Die Lösung nimmt (3 | 2,7) als Ende;
nimmt der Schüler das sichtbare Ende (3,42 | 4), hat die Sekante die
Steigung 1,17 > 1, und das Urteil kippt auf „nicht erfüllt". –
Vorschlag: „für 0 ≤ x ≤ 3" in den Text und
\funktionab{0.1*\x^3}{f}{0}{3}.

ableitung-und-aenderungsrate-e1-k1-s9-v2: Gleicher Mangel – kein
Definitionsbereich, \funktion{0.75*\x^2} verlässt das Fenster bei
x ≈ 2,31; die Lösung setzt den Endpunkt (2 | 3). Das Urteil
(steiler) bleibt bei jedem Endpunkt gleich, die Zeichnung ist aber
nicht eindeutig. – Vorschlag: „für 0 ≤ x ≤ 2" und
\funktionab{0.75*\x^2}{f}{0}{2}.

ableitung-und-aenderungsrate-e1-k1-s9-v3: Der Graph läuft bis x = 5
(w(5) = 1,9375), die Lösung nimmt den Endpunkt (4 | 2). Das Urteil
(flacher, Steigung 0,25 bzw. 0,19 < 0,5) bleibt, der Endpunkt ist
aber unbestimmt. – Vorschlag: „für 0 ≤ x ≤ 4" und
\funktionab{1+0.5*\x-0.0625*\x^2}{w}{0}{4}.

ableitung-und-aenderungsrate-e2-k1-s7-v1: Die Deutung „die Schaufel
läuft dort ohne Knick weiter" ist falsch: f'(0) und p'(0,5) gehören
zu verschiedenen Punkten, (0 | 0) und (0,5 | 0,75). Die Graphen
schneiden sich bei x ≈ 0,51, und dort ist f'(0,51) ≈ 1,08 ≠ p' = 2 –
am Schnittpunkt gibt es einen Knick. Richtig ist nur „die Tangenten
in diesen beiden Punkten sind parallel". – Vorschlag: Deutung auf
parallele Tangenten kürzen, oder p so wählen, dass p(0,5) = f(0)
gilt und die Stellen zusammenfallen (dann ist der glatte Übergang
echt).

ableitung-und-aenderungsrate-e2-k1-s7-v2: „die Kurve geht bei x = 5
knickfrei in die Gerade über (sogar gleiche Tangente)" ist falsch:
f(5) = 1,25 − 5 = −3,75, aber g(5) = −2,5 – die Graphen treffen sich
bei x = 5 nicht, die Tangente an f bei 5 ist y = −0,5x − 1,25 und
nicht g. Die Steigungen sind gleich, die Geraden parallel; der Text
sagt außerdem nicht, wo die Gerade beginnt. – Vorschlag: g(x) =
−0,5x − 1,25 für x ≥ 5; dann stimmen Rechnung und Deutung.

ableitung-und-aenderungsrate-e2-k2-s1-v1: f(t) = 5t² gibt f(2) = 20,
nicht 40. Die Lösung nennt „Tangente im Punkt (2 | 40)" und „nicht
der Wert 40". Die Steigung 20 (f'(2) = 20) ist richtig. –
Vorschlag: (2 | 20) und „nicht der Wert 20".

ableitung-und-aenderungsrate-e1-k2-s4-v1: fraglich: w(3) = 8 liegt
genau auf ymax = 8 – der zweite Sekantenpunkt sitzt auf dem oberen
Fensterrand, der Graph endet dort. – Vorschlag: ymax=12, ystep=2.

ableitung-und-aenderungsrate-zone-f2-v4: fraglich: Die Lösung warnt
vor „der sechsten Spalte", die Tabelle hat aber nur fünf
Wertespalten (t = 0 bis 8) – der Fallstrick „Zeilennummer statt
Stelle" kann so nicht greifen. – Vorschlag: Tabelle bis t = 10
verlängern (sechs Spalten), dann ist die sechste Spalte t = 10.

ableitung-und-aenderungsrate-e4-k1-s1-v1, -v2, -v3, -v4, -v5:
fraglich: „Gib die Nullstelle an und nenne den Zeitpunkt … an" –
„nenne … an" ist kein Deutsch; in allen fünf Grundfallzeilen. –
Vorschlag: „und nenne den Zeitpunkt der größten …".

ableitung-und-aenderungsrate-e1-k2-s4-v1, -v2, -v3: fraglich:
sprosse_text heißt „Sekantengleichung durch zwei Punkte eines
Graphen ermitteln", keine der drei Zeilen verlangt eine Gleichung –
gefragt ist nur Sekante zeichnen und Steigung bzw. Rate angeben.
Die Aufgaben passen zum merkmal (Darstellungswechsel), nicht zum
Typnamen. – Vorschlag: entweder je Zeile „und gib die Gleichung der
Sekante an" ergänzen oder den Typnamen der Pflicht darstellung
anders wählen.

ableitung-und-aenderungsrate-e2-k4-s3-v2, -v3: fraglich:
sprosse_text „Stelle mit vorgegebener momentaner Änderungsrate über
die Ableitung berechnen" – v2 und v3 berechnen den Ableitungswert
an gegebener Stelle, keine Stelle zu gegebener Rate; nur v1 tut
das. Das merkmal („der Ableitungswert oder die Stelle") ist weiter
als der Typname. – Vorschlag: v2 und v3 als Rückrichtung stellen
(etwa: ab wann wächst der Umsatz momentan mit höchstens … je Monat)
oder den Typnamen der Pflicht anwendung anpassen.

Sauber: 203 Zeilen ohne Befund

## Abgleich

Gelesen nach dem eigenen Befundteil. Die beiden vom Erstleser
korrigierten Zeilen (e1-k1-s6-v2, e1-k2-s4-v1) lagen mir schon in
der korrigierten Fassung vor; beide sind nachgerechnet richtig.

- Beide Leser: e1-k1-s9-v1, -v2, -v3 (Endpunkt nicht festgelegt,
  Graph verlässt das Fenster, bei v1 kippt das Urteil);
  e2-k1-s7-v1 (kein Anschluss, nur parallele Tangenten);
  e2-k1-s7-v2 (f(5) ≠ g(5), kein knickfreier Übergang; gleicher
  Vorschlag g(x) = −0,5x − 1,25); e2-k2-s1-v1 (Punkt (2 | 20), nicht
  (2 | 40) – der Erstleser ändert die Grafik auf 5x² + 20, damit
  f(2) = 40 ≠ f'(2) = 20 bleibt; das ist der bessere Weg, weil der
  Hinweis „nicht der Wert" dann greift); e1-k2-s4-v1 (Punkt (3 | 8)
  auf ymax; Sekantengleichung nicht gefragt); e4-k1-s1-v1 bis -v5
  („nenne … an").
- Nur Zweitleser: zone-f2-v4 (Tabelle hat keine sechste Spalte,
  der Fallstrick greift nicht); e1-k2-s4-v2, -v3 (Typname
  „Sekantengleichung" – der Erstleser nennt es unter v1 für alle
  drei Varianten, nur die ids fehlen); e2-k4-s3-v2, -v3 (Typname
  „Stelle mit vorgegebener Rate", die Zeilen berechnen den Wert).
- Nur Erstleser:
  - zone-f1-v3 pruef [2, −1]: teils – in der Sache ja, aber −1 steht
    in „2x − 1" nicht an einer Ergebnisstelle nach bank.md
    („erste Zahl nach ="); vor dem Ändern das Prüfskript laufen
    lassen. Gleiches gilt für zone-f1-v4 (7 in „−3x + 7"),
    e1-k1-s5-v1 (2,277) und e1-k1-s5-v3 (−4 in „3x − 4").
  - zone-f1-v3 \steigungsdreieck{1}{1}{1}: Zustimmung – das dritte
    Argument ist die Steigung (mathblatt.sty, Z. 633: „1 nach
    rechts, m=2 nach oben"); {1}{1}{2} ist richtig. Ich hatte das
    Argument als Breite gelesen und den Fehler übersehen.
  - zone-f6-v4 Achse x, Optionen t: Zustimmung – die Grafik hat
    anders als f6-v3 kein xlabel.
  - e2-k4-s4-v3 pruef und „an welcher Stelle": Zustimmung – zwei
    Stellen, Plural und pruef [9, −3, 9, 1, −1].
  - e4-k2-s3-v2, -v3 „In welchem Monat / An welchem Tag" bei t = 10:
    Zustimmung – „nach 10 Monaten" ist eindeutig, „im 10." und
    „im 11." sind beide vertretbar.
  - e4-k2-s4-v3 ymin2 = −4, f'(6) = −12: Zustimmung – f' verlässt
    das untere System ab x ≈ 4,83 (x² − 4x − 4 = 0); ymin2=-12
    oder Intervall bis 4.
  - zone-f3-v2 Varianten tragen verschiedene Teile des Merkmals:
    teils – der Erstleser hat recht, dass v1 und v2 nicht
    austauschbar sind; die Zone-Regel verlangt aber nur zwei sehr
    leichte Zeilen je Fertigkeit, und die Fertigkeit ist hier ein
    Bündel; sauberer wäre ein merkmal je Zeile.
  - e1-k1-s1-v3 „ersten bis 15. Tag" (14 Tage): teils – die Aufgabe
    ist eindeutig lösbar, aber schwerer als die anderen vier
    Grundfallzeilen; „nach 14 Tagen" passt besser zum Grundfall.
  - e1-k1-s8-v2 nur eine Lösung: Zustimmung – das Merkmal „die
    kleinere Lösung wählen" wird in v2 nicht geübt.
  - e1-k1-s10-v3 und e4-k1-s9-v4 (Varianten teilen die Sprosse):
    Widerspruch – der Erstleser sieht ungleichwertige Varianten,
    bank.md verlangt aber „Prüfungshöhe 2 je Original", und die
    Sprosse fasst zwei Originale zusammen; die Aufteilung 2 + 2
    (bzw. 3 + 2 + 2) folgt der Regel, nur der Sprossentext ist ein
    „und"-Satz aus zwei Typen.
  - e1-k2-s2-v3 Begründung zur Uhrzeit: teils – gehört nicht zum
    Begründen-Typnamen, übt aber den Fallstrick der Einheit (Zone
    f3, Sprosse s2); ein Satz zur Einheit des Differenzenquotienten
    wäre näher am Typ.
  - e1-k2-s3-v1, -v3 „aus dem Funktionsterm" ohne Term: Zustimmung –
    beide Zeilen rechnen aus Messwerten, nur v2 hat einen Term.
  - e2-k1-s0-v1 Einheit nicht gefragt: Zustimmung – das Merkmal
    nennt „die Einheit nennen", kein Auftrag verlangt sie, v3/v4
    haben keine.
  - e2-k1-s3-v3 g'(0) = 0 ohne Steigungsdreieck: teils – als dritte
    Variante ist die waagerechte Tangente ein guter Sonderfall,
    aber das Merkmal (Steigungsdreieck) fehlt; eine Stelle mit
    g'(x₀) ≠ 0 wäre merkmaltreu.
  - e4-k1-s5-v2 nur eine Nullstelle, keine Uhrzeit: Zustimmung –
    die Zeile ist eine Wiederholung von Sprosse 1 mit Term.
  - e4-k1-s7-v2 beide Lösungen in der Phase, „ist $= 4$":
    Zustimmung – das Verwerfen entfällt, der Tippfehler steht da.
  - e4-k2-s2-v3 Randvergleich nicht im Begründen-Text: teils –
    nicht im Typnamen, aber das Fehlermuster „Randwerte nicht
    geprüft" steht in der Fehler-finden-Sprosse derselben Einheit;
    ich würde die Zeile lassen und den Typnamen erweitern.
  - e2-k1-s6-v3 „Fläche unter dem Graphen": teils – die Wendung
    greift dem Integral vor; die Begründung über die Einheit (km je
    Stunde ist eine Rate) reicht und ist im Stand der Kette.
  - e2-k4-s2-v3 „Grenzwert von Differenzenquotienten": teils – der
    Grenzwert ist erst Einheit 3, die Begründung über das
    Steigungsdreieck (m durch s) ist in Einheit 2 verfügbar.
  - e4-k2-s1-v3 mehrere Fehler vermischt, z(0) = 4: Zustimmung –
    Lea macht zwei Fehler auf einmal (Maximum statt Minimum, Stelle
    statt Wert), und die 4 fällt mit z(0) zusammen.

Zahlen: Zweitleser 17 Befunde, Erstleser 38, gemeinsam 12, nur
Zweitleser 5. Gezählt sind ids: jede id mit mindestens einem Befund
zählt einmal, auch „fraglich"; beim Erstleser sind das 220 − 182 =
38 ids (seine Punkte 1–6 nennen einige ids mehrfach); gemeinsam
sind die ids, die in beiden Listen stehen; „nur Zweitleser" sind
meine 17 minus die 12 gemeinsamen – in der Sache sind es 3, weil
e1-k2-s4-v2/-v3 beim Erstleser unter v1 mitgemeint sind.
