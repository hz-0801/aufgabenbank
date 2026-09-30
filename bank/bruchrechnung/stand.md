# Stand: bruchrechnung

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/bruchrechnung.md)
Datum: 2026-09-30 08:43 (date, UTC)
Grundlage: bank.md 2026-09-30b, werkzeuge/bank-pruef.py v0.9,
Vorlage auftrag-eintrag.md 2026-09-29e; Nachtrag zu den
Katalogänderungen vom 30.09. (Fehlerzeile Z. 87 und Typzeile Z. 25:
Nenner geteilt statt malgenommen; Fertigkeit Z. 35: Einmaleins und
Kopfrechnen). Vorheriger Stand: Nachzug vom 29.09. auf d78032a.
Endstand: 0 Abweichungen, 0 Warnungen mit `--katalog`.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      26         0        12      13        0       1
    e1.jsonl        62        12         5      21       12      12
    e2.jsonl        35         4         5      15        2       9
    e3.jsonl        61         4        10      24       11      12
    e4.jsonl        42         4         5      18        6       9
    e5.jsonl        42         4         5      18        6       9
    gesamt         268        28        42     109       37      52

Pflicht je Einheit (fehler/begruenden/anwendung/darstellung):
e1 3/3/3/3 · e2 3/3/3/– · e3 3/3/3/3 · e4 3/3/3/– · e5 3/3/3/–;
Zone fehler 1 (Paar).

## Nachtrag 30.09. je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         24      0              2          0
    e1           62      0              0          0
    e2           35      0              0          0
    e3           60      0              1          0
    e4           42      0              0          0
    e5           42      0              0          0

Zone: kette und sprosse_text der Fertigkeit 5 nachgezogen (vier
Zeilen); die mittlere Zeile und der Fallstrick (schriftliches
Addieren und Subtrahieren) sind auf Kopfrechnen umgeschrieben
(Vervielfachen mit Zerlegen, Teilen mit Zerlegen der Zehner). e3:
sprosse_text der drei fehler-Zeilen nachgezogen; die Serie P1
zeigte das Muster „Nenner geteilt“ schon (5/8 : 4 = 5/2), ihre
Lösung nennt den Fehler jetzt beim Namen. Prüfskript vor dem
Nachtrag: 7 Abweichungen (zone 4, e3 3), alle „sprosse_text nicht
wortgleich“; Formprobe 0. Keine ids umbenannt.

## Nachzug 29.09. je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         26      0              0          0
    e1           49      3             10          0
    e2           25      0             10          0
    e3           40      6             15          4
    e4           32      0             10          0
    e5           30      0             12          0

Übernommen: Aufgabe und Lösung wortgleich, nachgezogen nur id,
kette_nr, sprosse, quelle (98–103 → 99–104), sprosse_text und
merkmal der Prüfungshöhe. Umgeschrieben: Päckchen (je Kette 5),
je Einheit zwei fehler- und zwei begruenden-Zeilen (Pflichtformen),
Urteil zuerst in anwendung, e5 Termprüfung (Urteil zuerst). Neu:
e1 s5 Hauptnenner (3), e3 k1 s2 Stammbruch von einem Bruch (3),
e3 k2 s2 Kontrolle (3). Entfallen: e3 Erkennungsschritt
„Von heißt mal“ (4).

## Originale je Einheit

- e1: 2014-OS-K6c, 2015-OS-K7d, 2020-OS-K6c, 2017-OS-K6b,
  2026-FOR-K6c, 2014-OS-B1d
- e2: 2014-OS-K4d
- e3: 2019-OS-K6c, 2018-OS-K7c, 2019-OS-K6b, 2024-OS-K5c;
  Dividieren ohne Original (3 Zeilen, original null)
- e4: 2014-OS-K4c, 2024-OS-K2d, 2023-OS-B1f
- e5: 2021-OS-B1g, 2016-OS-B1i, 2015-OS-K2a

## Prüfskript vor der Korrektur

- Bestand gegen die neue Mappe: 155 Abweichungen (e1 36, e2 23,
  e3 40, e4 29, e5 27), 153 × „sprosse_text nicht wortgleich in
  Zeile quelle“ (Zeilen verschoben), 2 × „\janein: loesung beginnt
  nicht mit ja oder nein“ (e5 Termprüfung); zone 0.
