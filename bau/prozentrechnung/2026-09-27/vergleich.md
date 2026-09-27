# Prüfstein prozentrechnung – Bank-Blatt gegen Muster

Stand 2026-09-27, zusammenbau v0.1, Bank beim Commit mit
„prozentrechnung: Nachbesserung auf bank.md 2026-09-27b“
(f90893f, bringt das Zone-Paar).

## Läufe

    lernblatt/          zusammenbau.py prozentrechnung
    fokus-prozentsatz/  zusammenbau.py prozentrechnung
                          --fokus Prozentsatz
    schwach-7/          zusammenbau.py prozentrechnung
                          --schwach --klasse 7

Muster (hz-0801/mathe-nachhilfe, blaetter/):

    Lernblatt  prozentrechnung/2026-09-22/src/ blatt0_a, e1_a–e5_a
    Fokus      prozentrechnung/2026-09-24/src/fokus_a.tex; Zone ab
               „\einheitenkopf*{Blatt 0“, Fokus ab
               „\einheitenkopf*{Fokus“ (Vorspann nicht gezählt)
    schwach    testlauf-2026-09-26/3-prozent-7-schwach/ zone_a,
               e1_a–e4_a (dort e1 = Katalog-Einheit 2 usw.)

Fokus-Kette: fokus_a.tex übt „Fokus · Prozentsatz berechnen“
(Zeile 91), also die Bank-Kette „Prozentsatz“ (e2 k3, dazu die
gleichnamige Pflichtkette e2 k5).

## Zählweise

zaehl.py in diesem Ordner, je Aufgabendatei, Kommentarzeilen
ausgenommen außer bei „Zeilen“:

- Hauptnummern: `\begin{aufgabe}`
- Teilaufgaben: `\teil \steil \tz \stz \swz \swa \swfrage \gl
  \sgl` (im Muster zählen auch die `\tz`-Felder unter einer
  `\streifenreihe`)
- Merkkästen: `\uebersichtskasten`
- Grafiken: Streifen-Familie, `\sachtabelle`, `dreisatz`, `ksys`,
  Bruch-, Zahlenstrahl- und Diagrammbausteine
- Zeilen: alle Zeilen der Datei; beim Bank-Blatt in Klammern ohne
  die `%`-Zeilen (TODO-Kommentare)

Angabe je Zelle: Bank / Muster.

## Lernblatt

    Blatt   Hauptnr.  Teilaufg.  Kästen  Grafiken  Zeilen
    blatt0   8 / 7     14 / 34   0 / 0    2 / 5     77 (60) / 119
    e1       3 / 7     14 / 31   0 / 0    4 / 4     49 (40) / 93
    e2       5 / 8     17 / 30   0 / 0    3 / 1     65 (52) / 74
    e3       3 / 7     15 / 28   0 / 0    2 / 2     48 (39) / 71
    e4       3 / 7     12 / 26   0 / 0    2 / 1     45 (36) / 67
    e5       3 / 9     16 / 36   0 / 0    0 / 0     43 (34) / 89
    Summe   25 / 45    88 / 185  0 / 0   13 / 13   327 (261) / 513

Drei Unterschiede im Aufbau:

1. Grundfall einmal statt vier- bis fünfmal. Bank
   lernblatt/e2_a.tex:33 setzt „17 von 100“ als einzige
   Grundfall-Teilaufgabe (Regel „je Sprosse Variante 1“); Muster
   e2_a.tex:26–27 hat vier („19, 7, 64, 90 von 100“), wie
   unterrichtsblatt 2.3 b verlangt. Dasselbe trifft die
   Erkennungsschritte: Bank e2_a.tex:9 „Was ist das Ganze?“ mit
   einer Teilaufgabe, Muster e2_a.tex:5 mit fünf (2.3 a: vier
   bis fünf).
2. Eine Kette, eine Hauptnummer. Bank e2_a.tex:27 fasst die
   ganze Kette „Prozentsatz“ (Vorstufe bis Prüfungshöhe, zehn
   Teilaufgaben) in Nr. 14; Muster zerlegt sie nach Form in
   „am Streifen“ (e2_a.tex:15), „rechnen“ (:23) und „aus dem
   Sachtext“ (:44), je mit eigenem Titel.
3. Pflichtelemente in einer Nummer. Bank e2_a.tex:55 setzt
   Fehler finden, Begründen, Darstellungswechsel und Anwendung
   als a)–d) in Nr. 16; Muster hat je eine Hauptnummer
   (e2_a.tex:53, :61, :68), wie 2.3 c es fordert („eine
   Hauptnummer, eine Fertigkeit, eine Antwortform“).

