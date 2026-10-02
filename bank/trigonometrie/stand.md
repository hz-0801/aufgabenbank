# Stand: trigonometrie

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf von mappen/trigonometrie.md)
Datum: 2026-09-27 12:30 UTC

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        – |        18 |      19 |        – |       1 |    38 |
| e1    |       12 |         5 |      51 |       14 |       9 |    91 |
| e2    |        4 |         5 |      33 |       12 |       9 |    63 |
| e3    |        4 |         5 |      48 |       12 |       9 |    78 |
| e4    |        4 |         5 |      42 |       12 |       9 |    72 |
| Summe |       24 |        38 |     193 |       50 |      37 |   342 |

## Originale je Einheit

- e1: 2021-OS-K3a, 2021-OS-K3b, 2017-OS-K4b, 2022-OS-K5d,
  2020-OS-B1j, 2025-OS-B1g, 2020-OS-B1c (Prüfungshöhe);
  2017-OS-B1j, 2019-OS-B1h (s1), 2018-OS-B1g (s2)
- e2: 2024-OS-K6b, 2019-OS-K3b, 2026-FOR-K4b, 2022-OS-K5b,
  2025-OS-K4a, 2019-OS-K2d
- e3: 2018-OS-K4d, 2020-OS-K5b, 2023-OS-K7b, 2026-FOR-K4c,
  2016-OS-K7c, 2015-OS-K5d
- e4: 2024-OS-K6d, 2025-OS-K4c, 2018-OS-K4c, 2019-OS-K3c,
  2020-OS-K7c, 2021-OS-K3c (Prüfungshöhe); 2015-OS-K5c (s4),
  2014-OS-K2b (s10)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                |
|-------|-------------:|----------:|---------------------------------|
| zone  |            5 |         0 | merkmal uneinheitlich je Sprosse |
| e1    |            6 |         0 | grundfall nach höherer Stufe (5) |
| e2    |            0 |         0 | –                               |
| e3    |            0 |         0 | –                               |
| e4    |            0 |         0 | –                               |

Dazu aus der eigenen Gegenprobe je eine Kastenzahl (180) in e2 und
e4, zeilenweise ersetzt.

## Entscheidungen

- Grundfall der Kette „Seite berechnen“ ist die erste Sprosse nach
  der Vorstufe (Bruch eintragen), nicht die mit „(4×)“ markierte
  Sinus-Sprosse; das Skript verlangt den Grundfall vor jeder höheren
  Sprosse.
- Jedes an der Prüfungshöhe genannte Original steht dort mit zwei
  Zeilen; sprosse_text ist der ganze Abschnitt „Prüfungshöhe: …“,
  weil das Skript einen Text je Sprosse verlangt.
- Originale außerhalb der Prüfungshöhe stehen an ihrer
  P10-Form-Sprosse (siehe oben); 2017-OS-K4c hat keine eigene Zeile.
- Pflicht darstellung entfällt in allen Einheiten: kein Typ trägt
  einen Darstellungswechsel außerhalb der Ketten.
- Zone-Paar an „Gleichung mit einem Bruch … umstellen“, Fallstrick
  Größe im Nenner (drei Originale, häufigster Umstellfehler).
- Zone-Folge: Fertigkeiten ab Einheit 1 in Eintragsfolge, dann
  Winkelsumme (Einheit 2), dann Einheiten und Figuren (Einheit 3);
  die Taschenrechner-Fertigkeit ohne sin-Taste (Zone nennt keinen
  Begriff des Themas).
- sin, cos, tan als `\mathrm{sin}\,` gesetzt, weil `\sin` im Skript
  als unbekannter Baustein gilt.
- Typen ohne Kette: e1 drei, e2 zwei, e3 einer, e4 keiner – die
  übrigen Typen stehen als Sprossen in der Kette.
- Die Vorrat-Sprossen der Kette „Sinussatz“ (Kosinussatz nach dem
  Winkel, Herleitung) stehen mit je drei Zeilen in der Kette.
- `\dreieck` zeigt keinen rechten Winkel; er steht im Aufgabentext.

## Befunde

- Katalog: Die Erkennungsschritte „Vom Winkel aus schauen“ (e1),
  „Seite oder Winkel gesucht?“ (e2), „Teildreieck nachfahren“ (e3),
  „Rechtwinklig oder nicht?“ und „Paare finden“ (e4) wiederholen die
  Vorstufe ihrer Einheit; sie entfallen, die Vorstufe bleibt.
- Katalog: Die Kette „Seite berechnen“ markiert „(4×)“ an der
  vierten Sprosse, bank.md setzt den Grundfall an die erste.