- Erster Wurf: e1, e2, e4, e5 je 0; e3 1 Abweichung („kette-Name
  wechselt“ in der Pflichtkette), nach einer Korrektur 0. Keine
  Einheit ist zweimal gescheitert. Warnungen 0.

## Entscheidungen

1. Zone bleibt: Fertigkeiten Z. 31–36 unverändert.
2. Prüfungshöhe mit „daneben“ (e1, e3 k1, e4, e5) ist eine
   Sprosse mit dem ganzen Text der Zeile, weil die Katalogzeile
   sie als eine nennt; je Original 2 Zeilen wie bisher.
3. Päckchen: fester Wert e1 „3/11“, e2 „5,2“, e3 k1 „2/13“, e3 k2
   „3/5“, e4 „mal 10“, e5 „20 + 3 · …“; der feste Wert steht im
   merkmal.
4. e3: Pflicht in einer Kette „Multiplizieren“ (k3) nach bank.md;
   die Dividieren-Zeilen (1 fehler, 3 begruenden) tragen diesen
   Kettennamen, inhaltlich bleiben sie beim Teilen.
5. P1-Serie je Einheit am Kennzeichen „Überschlag“ (Summe größer
   als Summand, Produkt kleiner als 1, Teilen durch Zahl kleiner
   als 1, Endziffer).
6. e3 Stammbruch-Sprosse ohne „von“-Satz als Rechnung „Berechne
   1/n von a/b“, Lösung mit Schrittnamen; die Sprosse steht als
   Vorrat laut Katalog an Stelle 2.
7. Urteile je Einheit: e1–e3 je Richtig/Ja/Nein, e4 und e5 je ein
   Ja (P2 „Richtig“) und zwei Nein; dazu je eine Aussagenserie mit
   wahr und falsch.
8. e5 Termprüfung: Lösung beginnt mit der Folge der Urteile
   („Ja, nein, ja.“), weil \janein das erste Wort verlangt.
9. Zone Fertigkeit 5 (30.09.): kette ist der Fertigkeitstext bis
   zum Gedankenstrich, mit der Klammer; Fallstrick ist das
   Zerlegen der Zehner beim Teilen im Kopf (96 : 8), weil die
   Katalogzeile keinen Fallstrick nennt und dieser Handgriff in
   Einheit 4 (Dezimalzahl geteilt durch natürliche Zahl) gebraucht
   wird.
10. e3 fehler (30.09.): die beiden Muster des Sprossentexts
   verteilen sich auf die Schülerrechnung (Kehrbruch beim
   Multiplizieren) und die Serie P1 (Nenner geteilt); die
   fehlerfreie Vorlage P2 bleibt beim Multiplizieren.

## Befunde

1. Katalog: Erkennungsschritt „Von heißt mal“ (Z. 40) wiederholt
   die Vorstufe „„von“ markieren“ (Z. 101) und entfällt jetzt
   (bank.md, Vorlage 29c); Befund 9 des Stands vom 27.09. ist
   damit entschieden.
2. Erledigt 30.09.: Katalog Z. 87 und Z. 25 nennen jetzt „Nenner
   geteilt statt malgenommen“; Bank und Beispiel stimmen überein.
3. Erledigt 30.09.: Katalog Z. 35 heißt „Einmaleins und
   Kopfrechnen“; die Zone hat keine schriftlichen Verfahren mehr.
4. Prüfskript: \janein-Probe verlangt ja/nein als erstes Wort auch
   bei drei \janein in einer Aufgabe; die Lösung muss dann die
   Urteilsfolge voranstellen.

## Offene Punkte

- Schrittnamen nur in neuen und umgeschriebenen Lösungen; der
  übernommene Bestand zeigt reine Ergebnisse.
- Kein LaTeX-Lauf; Grafikbausteine unverändert.
- Die Prüfungshöhen in e1 und e3 setzen Pfadwahrscheinlichkeiten
  voraus, die Klasse 6 nicht kennt (Zielmarke).
