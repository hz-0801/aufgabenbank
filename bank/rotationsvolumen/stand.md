# Stand: rotationsvolumen

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
(2026-09-26, „katalog: Sek-II-Einträge auf die Katalogzeilen vom
27.09.“)
Datum: 2026-09-27
bank.md: Stand 2026-09-27b; Prüfskript v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     25 |      – |      10 |      14 |      – |       1 |
| e1    |     31 |      4 |       5 |       9 |      4 |       9 |
| e2    |     31 |      4 |       5 |       9 |      4 |       9 |

## Originale je Einheit

- e1 Prüfungshöhe: 2018MerhoehtBAnalysisWTR2-2b, 2019-A-2d; Kette:
  2020-C-2b, 2024-C-2c, 2018MerhoehtBAnalysisWTR2-2a,
  2017MerhoehtBAnalysisWTR2-2e
- e2 Prüfungshöhe: 2017-bb-ea-B2.1f, 2026MerhoehtBAnalysisWTR3-1d;
  Kette: 2022MerhoehtBAnalysisWTR3-2b, 2018-bb-ea-B2.1h,
  2017MerhoehtBAnalysisWTR2-2d, 2023MerhoehtAAnalysis13-b,
  2017-bb-ea-B2.1d, 2018-bb-ea-B2.1i

## Prüfskript vor der Korrektur

- zone: 0 Abweichungen, 0 Warnungen
- e1: 0 Abweichungen, 0 Warnungen
- e2: 0 Abweichungen, 0 Warnungen

Keine Korrektur nötig; keine Einheit ist gescheitert.

## Entscheidungen

1. Integrale stehen als „Integral von a bis b über …“, weil das
   Prüfskript `\int` nicht kennt (Befund); der Katalog schreibt
   selbst „π · Integral über …“.
2. Zone: kette und sprosse_text sind die Fertigkeit bis zum
   Doppelpunkt, ohne Doppelpunkt bis zum Gedankenstrich; Folge wie
   im Katalog (vier Fertigkeiten für Einheit 1, dann Pythagoras
   für Einheit 2); das Zone-Paar (gemischtes Glied) steht in
   „Binomisch quadrieren“.
3. Prüfungshöhe mit zwei Originalen: sprosse_text ist der ganze
   Abschnitt ab „Prüfungshöhe:“ wortgleich; die fhr-Zielmarke
   2019-A-2d zählt als zweites Original von e1 (2 Zeilen).
4. Originale an Kettensprossen: je Sprosse höchstens eine
   Variante je Original; die Zielmarken 2017MerhoehtBAnalysisWTR2-2e
   (e1 s4) und 2017MerhoehtBAnalysisWTR2-2d (e2 s2) stehen an der
   Sprosse ihres Typs, nicht in der Prüfungshöhe.
5. 2019-A-2e (Sprosse „zusammengesetzte Körper“) steht nicht in
   Abschnitt 2 der Mappe; die Sprosse trägt kein Original.
6. Pflichtelemente: fehler, begruenden, anwendung je 3;
   darstellung entfällt (kein Darstellungswechsel unter „Dazu“).
7. Anwendung: sprosse_text ist ein Typ der Einheit aus „Typen je
   Lerneinheit“ (Rotationsvolumen berechnen; Querschnittsfläche
   als Term der Füllhöhe).
8. Kastenzahlen: der Merkkasten hat außer Kennungen keine
   mehrstelligen Zahlen; gesperrt blieben f(x) = x + 1 und
   (x + 1)².
9. Prüfkennung FHR als „(FHR Jahr)“, papier A oder C nach der
   Mappe.

## Befunde

- Katalog: Beide Erkennungsschritte („Was rotiert um welche
  Achse?“, Zeile 31; „Was ist hier der Radius?“, Zeile 32) sind
  zugleich Vorstufen der Ketten e1 und e2 (Zeilen 64, 65); sie
  entfallen, die Vorstufe bleibt.
- Katalog: Die Sprossenzeilen nennen den Grundfall „viermal“,
  bank.md fünf Zeilen; bank.md angewandt.
- Katalog: Zeile 21 nennt einen Nachtrag vom 28.09.2026, der
  Katalog-Commit ist vom 26.09.2026.
- Katalog: Die Zielmarke nennt für e1 auch
  2018-bb-ea-cas-B2.1h (Materialabzug), die Sprossenzeile nicht;
  die Prüfungshöhe folgt der Sprossenzeile.
- Prüfskript: `\int` fehlt in der Liste STANDARD; ein
  Integralzeichen führt zu „Baustein nicht in _bausteine.md“.

## Offene Punkte

- Die Integral-Schreibweise („Integral von … bis … über …“) ist
  bankweit nicht einheitlich (andere Einträge nutzen ∫); zu
  entscheiden, sobald das Prüfskript `\int` kennt.
