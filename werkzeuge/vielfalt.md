# vielfalt.py – Vielfalt der P10-Bankaufgaben (v0.1, 06.10.2026)

Misst ohne Modell, wie verschieden die Bankaufgaben sind, die die
P10-Prüfungshefte nutzen, und legt reine Kopien still (Auftrag B 06.10.;
Regel `bau/pruefheft/beschluesse-2026-10-06b.md` N1 Punkt 3, Zählregel in
bank.md „Mengen je Kette“).

## Aufruf (Wurzel von aufgabenbank)

    python3 werkzeuge/vielfalt.py                 Bericht bau/vielfalt-p10-<datum>.md
    python3 werkzeuge/vielfalt.py --stilllegen    dazu Feld "ruht" in die Bank
    --mn ../mathe-nachhilfe   --aus DATEI   --datum JJJJ-MM-TT

Der Lauf ohne `--stilllegen` schreibt nur den Bericht. `--stilllegen` ist
wiederholbar (schreibt nur Zeilen, deren Wert sich ändert).

## Grundlage

Sprossen: Spalte bank_sprossen der zehn `msa/zuordnung-*.csv`; „(i)“ und
„[…]“ (Teilauswahl nach Original oder Variante) werden abgeschnitten, die
Sprosse zählt ganz. `msa/prozent-zusatz.jsonl(5)` ist keine Bank-Sprosse.
Aufgaben: alle Zeilen `bank/<eintrag>/e<n>.jsonl` dieser Sprossen (nicht
`weg.jsonl`, nicht `zone.jsonl`).

## Merkmale je Aufgabe (geschätzt)

- sache: erstes Hauptnomen des Aufgabentexts, das kein Operator, kein
  Mathe-Wort, keine Einheit und kein Vorname ist (Liste STOP/NAMEN im
  Skript); „–“ = innermathematisch.
- darst: graph (ksys mit Gerade/Parabel/Funktion), diagramm (Säulen,
  Kreis, Baum, Streifen …), tabelle (form tabelle, Wertetabelle,
  Sachtabelle), bild (jede andere Grafik außer Rechenplatz), sonst text.
- richtung: pruefen (Prüfe, stimmt, recht, Fehler, Reicht, pflicht fehler
  oder begruenden), vergleichen (Vergleiche, günstiger …), rueckwaerts
  (merkmal „rückwärts“/„Umkehr“, „vorher“, „so, dass“, „Wie groß muss“),
  darstellen (form zeichnen, Zeichne, Trage, Stelle … auf/dar, pflicht
  darstellung), sonst vorwaerts.
- zahlart: kopf | glatt | krumm wie `zahlklasse()` in pruefheft.py
  (nachgebaut; Ergebnis aus der ganzen loesung statt dem Kurzergebnis).
- schablone: Klartext von aufgabe und antwort, dazu die grafik, alle
  Zahlen durch #, Prüfkennung „(P10 …)“ entfernt, klein geschrieben.

## Stilllegen

Gleiche Schablone in derselben Sprosse = Kopie. Je Gruppe bleibt aktiv:
zuerst eine Zeile mit original, dann die, deren Zahlart zur hoehe passt
(Vorstufe/Grundfall kopf, Sprosse/Pflicht glatt, Prüfung krumm), dann die
kleinste Variante. Die übrigen bekommen `"ruht": "kopie von <id>"` als
letztes Feld; nichts wird gelöscht.

Nicht stillgelegt (Entscheidung 06.10.), im Bericht als „gleich“ gezählt:
innermathematische Aufgaben und Sprossen mit „(i)“ – die Zählregel sagt,
innermathematisch genügen andere Zahlen; hoehe grundfall – das Päckchen
verlangt denselben Kontext mit einem wandernden Wert.

Das Feld `ruht` gab es vorher nicht (grep bank.md, pruefheft.py,
zusammenbau.py). bank-pruef.py kennt es seit 06.10. als Wahlfeld.
pruefheft.py und zusammenbau.py beachten es noch nicht.

## Schwache Sprossen

Nach dem Stilllegen weniger als 3 aktive Aufgaben, nur eine Sache oder
nur eine Darstellung. Arbeitsliste fürs Auffüllen aus Fremdprüfungen und
fürs Herauslösen (N1 Punkte 2 und 4).
