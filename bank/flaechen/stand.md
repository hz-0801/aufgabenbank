# Stand: flaechen

Katalog-Commit: de503c9cea3976774daeb6c514adb85829d8df2e
(2026-09-25, aus dem Kopf von mappen/flaechen.md)
Datum: 2026-09-27 07:12 UTC
Prüfskript: werkzeuge/bank-pruef.py; zone und e1 unter v0.2 gebaut,
e2 bis e5 unter v0.3 (kam während der Sitzung per Pull). Endstand
unter v0.3: 244 Zeilen OK, 0 Abweichungen, 0 Warnungen.

## Dateien

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     31 |        0 |        14 |      16 |        0 |       1 |
| e1    |     54 |        8 |         5 |      27 |        2 |      12 |
| e2    |     36 |        4 |         5 |      15 |        3 |       9 |
| e3    |     44 |        4 |         5 |      21 |        2 |      12 |
| e4    |     38 |        4 |         5 |      18 |        2 |       9 |
| e5    |     41 |        4 |         5 |      21 |        2 |       9 |

Pflicht: e1 und e3 fehler 3, begruenden 3, anwendung 3,
darstellung 3; e2, e4, e5 fehler 3, begruenden 3, anwendung 3.
Zone: pflicht fehler 1 (Zone-Paar). e1 vorstufe 8 = Erkennungs-
schritt „Gegeben – gesucht“ 4 + Vorstufe der Kette 4.

## Originale je Einheit (hoehe pruefung)

- e1: 2018-OS-B1f (2 Zeilen)
- e2: kein P10-Original; Zielmarke RLP E / LISUM-PH, original null
  (3 Zeilen)
- e3: 2020-OS-K7b (2 Zeilen)
- e4: 2014-OS-K5c (2 Zeilen)
- e5: 2017-OS-K3b (2 Zeilen)

## Prüfskript vor der Korrektur

- zone: 0 Abweichungen, 0 Warnungen im ersten Lauf (v0.2).
- e1: 1 Abweichung, 0 Warnungen im ersten Lauf (v0.2): Sperre
  „u = 2 · (a + b)“ aus Original 2026-FOR-B1h in e1-k1-s0-v3;
  Formel dort durch „u = a + b + a + b“ ersetzt. Nachlauf unter
  v0.3: 0/0.
- e2: 0 Abweichungen, 0 Warnungen im ersten Lauf (v0.3).
- e3: 0 Abweichungen, 0 Warnungen im ersten Lauf (v0.3).
- e4: 0 Abweichungen, 0 Warnungen im ersten Lauf (v0.3).
- e5: 0 Abweichungen, 0 Warnungen im ersten Lauf (v0.3).
- Zweimal gescheitert: keine Einheit.

Eigene Zusatzprobe Kastenzahlen (Entscheidung 9): e2 im ersten
Lauf 1 Treffer (22 als Fehlrechnung in e2-k3-s1-v3), vor dem
Commit auf 23,1 geändert; alle übrigen Dateien 0.

## Entscheidungen

1. Prüfungshöhe: nur das Original der Kettenzeile („Prüfungshöhe:
   …“) trägt hoehe pruefung, je 2 Zeilen. Die übrigen Originale
   der Zielmarke (2020-OS-B1d, 2025-OS-B1i, 2014-OS-B1g,
   2015-OS-K5d, 2023-OS-K2c, 2018-OS-K6a, 2023-OS-K5c) stecken
   als P10-Form in Sprossen und Typen ohne Kette, ohne Feld
   original (bank.md erlaubt es dort, verlangt es nicht).
2. e2: Prüfungshöhe ohne Original mit 3 Zeilen, original null;
   sprosse_text ist der Zielmarkentext der Kettenzeile (Zeile 101,
   „die Höhe zur genannten Grundseite einzeichnen, …“).
3. kette der Verfahrenskette: Name vor „(Einheit n)“ („Rechteck“,
   „Parallelogramm“, „Dreieck“, „Trapez“, „Zusammengesetzte
   Figuren“). sprosse_text: wortgleicher Abschnitt der
   Kettenzeile ohne „(Vorstufe)“, „(4×)“ und „Prüfungshöhe:“.
