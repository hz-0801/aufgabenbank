# originalneu.py – Prüfstein „Original neu“ (v0.1, 2026-10-11)

Setzt ein P10-Heft neu (pruefung.md § 4 „Original neu“): Aufgaben in
Heftreihenfolge mit gleicher Nummerierung, Punkte am Rand, Abbildungen
als kursive Beschreibung (Aufgabe 1: Figuren aus basis-originale.jsonl),
durchsuchbar; am Ende Lösungsblatt und Register nach Themen des Katalogs
(Hauptthema fett, Nebenthema grau, jede Teilaufgabe mit Sprungmarke und
Seite). Nur für den Lehrer – Wortlaut und Ausgabe bleiben im privaten Repo.

    python3 werkzeuge/originalneu.py --heft 2026-for

Quellen (neben dem Repo oder per Option/Umgebungsvariable):

- `aufgabenbank-privat/basis-originale.jsonl` (Aufgabe 1) und
  `hauptteil-originale.jsonl` (Aufgaben 2 ff.; Felder wie basis, dazu
  `nummer`, `titel`, `gesamtpunkte`, `stamm` = Text vor der Teilaufgabe,
  `grafik` = Beschreibung, `loesung_herkunft`) – `--privat`, `$PRIVAT`
- `mathe-nachhilfe/msa/msa-katalog-{basis,kontext}.csv` (Felder `thema`,
  `neben`, `typ`) – `--katalog`, `$KATALOG`
- `blattbau/mathblatt.sty` – `--vorlage`, `$BLATTBAU`

Ausgabe: `aufgabenbank-privat/originalneu/<heft>/src/<heft>-original-neu.tex`
(mit Kopie der Vorlage) und `pdf/<heft>-original-neu.pdf`; xelatex läuft
dreimal (lastpage, Sprungmarken). `--kein-pdf` schreibt nur den Quelltext.
Fehlt eine Katalogzeile, steht die Kennung unter dem Register.

Grenzen v0.1: ein Heft je Lauf (kein Inhaltsverzeichnis über mehrere
Jahre); Abbildungen des Hauptteils werden nicht nachgebaut; Lösungen sind
Katalogergebnisse (eigene Rechnung), keine amtlichen.
