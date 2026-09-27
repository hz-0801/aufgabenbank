# Stand: lagebeziehungen

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08 (2026-09-26)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     27 |        0 |        12 |      14 |        0 |       1 |
| e1    |     36 |        8 |         5 |      15 |        2 |       6 |
| e2    |     26 |        4 |         5 |       9 |        2 |       6 |
| e3    |     31 |        4 |         5 |      12 |        4 |       6 |
| e4    |     26 |        4 |         5 |       9 |        2 |       6 |
| gesamt|    146 |       20 |        32 |      59 |       10 |      25 |

## Originale je Einheit

- e1: 2018MerhoehtAAGLAA211-a, 2021MerhoehtAAGLAA211-a,
  2021-be-gk-A1.5a, 2018-be-gk-B2.1b, 2025MgrundlegendAAGLAA213-b,
  2026MgrundlegendAAGLAA211-a, 2024MgrundlegendBAGLAA2WTR2-1d,
  2023-bebb-gk-B3f, 2019MgrundlegendBAGLAA2WTR2-1c,
  2026MerhoehtBAGLAA2MMS2-1c (Prüfungshöhe)
- e2: 2022MerhoehtBAGLAA2WTR1-1e, 2023MgrundlegendAAGLAA22-a,
  2023MgrundlegendBAGLAA2WTR1-1b, 2023MerhoehtBAGLAA2WTR1-1b,
  2026MerhoehtAAGLAA221-a, 2019MerhoehtAAGLAA22-a (Prüfungshöhe)
- e3: 2021-be-gk-A1.4b, 2017-be-gk-B2.1d, 2024MgrundlegendAAGLAA213-a,
  2017MgrundlegendBAGLAA2WTR2-1a, 2026MerhoehtBAGLAA2WTR2-1d,
  2019MerhoehtAAGLAA22-b, 2024-bebb-lk-A1.8a (Prüfungshöhe),
  2020MerhoehtAAGLAA22-b (Prüfungshöhe)
- e4: 2020MerhoehtAAGLAA212, 2024MgrundlegendBAGLAA2WTR1-1d,
  2023MgrundlegendBAGLAA2WTR1-1g, 2018MerhoehtBAGLAA2WTR3-1e,
  2018MerhoehtBAGLAA2WTR3-1g (Prüfungshöhe),
  2017MerhoehtBAGLAA2WTR1-1e, 2017MerhoehtBAGLAA2CAS1-1f

## Prüfskript vor der Korrektur

| Datei | Abweichungen | häufigster Grund                  | Warnungen |
|-------|-------------:|-----------------------------------|----------:|
| zone  |            1 | Sperre: Tripel aus einem Original |         0 |
| e1    |            3 | Sperre: Tripel aus Kasten/Original|         0 |
| e2    |            0 | –                                 |         0 |
| e3    |            1 | Sperre: Tripel aus einem Original |         0 |
| e4    |            1 | Sperre: Tripel aus einem Original |         0 |

## Entscheidungen

- Zone: kette und sprosse_text enden am ersten Doppelpunkt, sonst
  vor „ – "; das Zone-Paar steht bei „Ebenengleichungen lesen"
  (fehlende Variable, das meistbelegte Fehlermuster).
- Koordinaten heißen x, y, z wie im Merkkasten, nicht x1, x2, x3.
- „Wer und wogegen?" steht als Erkennungsschritt (eigene Kette k1)
  in e1, der ersten Einheit seines Bereichs; die gleichnamige
  Vorstufe der Kette in e2 bleibt, weil sie in einer anderen
  Einheit steht.
- e1: 2018MerhoehtAAGLAA211-a und 2021MerhoehtAAGLAA211-a stehen an
  s2 (fehlende Variable), nicht am Grundfall, weil ihre Falle das
  Merkmal von s2 ist.
- Von wortgleichen Dubletten zwischen Pool und Landesheft trägt
  eine Kennung die Zeilen, die andere bekommt keine.
- Typ ohne Kette nur in e4 („… Länge eines Schattens auf einer
  Dachfläche …"); „Parallelität … über das Skalarprodukt" steht
  an e3 s2 mit 2017-be-gk-B2.1d.
- Pflichtelemente nur fehler und begruenden, weil „Typen je
  Lerneinheit" nur diese nennt.
- Kastenzahlen: 1,5, 12, 15, 20 und 60 gelten als mehrstellig.
- pruef bei Nachweisen: eine Zahl an der Ergebnisstelle; jede Lage
  und jeder Schnittpunkt mit sympy nachgerechnet.

## Befunde

- Katalog: Der Erkennungsschritt „Erfüllt, größer oder kleiner?"
  wiederholt die Vorstufe von e1 und entfällt; die Vorstufe bleibt.
- Katalog: Der Erkennungsschritt „Fällt der Parameter heraus?"
  wiederholt die Vorstufe von e3 und entfällt; die Vorstufe bleibt.
- Katalog: Der Erkennungsschritt „Rechnung fertig – Frage
  beantwortet?" wiederholt die Vorstufe von e4 und entfällt.
- Katalog: „Wer und wogegen?" steht als Erkennungsschritt vor e1
  und e3 und zugleich als Vorstufe der Kette von e2 – derselbe
  Handgriff an zwei Stellen.
- Katalog/Mappe: Der Grundfall von e3 nennt
  2026MerhoehtBAGLAA2MMS2-1d, das die Mappe nicht aufnimmt.
- Prüfskript: Die Sperre liest Tripel nur mit senkrechtem Strich;
  Tripel der Originale mit Semikolon, etwa P(0; −1; 1), sperrt sie
  nicht.
- Prüfskript: Die Sperre trifft auch Gegenstände des Themas wie den
  Normalenvektor (0 | 0 | 1) der xy-Ebene; sie wurden umgangen.
- Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die
  Gegenprobe lief mit eigenem Skript (0 Treffer).

## Offene Punkte

- Ohne Zeile, weil wortgleiche Dublette: 2022-bebb-gk-A1.4a,
  2025-bebb-gk-A1.5b, 2026-bb-gk-A1.2a, 2023-bebb-lk-A1.5a,
  2024-bebb-gk-A1.2a, 2026-bb-ea-A1.8a, 2022-bebb-lk-B3h,
  2026-bb-ea-B3d, 2017MerhoehtBAGLAA2WTR2-1a; weil Kastenbeispiel:
  2022MgrundlegendAAGLAA211-a, 2023MerhoehtAAGLAA213-a.
- Die Schattenlänge auf der Dachfläche ist im Katalog Ermessen;
  wandert der Typ, wandern die drei Zeilen mit.
- Kein LaTeX-Lauf; die einzige Grafik (ksys3 in der Zone) ist nur
  auf Bausteinname und Bereich geprüft.
