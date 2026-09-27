# Stand: ableitungsregeln

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.4, nachgeprüft mit v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     30 |        0 |        14 |      15 |        0 |       1 |
| e1    |     47 |        8 |         5 |      24 |        4 |       6 |
| e2    |     29 |        4 |         5 |      12 |        2 |       6 |
| e3    |     32 |        4 |         5 |      15 |        2 |       6 |
| gesamt|    138 |       16 |        29 |      66 |        8 |      19 |

## Originale je Einheit

- e1: 2026-C-1c, 2025-C-1c, 2026-B-1c, 2019-be-gk-A1.1a, 2024-C-1c,
  2021MerhoehtAAnalysis12-a, 2025-bebb-lk-B2.1b,
  2022MgrundlegendBAnalysisWTR1-1c, 2024-B-1d (Prüfungshöhe),
  2023-C-1b (Prüfungshöhe), 2022-B-1a, 2021-A-1a
- e2: 2024MerhoehtAAnalysis23, 2020MerhoehtAAnalysis22
  (Prüfungshöhe), 2017MerhoehtBAnalysisWTR1-3d
- e3: 2021MerhoehtAAnalysis13-a, 2022-bebb-lk-B2.2b,
  2022MerhoehtBAnalysisWTR2-1b, 2024MgrundlegendBAnalysisWTR1-1a,
  2022-bebb-lk-A1.4a, 2020-be-gk-B2.1c, 2024-bebb-lk-B2.1d,
  2018-bb-ea-B2.1e, 2026MgrundlegendAAnalysis21-b,
  2025MerhoehtAAnalysis21-a (Prüfungshöhe)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | häufigster Grund                  | Warnungen |
|-------|-------------:|-----------------------------------|----------:|
| zone  |            0 | –                                 |         0 |
| e1    |           12 | original unvollständig (11)       |         0 |
| e2    |            8 | original unvollständig (8)        |         0 |
| e3    |           17 | original unvollständig (17)       |         0 |

Echte Abweichungen darunter: e1 ein falsches pruef, e2 eine Sperre
(f(0) = 1) und ein fehlendes pruef. Nach der Korrektur bleiben 37
Abweichungen, alle „original unvollständig" (Befund 1).

v0.5: 0 Abweichungen, 0 Warnungen, ohne Änderung an den jsonl;
auch die Sperre für x⁴, x⁵ aus der Mappe trifft keine Aufgabe.

## Entscheidungen

- Zone: kette und sprosse_text enden am ersten Doppelpunkt, sonst
  vor „ – ", weil die Fertigkeitszeilen „was – wofür" schreiben.
- Zone: je Fertigkeit ein Fallstrick; das Zone-Paar steht bei den
  Potenzen (Vorfaktor und Exponent), dem meistbelegten Muster.
- e1 s2 trägt original null; die fhr-Originale mit drei
  Ableitungen stehen an s3 und am Typ „Verhalten im Unendlichen".
- „Verhalten im Unendlichen bestimmen" ist Typ ohne Kette in e1,
  mit Grenzverhalten und drei Ableitungen wie die fhr-Originale.
- Pflichtelemente nur fehler und begruenden, weil „Typen je
  Lerneinheit" nur diese nennt; keine anwendung, keine darstellung.
- Prüfkennung: „(FHR Jahr)", sonst „(Abitur Jahr GK|LK)"; iqb
  grundlegend und be-gk = GK, iqb erhöht, bebb-lk und bb-ea = LK.
- sin, cos, ln als `\mathrm{…}`, weil `\sin`, `\cos`, `\ln` weder
  Standard noch Baustein sind; sin' und cos' stehen im Aufgabentext.
- pruef bei Termen: die Zahlen an der Ergebnisstelle (meist
  Leitkoeffizienten); jeder Term zusätzlich mit sympy nachgerechnet.
- Fünf Originale ohne Nennung in einer Kettensprosse bekommen keine
  Zeile (siehe Offene Punkte).
- Gegenprobe Kastenzahlen: 0,5, 10, 27, 40, 120 gelten als
  mehrstellig; zwölf Aufgaben nachträglich geändert (0932acf).

## Befunde

- Prüfskript: KENNUNG verwirft Landesabitur-Kennungen
  (2019-be-gk-A1.1a) und IQB-Kennungen mit Kleinbuchstaben
  (2021MerhoehtAAnalysis12-a); die Kennungen sind nach Mappe
  richtig. (v0.5)
- Prüfskript: Die Sperre vergleicht x⁴, x⁵ der Mappe nicht mit x^4,
  x^5 der Bank; Terme ab Exponent 4 sind damit nie gesperrt. (v0.5)
- Prüfskript: pruef sieht bei Termen nur die erste Zahl; zwei
  fehlende Klammern in e3 s5 fand erst die Durchsicht.
- Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die zwölf
  Treffer der Gegenprobe meldete es nicht.
- Katalog: Der Erkennungsschritt „Welche Regel?" wiederholt die
  Vorstufe von e1 und entfällt; die Vorstufe bleibt.
- Katalog: Der Erkennungsschritt „Innen und außen?" wiederholt die
  Vorstufe von e2 und entfällt; die Vorstufe bleibt.
- Katalog: Die Fertigkeitszeilen der Voraussetzungen haben keinen
  Doppelpunkt, die Zone-Regel von bank.md greift nur bei „Terme
  umformen".
- Katalog: e1 s2 nennt Originale, deren Form (drei Ableitungen)
  erst s3 einführt.

## Offene Punkte

- Ohne Zeile: 2017-be-gk-B1.2a, 2017-be-gk-cas-B1.2b,
  2018-bb-ea-cas-B2.1e, 2017MgrundlegendBAnalysisWTR-1d,
  2017MerhoehtBAnalysisWTR2-1d.
- Verhalten im Unendlichen und die Sinusableitung sind im Katalog
  Ermessen; wandern sie in andere Einträge, wandern die Zeilen mit.
- Kein LaTeX-Lauf; Grafiken (ksys mit \parabel, \gerade,
  \tangentean) sind nur auf Bausteinname und Bereich geprüft.
