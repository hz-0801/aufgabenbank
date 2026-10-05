# pruefheft.py – Prüfungsheft aus Daten (v0.1, 05.10.2026)

Setzt ein Prüfungsheft (Skript) ohne Modell: Bestellung rein, .tex und PDF
(Heft + eigene Lösungsdatei) raus. Probelauf am P10-Kapitel Prozent.

## Aufruf (aus der Wurzel von aufgabenbank)

    python3 werkzeuge/pruefheft.py --kapitel prozent --art normal
    python3 werkzeuge/pruefheft.py --kapitel prozent --art schwach
    python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --portion 1
    python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --fokus grundwert

Pfade: `--mn ../mathe-nachhilfe --bb ../blattbau` (Vorgabe: Nachbarordner).
`--bank n` setzt die Bankaufgaben je Stufe (Vorgabe Kern 3, sonst 2; Fokus
bis zur Zielzahl der Zuordnung). Braucht xelatex, pdfinfo und mathblatt.sty
ab 2026-10-05b (Abschnitt P). Ausgabe:
`bau/pruefheft/<kapitel>-<art>[-p<n>|-fokus-<wort>]-<datum>/src|pdf/`.

## Was es setzt

- Übersicht vorn (Stufen in Lernreihenfolge, Stichwörter, Seite), außer
  Serie und Fokus.
- je Stufe „neu: …“, „kommt das dran?“ (Jahre, zuletzt, BE aus dem
  Katalog; „selten geprüft“ = in den letzten fünf Prüfungsjahren nie oder
  insgesamt höchstens einmal), Leitaufgabe groß mit Rechenplatz (nicht bei
  reinem Ankreuzen), „weitere dieser Art“ zweispaltig, je mit BE und
  Fundstelle bzw. „eigene Aufgabe (nach P10 …)“; Nebenplatz mit „kennst du
  aus …“.
- Kontrollwert (Kurzlösung) und Tipp (ein Stichwort, das nicht im
  Stufennamen steht) kopfüber am Fuß derselben Seite (\fusshilfe, zweiter
  Lauf).
- Prüfstein auf eigener Seite: jüngste Kontextaufgabe, deren Teilaufgaben
  alle eigenen Wortlaut haben; ihre Teilaufgaben fehlen dann im Stufenteil.
- schwach: alle Aufgaben mit Rechenraster (Zeile je Schritt), Ausblenden
  (erste Aufgabe mit Zwischenfragen bekommt alle, zweite die erste, dann
  keine), Lösung „Wort: Ansatz ⇒ Wert“.
- Serie: Rückblick (zwei Zone-Grundlagen, passend zu den Stichwörtern),
  dann so viele Stufen (Kern zuerst), wie auf eine Seite passen – gemessen
  durch Probeläufe von xelatex, Schnitt nur an Stufengrenzen.
- Lösungsdatei: eine Tabelle je Nummer, nie über Seitenwechsel; links fett
  das Ergebnis, rechts Zwischenergebnisse, BE an der Zeile. Bank-Lösungen
  werden zerlegt (Fehlerhinweise in Klammern, Antwortsätze und „Kontrolle“
  fallen weg).

## Abbildungen

Aus der Beschreibung im Feld `abbildung` nach Typ am Anfang: Säulendiagramm
(Wertepaare, „Achse beginnt bei“), Tabelle (Spalten a. bis b. Wort),
leerer Kreis, rechtwinkliges Dreieck, Ankreuztabelle; „keine“ und „wie im
Text“ setzen nichts. Unbekannte Typen meldet das Programm als Datenbefund.
