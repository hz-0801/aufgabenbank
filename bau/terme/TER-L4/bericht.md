# Lernblatt Terme TER-L4 – Bericht (zusammenbau v0.9)

Stand 2026-09-30. Auftrag: archiv/auftrag-lernblatt-v09-2026-09-30.md
(zweiter Durchgang v0.9; der erste baute TER-L3). Gebaut mit
`python3 werkzeuge/zusammenbau.py terme` (Skript fb02d3e), gemessen mit
`python3 bau/terme/lernblatt-messen.py bau/terme/TER-L4` (xelatex je
Dokument zweimal, pdftoppm -r 80). Vorlage mathblatt.sty 2026-09-28a
aus hz-0801/blattbau, unverändert. Modell: Claude Opus 5.5.

## Vorher und nachher

HN: Hauptnummern, TA: Teilaufgaben, S.: Seiten des Einzeldokuments
(<K>-e<n>.pdf; Zone <K>-blatt0.pdf). „v0.8“ ist die Probe des
Ist-Stands vor v0.9 (Commit 546d722, TER-L0), „v0.9/1“ der erste
Durchgang (Probe mit dem Stand von TER-L3), „v0.9/2“ ist TER-L4.

| Teil | v0.8 HN/TA/S. | v0.9/1 HN/TA/S. | v0.9/2 HN/TA/S. |
| --- | --- | --- | --- |
| Zone | 6 / 10 / 1 | 5 / 18 / 1 | 5 / 18 / 1 |
| e1 Terme aufstellen und berechnen | 4 / 13 / 2 | 9 / 29 / 4 | 9 / 28 / 4 |
| e2 Terme zusammenfassen | 6 / 25 / 2 | 12 / 48 / 4 | 12 / 48 / 4 |
| e3 Klammern auflösen | 3 / 13 / 2 | 8 / 27 / 4 | 8 / 26 / 4 |
| e4 Ausklammern | 3 / 17 / 1 | 9 / 37 / 4 | 9 / 37 / 4 |
| Prüfe dich | – | – | 5 / 5 / (im Gesamt S. 18) |
| Gesamt | 22 / 78 / 9 | 43 / 159 / 18 | 48 / 162 / 18 |
| Lösungen (Seiten) | 2 | 3 | 4 |

Weniger TA in e1 und e3 gegenüber v0.9/1: Der Grundfall steht so oft,
wie der Katalog sagt – „passenden Term ankreuzen (3×)“ und
„Plusklammer weglassen (3×)“ –, nicht mehr pauschal viermal.

Altes Blatt (mathe-nachhilfe, blaetter/testlauf-2026-09-26/
10-ka-terme-8-gym, TermeBinomischeFormeln_Gesamt.pdf, 22 Seiten, fünf
Einheiten). Seine Terme-Einheiten laut Zweigzeile und Kommentarzeile
der e<n>_a.tex: alte Einheit 1 „Klammern auflösen“ (terme.md
Einheit 3) und alte Einheit 2 „Ausklammern“ (terme.md Einheit 4); die
alten Einheiten 3 „Summe mal Summe“ und 4 „Binomische Formeln“ gehören
zu binomische-formeln.md. Termwert und Zusammenfassen standen dort in
der Zone.

| Einheit | alt HN/TA/S. | TER-L4 HN/TA/S. | HN ≥ alt |
| --- | --- | --- | --- |
| Klammern auflösen (alt 1, Bank e3) | 7 / 31 / 4 | 8 / 26 / 4 | ja |
| Ausklammern (alt 2, Bank e4) | 4 / 20 / 2 | 9 / 37 / 4 | ja |
| Zone | 9 / 47 / 2 | 5 / 18 / 1 | – |

Wörtlich „Einheiten 1–4 des alten Blatts“ gegen Bank e1–e4 gelesen:
9 ≥ 7, 12 ≥ 4, 8 ≥ 8, 9 < 11 (alt 4 = Binomische Formeln, anderes
Thema). TA zählen im alten Blatt `\teil`, `\tz`, `\gl`, eine Nummer ohne
Teile als eine.

## Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| Kompilierfehler (4 Dokumente + 4 Einheiten) | 0 |
| „Missing character“ | 0 (Overfull 0) |
| PDFs enthalten Text (pdftotext) | ja (Gesamt 19 057 Zeichen) |
| BANKWORT (log, PDF-Text) | 0 Treffer |
| „TODO“ im PDF-Text | 0 |
| AUFTRAG: Auftragssatz in mehr als einer Teilaufgabe | 0 Hauptnummern |
| Hinweis AUFTRAG-SATZ (gleicher Satz, kein gemeinsamer Auftrag) | 3 Sätze in Nr. 34, 35 (unten) |
| HN je Terme-Einheit ≥ altes Blatt | ja (8 ≥ 7, 9 ≥ 4) |
| Grundfall „Zusammenfassen“ (e2) | 4 TA |
| Vorstufen davor (Erkennungsschritte e2) | 4, 4, 4 TA (Nr. 15–17) |
| „Termwert berechnen“ | 3 TA (Nr. 9) |
| Originale Prüfungshöhe e1 | 2 im Blatt = 2 Originale der jüngsten fünf Jahrgänge in bank/terme/e1.jsonl (2023-OS-B1h, 2017-OS-B1i) |
| kennung-probe.py TER-L4 | 0 Fehler (Register, bau.json, TA je Nummer, Kennung in Fuß und Namen, 8 Dokumente) |
| zwei gleiche Aufrufe | Aufgaben- und Lösungsdateien wortgleich, Aufgabenliste gleich |
| Regressionsprobe prozentrechnung, quadratische-gleichungen | Struktur 0 Fehler, Gesamt kompiliert ohne Fehler, 0 fehlende Zeichen, kein Bank-Wort |
| Rezept K (PRZ, Prozentsatz, Einheit 2) | Quelltext byte-gleich, kompiliert (3 Seiten) |
| Rezepte H, Z, P | Quelltexte byte-gleich |

## Was auf dem Blatt anders ist

- Kopf „Terme · Lernblatt · <Einheit>“, Fuß „TER-L4“ und Seite.
- Blatt 0 „Das kennst du schon“: vier Fertigkeiten mit Ich-kann-Titel,
  das Fehler-Paar am Ende, unter jeder Nummer „Hängst du hier → Nr. n“;
  in der Lösung „falsch → Lücke: …“ bei den Fallstrick-Aufgaben.
- Zweigzeile „Hier lernst du, Terme zusammenzufassen – gleichartige
  Glieder, Malnehmen von Termen · ab Kl. 7 … · P10 ×1 · baut auf: …“.
- Letzte Seite: „Prüfe dich“ (Nr. 44–48, je Verfahrenskette eine
  Aufgabe, gemischt, Auftrag in der Zeile der Nummer; Lösung „falsch →
  Nr. n“) und darunter „Das kann ich“ je Kette.
- Kurzer Term allein steht wie im Paar mit „= ____“ in einer Zeile.

## Befunde an Bank, Mappe, Katalog (nicht geändert)

1. bank/terme/e4 k1 („Was steckt in jedem Glied?“): Die vier Zeilen
   sind verschieden formuliert („Kreise den Faktor ein, der in beiden
   Gliedern steckt“ / „Kreise ein, was in beiden Gliedern steckt: Zahl,
   Variable oder beides“ / „… in allen drei Gliedern“). Folge in Nr. 35:
   „Was steckt in jedem Glied von …?“ und „Klammere nichts aus.“ stehen
   dreimal. Eine Formulierung für alle vier behebt es.
2. bank/terme/e4 k2 Vorstufen −1 und 0: Der Faktor steht als Zahl im
   Text („als Produkt mit dem Faktor 4“, „Klammere den Faktor 3 aus:“).
   Ein gemeinsamer Auftrag geht so nicht; Nr. 36 und 37 tragen den Satz
   in jeder Teilaufgabe (als ganze Aufgabe paarweise).
3. bank/terme/e3 k3 anwendung: „Löse die Klammer auf.“ steht in a) und
   c) (Nr. 34) – Sachaufgaben, vertretbar.
