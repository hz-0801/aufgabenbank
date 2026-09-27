# Auftrag: Zusammenbau v0.1 – aus der Bank ein Blatt (Quelltext)

Modell: Opus. Web-Sitzung, Repo aufgabenbank, main. Commit je Teil,
vor jedem Push `git pull --rebase`, `git push origin main`, kein
eigener Branch, kein Pull Request. Geschrieben wird nur in
werkzeuge/zusammenbau.py, werkzeuge/zusammenbau.md, bau/ und in
diesen Auftrag (Verschieben am Ende). Nichts unter bank/, nicht
bank.md, nicht mappen/.

## Ausgangslage

Die Bank hält je Sprosse geprüfte Aufgaben (bank.md: Felder,
hoehe, form, grafik, Bausteine). Blätter sollen künftig durch
Auswahl aus der Bank entstehen, nicht durch Erzeugung im Chat
(ziel.md in hz-0801/mathe-nachhilfe, Linie vom 26.09.). Dafür
fehlt das Werkzeug: ein Skript, das aus bank/<eintrag>/ nach
einer Bestellung LaTeX-Quelltexte für die Vorlage mathblatt.sty
baut. Kompiliert wird hier nicht (kein LaTeX); der erste Render
kommt im Code-Tab. Prüfstein ist prozentrechnung, für das drei
vom Prompt gebaute Blätter als Vergleich vorliegen.

## Quellen (lesen, nicht ändern)

- bank.md, mappen/_bausteine.md, bank/prozentrechnung/.
- hz-0801/blattbau (klonen): Anleitung_mathblatt.md (Grundgerüst,
  Makros, Schreibweisen), mathblatt.sty (Kopf mit Versionszeile),
  unterrichtsblatt.md Abschnitte 3 „Inhalt der Blätter“ und 4
  „Layout und PDF“ – die beschreiben, wie ein fertiges Blatt
  aussieht; Abschnitt 2 nur, wo 3 und 4 darauf verweisen.
- hz-0801/mathe-nachhilfe (klonen, `--filter=blob:none` reicht):
  blaetter/prozentrechnung/2026-09-22/src/ (Lernblatt, Dateien
  blatt0, e1–e5, je _a und _l), blaetter/prozentrechnung/
  2026-09-24/src/ (Fokus), blaetter/testlauf-2026-09-26/
  3-prozent-7-schwach/ (Form schwach) als Muster für Aufbau und
  Dateisatz; mappen/prozentrechnung.md für Merkkästen und
  Marken.

## Teil 1: werkzeuge/zusammenbau.py

Aufruf: `python3 werkzeuge/zusammenbau.py <eintrag> [--einheiten
1,3] [--zone ja|nein|kurz] [--fokus <kette>] [--schwach]
[--klasse 7] [--aus bau/<eintrag>/<datum>/]`. Ohne Schalter:
Lernblatt mit Zone und allen Einheiten, je Sprosse Variante 1,
Klasse ohne.

Ausgabe unter bau/<eintrag>/<datum aus date>/: derselbe Dateisatz
wie im Muster 2026-09-22 (blatt0, e<n>, gesamt, loesungen; je
Blatt Aufgaben- und Lösungsfassung, wenn das Muster es so
trennt), dazu mathblatt.sty als Kopie aus blattbau und eine
zusammenbau.log mit jeder Auswahlentscheidung (welche Zeile,
warum).

Regeln des Baus, deterministisch (gleiche Eingabe, gleiche
Ausgabe):
- Reihenfolge je Einheit: Erkennungsschritte → Verfahrensketten
  in kette_nr → Typen ohne Kette → Pflichtelemente, innerhalb der
  Kette nach sprosse, je Sprosse Variante 1 (Fokus: alle
  Varianten der genannten Kette, andere Ketten entfallen).
- Zone aus zone.jsonl: „ja“ alle Fertigkeiten je s1 und s2 plus
  das Zone-Paar; „kurz“ nur s1; „nein“ entfällt.
- Hauptnummer je Kette, Teilaufgaben je Sprosse; form bestimmt den
  Baustein (teil, gleichungsraster, dreisatz, streifenfeld,
  streifenleer, ankreuzen, tabelle, zeichnen, text) nach
  Anleitung_mathblatt.md; grafik und loesungsgrafik wörtlich
  eingesetzt; antwort als Antwortlinie oder Raster.
