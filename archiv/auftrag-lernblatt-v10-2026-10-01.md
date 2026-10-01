# Auftrag: Lernblatt-Rezept v1.0 im Zusammenbau (Befunde des Lehrers am Blatt TER-L4)

Modell: Opus. Datum des Starts aus `date +%F`.
Stelle keine Rückfragen; was der Auftrag nicht regelt, entscheidest du
selbst und schreibst es in den Bericht.

## Ausgangslage

Repo hz-0801/aufgabenbank, `werkzeuge/zusammenbau.py` v0.9 (Commits
4c5f971 … c2a80b9 vom 30.09., Auftrag in
`archiv/auftrag-lernblatt-v09-2026-09-30.md`, Bericht in
`bau/terme/TER-L4/bericht.md`). Der Lehrer hat das Blatt TER-L4 neben
das Blatt des alten Prompts gelegt
(hz-0801/mathe-nachhilfe, `blaetter/testlauf-2026-09-26/10-ka-terme-8-gym/`)
und die folgenden Befunde gegeben. Sie gelten für das Lernblatt
(Rezept L); wo das Kompetenzblatt (K) dieselbe Funktion nutzt, darf
es sich mitändern, muss aber weiter bauen. Nichts in `bank/`,
`mappen/`, `bank.md`, `mathblatt.sty` ändern; eine Katalogänderung
(Punkt 1) geschieht im Repo mathe-nachhilfe.

## Befunde und Regeln (so umsetzen)

1. Blattfolge (Katalog, Repo mathe-nachhilfe). `katalog/terme.md`
   bekommt im Abschnitt „Lerneinheiten" nach der nummerierten Liste
   eine Zeile `Blattfolge: 2, 3, 4, 1` (Reihenfolge der Einheiten auf
   dem Lernblatt; die Nummern der Einheiten und die Bank-Kennungen
   bleiben). `katalog/_vorlage.md` bekommt die Zeile als optionales
   Element mit einem Satz Erklärung (fehlt sie, gilt die
   Katalogreihenfolge). `werkzeuge/mappe.py` übernimmt die Zeile in
   die Mappe (Abschnitt Lerneinheiten); baue die Mappe terme neu.
   Das Skript liest die Blattfolge aus der Mappe und setzt die
   Einheiten in dieser Reihenfolge (Nummern laufen durch; Kopfzeile
   und Titel nennen die Katalognummer nicht mehr, siehe 7). Innerhalb
   von Einheit 1 steht die Kette „Termwert berechnen" vor „Term
   aufstellen" (allgemeine Regel: Typen ohne Kette mit hoehe sprosse
   vor den Verfahrensketten, wenn die Blattfolge die Einheit nach
   hinten stellt – oder einfacher und so umsetzen: innerhalb jeder
   Einheit zuerst die Ketten ohne Textaufgabe im Grundfall, dann die
   mit; log FOLGE je Einheit).

2. Keine Verzeichniszeile. Weder im Gesamt noch in den Teilen; die
   doppelte Überschrift „Das kennst du schon" entfällt damit.

