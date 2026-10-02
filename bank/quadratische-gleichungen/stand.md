# Stand: quadratische-gleichungen

Katalog-Commit: 99da6894e7ec588195ab9928aa32d68f2b09c9fa
(2026-09-25, aus dem Kopf der Mappe)
Datum: 2026-09-27 (`date`, 05:26 UTC)
Prüfskript: werkzeuge/bank-pruef.py v0.2 – Endstand 0 Abweichungen,
0 Warnungen in allen fünf Dateien.

## Dateien

    Datei       Zeilen vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      34        0        16      17        0       1
    e1.jsonl        63        8         5      36        2      12
    e2.jsonl        43        4         5      24        4       6
    e3.jsonl        79       12         5      36       14      12
    e4.jsonl        39        4         5      21        3       6
    gesamt         258       28        36     134       23      37

(Zahlen nach der Nachbesserung 2026-09-27.)

Pflicht je Einheit: e1 und e3 fehler, begruenden, darstellung,
anwendung je 3; e2 und e4 fehler und begruenden je 3. Zone: ein
Zone-Paar (fehler + Rechenaufgabe) an f1.

## Originale je Einheit

- e1: 2021-OS-K7c (2 Zeilen)
- e2: 2025-OS-B1h (2), 2020-OS-K3e (2, Faktorisieren)
- e3: 2020-OS-K3e, 2025-OS-K5c, 2023-OS-K4c, 2021-OS-K2c,
  2022-OS-K3c, 2024-OS-K3d, 2017-OS-K5d (je 2)
- e4: keines (Katalog: kein P10-Original)

## Prüfskript vor der Korrektur

Erster vollständiger Lauf je Datei (vorher liefen Formatproben mit
Testzeilen, um ID-Schema und Ergebnisstelle zu klären; sie zählen
hier nicht):

- zone.jsonl: 0 Abweichungen, 0 Warnungen
- e1.jsonl: 30 Abweichungen, 0 Warnungen – „hoehe sprosse nach
  höherer Stufe“: die P10-Form-Sprossen 2020-OS-B1d und 2022-OS-K2d
  standen als pruefung mitten in der Kette
- e2.jsonl: 3 Abweichungen, 0 Warnungen – Ergebnisstelle bei
  geordneten Termen (pruef −10, −18, −7 nicht gefunden)
- e3.jsonl: 0 Abweichungen, 0 Warnungen
- e4.jsonl: 0 Abweichungen, 0 Warnungen

Die eigene Nachprüfung (Sperrliste aus Kasten, Typische Fehler,
Originalen, Voraussetzungen; sprosse_text in Zeile quelle) fand vor
dem Commit zusätzlich: e1 (x + 3)² = 25, (x + 3)² = 4 und
x² = −36; e3 −x² + 6x + 7 und die Gerade −3x + 1. Alles ersetzt;
das Skript hatte keine davon gemeldet. Keine Einheit scheiterte
zweimal.

## Entscheidungen

1. Erkennungsschritt und gleichnamige Vorstufe der Kette sind
   inhaltlich getrennt: e1 Erkennung an x² = c, Vorstufe an
   (x − d)² = c; e2 Erkennung an x·(x + a), Vorstufe an zwei
   Klammern; e3 „Was sind p und q?“ an Termen, Vorstufe an ganzen
   Gleichungen mit unsichtbarer Eins und fehlender Zahl; e4
   Erkennung Länge/Anzahl, Vorstufe mit dem Fall „beide“
   (Zahlenrätsel). (Überholt, Nachbesserung 2026-09-27: die vier
   Erkennungsschritte sind gestrichen.)
2. „Zwei, eine oder keine?“ ohne Null-Fall: x² = 0 steht im
   Merkkasten. Den Null-Fall trägt die Vorstufe mit (x − 4)² = 0.
   (Erkennungsschritt gestrichen, Nachbesserung 2026-09-27.)
3. P10-Form-Sprossen in der Kettenmitte (e1 s2 zu 2020-OS-B1d,
   s6 zu 2022-OS-K2d) als hoehe sprosse, 3 Zeilen, ohne original
   und ohne Prüfkennung – das Skript verlangt steigende hoehe.
