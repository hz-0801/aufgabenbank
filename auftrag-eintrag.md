# Auftrag: Aufgabenbank – <eintrag>

Modell: Opus. Läuft als Unteragent aus dem Chat oder als
Web-Sitzung, Repo aufgabenbank. Keine Rückfrage; Commit je Einheit
auf main, push nach jedem Commit (vorher `git pull --rebase`), kein
eigener Branch. Geschrieben wird nur unter bank/<eintrag>/.

Vorlage: `<eintrag>` ist der Dateiname des Katalogeintrags ohne
`.md` (etwa lineare-funktionen); vor dem Einsatz überall ersetzen.
Stand der Vorlage: 2026-09-29b, nach bank.md fünfte Fassung und
dem Prüfstein terme (Prüfungshöhe je Verfahrenskette, Schrittnamen
mit Beispiel, pruef bei P1). Vorherige Fassung 2026-09-27b in
archiv/.

## Ausgangslage

Die Bank (bank.md) hält je Sprosse des Themenkatalogs geprüfte
Aufgaben mit Lösung. Dieser Auftrag füllt sie für den Eintrag
<eintrag> oder zieht einen vorhandenen Ordner auf den Stand von
Katalog und bank.md nach. Form, Felder, Mengen, Reihenfolge und
Regeln stehen in bank.md; was dort steht, wird nicht neu
entschieden.

## Quellen

Nur diese drei, aus dem Repo, jede genau einmal gelesen:
- mappen/<eintrag>.md – Katalogeintrag mit Zeilennummern (Feld
  quelle), Originale mit Spalten aus den Prüfungsdateien,
  Maßstab aus unterrichtsblatt.md (2.2, 2.3 c, 2.4 b–c, 3.6).
  Lange Quellenzeilen sind gekürzt; sie tragen zum Schreiben
  nichts bei. Der Katalog-Commit im Kopf der Mappe ist der Stand
  für stand.md.
- mappen/_bausteine.md – Bausteine der Vorlage (Name,
  Argumentzahl, Beispiele).
- bank.md.

