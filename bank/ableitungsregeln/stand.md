# Stand: ableitungsregeln

Katalog-Commit: f56cacecc590f51abf34cf81948a0d2b751d7d33
(2026-09-28, aus dem Kopf von mappen/ableitungsregeln.md)
Datum: 2026-09-29 15:11 CEST (date)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.9
(--katalog aus der Mappe); Nachzug des Bestands vom 27.09.
(Katalog 95b0f8b). Umbauskript:
werkzeuge/einmalig/nachzug-ableitungsregeln-2026-09-29.py.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      30         0        14      15        0       1
    e1.jsonl        47         8         5      24        4       6
    e2.jsonl        33         8         5      12        2       6
    e3.jsonl        32         4         5      15        2       6

Pflicht je Einheit: fehler 3, begruenden 3 (Typenzeilen 21–23
nennen nur diese); Zone fehler 1 (Paar).

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         30      0              0          0
    e1           36      0             11          0
    e2           18      4             11          0
    e3           21      0             11          0

Umgeschrieben: je Einheit die fünf Grundfallzeilen (Päckchen) und
die sechs Pflichtzeilen (bei v1 von fehler und begruenden nur
merkmal). Nachgezogen in allen übernommenen Zeilen: quelle
(Katalog 97 → 96, 98 → 97, 99 → 98, 38 → 37) und id; in e2 die
alte Vorstufe als Sprosse −1 mit dem Sprossentext bis „nichts
rechnen“.

## Originale je Einheit

- e1: 2026-C-1c, 2025-C-1c, 2026-B-1c, 2019-be-gk-A1.1a, 2024-C-1c,
  2021MerhoehtAAnalysis12-a, 2025-bebb-lk-B2.1b,
  2022MgrundlegendBAnalysisWTR1-1c, 2022-B-1a, 2021-A-1a;
  Prüfungshöhe 2024-B-1d, 2023-C-1b.
- e2: 2024MerhoehtAAnalysis23, 2017MerhoehtBAnalysisWTR1-3d;
  Prüfungshöhe 2020MerhoehtAAnalysis22.
- e3: 2021MerhoehtAAnalysis13-a, 2022-bebb-lk-B2.2b,
  2022MerhoehtBAnalysisWTR2-1b, 2024MgrundlegendBAnalysisWTR1-1a,
  2022-bebb-lk-A1.4a, 2020-be-gk-B2.1c, 2024-bebb-lk-B2.1d,
  2018-bb-ea-B2.1e, 2026MgrundlegendAAnalysis21-b;
  Prüfungshöhe 2025MerhoehtAAnalysis21-a.

## Prüfskript vor der Korrektur

- Bestand vor dem Nachzug (v0.9 --katalog): 80 Abweichungen, alle
  „sprosse_text nicht wortgleich in Zeile“ (Zeilen verschoben).
- zone.jsonl: 0 / 0 (unverändert).
- e1.jsonl: 0 / 0.
- e2.jsonl: 0 / 0.
- e3.jsonl: 1 / 0 – pruef nicht an der Ergebnisstelle (Päckchen-
  zeile mit Vorfaktor −1); eine Zeile korrigiert.
- Keine Einheit ist zweimal gescheitert.

## Entscheidungen

- Zone bleibt: Fertigkeiten (Zeilen 28–34) unverändert.
- Päckchen: e1 „2x³ − 5x + 4“ fest, der Koeffizient von x² wandert;
  e2 „e^(kx)“ fest, k wandert; e3 „x² · eˣ“ fest, der Vorfaktor
  wandert (Sek-II-Form mit festem Term statt fester Zahl).
- Schreibform der Kettenregel (Hinweis Sek II, regeln.md 12): innere
  Funktion, äußere Funktion, innere Ableitung, äußere Ableitung,
  zusammensetzen, Ergebnis; die Vorstufe 0 schreibt nur die ersten
  beiden Zeilen oder setzt rückwärts zusammen.
- Vorstufe 0 in e2: zwei Varianten zerlegen, zwei setzen rückwärts
  zusammen (Sprossentext nennt beide Richtungen).
- P1-Serie in allen drei Einheiten (Kennzeichen: Exponent,
  Konstante, Vorfaktor bzw. innere Ableitung, Vorzeichen), weil
  keine Einheit Gleichungen umformt (P3 entfällt).
- P6-Personenaussagen am häufigsten Muster der Einheit (Parameter,
  e-Funktion als eigene Ableitung, innere Ableitung im e-Faktor);
  alle drei mit „Nein“, P2 je Einheit „Richtig“ als Gegengewicht.
- Grundfallwerte e2 ohne k = 4 und k = −6, weil e^(4x) und
  e^(−6x) schon in Pflichtzeilen stehen (keine Aufgabe doppelt).

## Befunde

- Katalog: Zeile 97 trennt die Vorstufen mit „(Vorstufe) →“; der
  Sprossentext von −1 endet daher bei „nichts rechnen“, die Klammer
  bleibt draußen.
- Katalog: Erkennungsschritt „Welche Regel?“ wiederholt die Vorstufe
  von e1, „Innen und außen?“ die Vorstufe −1 von e2; beide
  entfallen, die Vorstufen bleiben (wie 27.09.).
- Katalog: „Zahl oder Variable?“ steht als Erkennungsschritt vor e1
  (k1) und gilt laut Zeile 37 auch vor e3; in e3 steht er nicht
  noch einmal (bank.md: einmal, in der ersten Einheit).
- Prüfskript: prüft die Form der Pflichtzeilen (P1–P6) nicht; die
  drei Formen je Einheit sind nur durch Durchsicht gesichert.
- Prüfskript: Doppel nur bei gleicher aufgabe; derselbe Term in
  einer Grundfall- und einer Pflichtzeile fiel nicht auf.

## Offene Punkte

- Ohne Zeile wie 27.09.: 2017-be-gk-B1.2a, 2017-be-gk-cas-B1.2b,
  2018-bb-ea-cas-B2.1e, 2017MgrundlegendBAnalysisWTR-1d,
  2017MerhoehtBAnalysisWTR2-1d.
- Grundvorstellung (Zeile 94) steht nicht in der Bank.
- Schrittnamen nur in neuen und umgeschriebenen Zeilen; der
  übernommene Bestand zeigt Rechnung ohne Schrittnamen.
- gegenlese.md, gegenlese2.md und uebersicht.md beziehen sich auf
  den Stand vom 27./28.09. und sind nicht nachgezogen.