4. Prüfungshöhe e4 ohne Original als hoehe sprosse mit 3 Zeilen –
   das Skript verlangt bei pruefung ein original. (Überholt,
   Nachbesserung 2026-09-27: jetzt hoehe pruefung, original null.)
5. Eine Prüfungshöhen-Sprosse trägt alle Originale der Kette, je 2
   Zeilen. 2017-OS-K5d (Nebenmarke der Zielmarke e3, nicht in der
   Kettenzeile) ist aufgenommen.
6. Nicht aufgenommen: 2014-OS-K7a (Nebenmarke e4, inhaltlich
   Gleichsetzen); 2018-OS-B1c und 2022-OS-B1c (linear, Typ bei
   lineare-gleichungen.md); 2020-OS-B1d und 2022-OS-K2d nur als
   P10-Form (Punkt 3).
7. Pflichtelemente: je Pflichtart eine Sprosse mit 3 Varianten; die
   Fehler-Varianten nehmen je ein Muster der Typenzeile, e4 v3 das
   Muster „Zahlenrätsel: eine Zahl weggelassen“ (Z. 100).
   darstellung und anwendung nur in e1 und e3; e2 hat keinen Typ
   dafür, e4 ist als Kette selbst Anwendung.
8. sprosse_text der Pflicht wortgleich: Fehler finden und Begründen
   aus „Typen je Lerneinheit“; darstellung e1 Z. 24 „Zahl der
   Lösungen am Graphen ablesen …“, e3 Z. 26 „grafische Kontrolle an
   der Parabel (Vorrat) [OS 9]“; anwendung e1 Z. 106 „Einstieg im
   Sachzusammenhang“, e3 Z. 8 „Sachkontexte: Architektur und
   Brückenbogen, Wurfparabeln.“
9. Typen ohne Kette: e3 „Gerade und Parabel gleichsetzen als
   Anwendung“, e4 „Quadrat mit Rand (Vorrat)“. Als gedeckt gelten:
   e1 „Zahl der Lösungen an c begründen“ (Vorstufe und Begründen),
   e2 „Nullstellen durch Faktorisieren“ (Prüfungshöhe 2020-OS-K3e),
   e3 „Zahl der Lösungen am Wert unter der Wurzel beurteilen“ (s8).
10. Zone: Folge nach erster Verwendung, bei gleicher Einheit
    Reihenfolge des Eintrags: f1 Quadrieren, f2 Wurzel, f3 lineare
    Gleichung, f4 Einsetzen, f5 Klammer zuerst, f6 Scheitelpunktform
    (e1), f7 Ausklammern/binomisch (e2), f8 Terme ordnen (e3). Je
    Fertigkeit s1 leicht (2), s2 mittel (1), s3 ein Fallstrick (1);
    kette und sprosse_text = Fertigkeit bis zum Doppelpunkt; hoehe
    sprosse. Zone-Paar an f1 (Vorzeichen beim Quadrieren), s4 fehler,
    s5 Rechenaufgabe. Varianten laufen je Fertigkeit 1..n durch.
    (hoehe überholt, Nachbesserung 2026-09-27: s1 grundfall.)
11. gleichungsraster: aufgabe ist nur die Gleichung, ohne $ (für
    \gl{…}) und ohne Fragewort – die Anweisung trägt die Hauptnummer.
12. Ankreuzen: jede Option nach „\\ “ in eigener Zeile. Wortoptionen
    (zwei/eine/keine, gilt/gilt nicht, wahr/falsch) mit pruef "" und
    ziffernfreier Lösung.
13. Terme als Ergebnis (Zone f7/f8, e2 s9): pruef ist der erste
    Koeffizient nach x²; ein negativer ohne Leerzeichen nach dem
    Minus notiert (TeX setzt es gleich).
14. „Keine Lösung“: pruef ist der negative Wert unter der Wurzel
    bzw. von x².
15. Vierstellige Zahlen ohne Tausenderzwischenraum (2400, 6000).
16. x ist in jeder Aufgabe die gesuchte Größe und wird im Text
    benannt; e3: f, g Funktionsnamen (nicht p, das ist der
    Formelparameter), h Höhe, D Diskriminante.
