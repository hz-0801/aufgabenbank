# Mappe: rekonstruktion-von-bestaenden

Eintrag: hz-0801/mathe-nachhilfe, katalog/rekonstruktion-von-bestaenden.md
Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26T16:47:30+02:00, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:43 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Rekonstruktion von Beständen
 3
 4  ### Verortung
 5  Das Integral als wiedergewonnener Bestand: aus einer Änderungsrate (Zufluss, Geschwindigkeit, Melderate) und einem Anfangsbestand den Bestand rekonstruieren – neuer Bestand gleich alter Bestand plus I … (gekürzt, 2518 Zeichen)
 6  [GOST] Q2, 2. Kurshalbjahr „Analysis; Stochastik“ (BB S. 25–26), Grund- und Leistungskursfach, zwei eigene Zeilen: L2-Zeile „Bestände aus Änderungsraten und Anfangsbestand berechnen“ mit dem Inhalt „R … (gekürzt, 1060 Zeichen)
 7  [FOS] Kein fhr-Bestand: Die Leitideenprosa des RLP FOS nennt „sowohl funktionale Größen wie Änderungsraten und (re-)konstruierte Bestände“ (Zeilen 903–904 der Textfassung), aber das Pflichtthema 3 „Integralrechnung“ führt keine Bestandszeile, und der fhr-Katalog stellt keine Aufgabe dazu – die fhr-Flächenkette bleibt geometrisch (→ flaecheninhalt-durch-integration.md). themen.csv führt keine fhr-Zeile.
 8  [LS-AA] Qualifikationsphase Kapitel III „Integralrechnung“: 1 Rekonstruieren einer Größe (Zeile 290 der Textfassung) – die erste Lerneinheit des Integralkapitels, vor dem orientierten Flächeninhalt: das Lehrwerk beginnt die Integralrechnung mit dem Bestandsblick. Zuordnung: alle drei Einheiten = QP III 1. Suchprotokoll `_suche_quelle.py --datei ../quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt`: Rekonstruieren über das Kapitelinventar (290, 1684 sinngemäß); Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Bestand aus Rate – berechnen und aufstellen: die Zunahme in einem Zeitraum als Integral der Rate (mit Einheiten: Rate mal Zeit, Minuten gegen Stunden, Faktor Tausend); der Bestand am Ende als Anfan … (gekürzt, 817 Zeichen)
