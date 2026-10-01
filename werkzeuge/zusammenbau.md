# zusammenbau.py – aus der Bank ein Blatt (Quelltext)

Stand 2026-10-01, v1.1 (Lernblatt nach den Befunden am TER-L5, siehe
„Rezept Lernblatt (v1.1)“; erstes Blatt TER-L6). Davor v1.0 (Lernblatt
nach den Befunden des Lehrers am
TER-L4: Blattfolge, Test „Kannst du das schon?“ am Kopf jeder Einheit,
„Verstanden?“, Titel im Infinitiv, Auftrag nur bei Mehrdeutigkeit,
Lösungen am Ende des Gesamt, siehe „Rezept Lernblatt (v1.0)“; erstes
Blatt TER-L5). Davor v0.9 (Lernblatt im Satz des Kompetenzblatts:
Auftrag über der Nummer, kurze Terme nebeneinander, Ich-kann-Titel,
Zweigzeile, Mengen nach bank.md, Zone-Verweis, siehe „Rezept Lernblatt (v0.9)“;
zweiter Durchgang am selben Tag: Grundfall nach „(n×)“ im Katalog,
Prüfungshöhe nach der Regel des Kompetenzblatts, Seite „Prüfe dich“ mit
„Das kann ich“, Verweis „Hängst du hier → Nr. n“ unter der Nummer,
Auftrag einmal auch im Kompetenzblatt, erstes Blatt TER-L4; v0.8 Rezept
Kompetenzblatt nach dem Sprachlauf: Aufgabe in Sätzen als Absatz,
Merkkasten als Mathe, siehe „Rezept Kompetenzblatt“; v0.7 Rezept
Kompetenzblatt: `--kompetenz`, Kennung XXX-K<n>, Vorspann vorspann.tex;
v0.6 Rezept Prüfungs-Fokus: `--fokus-pruefung`, Kennung XXX-P<n>; v0.5
Rezept Zettel: `--zettel basis`; Prüfkennung kurz in allen Rezepten;
Zweigzeile „P10 ×n“; v0.4 Rezept Heft: `--heft`, `--nur-basis`; v0.3
Kennung, Register, Bauzettel; eine v0.2 gab es im Repo nicht, v0.3 setzt
auf v0.1 auf). Baut aus bank/<eintrag>/ LaTeX-Quelltexte für die Vorlage
mathblatt.sty (hz-0801/blattbau). Kompiliert wird nicht; die
Strukturprüfung im Skript ersetzt den Lauf bis zum ersten Render.

## Aufruf

    python3 werkzeuge/zusammenbau.py <eintrag> [--einheiten 1,3]
        [--zone ja|nein|kurz] [--fokus <kette>] [--schwach]
        [--klasse 7] [--kasten] [--aus <ordner>]
        [--vorlage <pfad/mathblatt.sty>] [--ohne-register]
        [--kuerzel <pfad/_kuerzel.csv>] [--nummer n]
        [--mit-sachaufgaben]

Ohne Schalter: Lernblatt mit Zone und allen Einheiten, Mengen nach
bank.md (seit v0.9; bis v0.8 je Sprosse Variante 1), ohne Klasse, mit
Registerzeile. Rückgabe 1, wenn die
Strukturprüfung Fehler findet (die Dateien und die Registerzeile
werden trotzdem geschrieben).

| Schalter | Wirkung |
| --- | --- |
| `--einheiten 1,3` | nur diese Einheiten und ihre Fertigkeiten |
| `--zone ja` | je Fertigkeit Sprosse 1 und 2, dazu das Zone-Paar |
| `--zone kurz` | je Fertigkeit nur Sprosse 1 |
| `--zone nein` | keine Zone |
| `--fokus <kette>` | Name wie im Feld kette; alle Varianten |
| `--schwach` | Form nach unterrichtsblatt 2.8 |
| `--klasse n` | Zeitmarke relativ; bis Klasse 10 `\weit` |
| `--kasten` | Merkkasten am Anfang jeder Einheit (3.1) |
| `--aus <ordner>` | Ausgabeordner statt bau/<eintrag>/<kennung>/ |
| `--vorlage <sty>` | Pfad zu mathblatt.sty |
| `--ohne-register` | Probe: Kennung XXX-R0, keine Registerzeile |
| `--kuerzel <csv>` | Pfad zu katalog/_kuerzel.csv |
| `--nummer n` | Kennung XXX-R<n> vorgegeben (v0.9; bricht ab, wenn sie im Register steht) |
| `--mit-sachaufgaben` | Lernblatt: alle Sachaufgaben der Ketten (v1.0; sonst je Kette eine) |

mathblatt.sty sucht das Skript sonst unter $BLATTBAU,
../hz-0801/blattbau/ und ../blattbau/ neben dem Repo;
_kuerzel.csv unter $MATHE_NACHHILFE/katalog/,
../mathe-nachhilfe/katalog/ und ../hz-0801/mathe-nachhilfe/katalog/.

## Kennung

Jedes Blatt aus der Bank trägt eine Kennung `XXX-R<n>` (Beschluss
des Lehrers vom 28.09.), z. B. PRZ-L3:

- XXX: Kürzel des Eintrags aus katalog/_kuerzel.csv in
  hz-0801/mathe-nachhilfe (Spalten kuerzel;eintrag). Fehlt die
  Datei oder der Eintrag darin, die ersten drei Buchstaben des
  Eintrags groß; die log (KENNUNG) und bau.json (kuerzel_quelle)
  sagen, woher das Kürzel kam. Heft mit mehreren Einträgen: Kürzel
  des ersten.
- R: Rezept – L Lernblatt, F Fokus (`--fokus`), S schwach
  (`--schwach`), H Heft (`--heft`, ab v0.4), Z Zettel (`--zettel`,
  ab v0.5; Kürzel fest BAS), P Prüfungs-Fokus (`--fokus-pruefung`,
  ab v0.6), K Kompetenzblatt (`--kompetenz`, ab v0.7).
- n: laufende Nummer je Kürzel und Rezept ab 1, die nächste freie
  aus bau/register.csv (größte vergebene + 1). Zweimal derselbe
  Aufruf gibt zwei Kennungen (PRZ-L1, PRZ-L2).
- `--ohne-register`: n = 0 (PRZ-L0), keine Registerzeile; der
  Ordner PRZ-L0 wird bei jeder Probe überschrieben.

Die Kennung steht:

- in der Fußzeile jeder Seite unten links, wo `\blattfuss` die
  Bezeichnung trägt: „Prozentrechnung · Lernblatt · PRZ-L3“ (Thema ·
  Bezeichnung des Dokuments · Kennung). Gesetzt über das dritte
  Argument von `\blattkopf*`, weil `\blattfuss` und `\blattkopf`
  beide `\fancyhf{}` rufen und sich gegenseitig löschen; die
  Kopfzeile mit der Einheit bleibt so erhalten. Seit v0.9 (L, F, S) steht
  dort nur die Kennung, Thema und Blattart stehen im Kopf (Befund 2).
- in den Dateinamen und im Ordner: bau/<eintrag>/<kennung>/ mit
  <kennung>.tex (das Blatt), <kennung>-loesungen.tex; beim
  Lernblatt dazu <kennung>-gesamt.tex, <kennung>-blatt0.tex,
  <kennung>-e<n>.tex. Kompiliert heißen sie PRZ-L3.pdf,
  PRZ-L3-loesungen.pdf. Die eingebundenen Teile (blatt0_a,
  e<n>_a/_l, abhaken) behalten ihre Namen.

Ist der Zielordner einer Registerkennung schon belegt, bricht das
Skript ab, ohne etwas zu bauen (Register und Ordner passen dann
nicht zusammen).

## Register

bau/register.csv, Semikolon, UTF-8, LF, eine Zeile je Bau:

    kennung;datum;eintraege;rezept;bestellung;bank_commit;
    zusammenbau;vorlage;pfad

- datum: Uhr des Rechners (`date +%F`).
- eintraege: Einträge, mit Komma getrennt.
- bestellung: alle Schalter mit Wert, auch die Voreinstellungen
  (`einheiten=alle, zone=ja, fokus=–, …`).
- bank_commit: `git rev-parse --short HEAD`; „+geändert“, wenn
  bank/, mappen/ oder werkzeuge/ ungesichert von HEAD abweichen.
- zusammenbau: Version des Skripts; vorlage: Versionszeile aus
  mathblatt.sty („Version 2026-09-28a“).
- pfad: Ausgabeordner relativ zur Repo-Wurzel.

Die Zeile wird angehängt, nachdem die Dateien geschrieben sind.
Parallele Web-Sitzungen, die bauen, schreiben alle in diese eine
Datei: vor dem Bau `git pull --rebase`, sonst können zwei Sitzungen
dieselbe Nummer vergeben.

## Bauzettel

