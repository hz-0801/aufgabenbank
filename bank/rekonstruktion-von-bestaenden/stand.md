# Stand: rekonstruktion-von-bestaenden

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27 15:00 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     22 |        – |        10 |      11 |        – |       1 |
| e1    |     41 |        4 |         5 |      15 |        5 |      12 |
| e2    |     32 |        4 |         5 |       9 |        2 |      12 |
| e3    |     27 |        – |         5 |       6 |        4 |      12 |

## Originale je Einheit

- e1: 2017MerhoehtBAnalysisWTR1-2d, 2017MgrundlegendBAnalysisCAS-2e,
  2021MerhoehtAAnalysis13-c, 2022MerhoehtBAnalysisWTR1-1c,
  2024-bebb-lk-B2.2i, 2024MgrundlegendBAnalysisWTR1-2d,
  2025-bebb-lk-B2.1h, 2026-bb-ea-B2.2g
- e2: 2017MerhoehtBAnalysisWTR1-2b, 2018MgrundlegendAAnalysis2-a,
  2021MgrundlegendBAnalysisWTR-2b, 2023-bebb-lk-B2.2d,
  2023-bebb-lk-B2.2e, 2026MerhoehtBAnalysisMMS2-1d
- e3: 2019-be-gk-B2.1g, 2024MgrundlegendBAnalysisWTR2-2e,
  2026MerhoehtBAnalysisMMS1-1g

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund |
|-------|-------------:|----------:|------------------|
| zone  |            0 |         0 | –                |
| e1    |            0 |         0 | –                |
| e2    |            0 |         0 | –                |
| e3    |            0 |         0 | –                |

Die Sperrprobe lief vor dem Schreiben mit und fand nichts. In e1 wurde
nach dem Lauf eine Zeile inhaltlich korrigiert (falscher Zwischenwert
in der Fehler-finden-Rechnung von Mila), ohne Meldung des Skripts.

## Entscheidungen

- Zone: kette und sprosse_text enden am Doppelpunkt, wo die Fertigkeit
  einen hat, sonst am Gedankenstrich.
- Das Zone-Paar gehört zum Fallstrick „Minuten und Stunden nicht
  angeglichen“ in der Fertigkeit Einheiten umrechnen.
- Integrale stehen als Zeichen ∫ mit Grenzen, Grenzwerte als
  \mathrm{lim}, weil \int und \lim keine erlaubten Befehle sind.
- Pooldubletten zählen als ein Original; das Feld trägt die Kennung
  des Landeshefts (2024-bebb-lk-B2.2i, 2026-bb-ea-B2.2g, 2023-bebb-lk-
  B2.2d).
- Die Prüfungshöhe „Zunahme samt mittlerer Änderungsrate“ in e1 hat
  kein Original in der Mappe: original null, 3 Zeilen.
- e3 hat keine Vorstufe; der Katalog nennt „Wo kippt der Bestand?“
  dort nur als Anschluss an e2, die Kette beginnt beim Grundfall.
- Typen ohne Kette: e1 der Zeitpunkt gleichen Bestands über das
  Integral gleich null, e2 der Zeitraum der Abnahme, je 3 Zeilen.
- Begründungen an Kettensprossen (Grundfall e2) tragen als pruef die
  Nullstellen der Rate, weil dort pruef nicht leer sein darf.
- Pflichtelemente sind die Sprossen 1–4 der Pflichtkette; darstellung
  und anwendung tragen einen Typnamen der Einheit als sprosse_text.

## Befunde

- Katalog: „Bestand oder Rate?“ und „Was war schon da?“ sind
  Erkennungsschritte und Vorstufe von e1, „Wo kippt der Bestand?“
  Erkennungsschritt und Vorstufe von e2; die Erkennungsschritte
  entfallen.
- Prüfskript und Bausteine: \int und \lim fehlen; Integrale lassen
  sich nur als Unicode-Zeichen ∫ schreiben.
- Prüfskript: pruef "" gilt nur für pflicht begruenden, nicht für
  Begründungen an Kettensprossen; dort braucht es einen Ersatzwert.
- Mappe: Die Sprossenzeilen nennen 2023-bebb-lk-B2.2f,
  2023MerhoehtBAnalysisWTR1-1f und 2023-bebb-lk-B2.2g, Abschnitt 2
  führt sie nicht.

## Offene Punkte

- Ob die Vorlage das Zeichen ∫ setzt, ist ungeprüft (kein LaTeX in
  der Sitzung); sonst ∫ beim Zusammenbau durch \int ersetzen.
- loesungsgrafik ist nur bei den zwei Skizzieraufgaben ohne feste
  Punktlösung gefüllt.

## Nachbesserung Gegenlese 2026-09-28
- Grundlage: gegenlese.md und gegenlese2.md (Abgleich); geändert nur rechnerisch falsche Zeilen (beide Leser oder ein Leser plus eigene sympy-Rechnung); Übriges in bank/_strittig.md.
- rekonstruktion-von-bestaenden-e1-k3-s4-v3: Modellbereich $0 \le t \le 5$ ergab Ladestand 115 % (über 100 % ab t ≈ 3,06) → $0 \le t \le 3$ (höchstens 99 %); Lösung 64 und 79 % unverändert (Regel a).
- Prüfskript: Abweichungen 0.