4. Erkennungsschritt „Gegeben – gesucht“ (Zeile 43, vor Einheit 1
   und 3) steht nur in e1, der ersten Einheit seines Bereichs;
   kette „Gegeben – gesucht“, sprosse_text wortgleich aus Zeile 43.
5. Pflichtelemente: fehler und begruenden mit sprosse_text aus
   „Typen je Lerneinheit“. anwendung mit sprosse_text „Berechnen
   in Sachkontexten mit verschiedenen Einheiten“ (Zeile 8,
   LISUM-PH), weil die Typenzeilen keine Anwendung führen.
   darstellung nur in e1 und e3, wo „Term zu Figur“ als Typ steht;
   dort die Richtung Term → Figur (zeichnen), die Richtung
   Figur → Term steht schon in der Kette. e2, e4, e5 tragen keinen
   Darstellungstyp und bleiben ohne darstellung.
6. Typen ohne Kette (je 3 Zeilen, sprosse 1): e1 „aus Rechtecken
   zusammengesetzte Fläche (Summe)“, „Einheit wechseln vor dem
   Rechnen (cm und m gemischt)“; e2 „Umfang aus den Seiten“; e3
   „Höhe zur passenden Grundseite wählen (drei Höhen)“, „Umfang“;
   e4 „Umfang mit Schenkel aus Pythagoras oder Sinus (Vorrat)“,
   „Diagonale aus A“; e5 „Sachaufgabe mit Entscheidung (reicht
   die Platte?)“, „Verschnitt in Prozent (Vorrat, Niveau III)“.
   Vorrat-Typen angelegt, weil sie unter den Typen stehen.
7. Zone: kette und sprosse_text sind die Fertigkeit bis „ – “
   (die Zeilen haben keinen Doppelpunkt, Befund 2). Reihenfolge
   Zeile 31, 32, 33, 34, 36 (alle ab Einheit 1, Folge des
   Eintrags), dann 35 (ab Einheit 2), 37 (Einheit 5). Je
   Fertigkeit ein Fallstrick, Dezimalzahlen zwei (Komma beim
   Multiplizieren, Nullen beim Teilen, P10 2023-OS-B1c). Zone-Paar
   in „Flächeneinheiten“ (mit 10 statt 100 umgerechnet, Typische
   Fehler Zeile 93); der häufigste Fehler des Eintrags (Fläche und
   Umfang vertauscht) ist Themenstoff und gehört nicht in die Zone.
8. Term-Lösungen (Term zu Figur, Formel ankreuzen): Enthält die
   Lösung eine Ziffer, trägt pruef den Zahlfaktor des Terms (6 in
   „u = 6x“); reine Buchstabenlösungen und Formeloptionen beim
   Ankreuzen pruef "" (v0.3, Regel d).
9. Kastenzahlen streng gelesen: keine mehrstellige Zahl des
   Merkkastens (10, 12, 18, 22, 28, 30, 36, 40, 50, 60, 75, 81, 84)
   in einer aufgabe, auch nicht in vorgegebenen Fehlrechnungen;
   in loesung erlaubt. Die Prüfkennung „P10“ und Jahreszahlen
   zählen nicht. Eigene Probe, weil das Skript sie nicht prüft.
10. Zusammengesetzte Figuren ohne Grafik, als Text mit Teilmaßen,
    wo kein Baustein die Figur trägt (L-Form, T-Form, Rechteck mit
    Halbkreisen); Grafik nur mit \viereck, \trapez, \drachen,
    \parallelogramm, \dreieck, \dreieckrw.
11. Skizzen zum Einzeichnen (Höhe, rechter Winkel): form zeichnen,
    Lösung in Worten, loesungsgrafik "". Term → Figur: grafik
    `\rechenplatz[halb]{4}`, Lösung in loesungsgrafik, wo ein
    Baustein sie trägt.
12. Entscheidungsaufgaben (e4 Prüfungshöhe, e5 „reicht die
    Platte?“) mit gemischten Antworten ja/nein.

## Nachbesserung 2026-09-27

