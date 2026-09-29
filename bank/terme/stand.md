# Stand: terme

Katalog-Commit: d78032a884b6073d9e4c92cc8407e909e3c4ea2a
(2026-09-29, aus dem Kopf von mappen/terme.md)
Datum: 2026-09-29 09:31 (date, UTC)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.7;
Nachzug des Bestands vom 27./28.09. (Commits „terme: e1" bis
„terme: e4", „terme: muster").

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      18         0         8       9        0       1
    e1.jsonl        39         0         5      21        4       9
    e2.jsonl        81        12        10      42        5      12
    e3.jsonl        36         4         5      15        3       9
    e4.jsonl        52         8         5      24        3      12

Pflicht je Einheit: e1 fehler, darstellung, anwendung · e2 fehler,
begruenden, darstellung, anwendung · e3 fehler, begruenden,
darstellung · e4 fehler, begruenden, darstellung, anwendung
(je 3) · Zone fehler 1 (Paar).

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         18      0              0          0
    e1           28      0             11          0
    e2           60      0             21          0
    e3           25      0             11          0
    e4           18     23             11          0

Umgeschrieben heißt auch: nur merkmal angeglichen (je Pflicht-
sprosse ein merkmal für drei Formen; 5 Zeilen in e1–e3).

## Originale je Einheit

- e1: 2023-OS-B1h, 2017-OS-B1i (je 2 Zeilen, k1 s7).
- e2: 2025-GYM-B2a (2 Zeilen, k4 s11).
- e3: keins; Prüfungshöhe als Zielmarke, original null.
- e4: keins; Prüfungshöhe als Zielmarke, original null.

## Prüfskript vor der Korrektur

- zone.jsonl: 0 Abweichungen, 0 Warnungen (unverändert).
- e1.jsonl: 0 / 0.
- e2.jsonl: 2 / 0 – „pruef fehlt" (P1-Serie) und „merkmal
  uneinheitlich" (Darstellung); je eine Zeile korrigiert.
- e3.jsonl: 1 / 0 – Nummer der Rechnung „(2)" stand an der
  Ergebnisstelle; Lösungssatz umformuliert.
- e4.jsonl: 1 / 0 – „pruef fehlt" (P2 fehlerfrei, Lösung mit
  Ziffer). Keine Einheit ist zweimal gescheitert.

## Entscheidungen

- Zone bleibt: Fertigkeiten (Zeilen 28–31) unverändert.
- Päckchen: fester Wert e1 „das Vierfache", e2 k4 „7x", e2 k5
  Faktor 5, e3 „5a + (2b − …)", e4 „5x"; es wandert die Zahl.
- P1-Serie in e1 am Termwert (Kennzeichen gerade/ungerade und
  Vorzeichen), weil e1 keine Umformungskette hat.
- Vorstufe s-1 (Zerlegen) mit Gerüst „4 · __ + 4 · __" in antwort;
  pruef als Liste der Lückenwerte.
- Neue Sprossen e4 s7 (Figur) und s8 (Rabatt) als Text ohne
  Grafik: zwei Rechtecke nebeneinander hat kein Baustein; das
  Bild beschreibt die Aufgabe in Worten.
- e4 Pflichtelemente neu (begruenden, darstellung, anwendung),
  weil die Typenzeile 24 sie jetzt trägt; quelle 24.
- Kastenzahl 12 (Zeile 43, 50) aus allen Aufgaben genommen:
  e1 k3 v1, e1 k4 s3 v1, e2 k4 s2 v3, e3 k3 s1 v1/v3 (umgeschrieben),
  e4 s1 v5, s3 v2, s9 v2, s10 v3, k2 v1.
- In P1-Serien stehen die Rechnungen als (1)…(4); die Lösung
  nennt sie „Rechnungen 2 und 3" (Prüfskript liest „(2)" sonst als
  Ergebnis).

## Befunde

- Gegenprobe „je Einheit genau eine Sprosse mit hoehe pruefung"
  passt nicht zu e2 mit zwei Verfahrensketten (je Kette eine
  Prüfungshöhe nach 2.4 c; Ist 2).
- Katalog: e1 trägt weiter keinen Typ Begründen, e3 keine
  Anwendung; die Pflichtmengen fehlen dort nach den Typen.
- Katalog, Erkennungsschritte: keiner wiederholt eine Vorstufe
  derselben Einheit; e4 hat keinen Erkennungsschritt.
- 2022-GYM-B2b (e3) bleibt unverfremdet: Kern ist die binomische
  Formel (binomische-formeln.md).
- Vorlage: kein Baustein für zwei Rechtecke mit gemeinsamer Seite
  (e4 s7, Typenzeile 24).
- Prüfskript: P1-Serien ohne Zahlenergebnis verlangen ein pruef,
  sobald die Lösung eine Ziffer trägt; die Nummern der Rechnungen
  zählen dann als Ergebnis.

## Offene Punkte

- Grundvorstellung (Zeile 70) steht weiter nicht in der Bank.
- Schrittnamen nur in neuen und umgeschriebenen Zeilen; der
  übernommene Bestand zeigt reine Ergebnisse.
- Termbaum (e1) und \viereck mit Termlabels nicht gerendert.
