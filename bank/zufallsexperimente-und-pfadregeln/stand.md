# Stand: zufallsexperimente-und-pfadregeln

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26)
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen, 2 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone  |     41 |      – |      18 |      22 |      – |       1 |
| e1    |     40 |      4 |       5 |      15 |      4 |      12 |
| e2    |     46 |      4 |       5 |      21 |      4 |      12 |
| e3    |     54 |      4 |       5 |      27 |      6 |      12 |
| e4    |     32 |      4 |       5 |       9 |      2 |      12 |
| e5    |     38 |      4 |       5 |      15 |      2 |      12 |
| e6    |     38 |      4 |       5 |      15 |      2 |      12 |
| e7    |     41 |      4 |       5 |      18 |      2 |      12 |
| e8    |     38 |      4 |       5 |      15 |      2 |      12 |

## Originale je Einheit

- e1: 2023-bebb-lk-B4b
- e2: 2019MgrundlegendBStochastikWTR2-3b
- e3: 2026-bb-ea-A1.10a, 2022-bebb-gk-B4f, 2020-be-gk-B4.1f
- e4: 2021-be-gk-A1.7b
- e5: 2025-bebb-lk-A1.9b
- e6: 2023-bebb-lk-A1.8b
- e7: 2026-bb-ea-A1.10b
- e8: 2022MgrundlegendAStochastik2

## Prüfskript vor der Korrektur

- zone: 13 Abweichungen (merkmal der Sprosse 1 uneinheitlich, 9×),
  0 Warnungen
- e1: 0 Abweichungen, 1 Warnung (Prüfungshöhe ohne Original 2 Zeilen)
- e2: 0 Abweichungen, 1 Warnung (Prüfungshöhe ohne Original 2 Zeilen)
- e3: 0 Abweichungen, 0 Warnungen
- e4: 0 Abweichungen, 0 Warnungen
- e5: 1 Abweichung (Sperre: n − k + 1 aus dem Merkkasten),
  4 Warnungen (Dublette mit zwei Kennungen je 1×)
- e6: 0 Abweichungen, 0 Warnungen
- e7: 1 Abweichung (Sperre: Zahlenpaar 0,4 · 3), 0 Warnungen
- e8: 1 Abweichung (pruef 1/3 nicht an der Ergebnisstelle),
  0 Warnungen

Die zwei Warnungen des Endstands (e1, e2) sind gewollt, siehe
Entscheidung 2.

## Entscheidungen

1. Alle sieben Erkennungsschritte entfallen, weil jede Kette mit
   derselben Ankreuz-Vorstufe beginnt; e3 trägt beide Vorstufen
   („Bleibt p gleich?“, „Ein Pfad oder viele gleiche?“) je zweimal.
2. Prüfungshöhen-Originale ohne Eintrag in Abschnitt 2 der Mappe
   (2023MgrundlegendBStochastikWTR1-2d, …WTR2-3a) stehen mit
   original null in 2 Zeilen wie ein Original, mit Prüfkennung.
3. Eine Dublette (abi und iqb, dieselbe Aufgabe) zählt als ein
   Original; beide Zeilen tragen die abi-Kennung (e5, e6, e7).
4. Originale nur an der Prüfungshöhe; Kettensprossen tragen
   original null, auch wo sie einem Zielmarke-Original ähneln.
5. Typen ohne Kette: e2 „Aussage … ohne Grundgesamtheit
   beurteilen“, e3 „Gleich wahrscheinliche Ergebnisse …“ und
   „Kosten je Erfolg …“; alle übrigen Typen stecken in einer Sprosse.
6. Pflichtelemente in allen acht Einheiten alle vier Arten;
   sprosse_text „Fehler finden“, „Begründen“, „Anwendung“,
   „Darstellungswechsel“, quelle die Typen-Zeile (32–39).
7. Zone: kette ist die Fertigkeit bis zum Gedankenstrich (ohne
   Doppelpunkt in der Zeile), „Kombinatorik“ bis zum Doppelpunkt;
   Folge nach erster Verwendung, Zone-Paar an f7 (ohne Zurücklegen).
8. Binomialkoeffizienten stehen als „n über k“ im Text, weil
   \binom kein Baustein ist.
9. Terme in n (e5 Prüfungshöhe) nennen zusätzlich den Wert für ein
   festes n, damit pruef eine Zahl prüft.
10. Bäume nur mit zwei Ästen je Knoten (\baumzwei, \baumdrei,
    \baumdreigleich); dreiwertige Stufen stehen ohne Baum.

## Befunde

- Katalog: Alle sieben Erkennungsschritte verlangen denselben
  Handgriff wie die Vorstufe der Kette ihrer Einheit.
- Katalog: Merkkasten Einheit 7 (Zeile 131) nennt „siebzehn der
  einundzwanzig Zeilen“, Zeile 24 „siebzehn der dreiundzwanzig“.
- Mappe: Kennungen der Prüfungshöhe außerhalb von Prüfungsform und
  Zielmarke fehlen in Abschnitt 2 (etwa 2026MerhoehtAStochastik21-a).
- Bausteine: Es fehlt ein Baustein für den Binomialkoeffizienten
  und ein Baum mit drei Ästen je Knoten; Stochastik braucht beide.
- Prüfskript: Die Warnung „Prüfungshöhe ohne Original 3“ trifft
  auch Katalog-Originale, die nur in der Mappe fehlen.

## Offene Punkte

- Bäume mit Astlabel „1-p“ und \vierfeldertafel mit Dezimalkomma
  sind ungesetzt; ein LaTeX-Lauf steht aus.