- Einheitenkopf, Zweigzeile (was gelernt wird · Zeitmarke ·
  Prüfungswort) und Merkkasten kommen aus der Mappe des Eintrags
  (Abschnitt 1, Marken-Zeilen und Merkkästen je Einheit); was
  sich nicht sicher parsen lässt, steht als „%% TODO <was>“ im
  Quelltext und in der log, nie als geratener Text.
- Prüfkennung und Sternchen wie in unterrichtsblatt 3.6; hoehe
  pruefung setzt die Marke, die das Muster dafür nutzt.
- Klasse gesetzt: Zeitmarke relativ („neu in diesem Jahr“) nach
  den Marken-Zeilen; ohne Klasse absolut.
- Form schwach: Aufbau nach unterrichtsblatt 2 und dem
  Testlauf-Muster 3-prozent-7-schwach (Raster je Schritt,
  Darstellung neben der Aufgabe, Merkkasten am Ende).
- Lösungen: loesung je Aufgabe in der Lösungsfassung, mit
  loesungsgrafik.

Strukturprüfung statt Kompilieren, als Funktion im Skript:
Klammern ausgeglichen; jeder \-Befehl entweder Standard-LaTeX
(Liste aus bank-pruef.py STANDARD) oder Baustein aus
_bausteine.md mit richtiger Argumentzahl; kein nacktes %; jede
Umgebung geschlossen; Umlaute direkt. Verstöße als Fehler mit
Datei und Zeile.

Commit „zusammenbau v0.1“, push.

## Teil 2: Prüfstein prozentrechnung

Drei Läufe: Lernblatt (Standard), Fokus auf die Kette, die das
Muster 2026-09-24 übt (aus dessen Quelltext ablesen), schwach mit
Klasse 7. Für jeden Lauf gegen das Muster vergleichen, Zahl je
Blatt: Hauptnummern, Teilaufgaben, Merkkästen, Grafiken, Zeilen
Quelltext; dazu je Lauf drei Stellen, an denen Bank-Blatt und
Muster sich im Aufbau sichtbar unterscheiden, mit Zeilenangabe.
Ergebnis nach bau/prozentrechnung/<datum>/vergleich.md. Commit
„bau: Prüfstein prozentrechnung“, push.

## Teil 3: werkzeuge/zusammenbau.md

Kurz: Aufruf, Schalter, Bauregeln wie oben, was v0.1 nicht kann
(Liste), was der erste Render prüfen muss. Commit „zusammenbau:
Anleitung“, push.

## Gegenprobe

- Zweimal derselbe Aufruf ergibt byteidentische .tex (bis auf
  Datum im Ordnernamen).
- Strukturprüfung 0 Fehler für alle drei Läufe.
- Jede Zeile von bank/prozentrechnung/ mit hoehe grundfall
  erscheint im Lernblatt genau einmal (Variante 1); keine Zeile
  mit variante 2 erscheint, außer im Fokus.
- Zahl der Hauptnummern im Lernblatt = Zahl der Ketten mit
  Sprossen in den e-Dateien (Erkennungsschritte mitgezählt, wie
  das Skript es entscheidet und in der log begründet).

## Regeln

- Kein LaTeX kompilieren; ist doch ein xelatex verfügbar, darfst
  du es nutzen und sagst es im Bericht.
- Zeilen in md höchstens 72 Zeichen; .tex und .py frei.
- Was der Auftrag nicht regelt, entscheidest du und schreibst es
  in den Bericht und in zusammenbau.md „Offen“.
- Am Ende diesen Auftrag nach archiv/auftrag-zusammenbau-
  2026-09-28.md verschieben (git mv, Datum aus `date`), Commit
  „archiv: auftrag-zusammenbau“, push.

## Bericht

Im Chat, am Ende. Erste Zeile das Modell. Dann: Aufruf und Schalter
wie gebaut; Vergleichstabelle der drei Läufe; die neun Stellen
mit Unterschied; die TODO-Liste aus den Quelltexten; was v0.1
nicht kann; Entscheidungen, die der Auftrag offenließ. Letzte
Zeile: „gepusht auf main, Commit <hash>“.
