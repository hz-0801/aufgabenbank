# Stand: potenzen-wurzeln

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(2026-09-25, aus dem Kopf der Mappe)
Datum: 2026-09-27 (`date`, 07:16 UTC)
Prüfskript: werkzeuge/bank-pruef.py v0.3 – Endstand 0 Abweichungen,
0 Warnungen in allen vier Dateien.

## Dateien

    Datei       Zeilen vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      46        0        18      27        0       1
    e1.jsonl        79       12         5      48        8       6
    e2.jsonl        68        4         5      45        8       6
    e3.jsonl        64        8         5      33       12       6
    gesamt         257       24        33     153       28      19

Pflicht je Einheit: fehler und begruenden je 3. Zone: neun
Fertigkeiten, ein Zone-Paar (fehler + Rechenaufgabe) an f3.

## Originale je Einheit

- e1, Prüfungshöhe (s15): 2020-OS-B1h, 2024-OS-B1g, 2019-OS-B1d,
  2022-OS-B1j (je 2)
- e2, Prüfungshöhe (s17): 2025-OS-B1d, 2019-OS-B1j, 2015-OS-K3a,
  2017-OS-B1e (je 2); an Kettensprossen: 2016-OS-B1h (s6, 3),
  2015-OS-K3b (s9, 3)
- e3, Prüfungshöhe (s13): 2015-OS-B1j, 2015-OS-B1c, 2014-OS-B1h,
  2024-OS-K6a, 2022-OS-K2d, 2025-OS-K5c (je 2); an einer
  Kettensprosse: 2020-OS-B1d (s10, 3)
- nicht aufgenommen: 2017-OS-B1g (Basismarke e2, als Form im
  Grundfall ohne Feld original); 2025-OS-B1h, 2023-OS-B1f,
  2014-OS-K7a, 2017-OS-K5d, 2014-OS-K3c, 2020-OS-K4c,
  2026-FOR-K7c, 2015-OS-K3c (Prüfungsform nennt sie als
  Voraussetzung in anderen Einträgen; K3c-Verfahren als Vorrat
  e2 s16 ohne original)

## Prüfskript vor der Korrektur

Erster vollständiger Lauf je Datei (alle mit v0.3):

- zone.jsonl: 0 Abweichungen, 0 Warnungen
- e1.jsonl: 0 Abweichungen, 0 Warnungen
- e2.jsonl: 0 Abweichungen, 0 Warnungen
- e3.jsonl: 1 Abweichung, 0 Warnungen – s4 v2: 2,5 stand in der
  Lösung vor dem „=", nicht an der Ergebnisstelle

Die eigene Gegenprobe (mehrstellige Kastenzahlen, Entscheidung 15)
fand vor dem Commit zusätzlich: 47 in zone f6 v1 (47 · 38) und in
e3 s2 v2 (√47), 2¹⁰ in e1 s15 (Zahl 10 außerhalb der Sprosse mit
Basis zehn). Alles ersetzt. Keine Einheit scheiterte zweimal.

## Entscheidungen

1. Erkennungsschritte, die die Vorstufe ihrer Kette wiederholen,
   entfallen (Befund 3): e1 „Hoch oder mal?“ und „Wer ist Basis,
   wer ist Exponent?“, e2 „Groß oder klein?“ und „Stellen oder
   Nullen?“, e3 „Quadratzahl oder nicht?“ und „Zwischen welchen
   Quadratzahlen?“. Es bleiben e1 k1 „Plus oder minus?“, e1 k2
   „Bruch oder minus?“ und e3 k1 „Was zuerst?“.
2. Vorstufen mit zwei Handgriffen (e1 hoch/mal und Basis/Exponent,
   e2 groß/klein und Stellen/Nullen, e3 Quadratzahl und Nachbarn):
   v1–v2 der erste, v3–v4 der zweite Handgriff, ein merkmal.
3. sprosse_text als wortgleicher Teil der Zeile quelle, ohne den
   Katalogzusatz „(4×)“ und ohne die LISUM-Klammer (e1 s13,
   e2 s10).
4. Prüfungshöhe: eine Sprosse je Einheit trägt alle Originale der
   Kettenzeile, je 2 Zeilen. Ein Original der Einheit, das nicht
   in der Prüfungshöhe steht, aber eine P10-Form-Sprosse hat,
   steht im Feld original an dieser Sprosse (3 Zeilen, mit
   Prüfkennung): e2 s6, s9; e3 s10. P10-Form-Sprossen, deren
   Original schon in der Prüfungshöhe steht (e1 s9, s10, s14;
   e2 s3, s8, s10, s12), bleiben original null ohne Kennung.
