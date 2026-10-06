# pruefheft.py – Prüfungsheft aus Daten (v0.2, 06.10.2026)

Setzt ein Prüfungsheft (Skript) ohne Modell: Bestellung rein, .tex und PDF
(Heft + eigene Lösungsdatei) raus. Probelauf am P10-Kapitel Prozent. Regeln:
Arbeitsliste `bau/pruefheft/beschluesse-2026-10-06.md` (Punkte 1–29); die
Nummer steht im Programm am Kommentar.

## Aufruf (aus der Wurzel von aufgabenbank)

    python3 werkzeuge/pruefheft.py --kapitel prozent --art normal
    python3 werkzeuge/pruefheft.py --kapitel prozent --art schwach
    python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --portion 1
    python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --fokus grundwert
    … --kurs EBR        Heft ab 2026 nach Kurs (Vorgabe FOR, Beschluss 27)

Pfade: `--mn ../mathe-nachhilfe --bb ../blattbau` (Vorgabe: Nachbarordner).
`--seiten n` Startmaß einer Portion (Vorgabe 2). `--ohne-register` schreibt
keine Zeile in `bau/register.csv` (sonst eine Zeile je Bau, Kennung PRZ-PH<n>).
Braucht xelatex, pdfinfo, sympy und mathblatt.sty ab 2026-10-06. Ausgabe:
`bau/pruefheft/<kapitel>-<art>[-p<n>|-fokus-<wort>][-ebr]-<datum>/src|pdf/`.

## Was es setzt

- Vorn immer der Rückblick (18): ganzes Heft, Portion 1 und Fokus = Grundlagen
  aus der Zone (eine Aufgabe je Voraussetzung der Kern-Stufen, mindestens drei;
  schwach zwei je Voraussetzung); spätere Portionen = drei Aufgaben aus den
  Sprossen der vorigen Portion. Keine Übersicht (12).
- Je Stufe der Kopf „Grundwert G“ mit grauem „in k der letzten 5 Prüfungen“
  bzw. „selten geprüft“ (13), dann die Leiter (1): Vorstufen der Ketten und
  der passenden Erkennungsschritte (Zeilen „Vor Einheit …“ im Themenkatalog);
  normal zwei, schwach und Fokus alle (je zwei Varianten). Darüber Grundfall,
  die Sprossen der Zuordnung, oben die echten Aufgaben; Bank-Prüfungshöhe nur,
  wenn weniger als zwei echte da sind (21, 22).
- Gruppen (8): rechnen, Ankreuzen, Sachaufgabe, Vergleich; Gruppen nach ihrer
  leichtesten Aufgabe geordnet, in der Gruppe Prüfungshöhe zuletzt, sonst
  kopfrechenbar → glatt → krumm, wenig Text vor viel, eine Frage vor zwei (2).
  „kopfrechenbar“ (3): Sätze 1, 5, 10, 20, 25, 50, 75, 100, 200 %, übrige
  Zahlen ganz mit höchstens zwei geltenden Ziffern, Ergebnis ganz oder mit
  einer Nachkommastelle; „krumm“ bei ≈, „Runde“ oder Satz mit Komma. Unten
  zusätzlich nach dem Muster 10 → 50 → 25 → 1 → 20 % (6).
- Aufgabenbild-Wort am Gruppenanfang (10) aus dem Bankfeld `bild`; fehlt es,
  steht keins (das Programm meldet die Zahl der Zeilen ohne `bild`).
- Aufgabenzeile (14): grau „P10 ’26“ bzw. „eigene Aufgabe“ links, Nummer,
  Text, Punkte rechts (echte Aufgaben; Bankzeilen mit umfang ganz aus
  `bank/_punkte.csv`). * vor der Nummer bei FOR-only (26: Katalog stern ja oder
  FOR-Teil 2026 ohne EBR-Zwilling). Alles untereinander, Rechenplatz nach
  Schrittzahl, ohne bei Ankreuzen und Ein-Wort-Antwort (11). „ab hier:
  G = W : p“ einmal vor der ersten Aufgabe, die die Formel braucht (15).
- Seitenfuß auf jeder Seite (23), kopfüber: Kontrollwert, wo er kurz ist;
  Tipp nur als Ansatz mit Zahlen aus dem Katalogfeld zwischenergebnis.
- schwach (29): Rechenraster (Zeile je Schritt), Zwischenfragen mit Ausblenden
  nur an echten Mehrschritt-Aufgaben (5), Lösung „Wort: Ansatz ⇒ Wert“.
- Serie (19): eine Portion endet nach einem abgeschlossenen Block (Vorstufen
  oder Gruppe), auch mitten in der Stufe („Fortsetzung“ im Kopf); so viele
  Blöcke, wie in `--seiten` Seiten passen (Probeläufe mit xelatex).
- Fokus (7): beginnt ganz unten (alle Vorstufen der Kette, vier Grundfälle,
  jede Sprosse der Kette), dazu „nach Rabatt (80 %)“ aus Einheit 5 (6).
- Prüfstein (20): ganze echte Aufgabe der letzten fünf Jahre im eigenen
  Wortlaut, ohne Nummer, ohne Fuß; fehlt eine ganze, die jüngste mit
  mindestens zwei Teilen (Datenbefund).
- Lösungsdatei (24, 25): keine Punkte; grau über der Zeile die Fundstelle
  (Heft · Aufgabe, nur echte); Bank-Ergebnisse mit ≈ bekommen den exakten
  Wert aus `pruef` davor (Bruch, Nenner ≤ 1000).

## Abbildungen

Aus der Beschreibung im Feld `abbildung` nach Typ am Anfang: Säulendiagramm
(Wertepaare, „Achse beginnt bei“), Tabelle (Spalten a. bis b. Wort),
leerer Kreis, rechtwinkliges Dreieck, Ankreuztabelle; „keine“ und „wie im
Text“ setzen nichts. Unbekannte Typen meldet das Programm als Datenbefund.
