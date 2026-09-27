# Stand: lineare-funktionen

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf der Mappe)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.2, Endstand 0 Abweichungen,
0 Warnungen in allen Dateien.

## Zeilen je Datei und hoehe

| Datei  | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|--------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone   |     26 |      0 |      12 |      13 |      0 |       1 |
| e1     |     45 |      4 |       5 |      24 |      0 |      12 |
| e2     |     82 |     12 |      10 |      33 |     18 |       9 |
| e3     |     58 |      4 |       5 |      21 |     16 |      12 |
| e4     |     41 |      0 |       5 |      18 |      6 |      12 |
| e5     |     58 |      8 |       5 |      15 |     18 |      12 |
| gesamt |    310 |     28 |      42 |     124 |     58 |      58 |

Pflicht je Einheit: e1, e3, e4, e5 je 3 fehler, 3 begruenden,
3 darstellung, 3 anwendung; e2 je 3 fehler, begruenden,
darstellung, keine anwendung. Zone: 1 fehler (Zone-Paar).

## Originale je Einheit (je 2 Zeilen, verfremdet)

- e1: keins (Katalog: Zielmarke ohne P10-Original)
- e2: 2026-FOR-K5a, 2024-OS-K3a, 2022-OS-K3a, 2021-OS-K2a
  (Kette Graph zeichnen); 2019-OS-K2c, 2019-OS-K2b, 2016-OS-B1c,
  2024-OS-B1i, 2025-OS-B1f (Kette Ablesen)
- e3: 2022-OS-K3a, 2021-OS-K6d, 2019-OS-K2a, 2023-OS-K4a,
  2017-OS-K5b, 2026-FOR-K5b, 2021-OS-K2b, 2023-OS-B1i
- e4: 2025-OS-K5a, 2015-OS-K4d, 2017-OS-K5a
- e5: 2023-OS-K3b, 2016-OS-K6b, 2021-OS-K7a, 2022-OS-K6b,
  2016-OS-K6c, 2022-OS-K6a, 2021-OS-K6a, 2016-OS-K6a, 2023-OS-K3a

## Prüfskript vor der Korrektur

- zone: 28 Abweichungen (pruef als Zahl statt Zeichenkette 25,
  merkmal je Sprosse uneinheitlich 3), 0 Warnungen
- e1: 3 Abweichungen (original fehlt bei Prüfungshöhe ohne
  Original 2, grafik fehlt wegen Wort „Graph" 1), 0 Warnungen
- e2: 5 Abweichungen (Sperre (2|2) 1, Zahl nicht an der
  Ergebnisstelle 4), 0 Warnungen
- e3: 11 Abweichungen (grafik fehlt wegen Wort „Graph" in
  Rechenaufgaben 11, in einer davon zusätzlich Sperre (1|3) und
  (−2|0)), 0 Warnungen
- e4: 2 Abweichungen (Sperre (3|5) und (−1|6)), 0 Warnungen
- e5: 11 Abweichungen (Zahl nicht an der Ergebnisstelle 10,
  nacktes % 1), 0 Warnungen

Keine Einheit scheiterte zweimal; alle Abweichungen wurden an den
Aufgaben korrigiert, nicht am Skript. Nachträglich in e3 eine
Nullstellenaufgabe geändert (−2x + 10 enthielt den Kastenterm
2x + 1 als Teilstring; vom Skript nicht gemeldet, von Hand
bereinigt).

## Entscheidungen

1. Zone: Fertigkeiten in der Reihenfolge des Eintrags (Zeilen
   29–34); sie deckt sich mit der ersten Verwendung (Koordinaten
   und Dreisatz Einheit 1, negative Zahlen Einheit 1, Brüche
   ab 2, Gleichungen 3, Terme 4).
2. Zone: kette ist die Fertigkeit ohne Quellenmarken und
   Themenverweis. Sprosse 1 = zwei sehr leichte (hoehe
   grundfall), 2 = mittlere, 3 = Fallstrick (hoehe sprosse);
   variante zählt je Fertigkeit durch, weil das id-Muster der
   Zone keine Sprosse trägt.
3. Zone: je Fertigkeit genau ein Fallstrick, aus Typische Fehler
   und den Fehlerquellen der Originale gewählt: x/y vertauscht;
   gleiche Differenz statt gleicher Quotient; Minus mal Minus;
   mal ½ als Verdoppeln; durch Dezimalzahl teilen statt
   malnehmen; Minus vor beiden x-Gliedern.
4. Zone-Paar: häufigster Fallstrick ist Minus mal Minus beim
   Einsetzen (Fehlerquellen 2026-FOR-K5b, 2023-OS-B1i,
   2017-OS-K5b); Paar als Sprosse 4 (pflicht fehler) und 5 in
   der Fertigkeit „Negative Zahlen multiplizieren und dividieren".
5. Die Grundvorstellung aus „Für schwache Schüler" (Tabelle aus
   Wortvorschrift) steht nicht in der Zone; bank.md nennt als
   Zone nur die Fertigkeiten.
