# pruefheft.py – Art p: Prüfungsblatt der Sorte P aus Daten (v0.11, 13.10.2026; Datenfelder 12.10.)

v0.11 (Runde 7, Lehrer 13.10.): Marke wie im Heft „’25 · 1f“ (ohne B); rechts
„Basis“ als Wort, daneben „FOR“ und das durchgestrichene TR. `--pruefungsjahr`
(Vorgabe 2027): ab 2028 (hilfsmittelfreier Teil, 10 BE, Fachbrief 10) tragen
alle Basisaufgaben `\pfohnetr`, und der Kopf nennt „Prüfung 2028 · Basisteil
ohne TR“; davor nur Originale mit hilfsmittel = nein, kein Jahr. Hinweis auf
die Formelsammlung einmal je Blatt: der erste in Blattfolge (Frage unter dem
Kopf, Formel-Frage, Schülerfrage mit „Formelsammlung“ oder „Seite ___“) bleibt,
spätere entfallen (Hinweis im Lauf). Antwortzeilen je Größe (unten). Leere
Stufe aus älteren Originalen (unten). Gemischt-Abschnitt (unten).

v0.10 (Runde 6, Lehrer 13.10.): Bedingungen rechts = TR durchgestrichen
(`\pfohnetr`, nur bei Katalog hilfsmittel = nein, keine Annahme über 2028)
und „FOR“, kein „Basis“, keine Legende. Stufenkopf: steht in der
Gliederung unter der Stufe „- **Häufigkeit:** fast immer“ (oder „immer“),
nur dieses Wort; sonst nur die Jahre (nur P10-Hefte OS, EBR, FOR,
MUSTER-*), kein „oft“/„selten“. Figur links, Antwort direkt daneben
(Spalte so breit wie die Figur); Skizzenfeld als Karo ab dem linken Rand
mit „Skizze“ oben links. Teile desselben Originals direkt nacheinander:
eine Nummer, Vorspann einmal, a) b); „Angaben wie in Nr. k“ nur getrennt.
Bündel nebeneinander nur, wenn jedes System in seine Spalte passt (sonst
untereinander, nie verkleinert).

    python3 werkzeuge/pruefheft.py --kapitel dreiecke --art p \
        --einheit "Winkel ohne Rechnung bestimmen oder begründen"

Ausgabe: `bau/pruefheft/<kapitel>-p-<einheit-kurz>-<datum>/` (`src/`, `pdf/`:
1-uebersicht, 2-blatt, 3-loesungen), Zeile in bau/register.csv (Rezept P, mit
`fassung=`), neue Fassung in bau/fassungen.csv (v0.9, unten).
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
(schwerste am Ende), Marke „nach P10 ’yy · 6a“ (seit v0.9 ohne Stern; Bedingungen
rechts, unten), Skizze als Text kursiv links, Karo rechts.
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
## Nachzug 12.10. (QGC Lineare, ein Blatt mit drei Stufen)
- `form`-Teile: `bilder` (Bildoptionen A–D aus `grafik` mit „||“, Buchstabe
  ohne Kästchen, Antwort über `teil`: „Angebot 1 = ___“), `wahrfalsch`
  (Aussagen aus „Entscheide, ob die Aussagen wahr oder falsch sind: … / …“,
  je Zeile „(1) Aussage  wahr □ falsch □“; der Satz nach der letzten Aussage
  steht vor dem nächsten Teil), `linie` auch als Teil („y = ____“, letzter
  Lösungsteil mit „=“). Bildreihe: Breite je Bild nach ihrer Zahl
  (`\gbildbreite`, vier Bilder 0,24).
- Koordinatensystem als `grafik`: `\begin{ksys}[xmin=…,karo=0.35]…\end{ksys}`
  der Vorlage; Fenster nach pruefung.md § 5 „Andere Zahlen“ (Schnittpunkte
  im Bild). Sechs Systeme je Blatt geben mit 15 Nummern 4 Seiten.
- Bau gibt je Karo-Faktor die Probeseitenzahl aus („Probe: Faktor …“).
## Nachzug 12.10. (XU6 Quadratische, Parabel: Scheitelpunkt und Skizze; pruefheft.py 8a93a1c)
- Eine Stufe der Gliederung ohne Original der letzten fünf Jahre (und ohne Zeile mit
  auf_blatt = ja) entfällt auf dem Blatt; der Setzer meldet „Hinweis: Stufe … entfällt
  auf dem Blatt“ und zählt sie nicht in `stufen=` (Register). Ihre Originale bleiben im
  Mehr-Block (hier „Punkt auf der Parabel prüfen“, 2024-OS-K3c Hauptplatz in lineare).
