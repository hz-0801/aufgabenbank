# Stand: pyramide-kegel-kugel

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf von mappen/pyramide-kegel-kugel.md)
Datum: 2026-09-27 07:18 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.3, Endstand 246 Zeilen OK,
0 Abweichungen, 0 Warnungen; mit `--katalog` (Katalogzeilen aus
Teil 1 der Mappe) ebenfalls 0/0.

## Dateien

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     48 |        0 |        18 |      29 |        0 |       1 |
| e1    |     77 |       20 |         5 |      36 |        4 |      12 |
| e2    |     63 |        8 |         5 |      36 |        2 |      12 |
| e3    |     58 |        4 |         5 |      33 |        4 |      12 |

Pflicht je Einheit: fehler 3, begruenden 3, darstellung 3,
anwendung 3. Zone: pflicht fehler 1 (Zone-Paar).

## Originale je Einheit

- e1: 2015-OS-K6b, 2015-OS-K6c (je 2 Zeilen, hoehe pruefung)
- e2: 2026-FOR-K2d (2 Zeilen, hoehe pruefung); 2026-FOR-K2b an
  der Kettensprosse s12 (3 Zeilen, hoehe sprosse)
- e3: 2016-OS-K3c, 2016-OS-K3d (je 2 Zeilen, hoehe pruefung)

## Prüfskript vor der Korrektur

- zone: 1. Lauf mit v0.2 (lokaler Stand beim Start) 0
  Abweichungen, 0 Warnungen; mit v0.3 nachgeprüft 0/0.
- e1: 0 Abweichungen, 0 Warnungen im ersten Lauf (v0.3).
- e2: 1. Lauf 1 Abweichung, 0 Warnungen: k3-s3-v2 „4 nicht an der
  Ergebnisstelle" – die Lösung nannte 3 m statt 4 m als fehlende
  Höhe; Lösung korrigiert. 2. Lauf 0/0. Danach Nachtrag original
  an k2-s12 (neue Auftragsfassung), 0/0.
- e3: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- Zweimal gescheitert: keine Einheit.

Eigene Zusatzprobe (mehrstellige Kastenzahlen in aufgabe und
grafik; Ergebnisse aus Kasten, „Typische Fehler" und Zielmarke in
loesung, etwa 282,7, 523,6, 904,8, 235,6): e1 im ersten Lauf 4
Treffer „10" – Fehlalarm der Probe (die 10 aus „(P10 …)"), Probe
berichtigt; sonst 0 Treffer.

## Entscheidungen

1. Zone: Reihenfolge nach erster Verwendung. „alle Einheiten" und
   „Einheit 1 und 2" zählen als Einheit 1, innerhalb gleicher
   Einheit Folge des Eintrags: Zeilen 27, 28, 29, 31, 32, 33, dann
   30, 34, 35 (f1–f9).
2. Zone: kette und sprosse_text bis zum Doppelpunkt, wo die Zeile
   einen hat (29, 32, 35), sonst bis „ – Einheit". Je Fertigkeit
   ein bis drei Fallstricke, rückwärts aus den Stellen des
   Lernblatts geplant.
3. Zone-Paar in f7 „Radius aus Durchmesser" (s4 Fehler finden,
   s5 Rechenaufgabe): Durchmesser statt Radius ist der erste
   Eintrag in „Typische Fehler" und steht in zwei P10-Originalen.
   Gerechnet wird an der Kreisfläche, weil die Zone keinen Begriff
   des Themas nennt.
4. Erkennungsschritte: e1 k1–k4 (Zeilen 37, 39, 41, 42), e2 k1
   (Zeile 40), je 4 Zeilen. „Welche Strecke ist das?" (Zeile 38)
   entfällt (Befund 1). „Stützdreieck einzeichnen" steht nur an der
   Pyramide; das Stützdreieck des Kegels übt e2 s5.
