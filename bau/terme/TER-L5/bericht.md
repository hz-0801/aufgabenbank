# Lernblatt Terme TER-L5 – Bericht (zusammenbau v1.0)

Stand 2026-10-01. Auftrag: archiv/auftrag-lernblatt-v10-2026-10-01.md
(Befunde des Lehrers am TER-L4). Gebaut mit
`python3 werkzeuge/zusammenbau.py terme` (Skript 54aaeb3), gemessen mit
`python3 bau/terme/lernblatt-messen.py bau/terme/TER-L5` (xelatex je
Dokument zweimal, pdftoppm -r 80). Vorlage mathblatt.sty 2026-09-28a,
unverändert. Mappe terme mit Katalog-Commit 3f1a389 (mathe-nachhilfe,
Zeile „Blattfolge: 2, 3, 4, 1“). Modell: Claude Opus 5.5.

## Vorher und nachher

HN: Hauptnummern, TA: Teilaufgaben, S.: Seiten des Einzeldokuments
(<K>-e<n>.pdf; Zone <K>-blatt0.pdf). Einheiten in der Folge von
TER-L5.

| Teil | TER-L4 HN/TA/S. | TER-L5 HN/TA/S. |
| --- | --- | --- |
| Zone | 5 / 18 / 1 | 5 / 18 / 1 |
| e2 Terme zusammenfassen | 12 / 48 / 4 | 9 / 42 / 3 |
| e3 Klammern auflösen | 8 / 26 / 4 | 5 / 19 / 2 |
| e4 Ausklammern | 9 / 37 / 4 | 7 / 28 / 3 |
| e1 Terme aufstellen und berechnen | 9 / 28 / 4 | 6 / 20 / 3 |
| Prüfe dich | 5 / 5 / – | entfällt |
| Gesamt | 48 / 162 / 18 | 32 / 127 / 14 |
| davon Lösungen im Gesamt | – | 2 Seiten |
| Lernblatt ohne Zone (<K>.pdf) | 18 Seiten | 11 Seiten |
| Lösungen (<K>-loesungen.pdf) | 4 Seiten | 2 Seiten |

Weniger HN: kein „– weiter“ (Zusammenfassen, Malnehmen, Ausklammern je
eine Leiter), die vier Pflichtnummern je Einheit sind eine
(„Verstanden?“), dazu je Einheit der Test. Weniger TA: Pflicht 12 → 4
je Einheit; Sachaufgaben e1 und e4 (3 ausgelassen); der Test bringt 1–2
TA je Einheit dazu.

## Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| Kompilierfehler (Gesamt, Blatt, Blatt 0, Lösungen, 4 Einheiten) | 0 |
| Missing character / Overfull | 0 / 0 |
| Bank-Wort im PDF-Text, TODO im PDF-Text | 0 / 0 |
| „Ich kann“ im PDF-Text (Gesamt) | 0 |
| „weiter“ im PDF-Text | nur „Dann weiter zu“ (3 Tests) und die Lösung 5a der Zone aus der Bank („um 5 weiter nach unten“) |
| „Einheit n von“ / „Hier lernst du“ | 0 / 0 |
| Folge der Einheiten im Gesamt | 2, 3, 4, 1 |
| Jede Einheit beginnt mit „Kannst du das schon“ | 4 von 4 (Nr. 6, 15, 20, 27) |
| Pflicht-TA je Einheit (höchstens 4) | 4, 4, 4, 4 |
| Sachkontext-TA je Kette (höchstens 1) | Term aufstellen 1 (s6), Ausklammern 1 (s9), sonst 0 |
| dasselbe mit `--mit-sachaufgaben` (Probe ohne Register) | 5 (Term aufstellen 2, Ausklammern 3); 32 HN, 130 TA |
| Gegenprobe Test Einheit 2 (Ketten Zusammenfassen, Malnehmen) | 2 TA |
| Gegenprobe „Termwert berechnen“ vor „Term aufstellen“ | ja (Nr. 28 vor Nr. 29) |
| Gegenprobe Grundfall Zusammenfassen | 4 TA (Nr. 10 a–d) |
| AUFTRAG (nackte Terme, kein Auftrag zweimal in einer Nummer) | 1: Nr. 17 „Löse die Klammer auf.“ (unten) |
| kennung-probe.py TER-L5 | 0 Fehler (127 TA, 32 HN, 8 Dokumente) |
| zwei gleiche Aufrufe | *_a.tex, *_l.tex, vorspann.tex wortgleich, Aufgabenliste gleich |
| Regression prozentrechnung (ohne Register, Gesamt einmal) | 0 Struktur-, 0 Kompilierfehler, 0 fehlende Zeichen; 62/206 → 37/163 HN/TA |
| Regression quadratische-gleichungen | ebenso 0/0/0; 51/170 → 33/141 HN/TA |
| Kompetenzblatt PRZ Prozentsatz (ohne Register) | baut, 3 Seiten, 0 Fehler; Quelltexte bis auf die Versionszeile gleich |
| Fokus, schwach (terme, Probe) | Quelltexte bis auf die Versionszeile gleich |