- Stufenkopf bleibt bei der ersten Aufgabe der Stufe (`\gkopfvor`), kein Kopf allein am
  Seitenende.
- `loesung`: „ | “ trennt Teilfragen („S(4|−3) | p(x) = (x − 4)² − 3“), ebenso `pruef`;
  „p(x) =“ bleibt in der Lösung stehen (kein Vermerk), nur „(x)“ ohne Gleichung wird
  gestrichen. `grafik` mit `||` setzt mehrere Bausteine nebeneinander (Wertetabellen
  zum Ankreuzen, A/B/C darunter). Koordinatensystem: `\begin{ksys}[xmin,xmax,ymin,
  ymax,karo=0.5]\parabel{a}{xs}{ys}{p}\end{ksys}`; Fenster je Zahlenwahl, Scheitel
  ganzzahlig wie im Original.
- Nachzug 12.10. (TAL Lineare, zweite Fassung): folgen zwei Nummern derselben
  Original-Aufgabe aufeinander (eltern_id bis auf den Buchstaben gleich), setzt
  der Setzer bei der zweiten statt des gemeinsamen Vorspanns (ganze Sätze,
  ≥ 40 Zeichen) „Angaben wie in Nr. k.“ – eine Zahlenwahl je Aufgabe
  (pruefung.md § 5 „Andere Zahlen“); im TeX „% Vorspann wie Nr. k“. Dafür den
  rang so setzen, dass die Teile nacheinander stehen.
## v0.9 (12.10., Festlegungen des Lehrers vom 12.10.; pruefung.md § 5, gemeinsam.md „Satz“, „Kennung mit Fassung“)
- **Bedingungen rechts:** am rechten Rand jeder echten Aufgabe klein grau, auf der Zeile der
  Nummer, „Basis · ohne TR“, „FOR“ oder beides (`pfaufg` drittes Argument, `\gbedrand`). Aus
  dem Katalog: block Basis (id …-B…) → „Basis · ohne TR“ (Regel `P_OHNE_TR_BLOCK` im Setzer:
  ab 2028 ist der Basisteil hilfsmittelfrei; ändert sich das, eine Zeile), hilfsmittel =
  nein → „ohne TR“; stern = ja oder FOR-Heft ohne EBR-Zwilling (`stern_fuer`) → „FOR“. Der
  Stern an der Marke entfällt; Basisaufgaben „’25 · B1e“, Kontext „nach P10 ’23 · 2c“.
- **Häufigkeitswort im Stufenkopf** vor den Jahren: Zahl der letzten fünf Prüfungsjahre mit
  der Stufe (dieselben Jahre wie bisher) – 4–5 „immer“, 2–3 „oft“, 0–1 „selten“. Bei „immer“
  nur die jungen Jahre, sonst auch die älteren nach dem Strich („selten · 26 | 14“).
- **Gleichartige Originale gebündelt – neue Spalte `buendel` in msa/mehr-p10.csv:**
  `<schlüssel>` oder `<schlüssel>: <gemeinsamer Auftrag>`. Zeilen derselben Stufe mit
  gleichem Schlüssel werden eine Nummer mit a), b) am Platz des ersten Glieds (rang); je
  Glied Marke links und Bedingungen rechts auf der Zeile des Buchstabens. Der gemeinsame
  Auftrag steht einmal oben und ersetzt in jedem Glied den Satz, der mit demselben Wort
  beginnt („Zeichne …“); ohne Auftrag stehen die gleichen Anfangssätze oben. Haben alle
  Glieder (höchstens drei) ein Koordinatensystem in `grafik`, stehen sie nebeneinander, je
  eigenes kleines System, kein Karo (Antwortlinie „p(x) = ___“ je Gleichung der Lösung);
  sonst untereinander. Lösung: „5. a) …“, „b) …“; Fuß „5: a) … ; b) …“. Leer = kein Bündel.
  Kennzeichnen (Schlüssel vergeben) machen die Bau-Agenten: nur Originale, die sich allein
  in den Zahlen unterscheiden (pruefung.md § 5).
