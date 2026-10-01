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
