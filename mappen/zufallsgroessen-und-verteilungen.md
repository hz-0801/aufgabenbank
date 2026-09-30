# Mappe: zufallsgroessen-und-verteilungen

Eintrag: hz-0801/mathe-nachhilfe, katalog/zufallsgroessen-und-verteilungen.md
Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25T09:16:56Z, „katalog: Marken-Zeilen je Lerneinheit, drei Einheiten ergänzt, marken-bau.py“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:15 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Zufallsgrößen und Verteilungen
 3
 4  ### Verortung
 5  Die Zufallsgröße als Zuordnung und ihre Verteilung ohne spezielles Modell: die Verteilung aufstellen (Werte einer Auszahlung aus Spielregeln nachweisen, die Tabelle einer Augensumme durch Abzählen fül … (gekürzt, 1566 Zeichen)
 6  [GOST] Q2 (BB S. 26–27): L4-Zeile „Zufallsgrößen und Wahrscheinlichkeitsverteilungen zur Beschreibung stochastischer Situationen nutzen“ mit „Zufallsgrößen als Zuordnung von Ergebnissen von Zufallsexp … (gekürzt, 689 Zeichen)
 7  [FOS] Pflichtthema 4 nennt Zufallsvariablen über den „Erwartungswert von Zufallsvariablen“ (Zeile 1188) – die fhr-Zeilen liegen bei kenngroessen-von-verteilungen.md.
 8  [LS-AA] Klasse 8 Kapitel VIII 5 „Wahrscheinlichkeitsverteilung einer Zufallsgröße“ als Vorläufer; in der Oberstufe geht die Verteilung in den Binomial-Kapiteln auf (EP V, QP VIII). Zuordnung: beide Einheiten = Vorläuferkapitel plus Rohdatei (Ermessen). Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Verteilung aufstellen: die Werte der Zufallsgröße aus den Regeln gewinnen (alle Ergebnisfolgen durchrechnen), die Tabelle durch Abzählen füllen (günstige Paare je Wert), fehlende Wahrscheinlichkeiten über die Summe eins – auch mit Parameter und über unmögliche Werte. (Q2, GK-Kern „Zufallsgrößen als Zuordnung“, „Verteilung in Tabellen“) ← Eingabe „wahrscheinlichkeitsverteilung“, „zufallsgröße tabelle“, „summe eins“
12    Marken: BE Q2/4 · BB Q2 · GK (BE nur LK) · keine Prüfungsaufgabe
13  2. Verteilung lesen: die Symmetrie einer Verteilung nutzen (Restwahrscheinlichkeit gleich verteilen, kumulierte Werte daraus), beschriebene Zufallsgrößen den Säulendiagrammen zuordnen (Symmetrie, Verhältnisse einzelner Säulen). (Q2, GK-Kern „Verteilung in … Diagrammen“; OHiMi 2.4 Histogramme) ← Eingabe „verteilung zuordnen“, „symmetrische verteilung“, „säulendiagramm zufallsgröße“
14    Marken: BE Q2/4 · BB Q2 · GK (BE nur LK) · Abitur LK
15  Warum Kurzform: sechs Zeilen, sechs Typen, alle in Teil A – die Substanz trägt zwei Einheiten (aufstellen und lesen); die große Diagrammarbeit liegt beim Binomialmodell (binomialverteilung.md Einheit 5). Niveaustufung: fhr = über den Erwartungswert (Zeilen bei kenngroessen-von-verteilungen.md); GK = beide Einheiten; LK = dieselben – die Zuordnungsaufgabe und die Symmetrieaufgabe liegen erhöht; die Grenze kommt aus dem Niveau der Zeilen, nicht aus dem Plan.
16
17  ### Typen je Lerneinheit
18  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen; die Rohdatei führt keine Nebentypen.
19  Einheit 1: Wahrscheinlichkeitsverteilung der Augensumme in einer Tabelle vervollständigen (1) · Wahrscheinlichkeitsverteilung über ein unmögliches Ergebnis vervollständigen (1) — Nachweis: Mögliche Werte einer Auszahlung aus zweistufigen Spielregeln nachweisen (1) · Wahrscheinlichkeit p aus der Summe 1 im Diagramm nachweisen (1) — kein Deutungstyp. Dazu: Fehler finden (spiegelbildliche Ergebnisfolgen als verschiedene Beträge erwartet; Paare nur einmal gezählt; fehlende Werte geraten statt über die Summe eins bestimmt; die Säulenhöhen als Auszahlungen gelesen) · Begründen (warum sich alle Wahrscheinlichkeiten zu eins summieren; warum ein unmöglicher Wert die Restverteilung festlegt).
20  Einheit 2: Wahrscheinlichkeit eines Ereignisses aus einer symmetrischen Verteilung und einem Einzelwert bestimmen (1) — kein Nachweistyp — Deutung: Verteilungen zweier Zufallsgrößen den Säulendiagrammen zuordnen (1). Dazu: Fehler finden (den Einzelwert selbst als kumulierte Wahrscheinlichkeit angegeben; die Zuordnung nur nach der Form entschieden, ohne einzelne Säulenverhältnisse zu prüfen) · Begründen (warum die Symmetrie die Restwahrscheinlichkeit halbiert; warum ein Säulenverhältnis eine Verteilung identifiziert).
21  Zählung: 4 + 2 = 6 Haupttypen, 4 + 2 = 6 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal.
22
23  ### Voraussetzungen (Blatt 0)
24  Fertigkeiten (je Zeile: was, wofür):
25  - Ergebnismengen zweistufiger Experimente aufzählen und günstige Fälle abzählen (Paare, Reihenfolge beachten) – das Aufstellen in Einheit 1. Sek-I-Thema wahrscheinlichkeit.md. [GOST Eingangsvoraussetzung L5 „Laplace-Regel“; GOST Q2 L4]
26  - Brüche addieren und zur Summe eins ergänzen – die Restbestimmung in Einheit 1. Sek-I-Thema bruchrechnung.md. [GOST-OHiMi 2.1]
27  - Säulendiagramme lesen (Höhen, Symmetrie, Verhältnisse) – das Zuordnen in Einheit 2. Sek-I-Thema daten.md. [GOST-OHiMi 2.4 „Darstellung von Zufallsgrößen in Histogrammen“]
28  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
29  - „Welche Werte kann die Größe annehmen?“ – zu Spielregeln die möglichen Werte auflisten, ohne Wahrscheinlichkeiten zu rechnen. Vor Einheit 1. [GOST Q2 L4 „Zufallsgrößen als Zuordnung“; iqb 2018MgrundlegendAStochastik12-a]
30  - „Was muss eins ergeben?“ – zu Tabellen und Diagrammen ankreuzen, welche Werte sich zu eins summieren müssen und welcher fehlt; nichts rechnen. Vor Einheit 1 und 2. [Rohdatei: Summe-eins-Typen; iqb 2021MerhoehtAStochastik13-a]
31
32  ### Merkkasten
33  Einheit 1 (Verteilung aufstellen):
34      Zuordnung: eine Zufallsgröße ordnet jedem Ergebnis eine Zahl zu – erst alle Ergebnisse (auch Reihenfolgen!) durchgehen, dann die Werte sammeln; verschiedene Ergebnisse können denselben Wert liefern.
35      Tabelle: je Wert die günstigen Fälle zählen und durch die Gesamtzahl teilen; die Summe aller Wahrscheinlichkeiten ist eins – der Rest bestimmt fehlende Einträge, ein unmöglicher Wert bekommt die Null.
36      Mit Parameter: sind die Höhen Vielfache von p, liefert die Summe eins den Wert von p.
37      Auswendig (Teil A): der ganze Kasten – [GOST Q2 L4] „Zufallsgrößen als Zuordnung“, „Verteilung in Tabellen“; alle Zeilen des Bestands stehen in Teil A (Belege 2018MgrundlegendAStochastik12-a, 2018MerhoehtAStochastik12-a, 2021MerhoehtAStochastik13-a, 2022MgrundlegendAStochastik13-b).
38      Formelsammlung: keine – [FS-IQB 1.4] führt keine allgemeinen Verteilungsregeln – [FS] offen
39  Quelle: eigene Formulierung nach [GOST Q2 L4] und [GOST-OHiMi 2.4]; ohne Zahlenbeispiel (die Regeln sind zahlenfrei formuliert; Ermessen); [LS-AA Kl. 8 VIII 5 als Vorläufer].
40
41  Einheit 2 (Verteilung lesen):
42      Symmetrie: ist die Verteilung symmetrisch und der mittlere Einzelwert bekannt, verteilt sich der Rest zu gleichen Teilen auf beide Seiten – kumulierte Werte folgen durch Addieren bis zur Mitte.
43      Zuordnen: eine beschriebene Zufallsgröße erkennt man am Diagramm über Symmetrie oder Schiefe und über das Verhältnis einzelner Säulen (Abzählargument) – nie nur über die Form.
44      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] „Darstellung von Zufallsgrößen in Histogrammen“ (Belege 2022-bebb-lk-A1.8a, 2022MerhoehtAStochastik11-b).
45      Formelsammlung: keine – [FS] offen
46  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] und [GOST Q2 L4] „Verteilung in … Diagrammen“; ohne Zahlenbeispiel; [LS-AA Kl. 8 VIII 5].
47
48  ### Typische Fehler
49  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 6 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet.
50  - Beim Aufstellen: spiegelbildliche Ergebnisfolgen als verschiedene Beträge erwartet; Paare mit vertauschter Reihenfolge nur einmal gezählt; fehlende Werte geraten statt über die Summe eins und den unmöglichen Wert bestimmt; die Säulenhöhen als Auszahlungen gelesen. [iqb 2018MgrundlegendAStochastik12-a, 2018MerhoehtAStochastik12-a, 2022MgrundlegendAStochastik13-b, 2021MerhoehtAStochastik13-a]
51  - Beim Lesen: den bekannten Einzelwert selbst als kumulierte Wahrscheinlichkeit angegeben oder die Summe falsch geschlossen; die Zuordnung nur nach der Form entschieden, ohne die Säulenverhältnisse zu prüfen. [abi 2022-bebb-lk-A1.8a; iqb 2022MerhoehtAStochastik11-b]
52
53  ### Für schwache Schüler
54  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q2: beide Einheiten (Zuordnung, Tabelle, Diagramm); kein LK-Zusatz. Ohne Hilfsmittel: alles – der ganze Bestand liegt in Teil A. RLP FOS (fhr): Zufallsvariablen über den Erwartungswert (Zeilen bei kenngroessen-von-verteilungen.md). Vorrat: keiner – die Kurzform deckt den Bestand. Niveaustufe H der E-Phase [RLP]: die Verteilungstabelle ist Sek-I-Bestand (Kl. 8, wahrscheinlichkeit.md als Träger) – die Sek-II-Neuerung ist der Begriff und der Parameterumgang. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: Zufallsgrößen und Verteilungen decken sich mit dem GK-Kern, kein zusätzlicher Posten.
55  Grundvorstellung (Blatt 0) [GOST Q2 L4, MO]: Die Zufallsgröße ist eine Zählvorschrift, keine Zahl. „Wirf zwei Würfel (oder stell es dir vor), kein Term. Die Regel heißt: notiere die Summe. Welche Summen sind überhaupt möglich? Gibt es Summen, die auf mehr Arten entstehen als andere – welche, und über welche Würfelpaare? Zählt das Paar drei-und-vier gleich wie vier-und-drei? Und wenn die Regel stattdessen hieße: notiere die größere der beiden Zahlen – welche Werte sind dann möglich, und welcher ist der häufigste?“ Wer Reihenfolgen verschluckt oder die Werte der Größe mit den Würfelzahlen verwechselt, braucht das vor jeder Tabelle: Die Größe ordnet zu, die Ergebnisse tragen die Wahrscheinlichkeit, und gleiche Werte sammeln mehrere Ergebnisse ein. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q2 L4 „Zuordnung“), die Aufgabenform Ermessen. [GOST Q2 L4; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Paare nur einmal zählen“, iqb 2018MerhoehtAStochastik12-a; BASICS nur als Strukturvorbild, keine Inhalte]
56  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [Rohdatei; Sprossenfolge Ermessen]:
57  - Verteilung aufstellen (Einheit 1): „Welche Werte kann die Größe annehmen?“ ankreuzen (Vorstufe, Grundvorstellung) → die Tabelle einer Summe durch Abzählen füllen (Grundfall, viermal; iqb 2018MerhoehtAStochastik12-a, Teil A) → die möglichen Werte einer Auszahlung aus den Regeln nachweisen (iqb 2018MgrundlegendAStochastik12-a, Teil A) → den Parameter über die Summe eins nachweisen (iqb 2021MerhoehtAStochastik13-a, Teil A) → Prüfungshöhe: die Verteilung über einen unmöglichen Wert schließen (iqb 2022MgrundlegendAStochastik13-b, Teil A, Niveau III).
58  - Verteilung lesen (Einheit 2): „Was muss eins ergeben?“ ankreuzen (Vorstufe) → die kumulierte Wahrscheinlichkeit aus Symmetrie und Einzelwert bestimmen (Grundfall, viermal; abi 2022-bebb-lk-A1.8a, Teil A) → Prüfungshöhe: zwei beschriebene Zufallsgrößen den Diagrammen zuordnen und mit Säulenverhältnissen begründen (iqb 2022MerhoehtAStochastik11-b, Teil A, Niveau II).
59
60  ### Prüfungsform (fhr / abi / iqb)
61  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich; die Geltungsdateien führen das Thema für alle vier Zielprüfungen mit „ja“. Für fhr ist der Pool keine Vorgabe; die fhr-Zufallsvariablen liegen bei kenngroessen-von-verteilungen.md. Die Rohdatei zählt 6 Zeilen mit 6 Haupttypen (abi 1 Zeile, 1 Typ; iqb 5 Zeilen, 5 Typen; kein gemeinsamer Typ), Jahre 2018–2022. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
62  fhr: kein eigener Bestand – die Zufallsvariablen der FHR-Prüfungen laufen über den Erwartungswert (kenngroessen-von-verteilungen.md).
63  abi (1 Zeile, 1 Typ; Landesheft bebb-lk 2022) [abi-Katalog]: Wahrscheinlichkeit eines Ereignisses aus einer symmetrischen Verteilung und einem Einzelwert bestimmen (1, E2). Muster: die eine Zeile ist eine Teil-A-Aufgabe (zwei Punkte, Niveau II) – das Thema ist im Landesbestand ein Einzelstück.
64  iqb (5 Zeilen, 5 Typen; Pool 2018–2022, grundlegend 2 und erhöht 3 Zeilen, alle Teil A) [iqb-Katalog]: je 1: Mögliche Werte einer Auszahlung aus zweistufigen Spielregeln nachweisen (E1) · Verteilungen zweier Zufallsgrößen den Säulendiagrammen zuordnen (E2) · Wahrscheinlichkeit p aus der Summe 1 im Diagramm nachweisen (E1) · Wahrscheinlichkeitsverteilung der Augensumme in einer Tabelle vervollständigen (E1) · Wahrscheinlichkeitsverteilung über ein unmögliches Ergebnis vervollständigen (E1). Muster: alle fünf Zeilen sind kleine Teil-A-Aufgaben (ein bis drei Punkte) an Spiel- und Urnenkontexten – die Verteilung ohne Modell ist reine Teil-A-Materie; in Teil B übernimmt stets ein Modell (Binomial, hypergeometrisch). Amtlicher Anforderungsbereich in allen 5 Zeilen (höchster Bereich: I 2, II 3); Niveau I 2, II 2, III 1. Kontexte: Glücksrad-Spiele, Würfel, Kugelkisten. Keine Dubletten.
65  Zielmarke: Einheit 1 – iqb: die Verteilung über den unmöglichen Wert (2022MgrundlegendAStochastik13-b, Teil A, Niveau III) und der Parameternachweis (2021MerhoehtAStochastik13-a, Teil A, Niveau I). Einheit 2 – abi: die Symmetrieaufgabe (2022-bebb-lk-A1.8a, Teil A, Niveau II); iqb: die Diagrammzuordnung (2022MerhoehtAStochastik11-b, Teil A, Niveau II).
````

