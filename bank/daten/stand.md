# Stand: daten

Katalog-Commit: 72a01d36d39f9def19828a6f3a5cc5292cdd659f (2026-09-27,
aus dem Kopf der Mappe). Zeilennummern in quelle beziehen sich auf
diesen Stand.
Datum: 2026-09-28 04:34 UTC (`date`), Nachtwächter-Sitzung.
Prüfskript: werkzeuge/bank-pruef.py v0.5, Endstand 538 Zeilen,
0 Abweichungen, 0 Warnungen; mit `--katalog` (Zeilen der Mappe
als Katalogdatei) ebenfalls 0.

## Zeilen je Datei und hoehe

| Datei  | Zeilen | vorst. | grundf. | spr. | pruef. | pfl. | graf. |
|--------|-------:|-------:|--------:|-----:|-------:|-----:|------:|
| zone   |     55 |      – |      24 |   30 |      – |    1 |     5 |
| e1     |     88 |      8 |      10 |   54 |      4 |   12 |    37 |
| e2     |     59 |      8 |       5 |   30 |      4 |   12 |    54 |
| e3     |     54 |      4 |       5 |   27 |      6 |   12 |    30 |
| e4     |     79 |      8 |      10 |   45 |      4 |   12 |     6 |
| e5     |     87 |      8 |      10 |   48 |      9 |   12 |    48 |
| e6     |     41 |      4 |       5 |   18 |      2 |   12 |    28 |
| e7     |     75 |      8 |      10 |   39 |      6 |   12 |    65 |
| gesamt |    538 |     48 |      79 |  291 |     35 |   85 |   273 |

loesungsgrafik: in keiner Zeile (keine Skizzieraufgabe, deren
Lösung mehr als Zahlen braucht). Pflichtelemente: alle sieben
Einheiten fehler, begruenden, darstellung, anwendung je 3.

## Originale je Einheit

Prüfungshöhe je 2 Zeilen, die übrigen Originale je 1 Zeile an ihrer
Kettensprosse (Entscheidung 2).

- e1: 2015-OS-K7b (Prüfungshöhe k1) · 2024-C-3b (Prüfungshöhe k2)
  · 2023MgrundlegendBStochastikWTR2-2a, 2023-A-3a (k2)
- e2: 2023-OS-K6d, 2018-OS-K3a (Prüfungshöhe) · 2016-OS-K2b,
  2020-OS-K2b, 2016-OS-K2a, 2020-OS-K2a, 2026-FOR-K3d
- e3: 2024-OS-K2c, 2017-OS-K2c, 2025-OS-K6b (Prüfungshöhe) ·
  2018-OS-K3c, 2021-OS-K5b, 2015-OS-K7c, 2022-OS-K4d
- e4: 2025-OS-K6c (Prüfungshöhe k1) · 2019-A-3a (Prüfungshöhe k2)
  · 2014-OS-K4a, 2023-OS-K6c, 2019-OS-B1i, 2014-OS-K4b,
  2026-FOR-K3a, 2015-OS-B1f, 2024-OS-B1h, 2016-OS-B1a,
  2017-OS-B1h, 2021-OS-B1f, 2021-OS-K5a, 2020-OS-K2c, 2022-OS-K4a,
  2024-OS-K2a, 2015-OS-K7a, 2024-OS-K2b, 2022-OS-B1d, 2025-OS-K6a,
  2020-OS-K2d, 2026-FOR-K3b (k1) · 2026MgrundlegendBStochastik-
  WTR2-1e (k2)
- e5: 2019-OS-K5c, 2026-FOR-K3e, 2018-OS-K3d (Prüfungshöhe k1) ·
  2022-OS-K4c (k1) · k2 Boxplot: kein Original, Prüfungshöhe ohne
  Original mit 3 Zeilen
