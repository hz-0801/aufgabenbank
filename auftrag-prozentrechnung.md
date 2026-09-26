# Auftrag: Prüfstein Aufgabenbank – prozentrechnung

Modell: Opus. Web-Sitzung, Repo aufgabenbank. Kein Rückfrage-
Stopp; Commit je Einheit auf main, push nach jedem Commit (vorher
`git pull --rebase`), kein eigener Branch.

## Ausgangslage

Die Bank ist neu (bank.md, Datei 1). Dieser Auftrag füllt sie für
den ersten Eintrag, prozentrechnung, damit der Chat morgen die
Form am Ergebnis beurteilt. Zum Vergleich liegen drei Blätter zu
diesem Thema in hz-0801/mathe-nachhilfe unter blaetter/
prozentrechnung/ und blaetter/testlauf-2026-09-25/03-prozent-7-
schwach/ (nur lesen, nicht kopieren).

## Quellen (per Raw-URL, https://raw.githubusercontent.com/…)

- hz-0801/mathe-nachhilfe/main/katalog/prozentrechnung.md – der
  Eintrag; Commit-Hash über die GitHub-API
  (repos/hz-0801/mathe-nachhilfe/commits?path=katalog/
  prozentrechnung.md&per_page=1) in stand.md.
- hz-0801/blattbau/main/Anleitung_mathblatt.md – Bausteine.
- hz-0801/blattbau/main/unterrichtsblatt.md – nur Abschnitt 2.2
  (Zone), 2.3 c (Pflichtelemente), 2.4 (Progression), 3.6
  (Zahlen) als Maßstab; nichts davon in die Bank kopieren.
- hz-0801/mathe-nachhilfe/main/msa/msa-katalog-kontext.csv und
  msa-katalog-basis.csv – die Originale, deren Kennungen der
  Eintrag unter „Prüfungsform" nennt (Spalten gegeben, gesucht,
  verfahren, fehlerquelle).

## Schritte

1. Repo-Grundlage: README.md um einen Absatz ergänzen (was die
   Bank ist, Verweis auf bank.md); Ordner bank/ und werkzeuge/;
   .gitattributes mit `* text eol=lf`. Commit „bank: Grundlage".
2. werkzeuge/bank-pruef.py nach bank.md „Prüfung" schreiben
   (Python 3, nur Standardbibliothek; pruef wird mit eval in einem
   leeren Namensraum plus math ausgewertet; Zahlen in loesung
   werden mit einem regulären Ausdruck gezogen, Komma als
   Dezimaltrenner, Prozentzeichen und Einheiten ignoriert;
   Vergleich mit Toleranz 0,005 nach Rundung auf die Stellen der
   Lösung). Selbsttest mit drei Beispielzeilen. Commit
   „werkzeuge: bank-pruef.py".
3. Eintrag lesen, ganz. Aus „Für schwache Schüler" die fünf
   Sprossenketten (Einheit 1–5), aus „Typen je Lerneinheit" die
   Typen ohne Kette, aus „Typische Fehler" die Muster, aus
   „Prüfungsform" und „Zielmarke" die Originale mit Kennung, aus
   „Voraussetzungen (Blatt 0)" die Fertigkeiten. Die Merkkästen
   nur für die Sperre lesen.
4. Zone: bank/prozentrechnung/zone.jsonl nach bank.md, Mengen
   „Zone". Prüfskript, Commit „prozentrechnung: zone".
5. Einheit 1 bis 5, nacheinander, je Einheit: e<n>.jsonl mit
   allen Ketten in Kettenfolge, Vorstufe zuerst, danach die
   Pflichtelemente; Prüfskript bis null Abweichungen; Commit
   „prozentrechnung: e<n>", push. Fehlerregel: Scheitert eine
   Einheit zweimal am Prüfskript, bleibt sie mit dem Stand
   liegen, stand.md sagt es, die nächste Einheit folgt.
6. stand.md: Katalog-Commit, Datum aus `date`, je Datei Zahl der
   Zeilen, Zahl je hoehe, offene Punkte. Commit
   „prozentrechnung: stand".

## Gegenprobe

katalog/prozentrechnung.md führt fünf Einheiten und fünf
Sprossenketten (eine je Einheit); die Zeilen „Sprossen je
Verfahrenstyp" nennen für Einheit 2 den Grundfall „Teil von 100
(4×)" – in e2.jsonl stehen dafür fünf Zeilen mit hoehe grundfall.
Die Kastenzahlen des Eintrags (Merkkasten Einheit 1–5) kommen in
keiner aufgabe als ganze Gleichung vor; grep über die jsonl auf
die Beispielzeilen der Kästen: 0 Treffer.

## Regeln

- Zeilen in jsonl beliebig lang; in md höchstens 72 Zeichen.
- Nichts aus den Blättern unter blaetter/ kopieren; sie sind
  Vergleich, nicht Quelle.
- Kein LaTeX kompilieren (nicht verfügbar); die Bausteinaufrufe
  gegen die Anleitung prüfen (Name und Argumentzahl).
- Was der Auftrag nicht regelt, entscheidest du und schreibst es
  in stand.md unter „Entscheidungen".

## Bericht

Im Chat, am Ende. Erste Zeile das Modell. Je Einheit: Zeilen,
davon grundfall/sprosse/pruefung/pflicht, Abweichungen des
Prüfskripts vor der Korrektur, was zweimal scheiterte. Die
Gegenprobe im Wortlaut mit Ist-Wert. Drei Beispielzeilen (je eine
aus Grundfall, Prüfungshöhe, Fehler finden) wortgleich. Letzte
Zeile: „gepusht auf main, Commit <hash>".
