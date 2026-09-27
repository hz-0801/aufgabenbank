# Stand: kreis

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf von mappen/kreis.md)
Datum: 2026-09-27 07:10 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.3, Endstand 174 Zeilen OK,
0 Abweichungen, 0 Warnungen; zusätzlich mit `--katalog` gegen die
Katalogzeilen der Mappe (sprosse_text und kette wortgleich): 0.

## Dateien

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     26 |        0 |        12 |      13 |        0 |       1 |
| e1    |     55 |        8 |         5 |      27 |        3 |      12 |
| e2    |     49 |        4 |         5 |      24 |        4 |      12 |
| e3    |     44 |        4 |         5 |      21 |        2 |      12 |

Pflicht je Einheit: fehler 3, begruenden 3, anwendung 3,
darstellung 3. Zone: pflicht fehler 1 (Zone-Paar).

## Originale je Einheit

- e1: keins (Prüfungshöhe ohne Original, 3 Zeilen, original null)
- e2: 2016-OS-K3b (2 Zeilen), 2024-OS-K4a (2 Zeilen)
- e3: 2025-OS-B1e (2 Zeilen)

## Prüfskript vor der Korrektur

- zone: 1. Lauf (v0.2) 0 Abweichungen, 0 Warnungen; nach dem
  Wechsel auf v0.3 (während der Sitzung auf main erschienen)
  erneut 0/0.
- e1: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e2: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e3: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- Zweimal gescheitert: keine Einheit.

Eigene Zusatzprobe (mehrstellige Kastenzahlen, Zahlen der
Originale in aufgabe): e3 im ersten Lauf ein Treffer (80° in einer
Ausschnittsfläche, zufällig wie h = 80 cm in 2024-OS-K4a), vor dem
Commit durch 84° ersetzt. Endstand 0.

## Entscheidungen

1. Erkennungsschritte: nur „Rand oder Fläche?“ bleibt (e1, k1).
   Die drei anderen entfallen, weil sie den Handgriff der Vorstufe
   derselben Einheit verlangen (bank.md; Befund 1).
2. e1, Prüfungshöhe: hoehe pruefung, original null, 3 Zeilen. Der
   Katalog sagt „kein eigenes P10-Original“; 2022-OS-K2a und
   2023-OS-K5a gehören zu koerper.md. Form wie dort (Länge des
   Mantelrechtecks aus dem Radius, eine Stelle), ohne Prüfkennung.
3. e2, Prüfungshöhe: eine Sprosse mit vier Zeilen, je Original der
   Kettenzeile zwei; sprosse_text ist der ganze Abschnitt der
   Kettenzeile. merkmal allgemein („Kreisfläche in Prüfungsform,
   Falle Durchmesser als Radius oder Umfang statt Fläche“), weil
   2024-OS-K4a vom Radius ausgeht.
4. kette: „Umfang“, „Fläche“, „Kreisteile“ (Name vor „(Einheit
   n)“). Typen ohne Kette: kette = Typtext aus „Typen je
   Lerneinheit“ ohne Stufenklammer, bei „Term zu Figur“ ohne die
   Beispielklammer. Pflichtkette: Name der Verfahrenskette,
   Sprossen 1 fehler, 2 begruenden, 3 anwendung, 4 darstellung.
5. sprosse_text der Pflichtsprossen: Fehler finden und Begründen
   aus „Typen je Lerneinheit“ (Zeile 19–21). Anwendung e1 aus
   Zeile 19 (Sachaufgabe), e2 und e3 aus LISUM-PH Zeile 8 („Berechnen
   in Sachkontexten …“, „Berechnen von Umfang und Flächeninhalt …“),
   damit sie sich von Kettensprosse bzw. Typ „Sachaufgabe“
   unterscheiden. Darstellung e1 aus Zeile 8 (Proportionalität
   d–u, Tabelle), e2 aus Zeile 13 („Halbkreis und Viertelkreis“:
   Term ↔ Text ↔ Skizze), e3 aus Zeile 21 („Sektor im
   Kreisdiagramm“).
6. Typen ohne Kette: e1 „Radius, Durchmesser, Mittelpunkt …
   einzeichnen“, „Kreis … zeichnen“, „Umfang messen und u : d
   bilden“; e2 „Term zu Figur“, „Sachaufgabe (Abwurfring …)“,
   „Fläche oder Umfang: die passende Formel wählen“; e3
   „Sachaufgabe (Rasensprenger …)“. „d = 2 · r und r = d : 2“
   steckt in der Vorstufe von e1 und hat keine eigene Kette.
7. Zone: kette und sprosse_text = Fertigkeit bis „ – “ (die
   Fertigkeitszeilen haben keinen Doppelpunkt; Befund 2).
   Reihenfolge nach erster Verwendung, bei gleicher Einheit nach
   Lehrplanfolge: Fläche/Umfang (Zeile 30), Dezimalzahlen (25),
   Umstellen (27), Quadrieren (26), Winkel (28), Anteil (29).
   Je Fertigkeit ein Fallstrick.
8. Zone-Paar in der Fertigkeit Fläche/Umfang: „Umfang und Fläche
   vertauscht“, am Rechteck. Es ist das Muster mit den meisten
   P10-Belegen unter „Typische Fehler“ (Zeile 63); die Zone
   braucht dafür keinen Kreis.