5. Prüfungshöhe mit zwei Originalen in einem Kettenschritt (e1
   s14: K6b zeichnen, K6c nachweisen; e3 s13: K3c, K3d): eine
   Sprosse mit 4 Zeilen, je Original 2, wie quadratische-
   funktionen e3 s9.
6. e2 s12 Kegeldach (P10-Form 2026-FOR-K2b/c): original K2b, weil
   Dachfläche und Kosten der Kern sind; die Gesamthöhe (K2c) steht
   in denselben Zeilen. Prüfkennung „(P10 2026 FOR)".
7. Keine Typen ohne Kette: Alle Typen der Zeilen 21–23 stehen in
   einer Kette oder den Pflichtelementen, verweisen auf andere
   Einträge (Restvolumen → koerper.md) oder sind Vorrat (r aus V,
   Sektorwinkel).
8. Pflichtelemente: eigene letzte Kette mit dem Namen der
   Verfahrenskette, Sprossen 1 fehler, 2 begruenden,
   3 darstellung, 4 anwendung; sprosse_text aus „Typen je
   Lerneinheit". Darstellung: e1 „Schrägbild zeichnen, Höhe
   einzeichnen und beschriften", e2 „Schrägbild eines Kegels
   skizzieren (…)", e3 „Kugel skizzieren (…)".
9. sprosse_text: Teilstring der Kettenzeile ohne „(4×)",
   „(Vorstufe)", GYM- und LISUM-Zusätze; Prüfungshöhe = Text
   zwischen „Prüfungshöhe: " und „ (P10-Form"; e3 s11 ohne
   „Sachaufgabe (".
10. Kastenzahlen streng: keine mehrstellige Zahl aus dem
    Merkkasten in aufgabe oder grafik; zusätzlich keine
    Aufgabenzahlen, deren Ergebnis ein Kasten- oder
    Zielmarkenergebnis ist (Kugel r = 5 oder 6, Kegel r = 5 mit
    h = 12, Pyramide a = 10 mit h = 12).
11. e1 s12 „h aus V und G" trägt die GYM-Marke im merkmal und
    bleibt in der Kette; Blätter für die Oberschule wählen die
    Sprosse ab.
12. e1 s10 „Netz … vervollständigen": Maße ins vorgegebene Netz
    schreiben und Seitenhöhen einzeichnen, weil `\netzpyramide`
    nur das ganze Netz zeichnet. e2 s10 Kegelnetz ohne Grafik
    (kein Baustein), als Radien von Kreis und Kreisausschnitt.
13. e2 s14 verfremdet K2d mit derselben Falle ((k · r)² als k · r²
    führt auf die Behauptung): Faktor 6 („doppeltes Volumen",
    richtig zwölffach) und 1,5 („halb so viel", richtig drei
    Viertel).
14. Vorstufen e1 und e2 als Ankreuzen; Strecken, die `\pyramide`
    nicht markieren kann (Seitenhöhe, Seitenkante), im Text
    beschrieben.
15. Buchstaben: e1 h Höhe, h_s Seitenhöhe (nur in Lösungen und
    erklärt in Fehler-finden), Seitenkante ohne Buchstaben; e2 r,
    h, s; e3 r, d, V, O. Einheiten ² und ³ als Unicode außerhalb
    der Mathe-Umgebung.
16. Grafik nur, wo an ihr gelesen oder gezeichnet wird; freie
    Zeichenaufgaben mit `\rechenplatz` als Zeichenfläche und der
    Lösung in loesungsgrafik, wo ein Baustein passt.

## Befunde

1. Katalog: Der Erkennungsschritt „Welche Strecke ist das?"
   (Zeile 38) verlangt denselben Handgriff wie die Vorstufen „Höhe,
   Seitenhöhe oder Seitenkante benennen" (e1) und „Höhe,
   Mantellinie oder Radius benennen" (e2). Nach bank.md entfällt
   er; der Katalog führt beide.
2. Katalog/bank.md: Die Vorstufe e3 „Radius oder Durchmesser
   benennen" wiederholt den Erkennungsschritt „Radius oder
   Durchmesser?" (Zeile 40). Der steht nach bank.md in e2 (erste
   Einheit seines Bereichs, dort keine gleiche Vorstufe), der
   Handgriff also zweimal im Eintrag. bank.md regelt nur die
   gleiche Vorstufe in derselben Einheit.