- e6: 2026MerhoehtBStochastikWTR2-1e (Prüfungshöhe) · 2024-B-3b,
  2019-A-3b, 2024-B-3a, 2026MerhoehtBStochastikWTR2-1d, 2020-C-3b,
  2021-A-3b, 2020-C-3e, 2020-C-3c, 2022-C-3d
- e7: kein Original; beide Ketten enden auf einer Prüfungshöhe ohne
  Original mit 3 Zeilen (Zielmarke Lehrwerk, LISUM-PH)

Alle 59 Kennungen aus Abschnitt 2 der Mappe sind verfremdet; keine
fehlt (2014-OS-K3d steht nicht in Abschnitt 2, s. Offene Punkte).

## Prüfskript vor der Korrektur

| Datei | Abw. | häufigster Grund                             | Warn. |
|-------|-----:|----------------------------------------------|------:|
| zone  |    1 | pruef nicht an der Ergebnisstelle            |     0 |
| e1    |    0 | –                                            |     0 |
| e2    |    3 | Ankreuzoption mit \leerfeld ungleich (2)     |     0 |
| e3    |    6 | Ergebnisstelle: Gradzeichen in Aufzählung (5)|     0 |
| e4    |    3 | pruef nicht an der Ergebnisstelle (2)        |     0 |
| e5    |    3 | pruef nicht an der Ergebnisstelle            |     0 |
| e6    |    8 | pruef nicht an der Ergebnisstelle (7)        |     0 |
| e7    |    6 | pruef nicht an der Ergebnisstelle (4)        |     0 |

e2 brauchte zwei Korrekturrunden (die Ankreuzoption „nein,
Startwert: \leerfeld“ blieb nach der ersten ungleich); keine
Einheit ist liegen geblieben. Außerhalb der Meldungen geändert:
e6-k1-s8-v2 (Termwert 11,7 statt 10,05 – das Skript fand es),
dazu die Gegenprobe Kastenzahlen (Commit abf4114): e1-k1-s7-v1
(0,28 → 0,26), e2-k1-s0-v2 (Achse 60–68 → 70–78), e7 mit neuen
Tafelzahlen in 33 Zeilen (Randsummen 19, 20, 13 und die Zelle 12
lagen in der Rolle des Kastens 7).

## Gegenprobe (Ist-Werte)

- Verfahrensketten: e1 zwei, e2 eine, e3 eine, e4 zwei, e5 zwei,
  e6 eine, e7 zwei; jede mit genau 5 Zeilen grundfall (Skript ohne
  Warnung), jeder sprosse_text wortgleich in der Zeile quelle
  (`--katalog`, 0).
- Prüfungshöhe: je Verfahrenskette genau eine Sprosse hoehe
  pruefung als letzte; Originale je 2 Zeilen, ohne Original 3.
- Kastenzahlen (mehrstellig aus den Merkkästen 1–7, 65 Zahlen):
  in der Rolle des Kastens 0 Treffer nach der Nachbesserung; in
  anderer Rolle 447 Treffer, davon 250 auf 10, 12, 15, 20, 25, 30
  (Prozentsätze, Anzahlen, Achsenschritte) und die Konstanten
  100 %, 360°, 10 cm als Gegenstand der Ketten (Entscheidung 9).
  Sperrprobe des Skripts: 0.
- form zeichnen: 54 Zeilen, alle mit grafik; jede Zeile mit
  Lies/Zeichne/ablesen im Text hat grafik (Skript).
- Ankreuzzeilen: 34; Lösung nennt genau eine Option wortgleich
  oder die Lösungszahl steht in genau einer Zahloption (Skript, 0);
  die vier Doppelaussagen (richtig/falsch je Aussage, e5) lässt
  das Skript ohne Probe durch.

## Entscheidungen

1. Von den zwölf Erkennungsschritten bleibt nur „Wo fängt die
   Achse an?“ (e2 k1); die elf anderen entfallen, weil sie den
   Handgriff der Vorstufe einer Kette ihrer Einheit wiederholen
   (Befund 1). „Was ist das Ganze?“ entfällt auch vor Einheit 3,
   weil es nur einmal, in seiner ersten Einheit, stünde und dort
   die Vorstufe ist.
