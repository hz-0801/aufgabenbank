# Stand: wahrscheinlichkeit

Katalog-Commit: 99da6894e7ec588195ab9928aa32d68f2b09c9fa
Datum: 2026-09-27 12:29 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.4 – 0 Abweichungen,
0 Warnungen in allen Dateien.

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | ges. |
|-------|---------:|----------:|--------:|---------:|--------:|-----:|
| zone  |        – |        10 |      11 |        – |       1 |   22 |
| e1    |        4 |         5 |      24 |        2 |      12 |   47 |
| e2    |       12 |         5 |      39 |        2 |      12 |   70 |
| e3    |       12 |         5 |      27 |        2 |      12 |   58 |
| e4    |        4 |         5 |      24 |        2 |      12 |   47 |

## Originale je Einheit

- e1: 2017-OS-K6b (Prüfungshöhe), 2016-OS-K5b, 2016-OS-K5a,
  2017-OS-B1f, 2025-OS-K3a, 2020-OS-K6a, 2015-OS-K5a
- e2: 2016-OS-K5d (Prüfungshöhe), 2019-OS-K6a, 2014-OS-K6a,
  2017-OS-K6a, 2014-OS-B1b, 2016-OS-K5c, 2016-OS-B1f,
  2014-OS-B1d, 2018-OS-B1j, 2019-OS-B1g, 2018-OS-K7b, 2015-OS-B1a
- e3: 2020-OS-K6c (Prüfungshöhe), 2026-FOR-K6b, 2014-OS-K6b,
  2024-OS-K5b, 2025-OS-K3c, 2014-OS-K6c, 2026-FOR-K6c,
  2025-OS-K3b, 2020-OS-K6b, 2025-OS-K3d, 2026-FOR-K6d
- e4: 2018-OS-K7c (Prüfungshöhe), 2024-OS-K5c, 2019-OS-K6b,
  2015-OS-K7d, 2019-OS-K6c

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund |
|-------|-----:|------:|------------------|
| zone  |   22 |     0 | pruef als Zahl statt als Ausdruck-String |
| e1    |    4 |     0 | Zahl nicht an der Ergebnisstelle |
| e2    |    7 |     0 | Zahl nicht an der Ergebnisstelle (4) |
| e3    |    0 |     0 | – |
| e4    |    0 |     0 | – |

## Entscheidungen

1. Zone: Die Fertigkeitszeilen haben keinen Doppelpunkt; kette und
   sprosse_text sind der Text bis „ – Einheit“.
2. Zone-Paar zur Fertigkeit „Anzahl der Zahlen in einem Bereich“
   (erste Nummer mitzählen), dem ersten Muster der Typischen Fehler.
3. „(4×)“ hinter den Grundfallsprossen fehlt im sprosse_text; es ist
   eine Mengenangabe, der Grundfall trägt 5 Zeilen nach bank.md.
4. hoehe pruefung trägt je Einheit nur das erste Original der
   Prüfungshöhe; die „daneben“-Originale und die übrigen
   Hauptoriginale stehen an ihrer Kettensprosse (Feld original).
5. „Zufallsgerät entwerfen (Kugeln einzeichnen)“ als Glücksrad mit
   \kreisleer, weil _bausteine.md keinen Baustein für ein Gefäß mit
   Kugeln führt; 2019-OS-B1g ist entsprechend verfremdet.
6. Grundfall e3 („Baum … zeichnen“) als Beschriften eines Baums mit
   leeren Wahrscheinlichkeitsfeldern (\baumzwei mit Labels).
7. 2015-OS-K5a mit einer kollinearen Dreiergruppe verfremdet (9);
   die Falle „alle Dreierauswahlen“ (10) fehlt als Option, weil 10
   Kastenzahl ist.
8. 2020-OS-K6b und 2025-OS-K3b ohne Ankreuzteil, nur als Begründung
   (unterrichtsblatt 2.3 c: Ankreuzen und Begründen getrennt).
9. Anwendung und Darstellung zitieren Lerneinheiten- oder
   Typenzeilen (11, 15, 17, 22, 24), weil der Katalog dafür keinen
   eigenen Typ nennt; der Typ „Ereignis zu einer gegebenen Rechnung
   in Worten“ (e4) steht als Darstellung, nicht als Typ ohne Kette.
10. Die Grundvorstellung aus „Für schwache Schüler“ (Anteil statt
    Anzahl; sicher – möglich – unmöglich) steht nicht in der Zone,
    weil bank.md die Zone auf „Voraussetzungen (Blatt 0)“ legt.

## Befunde

- Katalog: Der Erkennungsschritt „Was ist möglich, was ist günstig?“
  (Zeile 35) wiederholt die Vorstufe der Kette Einstufig (Zeile 96);
  er entfällt.
- Katalog: Der Erkennungsschritt „Mit oder ohne Zurücklegen?“
  (Zeile 37) wiederholt die Vorstufe der Kette Mit Zurücklegen
  (Zeile 97); er entfällt und steht damit auch in e4 nicht.
- bank.md: „Fertigkeit bis zum Doppelpunkt“ passt nicht auf
  Fertigkeitszeilen ohne Doppelpunkt wie in diesem Eintrag.
- Prüfskript: Ein Ergebnis nach „also“ am Satzende gilt nicht als
  Ergebnisstelle; Begründungen mussten mit dem Ergebnis beginnen.
- Prüfskript: „Behauptung prüfen“ an einer Kettensprosse verlangt
  pruef, obwohl bank.md "" bei Begründen erlaubt.

## Offene Punkte

- 2024-OS-K5a und 2026-FOR-K6a sind in keiner Zeile verfremdet.
- Die Grafiken (\baumzwei und \baumdrei mit Wort-Labels und leeren
  Feldern, zwei \kreisdiagramm in einem Feld, \kreisleer) sind
  ungerendert, weil LaTeX nicht verfügbar ist.
