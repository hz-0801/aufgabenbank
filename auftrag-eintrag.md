# Auftrag: Aufgabenbank – <eintrag>

Modell: Opus. Web-Sitzung, Repo aufgabenbank. Keine Rückfrage;
Commit je Einheit auf main, push nach jedem Commit (vorher
`git pull --rebase`), kein eigener Branch. Geschrieben wird nur
unter bank/<eintrag>/.

Vorlage: `<eintrag>` ist der Dateiname des Katalogeintrags ohne
`.md` (etwa lineare-funktionen); vor dem Einsatz überall ersetzen.
Stand der Vorlage: 2026-09-27, nach acht Einträgen.

## Ausgangslage

Die Bank (bank.md) hält je Sprosse des Themenkatalogs geprüfte
Aufgaben mit Lösung. Dieser Auftrag füllt sie für den Eintrag
<eintrag>. Form, Felder, Mengen, Reihenfolge und Regeln stehen in
bank.md; was dort steht, wird nicht neu entschieden.

## Quellen

Nur diese drei, aus dem Repo:
- mappen/<eintrag>.md – Katalogeintrag mit Zeilennummern (Feld
  quelle), Originale mit Spalten aus den Prüfungsdateien,
  Maßstab aus unterrichtsblatt.md (2.2, 2.3 c, 2.4 b–c, 3.6).
  Der Katalog-Commit im Kopf der Mappe ist der Stand für
  stand.md.
- mappen/_bausteine.md – Bausteine der Vorlage (Name,
  Argumentzahl, Beispiele).
- bank.md.

Katalog, Anleitung, Prompt, CSV und Vergleichsblätter liest die
Sitzung nicht selbst (bank.md, „Quellen je Sitzung"). Fehlt die
Mappe, bricht die Sitzung ab und sagt es im Bericht.

## Schritte

1. Mappe lesen, ganz. Aus „Für schwache Schüler" die
   Sprossenketten je Einheit, aus „Typen je Lerneinheit" die
   Typen ohne Kette, aus „Typische Fehler" die Muster, aus
   „Prüfungsform" und „Zielmarke" die Originale mit Kennung, aus
   „Voraussetzungen (Blatt 0)" die Fertigkeiten und
   Erkennungsschritte. Die Merkkästen nur für die Sperre lesen.
2. Zone: bank/<eintrag>/zone.jsonl nach bank.md (Mengen „Zone",
   Zone-Paar; s1 grundfall, ab s2 sprosse, Fallstrick im
   merkmal), in einem Schreibvorgang. Prüfskript, Commit
   „<eintrag>: zone", push.
3. Einheiten nacheinander, je Einheit: e<n>.jsonl mit allen
   Ketten in der Reihenfolge nach bank.md („Reihenfolge je
   Datei"), die ganze Datei in einem Schreibvorgang;
   `python3 werkzeuge/bank-pruef.py <eintrag>` bis null
   Abweichungen; Commit „<eintrag>: e<n>", push. Fehlerregel:
   Scheitert eine Einheit zweimal am Prüfskript, bleibt sie mit
   dem Stand liegen, stand.md sagt es, die nächste Einheit folgt.
   Dabei nach bank.md: Grundfall je Verfahrenskette; Prüfungshöhe
   ohne Original als hoehe pruefung, original null, 3 Zeilen;
   Original an einer Kettensprosse im Feld original; ein
   Erkennungsschritt, der die Vorstufe einer Kette derselben
   Einheit wiederholt, entfällt (Befund in stand.md).
4. stand.md: Katalog-Commit (aus dem Kopf der Mappe), Datum aus
   `date`, je Datei Zahl der Zeilen und Zahl je hoehe, Originale
   je Einheit, Abweichungen und Warnungen des Prüfskripts vor der
   Korrektur je Datei, „Entscheidungen", „Befunde" (bank.md,
   „Befunde"), „Offene Punkte". Commit „<eintrag>: stand", push.

## Gegenprobe

Für jede Verfahrenskette: die Zahl der Zeilen mit hoehe
grundfall ist 5 (bank.md, „Mengen je Kette"), der sprosse_text
des Grundfalls steht wortgleich in der Mappe in der Zeile quelle.
Jede Einheit hat genau eine Sprosse mit hoehe pruefung, als
letzte ihrer Verfahrenskette. Mehrstellige Kastenzahlen des
Eintrags (Merkkasten aller Einheiten) kommen in keiner aufgabe
vor; die Sperrprobe des Prüfskripts meldet 0. Jede Zeile mit form
zeichnen oder einem Ablese- oder Zeichenauftrag hat ein
nichtleeres grafik. Jede Ankreuzzeile nennt in loesung genau eine
Option wortgleich.

## Regeln

- Zeilen in jsonl beliebig lang; in md höchstens 72 Zeichen.
- Kein LaTeX kompilieren (nicht verfügbar); Bausteine nur aus
  mappen/_bausteine.md, das Prüfskript prüft Name und
  Argumentzahl.
- Was der Auftrag und bank.md nicht regeln, entscheidest du und
  schreibst es in stand.md unter „Entscheidungen".
- Was du an Katalog, bank.md oder Prüfskript für falsch hältst,
  steht in stand.md unter „Befunde"; du änderst es nicht.

## Bericht

Im Chat, am Ende. Erste Zeile das Modell. Je Einheit: Zeilen,
davon grundfall/sprosse/pruefung/pflicht, Abweichungen und
Warnungen des Prüfskripts vor der Korrektur, was zweimal
scheiterte. Die Gegenprobe im Wortlaut mit Ist-Wert. Drei
Beispielzeilen (je eine aus Grundfall, Prüfungshöhe, Fehler
finden) wortgleich. Letzte Zeile: „gepusht auf main, Commit
<hash>".
