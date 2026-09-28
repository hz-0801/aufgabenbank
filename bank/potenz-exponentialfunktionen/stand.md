# Stand: potenz-exponentialfunktionen

Katalog-Commit: ca7939b8873ca0ea0c6a99ac2fbb90395bd0a700 (2026-09-27,
aus dem Kopf der Mappe). Zeilennummern in quelle beziehen sich auf
diesen Stand.
Datum: 2026-09-28 03:23 UTC (`date`), Nachtwächter-Sitzung.
Prüfskript: werkzeuge/bank-pruef.py v0.5, Endstand 464 Zeilen,
0 Abweichungen, 0 Warnungen; mit `--katalog` (Zeilen der Mappe
als Katalogdatei) ebenfalls 0.

## Zeilen je Datei und hoehe

| Datei  | Zeilen | vorst. | grundf. | spr. | pruef. | pfl. | grafik |
|--------|-------:|-------:|--------:|-----:|-------:|-----:|-------:|
| zone   |     62 |      – |      30 |   31 |      – |    1 |      3 |
| e1     |     95 |     12 |      15 |   42 |     14 |   12 |     55 |
| e2     |     74 |      8 |      10 |   33 |     14 |    9 |      0 |
| e3     |     79 |      8 |      10 |   33 |     16 |   12 |      0 |
| e4     |     43 |      4 |       5 |   21 |      4 |    9 |      9 |
| e5     |    111 |     12 |      15 |   63 |      9 |   12 |     19 |
| gesamt |    464 |     44 |      85 |  223 |     57 |   55 |     86 |

loesungsgrafik: 12 Zeilen in e5 (Skizzieraufgaben), sonst "".
Pflichtelemente: e1, e3, e5 fehler, begruenden, darstellung,
anwendung; e2 und e4 fehler, begruenden, anwendung (Entscheidung 5).

## Originale je Einheit (je 2 Zeilen)

- e1: 2018-OS-K2b, 2016-OS-K4d (k1) · 2026-FOR-K7b, 2019-OS-K7c
  (k2) · 2025-OS-K7a, 2017-OS-K7b, 2016-OS-K4b (k3)
- e2: 2025-OS-K7b, 2018-OS-K2a (k1) · 2026-FOR-K7a, 2020-OS-K4a,
  2016-OS-K4a, 2019-OS-K7a, 2017-OS-K7a (k2)
- e3: 2026-FOR-K7c, 2017-OS-K7c, 2019-OS-K7b (k1) · 2025-OS-K7b,
  2020-OS-K4c, 2016-OS-K4e, 2017-OS-K7d, 2018-OS-K2c (k2)
- e4: 2020-OS-K4b, 2016-OS-K4c
- e5: kein Original; je Kette eine Prüfungshöhe ohne Original mit
  3 Zeilen (Zielmarke RLP/LISUM-PH)

## Prüfskript vor der Korrektur

| Datei | Abw. | häufigster Grund                            | Warn. |
|-------|-----:|---------------------------------------------|------:|
| zone  |   16 | merkmal uneinheitlich (15, Generator)       |     0 |
| e1    |    1 | pruef nicht an der Ergebnisstelle           |     0 |
| e2    |    4 | pruef nicht an der Ergebnisstelle (3)       |     0 |
| e3    |    7 | Lösungszahl falsch gerundet (6)             |     0 |
| e4    |    7 | Baustein \log (3), pruef-Liste zu lang (3)  |     0 |
| e5    |    3 | Sperre y=x^4, Punkt außerhalb, Ergebnisst.  |     0 |

e3 brauchte zwei Korrekturrunden (nach der ersten blieb eine
falsch gerundete Zahl); keine Einheit ist liegen geblieben.
Außerhalb der Meldungen geändert: e1-k3-s5-v3 (Tabellenwert 372
statt 371), e2-k2-s8-v8 (9,522 statt 9,521 – innerhalb der
Toleranz, aber falsch), 48 Zeilen der Gegenprobe Kastenzahlen
(Commit e7b25fb), zwei Pflicht-Sprossen mit quelle 123 und 15
(sprosse_text war nicht wortgleich in Zeile 23 bzw. 25).

## Gegenprobe (Ist-Werte)

- Verfahrensketten: e1 drei, e2 zwei, e3 zwei, e4 eine, e5 drei;
  jede mit genau 5 Zeilen grundfall (Skript ohne Warnung), jeder
  sprosse_text wortgleich in der Zeile quelle (`--katalog`, 0).
- Prüfungshöhe: je Verfahrenskette genau eine Sprosse hoehe
  pruefung als letzte; Originale je 2 Zeilen, ohne Original 3.
- Kastenzahlen (mehrstellig aus den Merkkästen 1–5: 20, 25, 30,
  45, 1,5, 1,06, 0,94, 72, 60, 1,2, 200, 1,3, 571, 2020, 2024,
  64, 32, 81, 27): in der Rolle des Kastens 0 Treffer nach der
  Nachbesserung; in anderer Rolle bleiben 20/25/30 als
  Prozentsätze (50 Zeilen), 1,5 als x-Wert, 200 als Zielwert
  oder Betrag, 2020 als Prüfkennung (Entscheidung 8). Sperrprobe
  des Skripts: 0.
- form zeichnen: 37 Zeilen, alle mit grafik; jede Zeile mit
  Lies/Zeichne/Koordinatensystem im Text hat grafik (Skript).
