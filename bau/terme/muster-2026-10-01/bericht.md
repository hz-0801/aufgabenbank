# Musterblatt Terme, von Hand gesetzt – Bericht

Modell: Claude Opus 5.5 (claude-opus-5-5). Datum: 2026-10-01 (aus `date`).

Dateien: `muster.tex` (Blatt und Lösungen in einem Dokument),
`muster.pdf`, `mathblatt.sty` (Kopie aus blattbau, unverändert),
`pruef.py` (Rechenprobe aller Lösungen).

## Zahlen

Seiten gesamt: 8 (7 Seiten Blatt, 1 Seite Lösungen zweispaltig).
Hauptnummern: 29. Teilaufgaben: 115.

| Teil | Nummern | Teilaufgaben | aus Bank | geändert | neu |
|---|---|---|---|---|---|
| Blatt 0 „Das kennst du schon“ | 4 | 15 | 11 | 0 | 4 |
| Terme zusammenfassen (E2) | 7 | 31 | 16 | 0 | 15 |
| Klammern auflösen (E3) | 7 | 32 | 14 | 2 | 16 |
| Ausklammern (E4) | 5 | 19 | 9 | 0 | 10 |
| Terme aufstellen und berechnen (E1) | 6 | 18 | 8 | 1 | 9 |
| zusammen | 29 | 115 | 58 | 3 | 54 |

„Aus der Bank“ heißt: Term und Zahlen wortgleich, der Auftrag steht im
Titel der Hauptnummer statt in der Teilaufgabe, die Prüfkennung klein
rechts statt im Text. Geändert sind zwei Tabellenaufgaben (Zahl mal
Klammer ohne Tabelle) und die Figuraufgabe Rechteck (Feld neben der
Figur).

Aufbau je Einheit: „Kannst du das rechnen? Wenn ja, weiter bei
Aufgabe n“ (n = Prüfungs- bzw. Sachaufgabe, per `\ref`) → Übungen →
Prüfungs-/Sachaufgabe → Für Schnelle → Gemischt.

## Prüfungen

- xelatex: sechs Durchläufe insgesamt; letzter Lauf 0 Fehler,
  0 „Missing character“, 0 Overfull, 0 undefined. Der letzte Lauf meldet
  „Label(s) may have changed“: Es haben sich nur die Seitenzahlen der
  vier Labels geändert, die das Blatt nicht zeigt; die Verweise
  (9, 16, 21, 27) sind richtig (pdftotext geprüft).
- Jede Seite als PNG (80 dpi) angesehen und nachgebessert: Rechenketten
  brechen nur so um, dass auf beiden Seiten mindestens drei Zeilen
  stehen (vorher stand eine einzelne Zeile i) allein oben auf der
  Seite); Figuren mittig neben ihren Feldern; einheitliche Feldbreite
  4,5 cm (Blatt 0: 2 cm).
- `python3 pruef.py`: 116 Proben, 0 Fehler (jede Kette mit sympy,
  Termwerte durch Einsetzen, Textaufgaben über `% pruef:`-Zeilen).
  Gegenprobe: eine absichtlich falsche Lösung (7x + 2x = 8x) wird
  gemeldet. Größter gemeinsamer Faktor beim Ausklammern von Hand
  geprüft.
- Bekannter Mangel, nicht mehr behoben (Laufgrenze erreicht): Seite 7
  trägt nur Nr. 29 „Gemischt“ der Einheit 1 (etwa ein Viertel der
  Seite). Abhilfe für den nächsten Satz: Nr. 26 c (Rechteck) in Nr. 28
  ziehen oder Nr. 24 b streichen; dann passt Nr. 29 auf Seite 6, und das
  Blatt hat 7 Seiten.

## Gegenüber TER-L7 weggelassen (14 Seiten → 8)

- Kopfzeile, Inhaltsverzeichnis, Zweigzeile, Zeitmarken, „Ich kann“,
  „Hängst du hier → Nr.“ – Vorgabe des Lehrers.
- Graue Kästen („Kannst du das schon?“, „Verstanden?“) und der kursive
  Hinweis „Gemischt – erkenne selbst …“ – keine Kästen, keine
  Hervorhebungen; der Test ist jetzt eine normale Nummer.