## 2 Originale (6)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2022MgrundlegendAStochastik13-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Verteilung aus a; X = Anzahl der Kisten mit verschiedenfarbigen Kugeln; P(X = 0) = 0, P(X = 1) = 0,6
- gesucht: P(X = 2) und P(X = 3)
- verfahren: X = 2 als unmöglich begründen (zwei gemischte Kisten lassen eine rote und eine gelbe Kugel für die dritte), Rest auf X = 3
- fehlerquelle: P(X = 2) und P(X = 3) als je 0,2 raten

### 2021MerhoehtAStochastik13-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 1 · format Rechnung · antwort Text
- gegeben: Einsatz 3 Euro; Auszahlung A mit P(A = 0) = p, P(A = b) = 3p, P(A = 6) = 2p aus dem Diagramm
- gesucht: Nachweis, dass p = 1/6
- verfahren: Summe der Säulen gleich 1
- fehlerquelle: die Säulenhöhen als Auszahlungen lesen

### 2022-bebb-lk-A1.8a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Zufallsgröße X mit Werten 0, 1, 2, 3, 4; Verteilung symmetrisch; P(X = 2) = 0,6
- gesucht: P(X ≤ 2)
- verfahren: Restwahrscheinlichkeit 0,4 symmetrisch auf beide Seiten von 2 verteilen
- fehlerquelle: P(X ≤ 2) = 0,6 oder 0,4 + 0,6 = 1 antworten