17. Prüfkennung „(P10 Jahr OS)“, papier aus der Mappe.
18. Faktorisieren in e2 (2020-OS-K3e) mit Hinweis im Aufgabentext
    (Produkt und Summe), weil die Kette es nicht einführt.

## Befunde

1. Prüfskript/bank.md: Das Zone-ID-Muster hat keine Sprossennummer;
   das Skript verlangt darum Varianten 1..n über die ganze
   Fertigkeit. bank.md sagt das nicht. (erledigt v0.5)
2. Prüfskript/bank.md: bank.md erlaubt original null bei pruefung,
   das Skript nicht. Eine Einheit ohne Original (e4) kann keine
   Prüfungshöhe tragen. (erledigt v0.5)
3. Prüfskript/Katalog: hoehe muss in der Kette steigen, der Katalog
   setzt P10-Form-Sprossen in die Mitte (e1). Deren Originale gehen
   dem Feld original verloren. (erledigt v0.5: original steht an
   jeder hoehe; die Daten nutzen es noch nicht, Befund 11)
4. Prüfskript, Sperre: meldet x² = 36 (Merkkasten) nicht (Probe)
   und nicht (x + 3)² in (x + 3)² = 25 (Typische Fehler,
   2017-OS-K5d). (erledigt v0.5)
5. Prüfskript, Ergebnisstelle: „x^2 - 12x“ wird als 12 gelesen, das
   Minus geht mit dem Leerzeichen verloren; Terme sind nur über den
   ersten Koeffizienten prüfbar. (erledigt v0.5 für das Minus;
   Terme bleiben nur über einen Koeffizienten prüfbar)
6. Prüfskript: pruef "" gilt als „pruef fehlt“, sobald loesung eine
   Ziffer enthält, auch die 2 in x^2. (erledigt v0.5)
7. Katalog: Die Erkennungsschritte „Zwei, eine oder keine?“, „Steht
   rechts eine Null?“ und „Welche Lösung passt zur Frage?“ decken
   sich mit den Vorstufen der Ketten e1, e2, e4; mit bank.md
   (Erkennungsschritt als eigene Kette plus Vorstufe 4) entsteht
   Doppelung. Dasselbe gilt für „Was sind p und q?“ und die Vorstufe
   der p-q-Formel (e3, beide: p und q mit Vorzeichen einkreisen).
   Nach bank.md 2026-09-27b sind die vier Erkennungsschritte in der
   Bank gestrichen; der Katalog führt weiter beide.
8. Katalog: Die Prüfungshöhe e2 (2020-OS-K3e) verlangt Faktorisieren
   einer Normalform, das die Kette nicht einführt (2.4 c).
9. Katalog: Die Prüfungshöhe e3 (2021-OS-K2c, 2022-OS-K3c,
   2024-OS-K3d) verlangt Gleichsetzen, das die Kette nicht hat; hier
   über den Typ ohne Kette abgefangen.
10. Katalog: Zielmarke e4 nennt 2014-OS-K7a; das ist Gleichsetzen
    Gerade–Parabel und gehört zu e3.
11. Bank: Die P10-Form-Sprossen e1 s2 (2020-OS-B1d) und s6
    (2022-OS-K2d) tragen original null und keine Prüfkennung; nach
    bank.md darf das Feld dort stehen. Nicht nachgezogen, weil der
    Auftrag es nicht nennt und die Mengenregel dafür offen ist (3
    Zeilen als Sprosse oder 2 je Original).

## Offene Punkte

- LaTeX nicht kompiliert: \rechnung mit \text{oder} und
  &-Ausrichtung (e1, e2, e4), \kreuz nach „\\ “ im Aufgabentext,
  \parabel und \gerade mit leerem Label ungeprüft.
- Konvention gleichungsraster (aufgabe ohne $) mit dem Zusammenbau
  abgleichen.
- Die eigene Sperrliste ist von Hand aus der Mappe gezogen; eine
  vollständige Sperre gehört ins Skript (Befund 4, erledigt v0.5).

## Nachbesserung 2026-09-27