Dazu, wenn der Ordner bank/<eintrag>/ schon besteht: seine
jsonl-Dateien und stand.md (Bestand). Katalog, Anleitung, Prompt,
CSV und Vergleichsblätter liest die Sitzung nicht selbst (bank.md,
„Quellen je Sitzung"). Fehlt die Mappe, bricht die Sitzung ab und
sagt es im Bericht.

## Schritte

1. Mappe lesen, ganz. Aus „Für schwache Schüler" die
   Sprossenketten je Einheit, aus „Typen je Lerneinheit" die
   Typen ohne Kette, aus „Typische Fehler" die Muster, aus
   „Prüfungsform" und „Zielmarke" die Originale mit Kennung, aus
   „Voraussetzungen (Blatt 0)" die Fertigkeiten und
   Erkennungsschritte. Die Merkkästen nur für die Sperre lesen.
   Vorstufen zählen: Die Vorstufe direkt vor dem Grundfall ist
   Sprosse 0, jede weitere davor −1, −2 (id s-1, s-2); der
   Grundfall ist immer Sprosse 1 (bank.md, Feld sprosse).
2. Zone: bank/<eintrag>/zone.jsonl nach bank.md (Mengen „Zone",
   Zone-Paar; s1 grundfall, ab s2 sprosse, Fallstrick im
   merkmal), in einem Schreibvorgang. Prüfskript, Commit
   „<eintrag>: zone", push. Besteht die Zone schon und die
   Fertigkeiten der Mappe sind unverändert, bleibt sie.
3. Einheiten nacheinander, je Einheit: e<n>.jsonl mit allen
   Ketten in der Reihenfolge nach bank.md („Reihenfolge je
   Datei"), der erste Wurf als ganze Datei in einem
   Schreibvorgang; `python3 werkzeuge/bank-pruef.py <eintrag>`
   bis null Abweichungen; Commit „<eintrag>: e<n>", push.
   Korrekturen ändern nur die gemeldete Zeile (Edit), nie die
   ganze Datei; die Datei wird nach dem Schreiben nicht
   zurückgelesen – das Skript sagt, was falsch ist. Fehlerregel:
   Scheitert eine Einheit zweimal am Prüfskript, bleibt sie mit
   dem Stand liegen, stand.md sagt es, die nächste Einheit folgt.
   Jede Lösung, die neu entsteht oder umgeschrieben wird, trägt in
   jeder Rechenzeile vorn den Schrittnamen in Schülerworten, mit
   Doppelpunkt (regeln.md 12; dieselben Wörter wie in den
   Anweisungen der Kette). Beispiel für loesung: „Klammer
   auflösen: 3x + 6 − 2x; ordnen: 3x − 2x + 6; zusammenfassen:
   x + 6; Ergebnis: x + 6“. Eine Lösung, die nur das Ergebnis
   nennt (Ablesen, Ankreuzen, einschrittige Rechnung), braucht
   keinen Schrittnamen. Der übernommene Bestand bleibt ohne.
   Dabei nach bank.md: Grundfall je Verfahrenskette als Päckchen
   (fünf Zeilen, ein Wert bleibt, genau einer wandert; Sek II:
   derselbe Körper mit festen Eckpunkten je Variante);
   Prüfungshöhe ohne Original als hoehe pruefung, original null,
   3 Zeilen; Original an einer Kettensprosse im Feld original;
   ein Erkennungsschritt, der die Vorstufe einer Kette derselben
   Einheit wiederholt, entfällt (Befund in stand.md).
   Pflichtformen je Einheit nach bank.md P1–P8: die drei
   fehler-Zeilen in drei Formen (Schülerrechnung mit Fehler;
   fehlerfreie Vorlage P2; Serie „Welche Ergebnisse können nicht
   stimmen?" P1 oder Prüfzahl P3 bei Gleichungen), die drei
   begruenden-Zeilen in drei Formen („Begründe, warum …";
   Aussagenserie P4; Personenaussage P6), darstellung mit zwei
   Richtungen (P7), anwendung mit einer Entscheidung am
   Grenzwert (P8); Urteilsfragen etwa halb Ja, halb Nein, das
   Urteil als erstes Wort der Lösung.
   Sek II: dazu die Bedingung als Zeilenkopf („Bedingung f''(x) =
   0:“, „Nebenbedingung:“). Verlangt die Sprosse Probe, Kontrolle
   oder Überschlag, steht sie als eigene beschriftete Zeile.
   Serie P1 und Aussagenserie P4 tragen pruef "" (bank.md); das
   Prüfskript (v0.8) lässt das bei hoehe pflicht zu.
   Antwortgerüste ins Feld antwort, nicht als \leerfeld in
   aufgabe – auch Lückenterme („P = 1 − (__)^__") und
   Gerüste wie „m = __" oder „Vorzeichen: __ Betrag: __
   Ergebnis: __" (rationale-zahlen nur in den ersten zwei
   Varianten der genannten Sprossen, bank.md).
   Besteht die Einheit schon: Zeilen, deren sprosse_text in der
   Mappe unverändert steht, bleiben wortgleich, nur id, sprosse,
   kette_nr und quelle werden nachgezogen; neue Sprossen werden
   geschrieben, Zeilen zu gestrichenen Sprossen entfallen; die
   Pflichtformen werden hergestellt, indem vorhandene fehler- und
   begruenden-Zeilen umgeschrieben werden, nicht ergänzt (die
   Menge bleibt drei).
4. Musterbeispiel: bank/<eintrag>/muster.md, je Verfahrenskette
   ein Abschnitt „## e<n> k<k> <kette>": die Aufgabe des
   Grundfalls mit eigenen Zahlen (nicht aus den fünf
   Päckchenzeilen), darunter die Rechnung als Tabelle mit den
   Spalten Schritt | Zeile, eine Zeile je Umformung, das
   Ergebnis als letzte Zeile mit Schritt „Ergebnis". Keine
   Bausteine, reine Daten; die Form auf dem Blatt setzt der
   Zusammenbau (layout-befunde 55). Liefert der Lehrer ein
   Beispiel (Mappe, Abschnitt „Musterbeispiel"), gilt seins.
   Commit „<eintrag>: muster", push.
5. stand.md, kurz: Katalog-Commit (aus dem Kopf der Mappe), Datum
   aus `date`, eine Tabelle Zeilen je Datei und hoehe, Originale
   je Einheit als Kennungen, Abweichungen und Warnungen des
   Prüfskripts vor der Korrektur als Zahl je Datei mit dem
   häufigsten Grund; bei einem Nachzug dazu je Einheit die Zahl
   der übernommenen, neuen, umgeschriebenen und entfallenen
   Zeilen. „Entscheidungen": nur, was von Katalog oder bank.md
   abweicht oder was beide offenlassen, je ein Satz, höchstens
   zehn. „Befunde" (bank.md, „Befunde") und „Offene Punkte" je
   ein Satz. Commit „<eintrag>: stand", push.

## Gegenprobe

Für jede Verfahrenskette: die Zahl der Zeilen mit hoehe
grundfall ist 5 (bank.md, „Mengen je Kette"), in allen fünf steht
derselbe feste Wert, der sprosse_text des Grundfalls steht
wortgleich in der Mappe in der Zeile quelle. Jede Vorstufe hat 4
Zeilen; bei mehreren Vorstufen einer Kette sind die Sprossen 0,
−1, −2 lückenlos und der Grundfall ist 1. Jede Verfahrenskette hat
genau eine Sprosse mit hoehe pruefung, als letzte; eine Einheit
mit zwei Verfahrensketten hat also zwei. Je Einheit tragen die
drei fehler-Zeilen drei verschiedene Formen und die drei
begruenden-Zeilen drei verschiedene Formen (P1–P6). Mehrstellige
Kastenzahlen des Eintrags (Merkkasten aller Einheiten) kommen in keiner aufgabe
vor; die Sperrprobe des Prüfskripts meldet 0. Jede Zeile mit form
zeichnen oder einem Ablese- oder Zeichenauftrag hat ein
nichtleeres grafik. Jede Ankreuzzeile nennt in loesung genau eine
Option wortgleich. muster.md hat je Verfahrenskette einen
Abschnitt.

## Regeln

- Zeilen in jsonl beliebig lang; in md höchstens 72 Zeichen
  (Tabellenzeilen in muster.md ausgenommen).
- Kein LaTeX kompilieren (nicht verfügbar); Bausteine nur aus
  mappen/_bausteine.md, das Prüfskript prüft Name und
  Argumentzahl.
- Shell ist Linux: Datum aus `date`, kein PowerShell.
- Was der Auftrag und bank.md nicht regeln, entscheidest du und
  schreibst es in stand.md unter „Entscheidungen".
- Was du an Katalog, bank.md oder Prüfskript für falsch hältst,
  steht in stand.md unter „Befunde"; du änderst es nicht.

## Bericht

Im Chat, am Ende, kurz. Erste Zeile das Modell. Je Einheit eine
Zeile: Zeilen, davon vorstufe/grundfall/sprosse/pruefung/pflicht,
Abweichungen vor der Korrektur, was zweimal scheiterte; bei einem
Nachzug übernommen/neu/umgeschrieben/entfallen. Die Gegenprobe
als Ist-Werte. Letzte Zeile: „gepusht auf main, Commit <hash>".
