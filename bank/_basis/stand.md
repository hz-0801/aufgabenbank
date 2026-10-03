# Stand bank/_basis/ – Basisvorrat

Datum 2026-09-28. Auftrag „Basisvorrat und Zettel-Rezept“ (Beschlüsse
des Lehrers vom 28.09.). Grundlage: Bank-Commit 8ead8d3 (alle
Einträge), Katalog hz-0801/mathe-nachhilfe a439398
(msa/msa-katalog-basis.csv, msa/msa-katalog-gym.csv).

## Zahlen

Stand 2026-10-02 (Erweiterung, Lehrer 02.10.; Abschnitt „Erweiterung
02.10.2026“ unten):

- 64 Basis-Typen (typen.md, typen.csv): alle 62 Typen des Basisteils
  der P10 (msa-katalog-basis.csv) und die zwei GYM-Typen aus der Bank
  (Antiproportionale Zuordnung Dreisatz; Term durch Zusammenfassen
  gleichartiger Glieder vereinfachen). Vorher 41.
- 640 Aufgaben in 21 Dateien (vorher 410 in 18): 230 neu.
- `python3 werkzeuge/bank-pruef.py _basis`: 10 Abweichungen (alle eine
  Ursache: zuordnungen-basis-k2, original 2023-OS-B1a steht nicht in
  mappen/zuordnungen.md), 12 Warnungen (Ketten mit 5 oder 20 statt 10
  Varianten – gewollt, Ziel je Typ).
- `python3 werkzeuge/duplikate.py`: Abschnitt A (wortgleich) unverändert,
  keine Basiszeile darin.
