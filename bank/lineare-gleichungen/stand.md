# Stand: lineare-gleichungen

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/lineare-gleichungen.md)
Datum: 2026-09-30 08:42 (date, UTC)
Grundlage: bank.md 2026-09-30b, werkzeuge/bank-pruef.py v0.9,
Vorlage auftrag-eintrag.md 2026-09-29e; Nachzug 30.09. nach den
Katalogänderungen vom 30.09. (Einheit 2, Kette Umformen), davor
Nachzug 29.09. (Katalog cebfd50) des Bestands vom 27./28.09.
Endstand: 0 Abweichungen, 0 Warnungen in zone und e1–e4
(weg.jsonl: Dateiname, Bestand, nicht Teil des Auftrags).

## Nachzug 30.09.

Nur e2, Kette Umformen (k3), Katalogzeile 78: Vorstufe s0 ohne
„Blatt 0“ im Text; neue Sprosse 8 „Klammer als Block“ mit den
P10-Formen 2020-OS-B1e und 2024-OS-B1d; Umkehrung rückt auf s9;
Prüfungshöhe s10 mit 2023-OS-B1e (Zahl außerhalb der Klammer).

    Datei  übernommen  neu  umgeschrieben  entfallen
    e2             44    0              5          1

Übernommen: 37 Zeilen unverändert, 4 Zeilen der Vorstufe s0 nur
sprosse_text, 3 Zeilen Umkehrung nur id und sprosse. Umgeschrieben:
die 3 Zeilen der neuen Sprosse 8 und die 2 Prüfungszeilen tragen
ihre alte Aufgabe wortgleich, aber hoehe (s8: pruefung → sprosse),
merkmal, sprosse_text, id neu. Entfallen: eine der zwei
2024-OS-B1d-Zeilen (3 · (x + 1,5) = 0), weil eine Sprosse drei
Zeilen hält (bank.md, Prüfskript-Warnung bei vier). Prüfskript vor
dem Nachzug: 10 Abweichungen in e2, alle „sprosse_text nicht
wortgleich in Zeile 78“ (s0 und s9); danach 0 / 0; Formprobe 0.
Zone, e1, e3, e4: keine Änderung des Katalogs, 0 / 0, unverändert.
Punkte: werkzeuge/punkte-nachziehen.py 7c950d2^ lineare-gleichungen
(ids umbenannt).

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      28         0        10      17        0       1
    e1.jsonl        48         4        10      18        7       9
    e2.jsonl        50        12         5      21        6       6
    e3.jsonl        40         8         5      18        3       6
    e4.jsonl        40         0         5      15        8      12

Pflicht je Einheit: e1 fehler, begruenden, darstellung · e2 fehler,
begruenden · e3 fehler, begruenden · e4 fehler, begruenden,
darstellung, anwendung (je 3) · Zone fehler 1 (Paar).

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         25     0              3          0
    e1           27     0             21          0
    e2           26     3             21          0
    e3           22     4             14          0
    e4           22     0             18          0

Übernommen heißt: nur id, sprosse, kette_nr, quelle nachgezogen
(die Katalogzeilen ab 34 sind um eins gerückt). Umgeschrieben
zählt auch Zeilen, bei denen nur merkmal oder sprosse_text
angeglichen wurde (Päckchen-Merkmal, Vorstufen-Text).

## Originale je Einheit

- e1: 2018-OS-B1c, 2022-OS-B1c (je 2, k2 s5).
- e2: 2023-OS-B1e (2, k3 s10, Prüfungshöhe); 2020-OS-B1e (2) und
  2024-OS-B1d (1) an der Sprosse k3 s8 „Klammer als Block“ (hoehe
  sprosse, Feld original gesetzt).
- e3: keins; Prüfungshöhe als Zielmarke, original null (k2 s7).
- e4: 2020-OS-K2e, 2018-OS-K3b, 2016-OS-B1b, 2021-OS-B1e
  (je 2, k1 s6). 2025-OS-B1h bei quadratische-gleichungen.

## Prüfskript vor der Korrektur

- Bestand vor dem Nachzug, mit Katalogprobe: 136 Abweichungen,
  alle „sprosse_text nicht wortgleich" (quelle um eine Zeile
  verrückt, zwei Vorstufentexte gekürzt).
