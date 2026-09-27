# Stand – quadratische-funktionen

Katalog: hz-0801/mathe-nachhilfe, katalog/quadratische-funktionen.md,
Commit c8c16ef37505be2d5dce5f89e49557f807d88786
(2026-09-26 14:19 +0200, „katalog: Merkkasten Nullstellengleichung
0 = f(x)"). Ermittelt mit `git log -1 -- katalog/…` im Klon, weil die
GitHub-API für das Repo in dieser Sitzung gesperrt ist; die Raw-Datei
ist byte-gleich mit dem Stand dieses Commits. Zeilennummern in quelle
beziehen sich auf diesen Stand.

Datum: 2026-09-26 20:05 UTC (`date`).

Prüfung: `python3 werkzeuge/bank-pruef.py quadratische-funktionen
--katalog <Eintrag>` – 257 Zeilen, 0 Abweichungen (Skript aus der
Sitzung prozentrechnung, Stand main nach Commit 331e79e).

## Zeilen

    Datei  Zeilen  vorst.  grundf.  spr.  pruef.  pflicht  grafik
    zone       46       –       16    30       –        –       8
    e1         49       4        5    24       4       12      19
    e2         60       4        5    33       6       12      19
    e3         42       4        5    21       6        6      12
    e4         60       4        5    33       6       12       6
    gesamt    257      16       36   141      22       42      64

Pflichtelemente (je 3): e1, e2, e4 fehler, begruenden, darstellung,
anwendung; e3 fehler, begruenden (siehe Entscheidung 9).

Originale (je 2 Zeilen): e1 2026-FOR-B1e, 2015-OS-K4b · e2
2017-OS-K5e, 2020-OS-K3d, 2018-OS-K5d · e3 2025-OS-K5b, 2018-OS-K5c,
2017-OS-K5d · e4 2022-OS-K3c, 2025-OS-K5c, 2023-OS-K4c.

## Prüfverlauf

Abweichungen des Prüfskripts vor der Korrektur: zone 0, e1 0, e2 0,
e3 0, e4 0. Treffer des eigenen Sperrskripts vor der Korrektur:
zone 1, e1 0, e2 1, e3 1, e4 6 echte und 1 Fehlalarm (Muster schnitt
längere Zahl an, Skript geschärft). Nichts ist zweimal gescheitert.

## Gegenprobe

- Vier Einheiten, vier Sprossenketten (Kette 1 je Datei); Kette 2
  sind die Pflichtelemente.
- e4: fünf Zeilen hoehe grundfall mit sprosse_text „Nullstellen aus
  der Scheitelpunktform durch Wurzelziehen, ganzzahlig (4×)".
- Kastenzahlen: grep auf „(x - 3)^2 + 1" und „(x + 3)^2 - 1" über
  alle jsonl: 0 Treffer. Sperrskript mit 77 Mustern (Merkkasten 1–4,
  Terme und Zahlenpaare der Originale laut CSV, Beispiele aus
  „Typische Fehler", Erkennungsschritten und Fertigkeiten) über jedes
  Feld aufgabe: 0 Treffer.
- form zeichnen: 16 Zeilen, alle mit grafik. Ablesegrafiken: jede
  Zeile, deren aufgabe einen Graphen zum Ablesen meint, hat grafik;
  die übrigen Zeilen mit dem Wort „Graph" sind Begründungen ohne
  Ablesen.

## Entscheidungen

1. Pflichtelemente als eigene letzte Kette (kette_nr 2, sprosse 1–4
   in der Folge fehler, begruenden, darstellung, anwendung), wie in
   prozentrechnung; kette = Name der Lerneinheit.
2. Prüfungshöhe: jedes Original eine eigene Sprosse, sprosse_text =
   Teil der Prüfungshöhe bis zum Semikolon. Ausnahme e3 s9: der
   Katalog nennt 2025-OS-K5b und 2018-OS-K5c in einem Schritt, also
   eine Sprosse mit vier Zeilen (zwei je Original).
3. papier nach der CSV: OS bis 2025, FOR 2026; Aufgabenende
   „(P10 2017 OS)". Das Beispiel in bank.md weicht ab (Befunde).
4. Namen: Parabel f (A9, nicht P10-p(x)), Gerade g, zweite Parabel
   g in e2/e3, h in e4 (dort ist g die Gerade); Sachkontext h für
   die Höhe. Scheitelpunktform in P10-Schreibweise (x − d)² + e.
5. Sperre bei Objektthemen: f(x) = x² ist Gegenstand der Kette
   („Wertetabelle zu x²") und bleibt frei; S(0|0) steht nur in
   Lösungen. Gesperrt bleiben 2x² (Kasten 1), −x² (Kasten 1,
   2014-OS-K7) und 3x² (2026-FOR-B1e) als Funktionen.
6. e1 s8 „verdoppelt oder halbiert": 2x² ist gesperrt, deshalb die
   Faktoren 0,5; 0,25 und 4.
7. Zone: Reihenfolge nach erster Verwendung, für Einheit 4 nach
   Lehrplanfolge (lineare Gleichung, Schnittpunkt zweier Geraden,
   Wurzel, quadratische Gleichung). Je Fertigkeit s1 zwei, s2 eine,
   ab s3 je Fallstrick eine Zeile. Das Paar „Fehler finden und
   gleichartige Aufgabe" (unterrichtsblatt 2.2) steht bei der
   binomischen Formel als zwei Fallstrick-Sprossen.
8. e2 darstellung ist der einzige kettenlose Typ des Eintrags,
   „Aussagen zur Parabel als wahr/falsch beurteilen", mit Graph
   (Gleichung gegen Graph). Vorrat (H: quadratische Ergänzung,
   allgemeine Form) nicht aufgenommen.
9. e3 ohne darstellung und anwendung: die Kette trägt beide
   Richtungen (Scheitelpunktform → Normalform s3–s5, s10; Normalform
   und Graph → Scheitelpunktform s6, s7, s9), kein Typ der Einheit
   hat einen Sachkontext.
10. e4 darstellung aus dem Nebenbestand (Zeile 109, „der
    zeichnerische Zugang zu Einheit 4", 2023-OS-K4a): Schnittpunkte
    ablesen und durch Einsetzen bestätigen.
11. anwendung: sprosse_text „Modellieren mit Wurfparabel und
    Bauwerk" (Zeile 98); Sachaufgaben mit Orten in einer Figur
    tragen eine Skizze (unterrichtsblatt 3.5).
12. Sprossen ohne veränderbare Zahlen (e1 s3 Eigenschaften der
    Normalparabel, e2 s10 offene Aufgabe): die Varianten fragen
    verschiedene Eigenschaften. e2 s7 nennt drei Unterschritte
    (oben/unten, rechts/links, beides) – je einer pro Variante.
13. Grafik: Ablesegrafik mit `ablesen` (Karo 6 mm), Zeichenfläche
    ohne Schlüssel (8 mm), ystep=2, wo die Fläche sonst über 16 cm
    hoch würde; der Ursprung liegt immer im Bereich. Parabeln als
    `\parabel` (auch zu Normalformen, Scheitel umgerechnet), Geraden
    als `\gerade`, Sachkontexte als `\funktionab` auf dem
    sinnvollen Bereich.
14. Wertetabellen stehen als `\wertetabelle` in aufgabe, nicht in
    grafik; grafik trägt nur ksys.
15. Negative Zahlen in loesung ohne Leerzeichen nach dem Minus
    („$-4$", „$S(1|{-4})$"), damit das Prüfskript sie als negativ
    liest; pruef nennt die Zahlen, wie sie in loesung stehen.
16. Zwei Ablesegrafiken mit gleicher Grafik-Art haben verschiedene
    Formulierungen, weil das Skript nur aufgabe auf Doppel prüft.

## Befunde zu bank.md

- (erledigt v0.5) Kein Feld für die Lösungsgrafik. Zeichenaufgaben
  (Parabel skizzieren, Spiegelbild) haben die Lösung nur als Punktliste;
  unterrichtsblatt 3.5 will für Parabeln eine Lösungsgrafik. Vorschlag:
  Feld grafik_loesung mit dem Bausteinaufruf (ksys[klein] mit \parabel).
- form kennt kein „ablesen"; Ablesegrafiken laufen als teil oder
  ankreuzen mit grafik. Auswählen lassen sie sich nur über
  grafik ≠ "".
- (erledigt v0.5) Wo die Pflichtelemente stehen (Kette, Sprosse), regelt
  bank.md nicht; beide Sitzungen haben eine eigene letzte Kette gewählt.
- Prüfungshöhe mit zwei Originalen in einem Katalogschritt: eine
  oder zwei Sprossen? Nicht geregelt.
- (erledigt v0.5) Zone: sprosse_text = Fertigkeit und hoehe
  grundfall/sprosse für leicht, mittel, Fallstrick sind Konvention des
  Skripts, nicht bank.md.
- (erledigt v0.5) Das Beispiel „2018-OS-K7a … papier FOR" widerspricht
  der CSV (papier OS für alle OS-Kennungen).
- (erledigt v0.5) Sperre: bei Objektthemen ist die Grundfunktion (x²)
  selbst Kastenfunktion; eine Ausnahme für den Gegenstand der Kette
  fehlt.
- (erledigt v0.5) pruef "" erlaubt bank.md nur bei Begründen und
  Zeichnen; das Skript erlaubt es auch bei Lösungen ohne Ziffer
  (Ankreuzen „Gerade"/„Parabel") – bank.md nachziehen.

## Befunde zum Prüfskript (Grafikaufgaben)

- (erledigt v0.5) grafik wird nicht geprüft: weder Makroname und
  Argumentzahl noch Achsenbereich. Ein \parabel mit drei Argumenten oder
  ein Scheitel außerhalb der Fläche ginge durch. Hier mit eigenem Skript
  geprüft (Name, Argumentzahl, Ursprung im Bereich, Fläche höchstens 16
  cm, jeder gefragte Punkt im Bereich).
- (erledigt v0.5) Die Regel „form zeichnen ⇒ grafik nicht leer" fehlt.
- Ob die Grafik zu den Aufgabenwerten passt (\parabel{1}{2}{-3} zu
  f(x) = x² − 4x + 1), prüft das Skript nicht. Vorschlag: \parabel,
  \gerade, \punkt aus grafik lesen und die Punkte der Lösung darin
  auswerten.
- (erledigt v0.5) Doppelprüfung nur über aufgabe: Ablesegrafiken mit
  gleichem Text und anderer Grafik gelten als doppelt. Vorschlag:
  aufgabe und grafik zusammen vergleichen.
- (erledigt v0.5) Zahlenfang: „- 4" mit Leerzeichen wird als +4 gelesen;
  bei Termen (x² − 6x) richtig, bei Ergebnissen eine Falle (Entscheidung
  15). „x^2" liefert eine 2, „x_1" eine 1 – harmlos, weil nur pruef ⊂
  loesung geprüft wird.
- (erledigt v0.5) Keine Sperrprüfung (Kasten- und Originalterme in
  aufgabe); hier eigenes Skript mit Musterliste.
- --katalog prüft sprosse_text als Teilstring der Zeile quelle;
  bei Pflichtelementen geht damit jeder Teilstring durch.

## Offene Punkte

- Nicht kompiliert. Bausteine gegen Anleitung_mathblatt.md und
  mathblatt.sty 2026-09-28a geprüft (\parabel 4, \gerade [o]3,
  \punkt 3, \funktion [o]2, \funktionab [o]4 Argumente);
  \wertetabelle mit „0{,}5" im optionalen Argument ist nicht
  erprobt.
- e1 s8: „verdoppelt" ist nicht belegt (2x² gesperrt) – im Chat
  entscheiden, ob die Kastenfunktion als Gegenstand frei ist.
- e3: keine darstellung, keine anwendung (Entscheidung 9).
- e4 fehler: drei Varianten für vier Muster; „y-Werte vergessen"
  steckt nur im Merkmal von s9, nicht als Fehler finden.
- Generator und Sperrskript dieser Sitzung liegen nicht im Repo
  (Auftrag: nur unter bank/quadratische-funktionen/ schreiben);
  bei Bedarf nach werkzeuge/ übernehmen.

## Nachbesserung 2026-09-27

- Prüfskript v0.5 vorher 33 Abweichungen, 6 Warnungen, nachher
  0/0.
- Alle 257 Zeilen tragen das Feld loesungsgrafik, überall "";
  die Parabel-Zeichenaufgaben haben ihre Lösung weiter als
  Punktliste.
- Zone-Paar: zone-f4-v5 (Fehler finden, Mittelglied vergessen)
  trägt jetzt hoehe pflicht, pflicht fehler; f4-v6 bleibt die
  gleichartige Rechenaufgabe (Entscheidung 7).
- pruef an der Ergebnisstelle: Bei Termlösungen nennt pruef das
  Mittelglied mit Vorzeichen (zone-f4-v1 bis v4, v6), bei
  Nachweis, Fehler finden und Gleichung-Aufstellen die erste Zahl
  der Lösung (zone-f4-v5, e2-k1-s5, e3-k1-s5, e3-k1-s10,
  e3-k2-s1-v1, e4-k1-s0), bei der Brücke $-8$ (e1-k2-s4-v1); die
  Lösungen bleiben wortgleich.
- e3-k1-s3 und s4: die Lösung beginnt mit der Normalform, die
  Rechnung folgt nach „denn"; pruef ist das Mittelglied.
- e2-k1-s11-v1 und v2: das Ergebnis (Verschiebung um 6, zwei
  gemeinsame Punkte) steht am Satzanfang, pruef wie vorher;
  v3 pruef 2.
- e3-k1-s8-v2: pruef ohne die 5 aus der Aufgabe; zone-f2-v2
  (Punkt eintragen, form zeichnen) und zone-f8-v6: pruef "" bzw.
  $-2$.
- e4-k1-s7-v3: Sperre x² + 4x (Typische Fehler, Zeile 91);
  Aufgabe jetzt $f(x) = x^2 + 5x$ und $g(x) = -x - 5$, Lösungen
  $-1$ und $-5$.
- Prüfungshöhen: alle zehn Prüfungssprossen tragen ein Original;
  keine Zeile geändert (Befund N1).
- Erkennungsschritte: keiner steht im Eintrag, also keiner
  gestrichen; vier der sechs verdoppeln die Vorstufe ihrer Einheit
  und entfallen ohnehin (Befund N2).

## Befunde der Nachbesserung

- N1 Katalog/bank.md: e1 s8, e2 s12 und e4 s12 tragen im Katalog
  „(ohne Original; Zielmarke nach RLP und LISUM-PH …)", stehen aber
  vor der „Prüfungshöhe:" mit Originalen (e1 s8 sogar vor s9).
  bank.md gibt der Prüfungshöhe ohne Original hoehe pruefung, behält
  pruefung aber der letzten Sprosse vor; hier als hoehe sprosse
  belassen.
- N2 Katalog: „Gerade oder Parabel?", „Wo steht der Scheitel?",
  „Welche Form ist das?" und „Was wird gleichgesetzt?" (Zeilen
  38, 41, 42, 43) verlangen denselben Handgriff wie die Vorstufe
  von e1, e2, e3, e4; der Katalog führt beide.
- N3 Lücke: „Minus und Quadrat" (Zeile 39) und „Nach oben oder
  nach unten?" (Zeile 40) haben keine Zeilen; nach bank.md stünden
  sie als eigene Ketten mit je 4 Zeilen in e1 (kette_nr der
  folgenden Ketten rückten auf). Nicht nachgetragen, weil der
  Auftrag nur Nachbesserung war.
- N4 bank.md: e2 darstellung „Aussagen zur Parabel als
  wahr/falsch beurteilen" ist ein Typ ohne Kette (Entscheidung 8),
  steht aber als pflicht darstellung; nach bank.md wäre er eine
  eigene Kette mit hoehe sprosse, 3 Zeilen, vor den
  Pflichtelementen.
- N5 bank.md 2026-09-27b: Punkte „als Zeilentupel mit senkrechtem
  Strich, A(1 | 2 | 0)"; der Eintrag schreibt S(1|2) ohne
  Leerzeichen. Nicht geändert; das Skript liest beides.
- N6 Prüfskript: Bei Termlösungen und Nachweisen prüft pruef nur
  eine Zahl (erste Zahl der Lösung); das absolute Glied einer
  Normalform liegt nie an der Ergebnisstelle.
