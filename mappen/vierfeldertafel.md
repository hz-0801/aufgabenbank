# Mappe: vierfeldertafel

Eintrag: hz-0801/mathe-nachhilfe, katalog/vierfeldertafel.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:14 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Vierfeldertafel
 3
 4  ### Verortung
 5  Die Vierfeldertafel als Darstellungsmittel zweier Merkmale: die Tafel aus Anteilen füllen (Ränder zuerst, Felder als Differenzen; bedingte Angaben erst über die Multiplikation zum Schnittanteil machen … (gekürzt, 1800 Zeichen)
 6  [GOST] Q2, 2. Kurshalbjahr (BB S. 27), Grund- und Leistungskursfach: L5-Zeile „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingt … (gekürzt, 1194 Zeichen)
 7  [FOS] Pflichtthema 4 „Stochastik“ (S. 28): „bedingte Wahrscheinlichkeiten (Unabhängigkeit von Ereignissen, Vierfeldertafel/Doppelbaum)“ (Zeilen 1185–1187 der Textfassung) – die Tafel ist FOS-Stoff, die zentralen Prüfungen stellen sie im Rahmen der Unabhängigkeitsaufgaben; die fhr-Zeilen liegen bei unabhaengigkeit.md, themen.csv führt für dieses Thema keine fhr-Zeile.
 8  [LS-AA] Qualifikationsphase Kapitel VIII 3 „Bedingte Wahrscheinlichkeit“ – die Tafel ist dort Werkzeug, ein eigenes Tafel-Kapitel gibt es nicht. Zuordnung: beide Einheiten = QP VIII 3 (Werkzeugteil). Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Die Tafel füllen: Aufbau (zwei Merkmale mit Gegenereignissen, vier Felder, Ränder, Summe eins bzw. Gesamtzahl), Füllregeln (Ränder zuerst, Felder als Differenzen der Ränder), der Kernschritt bei be … (gekürzt, 678 Zeichen)
12    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK
13  2. Aus der Tafel rechnen: die Vereinigung „A oder B“ als eins minus Gegenfeld (oder über den Additionssatz), das ausschließende Entweder-oder als Summe der beiden gemischten Felder, fehlende absolute Häufigkeiten durch Subtraktion, Anteile aus Anteilen und bedingten Anteilen kombinieren. (Q2, GK-Kern; OHiMi 2.4 „Additionssatz“) ← Eingabe „a oder b tafel“, „entweder oder“, „vereinigung tafel“
14    Marken: BE Q2 · BB Q2 · GK · Abitur GK
15  Warum zwei: Die Rohdatei besteht zu vier Fünfteln aus dem einen Fülltyp (neunzehn von neunundzwanzig Zeilen) – das Füllen ist die eine Fertigkeit, das Ablesen mit Additionsregeln die andere; mehr Einh … (gekürzt, 684 Zeichen)
16
17  ### Typen je Lerneinheit
18  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
19  Einheit 1: Vierfeldertafel aus Anteilen vervollständigen (19) · Tabelle mit drei Spalten analog zur Vierfeldertafel aus Anteilen vervollständigen (1) · Vierfeldertafel mit absoluten Häufigkeiten aus Gruppengrößen und bedingten Anteilen vervollständigen (1) — Nachweis: Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen (1) — kein Deutungstyp. Dazu: Fehler finden (einen bedingten Anteil unmittelbar als Feld eingetragen, ohne mit dem Rand zu multiplizieren – das Kernfehlmuster des Themas; „weder–noch“ als Randwert gelesen; „entweder–oder“ als Vereinigung gelesen; einen Schnitt als Produkt der Ränder angesetzt und damit Unabhängigkeit unterstellt; einen Prozentwert auf die falsche Gesamtheit bezogen) · Begründen (warum ein Anteil „innerhalb einer Gruppe“ bedingt ist und erst die Multiplikation mit dem Rand das Feld liefert; warum die Felder einer Zeile sich zum Rand summieren).
20  Einheit 2: Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen (2) · Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen (2) · Anteil aus Anteilen und bedingten Anteilen über die Vierfeldertafel berechnen (1) — kein Nachweistyp — Deutung: Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen (2). Dazu: Fehler finden (die Ränder addiert, ohne den Schnitt abzuziehen; das einschließende statt des ausschließenden Oder gerechnet; die falsche Teilgruppe subtrahiert) · Begründen (warum „A oder B“ das Gegenfeld von „weder A noch B“ ist; warum das ausschließende Oder genau zwei Felder summiert).
21  Zählung: 4 + 4 = 8 Haupttypen, 22 + 7 = 29 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal.
22
23  ### Voraussetzungen (Blatt 0)
24  Fertigkeiten (je Zeile: was, wofür):
25  - Anteile, Prozentsätze und absolute Häufigkeiten ineinander umrechnen – jede Tafel, beide Einheiten. Sek-I-Thema prozentrechnung.md. [RLP E–F Prozentrechnung; GOST Eingangsvoraussetzung L4 „Prozentdarstellungen“]
26  - Zweistufige Zufallsexperimente und Pfadregeln (Baumdiagramm als Schwesterdarstellung, „Anteil vom Anteil“ als Produkt) – der Kernschritt bedingte Angabe mal Rand. Sek-II-Nachbarthema zufallsexperimente-und-pfadregeln.md Einheit 6 (Situationsbaum: bedingter Anteil am Ast, Anteil aller als Pfad). [GOST Eingangsvoraussetzung L5 „Baumdiagrammen sowie Pfadregeln“; RLP G „Vierfeldertafeln“]
27  - Gegenereignis und Komplement (der Rest zu eins bzw. zur Gesamtzahl) – Ränder ergänzen, Vereinigung über das Gegenfeld, Einheit 1 und 2. Sek-I-Thema wahrscheinlichkeit.md. [RLP G „Gegenwahrscheinlichkeiten“]
28  - Tabellen lesen und ausfüllen (Zeilen- und Spaltensummen) – die Tafelarbeit selbst. Sek-I-Thema daten.md. [GOST Eingangsvoraussetzung L5 sinngemäß]
29  - Lineare Gleichungen und Ungleichungen mit einem Parameter lösen (negative Werte ausschließen) – die Parametertafel in Einheit 1. Sek-I-Thema lineare-gleichungen.md. [GOST-OHiMi 2.1]
30  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
31  - „Weder–noch, entweder–oder, oder?“ – zu Formulierungen ankreuzen, welches Feld oder welche Feldsumme gemeint ist: „weder A noch B“ (ein Feld), „entweder A oder B“ (zwei Felder), „A oder B“ (drei Felder, Gegenfeld nutzen); nichts rechnen. Vor Einheit 1 und 2. [GOST-OHiMi 2.4 „Additionssatz“; abi 2023-bebb-gk-B4.1b, iqb 2018MerhoehtBStochastikWTR2-1b, 2025MgrundlegendBStochastikWTR3-1b]
32
33  ### Merkkasten
34  Einheit 1 (Die Tafel füllen):
35      Aufbau: zwei Merkmale mit ihren Gegenereignissen – vier Innenfelder, vier Ränder, rechts unten die Summe eins (oder die Gesamtzahl). Jede Zeile und jede Spalte summiert sich zu ihrem Rand.
36      Füllregeln: erst die Ränder eintragen (Gegenanteile als Rest zu eins), dann die Felder als Differenzen – ein bekanntes Feld genügt, der Rest folgt.
37      Bedingt heißt multiplizieren: „ein Anteil innerhalb einer Gruppe“ ist eine bedingte Angabe – das Feld ist Rand mal bedingter Anteil, nie der bedingte Anteil selbst.
38        In einer Gemeinde sind 52,1 % Frauen, 64,8 % der Frauen tragen eine Brille: das Feld Frau-und-Brille ist 0,521 · 0,648 ≈ 0,338 – nicht 0,648.
39      Sonderangaben: „weder A noch B“ ist das Feld ¬A ∩ ¬B (kein Rand!); „entweder A oder B“ ist die Summe der beiden gemischten Felder.
40        Display defekt 10,7 %, weder Display noch Netzteil defekt 87,3 %: aus dem Rand 89,3 % für „Display heil“ folgt das Feld heil-und-Netzteil-defekt als 89,3 − 87,3 = 2,0 %.
41      Mit Zahlen und mit Parameter: absolute Häufigkeiten füllen die Tafel genauso (Gruppengröße mal Anteil, Randsummen); bei Parametertafeln schließt eine negative Wahrscheinlichkeit Werte aus.
42      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] „Vierfeldertafel“ (Teil-A-Beleg 2021MerhoehtAStochastik11-a; die Tafel selbst prüft der Pool sonst in Teil B, aber ohne Formelsammlungsstütze).
43      Formelsammlung: keine – [FS-IQB 1.4] führt die bedingte Wahrscheinlichkeit und die Unabhängigkeit, keine Tafelregeln – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
44  Quelle: eigene Formulierung nach [GOST Q2 L5] „Vierfeldertafel“ und [GOST-OHiMi 2.4]; Zahlenbeispiele aus abi 2018-bb-ea-B4.2a und 2018-be-gk-B3.2e (wörtlich); [LS-AA QP VIII 3].
45
46  Einheit 2 (Aus der Tafel rechnen):
47      A oder B: über das Gegenfeld – P(A ∪ B) = 1 − P(¬A ∩ ¬B); gleichwertig der Additionssatz P(A ∪ B) = P(A) + P(B) − P(A ∩ B) – die Ränder addieren und den Schnitt einmal abziehen.
48      Entweder A oder B (ausschließend): die Summe der beiden gemischten Felder P(A ∩ ¬B) + P(¬A ∩ B) – der Schnitt zählt hier gar nicht.
49      Anzahlen: fehlende absolute Häufigkeiten entstehen durch Subtraktion von Gesamtzahl und Randsummen – die Tafel muss dafür nicht vollständig sein.
50      Kombinieren: ein Gesamtanteil setzt sich aus Feldern zusammen, die einzeln als Rand mal bedingter Anteil entstehen können.
51      Auswendig (Teil A): „A oder B“ und „Entweder A oder B“ – [GOST-OHiMi 2.4] „Additionssatz“; das Übersetzen der Oder-Formen ist das Prüfmuster beider Profile.
52      Formelsammlung: keine – der Additionssatz steht in der Anlage, nicht in [FS-IQB 1.4] – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
53  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] „Additionssatz“ und [GOST Q2 L5]; Zahlenbeispiele keine (die Regeln sind zahlenfrei formuliert; Ermessen); [LS-AA QP VIII 3].
54
55  ### Typische Fehler
56  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 29 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
57  - Bedingten Anteil als Feld eingetragen – das Kernfehlmuster: den Anteil innerhalb einer Gruppe ohne Multiplikation mit dem Rand in die Tafel geschrieben oder als Feld gelesen; „die Hälfte der M-Kunden“ auf alle Kunden bezogen; einen Anteil auf die falsche Gesamtheit bezogen. [abi 2018-bb-ea-B4.2a, 2023-bebb-gk-B4.1a, 2022-bebb-gk-B4h, 2017-bb-ea-B4.1a; iqb 2023MgrundlegendBStochastikWTR3-1a, 2022MgrundlegendBStochastikWTR1-1e, 2022MerhoehtBStochastikWTR2-1a, 2018MgrundlegendBStochastikWTR1-1a, 2021MgrundlegendBStochastikWTR3-1a, 2020MgrundlegendAStochastik12-a]
58  - Sonderangaben falsch gelesen: „weder–noch“ als Randwert oder als „genau eines defekt“; „entweder–oder“ als Vereinigung; ein Feld als Rand oder ein Rand als Feld; einen Schnitt als Produkt der Ränder angesetzt und damit Unabhängigkeit unterstellt. [abi 2018-be-gk-B3.2e, 2024-bebb-gk-B4.1b; iqb 2018MgrundlegendBStochastikWTR2-1e, 2018MerhoehtBStochastikWTR2-1b, 2026MerhoehtBStochastikWTR2-1b, 2025MgrundlegendBStochastikWTR3-1a, 2025MerhoehtBStochastikWTR1-1a, 2024MgrundlegendBStochastikWTR1-1b, 2024MgrundlegendBStochastikWTR2-1b, 2024MerhoehtBStochastikWTR2-1a, 2026MgrundlegendBStochastikWTR2-1a]
59  - Beim Rechnen aus der Tafel: die Ränder addiert, ohne den Schnitt abzuziehen; das einschließende statt des ausschließenden Oder; die falsche Teilgruppe subtrahiert; Prozentangaben unbesehen als Feldwerte eingetragen. [abi 2023-bebb-gk-B4.1b, 2019-be-gk-B4.1c; iqb 2023MgrundlegendBStochastikWTR3-1b, 2025MgrundlegendBStochastikWTR3-1b, 2025MerhoehtBStochastikWTR1-1b, 2019MgrundlegendBStochastikWTR1-1c, 2019MgrundlegendBStochastikWTR3-1a]
60  - Mit Parameter: die Differenz zweier Parameterterme falsch gebildet; den Ausschluss über das Vorzeichen nicht geprüft. [iqb 2021MerhoehtAStochastik11-a]
61
62  ### Für schwache Schüler
63  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q2 Brandenburg und Berlin: die L5-Zeile „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen“ trägt beide Einheiten; kein LK-Zusatz. Ohne Hilfsmittel (Anlage OHiMi 2.4, Prüfungsteil A): „Vierfeldertafel“ und „Additionssatz“ – beide Kästen vollständig. Vorrat (Ermessen nach dem Niveau der Rohdatei): die Parametertafel und die Entweder-oder-Deutungen. Niveaustufe H der E-Phase [RLP]: die Vierfeldertafel ist Sek-I-Bestand (RLP G, wahrscheinlichkeit.md) – die Sek-II-Neuerung ist der systematische Umgang mit bedingten Angaben. RLP FOS (fhr): „Vierfeldertafel/Doppelbaum“ ist Pflichtstoff; die fhr-Zeilen liegen bei unabhaengigkeit.md. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung bedingte Wahrscheinlichkeiten mit Vierfeldertafel – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
64  Grundvorstellung (Blatt 0) [GOST Eingangsvoraussetzung L5, MO]: Ein Feld der Tafel ist ein Anteil an allen – ein Anteil „innerhalb einer Gruppe“ ist etwas anderes. „Hier sind zwanzig Spielkarten in zwei Farben, einige davon markiert, kein Term. Sortiere sie in vier Häufchen: rote markierte, rote unmarkierte, schwarze markierte, schwarze unmarkierte. Welcher Anteil aller Karten ist rot und markiert? Und welcher Anteil der roten Karten ist markiert – zähle beide aus: warum sind die Zahlen verschieden, obwohl beide ‚markierte rote Karten‘ zählen? Durch welche Gesamtheit hast du jeweils geteilt?“ Wer beide Anteile für dieselbe Zahl hält, braucht das vor jeder Tafel: Ein Feld teilt durch alle, ein bedingter Anteil nur durch die Gruppe – deshalb wird aus dem bedingten Anteil erst durch Multiplizieren mit dem Gruppenanteil ein Feld. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q2-Kern „Vierfeldertafel“, „bedingte Wahrscheinlichkeit“), die Aufgabenform ist Ermessen. [GOST Q2 L5; GOST Eingangsvoraussetzung L5; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „die 64,8 % unmittelbar als Feld der Tafel eintragen“, abi 2018-bb-ea-B4.2a; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
65  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
66  - Die Tafel füllen (Einheit 1): „Rand, Feld oder bedingt?“ – zu jeder Prozentangabe eines Aufgabentexts ankreuzen, ob sie ein Rand (Anteil an allen), ein Feld (Anteil an allen mit beiden Merkmalen) oder ein bedingter Anteil (Anteil innerhalb einer Gruppe) ist; „Anteil oder Anzahl?“ – ankreuzen, ob die Tafel mit Wahrscheinlichkeiten (Summe eins) oder absoluten Häufigkeiten (Summe gleich Gesamtzahl) zu füllen ist; nichts rechnen (Vorstufe, Grundvorstellung) → die Tafel aus zwei Rändern und einem Feld füllen: Ränder ergänzen, Felder als Differenzen (Grundfall, viermal; iqb 2018MgrundlegendBStochastikWTR1-1a, 2023MgrundlegendBStochastikWTR3-1a; abi 2023-bebb-gk-B4.1a, 2024-bebb-gk-B4.1b) → eine bedingte Angabe erst zum Feld machen: Rand mal bedingter Anteil (abi 2018-bb-ea-B4.2a, 2022-bebb-gk-B4h; iqb 2022MgrundlegendBStochastikWTR1-1e, 2024MerhoehtBStochastikWTR2-1a) → Sonderangaben übersetzen: „weder–noch“ als Feld, „entweder–oder“ als Feldsumme (abi 2018-be-gk-B3.2e; iqb 2018MgrundlegendBStochastikWTR2-1e, 2018MerhoehtBStochastikWTR2-1b, 2026MerhoehtBStochastikWTR2-1b, 2026MgrundlegendBStochastikWTR2-1a, 2025MgrundlegendBStochastikWTR3-1a, 2025MerhoehtBStochastikWTR1-1a, 2024MgrundlegendBStochastikWTR1-1b, 2024MgrundlegendBStochastikWTR2-1b) → mit absoluten Häufigkeiten füllen: Gruppengrößen mal Anteile, Randsummen (iqb 2019MgrundlegendBStochastikWTR3-1a; abi 2017-bb-ea-B4.1a) → die Tafel mit drei Spalten (iqb 2022MerhoehtBStochastikWTR2-1a) → Prüfungshöhe: die Parametertafel füllen und einen Wert über die negative Wahrscheinlichkeit ausschließen (iqb 2021MerhoehtAStochastik11-a, Teil A, Niveau II).
67  - Aus der Tafel rechnen (Einheit 2): „Weder–noch, entweder–oder, oder?“ ankreuzen (Vorstufe) → die fehlende Anzahl durch Subtraktion (Grundfall, viermal; abi 2019-be-gk-B4.1c, iqb 2019MgrundlegendBStochastikWTR1-1c) → „A oder B“ über das Gegenfeld oder den Additionssatz (abi 2023-bebb-gk-B4.1b, iqb 2023MgrundlegendBStochastikWTR3-1b) → Anteile aus Anteilen und bedingten Anteilen zusammensetzen (iqb 2020MgrundlegendAStochastik12-a, Teil A) → Prüfungshöhe: die Entweder-oder-Aussage beurteilen (iqb 2025MgrundlegendBStochastikWTR3-1b, 2025MerhoehtBStochastikWTR1-1b, Niveau II).
68
69  ### Prüfungsform (fhr / abi / iqb)
70  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; die FOS-Vierfeldertafeln liegen beim Thema Unabhängigkeit von Ereignissen, themen.csv führt hier keine fhr-Zeile. Die Rohdatei zählt 29 Zeilen mit 8 Haupttypen (abi 8 Zeilen, 3 Typen; iqb 21 Zeilen, 8 Typen; 3 Typen in beiden Profilen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
71  fhr: kein eigener Bestand – die Vierfeldertafeln der FHR-Prüfungen (Pflichtthema 4) laufen als Bausteine der Unabhängigkeitsaufgaben und liegen mit ihren Zeilen bei unabhaengigkeit.md.
72  abi (8 Zeilen, 3 Typen; Landeshefte bb-ea, be-gk, bebb-gk 2017–2024) [abi-Katalog]: Vierfeldertafel aus Anteilen vervollständigen (6, E1) · je 1: Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen (E2) · Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen (E2). Muster: Alle 8 Zeilen liegen in Teil B (zwei bis fünf Punkte) – die Tafel eröffnet die Stochastik-Kontextaufgabe als Darstellungsauftrag („Stellen Sie den Sachverhalt in einer Vierfeldertafel dar“) und füttert die folgenden Teilaufgaben (bedingte Wahrscheinlichkeit, Unabhängigkeit – die Zeilen dort); 6 der 8 Zeilen sind wortgleiche Pooldubletten (2018-be-gk-B3.2e, 2019-be-gk-B4.1c, 2022-bebb-gk-B4h, 2023-bebb-gk-B4.1a, 2023-bebb-gk-B4.1b, 2024-bebb-gk-B4.1b), Landeszusätze die beiden 2017/2018er Häufigkeitsaufgaben (2017-bb-ea-B4.1a, 2018-bb-ea-B4.2a). Niveau I 5, II 3.
73  iqb (21 Zeilen, 8 Typen; Pool 2018–2026, grundlegend 14 und erhöht 7 Zeilen, Teil A 2 und Teil B 19 Zeilen) [iqb-Katalog]: Vierfeldertafel aus Anteilen vervollständigen (13, E1) · Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen (2, E2) · je 1: Anteil aus Anteilen und bedingten Anteilen über die Vierfeldertafel berechnen (E2) · Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen (E2) · Tabelle mit drei Spalten analog zur Vierfeldertafel aus Anteilen vervollständigen (E1) · Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen (E1) · Vierfeldertafel mit absoluten Häufigkeiten aus Gruppengrößen und bedingten Anteilen vervollständigen (E1) · Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen (E2). Muster: In Teil B eröffnet die Tafel fast jede zweite Stochastik-Kontextaufgabe des Pools (zwei bis vier Punkte, Anforderungsbereich I bis II) – Bildschirme 2018, Glücksspiel und Fahrprüfung 2019, Werbeabteilung 2021, Tarife 2022, Lehrkräfte 2023, Lastenräder und Geräte 2024, Großstadt 2025, Fahrzeuge und Musik 2026; Teil A stellt die Parametertafel (2021MerhoehtAStochastik11-a) und die Anteilskombination (2020MgrundlegendAStochastik12-a). Amtlicher Anforderungsbereich in allen 21 Zeilen (höchster Bereich: I 13, II 8); Niveau I 14, II 7. Kontexte: Bildschirme, Fahrprüfungen, Glücksspiel, Tarife, Lehrkräfte, Lastenräder, Haushalte, Musiktitel. 6 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste), keine abgewandelt.
74  Zielmarke: Einheit 1 – abi: die Tafel mit bedingter Angabe (2018-bb-ea-B4.2a, Niveau II) und die Standard-Tafel (2023-bebb-gk-B4.1a, Niveau I); iqb: die Parametertafel mit Ausschluss (2021MerhoehtAStochastik11-a, Teil A, Niveau II) und die Dreispaltentabelle (2022MerhoehtBStochastikWTR2-1a, Niveau II). Einheit 2 – abi: die Vereinigung über das Gegenfeld (2023-bebb-gk-B4.1b, Niveau I); iqb: die Entweder-oder-Beurteilung (2025MerhoehtBStochastikWTR1-1b, Niveau II) und die Anteilskombination in Teil A (2020MgrundlegendAStochastik12-a, Niveau II).
````

## 2 Originale (28)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2018-be-gk-B3.2e (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: Für einen zufällig ausgewählten Bildschirm gilt: das Display ist mit der Wahrscheinlichkeit 10,7 Prozent defekt, das Netzteil mit 3,0 Prozent, und mit 87,3 Prozent ist weder das Display noch das Netzteil defekt.
- gesucht: vollständig ausgefüllte Vierfeldertafel
- verfahren: Aus dem Rand für das Display folgt der Gegenwert 89,3 Prozent; das Feld Display heil und Netzteil defekt ergibt sich als 89,3 − 87,3 = 2,0 Prozent. Damit ist das Feld Display defekt und Netzteil defekt 3,0 − 2,0 = 1,0 Prozent und das Feld Display defekt und Netzteil heil 10,7 − 1,0 = 9,7 Prozent.
- fehlerquelle: die 87,3 Prozent als Wahrscheinlichkeit dafür lesen, dass das Display heil ist, statt dass beide Bauteile heil sind

### 2019-be-gk-B4.1c (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Fahrprüfungen einer Region: 13 879 Prüflinge, davon 2 482 mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; Ereignisse A: mindestens 30 Jahre alt, B: Prüfung bestanden
- gesucht: Anzahl der Prüflinge, die jünger als 30 waren und nicht bestanden haben
- verfahren: Gesamtzahl minus mindestens 30-Jährige minus jüngere Bestandene
- fehlerquelle: 11 104 − 8 870 = 2 234 (Bestandene ab 30) als Antwort nehmen

### 2022-bebb-gk-B4h (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: P(S) = 5 %, P(Z) = 10 %, P_Z(S) = 8 %
- gesucht: vollständige Vierfeldertafel
- verfahren: S∩Z = 0,008, Rest aus den Rändern
- fehlerquelle: 8 % direkt als Feld S∩Z eintragen

### 2023-bebb-gk-B4.1a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich.
- gesucht: vollständig ausgefüllte Vierfeldertafel
- verfahren: Fehlende Felder als Differenzen der Ränder.
- fehlerquelle: 15 % als bedingte Wahrscheinlichkeit lesen

### 2023-bebb-gk-B4.1b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich. Vierfeldertafel aus a.
- gesucht: Wahrscheinlichkeit, dass eine zufällig ausgewählte Lehrkraft weiblich ist oder an einem Gymnasium arbeitet
- verfahren: Eins minus Feld ¬W∩¬G, alternativ 72 % + 25 % − 15 %.
- fehlerquelle: 72 % + 25 % ohne Abzug des Schnitts

### 2024-bebb-gk-B4.1b (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: 60 % Treuekunden, 20 % Morgenkunden, P(¬T ∩ M) = 0,05
- gesucht: vollständige Vierfeldertafel
- verfahren: Differenzen der Ränder
- fehlerquelle: 0,05 in das Feld T∩M eintragen

### 2017-bb-ea-B4.1a (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Zu einer Autogrammstunde haben 30 Frauen und 50 Männer je eine Frage eingereicht. 75 Prozent aller eingereichten Fragen beziehen sich auf den Fußball, die übrigen sind eher allgemeiner Natur. Die Fragen der Frauen verteilen sich zu gleichen Teilen auf rein fußballerische und allgemeine.
- gesucht: Anzahl der von Männern gestellten Fragen, die eher allgemeine Dinge betreffen
- verfahren: Insgesamt sind es 80 Fragen, davon 25 % allgemeine, also 20. Von den Frauen stammen 15 allgemeine Fragen; die Differenz entfällt auf die Männer.
- fehlerquelle: die 75 Prozent auf die Männerfragen statt auf alle Fragen beziehen

### 2018-bb-ea-B4.2a (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 5 · format Tabelle|Rechnung · antwort Tabelle|Zahl
- gegeben: In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen sind. Eine aus der Bevölkerung zufällig ausgewählte Person ist ein Mann.
- gesucht: Darstellung des Sachverhalts in einer Vierfeldertafel|Wahrscheinlichkeit dafür, dass dieser Mann eine Brille trägt
- verfahren: Die Randwerte 0,625 für Brille und 0,521 für Frauen eintragen. Die 64,8 % sind ein Anteil innerhalb der Frauen, also eine bedingte Wahrscheinlichkeit; daraus folgt das Feld Frau und Brille als 0,521 · 0,648. Die übrigen Felder über die Randsummen ergänzen. Die gesuchte Wahrscheinlichkeit ist das Feld Mann und Brille geteilt durch den Randwert der Männer.
- fehlerquelle: die 64,8 % unmittelbar als Feld der Tafel eintragen, also ohne Multiplikation mit 0,521

### 2021MerhoehtAStochastik11-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 3 · format Tabelle|Begründung · antwort Term|Text
- gegeben: Vierfeldertafel mit P(A∩B) = p, P(A) = 3p, P(Ā) = 1 − 3p, P(B) = 4p; p ≠ 0
- gesucht: vollständige Tafel; Nachweis, dass p nicht 1/5 sein kann
- verfahren: fehlende Felder als Differenzen, Vorzeichen von 1 − 6p prüfen
- fehlerquelle: 1 − 3p − 3p falsch als 1 − 3p rechnen

### 2020MgrundlegendAStochastik12-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Anteil verkleideter Erwachsener unter allen Gästen 12 %, Anteil aller Erwachsenen 60 %; 75 % der Jugendlichen verkleidet
- gesucht: Anteil der nicht Verkleideten unter allen Gästen
- verfahren: 0,48 + 0,25 · 0,4
- fehlerquelle: 12 % als bedingten Anteil unter den Erwachsenen lesen

### 2022MerhoehtBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: 20 % Tarif S, 25 % L; 47 % haben angerufen, darunter die Hälfte der M-Kunden; 11 % haben S und nicht angerufen
- gesucht: vollständige Tabelle
- verfahren: M-Anteil als Rest, dann Zeilen und Spalten ergänzen
- fehlerquelle: „die Hälfte der M-Kunden“ als 50 % aller Kunden lesen

### 2025MerhoehtBStochastikWTR1-1b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Vierfeldertafel aus a; Aussage: P(G und nicht J) ist etwa halb so groß wie P(entweder G oder nicht J)
- gesucht: Beurteilung
- verfahren: beide Wahrscheinlichkeiten aus der Tafel, Verhältnis
- fehlerquelle: einschließendes Oder (0,82) rechnen

### 2018MgrundlegendBStochastikWTR1-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: Jugendliche eines Landes: 49,20 % weiblich (W), 47,10 % erledigen Finanzangelegenheiten regelmäßig mit Smartphone oder Tablet (S), 19,68 % sind weiblich und tun das
- gesucht: vollständig ausgefüllte Vierfeldertafel
- verfahren: Differenzen der Ränder
- fehlerquelle: 19,68 % als bedingten Anteil lesen

### 2023MgrundlegendBStochastikWTR3-1a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: 25 % der Lehrkräfte am Gymnasium; 15 % weiblich und am Gymnasium; 72 % weiblich
- gesucht: vollständige Vierfeldertafel
- verfahren: Fehlende Felder als Differenzen
- fehlerquelle: 15 % als bedingte Wahrscheinlichkeit lesen

### 2022MgrundlegendBStochastikWTR1-1e (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: P(S) = 5 %, P(Z) = 10 %, P_Z(S) = 8 %
- gesucht: vollständige Vierfeldertafel
- verfahren: S∩Z = 0,008, Rest aus den Rändern
- fehlerquelle: 8 % direkt als Feld S∩Z eintragen

### 2024MerhoehtBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Tabelle · antwort Tabelle
- gegeben: 60 % mit Pkw, 8 % mit Lastenrad, 14 % der Haushalte ohne Pkw mit Lastenrad
- gesucht: vollständige Vierfeldertafel
- verfahren: 0,4 · 0,14 als Schnitt, Rest über Differenzen
- fehlerquelle: 0,14 direkt als Feld eintragen

### 2018MgrundlegendBStochastikWTR2-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: Für einen zufällig ausgewählten Bildschirm: Display defekt 10,7 %, weder Display noch Netzteil defekt 87,3 %, Netzteil defekt 3,0 %
- gesucht: vollständig ausgefüllte Vierfeldertafel
- verfahren: ¬D∩¬N = 87,3 %, Ränder 10,7/89,3 und 3,0/97,0, Rest als Differenzen
- fehlerquelle: 87,3 % als Feld „genau eines defekt“ lesen

### 2018MerhoehtBStochastikWTR2-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 4 · format Tabelle · antwort Tabelle
- gegeben: Für einen zufällig ausgewählten Bildschirm: Display defekt 10,7 %, weder Display noch Netzteil defekt 87,3 %, entweder Display oder Netzteil defekt 11,7 %
- gesucht: vollständig ausgefüllte Vierfeldertafel
- verfahren: D∩N aus 100 − 87,3 − 11,7; Rest als Differenzen
- fehlerquelle: 11,7 % als P(D ∪ N) lesen

### 2026MerhoehtBStochastikWTR2-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Tabelle · antwort Tabelle
- gegeben: A: mindestens fünf Jahre alt (70,8 %); B: Pkw (80 %); P(nicht A und nicht B) = 0,044
- gesucht: alle Felder der Vierfeldertafel
- verfahren: Ränder eintragen, Felder als Differenzen
- fehlerquelle: 0,044 als P(nicht A) lesen

### 2026MgrundlegendBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Tabelle · antwort Tabelle
- gegeben: 32 % Hip-Hop-Songs (H), 40 % mindestens 4 Minuten lang (L), P(H und L) = 0,14
- gesucht: fehlende Wahrscheinlichkeiten der Vierfeldertafel
- verfahren: Ränder eintragen, Innenfelder als Differenzen
- fehlerquelle: 0,32 · 0,4 als Schnitt ansetzen (Unabhängigkeit unterstellt)

### 2025MgrundlegendBStochastikWTR3-1a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: 72 % jünger als 50 Jahre; 18 % jünger als 50 und nicht in einer Großstadt; 75 % in einer Großstadt
- gesucht: vollständige Vierfeldertafel
- verfahren: Ränder eintragen, Felder als Differenzen
- fehlerquelle: 0,18 als P(nicht G) lesen

### 2025MerhoehtBStochastikWTR1-1a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: 72 % jünger als 50 Jahre; 18 % jünger als 50 und nicht in einer Großstadt; 75 % in einer Großstadt
- gesucht: vollständige Vierfeldertafel
- verfahren: Ränder eintragen, Felder als Differenzen
- fehlerquelle: 0,18 als P(nicht G) lesen

### 2024MgrundlegendBStochastikWTR1-1b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: 60 % Treuekunden, 20 % Morgenkunden, P(nicht T ∩ M) = 0,05
- gesucht: vollständige Vierfeldertafel
- verfahren: Ränder eintragen, Felder als Differenzen
- fehlerquelle: 0,05 als P(T ∩ M) eintragen

### 2024MgrundlegendBStochastikWTR2-1b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 4 · format Tabelle|Kurzantwort · antwort Tabelle
- gegeben: P(L) = 0,56, P(D) = 0,33, P(nicht L ∩ nicht D) = 0,28
- gesucht: vollständige Vierfeldertafel und P(Laptop, aber kein Desktop-PC)
- verfahren: Felder aus Rändern und 0,28, Feld ablesen
- fehlerquelle: 0,28 als P(nicht L) eintragen

### 2019MgrundlegendBStochastikWTR3-1a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 3 · format Tabelle · antwort Tabelle
- gegeben: Befragung von 2 360 Männern und 2 200 Frauen (Glücksspielteilnahme): 2,5 % der Männer und 0,5 % der Frauen mit Anzeichen spielsüchtigen Verhaltens; M: Person ist ein Mann, S: Anzeichen spielsüchtigen Verhaltens
- gesucht: vollständig ausgefüllte Vierfeldertafel
- verfahren: Anzahlen je Feld berechnen, Randsummen bilden
- fehlerquelle: Prozentangaben direkt als Feldwerte eintragen

### 2019MgrundlegendBStochastikWTR1-1c (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Fahrprüfungen einer Region: 13 879 Prüflinge, 2 482 davon mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; A: Prüfling mindestens 30, B: Prüfung bestanden
- gesucht: Anzahl der Prüflinge unter 30, die nicht bestanden haben
- verfahren: Randsumme der Jüngeren minus Bestandene der Jüngeren
- fehlerquelle: 11 104 − 8 870 (die älteren Bestandenen) angeben

### 2023MgrundlegendBStochastikWTR3-1b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Vierfeldertafel aus a
- gesucht: Wahrscheinlichkeit, dass eine Lehrkraft weiblich ist oder am Gymnasium arbeitet
- verfahren: Eins minus Feld ¬W∩¬G
- fehlerquelle: 72 % + 25 % ohne Abzug des Schnitts

### 2025MgrundlegendBStochastikWTR3-1b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Vierfeldertafel aus a; Aussage: P(entweder in Großstadt oder nicht jünger als 50) < 60 %
- gesucht: Beurteilung
- verfahren: die beiden passenden Felder addieren
- fehlerquelle: einschließendes Oder rechnen (0,75 + 0,28 − 0,21 = 0,82)

Nur außerhalb von „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ genannt, nicht aufgenommen: 2021MgrundlegendBStochastikWTR3-1a

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