- Ankreuzzeilen: Lösung nennt genau eine Option wortgleich oder
  die Lösungszahl steht in genau einer Zahloption (Skript, 0).

## Entscheidungen

1. Alle neun Erkennungsschritte entfallen: jeder verlangt den
   Handgriff der Vorstufe einer Kette derselben Einheit (Befund 1).
   Die Verfahrensketten beginnen deshalb überall mit k1.
2. Prüfungshöhe mit mehreren Originalen: eine Sprosse je Kette,
   2 Zeilen je Original (e2 k2 und e3 k2 je 10 Zeilen).
3. e4 s8 „Logarithmus (Vorrat)“ ist als Kettensprosse mit 3 Zeilen
   gebaut, weil die Kette sonst eine Lücke hätte; log als
   `\mathrm{log}`, weil `\log` kein Baustein ist.
4. Pflichtelemente als letzte Kette mit dem Namen der ersten
   Verfahrenskette; quelle ist die Zeile „Typen je Lerneinheit“
   (23–27), bei e1 anwendung Zeile 123 und e3 anwendung Zeile 15.
5. darstellung nur in e1 (Tabelle ↔ Graph), e3 (Tabelle ↔
   Gleichung ↔ Text) und e5 (Tabelle ↔ Gleichung ↔ Graph); e2 und
   e4 tragen keinen Darstellungswechsel, den die Ketten nicht schon
   haben.
6. Drei-Graphen-Bilder (e1 k2): Exponentialkurve ab Startwert als
   `\funktionab{a*q^\x}`, Gerade als `\gerade`, „gekrümmt ab
   Ursprung“ als `\parabel{p}{0}{0}` – die P10-Skizze hat keine
   Gleichung, ein Exponentialterm kann nicht bei null beginnen.
7. Wertetabellen stehen als `\wertetabelle` in aufgabe (auch
   Sachtabellen der Wachstumsprozesse); grafik trägt nur ksys und
   Zahlenstrahl.
8. Kastenzahlen (Gegenprobe): gesperrt in der Rolle des Kastens
   (Faktor, Anfangswert, Tabellenfolge, Menge in mg, Jahrespaar,
   Potenzwert), frei in anderer Rolle (Prozentsatz, Zeit, x-Wert,
   Zielwert, Kennung). Quellenzeilen der Kästen (1,05; 1,08; 0,89)
   zählen nicht als Kastenzahlen.
9. Potenzfunktionen in aufgabe als f(x), g(x) …, nie „y = x⁴“,
   weil „y=x^4“ aus Typische Fehler Zeile 112 gesperrt ist.
10. Zone: 15 Fertigkeiten mit je einem Fallstrick; Zone-Paar bei
    Fertigkeit 1 (Prozentsatz statt Faktor), dem häufigsten
    Fallstrick der Einheiten 2 und 3; Reihenfolge nach kleinster
    Einheit der Fertigkeitszeile.

## Befunde

1. Katalog: Alle neun Erkennungsschritte (Zeilen 47–55)
   wiederholen die Vorstufe einer Kette ihrer Einheit; der Katalog
   führt beide.
2. Katalog: e1 k3 s5 nennt drei Originale mit zwei verschiedenen
   Leistungen (Punkte in vorbereitetes System; Achsen selbst
   einteilen) in einer Prüfungshöhe.
3. Katalog/bank.md: e4 führt den Logarithmus als „Vorrat“ mitten
   in der Kette vor der Prüfungshöhe; bank.md regelt Vorrat nicht.
4. Prüfskript: `\log`, `\ln`, `\sin` fehlen in STANDARD; Lösungen
   müssen `\mathrm{log}` schreiben.
5. Prüfskript: Eine pruef-Liste verlangt jeden Wert an einer
   Ergebnisstelle; Aufzählungen mit Wörtern dazwischen („bei Tag 1
   … Tag 3“) fallen durch, obwohl die Zahlen stimmen.
6. Prüfskript: Mehrstellige Kastenzahlen prüft es nicht; die 48
   Treffer der Gegenprobe fand erst eine eigene Probe.
7. Prüfskript: Rundungstoleranz 0,005 lässt 9,522 statt 9,521
   durch.
8. bank.md: Ob Fehler finden als Kettensprosse (e5 k2 s9, aus dem
   Katalog) neben dem Pflichtelement fehler steht, ist nicht
   geregelt; hier beides.

## Offene Punkte

- Kein LaTeX-Lauf. `\funktionab{a*q^\x}` mit Dezimalbasis und
  `2^\x` sind in der Anleitung nicht belegt (nur Polynome und
  `1/\x`); ob pgfmath `1.15^\x` so setzt, ist zu prüfen.
- Zone f2 v2 und f12 v2 (Punkte eintragen) haben ein leeres ksys
  mit Karo 8 mm; die Achsenbeschriftung übernimmt die Vorlage.
- e1 k3 s4 und s5 (Achseneinteilung selbst wählen) nutzen ein
  unbeschriftetes ksys 0..8 bzw. 0..10 als Karoraster; ein
  Baustein „leeres Karo“ fehlt.
- Ohne Zeile: 2014-OS-K3c (Brücke Zinsrechnung), 2014-OS-K3b,
  2016-OS-K6b, 2018-OS-B1h, 2021-OS-K4b, 2026-FOR-K3e,
  2020-GYM-K3b (in der Mappe nur als Abgrenzung genannt).
- Generatoren dieser Sitzung liegen nicht im Repo (Auftrag: nur
  unter bank/<eintrag>/ schreiben).