## Was auf dem Blatt anders ist

- Einheiten in der Folge Zusammenfassen, Klammern, Ausklammern,
  Aufstellen und Berechnen; Kopf nur der Titel, Kopfzeile „Terme ·
  Lernblatt · <Titel>“; keine Verzeichniszeile, keine Zweigzeile.
- Titel im Infinitiv („Terme zusammenfassen“, „Den Fehler beim Rechnen
  mit negativen Zahlen finden“).
- Jede Einheit beginnt mit „Kannst du das schon? Dann weiter zu …“, je
  Kette eine Aufgabe der Prüfungshöhe in einer freien Variante; die
  Lösung sagt „richtig → Nr. 10–11 überspringen“.
- Blatt 0 ohne „Rechne.“: „4 − 9 = ____“ steht allein unter dem Titel.
- „Termwert berechnen“ als ganze Sätze je Teilaufgabe („Berechne den
  Wert des Terms 4x − 3 für x = 5.“), ebenso Ankreuz- und
  Erkennungsaufgaben mit Bedingung.
- Rechenweg-Striche schwarz, halbe Breite, eine Zeile Luft; Figur,
  Termbaum und Tabelle links, Antwortfeld rechts daneben.
- „Verstanden?“ am Ende jeder Einheit: Fehler, Begründen, Darstellung,
  Anwendung je eine.
- Lösungen auf den letzten zwei Seiten des Gesamt.

## Abweichungen vom Auftrag

1. Prüfung AUFTRAG ergibt 1 statt 0: In der Leiter „Klammern“ (Nr. 17)
   unterbrechen die Sprossen „mit der Tabelle“ und „auf zwei Wegen“ die
   Folge der Aufgaben „Löse die Klammer auf: …“; der Auftrag steht vor
   a) und wieder vor f). Ohne Teilung (Befund 9) und ohne Umsortieren
   der Sprossen geht es nicht anders; der Schüler braucht den Auftrag
   nach dem Wechsel wieder.
2. Commit-Zeile „Co-Authored-By“ mit dem Modell, das lief (Opus 5.5),
   nicht Fable 5.1.
3. Der Katalog-Commit in mathe-nachhilfe (3f1a389) ließ sich nicht
   pushen (keine Rechte der Sitzung); die Mappe ist aus dem lokalen
   Klon gebaut (mappe.py, MATHE_NACHHILFE) und nennt diesen Commit.
4. Die Zeile „Blattfolge“ steht an der Stelle der Leerzeile unter der
   Liste: Eine eingefügte Zeile hätte alle Zeilennummern darunter
   verschoben, und das Feld quelle der Bank (Zeilennummer) zeigte auf
   die falsche Zeile (bank-pruef --katalog: 227 Abweichungen).
5. Der Bau trägt bank_commit 54aaeb3; danach bekam das Skript feste
   Ersatzsätze im Infinitiv (17c4b5e). Die Quelltexte von terme sind
   damit wortgleich (Probe), die Änderung wirkt in prozentrechnung und
   quadratische-gleichungen (Zone-Paar).

