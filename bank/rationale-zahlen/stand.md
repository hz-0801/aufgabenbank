# Stand: rationale-zahlen

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/rationale-zahlen.md)
Datum: 2026-09-30 08:52 (date, UTC)
Grundlage: bank.md 2026-09-30b, werkzeuge/bank-pruef.py v0.9,
Vorlage auftrag-eintrag.md 2026-09-29e; Nachzug 30.09. auf den
Bestand vom 29.09. (Katalog cebfd50; Stand davor in der
Git-Geschichte dieser Datei).
Endstand: 0 Abweichungen, 0 Warnungen, auch mit `--katalog`.

## Nachzug 30.09.

Katalogänderung 30.09. (Kopfzeile des Eintrags): Einheit 2, die
Sprosse „nur das Vorzeichen“ begründet am Pfeilbild statt mit den
Beträgen (Z. 85). Prüfskript mit `--katalog` vor dem Nachzug: 3
Abweichungen, alle e2 s2 „sprosse_text nicht wortgleich in Zeile
85“; 0 Warnungen, Formprobe 0 Hinweise. Danach 0/0.

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         23      0              0          0
    e1           46      0              0          0
    e2           59      0              3          0
    e3           44      0              0          0
    e4           37      0              0          0

Umgeschrieben: e2 k3 s2 v1–v3 (sprosse_text, merkmal, aufgabe,
loesung, grafik); Zahlen und ids blieben, keine id umbenannt.
Zone, muster.md und die Zahlen je Datei sind unverändert.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      23         0        10      12        0       1
    e1.jsonl        46         4         5      21        4      12
    e2.jsonl        62        12         5      30        3      12
    e3.jsonl        44         4         5      18        8       9
    e4.jsonl        37         4         5      15        4       9
    gesamt         212        24        30      96       19      43

Pflicht je Einheit (fehler/begruenden/darstellung/anwendung):
e1 3/3/3/3 · e2 3/3/3/3 · e3 3/3/–/3 · e4 3/3/–/3; Zone fehler 1.

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         23      0              0          0
    e1           36      0             10          0
    e2           49      3             10          0
    e3           32      0             12          0
    e4           28      0              9          0

Übernommen: aufgabe, antwort, loesung, pruef wortgleich; nachgezogen
quelle (87–90 → 84–87, 36 → 35), sprosse, id, bei e3 s0 der längere
Vorstufentext, bei der Prüfungshöhe sprosse_text und merkmal.
Umgeschrieben: Päckchen (je Kette 5), Pflichtformen, e2 s5 v1–v2
(Gerüst), e3 s4 (Teilprodukt-Zeile). Neu: e2 s2 „nur das
Vorzeichen“ (3 Zeilen), die Sprossen danach rücken um eins.

## Originale je Einheit

- e1: 2015-OS-B1b, 2014-OS-B1h
- e2: keins; Prüfungshöhe ohne Original, original null (k3 s9)
- e3: 2021-OS-B1g, 2016-OS-B1i, 2026-FOR-B1g, 2015-OS-B1g
- e4: 2016-OS-K2d, 2017-OS-K2a

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 116 Abweichungen
  (e1 25, e2 34, e3 32, e4 25), alle „sprosse_text nicht wortgleich
  in Zeile quelle“ (Katalogzeilen verschoben); zone 0.
- Erster Wurf je Einheit: e1–e4 je 0 Abweichungen, 0 Warnungen.
  Vor dem Commit von e1 eine Urteilszeile getauscht (e1 k5 s4 v3
  von Ja auf Nein, Ausgleich der Urteile). Keine Einheit scheiterte.

## Entscheidungen

1. Prüfungshöhe mit „daneben …“: alle Originale einer Kette in einer
   Sprosse (die letzte), je Original 2 Zeilen; sprosse_text ist der
   ganze Prüfungsabschnitt der Kettenzeile bis zum Satzende (e2 ohne
   den Zusatzsatz). Bisher je Original eine Sprosse.
2. Päckchen, fester Wert im merkmal: e1 die Zahl $-5$, e2 der Start
   $-7$, e3 der Faktor $-6$, e4 der Startwert $-60$ €.
3. Gerüst „Vorzeichen: __ Betrag: __ Ergebnis: __“ in e3 s1 v1–v2
   (Päckchen) und e2 s5 v1–v2; die Lösung trägt dieselben Wörter.
4. e2 s2 „nur das Vorzeichen“ (seit 30.09.): Ankreuzen mit zwei
   Optionen; der Schüler zeichnet den Pfeil vom Start auf einer
   Zahlengeraden (`\zahlenstrahl`, Start markiert, Bereich so, dass
   Start, Null und Pfeilende liegen); die Lösung nennt die Option
   zuerst, dann das Pfeilbild (Ende, reicht über die Null oder
   nicht); pruef "". Die Vorlage hat keinen Pfeil-Baustein für den
   Zahlenstrahl, darum zeichnet der Schüler; die Zahlen blieben.
5. P6 steht, wo der Bestand eine Personenaussage hatte (e1, e2);
   e3 und e4 bekamen eine neue (Vorzeichenregel „nicht
   entscheidbar“, Temperaturunterschied); dort wich die
   Begründungszeile ohne Form.
6. P1-Kennzeichen: e1 Lage zwischen den Zahlen, e2 Richtung auf der
   Zahlengeraden, e3 Vorzeichen, e4 Vorzeichen der Klammer.
7. Urteile der Pflichtzeilen: e1 1 Ja / 2 Nein, e2 2 Ja / 1 Nein, e3 2 Ja /
   1 Nein, e4 3 Ja / 2 Nein (P2 „Richtig“ als Ja gezählt).
8. Musterbeispiele je Kette mit eigenen Zahlen außerhalb von
   Päckchen und Bestand.

## Befunde

1. Katalog Z. 33–35 und Vorstufen: „Pfeil an der Zahlengeraden“,
   „Wie viele Minuszeichen?“, „Startwert und Änderung“ stehen als
   Vorstufe; die Erkennungsschritte davon sind entfallen (wie 27.09.).
2. Katalog Z. 85: Die Sprosse „nur das Vorzeichen“ verlangte das
   Betragsdenken der Typ-Zeile „Beträge“ vor ihrer Zeit; seit 30.09.
   begründet sie am Pfeilbild – der Befund vom 29.09. ist damit
   erledigt.
5. Bausteine: Ein Pfeil an der Zahlengeraden (Start, Länge,
   Richtung) fehlt in `_bausteine.md`; Pfeilbilder (e2 s0, s2) sind
   darum nur als Zeichenauftrag des Schülers möglich, eine
   Lösungsgrafik mit dem Pfeil gibt es nicht.
3. Prüfskript: Serie P1 und Aussagenserie P4 werden nur über
   pflicht erkannt; eine P2-Vorlage mit „Richtig.“ braucht pruef ""
   ohne eigene Regel (geht über pflicht fehler).
4. bank.md, Gerüst rationale-zahlen: „die ersten zwei Varianten“ ist
   beim Päckchen (fünf Zeilen) knapp; offen, ob v3–v5 es ohne Gerüst
   üben sollen oder ob das Blatt das Gerüst mitzieht.

## Offene Punkte

- Kein LaTeX-Lauf: `\kreuz` mit längeren Optionen in e2 s2 und die
  Serien mit `\\` ungerendert.
- Schrittnamen nur in neuen und umgeschriebenen Lösungen; der
  übernommene Bestand zeigt reine Ergebnisse.
- e4 Prüfungshöhe 2016-OS-K2d ist Niveau III (Vorrat, Z. 87).
