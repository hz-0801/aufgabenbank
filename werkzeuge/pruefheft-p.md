# pruefheft.py – Art p: Prüfungsblatt der Sorte P aus Daten (v0.8, 12.10.2026; Datenfelder 12.10.)

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
## Datenfelder (seit 12.10., Lauf AZL Körper; fehlen sie, steht „% SETZER: fehlt – …“ im TeX)
- Gliederung `msa/gliederung/<kapitel>.md`, Kopf: `Anzeigenamen: <Zuschnitt> =
  <Name in Schülersprache> | …` (mehrere Zeilen erlaubt; fehlt der Name, gilt
  der Zuschnitt). Je Stufe unter `### <Stufe>`:
  `- **Anzeigename:** …` (Stufenkopf, Stufenzeile, Übersicht, Lösung; fehlt er,
  der Stufenname), `- **Schülerfrage:** …` (Frage ohne Rechnen, erste Nummer der
  Stufe), `- **Schülerfrage-Fälle:** <Lage> = <Antwort> | …` (a, b, c …
  untereinander, Lücke an derselben Stelle), `- **Schülerfrage-Form:** linie`
  | `linie:<Nachsatz>` (z. B. `-mal so groß`) | `kreuz:<Label>` (Kästchen je
  Fall, Antwort ja/nein; Lösung nennt die Fälle mit ja),
  `- **Schülerfrage-Weg:** …` (rechte Spalte der Lösung; steht im Fuß, wenn die
  Antworten länger als 60 Zeichen sind).
- `msa/mehr-p10.csv`, Spalten `grafik` (TikZ-Baustein der Vorlage oder freies
  TikZ, Skizze zu den neuen Zahlen; ersetzt den Text aus `abbildung`) und
  `form`: `text` (Karo), `teil` (Antwortlinie rechts in der Zeile, Einheit aus
  `loesung`), `skizze` (Skizzenfeld: links „Skizze“, rechts Karo), leer = wie
  bisher; `ankreuzen` kommt aus dem Wortlaut („Kreuze … an: a / b“).
- Lösung: beginnt `loesung` mit ja/nein/richtig/falsch/stimmt, ist das Urteil
  das Ergebnis; sonst „Name op Wert“ der letzten Gleichung (Name nur bis 20
  Zeichen); Klammern mit Zahl bleiben Rechnung, ohne Zahl sind sie Vermerk.
- Satz (nur Art p): `\pfstufekopf` ohne die 14 Zeilen Vorhalt der Vorlage, der
  Setzer fordert 0,16 Seitenhöhe vor dem Kopf; Aufgabenabstand 5 pt; kleinerer
  Karo (0,75, 0,5) auch, wenn das Blatt über zwei Seiten geht und der kleinere
  Karo Seiten spart.
- Noch offen: herausgelöste Fassung mit anderen Zahlen (Spalte `herausgeloest`
  oder h-Zeile); Makrowunsch `\winkelbei{V}{P}{Q}{Label}`, graues Teildreieck
  (mathblatt.sty unverändert).
## Ergänzt im Lauf EF4 (Netz und Schrägbild, 12.10.; Zeichen-Aufgaben)
- Gliederung je Stufe: `- **Frage:** „…“` = kurze Schülerfrage kursiv unter
  dem Stufenkopf (Blatt und Lösung), wo die Stufe keine Frage mit Fällen hat.
- `grafik`: „||“ trennt Bildoptionen zum Ankreuzen (Reihe, Buchstabe und
  Kästchen darunter; Lösung nennt den Buchstaben).
- `form` als Folge von Teilen mit „+“ in Blattfolge: `ankreuzen` (Text-
  optionen aus dem Wortlaut rechts neben der Grafik, oder Bildoptionen),
  `einzeichnen` (die Grafik ist das Antwortfeld, kein Karo), `zeichnen`
  (Grafik links, Karo rechts, 4 Zeilen), `teil` (je Ergebnis „Name = ___“),
  `karo` (gerechnete Teile + 1, mindestens 2). Der Satz nach der letzten
  Option („Begründe deine Wahl.“) steht vor dem Karo. `teil`, `skizze` und
  `grafik` allein gehen den Weg oben.
