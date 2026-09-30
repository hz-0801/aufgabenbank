# Mappe: schnittmengen

Eintrag: hz-0801/mathe-nachhilfe, katalog/schnittmengen.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:12 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Schnittmengen
 3
 4  ### Verortung
 5  Die Schnittobjekte: der Schnittpunkt von Gerade und Ebene (Einsetzen in die Koordinatenform, Sonderfälle mit Achsen, senkrechten und achsenparallelen Geraden, Schattenpunkte bei paralleler Projektion, … (gekürzt, 2343 Zeichen)
 6  [GOST] Q3, 3. Kurshalbjahr „Analytische Geometrie“ (BB S. 29–30), Grund- und Leistungskursfach: L3-Zeile „Geraden und Ebenen analytisch beschreiben und Lagebeziehungen … untersuchen“ mit dem Inhalt „S … (gekürzt, 1646 Zeichen)
 7  [FOS] Kap. 4 Wahlthema 5 „Analytische Geometrie“ (S. 29): „Lagebeziehung Punkt–Gerade und Gerade–Gerade“ (Zeilen 1209–1213 der Textfassung) – der Geradenschnitt wäre Wahlstoff, Ebenen fehlen ganz; Wahlstoff ohne Prüfungsbeleg, kein fhr-Bestand, keine fhr-Zeile in themen.csv.
 8  [LS-AA] Einführungsphase Kapitel III 6 „Schnitt von Geraden“ (Zeile 279 der Textfassung); Qualifikationsphase Kapitel VI 8 „Gegenseitige Lage von Ebenen und Geraden“ (337) und 9 „Gegenseitige Lage von … (gekürzt, 648 Zeichen)
 9
10  ### Lerneinheiten
11  1. Schnittpunkt von Gerade und Ebene – Einsetzen: die Koordinaten der Geraden in die Koordinatengleichung einsetzen, den Parameter bestimmen, den Punkt angeben (Kontrollwerte nutzen); Sonderfälle, die … (gekürzt, 928 Zeichen)
12    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
13  2. Schnittpunkt zweier Geraden – Gleichsetzen: zwei Parameterformen gleichsetzen (verschiedene Parameterbuchstaben!), zwei Gleichungen lösen, die dritte als Probe; rückwärts einen Parameter im Stütz-  … (gekürzt, 693 Zeichen)
14    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
15  3. Spuren, Schnittgeraden und Schnittfiguren – die Schnittmenge als Linie und Figur: Spurpunkte einer Ebene auf den Achsen (die anderen Koordinaten null setzen), Spurgeraden in den Koordinatenebenen b … (gekürzt, 898 Zeichen)
16    Marken: BE Q3 · BB Q3 · GK (BB nur LK) · Abitur GK · Abitur LK
17  Warum drei: Die Plan-Zeile nennt zwei Schnittmengen (Geraden, Gerade–Ebene), der LK-Zusatz die dritte (Ebenen); die Rohdatei bündelt die Ebenen-Schnitte mit den Spuren und Figuren zu einer Zeichen- un … (gekürzt, 839 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
21  Einheit 1: Schnittpunkt von Gerade und Ebene berechnen (7) · Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen (4) · Schattenpunkt bei paralleler Projektion bestimmen (2) · Durchstoßpunkt einer achsenparallelen Geraden mit einer Ebene berechnen und Abstand im Sachzusammenhang angeben (1) · Zeit bis zum Erreichen einer Ebene aus dem Geradenparameter bestimmen (1) · Höhe einer Spitze aus dem Abstand ihres Schattenpunkts zu einem Punkt bestimmen (1; Ermessen, siehe Offene Punkte) — kein Nachweistyp — Deutung: Rechenweg für den Schnittpunkt einer Geraden mit einer Ebene durch drei Punkte beschreiben (1). Dazu: Fehler finden (beim Einsetzen den Aufpunkt vergessen und nur den Richtungsvektor eingesetzt; ein Vorzeichen beim Ausmultiplizieren verloren; die Ebene aufwendig aus drei Punkten bestimmt, wo der gemeinsame Koordinatenwert sie liefert; den Lotfußpunkt gesucht, wo der Durchstoßpunkt gefragt ist) · Begründen (warum das Einsetzen der Geradenkoordinaten eine Gleichung im Parameter liefert; warum bei einer Ebene z gleich Konstante nur die dritte Koordinate zählt).
22  Einheit 2: Parameter aus dem Schnitt zweier Geraden ermitteln (3) · Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen (2) · Höhe des Endpunkts einer Strecke auf einer senkrechten Geraden über den Schnitt mit einer Kante berechnen (1) · Schattenpunkt auf einer Kante als Schnittpunkt von Lichtgerade und Kantengerade berechnen (1; Ermessen, siehe Offene Punkte) — kein Nachweistyp — Deutung: Gegebene Rechnung zum Geradenschnittpunkt erläutern (2). Dazu: Fehler finden (für beide Geraden denselben Parameterbuchstaben verwendet; die dritte Gleichung nicht geprüft; eine Lösung außerhalb der Kante nicht verworfen; die Terme der vorgelegten Rechnung nicht als Kantengeraden benannt) · Begründen (warum zwei Parameter zwei Gleichungen brauchen und die dritte die Probe ist; warum der Kantenparameter zwischen null und eins liegen muss).
23  Einheit 3: Endpunkt der Schnittstrecke eines Vierecks mit einer achsenparallelen Ebene bestimmen (1) — Nachweis: Halbierung eines Quadrats durch gegebene Ebenen entscheiden und begründen (1) · Lage zweier Ebenen über die Normalenvektoren entscheiden und Schnittgerade berechnen (1) — Deutung: Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen (3) · Koordinate eines Punktes aus der Schnittfigur zeichnerisch ermitteln und Vorgehen beschreiben (2) · Schnittfigur einer Ebene mit einem Würfel einzeichnen (2) · Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen (1). Dazu: Fehler finden (die Spurgerade in der falschen Koordinatenebene gezeichnet; den Achsenpunkt auf falscher Höhe eingetragen; die Schnittfigur an den Ecken statt an den Kantenmitten enden lassen; die Koeffizienten statt der Achsenabschnitte als Spurpunkte angegeben; beide Koordinatengleichungen gleichgesetzt statt die Parameterform einzusetzen) · Begründen (warum parallele Flächen parallele Schnittkanten liefern; warum das Nullsetzen zweier Koordinaten den Achsenpunkt gibt).
24  Zählung: 7 + 5 + 7 = 19 Haupttypen, 17 + 9 + 11 = 37 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeile vom 27.09.2026: Pool 2017 grundlegend Teil B; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2018 erhöht und 2017 grundlegend Teil B CAS) samt der Niveau-Korrektur des Abgleichlaufs 27).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Geradengleichungen aufstellen und den allgemeinen Geradenpunkt bilden – der Rechenkern aller Einheiten. Sek-II-Nachbarthema geraden.md (dasselbe Kurshalbjahr; Klarstellung Geometrie: Fertigkeit aus dem Nachbarthema derselben Stufe). [GOST Q3 L3 „Parameterform“; GOST-OHiMi 2.3 „Geraden: Parameterform“]
29  - Ebenengleichungen lesen (Koordinatenform, Parameterform, Normalenvektor) – die Prüfregeln in Einheit 1 und 3. Sek-II-Nachbarthema ebenen.md. [GOST Q3 L3 „analytische Beschreibung von Geraden und Ebenen“; GOST-OHiMi 2.3]
30  - Den Lagebefund vorweg führen (liegt der Punkt darin, schneidet die Gerade überhaupt – Merkregel über das Skalarprodukt) – die Fallprüfung vor jeder Schnittrechnung. Sek-II-Nachbarthema lagebeziehungen.md (dasselbe Bündel). [GOST Q3 L3 „Lagebeziehungen …“; GOST-OHiMi 2.3]
31  - Lineare Gleichungssysteme mit zwei und drei Unbekannten lösen, auch überbestimmte mit Probegleichung – das Gleichsetzen in Einheit 2 und die Schnittgerade in Einheit 3. Sek-I-Thema lineare-gleichungssysteme.md (kanonisch auch für die Sek-II-Zeilen). [GOST Eingangsvoraussetzung L1 „lösen lineare (2,2)- und (3,3)-Gleichungssysteme“; GOST Q3 L1 „Bestimmung von Schnittmengen“; GOST-OHiMi 2.1]
32  - Teilverhältnisse und Parameterbereiche von Strecken lesen – die Kantenschnitte in Einheit 2 und 3. Sek-II-Nachbarthemen geraden.md, punkte-und-strecken-im-koordinatensystem.md; Sek-I-Thema strahlensaetze.md. [GOST Q3 L3 „Teilverhältnisse von Strecken“]
33  - Schrägbilder lesen und zeichnen – das Einzeichnen der Spuren und Schnittfiguren in Einheit 3. Sek-II-Nachbarthema punkte-und-strecken-im-koordinatensystem.md; Sek-I-Vorläufer koerper.md. [RLP D–G „Skizzieren von Schrägbildern“; GOST-OHiMi 2.3 „Darstellung …“]
34  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
35  - „Was wird geschnitten – und was kann herauskommen?“ – zu Aufgaben das Objektpaar und die erwartete Schnittmenge ankreuzen (Punkt, Gerade, Strecke, Figur, leer); nichts rechnen. Vor allen Einheiten. [GOST Q3 L3 „Schnittmenge: …“; abi 2021-be-gk-B3e]
36  - „Einsetzen oder gleichsetzen?“ – ankreuzen, welcher Weg passt: Koordinatenform vorhanden → einsetzen; zwei Parameterformen → gleichsetzen mit verschiedenen Parameterbuchstaben; nichts rechnen. Vor Einheit 1 und 2. [Rohdatei-Fehlerquelle „für h denselben Parameter s wie für g verwenden“; abi 2023-bebb-gk-A1.4b]
37
38  ### Merkkasten
39  Einheit 1 (Schnittpunkt von Gerade und Ebene):
40      Einsetzen: die drei Koordinaten des allgemeinen Geradenpunkts in die Koordinatengleichung der Ebene einsetzen – eine Gleichung im Parameter; den Parameter bestimmen und in die Gerade einsetzen.
41        E: x + y + 2z = 4, g: x = (2 | 1 | −2) + λ · (2 | −1 | −3): (2 + 2λ) + (1 − λ) + 2 · (−2 − 3λ) = 4 ⇔ −1 − 5λ = 4 ⇔ λ = −1 → Schnittpunkt S(0 | 2 | 1).
42      Sonderfälle sparen Arbeit: eine Ebene z gleich Konstante braucht nur die dritte Koordinate; eine Spitze auf einer Achse hat zwei Koordinaten null; eine senkrechte oder achsenparallele Gerade hält zwei Koordinaten fest.
43      Schatten bei paralleler Projektion: die Lichtrichtung ist der Vektor von einem Punkt zu seinem bekannten Schattenpunkt; der gesuchte Schatten ist der Durchstoßpunkt der Lichtgeraden durch die Grundebene.
44      Zeit als Parameter: entspricht der Parameterschritt eins einer bekannten Zeitspanne, ist die Zeit bis zur Ebene das Parameter-Vielfache dieser Spanne.
45      Auswendig (Teil A): „Einsetzen“ und die „Sonderfälle“ – begründetes Ermessen: die Anlage nennt die Schnittmenge nicht (Nulltreffer), die Teil-A-Zeilen 2017MerhoehtAAGLAA211-b und 2019MerhoehtAAGLAA21-a verlangen den Schnittpunkt ohne Rechner; nach [IQB-VER 3.2] sind Schnittpunkte von Gerade und Koordinatenebene und von Ebene und Koordinatenachse vorausgesetzt, der Schnitt beliebiger Geraden mit beliebigen Ebenen wird grundlegend nicht gefordert – beide Teil-A-Belege stehen im erhöhten Pool.
46      Formelsammlung: keine – der Schnittkalkül steht nicht in [FS-IQB 1.3] – [FS] offen
47  Quelle: eigene Formulierung nach [GOST Q3 L3] „Schnittmenge: … einer Geraden und einer Ebene“ und [IQB-VER 3.2]; Zahlenbeispiel aus dem Pool (2017MerhoehtAAGLAA211-b, wörtlich); [LS-AA QP VI 8].
48
49  Einheit 2 (Schnittpunkt zweier Geraden):
50      Gleichsetzen: die beiden Parameterformen mit verschiedenen Parameterbuchstaben gleichsetzen – drei Gleichungen für zwei Unbekannte; zwei Gleichungen lösen, die dritte ist die Probe (geht sie nicht auf, schneiden sich die Geraden nicht).
51      Parameter rückwärts: steckt eine Unbekannte im Stütz- oder Richtungsvektor, liefern zwei Koordinaten die beiden Geradenparameter und die dritte die Unbekannte.
52        g: x = (2 | 3 | −7) + s · (1 | 0 | 5), h durch A(4 | 0 | 0) und B(5 | 1 | b): aus der zweiten Koordinate r = 3, aus der ersten s = 5, die dritte liefert 18 = 3b, also b = 6.
53      Auf der Kante? Bei Kantengeraden den Kantenparameter prüfen: nur Werte zwischen null und eins liegen auf der Kante – andere Lösungen verwerfen; der Kantenparameter ist zugleich das Teilverhältnis.
54      Auswendig (Teil A): „Gleichsetzen“ mit der Probegleichung – begründetes Ermessen: die Anlage nennt die Schnittmenge nicht, die Teil-A-Zeile 2023MgrundlegendAAGLAA212-b (grundlegend) verlangt das Gleichsetzen ohne Rechner; das Werkzeug steht in [GOST-OHiMi 2.1] „Lösbarkeit und Lösungsmenge von linearen Gleichungssystemen“.
55      Formelsammlung: keine – [FS] offen
56  Quelle: eigene Formulierung nach [GOST Q3 L3] „Schnittmenge: zweier Geraden“ und [GOST Q3 L1] „Bestimmung von Schnittmengen“; Zahlenbeispiel aus dem Pool (2023MgrundlegendAAGLAA212-b, wörtlich; wortgleiche Dublette 2023-bebb-gk-A1.4b); [LS-AA EP III 6].
57
58  Einheit 3 (Spuren, Schnittgeraden und Schnittfiguren):
59      Spurpunkte: die Schnittpunkte einer Ebene mit den Achsen – je zwei Koordinaten null setzen; sie sind die Achsenabschnitte, nicht die Koeffizienten.
60        E₁: 12x + 4y + 9z = 36: Spurpunkte (3 | 0 | 0), (0 | 9 | 0), (0 | 0 | 4).
61      Spurgerade: die Schnittgerade der Ebene mit einer Koordinatenebene – eine Koordinate null setzen; im Schrägbild verbindet sie die beiden zugehörigen Spurpunkte.
62      Schnittgerade zweier Ebenen: erst die Nichtparallelität über die Normalenvektoren begründen, dann die Parameterform der einen Ebene in die Koordinatenform der anderen einsetzen – ein Parameter fällt, der andere bleibt als Geradenparameter.
63      Schnittfigur am Körper: parallele Flächen geben parallele Schnittkanten – die Figur endet an den Punkten, in denen die Ebene die Kanten trifft (Kantenmitten mitprüfen); zum Ablesen einer Koordinate eine Schnittkante bis zu einer bekannten Geraden verlängern.
64      Auswendig (Teil A): „Spurpunkte“ und „Spurgerade“ – [GOST-OHiMi 2.3] „Darstellung und Beschreibung von Punkten, Geraden, Flächen und Körpern im dreidimensionalen Koordinatensystem“ und [IQB-VER 3.2] (Schnittpunkte von Ebene und Koordinatenachse vorausgesetzt; Teil-A-Beleg 2017MerhoehtAAGLAA211-a); die „Schnittgerade zweier Ebenen“ ist LK-Stoff des Plans, die „Schnittfigur“ Zeichenarbeit des Teils B.
65      Formelsammlung: keine – Spuren und Schnittfiguren stehen nicht in der Formelsammlung – [FS] offen
66  Quelle: eigene Formulierung nach [GOST Q3 L3] „Darstellung …“, LK-Zusatz „Schnittmenge zweier Ebenen“ und [GOST-OHiMi 2.3]; Zahlenbeispiel aus dem Landesheft (2020-be-gk-B3.1b, wörtlich); [LS-AA QP VI 7 und 9].
67
68  ### Typische Fehler
69  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 31 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Didaktik der Analytischen Geometrie, die Muster sind allein aus den Katalogzeilen belegt.
70  - Einsetzen verfehlt: den Aufpunkt vergessen und nur den Richtungsvektor eingesetzt; ein Vorzeichen beim Ausmultiplizieren verloren; einen Vorzeichenfehler im Ansatz der dritten Koordinate gemacht; den Richtungsvektor in Gegenrichtung angesetzt. [abi 2023-bebb-gk-B3d; iqb 2017MerhoehtAAGLAA211-b, 2019MerhoehtAAGLAA21-a, 2023MgrundlegendBAGLAA2WTR2-1d]
71  - Sonderfall nicht gesehen: die Ebene des parallelen Dreiecks aufwendig aus drei Punkten bestimmt statt am gemeinsamen Koordinatenwert abzulesen; Quader- und Pyramidenhöhe verwechselt oder nur die Teilhöhe angegeben; den Lotfußpunkt bestimmt, wo der Durchstoßpunkt mit der senkrechten Ebene gefragt ist; den Abstand zur Ebene statt der senkrechten Strecke berechnet oder den Zuschlag vergessen. [abi 2018-bb-ea-B3.1e, 2017-bb-ea-B3.2b, 2018-be-gk-B2.1e, 2019-be-gk-B3.1b]
72  - Schatten falsch verfolgt: die Lichtrichtung aus dem falschen Punktepaar vermutet oder die dritte Koordinate nicht null gesetzt; den Schatten des falschen Eckpunkts verfolgt. [iqb 2020MgrundlegendBAGLAA2WTR-1d, 2019MgrundlegendBAGLAA2WTR2-1g]
73  - Gleichsetzen verfehlt: für beide Geraden denselben Parameterbuchstaben verwendet; die dritte Gleichung nicht geprüft; eine Lösung außerhalb der Kante nicht verworfen; den Parameterbereich der Kante falsch angewendet und eine gültige Lösung verworfen. [abi 2023-bebb-gk-A1.4b, 2019-be-gk-B3.2f, 2026-bb-ea-B3c; iqb 2023MgrundlegendAAGLAA212-b, 2021MgrundlegendBAGLAA2WTR2-1c, 2019MgrundlegendBAGLAA2WTR1-1f, 2026MerhoehtBAGLAA2WTR2-1c]
74  - Ansatz an der falschen Stelle: die untere Netzkante auf der Plattformhöhe angesetzt; die Sichtgrenze als Gerade statt als Ebene angesetzt; das Teilverhältnis auf die Diagonale statt auf eine Seite angewendet. [iqb 2018MerhoehtBAGLAA2WTR2-1f, 2023MerhoehtBAGLAA2WTR1-1e, 2018MerhoehtBAGLAA1WTR-1b]
75  - Vorgelegte Rechnung nicht benannt: die Terme nachvollzogen, ohne sie als Kantengeraden zu benennen; den Punkt der Schnittfigur innerhalb der Figur gesucht statt auf der verlängerten Kante. [abi 2018-bb-ea-B3.1a; iqb 2018MgrundlegendBAGLAA2WTR1-1c, 2018MerhoehtBAGLAA2WTR1-1d]
76  - Spuren und Figuren falsch gezeichnet: die Spurgerade in der falschen Koordinatenebene; den Achsenpunkt auf falscher Höhe oder neben der Achse; die Koeffizienten statt der Achsenabschnitte als Spurpunkte; die Schnittfigur an den Ecken statt an den Kantenmitten enden lassen; die Halbierungsebene als Ebene durch die falschen Punkte gelesen. [abi 2021-be-gk-B3h, 2020-be-gk-B3.1b, 2025-bebb-lk-A1.3b, 2021-be-gk-B3e; iqb 2017MerhoehtAAGLAA211-a, 2021MgrundlegendBAGLAA2WTR1-1e, 2025MerhoehtAAGLAA212-b]
77  - Schnittgerade falsch angesetzt: beide Koordinatengleichungen gleichgesetzt statt die Parameterform einzusetzen. [abi 2020-be-gk-B3.1d]
78
79  ### Für schwache Schüler
80  Mindeststoff (GK-Kern Q3 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q3 Brandenburg und Berlin: „Schnittmenge: zweier Geraden, einer Geraden und einer Ebene“ – Einheit 1 und 2 vollständig, Einheit 3 mit Spurpunkten und Spurgeraden (über die Darstellungs-Zeile). Ohne Hilfsmittel (Anlage OHiMi, Prüfungsteil A): die Anlage nennt die Schnittmenge nicht – ohne Rechner sitzen müssen die Bausteine (Lagebeziehungen, Gleichungssysteme, Darstellung) und nach [IQB-VER 3.2] die Schnitte mit Koordinatenebenen und -achsen; der Schnitt beliebiger Geraden mit beliebigen Ebenen wird grundlegend nicht gefordert. LK-Zusatz: die Schnittgerade zweier Ebenen (Einheit 3, amtlich). Vorrat, weil der Plan keine Grenze zieht (Ermessen nach dem Niveau der Rohdatei): die parameterabhängigen Kantenschnitte (Einheit 2, Niveau III), die zeichnerische Auswertung der Schnittfiguren und die Halbierungsfrage (Einheit 3), die Verfahrensbeschreibungen. Niveaustufe H der E-Phase [RLP]: kein Posten – die Sek-I-Pläne kennen nur den Schnittpunkt zweier Geraden in der Ebene (lineare-funktionen.md), Blatt-0-Stoff. RLP FOS (fhr): kein Bestand. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung Schnittpunkte und Schnittgeraden – wenn das zutrifft, deckt es sich mit dem GK-Kern samt LK-Zeile, kein zusätzlicher Posten.
81  Grundvorstellung (Blatt 0) [GOST Q3 L3, MO]: Schneiden heißt gleichzeitig auf beiden – ein Schnittpunkt erfüllt beide Gleichungen zugleich. „Hier sind ein gespannter Faden als Gerade und eine Glasplatte als Ebene im Schuhkarton, kein Term. Wo durchstößt der Faden die Platte – zeige den Punkt. Kann der Faden die Platte verfehlen? Wie muss er dazu liegen? Kann er ganz in ihr liegen? Und zwei Fäden: finden sie immer einen gemeinsamen Punkt, wenn sie nicht parallel sind – auch im Raum? Was bleibt übrig, wenn zwei Platten einander durchdringen – ein Punkt, eine Linie, eine Fläche?“ Wer dem Geradenpaar im Raum immer einen Schnittpunkt gibt, wer den Durchstoßpunkt für einen Ebenenpunkt ohne Geradeneigenschaft hält oder wer beim Plattenpaar einen Punkt erwartet, braucht das vor jeder Rechnung: Die Schnittmenge ist das, was auf beiden Objekten zugleich liegt – und sie kann leer sein. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q3-Kern „Schnittmenge“), liegt aber im Kurshalbjahr selbst, nicht in den Eingangsvoraussetzungen (Klarstellung Geometrie); die Aufgabenform ist Ermessen. [GOST Q3 L3; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „dritte Gleichung nicht prüfen“, iqb 2021MgrundlegendBAGLAA2WTR2-1c; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
82  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
83  - Schnittpunkt von Gerade und Ebene (Einheit 1): „Einsetzen oder gleichsetzen?“ ankreuzen (Vorstufe) → den allgemeinen Geradenpunkt in die Koordinatengleichung einsetzen, Parameter und Punkt bestimmen (Grundfall, viermal; iqb 2017MerhoehtAAGLAA211-b, 2019MerhoehtAAGLAA21-a, Teil A) → die Kante einer Pyramide mit einer Ebene schneiden, Kontrollwert nutzen (abi 2023-bebb-gk-B3d, 2026-bb-ea-B3c; iqb 2026MerhoehtBAGLAA2WTR2-1c) → Sonderfälle nutzen: Ebene mit gemeinsamem Koordinatenwert (abi 2018-bb-ea-B3.1e), Spitze auf der Achse (abi 2017-bb-ea-B3.2b; iqb 2023MgrundlegendBAGLAA2WTR2-1d), senkrechte Gerade mit Maßstab und Zuschlag (abi 2019-be-gk-B3.1b) → Schattenpunkte bei paralleler Projektion: Lichtrichtung aus Punkt und Schattenpunkt, Durchstoß mit der Grundebene (iqb 2020MgrundlegendBAGLAA2WTR-1d, 2019MgrundlegendBAGLAA2WTR2-1g) → die Zeit als Parameter-Vielfaches der bekannten Zeitspanne (abi 2018-be-gk-B2.1e, Niveau III) → Prüfungshöhe: den Rechenweg für den Schnitt mit einer Ebene durch drei Punkte beschreiben – Sichtgrenze als Ebene, Gleichsetzen der Parameterformen (iqb 2023MerhoehtBAGLAA2WTR1-1e, Niveau III).
84  - Schnittpunkt zweier Geraden (Einheit 2): „Wie viele Gleichungen, welche ist die Probe?“ – beim Gleichsetzen ankreuzen, wie viele Gleichungen und Unbekannte entstehen (zwei Unbekannte, drei Gleichungen) und welche Gleichung die Probe ist; nichts rechnen (Vorstufe) → zwei Geraden gleichsetzen, Parameter lösen, Probe führen (Grundfall, viermal; iqb 2021MgrundlegendBAGLAA2WTR2-1c mit Kontrollwert) → den Parameter im Richtungsvektor rückwärts bestimmen (abi 2023-bebb-gk-A1.4b, iqb 2023MgrundlegendAAGLAA212-b, Teil A) → die unbekannte Höhe über den Schnitt mit der Kantengeraden (iqb 2018MerhoehtBAGLAA2WTR2-1f, Niveau III) → eine vorgelegte Rechnung erläutern: Terme als Kantengeraden benennen, das Gleichsetzen deuten (abi 2018-bb-ea-B3.1a) → Prüfungshöhe: den Schnittpunkt der parameterabhängigen Geraden mit der Kante finden und das Teilverhältnis angeben – Lösungen außerhalb der Kante verwerfen (abi 2019-be-gk-B3.2f, iqb 2019MgrundlegendBAGLAA2WTR1-1f, Niveau III).
85  - Spuren, Schnittgeraden und Schnittfiguren (Einheit 3): „Welche Koordinate ist null?“ – bei Spuren ankreuzen, welche Koordinaten null sind: beim Achsenpunkt zwei, bei der Spurgeraden in einer Koordinatenebene eine; nichts rechnen (Vorstufe) → die Spurpunkte einer Ebene auf den Achsen bestimmen (Grundfall, viermal; abi 2020-be-gk-B3.1b) → die Spurgeraden in zwei Koordinatenebenen bestimmen und ins Schrägbild einzeichnen (abi 2021-be-gk-B3h; iqb 2021MgrundlegendBAGLAA2WTR1-1e, 2017MerhoehtAAGLAA211-a, Teil A) → die Schnittstrecke mit einer achsenparallelen Ebene über den Seitenparameter (iqb 2018MerhoehtBAGLAA1WTR-1b) → die Schnittfigur einer Ebene mit dem Würfel über parallele Schnittkanten einzeichnen (abi 2025-bebb-lk-A1.3b, iqb 2025MerhoehtAAGLAA212-b, Teil A) → eine Koordinate aus der Schnittfigur zeichnerisch gewinnen: Schnittkante verlängern, Höhe ablesen, Vorgehen beschreiben (iqb 2018MgrundlegendBAGLAA2WTR1-1c, 2018MerhoehtBAGLAA2WTR1-1d) → die Halbierungsfrage am Quadrat entscheiden und begründen (abi 2021-be-gk-B3e) → Prüfungshöhe: die Schnittgerade zweier Ebenen – Nichtparallelität begründen, Parameterform einsetzen (abi 2020-be-gk-B3.1d, Niveau II, LK-Stoff).
86
87  ### Prüfungsform (fhr / abi / iqb)
88  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; das Thema ist dort kein Stoff, themen.csv führt keine fhr-Zeile. Die Rohdatei zählt 37 Zeilen mit 19 Haupttypen (abi 14 Zeilen, 12 Typen; iqb 23 Zeilen, 14 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; das Thema ist selbst der Gegenstand und führt keine Gegenstandsklassen, die Typnamen stehen ohne Präfix). Pool-Sachgebiet: Alternative A2 „Analytische Geometrie“ der Aufgabengruppe AG/LA [IQB-STR 1].
89  fhr: kein Bestand, keine Zeile – das Wahlthema 5 des RLP FOS 2019 endet bei der Lage von Geraden; der fhr-Katalog führt kein Thema der Analytischen Geometrie.
90  abi (14 Zeilen, 12 Typen; Landeshefte bb-ea, be-gk, bebb-gk, bebb-lk 2017–2026) [abi-Katalog]: Schnittpunkt von Gerade und Ebene berechnen (3, E1) · je 1: Durchstoßpunkt einer achsenparallelen Geraden mit einer Ebene berechnen und Abstand im Sachzusammenhang angeben (E1) · Gegebene Rechnung zum Geradenschnittpunkt erläutern (E2) · Halbierung eines Quadrats durch gegebene Ebenen entscheiden und begründen (E3) · Lage zweier Ebenen über die Normalenvektoren entscheiden und Schnittgerade berechnen (E3) · Parameter aus dem Schnitt zweier Geraden ermitteln (E2) · Schnittfigur einer Ebene mit einem Würfel einzeichnen (E3) · Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen (E2) · Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen (E1) · Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen (E3) · Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen (E3) · Zeit bis zum Erreichen einer Ebene aus dem Geradenparameter bestimmen (E1). Muster: Die Schnittrechnung ist das Mittelglied der Geometrieaufgaben in Teil B – nach Ecken, Figuren und Ebenengleichung folgt der Schnitt (Lüftungsrohr 2019-be-gk-B3.1b, Museumsspitze 2018-bb-ea-B3.1a/e, Pavillonspitze 2017-bb-ea-B3.2b, Fahrzeug unter der Strebe 2018-be-gk-B2.1e, Punkt Q am Oktanten-Körper 2023-bebb-gk-B3d, Kantenpunkt H 2026-bb-ea-B3c, Würfelkante mit Parameter 2019-be-gk-B3.2f, Quadrat-Halbierung 2021-be-gk-B3e, Spurgeraden am Holzkörper 2021-be-gk-B3h, Spurpunkte und Schnittgerade 2020-be-gk-B3.1b/d); Teil A stellt den Parameter aus dem Geradenschnitt (2023-bebb-gk-A1.4b) und die Würfel-Schnittfigur des Leistungskurses (2025-bebb-lk-A1.3b). 7 der 14 Zeilen sind wortgleiche Pooldubletten (2019-be-gk-B3.2f, 2021-be-gk-B3h, 2023-bebb-gk-A1.4b, 2025-bebb-lk-A1.3b, 2026-bb-ea-B3c; seit dem Abgleichlauf 27 auch die Museumszeilen 2018-bb-ea-B3.1a und 2018-bb-ea-B3.1e als Dubletten der CAS-Fassung des Pools 2018 erhöht, 2018MerhoehtBAGLAA2CAS1-1a und 2018MerhoehtBAGLAA2CAS1-1e – B3.1e mit Niveau nach dem amtlichen Bereich I statt II); Landeszusätze sind die Sachschnitte der Berliner Hefte 2018–2020 und die Halbierungsfrage 2021. Niveau I 3, II 9, III 2 (2018-be-gk-B2.1e, 2019-be-gk-B3.2f).
91  iqb (23 Zeilen, 14 Typen; Pool 2017–2026, grundlegend 10 und erhöht 13 Zeilen, Teil A 5 und Teil B 18 Zeilen, davon 5 CAS) [iqb-Katalog]: Schnittpunkt von Gerade und Ebene berechnen (4, E1) · Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen (3, E1) · Koordinate eines Punktes aus der Schnittfigur zeichnerisch ermitteln und Vorgehen beschreiben (2, E3) · Parameter aus dem Schnitt zweier Geraden ermitteln (2, E2) · Schattenpunkt bei paralleler Projektion bestimmen (2, E1) · Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen (2, E3) · je 1: Endpunkt der Schnittstrecke eines Vierecks mit einer achsenparallelen Ebene bestimmen (E3) · Gegebene Rechnung zum Geradenschnittpunkt erläutern (E2) · Höhe des Endpunkts einer Strecke auf einer senkrechten Geraden über den Schnitt mit einer Kante berechnen (E2) · Höhe einer Spitze aus dem Abstand ihres Schattenpunkts zu einem Punkt bestimmen (E1) · Rechenweg für den Schnittpunkt einer Geraden mit einer Ebene durch drei Punkte beschreiben (E1) · Schattenpunkt auf einer Kante als Schnittpunkt von Lichtgerade und Kantengerade berechnen (E2) · Schnittfigur einer Ebene mit einem Würfel einzeichnen (E3) · Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen (E2). Muster: Teil A (5 Zeilen, zwei bis vier Punkte) prüft den Schnittpunkt von Gerade und Ebene mit dem zugehörigen Spurgeraden-Bild (2017MerhoehtAAGLAA211-a/b), den Schnittpunkt mit Parameter rückwärts (2023MgrundlegendAAGLAA212-b), den Geradenschnitt an der Ebene (2019MerhoehtAAGLAA21-a) und die Würfel-Schnittfigur (2025MerhoehtAAGLAA212-b); Teil B stellt die Sachschnitte – Pagode 2017 (2017MgrundlegendBAGLAA2WTR1-1d: die Spitze der gedachten Dachpyramide als Schnitt einer Kantengeraden mit der z-Achse, drei Punkte, Niveau I; seit dem Nachzug 2026-09-28), Kletternetz 2018 (2018MerhoehtBAGLAA2WTR2-1f, dazu die Schnittfigur-Ablesungen 2018MgrundlegendBAGLAA2WTR1-1c und 2018MerhoehtBAGLAA2WTR1-1d und die Schnittstrecke 2018MerhoehtBAGLAA1WTR-1b), Haus mit Sonnenlicht 2019 (2019MgrundlegendBAGLAA2WTR2-1g, dazu der Kantenschnitt 2019MgrundlegendBAGLAA2WTR1-1f), Sonnensegel 2020 (2020MgrundlegendBAGLAA2WTR-1d), Mähroboter 2021 (2021MgrundlegendBAGLAA2WTR2-1c, dazu die Spurgeraden 2021MgrundlegendBAGLAA2WTR1-1e), Sichtgrenze 2023 (2023MerhoehtBAGLAA2WTR1-1e, dazu die Spitze 2023MgrundlegendBAGLAA2WTR2-1d) und der Kantenpunkt 2026 (2026MerhoehtBAGLAA2WTR2-1c); die CAS-Stapel (Teil B CAS, 5 Zeilen, seit dem Nachzug 2026-09-29) bringen das Museum 2018 erhöht (2018MerhoehtBAGLAA2CAS1-1a: die vorgelegte Rechnung zur Spitze erläutern; 2018MerhoehtBAGLAA2CAS1-1e: den Schnitt der Geraden AG mit der Ebene des Dreiecks DEF nachweisen, Niveau I – beide wortgleich im Landesheft 2018-bb-ea), den Obelisken 2018 erhöht (2018MerhoehtBAGLAA2CAS2-1a: die Spitze der ergänzten Pyramide als Schnitt einer Kantengeraden mit der z-Achse, Niveau I; 2018MerhoehtBAGLAA2CAS2-1g: neu die Höhe der Spitze aus dem Abstand ihres Schattenpunkts zu einem Punkt, amtlich Anforderungsbereich III, geschätzt II) und den Spielplatzturm 2017 grundlegend (2017MgrundlegendBAGLAA2CAS1-1e: neu der Schattenpunkt auf einer Kante als Schnitt von Lichtgerade und Kantengerade, Niveau II). Amtlicher Anforderungsbereich in allen 23 Zeilen (höchster Bereich: I 6, II 12, III 5); Niveau I 6, II 14, III 3. Kontexte: Pagode, Kletteranlage mit Netz, Haus mit Glasfassade, Sonnensegel, Mähroboter, Mauer mit Sichtgrenze, Pyramidenzelt, Museum, Obelisk, Spielplatzturm. 7 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste).
92  Zielmarke: Einheit 1 – abi: die Zeit bis zur senkrechten Ebene (2018-be-gk-B2.1e, Niveau III) und das Lüftungsrohr mit Maßstab und Zuschlag (2019-be-gk-B3.1b, Niveau II); iqb: der Schnittpunkt in Teil A (2017MerhoehtAAGLAA211-b, 2019MerhoehtAAGLAA21-a, Niveau II) und der beschriebene Rechenweg zur Sichtgrenze (2023MerhoehtBAGLAA2WTR1-1e, Niveau III). Einheit 2 – abi: der Kantenschnitt mit Teilverhältnis (2019-be-gk-B3.2f, Niveau III) und die erläuterte Rechnung zur Museumsspitze (2018-bb-ea-B3.1a, Niveau II); iqb: die Netzkantenhöhe (2018MerhoehtBAGLAA2WTR2-1f, Niveau III) und der Parameter rückwärts in Teil A (2023MgrundlegendAAGLAA212-b, Niveau II). Einheit 3 – abi: die Schnittgerade zweier Ebenen (2020-be-gk-B3.1d, Niveau II, LK-Stoff) und die Halbierungsfrage (2021-be-gk-B3e, Niveau II); iqb: die Würfel-Schnittfigur mit Schnittgerade (2025MerhoehtAAGLAA212-b, Niveau II, Teil A) und das zeichnerische Ablesen mit Vorgehensbeschreibung (2018MerhoehtBAGLAA2WTR1-1d, Niveau II).
````

