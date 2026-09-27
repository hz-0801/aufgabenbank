# Stand: funktionsscharen-und-ortskurven

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
(2026-09-26, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“)
Datum: 2026-09-27
Prüfskript: bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     30 |        – |        14 |      15 |        – |       1 |
| e1    |     40 |        4 |         5 |      18 |        4 |       9 |
| e2    |     37 |        4 |         5 |      18 |        4 |       6 |
| e3    |     36 |        – |         5 |      18 |        4 |       9 |
| e4    |     42 |        4 |         5 |      18 |        6 |       9 |
| e5    |     37 |        4 |         5 |      18 |        4 |       6 |
| Summe |    222 |       16 |        39 |     105 |       22 |      40 |

Pflicht: fehler und begruenden je 3 in e1–e5; anwendung je 3 in
e1, e3, e4.

## Originale je Einheit

- e1, Prüfungshöhe: 2024MerhoehtBAnalysisWTR1-2d,
  2024MerhoehtBAnalysisWTR1-2a. Kette: 2024-bebb-lk-A1.1a,
  2022-bebb-lk-A1.3a, 2025MerhoehtBAnalysisWTR1-1a,
  2025MerhoehtBAnalysisWTR3-1a, 2025MerhoehtBAnalysisWTR2-2a,
  2023MgrundlegendBAnalysisWTR1-3a, 2019-be-gk-B2.2h,
  2022MerhoehtAAnalysis13-a.
- e2, Prüfungshöhe: 2022-bebb-lk-B2.2k, 2026MerhoehtBAnalysisMMS1-1a.
  Kette: 2026MerhoehtBAnalysisMMS2-2a, 2024MerhoehtAAnalysis13-a,
  2026MerhoehtBAnalysisWTR2-1a, 2018-bb-ea-B2.1a,
  2018MerhoehtBAnalysisCAS1-1e, 2024-bebb-lk-B2.1a,
  2023-bebb-lk-B2.2h, 2025MerhoehtBAnalysisMMS2-1a,
  2018MerhoehtBAnalysisCAS1-1d, 2026-bb-ea-B2.1a,
  2025MerhoehtAAnalysis11-a, 2022-bebb-lk-B2.1c.
- e3, Prüfungshöhe: 2018-bb-ea-B2.2e, 2026MerhoehtAAnalysis22.
  Kette: 2020MerhoehtAAnalysis13-a, 2024MerhoehtBAnalysisWTR3-2b,
  2026-bb-ea-B2.2a, 2020MgrundlegendBAnalysisWTR1-1g,
  2017-bb-ea-B2.1b, 2017-bb-ea-B2.2b, 2018-bb-ea-cas-B2.1d,
  2018MerhoehtBAnalysisWTR1-2f, 2025-bebb-lk-B2.1c,
  2025MerhoehtBAnalysisMMS1-1b, 2017MerhoehtBAnalysisWTR2-1e;
  Pflicht anwendung: 2017MgrundlegendBAnalysisCAS-2d.
- e4, Prüfungshöhe: 2022-bebb-lk-B2.2o, 2023-bebb-lk-B2.1a,
  2020MerhoehtAAnalysis21-b. Kette: 2024MgrundlegendBAnalysisWTR1-1e,
  2017MgrundlegendAAnalysis2-b, 2017-bb-ea-cas-B2.1f,
  2021MerhoehtAAnalysis12-b, 2022-bebb-lk-A1.2b,
  2017MgrundlegendBAnalysisCAS-2c, 2018MerhoehtBAnalysisCAS3-1f,
  2018MerhoehtBAnalysisWTR2-1d, 2022MerhoehtBAnalysisWTR1-1e,
  2022MgrundlegendBAnalysisWTR1-2c, 2017MerhoehtBAnalysisCAS2-1b,
  2018MerhoehtBAnalysisCAS3-2a.
