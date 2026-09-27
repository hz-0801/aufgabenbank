# Stand: koerper

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf von mappen/koerper.md)
Datum: 2026-09-27 07:22 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.3, Endstand 290 Zeilen OK,
0 Abweichungen, 0 Warnungen.

## Dateien

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     28 |        0 |        12 |      15 |        0 |       1 |
| e1    |     52 |        4 |         5 |      27 |        4 |      12 |
| e2    |     56 |        4 |         5 |      30 |        5 |      12 |
| e3    |     47 |        4 |         5 |      24 |        2 |      12 |
| e4    |     57 |        8 |         5 |      30 |        2 |      12 |
| e5    |     50 |        4 |         5 |      27 |        2 |      12 |

Pflicht je Einheit: fehler 3, begruenden 3, anwendung 3,
darstellung 3. Zone: pflicht fehler 1 (Zone-Paar). e4 vorstufe 8:
Erkennungsschritt „Welche Einheit?“ (4) und Vorstufe der Kette (4).

## Originale je Einheit

Prüfungshöhe (je Einheit eine Sprosse, letzte der Kette):
- e1: 2016-OS-B1j 2, 2019-OS-B1f 2 (eine Sprosse, 4 Zeilen)
- e2: 2026-FOR-B1f 2; dazu Aquarium ohne Original 3 (original null)
- e3: 2019-OS-K4c 2
- e4: 2023-OS-K5d 2
- e5: 2024-OS-K4c 2

An Kettensprossen und Typen (Feld original, Kennung im Text):
- e1: 2017-OS-B1c (s0 v1–v2), 2015-OS-K6b (s7), 2024-OS-K4b (k4,
  Kegel im Quader), 2018-OS-B1i (k5 s4 v1, darstellung)
- e3: 2014-OS-K5a (s1 v4–v5, gegebene Trapezfläche)
- e4: 2022-OS-K2d (s9), 2023-OS-K5b (s10 v1, v3), 2022-OS-K2b
  (s10 v2)
- e5: 2024-OS-K4b (s6, kleinste Verpackung)

## Prüfskript vor der Korrektur

- zone: 0 Abweichungen, 0 Warnungen im ersten Lauf (v0.2; nach dem
  Pull auf v0.3 erneut 0/0).
- e1: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e2: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e3: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e4: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e5: 1 Abweichung, 0 Warnungen im ersten Lauf (k4-s3-v2: „132
  nicht an der Ergebnisstelle“, Summand statt Ergebnis in pruef);
  zweiter Lauf 0/0.
- Zweimal gescheitert: keine Einheit.

Eigene Zusatzprobe (mehrstellige Kastenzahlen in aufgabe,
sprosse_text wortgleich in Zeile quelle, grafik bei zeichnen):
e3 eine Kastenzahl (16 in einer vorgegebenen Fehlrechnung), e5
eine (12 als Uhrzeit), vor dem Commit ersetzt. Weiche Treffer
(Zahlen aus Originalen und Typische Fehler: 100, 1,8, 1,3, 54, 27)
ebenfalls ersetzt; 1,5 als Zahl unter 10 belassen. In e3 stand vor
dem Commit ein Gleitkomma-Rest in einer Lösung (1,404…01),
behoben.

## Entscheidungen

1. Erkennungsschritte: Fünf von sechs verlangen denselben Handgriff
   wie die Vorstufe der Kette ihrer ersten Einheit und entfallen
   (bank.md; Befund 1). Es bleibt „Welche Einheit?“ in e4 (k1),
   weil die Vorstufe dort Radius oder Durchmesser ist.
2. Zone: Reihenfolge nach erster Verwendung, bei gleicher Einheit
   Folge des Eintrags (die Lehrplanfolge steht nicht in der Mappe):
   Räumliches Vorstellen (Z. 36), Flächeninhalt (31), Einheiten
   (32), Umstellen (34), Multiplizieren/π/Wurzel (33), Prozentwert
   (35). kette = Fertigkeit bis zum Doppelpunkt, ohne Doppelpunkt
   bis „ – Einheit“.
3. Zone-Paar in „Flächeninhalt …“: Durchmesser statt Radius beim
   Kreis – der häufigste Fehler des Eintrags (fünf P10-Belege in
   Typische Fehler, Z. 89).
4. Prüfungshöhe: je Einheit genau eine Sprosse. e1 trägt beide
   Originale der Kettenzeile in einer Sprosse (4 Zeilen); e2 den
   Würfel (2, Original) und das Aquarium (3, original null) in
   einer Sprosse, sprosse_text die ganze Prüfungszeile.
5. Originale der Zielmarke an Kettensprossen im Feld original
   (Liste oben), nur an Varianten, die das Original verfremden.
   2019-OS-K4b nicht, weil die Mappe es bei flaechen.md führt.
6. Typen ohne Kette: e1 drei (Grund- und Deckfläche benennen;
   Schrägbild lesen; Kegel im Quader), e2 vier (Oberfläche ohne
   Deckel; Würfelkante aus V; m³ und Liter; Füllhöhe), e5 zwei
   (Füllstand; Oberfläche zusammengesetzt, obwohl Vorrat). e3 und
   e4 keine: jede Typangabe steckt in der Kette oder in den
   Pflichtelementen (Sachaufgabe als anwendung).
