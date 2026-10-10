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