## 2 Originale (37)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2019-be-gk-B3.1b (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Autotunnel als Teil einer Geraden von S(0 | 40 | 6) nach N(30 | 65 | 7); x-y-Ebene auf Meeresspiegelhöhe, 1 LE = 100 m; Nothaltebucht L(15 | 52,5 | 6,5); Lüftungsrohr senkrecht zum Meeresspiegel nach oben, ragt 2 m aus dem Berg; Bergoberfläche F: 10x + 5y + 7z = 475,5
- gesucht: Länge des Lüftungsrohrs
- verfahren: Senkrechte Gerade durch L (Richtung (0 | 0 | 1)) mit F schneiden, z-Differenz mal 100 m plus 2 m
- fehlerquelle: den Abstand von L zur Ebene (Lot senkrecht zu F) statt der senkrechten Strecke berechnen oder die 2 m vergessen

### 2018-bb-ea-B3.1a (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt. Die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist. Das Dreieck ABC liegt in der x-y-Ebene, das Dreieck DEF parallel dazu. Im kartesischen Koordinatensystem gilt A(−5 | 5 | 0), B(−5 | 25 | 0), D(0 | 0 | 15), E(0 | 30 | 15), F(−25 | 5 | 15) und G(−10 | 10 | 35). Eine Längeneinheit entspricht 1 m in der Realität. Abgedruckt ist eine Rechnung: zuerst wird (0 | 0 | 15) + r · (−5 | 5 | −15) gleich (0 | 30 | 15) + s · (−5 | −5 | −15) gesetzt, woraus r = s = 3 folgt; danach wird r = 3 eingesetzt und S(−15 | 15 | −30) abgelesen.
- gesucht: Erläuterung des dargestellten Vorgehens zur Ermittlung der Koordinaten von S
- verfahren: Erkennen, dass die beiden Terme die Geraden durch D und A sowie durch E und B in Parameterform sind, denn A − D = (−5 | 5 | −15) und B − E = (−5 | −5 | −15). Das Gleichsetzen sucht den gemeinsamen Punkt der beiden Seitenkanten, das Gleichungssystem liefert r = s = 3, und das Einsetzen in eine der beiden Geraden liefert den Ortsvektor der Pyramidenspitze S.
- fehlerquelle: die Rechnung nachvollziehen, ohne die beiden Terme als die Seitenkanten DA und EB des Körpers zu benennen

