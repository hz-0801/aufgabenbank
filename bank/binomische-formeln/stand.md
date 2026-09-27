# Stand: binomische-formeln

Katalog-Commit: 99da6894e7ec588195ab9928aa32d68f2b09c9fa
(2026-09-25, aus dem Kopf von mappen/binomische-formeln.md)
Datum: 2026-09-27 (date, UTC)
Prüfskript: werkzeuge/bank-pruef.py v0.3, Endstand 0 Abweichungen,
0 Warnungen in allen Dateien, auch mit --katalog (Katalogzeilen
aus Teil 1 der Mappe).

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      30         0        14      15        0       1
    e1.jsonl        48         4         5      30        3       6
    e2.jsonl        50         8         5      27        4       6
    e3.jsonl        42         4         5      24        3       6

Pflicht je Einheit: e1, e2, e3 je fehler 3, begruenden 3 ·
Zone fehler 1 (Paar).

## Originale je Einheit

- e1: keins (Katalog: keine P10-Aufgabe); Prüfungshöhe ist die
  Zielmarke, hoehe pruefung, original null, 3 Zeilen.
- e2: 2017-OS-K5d (2 Zeilen), 2022-OS-K3c (2 Zeilen), beide an
  der Prüfungssprosse s10 der Kette Binomische Formeln.
- e3: keins (Katalog: keine P10-Aufgabe); Zielmarke wie e1.

## Prüfskript vor der Korrektur

- zone.jsonl: 0 Abweichungen, 0 Warnungen.
- e1.jsonl: 0 Abweichungen, 0 Warnungen.
- e2.jsonl: 0 Abweichungen, 0 Warnungen.
- e3.jsonl: 0 Abweichungen, 0 Warnungen.

Keine Einheit ist gescheitert. Vor jedem Schreiben lief eine
eigene Probe (Skript im Scratchpad, nicht im Repo): Termgleichheit
von Aufgabe und Lösung durch Einsetzen zufälliger Brüche (114
Paare), eigene Sperrliste, mehrstellige Kastenzahlen, sprosse_text
und kette wortgleich in der Zeile quelle, Ankreuzlösung. Sie fand
in e1 „2ab" (Glied der Formel im Kasten) und in e3 „(x + 6)²"
(Typische Fehler, Zeile 80); beide vor dem ersten Skriptlauf
geändert. Gegenprobe der Sperre: fünf gesperrte Terme in einer
Kopie von e2 wurden alle gemeldet.

## Entscheidungen

1. sprosse_text ist das Segment zwischen zwei Pfeilen der
   Kettenzeile, wortgleich samt Zusätzen („(4×)", „(Vorrat)"),
   ohne Schlusspunkt. Prüfungshöhe e1 und e3 ohne die
   Quellenklammer. Prüfungshöhe e2: das ganze Segment mit beiden
   Originalen, weil die Gegenprobe genau eine Prüfungssprosse je
   Einheit verlangt; 4 Zeilen, 2 je Original.
2. Erkennungsschritt: kette ist die Frage ohne Anführungszeichen,
   sprosse_text Frage und Handlung bis vor die Beispielklammer.
3. Zone: kette und sprosse_text bis zum Doppelpunkt; Zeile 25 und
   29 haben keinen, dort bis vor „ – " bzw. vor die
   Beispielklammer. quelle ist die Fertigkeitszeile.
4. Zone-Folge nach erster Verwendung, bei gleicher Einheit nach
   Lehrplanfolge der Voraussetzungsthemen: Einheit 1 f1 Vorzeichen
   (rationale Zahlen), f2 Termwert, f3 Zusammenfassen, f4 Klammer
   (terme E1–E3); Einheit 2 f5 Quadratzahlen vor f6
   Scheitelpunktform; Einheit 3 f7 Ausklammern. Je Fertigkeit ein
   Fallstrick.
5. Zone-Paar an f4 (Minusklammer, s4 fehler, s5 Rechnung): trägt
   e1 (Minus in Klammern), e2 (Minus vor der Klammer) und den
   P10-Nachbarfehler 2023-OS-K4b. „Mittelglied fehlt" ist der
   häufigste Fehler des Eintrags, aber Themenstoff, nicht Zone.
6. Erkennungsschritte: vier entfallen nach bank.md (Befund 1);
   „Gleiche Klammer zweimal?" bleibt als e2 k1. Die Vorstufe e2
   trägt je Zeile Formel und a, b; die Vorstufe e3 je Zeile
   Quadrate, Wurzeln und Mittelglied.
7. e1 Vorstufe: Die Pfeile gehen über den gedruckten Term, daher
   ohne grafik und mit „Verbinde … durch einen Pfeil"; kein
   Baustein trägt Pfeile zwischen Termgliedern.