### 2022MerhoehtAStochastik11-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: X Augensumme zweier Würfel; Y Anzahl schwarzer Kugeln bei zwölf Zügen mit Zurücklegen aus 60 schwarzen und 40 weißen; Diagramme I, II, III
- gesucht: Zuordnung von X und Y zu den Diagrammen mit Begründung
- verfahren: Asymmetrie für Y, Verhältnis P(X = 3) : P(X = 2) = 2 für X
- fehlerquelle: X dem Diagramm I zuordnen (Säulen bei 2 und 3 nicht prüfen)

### 2018MerhoehtAStochastik12-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Tabelle · antwort Tabelle
- gegeben: Glücksrad mit drei gleichen Sektoren 1, 2, 3, zweimal gedreht; X Summe der Zahlen; Tabelle mit P(X = 2) = 1/9 und P(X = 4) = 1/3
- gesucht: fehlende Werte P(X = 3), P(X = 5), P(X = 6)
- verfahren: günstige Paare je Summe zählen, durch 9 teilen
- fehlerquelle: Paare (1; 2) und (2; 1) nur einmal zählen

### 2018MgrundlegendAStochastik12-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Einsatz 4 Euro, zweimal drehen; A halbiert, B verdoppelt den Betrag; der Betrag nach dem zweiten Drehen wird ausgezahlt
- gesucht: Nachweis, dass nur 1, 4 und 16 Euro ausgezahlt werden können
- verfahren: alle vier Ergebnisfolgen durchrechnen
- fehlerquelle: AB und BA als verschiedene Beträge erwarten

