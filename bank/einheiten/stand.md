# Stand: einheiten

Katalog-Commit: cba84caafb6b2346ec42fccf52a733e76ad9b144
(2026-09-25, hz-0801/mathe-nachhilfe, katalog/einheiten.md, aus dem
Kopf von mappen/einheiten.md vom 2026-09-27 06:16 UTC)
Datum: 2026-09-27 07:16 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.3, Endstand 334 Zeilen OK,
0 Abweichungen, 0 Warnungen.

## Dateien

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     46 |        0 |        22 |      23 |        0 |       1 |
| e1    |     87 |       12 |        10 |      51 |        2 |      12 |
| e2    |     59 |        4 |         5 |      36 |        2 |      12 |
| e3    |     68 |        8 |        10 |      36 |        2 |      12 |
| e4    |     74 |        8 |        10 |      42 |        5 |       9 |

Pflicht je Einheit (fehler/begruenden/anwendung/darstellung):
e1 3/3/3/3 · e2 3/3/3/3 · e3 3/3/3/3 · e4 3/3/3/–;
Zone: 1 fehler (Zone-Paar).

## Originale je Einheit

hoehe pruefung (je 2 Zeilen, letzte Sprosse der Sek-I-Kette):
- e1: 2016-OS-K3a
- e2: 2021-OS-B1a
- e3: 2017-OS-K3d
- e4: 2014-OS-K4e

Feld original an einer Kettensprosse (hoehe sprosse, 3 Zeilen):
- e1: 2019-OS-B1b (2 Zeilen), 2026-FOR-B1d (1)
- e2: 2018-OS-B1e, 2025-OS-B1b, 2024-OS-B1a (je 1)
- e3: 2022-OS-B1h (3)
- e4: 2016-OS-K3d (3), 2015-OS-K6d (3)

Sek-II-Prüfungshöhen ohne Feld original (Entscheidung 3):
e1 2025-C-2b, e3 2022-B-2d, e4 2022-B-2b – je 3 Zeilen, Kennung
„(FHR Jahr)“ im Aufgabentext.

## Prüfskript vor der Korrektur (erster Lauf je Datei)

- zone.jsonl: 0 Abweichungen, 0 Warnungen.
- e1.jsonl: 0 Abweichungen, 0 Warnungen. Eigene Kastenprobe: ein
  Treffer („50“ cm Stangenabstand in e1-k3-s5-v1), vor dem Commit
  ersetzt (Faktor 1,6 m, Abstand 40 cm).
- e2.jsonl: 0 Abweichungen, 0 Warnungen.
- e3.jsonl: 1 Abweichung, 0 Warnungen: e3-k5-s6-v3, „2040.5 nicht
  an der Ergebnisstelle“ – Aufzählung nach „m³“ (Befund 5);
  Einheit als „m$^3$“ geschrieben, 2. Lauf 0/0.
- e4.jsonl: 0 Abweichungen, 0 Warnungen.
- Zweimal gescheitert: keine Einheit.

## Entscheidungen

1. Zwei Verfahrensketten in e1, e3, e4: die Sek-I-Kette (Z. 115,
   117, 118) und die Sek-II-Kette (Z. 119, 120, 121), je mit
   eigenem Grundfall (5 Zeilen). Folge je Datei: Erkennungsschritt
   → Sek-I-Kette → Sek-II-Kette → Typen ohne Kette → Pflicht.
2. Genau eine Sprosse hoehe pruefung je Einheit (Gegenprobe), an
   der Sek-I-Kette, weil die P10 die Prüfung des Eintrags ist.
   Gewählt ist jeweils die Zielmarke der Einheit (e1 Faktor mit
   Nachweis, „die anspruchsvollste Marke“; e2 Ankunftszeit; e3
   Dauer aus Menge und Durchsatz; e4 Fehler in fremder Rechnung,
   Niveau III). Die übrigen Originale der Kettenzeile stehen davor
   als eigene Sprosse mit hoehe sprosse, Feld original, 3 Zeilen
   (bank.md „Original an einer Kettensprosse“).