12    Marken: BE Q2 · BB Q2 · GK · Abitur LK
13  2. Rate und Bestand als Paar – begründen: die Rate ist die Ableitung des Bestands – der Bestand wächst genau dort, wo die Rate positiv ist (Vorzeichen über Nullstellen); der größte Bestand liegt an de … (gekürzt, 685 Zeichen)
14    Marken: BE Q2 · BB Q2 · GK · Abitur LK
15  3. Am Ratengraphen – Flächen als Bestände deuten: die Fläche unter dem Ratengraphen ist die Bestandsänderung; zwei Zeitpunkte mit gleichem Bestand heißen gleich große Flächen ober- und unterhalb der A … (gekürzt, 647 Zeichen)
16    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK
17  Warum drei: rechnen (vorwärts und rückwärts), begründen (die Paarbeziehung), deuten am Bild – die Rohdatei trennt die drei Handlungen selbst, und die Folge ist die Lehrwerksfolge (QP III 1 beginnt mit … (gekürzt, 671 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
21  Einheit 1: Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten (4) · Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen (2) · Bestand nach einem Zeitraum aus Anfangsbestand und Integral der Änderungsrate berechnen (2) · Bestandsänderung grafisch als Fläche unter dem Ratengraphen bestimmen (2) · Anfangsbestand aus Endbestand und Fläche unter dem Ableitungsgraphen ermitteln (1) · Zeitpunkt mit gleichem Bestand wie zu Beginn über das Integral der Änderungsrate gleich null untersuchen (1; Ermessen, siehe Offene Punkte) · Zurückgelegte Strecke als Integral der Geschwindigkeit mit Umrechnung der Einheiten berechnen (1) · Zurückgelegte Strecke aus dem Integral der Geschwindigkeit und einer Phase konstanter Geschwindigkeit berechnen (1) — Deutung: Term für einen Bestand aus einer Rate über ein Integral angeben (3) · Gleichung für den Zeitpunkt eines Bestandswerts über ein Integral der Rate angeben (1). Dazu: Fehler finden (den Anfangsbestand vergessen; die Grenzen als Uhrzeiten statt als Modellstunden eingesetzt; den Einheitenfaktor verloren; die Rate über ihren Geltungsbereich hinaus integriert) · Begründen (warum der neue Bestand alter Bestand plus Integral ist; warum die Einheit des Integrals Rate mal Zeit ist).
22  Einheit 2: Zeitraum der Abnahme eines Bestands über Nullstellen und Vorzeichen der Änderungsrate berechnen (1) — Nachweis: Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen (3) · Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen (2) · Zunahme eines Bestands aus dem Vorzeichen der Rate begründen (1) — Deutung: Integralfunktion einer Rate und ihren Grenzwert als Bestand und Endwert im Sachzusammenhang deuten (1). Dazu: Fehler finden (den Hochpunkt der Rate mit dem größten Bestand verwechselt; nur die Ableitung geprüft und den Anfangswert vergessen; die Rate als Bestand gelesen und ihre Monotonie untersucht) · Begründen (warum der Bestand am Vorzeichenwechsel der Rate kippt; warum eine Kandidatenfunktion zwei Prüfungen braucht).
23  Einheit 3: Integral der Differenz zweier Änderungsraten berechnen und als Bestandsdifferenz deuten (1) — Nachweis: Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen (2) · Gleichheit der Flächen unter Eingangs- und Ausgangsrate als gleiche Gesamtzahl im Sachzusammenhang erläutern (1) · Nullstelle eines Differenzintegrals als Zeitpunkt gleicher Strecke deuten und ihre Lage begründen (1). Dazu: Fehler finden (den Zeitpunkt mit gleichem Ratenwert statt gleichem Bestand markiert; die Nullstelle des Differenzintegrals mit dem Schnittpunkt der Raten gleichgesetzt; Teilflächen verglichen, ohne den gemeinsamen Teil zu erwähnen) · Begründen (warum gleiche Bestände gleiche Flächen ober- und unterhalb bedeuten; warum die Streckengleichheit nach dem Geschwindigkeitsschnittpunkt liegt).
24  Zählung: 10 + 5 + 4 = 19 Haupttypen, 18 + 8 + 5 = 31 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 28.09.2026: Pool 2017 erhöht Teil B; nachgezogen 2026-09-29 um die Katalogzeile des CAS-Nachtrags: Pool 2017 grundlegend Teil B CAS).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Bestimmte Integrale berechnen (Stammfunktion, Hauptsatz, auch mit Rechner) – das Rechnen in Einheit eins. Sek-II-Nachbarthema stammfunktion-und-hauptsatz.md. [GOST Q2 L4; Rohdatei-Fehlerquelle „Kettenfaktor beim Integrieren vergessen“, abi 2026-bb-ea-B2.2g]
29  - Die Rate als Ableitung lesen: momentane Änderungsrate im Sachzusammenhang – die Paarbeziehung in Einheit zwei. Sek-II-Nachbarthema ableitung-und-aenderungsrate.md. [GOST Q1 „Ableitung als lokale Änderungsrate“; iqb 2018MgrundlegendAAnalysis2-a]
30  - Vorzeichen einer Funktion über Nullstellen bestimmen – die Begründungen in Einheit zwei. Sek-II-Nachbarthema funktionsklassen-und-eigenschaften.md Einheit zwei. [Rohdatei-Fehlerquelle „Hochpunkt der Rate mit dem größten Bestand verwechselt“, iqb 2021MgrundlegendBAnalysisWTR-2b]
31  - Einheiten umrechnen: Liter, Kilogramm, Kilometer, Minuten und Stunden, Faktor Tausend – die Sachdeutungen in Einheit eins. Sek-I-Thema einheiten.md. [Rohdatei-Fehlerquelle „Faktor ein Sechzigstel vergessen“, iqb 2022MerhoehtBAnalysisWTR1-1c]
32  - Rate mal Zeit als Menge deuten (je-desto, proportionale Grundvorstellung) – der Einstieg aller Einheiten. Sek-I-Thema zuordnungen.md. [RLP Gleichungen und Funktionen; iqb 2024MgrundlegendBAnalysisWTR2-2d]
33  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
34  - „Bestand oder Rate?“ – zu Größen mit Einheit ankreuzen, ob sie einen Bestand (Liter, Meter, Anzahl) oder eine Rate (Liter je Stunde, Meter je Sekunde) beschreiben; nichts rechnen. Vor Einheit eins. [Rohdatei-Fehlerquelle „die Rate als Volumen gelesen“, iqb 2018MgrundlegendAAnalysis2-a]
35  - „Was war schon da?“ – zu Aufgabentexten ankreuzen, ob ein Anfangsbestand genannt ist und ob er in die Rechnung gehört; nichts rechnen. Vor Einheit eins. [Rohdatei-Fehlerquelle „Anfangsbestand vergessen“, iqb 2018MgrundlegendAAnalysis2-b, 2021MgrundlegendBAnalysisWTR-2d]
36  - „Wo kippt der Bestand?“ – an Ratengraphen ankreuzen, wo der Bestand wächst, fällt und am größten ist; nichts rechnen. Vor Einheit zwei. [Rohdatei-Fehlerquelle „Hochpunkt statt Nullstelle“, abi 2023-bebb-lk-B2.2d]
37
38  ### Merkkasten
39  Einheit 1 (Bestand aus Rate):
40      Neuer Bestand = alter Bestand + Integral der Rate über den Zeitraum; die Zunahme allein ist das Integral.
41        Anfang zwei Liter, Rate f(t) = −t · (t − 4): der Behälter enthält sieben Liter, wenn 2 + Integral bis t über f gleich 7 ist.
42      Einheiten: Rate mal Zeit gibt die Menge – Liter je Stunde mal Stunden, Meter je Sekunde mal Sekunden; Zeiteinheiten vorher angleichen.
43      Mittlere Änderungsrate: Zunahme geteilt durch die Zeitspanne.
44      Grenzen sind Modellzeiten, keine Uhrzeiten – erst umrechnen, dann integrieren.
45      Auswendig (Teil A): „Neuer Bestand = alter Bestand + Integral“ – begründetes Ermessen: die Anlage nennt Bestände nicht, die Teil-A-Zeilen 2018MgrundlegendAAnalysis2-b und 2021MerhoehtAAnalysis13-c verlangen den Ansatz ohne Rechner.
46      Formelsammlung: keine – Bestandsformeln stehen nicht in der Formelsammlung – [FS] offen
47  Quelle: eigene Formulierung nach [GOST Q2 L2] „Bestände aus Änderungsraten und Anfangsbestand berechnen“; Zahlenbeispiel aus dem Pool (2018MgrundlegendAAnalysis2-b, wörtlich); [LS-AA QP III 1].
48  Einheit 2 (Rate und Bestand als Paar):
49      Die Rate ist die Ableitung des Bestands: der Bestand wächst genau dort, wo die Rate positiv ist, und fällt, wo sie negativ ist.
50      Größter Bestand: an der Nullstelle der Rate mit Wechsel von plus nach minus – nicht am Hochpunkt der Rate (dort ist nur das Wachsen am schnellsten).
51      Kandidat prüfen: eine Funktion beschreibt den Bestand, wenn ihre Ableitung die Rate ist und ihr Anfangswert stimmt – beides prüfen, dann Endwerte nachrechnen.
52      Auswendig (Teil A): „Die Rate ist die Ableitung des Bestands“ und „Größter Bestand“ – begründetes Ermessen: die Anlage nennt Bestände nicht, die Teil-A-Zeile 2018MgrundlegendAAnalysis2-a verlangt die Vorzeichenbegründung ohne Rechner.
53      Formelsammlung: keine – [FS] offen
54  Quelle: eigene Formulierung nach [GOST Q2 L4] „das bestimmte Integral deuten, insbesondere als (re-)konstruierten Bestand“; ohne Zahlenbeispiel (die Regeln sind termfrei); [LS-AA QP III 1].
55  Einheit 3 (Am Ratengraphen):
56      Die Fläche unter dem Ratengraphen ist die Bestandsänderung – oberhalb der Achse kommt dazu, unterhalb geht weg.
57      Gleicher Bestand zu zwei Zeitpunkten: die Fläche über der Achse bis zur Nullstelle und die Fläche unter der Achse danach sind gleich groß – markieren, vergleichen, begründen.
58      Zwei Raten nebeneinander: das Integral der Differenz ist der Unterschied der Bestände (bei gleichem Start); die Flächen unter Eingangs- und Ausgangsrate sind die Gesamtzahlen.
59      Auswendig (Teil A): keine – die Bildarbeit dieses Kastens stellt der Pool in Teil B mit Rechner; sitzen muss die Bilanzvorstellung (Kasten fünf von flaecheninhalt-durch-integration.md).
60      Formelsammlung: keine – [FS] offen
61  Quelle: eigene Formulierung nach [GOST Q2 L4] und der Poolpraxis (Rohdatei); ohne Zahlenbeispiel (Bildarbeit); [LS-AA QP III 1 und 2 sinngemäß].
62
63  ### Typische Fehler
64  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 27 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Didaktik der Bestandsrekonstruktion, die Muster sind allein aus den Katalogzeilen belegt.
65  - Den Anfangsbestand vergessen: das Integral als Endbestand gedeutet, die Anfangshöhe weggelassen, die Bestandsgleichung ohne den Startwert angesetzt. [iqb 2021MgrundlegendBAnalysisWTR-2d, 2026MerhoehtBAnalysisMMS2-1d, 2018MgrundlegendAAnalysis2-b]
66  - Hochpunkt der Rate mit größtem Bestand verwechselt: das Maximum der Rate statt der Nullstelle mit Vorzeichenwechsel genommen. [abi 2023-bebb-lk-B2.2d; iqb 2023MerhoehtBAnalysisWTR1-1d, 2021MgrundlegendBAnalysisWTR-2b]
67  - Rate und Bestand vertauscht: die Rate als Volumen gelesen und ihre Monotonie untersucht, die Differenz zweier Ratenwerte statt der Fläche genommen, das Integral als Höhe statt als Höhenunterschied gedeutet. [iqb 2018MgrundlegendAAnalysis2-a, 2021MgrundlegendBAnalysisWTR-2c; abi 2019-be-gk-B2.1g]
68  - Kandidat halb geprüft: nur die Ableitung verglichen und den Anfangswert vergessen. [abi 2023-bebb-lk-B2.2e; iqb 2023MerhoehtBAnalysisWTR1-1e]
69  - Grenzen und Geltungsbereiche: Uhrzeiten statt Modellstunden eingesetzt, die Rate über ihren Geltungsbereich hinaus integriert, die falsche Ratenfunktion oder die falschen Grenzen gewählt, das Integral erst ab dem Pumpenstart laufen lassen. [abi 2023-bebb-lk-B2.2f, 2024-bebb-lk-B2.2i, 2025-bebb-lk-B2.1h; iqb 2023MerhoehtBAnalysisWTR1-1f, 2024MgrundlegendBAnalysisWTR2-2d, 2024MerhoehtBAnalysisWTR2-2d, 2021MerhoehtAAnalysis13-c, 2025MerhoehtBAnalysisMMS1-2d]
70  - Einheiten und Faktoren: den Umrechnungsfaktor der Zeit oder den Faktor Tausend vergessen, den Kettenfaktor beim Integrieren verloren, den Abpumpterm falsch aufgesetzt. [iqb 2022MerhoehtBAnalysisWTR1-1c, 2026MerhoehtBAnalysisWTR1-2b; abi 2026-bb-ea-B2.2g, 2025-bebb-lk-B2.1h]
71  - Bildargumente verfehlt: den Zeitpunkt mit gleichem Ratenwert statt gleicher Staulänge markiert, die Flächen addiert statt subtrahiert, Teilflächen verglichen ohne den gemeinsamen Teil, die Nullstelle des Differenzintegrals als Zeitpunkt gleicher Geschwindigkeit gedeutet. [abi 2023-bebb-lk-B2.2g; iqb 2023MerhoehtBAnalysisWTR1-1g, 2024MgrundlegendBAnalysisWTR1-2d, 2026MerhoehtBAnalysisMMS1-1g, 2024MgrundlegendBAnalysisWTR2-2e]
72
73  ### Für schwache Schüler
74  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: das ganze Thema – beide Planzeilen (L2 „Bestände aus Änderungsraten und Anfangsbestand berechnen“, L4 „das bestimmte Integral deuten, insbesondere als (re-)konstruierten Bestand“) stehen ohne LK-Zusatz im Kern der Q2; Einheit 1 und 2 an ganzrationalen Raten sind der Pflichtkern, die Bildarbeit der Einheit 3 gehört dazu, sobald der Ratengraph vorliegt. Ohne Hilfsmittel: die Anlage nennt Bestände nicht – sitzen müssen der Ansatz „alter Bestand plus Integral“ und die Vorzeichenbegründung (Teil-A-Belege 2018MgrundlegendAAnalysis2-a/b, 2021MerhoehtAAnalysis13-c). RLP FOS (fhr): kein Stoff. Niveaustufe H der E-Phase [RLP H]: kein Posten – die Sek-I-Pläne kennen das Integral nicht; Rate mal Zeit (zuordnungen.md) ist Blatt-0-Stoff. Vorrat: die Terme mit Abpumpphase und die Lagevergleiche der Einheit 3 nach dem Niveau der Rohdatei. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt die Bestandsdeutung des Integrals unter Analysis – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
75  Grundvorstellung (Blatt 0) [GOST Q2 L4, MO]: Die Badewanne: der Bestand ist, was drin ist; die Rate ist, was je Minute dazukommt oder abfließt. „Hier ist der Graph einer Zuflussrate über der Zeit, kein Term. Lege den Finger auf einen Zeitpunkt: fließt gerade Wasser hinein oder heraus – woran siehst du das? Wird das Wasser in der Wanne gerade mehr oder weniger? Wann ist am meisten Wasser drin – dort, wo am stärksten einläuft, oder dort, wo der Zulauf auf null fällt? Und wenn zu Beginn schon drei Eimer drin waren: ändert das den Verlauf deiner Antwort oder nur die Startmenge?“ Wer Rate und Bestand verwechselt oder den Anfangsbestand vergisst, braucht das vor jeder Rechnung: erst die Rollen, dann das Integral. Verständnis, nicht Verfahren; amtlich in der Vorstellung („das bestimmte Integral deuten, insbesondere als (re-)konstruierten Bestand“), Ermessen in der Aufgabenform. [MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „das Maximum der Rate mit dem Maximum des Bestands verwechselt“, iqb 2021MgrundlegendBAnalysisWTR-2b; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
76  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
77  - Bestand aus Rate (Einheit 1): „Bestand oder Rate?“ und „Was war schon da?“ ankreuzen (Vorstufe, Grundvorstellung) → die Zunahme als Integral der Rate mit Einheit berechnen und deuten (Grundfall, viermal; abi 2026-bb-ea-B2.2g; iqb 2026MerhoehtBAnalysisWTR1-2b, 2024MgrundlegendBAnalysisWTR2-2d) → den Bestand als Anfang plus Integral berechnen, rückwärts den Anfang aus Endbestand und Fläche (iqb 2021MgrundlegendBAnalysisWTR-2d, 2024MgrundlegendBAnalysisWTR1-2d) → die Änderung grafisch über Kästchen bestimmen (iqb 2021MgrundlegendBAnalysisWTR-2c) → Strecken aus Geschwindigkeiten, mit Einheitenumrechnung und konstanter Phase (iqb 2022MerhoehtBAnalysisWTR1-1c, 2024MgrundlegendBAnalysisWTR2-2d) → Terme und Gleichungen für Bestände angeben: Zielbestand, Wochenzeitraum, Abpumpphase (iqb 2018MgrundlegendAAnalysis2-b, 2021MerhoehtAAnalysis13-c, 2025MerhoehtBAnalysisMMS1-2d; abi 2025-bebb-lk-B2.1h) → Prüfungshöhe: Modellwert gegen Tabellenwert mit prozentualer Abweichung (abi 2024-bebb-lk-B2.2i; iqb 2024MerhoehtBAnalysisWTR2-2d, Niveau II) und die Zunahme samt mittlerer Änderungsrate aus der Bestandsfunktion (abi 2023-bebb-lk-B2.2f; iqb 2023MerhoehtBAnalysisWTR1-1f, Niveau II); fhr-Zielmarke: keine – kein Stoff.
78  - Rate und Bestand als Paar (Einheit 2): „Wo kippt der Bestand?“ ankreuzen (Vorstufe) → das Wachsen aus dem Vorzeichen der Rate begründen (Grundfall, viermal; iqb 2018MgrundlegendAAnalysis2-a) → den Zeitpunkt des größten Bestands über den Vorzeichenwechsel begründen (abi 2023-bebb-lk-B2.2d; iqb 2023MerhoehtBAnalysisWTR1-1d, 2021MgrundlegendBAnalysisWTR-2b) → eine Kandidatenfunktion doppelt prüfen: Ableitung und Anfangswert, dann Endwert bestätigen (abi 2023-bebb-lk-B2.2e; iqb 2023MerhoehtBAnalysisWTR1-1e) → Prüfungshöhe: die Integralfunktion einer Rate samt Grenzwert im Sachzusammenhang deuten (iqb 2026MerhoehtBAnalysisMMS2-1d, Niveau II); fhr-Zielmarke: keine.
79  - Am Ratengraphen (Einheit 3): den Ratengraphen in Bestandssprache lesen (Grundfall, viermal; Vorstufe „Wo kippt der Bestand?“ als Anschluss) → das Integral der Differenz zweier Raten berechnen und als Bestandsunterschied deuten (abi 2019-be-gk-B2.1g) → den Zeitpunkt gleichen Bestands über gleiche Flächen markieren und begründen (abi 2023-bebb-lk-B2.2g; iqb 2023MerhoehtBAnalysisWTR1-1g) → Prüfungshöhe: die Flächengleichheit unter Eingangs- und Ausgangsrate über die Gesamtzahlen erläutern (iqb 2026MerhoehtBAnalysisMMS1-1g, Niveau II) und die Nullstelle des Differenzintegrals gegen den Schnittpunkt der Raten abgrenzen (iqb 2024MgrundlegendBAnalysisWTR2-2e, Niveau III); fhr-Zielmarke: keine.
80
81  ### Prüfungsform (fhr / abi / iqb)
82  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md. Ein fhr-Bestand existiert nicht. Die Rohdatei zählt 31 Zeilen mit 19 Haupttypen (abi 8 Zeilen, 7 Typen; iqb 23 Zeilen, 18 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; das Thema ist selbst der Gegenstand und führt keine Gegenstandsklassen, die Typnamen stehen ohne Präfix).
83  fhr: kein Stoff, keine Zeile – die FOS-Leitideenprosa nennt Bestände nur als Bezugsrahmen, das Pflichtthema 3 bleibt geometrisch.
84  abi (8 Zeilen, 7 Typen; Landeshefte be-gk, bebb-lk, bb-ea 2019–2026) [abi-Katalog]: Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten (2, E1) · je 1: Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen (E2) · Integral der Differenz zweier Änderungsraten berechnen und als Bestandsdifferenz deuten (E3) · Term für einen Bestand aus einer Rate über ein Integral angeben (E1) · Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen (E2) · Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen (E3) · Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen (E1). Muster: Die Bestandskette hängt an einer Teil-B-Sachaufgabe mit Ratenfunktion – der Stau 2023 trägt allein fünf Zeilen (2023-bebb-lk-B2.2d/e/f/g und die Rate aus B2.2a), dazu die Bäume 2019 (2019-be-gk-B2.1g), die Lesebestätigungen 2024 (2024-bebb-lk-B2.2i), das Regenbecken 2025 (2025-bebb-lk-B2.1h) und die Wassermenge 2026 (2026-bb-ea-B2.2g). Sieben der 8 Zeilen sind wortgleiche Pooldubletten (alle außer 2019-be-gk-B2.1g), keine abgewandelt. Niveau II 5, III 3.
85  iqb (23 Zeilen, 18 Typen; Pool 2017–2026, grundlegend 9 und erhöht 14 Zeilen, Teil A 3 und Teil B 20 Zeilen, davon 3 MMS und 1 CAS) [iqb-Katalog]: Bestand nach einem Zeitraum aus Anfangsbestand und Integral der Änderungsrate berechnen (2, E1) · Bestandsänderung grafisch als Fläche unter dem Ratengraphen bestimmen (2, E1) · Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten (2, E1) · Term für einen Bestand aus einer Rate über ein Integral angeben (2, E1) · Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen (2, E2) · je 1: Anfangsbestand aus Endbestand und Fläche unter dem Ableitungsgraphen ermitteln (E1) · Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen (E2) · Gleichheit der Flächen unter Eingangs- und Ausgangsrate als gleiche Gesamtzahl im Sachzusammenhang erläutern (E3) · Gleichung für den Zeitpunkt eines Bestandswerts über ein Integral der Rate angeben (E1) · Integralfunktion einer Rate und ihren Grenzwert als Bestand und Endwert im Sachzusammenhang deuten (E2) · Nullstelle eines Differenzintegrals als Zeitpunkt gleicher Strecke deuten und ihre Lage begründen (E3) · Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen (E3) · Zeitpunkt mit gleichem Bestand wie zu Beginn über das Integral der Änderungsrate gleich null untersuchen (E1) · Zeitraum der Abnahme eines Bestands über Nullstellen und Vorzeichen der Änderungsrate berechnen (E2) · Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen (E1) · Zunahme eines Bestands aus dem Vorzeichen der Rate begründen (E2) · Zurückgelegte Strecke als Integral der Geschwindigkeit mit Umrechnung der Einheiten berechnen (E1) · Zurückgelegte Strecke aus dem Integral der Geschwindigkeit und einer Phase konstanter Geschwindigkeit berechnen (E1). Muster: Der Pool stellt die Bestandskette in fast jedem Jahrgang – das Wasserbecken 2017 mit Zeitraum der Abnahme, Anfangsvolumen und der Frage nach einem Zeitpunkt gleichen Volumens über das Integral gleich null (2017MerhoehtBAnalysisWTR1-2b, 2017MerhoehtBAnalysisWTR1-2c, 2017MerhoehtBAnalysisWTR1-2d), im CAS-Stapel 2017 grundlegend die Temperatur aus einem abgebildeten Ratengraphen – die Änderung der ersten vier Minuten als Fläche nähern, Zu- oder Abnahme angeben und einen möglichen Temperaturverlauf skizzieren (2017MgrundlegendBAnalysisCAS-2e, fünf Punkte, Niveau III), Behälter mit Zuflussrate in Teil A (2018MgrundlegendAAnalysis2-a/b), infizierte Computer (2021MerhoehtAAnalysis13-c), der Glyzerintank (2021MgrundlegendBAnalysisWTR-2b/2c/2d), die ICE-Strecke (2022MerhoehtBAnalysisWTR1-1c), der Stau (2023MerhoehtBAnalysisWTR1-1d/e/f/g), Radfahrer und CO₂-Raum 2024 (2024MgrundlegendBAnalysisWTR1-2d, 2-2d/2e, 2024MerhoehtBAnalysisWTR2-2d), Regenbecken 2025 (2025MerhoehtBAnalysisMMS1-2d), Gäste und Pflanze 2026 (2026MerhoehtBAnalysisMMS1-1g, MMS2-1d) und die Wassermenge 2026 (2026MerhoehtBAnalysisWTR1-2b). Sieben Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste), keine abgewandelt. Niveau I 1, II 14, III 8.
86  Zielmarke: Einheit 1 – abi: Modellwert gegen Tabellenwert mit Abweichung (2024-bebb-lk-B2.2i, Niveau II); iqb: der Bestandsterm mit Abpumpphase (2025MerhoehtBAnalysisMMS1-2d, Niveau III). Einheit 2 – abi: die Kandidatenprüfung mit Endwertbestätigung (2023-bebb-lk-B2.2e, Niveau II); iqb: die Integralfunktion mit Grenzwertdeutung (2026MerhoehtBAnalysisMMS2-1d, Niveau II). Einheit 3 – abi: der Höhenunterschied zweier Bäume aus dem Differenzintegral (2019-be-gk-B2.1g, Niveau III); iqb: die Lage der Streckengleichheit zum Geschwindigkeitsschnittpunkt (2024MgrundlegendBAnalysisWTR2-2e, Niveau III). fhr: keine (kein Bestand).
````

## 2 Originale (22)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2023-bebb-lk-B2.2d (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 2 · format Kurzantwort|Begründung · antwort Text
- gegeben: f wie in a mit Nullstellen 0, 8/5, 4
- gesucht: Zeitpunkt des längsten Staus mit Begründung
- verfahren: Bestand wächst genau bei positiver Rate, also bis zur Nullstelle mit Vorzeichenwechsel
- fehlerquelle: Hochpunkt von f (stärkste Zunahme) mit dem längsten Stau verwechseln

### 2019-be-gk-B2.1g (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 6 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Graphen von g'(t) = −6t² + 60t und h'(t) = −0,4t³ + 40t schließen im I. Quadranten zwei Teilflächen ein; Intervall I = [0; 5]; aus d: beide Bäume starten mit Höhe 0, aus f: Schnittstelle der Graphen bei t = 5
- gesucht: Flächeninhalt der Teilfläche in [0; 5]; Interpretation im Sachzusammenhang unter Einbeziehung von d und f
- verfahren: Auf [0; 5] gilt g' ≥ h'; Integral der Differenz 0,4t³ − 6t² + 20t von 0 bis 5 = 62,5; Deutung: Integral der Geschwindigkeitsdifferenz = Höhenunterschied, da beide bei 0 starten
- fehlerquelle: das Integral als Höhe eines Baums statt als Höhenunterschied deuten

### 2024-bebb-lk-B2.2i (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: k wie in b; Tabellenwerte 4364 (10:00 Uhr) und 7572 (15:00 Uhr)
- gesucht: Anzahl der Lesebestätigungen von 10:00 bis 15:00 Uhr laut Modell; prozentuale Abweichung vom Tabellenwert
- verfahren: Integral über v von 3 bis 8, Differenz der Tabellenwerte, Quotient
- fehlerquelle: Integral über u statt v oder Grenzen 10 bis 15

### 2025-bebb-lk-B2.1h (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 3 · format Kurzantwort · antwort Term
- gegeben: Becken zu Beginn mit 186 m³ gefüllt; nach 3,5 Stunden wird eine Pumpe eingeschaltet, die bis zum Ende des Zeitraums mit konstanter Rate abpumpt; Zufluss weiterhin r
- gesucht: Term für das Wasservolumen zu einem beliebigen Zeitpunkt t nach dem Einschalten der Pumpe
- verfahren: Anfangswert plus Integral der Zuflussrate minus Pumpmenge seit 3,5 h
- fehlerquelle: Pumpmenge als p · t ansetzen; Integral erst ab 3,5 laufen lassen

### 2026-bb-ea-B2.2g (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 4 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: h wie in a; Integral von 5 bis 9 über h(x) dx
- gesucht: Wert des Integrals und seine Bedeutung
- verfahren: Stammfunktion, Einsetzen, als Wassermenge deuten
- fehlerquelle: Kettenfaktor 3/π beim Integrieren vergessen

### 2017MerhoehtBAnalysisWTR1-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Für ein anderes Becken beschreibt g(t) = 0,4 · (2t^3 − 39t^2 + 180t) für 0 <= t <= 15 die momentane Änderungsrate des Wasservolumens in m^3/h, t in Stunden seit Beobachtungsbeginn; G(t) = 0,2 · (t^4 − 26t^3 + 180t^2) ist eine Stammfunktion von g
- gesucht: rechnerisch der Zeitraum, in dem das Volumen des Wassers abnimmt
- verfahren: g(t) = 0 ⇔ 2t · (t^2 − 19,5t + 90) = 0 ⇔ t = 0, 7,5 oder 12; mit einem Testwert (g(10) < 0) das Intervall mit negativer Rate bestimmen
- fehlerquelle: den Zeitraum mit fallender Rate (g' < 0) statt negativer Rate angeben

### 2017MerhoehtBAnalysisWTR1-2c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Für ein anderes Becken beschreibt g(t) = 0,4 · (2t^3 − 39t^2 + 180t) für 0 <= t <= 15 die momentane Änderungsrate des Wasservolumens in m^3/h, t in Stunden seit Beobachtungsbeginn; G(t) = 0,2 · (t^4 − 26t^3 + 180t^2) ist eine Stammfunktion von g; drei Stunden nach Beobachtungsbeginn sind im Becken 350 m^3 Wasser enthalten
- gesucht: Volumen des Wassers zu Beobachtungsbeginn
- verfahren: Die Zunahme von 0 bis 3 als ∫ von 0 bis 3 g(t) dt = G(3) − G(0) berechnen und von 350 abziehen
- fehlerquelle: die Zunahme zu 350 addieren statt abzuziehen

### 2017MerhoehtBAnalysisWTR1-2d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 5 · format Rechnung|Begründung · antwort Text
- gegeben: Für ein anderes Becken beschreibt g(t) = 0,4 · (2t^3 − 39t^2 + 180t) für 0 <= t <= 15 die momentane Änderungsrate des Wasservolumens in m^3/h, t in Stunden seit Beobachtungsbeginn; G(t) = 0,2 · (t^4 − 26t^3 + 180t^2) ist eine Stammfunktion von g
- gesucht: rechnerische Untersuchung, ob es nach Beobachtungsbeginn einen Zeitpunkt gibt, zu dem das Wasservolumen ebenso groß ist wie zu Beobachtungsbeginn
- verfahren: Gleiches Volumen heißt ∫ von 0 bis x g(t) dt = 0, also G(x) − G(0) = 0,2 · x^2 · (x^2 − 26x + 180) = 0; der quadratische Faktor hat keine reelle Nullstelle, es bleibt nur x = 0
- fehlerquelle: g(t) = 0 statt des Integrals gleich null ansetzen

### 2017MgrundlegendBAnalysisCAS-2e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 5 · format Rechnung|Kurzantwort|Zeichnen · antwort Zahl|Text|Grafik
- gegeben: Für einen gesteuerten Temperaturverlauf zeigt der Graph in Abbildung 2 die Änderungsrate der Temperatur in Grad pro Minute in Abhängigkeit von der Zeit in Minuten seit Beginn des Vorgangs; die Rate ist für 0 < t < 4 positiv und für t > 4 negativ
- gesucht: Näherungswert für die Änderung der Temperatur in den ersten vier Minuten und Angabe, ob die Temperatur zu- oder abnimmt; Skizze eines möglichen Temperaturverlaufs für die ersten zwölf Minuten
- verfahren: Fläche zwischen Ratengraph und Zeitachse von 0 bis 4 durch Auszählen der Kästchen abschätzen, positive Rate heißt Zunahme; Skizze: Temperatur steigt bis t = 4 (Hochpunkt), Wendepunkte an den Extremstellen der Rate, danach fallend
- fehlerquelle: den Wert der Rate bei t = 4 als Änderung angeben oder im Temperaturgraphen bei t = 4 einen Tiefpunkt zeichnen

### 2018MgrundlegendAAnalysis2-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Behälter mit 2 Litern zu Beginn; Zuflussrate f(t) = −t · (t − 4) in Litern je Stunde für 0 ≤ t ≤ 5
- gesucht: Begründung, dass das Volumen in den ersten vier Stunden durchgehend zunimmt
- verfahren: Zunahme auf positive Rate zurückführen, Vorzeichen von f auf (0; 4) über die Nullstellen
- fehlerquelle: f als Volumen statt als Rate lesen und Monotonie von f untersuchen

### 2021MerhoehtAAnalysis13-c (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 2 · format Kurzantwort · antwort Term
- gegeben: f(t) Rate in Tausend Computern pro Tag; Zeitraum der zweiten Woche nach der ersten Infizierung
- gesucht: Term für die Anzahl der in diesem Zeitraum infizierten Computer
- verfahren: Integral der Rate von 7 bis 14 mal 1000
- fehlerquelle: Grenzen 8 bis 14 oder Faktor 1000 vergessen

### 2021MgrundlegendBAnalysisWTR-2b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Glyzerintank: f(x) = −5/16 x⁴ + 5x³ beschreibt für 0 ≤ x ≤ 20 die momentane Änderungsrate des Tankinhalts in kg/h, x Zeit in Stunden seit Beobachtungsbeginn; zu Beobachtungsbeginn 1200 kg im Tank; die Abbildung zeigt den Graphen von f; Aussage: Zwölf Stunden nach Beobachtungsbeginn ist die größte Menge Glyzerin im Tank enthalten
- gesucht: Beurteilung der Aussage
- verfahren: Hochpunkt der Rate bei 12 von der Nullstelle der Rate bei 16 unterscheiden
- fehlerquelle: das Maximum der Rate mit dem Maximum des Bestands verwechseln

### 2022MerhoehtBAnalysisWTR1-1c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: f wie in a; erste zwei Minuten
- gesucht: Länge der zurückgelegten Strecke
- verfahren: Integral von 0 bis 2 über f, mit 1/60 in km umrechnen
- fehlerquelle: Faktor 1/60 vergessen (360 km)

### 2023MerhoehtBAnalysisWTR1-1d (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Kurzantwort|Begründung · antwort Text
- gegeben: f wie in a mit Nullstellen 0, 8/5, 4
- gesucht: Zeitpunkt des längsten Staus mit Begründung
- verfahren: Bestand wächst genau bei positiver Rate, also bis zur Nullstelle mit Vorzeichenwechsel
- fehlerquelle: Hochpunkt von f (stärkste Zunahme) mit dem längsten Stau verwechseln

### 2024MgrundlegendBAnalysisWTR1-2d (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 4 · format Rechnung|Zeichnen · antwort Zahl
- gegeben: a(10) = 100 mg/m³; Graph von a' in Abbildung 3
- gesucht: a(0) mit Veranschaulichung in Abbildung 3
- verfahren: Dreiecksfläche unter a' schätzen, von a(10) abziehen
- fehlerquelle: Fläche addieren statt subtrahieren

### 2024MerhoehtBAnalysisWTR2-2d (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: k wie in b; Tabellenwerte 4364 (10:00 Uhr) und 7572 (15:00 Uhr)
- gesucht: Anzahl der Lesebestätigungen von 10:00 bis 15:00 Uhr laut Modell; prozentuale Abweichung vom Tabellenwert
- verfahren: Integral über v von 3 bis 8, Differenz der Tabellenwerte, Quotient
- fehlerquelle: Integral über u statt v oder Grenzen 10 bis 15

### 2025MerhoehtBAnalysisMMS1-2d (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea-mms · punkte 3 · format Kurzantwort · antwort Term
- gegeben: Regenwasser-Auffangbecken: momentane Zuflussrate r(x) = eˣ · f_(2,5)(x) für 0 ≤ x ≤ 5 (f_(2,5) aus der Schar mit k = 2,5), x Zeit in Stunden seit Beginn des Zuflusses, r(x) in m³/h; zu Beginn 186 m³ im Becken; nach 3,5 Stunden pumpt eine Pumpe bis zum Ende des Zeitraums mit konstanter Rate ab; der Zufluss folgt weiter r
- gesucht: Term für das Wasservolumen zu einem beliebigen Zeitpunkt nach dem Einschalten der Pumpe
- verfahren: Anfangsbestand, Integral der Rate und linearen Abpumpterm zusammensetzen
- fehlerquelle: das Integral erst ab 3,5 beginnen lassen und den Zufluss davor vergessen

### 2026MerhoehtBAnalysisMMS1-1g (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 4 · format Begründung · antwort Text
- gegeben: g Eingangsrate, h Ausgangsrate in 1/h auf [0; 12]; die Graphen und die x-Achse schließen die Flächen I (unter g, links vom Schnittpunkt), II (unter beiden) und III (unter h, rechts) ein; außerhalb der Öffnungszeit ist kein Gast im Bad
- gesucht: Erläuterung im Sachzusammenhang, dass I und III gleichen Inhalt haben
- verfahren: Flächen unter g und unter h als Gesamtzahl der eintretenden bzw. gehenden Gäste deuten, beide gleich, gemeinsamer Teil II herausnehmen
- fehlerquelle: Flächen I und III direkt vergleichen, ohne den gemeinsamen Teil II zu erwähnen

### 2026MerhoehtBAnalysisWTR1-2b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: h wie in a; Integral von 5 bis 9 über h(x) dx
- gesucht: Wert des Integrals und seine Bedeutung
- verfahren: Stammfunktion, Einsetzen, als Wassermenge deuten
- fehlerquelle: Kettenfaktor 3/π beim Integrieren vergessen

### 2023-bebb-lk-B2.2e (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Begründung|Rechnung · antwort Text
- gegeben: s(x) = (x/4)² · (4 − x)³ = −1/16x⁵ + 3/4x⁴ − 3x³ + 4x²; Aussage: die Staulänge kann für jeden Zeitpunkt von 06:00 bis 10:00 Uhr durch s angegeben werden
- gesucht: Begründung der Aussage; rechnerische Bestätigung, dass sich der Stau um 10:00 Uhr aufgelöst hat
- verfahren: s' mit f vergleichen und s(0) = 0 prüfen; s(4) berechnen
- fehlerquelle: nur s' = f zeigen, Anfangswert s(0) = 0 vergessen

### 2026MerhoehtBAnalysisMMS2-1d (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 3 · format Kurzantwort · antwort Text
- gegeben: w mit w' = r und w(0) = 0; lim (w(t) + 3) = 27 für t → ∞; Anfangshöhe 3 cm
- gesucht: Bedeutung von w(t) und des Wertes 27 im Sachzusammenhang
- verfahren: w als Integral der Rate ab 0 deuten (Höhenzunahme), w(t) + 3 als Höhe, Grenzwert als Höhe, der sich die Pflanze nähert
- fehlerquelle: w(t) als Höhe der Pflanze deuten (Anfangshöhe 3 cm vergessen)

### 2024MgrundlegendBAnalysisWTR2-2e (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: z mit 0 < z < 10 und ∫_0^z (f(x) − h(x)) dx = 0; x_s aus b
- gesucht: Bedeutung von z und Begründung, dass z > x_s
- verfahren: Integral als Streckendifferenz deuten, Lage aus dem Vorzeichen von f − h
- fehlerquelle: z als Zeitpunkt gleicher Geschwindigkeit deuten (das ist x_s)

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2024MgrundlegendBAnalysisWTR2-2d, 2018MgrundlegendAAnalysis2-b, 2021MgrundlegendBAnalysisWTR-2d, 2021MgrundlegendBAnalysisWTR-2c, 2023MerhoehtBAnalysisWTR1-1e, 2023-bebb-lk-B2.2f, 2023MerhoehtBAnalysisWTR1-1f, 2023-bebb-lk-B2.2g, 2023MerhoehtBAnalysisWTR1-1g

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
