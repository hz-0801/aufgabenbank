# Stand: brueche-dezimalzahlen

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf der Mappe mappen/brueche-dezimalzahlen.md
vom 2026-09-27 06:15 UTC)
Datum: 2026-09-27 07:17 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.3 (Zone zuerst mit v0.2
geprüft, danach mit v0.3), Endstand 0 Abweichungen, 1 Warnung
(e1, Befund 2). Zusätzlich mit `--katalog` gegen die Zeilen der
Mappe: sprosse_text und kette wortgleich, 0 Abweichungen.

## Zeilen je Datei und hoehe

| Datei  | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|--------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone   |     30 |      0 |      14 |      15 |      0 |       1 |
| e1     |     79 |      8 |      10 |      27 |     22 |      12 |
| e2     |     47 |      4 |       5 |      24 |      2 |      12 |
| e3     |     41 |      4 |       5 |      18 |      2 |      12 |
| e4     |     49 |      4 |       5 |      24 |      4 |      12 |
| e5     |     65 |      8 |       5 |      30 |     10 |      12 |
| gesamt |    311 |     28 |      44 |     138 |     40 |      61 |

Pflicht je Einheit: e1 bis e5 je 3 fehler, 3 begruenden,
3 darstellung, 3 anwendung. Zone: 1 fehler (Zone-Paar).
Grundfall je Verfahrenskette 5 Zeilen (e1 hat zwei Ketten).

## Originale je Einheit (je 2 Zeilen, verfremdet)

- e1, Prüfungshöhe „Anteil bestimmen": 2019-OS-B1c, 2024-OS-B1b,
  2014-OS-B1i, 2022-OS-B1a, 2023-OS-B1d, 2017-OS-B1a,
  2021-OS-B1b, 2025-OS-B1c, 2026-FOR-B1b; P10-Form-Sprosse
  „Bruchteil einer Größe" (hoehe pruefung, siehe Nachbesserung):
  2015-OS-B1h,
  2018-OS-B1a
- e2: 2014-OS-B1i
- e3: 2014-OS-B1c
- e4: 2015-OS-B1c, 2018-OS-B1d
- e5: 2023-OS-B1f, 2014-OS-B1h, 2015-OS-B1c, 2018-OS-B1d,
  2020-OS-B1f

Nicht aufgenommen: 2019-OS-B1d, 2022-OS-B1j, 2017-OS-B1e (führt
potenzen-wurzeln.md, Katalog Z. 120), 2025-OS-B1h (nur als
Muster genannt).

## Prüfskript vor der Korrektur (erster Lauf je Datei)

- zone: 0 Abweichungen, 0 Warnungen (v0.2 und v0.3)
- e1: 0 Abweichungen, 1 Warnung (k2 s6: 4 Zeilen, Menge sprosse
  = 3; Befund 2)
- e2: 0 Abweichungen, 0 Warnungen
- e3: 0 Abweichungen, 0 Warnungen
- e4: 0 Abweichungen, 0 Warnungen
- e5: 0 Abweichungen, 0 Warnungen

Keine Einheit scheiterte am Prüfskript. Nach e5 hat die Gegenprobe
von Hand zwei Korrekturen ausgelöst (Entscheidung 18); das Skript
blieb danach bei 0 Abweichungen.

## Entscheidungen

1. Zone: Fertigkeiten in der Reihenfolge des Eintrags (Z. 31–37),
   nicht nach erster Verwendung umsortiert. kette und
   sprosse_text sind die Fertigkeit bis vor „– Einheit"; die
   Zeilen haben keinen Doppelpunkt (Befund 5). Die Fertigkeit
   Kreissektor (nur P10-Form) steht in der Zone, weil e1 die
   Originale 2019-OS-B1c und 2026-FOR-B1b trägt.
2. Zone: je Fertigkeit ein Fallstrick. Zone-Paar in „Prozent als
   Hundertstel": einstelliger Prozentsatz als Zehntel gelesen
   (Fehlerquellen 2018-OS-B1d, 2014-OS-B1i, 2022-OS-B1a,
   2023-OS-B1d; trägt e1 und e5). Die Zone sagt „Kommazahl",
   nicht „Dezimalzahl" (kein Begriff des Themas, 2.2).
