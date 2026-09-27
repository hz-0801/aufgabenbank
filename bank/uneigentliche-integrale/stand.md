# Stand: uneigentliche-integrale

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
(2026-09-26, „katalog: Sek-II-Einträge auf die Katalogzeilen vom
27.09.“)
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     16 |        0 |         6 |       9 |        0 |       1 |
| e1    |     23 |        4 |         5 |       3 |        5 |       6 |
| e2    |     20 |        4 |         5 |       3 |        2 |       6 |
| Summe |     59 |        8 |        16 |      15 |        7 |      13 |

## Originale je Einheit

- e1: 2017MerhoehtBAnalysisCAS1-1e (dazu 3 Zeilen Prüfungshöhe
  ohne Original)
- e2: 2022MerhoehtBAnalysisWTR2-1e

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                          |
|-------|-----:|------:|-------------------------------------------|
| zone  |    0 |     0 | –                                         |
| e1    |    1 |     0 | pruef-Zahl nicht an der Ergebnisstelle    |
| e2    |    5 |     0 | Sperre: F(w) − F(0) aus dem Merkkasten    |

Keine Einheit ist zweimal gescheitert.

## Entscheidungen

- e1 Prüfungshöhe: 3 Zeilen ohne Original (Existenzfrage, Vermerk
  der Kette) und 2 Zeilen zur Zielmarke
  2017MerhoehtBAnalysisCAS1-1e, an derselben Sprosse.
- Das CAS-Original ist ohne Rechner verfremdet: die Stammfunktion
  steht in der Aufgabe.
- e2: 2022-bebb-lk-B2.2h ist wortgleiche Dublette von
  2022MerhoehtBAnalysisWTR2-1e und steht nur einmal (iqb, LK).
- Pflichtelemente nur Fehler und Begründen; die Typen tragen keine
  eigene Anwendung und keinen Darstellungswechsel. Typen ohne
  Kette gibt es nicht.
- Zone: Grenzverhalten (e1) vor Hauptsatz und Flächen (e2); das
  Zone-Paar hängt an „Hauptsatz lesen“ (Differenz als Fläche).
- Integralzeichen als Unicode ∫, Grenzwerte in Worten, weil das
  Prüfskript \int und \lim als Bausteine ablehnt.
- In fünf e2-Zeilen heißt die wandernde Grenze b statt w, weil die
  Sperre F(w) − F(0) aus dem Merkkasten trifft.

## Befunde

- Katalog: Die Erkennungsschritte vor e1 und e2 sind wortgleich
  die Vorstufen der Ketten; sie entfallen, die Vorstufe bleibt.
- Katalog: Die Ketten nennen den Grundfall „viermal“, bank.md
  verlangt 5 Zeilen; geschrieben sind 5.
- Katalog: Die e1-Kette vermerkt „kein Original“, die Zielmarke
  nennt seit dem Nachzug 2017MerhoehtBAnalysisCAS1-1e.
- Prüfskript: \int und \lim fehlen in der Liste der
  Standardbefehle; für dieses Thema sind beide zentral.
- Prüfskript: Die Sperre trifft F(w) − F(0), den Gegenstand von
  e2, weil der Sprossentext ihn nur in Worten nennt.

## Offene Punkte

- Unicode ∫ beim ersten Kompilieren prüfen (Schrift, unicode-math).
- Nicht kompiliert (kein LaTeX in der Sitzung).