- Vorstufen: Vorzahl ablesen, Glieder mit Vorzeichen aufschreiben,
  „Was steht vor der Klammer?“, Faktor einkreisen, Zerlegen mit
  vorgegebenem Faktor, Minusklammer mit Zahlen auf zwei Wegen – gehören
  ins Blatt für Schwache. „Gleichartige Glieder erkennen“ blieb (der
  Lehrer nennt es als Beispiel), aber ab c) mit Produkten (3ab/−ab,
  2x²y/−x²y), damit es keine Vorstufe ist.
- Fehler finden, Wahr/falsch-Begründen, Termbaum, Situation zu einem
  Term erfinden, Figur in Worten beschreiben – nur auf Zuruf bzw. zu
  viel Text; Begründen bleibt einmal als Anwendung (Rabatt, E4).
- Grundfall viermal und Teilaufgaben, die sich nur in Zahlen gleichen –
  jetzt höchstens zweimal Grundfall, danach steigt jede Zeile.
- Tabelle beim Ausmultiplizieren (Bild für Schwache) und Paarsatz
  zweier Spalten (unruhig) – jetzt eine Teilaufgabe je Zeile mit
  Gleichheitszeichen in einer Flucht.

## Vorschlagsliste für katalog/terme.md (Sprossen der neuen Aufgaben)

| Einheit | Kette | Sprossentext (Vorschlag) | Beispiel im Muster |
|---|---|---|---|
| 0 | Plus und Minus | eine negative Dezimalzahl subtrahieren | −1,5 − (−4) |
| 0 | Plus und Minus | zwei Minuszeichen mit Dezimalzahlen | −0,4 − 0,8 |
| 0 | Mal mit Vorzeichen | zwei negative Faktoren, einer Dezimalzahl | (−1,5) · (−4) |
| 0 | Punkt vor Strich | Zahl minus Produkt mit negativem Faktor | 2 − 3 · (−4) |
| 2 | Gleichartige Glieder erkennen | Glieder mit zwei Variablen und Potenz sortieren (xy² ≠ x²y) | 2x²y, 3xy², −x²y, 4xy, −xy² |
| 2 | Zusammenfassen | negatives erstes Glied, Vorzahl 1 und zwei Zahlglieder zugleich | −2x + 7 − x − 9 |
| 2 | Zusammenfassen | Potenz und Dezimalvorzahl mit negativem Ergebnis | 1,5x² − 2x + 0,5x − 3x² + 4 |
| 2 | Zusammenfassen | Brüche als Vorzahl, Produktglied ab bleibt eigene Sorte | ½a + 3ab − ¾a − 5ab + 2b |
| 2 | Malnehmen | drei Faktoren, zwei negativ, Potenz entsteht (a³) | (−2a) · 3ab · (−a) |
| 2 | Malnehmen | Bruch als Vorzahl, zwei Variablen | −⅔x · 6y · (−xy) |
| 2 | Für Schnelle (neu) | Malnehmen und Zusammenfassen in einem Term | 3x·2y − 4xy + x·(−5y) + 2y·3x |
| 2 | Für Schnelle (neu) | Kantensumme und Volumen eines Quaders als Term | Kanten 2x, 3x, 5 |
| 3 | Minusklammer | Minusklammer mit Dezimalzahlen und negativem erstem Glied | 4,5 − (−x + 2,5y − 1,5) |
| 3 | Minusklammer | drei Klammern mit Potenzen, auflösen und zusammenfassen | −(a² − 2ab) + (3ab − a²) − (−b²) |
| 3 | Zahl mal Klammer | Variable mal Klammer (Potenz entsteht) | 2x · (3x − 4) |
| 3 | Zahl mal Klammer | negative Zahl hinter der Klammer, drei Glieder | (a − 2b + 5) · (−4) |
| 3 | Zahl mal Klammer | Dezimal- bzw. Bruchfaktor mit Variable, drei Glieder | −0,5y · (4y − 6 + 2x); ⅔a · (9ab − 6a + 3) |
| 3 | Auflösen und zusammenfassen | zwei Klammern mit Variable davor | 2a · (a − 3) − a · (5 − a) |
| 3 | Auflösen und zusammenfassen | Klammer in der Klammer | 5x − [2 − 3 · (x − 4)] |
| 3 | Für Schnelle (neu) | dreifach verschachtelte Klammern; Bruchfaktoren vor zwei Klammern | 3x − {2y − [x − (y − 4x)]} |
| 4 | Ausklammern | negativer Faktor mit zwei Variablen, drei Glieder | −6a²b + 9ab² − 3ab |
| 4 | Ausklammern | Dezimalfaktor mit Variable, Eins bleibt in der Klammer | 1,5x³ − 4,5x² + 0,5x |
| 4 | Für Schnelle (neu) | eine Klammer als gemeinsamer Faktor | 4x · (a + b) − 3y · (a + b) |
| 4 | Für Schnelle (neu) | Bruchfaktor mit zwei Variablen ausklammern | ¾x²y − ¼xy² + ½xy |
| 4 | Figur aus zwei Rechtecken | gemeinsame Seite ist ein Term mit Variable (2a), Potenz entsteht | 2a · a + 2a · 5 = 2a · (a + 5) |
| 1 | Termwert | Quadrat bei negativer Einsetzung | x² − 4x für x = −3 |
| 1 | Termwert | zwei Variablen, Bruch als Vorzahl und als Einsetzung | ½a − 3b für a = 6, b = −⅔ |
| 1 | Termwert | Quadrat einer Klammer, zwei Variablen | 2 · (x − y)² − xy für x = −1, y = 2 |
| 1 | Term aufstellen | Figur aus zwei Rechtecken: Fläche und Umfang (Stufenform) | Rechtecke 3x × 2 und x × x |
| 1 | Term aufstellen | Sachtext mit drei Personen, Klammer und Zusammenfassen | Lea, Bruder, Mutter: 3 · (x + x − 3) |

