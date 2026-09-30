# Stand: integrationsregeln

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     15 |      – |       6 |       8 |      – |       1 |
| e1    |     18 |      4 |       5 |       6 |      3 |       – |
| e2    |     23 |      4 |       5 |       6 |      2 |       6 |

## Originale je Einheit

- e1: keines (Prüfungshöhe ohne Original, 3 Zeilen)
- e2: 2022-bebb-lk-B2.2g

## Prüfskript vor der Korrektur

- zone: 0 Abweichungen, 0 Warnungen
- e1: 0 Abweichungen, 0 Warnungen
- e2: 9 Abweichungen (Baustein \int nicht in _bausteine.md, 9×),
  0 Warnungen

## Entscheidungen

1. Beide Erkennungsschritte entfallen, weil sie denselben Handgriff
   verlangen wie die Vorstufe der Kette ihrer Einheit.
2. e1 hat keine Pflichtelemente: Die Typen-Zeile nennt „kein Typ“,
   Typische Fehler trägt nur das Muster der Einheit 2.
3. e2 hat nur Fehler finden und Begründen (je 3); Anwendung und
   Darstellungswechsel tragen die Typen der Einheit nicht.
4. Das Integral steht in Worten („das Integral von 0 bis 1 über …“),
   weil das Prüfskript \int nicht kennt.
5. Die Dublette 2022-bebb-lk-B2.2g / 2022MerhoehtBAnalysisWTR2-1d
   zählt als ein Original; beide Zeilen tragen die abi-Kennung.
6. Zone: Folge nach erster Verwendung (Potenzen mit Brüchen vor
   Einheit 1, dann Ableitungsregeln, Terme umformen); Zone-Paar an
   „Terme umformen“ (Vorzeichen ausklammern), weil die Zeile den
   Vorzeichenfehler der Rohdatei nennt.
7. Zone: kette ohne Doppelpunkt ist die Fertigkeit bis zum
   Gedankenstrich („Ableitungsregeln vorwärts, …“).
8. Terme ohne Ziffer nach dem Zusammenziehen (etwa $x^{-2}$) tragen
   pruef "", Stammfunktionen prüfen den ersten Koeffizienten.

## Befunde

- Prüfskript: \int fehlt in STANDARD; ein Integrations-Eintrag kann
  das Integralzeichen sonst nicht setzen (ebenso \binom).
- Katalog: Beide Erkennungsschritte verlangen denselben Handgriff
  wie die Vorstufe der Kette ihrer Einheit.
- Katalog: Einheit 1 hat keinen Typ und kein Original; die Kette
  endet auf einer Prüfungshöhe ohne Vorlage (Vermerk im Katalog).

## Offene Punkte

- Stehen \int und \binom in STANDARD, kann e2 auf das Integralzeichen
  umgestellt werden.

## Nachbesserung 2026-09-30

- Teil 1, Antwortgerüst: 41 Zeilen (e1.jsonl 14, e2.jsonl 13, zone.jsonl 14) –
  im Feld antwort `\leerfeld[X]` → `__ X` und `\leerfeld` → `__`,
  weil bank.md (Feld antwort) das Gerüst „__“ vorschreibt; alle
  Zeilen dieser Dateien mit `\leerfeld` in antwort, ids über
  `git show` des Commits oder das Skript
  werkzeuge/einmalig/leerfeld-antwort-2026-09-30.py.
