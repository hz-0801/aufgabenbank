# Übersicht je Eintrag – Vorschlag für bank.md

Stand 2026-09-27, nach dem Prüfstein an prozentrechnung, pythagoras und
ableitungsregeln (bank/<eintrag>/uebersicht.md). Vorschlag, nicht beschlossen;
bank.md und zusammenbau.py sind unverändert.

## Was der Prüfstein zeigt

| Eintrag | Kästen (je 3 Fassungen) | Tabellenzeilen | Abbildungen | Fehlerzeilen |
| --- | --- | --- | --- | --- |
| prozentrechnung | 5 | 7 | 1 (`\streifenwertreihe`) | 12 |
| pythagoras | 3 | 6 | 2 (`\dreieckrw`, `\kegel`) | 14 |
| ableitungsregeln | 3 | 5 | 1 (`\termbaum`) | 13 |

Alle tex-Blöcke bestehen die Strukturprüfung aus zusammenbau.py
(`pruefe_struktur`: Klammern, $, Bausteine und Argumentzahl aus
mappen/_bausteine.md, Umgebungen). Kompiliert ist nichts – im Container
gibt es kein TeX.

## Empfehlung: Datei je Eintrag, als jsonl

    bank/<eintrag>/uebersicht.jsonl    eine Zeile je Baustein der Übersicht

Nicht als Markdown wie im Prüfstein. Der Grund ist die Auswahl:
`--einheiten 1,3` oder `--fokus` bauen ein Blatt aus einem Teil der
Einheiten. Eine Übersichtstabelle als ein fertiger `\sachtabelle`-Block
lässt sich nicht kürzen; einzelne Zeilen mit `einheit` schon. Zweiter
Grund: Die Fehlerzeilen und Beispiele tragen Ergebnisse
($1{,}25 : 7{,}8 \approx 16{,}0\,\%$, $h = 21$ cm). In jsonl kann
bank-pruef.py sie über `pruef` nachrechnen wie jede Aufgabe; im Markdown
prüft sie niemand.

Felder je Zeile:

    id        "<eintrag>-u-<art>-e<n>-<k>"  (k laufend je Art und Einheit)
    eintrag   Katalogdatei ohne .md
    art       "kasten" | "zeile" | "abbildung" | "fehler"
    einheit   Nummer; bei abbildung eine Liste, wenn das Bild mehrere
              Einheiten trägt ([2, 3, 4] beim Prozentstreifen)
    kasten:   regel, beispiel, schritte – je ein fertiger
              \uebersichtskasten{...}
    zeile:    verfahren, wann, merkmal – je eine Zelle, ohne &
    abbildung: grafik (Bausteinaufruf), text (Satz darunter)
    fehler:   achtung, falsch, richtig – je eine Zelle, ohne &
    pruef     wie in bank.md: Zahl oder Liste der Ergebnisse in beispiel
              bzw. richtig; "" ohne Ziffer
    quelle    Katalogzeile (Merkkasten, Typische Fehler) oder Original-id

Die Zellen ohne `&` baut der Zusammenbau zur `\sachtabelle` zusammen –
so bleibt die Spaltenfolge an einer Stelle.

Regel für den Inhalt, als Zusatz unter „Regeln für den Inhalt“: Die
Übersicht nimmt ihre Zahlen aus Merkkasten, Typische Fehler und
Originalen der Mappe, nie aus einer Bankzeile – sonst steht auf der
Übersichtsseite die Lösung einer Aufgabe desselben Blatts. Die Sperre
gilt für die Übersicht deshalb umgekehrt: Bankzahlen sind dort gesperrt.

## Was der Zusammenbau daraus setzt

- **Kasten am Ende jeder Einheit.** Nach der letzten Hauptnummer der
  Einheit ein `\uebersichtskasten` aus der Zeile `art kasten` dieser
  Einheit. Fassung nach Blattart: Lernblatt `beispiel`, schwach
  `schritte`, `--kasten` (Kasten am Anfang) `regel`. Neuer Schalter
  `--fassung regel|beispiel|schritte` überschreibt das. Der bisherige
  Merkkasten aus der Mappe (`kasten()` in zusammenbau.py) bleibt als
  Rückfall, wenn uebersicht.jsonl fehlt.
- **Übersichtsseite am Ende des Lernblatts.** Eigene Datei
  `uebersicht.tex`, in lernblatt.tex und gesamt.tex nach der letzten
  Einheit und vor dem Begleitteil eingebunden: `\clearpage`, eine
  Kopfzeile, die Verfahrenstabelle aus allen `zeile` der gewählten
  Einheiten, darunter die Abbildungen, deren `einheit` eine gewählte
  Einheit enthält, zuletzt die Fehlertabelle aus allen `fehler` der
  gewählten Einheiten. Im Fokus nur die Einheit des Fokus. Die
  Kopfzeile braucht einen Rahmenbefehl – `\hilfeseite` setzt „Hilfe:
  Lösungsstrategie“ und passt nicht.