3. Sek-II-Prüfungshöhen (fhr) als höchste Sprosse der Sek-II-Kette
   mit hoehe sprosse, original null, 3 Zeilen: eine Einheit trägt
   nur eine pruefung (Entscheidung 2), und das Prüfskript nimmt
   fhr-Kennungen im Feld original nicht an (Befund 1).
4. Erkennungsschritte: nur „Passt die Angabe?“ (Z. 47) bleibt, als
   k1 in e1 (erste Einheit seines Bereichs). Z. 44, 45, 46, 48,
   49, 50, 51 und 52 entfallen, weil sie die Vorstufe einer Kette
   derselben Einheit wiederholen (Befund 2).
5. Kette Z. 117: „Flächeneinheiten der Größe nach ordnen“ steht im
   Katalog vor dem Grundfall. Eine Sprosse vor dem Grundfall
   bricht die Höhenfolge; sie ist durch den Typ ohne Kette
   „Flächeneinheiten ordnen (mm² bis km², a und ha einordnen)“
   (Z. 26) abgedeckt, die Kette geht von der Vorstufe zum
   Grundfall (Befund 3).
6. Pflicht: fehler und begruenden je 2 Zeilen Sek I und 1 Zeile
   Sek II, als eigene Sprossen mit dem Wortlaut der Sek-I- bzw.
   Sek-II-Klammer der Typenzeile. anwendung und darstellung nur
   Sek I, sprosse_text aus der RLP-Zeile 6 (quelle 6), weil die
   Typenzeilen dafür keinen Wortlaut haben. darstellung: e1
   Stellenwerttafel, e2 drei Schreibweisen einer Dauer, e3
   Einheitentafel; e4 ohne darstellung (kein Darstellungswechsel
   unter den Typen).
7. Typen ohne Kette (hoehe sprosse, 3 Zeilen): e1 Einheiten
   ordnen, Repräsentanten zuordnen, drei bis vier Größen ordnen,
   Faktor bei nichtmetrischen Einheiten, gleiche Einheit addieren;
   e2 Zeiteinheiten ordnen, Startzeit, Fahrplan, sinnvolle
   Einheit; e3 Flächeneinheiten ordnen, Repräsentanten; e4 Dichte
   aus Masse und Volumen, Euro und Cent. Typen, die eine
   Kettensprosse schon abdeckt, stehen nicht doppelt.
8. Namen: kette = Name vor „(Einheit n)“; sprosse_text ohne
   „(Vorstufe)“, „(4×)“ und „(Grundfall, viermal; …)“. Zone: kette
   und sprosse_text = Fertigkeit bis „ – Einheit“, bei Sek-II-Zeilen
   ohne das vorangestellte „Sek II: “ (Befund 9).
9. Zone: alle elf Fertigkeiten, Folge nach erster Verwendung, bei
   gleicher Einheit Folge des Eintrags (Z. 32, 33, 34, 35, 40, 41,
   36, 42, 37, 38, 39). Je Fertigkeit ein Fallstrick; Z. 32 hat
   zwei (Richtung, Nullen). Zone-Paar in f1 (Kommaverschiebung):
   Komma in die falsche Richtung, der erste und häufigste Eintrag
   der Typischen Fehler (Z. 94). Die Zone rechnet ohne
   Einheitenumrechnung (unterrichtsblatt 2.2: kein Themenbegriff).
10. Kastenzahlen: alle mehrstelligen Zahlen und alle Dezimalzahlen
    der Kastenzeilen (Z. 56–90) gemieden, auch 10, 24, 60, 100,
    1000 und 0,5. Umrechnungszahlen stehen in aufgabe als Wort
    („mal hundert“, Ankreuzoption „tausend“); die Kennung „P10“
    zählt nicht als Zahl.