4. Mappe terme, Voraussetzungen: „Multiplizieren mit Vorzeichen“ („für
   Malnehmen und Minusklammer“) und „Dezimalzahlen und einfache Brüche“
   („nur, wenn die Einheit sie braucht“) nennen keine Einheit. Nach der
   Regel des Auftrags zeigt ihr Verweis auf Nr. 6 (Einheit 1), obwohl
   Malnehmen in Einheit 2 (Nr. 21) und die Minusklammer in Einheit 3
   steht. Der Katalog sollte „Einheit 2 und 3“ nennen.
5. Mappe terme, Lerneinheit 4: Die Beschreibung trägt einen
   Lehrerhinweis in Klammern („Kl. 7/8; … → binomische-formeln.md
   Einheit 1“); das Skript lässt ihn weg.
6. Katalog: Grundfall „(3×)“ bei Klammern und Term aufstellen, Bank je
   fünf Zeilen – zwei bleiben Reserve (log RESERVE).
7. Teilaufgaben „Klammern auflösen“ 26 gegen 31 im alten Blatt: Das
   alte Blatt hatte zehn Grundfall-Aufgaben in einer Nummer; die Bank
   gibt je Sprosse eine. Keine Zeile erfunden.

## Annahmen und Abweichungen

1. Der Auftrag lag in einer ersten Fassung schon ausgeführt vor (Commit
   032aeef, TER-L3). Dieser Lauf setzt auf dessen Skript auf und baut
   die neuen Punkte (Grundfall nach Katalog, Prüfungshöhe nach der Regel
   des Kompetenzblatts, Auftrag einmal auch in K, Prüfung AUFTRAG,
   Zweigzeile mit Beschreibung, Verweis als Zeile, Zone-Paar am Ende,
   Fallstrick-Lücke, Prüfe dich, Das kann ich, Kopf „Lernblatt“, lage in
   fünf Werten). Vorher-Werte: v0.8 und v0.9/1.
2. „Einheit n von m · <Titel>“ bleibt im Einheitenkopf, die Zweigzeile
   beginnt mit „Hier lernst du“ – wie im alten Blatt.
3. Blatt 0 behält die Menge nach bank.md (zwei sehr leichte, eine
   mittlere, je Fallstrick eine) statt „Sprosse 1 und 2“: ohne die
   Fallstrick-Zeilen gäbe es keine „Lücke“ in der Lösung.
4. „Hängst du hier → Nr. n“ wörtlich ohne Fragezeichen.
5. „Das kann ich“ je Kette: Pflichtelemente tragen den Namen der ersten
   Verfahrenskette und zählen zu ihr („6–8, 11–14“).
6. Mittlere Sprosse bei gerader Zahl: die obere Mitte. Prüfe dich
   gemischt nach der Prüfsumme der id (fest bei gleicher Bestellung).
7. Lösung von Prüfe dich mit „(falsch → Nr. n)“ auf die Leiter der
   Sprosse (nicht verlangt, analog zur Zone).
8. Teilung erst nach Maß, dann am wiederholten Auftrag; zählt jetzt
   auch den Auftrag einer einzelnen Teilaufgabe.
9. Zweigzeile, Verweis, Fallstrick-Lösung und kurzer Term gelten auch
   in Fokus und schwach (gemeinsamer Code; beide bauen, Probe
   kompiliert); Kopf, Prüfe dich, Das kann ich nur im Lernblatt.
10. Messwerte schreibt das neue bau/terme/lernblatt-messen.py in
    bau.json (zusammenbau.py kompiliert nicht).
11. Commit-Zeile „Co-Authored-By“ mit dem Modell, das lief (Opus 5.5),
    nicht wie im Auftrag Fable 5.1.

## Offen

- Gemeinsamer Auftrag bei Zahlen im Aufgabentext (Befund 2) und bei
  verschieden formulierten Varianten (Befund 1): Bank oder Skript.
- Hinweis AUFTRAG-SATZ in anderen Einträgen häufig (prozentrechnung 12,
  quadratische-gleichungen 13 Sätze, meist Ankreuz- und Kontextaufgaben)
  – dort wiederholt sich der Auftrag noch.
- Seite 13 des Gesamt trägt nur eine Teilaufgabe (Nr. 34 c), weil jede
  Einheit auf neuer Seite beginnt.
- Blatt 0 mit Verweis auf Nr. 6 für Fertigkeiten ohne Einheitenangabe
  (Befund 4).
