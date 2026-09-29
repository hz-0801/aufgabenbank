# Mappe: extremalprobleme

Eintrag: hz-0801/mathe-nachhilfe, katalog/extremalprobleme.md
Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719 (2026-09-28T22:05:53Z, „Katalog-Nachzug Teil 2: Sek II aus den Urteilen vom 28.09.“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-29 13:56 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Extremalprobleme
 3
 4  ### Verortung
 5  Die Extremwertaufgabe mit Nebenbedingung: eine geometrische Größe (Flächeninhalt, Umfang, Abstand) soll möglichst groß oder klein werden – die Figur wird ins Koordinatensystem gezeichnet, ihr Term aus … (gekürzt, 2132 Zeichen)
 6  [GOST] Q1, 1. Kurshalbjahr „Analysis; Lineare Algebra“ (BB S. 23–25), Grund- und Leistungskursfach: L4-Zeile „Funktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammenhänge nutzen“ mit d … (gekürzt, 1308 Zeichen)
 7  [FOS] Pflichtthema 2 „Differentialrechnung“ (S. 26), Thema „Extremwertaufgaben“ (L2, L3, L4): „Ermitteln der Zielfunktion und Untersuchung auf lokale Extrema“, „Umfang und Flächeninhalt ebener Figuren in Zusammenhang mit Funktionsgraphen“, „Umfang und Flächeninhalt ebener Figuren in Anwendungsaufgaben“, „Oberflächeninhalt und Volumen von Körpern“. Befund: Körper (Oberfläche, Volumen) stehen im Plan, aber die Hefte 2019–2026 prüfen nur Flächen und Umfänge – kein Original in der Rohdatei; die Zielfunktion heißt im Plan wörtlich so.
 8  [LS-AA] Qualifikationsphase Kapitel I „Grundlagen der Differenzialrechnung“: 8 Extremwertprobleme mit Nebenbedingungen (nach 5 Monotonie und Krümmung, 6 Extrem- und Wendepunkte, 7 Tangente und Normale … (gekürzt, 834 Zeichen)
 9
10  ### Lerneinheiten
11  1. Figur und Term – die Figur am Graphen: Ecken als (x | f(x)), Seiten als Koordinaten, Differenzen und Funktionswerte; Rechteck, Dreieck und Trapez für konkrete Werte in ein Koordinatensystem einzeic … (gekürzt, 603 Zeichen)
12    Marken: BE Q1 · BB Q1 · GK · Abitur LK · FHR
13  2. Zielfunktion aus Haupt- und Nebenbedingung – die zu optimierende Größe als Hauptbedingung mit zwei Variablen, den festen Zusammenhang als Nebenbedingung (Punkt auf dem Graphen, feste Material- oder Umfangslänge), umstellen und einsetzen; die Zielfunktion ausmultiplizieren und mit sinnvollem Definitionsbereich angeben; vorgegebene Zielfunktionen nachweisen; für konkrete Werte rechnen, bevor verallgemeinert wird. (Q1, GK-Kern „Extremalprobleme“; FOS „Ermitteln der Zielfunktion“) ← Eingabe „zielfunktion“, „nebenbedingung“, „hauptbedingung“, „extremwertaufgabe aufstellen“
14    Marken: BE Q1 · BB Q1 · GK · FHR
15  3. Maximum bestimmen und deuten – die Zielfunktion ableiten, A'(x) = 0 lösen, Lösungen außerhalb des Definitionsbereichs verwerfen, Art über die zweite Ableitung oder den Vorzeichenwechsel, Randwerte  … (gekürzt, 771 Zeichen)
16    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
17  Warum drei: Plan und Lehrwerk führen das Thema als einen Block (QP I 8); die drei Einheiten folgen den drei Arbeitsschritten Figur → Zielfunktion → Extremum, die die fhr-Hefte als Teilaufgabenketten g … (gekürzt, 709 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
21  Einheit 1: kein Berechnungstyp — Nachweis: Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen (1) · Flächenterm eines einbeschriebenen Trapezes über die Mittelparallele geometrisch herleiten (1) — Deutung: Dreieck in das Koordinatensystem einzeichnen (1) · Dreieck zu Schnittpunkten mit einer Parallelen zur x-Achse einzeichnen (1; Ermessen, siehe Offene Punkte) · Einbeschriebenes Trapez zu einem Parameterwert in die Abbildung einzeichnen (1) · Rechteck in das Koordinatensystem einzeichnen (1) · Term für die Schenkellänge eines einbeschriebenen Trapezes aufstellen (1). Dazu: Fehler finden (die Höhe als Stelle statt als Funktionswert genommen; nur eine Seite verdoppelt; die Schenkellänge mit der Differenz der parallelen Seiten verwechselt; eine Ecke falsch gelesen) · Begründen (warum die Seiten der Figur Koordinaten und Funktionswerte sind; warum die Trapezfläche Mittelparallele mal Höhe ist).
22  Einheit 2: Zielfunktion aus Haupt- und Nebenbedingung aufstellen (3) · Flächeninhalt bei gegebener Nebenbedingung berechnen (1). Dazu: Fehler finden (die Nebenbedingung nach der falschen Variablen umgestellt; den Umfang als einfache statt doppelte Summe angesetzt; das Material auf vier statt drei Seiten verteilt; den Faktor ein halb der Dreiecksfläche im Term verloren) · Begründen (warum die Zielfunktion nur noch eine Variable haben darf; warum der Definitionsbereich zur Figur gehört).
23  Einheit 3: Größten oder kleinsten vertikalen Abstand zweier Graphen über die Differenzfunktion bestimmen (6; Ermessen, siehe Offene Punkte) · Maximum der Zielfunktion bestimmen (3) · Parameter für den größten Flächeninhalt über die Ableitung bestimmen (3) · Achsenparalleles Rechteck maximaler Fläche zwischen Ursprung und Graphenpunkt bestimmen (1) · Kleinsten Abstand eines Punktes zu einem Graphen über die Abstandsfunktion bestimmen (1; Ermessen, siehe Offene Punkte) — Nachweis: Ausschluss einer Stelle als Maximalstelle einer Rechtecksfläche über die notwendige Bedingung nachweisen (1) — Deutung: Aufgabenstellung zu einer Extremwertaufgabe mit Dreiecksfläche aus dem Lösungsweg formulieren und Schritte erläutern (1). Dazu: Fehler finden (die Lösung außerhalb des Definitionsbereichs verwendet; die Extremstelle statt des Extremwerts angegeben; das Minimum der Differenz als Maximalstelle genommen; die hinreichende Bedingung vergessen; f' statt A' betrachtet) · Begründen (warum am Rand die Figur entartet und das größte Exemplar im Inneren liegt; warum der vertikale Abstand die Differenz der Funktionswerte ist).
24  Zählung: 7 + 2 + 7 = 16 Haupttypen, 7 + 4 + 16 = 27 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: CAS-Nachtrag 2018 und Pool 2017 erhöht Teil B, CAS; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags: Pool 2017 grundlegend Teil B CAS, Berliner CAS-Heft 2018 GK, samt der Typumbenennung des Abgleichlaufs 28).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Extrempunkte über notwendige und hinreichende Bedingung, Randvergleich auf einem Intervall – das Werkzeug von Einheit 3. Thema kurvenuntersuchung.md Einheit 2 (dasselbe Kurshalbjahr; Blatt 0 verweist auf ein Nachbarthema derselben Stufe, Klarstellung in Entscheidung 36). [GOST Q1 L4 „die Ableitung zur Bestimmung von … Extrempunkten … nutzen“, „Randextrema“; GOST-OHiMi 2.2 „Extrempunkte und Wendepunkte (notwendiges und hinreichendes Kriterium)“; FOS „Untersuchung auf lokale Extrema“]
29  - Ableitungen bilden: Potenz-, Faktor- und Summenregel; GK und LK zusätzlich Produkt- und Kettenregel für e-Funktions-Produkte – die Ableitung der Zielfunktion in Einheit 3. Thema ableitungsregeln.md. [GOST Q1 L4 „Funktionen ableiten …“; FOS „Ableitungsregeln“; FS-IQB 1.2]
30  - Gleichungen lösen: linear, quadratisch mit Lösungsformel, biquadratisch mit Substitution, Ausklammern und Nullprodukt – die nullgesetzte Ableitung der Zielfunktion in Einheit 3. Thema gleichungen-loesen.md. [GOST Q1 L1 „lineare, allgemeine quadratische und biquadratische Gleichungen“; FOS Pflichtthema 1 „Lösungsverfahren ganzrationaler Gleichungen“]
31  - Flächen- und Umfangsformeln von Rechteck, Dreieck und Trapez, Satz des Pythagoras für Streckenlängen – die Hauptbedingung in Einheit 1 und 2. Sek-I-Themen flaechen.md, pythagoras.md. [GOST Eingangsvoraussetzung L3 „berechnen Größen … von Figuren“; RLP E–F Flächeninhalt und Umfang; FS-IQB 1.1]
32  - Punkte (x | f(x)) im Koordinatensystem lesen und Figuren einzeichnen, Funktionswerte berechnen – Einheit 1 und die Kontrolle in Einheit 3. Sek-I-Thema lineare-funktionen.md (Koordinatensystem, Funktionswert). [GOST Eingangsvoraussetzung L4; FOS Pflichtthema 1 „Funktionsdarstellungen“]
33  - Terme ausmultiplizieren und zusammenfassen – die Zielfunktion in die ableitbare Form bringen, vorgegebene Terme nachweisen, Einheit 2. Sek-I-Thema terme.md. [GOST Eingangsvoraussetzung L1 „formen Terme … um“; RLP E–F Terme]
34  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt): keine eigenen – seit 27.09.2026 gestrichen, weil die Vorstufen der Ketten denselben Handgriff verlangen.
35
36  ### Merkkasten
37  Einheit 1 (Figur und Term):
38      Ecken aus dem Graphen: Ein Punkt auf dem Graphen hat die Koordinaten (x | f(x)) – die Seiten der Figur sind Koordinaten, Differenzen und Funktionswerte. Rechteck mit Ecken auf Achsen und Graph: Breite x, Höhe f(x).
39      Dreieck: Fläche = halbes Produkt aus Grundseite und Höhe; Grundseite auf einer Achse, Höhe als Funktionswert. Ecken im Ursprung, bei (a | 0) und (a | f(a)): Grundseite a, Höhe f(a).
40      Trapez: Fläche = Mittelparallele mal Höhe (halbe Summe der parallelen Seiten mal Höhe); die Schenkellänge liefert der Satz des Pythagoras.
41      Symmetrie: Liegt die Figur symmetrisch zur Hochachse, ist die Breite doppelt so groß wie die Stelle – beide Hälften zählen.
42      Auswendig (Teil A): „Ecken aus dem Graphen“ und „Dreieck“ – kein eigener Anlagenpunkt; begründetes Ermessen: die Flächenformeln sind Sek-I-Stoff (flaechen.md), der ohne Hilfsmittel sitzt, und die Teil-A-Zeile 2020MerhoehtAAnalysis11-a prüft genau den Dreiecksterm; „Trapez“ und „Symmetrie“ sind Anwendungen (Teil B).
43      Formelsammlung: Grundlagen – Flächenformeln [FS-IQB 1.1]; der Schritt vom Graphen zur Figur steht nicht in der Formelsammlung – [FS] offen
44  Quelle: eigene Formulierung nach [FOS] „Umfang und Flächeninhalt ebener Figuren in Zusammenhang mit Funktionsgraphen“ und [GOST Q1 L4] „Extremalprobleme“; Figuren aus der Rohdatei (Rechteck, Dreieck, Trapez); keine Zahlenbeispiele (allgemeine Buchstaben, Ermessen); [LS-AA QP I 8].
45
46  Einheit 2 (Zielfunktion aus Haupt- und Nebenbedingung):
47      Hauptbedingung: die Größe, die möglichst groß oder klein werden soll, als Formel – sie enthält noch zwei Variablen (A = a · b, u = 2x + 2y).
48      Nebenbedingung: der feste Zusammenhang zwischen den Variablen – ein Punkt liegt auf dem Graphen (y = f(x)), eine Länge ist fest vorgegeben.
49      Einsetzen: die Nebenbedingung nach einer Variablen umstellen und in die Hauptbedingung einsetzen → Zielfunktion in einer Variablen, ausmultipliziert und mit Definitionsbereich.
50        Rechteck an einer Wand, Materiallänge ℓ für drei Seiten: Nebenbedingung b + 2a = ℓ, Hauptbedingung A = a · b → A(a) = a · (ℓ − 2a) für 0 < a < ℓ/2.
51      Definitionsbereich: nur Werte, für die die Figur existiert – alle Seiten positiv.
52      Auswendig (Teil A): „Hauptbedingung“, „Nebenbedingung“ und „Einsetzen“ als Ansatz – kein eigener Anlagenpunkt (die Anlage nennt Extremalprobleme nicht); begründetes Ermessen: der Ansatz ist das Kernverfahren des Themas nach [GOST Q1 L4] „Extremalprobleme“ und [FOS] „Ermitteln der Zielfunktion“, und die Teil-A-Zeilen 2021-be-gk-A1.3b und 2020MerhoehtAAnalysis11-a setzen ihn ohne Rechner voraus.
53      Formelsammlung: keine Formel zum Ansatz in [FS-IQB]; die Flächenformeln stehen in 1.1 – [FS] offen
54  Quelle: eigene Formulierung nach [FOS] „Ermitteln der Zielfunktion“ (wörtlich nur dort) und [GOST Q1 L4] „Extremalprobleme, auch im Kontext außermathematischer Problemstellungen“; Beispiel eigen (Ermessen; die Wand-Aufgabe ist der Standardfall der Rohdatei, keine Zahl übernommen – Materiallänge als Buchstabe); [LS-AA QP I 8 „Extremwertprobleme mit Nebenbedingungen“].
55
56  Einheit 3 (Maximum bestimmen und Antwort):
57      Rechnen: Zielfunktion ableiten, A'(x) = 0 lösen, Lösungen außerhalb des Definitionsbereichs verwerfen; Art mit A''(x) oder dem Vorzeichenwechsel von A'; auf abgeschlossenen Bereichen die Randwerte vergleichen.
58        A(a) = a · (ℓ − 2a) = ℓa − 2a²: A'(a) = ℓ − 4a = 0 ⇔ a = ℓ/4; A''(a) = −4 < 0 → Maximum; b = ℓ − 2 · ℓ/4 = ℓ/2.
59      Antwort vollständig: angeben, was gefragt ist – Stelle, Seitenlängen und Extremwert mit Einheit; die Extremstelle allein ist kein Flächeninhalt.
60      Existenz ohne Rechnung: An den Rändern des Bereichs entartet die Figur (Breite oder Höhe gegen null) – dazwischen liegt ein größtes Exemplar; ein kleinstes gibt es nicht, wenn die Randfälle ausgeschlossen sind.
61      Abstand zweier Graphen: der vertikale Abstand ist die Differenz der Funktionswerte – Zielfunktion d(x) = f(x) − g(x) (oberer minus unterer Graph), dann wie oben.
62      Auswendig (Teil A): „Rechnen“ als Ansatz – über [GOST-OHiMi 2.2] „Extrempunkte und Wendepunkte (notwendiges und hinreichendes Kriterium)“ (das Werkzeug aus kurvenuntersuchung.md); „Antwort vollständig“ ist Arbeitsregel, „Existenz ohne Rechnung“ und „Abstand zweier Graphen“ sind Teil-B-Stoff.
63      Formelsammlung: Analysis – Ableitung, Ableitungsregeln [FS-IQB 1.2]; die Kriterien stehen nicht in der Formelsammlung (siehe kurvenuntersuchung.md) – [FS] offen
64  Quelle: eigene Formulierung nach [GOST Q1 L4] „Extremalprobleme“, „Randextrema“ und [FOS] „Untersuchung auf lokale Extrema“; Existenzargument aus der Rohdatei (abi 2017-bb-ea-B2.2c), Differenzansatz aus den vier Abstandszeilen; Zahlenbeispiel schließt an Kasten 2 an (Ermessen); [LS-AA QP I 8].
65
66  ### Typische Fehler
67  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 23 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: die Muster sind allein aus den Katalogzeilen belegt.
68  - Faktoren der Figur verloren: den Faktor ein halb der Dreiecksfläche vergessen, nur eine von zwei symmetrischen Seiten verdoppelt (Faktor vier verfehlt), beide Seiten unverdoppelt gelassen, den Umfang als einfache statt doppelte Summe angesetzt, das Material auf vier statt drei Seiten verteilt, die Höhe als Stelle statt als Funktionswert genommen, die Schenkellänge mit der Differenz der parallelen Seiten verwechselt, den Flächenterm als Rechteck statt als Trapez gedeutet, eine Ecke falsch gelesen – das häufigste Muster des Themas. [fhr 2023-A-1e, 2020-C-2d, 2020-C-2c, 2020-A-1f, 2025-A-2d; iqb 2020MerhoehtAAnalysis11-a, 2019MgrundlegendBAnalysisWTR2-1g, 2019MgrundlegendBAnalysisWTR2-1h, 2019MgrundlegendBAnalysisWTR2-1f]
69  - Zielfunktion falsch besetzt: A(u) = f(u) statt u · f(u) maximiert, die Nebenbedingung nach der falschen Variablen umgestellt, f'(x₀) statt A'(x₀) betrachtet, das Dreieck mit der falschen Ecke angesetzt. [abi 2022-bebb-gk-B2.1h, 2021-be-gk-A1.3b; fhr 2025-A-2e; iqb 2024MerhoehtBAnalysisWTR3-2f]
70  - Lösungsauswahl und Rand: die Lösung außerhalb des Intervalls verwendet oder mit angegeben, die negative Lösung zurücksubstituiert, den Rand als Lösung genommen, die hinreichende Bedingung vergessen, die Randfälle als mögliche Figuren zugelassen, das Minimum der Differenz als Maximalstelle genommen. [fhr 2023-A-1f; abi 2021-be-gk-B2.2i, 2017-bb-ea-B2.2c, 2024-bebb-gk-B2.2g, 2018-be-gk-B1.1g; iqb 2019MgrundlegendBAnalysisWTR2-1i]
71  - Antwort unvollständig oder falsch bezogen: die Extremstelle statt des Flächeninhalts angegeben, nur eine Seite ohne die zweite und den Inhalt, den Abstand senkrecht zur Kurve statt vertikal gedeutet, die Differenz mit negativem Vorzeichen geführt. [fhr 2020-C-2e, 2025-A-2f; abi 2018-be-gk-B1.1g, 2020-be-gk-B2.1g]
72  - Ableitungsfehler in der Zielfunktion: die Kettenregel beim e-Term mit Parameter vergessen (Vorzeichen). [iqb 2020MerhoehtAAnalysis11-b]
73
74  ### Für schwache Schüler
75  Mindeststoff (GK-Kern Q1 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q1: „Extremalprobleme, auch im Kontext außermathematischer Problemstellungen“ und „Randextrema“ – alle drei Einheiten mit ganzrationalen Funktionen und Potenz- bzw. natürlichen Exponentialfunktionen; das Kriterienwerkzeug ist Mindeststoff von kurvenuntersuchung.md. Ohne Hilfsmittel (Anlage OHiMi 2.2, Prüfungsteil A): kein eigener Punkt – tragfähig sind die Kriterien („Extrempunkte und Wendepunkte“) und die Sek-I-Flächenformeln; die Teil-A-Zeilen der Rohdatei (2021-be-gk-A1.3b, 2020MerhoehtAAnalysis11-a/b) verlangen genau diese Kombination. LK-Zusatz: keiner (nur die Funktionsklassen; die Scharzeilen der Rohdatei liegen auf erhöhtem Niveau). Niveaustufe H der E-Phase [RLP H]: kein eigener Posten – die Sek-I-Pläne kennen die Extremwertaufgabe nicht; Flächenformeln und Pythagoras (RLP E–G) sind Blatt-0-Stoff (Voraussetzung vier). RLP FOS (fhr) [FOS Pflichtthema 2 „Extremwertaufgaben“]: „Ermitteln der Zielfunktion und Untersuchung auf lokale Extrema“, „Umfang und Flächeninhalt ebener Figuren“ – alle drei Einheiten mit ganzrationalen Funktionen; „Oberflächeninhalt und Volumen von Körpern“ steht im Plan, hat aber kein Original (Vorrat mit Planstütze). Vorrat: e-Funktions- und Scharzeilen (GK/LK), die Rückwärtsaufgabe (Aufgabenstellung formulieren) und die Existenzbegründung ohne Rechnung – nach dem Niveau der Rohdatei gesetzt (Ermessen, der Plan zieht keine Grenze). COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung Extremwertaufgaben mit Nebenbedingungen unter Differentialrechnung – deckt sich mit dem Kern, kein zusätzlicher Posten.
76  Grundvorstellung (Blatt 0) [GOST Q1 L4, MO]: Unter allen Figuren derselben Bauart gibt es verschieden große – und meist genau eine größte; die Größe hängt von einer Stellgröße ab, das ist eine Funktion. „Hier ist ein Bogen über einer Grundlinie, kein Term. Zeichne drei verschiedene Rechtecke, die mit der Grundlinie und zwei Ecken am Bogen eingeschlossen sind: ein schmales hohes, ein breites flaches, eines dazwischen. Welches wirkt am größten? Was passiert mit der Fläche, wenn die Ecke ganz an den Rand wandert – und ganz in die Mitte? Wovon hängt die Fläche ab, wenn du die Ecke verschiebst? Schreibe unter jedes Rechteck nur: schmal, breit oder dazwischen – und ordne nach der Fläche.“ Wer glaubt, alle einbeschriebenen Rechtecke seien gleich groß, wer das größte am Rand sucht oder wer nicht sieht, dass die Fläche mit der Lage der Ecke wandert, braucht das vor jeder Rechnung: Die Fläche ist eine Funktion der Stellgröße – und die Ableitung findet ihr Maximum. Verständnis, nicht Verfahren; Ermessen in Vorstellung und Aufgabenform – keine amtliche Eingangsvoraussetzung nennt eine Vorstellung zum Optimieren, die Stütze ist der Q1-Inhalt selbst (wie beim Geometrie-Formbefund von ebenen.md). [GOST Q1 L4 „Extremalprobleme“; MO-Logik: Vorstellung vor Verfahren; abi 2017-bb-ea-B2.2c (Existenz von größtem und kleinstem Exemplar); BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
77  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
78  - Figur und Term (Einheit 1): „Wo sitzen die Ecken?“ – zu Figuren am Graphen ankreuzen, welche Ecken auf dem Graphen, auf den Achsen oder fest liegen und welche Seite welche Koordinate oder welcher Funktionswert ist; nichts rechnen (Vorstufe, Grundvorstellung) → zu einer markierten Ecke auf dem Graphen die Seiten der Figur als Stelle und Funktionswert benennen (Grundfall, viermal) → Rechteck oder Dreieck für einen konkreten Wert einzeichnen (fhr 2020-C-2c, 2023-A-1e; iqb 2019MgrundlegendBAnalysisWTR2-1f) → den Flächenterm eines Dreiecks unter dem Graphen begründen (iqb 2020MerhoehtAAnalysis11-a, Teil A) → den Trapezterm über die Mittelparallele herleiten und die Schenkellänge mit dem Satz des Pythagoras angeben (iqb 2019MgrundlegendBAnalysisWTR2-1h, 2019MgrundlegendBAnalysisWTR2-1g) → Prüfungshöhe: das Dreieck zu den Schnittpunkten mit einer Parallelen einzeichnen und die Existenz von größtem und kleinstem Exemplar ohne Rechnung beurteilen (abi 2017-bb-ea-B2.2c, Niveau III); fhr-Zielmarke: Dreieck einzeichnen, Fläche berechnen und Zielfunktion nachweisen (fhr 2023-A-1e, Niveau II).
79  - Zielfunktion aufstellen (Einheit 2): „Was wird extremal, was ist fest?“ – Hauptbedingung und Nebenbedingung im Text markieren und ankreuzen, wonach umgestellt wird; nichts rechnen (Vorstufe) → Haupt- und Nebenbedingung notieren und die Nebenbedingung nach einer Variablen umstellen (Grundfall, viermal) → eine feste Nebenbedingung, wechselnde Zielfunktion ohne Figur: eine Zahl in zwei Summanden zerlegen, einmal das Produkt, einmal die Summe der Quadrate als Zielfunktion aufstellen und ausmultiplizieren → den Flächeninhalt für konkrete Werte aus der Nebenbedingung berechnen (fhr 2025-A-2d) → die Zielfunktion durch Einsetzen aufstellen und ausmultiplizieren (fhr 2025-A-2e) → eine vorgegebene Zielfunktion nachweisen: Fläche mit Symmetriefaktoren (fhr 2020-C-2d), Umfang (fhr 2020-A-1f) → den Ansatz an einer Figur zwischen Ursprung und Graphenpunkt aufstellen (abi 2022-bebb-gk-B2.1h als Ansatz) → Prüfungshöhe: den Flächenterm an einer Schar mit e-Funktion begründen (iqb 2020MerhoehtAAnalysis11-a, Teil A, Niveau I bis II); fhr-Zielmarke: Umfangs-Zielfunktion nachweisen (fhr 2020-A-1f, Niveau III).
80  - Maximum bestimmen (Einheit 3): „Stelle, Seiten oder Inhalt?“ – ankreuzen, was verlangt ist (die Stelle, die Maße, der Extremwert) und ob Art und Randwerte zu prüfen sind; nichts rechnen (Vorstufe) → die Zielfunktion ableiten, null setzen und die Lösung im Definitionsbereich wählen (Grundfall, viermal) → die Art über die zweite Ableitung bestätigen und alle gefragten Größen mit Einheit angeben (fhr 2025-A-2f, 2020-C-2e) → mit Substitution lösen und Lösungen außerhalb des Intervalls verwerfen (fhr 2023-A-1f) → Randmaximum: die Zielfunktion hat im Innern nur ein Minimum; das gesuchte Maximum über die Randwerte des Definitionsbereichs bestimmen (Vorrat: kein Abitur-GK-Beleg im Katalog) → das achsenparallele Rechteck maximaler Fläche über die Zielfunktion aus Stelle mal Funktionswert (abi 2022-bebb-gk-B2.1h) → den maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen (abi 2018-be-gk-B1.1g, 2020-be-gk-B2.1g, 2021-be-gk-B2.2i, 2024-bebb-gk-B2.2g) → den Parameter für den größten Flächeninhalt bestimmen (iqb 2020MerhoehtAAnalysis11-b, 2019MgrundlegendBAnalysisWTR2-1i) → eine Stelle als Maximalstelle über die notwendige Bedingung ausschließen (abi 2021-be-gk-A1.3b, Teil A) → Prüfungshöhe: zu vorgelegten Lösungsschritten die Extremwertaufgabe formulieren und die Schritte erläutern (iqb 2024MerhoehtBAnalysisWTR3-2f, Niveau III); fhr-Zielmarke: Maximum mit Substitution und Intervallprüfung (fhr 2023-A-1f, Niveau III).
81
82  ### Prüfungsform (fhr / abi / iqb)
83  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen (be-gk, be-lk, bb-gk, bb-ea) mit „ja“ führen. Für fhr ist der Pool keine Vorgabe: dort gelten RLP FOS 2019 und der fhr-Katalog. Die Rohdatei zählt 27 Zeilen mit 16 Haupttypen (fhr 9 Zeilen, 5 Typen; abi 9 Zeilen, 5 Typen; iqb 9 Zeilen, 7 Typen), Jahre 2017–2025. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
84  fhr (9 Zeilen; fhr-Thema „Extremwertaufgaben“) [FOS, fhr-Katalog]: Maximum der Zielfunktion bestimmen (3, E3) · Zielfunktion aus Haupt- und Nebenbedingung aufstellen (3, E2) · je 1: Dreieck in das Koordinatensystem einzeichnen (E1) · Flächeninhalt bei gegebener Nebenbedingung berechnen (E2) · Rechteck in das Koordinatensystem einzeichnen (E1). Muster: die Extremwertaufgabe kommt als dreiteilige Teilaufgabenkette am Ende einer Analysis-Aufgabe – Figur einzeichnen oder konkret rechnen, Zielfunktion nachweisen, Maximum bestimmen: Rechteck mit Umfang (2020-A-1f), Platine im Lautsprecher (2020-C-2c/2d/2e), Dreieck unter dem Graphen (2023-A-1e/1f), Trainingsfläche an der Wand (2025-A-2d/2e/2f); drei bis acht Punkte je Zeile, ganzrationale Funktionen. Niveau II 7, III 2 (2020-A-1f, 2023-A-1f – Umfangsnachweis und Substitution).
85  abi (9 Zeilen, 5 Typen; Landeshefte bb-ea, be-gk, bebb-gk 2017–2024, davon 2 aus den CAS-Fassungen bb-ea 2018 und be-gk 2018) [abi-Katalog]: Größten oder kleinsten vertikalen Abstand zweier Graphen über die Differenzfunktion bestimmen (5, E3) · je 1: Achsenparalleles Rechteck maximaler Fläche zwischen Ursprung und Graphenpunkt bestimmen (E3) · Ausschluss einer Stelle als Maximalstelle einer Rechtecksfläche über die notwendige Bedingung nachweisen (E3) · Dreieck zu Schnittpunkten mit einer Parallelen zur x-Achse einzeichnen (E1) · Kleinsten Abstand eines Punktes zu einem Graphen über die Abstandsfunktion bestimmen (E3). Muster: Teil B trägt acht der neun Zeilen; der Standardfall ist der maximale vertikale Abstand zweier Graphen mit der Differenz als Zielfunktion (Skisprung 2018-be-gk-B1.1g, Graphenpaar f und f' 2020-be-gk-B2.1g, Flügel 2021-be-gk-B2.2i, Näherungsvergleich 2024-bebb-gk-B2.2g, vier bis sieben Punkte, Niveau II; in der Berliner CAS-Fassung 2018 ohne WTR-Gegenstück der Abstand zwischen einem Höhenprofil und der Geraden, die es auf einem Teilintervall ersetzt, 2018-be-gk-cas-B1.2g, fünf Punkte, Niveau II), dazu das Rechteck am Graphen (2022-bebb-gk-B2.1h) und das Dreieck der e-Funktions-Schar mit Existenzbegründung (2017-bb-ea-B2.2c, Niveau III, neun Punkte); Teil A eine Zeile (Ausschluss über A'(1) ≠ 0, 2021-be-gk-A1.3b); nur in der CAS-Fassung 2018 der kleinste Abstand des Ursprungs zum Teichrand über das Abstandsquadrat (2018-bb-ea-cas-B2.2i, fünf Punkte, Niveau III, ohne WTR-Gegenstück) – die erste Zeile, deren Zielfunktion ein Abstand zu einem festen Punkt ist. Keine der Zeilen ist eine Pool-Dublette – die Landeshefte stellen eigene Extremwertaufgaben. Niveau II 7, III 2.
86  iqb (9 Zeilen, 7 Typen; Pool 2017–2024, grundlegend 5 und erhöht 4 Zeilen, Teil A 2 und Teil B 7 Zeilen, davon 2 CAS) [iqb-Katalog]: Parameter für den größten Flächeninhalt über die Ableitung bestimmen (3, E3) · je 1: Aufgabenstellung zu einer Extremwertaufgabe mit Dreiecksfläche aus dem Lösungsweg formulieren und Schritte erläutern (E3) · Einbeschriebenes Trapez zu einem Parameterwert in die Abbildung einzeichnen (E1) · Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen (E1) · Flächenterm eines einbeschriebenen Trapezes über die Mittelparallele geometrisch herleiten (E1) · Größten oder kleinsten vertikalen Abstand zweier Graphen über die Differenzfunktion bestimmen (E3) · Term für die Schenkellänge eines einbeschriebenen Trapezes aufstellen (E1). Muster: der Pool stellt die Extremwertaufgabe selten und dann kleinschrittig zerlegt – die Trapezkette an der Parabelschar (2019MgrundlegendBAnalysisWTR2-1f/1g/1h/1i: einzeichnen, Schenkel, Flächenterm, Maximum; zwei bis fünf Punkte) und die Dreieckskette an der e-Funktion in Teil A (2020MerhoehtAAnalysis11-a/b), dieselbe Dreiecksfläche unter x² · e^(−0,2x) schon in der CAS-Fassung 2017 in Teil B (2017MerhoehtBAnalysisCAS1-1d, fünf Punkte) – oder rückwärts als Deutung eines vorgelegten Lösungswegs (2024MerhoehtBAnalysisWTR3-2f, Niveau III); dazu im CAS-Stapel 2017 grundlegend die erste Poolzeile zum vertikalen Abstand – die größte Abweichung zweier Temperaturmodelle in der Abkühlphase über die Differenzfunktion, mit dem Rechner und Randvergleich (2017MgrundlegendBAnalysisCAS-1f, fünf Punkte, Niveau II, Anforderungsbereich bis III). Keine Zeile kehrt wortgleich in Landesheften wieder. Niveau I 3, II 5, III 1.
87  Zielmarke: Einheit 1 – fhr: Dreieck einzeichnen mit Flächen- und Zielfunktionsnachweis (2023-A-1e, Niveau II); abi: Dreieck der Schar mit Existenzbegründung (2017-bb-ea-B2.2c, Niveau III); iqb: Trapezterm über die Mittelparallele (2019MgrundlegendBAnalysisWTR2-1h, Niveau II). Einheit 2 – fhr: Umfangs-Zielfunktion nachweisen (2020-A-1f, Niveau III) und Flächen-Zielfunktion aufstellen (2025-A-2e); abi/iqb: Ansatz an Rechteck bzw. Dreieck am Graphen (2022-bebb-gk-B2.1h, 2020MerhoehtAAnalysis11-a). Einheit 3 – fhr: Maximum mit Substitution und Intervall (2023-A-1f, Niveau III); abi: maximaler vertikaler Abstand (2018-be-gk-B1.1g, 2021-be-gk-B2.2i, Niveau II), kleinster Abstand zu einem Punkt nur CAS (2018-bb-ea-cas-B2.2i, Niveau III); iqb: Parameter für den größten Flächeninhalt (2019MgrundlegendBAnalysisWTR2-1i, 2017MerhoehtBAnalysisCAS1-1d) und die Rückwärtsaufgabe (2024MerhoehtBAnalysisWTR3-2f, Niveau III).
````

## 2 Originale (22)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2020-A-1f (fhr-katalog.csv)

jahr 2020 · papier A · punkte 8 · format Rechnung · antwort Term|Zahl
- gegeben: f(x) = −x^3 − x^2 + 4x + 4; x aus IR; ein Rechteck ABCD liegt so im Koordinatensystem, dass A im Koordinatenursprung, B auf der x-Achse und D auf der y-Achse liegt und C auf Gf im ersten Quadranten; x ist die x-Koordinate der Punkte B und C
- gesucht: Nachweis, dass sich der Umfang mit u(x) = −2x^3 − 2x^2 + 10x + 8 berechnen lässt|x-Koordinate von B und C für den maximalen Umfang
- verfahren: Hauptbedingung u = 2x + 2y aufstellen, die Nebenbedingung y = f(x) einsetzen und zusammenfassen; danach u' gleich null setzen, die Lösungen prüfen und die verbleibende Stelle über das Vorzeichen von u'' als Maximum bestätigen
- fehlerquelle: den Umfang als x + y statt als 2x + 2y ansetzen

### 2020-C-2c (fhr-katalog.csv)

jahr 2020 · papier C · punkte 4 · format Zeichnen|Rechnung · antwort Grafik|Zahl
- gegeben: f(x) = −(2/81)x^2 + 5; im Inneren des Lautsprechers liegt eine rechteckige Platine mit den Eckpunkten P(−x; −f(x)), Q(x; −f(x)), R(x; f(x)) und S(−x; f(x)) an der Außenwand, wobei x eine reelle Zahl zwischen 0 und 9 ist; für das aktuelle Modell gilt x = 6 mit P(−6; −37/9); eine Einheit entspricht einem Zentimeter
- gesucht: Zeichnung der Platine PQRS in der Abbildung|Flächeninhalt der Platine
- verfahren: die vier Eckpunkte eintragen und verbinden; die waagerechte Seite als 2x und die senkrechte als doppelten Funktionswert bestimmen und beide multiplizieren
- fehlerquelle: als Seitenlängen x und f(x) nehmen, statt beide zu verdoppeln

### 2023-A-1e (fhr-katalog.csv)

jahr 2023 · papier A · punkte 5 · format Zeichnen|Rechnung · antwort Grafik|Zahl|Term
- gegeben: f(x) = −(1/8)x^4 + 4x^2 + 8; x aus IR; die Punkte O(0; 0), P(2; 0) und Q(2; 22) bilden ein rechtwinkliges Dreieck; für ein beliebiges rechtwinkliges Dreieck OP'Q' ist Q'(x; f(x)) ein beliebiger Punkt auf Gf im Intervall 0 < x < 6 und P'(x; 0) liegt senkrecht unter Q' auf der x-Achse; die Zeichnung aus Teilaufgabe d liegt vor
- gesucht: Dreieck OPQ in der Zeichnung aus Teilaufgabe d|Maßzahl des Flächeninhalts des Dreiecks OPQ|Nachweis, dass A(x) = −(1/16)x^5 + 2x^3 + 4x den Flächeninhalt eines beliebigen Dreiecks OP'Q' angibt
- verfahren: das Dreieck mit den Eckpunkten O, P und Q eintragen; den Flächeninhalt aus Grundseite 2 und Höhe 22 berechnen; für den allgemeinen Fall die Hauptbedingung A = (1/2) g · h mit den Nebenbedingungen g = x und h = f(x) besetzen und ausmultiplizieren
- fehlerquelle: bei der Zielfunktion den Faktor 1/2 vergessen und den Term von f unverändert mit x multiplizieren

### 2025-A-2d (fhr-katalog.csv)

jahr 2025 · papier A · punkte 3 · format Rechnung · antwort Zahl
- gegeben: rechteckige Trainingsfläche, eine Seite liegt an der Außenwand der Sporthalle; für die übrigen drei Seiten stehen insgesamt 46 m Baumaterial zur Verfügung, das vollständig verwendet wird; a ist die zur Wand senkrechte Seite, b die zur Wand parallele; die Dicke des Materials wird vernachlässigt
- gesucht: Flächeninhalt der Trainingsfläche für a = 8 m|Flächeninhalt für a = 14 m
- verfahren: aus b = 46 − 2a die zweite Seite bestimmen und den Flächeninhalt als Produkt der beiden Seiten berechnen
- fehlerquelle: das Material auf alle vier Seiten verteilen und b halbieren

### 2023-A-1f (fhr-katalog.csv)

jahr 2023 · papier A · punkte 6 · format Rechnung · antwort Zahl
- gegeben: die Zielfunktion A(x) = −(1/16)x^5 + 2x^3 + 4x aus Teilaufgabe e beschreibt den Flächeninhalt des Dreiecks OP'Q' im Intervall 0 < x < 6
- gesucht: Extremstelle xE der Funktion A im Intervall 0 < x < 6|Nachweis, dass das durch xE festgelegte Dreieck OP'Q' den maximalen Flächeninhalt besitzt
- verfahren: A'(x) bilden, A'(x) = 0 mit der Substitution z = x^2 auf eine quadratische Gleichung bringen und lösen, zurücksubstituieren und die Lösung außerhalb des Intervalls verwerfen, dann mit A''(xE) < 0 das Maximum nachweisen
- fehlerquelle: die zweite Wurzel x ≈ −4,45 mit angeben, obwohl sie nicht im Intervall liegt, oder die negative Lösung z2 zurücksubstituieren

### 2018-be-gk-B1.1g (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 6 · format Begründung|Rechnung · antwort Text|Zahl
- gegeben: Flugbahn f mit f(x) = −0,008x² + 54 und Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m; der Sprung führt von S(0 | 54) bis zum Landepunkt L(73,9 | 10,3). Auf die hinreichende Bedingung darf verzichtet werden.
- gesucht: Nachweis, dass der maximale vertikale Abstand des Springers zum Hang höchstens 6 m beträgt
- verfahren: Die Differenzfunktion d(x) = f(x) − g(x) beschreibt den vertikalen Abstand. d'(x) = 0,004x − x³/500 000 = 0 liefert nach Ausklammern x = 0 und x² = 2000, also x = 20√5 ≈ 44,7 im Flugbereich. Einsetzen ergibt d(20√5) = 38 − 32 = 6.
- fehlerquelle: den Abstand als Abstand Punkt–Kurve senkrecht zum Hang deuten statt als vertikale Differenz, oder die Lösung x = 0 der Ableitung als Maximum nehmen

### 2020-be-gk-B2.1g (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: f(x) = (6x − 3) · e^(−x), x ∈ IR; f'(x) = (−6x + 9) · e^(−x); im Bereich x ≥ 1 gibt es eine Stelle x_M maximalen senkrechten Abstands der Graphen von f und f'; Nachweis des Maximums nicht verlangt
- gesucht: x_M und der Abstand der Graphen an dieser Stelle
- verfahren: Differenz d = f − f' bilden (f liegt für x > 1 oberhalb), d' = 0 lösen, d(x_M) berechnen
- fehlerquelle: Abstand als f'(x) − f(x) mit negativem Vorzeichen führen

### 2021-be-gk-B2.2i (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 7 · format Rechnung · antwort Zahl|Text
- gegeben: f(x) = (−1/10 x² + 2x) · e^(−0,1x) und h(x) = −3/4 x · e^(−0,1x), beide in IR; Graphen G und H; d(x) = f(x) − h(x) beschreibt die vertikale Höhe des Flügels auf [0; 27,5]; die maximale Höhe darf 7,15 dm nicht überschreiten
- gesucht: ob die Konstrukteure die Vorgabe beachtet haben
- verfahren: d' = 0 lösen, die Stelle im Intervall wählen, d dort berechnen und mit 7,15 vergleichen
- fehlerquelle: die Lösung außerhalb des Intervalls verwenden

### 2024-bebb-gk-B2.2g (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: f(x) = 0,5x⁴ − 4x² + 3,5, x ∈ IR, Graph G_f; Näherung von f für −1 ≤ x ≤ 1 durch p(x) = −3,5x² + 3,5; genau zwei Stellen in [−1; 1] mit maximaler Differenz von p und f
- gesucht: Nachweis, dass die maximale Differenz 1/8 beträgt
- verfahren: d = p − f aufstellen, d' = 0, Wert an ±1/√2
- fehlerquelle: x = 0 (Minimum von d) als Maximalstelle nehmen

### 2018-be-gk-cas-B1.2g (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6, 1 LE = 1 km. Im Intervall [2; 6] wird es durch die Gerade s durch (2 | f(2)) und (6 | f(6)) ersetzt, mit Rundungen s(x) = −0,19x + 1,48. Die Gerade s liegt stets oberhalb des Graphen von f.
- gesucht: maximaler vertikaler Abstand zwischen den Graphen im Intervall [2; 6]
- verfahren: Differenzfunktion d(x) = s(x) − f(x) bilden, d′(x) = 0 mit dem CAS lösen und d dort berechnen; an den Rändern ist d(2) = d(6) = 0 (Sekante).
- fehlerquelle: den Abstand nur an den Rändern oder an einer geschätzten Stelle berechnen oder die Einheit km nicht deuten

### 2022-bebb-gk-B2.1h (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x); Ursprung und P(u | v) auf dem Graphen mit u > 0 sind gegenüberliegende Ecken eines achsenparallelen Rechtecks; genau ein u liefert maximale Fläche; Kontrolle A'(u) = (2 − u²) · e^(−u)
- gesucht: Koordinaten von P für die maximale Fläche
- verfahren: A(u) = u · f(u) ableiten, A'(u) = 0 für u > 0, P berechnen
- fehlerquelle: A(u) = f(u) statt u · f(u) maximieren

### 2017-bb-ea-B2.2c (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 9 · format Zeichnen|Begründung|Rechnung · antwort Grafik|Text|Term
- gegeben: Funktionenschar f_a mit f_a(x) = e^(2ax) + e^(−2ax); für a = 0,15 ist f_0,15(x) = e^(0,3x) + e^(−0,3x) mit dem Graphen G_0,15. Dieser wird von den Parallelen zur x-Achse mit der Gleichung y = k; 2 < k < 6 in den Punkten A_k und B_k geschnitten. A_k, B_k und der Punkt C(0 | 6) bilden ein Dreieck. Ein Koordinatensystem mit dem Graphen G_0,15 ist auf der Folgeseite abgedruckt.
- gesucht: Zeichnung eines der möglichen Dreiecke A_k B_k C; Begründung ohne Rechnung, dass keines der Dreiecke einen minimalen Flächeninhalt haben kann, wohl aber eines einen maximalen; Gleichung für den Flächeninhalt in Abhängigkeit vom x-Wert des im I. Quadranten liegenden Eckpunktes
- verfahren: Wegen der Achsensymmetrie liegen A_k und B_k spiegelbildlich zur y-Achse: ist u der x-Wert des Eckpunktes im I. Quadranten, so ist die Grundseite 2u lang und die Höhe 6 − k = 6 − f_0,15(u). Für k gegen 2 schrumpft die Grundseite, für k gegen 6 die Höhe gegen null; da beide Randwerte wegen 2 < k < 6 nicht angenommen werden, gibt es kein kleinstes Dreieck, wegen der Stetigkeit im Inneren aber ein größtes.
- fehlerquelle: die Randfälle k = 2 und k = 6 als mögliche Dreiecke zulassen und daraus auf ein Minimum schließen

### 2021-be-gk-A1.3b (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 3 · format Rechnung · antwort Text
- gegeben: f(x) = x³ − 3x² + 4; P(x | f(x)) mit 0 < x < 2 legt ein achsenparalleles Rechteck fest, dessen Flächeninhalt für genau ein x_max maximal ist
- gesucht: Nachweis, dass x_max ≠ 1
- verfahren: A(x) = x · f(x) ableiten und A'(1) ≠ 0 zeigen
- fehlerquelle: f'(1) statt A'(1) betrachten

### 2018-bb-ea-cas-B2.2i (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea-cas · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Funktionenschar f_a mit f_a(x) = (1/a)·x³ + 3x² + 5x + 2a; x ∈ IR, a ∈ IR, a ≠ 0, und die Funktion h mit h(x) = −(1/2)·x^(−3); x ∈ IR, x ≠ 0. Die zugehörigen Graphen sind G_a und K. Ein Gartenbesitzer hat in einer Ecke seines Gartens einen Teich angelegt. Der Rand des Teiches an der Wasseroberfläche wird durch die Graphen G_2 und K modelliert. Im Intervall von −3 bis −2 verläuft eine Brücke über den Teich; 1 LE = 1 m. Eine Darstellung zeigt Teichoberfläche und Brücke senkrecht von oben betrachtet. Für einen Grillplatz hat der Gartenbesitzer eine Fläche betoniert; der Koordinatenursprung ist im Modell der Punkt der betonierten Fläche, der den geringsten Abstand zum Teichrand hat.
- gesucht: geringster Abstand des Koordinatenursprungs zum Teichrand
- verfahren: Der Ursprung liegt rechts unterhalb des Teichs, am nächsten liegt der untere Rand K. Das Abstandsquadrat d(x)² = x² + (h(x))² = x² + 0,25 · x^(−6) aufstellen und die Ableitung 2x − 1,5 · x^(−7) null setzen: x^8 = 0,75, also x ≈ −0,965, im Randstück zwischen den Schnittpunkten. Zum Vergleich ist der kleinste Abstand zum Randstück von G_2 etwa 1,80.
- fehlerquelle: den Abstand nur zu einem Randstück minimieren, ohne das andere zu prüfen, oder das Minimum von d² nicht in den Abstand umrechnen

### 2019MgrundlegendBAnalysisWTR2-1f (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Schar f_k(x) = −kx · (x − 8), k > 0, in IR definiert; Graph G_k; k = 1/4; Trapeze mit den Ecken A(0 | 0), B(8 | 0), C_u(8 − u | f_(1/4)(u)) und D_u(u | f_(1/4)(u)) für 0 < u < 4
- gesucht: Trapez für u = 1 in der Abbildung
- verfahren: D₁ und C₁ berechnen und mit A, B verbinden
- fehlerquelle: C₁ bei x = 8 − u falsch lesen

### 2020MerhoehtAAnalysis11-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: f(x) = x · e^(−x) in IR; Dreiecke mit O(0; 0), P(a; 0), Q(a; f(a)), a > 0
- gesucht: Begründung, dass der Flächeninhalt 1/2 a² e^(−a) beträgt
- verfahren: Grundseite und Höhe einsetzen
- fehlerquelle: Höhe als a statt f(a) nehmen

### 2017MerhoehtBAnalysisCAS1-1d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 5 · format Rechnung · antwort Zahl
- gegeben: f_0,2(x) = x^2 · e^(−0,2x) mit Graph G_0,2; für b ∈ IR+ die Punkte A(0; 0), B(b; 0) und C mit der x-Koordinate b auf G_0,2
- gesucht: der Wert von b, für den der Flächeninhalt des Dreiecks ABC maximal ist, und der zugehörige Flächeninhalt
- verfahren: Rechter Winkel bei B: A(b) = 1/2 · b · f_0,2(b) = 1/2 · b^3 · e^(−0,2b); A'(b) = 0 für b > 0 liefert b = 15 (Vorzeichenwechsel von + nach −); A(15) berechnen
- fehlerquelle: die Höhe b statt f_0,2(b) nehmen oder den Faktor 1/2 vergessen

### 2024MerhoehtBAnalysisWTR3-2f (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 6 · format Kurzantwort|Begründung · antwort Text
- gegeben: Schritte (1) p_k(u) = 1/2 · (u + 10) · f_k(u), (2) p_k'(u) = 0 ⇔ u = 10, (3) p_k''(10) < 0, (4) p_k(10) ≈ 73,6 · k; Punkte (−10 | 0) und (u | 0), u > −10
- gesucht: passende Aufgabenstellung und Erläuterung der Schritte
- verfahren: Dreieck mit den Ecken (−10 | 0), (u | 0), (u | f_k(u)) erkennen
- fehlerquelle: Dreieck mit Ecke im Ursprung statt in (−10 | 0)

### 2017MgrundlegendBAnalysisCAS-1f (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 5 · format Rechnung · antwort Zahl
- gegeben: In einem Produktionsprozess werden Flüssigkeiten erhitzt, eine Zeit lang bei konstanter Temperatur gehalten und anschließend wieder abgekühlt; bei einem durchgehend gesteuerten Vorgang beschreibt f(t) = 23 + 20 · t · e^(−t/10) (t in Minuten seit Beginn, f(t) in °C) den Temperaturverlauf während des Erhitzens und des Abkühlens modellhaft; betrachtet wird nun ein Vorgang, bei dem die Steuerung zwanzig Minuten nach Beginn abgeschaltet wird; das anschließende Abkühlen beschreibt für t >= 20 die Funktion h mit h(t) = 23 + b · e^(c · t) und b, c ∈ IR; b = 197,4 und c = −0,065
- gesucht: für die Phase des Abkühlens der Zeitpunkt, zu dem die Werte von f und h am stärksten voneinander abweichen, und die zugehörige Abweichung
- verfahren: Differenzfunktion d(t) = f(t) − h(t) aufstellen; den größten Betrag von d für t >= 20 über d'(t) = 0 mit dem Rechner bestimmen und mit dem Randverhalten vergleichen (d(20) ≈ 0,3, für große t gegen 0)
- fehlerquelle: den Hochpunkt von f oder eine Schnittstelle von f und h statt des Maximums der Differenz suchen

### 2019MgrundlegendBAnalysisWTR2-1h (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 4 · format Begründung · antwort Text
- gegeben: Schar f_k(x) = −kx · (x − 8), k > 0, in IR definiert; Graph G_k; k = 1/4; Trapeze mit den Ecken A(0 | 0), B(8 | 0), C_u(8 − u | f_(1/4)(u)) und D_u(u | f_(1/4)(u)) für 0 < u < 4; Flächenterm (8 − u) · f_(1/4)(u)
- gesucht: geometrische Überlegung, mit der sich der Term herleiten lässt
- verfahren: Mittelparallele als Mittelwert von 8 und 8 − 2u, Höhe als Funktionswert
- fehlerquelle: den Term als Rechteck 8 − u mal Höhe deuten

### 2025-A-2e (fhr-katalog.csv)

jahr 2025 · papier A · punkte 3 · format Rechnung · antwort Term
- gegeben: rechteckige Trainingsfläche, eine Seite liegt an der Außenwand der Sporthalle; für die übrigen drei Seiten stehen insgesamt 46 m Baumaterial zur Verfügung, das vollständig verwendet wird; a ist die zur Wand senkrechte Seite, b die zur Wand parallele; die Dicke des Materials wird vernachlässigt
- gesucht: Gleichung einer Funktion, die den Flächeninhalt in Abhängigkeit von der Seitenlänge a beschreibt
- verfahren: Hauptbedingung A = a · b und Nebenbedingung b + 2a = 46 notieren, die Nebenbedingung nach b umstellen und in die Hauptbedingung einsetzen
- fehlerquelle: die Nebenbedingung nach a umstellen und eine Funktion von b erhalten

### 2019MgrundlegendBAnalysisWTR2-1i (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Schar f_k(x) = −kx · (x − 8), k > 0, in IR definiert; Graph G_k; k = 1/4; Trapeze mit den Ecken A(0 | 0), B(8 | 0), C_u(8 − u | f_(1/4)(u)) und D_u(u | f_(1/4)(u)) für 0 < u < 4; Flächeninhalt (8 − u) · f_(1/4)(u); eines der Trapeze hat den größten Inhalt
- gesucht: zugehöriger Wert von u
- verfahren: T(u) aufstellen, T' = 0 lösen, Lösung im Intervall wählen
- fehlerquelle: u = 8 als Lösung nehmen; hinreichende Bedingung vergessen

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2020-C-2d, 2019MgrundlegendBAnalysisWTR2-1g, 2020-C-2e, 2025-A-2f, 2020MerhoehtAAnalysis11-b

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