3. Prüfskript v0.3: Die Sperre fängt Kastenterme mit Wurzel oder
   π nicht. Probe in e2 k2-s1-v1: „$s = \sqrt{12^2 + 5^2}$" und
   „$V = \frac{4}{3} \cdot \pi \cdot 5^3$" ohne Befund;
   „$G = 10 \cdot 10$" und „$\pi \cdot 5^2 \cdot 12 : 3$" erkannt.
4. bank.md: „kette und sprosse_text der Zone sind die Fertigkeit
   bis zum Doppelpunkt" – sechs der neun Fertigkeitszeilen haben
   keinen Doppelpunkt (Entscheidung 2).
5. bank.md: Ein Kettenschritt mit zwei Originalen (e1 s14 K6b/c,
   e2 s12 K2b/c, e3 s13 K3c/d) ist nicht geregelt; das Feld
   original trägt nur eines.
6. Katalog: Einheit 1 trägt die Marke „keine P10-Aufgabe" (Zeile
   14), ihre Prüfungshöhe nennt aber „P10-Form 2015-OS-K6b/c"
   (fremdgeführte Originale, Zeile 90). Hier als Originale mit
   hoehe pruefung geführt.

## Offene Punkte

- LaTeX nicht kompiliert. Ungeprüft: ob `\pyramide` die Höhe auch
  mit leerem Label zeichnet (dann verrät die Grafik in e1 k5 s14
  v1–v2 die Lösung); `?` als Label in `\kegel`, `\kugel`,
  `\netzpyramide`; `\rechenplatz` im Feld grafik; ² und ³ im Font.
- Kein Baustein für Kegelnetz und zusammengesetzte Körper
  (Zylinder oder Kegel mit Halbkugel): e2 k2 s10 ohne Grafik,
  e3 k2 s3 v1 und v3 ohne loesungsgrafik.
- Nicht als eigene Zeilen aufgenommen: 2024-OS-K4c (Restvolumen,
  koerper.md), 2024-OS-K4a und 2016-OS-K3b (Basismarken, Typ bei
  kreis.md), 2018-OS-K6d (pythagoras.md), 2024-OS-K4b
  (koerper.md).
- Einige Zahlen kehren in verschiedenen Sprossen wieder (etwa
  Kegel r = 4 cm, Kugel r = 3 cm) mit anderer gesuchter Größe;
  keine Aufgabe ist doppelt.

## Nachbesserung 2026-09-27

- Nachprüfung mit bank-pruef.py v0.5 und bank.md Stand
  2026-09-27b: 0 Abweichungen, 0 Warnungen vor und nach der
  Nachbesserung; keine Zeile geändert.
- Prüfungshöhen: alle drei tragen ein Original (e1 K6b/c, e2 K2d,
  e3 K3c/d); keine Prüfungshöhe ohne Original steht als hoehe
  sprosse.
- Erkennungsschritte: „Welche Strecke ist das?" ist bereits
  entfallen (Befund 1); die übrigen fünf verlangen keinen
  Handgriff einer Vorstufe derselben Einheit, keiner gestrichen.
- Befund 3 bleibt offen: v0.5 fängt „$\sqrt{12^2 + 5^2}$" und
  „$\frac{4}{3} \cdot \pi \cdot 5^3$" in aufgabe weiterhin nicht
  (Probe an einer Kopie von e2 k2-s1). Befunde 2, 4, 5 und 6
  bleiben offen; bank.md 2026-09-27b regelt sie nicht.