9. Zone ohne π und ohne Kreis (unterrichtsblatt 2.2: kein Begriff
   des Themas), obwohl die Fertigkeitszeilen 25 und 27 π nennen
   (Befund 3). Der Fallstrick „erst am Ende runden“ läuft über
   einen Näherungswert mit vielen Stellen.
10. Rechnen mit der π-Taste in allen Einheiten; Zwischenergebnisse
    in der Lösung gerundet, gerechnet wird ungerundet.
11. Einheiten im Quadrat als „cm²“ außerhalb des Mathemodus; in
    `\rechnung` als `\text{ cm}^2`. Winkel als `$90^\circ$`.
12. Formeloptionen beim Ankreuzen (e2, Vorstufe) in LaTeX, pruef ""
    (v0.3, Änderung d). Bruchoptionen (e3, Vorstufe): pruef
    Zähler und Nenner als Liste.
13. Die Konstante 360 (Vollwinkel) steht in keiner aufgabe, auch
    nicht in vorgegebenen Fehlrechnungen („250° : Vollwinkel“).
14. Zeichenfläche für Kreise ohne Vorlage: `\rechenplatz[halb]{n}`
    im Feld grafik, die Lösung in loesungsgrafik.

## Befunde

1. Katalog: Drei Erkennungsschritte verlangen den Handgriff der
   Vorstufe derselben Einheit: „Radius oder Durchmesser?“ (Zeile
   32) / e1 „Radius oder Durchmesser benennen“; „Welche Formel?“
   (Zeile 34) / e2 „Formel ankreuzen“; „Welcher Teil vom Kreis?“
   (Zeile 35) / e3 „Anteil zum Ausschnitt ankreuzen“. Der Katalog
   führt jeweils beide.
2. bank.md, Zone: „Fertigkeit bis zum Doppelpunkt“ passt nicht auf
   Fertigkeitszeilen ohne Doppelpunkt (hier alle sechs); gelesen
   als „bis zum Gedankenstrich“.
3. Katalog: Die Fertigkeitszeilen 25 und 27 nennen π und
   u = π · d; unterrichtsblatt 2.2 verbietet Begriffe des Themas
   in der Zone.
4. Katalog, Zielmarke Einheit 1: „kein eigenes P10-Original“, aber
   die Marke ist eine P10-Nebenleistung (2022-OS-K2a, 2023-OS-K5a),
   nicht Rahmenlehrplan oder Lehrwerk, wie bank.md die Prüfungshöhe
   ohne Original beschreibt. Hier als ohne Original gesetzt
   (Entscheidung 2).
5. Prüfskript v0.3, Sperre: π-Terme mit nur einer Zahl aus
   Merkkasten und Typische Fehler werden nicht gesperrt. Probe:
   aufgabe „Rechne $\pi \cdot 2{,}14^2$.“ (Zeile 62) ohne
   Abweichung; „Rechne $145 : 360$.“ wird richtig gesperrt.
6. Prüfskript: Die Gegenprobe „mehrstellige Kastenzahlen in keiner
   aufgabe“ prüft das Skript nicht (Probe „$d = 31{,}4$ cm“ ohne
   Abweichung); hier mit eigener Zusatzprobe erledigt.

## Offene Punkte

- LaTeX nicht kompiliert. Ungeprüft: `\begin{kreis}` mit leerem
  `\mittelpunkt{}` und leeren Labels, `\kreissektor` mit leerem
  Label, `\kreisdiagramm` mit Winkeln statt Prozent als Werten,
  `\sachtabelle` mit `\leerzelle` in mehreren Spalten, „cm²“ im
  Textmodus.
- 2024-OS-K4a verfremdet zweimal als Kegel (Sandhaufen, Zelt);
  Kontextwechsel zum Zylinder wäre möglich.
- Merkmal der Vorstufe e1 steckt nur in der Grafik; der
  Aufgabentext der vier Zeilen ist gleich.

## Nachbesserung 2026-09-27

Prüfskript v0.5 vorher 0 Abweichungen, 0 Warnungen; nachher 0/0.
Keine Zeile geändert oder gestrichen.

- Prüfungshöhe: e1-k2-s8 trägt schon hoehe pruefung mit original
  null (Entscheidung 2); nichts nachzuziehen.
- Erkennungsschritte: Die drei, die den Handgriff einer Vorstufe
  derselben Einheit verlangen, waren schon nicht angelegt
  (Entscheidung 1, Befund 1); „Rand oder Fläche?" (e1-k1) bleibt,
  weil es sich vom Handgriff der Vorstufe „Radius oder
  Durchmesser benennen" unterscheidet.
- Befunde 5 und 6 mit v0.5 nachgeprobt: „Rechne $\pi \cdot
  2{,}14^2$." und „$d = 31{,}4$ cm" in aufgabe bleiben ohne
  Abweichung, beide Befunde bleiben offen. Befunde 1 bis 4 sind
  durch bank.md 2026-09-27b nicht erledigt (1 und 3 Katalog;
  2 „bis zum Doppelpunkt" und 4 „Zielmarke aus Rahmenlehrplan oder
  Lehrwerk" stehen unverändert).
