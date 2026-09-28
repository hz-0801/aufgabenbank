# Stand: pythagoras

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf von mappen/pythagoras.md)
Datum: 2026-09-27 05:28 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.2, Endstand 248 Zeilen OK,
0 Abweichungen, 0 Warnungen.

## Dateien

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     38 |        0 |         0 |      37 |        0 |       1 |
| e1    |     69 |       12 |         5 |      36 |        4 |      12 |
| e2    |     62 |       12 |         5 |      27 |        6 |      12 |
| e3    |     79 |       12 |         5 |      42 |        8 |      12 |

Pflicht je Einheit: fehler 3, begruenden 3, anwendung 3,
darstellung 3. Zone: pflicht fehler 1 (Zone-Paar).

## Originale je Einheit (je 2 Zeilen, hoehe pruefung)

- e1: 2020-OS-K7a, 2025-OS-K4a
- e2: 2024-OS-K6a, 2022-OS-K5a, 2025-OS-K2c
- e3: 2018-OS-K6d, 2026-FOR-K2c, 2022-OS-K2c, 2019-OS-K2d

## Prüfskript vor der Korrektur

- zone: 1. Lauf 27 Abweichungen, 0 Warnungen (18 × „sprosse 0
  genau dann, wenn hoehe vorstufe“, 9 × „merkmal uneinheitlich“;
  in einer dieser Zeilen zusätzlich die Punkt-Lösung mit `\mid`
  nicht erkannt). 2. Lauf nach
  Umnummerieren 0 Abweichungen, 27 Warnungen (Zone verlangt s1
  leicht, s2 mittel). 3. Lauf 0/0.
- e1: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e2: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- e3: 0 Abweichungen, 0 Warnungen im ersten Lauf.
- Zweimal gescheitert: keine Einheit.

Eigene Zusatzprobe (Kastenzahlen, Zahlenpaare der Originale): e3
im ersten Lauf 3 Treffer (13 und 16 in vorgegebenen Fehlrechnungen,
109 und 60 zufällig wie in 2021-OS-K3b), vor dem Commit ersetzt.

## Entscheidungen

1. Prüfungshöhe: je Original der Kettenzeile („Prüfungshöhe: …“)
   eine eigene Sprosse mit 2 Varianten; sprosse_text ist der
   Abschnitt der Kettenzeile zu diesem Original. Nur die Originale
   der Kettenzeile tragen hoehe pruefung. Die übrigen Originale
   der Zielmarke (Ankreuzformen 2017-OS-B1d, 2021-OS-B1h,
   2026-FOR-B1j, 2022-OS-B1g, 2024-OS-B1f; Kathete 2016-OS-K7b,
   2019-OS-K3a, 2026-FOR-K4a) stecken als P10-Form in den
   Sprossen der Kette, ohne Feld original.
2. sprosse_text wortgleicher Teilstring der Kettenzeile, ohne die
   Zusätze „(4×)“ und „(Vorstufe)“; Raumdiagonale ohne die
   Begründungsklammer „(seit 11e Mindeststoff …)“.
3. kette: „Hypotenuse“, „Kathete“, „Figuren und Körper“ (Name vor
   „(Einheit n)“). Typen ohne Kette: kette = Typtext aus „Typen je
   Lerneinheit“. Pflichtkette: Name der Verfahrenskette,
   Sprossen 1 fehler, 2 begruenden, 3 anwendung, 4 darstellung;
   sprosse_text aus „Typen je Lerneinheit“ (Zeile 19, 20, 21).
4. Zone: kette = Fertigkeit bis „ – “, sprosse_text ebenso,
   quelle = Zeile der Fertigkeit. s1 zwei leichte, s2 mittel,
   s3 Fallstrick, alle hoehe sprosse (Prüfskript: sprosse 0 nur
   mit vorstufe, Zone verlangt s1/s2). Je Fertigkeit ein
   Fallstrick. Reihenfolge nach erster Verwendung: „alle
   Einheiten“ zuerst, sonst Folge des Eintrags; daher
   Längeneinheiten (Zeile 29) vor Umstellen (Zeile 28).
