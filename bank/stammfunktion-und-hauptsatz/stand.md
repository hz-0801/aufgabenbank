# Stand: stammfunktion-und-hauptsatz

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     25 |        0 |        10 |      14 |        0 |       1 |
| e1    |     32 |        4 |         5 |      12 |        5 |       6 |
| e2    |     27 |        0 |         5 |      12 |        4 |       6 |
| e3    |     32 |        4 |         5 |      12 |        5 |       6 |
| e4    |     34 |        4 |         5 |      15 |        4 |       6 |
| gesamt|    150 |       12 |        30 |      65 |       18 |      25 |

## Originale je Einheit

- e1: 2022MerhoehtBAnalysisWTR3-2a, 2020-be-gk-A1.1a,
  2018-be-gk-B1.2c, 2020MgrundlegendBAnalysisWTR2-1e,
  2024MerhoehtBAnalysisWTR1-1d, 2025MgrundlegendAAnalysis12-a,
  2026MgrundlegendBAnalysisWTR1-1d, 2020-be-gk-B2.1h,
  2024MgrundlegendBAnalysisWTR1-1f, 2026MerhoehtAAnalysis12-b,
  2023-bebb-gk-B2.1l (Prüfungshöhe)
- e2: 2023MgrundlegendAAnalysis13-a, 2018MgrundlegendBAnalysisWTR-1d,
  2026MerhoehtBAnalysisWTR3-1b, 2025MerhoehtBAnalysisWTR3-2c,
  2021MgrundlegendAAnalysis13-a, 2025-bebb-lk-B2.2b,
  2025-bebb-gk-B2.2d (Prüfungshöhe),
  2022MgrundlegendBAnalysisWTR1-1f (Prüfungshöhe),
  2017MerhoehtBAnalysisCAS1-2h, 2018MerhoehtBAnalysisCAS1-3c
- e3: 2023-bebb-gk-A1.2b, 2021MgrundlegendAAnalysis2-b,
  2023MerhoehtAAnalysis21-b, 2022MerhoehtAAnalysis11-a,
  2021MgrundlegendAAnalysis11-a, 2026-bb-gk-B2.1b, 2026-bb-ea-B2.1e,
  2019MgrundlegendBAnalysisWTR2-1e, 2022-bebb-lk-B2.1k,
  2024-bebb-gk-B2.1f, 2025MerhoehtBAnalysisMMS2-1c,
  2020MgrundlegendBAnalysisWTR2-1h (Prüfungshöhe)
- e4: 2018MerhoehtBAnalysisWTR1-1d, 2026MerhoehtAAnalysis23
  (Prüfungshöhe), 2026MerhoehtBAnalysisMMS1-1h (Prüfungshöhe),
  2017MerhoehtBAnalysisWTR2-1k, 2017MerhoehtBAnalysisWTR2-1j

## Prüfskript vor der Korrektur

| Datei | Abweichungen | häufigster Grund                  | Warnungen |
|-------|-------------:|-----------------------------------|----------:|
| zone  |            1 | pruef nicht an der Ergebnisstelle |         0 |
| e1    |            0 | –                                 |         0 |
| e2    |            0 | –                                 |         0 |
| e3    |            0 | –                                 |         0 |
| e4    |            0 | –                                 |         0 |

## Entscheidungen

- Integrale stehen in Worten („das Integral von 0 bis 2 über
  f(x)"), weil `\int` weder Baustein noch Standardbefehl des
  Prüfskripts ist (Befund).
- Zone: kette und sprosse_text enden am ersten Doppelpunkt, sonst
  vor „ – "; das Zone-Paar steht bei „Potenzen und Brüche rechnen"
  (Vorzeichen ungerader Potenzen, das meistbelegte Fehlermuster).
- Prüfungshöhen, deren Kennung die Mappe nicht in Abschnitt 2
  führt (e1 2026-bb-ea-B2.1f, e3 2025-bebb-lk-B2.2c), haben 3
  Zeilen mit original null neben den 2 Zeilen des Originals.
- e2: 2025MgrundlegendBAnalysisWTR2-1d bekommt keine Zeile, weil es
  die wortgleiche Dublette von 2025-bebb-gk-B2.2d ist.
- Nennt eine Sprosse mehrere Originale, trägt jede Variante ein
  anderes; der Grundfall trägt Originale nur auf einzelnen
  Varianten.
- Typen ohne Kette: e2 „Kurvenlänge …", e4 „… Verschiebung in
  y-Richtung …" und „Waagerechte Tangente und Wendepunkt …"; alle
  übrigen Typen stecken in Kettensprossen.
- Pflichtelemente nur fehler und begruenden, weil „Typen je
  Lerneinheit" nur diese nennt.
- Kastenzahlen: 12 und 13 (aus 13/12) gelten als mehrstellig;
  Jahres- und Belegangaben im Kasten nicht.
- Buchstaben: J für die Integralfunktion, L und M im Typ
  „Verschiebung" wie im Original, D für die Differenzfunktion der
  Sachaufgaben mit den Raten p und q.
- pruef bei Termen und Nachweisen: eine Zahl an der
  Ergebnisstelle; jeder Term mit sympy, jede Kurvenlänge mit
  mpmath nachgerechnet.

## Befunde

- Katalog: Der Erkennungsschritt „Ableiten oder aufleiten?"
  wiederholt die Vorstufe von e1 und entfällt; die Vorstufe bleibt.
- Katalog: Der Erkennungsschritt „Wer ist hier F, wer ist f?"
  wiederholt die Vorstufe von e3 und entfällt; die Vorstufe bleibt.
- Katalog: Der Erkennungsschritt „Wo ist das Integral null?"
  wiederholt die Vorstufe von e4 und entfällt; die Vorstufe bleibt.
- Katalog/Mappe: Sprossen nennen Kennungen, die die Mappe nicht
  aufnimmt (2026-bb-ea-B2.1f, 2025-bebb-lk-B2.2c,
  2018MerhoehtBAnalysisWTR1-1e/-1f, 2022MerhoehtBAnalysisWTR3-2c,
  2020-be-gk-A1.1b); diese Sprossen stehen ohne Original.
- Prüfskript: `\int` fehlt in STANDARD; jedes Integralzeichen
  gälte als unbekannter Baustein.
- Prüfskript: Die Sperre enthält kurze Schreibmuster aus Originalen
  wie „F(0)=0", „J(0)=0", „(x)+1", „e^x+1"; sie sperren
  Schreibweisen des Themas, keine Zahlbelegungen.
- Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die
  Gegenprobe lief mit eigenem Skript (0 Treffer).

## Offene Punkte

- Ohne Zeile: 2017-be-gk-B1.2d, 2022-bebb-gk-B2.2d,
  2023-bebb-lk-B2.1k, 2024-bebb-gk-B2.1e, 2020MerhoehtAAnalysis21-a
  (Nachweis, mehr Originale als Varianten), 2026-bb-gk-A1.7b und
  2026MgrundlegendAAnalysis22-b (e3 s5), 2017MerhoehtBAnalysisWTR2-1i
  (keiner Sprosse zugeordnet); Dubletten 2022-bebb-lk-A1.1a,
  2026-bb-gk-A1.1a, 2026MgrundlegendAAnalysis13-a (Kastenbeispiel),
  2025MgrundlegendBAnalysisWTR2-1d.
- Kurvenlänge ist im Katalog Ermessen; wandert der Typ, wandern
  die drei Zeilen mit.
- Kein LaTeX-Lauf; Grafiken nur auf Bausteinname und Bereich
  geprüft, `\funktion` mit atan rechnet in Grad (umgerechnet).
