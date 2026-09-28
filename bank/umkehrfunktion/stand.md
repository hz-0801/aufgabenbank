# Stand: umkehrfunktion

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
(2026-09-26, „katalog: Sek-II-Einträge auf die Katalogzeilen vom
27.09.“)
Datum: 2026-09-27

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     25 |        – |        10 |      14 |        – |       1 |
| e1    |     32 |        4 |         5 |       9 |        2 |      12 |
| e2    |     34 |        4 |         5 |       9 |        4 |      12 |

## Originale je Einheit

- e1: 2026MerhoehtBAnalysisWTR3-1e, 2025MerhoehtBAnalysisWTR2-1c,
  2017MerhoehtBAnalysisCAS2-3b
- e2: 2026MerhoehtBAnalysisWTR3-1g, 2025-bebb-lk-A1.5a,
  2025MerhoehtAAnalysis22

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                  |
|-------|-------------:|----------:|-----------------------------------|
| zone  |            2 |         0 | Ableseauftrag ohne grafik         |
| e1    |            5 |         0 | pruef nicht an der Ergebnisstelle |
| e2    |            1 |         0 | pruef nicht an der Ergebnisstelle |

Keine Einheit scheiterte zweimal.

## Entscheidungen

- Zone: alle Fertigkeiten ohne Doppelpunkt; kette ist der Text bis
  zum ersten „ – “.
- Zone: Folge des Eintrags (Einheit 1 vor 2); die Spiegelung an y = x
  (Fertigkeit 5) steht in der Zone, weil der Katalog sie als
  Voraussetzung führt.
- Grundfall e1: zum Term der Umkehrfunktion ein Funktionswert als
  Probe, damit die Lösung eine prüfbare Zahl trägt.
- Typ ohne Kette e1: Radius aus der Füllhöhe (Original
  2017MerhoehtBAnalysisCAS2-3b).
- e2 s4 (Trapez) ohne original: 2026MerhoehtBAnalysisWTR3-1h steht
  nicht in Abschnitt 2 der Mappe.
- Integrale in e2 in Worten („das Integral von 0 bis x_S über …“),
  weil das Prüfskript \int nicht kennt.
- Pflicht darstellung: sprosse_text aus der Grundvorstellung
  (Zeile 64), weil „Dazu:“ keinen Darstellungswechsel nennt.
- Anwendung e2: Kehrwert der Steigung an Wachstum, Geschwindigkeit
  und Wechselkurs, weil die Pool-Zeilen keinen Kontext haben.

## Befunde

- Katalog: beide Erkennungsschritte (Zeilen 31–32) wiederholen die
  Vorstufen der Ketten (Zeilen 66–67); nach bank.md entfallen sie.
- Mappe: 2026MerhoehtBAnalysisWTR3-1h wird in der Kette genannt, steht
  aber nicht in Abschnitt 2 („nur außerhalb von Prüfungsform“).
- Prüfskript: \int und \middle fehlen in STANDARD.
- Prüfskript: ein Bruch nach einem Wort („Steigung \frac{1}{14}“)
  gilt nicht als Ergebnisstelle, auch wenn er das Ergebnis ist.

## Offene Punkte

- ksys-Grafiken mit \funktionab (ln, Wurzel, Potenz mit
  Bruchexponent) sind nicht am Render geprüft (kein LaTeX).

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- umkehrfunktion-e2-k1-s3-v1: Lösung nannte den verlangten Berührpunkt nicht („Spiegelpunkt von Q“), pruef leer → $Q(2\,\mathrm{ln}\,3 | 0)$ und Berührpunkt mit g $(0 | 2\,\mathrm{ln}\,3) \approx (0 | 2{,}20)$ ergänzt, pruef `[0, 2*math.log(3)]` (Regel a).
- umkehrfunktion-e2-k1-s4-v2: Lösung ohne die verlangte Begründung des Trapezes → Satz „AA' und BB' stehen senkrecht auf y = x, sind also parallel“ ergänzt, Fläche 30 bestätigt (Regel a).
- Prüfskript: Abweichungen 0.
