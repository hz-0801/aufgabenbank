# Stand: terme

Katalog-Commit: 9e85c1e2b866d0abebae25b6c6de90ea47a1a5b6
(2026-10-01, aus dem Kopf von mappen/terme.md)
Datum: 2026-10-01 (date, UTC)
Grundlage: bank.md 2026-09-30b, werkzeuge/bank-pruef.py v0.12;
Nachzug von vier auf sechs Einheiten (Katalog-Commits 84abe58 und
9e85c1e), Zuordnung nach katalog/_terme-zuordnung-2026-10-01.md
(mathe-nachhilfe), maßgeblich der Katalog. Dazu die Übernahme von
eingang/terme-2026-10-01/neu.jsonl. Vorheriger Stand: Commit
5e8baab (Katalog bbcf2d4, vier Einheiten, 239 Zeilen).

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      22         0         8      13        0       1
    e1.jsonl        77         8         5      53        2       9
    e2.jsonl        38         0         5      27        3       3
    e3.jsonl        77         4        15      45        4       9
    e4.jsonl        73        12         5      38        3      15
    e5.jsonl        20         0         5      15        0       0
    e6.jsonl        47         0         5      29        4       9
    gesamt         354

Einheiten: 1 Zusammenfassen, 2 Malnehmen, 3 Klammern auflösen,
4 Ausklammern, 5 Termwerte, 6 Aufstellen. Ketten: e1 k1 Gleichartige
Glieder erkennen, k2 Vorzahl lesen, k3 Vorzeichen als Teil des
Gliedes, k4 Zusammenfassen, k5 Pflicht · e2 k1 Malnehmen, k2 Pflicht
· e3 k1 Zeichen vor der Klammer feststellen, k2 Plus- und
Minusklammer, k3 Zahl mal Klammer, k4 Auflösen und zusammenfassen,
k5 Pflicht · e4 k1 Was steckt in jedem Glied?, k2 Ausklammern, k3
Pflicht · e5 k1 Termwert · e6 k1 Term aufstellen, k2 Situation zu
Term angeben (Typ ohne Kette), k3 Pflicht.

Pflicht je Einheit: e1 fehler, begruenden, darstellung · e2 fehler
· e3 fehler, begruenden, darstellung · e4 fehler (6), begruenden,
darstellung, anwendung · e5 keine · e6 fehler, begruenden,
darstellung · Zone fehler 1 (Paar). Die Sachaufgaben stehen als
Sprosse „Abschluss (Anwendung)“ in der Kette (Katalog Zeile 30).

## Nachzug je Einheit

    Datei  übernommen  Eingang  neu  umgeschrieben  entfallen  (alt)
    zone         18        4     0              0          0  zone
    e1           58        4    15              0          0  e2
    e2           23        1    14              0          0  e2
    e3           42       12    23              0          0  e3
    e4           56        3    14              0          0  e4
    e5            3        5    12              0          0  e1
    e6           38        2     6              1          0  e1

Gegenprobe: alt 239 = übernommen 238 + umgeschrieben 1 + entfallen
0; neu 354 = 239 + Eingang 31 + neu 84. Alle 81 Sprossen der
Katalogzeilen 103–111 (68 davon mit „(Stufe)“) haben Zeilen; keine
Lücke.

Übernommen heißt: aufgabe und loesung wortgleich; nachgezogen id,
einheit, kette, kette_nr, sprosse, sprosse_text, quelle, variante,
bei 23 Zeilen auch hoehe und merkmal (Erkennungszeilen vorstufe →
sprosse; anwendung → Sprosse Abschluss; neue Grundfälle; „Faktor
nur aus einem Glied“ sprosse → pflicht fehler). Umgeschrieben: e6
k3 s2 v1 (alt e1 k4 s2 v1), Zahl 5 → 9, weil der neue Merkkasten
Einheit 6 den Term 2 · (x + 5) sperrt.

Eingang (31 übernommen, Nr. in neu.jsonl → id): 1–4 → zone f1–f4
v5; 5 → e1 k4 s9 v1; 6 → e1 k4 s12 v1; 8, 27 → e1 k4 s5 v4, v5;
7 → e2 k1 s7 v1; 9 → e3 k2 s5 v1; 10 → e3 k2 s6 v1; 11 → e3 k3 s3
v1; 12 → e3 k3 s4 v1; 13, 14 → e3 k3 s5 v1, v2; 18 → e3 k4 s1 v4;
15 → e3 k4 s2 v1; 16 → e3 k4 s3 v1; 17, 31 → e3 k4 s5 v1, v2;
26 → e3 k4 s8 v4; 20, 29 → e4 k2 s3 v4, v5; 19 → e4 k2 s8 v1;
21, 28 → e5 k1 s3 v1, v2; 22 → e5 k1 s4 v1; 23 → e5 k1 s5 v1;
24 → e5 k1 s6 v1; 25 → e6 k1 s6 v4; 30 → e6 k1 s7 v4. Herkunft
jeweils Blatt terme 2026-10-01, Nummer wie im Protokoll.
Nicht übernommen: Nr. 32 (Dublette, siehe Entscheidungen).

