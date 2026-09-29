# Stand: prozentrechnung

Katalog: hz-0801/mathe-nachhilfe, katalog/prozentrechnung.md,
Commit d78032a884b6073d9e4c92cc8407e909e3c4ea2a (Kopf der Mappe).
quelle = Zeilennummern dieses Stands.
Datum: 2026-09-29 13:41 CEST (date).
Prüfung: `python3 werkzeuge/bank-pruef.py prozentrechnung` (v0.8) –
257 Zeilen in e1–e5, 32 in der Zone, 0 Abweichungen, 0 Warnungen;
mit `--katalog` (Katalog aus Abschnitt 1 der Mappe) ebenfalls 0.

## Zahlen

    Datei       Zeilen  vorstufe  grundfall  sprosse  pruefung  pflicht
    zone.jsonl      32         0         12       19         0        1
    e1.jsonl        47         0          5       18        12       12
    e2.jsonl        60        12          5       21        10       12
    e3.jsonl        51         0          5       24        10       12
    e4.jsonl        47         8          5       18         4       12
    e5.jsonl        52         8          5       18        12        9
    gesamt         289        28         37      118        48       58

Nachzug je Einheit (übernommen / neu / umgeschrieben / entfallen):

    e1   39 / 0 /  8 / 0
    e2   42 / 3 / 15 / 0
    e3   36 / 3 / 12 / 0
    e4   26 / 6 / 15 / 0
    e5   43 / 0 /  9 / 0

„übernommen“ heißt: Aufgabe, Lösung und pruef wortgleich; nachgezogen
wurden id, sprosse, sprosse_text (wo der Katalog ihn geändert hat),
merkmal der Prüfungssprosse und quelle. Zone unverändert
(Fertigkeiten Z. 30–36 gleich).

Prüfskript vor der Korrektur (mit `--katalog`): e1 0, e2 0, e3 4
(3× sprosse_text nicht in Zeile quelle bei der neuen Sprosse s3,
1× Zwischenwert nicht an der Ergebnisstelle), e4 0, e5 1
(Zwischenwert nicht an der Ergebnisstelle). Keine Einheit scheiterte.

## Originale

- e1: 2020-OS-B1a, 2022-OS-B1f, 2023-OS-K6b, 2019-OS-K5b,
  2017-OS-K2b, 2021-OS-K5b
- e2: 2018-OS-K7a, 2023-OS-K6a, 2015-OS-K7c, 2014-OS-B1e,
  2025-OS-K6b
- e3: 2021-OS-B1c, 2017-OS-B1b, 2014-OS-B1a, 2026-FOR-B1a,
  2019-OS-K5a
- e4: 2025-OS-B1a, 2023-OS-B1b
- e5: 2026-FOR-K3c, 2022-OS-K4b, 2016-OS-K2c, 2024-OS-B1e,
  2015-OS-K2b, 2025-OS-K4b

## Entscheidungen

1. Prüfungshöhe: je Verfahrenskette eine Sprosse (die letzte), alle
   Originale der Katalogzeile darin, je 2 Zeilen; sprosse_text ist
   der Prüfungsabschnitt der Kettenzeile bis „→“ (auch „höhere
   Marke“ und „dazu …“), quelle die Kettenzeile.
2. Päckchen: e1 zehn Teile fest, Füllung wandert; e2 100 Kinder
   fest, Teil wandert; e3 25 % fest, Ganzes wandert; e4 24 kg
   fest, Satz wandert (auch 5 %); e5 70 € fest, Satz wandert.
3. e3: Die Kette stellt jetzt Zehn-Prozent-Schritte vor den
   Ein-Prozent-Weg; die Bestandszeilen folgen dieser Reihenfolge.
4. e2 s4 (Taschenrechner mit Überschlag): die drei Bestandszeilen
   umgeschrieben, Überschlag als eigene beschriftete Zeile vor der
   Rechnung, antwort mit zwei Feldern.
5. e4 Vorstufe: nach der neuen Katalogzeile ohne Zahl zum Ganzen;
   gefragt ist die Zahl der Abschnitte bis 100 % (pruef 100/p).
6. e5 Grundfall: Streifen nach dem neuen sprosse_text; die übrigen
   Sprossen tragen den längeren sprosse_text mit Streifen, Aufgaben
   bleiben ohne Streifen (übernommen).
7. Kastenzahlen: neue und umgeschriebene Aufgaben tragen keine
   mehrstellige Kastenzahl außer 100, 10, 20 (Prozent-Grundbegriff
   und glatte Sätze des Katalogs); der übernommene Bestand bleibt.

## Befunde

1. Gegenprobe „Kastenzahlen in keiner aufgabe“: Der Kasten nennt
   fast alle glatten Sätze (10, 20, 30, 35, 40, 45, 60, 75, 80);
   im übernommenen Bestand tragen 95 von 188 Aufgaben eine davon,
   56 außerhalb einer Prozentangabe. Die Sperrprobe meldet 0, weil
   sie Terme und Paare sperrt, keine Einzelzahlen.
2. Katalog: Kein Erkennungsschritt wiederholt eine Vorstufe
   derselben Einheit; „um oder auf?“ (Z. 41) ist wie bisher die
   Vorstufe von e5 und steht nicht doppelt.
3. Katalog: e5 hat keinen Typ Darstellung; pflicht darstellung
   fehlt dort (9 Pflichtzeilen).
4. Prüfskript: `--katalog` erwartet eine Datei; die Sitzung liest
   den Katalog nicht, er wurde aus Abschnitt 1 der Mappe
   nachgebaut (Kürzungen dort betreffen die Kettenzeilen nicht).

## Offene Punkte

- Übernommene Lösungen tragen keine Schrittnamen (Auftrag).
- Kein LaTeX kompiliert; `\bruchrechteck[5]{11}{20}` (e1 darstellung,
  rückwärts) und die neuen Streifen sind nur über das Prüfskript
  geprüft.
- Steigung in Prozent berechnen hat weiter kein eigenes Original.
