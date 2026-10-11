# Bericht – P4Z Länge mit Pythagoras (erster Prüfungsbau nach pruefung.md)

Dauer: 21:21–21:29 (date), etwa 8 min Wanduhr.

## Was pruefung.md nicht beantwortet hat (selbst entschieden)
- Stufenkopf bei 1–2 von 5: „in k der letzten 5 Prüfungen“ gesetzt; „selten geprüft“ nur bei 0 (Text sagt nur „sonst“).
- Gezählt nur Hauptplätze (§ 5 Zuschnitt); 2025-OS-K2a (Nebenplatz) zählt nicht, steht aber in der Fundstellenliste.
- Kern-Grenze für „zweite/dritte echte“: Kathete (3 von 5) bekam drei echte, Gleichung zwei; ob drei schon „deutlich länger“ ist, ist offen – kein anderes Blatt des Kapitels zum Vergleich.
- Basisaufgaben (1f, 1j) gelten als herausgelöst (Marke „nach P10 ’xx“), wie die vorhandenen B1-Zeilen in herausgeloest-p10.csv.
- Stern für FOR: Sternchenaufgabe 2022-OS-K2c bekommt $\star$ in der Marke; 2026-FOR-Aufgaben mit EBR-Zwilling ohne Stern. Wo der Stern sitzt, sagt weder pruefung.md noch gemeinsam.md.
- Welche echte bei nur einer erlaubt ist, wenn zwei gleich schwer sind (Becher ’22 vs. Turm ’26): „schwerste“ vor „jüngere stärker“ gewählt.
- Stufen „Hypotenuse gesucht“/„Kathete gesucht“ aus dem Zuschnitt statt der Gliederungsstufe „Kathete oder Hypotenuse direkt“; Zählung je Zuschnitt-Stufe.
- Bank-Einstieg je Stufe statt einmal unten fürs ganze Blatt (Lesart von „unten Einstieg, dann echte“ pro Stufe).
- Ankreuzen in Basisaufgaben: Optionen untereinander neben der Skizze statt in einer Zeile (Skizze links, Antwort rechts geht vor).
- Fundstellenliste: Reihenfolge nach Jahr absteigend; Form „2026 FOR · 4 · a“.
- Übersicht: Kapitel Dreiecke mit seinen Einheiten, Stufen eingerückt unter dem gelieferten Blatt; Rand grau = Sinussatz, Symmetrie (je 2 · 2).
- Seitenumbruch vor Stufe 2 von Hand (\newpage), weil \pfstufekopf mit Needspace sonst allein unten stand.
- Kein Prüfstein, keine Hilfsmittel, keine Punkte (pruefung.md eindeutig).

## Formmerkmale, die der Setzer (werkzeuge/setzer.py) für die Sorte P bräuchte
- Stufenkopf `\pfstufekopf{Name}{in k der letzten 5 Prüfungen}`, k aus Gliederung/Zuschnitt gezählt (Hauptplätze 2022–2026), sonst „selten geprüft“.
- Stufenkopf nie allein unten: Needspace bis zur Höhe der ersten Aufgabe der Stufe.
- Marke links aus Original-id: „nach P10 ’jj“, FOR-Sternchen mit $\star$, eigene leer.
- Eingabe „echte je Stufe“ aus herausgeloest-p10.csv (Wortlaut, Abbildung, Lösung) statt nur Bankzeilen.
- Regel „eine echte, mehr nur bei anders + Kern“ als Auswahl mit Feld darstellung/fragerichtung.
- Fundstellenliste `\blattende{Originale…}{Vorher · Weiter}` aus allen Originalen der Einheit (Gliederung), nicht nur gesetzten.
- Päckchen aus mehreren Bankzeilen in einer Nummer (a, b, c), mit gzwei-Zeilen Text links / Karo rechts.
- Skizzen mit Punktnamen (F, D) – `\dreieck` setzt immer A, B, C; Baustein mit freien Eckennamen fehlt, deshalb eigenes TikZ mit \mbrwmarke.
- Zylinder mit Raumdiagonale/Stab und Parallelogramm mit Höhe auf der Verlängerung als Baustein.
- Übersicht Sorte P: Kapitel-Einheiten mit Stufen des gelieferten Blatts.
- Registerzeile Sorte P mit Original-ids.

