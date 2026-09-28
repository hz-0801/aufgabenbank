# Stand: matrizen-und-uebergangsprozesse

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
(2026-09-26, aus dem Kopf der Mappe)
Datum: 2026-09-27 14:40 UTC

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     27 |      – |      12 |      14 |      – |       1 |
| e1    |     34 |      4 |       5 |      15 |      4 |       6 |
| e2    |     36 |      4 |       5 |      15 |      6 |       6 |
| e3    |     37 |      4 |       5 |      15 |      4 |       9 |
| e4    |     39 |      4 |       5 |      15 |      6 |       9 |
| e5    |     42 |      4 |       5 |      18 |      6 |       9 |

## Originale je Einheit

- e1: 2025MerhoehtAAGLAA122, 2020MgrundlegendAAGLAA12
- e2: 2026MerhoehtAAGLAA121-b, 2026MerhoehtAAGLAA122-b,
  2022MerhoehtBAGLAA1WTR-2c
- e3: 2025MerhoehtBAGLAA1MMS-2b, 2023MerhoehtBAGLAA1WTR-1d
- e4: 2026MgrundlegendBAGLAA1MMS-1c, 2022MgrundlegendBAGLAA1WTR-1f,
  2024MgrundlegendBAGLAA1WTR-1d
- e5: 2022MerhoehtBAGLAA1WTR-2d, 2023MerhoehtAAGLAA12-b,
  2026MerhoehtAAGLAA11-b

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund |
|-------|-------------:|----------:|------------------|
| zone  | 4 | 0 | Tripel mit \mid in loesung nicht erkannt |
| e1    | 2 | 0 | Sperre: Zahlenpaar aus dem Merkkasten |
| e2    | 5 | 0 | Sperre: Zahlenpaar (1 \| 3) aus dem Kasten |
| e3    | 1 | 0 | pruef-Zahl nicht an der Ergebnisstelle |
| e4    | 0 | 0 | – |
| e5    | 0 | 0 | – |

## Entscheidungen

1. Matrizen stehen als Tupel ihrer Zeilen, M = ((a | b), (c | d)):
   das Prüfskript lässt in aufgabe keine Umgebung (pmatrix) zu,
   die Vorlage hat keinen Matrix-Baustein.
2. Übergangs- und Verflechtungsdiagramme stehen als Pfeilliste im
   Text; Zeichenaufträge haben form zeichnen, grafik
   \rechenplatz{4}, die Lösung nennt die Pfeile.
3. Die Prüfungshöhe jeder Einheit trägt alle Originale ihrer
   Zielmarke (je 2 Zeilen), auch wenn die Kette sie früher zitiert;
   sprosse_text ist der erste Teil der Prüfungshöhe der Kette.
4. Teile der Prüfungshöhe ohne Original in Abschnitt 2 (Spur,
   Abbildungsmatrizen, Spielregel u. a.) entfallen; die
   Prüfungsform-Originale 2017/2018 sind nicht Prüfungshöhe.
5. Zone: kette und sprosse_text sind die Fertigkeit bis zum
   Gedankenstrich (kein Doppelpunkt in den Zeilen); Folge nach
   erster Verwendung: LGS (E1), Vektoren, Diagramme, Terme (E3),
   Anteile (E4), Potenzen (E5).
6. Zone-Paar zum Fallstrick „unterbestimmtes System, nur eine
   Lösung genannt“ (Typische Fehler: Lösungsmengen verkürzt).
7. Pflicht: fehler und begruenden in allen Einheiten, anwendung in
   E3 bis E5; darstellung ohne eigene Zeilen, weil Diagramm und
   Matrix in E3 und E4 schon Kettensprossen sind.
8. Typ ohne Kette nur in E5 (Eignung eines Populationsmodells);
   die übrigen Typen deckt eine Sprosse der Kette.
9. Rein algebraische Originale (E1, E2, E5 Teil A) sind in Zahlen
   und Form verfremdet, ohne Sachkontext.
10. pruef bei Nachweisen: die Zahl an der Ergebnisstelle
    (Spaltensumme 1, Faktor, Zwischenwert der Probe).

## Befunde

- Katalog: Alle vier Erkennungsschritte (Z. 41–44) verlangen
  denselben Handgriff wie die Vorstufen der Ketten (Z. 115–119);
  sie entfallen, die Vorstufen bleiben.
- Katalog: Die Sprossenzeilen 115 und 118 enthalten Platzhalter
  („2022MgrundlegendBAGLAA1WTR... siehe Muster“) statt Kennungen.
- Katalog: Die Zielmarke (Z. 126) setzt Originale als
  Prüfungshöhe, die die Kette an früheren Sprossen führt (etwa
  2020MgrundlegendAAGLAA12, 2026MerhoehtAAGLAA11-b).
- Katalog: Z. 30 nennt Nachträge vom 28. und 29.09.2026, der
  Katalog-Commit ist vom 26.09.2026.
- Prüfskript: `"\\begin{" in aufgabe` sperrt auch pmatrix, das
  UMGEBUNG_STANDARD sonst zulässt; Matrizen haben keine Satzform.
- Prüfskript: normiert() entfernt \mid, ein Tupel mit \mid in der
  Lösung zählt nicht als Ergebnis (mathnorm kennt \mid).
- Prüfskript: Die Sperre der Kasten-Tripel (1 | 0 | 0), (0 | 1 | 0)
  und (0 | 0 | 1) sperrt jede 3×3-Vertauschungsmatrix in aufgabe.
- Bausteine: Es fehlen Bausteine für Matrizen und für
  Pfeildiagramme (Übergangs- und Verflechtungsdiagramm).

## Offene Punkte

- Der E4-Typ „Aussage über laufende gegenüber einmaliger Entnahme“
  steht in keiner Kettensprosse und hat noch keine Zeilen.
- Der Zusammenbau muss ((a | b), (c | d)) in pmatrix übersetzen und
  für die Zeichenaufträge einen Diagramm-Baustein bekommen.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- matrizen-und-uebergangsprozesse-e4-k1-s5-v2: Lösung ließ den Zugang als unbestimmtes z stehen, obwohl die Aufgabe 50 Tiere im ersten Gebiet vorgibt; pruef leer → $M \cdot (M \cdot v + (50 | 0))$, pruef [50, 0] (Regel a).
- matrizen-und-uebergangsprozesse-zone-f1-v7: Lösung nannte für t = 3 nur y = 4, das Gerüst fragt x und y → „x = 3, y = 4“, pruef [10, 3, 4] (Regel b).
- Prüfskript: Abweichungen 0.
