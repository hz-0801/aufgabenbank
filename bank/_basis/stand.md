# Stand bank/_basis/ – Basisvorrat

Datum 2026-09-28. Auftrag „Basisvorrat und Zettel-Rezept“ (Beschlüsse
des Lehrers vom 28.09.). Grundlage: Bank-Commit 8ead8d3 (alle
Einträge), Katalog hz-0801/mathe-nachhilfe a439398
(msa/msa-katalog-basis.csv, msa/msa-katalog-gym.csv).

## Zahlen

- 41 Basis-Typen (typen.md, typen.csv), 410 Aufgaben in 18 Dateien.
- `python3 werkzeuge/bank-pruef.py _basis` (v0.6): 0 Abweichungen,
  0 Warnungen.
- Keine Aufgabe des Vorrats steht wortgleich (aufgabe und grafik) in
  einem anderen Ordner der Bank (Abgleich über alle bank/*/*.jsonl).

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