## Fokus Prozentsatz

    Blatt   Hauptnr.  Teilaufg.  Kästen  Grafiken  Zeilen
    Zone     4 / 5      8 / 15   0 / 0    2 / 6     43 (34) / 71
    Fokus    6 / 11    46 / 39   0 / 0    7 / 10   110 (95) / 116
    Summe   10 / 16    54 / 54   0 / 0    9 / 16   153 (129) / 187

Drei Unterschiede im Aufbau:

1. Erkennungsschritte und Umkehrung fehlen. Bank
   fokus-prozentsatz/e2_a.tex:9 beginnt direkt mit der Kette;
   Muster fokus_a.tex:93 („Was ist das Ganze?“), :108 („Streifen
   einteilen“) und :166 (Umkehrung) stehen davor bzw. dazwischen.
   Ursache: Regel „andere Ketten entfallen“; 2.5 verlangt die
   Vorstufe im Fokus.
2. Teilung nach Anzahl statt nach Form. Bank teilt die 34
   Zeilen der Kette an Sprossengrenzen nach dem Maß aus 2.3 g:
   Nr. 5 nur die vier Streifen der Vorstufe (e2_a.tex:9), Nr. 6
   Grundfall bis Taschenrechner (:29), Nr. 7 Runden bis Rabatt
   (:47). Muster teilt nach Darstellung: Zehnerstreifen
   (fokus_a.tex:122), Zwanzigerstreifen (:132), Erweitern (:140),
   Taschenrechner (:154).
3. Prüfungshöhe gebündelt. Bank Nr. 8 (e2_a.tex:63) enthält
   alle zehn P10-Varianten hintereinander (etwa :67–68, zweimal
   P10 2023); Muster verteilt drei P10-Teilaufgaben auf
   Sachtext und Anwendung (fokus_a.tex:178, :202, :203).

## schwach, Klasse 7

    Bank/Muster  HN       TA        MK     Gr        Zeilen
    blatt0/zone   8 / 11   14 / 49  0 / 0   2 / 44   69 (40) / 133
    e1/–          3 / –    19 / –   1 / –   8 / –    49 (35) / –
    e2/e1         5 / 12   22 / 41  1 / 1   3 / 21   67 (44) / 114
    e3/e2         3 / 10   20 / 29  1 / 1   6 / 18   51 (36) / 111
    e4/e3         3 / 8    17 / 25  1 / 1   2 / 13   50 (33) / 96
    e5/e4         3 / 13   21 / 41  1 / 1   0 / 18   58 (39) / 139
    Summe        25 / 54  113/185   5 / 4  21 / 114 344 (227) / 593

HN Hauptnummern, TA Teilaufgaben, MK Merkkästen, Gr Grafiken.

Drei Unterschiede im Aufbau:

1. Schnitt der Zeitachse. Bank schwach-7/e1_a.tex:3–4 setzt
   „Einheit 1 von 5 · Prozente als Anteile“ mit der Zeitmarke
   „kennst du wahrscheinlich seit Klasse 6“ auf das Blatt; im
   Muster ist Einheit 1 Prozentsatz (e1_a.tex:2, „von 4“), der
   Stoff von Katalog-Einheit 1 steht als Fertigkeiten in der
   Zone (zone_a.tex:5, :14). v0.1 schneidet nicht (1.5).
2. Darstellung neben der Rechnung fehlt. Bank e2_a.tex:26
   `\swz{…}{}` mit leerer rechter Spalte (TODO darüber); Muster
   e1_a.tex:41 `\swz{5 von 100 Losen gewinnen.}{\streifen…}`.
   Die Bank führt keine Schwach-Darstellung je Zeile; nur Zeilen
   mit grafik bekommen eine (Bank 21, Muster 114 Grafiken).
3. Gliederung der Kette. Bank e2_a.tex:23 eine Hauptnummer mit
   15 Teilaufgaben a)–o), Päckchen samt Erklärzeile (:35)
   mitten darin; Muster e1_a.tex:26–76 sieben Hauptnummern unter
   vier `\verfahren`-Zeilen, das Päckchen mit Erklärzeile als
   eigene Nummer (:37–45).

## Was die Zahlen sagen

Die Bank liefert Stoff und Reihenfolge, nicht die Form: Titel,
Anweisungen, Beispiele, die Grundfall-Menge und die Teilung nach
Form stehen im Muster und fehlen im Bank-Blatt (TODO oder Regel).
Der größte Hebel ist Punkt 1 im Lernblatt: mit Variante 1 je
Sprosse hat das Bank-Blatt halb so viele Teilaufgaben wie das
Muster (88 gegen 185).
