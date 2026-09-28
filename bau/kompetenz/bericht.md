# Kompetenzblätter – Prüfstein (Rezept K, zusammenbau v0.7)

Stand 2026-09-28. Gebaut mit `python3 bau/kompetenz/bauen.py` (Probe ohne
Register, dann Bau mit Registerzeile, xelatex je Dokument zweimal,
pdftoppm -r 80). Niveau FOR. Vorlage mathblatt.sty 2026-09-28a aus
hz-0801/blattbau, unverändert; alle Ergänzungen im Vorspann
(vorspann.tex, vom Zusammenbau geschrieben). Anleitung:
werkzeuge/zusammenbau.md, Abschnitt „Rezept Kompetenzblatt (v0.7)“.

## Die fünf Blätter

Seiten: Blatt + Lösungen (pdfinfo). HN: Hauptnummern. Teilaufgaben: Zone +
Leiter + Prüfungshöhe. Fehlende Zeichen: „Missing character“ in beiden
.log (Ziel 0). Ersatz: Zeichen, die der Vorspann aus der Ersatzschrift
(FreeSerif) bzw. als Mathe setzt; pdftotext findet jedes im PDF.

| Kennung | Eintrag / Kette | Seiten | HN | Teilaufgaben | Prüfungshöhe (Originale) | fehlende Zeichen | Ersatz | Overfull |
| --- | --- | --: | --: | --- | --- | --: | --- | --: |
| QGL-K1 | quadratische-gleichungen / p-q-Formel | 4 + 1 | 17 | 20 (3 + 13 + 4) | 2025-OS-K5c, 2024-OS-K3d, 2023-OS-K4c, 2022-OS-K3c | 0 | ₁ ₂ ≈ (im PDF: ja) | 0 |
| POT-K1 | potenz-exponentialfunktionen / Wachstumstabelle fortschreiben | 3 + 1 | 12 | 16 (3 + 8 + 5) | 2026-FOR-K7a, 2020-OS-K4a, 2019-OS-K7a, 2017-OS-K7a, 2016-OS-K4a | 0 | – | 0 |
| LIN-K1 | lineare-funktionen / Graph zeichnen | 4 + 1 | 11 | 14 (3 + 7 + 4) | 2026-FOR-K5a, 2024-OS-K3a, 2022-OS-K3a, 2021-OS-K2a | 0 | – | 0 |
| PRZ-K1 | prozentrechnung / Prozentsatz | 3 + 1 | 11 | 15 (3 + 7 + 5) | 2025-OS-K6b, 2023-OS-K6a, 2018-OS-K7a, 2015-OS-K7c, 2014-OS-B1e | 0 | – | 0 |
| TRI-K1 | trigonometrie / Sinussatz | 4 + 1 | 20 | 24 (3 + 16 + 5) | 2025-OS-K4c, 2024-OS-K6d, 2021-OS-K3c, 2020-OS-K7c, 2019-OS-K3c | 0 | α β γ ≈ (im PDF: ja) | 0 |

Alle fünf in 3–4 Seiten, Lösungen je eine Seite. TRI-K1 hatte in der Probe
fünf Seiten (16 Sprossen) und ist mit `--dicht` gebaut: kurze
Rechenaufgaben ohne Grafik stehen paarweise nebeneinander (Nr. 5–18).
Kein Kompilierfehler, keine Teilaufgabe weggelassen, kein Bank-Wort im
Blatttext (Prüfung BANKWORT im Skript, alle fünf log ohne Treffer).
Zum Vergleich: Die Prüfungs-Fokus v0.6 hatten 137 fehlende Zeichen, davon
QGL-P1 8 und TRI-P1 18.

Je Ordner: <K>.tex, <K>-loesungen.tex, vorspann.tex, mathblatt.sty,
<K>.pdf, <K>-loesungen.pdf, <K>-<n>.png, <K>-loesungen-1.png, bau.json,
zusammenbau.log. Übersicht maschinenlesbar: ergebnis.json.

## Layout-Befunde (bau/layout-befunde.md) – was umgesetzt ist