## 3 Maßstab (unterrichtsblatt.md, wortgleich)

### 2.2

````text
2.2 Zone „kennst du schon" – die Voraussetzungen, eine Stufe
zurück. Zweck: ins Thema hineinführen, sehen, ob der Schüler so
weit ist, an Vergessenes erinnern. Die Zone lehrt nichts Neues
und nennt keinen Begriff des Themas. Sie ist auf der Zeitachse
die Zone hinter dem Schüler, kein eigenes Blatt; bereitgestellt
wird sie trotzdem zuerst als eigenes PDF (2.7). Untertitel auf
dem Blatt: „Das kennst du schon". Hängt der Schüler hier, ist
die Lücke älter als das Thema – das zeigt das Blatt durch die
Zone selbst, ohne Kennzeichnung.
- Je Fertigkeit des Abschnitts eine Hauptnummer mit eigener
  Anweisung; Titel ist die Fertigkeit als Ich-kann-Satz mit dem
  Wort, das die Klasse kennt („Ich kann die Nullstelle einer
  Geraden berechnen", nicht „wo eine Gerade die x-Achse
  schneidet"). Die Nummern der Zone sind die ersten Nummern des
  Blatts (1, 2, 3 …), keine eigene Zählung (Z1) und kein
  Neubeginn im Lernblatt; die Nummer ist die Adresse.
- Breite nach Bestellung (1.1): mit Wiederholung alle
  Fertigkeiten, die das Lernblatt braucht, dazu die Zweige des
  Themas, die die Zeitmarke vor die Eingabeklasse legt, als je
  eine Fertigkeit mit dem Grundfall des Zweigs; „wiederholung
  kurz" je Fertigkeit eine leichte und eine Fallstrick-
  Teilaufgabe; „nur das neue" keine Zone.
- Reihenfolge nach erster Verwendung im Lernblatt: die Angabe
  „– Einheit n" der Fertigkeitszeile, kleinste Einheit zuerst;
  bei gleicher Einheit die Lehrplanfolge der Voraussetzungs-
  themen; ohne Angabe die Reihenfolge des Eintrags. Innerhalb
  der Hauptnummer leicht → Fallstrick.
- Je Fertigkeit: zwei sehr leichte Teilaufgaben (im Kopf lösbar),
  eine mittlere (negative Zahl, Dezimalzahl, Bruch, Einheit) und
  je eine für jeden Fallstrick der Fertigkeit, an dem das
  Lernblatt hängt. Du planst rückwärts: erst die Stellen des
  Lernblatts, die die Fertigkeit brauchen, daraus die
  Fallstricke. Eine Fertigkeit, die das Lernblatt nirgends
  braucht, entfällt – auch eine, die nur ein abgewählter Zweig
  gebraucht hätte. Dazu einmal je Zone eine Fehler-finden-
  Aufgabe zum häufigsten Fallstrick, unmittelbar darauf als
  eigene Hauptnummer eine gleichartige zum selbst Rechnen – das
  Paar gibt es nur in der Zone (2.3 c).
- Schreibform aus dem Eintrag: Nennt die Fertigkeitszeile eine
  Form (Tabelle, Dreisatz, Streifen), setzt du sie; ein Dreisatz
  steht im zweispaltigen Schema mit den Operationen am Pfeil, nie
  als Zeile mit Doppelpunkt (3.2). Die Zahlen eines Dreisatzes
  der Zone sind so gewählt, dass beide Schritte im Kopf gehen:
  glatter Teiler, Produkt ohne Übertrag (4 Hefte 6 €; nicht 3 m
  7,50 €). Schriftliche Multiplikation ist keine Fertigkeit der
  Zone, sondern ein eigenes Thema.
- Kein Kasten, keine Stufenmarkierung, keine Prüfungshöhe: die
  Zone hat keine Decke.
- Lösungen in der Lösungsdatei (3.4), dazu die Zeile, welche
  Hauptnummer welchen Zweig trägt („1–2 → Einheit 1 und 2 ·
  3 → Einheit 3").
Beim Fokus trägt die Zone nur die Fertigkeiten, die der Typ
braucht, je zwei Teilaufgaben, als erste Seite des Fokus.
````

### 2.3 c

````text
c) Pflichtelemente je Zweig, aus den Typen des Zweigs: Fehler
   finden – Muster aus „Typische Fehler", eigene Zahlen, in der
   Schreibform des Verfahrens (bei Umformungen senkrecht mit
   `\rechnung`), Fehler benennen und korrigieren; Begründen
   oder Entscheiden ohne Rechnung; Darstellungswechsel in beide
   Richtungen, soweit die Typen es tragen; eine Anwendung, deren
   Mathematik vom Kontext getragen wird (realistische Größen, im
   Kontext sinnvolle Frage). Typen des Zweigs, die in keiner
   Kette stehen (Ordnen, Ergänzen, Aussagen prüfen, Umkehrung),
   bekommen eine eigene Hauptnummer. Gemischte Aufgaben, deren
   Punkt die Zuordnung ist („erst zuordnen, dann rechnen"),
   verraten das Verfahren nicht.

   Eine Hauptnummer, eine Fertigkeit, eine Antwortform: Nach
   „Ich finde den Fehler" folgt in derselben Nummer keine
   Rechenaufgabe; Ankreuzen und Begründen stehen nicht in
   derselben Nummer; wechselt die Anweisung so, dass eine andere
   Fertigkeit gefragt ist, beginnt eine neue Hauptnummer. Die
   Zone ist die Ausnahme mit ihrem Paar aus Fehler finden und
   gleichartiger Rechenaufgabe (2.2), und dort sind es zwei
   Nummern.
````

### 2.4 b–c

````text
b) Die Kette. Maßstab ist das strukturelle Merkmal, nicht die
   Stückzahl: Ein Merkmal ist ein Fall, der eine andere
   Entscheidung oder einen anderen Schritt verlangt – anderer
   gegebener Wert, andere Einheit, Dezimalzahl oder Bruch statt
   ganzer Zahl, negatives Vorzeichen, Sonderfall, typischer
   Fallstrick, Umkehrung des Verfahrens. Die Sprossen kommen aus
   dem Eintrag; fehlt zwischen zwei Sprossen ein Schritt, den die
   Prüfungshöhe verlangt, schließt du ihn mit einer Zwischen-
   sprosse und sagst es im Ausgabeblock. Zwei Teilaufgaben, die
   sich nur in den Zahlen unterscheiden, sind dieselbe Sprosse
   und kommen nur beim Grundfall vor. Aufwandsmerkmale (Rundung,
   krumme Zahlen) kommen nach allen Strukturmerkmalen, nie
   zwischen die glatten Fälle. Ein Schüler, der das Thema gerade
   beginnt, schafft die ersten sechs Teilaufgaben jeder
   Verfahrens-Hauptnummer, ohne die Sprossen ab der Mitte zu
   können. Ablesetypen zählen als Verfahrenstypen, die Grafik ist
   nur der Träger: mehrere Objekte je Grafik, höchstens zwei
   Grafiken je Hauptnummer. Aufwandsintensive Typen (Wertetabelle,
   Zeichnen, Konstruktion): mindestens drei Teilaufgaben, die
   erste sehr leicht. Konzept- und Kontexttypen (Begründen,
   Entscheiden, Fehler finden, Textaufgaben mit einer Situation):
   eine bis drei Teilaufgaben, gestuft wie in einer Prüfung –
   Vorbereitungsschritt, Rechnung, Deutung; bei Begründen erst der
   klare Fall, dann der subtile. Bei Entscheidungstypen mit
   Ja/Nein-Antwort liegen richtig und falsch etwa halbe-halbe in
   gemischter Reihenfolge.

c) Prüfungshöhe. Jede Verfahrens-Hauptnummer endet mit genau einer
   Teilaufgabe in Form und Anspruch der zentralen Prüfung nach 1.5
   (P10, Abitur Teil A oder B, FHR). Nennt der Eintrag für die
   Einheit ein Original, ist das die Teilaufgabe – verfremdet, mit
   Jahr (3.6); sie darf eingeführte Merkmale kombinieren, führt
   aber kein neues ein. Zerfällt die Einheit in mehrere Haupt-
   nummern, trägt die letzte das Original, die anderen enden auf
   ihrer höchsten Sprosse. Prüfungsniveau wird in einer Stunde
   nicht erreicht; die Aufgabe ist Zielmarke und bleibt stehen.
   Trägt der Zweig „keine P10-Aufgabe", ist die Decke die
   Prüfungsaufgabe, in der er gebraucht wird, sonst die
   Lehrwerk-Konvention (1.5).