2. Originale außerhalb der Prüfungshöhe stehen als eine der drei
   Varianten ihrer Kettensprosse mit gesetztem Feld original
   (Muster wahrscheinlichkeit), nicht mit 2 Zeilen; e4 hat 22
   P10-Originale, mit 2 Zeilen je Original wären es 44 Zeilen in
   einer Prüfungshöhe. Die „daneben“-Originale der Prüfungshöhen
   (e3, e5, e2 Gitterlinien) stehen mit je 2 Zeilen in der
   Prüfungshöhe, weil der Sprossentext sie nennt.
3. e1 hat zwei Vorstufen mit demselben Handgriff (Ganzes
   unterstreichen, Sek I und Sek II); beide bleiben, die Sek-II-
   Vorstufe arbeitet an Tabellen mit Sorten und Klassen und der
   Falle „Zahl der Zeilen statt Gesamtzahl“.
4. Prüfungshöhe ohne Original (e5 Boxplot, e7 beide Ketten): hoehe
   pruefung, original null, 3 Zeilen; der Sprossentext ist der
   Teil des Katalogsatzes ab „zu zwei Datenreihen …“ bzw. „aus
   einem Sachtext …“ / „eine Aussage über den Anteil …“.
5. Zone: kette und sprosse_text sind die Fertigkeitszeile bis
   „ – Einheit“ (die Zeilen haben keinen Doppelpunkt; die Sek-II-
   Zeilen beginnen mit „Sek II:“, der Doppelpunkt dort ist keine
   Grenze). Reihenfolge nach kleinster Einheit; Zone-Paar bei
   „Prozentsatz berechnen“ (Fallstrick „durch die anderen statt
   durch alle geteilt“, häufigstes Muster der Einheiten 1 und 7).
6. \vierfeldertafel{A}{B}{…}: gelesen als Zeilenmerkmal A,
   Spaltenmerkmal B, neun Werte zeilenweise (A: B, nicht B, Summe;
   nicht A: …; Summen); die Anleitung sagt nur „zeilenweise B,
   nicht B, Summe“. Leere Felder als leere Listeneinträge.
7. Diagramme mit Achse ab einem Startwert (e2 k1, e5 k1) als
   \begin{ksys}[ymin=…] mit \punkt-Reihe (Liniendiagramm); ein
   Säulendiagramm mit abgeschnittener Achse hat keinen Baustein
   (\saeulenab kennt kein ymin), diese Aufgaben beschreiben die
   Achse im Text.
8. Quartile (e5 k2): bei ungerader Anzahl Mediane der Hälften ohne
   den Median (LS-Konvention); der Katalog legt es nicht fest.
9. Kastenzahlen (Gegenprobe): gesperrt in der Rolle des Kastens
   (Kasten 7: Tafelzahlen Mädchen/Brille; Kasten 1: 0,28 als
   relative Häufigkeit Bus; Kasten 5: Achse ab 60 mit 63/66),
   frei in anderer Rolle; 100 %, 360°, 3,6°, 10 cm sind Gegenstand
   der Ketten 1, 3 und 7.
10. Standardabweichung (e4 k2, e6): Nenner n als Hauptweg, in jeder
    Aufgabe genannt; Rechnerfunktion oder Abweichungsquadrate.
11. Erkennungsschritt e2 k1 und Sek-I-Vorstufen mit Ankreuzform:
    die Option „nein, Startwert“ trägt das \leerfeld außerhalb
    der \kreuz-Klammer, damit die Lösung wortgleich beginnen kann.
12. darstellung ohne eigenen Typ im Katalog zitiert die nächste
    Typenzeile (e1 „als Dezimalzahl und in Prozent“, e2 und e4
    „aus Tabelle oder Diagramm“ bzw. „Diagramm aus einer Tabelle
    zeichnen“, e6 „Mittelwert aus Häufigkeitstabelle“).

