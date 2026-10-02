# Stand: symmetrie-abbildungen

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
Datum: 2026-09-27 12:18 UTC
Prüfskript: bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen
(Nachbesserung 2026-09-27; vorher v0.4, 0 Abweichungen,
2 Warnungen)

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     30 |        0 |        14 |      15 |        0 |       1 |
| e1    |     54 |        8 |         5 |      27 |        2 |      12 |
| e2    |     87 |       12 |        10 |      45 |        8 |      12 |
| e3    |     54 |        4 |         5 |      30 |        3 |      12 |

## Originale je Einheit

- e1: 2020-OS-B1b
- e2: 2022-OS-B1i, 2021-OS-B1j, 2025-OS-K2a, 2018-OS-B1h
- e3: keins (Prüfungshöhe ohne Original, 3 Zeilen)

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                          |
|-------|-----:|------:|-------------------------------------------|
| zone  |   23 |     0 | pruef als Zahl statt Ausdruck (16)        |
| e1    |    4 |     0 | pruef nicht an der Ergebnisstelle (3)     |
| e2    |    5 |     2 | Ergebnisstelle der Tabellenlösung (3)     |
| e3    |    5 |     0 | Ergebnisstelle der Verschiebung (3)       |

(erledigt v0.5) Die 2 Warnungen in e2 bleiben (siehe
Entscheidungen, Punkt 4).

## Entscheidungen

1. Zone: kette und sprosse_text sind die Fertigkeit bis zum
   Gedankenstrich; die Zeilen haben keinen Doppelpunkt.
2. Zone-Paar in „Kästchen im Raster abzählen …“ (Fallstrick Linien
   statt Kästchen), weil diese Fertigkeit alle Einheiten trägt.
3. (überholt, siehe Nachbesserung) Einheit 2: hoehe pruefung an
   der letzten Kette (Spiegeln, 2018-OS-B1h); die Prüfungshöhe der
   Kette Symmetrieachsen steht als s9 (2022-OS-B1i, 2021-OS-B1j)
   und s10 (2025-OS-K2a) mit hoehe sprosse, 2 Zeilen je Original,
   Feld original gesetzt.
4. (überholt, siehe Nachbesserung) Daraus die Mengenwarnungen s9
   (4 statt 3) und s10 (2 statt 3).
5. 2025-OS-K2a nur mit der ersten Teilleistung (Achsenzahl); die
   Rechnung mit den Diagonalen gehört zu pythagoras.md.
6. Senkrechte Spiegelachse im ksys als `\asymptote{x=…}{a}`,
   waagerechte und schräge als `\gerade`; ksys hat keine
   senkrechte Gerade.
7. Verschiebungspfeil als Punktpaar P → Q im ksys, weil die
   Vorlage keinen ebenen Pfeil hat.
8. Typen ohne Kette: e1 drei, e2 zwei („[GYM 6]“ nicht im Text),
   e3 zwei; „Abbildung benennen, die zwei gegebene Figuren
   ineinander überführt“ steckt in der Prüfungshöhe von e3.
9. Einheit 2 nennt die Spiegelachse durchgehend a, auch in der
   Prüfungshöhe statt g des Originals.

## Befunde

- Katalog: „Welche Koordinate ist null?“, „Passt die Faltung?“,
  „Senkrecht zur Achse?“, „Welche Abbildung?“ und „Gleich groß?“
  wiederholen als Erkennungsschritt die Vorstufe derselben Einheit
  (Ankreuzen); sie entfallen, die Vorstufen bleiben.
- Katalog: „Erst rechts, dann hoch“ und „Wie viele Achsen?“ stehen
  als Erkennungsschritt (zeichnen) und in der Vorstufe (ankreuzen);
  beide bleiben, weil der Handgriff verschieden ist.
- (erledigt v0.5) bank.md: Für die Prüfungssprosse einer
  Verfahrenskette, die nicht die letzte ist, nennt „Mengen je
  Kette“ keine Menge; das Skript erwartet 3.
