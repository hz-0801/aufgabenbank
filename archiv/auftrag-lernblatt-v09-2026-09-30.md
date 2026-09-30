# Auftrag: Lernblatt-Rezept v0.9 im Zusammenbau (Satz wie Kompetenzblatt)

Modell: Opus. Datum des Starts aus `date +%F`.
Stelle keine Rückfragen; was der Auftrag nicht regelt, entscheidest du
selbst und schreibst es in den Bericht.

## Ausgangslage

Repo hz-0801/aufgabenbank: `werkzeuge/zusammenbau.py` v0.8 baut aus
`bank/<eintrag>/` LaTeX-Quelltexte für `mathblatt.sty`
(hz-0801/blattbau). Das Rezept Lernblatt (Aufruf ohne Schalter,
Kennung XXX-L<n>) steht im Satz auf dem Stand v0.1/v0.3: Überschriften
sind Kettennamen (Bank-Wörter), jede Teilaufgabe wiederholt ihren
Auftrag („Fasse zusammen: 7x + 2x" elfmal untereinander), Prüfkennung
in Klammern am Zeilenende, kein Bearbeitungsraum nach Aufgabenart,
Zweigzeile ohne „Hier lernst du …", je Sprosse nur Variante 1
(Grundfall einmal statt viermal, Vorstufe einmal statt vier, Typ ohne
Kette einmal statt dreimal). Das Rezept Kompetenzblatt (v0.7/v0.8,
`--kompetenz`) hat all das gelöst: `satzform`, `zerlege`,
`rechenzeilen`, `lies_ichkann`, `mappe_einheit`, `pruefwort_zahl`,
`kennung_kompetenz`, Vorspann `vorspann.tex` (kbaufgabe, kbteil,
kbfrage, kbantwort, kbpaar, kbwertetabelle, kbmerk, kbloesung),
BANKWORT-Prüfung, `--dicht`. Anleitung: `werkzeuge/zusammenbau.md`,
Layoutregeln: `bau/layout-befunde.md`, Sprachregeln:
`bau/sprachlauf/regeln.md`, Mengen und Felder: `bank.md`.

Vergleichsblatt des alten Prompts (Maßstab für Lesbarkeit und Dichte):
hz-0801/mathe-nachhilfe,
`blaetter/testlauf-2026-09-26/10-ka-terme-8-gym/` – dort
`TermeBinomischeFormeln_Gesamt.pdf` und die Quelltexte `lernblatt.tex`,
`e1_a.tex` … `e5_a.tex`, `zone_a.tex`. Das Blatt trägt zwei Einträge
(terme, binomische-formeln); Maßstab sind seine Terme-Einheiten.
Der Lehrer hat das Bank-Lernblatt Terme (v0.8, Probe TER-L0) daneben
gelegt und drei Dinge gesagt: zu wenige Aufgaben; liest sich schlecht
(der Auftrag wiederholt sich in jeder Teilaufgabe); Layout wie das
alte Blatt gewünscht.

Ziel: Das Lernblatt aus der Bank soll sich lesen wie das alte Blatt –
Ich-kann-Titel, ein Auftrag je Hauptnummer, kurze Terme nebeneinander,
Mengen nach bank.md – und dabei alles behalten, was der Bankweg schon
kann (Kennung, Register, Bauzettel, Blatt 0, Abhakseite, Lösungen).

## Schritte

1. Klone hz-0801/aufgabenbank, hz-0801/blattbau und
   hz-0801/mathe-nachhilfe nebeneinander (das Skript findet
   `mathblatt.sty` und `katalog/_kuerzel.csv` über `../blattbau/` und
   `../mathe-nachhilfe/katalog/`). Prüfe `which xelatex pdftotext
   pdffonts pdftoppm`; fehlt etwas, `apt-get` nach
   `werkzeuge/render.md` (Zählgrenze: zwei Anläufe). Lege diesen
   Auftrag als `auftrag-lernblatt-v09.md` in die Wurzel von
   aufgabenbank und committe ihn (Commit 1).

2. Lies `werkzeuge/zusammenbau.md` ganz, `bau/layout-befunde.md`,
   `bank.md` (Mengen je Kette, Felder), die Kompetenzblatt-Teile von
   `werkzeuge/zusammenbau.py` und das alte Blatt (`lernblatt.tex`,
   `e2_a.tex`, `zone_a.tex` des Vergleichsordners; das PDF nur, wenn
   du Seiten ansehen willst). Baue zuerst die Probe des Ist-Stands:
   `python3 werkzeuge/zusammenbau.py terme --ohne-register --aus
   /tmp/alt` – die Zahlen daraus (Hauptnummern je Einheit,
   Teilaufgaben, Seiten nach xelatex) sind der Vorher-Wert für den
   Bericht.

3. Lernblatt-Rezept v0.9 in `zusammenbau.py`. Kein neues Skript,
   keine Änderung an `bank/`, `mappen/`, `mathblatt.sty`; die anderen
   Rezepte (H, Z, P, K, F, S) bleiben unverändert und müssen weiter
   bauen. Fehlt der Bank oder Mappe etwas, steht es als `%% TODO` und
   in der log, nie als geratener Text.

   a. Mengen nach bank.md statt „Variante 1": Vorstufe alle vier
      Zeilen je Vorstufe; Grundfall vier der fünf Zeilen (Katalog
      „(4×)"; bei anderer Zahl im Katalog diese); jede weitere Sprosse
      eine Zeile (Variante 1; die volle Leiter, keine Sprosse fehlt);
      Prüfungshöhe: je Original eine Aufgabe, jüngste fünf Jahrgänge,
      verschiedene Formulierungen zuerst, bis fünf (Regel des
      Kompetenzblatts, Punkt 4); Prüfungshöhe ohne Original: eine der
      drei Zeilen; Typ ohne Kette: alle drei Zeilen; Erkennungsschritt:
      alle vier; Pflichtelemente je Einheit: je Sorte (fehler,
      begruenden, darstellung, anwendung) eine Hauptnummer mit allen
      drei Zeilen. Eine Hauptnummer je Kette wie bisher, Nummern
      laufen über alle Dateien durch; Teilung nach 2.3 g (höchstens 12
      Teilaufgaben, 6 mit Grafik) jetzt auch im Lernblatt, Fortsetzung
      „– weiter".

   b. Satz je Hauptnummer und Teilaufgabe wie im Kompetenzblatt
      (`satzform`, `zerlege`, `rechenzeilen`, Antwortfeld in eigener
      Zeile, Tabelle unter dem Text, Kreuze je Zeile, Prüfkennung
      klein rechts in der Auftaktzeile über `kennung_kompetenz`,
      Flattersatz, Hauptnummer als unteilbarer Block je Teilaufgabe,
      Vorspann `vorspann.tex` mit Ersatzzeichen). Dazu neu, für beide
      Rezepte (K und L): Haben alle Teilaufgaben einer Hauptnummer
      denselben Auftrag (Muster „Verb: Term", „Verb. Term", gleicher
      Satz vor dem Doppelpunkt), steht der Auftrag einmal unter dem
      Titel der Hauptnummer, die Teilaufgaben tragen nur den Term
      bzw. den Rest; Abweichungen einer einzelnen Teilaufgabe
      (Prüfkennung, Zusatzfrage) bleiben an ihr. Kurze Teilaufgaben
      ohne Grafik, ohne Kreuze und ohne Prüfkennung (Term oder
      Gleichung bis etwa 30 Zeichen Quelltext, wie Nr. 5 und 6 des
      alten Blatts) stehen zwei je Zeile mit „=" und Antwortfeld
      (Baustein `kbpaar` oder ein neuer im Vorspann; Muster: alte
      `e2_a.tex`); längere untereinander (Befund 6). Bearbeitungsraum
      nur bei Rechnen und Begründen (Befund 9).

   c. Titel: jede Hauptnummer trägt den Ich-kann-Satz aus
      `bau/regal/ich-kann.csv` (`lies_ichkann`; Sprosse leer = Titel
      der Kette, einheit 0 = Fertigkeit der Zone); fehlt die Zeile,
      „Ich kann: <merkmal>." und log ICH-KANN fehlt. Für terme fehlende
      Zeilen ergänzt du in ich-kann.csv (Spalte quelle „auftrag
      lernblatt v0.9"), aus Kettenname, merkmal, sprosse_text und der
      Mappe – Muster die Titel des alten Blatts (nicht wortgleich
      übernehmen, wo die Sprosse anders geschnitten ist).

   d. Zweigzeile je Einheit: „Einheit n von m · <Titel> · Hier lernst
      du, <Beschreibung> · <Zeitmarke> · <Prüfungswort> · baut auf:
      <Voraussetzungen>". Beschreibung aus der Lerneinheiten-Zeile
      der Mappe (Abschnitt „Lerneinheiten"; der alte Prompt hat sie
      aus demselben Katalogtext gebildet, siehe Zweigzeilen in
      `lernblatt.tex`), Zeitmarke und Prüfungswort wie bisher
      (`pruefwort_zahl`), „baut auf" aus den Voraussetzungen der
      Mappe, die diese Einheit nennen; Wortlaut wie im Katalog, nur
      „Hier lernst du," davor. Kein Kettenname, kein Bank-Wort.

   e. Blatt 0: Überschrift „Das kennst du schon", je Fertigkeit eine
      Hauptnummer mit Ich-kann-Titel (einheit 0), Inhalt wie bisher
      (Sprosse 1 und 2, das Zone-Paar am Ende). Unter jeder
      Hauptnummer eine Zeile „Hängst du hier → Nr. <n>", n = erste
      Hauptnummer der Einheit, die die Voraussetzungszeile der Mappe
      nennt („Einheit 2", „ab Einheit 2"; bei „alle Einheiten" oder
      ohne Angabe die erste Einheit des Blatts); in der Lösungsdatei
      bei jeder Zeile, deren merkmal mit „Fallstrick:" beginnt, der
      Zusatz „falsch → Lücke: <merkmal ohne ‚Fallstrick:'>".

   f. Schluss des Lernblatts (ziel.md § 2, neu): Seite „Prüfe dich" –
      je Verfahrenskette des Blatts eine Aufgabe, gemischt, ohne
      Titel und ohne Verfahrensüberschrift: die mittlere Sprosse der
      Kette in der kleinsten Variante, die im Blatt nicht steht
      (fehlt eine, Variante 1 und log). Darunter „Das kann ich" mit je
      Kette der Ich-kann-Zeile zum Abhaken (ersetzt die bisherige
      Abhakseite; im Gesamt mit den Fertigkeiten der Zone davor).

   g. Kopf „<Thema> · Lernblatt", Fußzeile Kennung links, Seite rechts
      (Befund 1, 2), Kopfzeile je Einheit mit Kurzform; Abschnitte
      ohne Linie; BANKWORT-Prüfung wie im Kompetenzblatt (Anlauf,
      Prüfungsaufgaben, Sprosse, Vorstufe, Grundfall, Fallstrick,
      Variante, Kette, Prüfungsform, ausgelassen).

   h. Dateisatz wie bisher (blatt0_a/_l, e<n>_a/_l, <K>-blatt0.tex,
      <K>-e<n>.tex, <K>.tex, <K>-gesamt.tex, <K>-loesungen.tex,
      vorspann.tex, bau.json, zusammenbau.log, Registerzeile);
      bau.json zusätzlich je Teilaufgabe lage (zone/leiter/pruefung/
      pflicht/pruefe-dich), zusammenbau „v0.9".

4. Bau und Render. `git pull --rebase`, dann terme mit Registerzeile:
   `python3 werkzeuge/zusammenbau.py terme` (Kennung die nächste
   freie TER-L<n>); `xelatex -interaction=nonstopmode
   -file-line-error` zweimal je Dokument (<K>-gesamt, <K>,
   <K>-blatt0, <K>-loesungen); PNG je Seite des Gesamt (pdftoppm
   -r 80); Messwerte in bau.json (seiten, seiten_loesungen,
   fehlende_zeichen, overfull, bankwort, hauptnummern je Einheit,
   teilaufgaben je Einheit). Zählgrenze: höchstens sechs
   Kompilierdurchläufe je Dokument über alle Nachbesserungen; ein
   Kompilierfehler wird im Skript behoben, nie in der Bankzeile (die
   Zeile kommt dann als Befund in den Bericht und wird mit einem
   Schalter `--ohne <id>` weggelassen, wie im Kompetenzblatt).
   Danach Probe ohne Register für prozentrechnung und
   quadratische-gleichungen (`--ohne-register --aus /tmp/…`), nur
   Strukturprüfung und ein Kompilierlauf des Gesamt – Regressionsprobe.
   Zuletzt `python3 bau/kompetenz/bauen.py` nicht neu laufen lassen;
   stattdessen `python3 werkzeuge/zusammenbau.py prozentrechnung
   --kompetenz "Prozentsatz" --einheiten 2 --ohne-register --aus
   /tmp/k` und ein Kompilierlauf: das Rezept K muss unverändert bauen.

5. Prüfungen (Bericht nennt jede mit Ergebnis):
   - 0 Kompilierfehler, 0 „Missing character" in allen vier Logs des
     Terme-Blatts; PDFs enthalten Text (pdftotext).
   - Kein BANKWORT-Treffer; kein „TODO" im PDF-Text.
   - Keine Hauptnummer, in der derselbe Auftragssatz in mehr als einer
     Teilaufgabe steht (Skript prüft das, log AUFTRAG).
   - Hauptnummern je Terme-Einheit ≥ die Zahl im alten Blatt
     (Einheiten 1–4 von `lernblatt.tex`/`e<n>_a.tex` des Vergleichs;
     die Zuordnung der alten Nummern zu Einheiten liest du aus
     dessen Zweigzeilen) – Abweichung nach unten ist ein Befund, kein
     Grund, Zeilen zu erfinden.
   - Gegenprobe mit bekannten Werten: der Grundfall „Zusammenfassen"
     (terme e2) hat vier Teilaufgaben, die Vorstufe davor vier; Nr.
     „Termwert berechnen" hat drei; Anzahl Originale an der
     Prüfungshöhe von e1 = Zahl der verschiedenen Originale der
     jüngsten fünf Jahrgänge dieser Kette in `bank/terme/e1.jsonl`.
   - `bau/prozentrechnung/kennung-probe.py` läuft für die neue Kennung
     durch (Register gegen bau.json, Kennung in Fuß und Dateinamen).
   - Zwei gleiche Aufrufe geben wortgleiche Aufgabendateien.

6. Dokumentation: `werkzeuge/zusammenbau.md` bekommt den Abschnitt
   „Rezept Lernblatt (v0.9)" (Mengen, Satz, Auftrag einmal, Paare,
   Zweigzeile, Blatt 0 mit Verweis, Prüfe dich) und die Versionszeile
   im Kopf; Abschnitt „Was v0.1 nicht kann" wird bereinigt (was jetzt
   geht, raus; was bleibt, bleibt). `bau/layout-befunde.md`: eine
   Zeile am Ende „Lernblatt v0.9 (2026-…): Befunde 1–12, 15–17, 20,
   25 im Lernblatt umgesetzt" mit den tatsächlich umgesetzten
   Nummern. Bericht als `bau/terme/<K>/bericht.md` (Muster
   `bau/kompetenz/bericht.md`): Vorher/Nachher-Zahlen (Hauptnummern,
   Teilaufgaben, Seiten je Einheit und gesamt, gegen das alte Blatt),
   Prüfungen, Befunde an Bank und Mappe (nicht geändert), Annahmen,
   Offenes.

7. Abschluss: Auftrag nach `archiv/auftrag-lernblatt-v09-<date +%F>.md`
   verschieben (git mv). Commit je Teil (Skript; Bau; Doku), jede
   Commit-Nachricht nennt den Anlass („Lernblatt v0.9: …"); vor jedem
   Push `git pull --rebase`, dann `git push origin main`, kein eigener
   Branch. PDFs im Repo brauchen `*.pdf binary` in einer
   `.gitattributes` des Ordners (Wurzel setzt `* text eol=lf`).
   Kopiere `<K>-gesamt.pdf`, `<K>-loesungen.pdf`, `<K>-blatt0.pdf` und
   `bericht.md` nach `/home/claude/out/` (Ordner anlegen).

## Regeln

- Linux-Shell, `date`, Python 3; kein PowerShell. UTF-8 ohne BOM, LF.
- Keine Rückfragen. Nach zwei gescheiterten Anläufen an einer Stelle:
  offen mit Grund im Bericht, nächster Teil.
- Zählgrenzen, keine Zeitgrenzen: sechs Kompilierdurchläufe je
  Dokument; zwei Anläufe je Installation; höchstens drei
  Nachbesserungsrunden am Skript nach dem ersten Render.
- Nichts in `bank/`, `mappen/`, `mathblatt.sty`, `bank.md` ändern;
  Befunde daran in den Bericht.
- Zeilen in md-Dateien höchstens 72 Zeichen (Datenzeilen ausgenommen).
- Commit-Nachrichten enden mit
  `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` und
  `Claude-Session: https://claude.ai/code/session_01R1Gp3xLQBoDLjn3827uckA`.

## Bericht (Rückgabe an den Chat)

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann: Kennung,
Commits (Hash, Anlass), Vorher/Nachher-Tabelle, Ergebnis jeder
Prüfung, Abweichungen vom Auftrag mit Grund, Annahmen, Befunde an
Bank/Mappe/Katalog, was offen blieb. Letzte Zeile: Pfad der PDFs in
`/home/claude/out/` und ob der Push durch ist.