````

### 3.6

````text
3.6 Zahlen, Verfremdung, Formulierung. Zahlenwerte so gewählt,
dass Ergebnisse endlich sind und leichte Aufgaben im Kopf
rechenbar; periodische Dezimalbrüche tragen einen Hinweis. Keine
Aufgabe erscheint doppelt. Keine ganze Gleichung, kein Term,
kein Zahlenpaar und keine Funktion aus Kasten, Beispiel oder
Original des Eintrags in einer Teilaufgabe (2.1). Verfremdetes
Original: gleiches Verfahren, gleiche Falle, gleiche Form
(Ankreuzen, Lückensatz, Rechnung mit Rundung), andere Zahlen,
anderer Kontext; am Ende des Aufgabentexts in Klammern Prüfung,
Jahr und Papier, wie der Eintrag es nennt: „(P10 2018 FOR)",
„(P10 2025 GYM)", „(Abitur 2022 GK)", „(FHR 2024)".
Formulierungen eindeutig. Buchstaben und Symbole, die im Aufgaben-
text nicht erklärt sind, werden nicht verwendet, auch nicht T für
Term oder L für Lösungsmenge. Ein Buchstabe steht auf einem Blatt
für genau eine Sache: Seitenlabels verschiedener Figuren und
Variablen in Textaufgaben überschneiden sich nicht.
````
