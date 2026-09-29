# Stand: brueche-dezimalzahlen

Katalog-Commit: cebfd509ea71ae238b589537bd00b7fc306df06f
(2026-09-28, aus dem Kopf von mappen/brueche-dezimalzahlen.md)
Datum: 2026-09-29 10:55 (date, UTC)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.8,
Vorlage auftrag-eintrag.md 2026-09-29b; Nachzug des Bestands vom
27./28.09. (Commits „brueche-dezimalzahlen: e1" bis „e5",
„muster"). Endstand: 0 Abweichungen, 0 Warnungen, auch mit
`--katalog` gegen die Zeilen der Mappe.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      30         0        14      15        0       1
    e1.jsonl        79         8        10      27       22      12
    e2.jsonl        47         4         5      24        2      12
    e3.jsonl        41         4         5      18        2      12
    e4.jsonl        52         4         5      27        4      12
    e5.jsonl        68         8         5      33       10      12
    gesamt         317        28        44     144       40      61

Pflicht je Einheit: fehler, begruenden, darstellung, anwendung
je 3; Zone fehler 1 (Paar).

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         30      0              0          0
    e1           62      0             17          0
    e2           31      0             16          0
    e3           22      0             19          0
    e4           33      3             16          0
    e5           49      4             15          1

Übernommen heißt: Aufgabe, Lösung und merkmal wortgleich, nur
quelle (Katalog 111–116 → 106–111, 45 → 40), sprosse und id
nachgezogen. Umgeschrieben: Päckchen (je Kette 5), neue
Vorstufentexte (e2–e4, je 4), Pflichtformen und merkmal der
Pflichtsprossen. Entfallen: e5 „Nullen anhängen" v4 (Vorstufe
mit 4 Zeilen wird Sprosse mit 3).

## Originale je Einheit

- e1 k1: 2019-OS-B1c, 2024-OS-B1b, 2014-OS-B1i, 2022-OS-B1a,
  2023-OS-B1d, 2017-OS-B1a, 2021-OS-B1b, 2025-OS-B1c,
  2026-FOR-B1b; e1 k2: 2015-OS-B1h, 2018-OS-B1a
- e2: 2014-OS-B1i
- e3: 2014-OS-B1c
- e4: 2015-OS-B1c, 2018-OS-B1d
- e5: 2023-OS-B1f, 2014-OS-B1h, 2015-OS-B1c, 2018-OS-B1d,
  2020-OS-B1f

## Prüfskript vor der Korrektur

- zone.jsonl: 0 / 0 (unverändert).
- e1–e5: erster Wurf je 0 Abweichungen, 0 Warnungen. Der alte
  Bestand gegen die neue Mappe mit `--katalog`: 311 Abweichungen,
  alle „sprosse_text nicht wortgleich in Zeile quelle"
  (Katalogzeilen verschoben).
- Vor dem Commit nach eigener Kastenprobe geändert
  (Entscheidung 6): e3 k3 s1 v2 und v3, e3 k3 s4 v1, e4 k4 s1
  v3; e1 k4
  s4 v2 Antwortgerüst nachträglich geleert (Commit „e1" zweimal).
  Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 31–37 unverändert.
2. Päckchen: fester Wert e1 k1 „Streifen mit 9 Teilen", e1 k2
   „das Ganze 48", e2 „der Bruch 2/9", e3 „6/11", e4 „Nenner
   100", e5 „0,64"; der feste Wert steht im merkmal.
3. e4 Grundfall nur noch Bruch → Dezimalzahl (Hundertstel), weil
   ein Päckchen genau einen wandernden Wert hat; die Gegenrichtung
   übt e4 s7 (Dezimalzahl → Bruch).
4. e5: „Nullen anhängen" ist jetzt s2 (Sprosse, 3 Zeilen, Bestand
   v1–v3 übernommen); neue Vorstufe s0 „Wo entscheidet es sich?"
   mit pruef "" (Antwort ist ein Stellenname).
5. e4 neue Sprosse s2 „Stellen einzeln gegeben → Dezimalzahl",
   drei Zeilen, zwei mit Null-Stelle; alle folgenden Sprossen um
   eins verschoben.
6. Kastenzahlen: Brüche und Dezimalzahlen mit zwei und mehr
   Ziffern aus dem Merkkasten (7/10, 3/10, 0,25 …) nicht in
   neuen Aufgaben; ganze Zahlen (24, 45, 120) wie bisher frei
   (Befund 2).
7. P1-Serie je Einheit an Kennzeichen: e1 Nenner teilt das Ganze
   nicht, e2 nur ein Teil verändert, e3 fehlendes Stück, e4 Zahl
   der Nachkommastellen, e5 Quadrat kleiner als die Zahl.
8. P8 je Einheit eine Grenzwert-Entscheidung (Mehl, Parkhaus,
   Akku, Laufstrecke, Koffer), Urteil zuerst; Antwortgerüst leer.
9. Urteile je Einheit: P2 „Richtig", Personenaussage Nein,
   Grenzwert Ja – je zwei Ja, ein Nein.

## Befunde

1. Katalog: Erkennungsschritt Z. 39 („Sind alle Teile gleich
   groß?") wiederholt die Vorstufe von e1 k1 und entfällt;
   Z. 40 („Welche Form?") bleibt als e5 k1.
2. Auftrag: Gegenprobe „Mehrstellige Kastenzahlen kommen in
   keiner aufgabe vor" ist für ganze Zahlen hier nicht erfüllbar
   (Kasten nennt 10, 100, 1000, 12, 15, 20, 25 als Gegenstand).
3. Prüfskript: Die Sperre erkennt einzelne Kastenzahlen (Bruch,
   Dezimalzahl) nicht; die Kastenprobe lief von Hand.
4. Katalog Z. 106: Drei Originale der e1-Prüfungshöhe verlangen
   Prozent, das der Eintrag erst für e5 voraussetzt (Z. 36).
5. Katalog Z. 110, 111: 2015-OS-B1c und 2014-OS-B1h verlangen
   Wurzeln und negative Zahlen (Vorrat, Z. 103).
6. Vorlage: kein Baustein für Kästchenfiguren mit mehreren Reihen
   (2021-OS-B1b „3 von 4 Spalten").
7. Prüfskript `--katalog` erwartet eine Katalogdatei; aus der
   Mappe muss sie erst gebaut werden (Zeilennummern).

## Offene Punkte

- Schrittnamen nur in neuen und umgeschriebenen Lösungen; der
  übernommene Bestand zeigt reine Ergebnisse.
- Kein LaTeX-Lauf; die Grafikbausteine sind unverändert.
- Grundvorstellung (Z. 104) steht nicht in der Bank.