## Befunde

1. Katalog: Elf der zwölf Erkennungsschritte (Zeilen 55–66)
   wiederholen die Vorstufe einer Kette ihrer Einheit; der Katalog
   führt beide.
2. Katalog: Die Prüfungsform (P10) nennt 40 Originale, Abschnitt 2
   der Mappe 59 Kennungen; 2014-OS-K3d (Zinsen, Achse ab 1060 €)
   steht in „Typische Fehler“ und „Prüfungsform“, nicht in
   Abschnitt 2 – es kann nicht als original gesetzt werden und ist
   in e5 k1 s6 nur sinngemäß verfremdet.
3. Katalog: Die Sprossenzeile der Kette Boxplot (Zeile 175) und
   der Vierfeldertafel (179, 180) tragen die Prüfungshöhe als
   Zielmarke mit Klammerverweisen; als sprosse_text taugt nur ein
   Teilsatz.
4. Katalog/bank.md: e5 k2 s9 „Fehler finden (falsche Bezugsgröße)“
   steht als Kettensprosse neben dem Pflichtelement fehler (wie
   potenz-exponentialfunktionen Befund 8); hier beides.
5. bank.md: „Mehrstellige Kastenzahlen kommen in keiner aufgabe
   vor“ ist bei sieben Kästen mit 65 Zahlen (darunter 10, 12, 15,
   20, 25, 30, 40, 50, 60, 100) nicht einhaltbar; die Rollenregel
   (potenz Entscheidung 8) sollte in bank.md stehen.
6. bank.md: Zwei Ketten derselben Einheit mit gleicher Vorstufe
   (e1) sind nicht geregelt.
7. Prüfskript: In einer Aufzählung von Ergebnissen mit ^\circ
   („$180^\circ$, $144^\circ$“) bleibt das ^ stehen und trennt die
   Glieder; nur „(in Grad)“ hinter der Liste half.
8. Prüfskript: Eine Ankreuzoption mit \leerfeld im Text kann nie
   wortgleich in der Lösung stehen.
9. Prüfskript: Ein Ergebnis hinter „das sind“, „also“ oder einem
   Namen zählt nicht als Ergebnisstelle; 20 der 30 Abweichungen
   waren nur Schreibweise der Lösung.
10. Bausteine: \saeulenab und \balkenab kennen kein ymin/xmin;
    abgeschnittene Achsen (Kern der Einheit 5) sind nur als
    Liniendiagramm im ksys oder als Textbeschreibung baubar.
    \saeulen ohne ymax für „Skala selbst wählen“ (e2 k3) fehlt.

## Offene Punkte

- Kein LaTeX-Lauf. Unbelegt in der Anleitung: \saeulenab mit
  Fragezeichen als Label („?/280“), leerer Wert bei \saeulenab
  („Do/“), \kreisdiagramm mit leerem Label neben beschrifteten,
  \histogramm mit dreistelligen Klassengrenzen (145:153),
  \sachtabelle mit Mathe-Zellen („$0 \le x < 15$“),
  \vierfeldertafel mit leeren Kopfargumenten (e7 k1 s0).
- Gruppierte Säulen (e1 k2 s3 v2) sind als ein \saeulen mit
  Labels 1A, 1B, … gebaut; ein Baustein für Gruppen fehlt.
- e2 k2 s7 v3 (2026-FOR-K3d) hat 50 Hilfslinien (yfein 0,05 auf
  2,5); im Original ist die Achse ab 1,75 abgeschnitten.
- Ohne Zeile: 2014-OS-K3d (nur sinngemäß), 2015-OS-K4a (Original
  bei lineare-funktionen.md); die fhr-Kennungen 2020-A-3a,
  2026-B-3b, 2026-C-3c, 2023-A-3b, 2025-C-3a, 2026-C-3a,
  2021-A-3a, 2020-C-3a, 2022-C-3b, 2025-A-3b, 2026-B-3a,
  2024-C-3a, 2023-C-3a, 2022-B-3c stehen nicht in Abschnitt 2 und
  tragen kein Feld
  original, obwohl die Ketten sie nennen.
