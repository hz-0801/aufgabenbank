# Zweitlesung rekonstruktion-von-bestaenden

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 122 (zone 22, e1 41,
e2 32, e3 27)

Prüfung: Jede Zeile der vier Dateien wurde vollständig gelesen. Alle
pruef-Ausdrücke wurden ausgewertet und gegen die Lösungszahl
verglichen; jedes Integral, jede Stammfunktion, jede Nullstelle,
jeder Vorzeichenwechsel und jeder Bestandswert wurde mit sympy aus
dem Aufgabentext neu berechnet (auch die Kettenfaktoren bei sin und
e hoch 0,5t, die Diskriminante in e1-k2-s1-v3, die Integrale 18
und −54 in den Begründungen von e2, die falschen Zwischenwerte der
Fehler-finden-Zeilen). Bei allen 22 Grafiken wurde die Funktion
gegen die Werte der Lösung und gegen den Achsenbereich geprüft
(Nullstellen, Ablesewerte, Dreiecks- und Trapezflächen, Endpunkte
der Kurven). Die Originale wurden mit Abschnitt 2 der Mappe
verglichen (Verfahren gleich, Zahlen und Kontext anders; keine
Zahl aus Merkkasten oder Original übernommen). Dubletten wurden über
aufgabe, grafik und die Funktionsterme der Grafiken gesucht.
bank-pruef.py v0.5: 0 Abweichungen, 0 Warnungen in allen vier
Dateien. Ankreuzzeilen: 10, in allen nennt loesung genau eine
Option wortgleich und sie ist die richtige. Fehler-finden-Zeilen:
10, in allen ist der eingebaute Fehler falsch (die Fehlrechnung
ergibt den genannten Wert, etwa 870 bei Mila) und die richtige
Rechnung stimmt. Rechenfehler: keiner.

## Befunde

e3-k1-s3-v3: Text wortgleich mit e3-k1-s3-v1 (Wasser, Becken, m³ je
Stunde; nur die Grafik unterscheidet die beiden), und die Grafik
ist Zeichen für Zeichen die von e3-k1-s1-v4 (t − 2 auf [0; 5],
gleicher Achsenbereich) – dort wird dieselbe Flächengleichheit 0–2
gegen 2–4 als Änderung null gelesen, hier als T = 4 markiert. Die
Zeile ist damit zweimal halb doppelt. – Vorschlag: anderen Kontext
(etwa Öl in einem Tank, Liter je Minute) und andere Gerade, z. B.
r(t) = 1,5t − 3 auf [0; 5] mit ymin=−4, ymax=5: Nullstelle 2,
T = 4, Flächen 3 und 3.

e1-k1-s3-v3, e2-k3-s3-v1, e3-k1-s3-v2, e2-k1-s0-v2, e3-k2-s3-v2,
e2-k1-s3-v2: dieselben Ratenfunktionen kehren über die Einheiten
wieder – 2 − 0,5t dreimal (in e1 und e2 mit identischem
ksys-Aufruf auf [0; 6]), t − 3 zweimal auf [0; 6] mit gleichen
Achsen, dazu 3 − t in e3-k1-s3-v1 und als Lösungsgrafik von
e3-k2-s3-v1; die Rate 4t + 2 steht in e1-k1-s2-v1 und e2-k1-s3-v2.
Ein Blatt, das aus mehreren Einheiten zieht, zeigt dann dasselbe
Bild zweimal. – Vorschlag: Steigungen und Achsenabschnitte je
Vorkommen variieren (z. B. 3 − 0,75t, 0,5t − 2, 2t − 6).

e1-k1-s6-v3, e1-k1-s6-v4, e1-k1-s6-v5, e3-k1-s4-v3, e3-k1-s4-v4:
sprosse_text nennt nur den ersten Teil der Prüfungshöhe
(„Modellwert gegen Tabellenwert …" bzw. „Flächengleichheit …
erläutern"), die Zeilen erfüllen aber den zweiten Teil, den der
Katalog mit „und …" anschließt (Zunahme samt mittlerer
Änderungsrate aus der Bestandsfunktion; Nullstelle des
Differenzintegrals gegen den Schnittpunkt abgrenzen). Das merkmal
deckt beide Teile, der sprosse_text nicht. – Vorschlag: sprosse_text
dieser Zeilen auf den Teil des Katalogsatzes setzen, den sie
erfüllen, oder bei allen Zeilen der Prüfungshöhe den ganzen
Katalogsatz mit „und" führen.