Die Test- und Gemischt-Aufgaben (Nr. 5, 12, 19, 24; 11, 18, 23, 29)
sind Mischungen der Sprossen oben und brauchen keine eigene Sprosse;
die Bank sollte sie als Varianten der höchsten Sprosse führen.

## Annahmen

- Kein Blatttitel über Blatt 0: Die Vorgabe „keine Kopfzeile“ habe ich
  so gelesen, dass auch kein Kopf auf Seite 1 steht; das Thema steht in
  der Fußzeile.
- Titel der Hauptnummer normal gesetzt, nur die Nummer halbfett
  („keine Hervorhebungen“); Einheitentitel groß und halbfett mit Linie.
- „Kannst du das rechnen? Wenn ja, weiter bei Aufgabe n“ springt zur
  Prüfungs- bzw. Sachaufgabe der Einheit (danach Für Schnelle und
  Gemischt), nicht zur nächsten Einheit.
- Einheiten 3 und 4 haben kein P10-Original (Katalog: „keine
  P10-Aufgabe“). Statt „Wie in der Prüfung“ steht dort „Sachaufgabe“ in
  Prüfungsform (Reicht …?) ohne Prüfkennung.
- Ankreuzaufgabe (Nr. 27) ohne Rechenraum; „Rechenraum nur bei …“ als
  Obergrenze gelesen, nicht als Pflicht.
- „Gemischt“ trägt einen Auftrag von zwei Wörtern („vereinfache“, „klammere
  aus oder löse auf“), weil die Zeile „Term =“ sonst offenlässt, ob
  ausgeklammert oder ausmultipliziert wird; keine Erklärung, kein Hinweis.
- Blatt 0 zweispaltig (je Spalte zwei Nummern, Rechnungen
  untereinander), damit es bei der halben Seite bleibt.
- Lange Rechenketten dürfen zwischen zwei Zeilen umbrechen (mindestens
  drei Zeilen auf jeder Seite); alles andere bleibt je Nummer auf einer
  Seite. Ohne das stand auf Seite 1 ein Drittel leer.
- Ziel 8–9 Seiten erreicht (8); mit der Abhilfe oben würden es 7.
- Aus katalog/terme.md habe ich zusätzlich den Abschnitt
  „Voraussetzungen (Blatt 0)“ kurz gelesen, um die vier Fertigkeiten
  von Blatt 0 zu benennen.
- Commit-Trailer mit dem Modell, das tatsächlich lief (Opus 5.5), nicht
  „Fable 5.1“ wie im Auftrag.

## Muster 2 (Entscheidungen des Lehrers 01.10.)