6. Grundfall ist immer die erste Sprosse nach der Vorstufe, auch
   in e2 „Graph zeichnen", wo der Katalog den Zählvermerk (4×)
   erst bei der vierten Sprosse setzt. Zählvermerke (3×, 4×) und
   Klammerzusätze stehen nicht in sprosse_text.
7. e1: Die Zielmarke ohne P10-Original ist Sprosse 8 mit hoehe
   sprosse, 3 Zeilen, original null (siehe Befund 1).
8. e1: Fehler finden (Differenz statt Quotient) steht als
   Sprosse 7 in der Kette; das Pflichtelement fehler nimmt ein
   anderes Muster (Punkt (x|y) vertauscht), damit nichts doppelt
   ist.
9. e2 hat zwei Verfahrensketten (k4 Graph zeichnen, k5 Ablesen);
   die Pflichtkette heißt nach der ersten, „Graph zeichnen".
   Originale nach Typ verteilt: „Gerade aus Gleichung zeichnen"
   an Graph zeichnen, die übrigen an Ablesen.
10. e2 ohne Pflicht anwendung: die Typen der Einheit sind rein
    grafisch und tragen keinen Sachkontext.
11. Typen ohne Kette: e1 Dreisatz als Kontrolle; e2 Parameter
    deuten; e3 Wertetabelle, Schnittpunkt mit y-Achse; e4 Gerade
    durch zwei Punkte zeichnen, Schnittpunkt zweier Geraden
    rechnerisch; e5 Graph zu Tarif zuordnen, Situation zu
    Gleichung beschreiben. Fehler finden und Begründen der
    Typenzeile laufen als Pflichtelemente.
12. Einheit je Original nach „Zielmarke". 2023-OS-B1i steht dort
    nicht, wird aber als „hier geführt" genannt; es kommt nach e3
    (Typ Punktprobe). 2021-OS-K6b ist nicht aufgenommen (Befund
    5). 2015-OS-K4a, 2021-OS-K6c und die drei Originale mit
    Exponentialthema führen andere Einträge.
13. 2022-OS-K3a: in e2 nur der Zeichenteil, in e3 Zeichnen und
    Nullstelle, wie die Zielmarke es je Einheit nennt.
14. e2 Prüfungshöhe Graph zeichnen: verfremdet mit ganzzahligem m
    wie in allen vier Originalen (gleiche Falle), teils mit
    negativem n; Bruch-m steht in Sprosse 6 (Befund 4).
15. 2023-OS-K4a verfremdet als eine Teilaufgabe: Gerade zeichnen,
    sichtbaren Schnittpunkt mit der Parabel ablesen, entscheiden,
    ob es zwei Schnittpunkte gibt (die Kernfalle); die übrigen
    Aussagen entfallen. Zweiter Schnittpunkt liegt außerhalb.
16. 2025-OS-B1f und 2023-OS-K3a: die vier Graphen stehen in einem
    Koordinatensystem mit Namen A bis D statt in vier Bildern;
    Knick über \funktion{abs(...)} bzw. \funktion{max(...)}.
17. Rechenaufgaben ohne Bild sagen „auf der Geraden" statt „auf
    dem Graphen", weil das Skript beim Wort „Graph" eine Grafik
    verlangt (Befund 3). Betrifft Punktprobe, 2026-FOR-K5b,
    2021-OS-K2b, 2023-OS-B1i und zwei Pflichtzeilen in e3.
18. Tabellen (\wertetabelle) stehen im Feld grafik, auch wenn
    daneben ein Koordinatensystem steht (e3 darstellung).