11. Uhrzeiten als Text „14:25 Uhr“. pruef trägt die Stunde nach
    „=“; die Minuten liest das Skript nicht als Ergebnisstelle
    (Befund 4), sie sind im Generator aus Minuten seit Mitternacht
    berechnet. Zeitspannen stehen zusätzlich in Minuten („= 85
    min“), dort prüft pruef die ganze Dauer.
12. Einheiten mit ² oder ³ in einer Aufzählung von Ergebnissen als
    „m$^2$“, sonst „m²“ (Befund 5).
13. Integrale in Worten mit Stammfunktion und Grenzen, ohne
    `\int` (Befund 6).
14. Vergleichszeichen (e1-k2-s9) als Lückensatz mit `\leerfeld`,
    antwort leer; Uhr ohne Grafik in Worten (kein Uhr-Baustein);
    Skala als `\zahlenstrahl`; Stellenwert- und Einheitentafeln,
    Fahrpläne als `\sachtabelle`.
15. Portionen (e3-k1-s9): Division mit Rest („= 6 Rest 50“), pruef
    ganzzahlig. Gebinde: kleinste einzelne Packung, die reicht.
16. Repräsentanten: Erkennungsschritt Z. 47 und Vorstufe Z. 117 als
    Einzelfrage mit drei Optionen; die Typen „Repräsentanten
    zuordnen“ als Zuordnung von drei Gegenständen zu drei Angaben.
17. Die Sek-II-Aufgaben sind so gebaut, dass Schnittstellen und
    Nullstellen ganzzahlig sind und die Flächen aufgehen (4,8; 2,4;
    14,4 Flächeneinheiten); die Gleichung vierten Grades hat je eine
    Lösung im Tor.
18. Operatoren in Du-Form („Weise nach“, „Begründe“, „Berechne“).

## Nachbesserung 2026-09-27

Prüfskript v0.5, bank.md Stand 2026-09-27b; erster Lauf 0
Abweichungen, 0 Warnungen, Endstand ebenso.

- e4-k2-s4 (fhr 2022-B-2b, nicht in der Mappe) trägt jetzt hoehe
  pruefung mit original null, 3 Zeilen (bank.md „Prüfungshöhe ohne
  P10-Original“).
- e1-k3-s5 trägt das Feld original 2025-C-2b (papier C) und e3-k2-s3
  das Feld original 2022-B-2d (papier B), je 3 Zeilen; v0.5 nimmt
  die Kennungen an, weil sie in Abschnitt 2 der Mappe stehen
  (Offener Punkt, Befund 1). hoehe bleibt sprosse (Befund 11).
- Erkennungsschritte: nichts zu streichen; der einzige verbliebene
  (e1-k1, Z. 47) verlangt einen anderen Handgriff als die Vorstufe
  von e1-k2 (Z. 115) und e1-k3 (Z. 119).

## Befunde

1. (erledigt v0.5) Prüfskript: Das Feld original nimmt nur Kennungen nach
   `\d{4}-[A-Z]+-[A-Z]\d+[a-z]` an; fhr-Kennungen wie 2025-C-2b
   ergeben „original unvollständig“ (Probe). bank.md regelt
   Sek-II-Originale nicht („Prüfungshöhe ohne P10-Original: null“
   meint Rahmenlehrplan und Lehrwerk).
2. Katalog: Acht der neun Erkennungsschritte wiederholen eine
   Vorstufe derselben Einheit – Z. 44 und 45 die Vorstufe von
   Z. 115, Z. 46 die von Z. 117, Z. 48 und 49 die von Z. 116,
   Z. 50 und 51 die von Z. 118, Z. 52 die von Z. 119 und Z. 120.
   Der Katalog führt beide; nach bank.md entfallen sie. Z. 47
   deckt sich zusätzlich mit der Vorstufe „passt die Angabe“ von
   Z. 117 (e3) und dem Typ „Repräsentanten zuordnen“ (Z. 24, 26).