## Aufgaben je Stufe (Nummern; davon echte)
- Gleichung aufstellen: 3 (2 echte)
- Hypotenuse gesucht: 2 (1 echte; Nr. 4 Päckchen a–c)
- Kathete gesucht: 4 (3 echte; Nr. 6 Päckchen a–b)
- Dreieck versteckt: 3 (1 echte)

## Seiten (pdfinfo)
- 1-uebersicht.pdf: 1 · 2-blatt.pdf: 5 · 3-loesungen.pdf: 1

Neue Bankzeilen: keine (jede Lücke hatte eine passende Zeile). Zahlen mit python3 nachgerechnet.

## Nacharbeit im Chat (10.10., Handwerk)
- Umbruch von Hand vor Stufe 2 raus, Needspace auf 0,25 Seitenhöhe; Karo 3 → 2 Reihen; Skizzen Nr. 10 und 12 kleiner: Blatt 5 → 3 Seiten, Fundstellen auf der letzten Seite.
- Fuß (kopfüber) braucht zwei xelatex-Läufe; mathblatt.sty über TEXINPUTS=../blattbau.
- Messwert Bau: Agent 0,23 Mio Token, 38 Werkzeugaufrufe, 8 min.

## Nachzug 11.10. (acht Festlegungen)
- Stufenkopf: Jahre statt Zählung, Hauptplätze 2022–2026, jüngstes zuerst („geprüft 2026 · 2024 · 2022“, „geprüft 2025“, „geprüft 2026 · 2022“).
- Kennung: `\pfheftkopf[\kennung]{…}{…}` rechts oben klein grau in allen drei Dateien; aus dem Fuß raus (Fuß = Standard von `\pfheftstil`).
- Nr. 4: je Teilaufgabe eine `\gzwei`-Zeile – links Buchstabe, Angaben, bei b) die Skizze darunter; rechts das eigene Karo. Linke Breite `\dimexpr0.5\textwidth-\gEin-\mbpfnr-5mm`, damit `\gzwei` nicht untereinander stapelt.
- Bank-Einstieg knapp: Nr. 4 und 6 nur die Angaben unter dem gemeinsamen Auftrag; Runden in den Auftrag gezogen.
- Ankreuzen: `\pfkreuzab{A}{…}` mit Buchstaben A–C; Fuß und Lösung nennen den Buchstaben („2: C“, „3: B“). Nr. 2 untereinander, weil neben der Skizze nur die halbe Breite frei ist.
- Marke mit Fundstelle: „nach P10 / ’26 · 1j“ (zwei Zeilen im Rand, mit `\\` getrennt), Stern bei Nr. 12 bleibt.
- Blattende: `\pfblattende{11}{…}{…}{…}` – graue Tabelle 26 FOR … 16 mit allen 17 Originalen der Einheit (Gliederung), 23 leer; darunter nur „Weiter: Seite oder Winkel mit sin, cos, tan“ („Vorher“ entfällt).
- Sorte = Erscheinungsform: Nr. 3 ist jetzt 2022-OS-B1g (Satz in Worten ankreuzen, eigener Wortlaut, Lösung B); 2024-OS-B1f (Gleichung ankreuzen wie Nr. 2) nur noch in der Tabelle. Herausgelöste Fassung 2022-OS-B1g-h1 an mathe-nachhilfe msa/herausgeloest-p10.csv angehängt.
- Übersicht: Dreiecke in der Lernfolge (Pythagoras · sin, cos, tan · Winkel ohne Rechnung · Sinussatz · Symmetrie), „Vorher“ weg, „Weiter: Flächeninhalt und Umfang“ bleibt.
- Neu in mathblatt.sty (Version 2026-10-11, blattbau): `\pfheftkopf` mit optionaler Kennung (rückwärtskompatibel), `\pfkreuz{A}{…}` (nebeneinander), `\pfkreuzab{A}{…}` (eigener Absatz, hängend), `\pfblattende{n}{Jahre}{Stellen}{Nachbarn}`.
- Seiten: Übersicht 1 · Blatt 3 · Lösungen 1; Fuß kopfüber auf jeder Seite; kein Stufenkopf allein unten.
- Offen: Nr. 11 („ja“/„nein“) ohne Buchstaben gelassen; der Setzer (werkzeuge/setzer.py, praeambel.tex mit `\blattende`, `\kk`) kennt die neuen Makros noch nicht.