3. Erkennungsschritte: sechs von sieben entfallen, weil sie die
   Vorstufe einer Kette derselben Einheit wiederholen (Befund 1).
   „Welche Form?" (Z. 45) bleibt als e5 k1 (anderer Handgriff als
   „Nullen anhängen"); kette = Frage ohne Anführungszeichen,
   sprosse_text = Katalogzeile bis vor „Vor Einheit".
4. e1 hat zwei Verfahrensketten. hoehe pruefung trägt „Anteil
   bestimmen", weil dort die Zielmarke 2019-OS-B1c (Niveau II)
   steht; „Bruchteil einer Größe" endet mit einer P10-Form-
   Sprosse an hoehe sprosse, original gesetzt, 2 Zeilen je
   Original (Befund 2). So hat jede Einheit genau eine
   Prüfungssprosse.
5. Prüfungshöhe mit „daneben …": eine Sprosse, sprosse_text ist
   der ganze Katalogtext ab „Prüfungshöhe:" ohne Schlusspunkt, je
   Original 2 Zeilen, variante zählt durch (e1 18, e5 10 Zeilen).
   merkmal einheitlich „Form und Anspruch der Prüfung: Original
   verfremdet".
6. Grafiken: Kästchenfiguren als `\bruchrechteck` (eine Reihe;
   die Vorlage hat kein Kästchengitter); halbe Kästchen als
   Ablese-ksys mit `\funktionab`-Linien (e1 s3 und 2024-OS-B1b);
   ungleiche Sektoren als `\kreisdiagramm` mit Buchstaben, die
   Markierung steht im Text; gleich geteilte Kreise
   `\bruchkreis`; 2026-FOR-B1b mit `\streifen[0]` (grauer Streifen
   ohne Teilstriche, Augenmaß-Falle) und `\kreissektor`; leeres
   Quadrat auf der Spitze als `\raute{4}{4}`, leerer Kreis
   `\kreisleer`; Stellenwerttafel als `\sachtabelle` mit
   ausgeschriebenen Stellen.
7. Buchstaben je Einheit: e1 Sektoren A–F, Auswahlfiguren P–S;
   e3 Zahlenstrahlpunkte A, B (Klassen nach Lehrkraft benannt).
8. Typen ohne Kette (hoehe sprosse, 3 Zeilen): e1 Ganzes aus
   Bruchteil; e2 gleichwertige Brüche am Streifen, Bruch als
   Geteilt-Aufgabe; e3 Zahl zwischen zwei Brüchen; e4
   Stellenwerttafel, Nachbarzahlen und Zählen in Schritten; e5
   Zahl zwischen zwei Zahlen, gemischte Liste ordnen, Aussagen
   prüfen. kette = Typtext wortgleich (e1 Kurzform „Ganzes aus
   Bruchteil"). Nicht aufgenommen: e5 „mit negativen Zahlen" und
   „mit Wurzeln" (Vorrat, andere Einträge).
9. Pflicht darstellung: e1 und e4 RLP Z. 6 (Bild, Wort, Symbol),
   e2 Z. 13 (Verfeinern, Vergröbern), e3 Z. 25 (Zahlenstrahl
   ablesen), e5 RLP Z. 6 (situationsangemessenes Darstellen).
   anwendung: e1 RLP Z. 6 (Bruchteile von Größen), e2 RLP Z. 6
   (gemischte Zahlen im Alltag: Zeit, Gewicht), e3 Z. 25
   (Anteile in Situationen), e4 Z. 7 (Dezimalzahlen bei Größen),
   e5 Z. 27 (runden, Größen: Laufzeiten, Preis je Liter).
10. Prozent in e1 (2014-OS-B1i, 2022-OS-B1a, 2023-OS-B1d),
    Wurzeln in e4 und e5 (2015-OS-B1c) und negative Zahlen in e5
    (2014-OS-B1h, 2020-OS-B1f) wie im Katalog an der
    Prüfungshöhe, mit der Falle des Originals (Befund 6, 7).
11. 2015-OS-B1c und 2018-OS-B1d je in e4 (Umwandeln als
    Nebenleistung) und e5 (Vergleichen), 2014-OS-B1i in e1 (Bruch
    ohne Kürzen, Prozent über Hundertstel) und e2 (vollständig
    kürzen); verschiedene Zahlen je Einheit.
12. 2015-OS-B1c verfremdet mit Grenzen 5/2, 7/4, 9/4, 13/4 und der
    Wurzel knapp darunter (√5, √3, √5, √10): gleiche Falle (Wurzel
    als die Zahl selbst gelesen), gleiche Form (drei Aussagen).
13. Ankreuzen: Bruchoptionen mit pruef [Zähler, Nenner]; Wort-,
    Buchstaben- und Aussageoptionen mit pruef ""; die loesung
    beginnt mit der Option wortgleich. \janein-Zeilen (e1 s0)
    haben loesung „ja" oder „nein".
14. Vergleiche: „Welcher ist größer?" nennt in loesung die Zahl,
    pruef ist sie; bei <, =, > nennt loesung die umgewandelte
    Zahl und das Zeichen, pruef ist die umgewandelte Zahl.
    Reihenfolgen mit „;" getrennt (Aufzählung für das Skript).
15. Offene Antworten (Zahl dazwischen): loesung „z. B." mit einer
    Lösung, pruef diese.
16. Periodische Dezimalzahlen mit `\overline`, Hinweis „Die
    Division geht nicht auf" in der Aufgabe (3.6).
17. „(4×)" im Katalog ist Blattmenge; in der Bank gilt Grundfall
    5, sprosse_text ohne Zählvermerk.
18. Nach e5, eigener Commit „Gegenprobe": fünf Aufgaben mit
    Kastenzahlen ersetzt (0,75 in zone f2; 11/4 in e4 s8; 0,25
    und 0,75 in e5 s0, s2, k5); Auswahlfiguren in e1 von A–D auf
    P–S, „Klasse A/B" in e3 auf Lehrkräfte (ein Buchstabe je
    Sache).
