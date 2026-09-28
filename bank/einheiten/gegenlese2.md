# Zweitlesung einheiten

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 334
(zone 46, e1 87, e2 59, e3 68, e4 74)

Prüfung: Jede Zeile aus dem Aufgabentext nachgerechnet und mit
loesung und pruef verglichen (Auszug aller Zeilen mit ausgewertetem
pruef, eigene Rechnung dagegen); die Sek-II-Zeilen mit sympy im
Scratchpad: Nullstellen, Stangenlängen und waagerechte Stangen der
drei Gitteraufgaben (e1-k3-s5, Substitution z = x², Monotonie im
Tor), Schnittstellen und Integrale der drei Flächen zwischen zwei
Graphen (e3-k2-s3: 24/5, 12/5, 72/5). Alle pruef-Zahlen stimmen mit
der eigenen Rechnung und nach Rundung mit der loesung (334 von 334;
Zeilen ohne Zahl bei Begründen und Ordnen). Ankreuzzeilen (37: je
Option gegen Text geprüft, jeweils genau eine richtig, loesung
wortgleich) und Fehler-finden-Zeilen (13, dazu die fremden
Rechnungen e4-k1-s9 und e4-k1-s12: Fehler jeweils wirklich falsch,
Richtigrechnung stimmt) einzeln gelesen. Fahrpläne, Stellenwert- und
Einheitentafeln gegen die Grafik gelesen. `werkzeuge/bank-pruef.py
einheiten`: 0 Abweichungen, 0 Warnungen. Nicht als Befund gezählt,
weil in stand.md schon geführt: hoehe sprosse an den letzten
Sek-II-Sprossen e1-k3-s5 und e3-k2-s3 sowie „(FHR 2022)“ in
e4-k2-s4 bei original null.

## Befunde

zone-f2-v3: [M] Merkmal „nur Hundertstel, Einer und Zehntel leer“,
aber 16 Hundertstel = 0,16 hat eine 1 an der Zehntelstelle – das
Merkmal trifft die Aufgabe nicht – Merkmal „mehr als zehn Hundertstel
bündeln“ oder Zahl unter zehn Hundertstel wählen (dann aber Abstand
zum Fallstrick f2-v4 wahren).

zone-f6-v3: [E] „senkrechter Abstand“ zweier Punkte mit
verschiedenen x-Werten (T(1|−1,5), S(0|2,25)) ist kein gebräuchlicher
Begriff; gemeint ist der Höhenunterschied – „Höhenunterschied?“
fragen.

e1-k7-s1-v1: [E] „Runde auf eine Stelle“ lässt offen, ob eine
Nachkommastelle oder eine Stelle insgesamt gemeint ist – „Runde auf
eine Stelle nach dem Komma“ (wie e4-k1-s10).

e2-k4-s1-v3: [E] „spätestens um 17:45 Uhr am Markt“: Bahn 1 (an
17:29) und Bahn 2 (an 17:44) kommen beide rechtzeitig an; die
Lösung nennt nur Bahn 2 – „möglichst spät losfahren“ oder „die
letzte Bahn, mit der sie rechtzeitig ankommt“ ergänzen.

e3-k2-s3-v3: [M] Der Sprossentext verlangt Quadratzentimeter und
Quadratmeter; die Variante rechnet in mm² und cm² (Längeneinheit
5 mm) und ändert damit mehr als Zahl und Kontext – Längeneinheit in
cm geben und in cm² und m² fragen.

e4-k1-s11-v2: [E] „Tom will die 1-l-Dose“ ist keine falsche
Behauptung (1 l reicht auch); „Wer hat recht?“ ist damit nicht
eindeutig – Tom eine prüfbare Aussage geben („Tom meint, 750 ml
reichen nicht“).

e4-k5-s1-v2: [F] Der eingebaute Fehler (4 · 90 = 360 m², m mal cm)
ist „gar nicht angeglichen“, nicht das Muster der Sprosse „nur eine
der beiden Größen umgerechnet“; der Lösungssatz „nur eine Größe
beachtet“ ist unklar – Fehler so bauen, dass eine Größe umgerechnet
ist und die andere nicht, oder den Lösungssatz auf „Zentimeter nicht
in Meter umgerechnet“ kürzen.

Sauber: 327 Zeilen ohne Befund

## Abgleich

Beide Leser:
- zone-f2-v3: Merkmal „Zehntel leer“ passt nicht zu 0,16; beide schlagen ein Merkmal „über zehn Hundertstel bündeln“ vor.
- e2-k4-s1-v3: Bahn 1 und Bahn 2 kommen beide vor 17:45 Uhr an; die Frage braucht „möglichst spät“.
- e3-k2-s3-v3: mm² und cm² statt der im Sprossentext verlangten cm² und m².
- e4-k5-s1-v2: Emil hat gar nicht umgerechnet, das Muster „nur eine der beiden Größen umgerechnet“ trifft nicht.

Nur Erstleser:
- e4-k1-s2-v1: bestätigt (leicht) – 80 mm ist ebenfalls handlicher als 0,08 m; die Lösung sollte 80 mm zulassen oder die Frage „in cm“ stellen.
- zone-f4-v2: bestätigt – 2,35 oder 2,4 ist derselbe Fallstrick (mehr Ziffern, kleiner) wie f4-v4; die sehr leichte Zeile braucht gleich viele Nachkommastellen.
- zone-f5-v1: nicht prüfbar – ob \zahlenstrahl bei xstep 0.1 jeden Strich beschriftet, steht nicht in mappen/_bausteine.md; nur am Satz zu klären.
- zone-f5-v3: bestätigt im Kern – unabhängig von der Beschriftung ist die Zeile gleich gebaut wie der Grundfall f5-v1 (xstep 0.1), das Merkmal „Zwischenstriche zwischen beschrifteten Marken“ unterscheidet sie nicht; die Beschriftungsfrage wie bei f5-v1 offen.
- e1-k2-s3-v3, e1-k2-s4-v3, e1-k2-s5-v3: nicht bestätigt – Kommazahlen stehen in der Kette schon vorher als Ergebnis (s2-v3 6,4 m, s4-v2 2,7 km) und bei Geld (s6) zwingend als Angabe; s8 zielt auf die Stellenwerttafel mit Null (1,07 m), das Merkmal der früheren Sprossen bleibt unberührt – Ermessen, kein Fehler.
- e4-k2-s3-v3: bestätigt – die Variante fügt den Schritt „Flächeneinheit mit quadriertem Maßstab“ hinzu, den v1 und v2 nicht haben; sie ändert mehr als Zahl und Kontext.

Nur Zweitleser:
- zone-f6-v3: „senkrechter Abstand“ zweier Punkte mit verschiedenen x-Werten, gemeint ist der Höhenunterschied.
- e1-k7-s1-v1: „Runde auf eine Stelle“ ist unklar, „nach dem Komma“ fehlt.
- e4-k1-s11-v2: „Tom will die 1-l-Dose“ ist keine falsche Aussage, „Wer hat recht?“ damit nicht eindeutig.

Widersprüche: keine – beide Leser finden keinen Rechenfehler und keinen Ankreuzfehler; abweichend ist nur das Urteil zu e1-k2-s3/s4/s5-v3 (Erstleser Befund, Zweitleser Ermessen).