3. Katalog Z. 117: Die Kette beginnt mit „Flächeneinheiten der
   Größe nach ordnen“ vor dem Grundfall „(4×)“. Eine Sprosse vor
   dem Grundfall verletzt die Höhenfolge (Prüfskript: hoehe
   grundfall nach höherer Stufe).
4. Prüfskript: In „13:12 Uhr“ gilt nur die Stunde als
   Ergebnisstelle; pruef [13, 12] ergibt „12 nicht an der
   Ergebnisstelle“ (Probe).
5. Prüfskript: Die Einheit zwischen zwei Gliedern einer Aufzählung
   darf nur aus Buchstaben bestehen; „$6$ cm²; $18$ m²“ bricht die
   Aufzählung (Probe; e3 erster Lauf).
6. Prüfskript: `\int` fehlt in der Liste der Standardbefehle und
   gilt als unbekannter Baustein (Probe). Für Sek-II-Einträge mit
   Integralen nötig.
7. Auftrag, Gegenprobe („genau eine Sprosse mit hoehe pruefung je
   Einheit“) gegen bank.md („Prüfungshöhe 2 je Original“): Bei
   mehreren Originalen je Kettenzeile und bei zwei
   Verfahrensketten (Sek I, Sek II) ist offen, welche Kette die
   pruefung trägt und wie viele Zeilen eine Kettensprosse mit zwei
   Originalen hat (hier 3, verteilt 2 + 1).
8. Katalog Z. 121 nennt fhr 2022-B-2b als Prüfungshöhe; die Mappe
   führt das Original nicht („nur außerhalb von Prüfungsform
   genannt, nicht aufgenommen“). Die Sprosse ist ohne
   Originaldaten nach dem Kettentext gebaut.
9. bank.md „Fertigkeit bis zum Doppelpunkt“ passt nicht auf diesen
   Katalog: die Fertigkeitszeilen haben keinen Doppelpunkt, die
   Sek-II-Zeilen beginnen mit „Sek II:“.
10. Gegenprobe „mehrstellige Kastenzahlen“: Der Kasten enthält die
    Umrechnungszahlen selbst (10, 60, 100, 1000, 24). Wörtlich
    gelesen dürfen sie in keiner Aufgabe als Ziffer stehen; das
    zwingt Wörter („mal hundert“). bank.md könnte die
    Umrechnungszahlen eines Einheiten-Eintrags ausnehmen.
11. bank.md gegen Nachbesserung: e1-k3-s5 (2025-C-2b) und e3-k2-s3
    (2022-B-2d) sind Prüfungshöhen mit Original in der Mappe. Nach
    bank.md trügen sie hoehe pruefung mit 2 Zeilen je Original; mit
    3 Zeilen warnt v0.5 („Original 3×, Menge 2“). Die Nachbesserung
    streicht nur Erkennungsschritte; hoehe pruefung und die Streichung
    je einer Variante (v3) stehen zur Entscheidung.
12. Befunde 4, 5 und 6 bestehen unter v0.5 fort (Probe: „13:12 Uhr“
    liest nur 13; „$6$ cm²; $18$ m²“ bricht die Aufzählung; `\int`
    gilt als unbekannter Baustein).

## Offene Punkte

- LaTeX nicht kompiliert. Ungeprüft: `\zahlenstrahl` mit
  xstep=0.1 (Beschriftung der Marken), `\sachtabelle` mit ² und ³
  in der Kopfzeile und mit Uhrzeiten, `\leerfeld` mitten im Satz,
  `\leerzelle` in der Einheitentafel.
- Uhrzeit-Lösungen: pruef prüft nur die Stunde (Entscheidung 11).
- (erledigt v0.5) Sek-II-Sprossen ohne Feld original (Entscheidung
  3); nachtragen, sobald das Prüfskript fhr-Kennungen annimmt.
- Die Zone hat keine Einheitenumrechnung; ob Blatt 0 für diesen
  Eintrag Größen mit Einheit zeigen soll (Fertigkeit Z. 33 nennt
  „null Komma null sechs Meter“), ist zu entscheiden.
