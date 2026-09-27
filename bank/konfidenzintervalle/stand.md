# Stand: konfidenzintervalle

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
(2026-09-26, aus dem Kopf der Mappe)
Datum: 2026-09-27 14:50 UTC

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     26 |      – |      12 |      13 |      – |       1 |
| e1    |     25 |      4 |       5 |       6 |      4 |       6 |
| e2    |     25 |      4 |       5 |       6 |      4 |       6 |
| e3    |     22 |      4 |       5 |       3 |      4 |       6 |

## Originale je Einheit

- e1: 2026MerhoehtBStochastikWTR3-2c, 2025MerhoehtBStochastikWTR3-2c
- e2: 2023MerhoehtBStochastikWTR1-4b, 2026MerhoehtBStochastikMMS3-2a,
  2017MerhoehtBStochastikWTR-1g (Typ ohne Kette)
- e3: 2025MerhoehtBStochastikWTR3-2d, 2018MerhoehtBStochastikWTR2-1g

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund |
|-------|-------------:|----------:|------------------|
| zone  | 0 | 0 | – |
| e1    | 4 | 0 | pruef-Zahl nicht an der Ergebnisstelle (2×) |
| e2    | 0 | 0 | – |
| e3    | 0 | 0 | – |

## Entscheidungen

1. Die Prüfungshöhe trägt alle Originale der Zielmarke (je 2
   Zeilen), auch 2026MerhoehtBStochastikMMS3-2a und
   2018MerhoehtBStochastikWTR2-1g, die die Kette früher zitiert.
2. Der E2-Typ „1,96σ-Intervall“ ist Typ ohne Kette; zwei seiner
   drei Zeilen verfremden 2017MerhoehtBStochastikWTR-1g.
3. Pflicht: fehler und begruenden je Einheit (nur diese führen die
   Typen); anwendung und darstellung ohne eigene Zeilen – jede
   Zeile hat Sachkontext, das Ablesen ist Kette in E1.
4. Grenzgraphen stehen als ksys mit zwei \funktion je
   Sicherheitswahrscheinlichkeit, Intervalldiagramme als
   zahlengerade mit einem \intervall je Zeile (Anteile in Prozent).
5. Abgelesene Grenzen auf Hundertstel, gerechnete auf Tausendstel;
   pruef rechnet die exakte Lösung der Grenzgleichung.
6. Die Grenzgleichung steht in aufgabe nie wortgleich (Sperre aus
   Kasten und Original), nur als Wort oder mit eingesetzten Zahlen.
7. Zone: kette und sprosse_text bis zum Gedankenstrich; Folge nach
   erster Verwendung: Anteile, Binomialverteilung, Graphen (E1),
   Sigma-Regeln, Gleichungen, Ungleichungen (E2).
8. Zone-Paar zum Fallstrick „genau“ als „mindestens“ gerechnet
   (Typische Fehler, Überdeckungszahl).
9. Der Grundfall von E3 ist eine Begründung ohne Zahl in der
   Lösung; pruef bleibt dort leer.

## Befunde

- Katalog: Alle drei Erkennungsschritte (Z. 35–37) verlangen
  denselben Handgriff wie die Vorstufen der Ketten (Z. 77–79); sie
  entfallen, die Vorstufen bleiben.
- Katalog: Die Zielmarke E2 (Z. 84) nennt 2026MerhoehtBStochastik-
  MMS3-2a (Niveau II), das die Kette als Grundfall führt.
- Katalog: Z. 24 und Z. 83 nennen einen Nachzug vom 28.09.2026, der
  Katalog-Commit ist vom 26.09.2026.
- Prüfskript: \binom fehlt in STANDARD, obwohl es LaTeX-Standard
  ist; der Binomialkoeffizient musste als Zahl stehen.
- Prüfskript: Die Sperre greift auf Einzelangaben wie „n = 500“ aus
  einem Original; hier umgangen mit „Umfang 500“.

## Offene Punkte

- Die Grafiken (\funktion mit Wurzelterm, \intervall mit
  Dezimalgrenzen) sind nicht gerendert geprüft.