## Annahmen

1. Textaufgabe im Grundfall (Folge der Ketten): form text oder ein Satz
   vor dem ersten Auftrag. Sachkontext (Test, Grenze je Kette): mehr als
   zwölf Wörter vor dem ersten Auftrag, Mathe als ein Wort.
2. Eine Kette mit mehreren Sachaufgaben behält die mit der höchsten
   Sprosse; der Grundfall bleibt immer. Folge: Ausklammern behält „Nora
   … Faktor nur aus einem Glied gezogen“ (s9) und verliert die
   Rechtecke (s7) und den Rabatt (s8); Term aufstellen behält „drei
   Anweisungen“ (s6) und verliert „Hefte und Stifte“ (s4).
3. Test: Prüfungshöhe zählt als oberste Sprosse; kleinste freie
   Variante. Einheit 1 hat nur eine Verfahrenskette (Term aufstellen);
   „Termwert berechnen“ ist ein Typ ohne Kette und steht nicht im Test.
4. „Überspringen“ nennt alle Nummern der Kette, Vorstufen eingeschlossen
   (Ausklammern Nr. 22–25), ohne „Verstanden?“.
5. Der Zone-Verweis zeigt auf die erste Nummer der Einheit, also auf den
   Test (Nr. 6), wie die Regel aus v0.9 es sagt.
6. GYM nur, wenn alle Teilaufgaben einer Nummer zum Typ gehören. In
   terme betreffen „Term mal Term“ und „Minusklammer“ nur einzelne
   Sprossen der Leitern Malnehmen (Nr. 12 f) und Klammern (Nr. 17 e–g):
   keine Marke, log GYM.
7. „Auftrag nur bei Mehrdeutigkeit“: Die Anweisung entfällt bei form
   teil mit „=“ oder reiner Zahlrechnung, wenn der Titel ein Verb im
   Infinitiv trägt; terme betrifft das nur Blatt 0.
8. Ganze Vorstufen nebeneinander nur bis 45 Zeichen, damit kein Satz in
   der halben Spalte umbricht (Befund 8 sinngemäß auf Vorstufen).
9. Rechenweg-Striche: „Länge wie der Antwortstreifen“ gelesen als halbe
   Textbreite (die Antwortspalte des Kompetenzsatzes).
10. Blattfolge nur im Lernblatt (L); Fokus und schwach behalten die
    Katalogfolge.

## Befunde an Bank, Mappe, Katalog (nicht geändert)

1. bank/terme/e1 k1 Grundfall (Term aufstellen): „Kreuze den Term an,
   der dazu passt.“ sagt „dazu“, bevor der Text kommt – jetzt steht der
   Satz in jeder Teilaufgabe. Vorschlag für die Gegenlese terme:
   „Welcher Term passt? Kreuze an.“
2. bank/terme/e4 k1 („Was steckt in jedem Glied?“): vier verschiedene
   Formulierungen, je mit „Klammere nichts aus.“ (Befund aus TER-L4
   bleibt).
3. quadratische-gleichungen Einheit 4 (Sachaufgaben): nur Textsprossen,
   darum kein Test (log TEST); prozentrechnung und
   quadratische-gleichungen haben keine Zeile „Blattfolge“
   (Katalogfolge).
4. ich-kann.csv, Spalte titel: nur für terme gefüllt. prozentrechnung
   und quadratische-gleichungen bauen ohne log TITEL; andere Einträge
   zeigt der erste Bau (log TITEL, bau.json titel_fehlt).

## Offen

- Push des Katalog-Commits 3f1a389 in mathe-nachhilfe (lokal in
  /home/claude/agent-lernblatt2/mathe-nachhilfe).
- Auftrag zweimal in Nr. 17 (Klammern): Sprossenfolge der Bank oder
  Hinnahme.
- Test der Einheit 3 und 4 je nur eine Teilaufgabe (eine
  Verfahrenskette).
- Antwortfeld neben der Grafik auf halber Höhe geschätzt (Höhe aus den
  Koordinaten), nicht gemessen.