Prüfskript v0.5, bank.md Stand 2026-09-27b. Vorher 3 Abweichungen,
16 Warnungen; nachher 0 Abweichungen, 0 Warnungen in allen fünf
Dateien.

- Sperre: e1-k1-s0-v3 (x − 2)² = 11 wird (x − 6)² = 11 (Original
  2022-OS-K3c).
- Sperre: e1 s8 v1 (x − 2)² = 16 wird (x − 6)² = 16, Lösungen 10
  und 2 (Original 2022-OS-K3c).
- Sperre: e2 s6 v2 x² + 4x = 0 wird x² + 11x = 0, Lösungen 0 und
  −11 (Original 2024-OS-K3d).
- Zone: die 16 Zeilen mit sprosse 1 tragen hoehe grundfall statt
  sprosse.
- e4 Sachaufgaben s8 (Prüfungshöhe ohne P10-Original, Entscheidung
  4) trägt hoehe pruefung, original null, 3 Zeilen.
- Erkennungsschritte gestrichen, weil sie denselben Handgriff wie
  die Vorstufe der Kette verlangen: e1 „Zwei, eine oder keine?“, e2
  „Steht rechts eine Null?“, e3 „Was sind p und q?“, e4 „Welche
  Lösung passt zur Frage?“, je 4 Zeilen; kette_nr und id der
  folgenden Ketten rücken um eins auf.
- Tabelle „Dateien“ auf die neuen Zahlen gebracht; Entscheidungen
  1, 2, 4 und 10 als überholt vermerkt.

## Nachbesserung Render 2026-09-28

Quelle: bau/render-alle/bericht.md, bau/hefte/bericht.md, bau/fokus/bericht.md, bau/layout-befunde.md Punkt 31. Übersicht aller Einträge: bau/render-alle/behoben.md.

