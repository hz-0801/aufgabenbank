# Stand: hypergeometrische-verteilung

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25)
Datum: 2026-09-27 15:03 UTC
Prüfskript: bank-pruef.py v0.5, am Ende 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     19 |        – |         8 |      10 |        – |       1 |
| e1    |     26 |        4 |         5 |       6 |        2 |       9 |
| e2    |     17 |        4 |         5 |       – |        2 |       6 |
| Summe |     62 |        8 |        18 |      16 |        4 |      16 |

## Originale je Einheit

- E1: 2022-bebb-gk-A1.6a (Grundfall), 2024MerhoehtBStochastikWTR2-1e
  (s2), 2017-bb-ea-B4.2e (Prüfung)
- E2: 2023-bebb-lk-B4l (Prüfung)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund |
|-------|-------------:|----------:|------------------|
| zone  |            0 |         0 | –                |
| e1    |            0 |         0 | –                |
| e2    |            0 |         0 | –                |

## Entscheidungen

- Zone: kette und sprosse_text enden am Gedankenstrich der
  Fertigkeitszeile; in Zeile 27 steht der Doppelpunkt in der Klammer
  („zur Abgrenzung: …“), die Klammer bleibt ganz.
- Zone-Folge wie im Eintrag, weil keine Fertigkeitszeile eine Einheit
  nennt; Zone-Paar zum Kernfehlmuster „Nenner nicht verkleinert“ in
  der Fertigkeit Pfadregeln.
- E2: Die einzige Katalogsprosse ist „Grundfall … Prüfungshöhe
  zugleich“; sie steht als s1 grundfall (5 Zeilen, kleine Zahlen) und
  s2 pruefung (2 Zeilen, Original) mit gleichem sprosse_text.
- Binomialkoeffizienten sind als „(n über k)“ mit \text gesetzt, weil
  das Prüfskript \binom nicht zulässt.
- Pflicht anwendung nur in E1 (Typ „über das Gegenereignis
  berechnen“); in E2 ist der einzige Typ schon Sachaufgabe;
  darstellung entfällt, kein Typ trägt einen Darstellungswechsel.
- Originale stehen an der Sprosse, die sie nennt: 2022-bebb-gk-A1.6a
  am Grundfall, 2024MerhoehtBStochastikWTR2-1e an s2; die
  Prüfungshöhe von E1 trägt nur 2017-bb-ea-B4.2e.
- Prüfkennung: iqb erhöht, bb-ea und bebb-lk als LK, bebb-gk als GK.

## Befunde

- Katalog: Die Erkennungsschritte „Mit oder ohne Zurücklegen?“ und
  „Direkt oder übers Gegenereignis?“ sind wortgleich die Vorstufe der
  Kette „Genau k ohne Zurücklegen“; sie entfallen, der Katalog führt
  beide.
- Katalog: „Kumulieren“ hat nur eine Sprosse, Grundfall und
  Prüfungshöhe fallen zusammen; die Gegenprobe verlangt beide
  getrennt.
- Prüfskript: \binom fehlt unter den erlaubten Befehlen; für
  Stochastik-Einträge wäre es die übliche Schreibweise.
- Mappe: 2023MgrundlegendBStochastikWTR1-1b, 2018-bb-ea-B4.1d und
  2023-bebb-lk-B4k aus den Sprossen stehen nicht in Abschnitt 2;
  original bleibt dort null.
- Gegenprobe Kastenzahlen: der Merkkasten hat keine Zahlen, Ist 0.

## Offene Punkte

- Für Berliner Zielprüfungen ist das Thema laut Katalog kein
  Blattstoff; die Auswahl beim Blattbau muss das beachten.
- Die Schreibweise „(n über k)“ beim Zusammenbau prüfen oder durch
  \binom ersetzen, sobald das Prüfskript es zulässt.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- hypergeometrische-verteilung-e2-k2-s2-v2: loesung „damit größer als $P(X = k)$ allein“ (falsch für k = 0, dort gleich) → „damit mindestens so groß wie $P(X = k)$ allein“ (Regel a).
- Prüfskript: Abweichungen 0.
