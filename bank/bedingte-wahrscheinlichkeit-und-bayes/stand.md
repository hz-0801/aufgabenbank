# Stand – bedingte-wahrscheinlichkeit-und-bayes

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     27 |      – |      10 |      16 |      – |       1 |
| e1    |     27 |      4 |       5 |       6 |      3 |       9 |
| e2    |     32 |      4 |       5 |       9 |      2 |      12 |
| e3    |     29 |      4 |       5 |       9 |      2 |       9 |
| Summe |    115 |     12 |      25 |      40 |      7 |      31 |

## Originale je Einheit

- e1: 2023-bebb-gk-B4.1c, 2017-bb-ea-B4.1b,
  2021MgrundlegendBStochastikWTR3-1b
- e2: 2020-be-gk-B4.2f, 2021MgrundlegendAStochastik11-b,
  2026MgrundlegendAStochastik13-b,
  2021MgrundlegendBStochastikWTR3-1g, 2024MerhoehtAStochastik21
- e3: 2026MerhoehtAStochastik22-b, 2026-bb-ea-B4e,
  2020MgrundlegendBStochastikWTR2-2c,
  2025MgrundlegendBStochastikWTR1-1e,
  2018MerhoehtBStochastikWTR2-1e

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                     |
|-------|-----:|------:|--------------------------------------|
| zone  |    3 |     0 | nacktes % in der Aufgabe (2)         |
| e1    |    0 |     0 | –                                    |
| e2    |    2 |     0 | pruef fehlt; Sperre Zahlenpaar       |
| e3    |    0 |     0 | –                                    |

Keine Einheit scheiterte zweimal. Außerhalb der Meldungen geändert:
e2-k1-s4-v3 (Aufteilung wie im Original, dann Kastenzahl 80).

## Entscheidungen

1. Nennt der Katalog an einer Kettensprosse Originale, trägt die
   letzte Variante eines davon mit Prüfkennung; die übrigen haben
   original null.
2. e1-Prüfungshöhe ohne Original: 3 Zeilen, original null, ohne
   Prüfkennung.
3. Pflichtelemente: fehler, begruenden, anwendung in allen drei
   Einheiten; darstellung nur in e2 (Baum und Vierfeldertafel).
4. Darstellungswechsel: das leere Gerüst steht in antwort
   (\vierfeldertafel{K}{T}{} oder \baumzwei ohne Werte), das
   gefüllte in loesungsgrafik.
5. Dezimalzahlen in \vierfeldertafel und \baumzwei mit Punkt, wie
   im Bausteinbeispiel von \baumzwei.
6. Parameterterme (e3 s1) tragen in loesung einen Probewert, damit
   pruef eine Zahl prüft.
7. Zone: kette und sprosse_text sind die Fertigkeit bis „ – “;
   Zone-Paar bei f1 (Rand statt Feld), am nächsten am
   Kernfehlmuster „durch den falschen Rand geteilt“.
8. Begründungen an Kettensprossen ohne Ziffern in der Lösung, damit
   pruef "" gilt.
9. Die e3-Vorstufe fragt nur, wo der Parameter steht; die Folge für
   das Wachsen des Bruchs trägt s2.

## Befunde

1. Katalog: „Was ist die Bedingung?“ wiederholt die Vorstufe von
   e1; der Erkennungsschritt entfällt.
2. Katalog: „Mit dem Baum oder gegen den Baum?“ wiederholt die
   Vorstufe von e2; er entfällt.
3. Katalog: „Was ändert der Parameter?“ wiederholt die Vorstufe
   von e3; er entfällt.
4. Mappe: 16 Kennungen der Sprossenzeilen stehen nicht in
   Abschnitt 2 und sind als original nicht verwendbar.
5. Katalog: die Zielmarke nennt für e1 Originale, die Prüfungshöhe
   der e1-Kette (Richtungen an der Tafel) hat keines.
6. Mappe: Zeile 24 des Katalogs nennt Nachzüge vom 28./29.09.2026,
   der Katalog-Commit ist vom 26.09.2026.
7. bank.md regelt nicht, wo beim Darstellungswechsel das leere
   Gerüst (Tafel, Baum) steht.

## Offene Punkte

1. Ungeprüft, ob \vierfeldertafel und \baumzwei Dezimalpunkte als
   Komma setzen (kein LaTeX in der Sitzung).
2. Ungeprüft, ob ksys mit xmax=0.3 und xstep=0.05 sauber
   beschriftet (e3-k1-s4-v3).