### 2017-bb-ea-B3.2b (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Pavillon aus Quader und aufgesetzter gerader quadratischer Pyramide; der Grundflächenmittelpunkt ist O(0 | 0 | 0), die Quaderkante AE reicht von A(1,5 | 1,5 | 0) bis E(1,5 | 1,5 | 2,1). Eine Dachkante ist Teil der Geraden g: x = (−1,5 | 1,5 | 2,1) + t · (−1,5 | 1,5 | −1); 1 LE = 1 m.
- gesucht: Gesamthöhe des Pavillons
- verfahren: Die Spitze liegt auf g und zugleich auf der z-Achse, also über dem Grundflächenmittelpunkt: aus −1,5 − 1,5 · t = 0 folgt t = −1. Einsetzen liefert den Punkt; die Gesamthöhe ist dessen z-Koordinate.
- fehlerquelle: die Quaderhöhe 2,1 m und die Pyramidenhöhe verwechseln oder nur die Pyramidenhöhe angeben

### 2018-be-gk-B2.1e (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Das Fahrzeug fährt geradlinig und gleichförmig von P(82 | 40 | 0) über Q(42 | 36 | 0) weiter; für die Strecke von P nach Q braucht es 1,5 s. Die Strebe durch A(0 | 0 | 5) und B(4,4 | 44 | 5) liegt in der Ebene E: −10x + y = 0, die senkrecht auf der Fahrbahn steht; 1 LE = 1 m.
- gesucht: Zeit, die das Fahrzeug von Q bis zu dem Punkt braucht, der genau vertikal unter der Strebe durch A und B liegt
- verfahren: Genau vertikal unter der Strebe liegen die Punkte der Fahrbahn, die in der Ebene E liegen, weil E senkrecht auf der Fahrbahn steht und die Strebe enthält. Die Fahrzeugbahn x = Q + r · (−40 | −4 | 0) in E einsetzen: −10 · (42 − 40r) + (36 − 4r) = 0 ergibt r = 32/33. Da r = 1 der Zeitspanne 1,5 s entspricht, ist die gesuchte Zeit 1,5 s · 32/33.
- fehlerquelle: den Fußpunkt als Lotfußpunkt auf die Gerade durch A und B bestimmen, statt den Durchstoßpunkt der Fahrbahnbahn mit der senkrechten Ebene E zu suchen