bau.json im Ausgabeordner: kennung, datum, eintraege (Liste),
rezept, rezept_name, bestellung (alle Schalter als Objekt),
bank_commit, zusammenbau, vorlage, pfad, kuerzel_quelle,
strukturfehler und aufgaben – die Bankzeilen in Blattreihenfolge
(Zone zuerst), je Teilaufgabe:

    {"aufgabe": "A16", "hauptnummer": 16, "teilaufgabe": "b",
     "id": "prozentrechnung-e2-k5-s2-v1", "datei": "e2_a.tex"}

A16 ist Hauptnummer 16 (Zeile aus PRZ-L1). Die Erklärzeile im
Päckchen (schwach) hat id null und einen hinweis. Prüfstein:
bau/prozentrechnung/kennung-probe.py <kennung> … prüft Register
gegen bau.json, jede Aufgabennummer auf genau eine Bankzeile,
Teilaufgaben je Hauptnummer im Quelltext gegen bau.json, Kennung in
Fußzeile und Dateinamen, und dass gleiche Bestellungen wortgleiche
Aufgabendateien geben.

## Ausgabe

Lernblatt und schwach: blatt0_a/_l (Zone), e<n>_a/_l je Einheit
(n = Nummer im Katalog), Rahmen <K>-blatt0.tex, <K>-e<n>.tex,
<K>.tex (bis v0.1 lernblatt.tex), <K>-gesamt.tex,
<K>-loesungen.tex, abhaken.tex (<K> = Kennung); seit v0.9 im
Lernblatt dazu pruefe_a/_l („Prüfe dich“) und vorspann.tex; seit
v1.0 im Lernblatt ohne pruefe_a/_l und abhaken.tex (Rezept Lernblatt
v1.0). Fokus:
blatt0_a/_l, e<n>_a/_l, <K>.tex, <K>-loesungen.tex (bis v0.1
fokus.tex, fokus_loesungen.tex). Dazu mathblatt.sty als Kopie,
bau.json und zusammenbau.log: Kennung (KENNUNG), jede Auswahl
(AUSWAHL, WEG), Köpfe, Teilungen, Warnungen, alle TODO mit Datei
und Zeile, die Strukturprüfung.

Kompilieren: `xelatex <K>-gesamt.tex` zweimal (Abhakseite),
ebenso <K>.tex, <K>-loesungen.tex, <K>-blatt0.tex. PDFs im Repo
brauchen `*.pdf binary` in einer .gitattributes des Ordners (die
Wurzel setzt `* text eol=lf`, das verfälscht PDFs).

## Bauregeln

- Reihenfolge je Einheit: Erkennungsschritte → Verfahrensketten
  (kette_nr) → Typen ohne Kette → Pflichtelemente; in der Kette
  nach Sprosse, je Sprosse die kleinste Variante (Variante 1).
- Eine Hauptnummer je Kette, eine Teilaufgabe je Zeile. Zone
  zuerst, Nummern laufen über alle Dateien durch.
- Fokus: nur die Ketten mit dem genannten Namen (auch die gleich-
  namige Pflichtkette), alle Varianten; Teilung an Sprossen-
  grenzen nach 2.3 g (höchstens 12 Teilaufgaben, 6 mit Grafik).
- schwach: `\swz` für Rechnungen, `\swa` mit Grafik, `\swfrage`
  für Begründen, Ankreuzen als `teile`; der Grundfall als
  Päckchen mit allen Varianten und der Erklärzeile; Merkkasten
  am Ende der Einheit.
- form wählt den Baustein: teile-Block für teil, text,
  ankreuzen, tabelle, zeichnen, streifenfeld, streifenleer,
  dreisatz; `gleichungsraster` für gleichungsraster. grafik und
  loesungsgrafik stehen wörtlich darin.
- antwort „__ <Einheit>“ wird `\leerfeld[<Einheit>]`, sonst
  `\leerfeld`; kein Feld, wenn die Grafik es schon trägt
  (`\streifenfeld`, `\dsleer`).
- Prüfkennung wie im Muster 2026-09-22: `\hfill (…)`, bei
  folgendem Feld mit `\\`; seit v0.5 in Kurzform (Abschnitt
  „Prüfkennung kurz“). Kein `\steil` außer im Heft (2.4 d).
- Kopf aus der Mappe: Titel aus „Lerneinheiten“, Zeitmarke und
  Prüfungswort aus der Marken-Zeile (1.5; seit v0.5 mit Zahl der
  Jahrgänge, Abschnitt „Zweigzeile“), Merkkasten aus
  „Merkkasten“, Zuordnung der Zone aus „Voraussetzungen“.
- Was Bank und Mappe nicht tragen, steht als `%% TODO` in der
  Zeile davor und in der log, nie als geratener Text.

## Rezept Lernblatt (v1.1)

Auftrag vom 01.10. (Befunde am TER-L5, dritter Lauf). Ersetzt v1.0, wo
es abweicht; K, F, S unverändert.

1. Eine Datei <K>-gesamt.tex (Blatt, dann Lösungen); <K>.tex,
   <K>-blatt0.tex, <K>-e<n>.tex, <K>-loesungen.tex entfallen.
2. Lösungen: je Teilaufgabe eine Zeile, nur das Ergebnis
   (`kurz_loesung`; Fehler/Begründen der erste Satz), zweispaltig,
   Blatt 0 mit „falsch → Nr. n“; `--mit-loesungsweg` gibt das Feld ganz.
3. Blatt 0 ohne Titel (`lbaufgabe`, Nummer vor a)); Zone-Paar nur die
   Fehlerzeile.
4. Einheitentitel als \einheitenkopf* (groß, halbfett, Linie).
5. Test ohne Nummer im grauen Kasten (`\lbtest`), kein Raum, kein
   Auftrag, Lösung klein unten rechts; Nummern beginnen bei der Übung.
6. Fragen und „Auftrag: Term“ mit kurzem Feld untereinander, Feld in
   der Zeile; nebeneinander nur Terme und Rechnungen mit „=“.
7. Auftrag einmal oben, wenn nur Term oder Zahl wechselt, auch bei
   Bedingung („a) 4x − 3 für x = 5: ____“).
8. Kein Auftrag, wenn der Titel die Handlung nennt (`titel_nennt`,
   Synonyme `LB_SYNONYM`) und der Auftrag einfach ist (ein Satz, keine
   Zahl, kein „und“, kein „mit“).
9. Grundfall zweimal (`LB_GRUNDFALL_LERN`), Vorstufen alle.
10. Prüfungshöhe ohne Original: letzte Teilaufgabe der Leiter.
11. Prüfungshöhe mit Original: Titel „Wie in der Prüfung“, zwei
    Schreibzeilen.
12. „Verstanden?“ im Kasten (`lbkasten`) mit „Gemischt – erkenne
    selbst, was zu tun ist.“; Fehler und Begründen die schwerste Zeile
    (`pflicht_rang`, log PFLICHT).

## Rezept Lernblatt (v1.0)

Auftrag vom 01.10. (auftrag-lernblatt-v10.md, archiv/): Der Lehrer legte
TER-L4 neben das Blatt des alten Prompts und gab 15 Befunde
(bau/layout-befunde.md, Abschnitt „Befunde des Lehrers 01.10. am
TER-L4“). Gilt für Rezept L; F, S und K teilen Code, ihre Quelltexte
sind bis auf die Versionszeile gleich geblieben (Probe). Was hier nicht
steht, gilt weiter wie in v0.9.

1. Blattfolge: Zeile „Blattfolge: 2, 3, 4, 1“ unter den Lerneinheiten
   des Katalogs (optional, katalog/_vorlage.md), über die Mappe gelesen
   (`Mappe.blattfolge`). Die Einheiten stehen in dieser Folge, die
   Nummern laufen durch; Dateinamen (e<n>_a.tex, <K>-e<n>.tex) behalten
   die Katalognummer. Je Einheit erst die Ketten ohne Textaufgabe im
   Grundfall, dann die mit (Textaufgabe: form text oder ein Satz vor dem
   Auftrag, `ist_textaufgabe`); Pflichtelemente zuletzt; log FOLGE.
2. Keine Verzeichniszeile, weder im Gesamt noch in den Teilen.
3. Auftrag nur bei Mehrdeutigkeit (`laeufe_lern`, `anweisung_noetig`):
   ein gemeinsamer Auftrag über der Nummer nur bei nackten Termen und
   Gleichungen („Fasse zusammen: $7x + 2x$“); Teilaufgaben mit Bedingung
   oder Kontext („… $4x - 3$ für $x = 5$“, Sachtext, gleicher
   Schlusssatz, gleiche Vorlage) tragen je den ganzen Satz (log
   AUFTRAG-SATZ-JE-TEIL). Die Anweisung entfällt, wenn jede Teilaufgabe
   form teil ist und ein „=“ trägt oder eine reine Zahlrechnung ist und
   der Titel die Handlung nennt (log ANWEISUNG-WEG). Prüfung AUFTRAG nur
   für nackte Terme.