- Generatoren dieser Sitzung liegen nicht im Repo (Auftrag: nur
  unter bank/<eintrag>/ schreiben).

## Nachbesserung Render 2026-09-28

Quelle: bau/render-alle/bericht.md, bau/hefte/bericht.md, bau/fokus/bericht.md, bau/layout-befunde.md Punkt 31. Übersicht aller Einträge: bau/render-alle/behoben.md.

- e2-k2-s11-v2 (1): Dimension too large – `\saeulenab` mit Werten bis 90\,000. Änderung: `\saeulenab` mit Werten bis 90\,000 (pgfmath rechnet nur bis 16\,383) → Werte in Tausend (90/10/10, 81/75/54); die Achse ist ohne Zahlen, das Bild bleibt gleich (5,4 Kästchen für D) – wie die Schwesterzeile s11-v1.
- e5-k1-s6-v1 (1): Dimension too large – ksys-x-Achse mit Jahreszahlen. Änderung: `ksys` mit Jahreszahlen auf der x-Achse (x bis 2025 → Maß über 16\,384 pt) → `\saeulenab` mit denselben Werten, Jahren als Kategorien und abgeschnittener y-Achse (ymin bleibt); loesung „jeder Punkt“ → „jede Säule“.
- e5-k1-s10-v1, e5-k1-s10-v2 (2): Dimension too large – ksys-x-Achse mit Jahreszahlen. Änderung: `ksys` mit Jahreszahlen auf der x-Achse (x bis 2025 → Maß über 16\,384 pt) → `\saeulenab` mit denselben Werten, Jahren als Kategorien und abgeschnittener y-Achse (ymin bleibt).

Nur diese 4 Zeilen geändert, alle übrigen byte-gleich. `bank-pruef.py daten`: 0 Abweichungen. Probe: jede Zeile allein in einem Minimaldokument mit mathblatt.sty (hz-0801/blattbau) gesetzt wie werkzeuge/zusammenbau.py v0.7 (teile_normal, teil_schwach, Lösung in \erg), xelatex ohne Fehler.

## Umsetzung Duden-Abgleich und Leiterregeln (2026-10-02)

Katalog: daten.md, Commit 919f3ee (Abgleich
katalog/_abgleich-duden9-kap10.md). Zeilen e1 88 → 95, e2 59 → 62,
e3 54 → 61, e4 79 → 90, e5 87 → 101, e7 75 → 78 (e6, zone unverändert).

Neue Sprossen (je 3 Zeilen; Entwürfe aus
eingang/duden9-2026-10-02/neu-st-duden9.jsonl, Rest herkunft „Regel
02.10.“): e1 k1 gemischt, e1 k5 s2 Säulendiagramm oder Histogramm
wählen (Vorrat, zweite Sprosse des Typs ohne Kette, quelle 31); e2 k2
gemischt; e3 k1 zwei Streifendiagramme vergleichen, gemischt; e4 k1 alle
Kenngrößen einer Liste, Mittelwert aus einer Häufigkeitstabelle; e4 k2
mittlere Abweichung (GYM, Vorrat); e5 k1 gemischt; e5 k2 Quartile über
den Rangplatz (Vorrat), rückwärts (Liste zum Boxplot), gemischt; e7 k2
rückwärts (Anzahl aus Zeilenanteil). Zusatzzeilen aus dem Duden-Eingang
(Beschluss 6): e1 k4 s1 v4, e3 k1 s4 v4, e4 k2 s1 v6, e4 k3 s1 v4,
e5 k2 s2 v4, e5 k2 s8 v4. Prüfskript: 0 Abweichungen, 6 Warnungen
(Menge, alle durch Zusatzzeilen); mit --katalog 0 → 0.