### 2023-bebb-gk-B3d (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Körper ABCDEF: Die Eckpunkte A(4 | 0 | 0), B(0 | 4 | 0) und C(0 | 0 | 4) liegen in der Ebene L1: x + y + z = 4, die Eckpunkte D, E und F jeweils auf einer Koordinatenachse und in der Ebene L2: 2x + 2y + 2z = 5 (also D(2,5 | 0 | 0), E(0 | 2,5 | 0), F(0 | 0 | 2,5)). M(2 | 2 | 0) ist der Mittelpunkt von AB; die Gerade durch P(0 | 0 | 2) und M schneidet L2 im Punkt Q.
- gesucht: Koordinaten von Q
- verfahren: Gerade durch P und M mit Richtungsvektor PM = (2 | 2 | −2) aufstellen, in 2x + 2y + 2z = 5 einsetzen, t = 1/4, Punkt berechnen.
- fehlerquelle: beim Einsetzen die Koordinaten des Aufpunkts vergessen (nur den Richtungsvektor einsetzen)

### 2026-bb-ea-B3c (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: L: −2x + y + 4 = 0 schneidet die Kante CD in H; Kontrolle H(2,8 | 1,6 | 0)
- gesucht: Koordinaten von H
- verfahren: Geradengleichung der Kante, Parameter aus L
- fehlerquelle: Parameter aus [0; 1] erwarten und μ = 1,4 verwerfen (Stützpunkt D)