4. Titel im Infinitiv: Spalte `titel` in bau/regal/ich-kann.csv (neu, am
   Ende der Zeile; für terme gefüllt), sonst „Ich kann …“ maschinell
   (`infinitiv_titel`), feste Ersatzsätze aus `ERSATZ_INFINITIV`; geht
   nichts, der Satz ohne Punkt und log TITEL.
5. Einheitenkopf nur der Titel
   (`\einheitenkopf[e<n>][<Titel>]{<Titel>}`), keine Zweigzeile, auch nicht mit `--klasse`; Kopfzeile „Thema ·
   Lernblatt · <Titel>“. Typen, die „Typen je Lerneinheit“ nur dem
   Gymnasium zuordnet („[GYM 8]“ ohne OS), geben „GYM“ klein rechts im
   Titel der Hauptnummer (`\lbgym`), wenn alle Teilaufgaben der Nummer
   zu dem Typ gehören (Kettenname, sprosse_text oder Klammerinhalt des
   Typs); sonst log GYM ohne Marke.
6. Striche für den Rechenweg (`\kbraum` im Vorspann neu): Linie wie das
   Antwortfeld (`\underline`, schwarz), halbe Textbreite, eingerückt wie
   die Teilaufgabe; vor dem ersten Strich und vor dem Antwortfeld
   (`\kbantwort`) eine Zeile Luft.
7. Kein „Einheit n von m“, weder im Kopf noch in der Kopfzeile.
8. Ankreuzen nebeneinander nur bis 120 Zeichen Quelltext (Text und
   Optionen); ganze Vorstufen paarweise nur bis 45 Zeichen (eine Zeile
   der halben Spalte).
9. Keine Teilung unter 27 Teilaufgaben (`hn_lern`); darüber an einer
   Sprossengrenze, das zweite Stück trägt den Titel seiner Sprosse.
10. Test am Kopf jeder Einheit (`test_hn`): „Kannst du das schon? Dann
    weiter zu „<nächste Einheit>““ (letzte: „Dann bist du fertig“); je
    Verfahrenskette eine Teilaufgabe der höchsten Sprosse mit form ≠
    text und ohne Sachkontext, kleinste Variante, die im Blatt nicht
    steht (sonst die höchste, log TEST); ohne Verfahrenskette die Typen
    ohne Kette. Lösung: „(richtig → Nr. a–b überspringen)“ mit den
    Nummern der Kette. „Prüfe dich“, „Das kann ich“ und abhaken.tex
    entfallen.
11. „Verstanden?“ am Ende der Einheit (`verstanden_hn`): je Sorte
    (fehler, begründen, darstellung, anwendung) eine Teilaufgabe, die
    kleinste Sprosse und Variante, Anwendung zuletzt.
12. Je Verfahrenskette höchstens eine Teilaufgabe mit Sachkontext
    (`hat_sachkontext`: mehr als zwölf Wörter vor dem ersten Auftrag,
    Mathe als ein Wort): die mit der höchsten Sprosse bleibt, die
    übrigen entfallen (log TEXT); der Grundfall bleibt immer.
    `--mit-sachaufgaben` hebt die Grenze auf.
13. Grafik links, Antwort rechts (`grafik_mass_lern` kennt \viereck,
    \dreieck, \termbaum, \sachtabelle): passt die Grafik in die Breite
    minus 4,5 cm, steht das Antwortfeld (mit Bezeichner aus dem
    Antwortgerüst) rechts daneben, etwa auf halber Höhe (log GRAFIK).
14. <K>-gesamt.tex endet mit „Lösungen“ auf neuer Seite (Kopfzeile
    „Thema · Lernblatt · Lösungen“); die Lösungsteile tragen ihre
    Überschrift als `\kbabschnitt`, ohne Einfluss auf die Kopfzeile.
    <K>-loesungen.tex bleibt.

Dateien: blatt0_a/_l, e<n>_a/_l, <K>.tex, <K>-gesamt.tex,
<K>-blatt0.tex, <K>-e<n>.tex, <K>-loesungen.tex, vorspann.tex
(VORSPANN, VORSPANN_LERN, VORSPANN_LERN10). bau.json im Lernblatt dazu:
lage test, titel_fehlt, gym, sachkontext_ausgelassen, test, blattfolge,
nach dem Messlauf pruefungen_v10 (bau/terme/lernblatt-messen.py).
Erstes Blatt: bau/terme/TER-L5 (bericht.md).

## Rezept Lernblatt (v0.9)

Zwei Aufträge vom 30.09. (Chat verbessereBlätter). Anlass: Der Lehrer
legte das Bank-Lernblatt Terme (v0.8, TER-L0) neben das Blatt des alten
Prompts (mathe-nachhilfe,
blaetter/testlauf-2026-09-26/10-ka-terme-8-gym) und sagte: zu wenige
Aufgaben; liest sich schlecht, weil sich der Auftrag in jeder
Teilaufgabe wiederholt; Layout wie das alte Blatt. Der erste Durchgang
baute TER-L3, der zweite (auftrag-lernblatt-v09.md, archiv/) TER-L4.
Seit v0.9 setzt das Lernblatt (Rezept L, ebenso F) im Satz des
Kompetenzblatts; Rezept S behält die Form 2.8 (`\swz`, `\swa`), bekommt
aber Titel und Zweigzeile wie L. Heft, Zettel und Prüfungs-Fokus sind
unverändert (Probe: Quelltexte byte-gleich), das Kompetenzblatt nur um
„Auftrag einmal“ ergänzt.

### Mengen (bank.md „Mengen je Kette“)

- Erkennungsschritt: alle Zeilen (4) in einer Nummer.
- Verfahrenskette: je Vorstufe eine Nummer mit allen Zeilen; dann eine
  Nummer mit dem Grundfall und je weiterer Sprosse Variante 1 (die volle
  Leiter); dann eine Nummer mit den Prüfungshöhen.
- Grundfall: so viele Zeilen, wie „(n×)“ am Grundfall in der Zeile der
  Kette unter „Für schwache Schüler“ der Mappe sagt (terme:
  Zusammenfassen, Malnehmen, Ausklammern 4; Klammern, Term aufstellen
  3); ohne Angabe vier; der Rest RESERVE in der log.
- Prüfungshöhe (`waehle_originale`, gemeinsam mit dem Kompetenzblatt):
  je Original eine Aufgabe (kleinste Sprosse und Variante), nur die
  jüngsten fünf Jahrgänge der Kette, verschiedene Formulierungen zuerst,
  bis fünf; ohne Original eine der drei Zeilen.
- Typ ohne Kette: alle Zeilen (3) in einer Nummer.
- Pflichtelemente: je Sorte (fehler, begründen, darstellung, anwendung)
  eine Nummer mit allen drei Zeilen.
- Teilung (`zerteile`): erst nach 2.3 g ausgewogen (höchstens 12
  Teilaufgaben, 6 mit Grafik, 13 → 7 + 6), dann in jedem Stück an einem
  Auftrag, der darin schon stand; Fortsetzung „<Titel> – weiter“ oder
  der eigene Ich-kann-Satz der ersten Sprosse des Stücks.
- Fokus (F): alle Varianten der Kette, Pflichtelemente je Element.
  schwach (S): Auswahl wie bis v0.8.

### Satz (gemeinsam mit dem Kompetenzblatt)

- `KbSatz` (satz_teil, satz_halb, satz_halb_text, halb_tauglich) ist die
  gemeinsame Klasse von `KompetenzBau` und `Bau`; kein Code kopiert.
- Jede Hauptnummer ist `kbaufgabe`, jede Teilaufgabe ein `kbblock`
  (Befund 21: unteilbar); Antwortfeld in eigener Zeile, Tabelle unter
  dem Text, Kreuze je Zeile, Flattersatz, Prüfkennung klein rechts in
  der Auftaktzeile („P10 ’23“, `kennung_kompetenz`).
- Bearbeitungsraum nur bei Rechnen und Begründen (Befund 9): Zeilen aus
  der Musterlösung (`rechenzeilen`), Text-, Fehler- und
  Begründungsaufgaben ohne Antwortgerüst zwei Schreibzeilen, Anwendung
  drei (log RAUM); kein Raum bei Vorstufe, Ankreuzen, Eintragen, kurzen
  Termen.
- Zeichen, die Latin Modern nicht hat: `zeichen_vorspann`, vorspann.tex
  (VORSPANN des Kompetenzblatts + VORSPANN_LERN); mathblatt.sty
  unverändert.
- BANKWORT-Prüfung (Liste des Kompetenzblatts) über alle *_a.tex, log;
  bau/terme/lernblatt-messen.py prüft dazu den PDF-Text.

