# Stand: lineare-gleichungssysteme

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf der Mappe)
Datum: 2026-09-27 (`date`, 07:21 UTC)
Prüfskript: werkzeuge/bank-pruef.py v0.3 – Endstand 0 Abweichungen,
0 Warnungen in allen sechs Dateien. Der erste Lauf der Zone lief
noch mit v0.2 (v0.3 kam während der Sitzung), alle weiteren mit
v0.3.

## Dateien

    Datei       Zeilen vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      42        0        20      21        0       1
    e1.jsonl        50        8        10      21        5       6
    e2.jsonl        44        4         5      27        2       6
    e3.jsonl        57        8        10      27        6       6
    e4.jsonl        65        8        10      30       11       6
    e5.jsonl        36        4         5      18        3       6
    gesamt         294       32        60     144       27      31

Pflicht je Einheit: fehler 3, begruenden 3. Zone: zehn
Fertigkeiten, je s1 zwei leichte (grundfall), s2 eine mittlere,
s3 ein Fallstrick; Zone-Paar (fehler + Rechenaufgabe) an f5.

## Originale je Einheit

- e1: 2016-OS-K6d (2 Zeilen)
- e2: 2022-OS-K7b (2)
- e3: keines (Zielmarke ohne P10-Original: pruefung, original
  null, 3 Zeilen)
- e4: 2024-OS-K7a, 2024-OS-K7b, 2022-OS-K7a, 2021-OS-K7b (je 2)
- e5: keines im Feld original (Prüfungshöhe nach iqb
  2024MerhoehtAAGLAA122-b: pruefung, original null, 3 Zeilen)
- Sek-II-Ketten e1, e3, e4: iqb 2023MgrundlegendAAGLAA111-a,
  2021MgrundlegendAAGLAA211-b, 2024MerhoehtAAGLAA122-a je als
  höchste Sprosse (3 Zeilen, hoehe pruefung seit der
  Nachbesserung, original null), Kennung nur im Aufgabentext
  (Entscheidung 3 und 4)

## Prüfskript vor der Korrektur

Erster vollständiger Lauf je Datei:

- zone.jsonl: 0 Abweichungen, 0 Warnungen (v0.2). Danach neu
  geschrieben, weil der Auftrag vom 27.09. mehrstellige
  Kastenzahlen (10, 11, 12, 13, 18, 20, 22, 24, 1,00, 1,50, 2,50,
  8,50) in keiner aufgabe erlaubt; der erste Stand hatte 10, 11,
  12, 20 und 2,50. Lauf danach (v0.3): 0, 0. Zwei Commits.
- e1.jsonl: 1 Abweichung, 0 Warnungen – Sperre −2x + y
  (Merkkasten Z. 101) in e1-k3-s3-v1
- e2.jsonl: 9 Abweichungen, 0 Warnungen – Sperre der Terme
  3x + 2y (4×), 3x + 5y (2×), 4x + 3y, 6x + 4y, y = x − 3
- e3.jsonl: 0 Abweichungen, 0 Warnungen
- e4.jsonl: 0 Abweichungen, 0 Warnungen
- e5.jsonl: 1 Abweichung, 0 Warnungen – Sperre x + y + z = 1
  (Merkkasten Z. 90) in e5-k1-s7-v1

Die eigene Kastenzahlprobe (vor jedem Schreiben) fand zusätzlich
vor dem ersten Skriptlauf e1 und e3 je eine, vor dem zweiten Lauf
e2 eine Kastenzahl; alle ersetzt. Keine Einheit scheiterte
zweimal.

## Entscheidungen

1. Kein Erkennungsschritt als eigene Kette: alle acht (Z. 47–54)
   verlangen denselben Handgriff wie eine Vorstufe derselben
   Einheit und entfallen (bank.md; Befund 1). Z. 47 → e1 k1 s0,
   Z. 48 → e1 k2 s0, Z. 49 → e2 k1 s0, Z. 50 → e3 k1 s0 und
   k2 s0, Z. 51 und 52 → e4 k1 s0 (Z. 51 auch k2 s0), Z. 53 und
   54 → e5 k1 s0.
2. e1, e3 und e4 haben je zwei Verfahrensketten (Sek I und
   „…, Sek II“ aus Z. 125–131), jede mit eigenem Grundfall
   (5 Zeilen). Die Pflichtkette heißt nach der ersten.
3. Eine Prüfungshöhe je Einheit (Gegenprobe des Auftrags,
   unterrichtsblatt 2.4 c): Sie steht an der Sek-I-Kette (P10-
   Original oder Zielmarke). Die Prüfungshöhe der Sek-II-Kette
   ist deren höchste Sprosse: hoehe sprosse, 3 Zeilen, merkmal
   „Abitur-Form: …“, sprosse_text wortgleich „Prüfungshöhe: …“.