19. pruef bei Gleichungen: m und n als Liste, die Lösung nennt
    „m = …, n = …" ausdrücklich; bei angekreuzten Gleichungen nur
    m; bei Zeichenaufgaben die Koordinaten der Lösungspunkte;
    Begründen, Ankreuzen von Buchstaben und Zuordnen ohne Ziffer
    in der Lösung mit pruef "".
20. Buchstaben: f(x), x, y, m, n, P durchgehend; e4 zusätzlich
    h(t) und V(t), im Aufgabentext erklärt; Personennamen in
    Fehler-finden-Aufgaben.
21. Ja/Nein-Entscheidungen gemischt (Punktprobe ja/nein/ja,
    Quotientenprobe ja/nein/ja, Prüfungshöhe Punktprobe ja/nein).
22. Tausender mit \, auch bei vier Stellen (e5: 1\,150, 1\,250,
    1\,500, 2\,000, 2\,340, 2\,850).
23. Die Zeilen entstanden mit einem Generatorskript außerhalb
    des Repos; die jsonl-Dateien sind die Quelle.

## Befunde

1. Prüfskript: Jede Zeile mit hoehe pruefung braucht ein
   original. Der Katalog gibt Einheit 1 ausdrücklich kein
   P10-Original, sondern eine Zielmarke; bank.md regelt den Fall
   nicht. Vorschlag: bank.md legt fest, ob eine Zielmarke ohne
   Original hoehe pruefung mit original null trägt, und das
   Skript lässt das zu.
2. bank.md „Mengen je Kette" gibt dem Grundfall 5 Zeilen je
   Kette; die Gegenprobe des Auftrags verlangt 5 je Einheit.
   Einheit 2 hat laut Katalog zwei Verfahrensketten, also 10.
   Beides zugleich geht nicht.
3. Prüfskript: Das Wort „Graph" im Aufgabentext verlangt eine
   Grafik, auch bei reinen Rechenaufgaben („liegt P auf dem
   Graphen von f?"). Die P10-Formulierung ist so nicht
   übernehmbar; die Regel sollte auf Ablese- und Zeichenaufträge
   zielen.
4. Katalog e2: Die Prüfungshöhe von „Graph zeichnen" lautet „m
   Bruch und n negativ", die vier Originale dazu haben alle ein
   ganzzahliges m. Sprossentext und Originale passen nicht
   zusammen.
5. Katalog: 2021-OS-K6b wird „hier geführt", hat aber keine
   Einheit in der Zielmarke, und seine Typen liegen ausdrücklich
   bei zuordnungen.md. Nicht aufgenommen, bis der Katalog es
   einer Einheit zuordnet.
6. Katalog e5: Der Erkennungsschritt „Anfangswert und Änderung
   im Text finden" und die Vorstufe der Kette „Anfangswert und
   Änderung im Text markieren" sind fast derselbe Schritt. Beide
   angelegt (8 Vorstufenzeilen), mit verschiedener Antwortform.
7. Prüfskript (vermutlich): Bei Ankreuzaufgaben mit Gleichungen
   als Optionen steht die Lösungszahl m in mehreren Optionen,
   ohne dass das Skript es meldet; die Regel „genau eine
   Zahloption" greift offenbar nur bei reinen Zahloptionen.
8. Sperre: Das Skript vergleicht ganze Terme und Zahlenpaare,
   keine Teilstrings. Das ist richtig so; Scheintreffer wie
   „−0,5x" gegen „x = −0,5" bleiben erlaubt.

## Offene Punkte

- Befund 2 entscheiden; bis dahin hat e2 zehn Grundfallzeilen.
- 2021-OS-K6b einer Einheit zuordnen oder streichen.
- Grafiken sind nicht kompiliert (kein LaTeX): ungeprüft sind
  \funktion mit max() und abs(), \funktionab mit 2/\x, die
  Argumentfolge von \steigungsdreieck (angenommen: x, y des
  Startpunkts, m), die Beschriftung bei vier Graphen in einem
  System und \wertetabelle mit Einheiten und \% im Kopf.
- Anwendungszeilen mit Freikilometern (2023-OS-K3a) zeigen den
  Knick als Funktionsgraph; ob der Zusammenbau das so setzt,
  klärt der erste Render.
