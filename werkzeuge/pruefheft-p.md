# pruefheft.py – Art p: Prüfungsblatt der Sorte P aus Daten (v0.6, 11.10.2026)

    python3 werkzeuge/pruefheft.py --kapitel dreiecke --art p \
        --einheit "Winkel ohne Rechnung bestimmen oder begründen"

Ausgabe: `bau/pruefheft/<kapitel>-p-<einheit-kurz>-<datum>/` (`src/`, `pdf/`:
1-uebersicht, 2-blatt, 3-loesungen), Zeile in bau/register.csv (Rezept P).
Regeln: pruefung.md § 5, gemeinsam.md „Satz“, „Lösungen“, „Übersicht und
Serie“. Muster (Hand-Satz T2U): bau/pruefung/2026-10-11/winkel-ohne-rechnung/.

Daten (nur gelesen): gliederung/<kapitel>.md (Name, Folge, Gruppen, Zuschnitt
je Stufe = Einheit), zuordnung-<kapitel>.csv (Stufen, katalog_ids, bank_sprossen,
jahre_letzte5), msa-katalog-*.csv (Jahr, Papier, Stern), mehr-p10.csv (echte
mit anderen Zahlen: auf_blatt = ja, stufe, schwere, rang, abbildung, loesung),
herausgeloest-p10.csv (nur Vermerk im TeX), bank/<eintrag>/*.jsonl (Einstieg:
leichteste Zeile der ersten Sprosse in bank_sprossen, ruhende nie).

Form je Stufe: Stufenkopf mit Jahren der Hauptplätze aus den letzten fünf (ohne
Hauptplatz: jahre_letzte5), Einstieg aus der Bank, echte nach Schwere und rang
(schwerste am Ende), Marke „nach P10 ’yy · 6a“ mit Stern (Katalog stern = ja
oder FOR ohne EBR-Zwilling), Skizze als Text kursiv links, Karo rechts.
Blattende: Fundstellentabelle (jüngstes Jahr … −10, „26 FOR“/„26 EBR“ bei
Kursheften, alle Originale der Einheit), Ausschnitt Vorher/▸/Weiter. Karo voll;
steht die Tabelle allein auf einer Seite, Faktor 0,75, 0,5. Lösung: Stufenköpfe
wortgleich, Nummer-/Buchstabenspalte, links Ergebnis oder Urteil, rechts Weg.

## Vergleich mit dem Muster T2U (Winkel)
gleich: Kopf mit Sorte und Kennung, Titel, graue Stufenzeile, Stufenköpfe
  mit Jahren (2026 · 2023 · 2022 / 2023 / 2025), Einstieg → echte → schwerste,
  Marken mit Fundstelle und Stern (’25 · 2c ⋆), Skizze links / Karo rechts,
  Fuß kopfüber mit Ergebnissen, Fundstellentabelle (26 FOR … 16, 1i 2c – 1g
  2a 7a 5c 1i – – 4b 4a –), Ausschnitt, Lösung mit Stufenköpfen und Spalten,
  Übersicht mit Gruppen, ▸ fett mit Stufen, Rand grau, „Weiter: Flächen“.
anders: Stufen- und Blattnamen wie in Gliederung/Zuordnung („Winkelsumme“
  statt „Innenwinkelsumme“, Zuschnitt statt „Winkel“); eine Einstiegsaufgabe
  je Stufe (Muster: Päckchen a/b aus zwei Sprossen); echte Aufgaben mit den
  Zahlen aus mehr-p10.csv und ganzem Vorspann (Muster: herausgelöst, Original-
  zahlen); Skizzen als Text (Muster: TikZ); Sinussatz unter „Rechtwinklige
  Dreiecke“ (Bank trigonometrie), Vierecke vor Winkel (Zuordnungsfolge);
  Blatt 2 statt 3 Seiten (Karo 0,75).
fehlt: Stufe „Winkelbeziehungen“ ohne Hauptplatz (nur im Muster), Schüler-
  frage je Stufe, Antwortlinien statt Karo bei Angeben-Aufgaben (Nr. 7 Muster),
  TikZ-Skizzen, Lückentext.

## Datenbedarf (im TeX als „% SETZER: fehlt – …“)
- Skizze als Grafik: Feld `grafik` (Bausteinaufruf wie Bank) in mehr-p10.csv;
  Prosa in `abbildung` reicht nur für den Text.
- Schülerfrage je Stufe: Spalte in der Zuordnung oder Zeile in der Gliederung.
- Anzeigenamen in Schülersprache für Stufe und Einheit (Übersicht, Köpfe).
- Herausgelöste Fassung mit anderen Zahlen (mehr-p10.csv trägt den ganzen
  Vorspann): Spalte `herausgeloest` oder h-Zeile mit neuen Zahlen.
- Antwortform je echter Aufgabe (Linie, Tabelle, Karo): Spalte `form` wie Bank.
- Makrowunsch (mathblatt.sty unverändert): `\winkelbei{V}{P}{Q}{Label}`, graues
  Teildreieck – erst sinnvoll, wenn `grafik` da ist.
