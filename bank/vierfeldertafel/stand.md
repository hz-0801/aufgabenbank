# Stand: vierfeldertafel

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     22 |        0 |        10 |      11 |        0 |       1 |
| e1    |     33 |        8 |         5 |      12 |        2 |       6 |
| e2    |     23 |        4 |         5 |       6 |        2 |       6 |
| gesamt|     78 |       12 |        20 |      29 |        4 |      13 |

## Originale je Einheit

- e1: 2023-bebb-gk-B4.1a, 2024-bebb-gk-B4.1b, 2018-bb-ea-B4.2a,
  2022-bebb-gk-B4h, 2018-be-gk-B3.2e, 2017-bb-ea-B4.1a,
  2022MerhoehtBStochastikWTR2-1a; Prüfungshöhe:
  2021MerhoehtAStochastik11-a
- e2: 2019-be-gk-B4.1c, 2023-bebb-gk-B4.1b,
  2020MgrundlegendAStochastik12-a; Prüfungshöhe:
  2025MerhoehtBStochastikWTR1-1b

Alle zwölf Originale der Mappe haben Zeilen.

## Prüfskript vor der Korrektur

| Datei | Abweichungen | häufigster Grund                | Warnungen |
|-------|-------------:|---------------------------------|----------:|
| zone  |            0 | –                               |         0 |
| e1    |            8 | nacktes % in loesung (5)        |         0 |
| e2    |            0 | –                               |         0 |

Nach eigener Durchsicht berichtigt: e1 s1 v1 (Tafel mit Summe 110),
e1 s2 v1 (leere Tafel als {} statt Kommaliste), e2 s1 v3 (Buchstabe P
für ein Ereignis gestrichen).

## Entscheidungen

1. Zone: kette endet vor „ – “; je Fertigkeit ein Fallstrick; das
   Zone-Paar steht bei den Pfadregeln, weil „bedingten Anteil als
   Feld eingetragen“ das Kernfehlmuster ist.
2. Der Erkennungsschritt „Weder–noch, entweder–oder, oder?“ steht als
   eigene Kette in e1, der ersten Einheit seines Bereichs; e2 behält
   ihn als Vorstufe, mit anderen Aufgaben (Ausdruck statt Feldzahl).
3. Die Vorstufe von e1 vereint zwei Handgriffe: drei Varianten
   fragen Rand, Feld oder bedingt, eine fragt Anteil oder Anzahl.
4. Tafeln in ganzen Prozent, damit \vierfeldertafel keine
   Dezimalkommas in der Kommaliste braucht; die volle Tafel steht in
   loesungsgrafik.
5. Tafeln mit drei Spalten als \sachtabelle mit \leerzelle.
6. Pflichtelemente nur fehler und begruenden, weil „Typen je
   Lerneinheit“ nur diese nennt.
7. sprosse_text von Vorstufe und Grundfall ohne die Klammer
   „(Vorstufe …)“ bzw. „(Grundfall …)“.
8. Keine Typen ohne Kette: alle acht Typen sind Sprossen der Ketten.
9. P steht nur für die Wahrscheinlichkeit; Ereignisse tragen andere
   Buchstaben.

## Befunde

1. Katalog: „Rand, Feld oder bedingt?“ und „Anteil oder Anzahl?“
   wiederholen die Vorstufe von e1 und entfallen; die Vorstufe bleibt.
2. Katalog: „Weder–noch, entweder–oder, oder?“ ist Erkennungsschritt
   vor e1 und e2 und zugleich Vorstufe von e2; bank.md regelt den
   Wegfall nur innerhalb einer Einheit (Entscheidung 2).
3. Katalog: Die Vorstufe von e1 fasst zwei Erkennungsschritte in eine
   Sprosse; Varianten ändern damit mehr als Zahlen und Kontext.
4. Katalog: Die meisten Sprossen belegen auch mit Kennungen, die die
   Mappe nicht aufnimmt (17 „nur außerhalb von Prüfungsform“).
5. Prüfskript: Zeilen- und Spaltensummen einer Tafel prüft es nicht;
   die Tafel mit Summe 110 fand erst die eigene Summenprobe.
6. Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die eigene
   Probe fand 0 Treffer.

## Offene Punkte

- Kein LaTeX-Lauf; \vierfeldertafel mit Termen (etwa 1-7p) und
  \sachtabelle mit \leerzelle sind nur auf Bausteinname und
  Argumentzahl geprüft.
- fhr hat keinen Bestand; der Katalog verweist auf unabhaengigkeit.md.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- vierfeldertafel-e2-k1-s1-v3: Angabe fehlte (dass alle übrigen Bewerbungen online kamen) → „kamen 300 per Post, die übrigen online“; Lösung 170 unverändert (Regel b).
- vierfeldertafel-e2-k1-s1-v4: Angabe fehlte (alle Lose verkauft, Rest am Nachmittag) → „Alle Lose wurden verkauft, 400 am Vormittag, der Rest am Nachmittag“; Lösung 520 unverändert (Regel a).
- Prüfskript: Abweichungen 0.