| Nr. | Befund | Kompetenzblatt |
| --- | --- | --- |
| 1 | Kopfzeile ohne Doppelung | umgesetzt: „<Thema> · Kompetenzblatt“ |
| 2 | Fußzeile nur, was nicht im Kopf steht | umgesetzt nach Beschluss: nur Kennung (links) und Seite (rechts); Sternlegende entfällt (Beschluss b) |
| 3 | Auftakt halbfett in eigener Zeile | umgesetzt; Mathe im Auftakt mit \boldmath; langer Kontext (über 70 Zeichen) normal, damit die Zeile nicht schwer wird |
| 4 | Frage in eigener Zeile, Antwortfeld darunter linksbündig | umgesetzt |
| 5 | Jede Teilaufgabe mit textlicher Aufforderung | umgesetzt: Anweisung über der Teilaufgabe aus bau/regal/ich-kann.csv, sonst aus form („Löse die Gleichung.“) oder aus „Rechne: …“; eine Kurzfrage, die die Anweisung wiederholt („p und q?“), entfällt |
| 6 | Gleichungen, Terme, Optionen untereinander | umgesetzt (kein zweispaltiges gleichungsraster; Kreuze je Zeile) |
| 7 | Ankreuzen: Frage, Umbruch, Kästchen | umgesetzt |
| 8 | Tabellen, Kästchen, Antwortlinien linksbündig | umgesetzt |
| 9 | Bearbeitungsraum nur bei Rechnen/Begründen | umgesetzt (`rechenzeilen`): Ablesen, Ankreuzen, Zeichnen, Ein-Zahl-Antworten ohne Rechnung nur mit Antwortzeile |
| 10 | Ruhiger, mehr Abstand, ein Satz je Zeile | umgesetzt (Aufträge je Satz eine Zeile; Abstände zwischen Nummern und Teilaufgaben). Der Abstand ist gegen die 4-Seiten-Grenze abgewogen (TRI) |
| 11 | Überschrift in Schülersprache, keine Bank-Wörter | umgesetzt: Blatttitel und jede Hauptnummer ein Ich-kann-Satz; Abschnitte „Das kennst du schon“, „Schritt für Schritt“, „Zum Merken“ |
| 12 | Prüfkennung klein rechts in der Auftaktzeile | umgesetzt nach Beschluss c: „P10 ’24“, FOR-Papier „P10 ’26 F“ |
| 13 | Punkte des Originals | entfällt nach Beschluss c (nur Prüfungsheft und Prüfungs-Fokus) |
| 14 | Stern vor dem Buchstaben | entfällt nach Beschluss b; `--niveau ebr` lässt Sternoriginale weg |
| 15 | Nie zwei Verfremdungen desselben Originals | umgesetzt: je Original höchstens eine Aufgabe |
| 16 | Prüfungshöhen: jüngste fünf Jahrgänge, 4–5, verschiedene Formulierungen | umgesetzt (Beschluss d); ältere und doppelte stehen als RESERVE in der log |
| 17 | Fertigkeitsaufgaben vor den Prüfungsaufgaben, ohne eigene Überschrift | umgesetzt: Leiter vor der Prüfungshöhe; keine Überschrift „Anlauf“ |
| 18 | Kein „(ausgelassen)“ | umgesetzt: bauen.py lässt eine fehlerhafte Zeile mit `--ohne` weg und zählt neu (in diesem Lauf nicht nötig) |
| 19 | Inhaltsverzeichnis ab 8 Seiten | nicht zutreffend (2–4 Seiten); gehört zum späteren Heft aus Kompetenzblättern |
| 20 | Fehlende Zeichen | umgesetzt: Vorspann mit \newunicodechar, Text aus FreeSerif (sonst DejaVu Serif, Cambria Math, Segoe UI Symbol), Mathe als Befehl; 0 fehlende Zeichen, pdffonts zeigt FreeSerif, pdftotext findet die Zeichen |
| 21 | Grafik über die Fußzeile | umgesetzt: jede Teilaufgabe ein unteilbarer Block mit \Needspace; 0 Overfull \vbox |
| 22 | Prüfkennung lang in alten Heften | nicht Kompetenzblatt (Hefte werden neu gebaut, wenn sie aus Kompetenzblättern entstehen) |
| 23 | Stern entfällt, Niveau beim Bestellen | umgesetzt (`--niveau for|ebr`) |
| 24 | Punkte nur in Prüfungsheft und Prüfungs-Fokus | umgesetzt: keine Punkte |
| 25 | Flattersatz | umgesetzt (\raggedright global und in allen Blöcken) |
| 26 | Tabellenkopf im Textmodus | umgesetzt (\kbwertetabelle: „Zeit in h“, „Tausend kWh“ als Text, x, t, f(x) als Mathe) |
| 27 | Grafik links, Antwort rechts; Tabelle und leeres Koordinatensystem nebeneinander | umgesetzt; Zeichenaufgaben paarweise nebeneinander. Tabelle + Koordinatensystem in einer Zeile kommt in den fünf Ketten nicht vor (Regel im Skript, ungeprüft am Blatt) |
| 28 | Text über der Tabelle | umgesetzt |
| 29 | „Gerade oder gekrümmt?“; Antwortzeilen je eine Zeile | Antwortzeilen umgesetzt („;“ trennt Zeilen); die Wortwahl betrifft eine Bankzeile in potenz-exponentialfunktionen e1, nicht auf diesen Blättern – Bankbefund, nicht Zusammenbau |
| 30 | Überschrift je Einheit, Zwischenzeile | nicht zutreffend (eine Kette je Blatt) |
| 31 | Bankfehler Radfahrer-Tabelle | nicht auf diesen Blättern (Bankbefund) |
| 32 | Ein Original höchstens einmal | umgesetzt (= 15) |
| 33 | Einheit des Bauens ist das Kompetenzblatt | umgesetzt (Rezept K, Kennung XXX-K<n>) |
| 34 | Regal | Teil 3 (bau/regal/) |