3. Auftrag nur bei Mehrdeutigkeit. Ein Auftragssatz („Rechne.",
   „Fasse zusammen.", „Löse die Gleichung.") steht nur, wenn der Term
   allein mehrdeutig ist: Gleichungen (lösen/umformen), Terme in
   Einheiten mit mehreren Verfahren (ausklammern/zusammenfassen/
   Klammern auflösen). Nackte Rechnungen mit „=" („−8 − 6 =")
   bekommen keinen Auftrag. Umsetzung: Die Anweisung aus
   `bau/regal/ich-kann.csv` bzw. die Ersatzanweisung entfällt, wenn
   die Teilaufgabe form teil ist, ein „=" trägt oder eine reine
   Zahlrechnung ist (kein Buchstabe außer Einheiten) und der Titel
   der Hauptnummer die Handlung schon nennt. Steht ein Auftrag, dann
   wie bisher einmal über der Nummer bei nackten Termen und
   Gleichungen; bei Teilaufgaben mit Bedingung oder Kontext („4x − 3
   für x = 5", Sachtext) dagegen je Teilaufgabe ein ganzer Satz
   („Berechne den Wert von 4x − 3 für x = 5.") – der Auftrag einmal
   oben gilt nur für nackte Terme und Gleichungen. Prüfung AUFTRAG
   bleibt für den Fall nackter Terme.

4. Titel ohne „Ich kann". Die Titel der Hauptnummern sind die
   Fertigkeit im Infinitiv: aus „Ich kann negative Zahlen addieren und
   subtrahieren." wird „Negative Zahlen addieren und subtrahieren";
   aus „Ich kann einen Term aufstellen." wird „Einen Term aufstellen".
   Umformung maschinell aus ich-kann.csv (Präfix „Ich kann " ab, Punkt
   ab, erster Buchstabe groß); Fälle, die so keinen Infinitiv ergeben
   („Ich finde den Fehler …", „Ich erkenne …"), bekommen eine Spalte
   `titel` in ich-kann.csv (für terme füllst du sie), sonst log
   TITEL. Die Abhakliste „Das kann ich" entfällt (siehe 10).

5. Keine Zweigzeile, keine Zeitmarke. Je Einheit nur der Titel
   (Kopfzeile wie bisher „Terme · Lernblatt · <Einheitstitel>").
   „Hier lernst du …", Marken, Prüfungswort, „baut auf" entfallen –
   auch mit `--klasse`. Prüfungsaufgaben tragen ihre Marke wie bisher
   an der Aufgabe. Typen, die der Katalog mit einer Klammer nur dem
   Gymnasium zuordnet („[GYM 8]" in „Typen je Lerneinheit" ohne
   OS-Angabe), bekommen rechts im Titel der Hauptnummer klein „GYM"
   (wie die Prüfkennung; log GYM je Nummer; fehlt die Zuordnung,
   nichts).

6. Striche für den Rechenweg: gleiche Stärke wie die Antwortlinie,
   Länge wie der Antwortstreifen (nicht die ganze Breite), eine
   Zeile Luft zwischen Aufgabentext und erstem Strich bzw.
   Antwortfeld (Befund 13 des Lehrers: die Linie klebt am Text).

7. Kein „Einheit n von m": weder im Einheitenkopf noch in der
   Kopfzeile; der Einheitstitel allein.

8. Ankreuzaufgaben in voller Breite; zwei nebeneinander nur, wenn
   beide kurz sind (Text und Optionen zusammen bis 120 Zeichen
   Quelltext). Kein Umbruch mitten im Satz durch halbe Breite.

9. Kein „– weiter". Eine Hauptnummer läuft über die Seite. Teilung
   nur, wenn sie mehr als 26 Teilaufgaben hätte; dann an einer
   Sprossengrenze, und der zweite Teil trägt als Titel die Fertigkeit
   dieser Sprosse (ich-kann.csv, Spalte sprosse), nie „weiter".

10. Test am Kopf jeder Einheit statt „Prüfe dich" und „Das kann ich".
    Jede Einheit beginnt unter dem Titel mit einer Hauptnummer
    „Kannst du das schon? Dann weiter zu ‹Titel der nächsten Einheit
    in Blattfolge›" (letzte Einheit: „Dann bist du fertig"). Inhalt:
    je Verfahrenskette der Einheit eine Teilaufgabe der obersten
    Sprosse ohne Textaufgabe – die höchste Sprosse der Kette, deren
    form nicht text ist und deren aufgabe keinen Sachkontext trägt
    (Heuristik: kein Satz mit mehr als zwölf Wörtern vor dem Term;
    log TEST je Kette mit gewählter Sprosse) –, in einer Variante,
    die im Blatt nicht noch einmal vorkommt (die Bank hält je
    Sprosse drei, je Original zwei; fehlt eine freie, die mit der
    höchsten Variantennummer und log). Die Seite „Prüfe dich" und
    die Abhakliste entfallen, abhaken.tex entfällt. In der Lösung
    steht je Testaufgabe „richtig → Nr. a–b überspringen" mit den
    Nummern der Kette.

11. Pflichtelemente sparsam. Je Einheit je Sorte (fehler,
    begruenden, darstellung, anwendung) eine Teilaufgabe, nicht
    drei; die Sorten einer Einheit stehen zusammen in einer
    Hauptnummer am Ende der Einheit mit dem Titel „Verstanden?"
    (Anwendung zuletzt). Die übrigen Bankzeilen bleiben für Fokus
    und Wiederholung.

12. Textaufgaben sparsam. Je Verfahrenskette höchstens eine
    Teilaufgabe mit Sachkontext (Heuristik wie in 10): die oberste
    Sprosse bzw. die Prüfungshöhe; weitere Textsprossen derselben
    Kette entfallen (log TEXT je Kette mit den ausgelassenen ids).
    Dazu die eine Anwendung aus 11. Ein neuer Schalter
    `--mit-sachaufgaben` hebt die Grenze auf.

13. Grafik links, Antwort rechts (Befund 27 des Lehrers): Bei einer
    Teilaufgabe mit Grafik steht das Antwortfeld rechts neben der
    Grafik, mit Bezeichner, wenn die Bankzeile ein Antwortgerüst
    trägt („A = ____ cm²"); nie als lose Linie darunter.

14. Lösungen am Ende des Gesamt: `<K>-gesamt.tex` endet mit einem
    Abschnitt „Lösungen" auf neuer Seite (Inhalt wie
    `<K>-loesungen.tex`, nach Nummern), die getrennte Lösungsdatei
    bleibt. Kopfzeile dort „Terme · Lernblatt · Lösungen".

15. Bankbefund (nicht ändern, nur melden): terme „Term aufstellen"
    Grundfall-Zeilen – „Kreuze den Term an, der dazu passt." sagt
    „dazu", bevor der Text kommt; Vorschlag „Welcher Term passt?
    Kreuze an." in die Gegenlese von terme (Bericht).

## Schritte

1. Klone aufgabenbank, blattbau, mathe-nachhilfe nebeneinander
   (`/home/claude/agent-lernblatt2/`); `which xelatex pdftotext
   pdffonts pdftoppm`, sonst `apt-get` nach `werkzeuge/render.md`.
   Lege diesen Auftrag als `auftrag-lernblatt-v10.md` in die Wurzel
   von aufgabenbank, Commit.
2. Lies `werkzeuge/zusammenbau.md` (Abschnitt Rezept Lernblatt v0.9
   und Kompetenzblatt), `bau/terme/TER-L4/bericht.md`,
   `bau/layout-befunde.md`, die betroffenen Teile von
   `zusammenbau.py`, `katalog/terme.md` und `katalog/_vorlage.md`.
3. Katalog (Punkt 1) in mathe-nachhilfe: Zeile, Vorlage, Commit mit
   Anlass „Blattfolge terme (Lehrer 01.10.)"; `git pull --rebase`,
   Push. Dann mappe.py und Mappe terme in aufgabenbank, Commit.
4. Skript v1.0 nach den Punkten 2–14. Regeln wie im Auftrag v0.9:
   `%% TODO` statt geratenem Text; Kompilierfehler im Skript beheben,
   nie in der Bankzeile.
5. Bau terme mit Registerzeile (nächste TER-L<n>), xelatex zweimal je
   Dokument (<K>-gesamt, <K>, <K>-blatt0, <K>-loesungen), PNG je
   Seite des Gesamt (pdftoppm -r 80), Messwerte in bau.json
   (`bau/terme/lernblatt-messen.py` nachziehen). Regressionsprobe
   wie beim v0.9-Auftrag: prozentrechnung und quadratische-
   gleichungen ohne Register (Struktur, ein Kompilierlauf des
   Gesamt), Kompetenzblatt PRZ Prozentsatz ohne Register (muss
   bauen; Änderungen gegenüber v0.9 im Bericht nennen).
   Zählgrenzen: sechs Kompilierdurchläufe je Dokument, drei
   Nachbesserungsrunden am Skript.
6. Prüfungen (Bericht nennt jede mit Ergebnis): 0 Kompilierfehler, 0
   Missing character, 0 Overfull; kein Bank-Wort, kein TODO im PDF;
   kein „Ich kann" und kein „weiter" und kein „Einheit n von" im
   PDF-Text; keine Zeile „Hier lernst du"; Reihenfolge der Einheiten
   im Gesamt = 2, 3, 4, 1; jede Einheit beginnt mit „Kannst du das
   schon"; je Einheit höchstens vier Pflicht-Teilaufgaben; je Kette
   höchstens eine Sachkontext-Teilaufgabe außer mit
   `--mit-sachaufgaben` (zweiter Probelauf ohne Register, Zahl
   nennen); Gegenprobe mit bekannten Werten: Einheit 2 hat die Ketten
   Zusammenfassen und Malnehmen → der Test von Einheit 2 hat genau
   zwei Teilaufgaben; „Termwert berechnen" steht in Einheit 1 vor
   „Term aufstellen"; Grundfall Zusammenfassen vier Teilaufgaben;
   `bau/prozentrechnung/kennung-probe.py` für die neue Kennung;
   zwei gleiche Aufrufe wortgleich.
7. Doku: `werkzeuge/zusammenbau.md` Abschnitt „Rezept Lernblatt
   (v1.0)" mit den Regeln 2–14 in Kurzform und Versionszeile;
   `bau/layout-befunde.md` am Ende ein Abschnitt „Befunde des
   Lehrers 01.10. am TER-L4" (die 15 Punkte je eine Zeile, Status
   umgesetzt/offen); Bericht `bau/terme/<K>/bericht.md` mit
   Vorher/Nachher (TER-L4 gegen neu: Hauptnummern, Teilaufgaben,
   Seiten je Einheit), Prüfungen, Abweichungen, Annahmen, Befunde
   an Bank/Mappe/Katalog, Offenes.
8. Abschluss: Auftrag nach `archiv/auftrag-lernblatt-v10-<date +%F>.md`
   (git mv); Commit je Teil mit Anlass („Lernblatt v1.0: …"); vor
   jedem Push `git pull --rebase`, `git push origin main`, kein
   Branch; `.gitattributes` mit `*.pdf binary` im Ordner. Kopiere
   `<K>-gesamt.pdf`, `<K>-loesungen.pdf`, `<K>-blatt0.pdf`,
   `bericht.md` nach `/home/claude/out2/`.

## Regeln

- Linux-Shell, `date`, Python 3; UTF-8 ohne BOM, LF; md-Zeilen bis
  72 Zeichen (Datenzeilen ausgenommen).
- Keine Rückfragen; nach zwei gescheiterten Anläufen offen mit
  Grund, nächster Teil. Zählgrenzen, keine Zeitgrenzen.
- Commit-Nachrichten enden mit
  `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` und
  `Claude-Session: https://claude.ai/code/session_01R1Gp3xLQBoDLjn3827uckA`.

## Bericht (Rückgabe an den Chat)

Erste Zeile: Modell. Dann Kennung, Commits (Hash, Anlass, Repo),
Vorher/Nachher-Tabelle, Ergebnis jeder Prüfung, Abweichungen vom
Auftrag mit Grund, Annahmen, Befunde an Bank/Mappe/Katalog, Offenes.
Letzte Zeile: Pfad der PDFs und ob die Pushes durch sind.