4. iqb-Originale: Feld original null (Kennungsmuster des Skripts
   und bank.md nur für P10). Kennung im Aufgabentext nach 3.6 als
   „(IQB Jahr grundlegend)“ bzw. „(IQB Jahr erhöht)“.
5. Originale: e4 trägt alle vier Kennungen, die „Prüfungsform
   (P10)“ der Einheit 4 zuordnet (aufstellen, deuten), je 2
   Zeilen in einer Prüfungssprosse. 2016-OS-K6d nur in e1,
   2022-OS-K7b nur in e2 (Kettenzeilen). Nicht aufgenommen:
   2021-OS-K6c, 2019-OS-K7b, 2018-OS-K7c (anderen Einträgen
   zugeordnet), 2021-OS-K7a (nur außerhalb „Prüfungsform“).
6. Pflichtelemente: fehler und begruenden je 3, je Einheit; das
   Sek-II-Muster bekommt je eine eigene Sprosse. Je Fehlermuster
   eine Sprosse mit einer Variante (merkmal je Muster).
   darstellung und anwendung ohne eigene Pflicht: Die Typen der
   Einheiten tragen keinen eigenen Typ dafür; in e1 ist die Kette
   selbst Darstellungswechsel, in e4 selbst Anwendung.
7. Typen ohne Kette: e2 „Bruch als Lösung (Vorrat)“; e3
   „Dezimalzahlen und Brüche“ (nur Brüche, Dezimalzahlen trägt
   k1 s6); e4 „Mischungen und Alter (Vorrat)“, „Probe im Text
   (Rechnung mit den Zahlen der Aufgabe)“, „Bestandteile einer
   Gleichung deuten“. Alle übrigen Typen der Z. 27–31 stehen in
   einer Kette.
8. Zone: Folge nach erster Verwendung, bei gleicher Einheit
   Reihenfolge des Eintrags: f1 Z. 37, f2 Z. 38, f3 Z. 39 (e1),
   f4 Z. 36, f5 Z. 40, f6 Z. 41 (e2), f7 Z. 42 (e4), f8–f10
   Z. 43–45 (e5). kette = Fertigkeit bis „ – “ vor der Einheit
   (Z. 38 und 43–45 haben einen Doppelpunkt im Text). Zone-Paar
   an f5 (Minus vor der Klammer, Typische Fehler Z. 111); auch
   dessen merkmal beginnt mit „Fallstrick:“.
9. Buchstaben: x und y sind die Unbekannten, in jeder Sachaufgabe
   benannt; I, II, III sind Gleichungsnamen wie im Kasten. e4
   Sek II: Anteile u, v, w (x + y + z = 1 ist gesperrt, x und y
   sind in e4 schon die Unbekannten). e4 Prüfung 2024-OS-K7b:
   a/m und b/h wie r/t im Original. e5: a Parameter, t
   Scharparameter (auch in der Prüfungshöhe, wo das Original s
   nimmt).
10. gleichungsraster bei Systemen: aufgabe mit $, Fragewort und
    beiden Gleichungen in einer Zeile.
11. Ankreuzen mit Gleichungen als Optionen (e2 Vorstufe): Optionen
    „Gleichung I“/„Gleichung II“, die Gleichungen stehen davor;
    loesung ohne Ziffer, pruef "".
12. Fehler finden: pruef ist die richtige Lösung; Brüche als
    Zähler und Nenner.
13. Vorstufe e4 (Anzahlen und Beträge markieren): loesung nennt
    zuerst die rechten Seiten, pruef sind diese Zahlen.
14. Grundfall der Sek-II-Ketten mit 5 Zeilen (bank.md), obwohl
    der Katalog „viermal“ sagt.

## Nachbesserung 2026-09-27

- Prüfskript v0.5 vorher und nachher 0 Abweichungen, 0 Warnungen
  in allen sechs Dateien; keine Zeile gestrichen.
- Die Prüfungshöhe der Sek-II-Ketten (e1 k2 s2, e3 k2 s3, e4 k2
  s3, je 3 Zeilen) trägt jetzt hoehe pruefung statt sprosse,
  original bleibt null (bank.md „Mengen je Kette“: Prüfungshöhe
  ohne P10-Original); Entscheidung 3 gilt insoweit nicht mehr.
