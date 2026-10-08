# Stand: kenngroessen-von-verteilungen

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, alle Dateien 0 Abweichungen,
0 Warnungen.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     26 |        0 |        12 |      13 |        0 |       1 |
| e1    |     43 |        4 |         5 |      18 |        4 |      12 |
| e2    |     50 |        4 |         5 |      30 |        2 |       9 |
| e3    |     38 |        4 |         5 |      15 |        2 |      12 |
| e4    |     29 |        4 |         5 |       6 |        2 |      12 |
| Summe |    186 |       16 |        32 |      82 |       10 |      46 |

## Originale je Einheit

- e1: 2018-bb-ea-A1.3b, 2018-be-gk-B3.1d, 2023-bebb-gk-B4.2b,
  2021-B-3e, 2023-bebb-gk-B4.2a, 2023MerhoehtBStochastikWTR1-3b,
  2022-bebb-gk-B4c, 2017MerhoehtBStochastikCAS1-5
- e2: 2025-bebb-lk-A1.4b, 2017-bb-ea-A1.3b, 2026-bb-ea-A1.9b,
  2018-be-gk-B3.1e, 2023-bebb-gk-B4.2c, 2023-bebb-lk-A1.7b,
  2022-bebb-lk-B4l, 2024-bebb-lk-A1.10a, 2024-bebb-gk-B4.2c,
  2021-be-gk-B4i, 2023-bebb-lk-B4g
- e3: 2017MgrundlegendAStochastik11-b, 2026-bb-gk-A1.9a,
  2017MgrundlegendBStochastikWTR2-2b,
  2024MgrundlegendBStochastikWTR2-3,
  2017MgrundlegendBStochastikWTR2-2a
- e4: 2026-bb-gk-A1.6a, 2025-bebb-gk-A1.9a, 2026-bb-ea-A1.4b

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                          |
|-------|-----:|------:|-------------------------------------------|
| zone  |    8 |     0 | merkmal je Sprosse uneinheitlich (6)      |
| e1    |    2 |     0 | pruef fehlt bei Deutungszeilen (2)        |
| e2    |    3 |     4 | pruef fehlt bei Begründen-Typ (3)         |
| e3    |    2 |     0 | \binom kein Baustein; Sperre p = 0,5 (je 1) |
| e4    |    3 |     0 | Zahl nicht an der Ergebnisstelle (2)      |

Warnungen e2: Pool-Dublette als zwei Originale mit je 1 Zeile.
Gegenprobe außerhalb des Skripts: eine Kastenzahl (20) in e3,
ersetzt.

## Entscheidungen

- Zone: Die Fertigkeitszeilen haben keinen Doppelpunkt; kette und
  sprosse_text sind der Text bis zum Gedankenstrich.
- Zone: Fertigkeiten in Katalogfolge f1–f6, je ein Fallstrick;
  das Zone-Paar steht in f2 (Reihenfolgen-Faktor, das Muster mit
  den meisten Belegen in „Typische Fehler“).
- Pflicht-Ketten: Sprosse 1 fehler, 2 begruenden, dann
  darstellung und anwendung; sprosse_text der beiden letzten ist
  ein Stück der Lerneinheitszeile (quelle 11, 13, 15, 17).
- Darstellung in e1, e3, e4; e2 ohne, weil ihre Typen reine
  Gleichungsansätze sind.
- Typen ohne Kette sind die Typen, die keine Sprosse übt (e1 3,
  e2 7, e3 2, e4 0); die Schranken-Begründung der e2 steht dort,
  weil ihr Beleg nicht in Abschnitt 2 der Mappe steht.
- Das Feld original steht auch an Mittelsprossen und Typen ohne
  Kette, wo die Zeile ein Original aus Abschnitt 2 verfremdet.
- Pool-Dubletten (2024-bebb-lk-A1.10a = 2024MerhoehtAStochastik22,
  2026-bb-ea-A1.4b = 2026MerhoehtAStochastik11-b) zählen als ein
  Original mit 2 Zeilen unter der abi-Kennung.
- e3 Prüfungshöhe: der Graph ohne Achsenzahlen ist in Kästchen
  beschrieben, grafik leer (siehe Befunde).
- Deutungs- und Begründen-Zeilen außerhalb pflicht mit Ziffern in
  der Lösung tragen pruef auf die erste Ergebniszahl.
- p = 0,5 steht in Aufgaben als „Trefferwahrscheinlichkeit
  50 %“, weil die Sperre p = 0,5 aus dem Merkkasten trifft.

## Befunde