- Keine Aufgabe des Vorrats steht wortgleich (aufgabe und grafik) in
  einem anderen Ordner der Bank (Abgleich über alle bank/*/*.jsonl).

Nachtrag 2026-10-02 abends (Lehrer, Basiszettel v0.7): keine
Prüfkennung „(P10 …)“ mehr in aufgabe (vorher in allen 640 Zeilen);
Bündel a)–c) in den Varianten 1, 3, 5, 7, 9 von Prozentwert berechnen,
Winkelfunktion Seitenverhältnis angeben, Wahrscheinlichkeit einstufig,
Winkel an geschnittenen Parallelen bestimmen, Zeiteinheiten umrechnen,
Arithmetisches Mittel berechnen (mit Median und Spannweite), Ergebnisse
mit sympy (assert in vorrat.py); Term zu Figur ohne Trapez, Raute,
Parallelogramm (zusammengesetzte Figuren: kein Baustein); Trigonometrische
Gleichung nur umstellen. typen.csv neu mit niveau und ab2020.
`bank-pruef.py _basis`: 0 Abweichungen, 12 Warnungen (Mengen 5/20).

Nachtrag 2026-10-03 (Auftrag „Basiszettel ins Skript“, Vorlage des
Lehrers vom 03.10., zusammenbau.py v1.5, Rezept Zettel v0.8): 777 Zeilen
(vorher 640): 78 als verfremdetes Original markiert (ist_original, Jahr
links vor der Nummer), 59 Vorstufen (a)/b) vor dem Grundfall), 72 Tipps;
Prüfungsverb vorn statt Frage; Ankreuzen A–D mit Buchstabe als Lösung;
„U“ statt „u“. Abgleich Vorlage ↔ v1.4: bau/zettel/abgleich-2026-10-03.md.
`bank-pruef.py _basis`: 0 Abweichungen, 52 Warnungen (Mengen je Kette).
Offen: Kern nach der 30-%-Regel sind nur 5 Typen; --schwach nimmt zwei
weitere dazu und meldet es (GEGENPROBE VERLETZT).

Nachtrag 2026-10-03 abends (Befunde des Lehrers, zusammenbau.py v1.6,
Rezept Zettel v0.9): 784 Zeilen (Bestand 640, Originale 78, Vorstufen 66
statt 59). Neue Vorstufen (7, alle mit `\rwbei` im Dreieck, γ an der
Spitze): Winkelfunktion Seitenverhältnis angeben 3 (a) Hypotenuse und
Gegen- bzw. Ankathete zu γ, Antwort zwei Buchstaben; b) sin γ bzw.
cos γ), Pythagoras Gleichung zuordnen 2 und Satz des Pythagoras
formulieren 2 (a) Hypotenuse benennen; b) Gleichung). Rechter Winkel
jetzt auch in den zehn Bestandsaufgaben der Winkelfunktion markiert
(`\rwbei`); dort, wo nach γ gefragt ist, steht C an der Spitze (vorher
stand das Label γ auf der Seite). Tipps: 36 statt 72 – die 37 Tipps an
Vorstufen entfallen (Vorstufe statt Tipp), 15 Regeln wurden zu ersten
Schritten („10 % heißt: durch 10 teilen.“ → „Rechne erst 10 %, dann
mal 3.“; „Ein Produkt ist 0, wenn ein Faktor 0 ist.“ → „Setze zuerst
die Klammer gleich 0.“), 20 blieben, einer kam dazu (Ankreuzen 20 %
Rabatt). Typen für schwach (Übergang bis zur Entscheidung des Lehrers):
17 Typen mit ab2020 ≥ 2; die 30-%-Kernregel steht nur noch als HINWEIS
im Log. Nicht markiert: das Trapez mit zwei rechten Winkeln
(Symmetrieachsen, k3-v7) – `\viereck` kann keinen rechten Winkel
markieren (Vorlage). `bank-pruef.py _basis`: 0 Abweichungen, 52
Warnungen.

## Dateien

    typen.py      bestimmt die Basis-Typen, schreibt typen.csv/typen.md
    typen.csv     je Typ: thema, jahrgaenge, Originale, eintrag,
                  jüngstes Original, einheit, quelle, kette_nr
    vorrat.py     die Aufgaben je Typ (von Hand geschrieben, Zahlen und
                  Kontexte im Skript), schreibt <eintrag>.jsonl
    <eintrag>.jsonl  je Basis-Typ des Eintrags zehn Zeilen

Neu bauen: `python3 bank/_basis/typen.py` (braucht mathe-nachhilfe
neben dem Repo), dann `python3 bank/_basis/vorrat.py`, dann die
Prüfung. Die jsonl nicht von Hand ändern, sondern vorrat.py.

## Entscheidungen (vom Auftrag nicht geregelt)

1. Datei je Typ: der Eintrag, in dem das jüngste Original des Typs als
   Prüfungshöhe steht; steht es in mehreren, der mit den meisten
   Originalen des Typs, dann alphabetisch (z. B. „Zahlen in
   verschiedenen Darstellungen vergleichen“ → brueche-dezimalzahlen,
   2023-OS-B1f steht auch in bruchrechnung).
2. Jüngstes Original: höchstes Jahr, bei gleichem Jahr FOR vor EBR vor
   OS vor GYM (nur FOR-Originale 2026 liegen in der Bank).
3. Felder: id `<eintrag>-basis-k<k>-v<v>`; einheit und quelle aus der
   Bankzeile des jüngsten Originals; kette = sprosse_text = Typname;
   kette_nr je Datei alphabetisch nach Typ; merkmal „Basisaufgabe in
   Prüfungsform, ohne Rechner“; loesungsgrafik "".
4. Prüfkennung im Text in der langen Form der Bank („(P10 2026 FOR)“);
   die Kurzform („(P26F)“) setzt zusammenbau.py v0.5 beim Bau.
5. Form wie im Original, mit drei Abweichungen fürs Kopfrechnen und
   die Zettelseite: „Lineare Gleichung lösen“ und „Trigonometrische
   Gleichung nach Seite umstellen“ als teil mit Feld „x = __“ (Original
   Kurzantwort; die Bank führt sie als gleichungsraster);
   „Antiproportionale Zuordnung Dreisatz“ als teil (Original
   Kurzantwort, Bank dreisatz). „Kreissektor Anteil berechnen“ mit
   glatten Winkeln (18°–270°) statt 145° mit Rundung: ohne Rechner.
6. Grafik nur, wo Original oder Bankzeile eine haben: Figuren
   (Bruchteil einer Fläche, Symmetrieachsen, Parallelen, Parallelogramm,
   Dreieck bei Winkelfunktion, Kreissektor), Koordinatensysteme,
   Würfelnetz (Buchstabenraster wie in der Bank), Wertetabellen. Ohne
   Grafik, wie in den Bankzeilen: Gleichschenkliges Dreieck,
   Rechteckseite, Figur nach Spiegelung (Text beschreibt die Lage).
   Symmetrieachsen: regelmäßiges Fünfeck und Halbkreis ohne Grafik (kein
   Baustein).
7. Wertetabellen in grafik, nicht im Aufgabentext (\wertetabelle endet
   mit \par, ein folgendes \\ bricht den Satz ab).
8. Labels in Koordinatensystemen: vorrat.py rückt Labels von Geraden
   und Funktionen, die näher als 1,8 Einheiten beieinander oder an der
   Achsenbeschriftung stehen, über das optionale [x] auseinander.
9. „Zahl zu Bedingung angeben“: pruef ist ein Beispiel, die Lösung
   nennt es mit „z. B.“ und den ganzen Bereich.
10. „Uhrzeit aus Startzeit und Dauer berechnen“: pruef wie in der Bank
    die Stunden (Zwischen- und Endzeit), die Minuten stehen im Text.

## Befunde

- Zwei Bankzeilen quadratische-funktionen e1 (Original 2026-FOR-B1e)
  setzen `\wertetabelle … \\` im Aufgabentext; das bricht beim
  Kompilieren („There's no line here to end“). Nicht geändert (Ordner
  nicht in diesem Auftrag).
- Der Katalog führt keinen Basis-Typ in allen 13 Jahrgängen; der
  häufigste („Bruchteil einer Fläche bestimmen“) hat 9.
- 23 der 62 Typen aus msa-katalog-basis.csv haben in der Bank kein
  Original als Prüfungshöhe und fehlen daher im Vorrat, darunter
  häufige: Term zu Figur angeben (5 Jahrgänge), Pythagoras Gleichung
  zuordnen (5), Arithmetisches Mittel berechnen, Zeiteinheiten
  umrechnen, Proportionale Zuordnung Dreisatz (je 3), Median bestimmen,
  Scheitelpunkt ablesen. Wer den Vorrat erweitern will, braucht zuerst
  diese Originale in der Bank (die Einträge daten, pythagoras,
  quadratische-funktionen u. a. führen sie bisher nicht als
  Prüfungshöhe).

## Erweiterung 02.10.2026

Auftrag des Lehrers vom 02.10.: Basisvorrat auf alle Basistypen der P10;
Ziel je Typ 20, 10 oder 5 Aufgaben (nach Jahrgängen), 250 Aufgaben für
die 25 Zieltypen (23 neu, zwei aufgestockt: Bruchteil einer Fläche
bestimmen und Lineare Gleichung lösen von 10 auf 20).

Entscheidungen:

1. Typenmenge: Typen aus msa-katalog-basis.csv (62) plus die Typen der
   Basisteil-Originale in der Bank; die zwei GYM-Typen bleiben (ihr
   Vorrat wird nicht gelöscht), daher 64 statt 62.
2. Eintrag eines neuen Typs: der Katalogeintrag, der sein Thema trägt
   (themen.csv, Profil msa; „Zählen und Kombinatorik“ →
   wahrscheinlichkeit, „Kenngrößen“ → daten). einheit von Hand nach den
   Einheiten des Katalogeintrags (NEU_EINHEIT in typen.py), quelle = die
   häufigste quelle der Bankzeilen dieser Einheit.
3. Original jedes Typs: das jüngste Basisteil-Original des Typs, das in
   der Mappe des Eintrags steht. Damit wechseln zwei Bestandstypen auf
   ein jüngeres Original (Wahrscheinlichkeit einstufig 2014-OS-B1d →
   2016-OS-B1f; Winkel an geschnittenen Parallelen bestimmen 2015-OS-B1d
   → 2020-OS-B1g). Ausnahme: Proportionale Zuordnung Dreisatz – keines
   seiner Originale steht in einer Mappe; original = 2023-OS-B1a, das
   Prüfskript meldet es, bis katalog/zuordnungen.md (mathe-nachhilfe)
   die Kennung nennt und die Mappe neu gebaut ist.
4. kette_nr der vorhandenen Typen bleibt (ids des Vorrats stabil); neue
   Typen hängen sich je Eintrag alphabetisch an. typen.py liest dazu die
   alte typen.csv.
5. Neu gerechnet: quelle (und bei den zwei Terme-Typen einheit) der
   Bestandstypen nach dem heutigen Stand der Bank – Folge der
   Katalogänderungen seit 28.09., nicht von Hand gesetzt.
6. Aufstockung: v11–v20 an die zehn vorhandenen Varianten angehängt;
   Bruchteil einer Fläche als Kurzantwort zu einer Figur (Bruch oder
   Prozent) statt Ankreuzen über vier Figuren.
7. Term zu Figur angeben: Kurzantwort mit Zahlfaktor (z. B. u = 4 · d)
   trägt den Faktor als pruef. Größen vergleichen: Form teil, Werte in
   aufgabe und antwort („0,3 l __ 30 ml“).
8. Grafiken mit den Bausteinen der Sty: \rechteck, \parallelogramm,
   \trapez, \raute (Schlüssel seiten, hoehe, diagonalen), \dreieckrw,
   \dreieck, \geradenkreuzung, \bruchrechteck, \bruchkreis, \netzquader,
   \netzzylinder, \netzpyramide, \netzwuerfel, \kegel, \parabel im ksys.
9. Probe: `zusammenbau.py --zettel basis --nummer 11 --ohne-register`
   (Kennung BAS-Z0), xelatex: 2 Seiten (Aufgaben, Lösungen), Grafiken
   erscheinen; Probe-PDF nicht im Repo.