Dateien: `muster2.tex`, `muster2.pdf`; `pruef.py` prüft jetzt auch die
vorgerechneten a) (Zwischenschritt und Ergebnis).

Seiten: 7 (6 Seiten Blatt, 1 Seite Lösungen). Nummern: 19.
Teilaufgaben: 111, davon 58 aus der Bank, 3 geändert, 50 neu.

| Teil | Nummern | Teilaufgaben | Bank | geändert | neu |
|---|---|---|---|---|---|
| Blatt 0 | 4 | 15 | 11 | 0 | 4 |
| 1 Terme zusammenfassen | 3 | 16 | 9 | 0 | 7 |
| 2 Terme malnehmen | 2 | 14 | 6 | 0 | 8 |
| 3 Klammern auflösen | 4 | 30 | 14 | 2 | 14 |
| 4 Ausklammern | 2 | 17 | 9 | 0 | 8 |
| 5 Termwerte berechnen | 2 | 9 | 4 | 0 | 5 |
| 6 Terme aufstellen | 2 | 10 | 5 | 1 | 4 |

Umbau gegenüber Muster 1:
- Die Testnummern und „Für Schnelle“ sind entfallen. Die Aufgaben aus
  „Für Schnelle“ stehen als letzte Teilaufgaben ihrer Nummer, mit der
  Marke „GYM“. Ausnahme ist der Quader: Er mischt Malnehmen und
  Aufstellen und steht deshalb in „Gemischt“ der Einheit 2.
- Prüfungsoriginale:
  - P10 ’23 (Ankreuzen) ist die letzte Teilaufgabe von „Terme
    aufstellen“.
  - P10 ’25 mischt Zusammenfassen und Termwert und steht deshalb in
    „Gemischt“ der Einheit 5.
  - Die Sachaufgaben aus E3 und E4 stehen in „Gemischt“.
- Testaufgaben aus Muster 1:
  - Sechs sind entfallen (E2, E3 und E4 je zwei). Sie lagen auf der Höhe
    der letzten Teilaufgaben.
  - Zwei sind geblieben: 3x² − 2x für x = −½ als Termwert e) und „Die
    Differenz aus dem Fünffachen …“ in „Gemischt“ der Einheit 6.
- „Gemischt“ der Einheit 1 hat zwei neue Aufgaben, weil die bisherigen
  das Malnehmen brauchen; sie stehen jetzt in Einheit 2.
- Teilaufgabe a) ist vorgerechnet: grau am Platz des Antwortfelds, mit
  höchstens einem Zwischenschritt, und sie steht nicht auf der
  Lösungsseite.
- Rechenketten: Der Term steht linksbündig; „=“ und das Feld stehen in
  einer festen Spalte, so breit wie der längste Term der Nummer.
- Bei Text- und Figuraufgaben steht das Antwortfeld direkt hinter dem
  Text bzw. neben der Figur.

Prüfungen:
- xelatex: 2 Durchläufe, 0 Fehler, 0 Missing character, 0 Overfull,
  0 undefined.
- `pruef.py muster2.tex`: 114 Proben, 0 Fehler. Auch Muster 1 ist
  weiter fehlerfrei (116 Proben).
- Alle sieben Seiten als PNG angesehen. Keine Seite trägt nur eine
  Nummer. Die größte Lücke liegt am Fuß von Seite 2 und 6 (etwa ein
  Fünftel); sie entsteht durch die Drittel-Regel bzw. weil „Gemischt“
  nicht geteilt wird.

Annahmen:
- Blatt 0 bleibt ohne vorgerechnete a), ist aber ebenfalls linksbündig
  gesetzt.
- In „Gleichartige Glieder erkennen“ ist a) mit grauen Unterstrichen
  vorgerechnet.
- Die Einheitentitel tragen ihre Nummer („1 Terme zusammenfassen“).
- Die Fußzeile lautet „Terme · Muster 2 2026-10-01“.
- „Gemischt“ der Einheiten 5 und 6 steht ohne Auftrag, weil die
  Teilaufgaben ihn selbst nennen.

## Muster 3 (aus Muster 2: Merkkästen knapp, 14 a Zwischenschritt, = am Term)

