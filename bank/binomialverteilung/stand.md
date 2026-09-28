# Stand: binomialverteilung

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
(2026-09-26, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“)
Datum: 2026-09-27

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     37 |        – |        16 |      20 |        – |       1 |
| e1    |     40 |        4 |         5 |      15 |        4 |      12 |
| e2    |     48 |        4 |         5 |      21 |        6 |      12 |
| e3    |     56 |        4 |         5 |      27 |        8 |      12 |
| e4    |     51 |        4 |         5 |      24 |        9 |       9 |
| e5    |     50 |        4 |         5 |      21 |        8 |      12 |

## Originale je Einheit

- e1: 2023-bebb-lk-A1.8a, 2022-bebb-gk-B4a, 2018-be-gk-B3.2g,
  2018MgrundlegendBStochastikWTR3-2d, 2024MerhoehtAStochastik23-b
- e2: 2017-be-gk-B3.1e, 2026MgrundlegendAStochastik12-a,
  2021MgrundlegendAStochastik2-a, 2022-bebb-gk-B4b,
  2019-be-gk-B4.1a, 2018-bb-ea-B4.2c
- e3: 2018-be-gk-B3.2a, 2018MerhoehtBStochastikWTR1-1a,
  2023-bebb-gk-B4.1d, 2017MerhoehtBStochastikCAS2-2,
  2017MerhoehtBStochastikCAS1-1b, 2022-bebb-lk-B4m,
  2023MerhoehtBStochastikWTR3-1c, 2024MgrundlegendAStochastik21-b,
  2020MgrundlegendAStochastik2-b, 2023MgrundlegendBStochastikWTR2-2b
- e4: 2017-bb-ea-B4.2b, 2018-be-gk-B3.2d,
  2019MgrundlegendBStochastikWTR1-1b, 2025MerhoehtAStochastik21,
  2022-bebb-lk-B4f, 2022MerhoehtBStochastikWTR1-1f,
  2017-be-gk-cas-B3.2d
- e5: 2017-be-gk-cas-B3.1e, 2023-bebb-gk-A1.7b,
  2025-bebb-gk-A1.9b, 2021MgrundlegendAStochastik2-b,
  2022MgrundlegendBStochastikWTR2-3a, 2022-bebb-lk-A1.8b

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund                |
|-------|-------------:|----------:|---------------------------------|
| zone  |            5 |         0 | merkmal je Sprosse uneinheitlich |
| e1    |            0 |         0 | –                               |
| e2    |            1 |         0 | pruef mit sum() nicht auswertbar |
| e3    |            0 |         0 | –                               |
| e4    |            3 |         0 | Ergebnis nach „≤“ nicht erkannt |
| e5    |            2 |         0 | Wert in Klammern ohne „≈“       |

Keine Einheit scheiterte zweimal.

## Entscheidungen

- Zone: Fertigkeiten ohne Doppelpunkt (Zeilen 36, 38–41) tragen als
  kette den Text bis zum ersten „ – “.
- Zone: Folge nach erster Einheit, bei gleicher Einheit nach dem
  Eintrag; die Rechnerfertigkeit übt eine Tabelle kumulierter Anteile
  ohne Begriff des Themas.
- Binomialkoeffizient als „(n über k)“ mit \text, Summen als \Sigma
  mit Grenzen; \binom und \sum kennt das Prüfskript nicht.
- Prüfungshöhe mit zwei Teilen: sprosse_text reicht bis zur ersten
  Belegklammer (e1, e2, e5 damit nur der erste Teil).
- original nur mit Kennungen aus Abschnitt 2 der Mappe; passt ein
  Original der Zielmarke zu einer Sprosse, trägt es die Sprosse
  (e2 s3, e4 s3, e5 s2).
- e4 Prüfungshöhe: der erste Teil (p aus zwei Einzelwerten) hat kein
  Original in der Mappe und steht als 3 Zeilen mit original null.
- Typen ohne Kette: e3 Restwahrscheinlichkeit und zwei Spieler, e4
  Trefferzahlen über einer Schranke, e5 obere Grenze über den
  Erwartungswert.
- e4 ohne Pflicht darstellung: die Typen der Einheit tragen keinen
  Darstellungswechsel.
- Säulendiagramme mit gerundeten Prozentwerten über \saeulenab,
  Ablesewerte in ganzen Prozent; Stabdiagramme über
  \binomialverteilung.
- Pflichtketten: sprosse_text aus „Dazu:“ oder dem Typnamen, e1
  darstellung aus der Grundvorstellung (Zeile 125).

## Befunde

- Katalog: alle vier Erkennungsschritte (Zeilen 43–46) wiederholen
  die Vorstufen der Ketten (Zeilen 127–131); nach bank.md entfallen
  sie, der Katalog führt beide.
- Katalog: „Genau, höchstens oder mindestens?“ ist Vorstufe von zwei
  Ketten (Einheit 2 und 3).
- Katalog und Mappe: Sprossen nennen Kennungen, die nicht in
  Abschnitt 2 stehen (etwa 2024-bebb-lk-A1.9a, 2021-be-gk-B4d,
  2019MerhoehtAStochastik11-b); sie bleiben original null.
- Prüfskript: \binom und \sum fehlen in STANDARD, beide braucht die
  Stochastik der Oberstufe.
- Prüfskript: ein Ergebnis nach „≤“ oder „≥“ (p ≤ 0,05) gilt nicht
  als Ergebnisstelle.
- Prüfskript: pruef ohne sum() und range() macht kumulierte Werte zu
  sehr langen Ausdrücken.
- Sperre: „P(X = 1)“ ist aus Kasten und Original gesperrt, obwohl es
  die Schreibweise des Gegenstands ist.

## Offene Punkte

- e3: der zweistufige Prüfplan (Original nicht in der Mappe) hat
  keine eigene Zeile.
- \saeulenab mit Prozent-Achse und \binomialverteilung mit Ausschnitt
  sind nicht am Render geprüft (kein LaTeX).
- Zone: „Säulendiagramm zeichnen“ hat keine eigene Zeile; e5 übt es
  in der Pflicht darstellung.

## Nachbesserung Render 2026-09-28

Quelle: bau/render-alle/bericht.md, bau/hefte/bericht.md, bau/fokus/bericht.md, bau/layout-befunde.md Punkt 31. Übersicht aller Einträge: bau/render-alle/behoben.md.

- e5-k1-s1-v1, e5-k1-s1-v2, e5-k1-s1-v3, e5-k1-s1-v4, e5-k1-s1-v5, e5-k1-s5-v1, e5-k1-s5-v2, e5-k3-s4-v2 (8): Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern. Änderung: `ylabel={…}` geklammert (`=` im Optionswert).

Nur diese 8 Zeilen geändert, alle übrigen byte-gleich. `bank-pruef.py binomialverteilung`: 0 Abweichungen. Probe: jede Zeile allein in einem Minimaldokument mit mathblatt.sty (hz-0801/blattbau) gesetzt wie werkzeuge/zusammenbau.py v0.7 (teile_normal, teil_schwach, Lösung in \erg), xelatex ohne Fehler.