- e1-k2-s1-v1, e1-k2-s1-v2, e1-k2-s1-v3, e1-k2-s1-v4, e1-k2-s1-v5, e1-k2-s3-v1, e1-k2-s3-v2, e1-k2-s3-v3, e1-k2-s5-v1, e1-k2-s5-v2, e1-k2-s5-v3, e1-k2-s7-v1, e1-k2-s7-v2, e1-k2-s7-v3, e1-k2-s8-v1, e1-k2-s8-v2, e1-k2-s8-v3, e1-k2-s9-v1, e1-k2-s9-v2, e1-k2-s9-v3, e1-k2-s10-v1, e1-k2-s10-v2, e1-k2-s10-v3, e2-k1-s1-v1, e2-k1-s1-v2, e2-k1-s1-v3, e2-k1-s1-v4, e2-k1-s1-v5, e2-k1-s2-v1, e2-k1-s2-v2, e2-k1-s2-v3, e2-k1-s3-v1, e2-k1-s3-v2, e2-k1-s3-v3, e2-k1-s4-v1, e2-k1-s4-v2, e2-k1-s4-v3, e2-k1-s6-v1, e2-k1-s6-v2, e2-k1-s6-v3, e2-k1-s7-v1, e2-k1-s7-v2, e2-k1-s7-v3, e2-k1-s8-v1, e2-k1-s8-v2, e2-k1-s8-v3, e3-k3-s1-v1, e3-k3-s1-v2, e3-k3-s1-v3, e3-k3-s1-v4, e3-k3-s1-v5, e3-k3-s2-v1, e3-k3-s2-v2, e3-k3-s2-v3, e3-k3-s3-v1, e3-k3-s3-v2, e3-k3-s3-v3, e3-k3-s4-v1, e3-k3-s4-v2, e3-k3-s4-v3, e3-k3-s5-v1, e3-k3-s5-v2, e3-k3-s5-v3, e3-k3-s6-v1, e3-k3-s6-v2, e3-k3-s6-v3, e3-k3-s7-v1, e3-k3-s7-v2, e3-k3-s7-v3, e3-k3-s9-v1, e3-k3-s9-v2, e3-k3-s9-v3, e3-k3-s11-v1, e3-k3-s11-v2, e3-k3-s11-v3 (75): Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`). Änderung: aufgabe in $…$ gesetzt.

Nur diese 75 Zeilen geändert, alle übrigen byte-gleich. `bank-pruef.py quadratische-gleichungen`: 0 Abweichungen. Probe: jede Zeile allein in einem Minimaldokument mit mathblatt.sty (hz-0801/blattbau) gesetzt wie werkzeuge/zusammenbau.py v0.7 (teile_normal, teil_schwach, Lösung in \erg), xelatex ohne Fehler.

## Nachbesserung Gegenlese 2026-09-28

- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- quadratische-gleichungen-e1-k3-s4-v2: Zwischenwert r² ≈ 0,95 führte auf r ≈ 0,97, nicht auf das genannte 0,98 → r² = 3 : π ≈ 0,955; r ≈ 0,98 m (Regel a).
- Prüfskript: Abweichungen 0.

## Duden-Abgleich und Leiterregeln 2026-10-02

- Grundlage: katalog/_abgleich-duden9-kap4.md, Lehrerbeschluss 02.10.2026 (Rückwärts- und Mischsprosse je Kette, krumme Zahlen oben, Gewicht je Einheit); Entwürfe aus eingang/duden9-2026-10-02/neu-quadratische-gleichungen-duden9.jsonl übernommen (Platzhalter durch echte Sprossen ersetzt, „Gib die Lösungsmenge an“ → „Gib die Lösungen an“), fehlende Zeilen selbst gebaut (herkunft „Regel 02.10.“, sympy-nachgerechnet).
- Nummerierung: Die Bankdateien tragen weiter die Folge vor dem Tausch vom 27.09. (e2 = Nullprodukt, e3 = p-q-Formel; Katalog: 2 = p-q-Formel, 3 = Nullprodukt); „Lösungsweg wählen“ steht noch als e3-k3-s16 in der p-q-Kette statt in der Nullprodukt-Kette. Umzug ist Sache des Nachzugs der 48. Neue Zeilen tragen die Nummern der Bankdatei.
- e1 (63 → 75): k2 neu s11 Quadrat erkennen, s15 Rückwärts (reinquadratisch), s16 krumme Zahlen, s17 Gemischt; alte s11–s14 → s12–s14, s18.
- e2 (43 → 49): k1 neu s10 krumme Zahlen (Vorzahl in der Klammer), s11 Rückwärts (Produktform); alte Prüfungshöhe s10 → s12.
- e3 (79 → 102): k3 neu s8 Zahl der Lösungen entscheiden (Katalogsprosse, fehlte), s9 Rückwärts (Zahl wählen), s11 Parameter (GYM), s14 Vieta (Vorrat), s17 krumme Zahlen (dazu die zwei Duden-Zeilen „Normieren mit 0,5 und ¼“), s18 gemischt; s15 (Klammer auflösen) +2 Zeilen (x-Glied hebt sich weg; Zusatzzeilen über der Sollmenge, Warnung erwartet); neue k5 Typ ohne Kette „grafisch lösen mit Normalparabel und Gerade“; Pflicht k5 → k6. Sperre-Altlast e3-k3-s13-v9 (jetzt s19-v9, (x − 3)² − 2 aus 2025-OS-K5b) durch (x − 3)² − 5 und y = −2x + 16 ersetzt.
- e4 (39 → 48): k1 neu s8 krumme Zahlen, s9 Rückwärts, s10 gemischt; Prüfungshöhe s8 → s11.
- e5 neu (74): Einheit 5 [GYM] [Vorrat] – Bruchgleichungen (k1, Vorstufe bis Prüfungshöhe), Wurzelgleichungen (k2), quadratische Ungleichungen (k3), Pflicht fehler und begruenden (k4).
- quelle: neue und verschobene Zeilen auf die Zeile des neuen Katalogstands; Zeilen, die vorher wortgleich passten, mitgezogen.
- Prüfskript: ohne --katalog 0 Abweichungen, 1 Warnung (e3 k3 s15, Zusatzzeilen); mit --katalog 195 → 169 (nur Altlasten: alte quelle-Nummern und nicht wortgleiche sprosse_text unverschobener Zeilen).
- Zeilen gesamt 258 → 382.