- Prüfskript: pruef als JSON-Zahl bricht mit einem eval-Fehler ab;
  bank.md sagt nicht, dass pruef ein String sein muss.
- Prüfskript: „$2$ nach rechts, dann $8$ nach oben“ gilt nicht als
  Aufzählung von Ergebnissen; nur „$2$, $8$“ besteht.
- bank.md: Die Prüfungshöhe der Kette Symmetrieachsen nennt im
  Katalog zwei Prüfungsformen; die Bank führt sie als s9 und s10,
  beide hoehe pruefung. „hoehe pruefung bleibt der letzten Sprosse
  vorbehalten“ regelt diesen Fall nicht.

## Offene Punkte

- Nicht kompiliert: `\asymptote` im Unterstufen-ksys und die
  Optionen `achsen=…`/`diagonalen` von `\drachen`, `\raute`,
  `\viereck` sind im Render ungeprüft.
- Buchstaben und Verkehrszeichen (e2 s7) stehen ohne Grafik; die
  Vorlage hat dafür keinen Baustein.

## Nachbesserung 2026-09-27

- e2 k2 s9 und s10 (Prüfungshöhe der Kette Symmetrieachsen, sechs
  Zeilen, 2 je Original) tragen hoehe pruefung statt sprosse, weil
  bank.md die Prüfungshöhe der letzten Sprosse jeder
  Verfahrenskette gibt; die zwei Mengenwarnungen entfallen.
- Tabelle „Zeilen je Datei und hoehe“ und Kopfzeile Prüfskript auf
  den neuen Stand gebracht; Entscheidungen 3 und 4 sind überholt.
- Prüfungshöhe ohne Original: e3 k1 s10 steht schon als hoehe
  pruefung mit original null; nichts umgestellt.
- Erkennungsschritte: „Erst rechts, dann hoch“ (e1 k1) und „Wie
  viele Achsen?“ (e2 k1) verlangen Zeichnen, die Vorstufen
  Ankreuzen; beide bleiben, keine Streichung.
- Befund JSON-Zahl in pruef: v0.5 bricht nicht mehr ab, sondern
  meldet eine Abweichung; bank.md sagt weiter nicht, dass pruef
  ein String ist, der Befund bleibt.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- symmetrie-abbildungen-e2-k2-s4-v3: Grafik \dreieck{(0,0)}{(5,0)}{(1,3)} war gleichschenklig (AB = BC = 5) gegen Text „drei verschieden lange Seiten“ und Lösung 0 → dritte Ecke (1.5,3), Seiten 5; 4,61; 3,35, Lösung 0 bleibt (Regel a).
- Prüfskript: Abweichungen 0.

## Nachtrag 2026-10-02: Duden-Abgleich und Leiterregeln

Katalog: mathe-nachhilfe katalog/symmetrie-abbildungen.md, Commit 2e7f1ee (Leiterregeln 02.10.2026; der Duden-Abgleich weist dem Eintrag nichts zu). Neue Sprossen je 3 Zeilen, herkunft „Regel 02.10.“: e1 Kette 2 Rückwärts (s8) und Gemischt (s9), Prüfung jetzt s10; e2 Kette 2 Rückwärts (s9) und Gemischt (s10), Prüfungssprossen jetzt s11 und s12; e2 Kette 3 Rückwärts (s8) und Gemischt (s9), Prüfung s10; e3 Kette 1 Rückwärts (s10) und Gemischt (s11), Prüfung s12. Verschobene Zeilen tragen quelle 73–76 und den Sprossentext wortgleich aus dem Katalog; ids in bank/_punkte.csv nachgezogen (10 Zeilen). Prüfskript ohne --katalog 0 Abweichungen, mit --katalog 170 → 157 (Rest alte quelle).

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|---|---:|---:|---:|---:|---:|---:|
| e1 | 8 | 5 | 33 | 2 | 12 | 60 |
| e2 | 12 | 10 | 57 | 8 | 12 | 99 |
| e3 | 4 | 5 | 36 | 3 | 12 | 60 |
| zone | 0 | 14 | 15 | 0 | 1 | 30 |

Summe 249 Zeilen.
