# Stand: strahlensaetze

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py, am Ende 0 Abweichungen,
0 Warnungen in allen Dateien.

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        – |        18 |      20 |        – |       1 |    39 |
| e1    |       12 |        10 |      42 |        6 |      12 |    82 |
| e2    |        4 |         5 |      33 |        3 |       9 |    54 |
| e3    |        4 |         5 |      27 |        3 |      12 |    51 |
| Summe |       20 |        38 |     122 |       12 |      34 |   226 |

## Originale je Einheit

- e1: 2018-OS-K6c, 2015-OS-K6a (Kette Maßstab umrechnen),
  2021-OS-K4c (Kette Maßstabsgerecht zeichnen), je 2 Zeilen.
- e2, e3: keine; Prüfungshöhe ohne Original, 3 Zeilen.

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund                          |
|-------|-----:|------:|-------------------------------------------|
| zone  |    1 |     0 | Baustein \ell nicht in _bausteine.md      |
| e1    |   18 |     0 | pruef-Zahl nicht an der Ergebnisstelle    |
| e2    |    3 |     0 | Sperre k = 0,5 (Merkkasten, Zeile 53)     |
| e3    |    0 |     0 | –                                         |

## Entscheidungen

1. Beide Verfahrensketten von e1 enden mit hoehe pruefung, weil
   der Katalog jeder eine Prüfungshöhe mit eigenen Originalen
   gibt; e1 hat damit zwei Prüfungssprossen.
2. Zone: Die Fertigkeitszeilen haben keinen Doppelpunkt nach dem
   Namen; kette und sprosse_text sind die Zeile bis „– Einheit“.
3. Zone-Folge nach erster Einheit, sonst Folge des Eintrags; die
   Draufsicht (f6, Einheit 1) steht daher vor dem Verhältnis (f7).
4. Typen ohne Kette: kette ist der Typname bis zur Klammer oder
   zum Doppelpunkt, sprosse_text der Typ wortgleich.
5. Pflicht darstellung nur in e1 (1 : n ↔ „1 cm ≙ …“) und e3
   (Figur ↔ Verhältnisgleichung); e2 trägt keinen Wechsel, der
   nicht schon Kettensprosse ist.
6. sprosse_text von anwendung und darstellung ist der nächste Typ
   aus „Typen je Lerneinheit“ (etwa „Sachaufgabe mit Skizze …“).
7. Zeichenfeld und Karoraster sind ein leeres ksys; der
   Skizzenplatz zu „Fertige eine Skizze an“ ist
   \rechenplatz[halb]{4}, die Lösungsskizze steht in
   loesungsgrafik.
8. \strahlensatz steht ohne strecken= und punkte=, weil deren
   Belegung in _bausteine.md fehlt; Namen und Maße (Z, A, A′, B,
   B′ wie im Merkkasten) stehen im Aufgabentext.
9. Ein Maßstab 1 : n als Ergebnis wird über die Rechnung geprüft
   (pruef = Wirklichkeit : Zeichnung, loesung „… = n, also 1 : n“).
10. Maßstab selbst wählen (e1 k3 s7) hat pruef "", weil mehrere
    Maßstäbe richtig sind.

## Befunde

- Katalog: Die Erkennungsschritte „Kleiner oder größer?“, „Mal
  oder geteilt?“, „Passt es ins Feld?“, „Gleiche Form?“, „Welche
  Seite gehört zu welcher?“, „V oder X?“ und „Vom Zentrum aus?“
  wiederholen die Vorstufe ihrer Kette und entfallen; es bleibt
  nur „Gleiche Einheit?“ (e1 k1).
- Auftrag: Die Gegenprobe „genau eine Sprosse mit hoehe pruefung
  je Einheit“ passt nicht auf e1 mit zwei Verfahrensketten, deren
  jede im Katalog eine Prüfungshöhe hat.
- bank.md: „Fertigkeit bis zum Doppelpunkt“ passt nicht auf
  Fertigkeitszeilen ohne Namen mit Doppelpunkt.
- Prüfskript: liest in „1 : n“ die Zahl n nicht als
  Ergebnisstelle.
- Prüfskript: prüft nicht, ob die ersten zwei Argumente von
  \punkt Zahlen sind; vertauschte Argumente in e2 liefen ohne
  Abweichung durch (selbst gefunden, korrigiert).
- Prüfskript: Die Ankreuzprobe nimmt eine Option, die Teilwort
  einer anderen ist („ähnlich“ in „nicht ähnlich“), als eindeutig
  (in e2 bei der Gegenprobe gefunden, Optionen umbenannt).
- _bausteine.md: Die Optionen strecken= und punkte= von
  \strahlensatz sind nicht erklärt.

## Offene Punkte

- Die Standardbeschriftung der \strahlensatz-Grafiken beim
  Zusammenbau gegen die Namen im Aufgabentext prüfen.
- Ein leeres ksys als Karofeld zeigt Achsen; ein Rasterbaustein
  ohne Achsen fehlt in der Vorlage.
- Die Gegenprobe der Kastenzahlen findet „10“ nur in der
  Prüfkennung „P10“; sonst keine Kastenzahl in einer aufgabe.

## Nachbesserung 2026-09-27

- Prüfskript v0.5: 0 Abweichungen, 0 Warnungen vor und nach der
  Nachbesserung; keine Zeile geändert.
- Die Prüfungshöhen ohne Original (e2 k1 s12, e3 k1 s9) stehen
  schon als hoehe pruefung mit original null.
- Der Erkennungsschritt „Gleiche Einheit?“ (e1 k1) bleibt: Er
  verlangt einen anderen Handgriff als die Vorstufen von k2
  („kleiner oder größer“, „mal oder geteilt“) und k3 („passt es
  ins Feld“).
- Kein Befund ist mit v0.5 erledigt; die Ankreuzprobe nimmt
  weiter eine Lösung an, die mit der kürzeren Option beginnt
  („ähnlich oder nicht ähnlich“ bei den Optionen „ähnlich“ und
  „nicht ähnlich“).