5. Der Grundfall trägt kein original; 2017-OS-B1g (100 000 = 10⁵)
   ist dort nur als Form vertreten.
6. Typen ohne Kette nur in e1: „Potenzen von Brüchen“ (Name aus
   Z. 90), „Potenz gegen Dezimalzahl und Prozent vergleichen“,
   „hoch null“ (Name aus Z. 11). In e2 und e3 stehen alle Typen
   der Typenzeile in der Kette.
7. Pflicht: fehler und begruenden je Einheit. darstellung und
   anwendung nicht, weil die Darstellungswechsel (Malkette und
   Potenz, Zehnerpotenzschreibweise hin und zurück) und die
   Anwendungen (e2 s15, e3 s10, Prüfungshöhe e3) Sprossen der
   Kette sind. Fehler-Varianten je ein Muster der Typenzeile: e1
   Basis mal Exponent, negative Hochzahl, größere Basis; e2 Nullen
   statt Stellen, Nullen an alle Ziffern, Vorzeichen übersehen; e3
   halbiert, termweise, „nicht definiert“. Begründen v3 ist je ein
   eigener Fall (negative Hochzahl, Vergleich, Wurzel aus einer
   negativen Zahl).
8. Zone, Reihenfolge nach erster Verwendung, bei gleicher Einheit
   Reihenfolge des Eintrags: f1 Z. 25, f2 Z. 26, f3 Z. 27, f4
   Z. 28, f5 Z. 31, f6 Z. 33 („alle Einheiten“, also ab Einheit
   1), f7 Z. 29, f8 Z. 30, f9 Z. 32. kette = Fertigkeit bis zum
   Doppelpunkt (f6 „Taschenrechner“, f8 „Kommaverschiebung“), ohne
   Doppelpunkt bis vor „– Einheit“.
9. Zone ohne Begriff des Themas: keine Potenzschreibweise außer f3
   (Quadrat einer negativen Zahl, von der Fertigkeitszeile selbst
   verlangt); f6 fragt Klammer und Runden am Ende, nicht die
   Tasten x², √ und EXP.
10. Zone-Paar an f3 (Vorzeichen beim Quadrieren einer negativen
    Zahl; Typische Fehler Z. 74, zwei P10-Fehlerquellen): s5
    fehler, s6 Rechenaufgabe, merkmal ohne „Fallstrick:“.
11. Vergleich mit Kästchen: aufgabe „a □ b – <, = oder >?“, form
    teil, antwort leer; pruef ist der Wert der Potenz oder Wurzel.
12. Unterstreichen (P10-Form 2019-OS-B1d) als form teil, nicht
    ankreuzen: das Skript liest Potenz-Optionen als ihre Basis
    (Befund 1); die P10 fragt ebenfalls „unterstreichen“.
13. 2017-OS-B1e verfremdet mit vier Zahlen der Form a · 10ⁿ
    (−4 · 10³ …) statt −10³: −10³ und −10² läse das Skript als
    dieselbe Zahl −10 (Befund 1). Beide Fallen bleiben: Betrag
    statt Lage (−4 · 10⁻²), übersehener Exponent (−4 · 10²).
14. Zehnerpotenz oder Hochzahl als Ergebnis: loesung mit
    „(Hochzahl = n)“, pruef [Faktor, Hochzahl] – das Skript liest
    keine Exponenten. Gesuchte Hochzahl heißt x, antwort „x = __“.
15. Mehrstellige Kastenzahlen (Probe von Hand): 12, 16, 25, 30,
    36, 47, 81, 125, 144, 1 000 000, 470 000, 32 500, 6 700 000,
    0,125, 3,25, 6,7, 4,2, 0,0042, 5,48 – in keiner aufgabe. Die 10
    als Basis der Zehnerpotenz ist Gegenstand der Kette e2, der
    Sprosse e1 s12 („Exponent mit Basis zehn“) und der Zone f7/f8
    („mal zehn“ in der Fertigkeitszeile); sonst kommt sie nicht
    vor (Befund 8). Die Prüfkennung „(P10 …)“ zählt nicht.
16. Auch die Beispiele der Typenzeilen (3⁴, 4³, (−3)⁴, 0,4²,
    (2/3)², 2⁸ gegen 3⁵, 2⁻³, 850 000, 0,00035, √169, √7, √50,
    √((−4)²), (√5)², ³√27, 2¹⁰, 5⁰) kommen in keiner aufgabe vor.
17. Prüfkennung „(P10 Jahr OS)“, papier aus der Mappe. Tausender
    ab vier Stellen mit `\,`.

## Nachbesserung 2026-09-27

- Prüfskript v0.5 vorher und nachher 0 Abweichungen, 0 Warnungen
  in allen vier Dateien; keine Zeile geändert oder gestrichen.
