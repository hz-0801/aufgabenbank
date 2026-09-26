# Auftrag: Prüfstein Aufgabenbank – quadratische-funktionen

Modell: Opus. Web-Sitzung, Repo aufgabenbank. Kein Rückfrage-
Stopp; Commit je Einheit auf main, push nach jedem Commit (vorher
`git pull --rebase`), kein eigener Branch.

## Ausgangslage

Die Bank ist neu (bank.md im Repo). Parallel füllt eine zweite
Sitzung den Eintrag prozentrechnung (Verfahrensthema); dieser
Auftrag füllt quadratische-funktionen (Objektthema mit Graphen,
Wertetabellen und Zeichenflächen), damit der Chat morgen die Form
an beiden Sorten beurteilt. Zum Vergleich liegen Blätter in
hz-0801/mathe-nachhilfe unter blaetter/nullstellen/ und
blaetter/testlauf-2026-09-25/07-nullstellen-fokus/ (nur lesen,
nicht kopieren).

## Quellen (per Raw-URL, https://raw.githubusercontent.com/…)

- hz-0801/mathe-nachhilfe/main/katalog/quadratische-funktionen.md –
  der Eintrag; Commit-Hash über die GitHub-API
  (repos/hz-0801/mathe-nachhilfe/commits?path=katalog/
  quadratische-funktionen.md&per_page=1) in stand.md.
- hz-0801/blattbau/main/Anleitung_mathblatt.md – Bausteine.
- hz-0801/blattbau/main/unterrichtsblatt.md – nur Abschnitt 2.2
  (Zone), 2.3 c (Pflichtelemente), 2.4 (Progression), 3.6
  (Zahlen) als Maßstab; nichts davon in die Bank kopieren.
- hz-0801/mathe-nachhilfe/main/msa/msa-katalog-kontext.csv und
  msa-katalog-basis.csv – die Originale, deren Kennungen der
  Eintrag unter „Prüfungsform" nennt (Spalten gegeben, gesucht,
  verfahren, fehlerquelle).

## Schritte

1. Nach dem Pull prüfen, dass bank.md und werkzeuge/bank-pruef.py
   vorhanden sind; das Skript einmal mit `--help` oder ohne
   Argument aufrufen. Fehlt das Skript nach zehn Pulls, schreib
   eine eigene Fassung nach bank.md „Prüfung" unter
   werkzeuge/bank-pruef-qf.py und sag es im Bericht.
2. Grafiken: Aufgaben mit Ablesegrafik oder Zeichenfläche tragen
   im Feld grafik den vollständigen Bausteinaufruf (ksys,
   funktion, Punkte) aus den Aufgabenwerten; Achsenbereich so,
   dass alles Gefragte in der Fläche liegt; Karo nach Anleitung.
   Was eine Aufgabe an Grafik meint, steht als Aufruf, nie als
   Beschreibung.
3. Eintrag lesen, ganz. Aus „Für schwache Schüler" die
   Sprossenketten (Einheit 1–4), aus „Typen je Lerneinheit" die
   Typen ohne Kette, aus „Typische Fehler" die Muster, aus
   „Prüfungsform" und „Zielmarke" die Originale mit Kennung, aus
   „Voraussetzungen (Blatt 0)" die Fertigkeiten. Die Merkkästen
   nur für die Sperre lesen.
4. Zone: bank/quadratische-funktionen/zone.jsonl nach bank.md, Mengen
   „Zone". Prüfskript, Commit „quadratische-funktionen: zone".
5. Einheit 1 bis 4, nacheinander, je Einheit: e<n>.jsonl mit
   allen Ketten in Kettenfolge, Vorstufe zuerst, danach die
   Pflichtelemente; Prüfskript bis null Abweichungen; Commit
   „quadratische-funktionen: e<n>", push. Fehlerregel: Scheitert
   eine Einheit zweimal am Prüfskript, bleibt sie mit dem Stand
   liegen, stand.md sagt es, die nächste Einheit folgt.
6. stand.md: Katalog-Commit, Datum aus `date`, je Datei Zahl der
   Zeilen, Zahl je hoehe, offene Punkte, Befunde zu bank.md und
   zum Prüfskript (was für Grafikaufgaben fehlt). Commit
   „quadratische-funktionen: stand".

## Gegenprobe

katalog/quadratische-funktionen.md führt vier Einheiten und vier
Sprossenketten (eine je Einheit); Einheit 4 beginnt mit
„Nullstellen aus der Scheitelpunktform durch Wurzelziehen,
ganzzahlig (4×)" – in e4.jsonl stehen dafür fünf Zeilen mit
hoehe grundfall. Die Kastenzahlen des Eintrags (Merkkasten
Einheit 1–4, etwa (x − 3)² + 1 und (x + 3)² − 1) kommen in keiner
aufgabe vor; grep über die jsonl: 0 Treffer. Jede Zeile mit form
zeichnen oder einer Ablesegrafik hat ein nichtleeres Feld grafik.

## Regeln

- Zeilen in jsonl beliebig lang; in md höchstens 72 Zeichen.
- Nichts aus den Blättern unter blaetter/ kopieren; sie sind
  Vergleich, nicht Quelle.
- Kein LaTeX kompilieren (nicht verfügbar); die Bausteinaufrufe
  gegen die Anleitung prüfen (Name und Argumentzahl); bei
  Grafiken zusätzlich rechnerisch, dass jeder gefragte Punkt im
  Achsenbereich liegt.
- Was der Auftrag nicht regelt, entscheidest du und schreibst es
  in stand.md unter „Entscheidungen".

## Bericht

Im Chat, am Ende. Erste Zeile das Modell. Je Einheit: Zeilen,
davon grundfall/sprosse/pruefung/pflicht, Abweichungen des
Prüfskripts vor der Korrektur, was zweimal scheiterte. Die
Gegenprobe im Wortlaut mit Ist-Wert. Drei Beispielzeilen (je eine
aus Grundfall, Prüfungshöhe, Fehler finden) wortgleich. Letzte
Zeile: „gepusht auf main, Commit <hash>".