19. Neben dem Prüfskript wurden alle Rechen-, Vergleichs- und
    Ankreuzaufgaben von Hand nachgerechnet; kein Fehler.

## Befunde

1. Katalog: sechs Erkennungsschritte wiederholen die Vorstufe
   einer Kette derselben Einheit: Z. 39 = Vorstufe Z. 111
   („gleich große Teile prüfen"), Z. 40 = Vorstufe Z. 112
   („Was ist das Ganze?"), Z. 41 = „Faktor benennen" (Z. 113),
   Z. 42 = „Vergleichsweg ankreuzen" (Z. 114), Z. 43 =
   „Nachkommastellen zählen" (Z. 115), Z. 44 = „Nullen anhängen"
   (Z. 116). Nach bank.md entfallen sie; der Katalog führt beide.
2. (erledigt v0.5) Auftrag, Gegenprobe „genau eine Sprosse mit hoehe pruefung je
   Einheit" gegen Katalog e1: beide Verfahrensketten haben eine
   Prüfungshöhe mit Originalen. Die zweite steht als P10-Form-
   Sprosse an hoehe sprosse; bank.md regelt deren Menge nicht,
   das Skript wendet „Sprosse 3" an und warnt bei 2 je Original
   (e1 k2 s6: 4 Zeilen). Vorschlag: auch dort 2 je Original.
3. Auftrag, Gegenprobe „Mehrstellige Kastenzahlen kommen in
   keiner aufgabe vor": Der Kasten dieses Eintrags nennt die
   Stufenzahlen 10, 100, 1 000 und die Nenner 12, 15, 20, 25 als
   Gegenstand; Zehnerbruch, Zwölftel, Zwanzigstel und
   Fünfundzwanzigstel stehen in Sprossen- und Typtexten. Wörtlich
   ist die Gegenprobe hier nicht erfüllbar. Die Bank hält sie für
   Brüche und Dezimalzahlen aus dem Kasten ein (kein Kastenbruch
   mit mehrstelligem Zähler oder Nenner, keine Kastendezimalzahl
   mit zwei oder mehr Nachkommastellen und nicht 2,7 in einer
   aufgabe), nicht für ganze Zahlen als Nenner oder Anzahl.
4. Prüfskript: Die Sperre erkennt einzelne Kastenzahlen nicht
   (0,75; 11/4), die Gegenprobe verlangt sie. Eine eigene Probe
   „mehrstellige Kastenzahl in aufgabe" fehlt; sie bräuchte die
   Ausnahme aus Befund 3.
5. bank.md, Zone: „Fertigkeit bis zum Doppelpunkt" – die
   Fertigkeitszeilen dieses Eintrags haben keinen Doppelpunkt;
   genommen bis vor „– Einheit".
6. Katalog Z. 111: Drei Originale der Prüfungshöhe von Einheit 1
   verlangen Prozent (2014-OS-B1i, 2022-OS-B1a, 2023-OS-B1d), das
   der Eintrag erst für Einheit 5 voraussetzt (Z. 36).
7. Katalog Z. 115 und 116: 2015-OS-B1c und 2014-OS-B1h verlangen
   Wurzeln und negative Zahlen, im Eintrag „Vorrat" (Z. 108); die
   Prüfungshöhe führt damit neue Merkmale ein (unterrichtsblatt
   2.4 c).
8. Vorlage: kein Baustein für Kästchenfiguren mit mehreren Reihen
   oder schraffierten halben Kästchen; die Falle „3 von 4
   Spalten" (2021-OS-B1b) ist mit `\bruchrechteck` nicht
   darstellbar.

## Offene Punkte

- Kein LaTeX-Lauf. Ungerendert: `\kreisdiagramm` mit Buchstaben
  als Sektornamen, `\streifen[0]` mit Füllung, `\raute{4}{4}` als
  Quadrat auf der Spitze, `\kreisleer`, ksys mit
  `\funktionab{…}{}{…}{…}` (leeres Label), `\zahlenstrahl` mit
  Hundertstelskala und Beschriftung `0{,}2`, `\bruchrechteck` mit
  32 und 36 Teilen, zwei `\bruchrechteck` mit `\\` untereinander,
  `\sachtabelle` als Stellenwerttafel.
- Beziffert `\zahlenstrahl` jeden Teilstrich selbst, verraten e3
  s5 und e4 s3 die Lösung; dann Skala ohne Zahlen setzen.
- Prüfungshöhen mit Prozent (e1) und mit Wurzeln oder negativen
  Zahlen (e4, e5) beim Blattbau als Zielmarke kennzeichnen.
- (erledigt v0.5) Warnung e1 k2 s6 bleibt bis zur Entscheidung zu
  Befund 2.

## Nachbesserung 2026-09-27

Nach bank.md Stand 2026-09-27b und Prüfskript v0.5; vorher
0 Abweichungen, 1 Warnung, danach 0 Abweichungen, 0 Warnungen in
allen Dateien.

- e1.jsonl: Die Prüfungshöhe der Kette „Bruchteil einer Größe“
  (e1-k2-s6, Z. 112, vier Zeilen, 2 je Original) trägt hoehe
  pruefung statt sprosse, weil bank.md die Prüfungshöhe der
  letzten Sprosse jeder Verfahrenskette gibt; e1 hat damit zwei
  Prüfungssprossen, eine je Kette (Entscheidung 4 überholt).
- Tabelle „Zeilen je Datei und hoehe“ und Abschnitt „Originale“
  auf den neuen Stand gebracht.
- Prüfungshöhe ohne Original: keine im Eintrag; nichts zu ändern.
- Erkennungsschritte: „Welche Form?“ (e5 k1, Formen ankreuzen)
  verlangt einen anderen Handgriff als die Vorstufe „Nullen
  anhängen“ und bleibt; die übrigen sechs fehlen schon (Befund 1).

## Nachbesserung Render 2026-09-28

Quelle: bau/render-alle/bericht.md, bau/hefte/bericht.md, bau/fokus/bericht.md, bau/layout-befunde.md Punkt 31. Übersicht aller Einträge: bau/render-alle/behoben.md.

- e4-k1-s8-v3, e4-k1-s8-v4, e5-k2-s6-v1, e5-k2-s6-v2, e5-k2-s6-v3, e5-k2-s7-v1, e5-k2-s7-v2, e5-k2-s7-v3, e5-k2-s8-v1, e5-k2-s8-v2, e5-k2-s8-v3, e5-k2-s9-v7, e5-k2-s9-v8 (13): Missing $ inserted – `__` als Lücke im Textmodus. Änderung: `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer.

Nur diese 13 Zeilen geändert, alle übrigen byte-gleich. `bank-pruef.py brueche-dezimalzahlen`: 0 Abweichungen. Probe: jede Zeile allein in einem Minimaldokument mit mathblatt.sty (hz-0801/blattbau) gesetzt wie werkzeuge/zusammenbau.py v0.7 (teile_normal, teil_schwach, Lösung in \erg), xelatex ohne Fehler.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- brueche-dezimalzahlen-e1-k1-s6-v17: pruef [1, 6] bei Buchstabenoptionen (bank.md: dann "") → pruef "" (Regel b).
- brueche-dezimalzahlen-e1-k1-s6-v18: pruef [1, 5] bei Buchstabenoptionen → pruef "" (Regel b).
- Prüfskript: Abweichungen 0.