### Auftrag einmal (L und K)

Aufeinander folgende Teilaufgaben mit demselben Auftrag bilden einen
Lauf (`laeufe_von`); der Auftrag steht einmal als `\kbanweisung`, die
Teilaufgabe trägt nur den Rest. Erkannt werden

1. „Verb …: Term“ („Fasse zusammen: $7x + 2x$“ → „Fasse zusammen.“),
   auch für eine einzelne Teilaufgabe;
2. „Verb. Term“ („Berechne. $\frac{600}{100}$“);
3. Satzanfang + Term + Satzende („Berechne den Wert des Terms $4x-3$ für
   $x = 5$.“ → „Berechne den Wert des Terms.“), Satzanfang + Term +
   Satzrest („Welche Vorzahl hat …?“), Term am Ende des ersten von zwei
   Sätzen („Löse die Gleichung. Gib die Lösungsmenge an.“), ab zwei;
4. gleicher Schlusssatz („… Kreuze den Term an, der dazu passt.“), ab
   zwei; eine Prüfkennung bleibt am Rest;
5. gleiche Aufgabe, in der sich nur Mathe an höchstens zwei Stellen
   unterscheidet, ab zwei.

Im Kompetenzblatt gilt das für eine Nummer, deren Teilaufgaben alle
einen Lauf bilden (meist die Prüfungshöhen: „Kreuze den passenden Term
an.“). Prüfung AUFTRAG: kein Auftragssatz zweimal in einer Hauptnummer,
gezählt über die Anweisungen und die Aufträge der Teilaufgaben mit
ganzem Text (log AUFTRAG, bau.json auftrag_doppelt). Hinweis
AUFTRAG-SATZ: derselbe Aufforderungs- oder Fragesatz (Mathe als „…“)
mehrfach, ohne dass ein gemeinsamer Auftrag erkannt wurde – meist
verschieden formulierte Bankzeilen einer Sprosse (bau.json
auftrag_satz_doppelt).

### Paare (zwei je Zeile)

- `\lbpaar` (Buchstaben in derselben Flucht wie untereinander): ein Lauf
  ab zwei Teilaufgaben mit Auftrag, deren Term bis 30 Zeichen hat, ohne
  Grafik, Kontext, Prüfkennung, Pflichtelement, `\rechnung`/`\kreuz`,
  mit höchstens zwei Feldern: „a) $7x + 2x =$ ____“ (Feld 2,6 cm,
  `\lbfeld`), kein Raum. „=“ nur bei Rechenaufträgen; sonst Feld mit
  Abstand; kein Feld bei Unterstreiche, Kreise, Markiere.
- Ebenso nebeneinander: Ankreuzaufgaben eines Laufs (Text bis 110,
  Optionen bis 24 Zeichen); Vorstufen ohne gemeinsamen Auftrag bis 75
  Zeichen als ganze Aufgabe.
- Ein kurzer Term allein (Auftrag darüber, kein Raum) steht wie im Paar
  in einer Zeile mit Feld (log KURZ); längere untereinander (Befund 6).

### Titel (Ich-kann-Satz je Hauptnummer)

Aus bau/regal/ich-kann.csv (`lies_ichkann`), Schlüssel eintrag;einheit;
kette;sprosse:

| Hauptnummer | sprosse | Ersatz ohne Zeile |
| --- | --- | --- |
| Erkennungsschritt, Typ ohne Kette | leer | „Ich kann: <merkmal>.“ |
| Vorstufe einer Kette | Zahl der Sprosse (0, -1) | „Ich kann: <merkmal>.“ |
| Grundfall und Sprossen | leer | „Ich kann: <merkmal>.“ |
| Prüfungshöhe | p | „Ich kann das auch in Aufgaben aus der Prüfung.“ |
| Pflichtelement | fehler, begruenden, … | feste Sätze (PFLICHT_ICHKANN) |
| Zone | einheit 0, Kette = Fertigkeit | „Ich kann <Fertigkeit>.“ |
| Zone-Paar | einheit 0, paar | „Ich finde den Fehler und rechne richtig.“ |

Ein fehlender Satz steht in der log (ICH-KANN fehlt) und in bau.json
(ichkann_fehlt). Für terme sind alle Zeilen da (35 mit quelle „Lernblatt
v0.9“ aus dem ersten Durchgang); TER-L4 hat keinen Ersatz.

### Zweigzeile

Unter dem Einheitenkopf „Einheit n von m · <Titel>“ (wie im alten
Blatt): „Hier lernst du, <Titel als zu-Infinitiv> – <Beschreibung> ·
Zeitmarke · Prüfungswort · baut auf: …“.

- Beschreibung: die Lerneinheiten-Zeile der Mappe nach „ – “, Wortlaut
  wie im Katalog (`beschreibung_katalog`); weg fallen die Eingabe-Marke
  „← Eingabe …“, Klammern mit Hinweisen für den Lehrer (→, .md, Kl.,
  LISUM, RLP, Zeile, Fachbrief, amtlich, Reihe, Katalog) und Glieder mit
  Bank-Wort („… als Grundfall“). Titel ohne Verb („Sachaufgaben“): „Hier
  lernst du: <Beschreibung>“. Ist die Beschreibung schon ein Satz („Hier
  lernst du …“), steht sie allein.