- Keine Prüfungshöhe ohne Original: alle drei Prüfungshöhen (e1
  s15, e2 s17, e3 s13) tragen P10-Originale und stehen schon als
  hoehe pruefung.
- Kein Erkennungsschritt zu streichen: die sechs doppelten waren
  schon nach Entscheidung 1 entfallen; die drei verbliebenen
  („Plus oder minus?“, „Bruch oder minus?“, „Was zuerst?“)
  verlangen einen anderen Handgriff als die Vorstufen ihrer
  Einheit (hoch oder mal, Basis und Exponent; Quadratzahl,
  Nachbarn).
- Befund 2 als erledigt markiert: v0.5 sperrt 4^x = 256
  (2024-OS-B1g) und 10^6 = 1 000 000 (Kasten Z. 55) in einer
  aufgabe (Probe am 2026-09-27).

## Befunde

1. Prüfskript: normiert streicht Exponenten. Eine Option wie
   $-10^{4}$ oder $2^{5}$ gilt als reine Zahl (−10, 2); Potenzen
   als Ankreuzoptionen sind so nicht prüfbar, und ein Ergebnis
   „10⁷“ oder eine Hochzahl steht nie an der Ergebnisstelle.
   Umgangen mit Entscheidungen 12–14.
2. (erledigt v0.5) Prüfskript, Sperre: „^“ ist kein Rechenzeichen
   der Tokenliste, Terme mit Hochzahl zerfallen. 4^x = 256 (2024-OS-B1g) wird in
   einer aufgabe nicht gesperrt (Probe); Kastengleichungen mit
   Hochzahl ab 4 (3⁴ = …, 10⁶ = …) stehen in der Mappe als
   Unicode, in LaTeX als ^4 – kein Treffer. Die eigene Probe
   (Entscheidungen 15, 16) ersetzt das hier.
3. Katalog: sechs Erkennungsschritte wiederholen die Vorstufen der
   Ketten fast wörtlich (e1 zwei, e2 zwei, e3 zwei; Entscheidung 1).
4. Katalog: „Plus oder minus?“ steht „vor Einheit 1 und 3“, nach
   bank.md aber einmal, in e1. Vor e3 s7/s8 (Wurzel aus einem
   negativen Quadrat) fehlt er damit.
5. Katalog: Die Prüfungshöhe e3 verlangt p-q-Formel und
   Zylinderradius; beide führt die Kette nicht ein (2.4 c). s11
   (Wurzel als letzter Schritt einer Formel) bereitet die Wurzel
   vor, die p-q-Formel selbst bleibt neu.
6. Katalog: Die Zielmarke e2 nennt 2015-OS-K3b, 2016-OS-B1h und
   2017-OS-B1g als Marken, die Kettenzeile der Prüfungshöhe nicht.
   „2 je Original des Katalogs“ lässt offen, wohin sie gehören
   (hier Entscheidungen 4 und 5).
7. Katalog: e3 s2 (Taschenrechner, auf zwei Stellen runden) ist ein
   Aufwandsmerkmal vor den Strukturmerkmalen s4–s9; 2.4 b stellt
   Aufwandsmerkmale ans Ende. Übernommen, die Kette kommt aus dem
   Katalog.
8. Auftrag, Gegenprobe: „Mehrstellige Kastenzahlen kommen in keiner
   aufgabe vor“ trifft bei diesem Eintrag die 10 jeder
   Zehnerpotenz (Kasten e2). Ohne Ausnahme für den Gegenstand der
   Kette wäre Einheit 2 nicht baubar (Entscheidung 15).

## Offene Punkte

- LaTeX nicht kompiliert: \square in den Vergleichen, \sqrt[3]{…},
  \left(…\right)^0, Anzeige „6.2E7“ als Text, \kreuz mit Formeln
  und mit „zwischen $7$ und $8$“.
- Kastenzahl- und Beispielprobe von Hand (Entscheidungen 15, 16);
  gehört ins Skript (Befund 2). Seit v0.5 sperrt das Skript
  Kastengleichungen mit Hochzahl; einzelne mehrstellige
  Kastenzahlen und Beispielpotenzen wie 3⁴ allein prüft es weiter
  nicht (Probe: „Berechne $3^4$.“ ohne Befund).
- Zone f6: ob die Zone die Tasten x², √ und EXP abfragen darf
  (Katalogzeile nennt sie, 2.2 verbietet Themenbegriffe), offen.
- Prüfungshöhe e2 zu 2015-OS-K3a mit Speicherchip und Herzschlag
  statt Astronomie (anderer Kontext); ob der Stamm „Sterne“
  erhalten bleiben soll, offen.
