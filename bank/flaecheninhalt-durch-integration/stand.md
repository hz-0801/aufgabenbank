# Stand: flaecheninhalt-durch-integration

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
(2026-09-26T16:47:30+02:00)
Datum: 2026-09-27 (14:39 UTC)
Prüfskript: bank-pruef.py v0.5, bank.md Stand 2026-09-27b

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        – |        12 |      13 |        – |       1 |    26 |
| e1    |        4 |         5 |      12 |        6 |       9 |    36 |
| e2    |        4 |         5 |      15 |        4 |       9 |    37 |
| e3    |        4 |         5 |      12 |        6 |      12 |    39 |
| e4    |        4 |         5 |      12 |        4 |       9 |    34 |
| e5    |        4 |         5 |      15 |        8 |      12 |    44 |

Pflicht je Einheit: fehler 3, begruenden 3, anwendung 3; darstellung
3 nur in e3 und e5.

## Originale je Einheit

- e1: 2024-bebb-lk-B2.1k, 2017MerhoehtAAnalysis2-a, 2021-B-1f
- e2: 2025MerhoehtBAnalysisMMS1-1d, 2023-C-2d
- e3: 2024-bebb-gk-B2.2e, 2020-be-gk-B2.2g, 2025-C-2c
- e4: 2025MgrundlegendBAnalysisWTR1-1d, 2026MerhoehtBAnalysisMMS2-2e
- e5: 2025-bebb-lk-B2.1d, 2025MerhoehtBAnalysisWTR2-1d,
  2019MgrundlegendBAnalysisWTR1-2e, 2024-bebb-lk-B2.1j

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund             |
|-------|-------------:|----------:|------------------------------|
| zone  |            0 |         0 | –                            |
| e1    |            0 |         0 | –                            |
| e2    |            2 |         0 | Sperre (Term aus Kasten/Orig.) |
| e3    |            3 |         0 | Sperre (Zahlenpaar, Term)    |
| e4    |            1 |         0 | Sperre (Zahlenpaar)          |
| e5    |            0 |         0 | –                            |

e3 und e4 brauchten je zwei Korrekturläufe: Der Ersatzpunkt traf
erneut die Paarsperre.

## Entscheidungen

- Integrale stehen als „Integral von a bis b über f(x)“, weil das
  Prüfskript `\int` nicht kennt.
- Prüfungshöhe: je Teil der Prüfungshöhe die erste Kennung, die in
  Abschnitt 2 der Mappe steht; Pooldubletten nur einmal.
- Teile der Prüfungshöhe ohne Kennung in der Mappe entfallen, statt
  sie mit original null zu führen (siehe Befunde).
- sprosse_text der Prüfungshöhe ist der Katalogtext ohne die
  Belegklammern, weil der Katalog Sprosse und Belege verschränkt.
- Zone: kette bis Doppelpunkt oder Gedankenstrich (Zeile 34 hat
  keinen Doppelpunkt), je Fertigkeit ein Fallstrick.
- Zone-Paar bei Fertigkeit 1: Vorzeichen an der unteren Grenze,
  nach „Typische Fehler“ Zeile 93 der häufigste Rechenfehler.
- darstellung nur in e3 und e5, wo Typen das Markieren oder
  Einzeichnen tragen; in e4 steckt es schon in Sprosse 4.
- Pflicht-sprosse_text: „Fehler finden“ und „Begründen“ aus der
  Typenzeile, anwendung und darstellung je ein Typname der Einheit.
- Kästchenzählen (e5): Grafik mit xstep=1, ystep=1; die Lösung nennt
  den genauen Wert, weil das Karo der Vorlage hier nicht bekannt ist.
- Fehlerregel „scheitert zweimal“ gelesen als zwei erfolglose
  Korrekturläufe; der erste Lauf mit Abweichungen zählt nicht.

## Befunde

- Katalog: Die Erkennungsschritte (Zeilen 41–44) wiederholen die
  Vorstufen von e1, e2, e3 und e5; sie entfallen, die Vorstufen
  bleiben.
- Prüfskript: `\int` und `\ln` fehlen in der Liste STANDARD;
  Sek-II-Integrale müssen in Worten stehen.
- Mappe: Kennungen aus den Prüfungshöhen fehlen in Abschnitt 2:
  2026-bb-gk-B2.2d, 2026MgrundlegendBAnalysisWTR2-1d,
  2025-bebb-lk-B2.1e, 2026MgrundlegendBAnalysisMMS2-1f,
  2020MgrundlegendBAnalysisWTR1-1f, 2022-bebb-gk-B2.2i,
  2025MerhoehtBAnalysisWTR2-1e, 2026MerhoehtBAnalysisWTR3-1c,
  2019MgrundlegendBAnalysisWTR1-3d.
- Prüfskript: Die Paarsperre trifft Allerweltspunkte wie (0|1) und
  (0|2), die im Original nur Nebenangaben sind.
- Katalog: Zeile 30 nennt Nachträge vom 28. und 29.09.2026, der
  Katalog-Commit ist vom 26.09.2026.

## Offene Punkte

- Kästcheninhalt der e5-Grafiken beim Zusammenbau am Karo prüfen.
- Die entfallenen Prüfungshöhe-Teile nachziehen, sobald die Mappe
  ihre Kennungen führt.
- Wenn das Prüfskript `\int` kennt, die Integrale auf die
  Formelschreibweise umstellen.