- Zeitmarke und Prüfungswort wie bisher (1.5, `pruefwort_zahl`).
- „baut auf:“ die Fertigkeiten der Voraussetzungen (Kurzname vor „ (“),
  deren Zeile diese Einheit nennt („Einheit 2“, „ab Einheit 2“); „alle
  Einheiten“, „jede Einheit“: jede Einheit; ohne Angabe: die erste
  Einheit des Blatts (`fertigkeit_ziel`). Kein Kettenname, kein
  Bank-Wort.

### Blatt 0 „Das kennst du schon“

- Je Fertigkeit eine Nummer mit Ich-kann-Titel (einheit 0): die zwei
  sehr leichten, die mittlere und je Fallstrick eine (bank.md); das
  Zone-Paar (Fehler finden und die gleichartige Rechnung) am Ende der
  Zone. `--zone kurz`: eine leichte und ein Fallstrick. Fokus und
  schwach behalten das Zone-Paar hinter seiner Fertigkeit.
- Unter jeder Nummer eine Zeile „Hängst du hier → Nr. n“ (`\lbhaengst`,
  im letzten Block der Nummer): n ist die erste Hauptnummer der
  kleinsten Einheit, die die Voraussetzungszeile nennt; bei „alle
  Einheiten“ oder ohne Angabe die erste Einheit des Blatts (log
  ZONE-VERWEIS mit Grund). Keine Zeile bei schwach.
- Lösung: bei jeder Zeile, deren merkmal mit „Fallstrick:“ beginnt, der
  Zusatz „(falsch → Lücke: <merkmal ohne ‚Fallstrick:‘>)“.

### Prüfe dich und Das kann ich (ziel.md § 2)

- Nach der letzten Einheit, neue Seite „Prüfe dich“ (pruefe_a.tex): je
  Verfahrenskette des Blatts eine Aufgabe, ohne Ich-kann-Titel und ohne
  Verfahrensüberschrift; der Auftrag steht in der Zeile der Nummer. Die
  Aufgabe ist die mittlere Sprosse der Kette (Grundfall und Sprossen,
  ohne Vorstufe und Prüfungshöhe; bei gerader Zahl die obere Mitte) in
  der kleinsten Variante, die im Blatt nicht steht; fehlt eine, Variante
  1 (log PRÜFE-DICH). Gemischt nach der Prüfsumme der id (fest bei
  gleicher Bestellung). Die Nummern laufen weiter.
- Lösung (pruefe_l.tex, am Ende der Lösungen): „(falsch → Nr. n)“ auf
  die Nummer der Leiter, in der die Sprosse steht.
- Darunter „Das kann ich“ (abhaken.tex, Umgebung `lbdaskannich`, keine
  neue Seite): je Kette einer Einheit die Ich-kann-Zeile der Kette
  (sprosse leer) mit allen Nummern der Kette („6–8, 11–14“, Pflicht-
  elemente tragen den Namen der ersten Verfahrenskette); im Gesamt davor
  je Fertigkeit der Zone ihre Zeile mit Nummer und Zone-Paar. Ersetzt
  die Abhakseite des Lernblatts; schwach behält sie.

### Kopf, Fuß, Dateien

- Kopf in jedem Dokument des Lernblatts „<Thema> · Lernblatt“ (Lösungen
  „<Thema> · Lernblatt · Lösungen“), dazu ab der Seite einer Einheit
  ihre Kurzform („Terme · Lernblatt · 2 Terme zusammenfassen“); Fuß
  links die Kennung, rechts die Seite (Befund 1, 2). Abschnitte ohne
  Linie.
- bau.json je Teilaufgabe lage (zone, leiter, pruefung, pflicht,
  pruefe-dich) und art (zone, zonepaar, erkennung, vorstufe, leiter,
  ohne, pruefung, pflicht, pruefe-dich); dazu je_datei (Hauptnummern und
  Teilaufgaben je Aufgabendatei), auftrag_doppelt, auftrag_satz_doppelt.
  bau/terme/lernblatt-messen.py kompiliert (je Dokument zweimal), setzt
  PNG je Seite des Gesamt und schreibt seiten, seiten_loesungen,
  seiten_je_einheit, fehlende_zeichen, overfull, kompilierfehler,
  bankwort, hauptnummern_je_einheit, teilaufgaben_je_einheit und
  messwerte in bau.json.

### Entscheidungen v0.9

1. Prüfungshöhe als eigene Nummer hinter der Leiter, nicht als letzte
   Teilaufgabe der Leiter: sie trägt die Prüfkennung und einen eigenen
   Ich-kann-Satz.
2. „Pflichtelemente je Zeile eine Teilaufgabe“ gelesen als: alle drei
   Zeilen je Element; je Element eine Nummer mit eigenem Titel.
3. Das Zone-Paar steht am Ende der Zone (zweiter Durchgang; im ersten
   hinter seiner Fertigkeit).
4. Der Verweis steht als eigene kleine Zeile unter der Nummer, wörtlich
   „Hängst du hier → Nr. n“ (zweiter Durchgang; im ersten klein rechts
   im Titel mit Fragezeichen).
5. Teilung erst nach Maß, dann am wiederholten Auftrag: so trennt die
   Teilung nach Maß zwei gleiche Aufträge oft schon, und kein Stück hat
   nur eine Teilaufgabe.
6. `--nummer` auch für L/F/S, damit eine im Chat vergebene Kennung
   gebaut werden kann.
7. Fußzeile nur Kennung (Befund 2); kennung-probe.py nimmt beide Formen.
8. „Einheit n von m · <Titel>“ bleibt im Einheitenkopf, die Zweigzeile
   beginnt mit „Hier lernst du“ – wie im alten Blatt; beide Zeilen lesen
   sich zusammen als die Zweigzeile des Auftrags.
9. Blatt 0 behält die Menge nach bank.md (zwei sehr leichte, eine
   mittlere, je Fallstrick eine) statt „Sprosse 1 und 2“: ohne die
   Fallstrick-Zeilen hätte die Lösung keine „Lücke“.
10. Zweigzeile, Verweis, Fallstrick-Lösung und kurzer Term in einer
    Zeile
    gelten auch in Fokus und schwach (derselbe Code); Kopf, Prüfe dich,
    Das kann ich und Zone-Paar am Ende nur im Lernblatt.

## Rezept Heft (v0.4)

Beschluss des Lehrers vom 28.09.: Prüfungshefte nach Themen, aus der
Bank. Aufruf:

    python3 werkzeuge/zusammenbau.py <eintrag> <eintrag> …
        --heft [msa|abitur-gk|abitur-lk|fhr] [--nur-basis]
        [--titel <text>] --aus bau/hefte/<name>

`--heft` ohne Wert heißt msa; `--nur-basis` setzt msa. Ohne `--aus`
landet das Heft unter bau/hefte/<kennung>/. Einträge ohne Ordner in
bank/ entfallen (log FEHLT, bau.json fehlende_eintraege).

- Je Kette (gleichnamige Pflichtkette eingeschlossen) zwei Lagen:
  Anlauf (eine Hauptnummer: Vorstufe, Grundfall, eine Sprosse mit
  Fallstrick – je kleinste Variante ohne Original, Prüfkennung
  entfernt) und Prüfungsaufgaben (alle Varianten aller Zeilen, deren
  Original zum Profil gehört, nach Sprosse und Variante; geteilt nach
  2.3 g, „– weiter“).
- Profil einer Zeile: original.papier (OS/FOR/EBR/GYM → msa; A/B/C →
  fhr; -ga/-gk → abitur-gk; sonst abitur-lk), ohne Original die
  Prüfkennung im Text. Zeilen hoehe pruefung ohne beides sind keine
  Prüfungsaufgaben des Hefts.
- Fallstrick-Sprosse: erste Sprosse nach dem Grundfall, deren Merkmal
  einen Fallstrick nennt (Muster FALLSTRICK im Skript), sonst die
  erste nach dem Grundfall. Die Bank zählt Fallstricke nicht nach
  Häufigkeit; die Wahl steht in der log.
- Ketten ohne Prüfungsaufgabe im Profil entfallen samt Anlauf.
- `--nur-basis`: nur Originale mit Papier OS/FOR/EBR und id
  -<Papier>-B<n> (Basisteil), kein Anlauf.
- Sternchen: `\steil`/`\sgl`, wenn das Original im Prüfungskatalog
  von mathe-nachhilfe (msa-/abi-/iqb-/fhr-katalog.csv, gesucht wie
  _kuerzel.csv) stern = ja trägt; Legende „⋆ = Original mit Sternchen
  (nur FOR)“ in der Fußzeile.
- Satz im Heft: Gleichung ohne $ im gleichungsraster als Mathe, Text
  im gleichungsraster als `\teil`.
- Dateien: <eintrag>_a.tex, <eintrag>_l.tex je Eintrag (Kopf
  `\einheitenkopf[t<i>]`), <K>.tex mit Verzeichniszeile,
  <K>-loesungen.tex;
  bau.json trägt je Teilaufgabe lage (anlauf/pruefung), original,
  punkte, stern, dazu fehlende_eintraege, leere_eintraege und
  ausgelassen (vom Render-Skript gefüllt).
- Nummern laufen über das ganze Heft; Einträge beginnen je auf neuer
  Seite.

Erster Lauf: bau/hefte/ (elf Hefte, bericht.md, render.py).

## Prüfkennung kurz (v0.5)

Beschluss des Lehrers vom 28.09.: Die Prüfkennung an einer Aufgabe ist
kurz. Die Bank behält die lange Form (bank.md), das Skript setzt sie
beim Bau in allen Rezepten um (`kurzkennung`):

| Bank | Blatt |
| --- | --- |
| (P10 2024 OS) | (P24) |
| (P10 2026 FOR) / EBR / GYM | (P26F) / (P25E) / (P22G) |
| (Abitur 2023 GK) / LK | (A23) / (A23L) |
| (FHR 2025) | (F25) |

Sternchen wie im Original dahinter („(P25*)“), wenn das Original der
Zeile (gleiches Jahr wie die Kennung) im Prüfungskatalog von
mathe-nachhilfe stern = ja trägt; ohne Katalog kein Sternchen. Im Heft
steht das Sternchen damit zweimal (`\steil` und Kennung); das
Prüfungsheft-Rezept bleibt sonst unverändert. „(P10-Form)“ bleibt, wie
es ist.

## Zweigzeile (v0.5)

Das Prüfungswort der Zweigzeile trägt die Zahl der Jahrgänge:
„P10 ×5“ heißt, der Typ kam in fünf der dreizehn P10-Jahrgänge vor;
ebenso „Abi GK ×8“, „Abi LK ×n“, „FHR ×n“ (`pruefwort_zahl`). Je
Prüfungsmarke der Marken-Zeile (P10, Abitur GK, Abitur LK, FHR): die
Originale der Bankzeilen dieser Einheit im Profil, deren Typen aus den
Prüfungskatalogen (msa-/abi-/iqb-/fhr-katalog.csv), dann die
verschiedenen Jahre, in denen einer dieser Typen im Profil vorkommt
(alle Blöcke, alle Papiere des Profils). Ohne Katalog: die Jahre der
Originale selbst; ohne Original die Marke ohne Zahl. „keine …“ bleibt
wörtlich; mehrere Marken stehen mit „ · “ nebeneinander (bis v0.4 nur
die erste). Die log zeigt je Einheit PRÜFWORT mit Quelle.

## Rezept Zettel (v0.5)

Beschluss des Lehrers vom 28.09.: Basisaufgaben (Teil A der P10, ohne
Rechner) werden getrennt geübt, am Stundenanfang ein Zettel mit zehn
kurzen Aufgaben, je Stunde ein neuer, ohne Wiederholung. Aufruf:

    python3 werkzeuge/zusammenbau.py --zettel basis [--nummer n]
        [--ohne-register] [--aus <ordner>] [--vorlage <sty>]

- Vorrat: bank/_basis/*.jsonl (je Basis-Typ zehn Aufgaben, bank.md
  „Basisvorrat“), Gewichte aus bank/_basis/typen.csv (Spalte
  jahrgaenge).
- Kennung BAS-Z<n>, n = nächste freie Nummer für BAS-Z in
  bau/register.csv; `--nummer n` baut Zettel n (bricht ab, wenn die
  Kennung schon im Register steht). `--ohne-register`: Ordner BAS-Z0,
  Inhalt von Zettel n (Voreinstellung die nächste freie Nummer).
- Inhalt von Zettel n hängt nur vom Vorrat und von n ab: der Plan wird
  von Zettel 1 bis n durchgerechnet (`zettel_plan`). Je Zettel zehn
  verschiedene Typen. Typen mit allen 13 Jahrgängen stehen auf jedem
  Zettel (zurzeit keiner; der häufigste hat neun); die übrigen Plätze
  nach Stride-Verfahren: gewählt die kleinsten Stände (bei Gleichstand
  das größere Gewicht, dann die Folge in typen.csv), danach Stand +
  1/Gewicht. Ein Typ mit neun Jahrgängen kommt so neunmal so oft wie
  einer mit einem, bis sein Vorrat leer ist. Startstand gestaffelt:
  der i-te von m Typen mit Gewicht w beginnt bei (i + 0,5) / (m · w);
  so mischen sich häufige und seltene Typen von Zettel 1 an (mit Start
  0 standen alle 41 Typen auf Zettel 1–4 und danach fast nur noch die
  häufigen). Der k-te Einsatz eines Typs nimmt Variante k: keine
  Aufgabe auf zwei Zetteln.
- Seitenmaß: höchstens zwei große Grafiken (Koordinatensystem,
  Wertetabellen) je Zettel und geschätzte Höhe der zehn Aufgaben
  höchstens 25 cm (`zettel_hoehe`, geeicht an 41 Probezetteln: Text
  nach Zeichen, Grafik nach Baustein; bei der Wahl bleibt für jeden
  noch offenen Platz 1,45 cm frei). Ein Typ, der nicht passt, wartet
  auf den nächsten Zettel. Geht das gegen Ende des Vorrats nicht mehr
  auf, wird ohne Maß gewählt; die log nennt dann „ÜBER DEM MASS“.
  Probe 28.09.: alle 41 Zettel des Vorrats zwei Seiten.
- Reicht der Vorrat nicht mehr für zehn Typen, baut das Skript nicht
  und meldet „Vorrat erschöpft ab Zettel n“ (log und bau.json
  `vorrat_erschoepft_ab`). Beim Vorrat vom 28.09. (41 Typen, 410
  Aufgaben): erschöpft ab Zettel 42, also 41 Zettel.
- Satz: eine Seite Aufgaben, nummeriert 1–10 (je `aufgabe`, Titel =
  Aufgabentext mit Feld und Kennung), danach `\begleitteil` mit
  `\erg{1}{…}` bis `\erg{10}{…}` als zweite Seite (Rückseite).
  Reihenfolge auf dem Zettel nach Bereich (ZETTEL_FOLGE im Skript:
  Zahlen, Prozente, Größen, Terme und Gleichungen, Funktionen,
  Geometrie, Wahrscheinlichkeit). Aufgabe mit einer Grafik: Text links
  (0,6 der Breite), Grafik rechts (0,37) in `minipage`; Reihe von
  Figuren (`\quad`) und Wertetabellen unter dem Text. Kurze
  Ankreuzoptionen (zusammen höchstens 70 Zeichen Quelltext) in einer
  Zeile statt je `\kreuz` eine Zeile – abweichend von der Anleitung,
  damit zehn Aufgaben auf eine Seite passen. `ablesen`-Koordinatensysteme
  in der Form `klein` (Karo 3,5 mm). Aufgabenteil in `\small`.
- Dateien: bau/zettel/<K>/<K>.tex, mathblatt.sty (Kopie), bau.json
  (je Aufgabe id, kette, jahrgaenge, variante, original),
  zusammenbau.log (VORRAT, AUSWAHL, SATZ, Strukturprüfung);
  Registerzeile mit eintraege `_basis`, bestellung
  `zettel=basis, nummer=n`.
- Kompilieren: `xelatex <K>.tex` einmal; soll zwei Seiten geben.

Erster Lauf: bau/zettel/ (BAS-Z1 bis BAS-Z10, bericht.md).

## Rezept Prüfungs-Fokus (v0.6)

Beschluss des Lehrers vom 28.09.: ein kleines Prüfungsheft zu genau
einer Kette, Rezeptbuchstabe P, Kennung XXX-P<n>. Aufruf:

    python3 werkzeuge/zusammenbau.py <eintrag> --fokus-pruefung "<kette>"
        [--heft msa|abitur-gk|abitur-lk|fhr] [--einheiten n]
        [--aus <ordner>] [--ohne-register]

- Kette wortgleich wie im Feld kette (ohne Rücksicht auf Groß- und
  Kleinschreibung), gleichnamige Pflichtkette eingeschlossen. Profil
  über `--heft` (ohne Angabe msa). Einheit über `--einheiten n` (genau
  eine), sonst die erste Einheit, in der die Kette Prüfungshöhen im
  Profil hat. Keine Prüfungshöhe: Abbruch mit den vorhandenen
  Kettennamen.
- Prüfungshöhe wie im Heft: jede Zeile der Kette, deren Original
  (sonst die Prüfkennung im Text) zum Profil gehört, gleich welche
  hoehe (`profil_von`).
- Inhalt: Nr. 1 Anlauf (Vorstufe, Grundfall, Sprosse mit Fallstrick,
  je kleinste Variante ohne Original, Prüfkennung entfernt; Regel wie
  im Heft, `HeftBau.anlauf`); danach die Prüfungsaufgaben (alle
  Varianten aller Originale, nach Sprosse und Variante, Prüfkennung
  kurz mit Sternchen, `\steil`/`\sgl` bei stern = ja; geteilt nach
  2.3 g, „– weiter“); am Ende der Merkkasten der Einheit aus der Mappe
  (`\uebersichtskasten`, wie `--kasten`; fehlt er, entfällt er, log
  KASTEN und bau.json `kasten`).
- Kopf: `\blattkopf*{<Thema>}{<Kette> · Prüfungs-Fokus MSA}{<Fuß>}`,
  Fußzeile „<Thema> · <Kette> · Prüfungs-Fokus MSA · <K>“ (Abitur:
  „Abitur GK“); `\einheitenkopf[e<n>]{Einheit n · <Titel>}`;
  Zweigzeile Zeitmarke (nur msa) und Prüfungswort nur für das Profil
  („P10 ×n“, „Abi GK ×n“), gezählt über die Typen der Originale
  dieser Kette, nicht der ganzen Einheit. `\weit` nur bei msa.
- Dateien: bau/fokus/<K>/ mit <K>.tex, <K>-loesungen.tex, e<n>_a.tex,
  e<n>_l.tex, mathblatt.sty, zusammenbau.log, bau.json (wie im Heft
  je Teilaufgabe lage, original, jahr, punkte, stern; dazu titel,
  kette, einheit, profil, pruefwort, kasten, anlauf, pruefungshoehe,
  originale, jahrgaenge, ausgelassen). Registerzeile mit bestellung
  `fokus_pruefung=<kette>, heft=<profil>, einheiten=<n>, aus=…`.
- Umfang: gedacht sind 2–4 Seiten plus Lösungen; das Skript misst
  nicht, die Seitenzahl steht nach dem Rendern im Bericht.

Erster Lauf: bau/fokus/ (30 Prüfungs-Fokus, bericht.md, render.py).

## Rezept Kompetenzblatt (v0.7)

Beschluss des Lehrers vom 28.09.: Die Grundeinheit des Bauens ist das
Kompetenzblatt – genau eine Kette, 2–4 Seiten, eigene Kennung
XXX-K<n>, einmal gut gemacht. Hefte sind später Zusammenstellungen von
Kompetenzblättern. Aufruf:

    python3 werkzeuge/zusammenbau.py <eintrag> --kompetenz "<kette>"
        --einheiten <n> [--niveau for|ebr] [--dicht] [--ohne <id,id>]
        [--aus <ordner>] [--ohne-register] [--nummer n]

Bauen und Rendern der Prüfsteinblätter: `python3 bau/kompetenz/bauen.py`
(Probe ohne Register, bei Kompilierfehler `--ohne`, bei mehr als vier
Seiten `--dicht`, dann Bau mit Registerzeile, xelatex zweimal, PNG je
Seite, Messwerte in bau.json).

### Aufbau

1. Titel: Ich-kann-Satz der Kette (groß), darunter die Zweigzeile
   (Zeitmarke aus der Marken-Zeile der Katalogeinheit, „P10 ×n“ über die
   Typen der Originale dieser Kette). Keine Einheitenüberschrift, keine
   Verzeichniszeile.
2. „Das kennst du schon“: höchstens drei Fertigkeiten aus zone.jsonl, je
   eine Aufgabe (Grundfall, kleinste Variante); nur Fertigkeiten, deren
   Voraussetzungszeile in der Mappe die Katalogeinheit der Kette nennt
   („Einheit 2“, „Einheit 1 bis 4“, „ab Einheit 2“), danach solche mit
   „alle Einheiten“ oder ohne Angabe; innerhalb der Gruppe mehr gemeinsame
   Wortstämme mit den Bankzeilen der Kette (merkmal, sprosse_text,
   loesung; seit v0.8 ohne aufgabe) zuerst, dann die spezifischere
   Angabe. Gibt es nur eine Fertigkeit, bekommt sie zwei Aufgaben
   (`fertigkeit_einheiten`, `staemme`; log ZONE).
3. Leiter (seit v0.8 ohne Überschrift „Schritt für Schritt“, Befund 37,
   53): die Leiter der Kette ohne Pflichtelemente, je
   Sprosse eine Hauptnummer mit einer Teilaufgabe (Variante 1; hat sie ein
   Original, die kleinste Variante ohne Original; nur Varianten mit
   Original: Variante 1 ohne Prüfkennung). Titel: Ich-kann-Satz der
   Sprosse.
4. Prüfungshöhen (Beschluss d), eine Hauptnummer „Ich kann das auch in
   Aufgaben aus der Prüfung.“: je Original höchstens eine Aufgabe (die
   kleinste Sprosse/Variante); nur Originale aus den jüngsten fünf
   Jahrgängen der Kette (ältere: log RESERVE); verschiedene
   Formulierungen zuerst (erste sechs Wörter des Texts ohne Zahlen und
   Mathe), bis fünf; weniger als vier: aufgefüllt mit weiteren Originalen
   gleicher Formulierung; gibt es nur ein Original, eine Aufgabe. Jüngstes
   Jahr zuerst. `--niveau ebr` lässt Originale mit Stern im
   Prüfungskatalog weg; for nimmt sie ohne Kennzeichnung (Beschluss b).
5. „Zum Merken“: Merkkasten der Katalogeinheit aus der Mappe, seit v0.8
   als Mathe gesetzt (`kasten_mathe`: Formeln in $…$, a/b und a : b als
   \frac, √ als \sqrt, Einheit nach Zahl als Text; Befund 40, 52).
   Abschnittsüberschriften ohne Linie (Befund 49).
6. Lösungen: eigene Datei <K>-loesungen.tex, je Teilaufgabe eine Zeile,
   Lösungsgrafik darunter.

Keine Punkte (Beschluss c). Prüfkennung klein rechts in der Auftaktzeile:
„P10 ’24“, anderes Papier dahinter („P10 ’26 F“), „Abi ’23“, „FHR ’25“
(`kennung_kompetenz`).

### Katalogeinheit der Kette

Die Bank zählt Einheiten nach ihrem Katalog-Commit, die Mappe nach dem
aktuellen (quadratische-gleichungen: p-q-Formel ist Bank e3, Katalog
Einheit 2). Kopf, Merkkasten und Zone kommen deshalb aus der Katalog-
einheit, gefunden über (`mappe_einheit`): die Zeile „- <Kette> (Einheit n“
in „Sprossen je Verfahrenstyp“, sonst Titel der Lerneinheit, „Typen je
Lerneinheit“, Wortüberdeckung, zuletzt die Nummer der Bank (log EINHEIT,
bau.json einheit_katalog_quelle). Rezept P (v0.6) nahm die Banknummer:
QGL-P1 trägt darum den Merkkasten „Nullprodukt“ – Befund.

### Ich-kann-Titel

bau/regal/ich-kann.csv (eintrag;einheit;kette;sprosse;ich_kann;
anweisung;quelle), gemeinsam mit werkzeuge/regal.py. sprosse leer = Titel
der Kette, `p` = Prüfungshöhen, Zahl = Sprosse; einheit 0 = Fertigkeit
der Zone. Der Katalog trägt keine Ich-kann-Sätze; die Titel sind aus
Kettenname, merkmal, sprosse_text und der Mappe umformuliert (Spalte
quelle). Fehlt eine Zeile, setzt das Skript „Ich kann: <merkmal>.“ und
schreibt ICH-KANN fehlt in die log. anweisung: Aufforderung über der
Teilaufgabe (Befund 5); ohne Eintrag bei einer nackten Gleichung „Löse
die Gleichung.“, bei „Rechne: …“ der Auftakt selbst.

### Satz einer Teilaufgabe (layout-befunde.md)

- v0.8 zuerst (`satzform`, bau/sprachlauf/regeln.md): Ist die Aufgabe in
  ganzen Sätzen geschrieben (kein „ – “, kein Stichwort mit Doppelpunkt,
  Satzende am Schluss), steht sie als ein normaler Absatz – kein
  halbfetter Auftakt, keine Kurzfrage. „Verb. Term“ („Berechne.
  $\frac{600}{100}$“): der Verb-Satz als Anweisung, der Term halbfett in
  \displaystyle. Fordert die Aufgabe selbst auf (Frage oder Imperativ),
  entfällt die Anweisung aus ich-kann.csv (log ANWEISUNG). Sonst gilt
  die Zerlegung darunter.

- Zerlegen (`zerlege`): Prüfkennung heraus; \wertetabelle und \kreuz
  heraus; „Kontext – Frage?“ (Frage bis 90 Zeichen) → Kontext als
  Auftakt, bei bis 70 Zeichen halbfett (Mathe mit \boldmath), Frage
  darunter; sonst „Auftakt: Auftrag“ (Auftakt bis 45 Zeichen, ist er
  ein Imperativ, wird er zur Aufforderung); sonst Sätze: Kontext bis
  zur ersten Frage oder Aufforderung, dann je Satz eine Zeile (Befund
  3, 4, 10). Frage beginnt groß; eine Kurzfrage bis drei Wörter
  („p und q?“) entfällt, wenn die Anweisung dasselbe sagt.
- Antwortfeld in eigener Zeile darunter, linksbündig, Felder 2,2 cm
  (\kbfeld), in Punkten 1,2 cm (\kbfeldk); „x1“ → x₁; „;“ trennt
  Zeilen (Befund 4, 8, 29). Ohne Antwortgerüst bei Ein-Zahl-Aufgaben
  ein leeres Feld; bei nackter Gleichung „Lösung: __“.
- Bearbeitungsraum nur bei Rechnen und Begründen (`rechenzeilen`,
  Befund 9): Operatoren der Lösung und Gleichheitszeichen über die Zahl
  der Antwortfelder hinaus; ab zwei Schritten zwei Schreibzeilen,
  Prüfungshöhe mit langer Lösung drei; Gleichung (gleichungsraster)
  immer zwei. Der Raum steht rechts neben Aufgabe und Antwort, bei
  langem Text rechts neben der Antwort, ohne Antwortfeld über die
  Breite.
- Tabelle unter dem Text, linksbündig, Köpfe im Textmodus (\kbwerte-
  tabelle; „Zeit in h“ als Text, x und f(x) als Mathe; Befund 26, 28).
  Grafik oder Tabelle bis halbe Breite links, Antwort/Kreuze/Raum rechts;
  Tabelle und Koordinatensystem nebeneinander; sonst untereinander
  (Befund 27). Kreuze je eine Zeile (Befund 6, 7).
- Zeichnen: Koordinatensystem höchstens 7,5 cm hoch (Karo kleiner, log
  KSYS); zwei Zeichenaufgaben stehen als Paar nebeneinander (zwei
  Hauptnummern oder zwei Teilaufgaben, Text über der Grafik).
- `--dicht`: kurze Rechenaufgaben ohne Grafik und ohne Prüfkennung
  paarweise nebeneinander – nur, wenn das Blatt sonst mehr als vier
  Seiten hat (bauen.py entscheidet an der Probe).
- Flattersatz überall (Befund 25); Hauptnummer als unteilbarer Block je
  Teilaufgabe, der Titel hängt am ersten Block, ein Block, der nicht
  mehr passt, rückt ganz auf die nächste Seite – keine Grafik über der
  Fußzeile (Befund 21).
- Kopfzeile „<Thema> · Kompetenzblatt“, Fußzeile nur Kennung links und
  Seite rechts (Befund 1, 2). Keine Bank-Wörter: das Skript prüft den
  Blatttext auf Anlauf, Prüfungsaufgaben, Sprosse, Vorstufe, Grundfall,
  Fallstrick, Variante, Kette, Prüfungsform, ausgelassen (log BANKWORT).

### Vorspann und fehlende Zeichen

mathblatt.sty bleibt unverändert (Kopie im Ordner). Was fehlt, steht in
vorspann.tex, das der Zusammenbau schreibt und beide Dokumente nach
\usepackage{mathblatt} einlesen: Kopf/Fuß, Titel, Abschnitt,
kbaufgabe/kbblock, kbteil, kbfrage, kbantwort, kbzweispaltig, kbpaar,
kbwertetabelle, kbmerk, kbloesung. Zeichen, die Latin Modern Roman nicht
hat (LM_FEHLT, gemessen mit fontTools über alle Zeichen in bank/ und
mappen/: ≈ α β γ π ∫ ⇔ ✓ ₁ ⁻ ℝ ↔ …), bekommen je eine
\newunicodechar-Zeile – nur die, die im Blatt vorkommen: im Text aus der
ersten vorhandenen Ersatzschrift (FreeSerif, DejaVu Serif, Cambria
Math, Segoe UI Symbol), in Mathe als Mathebefehl (\approx, \alpha);
Hoch- und Tiefzeichen in Mathe als Glyphe der Ersatzschrift. Ohne
Ersatzschrift setzt der Vorspann Mathe. In der Web-Sitzung:
`apt-get install fonts-freefont-otf` (neben den TeX-Paketen aus
render.md). Probe: bau.json schriften_im_pdf (pdffonts) und
ersatzzeichen_im_text (pdftotext).

### Dateien

bau/kompetenz/<K>/: <K>.tex, <K>-loesungen.tex, vorspann.tex,
mathblatt.sty (Kopie), <K>.pdf, <K>-loesungen.pdf, <K>-<n>.png und
<K>-loesungen-<n>.png (pdftoppm -r 80), zusammenbau.log, bau.json
(kennung, titel, kette, einheit, einheit_katalog, niveau, zweigzeile,
klasse_os, klasse_gym, zone, kasten, hauptnummern, teilaufgaben,
pruefungshoehe, originale, jahrgaenge, ersatzzeichen, aufgaben je
Teilaufgabe mit lage zone/leiter/pruefung, original, jahr,
stern_im_original; nach dem Rendern seiten, seiten_loesungen,
fehlende_zeichen, overfull, schriften_im_pdf, ersatzzeichen_im_text,
probe). Registerzeile mit bestellung `kompetenz=<kette>, einheiten=n,
niveau=for, dicht=…, ohne=…`.

Erster Lauf: bau/kompetenz/ (fünf Blätter, bericht.md).

### Regal

werkzeuge/regal.py plant aus allen Ketten der Bank die Kompetenzblätter
(bau/regal/regal.csv, regal.html; Anleitung im Kopf des Skripts): je
Verfahrenskette eines, je Einheit eines für die Typen ohne Kette.
Es nutzt Mappe, mappe_einheit, pruefwort_zahl und lies_ichkann dieses
Skripts. Die Kennungen im Regal sind vorgesehen; beim Bau nach dem Regal
`--nummer n` mitgeben.

## Strukturprüfung

Je Quelltext: Klammern {} ausgeglichen; jeder Befehl Standard-
LaTeX (STANDARD aus bank-pruef.py), Rahmenbefehl (RAHMEN im
Skript; seit v0.5 auch `\linewidth` und die Umgebung `minipage` für
den Zettel) oder Baustein aus mappen/_bausteine.md mit passender
Argumentzahl; kein nacktes %; Umgebungen paarig; Umlaute direkt;
gerade Zahl von $; höchstens 26 Teilaufgaben je Hauptnummer.
Zeilen ab Spalte 0 mit % sind Kommentar und werden übergangen.

## Was v0.1 nicht kann (Stand v0.9)

Seit v0.9 gehen: Ich-kann-Titel, Anweisungen und Zweigzeile Teil 1
(ich-kann.csv, Mappe), Zahl der Schreibzeilen (aus der Lösung),
Grundfall mehrfach und Vorstufe mit allen Zeilen, Teilung nach 2.3 g
außerhalb des Fokus, Pflichtelemente je eine Hauptnummer, kurze
Teilaufgaben zwei je Zeile, „baut auf:“. Es bleibt:

- `\verfahren`-Namen: nicht in der Bank.
- Teilung nach Form (Streifen, rechnen, Sachtext); Zeilenzahl im
  `gleichungsraster` nach dem Grundfall.
- Schnitt der Zeitachse nach Klasse (Zone, Ausblick), Schulform, „nicht
  für alle“.
- Darstellung für schwach, wo die Zeile keine grafik hat;
  Grundvorstellung als erste Hauptnummer der Zone.
- „mit beispiel“, „mit tipps“, Sek-II-Kursart.
- Fokus und schwach zusammen.
- Kompilieren im Skript (das tut bau/terme/lernblatt-messen.py),
  Seitenfüllung (4.2), Lösungsgrafiken klein nebeneinander.
- Ein gemeinsamer Auftrag, wenn Zahlen im Text stehen („Klammere den
  Faktor 3 aus: …“) oder die Bankzeilen einer Sprosse verschieden
  formuliert sind (Hinweis AUFTRAG-SATZ).

## Erster Render prüft

- Zeichen in Titeln und Kästen: ↔, →, ≙, · in der Schrift.
- Hauptnummern mit WARNUNG in der log (über dem Halbseitenmaß):
  Bruch über die Seite, `Package mathblatt Warning`.
- `\streifen` endet mit `\par`: das Feld steht darunter statt
  daneben (4.3).
- `\hfill (P10 …) \\` vor Feld oder `\kreuz`-Zeilen.
- `\rechnung` mitten im Text einer Teilaufgabe und in `\swz`.
- schwach: 10-cm-Streifen in der rechten Spalte (0,62 Breite);
  leere rechte Spalten.
- `\sachtabelle` erst nach den Ankreuzoptionen.
- Verzeichniszeile und Sprungziele; Abhakseite mit Zone nur im
  Gesamt; Kopfzeile mit Kurzform der Einheit.

## Offen

Entscheidungen, die der Auftrag vom 27.09. offenließ:

1. `--aus` ist der Ausgabeordner. Drei Läufe an einem Tag
   brauchen getrennte Ordner.
2. `--kasten` und `--vorlage` sind zusätzliche Schalter.
3. Dateisatz und Rahmen nach Stufe 6 (Verzeichniszeile,
   abhaken.tex, `\mitzone`, loesungen.tex) wie im Testlauf
   2026-09-26, nicht nach Stufe 3 wie im Muster 2026-09-22;
   e<n>.tex ohne Lösungen (4.1).
4. Dateinamen nach Katalognummer; der Kopf zählt die gewählten
   Einheiten („Einheit 1 von 2“), im Fokus Katalognummer ohne
   „von n“.
5. Zone: je Sprosse die kleinste Variante (s1 v1, s2 v3), das
   Zone-Paar als zwei Hauptnummern am Ende; es entfällt mit
   seiner Fertigkeit. Fallstricke (ab s3) entfallen.
6. Fokus: Erkennungsschritte entfallen nach Auftrag, obwohl 2.5
   sie verlangt. Teilung nur im Fokus, weil 34 Teilaufgaben in
   einer Nummer über z) hinaus zählen (Kompilierfehler).
7. schwach: Grundfall mit allen Varianten (2.8), abweichend von
   „Variante 1“; schwach gilt auch in der Zone; `\swz` mit drei
   Zeilen bei Fehler, Anwendung, Prüfung und Text, sonst zwei;
   `\streifenfeld` wird `\streifen`, das Feld wandert in den
   Text.
8. Zeitmarke ohne Klasse „ab Kl. n“, Gymnasium als Zusatz, wo es
   abweicht; mit Klasse nach 1.5. `\weit` ohne Klasse, wenn die
   Marken OS-Klassen tragen.
9. Merkkasten wortgleich als Text, `&` als „und“, lange Lücken
   als `\quad`; über fünf Zeilen nur TODO, nicht gekürzt.
10. Lösung der Erklärzeile: `\ldots` mit TODO.
11. Archivdatum nach `date` (2026-09-27), nicht 2026-09-28.

Entscheidungen, die der Auftrag vom 28.09. (v0.3) offenließ:

12. Fußzeile über `\blattkopf*` statt `\blattfuss` (siehe
    Kennung); Bezeichnung im Fuß ist die des Dokuments (Lernblatt,
    Gesamt, Lösungen, Einheit 2, Fokus Prozentsatz · Lösungen).
13. Das Blatt heißt <K>.tex: beim Lernblatt das bisherige
    lernblatt.tex (ohne Zone), beim Fokus fokus.tex; die übrigen
    Dokumente tragen die Kennung mit Zusatz.
14. Voreingestellter Ordner bau/<eintrag>/<kennung>/ statt
    bau/<eintrag>/<datum>/; die Prüfsteine unter 2026-09-27/
    bleiben.
15. Registerzeile auch bei Strukturfehlern: Die Dateien liegen
    unter der Kennung, die Nummer ist damit verbraucht;
    bau.json trägt die Fehlerzahl.
16. Rezept H: Buchstabe und Kürzelregel sind im Skript, einen
    Heftbau mit mehreren Einträgen hat v0.3 nicht.