### 2019-be-gk-B3.2f (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Würfel ABCDEFGH mit G(5 | 5 | 5) und H(0 | 5 | 5) im Koordinatensystem; I(5 | 0 | 1), J(2 | 5 | 0), K(0 | 5 | 2), L(1 | 0 | 5) liegen auf Kanten; Gerade g: x = (4 − r | 0 | r² + 1) + u · (4 | −5 | 0), u ∈ IR, schneidet für einen Wert von r die Kante GH
- gesucht: Verhältnis, in dem der Schnittpunkt die Kante GH teilt
- verfahren: g mit der Geraden GH gleichsetzen: aus y folgt u = −1, aus z folgt r² + 1 = 5, aus x folgt w; nur w ∈ [0; 1] (r = −2, w = 3/5) liegt auf der Kante
- fehlerquelle: r = 2 mit w = 7/5 nicht ausschließen (Punkt außerhalb der Kante)

### 2021-be-gk-B3e (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 4 · format Begründung · antwort Text
- gegeben: Quadrat ABCD mit A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0); Ebenen E₁: y = 5, E₂: −x + y = 0, E₃: z = 5
- gesucht: für jede Ebene, ob sie das Quadrat in zwei flächengleiche Figuren teilt
- verfahren: Schnittmenge jeder Ebene mit dem Quadrat bestimmen
- fehlerquelle: E₂ als Ebene durch B und D lesen

