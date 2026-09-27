# Stand: rationale-zahlen

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(hz-0801/mathe-nachhilfe, katalog/rationale-zahlen.md, laut Kopf der
Mappe mappen/rationale-zahlen.md vom 2026-09-27 06:15 UTC)
Datum: 2026-09-27 07:14 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.3, Endstand 0 Abweichungen,
0 Warnungen in allen Dateien.

## Dateien

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      23         –        10      12        –       1
    e1.jsonl        46         4         5      21        4      12
    e2.jsonl        59        12         5      27        3      12
    e3.jsonl        44         4         5      18        8       9
    e4.jsonl        37         4         5      15        4       9
    gesamt         209

Pflicht je Einheit (fehler/begruenden/anwendung/darstellung):
e1 3/3/3/3 · e2 3/3/3/3 · e3 3/3/3/– · e4 3/3/3/–;
Zone: 1 fehler (Zone-Paar). e2 vorstufe: 8 Zeilen aus zwei
Erkennungsschritten, 4 Zeilen Vorstufe der Kette.

Ketten je Datei (kette_nr: Name):
- zone: f1 Natürliche Zahlen … im Kopf (Einmaleins) · f2
  Zahlenstrahl · f3 Dezimalzahlen und Brüche … · f4 Punkt vor
  Strich und Klammern mit natürlichen Zahlen · f5 Wert eines Terms
  mit Platzhalter berechnen …
- e1: k1 Ordnen · k2 Mitte zweier Zahlen · k3 runden · k4 Punkte in
  vier Quadranten · k5 Ordnen (Pflicht)
- e2: k1 Vorzeichen oder Rechenzeichen? · k2 Zeichen
  zusammenfassen · k3 Addieren/Subtrahieren · k4 Beträge … · k5
  Dezimalzahlen und Brüche · k6 Umkehrung … · k7
  Addieren/Subtrahieren (Pflicht)
- e3: k1 Multiplizieren/Dividieren · k2 Vorzeichenregel als Aussage
  prüfen · k3 Multiplizieren/Dividieren (Pflicht)
- e4: k1 Terme und Sachaufgaben · k2 Rechenvorteile … · k3 Terme
  und Sachaufgaben (Pflicht)

## Originale je Einheit (je 2 Zeilen, verfremdet)

- e1: 2015-OS-B1b, 2014-OS-B1h
- e2: keines; Prüfungshöhe ohne P10-Original, original null,
  3 Zeilen
- e3: 2021-OS-B1g, 2016-OS-B1i, 2026-FOR-B1g, 2015-OS-B1g
- e4: 2016-OS-K2d, 2017-OS-K2a

## Prüfskript vor der Korrektur (erster Lauf je Datei)

- zone.jsonl: 0 Abweichungen, 0 Warnungen.
- e1.jsonl: 0 Abweichungen, 0 Warnungen.
- e2.jsonl: 0 Abweichungen, 0 Warnungen.
- e3.jsonl: 0 Abweichungen, 0 Warnungen.
- e4.jsonl: 0 Abweichungen, 0 Warnungen.

Keine Einheit ist am Prüfskript gescheitert.

Eigene Probe „Kastenzahlen“ (Entscheidung 11), erster Lauf nach
e4: 54 Zeilen mit einer mehrstelligen Zahl aus dem Merkkasten in
aufgabe (zone 5, e1 8, e2 12, e3 6, e4 23). zone und e1–e3 waren
da schon committet; korrigiert in einem eigenen Commit
(„rationale-zahlen: zone, e1–e3 ohne Kastenzahlen“), e4 vor seinem
Commit. Ein Treffer entstand bei der Korrektur neu und wurde vor
dem Commit ersetzt. Endstand 0.

Unabhängig nachgerechnet: 53 reine Rechenaufgaben aus dem
Aufgabentext gegen pruef, 0 Differenzen; Sachaufgaben,
Zeichenaufgaben und die zwei Preisaufgaben von Hand.

## Entscheidungen

1. Zone, kette und sprosse_text: Fertigkeit bis zum Doppelpunkt
   (nur Z. 29 hat einen: „Zahlenstrahl“); ohne Doppelpunkt bis vor
   „ – Einheit“ bzw. „ – alle Einheiten“. Reihenfolge wie im
   Eintrag (Einheit 1, 1, 2, 3, 3).