- bank.md: „kette der Zone ist die Fertigkeit bis zum Doppelpunkt“;
  nur eine Fertigkeitszeile hat einen, sonst bis zum Gedankenstrich.
- Prüfskript: `\sin`, `\cos`, `\tan` fehlen in STANDARD.
- Prüfskript: Ein pruef mit zwei Zahlen gilt bei ksys-Grafik als
  Punkt; Länge und Winkel (e2 s11 v11–v12) stehen deshalb mit den
  beiden abgelesenen Katheten in einer Liste aus vier Zahlen.
- Vorlage: `\dreieck` kennt keine Rechtwinkelmarke und keine Höhe;
  „eingezeichnete Höhe“ (e1 s16 v7–v8) zeigt nur das Dreieck.

## Offene Punkte

- Grafiken ungerendert (kein LaTeX); Lage und Beschriftung der
  Seiten sind aus den Koordinaten gerechnet, nicht angesehen.
- Bedeutung des Sterns der Sinussatz-Originale bleibt offen (Katalog).
- Rechtwinkelmarke und Höhe in `\dreieck` fehlen der Vorlage.

## Nachbesserung 2026-09-27

- Prüfskript v0.5: 0 Abweichungen, 0 Warnungen vor und nach der
  Nachbesserung; keine jsonl-Zeile geändert oder gestrichen.
- Prüfungshöhe: Alle vier Ketten enden auf einer Prüfungshöhe mit
  P10-Original; keine Prüfungshöhe ohne Original steht als hoehe
  sprosse, nichts umgestellt.
- Erkennungsschritte: Die fünf mit gleichem Handgriff waren schon
  entfallen (siehe Befunde); „sin, cos oder tan?“ und „Mal oder
  geteilt?“ (e1 k1, k2) verlangen einen anderen Handgriff als die
  Vorstufe (H, G, A beschriften) und bleiben.
- Befunde: Keiner ist mit v0.5 erledigt; `\sin` fehlt weiter in
  STANDARD, ein pruef mit zwei Zahlen gilt bei ksys weiter als
  Punkt.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- trigonometrie-e2-k1-s1-v2: „$\mathrm{sin}^{-1}(0{,}5556) \approx 33{,}7^\circ$“ falsch ($33{,}752^\circ$) → Umkehrtaste auf $\frac{5}{9}$ ($33{,}749^\circ \approx 33{,}7^\circ$), „$= 0{,}5556$“ → „$\approx 0{,}5556$“; pruef unverändert (Regel b).
- trigonometrie-e2-k1-s11-v5: $69{,}7^\circ$ folgte scheinbar aus $0{,}346$ (ergibt $69{,}757^\circ$) → „$\varepsilon = \mathrm{cos}^{-1}\left(\frac{9}{26}\right) \approx 69{,}7^\circ$“; pruef unverändert (Regel b).
- Prüfskript: Abweichungen 0.

## Nachtrag 2026-10-02: Duden-Abgleich und Leiterregeln

Katalog: mathe-nachhilfe katalog/trigonometrie.md, Commit 011af98 (Leiterregeln 02.10.2026). Neue Sprossen je 3 Zeilen, herkunft „Regel 02.10.“: e1 Kette 3 Rückwärts (s16), Prüfung jetzt s17; e2 Kette 1 Gemischt (s11), Prüfung s12; e3 Kette 1 Rückwärts (s17) und Gemischt (s18), Prüfung s19; e4 Kette 1 Gemischt (s16), Prüfung s17. Zusatzvarianten A14–A18 aus eingang/duden9-2026-10-02/neu-pyt-duden9.jsonl an den alten Sprossen (die Vorstufen e1 k3 s0 und e3 k1 s0 behalten ihren Kurztext, Altlast). Verschobene Prüfungszeilen tragen quelle 97–100 und den Katalogtext. ids in bank/_punkte.csv nachgezogen (50 Zeilen). Prüfskript ohne --katalog 0 Abweichungen, mit --katalog 250 → 208 (Rest alte quelle 39/40, 102–105).

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|---|---:|---:|---:|---:|---:|---:|
| e1 | 14 | 7 | 54 | 14 | 9 | 98 |
| e2 | 4 | 5 | 39 | 12 | 9 | 69 |
| e3 | 5 | 5 | 54 | 12 | 9 | 85 |
| e4 | 4 | 5 | 45 | 12 | 9 | 75 |
| zone | 0 | 18 | 19 | 0 | 1 | 38 |

Summe 365 Zeilen.