8. Typen ohne Kette: e1 „Termwert mit zwei Variablen berechnen
   (auch negativ)", e2 „Kopfrechnen mit der Formel (Vorrat)".
   e3 hat keinen; alle Typen stehen in der Kette.
9. Pflicht nur fehler und begruenden: Die Typenzeilen tragen weder
   Darstellungswechsel noch Sachanwendung (Flächenbild nur als
   Begründungsmittel; „Anwendung: Produktform gleich null" ist
   Kettensprosse e3 s8). Je Fehlervariante ein Muster der
   Typenzeile; e2 ohne „Vorzeichen des Mittelglieds" (drei
   Varianten, vier Muster).
10. 2017-OS-K5d verfremdet nur den Nachweis der Normalform, ohne
    Nullstellen; 2022-OS-K3c bis zur Gleichung „… = 0" ohne Lösen.
    Grund: Die Sprosse heißt „vor dem Gleichsetzen
    ausmultiplizieren", das Lösen ist quadratische-gleichungen.md
    Einheit 3 und wäre ein neues Merkmal (2.4 c).
11. Nicht als Original aufgenommen: 2018-OS-K5c, 2025-OS-K5b,
    2023-OS-K4c (quadratische Ergänzung nur als Alternative),
    2020-OS-K3c (Zahlenquadrat), 2020-OS-K3e (Faktorisieren als
    Alternative). Keins steht an einer Kettensprosse.
12. Ausmultiplizieren und Faktorisieren: form gleichungsraster,
    aufgabe kurzer Anweisungssatz mit Term in $…$ („Multipliziere
    aus: …", wie terme), antwort leer.
13. pruef bei Termergebnissen: erste Zahl der Lösung mit Vorzeichen
    (Vorzahl, Mittelglied oder Zahl der Klammer); v0.3 liest
    „x^2 - 18x" als −18. Die Gleichwertigkeit prüfte die eigene
    Probe (oben).
14. Buchstaben: e1 x, y, a, b als Variablen; e2 a, b nur als Teile
    der Formel, Terme mit x, y, z, p Parabel, g Gerade; e3 nur x.
15. Mehrstellige Kastenzahlen (10, 12, 13, 15, 25, 75) in keiner
    aufgabe; die eigene Sperrliste nimmt zusätzlich die Beispiele
    aus Voraussetzungen und Erkennungsschritten, die das Skript
    nicht sperrt.
16. Ankreuzen nur als ja/nein mit \janein; loesung beginnt mit
    „ja" oder „nein", pruef trägt die Zahlen der Begründung.

## Befunde

1. Katalog: Fünf Erkennungsschritte wiederholen den Handgriff der
   Vorstufe einer Kette derselben Einheit und entfallen nach
   bank.md: „Was mal was?" (e1-Vorstufe, Pfeile „jedes mit
   jedem"); „Was ist a, was ist b?" und „Welche Formel?"
   (e2-Vorstufe „Formel erkennen und a, b einkreisen"); „Ist das
   ein Quadrat?" und „Passt das Mittelglied?" (e3-Vorstufe nennt
   beide wörtlich). Der Katalog führt jeweils beide.
2. bank.md: „kette und sprosse_text der Zone sind die Fertigkeit
   bis zum Doppelpunkt" greift nicht bei Fertigkeitszeilen ohne
   Doppelpunkt (hier Zeile 25 und 29).
3. Prüfskript: Bei \janein gibt es keine \kreuz-Optionen; die
   Ankreuzprobe prüft dann nicht, dass loesung eine Option (ja
   oder nein) nennt. Hier von der eigenen Probe übernommen.
4. Prüfskript: Termlösungen bleiben über eine Zahl prüfbar; ob der
   Lösungsterm zur Aufgabe gleichwertig ist, prüft es nicht
   (Befund schon bei terme).
5. Katalog: Vorrat mitten in der Kette. e2 s3 (dritte Formel) und
   s6 (zwei Variablen) sind Vorrat, stehen aber vor den
   P10-tragenden Sprossen s7–s9; ein Blatt für den Mindeststoff
   muss sie überspringen. e3 ist als ganze Einheit Vorrat.
6. Katalog: Kein Typ trägt eine Sachanwendung oder einen
   Darstellungswechsel; die Pflichtelemente anwendung und
   darstellung fehlen darum im ganzen Eintrag.

## Offene Punkte

- LaTeX nicht kompiliert: \rechnung mit Zeilenwechsel (e1 k3 s1
  v3), \janein am Satzende nach dem Term, „… $= 0$" in
  Anführungszeichen (e2 s10).
- Pfeile über dem gedruckten Term (e1 Vorstufe) mit dem
  Zusammenbau klären.
- Konvention gleichungsraster (Anweisungssatz mit $…$ wie terme
  oder nur die Gleichung wie quadratische-gleichungen) angleichen.
