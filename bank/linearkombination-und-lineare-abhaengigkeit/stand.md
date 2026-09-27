# Stand: linearkombination-und-lineare-abhaengigkeit

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
(2026-09-26, „katalog: Sek-II-Einträge auf die Katalogzeilen vom
27.09.“)
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     18 |        – |         8 |       9 |        – |       1 |
| e1    |     18 |        4 |         5 |       6 |        3 |       – |
| e2    |     22 |        4 |         5 |       3 |        4 |       6 |
| Summe |     58 |        8 |        18 |      18 |        7 |       7 |

Pflicht e2: fehler 3, begruenden 3.

## Originale je Einheit

- e1: keins (Prüfungshöhe ohne Original, original null, 3 Zeilen).
- e2, Prüfungshöhe: 2017-bb-ea-B3.1d, 2017MerhoehtBAGLAA2CAS2-1d.

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund              |
|-------|-------------:|----------:|-------------------------------|
| zone  |            0 |         0 | –                             |
| e1    |            1 |         0 | Sperre (Tripel aus Kasten)     |
| e2    |            0 |         0 | –                             |

## Entscheidungen

1. Zone f1 und f3 haben keinen Doppelpunkt, f2 endet vor der
   Klammer; kette und sprosse_text reichen bis dorthin.
2. Das Zone-Paar steht in f1 (Minus beim Ausklammern), weil es der
   Handgriff der Umformung in Einheit 2 ist; „Typische Fehler“
   führt nur ein Muster, und das gehört ins Lernblatt.
3. e1 hat keine Pflichtelemente: Der Katalog führt für Einheit 1
   keinen Typ und kein „Dazu“, und „Typische Fehler“ trägt kein
   Muster dieser Einheit.
4. Die Prüfungshöhe von e1 („die Begriffe in den Nachbarthemen
   anwenden“) steht mit original null und ohne Prüfkennung.
5. e2 schreibt die Koeffizienten als $p$ und $q$ mit $p + q = 1$,
   weil „r + s = 1“, „r = 1 − s“ und „(1 − s) ·“ aus Kasten und
   Original gesperrt sind; der Punkt heißt $X$.
6. Die zwei Originale von e2 sind dieselbe Aufgabe (Heft und Pool);
   jedes bekommt 2 Zeilen, in vier verschiedenen Kontexten.
7. Keine Pflicht darstellung und anwendung in e2: Der Katalog nennt
   dort nur Fehler finden und Begründen.
8. Die Zone folgt der Reihenfolge der Fertigkeiten in der Mappe,
   nicht der ersten Verwendung (unterrichtsblatt 2.2).

## Befunde

- Katalog: Beide Erkennungsschritte (vor e1 und e2) verlangen
  denselben Handgriff wie die Vorstufe der Kette derselben Einheit;
  sie entfallen, die Vorstufen bleiben.
- Katalog: „Grundfall, viermal“ widerspricht bank.md (5 Zeilen); die
  Bank folgt bank.md.
- Prüfskript: Die Sperre greift auch den Gegenstand der Kette
  („r + s = 1“), weil der Sprossentext ihn in Worten nennt („r plus
  s gleich eins“); die Ausnahme aus bank.md läuft damit ins Leere.
- Prüfskript: Bei Nachweisen mit Vektorergebnis prüft pruef nur die
  Komponenten des Richtungsvektors, nicht die Umformung.

## Offene Punkte

- e1 ist ohne Pflichtelemente dünn (18 Zeilen); ob Begründen zur
  Grundvorstellung („abhängig heißt keine neue Richtung“) dazu soll,
  entscheidet der Katalog.
