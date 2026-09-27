# Auftrag: Bank-Sitzungen sparsamer – Skript v0.4, Mappen, Vorlage

Modell: Opus. Web-Sitzung, Repo aufgabenbank, main. Commit je Teil,
vor jedem Push `git pull --rebase`, main pushen, kein eigener
Branch. Geschrieben wird nur in werkzeuge/bank-pruef.py,
werkzeuge/mappe.py, mappen/, auftrag-eintrag.md und in diesen
Auftrag (Verschieben am Ende). Kein Eintrag unter bank/ und nicht
bank.md wird geändert.

## Ausgangslage

Achtzehn Einträge liegen in bank/. Zehn davon haben heute 84 $
Cloud-Guthaben gekostet, etwa 8 $ je Eintrag; 98 $ sind übrig,
neun Einträge stehen an. Der Kostentreiber ist, was eine Sitzung
liest und in ihrem Verlauf behält. Drei Messungen aus dem Repo:
- Das Prüfskript druckt je Lauf eine Zeile „OK <id>“ für jede
  Zeile der Bank (pythagoras: 248 Zeilen je Lauf), bei jedem
  Lauf, und alles bleibt im Verlauf der Sitzung.
- Die Mappe pythagoras hat 68 170 Zeichen; 16 Zeilen mit mehr als
  600 Zeichen (Belege, Gegenlesen, Katalogbefunde) tragen davon
  32 307 – fast die Hälfte, und nichts davon braucht das Schreiben
  einer Aufgabe.
- Die Vorlage sagt „die ganze Datei in einem Schreibvorgang“; das
  gilt auch für Korrekturen, also schreibt eine Sitzung für drei
  falsche Zeilen 80 Zeilen neu.
Dazu ein Skriptfehler aus einheiten/stand.md: Das Feld original
nimmt nur Kennungen nach `\d{4}-[A-Z]+-[A-Z]\d+[a-z]` an;
FHR-Kennungen (2025-C-2b) und Abitur-Kennungen
(2025MerhoehtAAGLAA121-a) fallen durch, und die Mappen der
nächsten neun (trigonometrie, wahrscheinlichkeit, zinsrechnung …)
führen solche Originale.

## Teil 1: werkzeuge/bank-pruef.py v0.4

a) Ausgabe: Ohne Schalter druckt das Skript nur ABWEICHUNG- und
   WARNUNG-Zeilen, je Datei die Summenzeile und die Gesamtzeile;
   keine OK-Zeilen. Der Schalter `--alle` druckt wie bisher.
b) original: Kennungen aller drei Prüfungen gelten. Muster: MSA
   wie bisher; FHR `\d{4}-[A-C]-\d[a-z]`; Abitur
   `\d{4}M(erhoeht|grundlegend)[A-Z0-9]+(-[a-z])?`. Welche Werte
   papier bei FHR und Abitur trägt, liest du aus den Mappen
   (Abschnitt „2 Originale“, Klammer hinter der Kennung) und
   schreibst es in den Kopf des Skripts und in den Bericht.
c) Selbsttest: je Änderung ein Fall (eine Zeile, die vorher falsch
   lief; eine, die weiter richtig läuft).
Kopf: v0.4, Datum aus `date`, Änderungen a–b je eine Zeile.
Commit „bank-pruef v0.4: stille Ausgabe, FHR- und Abitur-
Kennungen“, push.

## Teil 2: werkzeuge/mappe.py und mappen/

Zeilen des Katalogteils (vor „## 2 Originale“) mit mehr als 600
Zeichen werden nach 200 Zeichen abgeschnitten und enden mit
„ … (gekürzt, <n> Zeichen)“; die Zeilennummer bleibt. Die
Abschnitte, die eine Sitzung zum Schreiben braucht (Merkkästen,
Für schwache Schüler, Typen je Lerneinheit, Typische Fehler,
Voraussetzungen, Zielmarke, Prüfungsform), haben keine Zeilen
über 600 Zeichen; prüfe das mit einer Zählung je Abschnitt über
alle 27 Mappen und lass eine Ausnahme im Bericht stehen, statt
sie stumm zu kürzen. Der Kopf der Mappe nennt die Kürzungsregel
in einer Zeile. Alle 27 Mappen neu bauen, Zeichen je Mappe
vorher und nachher in den Bericht. Commit „mappe.py: lange
Quellenzeilen gekürzt; 27 Mappen“, push.

## Teil 3: auftrag-eintrag.md

Die Datei 2 dieses Blocks ersetzt sie wortgleich. Commit
„auftrag-eintrag: sparsame Sitzung“, push.

## Gegenprobe

`python3 werkzeuge/bank-pruef.py <eintrag>` für alle 18 Einträge
mit v0.4: dieselben Zahlen (Abweichungen, Warnungen) wie mit
v0.3 vor Teil 1 – Tabelle vorher/nachher im Bericht; `--alle`
für einen Eintrag druckt wieder OK-Zeilen. Selbsttest
bestanden. Mappe pythagoras nach Teil 2 unter 40 000 Zeichen;
kein Sprossentext aus „Für schwache Schüler“ ist gekürzt (Probe:
die längste Zeile dieses Abschnitts in pythagoras und einheiten
vorher = nachher).

## Regeln

- Kein Eintrag unter bank/ und nicht bank.md wird geändert.
- Zeilen in md höchstens 72 Zeichen (Mappen ausgenommen).
- Was der Auftrag nicht regelt, entscheidest du und schreibst es
  in den Bericht.
- Am Ende diesen Auftrag nach archiv/auftrag-bank-sparen-
  2026-09-27.md verschieben (git mv), Commit „archiv: auftrag-
  bank-sparen“, push.

## Bericht

Im Chat, am Ende. Erste Zeile das Modell. Dann: papier-Werte
für FHR und Abitur mit Beleg (Mappe, Zeile); Tabelle der 18
Einträge vorher/nachher; Zeichen je Mappe vorher/nachher;
Ausnahmen der Kürzung; Entscheidungen, die der Auftrag offen-
ließ. Letzte Zeile: „gepusht auf main, Commit <hash>“.