5. Zone-Paar: „Wurzel aus jedem Summanden einzeln“ in der
   Fertigkeit Wurzel (f2, s4 Fehler finden, s5 Rechenaufgabe). Der
   häufigste Fehler des Eintrags (Quadrate addiert) ist Themenstoff
   und gehört nicht in die Zone (2.2: kein Begriff des Themas).
6. Erkennungsschritt und gleichartige Vorstufe der Kette sind in
   allen drei Einheiten beide angelegt und inhaltlich getrennt:
   Erkennungsschritt an der Skizze ohne Maße, Vorstufe mit Maßen
   (e1), aus einem Text (e2) oder mit Benennen der Seiten (e3).
7. „Gilt der Satz hier?“ steht nur in e1 (erste Einheit seines
   Bereichs, bank.md), nicht noch einmal vor e3.
8. Typen ohne Kette: e1 „Quadrate über den Seiten zeichnen …“ und
   „Ergebnis mit sinnvoller Genauigkeit angeben“; e2
   „pythagoreische Tripel …“ trotz Vorrat-Vermerk, weil unter den
   Typen geführt; e3 „Rampe, Leiter, Seil an der Wand mit Skizze“.
9. Lösungen, die nur eine Formel sind, stehen in Textform mit
   Unicode-² („m² + n² = k²“); Ankreuzlösungen nennen die
   Position („Kreuz bei der dritten Gleichung“). Grund: siehe
   Befund 1.
10. Rechter Winkel in `\dreieck`-Skizzen über die Winkelbeschriftung
    „90°“; `\dreieckrw` nur in Standardlage (rechter Winkel bei C
    angenommen).
11. Skizze aus Text (darstellung): grafik `\rechenplatz[halb]{4}`
    als Zeichenfläche, die Lösung in loesungsgrafik.
12. Kastenzahlen streng gelesen: keine mehrstellige Zahl aus dem
    Merkkasten (10, 12, 13, 15, 16, 17, 20, 21, 25, 29, 36, 49, 64,
    74, 81, 100, 144, 169, 225, 256, 289, 400, 441, 841, 8,6) in
    einer aufgabe; einzelne Ziffern frei (bank.md). Eigene Probe,
    weil die Sperrprobe Terme nicht fängt (Befund 2).
13. Koordinatenstrecken ohne Längeneinheit; Operatoren in Du-Form
    („Weise nach“, „Begründe“).

## Befunde

1. (erledigt v0.5) Prüfskript: Der Exponent in `$x^2$` gilt als
   Lösungsziffer. Eine Lösung, die nur eine Formel ist, verlangt darum
   ein pruef; bei form ankreuzen steht die „2“ dann in allen Optionen.
   Probe: Ankreuzlösung „$z^2 = x^2 + y^2$“ mit pruef "" → „pruef
   fehlt“.
2. (teilweise erledigt v0.5: „$6^2 + 8^2$“ und „$6² + 8²$“ werden
   gefangen; „$x² + y² = z²$“ und „√74“ gehen in einer Probezeile weiter
   ohne Abweichung durch) Prüfskript: Die Sperrprobe fängt Zahlenpaare
   (Probe „(2|1)“ erkannt), aber keine belegten Terme und Gleichungen
   aus dem Merkkasten: „$6^2 + 8^2$“, „$6² + 8²$“, „$x² + y² = z²$“,
   „√74“ gingen in einer Probezeile ohne Abweichung durch.
3. Prüfskript: Der Kettenname wird nicht gegen die Mappe geprüft (Probe
   „Hypotenuse (Einheit 1)“ ohne Abweichung).
4. (erledigt v0.5; bank.md regelt den Fall, die drei Erkennungsschritte
   sind gestrichen) Katalog: Drei Erkennungsschritte decken sich mit der
   Vorstufe der Kette derselben Einheit („Wo ist der rechte Winkel?“ /
   Rechtwinkelmarke einkreisen; „Lange oder kurze Seite gesucht?“;
   „Teildreieck nachfahren“). bank.md verlangt beide (4 + 4 Zeilen); zu
   klären, ob die Vorstufe dann entfällt.
5. bank.md: „Prüfungshöhe 2 je Original des Katalogs“ lässt offen, ob
   nur die Originale der Kettenzeile gemeint sind oder alle der
   Zielmarke. Das Prüfskript warnt in keinem Fall.