2. Zone, Fallstricke rückwärts geplant: f1 Subtrahieren über den
   Zehner (e2, Beträge subtrahieren); f2 Schrittweite 0,25 statt
   0,1 (e1, Brüche eintragen); f3 Komma unter Komma (e2
   Dezimalzahlen) und Bruch mal ganze Zahl (Z. 30, Einheit 3); f4 von
   links nach rechts gerechnet (e3 Punkt vor Strich, alle drei
   Termwert-Originale); f5 „4x“ als Ziffernfolge (e3, e4
   Termwert). Die mittlere Aufgabe hat Dezimalzahl statt negativer
   Zahl, weil die Zone keinen Begriff des Themas nennt.
3. Zone-Paar bei f4 (Punkt vor Strich): Einheit 3 und 4 und die
   drei Termwert-Originale hängen daran.
4. Von fünf Erkennungsschritten stehen zwei (Z. 34 und 36, beide
   in e2). Drei entfallen nach bank.md, weil sie denselben Handgriff
   verlangen wie die Vorstufe ihrer Kette (Befund 1).
5. Erkennungsschritt „Zeichen zusammenfassen“: Die Lösung ist ein
   Term ohne Klammern ($6 + 5$), keine Ergebniszahl. pruef ist die
   erste Zahl der Lösung, weil das Skript pruef verlangt, sobald
   die Lösung Ziffern hat (Befund 4). „Vorzeichen oder
   Rechenzeichen?“ antwortet mit V/R, pruef leer.
6. „(4×)“ im Katalog (Z. 87–90, auch an „Zeichen zusammenfassen
   gemischt“) ist Blattmenge; in der Bank gilt Grundfall 5, jede
   weitere Sprosse 3. sprosse_text ohne „(4×)“ und ohne
   „(Vorstufe)“.
7. Prüfungshöhe mit „daneben …“: eine eigene Sprosse je Original,
   alle mit hoehe pruefung, je 2 Zeilen; sprosse_text ist der
   Satzteil des Originals.
8. e1: 2014-OS-B1c (Zielmarke, Original bei brueche-dezimalzahlen)
   nicht aufgenommen; die Sprossenzeile Z. 87 nennt es nicht, und
   es hat keine negative Zahl. 2014-OS-B1h ohne Wurzel verfremdet
   („hier nur der negative Teil“, Z. 87); Falle bleibt: negativer
   Bruch gegen nahe negative Dezimalzahl.
9. e2: Prüfungshöhe ohne P10-Original (Z. 88, 96): hoehe pruefung,
   original null, 3 Zeilen, wie bank.md es verlangt; Aufgabe ist
   die Klammer eines Terms mit eingesetzter negativer Zahl.
10. Typen ohne Kette: e1 Mitte zweier Zahlen, runden, Punkte in
    vier Quadranten (nur ganze Koordinaten, Kette in
    symmetrie-abbildungen); e2 Beträge, Dezimalzahlen und Brüche
    (nur Brüche, die Kette trägt die Dezimalzahlen), Umkehrung;
    e3 Vorzeichenregel als Aussage prüfen; e4 Rechenvorteile.
    Durch Kette oder Prüfungshöhe gedeckt: Zahl zu Bedingung (e1
    Prüfungshöhe), Termwert mit Klammer (e3 2026-FOR-B1g, e4
    Sprosse), Kontostand, Temperatur- und Höhenunterschied,
    Ausgangswert aus Differenz, Preiskombination (e4). Die
    Plusklammer (e4) steht nicht eigens; die Kette hat nur die
    Minusklammer.
11. Gegenprobe „Kastenzahlen“ streng gelesen wie in pythagoras und
    binomische-formeln: keine mehrstellige Zahl aus dem Merkkasten
    (1,5; 10; 11; 12; 13; 14; 16; 20; 24; 25; 32) in einer
    aufgabe, auch nicht mit anderem Vorzeichen; einzelne Ziffern
    frei (bank.md). „P10“ der Prüfkennung ausgenommen. Eigene
    Probe, weil die Sperrprobe nur Terme und Paare fängt.
12. Pflicht darstellung: e1 der Typ „Situation ↔ Zahl“ (Z. 21) in
    beide Richtungen; e2 Pfeilbild ↔ Term (LISUM, Z. 8). e3 und e4
    ohne darstellung, ihre Typen tragen keinen Wechsel.
13. Pflicht anwendung mit sprosse_text aus den amtlichen Zeilen:
    e1 und e4 RLP Z. 6 („Vergleichen und Ordnen …“, „Addition als
    Zusammenfassung …“), e2 RLP Z. 6 („… Änderung eines
    Zustandes“), e3 LISUM Z. 8 („Einfluss der Vorzeichen an
    Geldfluss …“). Fünf Anwendungen enden mit einer Entscheidung
    im Kontext (Pfütze, Kühlkammer, Buch, Tauchgrenze, Kühllaster).
14. Fehler finden: e4 (Minusklammer) senkrecht mit `\rechnung`,
    weil es eine Umformung ist; e1–e3 als Zeile.