### 2021-be-gk-B3h (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Holzkörper mit den Eckpunkten A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0) und E(0 | 10 | 6) (Pyramide über dem Quadrat ABCD mit Spitze E senkrecht über D); B, D, E liegen in der Symmetrieebene; 1 LE = 1 cm; L: 3x + 5z = 30; F = Schnittpunkt von L mit der z-Achse
- gesucht: F und die Schnittgeraden von L mit der xz- und der yz-Ebene in die Abbildung einzeichnen
- verfahren: F aus x = y = 0; Spurgeraden durch B und F bzw. F und E
- fehlerquelle: F auf der falschen Höhe eintragen

### 2020-be-gk-B3.1b (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 2 · format Kurzantwort · antwort Zahl
- gegeben: E₁: 12x + 4y + 9z = 36
- gesucht: die drei Schnittpunkte von E₁ mit den Koordinatenachsen
- verfahren: Achsenabschnitte aus der Koordinatengleichung
- fehlerquelle: Koeffizienten statt Quotienten angeben

### 2023-bebb-gk-A1.4b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: g: x = (2 | 3 | −7) + s · (1 | 0 | 5); Gerade h durch A(4 | 0 | 0) und B(5 | 1 | b) mit reellem b; g und h haben einen gemeinsamen Punkt.
- gesucht: Wert von b
- verfahren: h aufstellen und mit g gleichsetzen; die zweite Koordinate liefert r = 3, die erste s = 5, die dritte 18 = 3b.
- fehlerquelle: für h denselben Parameter s wie für g verwenden

### 2025-bebb-lk-A1.3b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 3 · format Zeichnen|Kurzantwort · antwort Grafik|Term
- gegeben: Würfel ABCDEFGH der Kantenlänge 4 wie in der Abbildung, Ebene K durch A, B und den Mittelpunkt von FG; Ebene L enthält E(0; 0; 4), F(4; 0; 4) und den Mittelpunkt (4; 2; 0) der Kante BC
- gesucht: Schnittfigur von L mit dem Würfel in der Abbildung|Gleichung der Schnittgeraden von K und L
- verfahren: L schneidet die Flächen x = 4 und x = 0 in parallelen Strecken von F bzw. E zu den Kantenmitten (4; 2; 0) bzw. (0; 2; 0), die Schnittfigur ist ein Rechteck; beide Ebenen enthalten Geraden in x-Richtung, die Schnittgerade verläuft durch den Schnittpunkt (0; 1; 2) der Schnittstrecken in der Ebene x = 0
- fehlerquelle: die Schnittfigur an den Ecken B und C enden lassen statt an den Kantenmitten

### 2018-bb-ea-B3.1e (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt. Die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist. Das Dreieck ABC liegt in der x-y-Ebene, das Dreieck DEF parallel dazu. Im kartesischen Koordinatensystem gilt A(−5 | 5 | 0), B(−5 | 25 | 0), D(0 | 0 | 15), E(0 | 30 | 15), F(−25 | 5 | 15) und G(−10 | 10 | 35). Eine Längeneinheit entspricht 1 m in der Realität. Behauptet wird, dass sich die Gerade durch A und G und die Ebene, in der das Dreieck DEF liegt, im Punkt R(−50/7 | 50/7 | 15) schneiden.
- gesucht: Nachweis dieses Schnittpunkts
- verfahren: Die Gerade durch A und G aufstellen: Stützvektor A, Richtungsvektor G − A = (−5 | 5 | 35). Da D, E und F alle den z-Wert 15 haben, ist ihre Ebene z = 15. Die z-Koordinate der Geraden gleich 15 setzen, den Parameter bestimmen und einsetzen.
- fehlerquelle: die Ebene des Dreiecks DEF aufwendig aus drei Punkten bestimmen, statt am gemeinsamen z-Wert 15 abzulesen

### 2018MerhoehtBAGLAA2CAS1-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Begründung · antwort Text
- gegeben: Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt; die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist; die Ebene, in der das Dreieck ABC liegt, beschreibt die Horizontale, das Dreieck DEF liegt parallel zu dieser Ebene; A(−5; 5; 0), B(−5; 25; 0), D(0; 0; 15), E(0; 30; 15), F(−25; 5; 15), G(−10; 10; 35); 1 LE = 1 m; abgedruckte Rechnung: (0; 0; 15) + r · (−5; 5; −15) = (0; 30; 15) + s · (−5; −5; −15) ⇔ r = s = 3; (0; 0; 15) + 3 · (−5; 5; −15) = (−15; 15; −30), d. h. S(−15; 15; −30)
- gesucht: Erläuterung des dargestellten Vorgehens zur Ermittlung der Koordinaten von S
- verfahren: Die beiden Terme als Geraden AD (Stützpunkt D, Richtung DA) und BE (Stützpunkt E, Richtung EB) erkennen; das Gleichsetzen liefert die Parameter des Schnittpunkts, das Einsetzen von r = 3 in die Gerade AD die Koordinaten der Spitze S
- fehlerquelle: die Rechnung nur nacherzählen, ohne die Terme als die Kantengeraden AD und BE zu benennen

### 2018MerhoehtBAGLAA2CAS1-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt; die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist; die Ebene, in der das Dreieck ABC liegt, beschreibt die Horizontale, das Dreieck DEF liegt parallel zu dieser Ebene; A(−5; 5; 0), B(−5; 25; 0), D(0; 0; 15), E(0; 30; 15), F(−25; 5; 15), G(−10; 10; 35); 1 LE = 1 m; Punkt R(−50/7; 50/7; 15)
- gesucht: Nachweis, dass sich die Gerade AG und die Ebene, in der das Dreieck DEF liegt, im Punkt R schneiden
- verfahren: D, E, F und R haben die x3-Koordinate 15; die Gerade AG aufstellen und zeigen, dass R sie für einen Parameterwert erfüllt
- fehlerquelle: nur zeigen, dass R in der Ebene liegt, und die Punktprobe mit der Gerade AG vergessen

### 2017MerhoehtAAGLAA211-a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Ebene E: x1 + x2 + 2x3 = 4 und die Gerade g: x = (2; 1; −2) + λ · (2; −1; −3); Schrägbild eines Koordinatensystems
- gesucht: Schnittgerade von E mit der x2x3-Ebene in der Abbildung
- verfahren: x1 = 0 setzen, die Spurpunkte auf der x2- und der x3-Achse bestimmen und verbinden
- fehlerquelle: die Spurgerade in der x1x2-Ebene zeichnen