Dateien: `muster3.tex`, `muster3.pdf`. Seiten: 7 (6 Seiten Blatt,
1 Seite Lösungen). Nummern und Teilaufgaben wie in Muster 2 (19 Nummern,
111 Teilaufgaben: 58 aus der Bank, 3 geändert, 50 neu).

Merkkästen stehen direkt unter dem Einheitentitel: ein schmaler grauer
Rahmen über die Textbreite, keine Fläche. Die Inhalte stammen aus
katalog/terme.md „Merkkasten“ und „Typische Fehler“; die Achtung-Zeile
zu Einheit 4 kommt aus den Fehleraufgaben der Bank (Eins bleibt stehen),
weil „Typische Fehler“ dazu nichts hat.
1. Zusammenfassen: „Nur gleiche Variablen mit gleicher Hochzahl
   zusammenfassen: Vorzahlen addieren, die Variable bleibt.“ /
   „3x + 5x = 8x   7a − 2a + 4 = 5a + 4   x² + 3x bleibt so“ /
   „Achtung: 3x + 4 ≠ 7x   x + 6x = 7x, nicht 6x“
2. Malnehmen: „Zahlen mal Zahlen, Variablen mal Variablen.“ /
   „3 · 4x = 12x   2x · 3x = 6x²   3a · 2b = 6ab“ /
   „Achtung: x · x = x², nicht 2x“
3. Klammern: „Plus vor der Klammer: Klammer weglassen.
   a + (b − c) = a + b − c“ / „Minus vor der Klammer: alle Vorzeichen
   drehen. a − (b − c) = a − b + c   Achtung: −(x − 4) = −x + 4“ /
   „Zahl mal Klammer: jedes Glied malnehmen. 3 · (x + 4) = 3x + 12“
4. Ausklammern: „Gemeinsamen Faktor vor die Klammer; Probe durch
   Ausmultiplizieren.“ / „6x + 9 = 3 · (2x + 3)   4a² + 2a =
   2a · (2a + 1)“ / „Achtung: 8x − 8 = 8 · (x − 1), die 1 bleibt in der
   Klammer“
5. Termwerte (eine Zeile): „Negative Zahlen in Klammern einsetzen:
   3x² für x = −2: 3 · (−2)² = 12“
6. Aufstellen (eine Zeile): „„um 5 vermindert“: x − 5   „das Doppelte
   der Summe aus x und 5“: 2 · (x + 5), mit Klammer“

Weitere Änderungen:
- Vorgerechnete a) mit Zwischenschritt:
  - 14 a: 5x + 10 = 5 · x + 5 · 2 = 5 · (x + 2)
  - 6 a: 7x + 2x = (7 + 2) · x = 9x
  - 8 a: 5 · 2x = 5 · 2 · x = 10x
  - 11 a, 12 a und 16 a hatten schon einen Zwischenschritt; 10 a hat
    keinen, weil dort kein Schritt dazwischenliegt.
- Rechenketten: „=“ steht direkt hinter dem Term. Nur die Antwortfelder
  stehen in einer festen Spalte, ebenso bei den Termwerten (Term und
  „für x = …:“ zusammen).
- Damit keine Seite nur eine Nummer trägt, ist der Satz etwas enger
  geworden:
  - Rechenraum: Linienabstand 7 statt 8 mm.
  - Textzeilen: 7 statt 9 pt Abstand davor.
  - Stufenfigur in 6 f: auf 80 % verkleinert.
  - Merkkasten von Einheit 6: auf eine Zeile gekürzt.
  - Im zweiten Lauf lag „Gemischt“ der Einheit 6 noch allein auf
    Seite 7; nach diesen Änderungen steht es auf Seite 6.

Prüfungen:
- xelatex: 3 Durchläufe, im letzten 0 Fehler, 0 Missing character,
  0 Overfull, 0 undefined.
- `pruef.py muster3.tex`: 117 Proben, 0 Fehler (die neuen
  Zwischenschritte sind mitgeprüft).
- Alle Seiten als PNG angesehen: keine Seite mit nur einer Nummer. Die
  größte Lücke liegt am Fuß von Seite 5 (etwa ein Fünftel); dort beginnt
  wegen der Drittel-Regel Einheit 6 auf der neuen Seite.

## Muster 4 (Ziel für das Skript: Kopf/Fuß, Abschluss, Schlusstest, a) nur mit Weg)