- Die Prüfkennung „(IQB Jahr grundlegend)“ heißt jetzt „(Abitur
  Jahr GK)“, „(IQB Jahr erhöht)“ jetzt „(Abitur Jahr LK)“ (bank.md,
  Prüfkennung), in e1 k2 s2, e3 k2 s3, e4 k2 s3 und e5 k1 s8 (12
  Zeilen); Entscheidung 4 gilt insoweit nicht mehr.
- Kein Erkennungsschritt zu streichen: alle acht waren schon nach
  Entscheidung 1 entfallen.

## Befunde

1. Katalog: Alle acht Erkennungsschritte (Z. 47–54) decken sich
   mit Vorstufen der Ketten (Z. 125–132); der Katalog führt
   beide.
2. Katalog: e3 hat zwei Vorstufen mit demselben Handgriff
   („gleiche Vorzahl oder Gegenzahl ankreuzen“, Z. 127 und 130);
   beide umgesetzt, mit anderen Zahlen.
3. (erledigt v0.5) Katalog/Auftrag: e1, e3, e4 haben je zwei
   Kettenzeilen mit „Prüfungshöhe“ (Sek I und Sek II); der Auftrag
   erlaubt eine Prüfungssprosse je Einheit, bank.md regelt den
   Fall nicht.
4. (erledigt v0.5, Skriptteil) bank.md/Prüfskript: iqb-Kennungen
   passen nicht ins Muster des Felds original, bank.md nennt nur P10 (papier aus der CSV;
   die Mappe gibt „2021-iqb-ga“). Die Sek-II-Originale gehen dem
   Feld verloren.
5. Prüfskript, Sperre: Das Präfix „I“ klebt an Kastengleichungen
   („Ix+y=7“, „Ix+y=9“, „I3x-y=4“, „Ix+2y=a“); x + y = 7 ohne
   „I:“ davor wird nicht gesperrt. Dazu Einträge ohne Gehalt aus
   Kennungen („111-a“, „-K7a/b“).
6. Prüfskript, Sperre: x + y + z = 1 ist gesperrt, obwohl die
   Sprosse „Summe der Anteile“ genau diese Form meint; die
   Ausnahme greift nur, wenn der Sprossentext die Gleichung
   wörtlich nennt.
7. Auftrag: Die Gegenprobe „mehrstellige Kastenzahlen“ sperrt
   Allerweltszahlen (10, 12, 20, 24) für den ganzen Eintrag; das
   Skript prüft sie nicht, die Sitzung prüfte selbst.
8. Katalog: „Prüfungsform (P10)“ nennt 2024-OS-K7b, 2021-OS-K7b
   und 2016-OS-K6d als Nebentyp „lösen“ (e2), die Kettenzeile
   Einsetzen nur 2022-OS-K7b; hier bei e4 und e1 umgesetzt.
9. bank.md/Prüfskript: v0.5 nimmt iqb-Kennungen der Mappe im Feld
   original an, bank.md setzt eine Prüfungshöhe ohne P10-Original
   aber auf original null, 3 Zeilen. Die vier Prüfungshöhen nach
   iqb (e1 k2 s2, e3 k2 s3, e4 k2 s3, e5 k1 s8) könnten die
   Kennung im Feld tragen, dann mit 2 Zeilen je Original; bank.md
   sagt nicht, ob iqb als Original im Sinn von „Mengen je Kette“
   zählt. Belassen bei null.
10. Prüfskript v0.5, Befunde 5 und 6 bestehen weiter: die Sperre
    liest „Ix+y=7“ mit Präfix und „111-a“, „-K7a/b“ als Terme;
    x + y + z = 1 bleibt gesperrt (Probe am 2026-09-27).

## Offene Punkte

- LaTeX nicht kompiliert: \rechnung mit \text{…} und &=,
  \wertetabelle mit sechs Stellen, \gerade mit Dezimalsteigung und
  Labels I/II.
- e1-k2-s0-v3 „dieselbe Gerade“: zwei \gerade mit gleichen Werten,
  die Labels liegen übereinander – am Render prüfen.
- e1-k1-s5-v3, e1-k3-s1-v1, e1-k3-s3-v1 erzählen ein Ablesen oder
  Zeichnen, ohne es zu verlangen, und haben kein grafik; bei
  k3-s1 würde eine Grafik den Fehler sichtbar machen.
- (erledigt v0.5) Kennung „(IQB Jahr grundlegend/erhöht)“ mit
  Prompt und Zusammenbau abgleichen: bank.md nennt jetzt „(Abitur
  Jahr GK/LK)“.
- Ob Blätter mit Ziel Abitur die Sek-II-Sprosse als Prüfungshöhe
  brauchen (Entscheidung 3).
