# Stand: zuordnungen

Katalog-Commit: de503c9cea3976774daeb6c514adb85829d8df2e
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py, am Ende 0 Abweichungen,
2 Warnungen

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        0 |        10 |      12 |        0 |       1 |    23 |
| e1    |        8 |        10 |      32 |        2 |      12 |    64 |
| e2    |       16 |         5 |      24 |        3 |      12 |    60 |
| e3    |        4 |         5 |      15 |        2 |      12 |    38 |
| e4    |       12 |        10 |      35 |        6 |      12 |    75 |
| ges.  |       40 |        40 |     118 |       13 |      49 |   260 |

## Originale je Einheit

- e1: 2025-OS-K7a (Darstellen s7), 2021-OS-K6b (pruefung)
- e2: keins (Prüfungshöhe mit original null)
- e3: 2014-GYM-B1c (pruefung)
- e4: 2014-OS-K4c, 2014-OS-K4d, 2024-OS-K2d, 2015-OS-K4c
  (Rate s5); 2014-OS-K2c, 2015-OS-K3c, 2024-OS-K6c (pruefung)

## Prüfskript vor der Korrektur

- zone: 0 Abweichungen, 0 Warnungen
- e1: 0 Abweichungen, 1 Warnung (Menge sprosse = 3 bei Original)
- e2: 0 Abweichungen, 0 Warnungen
- e3: 0 Abweichungen, 0 Warnungen
- e4: 0 Abweichungen, 1 Warnung (Menge sprosse = 3 bei Originalen)
- Gegenprobe von Hand: 2 Kastenzahlen in aufgabe (e1 „24“,
  e3 „12“), je eine Zeile korrigiert.

## Entscheidungen

1. Die Zone-Fertigkeiten haben keinen Doppelpunkt; kette und
   sprosse_text sind der Text bis „ – Einheit“.
2. Zone-Reihenfolge nach erster Verwendung: Punkte (Einheit 1)
   zuerst, danach die Fertigkeiten ab Einheit 2 in Eintragsfolge.
3. Einheit 1 hat zwei Verfahrensketten; pruefung trägt die letzte
   (Achseneinteilung), die Prüfungshöhe von Darstellen steht als
   hoehe sprosse mit original 2025-OS-K7a, 2 Zeilen (2.4 c).
4. Einheit 4 ebenso: Erkennen endet auf hoehe sprosse mit
   original null, 3 Zeilen; pruefung trägt Rate.
5. Die Kosten- und Geschwindigkeits-Originale der Einheit 4
   stehen an Rate s5 „Einheit umrechnen“, je 2 Zeilen, ohne
   Zeilen ohne Original (8 statt 3).
6. sprosse_text ohne die Marken „(4×)“ und „(Vorstufe …)“;
   Erkennungsschritte heißen nach dem Teil vor dem Gedankenstrich.
7. Pflichtelemente als s1 fehler, s2 begruenden, s3 darstellung,
   s4 anwendung; sprosse_text für darstellung und anwendung aus
   der Zeile der Lerneinheit, da die Typenzeile sie nicht nennt.
8. Die Vorstufe Achseneinteilung beschreibt die Achse im Text,
   da kein Baustein eine Achse mit wählbarem Kästchenwert zeigt.
9. Bei Uhrzeit-Ergebnissen trägt pruef nur Dauer in h und min;
   die Uhrzeit selbst prüft das Skript nicht.

## Befunde

1. Katalog: Der Erkennungsschritt „Je mehr …, desto …?“ (Z. 37)
   verlangt denselben Handgriff wie die Vorstufen von
   Antiproportional (Z. 94) und Erkennen (Z. 95); er entfällt.
2. Katalog: Die drei Originale von „Proportionale Zuordnung
   Dreisatz“ (Z. 99) haben keine Kennung in der Prüfungsform;
   die Mappe nimmt sie nicht auf, Einheit 2 hat kein Original.
3. Prüfskript: Ein Original an einer Kettensprosse (hoehe
   sprosse) löst „Menge sprosse = 3“ aus, obwohl bank.md 2 je
   Original vorsieht; die Originalmenge prüft es nur bei pruefung.
4. Prüfskript: Die Sperrprobe fängt einzelne mehrstellige
   Kastenzahlen nicht (24 und 12 standen in aufgabe, 0 gemeldet),
   die Gegenprobe des Auftrags verlangt es.
5. Katalog: Die Rate-Kette hat keine Sprosse für Kosten mit
   Zwischengröße (2014-OS-K4c, K4d), obwohl die Zielmarke K4d
   als schwerste Form nennt.
6. bank.md regelt nicht, wie kette der Zone gebildet wird, wenn
   die Fertigkeit keinen Doppelpunkt trägt.

## Offene Punkte

1. Die Grafiken sind nicht kompiliert; ob ystep die Kästchen so
   beschriftet, wie die Aufgaben es sagen, ist ungeprüft.
2. Uhrzeiten in den Lösungen von Rate s6 und der Anwendung sind
   nur von Hand nachgerechnet.