e2-k3-s4-v2: „am vierten Tag" ist nicht dasselbe wie t = 4 (Ende
des vierten, Beginn des fünften Tages, wenn t = 0 der Beginn von
Tag 1 ist); die Frage „Welcher Tag?" lässt beide Lesarten zu. –
Vorschlag: fragen „Nach wie vielen Tagen?" und antworten „nach
vier Tagen (t = 4)".

e1-k1-s2-v2, e1-k1-s5-v3: Buchstabe ohne Erklärung – in e1-k1-s2-v2
heißt die Rate c', die Lösung rechnet mit c(0), aber c ist im Text
nicht als Konzentration eingeführt; in e1-k1-s5-v3 verlangt antwort
„V(t) = __", V kommt im Aufgabentext nicht vor. – Vorschlag: „die
Konzentration c(t) … ihre Änderungsrate c'" bzw. „Gib einen Term
für das Volumen V(t) … an".

e3-k1-s4-v1, e3-k1-s4-v2: die Flächen I, II, III werden nur in
Worten beschrieben („links vom Schnittpunkt", „unter beiden"),
eine Abbildung fehlt; das Original zeigt die Graphen. Lösbar ist
die Zeile, aber die Schüler müssen das Bild erst im Kopf bauen. –
Vorschlag: ksys mit zwei Kurven e und a (etwa e = 0,5t·(12 − t)
mit Hochpunkt links, a gespiegelt) und Beschriftung I, II, III;
sonst „Skizziere zwei solche Graphen" in den Auftrag nehmen.

e3-k2-s1-v3: Radfahrer mit p = 8 km/h und q = 2t km/h, t in
Stunden – die Streckengleichheit liegt bei z = 8, also nach acht
Stunden Fahrt mit linear steigender Geschwindigkeit; die
Größenordnung ist unrealistisch. – Vorschlag: m/s und Sekunden
(p = 8, q = 2t; Schnittpunkt 4 s, z = 8 s) oder km/h mit
t in Minuten und Umrechnung.

e3-k2-s3-v3: die Grafik zeichnet e und a, die Achse heißt r. –
Vorschlag: ylabel=e,\,a oder „Rate".

e2-k1-s0-v1, e2-k1-s0-v4: die Ankreuzoptionen sind Zahlen (t = 2,5
und t = 5; t = 2 und t = 4), pruef ist aber leer; bank.md verlangt
bei Zahloptionen die Zahl. Das Skript hat die Form „$t = 5$" nicht
als Zahloption gelesen. – Vorschlag: pruef "5" bzw. "4".

Sauber: 99 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k3-s4-v2 (Tag gegen t = 4), e3-k2-s3-v3 (ylabel r
statt e, a), e1-k1-s6-v3/v4/v5 und e3-k1-s4-v3/v4 (Zeilen erfüllen
nicht den sprosse_text).
Nur Zweitleser: e3-k1-s3-v3 (Text gleich v1, Grafik gleich
e3-k1-s1-v4), Wiederkehr derselben Ratenfunktionen und Grafiken
(e1-k1-s3-v3, e2-k3-s3-v1, e3-k1-s3-v2, e2-k1-s0-v2, e3-k2-s3-v2,
e2-k1-s3-v2), e1-k1-s2-v2 und e1-k1-s5-v3 (c und V nicht
eingeführt), e3-k1-s4-v1/v2 (Flächen I–III ohne Abbildung),
e3-k2-s1-v3 (acht Stunden Radfahrt mit linear steigender
Geschwindigkeit), e2-k1-s0-v1/v4 (pruef leer bei Zahloptionen).
Nur Erstleser: e1-k3-s4-v3 (Ladestand über 100 % ab t ≈ 3,06 im
Modellbereich bis 5) – richtig, übersehen; e3-k2-s4-v2 („bleibt
übrig" netto 24 kWh gegen Überschuss nur in den Stunden mit
Erzeugung über 2 kW, etwa 24,7 kWh) – richtig, übersehen; die
Nettolesart ist die der Sprosse, aber die Frage sollte sie
aussprechen.
Widerspruch: Bei e1-k1-s6-v3/v4/v5 und e3-k1-s4-v3/v4 will der
Erstleser die Zeilen durch Varianten nach dem Muster v1/v2
ersetzen; der Zweitleser hält die Zeilen für katalogtreu, weil der
Katalog beide Aspekte mit „und" in derselben Prüfungshöhe nennt
(Zeile 77 und 79 der Mappe, stand.md führt die drei Zeilen ohne
Original als Entscheidung), und will nur den sprosse_text auf den
ganzen Katalogsatz oder den erfüllten Teil setzen – nach der
eigenen Entscheidung des Erstlesers zu mehrteiligen Sprossen
(e1-k1-s4, e1-k1-s5) wäre das auch hier kein Befund unter
Merkmal.