- **Strukturprüfung** wie bisher auf uebersicht.tex; neu eine Warnung,
  wenn eine Tabellenzeile über etwa 80 Zeichen sichtbaren Text kommt
  (siehe unten).

## Zu dicht

- **Einheiten mit mehreren Verfahren.** prozentrechnung Einheit 5 hat
  neuen Wert, Veränderung in Prozent, alten Wert, Brutto/Netto,
  Prozentpunkte und Steigung; pythagoras Einheit 2 Kathete und
  Umkehrung. „Regel in einem Satz“ wird dort ein Kettensatz, und fünf
  Schritte reichen nicht: Prozentpunkte und Steigung stehen nur noch in
  der Fehlertabelle, Brutto/Netto nur als „neuer Wert : Faktor“.
  Vorschlag: bis zu zwei Kästen je Einheit, wenn der Katalog in der
  Einheit ein zweites Verfahren nennt (Umkehrung, Veränderung in
  Prozent); Feld `k` trägt das schon.
- **Fehlertabelle.** 12 bis 14 Zeilen, dazu 5 bis 7 Zeilen
  Verfahrenstabelle und eine Abbildung – geschätzt gerade noch eine
  Seite, gerendert nicht geprüft. Vorschlag: höchstens acht Fehlerzeilen
  je Seite, Auswahl nach Zahl der P10-/Abitur-Belege in „Typische
  Fehler“; mit Filter nach Einheit fällt das meist von selbst.
- **Zellen ohne Umbruch.** `\sachtabelle` nimmt nur l, c, r: die Vorlage
  zerlegt die Spaltenangabe Zeichen für Zeichen, `p{4cm}` würde zu
  `|p|4cm|`. Jede Zelle bleibt einzeilig, die drei Spalten zusammen bei
  etwa 80 Zeichen (Textbreite 174 mm, 11 pt). Das zwingt zum
  Telegrammstil („Becher: Durchmesser“). Befund für blattbau: eine
  Spaltenart mit Umbruch oder ein Baustein für zweispaltige
  Gegenüberstellungen.

## Zu dünn

- **Regel ohne Beispiel.** Die Fassung `regel` allein ist dünner als der
  bisherige Merkkasten, der Regel, Beispiel und Formelsammlungshinweis
  zusammen trägt. Der Hinweis „Formelsammlung: …“ fehlt in allen drei
  Fassungen; er gehört als letzte Zeile in `regel` und `beispiel`.
- **„Wann“ und „Erkennungsmerkmal“** trennen sich bei pythagoras (plus
  oder minus) und ableitungsregeln (Aufbau des Terms) gut, bei
  prozentrechnung kaum – beides heißt dort „was ist gegeben“. Dort
  reichen zwei Spalten: Verfahren und Woran erkenne ich es.
- **Abbildungen.** Prozentstreifen und rechtwinkliges Dreieck tragen das
  Thema. Der Kegel trägt nur Einheit 3 und steht besser als Leitgrafik
  in deren Kasten (`\uebersichtskasten[<Grafik>]{...}`). Der Termbaum für
  ableitungsregeln ist eine Darstellung, die die Mappe für diesen
  Eintrag nicht nennt – er macht den Erkennungsschritt „Welche Regel?“
  sichtbar, ist aber streng genommen neu.
- **ableitungsregeln, Typische Fehler.** Zwei Punkte der Mappe gehören
  nach ihr selbst zu anderen Einträgen (Verhalten im Unendlichen,
  Anschluss an die Kurvenuntersuchung); aufgenommen ist davon nur der
  Anstieg über f(0). Die Mappe bündelt je Punkt mehrere Fehler; eine
  Zeile je Fehler braucht die Liste aus „Typen je Lerneinheit“ (Fehler
  finden) dazu.

## Offen für den ersten Render

- `&` im `\uebersichtskasten`: Die Vorlage warnt („kein &“), gemeint ist
  ein nacktes `&`. In den Kästen steht `&` nur in `\rechnung` (aligned),
  das sollte gehen – ungeprüft.
- `\begin{schritte}` im `\uebersichtskasten`: Liste in tcolorbox,
  ungeprüft.
- Anführungszeichen „ “ in `\text{…}` im Mathemodus (Einheit 1
  prozentrechnung).
