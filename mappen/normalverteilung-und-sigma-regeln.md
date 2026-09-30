# Mappe: normalverteilung-und-sigma-regeln

Eintrag: hz-0801/mathe-nachhilfe, katalog/normalverteilung-und-sigma-regeln.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:10 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Normalverteilung und Sigma-Regeln
 3
 4  ### Verortung
 5  Die Normalverteilung als stetiges Modell: die Gauß-Glocke als Dichtefunktion (μ als Symmetrieachse und Lage des Maximums, σ als Breitenmaß; Wahrscheinlichkeit ist Fläche unter der Dichte, ein Einzelwe … (gekürzt, 1726 Zeichen)
 6  [GOST] Q4, 4. Kurshalbjahr (BB S. 30), nur „Zusätzlich im Leistungskursfach“: L5-Zeilen „exemplarisch diskrete und stetige Zufallsgrößen unterscheiden und die ‚Glockenform‘ als Grundvorstellung von no … (gekürzt, 1773 Zeichen)
 7  [FOS] Kein Stoff: der RLP FOS 2019 führt weder Normalverteilung noch stetige Zufallsgrößen (Suchprotokoll: „Normalverteilung“ und „normalverteilt“ in der Textfassung ohne Treffer); die Stochastik des Pflichtthemas 4 endet bei Erwartungswert und Simulation. Keine fhr-Zeile.
 8  [LS-AA] Qualifikationsphase Kapitel X „Normalverteilung“: 1 „Die Normalverteilung“, 2 „Die Gauß’sche Glockenfunktion“, 3 „Sigma-Regeln“, 4 „Umkehraufgaben zur Normalverteilung“, 5 „Stetige Zufallsgrößen“. Zuordnung: Einheit 1 = X 1, 2 und 5; Einheit 2 = X 3; Einheit 3 = X 4. Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Modell und Glockenkurve: die Dichtefunktion lesen und skizzieren (μ als Symmetrieachse und Maximumsstelle, σ als Breitenmaß – größeres σ macht die Glocke breiter und niedriger, kleineres σ schmaler … (gekürzt, 632 Zeichen)
12    Marken: BE Q4 · BB Q4 · nur LK · Abitur LK
13  2. Wahrscheinlichkeiten berechnen: Intervall- und einseitige Wahrscheinlichkeiten mit dem Rechner, die Sigma-Regeln der Formelsammlung, Symmetrie und Gegenereignis (außerhalb wird halbiert), Sachbedingungen übersetzen („weicht um höchstens … ab“ als symmetrisches Intervall um den Sollwert, diskrete Anzahlen im stetigen Modell über halbe Schritte), Näherungen ohne Rechner (Rechteck unter der Dichte). (Q4 LK; FS-IQB Abschnitt „Sigma-Regeln“) ← Eingabe „normalverteilung wahrscheinlichkeit“, „sigma-regeln“, „intervall normalverteilung“
14    Marken: BE Q4 · BB Q4 · nur LK · Abitur LK
15  3. Umkehraufgaben und Argumente: μ aus einer Wahrscheinlichkeitsvorgabe bei bekanntem σ, Grenzen und Quantile, μ und σ am Graphen der Verteilungsfunktion (die Stelle mit dem Wert ein Halb) und am Dichteterm ablesen ([IQB-VER 4] vorausgesetzt), Argumente über die Parameter (Monotonie in σ, das beste Intervall fester Länge liegt symmetrisch um μ). (Q4 LK; Prüfungshöhe des Pools in Teil B) ← Eingabe „umkehraufgabe normalverteilung“, „mu gesucht“, „quantil“, „parameter ablesen“
16    Marken: BE Q4 · BB Q4 · nur LK · keine Prüfungsaufgabe
17  Warum drei: Das Modellverständnis (sechs Zeilen, alle Deutungs- und Begründungsformen) trägt die hilfsmittelfreien Teil-A-Aufgaben; das Berechnen (acht Zeilen) ist die Rechnerroutine des Teils B; die  … (gekürzt, 768 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; abitur-Typen wörtlich aus abitur/abitur-typen.csv.
21  Einheit 1: kein Berechnungstyp — Nachweis: Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen (2) · Eignung der Normalverteilung trotz negativer Werte im Definitionsbereich begründen (1) — Deutung: Dichtefunktion mit gleichem Erwartungswert und größerer Standardabweichung skizzieren (1) · Dichtefunktionen zu verschobenem Erwartungswert und kleinerer Standardabweichung skizzieren und Wirkung auf eine Wahrscheinlichkeit begründen (1) · Wahrscheinlichkeit eines Einzelwerts einer stetigen Zufallsgröße angeben (1). Dazu: Fehler finden (den Dichtewert als Wahrscheinlichkeit gedeutet; die Glocke breiter, aber gleich hoch gezeichnet – die Fläche wäre größer als eins; bei kleinerem σ die Glocke niedriger statt höher gezeichnet; das Modell wegen einer positiven, aber verschwindend kleinen Wahrscheinlichkeit verworfen) · Begründen (warum die Fläche unter jeder Dichte eins ist; warum ein Einzelwert einer stetigen Zufallsgröße die Wahrscheinlichkeit null hat).
22  Einheit 2: Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen (4) · Wahrscheinlichkeit außerhalb eines symmetrischen Intervalls über die Symmetrie der Normalverteilung berechnen (1) — kein Nachweistyp — Deutung: Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen (2) · Näherung einer Normalverteilungswahrscheinlichkeit über Rechteck und Symmetrie erläutern (1). Dazu: Fehler finden (einseitig statt zweiseitig gerechnet; die Sollwert-Abweichung ohne halbe Schritte übersetzt; außerhalb des symmetrischen Intervalls nicht halbiert; für eine diskrete Anzahl im stetigen Modell die Wahrscheinlichkeit null geantwortet) · Begründen (warum die halben Schritte nötig sind, wenn eine Anzahl stetig modelliert wird; warum die Symmetrie die Außenwahrscheinlichkeit halbiert).
23  Einheit 3: Erwartungswert einer Normalverteilung aus einer Wahrscheinlichkeitsvorgabe ermitteln und weitere Wahrscheinlichkeit berechnen (1) · Parameter aus der Dichtefunktion ablesen und Bedingungen an Wahrscheinlichkeiten der Normalverteilung prüfen (1) · Parameter einer Normalverteilung aus dem Graphen der Verteilungsfunktion ermitteln (1) · Standardabweichung einer Normalverteilung aus einer vorgegebenen Wahrscheinlichkeit bei festem Erwartungswert ermitteln (1; Ermessen, siehe Offene Punkte) — Nachweis: Implikation zweier Wahrscheinlichkeitsbedingungen der Normalverteilung über eine Schranke für σ begründen (1) · Quantil einer Normalverteilung bestimmen und Wahrscheinlichkeit dafür bei einer zweiten Verteilung beurteilen (1) · Maximale Wahrscheinlichkeit eines Intervalls fester Länge über die Lage um den Erwartungswert begründen (1) — kein Deutungstyp. Dazu: Fehler finden (σ falsch aus dem Vorfaktor des Dichteterms gelesen; die Achsenskalierung des Verteilungsfunktions-Graphen übersehen; μ gleich der vorgegebenen Grenze gesetzt; die Monotonie in σ nicht benannt und nur einen Einzelfall gerechnet; die Aufgabe bei unbekanntem μ für unlösbar gehalten) · Begründen (warum die Stelle mit dem Verteilungsfunktionswert ein Halb der Erwartungswert ist; warum kleineres σ die Masse näher an μ zieht).
24  Zählung: 5 + 4 + 7 = 16 Haupttypen, 6 + 8 + 7 = 21 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeile vom 28.09.2026: Pool 2017 erhöht Teil B, CAS).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Erwartungswert und Standardabweichung als Kenngrößen deuten – μ und σ steuern die Glocke in Einheit 1 und 3. Sek-II-Nachbarthema kenngroessen-von-verteilungen.md (dasselbe Bündel). [GOST Q4 LK „Einfluss von Erwartungswert und Standardabweichung“]
29  - Binomialverteilung und ihr Säulendiagramm lesen – der Grenzfall-Gedanke und die Näherung diskreter Anzahlen in Einheit 2. Sek-II-Nachbarthema binomialverteilung.md. [GOST Q4 LK „Normalverteilung als Grenzfall der Binomialverteilung“]
30  - Flächeninhalt unter einem Graphen als Größe deuten – Wahrscheinlichkeit als Fläche unter der Dichte in allen Einheiten. Sek-II-Themen stammfunktion-und-hauptsatz.md, flaecheninhalt-durch-integration.md. [GOST Q2 L2]
31  - Gegenereignis und Prozentrechnung – die Symmetrie- und Außenrechnungen der Einheit 2. Sek-I-Themen wahrscheinlichkeit.md, prozentrechnung.md. [GOST-OHiMi 2.4]
32  - Den Rechner für Verteilungswahrscheinlichkeiten einsetzen – die Teil-B-Rechnungen der Einheiten 2 und 3 (Werkzeugwissen; die Befehle stehen in keiner Formelsammlung). [IQB-STR 1: Teil B mit WTR]
33  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
34  - „Fläche oder Höhe?“ – zu Fragen ankreuzen, ob eine Wahrscheinlichkeit (Fläche unter der Dichte) oder ein Dichtewert (Höhe des Graphen) gemeint ist; nichts rechnen. Vor Einheit 1 und 2. [Rohdatei-Fehlerquelle „Dichtewert als Wahrscheinlichkeit“; iqb 2024MerhoehtAStochastik12-a]
35
36  ### Merkkasten
37  Einheit 1 (Modell und Glockenkurve):
38      Die Glocke: die Dichte ist symmetrisch um μ und hat dort ihr Maximum; σ misst die Breite – größeres σ macht sie breiter und niedriger, kleineres σ schmaler und höher, größeres μ verschiebt sie nach rechts; die Fläche unter jeder Dichte bleibt eins.
39      Fläche, nicht Höhe: Wahrscheinlichkeiten sind Flächen unter der Dichte – der Dichtewert selbst ist keine Wahrscheinlichkeit, und ein einzelner Wert einer stetigen Zufallsgröße hat die Wahrscheinlichkeit null.
40      Modellkritik: die Normalverteilung gibt auch unmöglichen Werten (negativen Füllmengen, absurden Anzahlen) eine positive Wahrscheinlichkeit – die ist verschwindend klein und darum kein Argument gegen das Modell.
41      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] führt im LK-Zusatz „Interpretationen von Darstellungen normalverteilter Zufallsgrößen“; die Teil-A-Zeilen des Themas sind genau diese Deutungen (Belege 2022MerhoehtAStochastik13-b, 2024MerhoehtAStochastik12-a).
42      Formelsammlung: [FS-IQB 1.4] führt die Dichtefunktion der Normalverteilung; die Wirkungsregeln für μ und σ stehen nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
43  Quelle: eigene Formulierung nach [GOST Q4 LK] „Einfluss von Erwartungswert und Standardabweichung auf die Normalverteilung und die graphische Darstellung ihrer Dichtefunktion“ und [GOST-OHiMi 2.4 LK]; ohne Zahlenbeispiel (die Wirkungsregeln sind zahlenfrei; Ermessen); [LS-AA QP X 1–2].
44
45  Einheit 2 (Wahrscheinlichkeiten berechnen):
46      Rechnerweg: Intervallwahrscheinlichkeit mit dem Normalverteilungsbefehl; einseitige Fragen über das Gegenereignis; erst das Intervall aufschreiben, dann rechnen.
47      Übersetzen: „weicht um höchstens k vom Sollwert ab“ ist das symmetrische Intervall um den Sollwert; zählt das Modell eine Anzahl, gehören halbe Schritte an die Grenzen.
48        Beispiel Treuepunkte: Sollwert 19, höchstens 2 daneben heißt 17 bis 21 Punkte – im stetigen Modell das Intervall von 16,5 bis 21,5.
49      Sigma-Regeln: das σ-Intervall um μ trägt etwa 68,3 %, das 2σ-Intervall etwa 95,4 %, das 3σ-Intervall etwa 99,7 % – außerhalb wird über die Symmetrie halbiert.
50      Ohne Rechner: die Fläche unter der Dichte durch ein Rechteck nähern, Symmetrie und Gegenereignis nutzen.
51      Auswendig (Teil A): Sigma-Regeln, Symmetrie-Halbierung und Rechteck-Näherung (Teil-A-Belege 2022MerhoehtAStochastik13-a, 2024MerhoehtAStochastik12-b); der Rechnerweg ist Teil-B-Stoff.
52      Formelsammlung: [FS-IQB] führt einen eigenen Abschnitt „Sigma-Regeln“ mit sechs Näherungen (Textfassung Zeilen 405–412) – in Teil B nachschlagbar, die Halbierungslogik nicht – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
53  Quelle: eigene Formulierung nach [FS-IQB „Sigma-Regeln“] und der Rohdatei; Zahlenbeispiel aus abi 2026-bb-ea-B4h; [LS-AA QP X 3].
54
55  Einheit 3 (Umkehraufgaben und Argumente):
56      Gesucht ist ein Parameter: bei bekanntem σ folgt μ aus einer Unterschreitungswahrscheinlichkeit (Quantil oder systematisches Probieren am Rechner); Grenzen c aus Vorgaben wie „wird mit vorgegebener Wahrscheinlichkeit übertroffen“.
57      Ablesen: am Graphen der Verteilungsfunktion liegt μ an der Stelle mit dem Funktionswert ein Halb, σ folgt aus einem weiteren abgelesenen Punkt; am Dichteterm stehen μ in der Klammer und σ im Nenner der Klammer – auf den Vorfaktor achten.
58        Beispiel: im Term mit ((x − 250)/2)² liest man μ = 250 und σ = 2 ab – nicht den Nenner des Vorfaktors als σ nehmen.
59      Argumente: kleineres σ zieht die Masse näher an μ (Monotonie in σ – benennen, nicht nur einen Einzelfall rechnen); ein Intervall fester Länge hat symmetrisch um μ die größte Wahrscheinlichkeit, unabhängig davon, wo μ liegt.
60      Auswendig (Teil A): das Ablesen von μ und σ an Glocke und Dichteterm – [IQB-VER 4] setzt es auf erhöhtem Niveau voraus; die Rechenwege sind Teil-B-Stoff mit WTR.
61      Formelsammlung: [FS-IQB 1.4] die Dichtefunktion; Verteilungsfunktion und Quantile stehen nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
62  Quelle: eigene Formulierung nach [IQB-VER 4] (Zeilen 146–148, Dichteterm vorausgesetzt) und der Rohdatei; Zahlenbeispiel aus iqb 2025MerhoehtBStochastikWTR1-2a; [LS-AA QP X 4].
63
64  ### Typische Fehler
65  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 20 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
66  - Dichte mit Wahrscheinlichkeit verwechselt: den Dichtewert als Wahrscheinlichkeit angegeben oder gedeutet; für eine über halbe Schritte modellierte Anzahl „Wahrscheinlichkeit null“ geantwortet; das Modell wegen einer positiven, aber verschwindend kleinen Wahrscheinlichkeit verworfen. [abi 2026-bb-ea-B4f, 2026-bb-ea-B4g; iqb 2026MerhoehtBStochastikWTR1-3a, 2026MerhoehtBStochastikWTR1-3b, 2024MerhoehtAStochastik12-a, 2024MerhoehtAStochastik12-b, 2023MerhoehtBStochastikWTR3-2b]
67  - Glocke falsch skizziert: bei größerem σ breiter, aber gleich hoch gezeichnet (die Fläche wäre größer als eins); bei kleinerem σ die Glocke niedriger statt höher. [iqb 2022MerhoehtAStochastik13-b, 2023MerhoehtBStochastikWTR3-2c]
68  - Intervall falsch übersetzt oder gerechnet: die Sollwert-Abweichung ohne halbe Schritte übersetzt; einseitig statt zweiseitig gerechnet; die Außenwahrscheinlichkeit nicht über die Symmetrie halbiert. [abi 2026-bb-ea-B4h; iqb 2026MerhoehtBStochastikWTR1-3c, 2024MerhoehtBStochastikWTR2-2a, 2023MerhoehtBStochastikWTR3-2a, 2022MerhoehtAStochastik13-a]
69  - Parameter falsch abgelesen oder angesetzt: σ aus dem Nenner des Vorfaktors statt aus der Klammer gelesen; die Achsenskalierung des Verteilungsfunktions-Graphen übersehen; μ gleich der vorgegebenen Grenze gesetzt; die Monotonie in σ nicht benannt und nur einen Einzelfall gerechnet; die Aufgabe bei unbekanntem μ für unlösbar gehalten; das Quantil bestimmt, aber die zweite Verteilung nicht herangezogen. [iqb 2025MerhoehtBStochastikWTR1-2a, 2025MerhoehtBStochastikWTR1-2b, 2024MerhoehtBStochastikWTR2-2b, 2024MerhoehtBStochastikWTR2-2c, 2022MerhoehtBStochastikWTR2-3a, 2022MerhoehtBStochastikWTR2-3b]
70
71  ### Für schwache Schüler
72  Mindeststoff (GK-Kern Q2/Q4 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: keiner – das Thema ist LK-Zusatz beider Länder, die Geltungsdateien führen es nur für die beiden Leistungskurs-Zielprüfungen mit „ja“, und der Pool stellt es ausschließlich erhöht; für Grundkursschüler ist das ganze Thema Vorrat (die Grundkurs-Q4-Zeile zu den k-σ-Regeln gehört zum Schätzen aus Stichproben, nicht hierher). RLP FOS (fhr): kein Stoff, keine Zeile. Mindeststoff innerhalb des LK: Einheit 1 vollständig (die hilfsmittelfreien Darstellungsdeutungen der Anlage) und die Grundformen der Einheit 2 (Rechnerweg, Sigma-Regeln, Symmetrie); die Übersetzungsformen der Einheit 2 (halbe Schritte) und die Einheit 3 sind Prüfungshöhe. Niveaustufe H der E-Phase [RLP]: kein Bezug – die Sek-I-Pläne kennen weder stetige Zufallsgrößen noch die Glocke; Blatt-0-Stoff sind Flächendeutung und Gegenereignis. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt die Normalverteilung nach Erinnerung nicht als Kernstoff – deckt sich mit der LK-Einordnung, kein zusätzlicher Posten.
73  Grundvorstellung (Blatt 0) [GOST Q4 LK „Glockenform als Grundvorstellung“, MO]: Die Glocke zeigt, wo die Werte dicht liegen: die meisten nahe beim Erwartungswert, nach außen immer weniger – und Wahrscheinlichkeit ist die Fläche unter der Kurve, nicht ihre Höhe. „Stell dir vor, sehr viele Flaschen einer Abfüllanlage werden gewogen und jede als Punkt auf einer Linie markiert, kein Term. Wo drängen sich die Punkte – und wie sähe der ‚Punkteberg‘ aus, wenn die Anlage genauer eingestellt würde? Was heißt es für den Berg, wenn die Füllmenge im Mittel erhöht wird? Und warum ist die Frage ‚wie wahrscheinlich ist exakt diese eine Füllmenge?‘ anders als die Frage nach ‚zwischen zwei Werten‘?“ Wer die Höhe der Kurve für eine Wahrscheinlichkeit hält oder dem Berg beim Genauerwerden die Höhe lässt, braucht das vor jeder Rechnung: die Fläche ist fest, die Form verteilt sie nur um. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (die „Glockenform“ steht wörtlich im Plan), die Aufgabenform ist Ermessen. [GOST Q4 LK; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquellen „Dichtewert als Wahrscheinlichkeit“, „Glocke breiter, aber gleich hoch“; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
74  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
75  - Modell und Glockenkurve (Einheit 1): „Fläche oder Höhe?“ ankreuzen (Vorstufe, Grundvorstellung) → die Wirkung von μ und σ an einer gegebenen Glocke beschreiben und eine zweite Glocke skizzieren (Grundfall, viermal; iqb 2022MerhoehtAStochastik13-b) → die Wahrscheinlichkeit eines Einzelwerts angeben und begründen (iqb 2024MerhoehtAStochastik12-a, Teil A) → die Modellkritik führen: vernachlässigbare Wahrscheinlichkeit unmöglicher Werte (abi 2026-bb-ea-B4g, iqb 2023MerhoehtBStochastikWTR3-2b, 2026MerhoehtBStochastikWTR1-3b) → Prüfungshöhe: zu zwei Änderungsvorschlägen je eine Dichte skizzieren und die Wirkung auf eine Wahrscheinlichkeit über die Fläche begründen (iqb 2023MerhoehtBStochastikWTR3-2c, sechs Punkte).
76  - Wahrscheinlichkeiten berechnen (Einheit 2): „Wörtlich oder übersetzt?“ – zu Sachbedingungen ankreuzen, ob das Intervall direkt dasteht oder erst zu übersetzen ist (Abweichung vom Sollwert, Anzahl mit halben Schritten); nichts rechnen (Vorstufe) → Intervall- und einseitige Wahrscheinlichkeiten mit dem Rechner (Grundfall, viermal; iqb 2023MerhoehtBStochastikWTR3-2a, 2024MerhoehtBStochastikWTR2-2a) → mit den Sigma-Regeln und der Symmetrie ohne Rechner: außerhalb halbieren (iqb 2022MerhoehtAStochastik13-a, Teil A) → die Anzahl im stetigen Modell: halbe Schritte an die Grenzen (abi 2026-bb-ea-B4f, iqb 2026MerhoehtBStochastikWTR1-3a) → die Sachbedingung übersetzen und mit der Schranke vergleichen (abi 2026-bb-ea-B4h, iqb 2026MerhoehtBStochastikWTR1-3c, Niveau III) → Prüfungshöhe: eine vorgelegte Näherungsrechnung über Rechteck, Symmetrie und Gegenereignis erläutern (iqb 2024MerhoehtAStochastik12-b, Teil A).
77  - Umkehraufgaben und Argumente (Einheit 3): „Vorwärts oder Umkehraufgabe?“ – ankreuzen, ob eine Wahrscheinlichkeit gesucht ist (Parameter gegeben) oder ein Parameter bzw. eine Grenze (Wahrscheinlichkeit gegeben); nichts rechnen (Vorstufe) → μ und σ ablesen: Verteilungsfunktion an der Halbwertsstelle, Dichteterm mit Blick auf den Vorfaktor (iqb 2024MerhoehtBStochastikWTR2-2c, 2025MerhoehtBStochastikWTR1-2a) → μ aus einer Wahrscheinlichkeitsvorgabe bei bekanntem σ, dann weiterrechnen (iqb 2022MerhoehtBStochastikWTR2-3b) → ein Quantil bestimmen und bei einer zweiten Verteilung beurteilen (iqb 2024MerhoehtBStochastikWTR2-2b) → Prüfungshöhe: Implikationen über eine Schranke für σ und das beste Intervall fester Länge begründen (iqb 2025MerhoehtBStochastikWTR1-2b, 2022MerhoehtBStochastikWTR2-3a, Niveau III).
78
79  ### Prüfungsform (fhr / abi / iqb)
80  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md: be-lk und bb-ea „ja“, be-gk und bb-gk „nein“ (abitur-vokabular.md führt das Thema unter „nur auf erhöhtem Niveau geprüft“). Für fhr gibt es keinen Stoff und keine Zeile. Die Rohdatei zählt 21 Zeilen mit 16 Haupttypen (abi 3 Zeilen, 3 Typen; iqb 18 Zeilen, 16 Typen; 3 abitur-Typen in beiden Abiturprofilen), Jahre 2017 und 2022–2026 – das Thema erscheint regelmäßig erst seit dem Pooljahr 2022; die einzige frühere Zeile ist die CAS-Fassung 2017 (seit dem Nachzug 2026-09-28 im Eintrag). Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
81  abi (3 Zeilen, 3 Typen; Landesheft bb-ea 2026) [abi-Katalog]: je 1: Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen (E2) · Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen (E1) · Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen (E2). Muster: Alle drei Zeilen stammen aus einem einzigen Heft (2026 bb-ea, Teil B, Treuepunkte-Kontext) und sind wortgleiche Pooldubletten (2026-bb-ea-B4f, 2026-bb-ea-B4g, 2026-bb-ea-B4h) – im Landesbestand ist das Thema reine Poolware und nur im erhöhten Anforderungsniveau vertreten. Niveau II 2, III 1.
82  iqb (18 Zeilen, 16 Typen; Pool 2017 und 2022–2026, ausschließlich erhöht, Teil A 4 und Teil B 14 Zeilen, davon 1 CAS) [iqb-Katalog]: Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen (3, E2) · je 1: Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen (E1) · Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen (E2) · Dichtefunktion mit gleichem Erwartungswert und größerer Standardabweichung skizzieren (E1) · Dichtefunktionen zu verschobenem Erwartungswert und kleinerer Standardabweichung skizzieren und Wirkung auf eine Wahrscheinlichkeit begründen (E1) · Wahrscheinlichkeit eines Einzelwerts einer stetigen Zufallsgröße angeben (E1) · Eignung der Normalverteilung trotz negativer Werte im Definitionsbereich begründen (E1) · Wahrscheinlichkeit außerhalb eines symmetrischen Intervalls über die Symmetrie der Normalverteilung berechnen (E2) · Näherung einer Normalverteilungswahrscheinlichkeit über Rechteck und Symmetrie erläutern (E2) · Erwartungswert einer Normalverteilung aus einer Wahrscheinlichkeitsvorgabe ermitteln und weitere Wahrscheinlichkeit berechnen (E3) · Parameter aus der Dichtefunktion ablesen und Bedingungen an Wahrscheinlichkeiten der Normalverteilung prüfen (E3) · Parameter einer Normalverteilung aus dem Graphen der Verteilungsfunktion ermitteln (E3) · Standardabweichung einer Normalverteilung aus einer vorgegebenen Wahrscheinlichkeit bei festem Erwartungswert ermitteln (E3) · Quantil einer Normalverteilung bestimmen und Wahrscheinlichkeit dafür bei einer zweiten Verteilung beurteilen (E3) · Implikation zweier Wahrscheinlichkeitsbedingungen der Normalverteilung über eine Schranke für σ begründen (E3) · Maximale Wahrscheinlichkeit eines Intervalls fester Länge über die Lage um den Erwartungswert begründen (E3). Muster: Teil A stellt nur die Darstellungsdeutungen der Einheit 1 und 2 (2022MerhoehtAStochastik13-a und 13-b, 2024MerhoehtAStochastik12-a und 12-b – ein bis vier Punkte, hilfsmittelfrei); Teil B trägt die Rechen- und Umkehrformen mit WTR (zwei bis sechs Punkte, die Füllmengen-Ketten 2023 und 2025 als mehrteilige Aufgaben), seit dem Nachzug 2026-09-28 dazu die älteste Zeile, eine Umkehraufgabe der CAS-Fassung 2017: die Teststreifen, deren Unbrauchbarkeitswahrscheinlichkeit sich halbiert hat – σ aus der Wahrscheinlichkeitsvorgabe bei festem μ (2017MerhoehtBStochastikCAS2-3c, vier Punkte, Anforderungsbereich III, Niveau II). Amtlicher Anforderungsbereich in allen 18 Zeilen (höchster Bereich: I 3, II 8, III 7); Niveau I 3, II 9, III 6. 3 Poolzeilen kehren wortgleich im Landesheft wieder (die Treuepunkte-Kette 2026MerhoehtBStochastikWTR1-3a bis 3c), keine abgewandelt. Kontexte: Füllmengen (Olivenöl, Konfitüre), Wartezeiten, Reifen-Laufleistungen, Treuepunkte, Teststreifen.
83  Zielmarke: Einheit 1 – iqb: die beiden Änderungsvorschläge mit Flächenargument (2023MerhoehtBStochastikWTR3-2c, sechs Punkte, Niveau II) und die Einzelwert-Frage in Teil A (2024MerhoehtAStochastik12-a); abi: das Modellargument (2026-bb-ea-B4g, Niveau II). Einheit 2 – abi und iqb: die Sollwert-Übersetzung mit halben Schritten (2026-bb-ea-B4h, 2026MerhoehtBStochastikWTR1-3c, Niveau III) und die Rechteck-Näherung in Teil A (2024MerhoehtAStochastik12-b, Niveau II). Einheit 3 – iqb: die Implikation über die σ-Schranke (2025MerhoehtBStochastikWTR1-2b, sechs Punkte, Niveau III) und das Intervall fester Länge bei unbekanntem μ (2022MerhoehtBStochastikWTR2-3a, Niveau III).
````

## 2 Originale (21)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2026-bb-ea-B4f (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: X normalverteilt mit μ = 19, σ = 3; P(C = k) = P(k − 0,5 ≤ X ≤ k + 0,5) für k ≥ 1
- gesucht: P(C = 20)
- verfahren: Intervallwahrscheinlichkeit der Normalverteilung
- fehlerquelle: P(X = 20) = 0 antworten

### 2026-bb-ea-B4g (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: C Anzahl der ausgegebenen Treuepunkte bei einem Einkauf von 95 bis 99,99 €; im Modell P(C = 1000) > 0
- gesucht: Begründung, dass dies kein Argument gegen das Modell ist
- verfahren: Wahrscheinlichkeit als verschwindend gering einordnen
- fehlerquelle: das Modell wegen P > 0 verwerfen

### 2026-bb-ea-B4h (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Annahme: mit mindestens 50 % weicht die ausgegebene Anzahl von der dem Warenwert entsprechenden Anzahl um höchstens zwei ab; Einkauf 95 bis 99,99 €, ein Punkt je 5 €
- gesucht: Beurteilung der Annahme
- verfahren: Sollwert 19, Intervall 17 bis 21, Normalverteilung von 16,5 bis 21,5
- fehlerquelle: Intervall 17 bis 21 ohne Stetigkeitskorrektur (≈ 49,5 %)

### 2022MerhoehtAStochastik13-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: A normalverteilt, Dichte in der Abbildung mit Maximum bei 8; P(A in [6; 10]) ≈ 68 %
- gesucht: P(A > 10)
- verfahren: (100 % − 68 %)/2
- fehlerquelle: 32 % angeben (nicht halbieren)

### 2024MerhoehtAStochastik12-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: Graph der Dichtefunktion einer normalverteilten Zufallsgröße X mit Erwartungswert 20 in der Abbildung
- gesucht: Wahrscheinlichkeit, dass X den Wert 14 annimmt
- verfahren: Eigenschaft stetiger Verteilungen
- fehlerquelle: den Dichtewert bei 14 (etwa 0,03) als Wahrscheinlichkeit angeben

### 2017MerhoehtBStochastikCAS2-3c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Die Indikatormenge Z auf den Teststreifen ist normalverteilt; ein Streifen mit weniger als 15 mg ist unbrauchbar; vor der Verbesserung μ = 20 mg und σ = 4,0 mg; durch die Verbesserung wurde die Wahrscheinlichkeit für einen unbrauchbaren Streifen halbiert, μ blieb unverändert
- gesucht: die geänderte Standardabweichung
- verfahren: P(Z < 15) mit σ = 4 berechnen, halbieren und die Gleichung P(Z < 15) = 5,3 % nach σ lösen
- fehlerquelle: σ halbieren statt die Wahrscheinlichkeit

### 2026MerhoehtBStochastikWTR1-3a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: X normalverteilt mit μ = 19, σ = 3; P(C = k) = P(k − 0,5 ≤ X ≤ k + 0,5) für k ≥ 1
- gesucht: P(C = 20)
- verfahren: Intervallwahrscheinlichkeit der Normalverteilung
- fehlerquelle: P(X = 20) = 0 antworten

### 2023MerhoehtBStochastikWTR3-2c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 6 · format Zeichnen|Begründung · antwort Grafik
- gegeben: Vorschlag 1: eingestellte Füllmenge 600,5 ml erhöhen; Vorschlag 2: Genauigkeit erhöhen; Abbildungen 1 und 2 mit der bisherigen Dichtefunktion
- gesucht: je Vorschlag eine passende Dichtefunktion skizzieren und begründen, dass P(X < 600) kleiner wird
- verfahren: Verschiebung bzw. Stauchung der Glocke einzeichnen, Fläche links von 600 vergleichen
- fehlerquelle: bei kleinerem σ die Glocke niedriger statt höher zeichnen

### 2026MerhoehtBStochastikWTR1-3c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Annahme: mit mindestens 50 % weicht die ausgegebene Anzahl von der dem Warenwert entsprechenden Anzahl um höchstens zwei ab; Einkauf 95 bis 99,99 €, ein Punkt je 5 €
- gesucht: Beurteilung der Annahme
- verfahren: Sollwert 19, Intervall 17 bis 21, Normalverteilung von 16,5 bis 21,5
- fehlerquelle: Intervall 17 bis 21 ohne Stetigkeitskorrektur (≈ 49,5 %)

### 2024MerhoehtAStochastik12-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Dichtefunktion von X mit Erwartungswert 20 in der Abbildung; vorgegebene Rechnung P(18 ≤ X ≤ 20) ≈ 2 · 0,06 = 0,12, somit P(|X − 20| > 2) ≈ 1 − 2 · 0,12 = 0,76
- gesucht: Erläuterung der Überlegungen, die zu dieser Bestimmung führen
- verfahren: die Fläche unter der Dichte über [18; 20] durch ein Rechteck der Breite 2 und Höhe 0,06 nähern; Symmetrie liefert dieselbe Fläche über [20; 22]; Gegenereignis
- fehlerquelle: 0,06 als Wahrscheinlichkeit statt als Dichtewert deuten

### 2025MerhoehtBStochastikWTR1-2b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 6 · format Begründung · antwort Text
- gegeben: andere Anlage: Füllmenge normalverteilt mit μ = 250 und unbekanntem σ; Aussage: erfüllt sie Bedingung II (P(Z ≤ 245,5) ≤ 6 %), so auch Bedingung III (P(Z ≤ 241) ≤ 0,2 %)
- gesucht: Begründung, dass die Aussage richtig ist
- verfahren: aus II eine Schranke für σ gewinnen, mit ihr III prüfen
- fehlerquelle: Monotonie in σ nicht benennen (nur den Fall σ = 3 rechnen)

### 2022MerhoehtBStochastikWTR2-3a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 4 · format Begründung|Rechnung · antwort Text
- gegeben: Wartezeit normalverteilt mit σ = 1 min 15 s; Erwartungswert unbekannt
- gesucht: ob ein zweiminütiges Intervall mit Wahrscheinlichkeit mindestens 60 % existiert
- verfahren: Bestes Intervall symmetrisch um μ, Wahrscheinlichkeit mit beliebigem μ berechnen und mit 60 % vergleichen
- fehlerquelle: μ als unbekannt für unlösbar halten

### 2022MerhoehtAStochastik13-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: Dichte von A in der Abbildung; B normalverteilt mit gleichem Erwartungswert und größerer Standardabweichung
- gesucht: Skizze eines möglichen Graphen der Dichte von B in der Abbildung
- verfahren: flachere, breitere Glockenkurve mit Maximum bei 8 einzeichnen
- fehlerquelle: Kurve breiter, aber gleich hoch zeichnen (Fläche größer als 1)

### 2023MerhoehtBStochastikWTR3-2b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Füllmenge nie negativ; Normalverteilung auch für negative Zahlen definiert mit positiven Dichtewerten
- gesucht: Begründung, dass die Normalverteilung dennoch sinnvoll ist
- verfahren: Wahrscheinlichkeit für negative Werte als vernachlässigbar klein einordnen
- fehlerquelle: Dichtewert mit Wahrscheinlichkeit verwechseln

### 2026MerhoehtBStochastikWTR1-3b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: C Anzahl der ausgegebenen Treuepunkte bei einem Einkauf von 95 bis 99,99 €; im Modell P(C = 1000) > 0
- gesucht: Begründung, dass dies kein Argument gegen das Modell ist
- verfahren: Wahrscheinlichkeit als verschwindend gering einordnen
- fehlerquelle: das Modell wegen P > 0 verwerfen

### 2023MerhoehtBStochastikWTR3-2a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Füllmenge normalverteilt mit μ = 600,5 ml, σ = 0,23 ml; A: mehr als 601 ml; B: höchstens 0,5 ml vom Erwartungswert entfernt
- gesucht: P(A), P(B)
- verfahren: Normalverteilung am Rechner
- fehlerquelle: B einseitig als P(X ≤ 601)

### 2024MerhoehtBStochastikWTR2-2a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Laufleistung V der Vorderradreifen normalverteilt mit μ = 6800 km, σ = 530 km
- gesucht: P(Abweichung vom Erwartungswert höchstens 600 km)
- verfahren: Intervall 6200 bis 7400 am Rechner
- fehlerquelle: einseitig P(V ≤ 7400) rechnen

### 2024MerhoehtBStochastikWTR2-2c (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Z ~ N(μ; σ); Abbildung des Graphen von f(x) = P(Z ≤ 1000 · x)
- gesucht: μ und σ in km
- verfahren: μ am Wert 0,5, σ aus einem weiteren abgelesenen Punkt
- fehlerquelle: Skalierung 1000x übersehen (μ = 5,5)

### 2025MerhoehtBStochastikWTR1-2a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 5 · format Rechnung · antwort Text
- gegeben: Füllmenge in g normalverteilt mit φ(x) = 1/(2√(2π)) · e^{−1/2 ((x − 250)/2)²}; Minusabweichung 4,5 g; Bedingungen: I Erwartungswert ≥ 250, II P(Y ≤ 245,5) ≤ 6 %, III P(Y ≤ 241) ≤ 0,2 %
- gesucht: ob jede der drei Bedingungen erfüllt ist
- verfahren: Parameter ablesen, zwei Wahrscheinlichkeiten berechnen
- fehlerquelle: σ = 4 aus dem Nenner 2 im Vorfaktor lesen

### 2022MerhoehtBStochastikWTR2-3b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: P(Y ≤ 3) = 15 %, σ = 1,25
- gesucht: P(Y ≥ 5) unter dieser Annahme
- verfahren: μ aus der Vorgabe ermitteln, dann die Wahrscheinlichkeit berechnen
- fehlerquelle: μ = 3 setzen

### 2024MerhoehtBStochastikWTR2-2b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: V ~ N(6800; 530), H ~ N(4600; 480); Aussage: die Laufleistung, die ein Vorderradreifen mit 90 % übertrifft, unterschreitet ein Hinterradreifen nahezu sicher
- gesucht: Begründung, dass die Aussage wahr ist
- verfahren: c aus P(V > c) = 0,9, dann P(H ≥ c)
- fehlerquelle: c als 90 %-Quantil (7479 km) bestimmen

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