15. Runden negativer Zahlen am Betrag (−12,85 → −13); pruef
    ungerundet, das Skript rundet vom Betrag weg, das stimmt
    überein.
16. Zahlengerade als `\zahlenstrahl` mit negativem xmin;
    Beschriften mit `{0/0}` (nur die Null markiert),
    Pfeilbild-Aufgaben mit den Labels „Start“ und „Ende“.
17. Zeichenaufgaben ohne pruef (erlaubt), außer Zone f2 v2, deren
    Lösung eine Zahl ist.
18. Preisaufgaben (2016-OS-K2d) mit eigenen Preislisten: Tierpark
    mit Großeltern-Enkel-Karte Mo–Fr (64 € gegen 76, 80, 84 €) und
    Freizeitbad mit Gruppenkarte am Wochenende (38 € gegen 43,
    51 €). Fallen wie im Original: Familienkarte reflexhaft, freies
    Kleinkind mitgezählt, Tagesbedingung.

## Befunde

1. Katalog, Erkennungsschritte gegen Vorstufen derselben Einheit
   (Katalogbefund nach bank.md): „Pfeil an der Zahlengeraden“
   (Z. 35) = Vorstufe „Pfeil an der Zahlengeraden“ (Z. 88); „Wie
   viele Minuszeichen?“ (Z. 37) = Vorstufe „Vorzeichen ankreuzen
   ohne Rechnung“ (Z. 89); „Was ist der Startwert, was die
   Änderung?“ (Z. 38) = Vorstufe „Startwert und Änderung
   markieren“ (Z. 90). Die Bank führt nur die Vorstufen.
2. Auftrag, Gegenprobe: „Die Kastenzahlen … kommen in keiner
   aufgabe vor“ ist wörtlich strenger als bank.md und die
   Sperrprobe (Terme, Paare). Die Einträge lesen es verschieden
   (streng: pythagoras, binomische-formeln, dieser; als
   Kastenterme: quadratische-funktionen). bank.md sollte es
   festlegen, das Prüfskript es dann prüfen.
3. Katalog Z. 22 nennt den Typ „Dezimalzahlen und Brüche“, die
   Kette Z. 88 nur „Dezimalzahlen“; die Brüche mit Vorzeichen
   stehen deshalb als Typ ohne Kette (Entscheidung 10).
4. Prüfskript: Eine Lösung, die ein Term ist (Erkennungsschritt
   „ohne Klammern aufschreiben“), braucht pruef, obwohl es keine
   Ergebniszahl gibt. Wie bei Ankreuzen sollte pruef "" erlaubt
   sein, wenn die Lösung ein Term ist.
5. Katalog Z. 87 führt 2014-OS-B1h als Prüfungshöhe von Einheit 1,
   das Original liegt bei brueche-dezimalzahlen. Beide Bänke
   verfremden es; beim Blattbau auf Beinahe-Doppel achten.

## Offene Punkte

- Kein LaTeX-Lauf: `\zahlenstrahl` mit negativem Bereich, `{0/0}`
  und Textlabels („Start“, „Ende“) ist ungerendert. Beschriftet die
  Vorlage die Striche selbst, sind die Beschriften-Aufgaben (e1 k1
  s0) auf dem Blatt schon gelöst; dann braucht es einen Strahl ohne
  Zahlen.
- `\kreuz{plus} \kreuz{minus}` nebeneinander (e3 Vorstufe) und die
  `\rechnung` im Fließtext (e4 Fehler finden) ungerendert.
- e4 Prüfungshöhe 2016-OS-K2d ist Niveau III (Vorrat, Z. 90); beim
  Blattbau als Zielmarke setzen.

## Nachbesserung 2026-09-27

Prüfskript v0.5, bank.md Stand 2026-09-27b. Vorher und nachher 0
Abweichungen, 0 Warnungen in allen fünf Dateien; keine Zeile
geändert oder gestrichen.

- Prüfungshöhe ohne Original: e2 s8 steht schon als hoehe pruefung,
  original null, 3 Zeilen (Entscheidung 9); nichts nachzuziehen.
- Erkennungsschritte: die zwei verbliebenen in e2 („Vorzeichen oder
  Rechenzeichen?“, „Zeichen zusammenfassen“) verlangen einen
  anderen Handgriff als die Vorstufe „Pfeil an der Zahlengeraden“;
  sie bleiben. Die drei doppelten sind schon gestrichen (Befund 1).
- Befund 4 gegen v0.5 geprüft: pruef "" ist weiter nur bei einer
  Lösung ohne Ziffer erlaubt; der Befund bleibt offen.