- `loesung`: Teil mit „(dritte Option)“ → Ergebnis ist der Buchstabe.
- Bank-Einstieg mit `form` zeichnen oder Grafik `\rechenplatz{n}`: Karo über
  die volle Breite (n Zeilen, höchstens 5).
- Noch offen: Anzeigename der Einheit (Kopfzeile `Anzeigenamen:` oben).
- Nachzug 12.10. (H37 Flächen): Einstieg nur aus der ersten Sprosse in
  bank_sprossen (Lernfolge; bis dahin niedrigste Höhe über alle Sprossen);
  liegt sie auf Prüfungshöhe, entfällt der Einstieg (die Bank ergänzt nur
  unten, plan.md Linie 4) – im TeX „% Einstieg entfällt“. `form` zusätzlich
  `linie` (Gleichung angeben: „A = ____“ rechts). Ankreuzen neben einer
  Skizze: eine Option je Zeile (`\gkreuzzeile`). Antwortfeld des Einstiegs
  ungeteilt (`\mbox`). Lösung: Klammern mit Operator sind Term („(b + c)“),
  nur Klammern ohne Zahl und Operator sind Vermerk; Doppelpunkt trennt nur
  direkt nach einem Wort („Nein: …“), „d · e : 2“ bleibt Geteiltzeichen.
## Nachzug 12.10. (H37 Flächen, zweite Fassung; pruefung.md § 5 „Eigene Aufgaben sparsam“)
- Gliederung je Stufe: `- **Einstieg:** nein` sperrt den Bank-Einstieg der Stufe
  (im TeX „% kein Einstieg: Gliederung …“). Ohne Schülerfrage/Frage oder ohne
  Bankzeile setzt Art p nichts und meldet nichts mehr („SETZER: fehlt“ entfällt
  dafür) – ein Einstieg nur, wo die Stufe ihn braucht.
- `Schülerfrage-Fälle`: Trenner „→“ statt „=“, wenn die Lage selbst ein „=“
  trägt („Rechteck: A = a · b, nach a umgestellt → a = A : b“). Ein einziger
  Fall steht ohne Buchstaben (Blatt und Lösung).
## Nachzug 12.10. (H37 Flächen, dritte Fassung; pruefung.md § 5 vom 12.10., mathblatt.sty 2026-10-12)
- Blatt = alle Originale der letzten fünf Jahre: je Stufe die Zeilen aus mehr-p10.csv
  (Stufe im Kapitel, dazu Zeilen anderer Kapitel, deren Original hier in katalog_ids
  steht, z. B. 2023-OS-K5c aus prozent) mit auf_blatt = ja, leicht → schwer (schwere,
  rang). auf_blatt bleibt die Angabe der Daten (ja = Jahr in den letzten fünf, sonst
  nein); weicht sie von der Jahresregel ab, meldet der Setzer „Hinweis: …“, ebenso,
  wenn die schwerste echte nicht am Ende des Blatts steht (kein Abbruch).
- Marke mit B: Basisaufgaben (Katalog block Basis bzw. id …-B…) „’25 · B1e“, einmal im
  Blattkopf rechts „B = Basisteil, ohne Taschenrechner“ (\pfheftkopf[…]); Kontext-
  aufgaben wie bisher „nach P10 ’23 · 2c“. Stern wie im Katalog.
- Einstieg nur aus der Gliederung (Schülerfrage, -Fälle, -Form, -Weg, -Skizze; oder
  Frage), nie aus der Bank; bank_sprossen und `Einstieg: nein` sind für Art p ohne
  Wirkung (Register: bank= leer). Neu `- **Schülerfrage-Skizze:** original` = die
  Figur (grafik) des ersten Originals der Stufe links, die Fälle rechts untereinander;
  sonst eigenes TikZ.
- Jahre im Stufenkopf aus allen Daten (Katalogjahre der katalog_ids, ohne Hauptplatz
  jahre_letzte5): `\pfjahre{25 · 24 · 23 · 22}{19 · 16}` – zweistellig, jüngstes
  zuerst, ältere als fünf Jahre nach dem Strich und heller; ohne Jahr „–“. Der
  Stufenkopf ist der der Vorlage (Linie, Abstand, 13 pt); der Setzer setzt nur
  `\mbpfstufevorhalt` auf 0 pt und fordert 0,16 Seitenhöhe vor dem Kopf.