### 2023MgrundlegendAAGLAA212-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: g: x = (2; 3; −7) + s · (1; 0; 5); h durch A(4; 0; 0) und B(5; 1; b) mit reellem b; g und h haben einen gemeinsamen Punkt
- gesucht: Wert von b
- verfahren: h aufstellen, mit g gleichsetzen; die zweite Koordinate liefert r, die erste s, die dritte b
- fehlerquelle: für h denselben Parameter s wie für g verwenden

### 2019MerhoehtAAGLAA21-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: g: x = (0; 2; 0) + r · (2; 4; 1); E: x1 + 2x2 − 2x3 = 2; g und E schneiden sich in S
- gesucht: Koordinaten von S
- verfahren: Einsetzen, r bestimmen, Punkt berechnen
- fehlerquelle: −2x3 mit +2r ansetzen

### 2025MerhoehtAAGLAA212-b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 3 · format Zeichnen|Kurzantwort · antwort Grafik|Term
- gegeben: Würfel ABCDEFGH der Kantenlänge 4 wie in der Abbildung, Ebene K durch A, B und den Mittelpunkt von FG; Ebene L enthält E(0; 0; 4), F(4; 0; 4) und den Mittelpunkt (4; 2; 0) der Kante BC
- gesucht: Schnittfigur von L mit dem Würfel in der Abbildung|Gleichung der Schnittgeraden von K und L
- verfahren: L schneidet die Flächen x = 4 und x = 0 in parallelen Strecken von F bzw. E zu den Kantenmitten (4; 2; 0) bzw. (0; 2; 0), die Schnittfigur ist ein Rechteck; beide Ebenen enthalten Geraden in x-Richtung, die Schnittgerade verläuft durch den Schnittpunkt (0; 1; 2) der Schnittstrecken in der Ebene x = 0
- fehlerquelle: die Schnittfigur an den Ecken B und C enden lassen statt an den Kantenmitten

### 2017MgrundlegendBAGLAA2WTR1-1d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Pagode mit drei Dachetagen aus je vier Dachflächen gleicher Form und Größe; die Dachflächen der mittleren und oberen Etage sind jeweils parallel zu einer Dachfläche der unteren Etage; die Dachflächen der unteren Etage sind Vierecke mit den Eckpunkten A1(5,5; −5,5; 6), B1(5,5; 5,5; 6), C1(−5,5; 5,5; 6), D1(−5,5; −5,5; 6), A2(2; −2; 8,1), B2(2; 2; 8,1), C2(−2; 2; 8,1) und D2(−2; −2; 8,1); die xy-Ebene ist die Horizontale, 1 LE = 1 m; die Strecke A1A2 ist Teil einer Geraden g
- gesucht: Koordinaten des Schnittpunkts von g mit der z-Achse
- verfahren: g: x = (5,5; −5,5; 6) + λ · (−3,5; 3,5; 2,1); aus x = 0 folgt λ = 11/7, damit y = 0 und z = 9,3
- fehlerquelle: nur x = 0 einsetzen und nicht bestätigen, dass dann auch y = 0 ist

### 2018MerhoehtBAGLAA2WTR2-1f (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 8 · format Rechnung · antwort Zahl
- gegeben: Kletteranlage im Koordinatensystem (x1x2-Ebene ist der Untergrund, 1 LE = 1 m): Pfähle durch P1(0 | 0 | 0) und P2(5 | 10 | 0); Kletterwand mit den Eckpunkten A(3 | 0 | 2), B(0 | 3 | 2), E(6 | 0 | 0), F(0 | 6 | 0); Plattform 2 mit den Eckpunkten R(5 | 7 | 3), S(8 | 13 | 3), T(2 | 10 | 3); Kletternetz als ebenes Viereck zwischen den Pfählen: untere Ecken bei (0 | 0 | 2) am Pfahl 1 und oberhalb der Plattform 2 am Pfahl 2, an jedem Pfahl Abstand 1,80 m zwischen den beiden dort befestigten Ecken; die untere Netzkante berührt die Plattform 2 an der Seite RT
- gesucht: Abstand des unteren Eckpunkts am Pfahl 2 von der Plattform 2
- verfahren: Untere Netzkante als Gerade durch (0 | 0 | 2) und U(5 | 10 | z_U), Schnitt mit der Geraden RT aus den ersten beiden Koordinaten, dritte Gleichung liefert z_U
- fehlerquelle: U auf der Höhe 3 der Plattform ansetzen

### 2018MgrundlegendBAGLAA2WTR1-1c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Quader mit den Eckpunkten A(4 | 0 | 0), B(4 | 4 | 0), C(0 | 4 | 0) und F(4 | 4 | 3); die Gerade h verläuft durch B und F; gepunktet die Schnittfigur des Quaders mit einer Ebene durch A, C und einen Punkt P von h
- gesucht: Beschreibung, wie man mithilfe der Abbildung ermittelt, dass P die x3-Koordinate 6 hat
- verfahren: Eine geeignete Seite der Schnittfigur so verlängern, dass sie h schneidet; der Schnittpunkt ist P, seine Höhe abzulesen
- fehlerquelle: P als Punkt der Schnittfigur selbst suchen

### 2018MerhoehtBAGLAA2WTR1-1d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Quader mit den Eckpunkten A(4 | 0 | 0), B(4 | 4 | 0), C(0 | 4 | 0) und F(4 | 4 | 3); die Gerade h verläuft durch B und F; P_t(4 | 4 | t) auf h, Ebenenschar E_t: t x1 + t x2 − 4 x3 − 4t = 0 durch A, C und P_t; eine Ebene E_t zerlegt den Quader, die Schnittfigur ist gepunktet abgebildet
- gesucht: Beschreibung, wie man mithilfe der Abbildung t = 6 ermittelt
- verfahren: Passende Seite der Schnittfigur bis h verlängern, x3 des Schnittpunkts ablesen
- fehlerquelle: P_t innerhalb der Schnittfigur suchen

### 2018MerhoehtBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Viereck ABCD mit A(0 | 0 | 0), B(0 | 6 | 0), C(−4 | 14 | 4), D(−4 | 8 | 4) im räumlichen Koordinatensystem (Abbildung mit Achsen x, y, z); Ebene parallel zur xy-Ebene durch (0 | 0 | 1) schneidet das Viereck in einer Strecke
- gesucht: Koordinaten eines Endpunkts dieser Strecke
- verfahren: z-Koordinate 1 auf der Seite AD (oder BC) über den Parameter
- fehlerquelle: k = 1/4 auf AC statt auf einer Seite anwenden

### 2019MgrundlegendBAGLAA2WTR2-1g (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 5 · format Rechnung|Zeichnen · antwort Zahl|Grafik
- gegeben: Haus als Körper ABCDIJKL: Quader ABCDEFGH und Dachprisma EFGHIJKL; A(0 | 0 | 0), G(10 | 6 | 10), H(0 | 6 | 10), K(10 | 6 | 10,5), L(0 | 6 | 13); verglaste Fassade IEHL; 1 LE = 1 m; Sonnenlicht durch die Fassade IEHL mit Richtungsvektor (3; −2; −2); ein Eckpunkt des beschienenen Flächenstücks auf dem Boden des Dachgeschosses liegt nicht am Rand
- gesucht: Koordinaten dieses Eckpunkts; alle beschienenen Flächenstücke in der Abbildung
- verfahren: Lichtgerade durch L mit dem Boden z = 10 schneiden; Schattenfigur einzeichnen
- fehlerquelle: den Schatten von I (auf der Höhe 13, y = 0) statt von L verfolgen; der Schatten von I trifft die Seitenwand y = 0 nicht den Boden

### 2019MgrundlegendBAGLAA2WTR1-1f (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Würfel ABCDEFGH mit G(5 | 5 | 5) und H(0 | 5 | 5) (A im Ursprung, Kantenlänge 5); I(5 | 0 | 1), J(2 | 5 | 0), K(0 | 5 | 2), L(1 | 0 | 5) auf Kanten des Würfels; g: x = (4 − r; 0; r² + 1) + u · (4; −5; 0), u ∈ IR; für einen Wert von r schneidet g die Kante GH
- gesucht: Verhältnis, in dem der Schnittpunkt die Kante GH teilt
- verfahren: g mit der Geraden GH gleichsetzen, r aus III, u aus II, w aus I; w ∈ [0; 1] wählen
- fehlerquelle: r = 2 mit w = 7/5 als Lösung außerhalb der Kante nicht verwerfen