- zone: 0 / 0. e1: 0 / 0. e3: 0 / 0. e4: 0 / 0.
- e2: 1 / 0 – Sperre: 3x + 4 + 2x aus „Typische Fehler" in der
  neuen Personenaussage; Zahlen getauscht.
- Keine Einheit ist zweimal gescheitert.

## Entscheidungen

- Zone bleibt (Fertigkeiten Zeilen 26–30 unverändert); drei
  Zeilen nur wegen der Kastenzahl 12 umgeschrieben.
- Päckchen: fester Wert e1 k2 „x + 8", e1 k3 „3x + 2", e2 k3
  „x + 9", e3 k2 „5x = 2x + …", e4 k1 „Eine Zahl plus … ergibt
  24"; es wandert die Zahl.
- Kastenzahlen 10, 11, 12, 13, 46, 54, 60 (Merkkasten aller
  Einheiten) aus allen Aufgaben genommen; Prüfkennungen „(P10
  Jahr Papier)" zählen nicht.
- e2 neue Sprosse 5 „x steht hinter dem Minus" (Katalog 28.09.)
  und Sprosse 8 „Klammer als Block“ (Katalog 30.09.); die
  folgenden Sprossen rücken (Umkehrung s9, Prüfungshöhe s10).
- e2 s8: die vier Klammer-Block-Zeilen der alten Prüfungshöhe
  (2020-OS-B1e, 2024-OS-B1d) werden nicht neu geschrieben, sondern
  auf die neue Sprosse gezogen; die Prüfungshöhe behält nur das
  Original, das die Katalogzeile ihr nennt (2023-OS-B1e), zwei
  Zeilen. Drei Zeilen je Sprosse gehen vor „zwei je Original“; die
  vierte Zeile entfällt.
- e2 s8 behält Prüfkennung „(P10 Jahr OS)“ und „mache die Probe“
  im Text, weil original gesetzt bleibt und die Aufgabe wortgleich
  übernommen ist.
- e3 neuer Erkennungsschritt „Was ist als Nächstes dran?" (Zeile
  35) als k1 mit Ankreuzform; die Verfahrenskette ist k2.
- P3 Prüfzahl in e2 (nur ein Glied geteilt) und e3
  (Minusklammer); P1 Serie in e1 (Probe weggelassen) und e4
  („vermindert um"); P2 fehlerfrei in allen vier Einheiten.
- e4 Anwendung: die Klassenfahrt-Zeile endet jetzt mit „Reicht
  das Geld?" (P8); Grenze 30 Personen, gefragt sind 31.
- Pflichtzeilen mit drei Formen tragen ein gemeinsames merkmal
  je Sprosse; die Form steht im Aufgabentext.

## Befunde

- Katalog: Erkennungsschritt „Umkehroperation benennen" (Zeile
  32) steht „vor Einheit 1 und 2"; nach bank.md nur in e1.
- Erledigt 30.09.: Kette Umformen führt jetzt „Klammer als
  Block“; die Vorstufe heißt nicht mehr „Blatt 0“.
- Katalog: Zielmarke (Zeile 84) nennt für Einheit 2 weiter alle
  drei Originale; die Kette (Zeile 78) legt zwei davon auf die
  Sprosse „Klammer als Block“ und eins auf die Prüfungshöhe. Die
  Bank folgt der Kette.
- bank.md R.1 (Erkennungsschritte, 30.09.b) geprüft: „Umkehr-
  operation benennen“ (e1, Frage nach der Gegenrechnung) und die
  Vorstufe „Umformung nur anschreiben“ (e2 k3 s0, Strich an einer
  Gleichung) sind verschiedene Vorlagen, also verschiedene
  Handgriffe; „Was steht bei x?“ und „Reihenfolge bestimmen“
  treffen andere Entscheidungen. Nichts entfällt.
- Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die
  Gegenprobe lief mit eigener Probe (0 Treffer).
- Kein Erkennungsschritt wiederholt eine Vorstufe derselben
  Einheit; keiner entfällt.

## Offene Punkte

- Grundvorstellung Waage (Zeile 74) steht weiter nicht in der
  Bank; kein Baustein für eine Waage.
- Schrittnamen nur in neuen und umgeschriebenen Zeilen; der
  übernommene Bestand zeigt reine Ergebnisse.
- gegenlese.md, gegenlese2.md und weg.jsonl sind Bestand.
