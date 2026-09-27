# Stand: spiegelung

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        – |        12 |      13 |        – |       1 |    26 |
| e1    |       12 |         5 |       9 |        2 |       6 |    34 |
| e2    |        4 |         5 |       9 |        2 |       6 |    26 |
| e3    |        4 |         5 |      12 |        4 |       6 |    31 |
| alle  |       20 |        27 |      43 |        8 |      19 |   117 |

## Originale je Einheit

- e1: 2025-bebb-gk-A1.5a, 2025MerhoehtBAGLAA1WTR-2a,
  2026-bb-gk-A1.2b, 2022-bebb-lk-B3g, 2021MerhoehtAAGLAA211-b;
  Prüfungshöhe 2022MerhoehtAAGLAA212-b
- e2: 2022MerhoehtAAGLAA212-a, 2018MerhoehtAAGLAA211-c,
  2023-bebb-lk-A1.6b, 2026-bb-gk-B3e; Prüfungshöhe
  2024MerhoehtAAGLAA222
- e3: 2026MerhoehtBAGLAA2WTR1-1b, 2022MerhoehtBAGLAA2WTR2-1a,
  2022-bebb-gk-B3e, 2024-bebb-lk-B3b, 2026MgrundlegendBAGLAA2MMS2-1b,
  2019MgrundlegendBAGLAA2WTR2-1b, 2025MerhoehtAAGLAA223-a,
  2023MgrundlegendBAGLAA2WTR1-1c; Prüfungshöhe 2026MerhoehtAAGLAA223,
  2025MerhoehtBAGLAA2MMS-1c

## Prüfskript vor der Korrektur

- zone: 5 Abweichungen (Sperre: Tripel aus Kasten und Originalen),
  im zweiten Lauf 1 (Sperre: Tripel), 0 Warnungen
- e1: 0 Abweichungen, 0 Warnungen
- e2: 1 Abweichung (pruef nicht an der Ergebnisstelle), 0 Warnungen
- e3: 3 Abweichungen (Sperre: Tripel aus Kasten und Originalen),
  0 Warnungen
- Gegenprobe: keine Kastenzahl (11, 12, 40) in einer aufgabe.

## Entscheidungen

- Zone: kette und sprosse_text reichen bis zum Gedankenstrich, nicht
  bis zum Doppelpunkt – die Fertigkeitszeilen trennen mit „–“.
- Zone: ein Fallstrick je Fertigkeit; Zone-Paar beim
  Verbindungsvektor (Anfang minus Ende), dem Muster „am falschen
  Punkt abgetragen“.
- Zone-Reihenfolge: in Einheit 1 zuerst die Sek-I-Fertigkeit
  (Achsenspiegelung), dann Lehrplanfolge der Nachbarthemen.
- Die Zone wurde nach dem zweiten Lauf noch einmal korrigiert (eine
  Zeile): die Fehlerregel des Auftrags nennt nur Einheiten.
- Pflichtelemente nur fehler und begruenden: die Typen nennen unter
  „Dazu“ nur diese.
- Wortgleiche Pooldubletten zählen als ein Original; das Feld trägt
  die Landesheft-Kennung, je Original eine Variante an Kettensprossen.
- sprosse_text von Vorstufe und Prüfungshöhe ohne die Klammerbelege
  des Katalogs.
- Winkelhalbierende (e2, Prüfungshöhe) im ebenen ksys mit konkreten
  Punkten; die Lösung nennt den Rautenterm und den Punkt.
- Der Scharparameter heißt in e3 t, wie im Original.

## Befunde

- Katalog: „Was wird gespiegelt – und woran?“ (Zeile 35) ist
  zugleich die Vorstufe der Kette e1 (Zeile 87); der
  Erkennungsschritt entfällt.
- Katalog: „Reicht ein Gegenbeispiel?“ (Zeile 38) ist Teil der
  Vorstufe e3 (Zeile 89); der Erkennungsschritt entfällt.
- Katalog: „Was ist gegeben, was gesucht?“ (Zeile 36) steht als
  Erkennungsschritt in e1 und als Vorstufe in e2 (Zeile 88);
  „Welche Koordinate wechselt?“ (Zeile 37) in e1 und in der Vorstufe
  von e3 – derselbe Handgriff zweimal über Einheitsgrenzen.
- Katalog: Zeile 24 nennt Nachzüge „2026-09-28“ und „2026-09-29“, die
  nach dem Katalog-Commit (26.09.) liegen.
- bank.md: „bis zum Doppelpunkt“ passt nicht auf Fertigkeitszeilen,
  deren Trenner der Gedankenstrich ist.
- bank.md und Prüfskript: „2 je Original“ zählt wortgleiche
  Pooldubletten als eigene Originale; Dubletten sind nicht geregelt.

## Offene Punkte

- Schnittfiguren (e3) und die Winkelhalbierende (e2) haben keine
  loesungsgrafik; die Vorlage kennt keinen Vieleck-Baustein für ksys3.
