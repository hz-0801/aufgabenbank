# zusammenbau.py – aus der Bank ein Blatt (Quelltext)

Stand 2026-09-27, v0.1. Baut aus bank/<eintrag>/ LaTeX-Quelltexte
für die Vorlage mathblatt.sty (hz-0801/blattbau). Kompiliert wird
nicht; die Strukturprüfung im Skript ersetzt den Lauf bis zum
ersten Render.

## Aufruf

    python3 werkzeuge/zusammenbau.py <eintrag> [--einheiten 1,3]
        [--zone ja|nein|kurz] [--fokus <kette>] [--schwach]
        [--klasse 7] [--kasten] [--aus <ordner>]
        [--vorlage <pfad/mathblatt.sty>]

Ohne Schalter: Lernblatt mit Zone und allen Einheiten, je Sprosse
Variante 1, ohne Klasse. Rückgabe 1, wenn die Strukturprüfung
Fehler findet (die Dateien werden trotzdem geschrieben).

| Schalter | Wirkung |
| --- | --- |
| `--einheiten 1,3` | nur diese Einheiten; Zone nur mit ihren Fertigkeiten |
| `--zone ja` | je Fertigkeit Sprosse 1 und 2, dazu das Zone-Paar |
| `--zone kurz` | je Fertigkeit nur Sprosse 1 |
| `--zone nein` | keine Zone |
| `--fokus <kette>` | Name wortgleich aus dem Feld kette; alle Varianten |
| `--schwach` | Form nach unterrichtsblatt 2.8 |
| `--klasse n` | Zeitmarke relativ; bis Klasse 10 `\weit` |
| `--kasten` | Merkkasten am Anfang jeder Einheit (3.1) |
| `--aus <ordner>` | Ausgabeordner statt bau/<eintrag>/<datum>/ |
| `--vorlage <sty>` | Pfad zu mathblatt.sty |

mathblatt.sty sucht das Skript sonst unter $BLATTBAU,
../hz-0801/blattbau/ und ../blattbau/ neben dem Repo.

## Ausgabe

Lernblatt und schwach: blatt0_a/_l (Zone), e<n>_a/_l je Einheit
(n = Nummer im Katalog), Rahmen blatt0.tex, e<n>.tex,
lernblatt.tex, gesamt.tex, loesungen.tex, abhaken.tex. Fokus:
blatt0_a/_l, e<n>_a/_l, fokus.tex, fokus_loesungen.tex. Dazu
mathblatt.sty als Kopie und zusammenbau.log: jede Auswahl
(AUSWAHL, WEG), Köpfe, Teilungen, Warnungen, alle TODO mit Datei
und Zeile, die Strukturprüfung.

Kompilieren (im Code-Tab): `xelatex gesamt.tex` zweimal (Abhak-
seite), ebenso lernblatt.tex, loesungen.tex, blatt0.tex.

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
- Prüfkennung wie im Muster 2026-09-22: `\hfill (P10 …)`, bei
  folgendem Feld mit `\\`. Keine Sternchen (2.4 d).
- Kopf aus der Mappe: Titel aus „Lerneinheiten“, Zeitmarke und
  Prüfungswort aus der Marken-Zeile (1.5), Merkkasten aus
  „Merkkasten“, Zuordnung der Zone aus „Voraussetzungen“.
- Was Bank und Mappe nicht tragen, steht als `%% TODO` in der
  Zeile davor und in der log, nie als geratener Text.

## Strukturprüfung

Je Quelltext: Klammern {} ausgeglichen; jeder Befehl Standard-
LaTeX (STANDARD aus bank-pruef.py), Rahmenbefehl (RAHMEN im
Skript) oder Baustein aus mappen/_bausteine.md mit passender
Argumentzahl; kein nacktes %; Umgebungen paarig; Umlaute direkt;
gerade Zahl von $; höchstens 26 Teilaufgaben je Hauptnummer.
Zeilen ab Spalte 0 mit % sind Kommentar und werden übergangen.

## Was v0.1 nicht kann

- Ich-kann-Titel, Anweisungen, Zweigzeile Teil 1, Zahl der
  Rechenplatz-Zeilen, `\verfahren`-Namen: nicht in der Bank,
  daher TODO.
- Grundfall mehrfach im Lernblatt (2.3 b) und Vorstufe mit vier
  bis fünf Teilaufgaben (2.3 a): Regel „Variante 1“ gibt je eine.
- Teilung nach 2.3 g außerhalb des Fokus; Teilung nach Form
  (Streifen, rechnen, Sachtext); Pflichtelemente je eine
  Hauptnummer (2.3 c).
- `teilezwei` für kurze Teilaufgaben; Zeilenzahl im
  `gleichungsraster` nach dem Grundfall.
- Schnitt der Zeitachse nach Klasse (Zone, Ausblick), Schulform,
  „baut auf:“, „nicht für alle“.
- Darstellung für schwach, wo die Zeile keine grafik hat;
  Grundvorstellung als erste Hauptnummer der Zone.
- „mit beispiel“, „mit tipps“, Sek-II-Kursart.
- Fokus und schwach zusammen.
- Kompilieren, Seitenfüllung (4.2), Lösungsgrafiken klein
  nebeneinander.

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