### 2020MgrundlegendBAGLAA2WTR-1d (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Sonnensegel als Dreieck ABC mit A(−1 | 1 | 2), B(−1 | 5 | 2), C(−4 | 3 | 3) zwischen drei Masten; Untergrund = x₁x₂-Ebene; 1 LE = 1 m; die Ebene des Dreiecks hat eine Gleichung der Form x₁ + 3x₃ = j; Schatten der unteren Eckpunkte A und B auf dem Untergrund: A'(−5 | 3 | 0), B'(−5 | 7 | 0) (paralleles Sonnenlicht); Kontrolle: (−10 | 6 | 0)
- gesucht: Koordinaten des Schattens des oberen Eckpunkts C
- verfahren: Lichtgerade durch C mit Richtung AA' aufstellen und x₃ = 0 setzen
- fehlerquelle: Lichtrichtung aus B und B' anders als aus A und A' vermuten oder x₃ = 3 belassen

### 2021MgrundlegendBAGLAA2WTR2-1c (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Ebene Rasenfläche mit den Eckpunkten A(0 | 0 | 0), B(18 | 0 | 1,5), C(12 | 10 | 1), D(12 | 15 | 1), E(0 | 15 | 0); AB ∥ DE; 1 LE = 1 m; Mähroboter: Mittelpunkt der kreisförmigen Unterseite (Radius 20 cm) berührt die Fläche, Start P(3,6 | 8 | 0,3), Bewegung entlang der Geraden g durch P mit Richtungsvektor (12; −4; 1) auf den Rand BC zu; Kontrolle: Q(15,6 | 4 | 1,3)
- gesucht: Koordinaten des Punkts Q, in dem g die Strecke BC schneidet
- verfahren: g und die Gerade BC gleichsetzen, λ aus zwei Gleichungen, dritte als Probe
- fehlerquelle: dritte Gleichung nicht prüfen; μ außerhalb [0; 1] nicht bemerken

### 2021MgrundlegendBAGLAA2WTR1-1e (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Holzkörper mit den Eckpunkten A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0) und E(0 | 10 | 6) (Pyramide über dem Quadrat ABCD, Spitze E senkrecht über D); B, D und E liegen in der Symmetrieebene des Körpers; 1 LE = 1 cm; L: 3x + 5z = 30; F = Schnittpunkt von L mit der z-Achse
- gesucht: F und die Schnittgeraden von L mit der xz- und der yz-Ebene in der Abbildung
- verfahren: F(0 | 0 | 6) eintragen, Geraden BF und FE einzeichnen
- fehlerquelle: F auf der Höhe von E, aber nicht auf der z-Achse eintragen

### 2023MerhoehtBAGLAA2WTR1-1e (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Mauerkante PQ mit P(20|−5|3), Q(20|25|3); Auge K(24|15|1); nicht sichtbares Dreieck GBH mit H auf BE
- gesucht: Beschreibung, wie H rechnerisch bestimmt werden könnte
- verfahren: H als Schnittpunkt der Kantengeraden BE mit der Ebene durch K, P, Q; Gleichungssystem nach λ
- fehlerquelle: Sichtgrenze als Gerade durch K und einen Mauerpunkt statt als Ebene ansetzen

### 2023MgrundlegendBAGLAA2WTR2-1d (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Körper ABCDEF ergänzt zur Pyramide mit Grundfläche ABC und Spitze S; D, E, F auf den Kanten; Kontrolle S(0|0|5)
- gesucht: Koordinaten von S
- verfahren: S liegt auf der x₃-Achse; Gerade durch A und D mit der x₃-Achse schneiden
- fehlerquelle: Richtungsvektor AD statt DA mit falschem Vorzeichen

### 2026MerhoehtBAGLAA2WTR2-1c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: L: −2x + y + 4 = 0 schneidet die Kante CD in H; Kontrolle H(2,8 | 1,6 | 0)
- gesucht: Koordinaten von H
- verfahren: Geradengleichung der Kante, Parameter aus L
- fehlerquelle: Parameter aus [0; 1] erwarten und μ = 1,4 verwerfen (Stützpunkt D)

### 2018MerhoehtBAGLAA2CAS2-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Modell eines Obelisken (nicht maßstabsgetreu) im kartesischen Koordinatensystem; die xy-Ebene beschreibt den ebenen Untergrund, 1 LE = 1 m; der untere Teilkörper ABCDEFGH mit B(0,45; 0,45; 0) ist ein Stumpf einer geraden Pyramide, der Mittelpunkt des Quadrats ABCD ist der Koordinatenursprung, das Quadrat EFGH ist parallel zur xy-Ebene; der obere Teilkörper EFGHS mit E(0,35; −0,35; 7,16) ist eine gerade Pyramide, ihre Spitze S liegt auf der z-Achse und stellt die Spitze des Obelisken dar; zur Kontrolle: z-Koordinate des Schnittpunkts 32,22
- gesucht: Koordinaten des Schnittpunkts der Gerade AE mit der z-Achse
- verfahren: A(0,45; −0,45; 0) folgt aus B und dem Mittelpunkt im Ursprung; Gerade AE aufstellen, x- und y-Koordinate gleich 0 setzen und r einsetzen
- fehlerquelle: A falsch aus B ablesen (etwa (−0,45; 0,45; 0)) oder mit E statt A als Stützpunkt falsch weiterrechnen

### 2018MerhoehtBAGLAA2CAS2-1g (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Modell eines Obelisken (nicht maßstabsgetreu) im kartesischen Koordinatensystem; die xy-Ebene beschreibt den ebenen Untergrund, 1 LE = 1 m; der untere Teilkörper ABCDEFGH mit B(0,45; 0,45; 0) ist ein Stumpf einer geraden Pyramide, der Mittelpunkt des Quadrats ABCD ist der Koordinatenursprung, das Quadrat EFGH ist parallel zur xy-Ebene; der obere Teilkörper EFGHS mit E(0,35; −0,35; 7,16) ist eine gerade Pyramide, ihre Spitze S liegt auf der z-Achse und stellt die Spitze des Obelisken dar; Sonnenlicht fällt im Modell in parallelen Geraden mit dem Richtungsvektor v = (1; 1; −2) auf den Obelisken; der Schatten der Spitze liegt auf dem Untergrund und hat von dem Punkt, der im Modell durch B dargestellt wird, den Abstand 5,1 m
- gesucht: Höhe des Obelisken
- verfahren: Lichtgerade durch S(0; 0; z_S) mit Richtung v mit der xy-Ebene schneiden: S'(z_S/2; z_S/2; 0); |BS'| = 5,1 nach z_S > 0 lösen
- fehlerquelle: den Schattenpunkt mit fester Höhe berechnen oder den Abstand zum Ursprung statt zu B ansetzen

### 2017MgrundlegendBAGLAA2CAS1-1e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m; an der Spitze des Dachs ist eine gerade Stange mit dem oberen Endpunkt T(0; 0; 5,5) befestigt; Sonnenlicht wird durch parallele Geraden mit dem Richtungsvektor (5; −1; −3) beschrieben; der untere Endpunkt des Schattens liegt auf der Dachkante EF
- gesucht: Koordinaten des Punkts, der den unteren Endpunkt des Schattens darstellt
- verfahren: Lichtgerade durch T mit dem Richtungsvektor (5; −1; −3) und die Gerade durch E und F gleichsetzen: (0; 0; 5,5) + r · (5; −1; −3) = (2; −3; 4) + s · (1; 5; 0); r = 0,5 einsetzen
- fehlerquelle: die Lichtgerade mit der Grundebene z = 0 statt mit der Dachkante schneiden

### 2017MerhoehtAAGLAA211-b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: E: x1 + x2 + 2x3 = 4; g: x = (2; 1; −2) + λ · (2; −1; −3), λ ∈ IR
- gesucht: Koordinaten des Schnittpunkts von E und g
- verfahren: Koordinaten von g in E einsetzen, λ bestimmen, Punkt berechnen
- fehlerquelle: Vorzeichen bei 2 · (−2 − 3λ)

### 2020-be-gk-B3.1d (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 4 · format Begründung|Rechnung · antwort Text|Term
- gegeben: E₁: x = (3 | 0 | 0) + r · (−3 | 9 | 0) + s · (−3 | 0 | 4), r, s ∈ IR; E₂: 6x + 2y + 9z = 18 mit E₁: 12x + 4y + 9z = 36
- gesucht: Begründung, dass E₁ und E₂ nicht parallel sind; Schnittgerade von E₁ und E₂
- verfahren: Normalenvektoren vergleichen; x, y, z aus der Parameterform von E₁ in E₂ einsetzen, s = 0, in E₁ einsetzen
- fehlerquelle: beide Koordinatengleichungen gleichsetzen und nicht nach einem Parameter auflösen

Nicht in den Prüfungsdateien gefunden: 2018-bb-ea

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