## Nachzug 12.10. (nach befund-kritiker-2026-10-11.md)

- Form aus T2U: Laufkopf, Titel „Pythagoras“, Stufenzeile, Seitenzahl n/N, Ausschnitt „▸ Pythagoras · Weiter: sin, cos, tan · Winkel · Sinussatz · Vierecke“ (kein Vorher: nichts Bestellbares); Stufenköpfe „letzte 5 Jahre: …“; Übersicht mit Gruppen. Stufen: Gleichung aufstellen · Hypotenuse gesucht · Kathete gesucht · in Figuren versteckt (gemeinsam.md „Namen“). Rampe ’25 bleibt in „Hypotenuse gesucht“ (direkt), Becher ’22 in „in Figuren versteckt“ (finden) – wie der Kritiker mehr-dreiecke sagt.
- Je Stufe die Schülerfrage zuerst (Regel 5), Hilfssätze raus: Nr. 1 „Markiere die Hypotenuse“ statt des Satzes „sie liegt dem rechten Winkel gegenüber“, Lücken untereinander mit Buchstabenspalte; Nr. 4 „in welchen Dreiecken ist die Hypotenuse gesucht?“ (ankreuzen); Nr. 7 Gleichung ankreuzen mit gesuchter Kathete (plus oder minus – die Form von 2024-OS-B1f, die im Mehr-Block liegt); Nr. 12 „zeichne das rechtwinklige Dreieck ein“ an gleichschenkligem Dreieck, Rechteck mit Diagonale und Zylinder von vorn; Nr. 13 ohne „Die Höhe teilt …“.
- Befunde umgesetzt: Satz in Worten ’22 (Nr. 2) vor der Wurzelformel ’26 (Nr. 3); Päckchen Nr. 5 Skizze → Text → krumm, Nr. 8a mit Skizze; „Runde, wo nötig“ weg (Nr. 5, 8).
- Gestrichen: alte Nr. 11 (Löffel im Messbecher, Bank) – der Schritt „Zylinder von vorn“ steht jetzt in Nr. 12c, und Nr. 14 ist die echte dazu; das Blatt bleibt schlank.
- Andere Zahlen (msa/mehr-p10.csv): Nr. 6 200 cm, 17 cm → 200,7 cm; Nr. 9 262 m, 396 m → 296,9 m; Nr. 10 13,2 m, 7,3 m → 11,0 m; Nr. 11 38 cm, 16 cm → 34,5 cm; Nr. 14 7,5 cm, 3,4 cm, 2 cm → 12,1 cm. Nr. 2, 3 ohne Zahlen. Alle Ergebnisse mit Python nachgerechnet.
- Aufgaben je Stufe (echte): Gleichung aufstellen 3 (2) · Hypotenuse gesucht 3 (1) · Kathete gesucht 5 (3) · in Figuren versteckt 3 (1) – 14 Nummern, 7 echte (vorher 12 / 7).
- Nicht umgesetzt: Blatt auf 3 Seiten – es sind 4 (eine Stufe je Seite; Stufenkopf fordert 14 Zeilen, Wunsch in nachzug-2026-10-12.md). Drei echte in „Kathete gesucht“ bleiben (Kern, drei Erscheinungsformen: Sache, Teildreieck mit Höhe und „Weise nach“, Parallelogramm).
- Seiten: Übersicht 1, Blatt 4, Lösung 2. herausgeloest.csv (Originalzahlen) unverändert.
