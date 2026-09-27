# Stand: funktionsklassen-und-eigenschaften

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
(2026-09-26, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“)
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     28 |        0 |        12 |      15 |        0 |       1 |
| e1    |     51 |        4 |         5 |      24 |        6 |      12 |
| e2    |     48 |        4 |         5 |      24 |        6 |       9 |
| e3    |     30 |        0 |         5 |      12 |        4 |       9 |
| e4    |     39 |        4 |         5 |      18 |        6 |       6 |
| e5    |     49 |        4 |         5 |      24 |        4 |      12 |
| e6    |     51 |        4 |         5 |      24 |        6 |      12 |
| Summe |    296 |       20 |        42 |     141 |       32 |      61 |

## Originale je Einheit

- e1: 2025-A-1d, 2024-bebb-lk-B2.2g, 2025MerhoehtBAnalysisWTR1-2b
- e2: 2026-B-1b, 2023-bebb-gk-B2.2a, 2023MerhoehtBAnalysisWTR1-1a
- e3: 2017-bb-ea-B2.1a, 2024MerhoehtBAnalysisWTR1-1e
- e4: 2026-B-1a, 2022-bebb-lk-B2.2a, 2021MerhoehtAAnalysis21-b
- e5: 2026-bb-ea-A1.5b, 2026MerhoehtBAnalysisMMS1-1d
- e6: 2023-C-1e, 2026MgrundlegendAAnalysis12-a,
  2023MgrundlegendAAnalysis13-b

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                          |
|-------|-----:|------:|-------------------------------------------|
| zone  |    1 |     0 | Sperre (Term aus einem Original)          |
| e1    |    0 |     0 | –                                         |
| e2    |    5 |     0 | grafik verlangt: Ankreuzoption „ablesen“  |
| e3    |    1 |     0 | Sperre (Zahlenpaar aus einem Original)    |
| e4    |    2 |     0 | Baustein \lim unbekannt                   |
| e5    |    4 |     0 | grafik verlangt: „Abbildung“ = Transform. |
| e6    |    1 |     0 | Sperre (Term aus einem Original)          |

Keine Einheit ist zweimal gescheitert.

## Entscheidungen

- Prüfungshöhe: je Einheit eine Sprosse mit sprosse_text
  „Prüfungshöhe“ (wortgleich im Katalog); sie trägt alle
  Zielmarken-Originale der Einheit aus Abschnitt 2, je 2 Zeilen.
- Kennungen der Prüfungshöhe, die nicht in Abschnitt 2 der Mappe
  stehen (etwa 2023MerhoehtBAnalysisWTR2-2c), bekommen keine Zeile.
- e6: 2026-bb-gk-A1.4a ist wortgleiche Dublette von
  2026MgrundlegendAAnalysis12-a und steht nur einmal (iqb, GK).
- Pflichtelemente: e1, e5, e6 alle vier; e2, e3 ohne Darstellung;
  e4 nur Fehler und Begründen – die Typen tragen nicht mehr.
- Anwendung und Darstellung tragen als sprosse_text einen Typnamen
  aus „Typen je Lerneinheit“ (quelle 27 bis 32).
- Typen ohne Kette nur in e1 (Werte a mit Lösungsanzahl) und e2
  (Nullstellenzahl aus Grenzverhalten und Tiefpunkt); die übrigen
  Typen decken die Kettensprossen.
- Zone nach erster Verwendung: Termwerte, lineare Funktionen,
  Maßstab (e1), quadratische Gleichungen (e2), Grundgraphen (e3),
  Spiegeln (e4); das Zone-Paar hängt an Termwerte (dritte Potenz).
- e1 Sprosse 3: „Steigung dort“ als Ableitungswert an der Stelle
  null eines ganzrationalen Terms.
- Zeichnen mit selbst gewählter Achseneinteilung (e6 s4, s10):
  grafik ist \wertetabelleleer, die Lösungsgrafik das ksys.
- Grenzwerte als \mathrm{lim} geschrieben, weil das Prüfskript
  \lim als Baustein ablehnt.

## Befunde

- Katalog: Die Erkennungsschritte vor e1, e2, e4 und e5 sind
  wortgleich die Vorstufen der Ketten; sie entfallen, die Vorstufe
  bleibt (bank.md, Mengen je Kette).
- Katalog: Die Ketten nennen den Grundfall „viermal“, bank.md
  verlangt 5 Zeilen; geschrieben sind 5.
- Mappe: Die Prüfungshöhen der Ketten nennen viele Kennungen, die
  Abschnitt 2 nicht aufnimmt; sie sind so nicht verfremdbar.
- Prüfskript: \lim fehlt in der Liste der Standardbefehle und wird
  als unbekannter Baustein gemeldet.
- Prüfskript: Der Ableseauftrag greift bei „Abbildung“ im Sinn von
  Transformation und bei der Ankreuzoption „ablesen“.

## Offene Punkte

- Eine Figur ohne Achsen (e6 Sprosse 6) gibt es als Baustein nicht;
  die Zeilen sind Textaufgaben mit Maßangaben.
- Ein leeres Karofeld ohne vorgegebene Achsen fehlt; für freie
  Achseneinteilung steht \wertetabelleleer als Behelf.
- Nicht kompiliert (kein LaTeX in der Sitzung).
