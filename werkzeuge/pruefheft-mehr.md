# pruefheft.py – Art „mehr“ (v0.5, 11.10.2026)

Setzt den Mehr-Block der Prüfung P10 (mathe-nachhilfe pruefung.md § 5
„Mehr-Block“) ohne Modell aus `mathe-nachhilfe/msa/mehr-p10.csv`.

    python3 werkzeuge/pruefheft.py --kapitel dreiecke --art mehr \
        --einheit "Seite oder Winkel mit sin, cos, tan" --portion 1 [--schueler S07]

- `--einheit`: Spalte `einheit`, genau oder ein eindeutiger Teil
  („sin, cos, tan“); bei Mehrdeutigkeit nennt das Skript die Einheiten.
- `--portion n`: welche Portion (Vorgabe 1); das Skript sagt, wie viele
  es gibt, und zeigt alle Portionen mit Schwere je Aufgabe.
- `--schueler`: nur ein Vermerk im Register (Nummer, nie Name).
- `--ohne-register`, `--aus`, `--datum`, `--mn`, `--bb` wie bisher.

Regel im Skript: nur Zeilen der Einheit mit `auf_blatt = nein`, Ordnung
`rang`. Portionen zu 6–8 Aufgaben, gleich groß: Stufen von schwer nach
leicht (III, II, I), darin nach rang, reihum auf die Portionen verteilt.
In der Portion reihum I, II, III, …; die schwerste Aufgabe der Portion
steht am Ende. Fehlen Stufen, nimmt die Portion, was da ist. Schwere
außerhalb I–III zählt als II.

Satz (Form wie bau/pruefung/2026-10-11/winkel-ohne-rechnung, Sorte P):
Laufkopf „P10 · mehr“, Einheit, „Portion n von N“, graue Stufenzeile;
je Aufgabe `pfaufg` mit Randmarke aus `marke` und Teilaufgabe aus
`quelle`; Abbildung als Text kursiv („Skizze: …“), keine Grafik.
Antwortraum: Ankreuzen (`Kreuze … an: a / b / c`) als `\pfkreuz` A–C,
Lücke `___` als Linie, Lösung ohne Zahl als Antwortfeld rechts, sonst
Karo mit Schritten der Lösung + 1 (höchstens 8). Fuß mit Ergebnis.
Lösungsblatt in `pfloesungb`/`\lzb`: Ergebnis (letzte Gleichung des
letzten Schritts, beim Ankreuzen der Buchstabe) und Weg aus `loesung`.

Seiten: Ziel eine Seite; passt es nicht, wird der Rechenraum auf 3/4
und 1/2 verkleinert; reicht auch das nicht, bleibt der volle Rechenraum
auf zwei Seiten (ein Blatt). Das Skript meldet es.

Ausgabe: `bau/pruefheft/<kapitel>-mehr-<einheit-kurz>-p<n>-<datum>/`
(src/, pdf/), Kennung wie bei G1 (drei Zeichen), eine Zeile in
`bau/register.csv` (Rezept PH, Bestellung mit ids und Schwere-Folge).
Die Daten in mathe-nachhilfe werden nur gelesen.
