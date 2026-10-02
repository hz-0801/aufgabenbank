# Stand: pythagoras

Katalog: hz-0801/mathe-nachhilfe, katalog/pythagoras.md,
Commit cebfd509ea71ae238b589537bd00b7fc306df06f (Kopf der Mappe).
quelle = Zeilennummern dieses Stands.
Datum: 2026-09-29 15:30 CEST (date).
Vorlage auftrag-eintrag.md 2026-09-29c; Nachzug des Bestands vom
27./28.09. (Vorgeschichte im git-Log dieses Ordners).
Prüfung: `python3 werkzeuge/bank-pruef.py pythagoras --katalog`
(v0.9): 240 Zeilen, 0 Abweichungen, 0 Warnungen.
Umbauskript: werkzeuge/einmalig/nachzug-pythagoras-2026-09-29.py
(erzeugt e1–e3 aus dem Stand 1e236dd byte-gleich).

## Zahlen

    Datei       Zeilen  vorstufe  grundfall  sprosse  pruefung  pflicht
    zone.jsonl      38         0         18       19         0        1
    e1.jsonl        65         8          5       36         4       12
    e2.jsonl        62        12          5       27         6       12
    e3.jsonl        75         8          5       42         8       12
    gesamt         240        28         33      124        18       37

Nachzug je Einheit (übernommen / neu / umgeschrieben / entfallen):

    e1   55 / 0 / 10 / 0
    e2   47 / 4 / 11 / 0
    e3   58 / 0 / 17 / 0

„übernommen“ heißt: Aufgabe, Lösung und pruef wortgleich;
nachgezogen wurden id, kette_nr, sprosse, variante, quelle,
sprosse_text (Vorstufen, Prüfungssprosse) und das merkmal der
Prüfungssprosse. Zone unverändert (Fertigkeiten Z. 25–33 gleich).

Prüfskript vor der Korrektur (mit `--katalog`, Stand 1e236dd):
e1 44, e2 43, e3 60 Abweichungen, zone 0; Grund in allen 147
„sprosse_text nicht wortgleich in Zeile quelle“ (Zeilennummern und
Vorstufentexte der neuen Mappe). Nach dem Umbau je Einheit im
ersten Lauf 0. Keine Einheit scheiterte.

## Originale

- e1 (k2 s12): 2020-OS-K7a, 2025-OS-K4a
- e2 (k3 s10): 2024-OS-K6a, 2022-OS-K5a, 2025-OS-K2c
- e3 (k2 s15): 2018-OS-K6d, 2026-FOR-K2c, 2022-OS-K2c, 2019-OS-K2d

## Entscheidungen

1. Prüfungshöhe: je Verfahrenskette eine Sprosse (die letzte), alle
   Originale der Kettenzeile darin, je 2 Zeilen; sprosse_text ist
   der Prüfungsabschnitt der Kettenzeile nach „→“ (wie
   prozentrechnung). Vorher eine Sprosse je Original.
2. Päckchen: e1 Kathete a = 36 cm fest, b wandert; e2 Hypotenuse
   85 cm fest, Kathete wandert; e3 Schenkel 65 cm fest, Grundseite
   wandert. Lösungen mit Schrittnamen (regeln.md 12).
3. Vorstufen e1 und e2 übernommen: die Aufgaben decken den längeren
   Sprossentext schon; e3 umgeschrieben, weil der Katalog jetzt
   Figuren mit Höhe und Pyramide/Kegel nennt (Bestand: Raute,
   Rechteck, Quader, Drachen).
4. „Satz oder Umkehrung?“ als k2 in e2 (nach „Welche Seite ist die
   längste?“, Folge des Katalogs); zwei Alltagssätze, ein Satz aus
   der Geometrie, der Satz des Pythagoras selbst; 2 ja, 2 nein.
5. P1 fehler als Serie in allen drei Einheiten (Kennzeichen: die
   Hypotenuse ist die längste Seite, kürzer als a + b); P3 entfällt,
   weil keine Kette eine Umformungskette ist.
6. P2 in e1 und e3 in der Mehrzahl (vier Rechnungen, eine falsch),
   in e2 als fehlerfreie Vorlage zur Umkehrung.
7. anwendung: in allen Urteilszeilen steht das Urteil als erstes
   Wort; die Grenzwertentscheidung (P8) trugen schon v1/v2.