- **Kein Karo bei „Zeichne“:** steht im Wortlaut „Zeichne/Skizziere“ und ist `grafik` ein
  Koordinatensystem (`{ksys}`), ist das System das Antwortfeld (form `zeichnen` oder leer);
  Karo nur, wo gerechnet wird. Breite höchstens die Spalte (`\gpassend`).
- **Zweitthema ausblenden – neue Spalten `wortlaut_einheit`, `loesung_einheit`,
  `pruef_einheit`, `grafik_einheit`, `form_einheit` in msa/mehr-p10.csv:** gefüllt ersetzen
  sie auf dem Einheitsblatt das gleichnamige Feld (fremder Teil weggelassen,
  Zwischenergebnis im Wortlaut gegeben, z. B. „… ist y = 4 gegeben (aus der Parabel)“);
  leer = wie bisher. Die ungekürzte Zeile bleibt für das Gemischt-Blatt und den Mehr-Block.
  Im TeX „% Zweitthema ausgeblendet“. `pruef_einheit` prüft `loesung_einheit` (mehr-pruef.py
  kennt die neuen Spalten noch nicht – beim ersten Füllen nachziehen).
- **Kennung mit Fassung:** Kennung fest je Einheit im Kopf der Gliederung
  `msa/gliederung/<kapitel>.md`: `Kennung: <Zuschnitt> = XYZ` (eine Zeile je Einheit, alle
  P10-Einheiten seit 12.10.); fehlt sie, Ersatz nach Ordner mit Hinweis. Auf dem Blatt
  Kennung und Fassung ohne Trenner (TAL1, Kopf rechts). Fassung aus `bau/fassungen.csv`
  (`kennung;fassung;fingerabdruck;datum;kapitel;einheit;pfad;bemerkung`): Fingerabdruck der
  Daten der Einheit (je Stufe Anzeigename, Jahre, Fragen der Gliederung; je echte Zeile
  wortlaut, abbildung, grafik, form, loesung, schwere, rang, buendel, *_einheit und die
  Katalogfelder jahr, papier, block, hilfsmittel, stern). Gleicher Abdruck = Nachdruck,
  gleiche Fassung; anderer = nächste Fassung, neue Zeile. Satz des Setzers zählt nicht. Kein
  Baudatum auf dem Blatt. `--fassung-erfassen` schreibt den heutigen Datenstand als
  Fassung 1, ohne zu setzen (so erfasst: AZL, EF4, Y5D, XU6, TAL aus dem Datenstand ihrer
  Lieferung; P4Z, GYW, LXA, T2U, NUB als Handsatz ohne Abdruck – ihr erster Satz aus Daten
  wird Fassung 2). Register: `fassung=` in der Bestellung; Lieferliste: `lieferung.py
  --kennung TAL1` (Kennung mit Fassung).
- **Formel-Frage einmal je Blatt:** bei der ersten Stufe, deren Original im Katalog
  (verfahren) eine Formel hat (rechts π, √, sin/cos/tan oder eine Größe als Buchstabe),
  kursiv unter dem Stufenkopf, eine von vier Formulierungen, fest je Einheit (wechselt von
  Blatt zu Blatt, nicht beim Nachdruck). Entfällt, wenn eine Frage der Gliederung auf dem
  Blatt schon nach der Formelsammlung fragt (Flächen).
- Geprüft mit Parabel (XU61, 2 S.) und Volumen (AZL1, 3 S.); Bündel und Ausblenden an einer
  Kopie der Daten (Lineare, Parabel, Flächen); Art mehr und normal unverändert.

## Antwortzeilen je gefragte Größe (v0.11)
Fragt eine Aufgabe nach mehreren Größen, bekommt jede eine eigene Zeile mit
Namen und Einheit („Winkel: ___ °“, „Prozent: ___ %“). Warum: zwei Fragen,
eine Zeile – Schüler verwechseln.
- Original (msa/mehr-p10.csv, Spalte `form`, ebenso `form_einheit`):
  `antwort:Winkel|°;Prozent|%` – Größen durch „;“ (oder „,“), je Größe
  `Name|Einheit`; Einheit darf fehlen (`Anzahl|`). Mit „+“ kombinierbar
  (`zeichnen+antwort:Steigung|`). Mit Figur (Spalte grafik): Zeilen direkt
  neben der Figur, sonst rechtsbündig untereinander.
- Schülerfrage (Gliederung): `- **Schülerfrage-Form:** antwort:Winkel|°;Prozent|%`
  – die Zeilen stehen rechts neben jedem Fall.
