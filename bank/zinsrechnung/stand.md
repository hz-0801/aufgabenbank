# Stand: zinsrechnung

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
Datum: 2026-09-27 12:22 UTC

## Zeilen

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        0 |        16 |      18 |        0 |       1 |    35 |
| e1    |        8 |        10 |      39 |        9 |       9 |    75 |
| e2    |        4 |         5 |      30 |        4 |      12 |    55 |

## Originale

- e1: 2015-OS-B1e, 2014-OS-B1e, 2014-OS-K3a
- e2: 2014-OS-K3b, 2014-OS-K3c

## Prüfskript vor der Korrektur

- zone: 3 Abweichungen, 0 Warnungen; merkmal je Sprosse uneinheitlich.
- e1: 5 Abweichungen, 0 Warnungen; merkmal je Sprosse uneinheitlich.
- e2: 1 Abweichung, 0 Warnungen; Lösungszahl falsch gerechnet.
- Eigene Kastenprobe e2: 2 Treffer (Einzahlung 100 €), korrigiert.

## Entscheidungen

- Alle fünf Erkennungsschritte entfallen, sie wiederholen die
  Vorstufen der drei Ketten (Befund).
- Einheit 1 hat zwei Verfahrensketten; hoehe pruefung nur in
  „Zinsen berechnen" (drei Originale, 6 Zeilen), damit die Einheit
  genau eine Prüfungssprosse hat. (überholt, Nachbesserung
  2026-09-27)
- Die Zielmarke von „Monats- und Tageszinsen" steht als hoehe
  sprosse, original null, 3 Zeilen (unterrichtsblatt 2.4 c).
  (überholt, Nachbesserung 2026-09-27)
- Eine Prüfungssprosse mit mehreren Originalen trägt als
  sprosse_text den ganzen Prüfungshöhe-Text der Kettenzeile.
- Typen ohne Kette: e1 Überschlag; e2 Tabelle mit jährlicher
  Einzahlung, Ratenkauf und Kredit mit Zinseszins.
- Startkapital rückwärts und Verdopplung durch Probieren stehen in
  der Sprosse „Startkapital oder Laufzeit rückwärts".
- darstellung nur in e2 (Wachstumsfaktor, Tabelle, Rechnung); die
  Typen von e1 tragen keinen Darstellungswechsel.
- sprosse_text der Pflichtelemente anwendung und darstellung: der
  passende Typ aus „Typen je Lerneinheit".
- Zone: Fertigkeit ohne Doppelpunkt bis vor „– Einheit";
  Grundwert ohne Fallstrick; Zone-Paar zu „Prozentsatz ohne Komma".
- Die Kastenzahlen 12, 30, 100 und 360 stehen in keiner aufgabe;
  Monate, Tage und Bankjahr werden in Worten genannt.

## Nachbesserung 2026-09-27

- Prüfskript v0.5 meldet vorher und nachher 0 Abweichungen und
  0 Warnungen.
- e1 „Monats- und Tageszinsen“ s5 (Zeilen 61–63): Die Zielmarke
  ohne P10-Original steht jetzt als hoehe pruefung statt sprosse,
  original null, 3 Zeilen; die Tabelle der Zeilen ist angepasst.
- Die fünf Erkennungsschritte sind schon entfallen; kein weiterer
  Erkennungsschritt doppelt eine Vorstufe.

## Befunde

- Katalog: Alle fünf Erkennungsschritte verlangen denselben
  Handgriff wie die Vorstufen der Ketten; der Katalog führt beide.
- bank.md: Die Regel „Prüfungshöhe ohne Original = hoehe pruefung"
  und „genau eine Prüfungssprosse je Einheit" widersprechen sich,
  wenn eine Einheit zwei Ketten hat. (erledigt v0.5)
- Prüfskript: Es prüft keine Zahlen in aufgabe (vorgegebene
  Fehlrechnung) und keine einzelnen Kastenzahlen; beides fiel erst
  bei der eigenen Probe auf.

## Offene Punkte

- Die 72er-Regel (Vorrat) ist nicht geübt.
- e1 hat kein Pflichtelement darstellung.
- zone f4 und f5: merkmal der zweiten Grundfall-Zeile passt nur
  ungefähr (Multiplizieren, fester Faktor pro Tag).

## Umsetzung Duden-Abgleich und Leiterregeln (2026-10-02)

Katalog: zinsrechnung.md, Commit b97e699 (Abgleich
katalog/_abgleich-duden9-kap9.md). Zeilen e1 75 → 86, e2 55 → 60.

Neue Sprossen (je 3 Zeilen): e1 k1 gemischt (Jahreszinsen), e1 k2
gemischte Zinstabelle (zwei Entwürfe aus
eingang/duden9-2026-10-02/neu-pz-duden9.jsonl, eine neu), e2 k1
gemischt (Zinseszins). Zusatzzeilen aus dem Duden-Eingang (Beschluss 6):
e1 k1 s0 v5, e1 k1 s6 v4–v5, e1 k2 s3 v4–v5, e2 k1 s6 v4–v5; die
Gruppen mit Zusatzzeilen tragen jetzt den wortgleichen sprosse_text und
die neue quelle. Prüfskript: 0 Abweichungen, 4 Warnungen (Menge); mit
--katalog 100 → 74, alle in unveränderten alten Zeilen. Altbefund:
e1 k1 s1/s2 stehen in der Bank in umgekehrter Folge wie im Katalog
(Dezimalzahl vor 1 %-Weg) – nicht angefasst.