Dateien: `muster4.tex`, `muster4.pdf`. Seiten: 7 (6 Seiten Blatt,
1 Seite Lösungen). 18 Nummern, 110 Teilaufgaben: 55 aus der Bank,
4 geändert, 51 neu.

| Einheit | Nummern | Teilaufgaben | Bank | geändert | neu |
|---|---|---|---|---|---|
| 0 Das kennst du schon | 1–4 | 15 | 11 | 0 | 4 |
| 1 Zusammenfassen | 5–7 (7 Abschluss) | 16 | 9 | 0 | 7 |
| 2 Malnehmen | 8–9 (9 Abschluss) | 13 | 6 | 0 | 7 |
| 3 Klammern auflösen | 10–13 (13 Abschluss) | 28 | 13 | 2 | 13 |
| 4 Ausklammern | 14 | 12 | 7 | 0 | 5 |
| 5 Termwerte | 15 | 8 | 4 | 0 | 4 |
| 6 Aufstellen | 16–17 (17 Abschluss) | 10 | 5 | 1 | 4 |
| Zum Schluss | 18 | 8 | 0 | 1 | 7 |

Schlusstest (Nr. 18, ungeteilt auf Seite 6, knapp halbe Seite; in der
Lösung je Aufgabe „falsch → Nr. n“):
- a) 5 − 2x² für x = −1,5 (Einheit 5, aus „Gemischt“ von Muster 3) → Nr. 15
- b) 4 · (2a − 3) − (5a − 7) (Einheit 3) → Nr. 12
- c) 2x + 5y − 6x + y (Einheit 1) → Nr. 6
- d) Klammere aus: 14ab − 21b (Einheit 4, aus „Gemischt“) → Nr. 14
- e) 3x · (−2xy) (Einheit 2) → Nr. 8
- f) Fitnessstudio 12 € + 6 € je Besuch, Term (Einheit 6) → Nr. 16
- g) GYM: 2a − {3b − [a − (2b − 3a)]} (wie 12 h) → Nr. 10, 12
- h) P10 ’25: 6b − 3b² − 2b vereinfachen, Wert für b = −2 (wie 15 h,
  neue Zahlen) → Nr. 6, 15

Änderungen gegenüber Muster 3:
- Kopf nur „Terme“ links; Fuß „Seite n von m“ Mitte, „Muster 4
  2026-10-01“ klein links. Keine Linie unter den Einheitentiteln (auch
  nicht unter „Lösungen“).
- „Gemischt“ heißt „Abschluss“, je drei Teilaufgaben mit einer
  Anwendung, nur in Einheit 1, 2, 3, 6. Weggefallen: in 2 „6a + 2b −
  a · 2b“ und die Kantensumme des Quaders (Quader nur noch Volumen,
  ohne GYM); in 3 „−4a · (−2b)“ und das Rahmenband (e3-k3-s4-v2). In
  Einheit 4 und 5 kein Abschluss: 14ab − 21b und 5 − 2x² wandern in den
  Schlusstest; 3a · (2a − 5), 8x − 2 · (3x − 4), Anna/Ben (e4-k2-s8-v1)
  und Trikots (e4-k3-s4-v1) entfallen.
- P10 ’25 (e2-k4-s11-v1) bleibt im Blatt als 15 h, damit der
  Schlusstest die gleiche Art mit neuen Zahlen bringen kann.
- Grau vorgerechnet nur noch 10 a, 11 a, 12 a, 14 a (mit
  Zwischenschritt) und 15 a; 5 a, 6 a, 8 a und 16 a sind normale
  Aufgaben.
- Nr. 16 darf umbrechen (a–f auf Seite 5, g auf Seite 6), damit
  Abschluss 17 und der Schlusstest mit auf Seite 6 passen; sonst lag der
  Schlusstest allein auf einer achten Seite.
- `pruef.py`: Einsetzungen mit Dezimalkomma (x = −1{,}5) werden richtig
  getrennt.

Prüfungen:
- xelatex: 3 Durchläufe, 0 Fehler, 0 Missing character, 0 Overfull.
- `pruef.py muster4.tex`: 112 Proben, 0 Fehler.
- Alle Seiten als PNG angesehen: keine Seite mit nur einer Nummer,
  Schlusstest ungeteilt, Merkkästen höchstens drei Zeilen.