Prüfskript v0.5, bank.md Stand 2026-09-27b; erster Lauf 0
Abweichungen, 0 Warnungen, Endstand ebenso.

- Keine Zeile geändert: die einzige Prüfungshöhe ohne Original
  (e2-k1-s6) trägt schon hoehe pruefung mit original null, und der
  einzige Erkennungsschritt (e1-k1 „Gegeben – gesucht“, Z. 43)
  verlangt einen anderen Handgriff als die Vorstufe von e1-k2
  („Fläche oder Umfang ankreuzen“).
- Befunde 2, 4, 5 und 6 bestehen unter v0.5 und bank.md
  2026-09-27b fort; keiner ist durch v0.5 erledigt.

## Befunde

1. Katalog: Vier der fünf Erkennungsschritte verlangen denselben
   Handgriff wie die Vorstufe einer Kette derselben Einheit und
   entfallen nach bank.md: „Fläche oder Umfang?“ (Zeile 39) /
   Rechteck-Vorstufe „Fläche oder Umfang ankreuzen“; „Wo ist die
   Höhe?“ (Zeile 40) / Parallelogramm „Höhe einzeichnen“ und
   Dreieck „Höhe zur markierten Grundseite einzeichnen“; „Welche
   Formel?“ (Zeile 41) / Trapez „Formel ankreuzen“; „Zerlege und
   benenne“ (Zeile 42) / „Teilflächen benennen“. Der Katalog führt
   jeweils beide.
2. bank.md: „kette und sprosse_text der Zone sind die Fertigkeit
   bis zum Doppelpunkt“ – die Fertigkeitszeilen dieses Eintrags
   haben keinen Doppelpunkt, sondern „ – Einheit n. Thema …“.
   Genommen bis „ – “ (Entscheidung 7).
3. Katalog: Der Typ „aus Rechtecken zusammengesetzte Fläche
   (Summe)“ (Einheit 1) und die Sprosse „zwei Rechtecke“
   (Einheit 5) sind derselbe Handgriff. Beide angelegt, in
   Kontext und Zahlen getrennt.
4. Prüfskript: Keine Probe der Kastenzahlen, obwohl die
   Gegenprobe des Auftrags sie verlangt; hier eigene Probe
   (Entscheidung 9). Auftrag und bank.md widersprechen sich
   wörtlich („kommen in keiner aufgabe vor“ gegen „einzelne
   Ziffern und Zahlen unter 10 frei“); gelesen als mehrstellige
   Zahlen.
5. Prüfskript: Bei Term-Lösungen mit Ziffer verlangt das Skript
   ein pruef; es prüft dann nur, dass der Zahlfaktor an der
   Ergebnisstelle steht, nicht den Term (Entscheidung 8).
6. Prüfskript: Die Dublettenprobe vergleicht nur den Text; zwei
   inhaltlich gleiche Aufgaben mit anderen Worten gehen durch
   (vgl. Befund 3).

## Offene Punkte

- LaTeX nicht kompiliert. Ungeprüft: ob \trapez die Seiten a und
  c selbst beschriftet; leere Labels in
  `\parallelogramm[seiten={$g$,,,}]`; Einheiten in
  `\viereck[seiten={$9$ m,…}]`; `\drachen` und `\raute` mit den
  Optionen der Kurzreferenz; `\rechenplatz` im Feld grafik; das
  Unicode-× in Maßangaben wie „$8$ m × $3$ m“.
- Skizzen sind nicht überall maßstäblich zu den Zahlen im Text
  (Parallelogramm-Prüfungshöhe, Vorstufen); sie dienen nur zum
  Einzeichnen.
- Stumpfwinkliges Dreieck: die äußere Höhe steht nur im Text, die
  Skizze zeigt sie nicht.
- Kein Baustein für Vielecke mit mehr als vier Ecken oder für
  Rechteck mit Halbkreisen; e5 bleibt dort ohne Grafik
  (Entscheidung 10).
- e4 „Umfang mit Schenkel aus Pythagoras …“ setzt Pythagoras
  voraus (Vorrat); nur mit Pythagoras gerechnet, nicht mit Sinus.
