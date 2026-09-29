# Stand: zufallsexperimente-und-pfadregeln

Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719
(2026-09-28, aus dem Kopf von mappen/zufallsexperimente-und-
pfadregeln.md)
Datum: 2026-09-29 20:43 CEST (date)
Grundlage: bank.md fünfte Fassung (29b), werkzeuge/bank-pruef.py
v0.10 (--katalog aus der Mappe), Vorlage auftrag-eintrag.md 29e;
Nachzug des Bestands vom 27.09. (Katalog 95b0f8b). Umbauskript:
werkzeuge/einmalig/nachzug-zufallsexperimente-und-pfadregeln-
2026-09-29.py. Endstand: 0 Abweichungen, 0 Warnungen.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      41         0        18      22        0       1
    e1.jsonl        41         4         5      15        5      12
    e2.jsonl        47         4         5      21        5      12
    e3.jsonl        57         4         5      30        6      12
    e4.jsonl        32         4         5       9        2      12
    e5.jsonl        38         4         5      15        2      12
    e6.jsonl        38         4         5      15        2      12
    e7.jsonl        41         4         5      18        2      12
    e8.jsonl        38         4         5      15        2      12
    gesamt         373        32        58     160       26      97

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         41      0              0          0
    e1           28      1             12          0
    e2           34      1             12          0
    e3           42      3             12          0
    e4           20      0             12          0
    e5           26      0             12          0
    e6           26      0             12          0
    e7           29      0             12          0
    e8           26      0             12          0

Übernommen: aufgabe, loesung, merkmal wortgleich; nachgezogen
quelle (161–168 → 155–162), bei e3 ab Sprosse 6 sprosse und id,
sprosse_text bei den Vorstufen (Katalogtext bis „nichts rechnen“),
bei den Prüfungshöhen von e1 und e3 (ganzes Glied) und bei
anwendung und darstellung (mit quelle).
Umgeschrieben: je Einheit die fünf Grundfallzeilen (Päckchen),
fehler v2/v3 und begruenden v2/v3 (Pflichtformen) samt merkmal
von v1, eine anwendung-Zeile (Grenzwert, P8).
Neu: e3 s6 „Lückenterm“ (3); je eine Zeile ohne Original an der
Prüfungshöhe von e1 und e2 (dritte Zeile, Menge 3).

## Originale je Einheit

- e1: 2023-bebb-lk-B4b (Prüfung)
- e2: 2019MgrundlegendBStochastikWTR2-3b (Prüfung)
- e3: 2026-bb-ea-A1.10a, 2022-bebb-gk-B4f, 2020-be-gk-B4.1f
  (Prüfung)
- e4: 2021-be-gk-A1.7b (Prüfung)
- e5: 2025-bebb-lk-A1.9b (Prüfung)
- e6: 2023-bebb-lk-A1.8b (Prüfung)
- e7: 2026-bb-ea-A1.10b (Prüfung)
- e8: 2022MgrundlegendAStochastik2 (Prüfung)

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe mit `--katalog`: 270 Abweichungen
  (e1 34, e2 37, e3 42, e4 26, e5 32, e6 32, e7 35, e8 32), alle
  „sprosse_text nicht wortgleich in Zeile quelle“ (Katalogzeilen
  um sechs verschoben); 2 Warnungen (e1, e2: Prüfungshöhe ohne
  Original 2 Zeilen, Menge 3).
- Erster Wurf: e8 1 (Sperre: a = 0,4 aus 2021-be-gk-B4f in einer
  Personenaussage), alle übrigen 0. Zweiter Wurf: 0. Warnungen 0.
  Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Zone bleibt: Fertigkeiten (Zeilen 44–52) unverändert.
2. Päckchen: e1 Münze fest, Sektorenzahl wandert; e2 60 Lose fest,
   Gewinnzahl wandert; e3 Rad fest, p wandert; e4 Urne 4 rot/6 blau
   fest, der Pfad wandert; e5 zehn Kugeln fest, Rotzahl wandert
   (drei mit, zwei ohne Zurücklegen); e6 30 %/40 % fest, der Anteil
   unter N wandert; e7 Münze 0,6 fest, der Term wandert; e8
   60 %/50 % fest, die Randwahrscheinlichkeit wandert.
3. Pflichtzeilen: sprosse_text der anwendung aus Zeile 6
   („Anwendungssituationen mithilfe von Urnenmodellen
   untersuchen“), der darstellung aus einem Typ oder Kastensatz je
   Einheit (Zeilen 33–38, 52, 103, 130); die Typen-Zeile nennt
   beides nicht.
4. Pflichtformen: fehler v1 Schülerrechnung (übernommen), v2 P2,
   v3 P1 (e8 P3, Umformungskette); begruenden v1 „Begründe“, v2
   P4, v3 P6; die P1-Serie in e3 trägt die Plausibilitätszeile
   „bei sieben Würfen 7/6 > 1“.
5. Urteile: P2 achtmal „Richtig“, P6 siebenmal Nein, einmal Ja
   (e4), P8 sechsmal Ja, zweimal Nein (e4, e6).
6. Lückenterm „P = 1 − (__)^__“ steht im Feld antwort; pruef
   prüft Basis und Exponent.
7. Neue Antwortgerüste „P = __“; übernommene Zeilen behalten
   „P = \leerfeld“.
8. Prüfungshöhen ohne Original in Abschnitt 2 (e1
   2023MgrundlegendBStochastikWTR1-2d, e2 …WTR2-3a) mit einer
   dritten Zeile auf Menge 3 gebracht, original null.

## Befunde

- Katalog: Der Erkennungsschritt „Anteil aller oder Anteil
  unter …?“ (Zeile 54) wiederholt die Vorstufe von e6; er entfällt.
- Katalog: Die Typen-Zeilen 32–39 nennen keinen Anwendungs- und
  keinen Darstellungstyp.
- Mappe: Kennungen an den Prüfungshöhen fehlen in Abschnitt 2
  (2023MgrundlegendBStochastikWTR1-2d,
  2019MgrundlegendBStochastikWTR2-3a, 2026MerhoehtAStochastik21-a
  und -b).
- Bausteine: kein Baustein für den Binomialkoeffizienten, kein Baum
  mit drei Ästen je Knoten.
- Prüfskript: prüft die Pflichtformen P1–P8 nicht.
- Prüfskript: \leerfeld in antwort bleibt unbemängelt, obwohl
  bank.md dort das Gerüst „__“ zeigt.

## Offene Punkte

- bank/_punkte.csv: 6 ids mit original haben sich geändert (e3
  s9 → s10); punkte-nachziehen.py steht aus.
- Schrittnamen nur in neuen und umgeschriebenen Zeilen.
- gegenlese.md und gegenlese2.md beziehen sich auf den Stand vom
  27./28.09.; nicht kompiliert (kein LaTeX in der Sitzung).
