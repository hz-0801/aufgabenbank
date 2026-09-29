# Stand: lineare-gleichungen

Katalog-Commit: cebfd509ea71ae238b589537bd00b7fc306df06f
(2026-09-28, aus dem Kopf von mappen/lineare-gleichungen.md)
Datum: 2026-09-29 11:28 (date, UTC)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.8,
Vorlage auftrag-eintrag.md 2026-09-29b; Nachzug des Bestands vom
27./28.09. Endstand: 0 Abweichungen, 0 Warnungen in zone und e1–e4
(weg.jsonl: Dateiname, Bestand, nicht Teil des Auftrags).

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
- e2: 2020-OS-B1e, 2023-OS-B1e, 2024-OS-B1d (je 2, k3 s9).
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
- e2 neue Sprosse 5 „x steht hinter dem Minus" (Katalog neu),
  die folgenden Sprossen rücken um eins (Prüfungshöhe s9).
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
- Katalog: Kette Umformen führt keine Klammer, alle drei
  e2-Originale haben eine (Klammer als Block gelöst).
- Katalog: Die Vorstufe der Kette Umformen heißt „Blatt 0", steht
  aber als Vorstufe der Einheit; hier in e2 geführt.
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