7. Pflichtelemente: Sprossen 1 fehler, 2 begruenden, 3 anwendung,
   4 darstellung; sprosse_text aus „Typen je Lerneinheit“, e2
   anwendung aus Zeile 13 („Aquarium und Kiste“).
8. Würfelnetze ohne passenden Baustein: grafik als
   `$\begin{array}…$` mit Buchstaben oder `\square`; Gültigkeit und
   Gegenflächen jedes Netzes per Faltsimulation geprüft.
9. Zeichnen auf Kästchenpapier: grafik `\rechenplatz{5}`, Lösung in
   loesungsgrafik (`\netzquader`, `\quader`, `\prismadreieck`,
   `\netzzylinder`, Maße halbiert). Schrägbild lesen ohne grafik,
   weil der Baustein die im Text genannten Längen nicht zeichnet.
10. Kastenzahlen: keine mehrstellige Zahl aus dem Merkkasten (10,
    12, 16, 40, 45, 48, 64, 76, 96, 120, 144, 160, 184, 188,5, 192,
    245,0, 282,7, 283, 1000) in einer aufgabe; auch nicht in
    Ankreuzoptionen und vorgegebenen Fehlrechnungen.
11. Ankreuzen mit Termoptionen: loesung beginnt mit der Option
    wortgleich und nennt den Wert; pruef trägt den Wert.
12. Einheiten als Unicode außerhalb der Mathematik („cm³“, „m²“);
    Buchstaben nur mit Erklärung im Text (Kegelformel in e5).

## Nachbesserung 2026-09-27

Prüfskript v0.5, bank.md Stand 2026-09-27b; erster Lauf 0
Abweichungen, 0 Warnungen, Endstand ebenso.

- Keine Zeile geändert: die einzige Prüfungshöhe ohne Original
  (Aquarium, e2-k1-s8) trägt schon hoehe pruefung mit original
  null, 3 Zeilen, und der einzige Erkennungsschritt (e4-k1 „Welche
  Einheit?“) verlangt einen anderen Handgriff als die Vorstufe von
  e4-k2 („Radius oder Durchmesser benennen“).
- Befund 5 besteht unter v0.5 fort (Probe: „$\pi \cdot 3^2 \cdot
  10$“ und „$1\,000 : (\pi \cdot 16)$“ ohne Abweichung,
  „$5 \cdot 4 \cdot 2$“ gefangen); kein Befund ist durch v0.5
  erledigt.

## Befunde

1. Katalog: Fünf Erkennungsschritte wiederholen die Vorstufe der
   Kette derselben Einheit: „Welcher Körper?“ / Körper ankreuzen
   (e1), „Volumen oder Oberfläche?“ / Volumen oder Oberfläche
   ankreuzen (e2), „Was ist die Höhe?“ / Grundfläche und Höhe
   markieren (e3), „Radius oder Durchmesser?“ / Radius oder
   Durchmesser benennen (e4), „Zerlege und benenne“ /
   Teilkörper benennen (e5). Der Katalog führt beide.
2. Katalog: Die Prüfungshöhe von e2 bündelt ein P10-Original und
   eine Sachaufgabe ohne Original („Aquarium in Litern“) in einer
   Zeile; bank.md kennt je Einheit eine Prüfungssprosse.
3. Katalog: „zusammengesetzt aus zwei Quadern“ (e2) und „zwei
   Quader“ (e5, Grundfall) verlangen denselben Handgriff in zwei
   Einheiten. „Kante aus V“ (Kette e2) deckt die Typen „Kante aus
   V und zwei Kanten“ und „Würfelkante aus V“ nicht beide.
4. Katalog: 2024-OS-K4b steht in der Zielmarke von e1 (Kegel
   einzeichnen) und in der Zuordnung von e5 (Verpackungsmaße);
   hier an beiden Stellen als Original geführt.
5. Prüfskript v0.3: Die Sperrprobe fängt Terme mit π nicht. Probe:
   „$\pi \cdot 3^2 \cdot 10$“ (Merkkasten, Z. 72) und
   „$1\,000 : (\pi \cdot 16)$“ (Original 2023-OS-K5d) ohne
   Abweichung; „$5 \cdot 4 \cdot 2$“ und „$12 \cdot 10$“ werden
   gefangen.

## Offene Punkte

- LaTeX nicht kompiliert. Ungeprüft: `$\begin{array}…$` als grafik
  im Zusammenbau, zwei Aufrufe in einem grafik-Feld
  (`\prismadreieck … \rechenplatz[halb]{4}`), Lage und
  Beschriftung von `\prismadreieck`, `\quader`, `\netzquader`,
  `\netzzylinder`, `\pyramide` mit leeren Labels.
- Kein Baustein für ein freies Würfelnetz oder ein Prismennetz
  (Vorlage: nur `\netzwuerfel` als Kreuz, `\netzquader`,
  `\netzpyramide`, `\netzzylinder`).
- Die Grundfälle von e2 (Kette) und e5 sind inhaltlich nah (zwei
  Quader addieren); verschiedene Zahlen und Kontexte, keine
  Aufgabe doppelt.
