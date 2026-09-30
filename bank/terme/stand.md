# Stand: terme

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/terme.md)
Datum: 2026-09-30 08:46 (date, UTC)
Grundlage: bank.md 2026-09-30b, werkzeuge/bank-pruef.py v0.11;
Nachzug des Stands vom 29.09. (Katalog d78032a) nach den
Katalogänderungen vom 30.09. (Kopfzeile „Änderungen 2026-09-30“:
Einheit 1 Typen Fehler finden und Begründen; Einheit 3 Typ Sachterm
mit Klammer; Erkennungsschritt vor Einheit 4). Vorheriger Stand:
Commit eb3d65c.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      18         0         8       9        0       1
    e1.jsonl        42         0         5      21        4      12
    e2.jsonl        81        12        10      42        5      12
    e3.jsonl        42         4         5      18        3      12
    e4.jsonl        56        12         5      24        3      12

Pflicht je Einheit: e1–e4 fehler, begruenden, darstellung,
anwendung (je 3) · Zone fehler 1 (Paar).

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         18      0              0          0
    e1           36      3              3          0
    e2           81      0              0          0
    e3           36      6              0          0
    e4           52      4              0          0

Übernommen heißt: Aufgabe wortgleich, nachgezogen nur quelle, id,
sprosse oder kette_nr. Mechanischer Teil zuerst: quelle in 147
Zeilen um eins verschoben (werkzeuge/einmalig/
terme-quelle-2026-09-30.py, Commit 38c3559). Umgeschrieben in e1:
die drei fehler-Zeilen (vorher Punkt vor Strich am Termwert, jetzt
die Muster der Typzeile 21). Neue ids: e1 k4 s2 v1–v3 (begruenden),
e3 k2 s3 v1–v3 (Minusklammer mit Zahlen auf zwei Wegen), e3 k3 s4
v1–v3 (anwendung), e4 k1 s0 v1–v4 (Erkennungsschritt). Umbenannt
ohne Textänderung: e1 k4 s2→s3, s3→s4; e3 k2 s3–s7 → s4–s8; e4
alle Zeilen k1→k2, k2→k3. punkte-nachziehen.py: 0 umbenannt, 0
entfernt (keine umbenannte Zeile trägt ein Original).

## Originale je Einheit

- e1: 2023-OS-B1h, 2017-OS-B1i (je 2 Zeilen, k1 s7).
- e2: 2025-GYM-B2a (2 Zeilen, k4 s11).
- e3: keins; Prüfungshöhe als Zielmarke, original null.
- e4: keins; Prüfungshöhe als Zielmarke, original null.

## Prüfskript vor der Korrektur

- Vor dem Nachzug: 147 Abweichungen („sprosse_text nicht wortgleich
  in Zeile n“, e1 24, e2 57, e3 26, e4 40), 0 Warnungen, Formprobe
  0 Hinweise. Nach dem quelle-Skript 0 / 0.
- e1, e3, e4 nach dem Umbau je 0 Abweichungen, 0 Warnungen,
  Formprobe 0 Hinweise im ersten Lauf; keine Einheit ist
  gescheitert. Urteile am Ende: ja 12, nein 14, richtig 4.

## Entscheidungen

- e1 fehler: dritte Form ist P2m (vier Übersetzungen, genau eine
  falsch), weil Term aufstellen kein Kennzeichen für eine P1-Serie
  und keine Umformungskette für P3 hat; die alte P1-Serie am
  Termwert ist entfallen, weil die Typzeile jetzt die Muster nennt.
- e1 Pflichtkette in der Folge fehler, begruenden, darstellung,
  anwendung wie in e2–e4; darstellung und anwendung rücken daher
  auf s3 und s4.
- e3: der Typ „Sachterm mit Klammer auflösen“ trägt die drei
  anwendung-Zeilen (eine mit Entscheidung am Grenzwert, P8), keine
  eigenen Typzeilen ohne Kette.
- e3 k2 s3 (Minusklammer mit Zahlen auf zwei Wegen) mit form
  gleichungsraster wie die übrigen Klammersprossen; die Lösung
  nennt beide Wege als beschriftete Schritte.
- e4 Erkennungsschritt bleibt: seine Entscheidung (den gemeinsamen
  Faktor selbst finden) ist ein anderer Handgriff als die
  Vorstufen der Kette Ausklammern (Faktor vorgegeben); nach bank.md
  eigene Kette k1, Ausklammern wird k2, Pflicht k3.
- Erkennungsschritt: form teil, kein Bild; die Lösung nennt den
  eingekreisten Faktor in Worten.
- Päckchen und feste Werte wie am 29.09. (e1 „das Vierfache", e2 k4
  „7x", e2 k5 Faktor 5, e3 „5a + (2b − …)", e4 „5x").

## Befunde

- Die Sprosse „Minusklammer mit Zahlen auf zwei Wegen“ (Zeile 75)
  stand schon beim Katalogstand d78032a im Katalog, fehlte aber in
  der Bank; der Nachzug vom 29.09. hat sie übersehen. Jetzt als
  e3 k2 s3 nachgetragen. Das Prüfskript meldet eine fehlende
  Sprosse nicht, weil es die Kette nur lückenlos zählt, nicht gegen
  die Sprossenliste der Mappe.
- Katalog, Typzeile 21: „Begründen (warum das Doppelte von x plus
  zwei eine Klammer braucht)“ ist zweideutig – „das Doppelte von x
  plus zwei“ ohne Klammer heißt 2x + 2; gemeint ist das Doppelte
  der Summe. Die Bankzeilen sagen „Doppelte der Summe aus x und …“.
- Gegenprobe „je Einheit genau eine Sprosse mit hoehe pruefung"
  passt nicht zu e2 mit zwei Verfahrensketten (Ist 2) – wie 29.09.
- 2022-GYM-B2b (e3) bleibt unverfremdet: Kern ist die binomische
  Formel (binomische-formeln.md).
- Vorlage: kein Baustein für zwei Rechtecke mit gemeinsamer Seite
  (e4 s7, Typzeile 24).
- Prüfskript: P1-Serien ohne Zahlenergebnis verlangen ein pruef,
  sobald die Lösung eine Ziffer trägt; die Nummern der Rechnungen
  zählen dann als Ergebnis (wie 29.09.).

## Offene Punkte

- Grundvorstellung (Zeile 71) steht weiter nicht in der Bank.
- Schrittnamen nur in neuen und umgeschriebenen Zeilen; der
  übernommene Bestand zeigt reine Ergebnisse.
- Termbaum (e1) und \viereck mit Termlabels nicht gerendert.
- Urteile für die neuen und umgeschriebenen Zeilen (ids oben)
  stehen aus.
