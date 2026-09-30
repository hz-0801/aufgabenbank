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
    e1.jsonl        40         4         5      15        4      12
    e2.jsonl        46         4         5      21        4      12
    e3.jsonl        57         4         5      30        6      12
    e4.jsonl        32         4         5       9        2      12
    e5.jsonl        38         4         5      15        2      12
    e6.jsonl        38         4         5      15        2      12
    e7.jsonl        41         4         5      18        2      12
    e8.jsonl        42         8         5      15        2      12
    gesamt         375        36        58     160       24      97
    (Stand nach dem Nachzug 30.09.b, unten)

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
  unter …?“ (Zeile 54, Bereich vor Einheit 6 und 8) hat in e6 die
  Vorstufe desselben Handgriffs (Zeile 160), in e8 nicht („Vorwärts
  oder rückwärts?“, Zeile 162); nach bank.md 30.09.b steht er
  einmal, in e8 als k1 (Nachzug 30.09.; bis dahin entfallen).
- Katalog: Die Typen-Zeilen 32–39 nennen keinen Anwendungs- und
  keinen Darstellungstyp.
- Mappe: Kennungen an den Prüfungshöhen fehlten in Abschnitt 2
  (2023MgrundlegendBStochastikWTR1-2d,
  2019MgrundlegendBStochastikWTR2-3a, 2026MerhoehtAStochastik21-a
  und -b) – seit der Mappe vom 30.09. (262 Originale) vorhanden,
  nachgezogen (unten).
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

## Nachbesserung 2026-09-30

- Teil 1, Antwortgerüst: 141 Zeilen (e1.jsonl 5, e2.jsonl 11, e3.jsonl 24, e4.jsonl 9, e5.jsonl 19, e6.jsonl 9, e7.jsonl 10, e8.jsonl 20, zone.jsonl 34) –
  im Feld antwort `\leerfeld[X]` → `__ X` und `\leerfeld` → `__`,
  weil bank.md (Feld antwort) das Gerüst „__“ vorschreibt; alle
  Zeilen dieser Dateien mit `\leerfeld` in antwort, ids über
  `git show` des Commits oder das Skript
  werkzeuge/einmalig/leerfeld-antwort-2026-09-30.py.
- Teil 2, zufallsexperimente-und-pfadregeln-e2-k1-s0-v4: Würfelpaar
  (4; 6)/(6; 4) statt (2; 5)/(5; 2) – das alte Paar stand wörtlich im
  Merkkasten; (4; 6) steht weder in der Mappe noch sonst in der Bank
  des Eintrags. Lösung „zwei Ergebnisse“ bleibt.

## Nachzug 2026-09-30b (Erkennungsschritte, Originale)

Datum: 2026-09-30 09:07 UTC (date). Grundlage: bank.md 30.09.b
(Erkennungsschritt einmal je Bereich; Sek-II-Deutungstypen tragen
darstellung und anwendung), Mappe vom 30.09. 08:15 UTC mit 262
Originalen (Abschnitt 2), Katalog unverändert (Commit 2a296e5, in
der Mappe; Auftrag nennt db8d2a3). Prüfskript vorher 0/0, nachher
0/0 (v0.12, --katalog); Formprobe unverändert 1 Hinweis (e5
darstellung eine Richtung – Bestand vom 29.09.).

    Datei  übernommen  neu  umgeschrieben  entfallen
    e1           37      0              2          1
    e2           43      0              2          1
    e8           38      4              0          0

- e1 s7: Die drei Zeilen ohne Original (Nachweis eines Schnitts aus
  Randanteil und „keiner der beiden Mängel“) verfremden
  2023MgrundlegendBStochastikWTR1-2d; zwei tragen jetzt das Original
  (v4, v5 → v3, v4, mit Schrittnamen), v3 (Fahrradcheck) entfällt
  (Menge 2 je Original). Zeilen mit Original: 4 statt 5.
- e2 s8: Die drei Zeilen ohne Original (Term in n als Anteil
  begründen) verfremden 2019MgrundlegendBStochastikWTR2-3a; v3, v4
  tragen es jetzt, v5 (Knöpfe) entfällt; sprosse_text der vier
  Zeilen auf das ganze Glied der Zeile 156 verlängert.
- e8: Erkennungsschritt „Anteil aller oder Anteil unter …?“ (Zeile
  54) als eigene Kette k1, vier Zeilen Sprosse 0, Ankreuzen wie in
  e6 s0, Situationstexte aus dem Rückwärtsstoff (Kundenkarte,
  Neukunden, Zufallsfrage, Pendler); Verfahrenskette „Rückwärts“
  jetzt k2, Pflichtkette k3 – ids aller 38 Bestandszeilen umbenannt.
- Pooldubletten an den Prüfungssprossen (2026-bb-ea-A1.10a =
  2026MerhoehtAStochastik21-a, 2025-bebb-lk-A1.9b =
  2025MerhoehtAStochastik22-b, 2023-bebb-lk-A1.8b =
  2023MerhoehtAStochastik22-b, 2026-bb-ea-A1.10b =
  2026MerhoehtAStochastik21-b; in der Mappe wortgleich) zählen als
  ein Original; die Bankzeilen behalten die abi-Kennung, keine
  weiteren Zeilen (bank.md, Pooldublette).
- Sek-II-Deutungstypen tragen darstellung und anwendung: die
  Pflichtzeilen bestehen bereits (Entscheidung 3); die Feststellung
  in den Befunden (Typen-Zeilen nennen keinen Anwendungs- und
  Darstellungstyp) ist damit erledigt, Zeilen unverändert.
- Zone, e3–e7 und muster.md unverändert (Sprossen und Fertigkeiten
  der Mappe unverändert; muster.md hält je Verfahrenskette einen
  Abschnitt, der Erkennungsschritt hat keinen Grundfall).
- bank/_punkte.csv nicht angefasst: neues Urteil brauchen e1-k1-s7-v3,
  e1-k1-s7-v4 (2023MgrundlegendBStochastikWTR1-2d), e2-k1-s8-v3,
  e2-k1-s8-v4 (2019MgrundlegendBStochastikWTR2-3a); umbenannt
  e8-k1-s7-v1, e8-k1-s7-v2 → e8-k2-s7-v1, e8-k2-s7-v2
  (2022MgrundlegendAStochastik2, Urteil bleibt);
  punkte-nachziehen.py steht aus.
