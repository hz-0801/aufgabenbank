# Stand: trigonometrische-funktionen

Katalog-Commit: 99da6894e7ec588195ab9928aa32d68f2b09c9fa
(2026-09-25, aus dem Kopf der Mappe)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.4; Endstand 0 Abweichungen,
0 Warnungen.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruefung | pflicht |
|-------|-------:|-------:|--------:|--------:|---------:|--------:|
| zone  |     46 |      0 |      22 |      23 |        0 |       1 |
| e1    |     54 |      4 |       5 |      36 |        3 |       6 |
| e2    |     60 |      4 |       5 |      39 |        3 |       9 |
| e3    |     57 |      4 |       5 |      39 |        3 |       6 |
| e4    |     51 |      4 |       5 |      33 |        3 |       6 |
| Summe |    268 |     16 |      42 |     170 |       12 |      28 |

## Originale je Einheit

- e1: 2015-OS-K5c, 2020-OS-K7c, 2025-OS-K4c (Sprosse 13)
- e2: keine
- e3: keine
- e4: 2019-OS-K7c (2 Zeilen), 2026-FOR-K7b (1 Zeile), Sprosse 12
- Prüfungshöhe aller Einheiten: Zielmarke, original null, 3 Zeilen

## Prüfskript vor der Korrektur

- zone: 4 Abweichungen, 0 Warnungen; Grund: \sin und \cos als
  Baustein nicht in _bausteine.md
- e1, e2, e3, e4: je 0 Abweichungen, 0 Warnungen
- Gegenprobe danach: 4 Zeilen mit Kastenzahl in aufgabe (360 in
  e1 s7 dreimal, 90 in e4 s6 v3), zeilengenau korrigiert

## Entscheidungen

- Alle sieben Erkennungsschritte entfallen, jeder ist die Vorstufe
  seiner ersten Einheit; in E1 und E4 trägt eine Vorstufe mehrere.
- Grundfall E1 mit einem Winkel je Quadrant, weil der Katalog
  keine eigene Sprosse für Winkel über 90° führt.
- Graphen im Gradmaß als ksys mit \funktion{sin(\x)} (pgf rechnet
  in Grad), nicht ksys[trigo] (Bogenmaß); Einheitskreis zum
  Ablesen und Einzeichnen als ksys mit zwei Halbkreisen.
- Zone: kette ist die Fertigkeit bis „ – Einheit“, weil nur eine
  Fertigkeitszeile einen Doppelpunkt hat; gleiche Einheit in
  Eintragsfolge.
- Zone-Paar in der Fertigkeit Taschenrechner (RAD statt DEG), dem
  einzigen P10-belegten Fallstrick.
- Pflicht anwendung entfällt: E1–E3 haben keinen Anwendungstyp,
  E4 ist selbst die Anwendungskette; darstellung nur in E2.
- „zwei Graphen mit verschiedenen Parametern vergleichen“ (E3) ist
  Typ ohne Kette mit 3 Zeilen.
- Nebenleistungs-Originale an Kettensprossen je eine Zeile; die
  dritte Zeile in E4 nimmt 2019-OS-K7c mit einer Sinuskurve im
  Kandidatenfeld.
- E3 führt die drei Vorrat-Sprossen (GYM) vor der Prüfungshöhe,
  wie der Katalog sie reiht.
- 90°, 180°, 270°, 360° stehen nicht in aufgabe (Vollkreis, ganz
  oben), nur in Lösung und Grafik.

## Befunde

- Katalog: Die sieben Erkennungsschritte (Zeile 41–47) wiederholen
  die Vorstufen der Ketten (Zeile 108–111); er führt beide.
- Prüfskript: \sin und \cos fehlen in STANDARD und gelten als
  Bausteine der Vorlage, obwohl sie Standard-LaTeX sind.
- Prüfskript: ksys_bereiche kennt die Option trigo nicht und
  prüft Punkte einer trigo-Grafik gegen −4 bis 4.
- Prüfskript: FOLGE kennt „°“ nicht als Einheit; in „0°; 180°“
  zählt nur die erste Zahl als Ergebnis.
- Auftrag: „Kastenzahlen“ trifft im Wortlaut auch Quellzeilen des
  Merkkastens (Kl. 10, Serlo 1961) und „P10“; gezählt wurde nur
  der Kasteninhalt.
- bank.md: „Fertigkeit bis zum Doppelpunkt“ passt nicht auf
  Fertigkeitszeilen ohne Doppelpunkt (hier zehn von elf).

## Offene Punkte

- Nicht kompiliert: Halbkreise mit \funktionab und
  sqrt(abs(1-\x^2)) sowie \funktion in Grad sind im Satz
  ungeprüft.
- \einheitskreis[ohne]: ob der Winkel eine Zahl trägt, ist
  ungeprüft; beim Messen des Winkels darf keine erscheinen.
- Gefüllte \wertetabelle mit 0.71 setzt vermutlich einen Punkt
  statt eines Kommas (e2 s2).

## Nachbesserung 2026-09-27

- Prüfskript v0.5: 0 Abweichungen, 0 Warnungen vor und nach der
  Nachbesserung; keine jsonl-Zeile geändert oder gestrichen.
- Prüfungshöhe: Alle vier Zielmarken ohne P10-Original stehen schon
  als hoehe pruefung, original null, 3 Zeilen; nichts umgestellt.
- Erkennungsschritte: Alle sieben waren schon entfallen, weil jede
  Vorstufe denselben Handgriff trägt; keine weitere Streichung.
- Befunde: Keiner ist mit v0.5 erledigt; `\sin` und `\cos` fehlen
  weiter in STANDARD, ksys_bereiche kennt trigo weiter nicht, FOLGE
  kennt „°“ weiter nicht.
