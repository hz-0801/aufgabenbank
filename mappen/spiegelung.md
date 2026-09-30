# Mappe: spiegelung

Eintrag: hz-0801/mathe-nachhilfe, katalog/spiegelung.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:13 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Spiegelung
 3
 4  ### Verortung
 5  Das Spiegeln im Raum: Punkte spiegeln (an einem Punkt, an einer Ebene über die Lotgerade oder den bekannten Lotfußpunkt, an Koordinatenebenen durch Vorzeichenwechsel), Spiegelebenen und Spiegelgeraden … (gekürzt, 2392 Zeichen)
 6  [GOST] Befund: Der RLP GOST Brandenburg nennt die räumliche Spiegelung in keinem Inhalt – Suchprotokoll `_suche_quelle.py` in `quellen/quelle-rlp-gost-bb-2022-mathematik.txt`: „Spiegel“ 1 Treffer (Zei … (gekürzt, 1404 Zeichen)
 7  [FOS] Kein Treffer: Das Wahlthema 5 „Analytische Geometrie“ des RLP FOS 2019 endet bei Geraden im Raum; Spiegelung und Symmetrieebene kommen im Plan nicht vor – kein fhr-Bestand, keine fhr-Zeile in themen.csv.
 8  [LS-AA] Qualifikationsphase Kapitel VII 4 „Spiegelung und Symmetrie“ (Zeile 349 der Textfassung) – die einzige Lerneinheit des Lehrwerks zum Thema, im Kapitel „Abstände und Winkel“ direkt nach den Abs … (gekürzt, 735 Zeichen)
 9
10  ### Lerneinheiten
11  1. Punkte spiegeln – der Spiegelpunkt: an einem Punkt (Spiegelzentrum plus Verbindungsvektor), an Koordinatenebenen (genau ein Vorzeichen wechselt – gespiegelte Eckpunkte ablesen), an einer Ebene über den bekannten Lotfußpunkt (Verbindungsvektor in Gegenrichtung abtragen) und über die Lotgerade (aufstellen, mit der Ebene schneiden, Parameter verdoppeln); der Punkt mit vorgegebenem Abstandsverhältnis auf der Spiegelachse. (Q3; [IQB-VER 3.2] grundlegend „für Punkte“) ← Eingabe „spiegelpunkt“, „punkt spiegeln“, „spiegelung an ebene“, „punktspiegelung“
12    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
13  2. Spiegelebene und Spiegelgerade bestimmen – die Spiegelfläche als Gesuchtes: die Spiegelebene aus Punkt und Spiegelpunkt (Verbindungsvektor als Normalenvektor, Mittelpunkt in der Ebene), die Spiegel … (gekürzt, 646 Zeichen)
14    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
15  3. Symmetrieebenen von Körpern – Symmetrie erkennen und begründen: die Prüfregel (jeder Eckpunkt wird auf einen Eckpunkt gespiegelt; Punktepaare unterscheiden sich in genau einer Koordinate durch Vorz … (gekürzt, 766 Zeichen)
16    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
17  Warum drei: Das Lehrwerk fasst alles in einer Lerneinheit (QP VII 4), die Rohdatei trennt drei Arbeitsrichtungen – das Bild eines Punktes berechnen (Einheit 1), die Spiegelfläche suchen (Einheit 2), d … (gekürzt, 906 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; die Rohdatei führt keine Nebentypen.
21  Einheit 1: Spiegelpunkt an einem Punkt bestimmen (2) · Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen (2) · Spiegelpunkt an einer Ebene über die Lotgerade bestimmen (2) · Punkt auf der Spiegelachse mit vorgegebenem Abstandsverhältnis zur Spiegelebene bestimmen (1) — kein Nachweistyp — Deutung: Koordinaten gespiegelter Eckpunkte aus den Symmetrieebenen eines Körpers angeben (1). Dazu: Fehler finden (den Verbindungsvektor am Ausgangspunkt statt am Spiegelzentrum abgetragen; beim Lotfußpunkt stehen geblieben statt den Parameter zu verdoppeln; den Lotfußpunkt neu berechnet, obwohl er gegeben ist; in die falsche Richtung abgetragen und den Ausgangspunkt erhalten; an der falschen Symmetrieebene gespiegelt; das Verhältnis vom Punkt statt vom Mittelpunkt aus angesetzt) · Begründen (warum das Spiegeln an einer Koordinatenebene genau ein Vorzeichen wechselt; warum der doppelte Lotparameter den Spiegelpunkt liefert).
22  Einheit 2: Spiegelebene aus Punkt und Spiegelpunkt bestimmen (3) · Spiegelebene zweier sich schneidender Geraden bestimmen (2) — kein Nachweistyp — Deutung: Spiegelgerade einer Geraden an einer Ebene aus Fixpunkt und bekanntem Spiegelpunkt angeben (1) · Spiegelgerade zweier Geraden zeichnen und Punkt der Winkelhalbierenden als Vektorterm angeben (1). Dazu: Fehler finden (den Mittelpunkt nicht in die Ebenengleichung eingesetzt, sondern den Punkt selbst; die Summe der Richtungsvektoren als Richtung der Ebene statt als Normalenvektor genommen; die Spiegelgerade durch Punkt und Spiegelpunkt gelegt – das ist die Lotgerade; die Summe der Ortsvektoren als Winkelhalbierenden-Term angegeben, ohne die Vektoren gleich lang zu machen) · Begründen (warum der Verbindungsvektor von Punkt und Spiegelpunkt Normalenvektor der Spiegelebene ist; warum die Rautendiagonale den Winkel halbiert und die Richtungsvektoren dafür gleich lang sein müssen).
23  Einheit 3: kein Berechnungstyp — Nachweis: Symmetrieebenen eines Körpers aus den Koordinaten begründen (3; Ermessen, siehe Offene Punkte) · Symmetrie einer geraden Pyramide bezüglich einer Koordinatenachse über Grundflächenmittelpunkt und Spitze begründen (3) · Symmetrie zweier Punkte bezüglich einer Koordinatenachse über die Koordinaten begründen (1) · Symmetrieebene eines geraden Prismas über die Symmetrieachse der Grundfläche begründen (1) · Symmetrieebene eines zusammengesetzten Körpers über verschiedene Höhen der Teilkörper ausschließen (1) — Deutung: Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen (6) · Symmetrieebene eines Körpers angeben und ihre Schnittfigur mit dem Körper einzeichnen (1). Dazu: Fehler finden (die waagerechte Ebene durch die Giebelspitzen gewählt; eine Ebene für symmetrisch gehalten, weil die Spitze in ihr liegt; die Diagonalebene mit der falschen Vorzeichenbedingung verwechselt; beim Rechteck eine Diagonalebene angegeben; die Mitte geschätzt statt den Mittelwert der Koordinaten zu bilden; die Symmetrie zur falschen Ebene behauptet; nur einzelne Punktepaare gespiegelt statt allgemein zu begründen; nur einen Parameterwert geprüft) · Begründen (warum eine einzige Punktprobe zum Ausschließen genügt; warum beim geraden Prisma die Ebene durch die Symmetrieachse der Grundfläche senkrecht auf ihr stehen muss).
24  Zählung: 5 + 4 + 7 = 16 Haupttypen, 8 + 7 + 16 = 31 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 28.09.2026: Pool 2017 erhöht Teil B, WTR und CAS; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2018 erhöht und 2017 grundlegend Teil B CAS)).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Verbindungsvektor bilden und an einem Punkt abtragen (Ortsvektor plus Vektor) – die Grundoperation aller Spiegelungen, Einheit 1 und 2. Sek-II-Nachbarthema vektoren-und-rechenoperationen.md (Klarstellung Geometrie: Fertigkeit aus dem Nachbarthema derselben Stufe). [GOST Q3 L3 „Vektoraddition“, „Ortsvektor“; GOST-OHiMi 2.3]
29  - Normalenvektor einer Ebene ablesen und die Lotgerade aufstellen – der Weg über die Lotgerade in Einheit 1, die Spiegelebene in Einheit 2. Sek-II-Nachbarthemen ebenen.md, abstaende.md. [GOST Q3 L3 „Normalenvektor“; GOST-OHiMi 2.3]
30  - Schnittpunkt von Gerade und Ebene berechnen (Einsetzen, Parameter bestimmen) – der Lotfußpunkt in Einheit 1. Sek-II-Nachbarthema schnittmengen.md. [GOST Q3 L3 „Schnittmenge: … einer Geraden und einer Ebene“; IQB-VER 3.2 „Schnittpunkt einer Gerade mit einer Koordinatenebene“ auch grundlegend]
31  - Mittelpunkt einer Strecke berechnen – die Spiegelebene aus Punkt und Spiegelpunkt in Einheit 2, die Mittelwerte der Symmetrieebenen in Einheit 3. Sek-II-Nachbarthema punkte-und-strecken-im-koordinatensystem.md. [GOST-OHiMi 2.3; BE Einführungsphase L2/3]
32  - Beträge von Vektoren vergleichen (gleich lange Richtungsvektoren erkennen oder herstellen) – die Raute der Winkelhalbierenden in Einheit 2. Sek-II-Nachbarthema abstaende.md. [GOST-OHiMi 2.3 „Betrag eines Vektors“]
33  - Achsenspiegelung und Symmetrie ebener Figuren (Spiegelpunkt gleich weit hinter der Achse, Deckabbildung) – die Vorstellung hinter allen drei Einheiten. Sek-I-Thema symmetrie-abbildungen.md. [GOST Eingangsvoraussetzung L3 „Eigenschaften von Figuren mithilfe von Symmetrie“; RLP Raum und Form]
34  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
35  - „Was wird gespiegelt – und woran?“ – zu Aufgaben ankreuzen: Punkt an Punkt, Punkt an Ebene, Gerade an Ebene, Gerade auf Gerade, Körper an Symmetrieebene; nichts rechnen. Vor allen Einheiten. [IQB-VER 3.2; Rohdatei: die fünf Gegenstände der Typenliste; abi 2025-bebb-gk-A1.5a, 2026-bb-gk-B3e]
36  - „Was ist gegeben, was gesucht?“ – ankreuzen, ob das Bild gesucht ist (spiegeln, Einheit eins) oder die Spiegelfläche (rückwärts, Einheit zwei); nichts rechnen. Vor Einheit 1 und 2. [Rohdatei: Typen „Spiegelpunkt … bestimmen“ gegen „Spiegelebene … bestimmen“; iqb 2022MerhoehtAAGLAA212-a]
37  - „Welche Koordinate wechselt?“ – zu Punktepaaren ankreuzen, ob sie sich in genau einer Koordinate unterscheiden (Vorzeichen oder Wert) und zu welcher Ebene sie dann symmetrisch liegen; nichts rechnen. Vor Einheit 1 und 3. [Rohdatei-Fehlerquelle „Symmetrie zur falschen Ebene behaupten“; iqb 2022MerhoehtBAGLAA2WTR2-1a, 2025MerhoehtBAGLAA1WTR-2a]
38
39  ### Merkkasten
40  Einheit 1 (Punkte spiegeln):
41      An einem Punkt: das Spiegelzentrum Q ist Mittelpunkt – der Spiegelpunkt ist Q plus Verbindungsvektor: OP′ = OQ + PQ.
42        P(0 | −1 | 1), Q(2 | 5 | 3): PQ = (2 | 6 | 2), P′(4 | 11 | 5).
43      An Koordinatenebenen: genau ein Vorzeichen wechselt (xy-Ebene: dritte Koordinate, xz-Ebene: zweite, yz-Ebene: erste) – gespiegelte Eckpunkte lassen sich ablesen.
44      Bekannter Lotfußpunkt: ist F der Lotfußpunkt von Q auf der Ebene, liegt der Spiegelpunkt auf der anderen Seite: R = F − FQ (den Verbindungsvektor in Gegenrichtung abtragen).
45        E: x₁ − 3x₂ + 2x₃ = 11, F(5 | 0 | 3) in E, Q(9 | −12 | 11): FQ = (4 | −12 | 8), R(1 | 12 | −5).
46      Über die Lotgerade: die Lotgerade durch P mit dem Normalenvektor aufstellen, den Schnittparameter λ mit der Ebene bestimmen – der Spiegelpunkt liegt bei 2λ.
47        P(−1 | 7 | 2), E: x₁ + 3x₂ = 0: aus (−1 + λ) + 3 · (7 + 3λ) = 0 folgt λ = −2; Spiegelpunkt bei 2λ = −4: P′(−5 | −5 | 2).
48      Auswendig (Teil A): der ganze Kasten – [IQB-VER 3.2] „Spiegelungen an Ebenen … auf grundlegendem Anforderungsniveau für Punkte“ (Teil-A-Belege 2025MgrundlegendAAGLAA213-a, 2026MgrundlegendAAGLAA211-b, 2021MerhoehtAAGLAA211-b); der GOST nennt die Raumspiegelung nicht – begründetes Ermessen mit dem IQB-Beleg.
49      Formelsammlung: keine – [FS-IQB 1.3] führt keine Spiegelformeln – [FS] offen
50  Quelle: eigene Formulierung nach [IQB-VER 3.2] und den Bausteinen aus [GOST-OHiMi 2.3] (Normalenvektor, Schnitt, Vektoraddition); Zahlenbeispiele aus dem Pool (2025MgrundlegendAAGLAA213-a, 2026MgrundlegendAAGLAA211-b, 2021MerhoehtAAGLAA211-b, wörtlich); [LS-AA QP VII 4].
51
52  Einheit 2 (Spiegelebene und Spiegelgerade bestimmen):
53      Aus Punkt und Spiegelpunkt: der Verbindungsvektor PQ ist Normalenvektor der Spiegelebene, der Mittelpunkt M von P und Q liegt in ihr – Konstante über M bestimmen.
54        P(1 | 2 | 3), Q(7 | 2 | 11): PQ = (6 | 0 | 8), also n = (3 | 0 | 4); M(4 | 2 | 7); E: 3x₁ + 4x₃ = 40.
55      Zwei sich schneidende Geraden: sind die Richtungsvektoren gleich lang, halbiert ihre Summe den Winkel und ist Normalenvektor der Ebene, die die eine Gerade auf die andere spiegelt; die Ebene geht durch den Schnittpunkt.
56        Richtungsvektoren (1 | 2 | 0) und (2 | 1 | 0), gleich lang: Summe (3 | 3 | 0); durch den Schnittpunkt (1 | 1 | 1): E: x + y = 2.
57      Spiegelgerade an einer Ebene: der Schnittpunkt der Geraden mit der Ebene bleibt fest (Fixpunkt) – die Spiegelgerade geht durch ihn und den Spiegelpunkt eines weiteren Geradenpunkts.
58      Winkelhalbierende als Raute: gleich lange Vektoren auf beiden Geraden abtragen – die Diagonale des entstehenden Parallelogramms (einer Raute) halbiert den Winkel; ungleiche Vektoren erst auf gleiche Länge skalieren.
59      Auswendig (Teil A): „Aus Punkt und Spiegelpunkt“ – die Bausteine (Normalenvektor, Mittelpunkt) stehen in [GOST-OHiMi 2.3]; der Pool prüft die Konstruktionen in Teil A nur erhöht (Belege 2022MerhoehtAAGLAA212-a, 2023MerhoehtAAGLAA222-b, 2018MerhoehtAAGLAA211-c) – [IQB-VER 3.2] „auf erhöhtem Anforderungsniveau uneingeschränkt“.
60      Formelsammlung: [FS-IQB 1.3] führt die Ebenenformen; Spiegel- und Winkelhalbierendenregeln stehen nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
61  Quelle: eigene Formulierung nach [IQB-VER 3.2] und [GOST-OHiMi 2.3] „Koordinaten- und Normalenform“; Zahlenbeispiele aus dem Pool (2022MerhoehtAAGLAA212-a, 2023MerhoehtAAGLAA222-b, wörtlich); [LS-AA QP VII 4].
62
63  Einheit 3 (Symmetrieebenen von Körpern):
64      Prüfregel: eine Ebene ist Symmetrieebene, wenn sie jeden Eckpunkt auf einen Eckpunkt des Körpers spiegelt – symmetrische Punktepaare unterscheiden sich in genau einer Koordinate: Vorzeichenwechsel (Koordinatenebene) oder gleicher Abstand zum Mittelwert (achsenparallele Ebene).
65      Auswählen und ausschließen: Kandidatengleichungen an Eckenpaaren und Kantenmittelpunkten prüfen; zum Ausschließen genügt ein Gegenbeispiel (eine Punktprobe oder ein Kantenvergleich), zum Begründen müssen alle Eckenpaare stimmen.
66      Mittelwerte: die achsenparallele Symmetrieebene liegt auf dem Mittelwert der Koordinaten der gespiegelten Ecken – auch mit Parameter.
67        A(0 | 0 | 0), B(4 | 0 | 0), C(4 | 6 | 0), D(0 | 6 | 0), gerade Pyramide darüber: Symmetrieebenen x = 2 (Mitte von AB) und y = 3 (Mitte von AD).
68      Gerades Prisma: die Ebene, die die Symmetrieachse der Grundfläche enthält und senkrecht auf der Grundfläche steht, ist Symmetrieebene.
69      Zusammengesetzte Körper: jede Symmetrieebene des Ganzen muss beide Teilkörper spiegeln – verschiedene Höhen oder Formen der Teilkörper schließen sie aus, für jeden Parameterwert.
70      Auswendig (Teil A): „Prüfregel“ und „Mittelwerte“ – begründetes Ermessen: die Anlage nennt die Raumsymmetrie nicht, der Pool prüft sie in Teil A (Belege 2025MerhoehtAAGLAA223-a, 2026MerhoehtAAGLAA223), die Vorstellung ist Sek-I-Bestand ([GOST Eingangsvoraussetzung L3] „Symmetrie“).
71      Formelsammlung: keine – Symmetrieregeln stehen nicht in der Formelsammlung – [FS] offen
72  Quelle: eigene Formulierung nach [GOST Eingangsvoraussetzung L3] „Eigenschaften von Figuren mithilfe von Symmetrie“ und [IQB-VER 3.2]; Zahlenbeispiel aus dem Pool (2025MerhoehtAAGLAA223-a, wörtlich); [LS-AA QP VII 4].
73
74  ### Typische Fehler
75  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 27 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Didaktik der Analytischen Geometrie, die Muster sind allein aus den Katalogzeilen belegt.
76  - Auf halbem Weg stehen geblieben: nur bis zum Lotfußpunkt gerechnet (λ statt 2λ), die Richtung des Normalenvektors falsch; den Lotfußpunkt neu berechnet, obwohl er gegeben ist, oder in die falsche Richtung abgetragen und den Ausgangspunkt zurückerhalten. [abi 2022-bebb-lk-B3g, 2026-bb-gk-A1.2b; iqb 2021MerhoehtAAGLAA211-b, 2026MgrundlegendAAGLAA211-b]
77  - Am falschen Punkt abgetragen: den Verbindungsvektor am Ausgangspunkt statt am Spiegelzentrum angesetzt und das Zentrum selbst erhalten; das Abstandsverhältnis vom Punkt statt vom Mittelpunkt aus gerechnet; Eckpunkte an der falschen Symmetrieebene gespiegelt. [abi 2025-bebb-gk-A1.5a; iqb 2025MgrundlegendAAGLAA213-a, 2022MerhoehtAAGLAA212-b, 2025MerhoehtBAGLAA1WTR-2a]
78  - Spiegelfläche falsch angesetzt: die Summe der Richtungsvektoren als Richtung der Ebene statt als Normalenvektor; den Punkt statt des Mittelpunkts in die Ebenengleichung eingesetzt; die Spiegelebene senkrecht zur Grundebene erzwungen; die Spiegelgerade durch Punkt und Spiegelpunkt gelegt (das ist die Lotgerade); die Summe der Ortsvektoren als Winkelhalbierenden-Term angegeben (Mittelpunkt statt Raute). [abi 2023-bebb-lk-A1.6b, 2026-bb-gk-B3e; iqb 2023MerhoehtAAGLAA222-b, 2022MerhoehtAAGLAA212-a, 2026MgrundlegendBAGLAA2WTR2-1e, 2018MerhoehtAAGLAA211-c, 2024MerhoehtAAGLAA222]
79  - Symmetrieebene falsch gewählt: die waagerechte Ebene durch die Giebelspitzen; eine Ebene, weil die Spitze in ihr liegt; die Diagonalebene mit der falschen Vorzeichenbedingung verwechselt; beim Rechteck eine Diagonalebene angegeben; die Mitte geschätzt statt den Mittelwert zu bilden; die Symmetrie zur falschen Ebene oder Achse behauptet; eine unsymmetrische Richtung übersehen. [abi 2022-bebb-gk-B3e, 2024-bebb-lk-B3b; iqb 2022MgrundlegendBAGLAA2WTR2-1c, 2024MerhoehtBAGLAA2WTR1-1b, 2026MgrundlegendBAGLAA2MMS2-1b, 2025MerhoehtAAGLAA223-a, 2026MerhoehtAAGLAA223, 2022MerhoehtBAGLAA2WTR2-1a, 2019MgrundlegendBAGLAA2WTR2-1b]
80  - Am Beispiel statt allgemein: nur einzelne Punktepaare gespiegelt, ohne allgemeine Begründung; nur ein Paar genannt; nur einen Parameterwert geprüft und die lange Kante übersehen. [iqb 2023MgrundlegendBAGLAA2WTR1-1c, 2026MerhoehtBAGLAA2WTR1-1b, 2025MerhoehtBAGLAA2MMS-1c]
81
82  ### Für schwache Schüler
83  Mindeststoff (GK-Kern Q3 / Niveaustufe H / RLP FOS) [IQB-VER, GOST, FOS]: Die amtliche Stufung kommt aus [IQB-VER 3.2]: grundlegend müssen Spiegelungen an Ebenen „für Punkte“ sitzen – Einheit 1 vollständig (an einem Punkt, an Koordinatenebenen, über Lotfußpunkt und Lotgerade); dazu Einheit 3, die der Pool grundlegend in Teil B prüft (Symmetrieebene auswählen, Schnittfigur, gerades Prisma). Ohne Hilfsmittel (Prüfungsteil A): die Punktspiegelungen (Kasten 1) – die Anlage selbst nennt die Raumspiegelung nicht, der Pool stellt sie in Teil A beider Niveaus. LK-Zusatz im Sinn der IQB-Stufung: Einheit 2 – Spiegelebenen und Spiegelgeraden konstruieren („uneingeschränkt“ nur erhöht; grundlegend einmal in Teil B mit Hilfsmitteln, 2026MgrundlegendBAGLAA2WTR2-1e). Vorrat (Ermessen nach dem Niveau der Rohdatei): die Winkelhalbierenden-Raute, das Abstandsverhältnis auf der Spiegelachse, die Parameter-Symmetrieebenen und der zusammengesetzte Körper. Niveaustufe H der E-Phase [RLP]: die Sek-I-Pläne führen die Achsenspiegelung in der Ebene (symmetrie-abbildungen.md) – Blatt-0-Stoff, kein Mindeststoff dieses Eintrags. RLP FOS (fhr): kein Bestand, keine Zeile. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung keine Raumspiegelung – kein zusätzlicher Posten.
84  Grundvorstellung (Blatt 0) [GOST Eingangsvoraussetzung L3, MO]: Das Spiegelbild liegt gleich weit auf der anderen Seite, und die Verbindung steht senkrecht auf der Spiegelfläche. „Hier ist eine Glasscheibe, die senkrecht auf dem Tisch steht, und ein Radiergummi davor, kein Term. Wo ‚steht‘ das Spiegelbild – wie weit hinter der Scheibe? Miss nach: ist es derselbe Abstand wie davor? Wie verläuft die Linie vom Radiergummi zu seinem Bild – schräg oder senkrecht zur Scheibe? Schiebe den Radiergummi parallel zur Scheibe: was macht das Bild? Und wenn du ihn auf die Scheibe zuschiebst, bis er sie berührt – wo ist das Bild dann?“ Wer das Spiegelbild irgendwo hinter der Scheibe vermutet, die Verbindung schräg zeichnet oder den Berührpunkt nicht als Fixpunkt erkennt, braucht das vor jeder Rechnung: Spiegeln heißt gleicher Abstand, senkrechte Verbindung, Fixpunkte auf der Spiegelfläche. Verständnis, nicht Verfahren; die Vorstellung ist Sek-I-Bestand (Eingangsvoraussetzung L3 „Symmetrie“), ihre Raumfassung liegt im Kurshalbjahr (Klarstellung Geometrie); die Aufgabenform ist Ermessen. [GOST Eingangsvoraussetzung L3; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „beim Lotfußpunkt stehen bleiben“, abi 2022-bebb-lk-B3g; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
85  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
86  - Punkte spiegeln (Einheit 1): „Was wird gespiegelt – und woran?“ ankreuzen (Vorstufe, Grundvorstellung) → an einem Punkt spiegeln: Spiegelzentrum plus Verbindungsvektor (Grundfall, viermal; abi 2025-bebb-gk-A1.5a, iqb 2025MgrundlegendAAGLAA213-a, Teil A) → an Koordinatenebenen ablesen: genau ein Vorzeichen wechselt (iqb 2025MerhoehtBAGLAA1WTR-2a) → mit bekanntem Lotfußpunkt: den Verbindungsvektor in Gegenrichtung abtragen (abi 2026-bb-gk-A1.2b, iqb 2026MgrundlegendAAGLAA211-b, Teil A) → über die Lotgerade: aufstellen, schneiden, Parameter verdoppeln (abi 2022-bebb-lk-B3g; iqb 2021MerhoehtAAGLAA211-b, Teil A) → Prüfungshöhe: den Punkt mit vorgegebenem Abstandsverhältnis auf der Spiegelachse bestimmen (iqb 2022MerhoehtAAGLAA212-b, Teil A, Niveau II).
87  - Spiegelebene und Spiegelgerade (Einheit 2): „Was ist gegeben, was gesucht?“ ankreuzen (Vorstufe) → die Spiegelebene aus Punkt und Spiegelpunkt: Verbindungsvektor als Normalenvektor, Mittelpunkt einsetzen (Grundfall, viermal; iqb 2022MerhoehtAAGLAA212-a, Teil A) → die Spiegelgerade an einer Ebene aus Fixpunkt und Spiegelpunkt angeben (iqb 2018MerhoehtAAGLAA211-c, Teil A) → die Spiegelebene zweier sich schneidender Geraden über die Summe gleich langer Richtungsvektoren (abi 2023-bebb-lk-A1.6b, iqb 2023MerhoehtAAGLAA222-b, Teil A, Niveau III) → die Spiegelebene am Körper aus einem Spiegelpaar samt Konstante (abi 2026-bb-gk-B3e, iqb 2026MgrundlegendBAGLAA2WTR2-1e, Niveau III) → Prüfungshöhe: die Winkelhalbierende zeichnen und den Punkt über die Raute als Vektorterm angeben (iqb 2024MerhoehtAAGLAA222, Teil A, Niveau III).
88  - Symmetrieebenen von Körpern (Einheit 3): „Welche Koordinate wechselt?“ ankreuzen und „Reicht ein Gegenbeispiel?“ – ankreuzen, ob eine Symmetrie zu begründen (alle Punktepaare) oder auszuschließen ist (eine Punktprobe genügt); nichts rechnen (Vorstufe) → Punktepaare vergleichen und die Symmetrie zu einer Ebene oder Achse begründen (Grundfall, viermal; iqb 2026MerhoehtBAGLAA2WTR1-1b, 2022MerhoehtBAGLAA2WTR2-1a) → die Symmetrieebene unter Kandidaten auswählen und eine mit Punktprobe ausschließen (abi 2022-bebb-gk-B3e, 2024-bebb-lk-B3b; iqb 2022MgrundlegendBAGLAA2WTR2-1c, 2024MerhoehtBAGLAA2WTR1-1b, 2026MgrundlegendBAGLAA2MMS2-1b) → die Symmetrieebene angeben und die Schnittfigur einzeichnen (iqb 2019MgrundlegendBAGLAA2WTR2-1b) → die achsenparallelen Symmetrieebenen über Mittelwerte angeben (iqb 2025MerhoehtAAGLAA223-a, Teil A) → das gerade Prisma über die Symmetrieachse der Grundfläche begründen (iqb 2023MgrundlegendBAGLAA2WTR1-1c) → Prüfungshöhe: die beiden Symmetrieebenen mit Parameter begründen (iqb 2026MerhoehtAAGLAA223, Teil A, Niveau III) und die Symmetrie eines zusammengesetzten Körpers für jeden Parameterwert ausschließen (iqb 2025MerhoehtBAGLAA2MMS-1c, Niveau II).
89
90  ### Prüfungsform (fhr / abi / iqb)
91  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; das Thema ist dort kein Stoff, themen.csv führt keine fhr-Zeile. Die Rohdatei zählt 31 Zeilen mit 16 Haupttypen (abi 7 Zeilen, 6 Typen; iqb 24 Zeilen, 16 Typen; 6 Typen in beiden Profilen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix). Pool-Sachgebiet: Alternative A2 „Analytische Geometrie“ der Aufgabengruppe AG/LA [IQB-STR 1].
92  fhr: kein Bestand, keine Zeile – der RLP FOS 2019 kennt weder Spiegelung noch Symmetrieebene; der fhr-Katalog führt kein Thema der Analytischen Geometrie.
93  abi (7 Zeilen, 6 Typen; Landeshefte bebb-gk, bebb-lk, bb-gk 2022–2026) [abi-Katalog]: Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen (2, E3) · je 1: Spiegelebene aus Punkt und Spiegelpunkt bestimmen (E2) · Spiegelebene zweier sich schneidender Geraden bestimmen (E2) · Spiegelpunkt an einem Punkt bestimmen (E1) · Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen (E1) · Spiegelpunkt an einer Ebene über die Lotgerade bestimmen (E1). Muster: Das Thema erscheint in den Landesheften erst seit 2022 – mit der hohen Poolquote: 6 der 7 Zeilen sind wortgleiche Pooldubletten (2022-bebb-gk-B3e, 2023-bebb-lk-A1.6b, 2024-bebb-lk-B3b, 2025-bebb-gk-A1.5a, 2026-bb-gk-A1.2b, 2026-bb-gk-B3e), einziger Landeszusatz ist die Lotgeraden-Spiegelung 2022-bebb-lk-B3g. Teil B trägt vier Zeilen (zwei bis fünf Punkte: die Symmetrieebenen-Auswahl 2022-bebb-gk-B3e und 2024-bebb-lk-B3b, der Spiegelpunkt 2022-bebb-lk-B3g, die Spiegelebene 2026-bb-gk-B3e), Teil A drei (zwei bis vier Punkte: 2025-bebb-gk-A1.5a, 2026-bb-gk-A1.2b, 2023-bebb-lk-A1.6b). Niveau I 1, II 4, III 2.
94  iqb (24 Zeilen, 16 Typen; Pool 2017–2026, grundlegend 8 und erhöht 16 Zeilen, Teil A 10 und Teil B 14 Zeilen, davon 2 MMS und 3 CAS, Alternative A2) [iqb-Katalog]: Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen (4, E3) · Symmetrie einer geraden Pyramide bezüglich einer Koordinatenachse über Grundflächenmittelpunkt und Spitze begründen (3, E3) · Symmetrieebenen eines Körpers aus den Koordinaten begründen (3, E3) · Spiegelebene aus Punkt und Spiegelpunkt bestimmen (2, E2) · je 1: Koordinaten gespiegelter Eckpunkte aus den Symmetrieebenen eines Körpers angeben (E1) · Punkt auf der Spiegelachse mit vorgegebenem Abstandsverhältnis zur Spiegelebene bestimmen (E1) · Spiegelebene zweier sich schneidender Geraden bestimmen (E2) · Spiegelgerade einer Geraden an einer Ebene aus Fixpunkt und bekanntem Spiegelpunkt angeben (E2) · Spiegelgerade zweier Geraden zeichnen und Punkt der Winkelhalbierenden als Vektorterm angeben (E2) · Spiegelpunkt an einem Punkt bestimmen (E1) · Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen (E1) · Spiegelpunkt an einer Ebene über die Lotgerade bestimmen (E1) · Symmetrie zweier Punkte bezüglich einer Koordinatenachse über die Koordinaten begründen (E3) · Symmetrieebene eines Körpers angeben und ihre Schnittfigur mit dem Körper einzeichnen (E3) · Symmetrieebene eines geraden Prismas über die Symmetrieachse der Grundfläche begründen (E3) · Symmetrieebene eines zusammengesetzten Körpers über verschiedene Höhen der Teilkörper ausschließen (E3). Muster: Teil A (10 Zeilen, ein bis fünf Punkte) prüft die Punktspiegelungen auf beiden Niveaus (2025MgrundlegendAAGLAA213-a, 2026MgrundlegendAAGLAA211-b, 2021MerhoehtAAGLAA211-b, 2022MerhoehtAAGLAA212-b) und die Konstruktionen nur erhöht (2022MerhoehtAAGLAA212-a, 2023MerhoehtAAGLAA222-b, 2024MerhoehtAAGLAA222, 2018MerhoehtAAGLAA211-c, 2025MerhoehtAAGLAA223-a, 2026MerhoehtAAGLAA223) – genau die Stufung aus [IQB-VER 3.2]; Teil B (14 Zeilen, zwei bis vier Punkte) stellt die Symmetrieebenen am Sachkörper (Kirchturmdach 2022MgrundlegendBAGLAA2WTR2-1c, Haus 2019MgrundlegendBAGLAA2WTR2-1b, Gebäude mit Anbau 2023MgrundlegendBAGLAA2WTR1-1c, Saarpolygon 2022MerhoehtBAGLAA2WTR2-1a, Sprungschanze 2026MerhoehtBAGLAA2WTR1-1b, Skulptur 2025MerhoehtBAGLAA1WTR-2a, dazu 2024MerhoehtBAGLAA2WTR1-1b, 2026MgrundlegendBAGLAA2MMS2-1b, 2025MerhoehtBAGLAA2MMS-1c), seit dem Nachzug 2026-09-28 auch die Achsensymmetrie des Pyramidendachs eines Spielplatzturms über Grundflächenmittelpunkt und Spitze (2017MerhoehtBAGLAA2WTR1-1c, wortgleich in der CAS-Fassung 2017MerhoehtBAGLAA2CAS1-1c, je drei Punkte, Niveau II), seit dem Nachzug 2026-09-29 dieselbe Teilaufgabe auch auf grundlegendem Niveau in der CAS-Fassung (2017MgrundlegendBAGLAA2CAS1-1c, drei Punkte, Niveau II) und die Auswahl der Symmetrieebenen eines Obelisken mit begründetem Ausschluss (2018MerhoehtBAGLAA2CAS2-1e, CAS, vier Punkte, Niveau II), und einmal die Spiegelebene aus dem Trapez-Spiegelpaar (2026MgrundlegendBAGLAA2WTR2-1e). Amtlicher Anforderungsbereich in allen 24 Zeilen (höchster Bereich: I 6, II 14, III 4); Niveau I 6, II 14, III 4. Kontexte: Kirchturmdach, Dachgeschoss, Saarpolygon, Wasserski-Schanze, Siebeneck-Skulptur, Gebäude mit Anbau, Spielplatzturm, Obelisk. 6 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste), keine abgewandelt.
95  Zielmarke: Einheit 1 – abi: der Spiegelpunkt über die Lotgerade (2022-bebb-lk-B3g, Niveau II) und der bekannte Lotfußpunkt in Teil A (2026-bb-gk-A1.2b, Niveau II); iqb: das Abstandsverhältnis auf der Spiegelachse (2022MerhoehtAAGLAA212-b, Teil A, Niveau II) und die Lotgerade in Teil A (2021MerhoehtAAGLAA211-b, Niveau II). Einheit 2 – abi: die Spiegelebene zweier Geraden mit Erläuterung (2023-bebb-lk-A1.6b, Teil A, Niveau III) und die Spiegelebene aus dem Trapez-Spiegelpaar (2026-bb-gk-B3e, Niveau III); iqb: die Winkelhalbierende mit Rautenterm (2024MerhoehtAAGLAA222, Teil A, Niveau III) und die Spiegelgerade aus Fixpunkt und Spiegelpunkt (2018MerhoehtAAGLAA211-c, Teil A, Niveau II). Einheit 3 – abi: die Auswahl mit begründetem Ausschluss (2024-bebb-lk-B3b, Niveau II); iqb: die Symmetrieebenen mit Parameter (2026MerhoehtAAGLAA223, Teil A, Niveau III) und der zusammengesetzte Körper (2025MerhoehtBAGLAA2MMS-1c, Niveau II).
````

## 2 Originale (31)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2022-bebb-gk-B3e (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Kurzantwort|Begründung · antwort Term|Text
- gegeben: Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; Ebenen M1: x = 8, M2: x − y = 0, M3: z = 6; eine ist Symmetrieebene des Dachs
- gesucht: diese Ebene mit Beschreibung ihrer Lage
- verfahren: M2 enthält die Diagonale AC und die Spitze S
- fehlerquelle: M3 wählen (waagerechte Ebene durch die Giebelspitzen ist keine Symmetrieebene)

### 2023-bebb-lk-A1.6b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung · antwort Term|Text
- gegeben: g und h mit gemeinsamem Punkt (1; 1; 1) und den Richtungsvektoren (1; 2; 0) und (2; 1; 0); g soll durch Spiegelung an einer Ebene auf h abgebildet werden
- gesucht: Gleichung einer geeigneten Ebene mit Erläuterung
- verfahren: die Richtungsvektoren sind gleich lang, ihre Summe halbiert den Winkel und ist Normalenvektor der Ebene, die g auf h spiegelt; Ebene durch den Schnittpunkt legen
- fehlerquelle: die Summe der Richtungsvektoren als Richtung der Ebene statt als Normalenvektor nehmen

### 2024-bebb-lk-B3b (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: Gleichungen (1) x − z = 0, (2) x + y + z = 4, (3) x + y = 0; genau eine beschreibt eine Symmetrieebene
- gesucht: die Symmetrieebene; Begründung für eine der anderen
- verfahren: Ebene durch S und O suchen, Gegenbeispiel über Punktprobe
- fehlerquelle: (2) wegen S ∈ Ebene für die Symmetrieebene halten

### 2025-bebb-gk-A1.5a (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: P(0; −1; 1) und Q(2; 5; 3); P' entsteht durch Spiegelung von P am Punkt Q
- gesucht: Koordinaten von P'
- verfahren: OP' = OQ + PQ, also Q plus den Vektor PQ = (2; 6; 2)
- fehlerquelle: PQ an P statt an Q abtragen und Q selbst erhalten

### 2026-bb-gk-A1.2b (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ebene E: x1 − 3x2 + 2x3 = 11; P(5; 0; 3) liegt in E; die Gerade g durch P und Q(9; −12; 11) steht senkrecht auf E; Q und R liegen symmetrisch bezüglich E
- gesucht: Koordinaten von R
- verfahren: P ist der Lotfußpunkt von Q auf E, also ist R = P − PQ (den Vektor PQ von P aus in Gegenrichtung abtragen)
- fehlerquelle: den Lotfußpunkt neu berechnen, obwohl er mit P gegeben ist, oder R = Q − PQ = P erhalten

### 2026-bb-gk-B3e (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 4 · format Rechnung · antwort Term
- gegeben: Trapeze TUVW (in z = 2) und BUVC (Seitenfläche) symmetrisch zu einer Ebene H; C(5 | 1 | 0), W(1 | 1 | 2), U(3,5 | −0,5 | 2)
- gesucht: Gleichung von H
- verfahren: C und W als Spiegelpaar, Normalenvektor CW, Konstante über U
- fehlerquelle: H als Ebene durch U und V senkrecht zur xy-Ebene ansetzen

### 2022-bebb-lk-B3g (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: L₈: 2x + 2y + z = 8; U(0|0|−1); Abstand 3 aus f
- gesucht: Koordinaten des Spiegelpunkts U' von U an L₈
- verfahren: Lotgerade schneiden, Lotvektor verdoppeln (oder U + 2 · 3 · n⁰)
- fehlerquelle: nur bis zum Lotfußpunkt rechnen; Richtung des Normalenvektors falsch

### 2025MgrundlegendAAGLAA213-a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: P(0; −1; 1) und Q(2; 5; 3); P' entsteht durch Spiegelung von P am Punkt Q
- gesucht: Koordinaten von P'
- verfahren: OP' = OQ + PQ, also Q plus den Vektor PQ = (2; 6; 2)
- fehlerquelle: PQ an P statt an Q abtragen und Q selbst erhalten

### 2026MgrundlegendAAGLAA211-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ebene E: x1 − 3x2 + 2x3 = 11; P(5; 0; 3) liegt in E; die Gerade g durch P und Q(9; −12; 11) steht senkrecht auf E; Q und R liegen symmetrisch bezüglich E
- gesucht: Koordinaten von R
- verfahren: P ist der Lotfußpunkt von Q auf E, also ist R = P − PQ (den Vektor PQ von P aus in Gegenrichtung abtragen)
- fehlerquelle: den Lotfußpunkt neu berechnen, obwohl er mit P gegeben ist, oder R = Q − PQ = P erhalten

### 2021MerhoehtAAGLAA211-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: P(−1; 7; 2), E: x1 + 3x2 = 0
- gesucht: Koordinaten des Spiegelpunkts von P an E
- verfahren: Lotgerade aufstellen, Lotfußpunkt über λ, Parameter verdoppeln
- fehlerquelle: beim Lotfußpunkt stehen bleiben (λ statt 2λ)

### 2022MerhoehtAAGLAA212-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: P, Q, M(4; 2; 7); R und S auf der Geraden PQ symmetrisch zu E, R auf der Seite von P; |RS| = 2 · |PQ|
- gesucht: Koordinaten von R
- verfahren: R = M − PQ (Abstand |PQ| vom Mittelpunkt in Richtung P)
- fehlerquelle: R = P − PQ = (−5; 2; −5) rechnen (Verhältnis von P statt von M aus)

### 2022MerhoehtAAGLAA212-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung · antwort Term
- gegeben: Spiegelung von P(1; 2; 3) an E ergibt Q(7; 2; 11)
- gesucht: Gleichung von E in Koordinatenform
- verfahren: Normalenvektor PQ, Mittelpunkt einsetzen
- fehlerquelle: P statt M in die Ebenengleichung einsetzen

### 2023MerhoehtAAGLAA222-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Rechnung · antwort Term|Text
- gegeben: g und h mit gemeinsamem Punkt (1; 1; 1) und den Richtungsvektoren (1; 2; 0) und (2; 1; 0); g soll durch Spiegelung an einer Ebene auf h abgebildet werden
- gesucht: Gleichung einer geeigneten Ebene mit Erläuterung
- verfahren: die Richtungsvektoren sind gleich lang, ihre Summe halbiert den Winkel und ist Normalenvektor der Ebene, die g auf h spiegelt; Ebene durch den Schnittpunkt legen
- fehlerquelle: die Summe der Richtungsvektoren als Richtung der Ebene statt als Normalenvektor nehmen

### 2024MerhoehtAAGLAA222 (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 5 · format Zeichnen|Kurzantwort · antwort Grafik|Term
- gegeben: Punkte A, B, P in einer Ebene (Abbildung); g durch A, g* durch B, h durch P; g und g* schneiden sich in P; g* entsteht aus g durch Spiegelung an h
- gesucht: g, g* und eine Gerade h in der Abbildung|Term, der aus A, B, P den Ortsvektor eines weiteren Punktes von h liefert
- verfahren: g = AP, g* = BP zeichnen, h als Winkelhalbierende in P; von B aus den Vektor AP auf die Länge |PB| skaliert abtragen: die Raute aus PB und dem skalierten Vektor hat h als Diagonale
- fehlerquelle: OA + OB als Term angeben (Mittelpunkt statt Raute)

### 2018MerhoehtAAGLAA211-c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Kurzantwort · antwort Term
- gegeben: P und Q gleich weit von E, PQ senkrecht zu E (aus b), S in E (aus a); g durch S und P, h Spiegelbild von g an E
- gesucht: eine Gleichung von h
- verfahren: Q als Spiegelpunkt von P erkennen, h durch S und Q
- fehlerquelle: h durch P und Q legen (das ist die Lotgerade)

### 2025MerhoehtAAGLAA223-a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 1 · format Kurzantwort · antwort Term
- gegeben: Körper ABCDEFGH ist Teil einer geraden Pyramide mit rechteckiger Grundfläche EFGH; ABCD und EFGH liegen in parallelen Ebenen mit Abstand 5; A(0; 0; 0), B(4; 0; 0), C(4; 6; 0), D(0; 6; 0)
- gesucht: Gleichung einer der beiden Symmetrieebenen des Körpers
- verfahren: die Symmetrieebenen stehen senkrecht auf den Rechtecken durch deren Mittellinien: x = 2 (Mitte von AB) oder y = 3 (Mitte von AD)
- fehlerquelle: eine Diagonalebene angeben, die beim Rechteck keine Symmetrieebene ist

### 2026MerhoehtAAGLAA223 (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 5 · format Kurzantwort|Begründung · antwort Term|Text
- gegeben: für t > 0 die Pyramide A_tB_tCDS_t mit A_t(1; 1 + 2t; 0), B_t(−1; 1 + 2t; 0), C(−1; −1; 0), D(1; −1; 0) und S_t(0; t; 6); jede Pyramide hat genau zwei Symmetrieebenen
- gesucht: je eine Gleichung der beiden Symmetrieebenen für jeden Wert von t, mit Begründung
- verfahren: x = 0: D und C sowie A_t und B_t unterscheiden sich nur im Vorzeichen der x-Koordinate, S_t hat x = 0; y = t: D und A_t sowie C und B_t unterscheiden sich nur in der y-Koordinate mit Mittelwert (1 + 2t − 1)/2 = t, S_t hat y = t
- fehlerquelle: y = 1 + t als Mitte der Grundfläche schätzen statt den Mittelwert der y-Koordinaten zu bilden

### 2022MgrundlegendBAGLAA2WTR2-1c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Kurzantwort|Begründung · antwort Term|Text
- gegeben: Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; Ebenen M1: x = 8, M2: x − y = 0, M3: z = 6; eine ist Symmetrieebene des Dachs
- gesucht: diese Ebene mit Beschreibung ihrer Lage
- verfahren: M2 enthält die Diagonale AC und die Spitze S
- fehlerquelle: M3 wählen (waagerechte Ebene durch die Giebelspitzen ist keine Symmetrieebene)

### 2019MgrundlegendBAGLAA2WTR2-1b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 2 · format Kurzantwort|Zeichnen · antwort Term|Grafik
- gegeben: Haus als Körper ABCDIJKL: Quader ABCDEFGH und Dachprisma EFGHIJKL; A(0 | 0 | 0), G(10 | 6 | 10), H(0 | 6 | 10), K(10 | 6 | 10,5), L(0 | 6 | 13); verglaste Fassade IEHL; 1 LE = 1 m
- gesucht: Gleichung der Symmetrieebene; Seiten der Schnittfigur in der Abbildung
- verfahren: Mittelebene y = 3 nennen und den Schnitt (Fünfeck) einzeichnen
- fehlerquelle: x = 5 als Symmetrieebene nehmen (Dach ist nicht symmetrisch in x)

### 2023MgrundlegendBAGLAA2WTR1-1c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Körper ABCDEFGH; Ebene L: x₂ − x₃ = 0 durch A, B, G
- gesucht: Begründung, dass L Symmetrieebene des Körpers ist
- verfahren: Körper als gerades Prisma über dem Drachen BCGF auffassen, L enthält die Symmetrieachse der Grundfläche und steht senkrecht auf ihr
- fehlerquelle: nur einzelne Punktepaare gespiegelt, keine allgemeine Begründung

### 2022MerhoehtBAGLAA2WTR2-1a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Streckenzug A(11|11|0), B(−11|11|28), C(11|−11|28), D(−11|−11|0), Ecken eines Quaders; 1 LE = 1 m
- gesucht: Begründung, dass B und C symmetrisch zur x₃-Achse liegen
- verfahren: Koordinaten vergleichen
- fehlerquelle: Symmetrie zur x₁x₃-Ebene behaupten

### 2026MerhoehtBAGLAA2WTR1-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Körper ABCDEF mit A(2 | 0 | −0,5), B(3 | 5 | −0,5), C(−3 | 5 | −0,5), D(−2 | 0 | −0,5), E(2 | 5 | 1), F(−2 | 5 | 1)
- gesucht: Begründung, dass die yz-Ebene Symmetrieebene ist
- verfahren: Punktepaare mit gespiegelter x-Koordinate
- fehlerquelle: nur ein Paar nennen

### 2025MerhoehtBAGLAA1WTR-2a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 3 · format Kurzantwort · antwort Zahl
- gegeben: gerades Prisma, Grundfläche Siebeneck ABCDEFG, H weiterer Eckpunkt; A(1 | 1 | 0), B(1 | 2 | 4), D(1 | 0 | 1); symmetrisch zur xz- und zur yz-Ebene
- gesucht: Koordinaten von F und H
- verfahren: B und A an den Symmetrieebenen spiegeln (Lage aus der Abbildung)
- fehlerquelle: F und H an der falschen Ebene spiegeln

### 2024MerhoehtBAGLAA2WTR1-1b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: Gleichungen (1) x − z = 0, (2) x + y + z = 4, (3) x + y = 0; genau eine beschreibt eine Symmetrieebene
- gesucht: die Symmetrieebene; Begründung für eine der anderen
- verfahren: Ebene durch S und O suchen, Gegenbeispiel über Punktprobe
- fehlerquelle: (2) wegen S ∈ Ebene für die Symmetrieebene halten

### 2026MgrundlegendBAGLAA2MMS2-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga-mms · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: genau eine der Gleichungen I x + y = 0, II x − y = 0, III z = 2 beschreibt eine Symmetrieebene des Quaders
- gesucht: welche; Begründung für eine andere, dass sie keine ist
- verfahren: Diagonalebene durch O und B erkennen; für III die Kante AE betrachten
- fehlerquelle: x + y = 0 mit der Diagonalebene verwechseln

### 2025MerhoehtBAGLAA2MMS-1c (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Punkte A(2 | 0 | 0), B(−2 | 0 | 0), C(−2 | 0 | 3), D(2 | 0 | 3), S(0 | −5 | 0), E_k(0 | k | 0), F_k(0 | k | 30 − 3k) mit 0 < k ≤ 10; zusammengesetzter Körper aus der Pyramide ABCDS und dem Körper ABCDE_kF_k; ABCD ist ein Rechteck
- gesucht: Begründung, dass die xz-Ebene für keinen Wert von k Symmetrieebene des zusammengesetzten Körpers ist
- verfahren: Beide Teilkörper an der xz-Ebene vergleichen: Pyramide der Höhe 5 gegen Körper, der höchstens (k = 10) eine Pyramide der Höhe 10 ist
- fehlerquelle: nur k = 5 prüfen und die Kante E₅F₅ (Länge 15) übersehen

### 2017MerhoehtBAGLAA2WTR1-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m; H(−3; −2; 4); EFGH ist ein Quadrat
- gesucht: Begründung, dass die Pyramide EFGHS symmetrisch bezüglich der x3-Achse ist
- verfahren: Der Mittelpunkt der Grundfläche (Mitte von EG) ist (0; 0; 4) und liegt wie S auf der x3-Achse; die Grundfläche ist ein Quadrat parallel zur x1x2-Ebene, die Pyramide gerade
- fehlerquelle: nur die Lage von S auf der x3-Achse nennen

### 2017MerhoehtBAGLAA2CAS1-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m; H(−3; −2; 4); EFGH ist ein Quadrat
- gesucht: Begründung, dass die Pyramide EFGHS symmetrisch bezüglich der x3-Achse ist
- verfahren: Der Mittelpunkt der Grundfläche (Mitte von EG) ist (0; 0; 4) und liegt wie S auf der x3-Achse; die Grundfläche ist ein Quadrat parallel zur x1x2-Ebene, die Pyramide gerade
- fehlerquelle: nur die Lage von S auf der x3-Achse nennen

### 2017MgrundlegendBAGLAA2CAS1-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m; H(−3; −2; 4); EFGH ist ein Quadrat
- gesucht: Begründung, dass die Pyramide EFGHS symmetrisch bezüglich der x3-Achse ist
- verfahren: Der Mittelpunkt der Grundfläche (Mitte von EG) ist (0; 0; 4) und liegt wie S auf der x3-Achse; die Grundfläche ist ein Quadrat parallel zur x1x2-Ebene, die Pyramide gerade
- fehlerquelle: nur die Lage von S auf der x3-Achse nennen

### 2018MerhoehtBAGLAA2CAS2-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Kurzantwort|Begründung · antwort Text
- gegeben: Modell eines Obelisken (nicht maßstabsgetreu) im kartesischen Koordinatensystem; die xy-Ebene beschreibt den ebenen Untergrund, 1 LE = 1 m; der untere Teilkörper ABCDEFGH mit B(0,45; 0,45; 0) ist ein Stumpf einer geraden Pyramide, der Mittelpunkt des Quadrats ABCD ist der Koordinatenursprung, das Quadrat EFGH ist parallel zur xy-Ebene; der obere Teilkörper EFGHS mit E(0,35; −0,35; 7,16) ist eine gerade Pyramide, ihre Spitze S liegt auf der z-Achse und stellt die Spitze des Obelisken dar; Gleichungen I x = 0,45, II y = 0, III x − y = 0, IV x − z = 0
- gesucht: für jede Gleichung die Entscheidung, ob sie eine Symmetrieebene des Obelisken beschreibt; für eine Gleichung die Begründung, dass sie keine solche Ebene darstellt
- verfahren: Symmetrieebenen enthalten die z-Achse und eine Seitenmitte oder eine Diagonale des Grundquadrats: y = 0 (Mitten von AB und CD) und x − y = 0 (durch B und D); x = 0,45 und x − z = 0 enthalten die z-Achse nicht
- fehlerquelle: x − y = 0 verwerfen, weil die Diagonalebene nicht parallel zu einer Seite ist

### 2026MgrundlegendBAGLAA2WTR2-1e (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 4 · format Rechnung · antwort Term
- gegeben: Trapeze TUVW (in z = 2) und BUVC (Seitenfläche) symmetrisch zu einer Ebene H; C(5 | 1 | 0), W(1 | 1 | 2), U(3,5 | −0,5 | 2)
- gesucht: Gleichung von H
- verfahren: C und W als Spiegelpaar, Normalenvektor CW, Konstante über U
- fehlerquelle: H als Ebene durch U und V senkrecht zur xy-Ebene ansetzen

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