6. (erledigt v0.5; bank.md: frei sind einzelne Ziffern und Zahlen unter
   10) Auftrag, Gegenprobe: „Die Kastenzahlen … kommen in keiner aufgabe
   vor“ widerspricht wörtlich bank.md („einzelne Ziffern … sind frei“);
   hier als mehrstellige Zahlen gelesen.

## Offene Punkte

- LaTeX nicht kompiliert. Ungeprüft: Eckenbeschriftung A, B, C von
  `\dreieck` und `\dreieckrw`, `\rechenplatz` im Feld grafik,
  `\viereck[diagonalen]` ohne Seitenbeschriftung, Label-Argumente
  von `\kegel`, `\pyramide` und `\zylinder` mit Maßen.
- Originale der Zielmarke ohne eigene Prüfungszeilen (Entscheidung
  1); bei Bedarf als weitere Sprossen nachtragen.
- 2025-OS-K2c, Variante 1: Drachenviereck wie im Original, nur
  Zahlen und Kontext (Fenster) geändert; Variante 2 wechselt die
  Figur.
- Einige pythagoreische Tripel kommen in mehreren Einheiten vor
  (etwa 9, 40, 41), jeweils mit anderer gesuchter Seite oder Figur;
  keine Aufgabe ist doppelt.

## Nachbesserung 2026-09-27

- Prüfskript v0.5 vorher 6 Abweichungen, 18 Warnungen, nachher
  0/0.
- Zone: die 18 Zeilen mit sprosse 1 (je Fertigkeit zwei sehr
  leichte) tragen jetzt hoehe grundfall statt sprosse
  (Entscheidung 4 insoweit überholt).
- e1 „Gleichung unter vier Optionen ankreuzen" und e2
  „Kathetengleichung unter vier Optionen ankreuzen": die sechs
  Lösungen nennen die richtige Option wortgleich statt ihrer
  Position (Entscheidung 9 insoweit überholt).
- Erkennungsschritte gestrichen, weil sie denselben Handgriff wie
  die Vorstufe derselben Einheit verlangen (Befund 4): e1 „Wo ist
  der rechte Winkel?", e2 „Lange oder kurze Seite gesucht?", e3
  „Teildreieck nachfahren", je 4 Zeilen; kette_nr und id der
  folgenden Ketten je um eins aufgerückt (Entscheidung 6
  überholt).
- Zeilen jetzt: zone 38 (grundfall 18, sprosse 19, pflicht 1),
  e1 65, e2 58, e3 75 (vorstufe je 8); die Tabelle oben zeigt den
  Stand vor der Nachbesserung.
- Prüfungshöhen: alle neun tragen ein Original der Kettenzeile;
  keine Prüfungshöhe ohne Original steht als hoehe sprosse.
- Befunde 3 und 5 bleiben offen: der Kettenname wird ohne
  --katalog nicht gegen die Mappe geprüft (Probe mit
  „Hypotenuse (Einheit 1)" für die ganze Kette: 0/0), und bank.md
  2026-09-27b klärt die Menge je Original der Zielmarke nicht.

## Nachbesserung Render 2026-09-28

Quelle: bau/render-alle/bericht.md, bau/hefte/bericht.md, bau/fokus/bericht.md, bau/layout-befunde.md Punkt 31. Übersicht aller Einträge: bau/render-alle/behoben.md.

- e1-k1-s0-v2, e1-k1-s0-v3, e1-k1-s0-v4, e1-k2-s0-v2, e1-k2-s0-v3, e1-k2-s0-v4, e1-k2-s2-v1, e1-k2-s2-v2, e1-k2-s2-v3, e3-k1-s0-v4, e3-k2-s1-v1, e3-k2-s1-v2, e3-k2-s1-v3, e3-k2-s1-v4, e3-k2-s1-v5, zone-f3-v2, zone-f3-v4 (17): Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`). Änderung: Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik.

Nur diese 17 Zeilen geändert, alle übrigen byte-gleich. `bank-pruef.py pythagoras`: 0 Abweichungen. Probe: jede Zeile allein in einem Minimaldokument mit mathblatt.sty (hz-0801/blattbau) gesetzt wie werkzeuge/zusammenbau.py v0.7 (teile_normal, teil_schwach, Lösung in \erg), xelatex ohne Fehler.