- e5, Prüfungshöhe: 2022-bebb-lk-B2.2n, 2023MerhoehtBAnalysisWTR1-2d.
  Kette: 2017MerhoehtBAnalysisCAS1-1c, 2017MerhoehtBAnalysisCAS2-1e,
  2020MgrundlegendBAnalysisWTR2-2a.

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund             |
|-------|-------------:|----------:|------------------------------|
| zone  |            0 |         0 | –                            |
| e1    |            1 |         0 | Sperre (k = 1/2, Original)   |
| e2    |            0 |         0 | –                            |
| e3    |            2 |         0 | Ergebnisstelle (Bruch)       |
| e4    |            0 |         0 | –                            |
| e5    |            2 |         0 | Ergebnisstelle, Sperre je 1  |

## Entscheidungen

1. Zone f2 und f5 haben keinen Doppelpunkt; kette und sprosse_text
   reichen dort bis zum Gedankenstrich.
2. Das Zone-Paar steht in f1 (Exponenten mit Buchstaben), weil
   „Vorzeichen und Exponenten mit Parameter verrechnet“ die meisten
   Belege unter „Typische Fehler“ hat.
3. Prüfungshöhe: 2 Zeilen je Original, das die Sprossenzeile unter
   „Prüfungshöhe“ nennt und das in Abschnitt 2 der Mappe steht;
   e4 hat damit 6 Zeilen, die übrigen Einheiten 4.
4. sprosse_text der Prüfungshöhe ist der Teilsatz, zu dem das erste
   aufgenommene Original gehört (e3: „genau eine waagerechte
   Tangente über die Diskriminante“).
5. Kettensprossen tragen original, wo eine Variante ein Original aus
   Abschnitt 2 verfremdet, auch wenn die Sprosse eine andere Kennung
   nennt und der Typ passt (etwa 2018MerhoehtBAnalysisCAS1-1d an e2).
6. Pflicht anwendung nur in e1, e3, e4, wo Typen mit Sachkontext
   stehen; e2 und e5 führen nur innermathematische Typen.
7. Keine Pflicht darstellung: Zuordnen und Skizzieren stehen in e1
   als eigene Kettensprossen; sprosse_text der Pflicht anwendung ist
   ein Typname aus „Typen je Lerneinheit“ (kein Katalogtext).
8. Keine Zeilen für Typen ohne Kette: Jeder Typ der fünf Einheiten
   gehört zu einer Kettensprosse.
9. Integrale und Grenzwerte stehen in Worten, ln und sin als
   \mathrm{…}, weil \int, \lim und \ln das Prüfskript nicht kennt.
10. pruef bei Termergebnissen: die Zahl an der Ergebnisstelle
    (Koeffizient, bei a/k-Brüchen der Zähler).

## Befunde

- Katalog: Die vier Erkennungsschritte (vor e1, e2, e4, e5)
  verlangen denselben Handgriff wie die Vorstufe der Kette derselben
  Einheit; sie entfallen, die Vorstufen bleiben.
- Katalog: „Grundfall, viermal“ in den Sprossenzeilen widerspricht
  bank.md (5 Zeilen je Grundfall); die Bank folgt bank.md.
- Katalog/Mappe: Die Prüfungshöhen nennen Kennungen, die nicht in
  Abschnitt 2 stehen (etwa 2022MerhoehtBAnalysisWTR1-1g,
  2023-bebb-lk-B2.2j, 2023-bebb-lk-B2.1g, 2025MerhoehtBAnalysisWTR2-2b,
  2022MerhoehtAAnalysis13-b); diese Teile haben keine Zeilen.
- Prüfskript: \int, \lim und \ln fehlen in STANDARD, obwohl Sek II
  sie braucht.
- Prüfskript: Die Ergebnisstelle kennt keine Terme im Parameter
  (16a, 3a/4); bei Termergebnissen prüft pruef nur Zahlanteile.
- Gegenprobe: Mehrstellige Zahlen im Merkkasten sind außer 27 nur
  Kennungsteile (11, 12, 13) und Jahre; 27 steht in keiner aufgabe.

## Offene Punkte

- LaTeX nicht kompiliert: \funktion mit exp() und die ksys-Bereiche
  der Grafiken sind nicht am Bild geprüft.
- Die Prüfungshöhen-Teile ohne Mappenoriginal (e1 Eignung am Bild,
  e3 Tiefpunkt oder Sattelpunkt, e5 Schnittwinkel, Ursprungsabstand,
  Punktsymmetrie, Schnittstellen) sind nicht belegt.