- Katalog: Die Erkennungsschritte „Auszahlung oder Gewinn?“,
  „Vorwärts oder rückwärts?“ und „Welche Formel für die
  Standardabweichung?“ wiederholen je die Vorstufe der Kette ihrer
  Einheit; sie entfallen, die Vorstufen bleiben.
- Katalog: Die Sprossen nennen den Grundfall „viermal“, bank.md
  verlangt 5 Zeilen; die Bank folgt bank.md.
- Katalog: Die Prüfungshöhe von „Streuung“ sagt, die Kennung der
  Achsenskalierung bleibe außerhalb der Sprossen; die Mappe führt
  2024MgrundlegendBStochastikWTR2-3 aber in Abschnitt 2, sie ist
  verwendet.
- Katalog/Mappe: Viele Sprossen-Belege (etwa
  2019MgrundlegendBStochastikWTR3-2b) stehen nicht in Abschnitt 2
  und sind darum als original nicht verwendbar.
- Vorlage: ksys beschriftet die Achsen immer; eine Grafik zur
  Achsenskalierung ohne Zahlen ist nicht baubar.
- Bausteine: \binom fehlt in _bausteine.md; der
  Binomialkoeffizient steht als Fakultätenbruch.
- Prüfskript: Pool-Dubletten zählen als zwei Originale und
  verlangen je 2 Zeilen, obwohl es dieselbe Aufgabe ist.
- Prüfskript: „pruef fehlt“ trifft Begründen-Typen ohne Kette mit
  Ziffern in der Lösung; bank.md erlaubt dort "".

## Offene Punkte

- Nicht verfremdet sind 2017-bb-ea-B4.1c (nur als Fehler-finden-
  Muster), 2019-be-gk-B4.2c, 2021-be-gk-A1.6b,
  2018MerhoehtBStochastikWTR1-2b/CAS1-2b und
  2018MerhoehtBStochastikCAS2-3a.
- e3 Prüfungshöhe bekommt eine Grafik, sobald die Vorlage ein
  Koordinatensystem ohne Achsenzahlen kennt.

## Nachbesserung Render 2026-09-28

Quelle: bau/render-alle/bericht.md, bau/hefte/bericht.md, bau/fokus/bericht.md, bau/layout-befunde.md Punkt 31. Übersicht aller Einträge: bau/render-alle/behoben.md.

- e1-k5-s3-v2 (1): Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern. Änderung: `ylabel={…}` geklammert (`=` im Optionswert).

Nur diese 1 Zeilen geändert, alle übrigen byte-gleich. `bank-pruef.py kenngroessen-von-verteilungen`: 0 Abweichungen. Probe: jede Zeile allein in einem Minimaldokument mit mathblatt.sty (hz-0801/blattbau) gesetzt wie werkzeuge/zusammenbau.py v0.7 (teile_normal, teil_schwach, Lösung in \erg), xelatex ohne Fehler.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- kenngroessen-von-verteilungen-e4-k2-s2-v2: Lösung „Maximum genau zwischen ihnen, dort liegt auch der Erwartungswert“ (nur bei p = 0,5 richtig) → „np = k + 1 − p; Erwartungswert zwischen den Säulen, genau in der Mitte nur bei p = 0,5“ (Regel a).
- kenngroessen-von-verteilungen-e3-k3-s1-v1, kenngroessen-von-verteilungen-e3-k3-s1-v2: Zuordnung der Diagramme zu X und Y fehlte, Verhältnis kippte (0,64 gegen 1,5625; 0,75 gegen 1,33) → „Das linke Diagramm gehört zu X, das rechte zu Y.“ ergänzt; Lösung unverändert (Regel b).
- kenngroessen-von-verteilungen-e4-k1-s2-v1, kenngroessen-von-verteilungen-e4-k1-s2-v2: Zuordnung der Diagramme fehlte, p_X und p_Y vertauschbar → Zuordnung links X, rechts Y ergänzt; Lösung unverändert (Regel b).
- Prüfskript: Abweichungen 0.
- 2026-10-08 Aufräumlauf: Sperre n = 100 (Original 2021MerhoehtAStochastik12-a) in e3-k1-s1-v1 (n = 400, σ = 10), e3-k1-s1-v2 (n = 900, σ = 9), e3-k4-s1-v2 (n = 900, σ = 9), e3-k4-s3-v1 (n = 400, σ 6; 8; 10; 8; 6), e4-k1-s4-v1 (n = 64, Säulen und grafik nachgezogen, P ≈ 0,467); Prüfskript: Abweichungen 5 → 0.