8. e3 darstellung v2 rückwärts (Rechnung → Skizze) statt Kegel
   „in Originalgröße zeichnen“, damit P7 zwei Richtungen hat.
9. Neue Zeilen meiden Seitenpaare, die der Bestand schon trägt
   (33/56/65, 3/4/5 der Knotenschnur), und die Tripel der
   Päckchen (eigene Paarprobe); der Bestand bleibt.

## Befunde

1. Katalog: Die drei alten Erkennungsschritte stehen jetzt als
   Vorstufe in der Kettenzeile; „Ganz oder halb?“ (Z. 38) und die
   e3-Vorstufe „Teildreieck nachfahren“ sind getrennte Handgriffe
   (Länge wählen / Dreieck finden), beide bleiben. Kein
   Erkennungsschritt wiederholt eine Vorstufe derselben Einheit.
2. Vorlage: Gegenprobe „genau eine Sprosse mit hoehe pruefung je
   Kette“ und bank.md „Prüfungshöhe 2 je Original“ passen nur
   zusammen, wenn eine Sprosse mehrere Originale trägt; das
   Prüfskript prüft die Zahl der Prüfungssprossen nicht.
3. bank/_punkte.csv (außerhalb des Schreibbereichs) trägt noch die
   alten ids (e1-k2-s13, e2-k2-s10…s12, e3-k2-s15…s18); die 18
   Zeilen brauchen einen Lauf von werkzeuge/punkte.py.
4. Prüfskript: Die Doppelprobe vergleicht ganze Aufgaben; gleiche
   Seitenpaare in verschiedenen Aufgaben (etwa 11/60/61 viermal im
   Bestand) meldet sie nicht. Hier mit einer eigenen Paarprobe
   geprüft; der Commit „e1, e3 (Zahlen der neuen Zeilen)“ nennt
   33/56/65 irrtümlich als Mappenpaar, es war ein Bestandspaar.

## Offene Punkte

- Kein LaTeX kompiliert; neu und ungeprüft: `\trapez[hoehe=h]`,
  `\parallelogramm[hoehe]`, `\pyramide` mit leeren Labels (e3 s0),
  `\dreieck` als loesungsgrafik (e3 darstellung v2).
- Übernommene Lösungen tragen keine Schrittnamen (Auftrag).
- duplikate.md und bau/sprachlauf/pythagoras.md nennen alte ids.

## Nachtrag 2026-10-02: Duden-Abgleich und Leiterregeln

Katalog: mathe-nachhilfe katalog/pythagoras.md, Commit 4f12b9c (Umsetzung 02.10.2026). e1 Kette 2 (Hypotenuse): Satz begründen, Zerlegungsbeweis (s12, GYM), Rückwärts (s13), Gemischt (s14), Prüfung jetzt s15. e2 Kette 3 (Kathete): Rückwärts (s10), Gemischt (s11 = Abgleich A2, unmittelbar vor der Prüfung statt nach s4), Prüfung s12. e2 neue Kette 4 Kathetensatz und Höhensatz (GYM): Grundfall 5, Kathetensatz, Abschnitte bilden, Rechteck in Quadrat, Rückwärts, Gemischt je 3, Prüfungshöhe ohne Original 3 (zwei aus den Entwürfen); die alten Ketten 4 (Tripel) und 5 (Pflicht) heißen jetzt 5 und 6. e3 Kette 2: Quadrat aus Diagonale (s7, alte 7–13 rücken um eins), Sichtweite/Tangente (s15, GYM), Raumdiagonale s16, Rückwärts (s17), Gemischt (s18), Prüfung s19. Zusatzvarianten A1, A3, A4, A6, A10, A12, A13 an den alten Sprossen. ids in bank/_punkte.csv nachgezogen (18 Zeilen). Prüfskript ohne und mit --katalog 0 Abweichungen.

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|---|---:|---:|---:|---:|---:|---:|
| e1 | 8 | 5 | 47 | 4 | 12 | 76 |
| e2 | 12 | 10 | 54 | 9 | 12 | 97 |
| e3 | 8 | 6 | 60 | 8 | 12 | 94 |
| zone | 0 | 18 | 19 | 0 | 1 | 38 |

Summe 305 Zeilen.