punkte-nachziehen.py 5e8baab terme: 6 umbenannt, 0 entfernt; keine
neue Zeile mit original, kein neues Urteil nötig.

## Originale je Einheit

- e1: 2025-GYM-B2a (2 Zeilen, k4 s15).
- e6: 2023-OS-B1h, 2017-OS-B1i (je 2 Zeilen, k1 s10).
- e2, e3, e4: keins; Prüfungshöhe als Zielmarke, original null.
- e5: keine Prüfungshöhe (Katalog: Prüfungshöhe in e1).

## Prüfskript vor der Korrektur

- zone, e1–e5: 0 Abweichungen; e6: 1 (Sperre 2·(x+5), Merkkasten
  Zeile 85, in der übernommenen begruenden-Zeile).
- Warnungen (bleiben): e1 1 (k4 s5 5 Zeilen), e3 1 (k4 s8
  Prüfungshöhe ohne Original 4 Zeilen), e4 2 (k2 s3 5 Zeilen;
  pflicht fehler 6×), e6 2 (k1 s6 und s7 je 4 Zeilen); Formprobe 1
  Hinweis (e4 fehler: Form F doppelt).
- Nach der Korrektur: 0 Abweichungen, 6 Warnungen. Urteile: ja 12,
  nein 15, richtig 5. Keine Einheit ist gescheitert.

## Entscheidungen

- Prüfungssprosse als letzte Sprosse (bank.md, Prüfskript), auch
  wo der Katalog GYM- und Abschlusssprossen dahinter stellt: e2 k1
  s11, e3 k4 s8, e4 k2 s14, e6 k1 s10; die Sprossen dahinter
  rücken um eins vor (Nummern weichen von der Zuordnungstabelle ab).
- Gleichartige Glieder erkennen: Kette mit vier Sprossen s1–s4,
  hoehe sprosse, je 3 Zeilen, ohne Grundfall (Erkennungsschritt,
  keine Verfahrenskette); Vorzahl lesen und Vorzeichen bleiben
  Erkennungsschritte s0 in e1, Zeichen vor der Klammer in e3.
- Abschluss (Anwendung): die alten anwendung-Zeilen von e1, e3, e6
  sind jetzt Sprosse der Kette (hoehe sprosse); e4 behält seine
  anwendung-Zeilen, die Kette hat ihre Sachaufgabe in s10.
- darstellung-Zeilen ohne eigene Sprosse bleiben pflicht
  darstellung (e1 Umfangsterm, e3 Flächenbild und Tabelle mit
  quelle 107, e6 Termbaum mit quelle 6), nicht Typ ohne Kette.
- e4: „Faktor nur aus einem Glied“ (alte Sprosse s9, im Katalog
  jetzt Zuruf-Typ) als zweite fehler-Sprosse; nichts gelöscht.
- Eingangszeilen an voller Sprosse bleiben (Menge über 3/5).
- Herkunft der Eingangszeilen nicht im Feld quelle (bank-pruef.py
  verlangt eine ganze Zahl), sondern hier und im Protokoll.
- Dublette: Variablennamen zählen wie Zahlen; Nr. 32 ist bis auf
  Zahlen und Namen gleich mit e1 k4 s15 v1 und entfällt.
- Eingang Nr. 23 in Bruchform (Sprosse verlangt Bruch), Nr. 30 mit
  Frage (Sprosse Abschluss verlangt eine).
- Zone: die vier „obersten Aufgaben“ (Muster 4) waren Lücken und
  stehen als Fallstrick s4; das Paar in f1 rückt auf v6, v7.

## Befunde

- Katalog: Prüfungshöhe mitten in vier Ketten widerspricht bank.md
  („Prüfungssprosse die letzte“); Zusammenbau zeigt sie daher nach
  den GYM-Sprossen. Entscheidung im Chat nötig.
- Zuordnungstabelle zählt Erkennungsschritte nicht als Ketten; die
  Bank zählt sie (bank.md), daher e1 Zusammenfassen k4 statt K2,
  e3 k2–k4 statt K1–K3, e4 Ausklammern k2 statt K1.
- bank.md kennt kein Feld für die Herkunft einer Eingangszeile.
- Auftrag: „81 Sprossen mit (Stufe)“; es sind 81 Sprossen, 68 mit
  der Marke.

## Offene Punkte

- Päckchen fehlt in übernommenen Grundfällen e3 k3 s1 und e3 k4 s1
  (kein fester Wert); e5 k1 s1 ist Päckchen (4x − 3 bleibt).
- e5 hat keine Pflichtelemente; der Katalog nennt für Einheit 5
  keine Zuruf-Typen.
- Gegenlese der 84 neuen und 31 übernommenen Eingangszeilen.
