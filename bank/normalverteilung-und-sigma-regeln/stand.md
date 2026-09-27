# Stand: normalverteilung-und-sigma-regeln

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
(2026-09-26, „katalog: Sek-II-Einträge auf die Katalogzeilen vom
27.09.“)
Datum: 2026-09-27
bank.md: Stand 2026-09-27b; Prüfskript v0.5

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     27 |      – |      10 |      16 |      – |       1 |
| e1    |     23 |      4 |       5 |       6 |      2 |       6 |
| e2    |     26 |      4 |       5 |       9 |      2 |       6 |
| e3    |     28 |      4 |       5 |       9 |      4 |       6 |

## Originale je Einheit

- e1 Prüfungshöhe: 2023MerhoehtBStochastikWTR3-2c; Kette:
  2024MerhoehtAStochastik12-a, 2026-bb-ea-B4g
- e2 Prüfungshöhe: 2024MerhoehtAStochastik12-b; Kette:
  2022MerhoehtAStochastik13-a, 2026-bb-ea-B4f, 2026-bb-ea-B4h
- e3 Prüfungshöhe: 2025MerhoehtBStochastikWTR1-2b,
  2022MerhoehtBStochastikWTR2-3a; Typ ohne Kette:
  2017MerhoehtBStochastikCAS2-3c

Nur als Prüfkennung im Text, Feld null:
- e1 k1 s1: 2022MerhoehtAStochastik13-b
- e2 k1 s1: 2023MerhoehtBStochastikWTR3-2a,
  2024MerhoehtBStochastikWTR2-2a
- e3 k1 s1: 2024MerhoehtBStochastikWTR2-2c,
  2025MerhoehtBStochastikWTR1-2a
- e3 k1 s2: 2022MerhoehtBStochastikWTR2-3b
- e3 k1 s3: 2024MerhoehtBStochastikWTR2-2b

## Prüfskript vor der Korrektur

- zone: 0 Abweichungen, 0 Warnungen
- e1: 1 Abweichung – pruef nicht an der Ergebnisstelle (Zahl in
  wissenschaftlicher Schreibweise „3E-7“ statt Dezimalzahl)
- e2: 0
- e3: 2 Abweichungen – Baustein \max nicht in _bausteine.md

Eigene Proben: 1 Kastenzahl („21“, e2 k2 s2 v3) ersetzt; dazu
e2 k1 s1 v5 (gleiches Ergebnis wie v3) und die Lösungstexte e3 k1
s3–s4 nachgebessert. Stand: 0 Abweichungen, 0 Warnungen.

## Entscheidungen

1. Zone: kette und sprosse_text bis zum Gedankenstrich; Folge
   nach erster Verwendung: Z. 28, 30 (E1), 29, 31, 32 (E2); das
   Zone-Paar steht in der Flächen-Kette zum Fallstrick „Fläche
   statt Höhe“, dem häufigsten Fehlermuster des Eintrags.
2. Pflicht je Einheit nur fehler und begruenden, weil „Dazu“ nur
   diese nennt; Skizzen und Sachanwendungen stehen in der Kette.
3. E3 hat einen Typ ohne Kette (σ aus einer Vorgabe bei festem μ,
   Z. 23) als k2 mit 3 Zeilen; die Pflichtelemente sind k3.
4. Originale stehen in jeder Zeile der Sprosse; Pooldubletten
   (B4f/WTR1-3a, B4h/WTR1-3c) unter der abi-Kennung; bb-ea ist LK.
5. Kennungen ohne Eintrag in Abschnitt 2: original null,
   Prüfkennung im Text (alle drei Grundfälle, e3 s2–s3).
6. Wahrscheinlichkeiten auf vier Stellen, Schrankenvergleiche auf
   drei; Folgerechnungen mit dem gerundeten μ bzw. c wie am
   Rechner.
7. Die Verteilungsfunktion (e3 s1) ist im ksys als logistische
   Näherung 1/(1 + e^(−1,702 z)) gezeichnet, weil die Vorlage
   keine Fehlerfunktion kennt; Abweichung unter 0,01.
8. Halbe Schritte stehen in Aufgaben in Worten („eine halbe
   Einheit darunter bis darüber“), weil die Formel des Originals
   gesperrt ist.
9. Die Prozentwerte der Sigma-Regeln (Kastenzahlen) stehen nur in
   Lösungen; die Aufgaben verweisen auf die Sigma-Regeln.
10. Entscheidungsaufgaben gemischt: e2 s4 zweimal ja, einmal
    nein; e3 s4 (Intervall fester Länge) einmal nein, einmal ja.

## Befunde

- Katalog: Alle drei Erkennungsschritte (Z. 34–36) sind zugleich
  Vorstufen der Ketten (Z. 77–79); sie entfallen, die Vorstufen
  bleiben.
- Katalog: Neun Kennungen der Sprossenzeilen fehlen in Abschnitt 2
  der Mappe; alle drei Grundfälle haben dadurch kein Original im
  Feld.
- Katalog: Der Commit vom 26.09.2026 heißt „Katalogzeilen vom
  27.09.“; Z. 24 und 82 nennen Nachzüge vom 28.09.2026.
- Katalog: E3 trägt die Marke „keine Prüfungsaufgabe“ (Z. 16),
  die Kette endet aber mit einer Pool-Prüfungshöhe (Z. 79); gebaut
  nach Z. 79.
- Katalog: Die Sprossenzeilen nennen den Grundfall „viermal“,
  bank.md fünf Zeilen; bank.md angewandt.
- Vorlage: kein Baustein für den Graphen einer
  Verteilungsfunktion; \normalverteilung zeichnet nur die Dichte.
- Prüfskript: \max (Standard-LaTeX) gilt als fremder Baustein; die
  Gegenprobe „Kastenzahlen“ prüft es nicht.

## Offene Punkte

- Rendern ungeprüft (kein LaTeX): \normalverteilung mit bis= und
  zwei Glocken in einer Lösungsgrafik, \funktion mit exp im ksys.
- Feld original nachtragen, sobald die Mappe die Kennungen führt.
- Das Thema ist nur LK-Stoff (Z. 74); für GK-Blätter ungeeignet.