## Entscheidungen dieses Laufs (vom Auftrag nicht geregelt)

1. Katalogeinheit: Die Bank zählt Einheiten nach einem älteren
   Katalog-Commit (p-q-Formel = Bank e3, Katalog Einheit 2). Kopf,
   Merkkasten und Zone kommen aus der Katalogeinheit, gefunden über
   „Sprossen je Verfahrenstyp“ der Mappe. Befund am Bestand: QGL-P1
   (Rezept P, v0.6) trägt den Merkkasten „Nullprodukt“ statt „p-q-Formel“.
2. Ich-kann-Titel: Der Katalog trägt keine Ich-kann-Sätze. Alle Titel
   (Kette, jede Sprosse, Prüfungshöhe, Zonen-Fertigkeiten) stehen in
   bau/regal/ich-kann.csv, umformuliert aus Kettenname, merkmal und
   Voraussetzungszeile (Spalte quelle). Die Prüfungshöhe heißt „Ich kann
   das auch in Aufgaben aus der Prüfung.“ – „Prüfungsaufgaben“ ist
   Bank-Wort (Befund 11).
3. Zone: höchstens drei Fertigkeiten mit je einer Aufgabe; zuerst die,
   deren Voraussetzungszeile die Katalogeinheit nennt, dann „alle
   Einheiten“/ohne Angabe; innerhalb nach gemeinsamen Wortstämmen mit
   der Kette. Die Voraussetzungszeilen sind je Eintrag verschieden
   geschrieben („– Einheit 2“, „für Einheit 1 und 5“, „ab Einheit 2“);
   das Skript liest alle drei Formen und ignoriert Einheitenangaben des
   Nachbarthemas („Thema …, Einheit 1“).
4. Leiter: Pflichtelemente (Fehler finden, Begründen, Darstellung,
   Anwendung) und Erkennungsschritte anderer Ketten stehen nicht auf dem
   Kompetenzblatt – der Auftrag nennt Zone, Leiter, Merkkasten. Eine
   Sprosse, deren Variante 1 ein Original trägt (Sinussatz s4, s10),
   nimmt die kleinste Variante ohne Original.
5. Prüfungshöhe: „jüngste fünf Jahrgänge“ = die fünf jüngsten Jahre unter
   den Originalen der Kette (nicht 2022–2026 absolut; sonst hätte POT-K1
   nur ein Original). Gleiche Formulierung zählt nach den ersten sechs
   Wörtern ohne Zahlen und Mathe. QGL-K1: drei Formulierungen im Fenster
   2021–2025, auf vier aufgefüllt (2022-OS-K3c); 2021-OS-K2c Reserve.
   LIN-K1: alle vier Originale haben dieselbe Formulierung („Graph
   zeichnen: Zeichne den Graphen …“) – vier Aufgaben, weil es keine
   andere gibt.
6. Seitenumfang: Zeichenaufgaben (Koordinatensystem bis 7,5 cm hoch, Karo
   dafür verkleinert) stehen paarweise nebeneinander; `--dicht` paart
   kurze Rechenaufgaben, nur wenn die Probe über vier Seiten kommt (TRI).
   Das berührt Befund 6 nicht (dort: Gleichungen einer Teilaufgabenreihe);
   ob der Lehrer das Paarbild will, ist offen.
7. Fehlende Antwortgerüste der Bank: bei nackter Gleichung ohne Antwort
   „Lösung: ___“ (QGL s7, keine Lösung), bei Ein-Zahl-Aufgaben ein leeres
   Feld (LIN-Zone). Ohne Antwortgerüst und mit Rechnung stehen die
   Schreibzeilen über die Breite (Prüfungshöhen im Textformat).
8. Ersatzschrift: FreeSerif (in der Web-Sitzung per apt
   `fonts-freefont-otf`); auf dem Rechner des Lehrers (MiKTeX) greift
   Cambria Math oder Segoe UI Symbol, sonst setzt der Vorspann die Zeichen
   als Mathe – ungeprüft, weil hier kein Windows.
9. bauen.py räumte im ersten Lauf auch zusammenbau.log weg (Endung .log);
   die fünf log sind danach mit denselben Schaltern ohne Register neu
   erzeugt (Quelltexte byte-gleich geprüft) und das Skript korrigiert.

## Befunde für den Chat

- Zweigzeile: „ab Kl. 9, je nach Buch bis Kl. 10 · P10 ×7“ – die Zahl
  ×n zählt Jahrgänge der Typen der Originale (wie v0.6), nicht die
  Originale der Kette (QGL: 7 Originale, 4 Typen).
- Die Leiter übernimmt jede Sprosse, auch die, die die Mappe als „Vorrat,
  GYM“ führt (Sinussatz s13–s15: Kosinussatz, Herleitung). Ohne sie hätte
  TRI-K1 ohne `--dicht` vier Seiten.
- Zone-Aufgaben der Bank sind knapp („ordnen?“, „wie viel?“); die
  Anweisung aus ich-kann.csv ersetzt die Kurzfrage.
