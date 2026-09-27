# Mappe: lineare-gleichungssysteme

Eintrag: hz-0801/mathe-nachhilfe, katalog/lineare-gleichungssysteme.md
Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25T11:16:56+02:00, „katalog: Marken-Zeilen je Lerneinheit, drei Einheiten ergänzt, marken-bau.py“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:32 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Lineare Gleichungssysteme
  3
  4  ### Verortung
  5  Lineare Gleichungen mit zwei Variablen, Lösungspaare, grafisches Lösen und systematisches Probieren, Lösbarkeit (ein Schnittpunkt, parallel, identisch): Stufe F (Gymnasium Kl. 8; Oberschule 9–10 regul … (gekürzt, 2057 Zeichen)
  6  [RLP] Gleichungen und Funktionen E (S. 58): „Prüfen einer Lösung (auch durch Einsetzen in die Ausgangsgleichung)“. F (S. 58): „Darstellen von außer- und innermathematischen Sachverhalten durch Terme, Gleichungen und lineare Gleichungssysteme mit zwei Variablen“, „Variablen verwenden (auch verschiedene Variablen in linearen Gleichungssystemen)“, „Angeben von passenden Situationen und grafischen Darstellungen zu vorgegeben Termen, Gleichungen und linearen Gleichungssystemen mit zwei Variablen“, „Lösen linearer Gleichungssysteme mit zwei Variablen (grafisch und durch systematisches Probieren, auch mithilfe von digitalen Mathematikwerkzeugen)“, „Untersuchen der Lösbarkeit und der Lösungsvielfalt von Gleichungen und linearen Gleichungssystemen mit zwei Variablen (z. B. grafisch) und Formulierung diesbezüglicher Aussagen und Begründungen“. G (S. 60): „Übersetzungen zwischen verschiedenen Darstellungen (symbolisch, grafisch, sprachlich, auch in Kontexten) von Termen, Gleichungen (auch für quadratische Zusammenhänge) und linearen Gleichungssystemen mit zwei Variablen (auch mithilfe von digitalen Mathematikwerkzeugen)“, „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“, „Vergleichen der Effektivität verschiedener Lösungsverfahren im Hinblick auf die jeweilige Fragestellung oder das Problem“; Funktionen G (S. 61): „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von Schnittpunkten von Funktionsgraphen“. H (S. 60): „Lösen von Gleichungssystemen – auch lineare Gleichungssysteme mit drei Variablen – auch Nutzen des Additionsverfahrens (z. B. bei Rekonstruktion von quadratischen Funktionen)“, „grafisches Darstellen von Gleichungssystemen (auch mit quadratischen Gleichungen)“. Der RLP nennt das Einsetzungs- und Gleichsetzungsverfahren nicht beim Namen („auch rechnerisch“, G); das Additionsverfahren steht erst auf H.
  7  [LS-AA] Klasse 8, Kapitel III „Lineare Gleichungssysteme“: 1 Lineare Gleichungen mit zwei Variablen · 2 Lineare Gleichungssysteme · 3 Gleichsetzungs- und Einsetzungsverfahren · 4 Additionsverfahren · 5 Probleme lösen mit Gleichungssystemen. Davor Kapitel I „Lineare Funktionen“ (5 Nullstellen und Schnittpunkte), danach Kapitel II „Terme mit mehreren Variablen“. Stundenumfang steht nicht im Fahrplan.
  8  [LISUM-PH] Planungshilfen für einen kompetenzorientierten Mathematikunterricht, Jahrgangsstufen 7 bis 10 (LISUM 2023, CC BY-SA 4.0): keine eigene Reihe; der Stoff liegt vollständig im Block „Gleichungssysteme“ der Reihe „Jahrgangsstufe 8, Mathematik: Terme und Gleichungen“ (Zeitumfang ca. 35 Stunden für die ganze Reihe, nicht je Block ausgewiesen), ergänzt um zwei Zeilen der Reihe „Jahrgangsstufe 9 (Gymnasium), Mathematik: Quadratische Funktionen und Gleichungen“. Differenzierung über Tiefgründigkeit, Details und Aufgabenmenge, dazu eine „nur Gym“-Marke. Jahrgangsstufe 8, RLP-Zeilen ① bis ③, ⑥, ⑦, Niveaustufe F, Leitidee Gleichungen und Funktionen. Block „Gleichungssysteme“: Aufstellen von Gleichungssystemen im Zusammenhang mit linearen Funktionen; grafisches Lösen im Zusammenhang mit linearen Funktionen, auch mit Funktionsplotter; Durchführen der Probe; Lösen von Systemen mit ganzzahligen Koeffizienten und Lösungen durch Probieren, auch mit Tabellenkalkulation; Lösen im Zusammenhang mit linearen Funktionen durch Gleichsetzen, also Schnittpunktberechnung; nur Gym das Einsetzungsverfahren; Erklären der Lösbarkeit über das Schnittverhalten zweier Geraden. Jahrgangsstufe 9 Gymnasium, Niveaustufe H, RLP-Zeile (13): lineare Gleichungssysteme auch mit drei Variablen und Nutzen des Additionsverfahrens, dort am Beispiel der Rekonstruktion einer quadratischen Funktion. Sachkontexte: Zahlen- und Altersrätsel, geometrische Kontexte (aus Umfang und Flächeninhalt auf Seitenlängen schließen), physikalische Einheiten, lineares Wachstum. Begriffe: Gleichung, Probe, einsetzen, gleichsetzen, umformen, gleichwertig, äquivalent, Äquivalenzumformung, unendlich viele Lösungen, überbestimmt, unterbestimmt. Material: LISUM „Material zur Diagnose und Förderung“, Gleichungen und Funktionen, Diagnoseaufgaben zu Gleichungen (vor der Reihe Stufe E, S. 50–52, nach der Reihe Stufe F, S. 53–55), Förderaufgaben „Idee der Gleichung“ (Sek I), Karten 49–63 (S. 222); KOSIMA-Handreichungen; Serlo-Kurs „Einführung in lineare Gleichungssysteme“ – keine eingesehen. Befund, der die Gliederung des Eintrags berührt: Das Additionsverfahren kommt in der Jahrgangsstufe 8 nicht vor. Amtlich sind dort grafisches Lösen, Probieren und Gleichsetzen, das Einsetzungsverfahren nur Gymnasium; das Additionsverfahren steht erst in der Niveaustufe H der Gymnasialreihe der Jahrgangsstufe 9. Der Eintrag folgt bisher dem Lehrwerk, das Gleichsetzungs-, Einsetzungs- und Additionsverfahren gleichrangig in Kl. 8 III führt. Für die Auswahlregel GYM-Sprossen aus 10b ist das der klarste Fall im Katalog: drei Verfahren mit drei verschiedenen amtlichen Zielgruppen. Zweiter Befund: Die Reihe verankert das Gleichungssystem durchgehend an den linearen Funktionen und am Schnittverhalten zweier Geraden – lineare-funktionen.md ist damit amtlich der Blatt-0-Geber dieses Eintrags. Dritter Befund, Mangel der Quelle: Die ersten vier Aufzählungspunkte des Blocks „Gleichungssysteme“ sind wörtlich die Punkte zur indirekten Proportionalität aus der Reihe „Jahrgangsstufe 7, Mathematik: Zuordnungen“ und gehören sachlich nicht hierher. Es handelt sich um einen Übernahmefehler der Planungshilfe; für den Katalog sind nur die übrigen Punkte des Blocks verwertbar.
  9  [GOST] (Sek-II-Teil) Q1, 1. Kurshalbjahr „Analysis; Lineare Algebra“ (BB S. 23–24), Grund- und Leistungskursfach: L1-Zeile „geeignete Verfahren zur Lösung von Gleichungen und Gleichungssystemen auswäh … (gekürzt, 2456 Zeichen)
 10  [FOS] (Sek-II-Teil) Eingangsvoraussetzung L1 (S. 17, Zeile 621): „lösen lineare (2,2)-Gleichungssysteme“ – nur zwei Variablen; Kap. 3 L1 (S. 22, Zeilen 891–892): „geeignete Verfahren zur Lösung von Gl … (gekürzt, 1018 Zeichen)
 11  [LS-AA] (Sek-II-Teil) Qualifikationsphase Kapitel V „Lineare Gleichungssysteme“: 1 Das Gauß-Verfahren · 2 Lösungsmenge linearer Gleichungssysteme · 3 Lineare Gleichungssysteme mit Parametern auf der r … (gekürzt, 735 Zeichen)
 12
 13  ### Lerneinheiten
 14  1. Gleichungen mit zwei Variablen und grafisches Lösen – Lösungspaare einer Gleichung, alle Lösungen als Gerade (nach y umstellen), zwei Geraden zeichnen und den Schnittpunkt ablesen, Probe in beiden Gleichungen; Sonderfälle parallel (keine Lösung) und identisch (unendlich viele); systematisches Probieren mit Tabelle. ← Eingabe „lgs grafisch“, „gleichungssystem zeichnen“
 15    Marken: OS Kl. 9 · GYM Kl. 8 · P10 · nicht für alle: Sekundo 9 LVL
 16  2. Einsetzungsverfahren – eine Gleichung nach einer Variablen umstellen (Vorzahl 1 zuerst), den Term in die andere Gleichung einsetzen, die lineare Gleichung lösen, zweite Variable berechnen, Probe in beiden Gleichungen; Gleichsetzen als Sonderfall, wenn beide Gleichungen nach y aufgelöst sind. ← Eingabe „einsetzungsverfahren“, „lgs lösen“
 17    Marken: OS Kl. 9 · GYM Kl. 8 · P10 · nicht für alle: Elemente 8 Zum Selbstlernen
 18  3. Additionsverfahren – Gleichungen addieren oder subtrahieren, damit eine Variable wegfällt; vorher eine oder beide Gleichungen vervielfachen; Verfahren wählen und begründen. ← Eingabe „additionsverfahren“
 19    Marken: OS Kl. 9 · GYM Kl. 8 · keine P10-Aufgabe
 20  4. Sachaufgaben – Anzahl-und-Preis-Aufgaben (x + y = Anzahl, Preis · x + Preis · y = Gesamtpreis) und Zahlenrätsel: Unbekannte benennen, zwei Gleichungen aufstellen, lösen, Lösung den Größen zuordnen, Antwortsatz; Gleichung im Sachzusammenhang deuten (Variablen und Bestandteile benennen, Gleichung als Satz). ← Eingabe „lgs sachaufgaben“, „gleichungssystem aufstellen“
 21    Marken: OS Kl. 9 · GYM Kl. 8 · P10 · nicht für alle: Mathematik 2023 9 Üben
 22  5. Drei Variablen und Lösungsvielfalt (Sek II) – Systeme mit drei Gleichungen und drei Variablen durch Einsetzen oder Addition lösen, gestaffelte Systeme (Dreiecksform) durch Rückwärtseinsetzen, eine  … (gekürzt, 1268 Zeichen)
 23    Marken: BE Q3 · BB Q1/3 · GK · keine Prüfungsaufgabe
 24  Niveaustufung des Sek-II-Teils: fhr = kein Bestand (Gleichungssysteme nur als Werkzeug der Rekonstruktion); GK = Einheit 1, 3, 4 und 5 über die grundlegenden Poolzeilen (2021, 2023, 2025, 2026 – Lösungsgerade, unlösbares System, Eindeutigkeit, erweitertes System, Kombination, Schar mit Zusatzbedingungen); LK/erhöht = dieselben Einheiten mit den Prüfungshöhen (gestaffelte Systeme mit Parameter im Koeffizienten, Nichtnegativität, Mischungsbilanz – 2017, 2023, 2024, 2025 erhöht); Einheit 2 trägt keine Sek-II-Zeile und bleibt Sek I.
 25
 26  ### Typen je Lerneinheit
 27  Einheit 1: Zahlenpaar als Lösung einer Gleichung prüfen (wA/fA) · Lösungspaare einer Gleichung finden (Tabelle) · Gleichung nach y umstellen [OS 9] · Gerade zu einer Gleichung zeichnen · zwei Geraden zeichnen, Schnittpunkt ablesen, Probe [OS 9, GYM 8] · Lösung eines Systems am gegebenen Bild ablesen · Sonderfälle erkennen (parallel: keine Lösung; identisch: unendlich viele) am Bild und an der Gleichung (gleiche Steigung) [OS 9] · systematisches Probieren mit Tabelle bei ganzzahliger Lösung · Fehler finden (Schnittpunkt ungenau abgelesen, keine Probe; Umstellen mit falschem Vorzeichen) · Begründen (warum der Schnittpunkt beide Gleichungen erfüllt; warum Parallelen keine Lösung haben). — Sek II (fhr / abi / iqb), Haupttypen der Rohdatei mit Zeilenzahl in Klammern, erst Nachweis-, dann Deutungstypen: Nachweis: Eindeutigkeit der Lösung eines Gleichungssystems durch Einsetzen und Vergleich begründen (1; zwei nicht äquivalente Gleichungen, Teil A) — Deutung: Lösungsmenge eines Gleichungssystems mit zwei Variablen als Gerade zeichnen und eine Lösung angeben (1; identische Geraden, Teil A). Dazu: Fehler finden (die Gerade mit dem falschen Vorzeichen der Steigung gezeichnet; nur eingesetzt und die Eindeutigkeit nicht begründet) · Begründen (warum zwei nicht äquivalente Gleichungen mit zwei Variablen höchstens eine gemeinsame Lösung haben).
 28  Einheit 2: eine Gleichung ist nach y aufgelöst, in die andere einsetzen · I nach y umstellen (Vorzahl 1) · nach x umstellen · Klammer mit Zahl davor auflösen · Minus vor der Klammer · Dezimalzahlen (Geld) · negative Lösung · Bruch als Lösung (Vorrat) · Gleichsetzen bei zwei Gleichungen der Form y = … (→ lineare-funktionen.md Einheit 4 für Schnittpunkte) [OS 9, GYM 8] · zweite Variable berechnen und Probe in beiden Gleichungen · Lösung als Zahlenpaar angeben · Fehler finden (Term in dieselbe Gleichung eingesetzt; Vorzahl nur auf das erste Glied der Klammer; zweite Variable vergessen) · Begründen (warum nach dem Einsetzen nur noch eine Variable übrig ist).
 29  Einheit 3: Gegenzahlen: Gleichungen addieren · gleiche Vorzahlen: subtrahieren · eine Gleichung vervielfachen · beide Gleichungen vervielfachen (kleinstes gemeinsames Vielfaches) · negative Zahlen · Dezimalzahlen und Brüche · Verfahren wählen (Einsetzen, Gleichsetzen, Addition) und begründen · Sonderfälle rechnerisch (0 = 5 keine Lösung; 0 = 0 unendlich viele) [GYM 8] · Fehler finden (nur die linke Seite vervielfacht; beim Subtrahieren nur ein Vorzeichen gewechselt) · Begründen (warum man Gleichungen addieren darf). — Sek II (fhr / abi / iqb), Haupttypen der Rohdatei mit Zeilenzahl in Klammern: Deutung: Koeffizienten für ein unlösbares Gleichungssystem angeben und begründen (1; Vielfaches der linken Seite mit anderer rechter Seite, Widerspruch über den Additionsschritt, Teil A). Dazu: Fehler finden (den Faktor mit falschem Vorzeichen gewählt, so dass das System eindeutig lösbar bleibt) · Begründen (warum eine falsche Aussage nach dem Addieren „keine Lösung“ heißt).
 30  Einheit 4: Unbekannte benennen und mit Einheit beschriften · aus zwei Angaben „zusammen …“ zwei Gleichungen aufstellen (nur aufstellen) · Anzahl-und-Preis mit Dezimalzahlen (Eintritt, Blumen, Bäume) · Anzahl-und-Bestand (Zimmer und Betten, Räder von Autos und Rädern) · Zahlenrätsel (Summe und Differenz, Vielfache) [OS 9] · Mischungen und Alter (Vorrat) · System aufstellen, lösen, Lösung zuordnen, Antwortsatz · Probe im Text (Rechnung mit den Zahlen der Aufgabe) · Gleichung im Sachzusammenhang deuten: Variablen benennen (Preis oder Anzahl?) · Gleichung als Satz formulieren („x + y = 20“: zusammen zwanzig Stück) · Bestandteile einer Gleichung deuten (Vorzahl, Absolutglied; bei linearen Funktionen → lineare-funktionen.md Einheit 5, bei Wachstum → potenz-exponentialfunktionen.md) · Fehler finden (Anzahlen und Preise vertauscht; Lösung den falschen Größen zugeordnet) · Begründen (warum zwei Gleichungen nötig sind). — Sek II (fhr / abi / iqb), Haupttypen der Rohdatei mit Zeilenzahl in Klammern: Deutung: Lineares Gleichungssystem im Sachzusammenhang interpretieren (1; Mischung dreier Säfte als Anteilssumme und Bilanz, Teil A). Dazu: Fehler finden (die Variablen als Prozentzahlen der Zutaten statt als Anteile der Säfte gedeutet) · Begründen (warum die Summe der Anteile eins ergibt und die zweite Gleichung eine Bilanz ist).
 31  Einheit 5: Sek II (fhr / abi / iqb), Haupttypen der Rohdatei mit Zeilenzahl in Klammern, erst Berechnungs-, dann Nachweis-, dann Deutungstypen: Gestaffeltes Gleichungssystem für einen Parameterwert lösen (1) · Lineares Gleichungssystem mit drei Variablen lösen (1) · Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen (1) — Nachweis: Lösungsanzahl eines gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung begründen (2; Ermessen, siehe Offene Punkte) · Aussage über die Lösungsmenge eines Gleichungssystems mit Nichtnegativität nachweisen (1) · Lösung eines Gleichungssystems durch Einsetzen nachweisen (1) — Deutung: Lösbarkeit eines Gleichungssystems mit Parameter beurteilen (2; Ermessen, siehe Offene Punkte) · Lösungsanzahl eines erweiterten Gleichungssystems in Abhängigkeit vom Parameter angeben (1). Dazu: Fehler finden (durch einen parameterabhängigen Koeffizienten geteilt, ohne den Fall null zu unterscheiden; nur den Sonderwert des Parameters geprüft und den allgemeinen Fall nicht ausgeführt; das System für eindeutig lösbar gehalten, obwohl eine Gleichung ein Vielfaches der anderen ist; die Ganzzahligkeit einer Variablen übersehen; für den passenden Parameterwert unendlich viele statt genau einer Lösung erwartet; ein Vorzeichen beim Rückwärtseinsetzen verfehlt; die Nichtnegativität der Variablen nicht herangezogen) · Begründen (warum ein Koeffizient null zwei verschiedene Fälle erzeugt; warum eine freie Variable eine ganze Schar von Lösungen liefert und Zusatzbedingungen daraus eine auswählen).
 32  Zählung: 2 + 0 + 1 + 1 + 8 = 12 Haupttypen, 2 + 0 + 1 + 1 + 10 = 14 Zeilen – alle Sek-II-Haupttypen der Rohdatei, jeder genau einmal (die P10-Typen der Einheiten stehen davor ohne Zeilenzahl, ihre Zuordnung unter „Prüfungsform (P10)“).
 33
 34  ### Voraussetzungen (Blatt 0)
 35  Fertigkeiten:
 36  - Lineare Gleichung mit Klammern, Dezimalzahlen und x auf beiden Seiten lösen, Schreibform mit Strich – Einheit 2 bis 4. Thema Lineare Gleichungen (lineare-gleichungen.md), Einheit 2 und 3. [RLP E/F; LS-AA Kl. 7 IV 5]
 37  - Lösung durch Einsetzen prüfen, Ergebnis mit (wA)/(fA) – alle Einheiten. Thema Lineare Gleichungen (lineare-gleichungen.md), Einheit 1. [RLP E „Prüfen einer Lösung“]
 38  - Gleichung nach einer Variablen umstellen (Formel umstellen: ax + by = c nach y) – Einheit 1 und 2. Thema Lineare Gleichungen (lineare-gleichungen.md), Einheit 4. [RLP E „Umstellen von Formeln“]
 39  - Gerade aus der Gleichung zeichnen (n und Steigungsdreieck), Punkt ablesen, Lage zweier Geraden (parallel bei gleicher Steigung) – Einheit 1. Thema Lineare Funktionen (lineare-funktionen.md), Einheit 2 und 4. [RLP F]
 40  - Klammer ausmultiplizieren (Zahl mal Klammer, Minus vor der Klammer), Terme mit zwei Variablen zusammenfassen – Einheit 2 und 3. Thema Terme (terme.md). [RLP E/F Distributivgesetz; LS-AA Kl. 8 II]
 41  - Rechnen mit Dezimalzahlen (Geld) und negativen Zahlen, Division mit dem Taschenrechner – Einheit 2 bis 4. Thema Bruchrechnung (bruchrechnung.md) Einheit 4, Rationale Zahlen (rationale-zahlen.md). [RLP D/E]
 42  - Gleichung mit einer Variablen aus einem Sachverhalt aufstellen (Preis · Anzahl, „zusammen“) – Einheit 4. Thema Lineare Gleichungen (lineare-gleichungen.md), Einheit 4. [P10 „Lineare Gleichung aus Sachverhalt aufstellen“]
 43  - Sek II: Terme mit drei Variablen zusammenfassen, Gleichungen vervielfachen und addieren, nach einer Variablen umstellen – Einheit 5; das Einsetzen und die Addition mit zwei Variablen (Einheit 2 und 3 dieses Eintrags) sind die Werkzeuge des dritten Schritts. Sek-I-Themen terme.md, lineare-gleichungen.md Einheit 2 und 4. [GOST Eingangsvoraussetzung L1 „lösen lineare (2,2)- und (3,3)-Gleichungssysteme“; GOST-OHiMi 2.1]
 44  - Sek II: lineare Ungleichungen in einer Variablen lösen und Lösungen sieben (Vorzeichenbedingung, Ganzzahligkeit, größter Wert) – Einheit 5 (Lösungsschar mit Zusatzbedingungen). Sek-I-Thema lineare-gleichungen.md Einheit 3; Sek-II-Nachbarthema gleichungen-loesen.md (Ungleichungen). [Rohdatei: iqb 2024MerhoehtAAGLAA122-b, 2026MgrundlegendAAGLAA12]
 45  - Sek II: Tripel als Punkte und Vektoren lesen und die Lösungsmenge als Menge schreiben – Einheit 5. Sek-II-Nachbarthemen punkte-und-strecken-im-koordinatensystem.md (Tupel), schnittmengen.md und lagebeziehungen.md (dort die Anwendung: Schnittpunkt von Gerade und Ebene als Gleichungssystem). [GOST Q3 L1 „Tupel in Form von Punkten und Vektoren angeben“, „Gleichungssysteme in Anwendungssituationen (Bestimmung von Schnittmengen)“]
 46  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 47  - „Ist das eine Lösung?“ – ein Zahlenpaar (x | y) in beide Gleichungen einsetzen und ankreuzen: Lösung von I, von II, von beiden, von keiner. Vor Einheit 1 und 2. [RLP E „Prüfen einer Lösung“; LS-AA Kl. 8 III 1]
 48  - „Schnittpunkt oder keiner?“ – zu zwei gezeichneten Geraden ankreuzen: ein Schnittpunkt, parallel, dieselbe Gerade; nichts rechnen. Vor Einheit 1. [RLP F „Lösbarkeit und Lösungsvielfalt“]
 49  - „Welche Gleichung ist fast fertig?“ – die Gleichung ankreuzen, in der eine Variable allein steht oder die Vorzahl 1 hat; die wird umgestellt und eingesetzt. Nichts rechnen. Vor Einheit 2. [LS-AA Kl. 8 III 3; P10 2022-OS-K7b, 2016-OS-K6d Verfahren]
 50  - „Gleiche Vorzahl oder Gegenzahl?“ – ankreuzen, ob eine Variable in beiden Gleichungen dieselbe Vorzahl oder Gegenzahlen hat (dann addieren oder subtrahieren ohne Vervielfachen). Vor Einheit 3. [LS-AA Kl. 8 III 4]
 51  - „Was ist unbekannt?“ – im Text die zwei gesuchten Größen mit x und y benennen und dazuschreiben, ob es ein Preis, eine Anzahl oder eine Länge ist; nichts rechnen. Vor Einheit 4. [P10 2022-OS-K7a Fehlerquelle „x und y als Anzahl der Bäume deuten“]
 52  - „Welche Zahl gehört wohin?“ – in Anzahl-und-Preis-Texten die Anzahlen und die Gesamtbeträge farbig markieren: Anzahlen kommen vor x und y, Gesamtbeträge rechts vom Gleichheitszeichen. Vor Einheit 4. [P10 2024-OS-K7a, 2021-OS-K7b Fehlerquelle „Anzahlen und Preise vertauschen“]
 53  - „Wie viele Lösungen?“ (Sek II) – zu den drei Rechenausgängen einer Umformung ankreuzen: wahre Aussage ohne Variable (unendlich viele Lösungen), falsche Aussage (keine), Wert der Variablen (genau eine); dazu ankreuzen, ob eine Gleichung ein Vielfaches einer anderen ist; nichts rechnen. Vor Einheit 5 (und Einheit 3, Sonderfälle). [GOST-OHiMi 2.1 „Lösbarkeit und Lösungsmenge“; Rohdatei: iqb 2025MgrundlegendAAGLAA12-b, 2026MgrundlegendAAGLAA12 Fehlerquellen]
 54  - „Parameter im Koeffizienten?“ (Sek II) – zu Systemen mit Parameter ankreuzen, ob der Parameter nur auf der rechten Seite steht (immer genau eine Lösung, die vom Parameter abhängt) oder als Faktor vor einer Variablen (Fallunterscheidung nötig: Faktor null oder nicht); nichts rechnen. Vor Einheit 5. [LS-AA QP V 3 „Parameter auf der rechten Seite“; Rohdatei: iqb 2023MerhoehtAAGLAA111, 2025MerhoehtAAGLAA121-b Fehlerquellen „ohne Fallunterscheidung geteilt“]
 55
 56  ### Merkkasten
 57  Einheit 1 (Grafisch):
 58      Eine Gleichung mit zwei Variablen hat viele Lösungspaare – alle zusammen liegen auf einer Geraden. Zum Zeichnen die Gleichung nach y umstellen.
 59        I x + y = 7 → y = −x + 7      II 2x − y = 2 → y = 2x − 2
 60      Lösung des Systems: der Punkt, der auf beiden Geraden liegt – der Schnittpunkt. Ablesen und mit der Probe in beiden Gleichungen prüfen.
 61        Schnittpunkt (3 | 4): 3 + 4 = 7 (wA)      6 − 4 = 2 (wA)
 62      Sonderfälle: parallele Geraden (gleiche Steigung) – keine Lösung; dieselbe Gerade – unendlich viele Lösungen.
 63      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.1] „graphisches Lösen von Gleichungssystemen mit zwei Gleichungen und zwei Variablen“, „Lösbarkeit und Lösungsmenge von linearen Gleichungssystemen“; Teil-A-Belege 2021MgrundlegendAAGLAA211-a (die Lösungsgerade eines Systems mit unendlich vielen Lösungen), 2023MgrundlegendAAGLAA111-a (Eindeutigkeit über nicht äquivalente Gleichungen). Für die Sek I gilt das nicht (P10 mit Hilfsmitteln).
 64      Formelsammlung: Gleichungen – lineare Gleichungssysteme, grafisches Lösen [FS]
 65  Quelle: [RLP F] grafisch, Lösbarkeit; [LS-AA Kl. 8 III 1–2]; eigene Formulierung.
 66
 67  Einheit 2 (Einsetzungsverfahren):
 68      Einsetzen: eine Gleichung nach einer Variablen umstellen und den Term in die andere Gleichung einsetzen – dann hat sie nur noch eine Variable.
 69        I x + y = 9      II 3x + 2y = 22      I: y = 9 − x      in II: 3x + 2 · (9 − x) = 22 → 3x + 18 − 2x = 22 → x = 4      y = 9 − 4 = 5
 70      Probe in beiden Gleichungen: 4 + 5 = 9 (wA)      12 + 10 = 22 (wA)      Lösung (4 | 5).
 71      Gleichsetzen: stehen beide Gleichungen in der Form y = …, die rechten Seiten gleichsetzen.
 72      Formelsammlung: Gleichungen – Einsetzungsverfahren, Gleichsetzungsverfahren [FS]
 73  Quelle: [Serlo 72872, 307508] „Einsetzen, wenn eine Gleichung schon nach einer Variablen aufgelöst ist; Gleichsetzen, wenn beide nach derselben Variablen aufgelöst sind“, sinngemäß; [P10 2022-OS-K7b, 2024-OS-K7b] Verfahren; [LS-AA Kl. 8 III 3].
 74
 75  Einheit 3 (Additionsverfahren):
 76      Addieren: die Gleichungen so vervielfachen, dass eine Variable in beiden Gegenzahlen als Vorzahl hat – dann beide Gleichungen addieren, die Variable fällt weg. Bei gleichen Vorzahlen subtrahieren.
 77        I 3x + 2y = 12      II 5x − 4y = −2      I verdoppeln: 6x + 4y = 24      plus II: 11x = 22 → x = 2      in I: 6 + 2y = 12 → y = 3
 78      Immer beide Seiten vervielfachen, auch die Zahl rechts.
 79      Verfahren wählen: eine Variable steht allein → Einsetzen; beide Gleichungen y = … → Gleichsetzen; gleiche Vorzahlen oder Gegenzahlen → Addition.
 80      Auswendig (Teil A): das Additionsverfahren mit Vervielfachen und die Sonderfälle nach dem Addieren (falsche Aussage: keine Lösung; wahre Aussage: unendlich viele) – im Pool hilfsmittelfrei, Teil-A-Beleg 2021MgrundlegendAAGLAA211-b (Koeffizienten für ein unlösbares System); [GOST-OHiMi 2.1] „Lösbarkeit und Lösungsmenge von linearen Gleichungssystemen“. Für die Sek I gilt das nicht (P10 mit Hilfsmitteln, kein Original zum Additionsverfahren).
 81      Formelsammlung: Gleichungen – Additionsverfahren [FS]
 82  Quelle: [Serlo 72872, 307508] „Additionsverfahren, wenn beim Addieren oder Subtrahieren eine Variable wegfällt“, sinngemäß; [LS-AA Kl. 8 III 4]; [RLP H] Additionsverfahren; [Lernhelfer] Begriff.
 83
 84  Einheit 4 (Sachaufgaben):
 85      Zwei Unbekannte, zwei Gleichungen: x und y benennen (mit Einheit), aus jeder Angabe im Text eine Gleichung machen.
 86        „Ein Heft und ein Stift kosten zusammen 2,50 €; vier Hefte und drei Stifte kosten 8,50 €.“      x Preis eines Hefts, y Preis eines Stifts: I x + y = 2,50      II 4x + 3y = 8,50      Lösung x = 1,00 €, y = 1,50 €
 87      Anzahl-und-Preis: die Anzahlen stehen vor x und y, der Gesamtbetrag steht rechts; „zusammen n Stück“ gibt x + y = n.
 88      Antwort: die Lösung den Größen zuordnen und den Satz aus der Frage bilden; Probe mit den Zahlen aus dem Text.
 89      Gleichung deuten: Vorzahl = Anzahl (oder Preis je Stück), Variable = das Gesuchte, rechte Seite = Gesamtwert. „x + y = 20“ heißt: zusammen zwanzig Stück.
 90      Auswendig (Teil A): das Deuten – Variablen benennen, eine Gleichung als Summe der Anteile oder als Bilanz lesen (auch mit drei Variablen: Mischung dreier Säfte, Anteile x, y, z mit x + y + z = 1 und der Bilanz der Zutat) – Teil-A-Beleg 2024MerhoehtAAGLAA122-a; [GOST Q1 L1] „lineare Gleichungssysteme in Anwendungssituationen“; die Anlage nennt Sachaufgaben nicht. Für die Sek I gilt das nicht (P10 mit Hilfsmitteln).
 91      Formelsammlung: Gleichungen – Sachaufgaben mit zwei Variablen [FS]
 92  Quelle: [RLP F] Sachverhalte durch lineare Gleichungssysteme darstellen; [P10 2024-OS-K7a/b, 2022-OS-K7a, 2021-OS-K7b, 2016-OS-K6d] Aufgabenform; eigene Formulierung.
 93
 94  Einheit 5 (Drei Variablen und Lösungsvielfalt, Sek II):
 95      Drei Variablen: eine Variable aus einer Gleichung ausdrücken oder zwei Gleichungen addieren, bis ein System mit zwei Variablen übrig ist, dann wie in Einheit 2 und 3; gestaffelte Systeme (Dreiecksform) von unten nach oben durch Rückwärtseinsetzen lösen; die Lösung als Tripel (x; y; z) mit Probe in allen Gleichungen.
 96        II x₂ + 2x₃ = 5, III x₂ + x₃ = 3: II − III gibt x₃ = 2, dann x₂ = 1, aus I 3x₁ − 2 = 13 folgt x₁ = 5 – Lösung (5; 1; 2).
 97      Drei Fälle: führt die Rechnung auf eine wahre Aussage (0 = 0), gibt es unendlich viele Lösungen; auf eine falsche (0 = c mit c ≠ 0), keine; sonst genau eine. Zwei Gleichungen sind äquivalent, wenn eine ein Vielfaches der anderen ist – zwei nicht äquivalente Gleichungen mit zwei Variablen haben höchstens eine gemeinsame Lösung.
 98      Unendlich viele Lösungen: eine Variable frei wählen (z = t), die anderen daraus ausdrücken – die Lösungsmenge ist eine Schar {(x(t); y(t); t) | t ∈ ℝ}; Zusatzbedingungen (alle negativ, ganzzahlig, größtes y) sieben aus der Schar die gesuchte Lösung.
 99        I −4x + z = 4, II 2y − z = 4, III 4y − 2z = 8 (III ist das Doppelte von II): z = t, x = t/4 − 1, y = t/2 + 2; alle drei negativ und ganzzahlig heißt t < −4 und t ein Vielfaches von 4, größtes y bei t = −8: Lösung (−3; −2; −8).
100      Parameter: einen parameterabhängigen Koeffizienten nie einfach wegteilen – erst den Fall „Koeffizient null“ ansehen: (4 − a²) · z = 2 + a hat für a = 2 keine Lösung (0 = 4), für a = −2 unendlich viele (0 = 0), sonst genau eine.
101      Erweitert und verwandt: eine dritte Gleichung mit Parameter passt genau dann zur eindeutigen Lösung der ersten beiden, wenn diese sie erfüllt (t = −3 aus (1; −1) in −2x + y = t); ein Parameterwert liefert unendlich viele Lösungen, wenn die dritte Gleichung eine Kombination der beiden anderen wird (I + II gleich III für a = 5).
102      Unlösbar konstruieren: dieselbe linke Seite bis auf einen Faktor, eine andere rechte Seite – 3 · I + II* mit a = 3 und b = −3 liefert 0 = −12.
103      Auswendig (Teil A): der ganze Kasten – alle vierzehn Poolzeilen des Themas sind hilfsmittelfrei; [GOST-OHiMi 2.1] „Lösbarkeit und Lösungsmenge von linearen Gleichungssystemen“; das Gauß-Verfahren nennt der Plan, die Anlage nicht beim Namen – der Pool verlangt gestaffelte Systeme und einzelne Additionsschritte (Teil-A-Belege 2025MerhoehtAAGLAA121-a, 2026MgrundlegendAAGLAA12, 2023MerhoehtAAGLAA111).
104      Formelsammlung: [FS-IQB 1.1] führt weder ein Lösungsverfahren noch die Lösbarkeitsfälle; in Teil A ohnehin nicht zugelassen – [FS] offen
105  Quelle: eigene Formulierung nach [GOST Q1 L1] „Gauß-Verfahren zur Lösung linearer Gleichungssysteme“, „Lösbarkeit eines linearen Gleichungssystems (eine Lösung, keine Lösung, unendlich viele Lösungen)“ und [GOST-OHiMi 2.1]; Zahlenbeispiele aus iqb 2017MerhoehtAAGLAA111-a, 2026MgrundlegendAAGLAA12, 2025MerhoehtAAGLAA121-b, 2023MgrundlegendAAGLAA111-b, 2025MgrundlegendAAGLAA12-b und 2021MgrundlegendAAGLAA211-b; [LS-AA QP V 1–3].
106
107  ### Typische Fehler
108  - Anzahlen und Preise vertauscht: x + y = 21,20 statt 3,80; Gleichungen mit vertauschten Anzahlen (2e + 3k statt e + 3k). [P10 2024-OS-K7a, 2021-OS-K7b]
109  - Variablen als Anzahl statt als Preis gedeutet („x = Anzahl der Apfelbäume“); „r + t = 13“ als „13 € für Rose und Tulpe“ gelesen. [P10 2022-OS-K7a, 2024-OS-K7b]
110  - Lösung den Größen falsch zugeordnet oder vertauscht (9 Drei-Bett-Zimmer statt 7); Antwort ohne Zuordnung. [P10 2022-OS-K7b, 2021-OS-K7b, 2016-OS-K6d]
111  - Rechenfehler beim Ausmultiplizieren nach dem Einsetzen: Vorzahl nur auf den ersten Summanden der Klammer, Minus vor der Klammer nicht auf beide Glieder; Probe in II vergessen. [P10 2024-OS-K7b, 2022-OS-K7b]
112  - Nur eine Gleichung aufgestellt und probiert, ohne Kommentar, ob alle Möglichkeiten geprüft sind. [P10 2016-OS-K6d]
113  - Cent und Euro gemischt („20 Cent“ als 20). [P10 2021-OS-K7a] (→ lineare-funktionen.md Einheit 5)
114  - Beim Einsetzen den Term in dieselbe Gleichung eingesetzt (ergibt 0 = 0); nach dem Einsetzen die zweite Variable vergessen (nur x angegeben); Lösung als eine Zahl statt als Zahlenpaar. [FD, aus dem Gedächtnis; P10 2022-OS-K7b Fehlerquelle „Ergebnisse vertauschen“]
115  - Additionsverfahren: nur die linke Seite vervielfacht; beim Subtrahieren nur beim ersten Glied das Vorzeichen gewechselt; Gleichungen addiert, obwohl die Vorzahlen gleich sind (Variable fällt nicht weg). [FD, aus dem Gedächtnis]
116  - Grafisch: Schnittpunkt zwischen Gitterpunkten „glatt“ abgelesen ohne Probe; Parallelen als „Lösung 0“ oder „unendlich“ gedeutet; Umstellen nach y mit falschem Vorzeichen (das Vorzeichen von x bleibt beim Rüberbringen nicht stehen). [FD, aus dem Gedächtnis; RLP F Lösbarkeit]
117  - Sek II, Parameter ohne Fallunterscheidung: durch einen parameterabhängigen Koeffizienten geteilt, ohne den Fall null zu unterscheiden; nur den Sonderwert geprüft und den allgemeinen Fall nicht ausgeführt; das System für den passenden Parameterwert als widersprüchlich gehalten oder für alle Werte als eindeutig lösbar erklärt; für den passenden Wert unendlich viele statt genau einer Lösung erwartet; den Faktor mit falschem Vorzeichen gewählt, so dass das System eindeutig lösbar bleibt. [iqb 2025MerhoehtAAGLAA121-b, 2023MerhoehtAAGLAA111, 2017MerhoehtAAGLAA111-b, 2025MgrundlegendAAGLAA12-b, 2023MgrundlegendAAGLAA111-b, 2021MgrundlegendAAGLAA211-b]
118  - Sek II, Vorzeichen beim Einsetzen und Auflösen: ein negativer Wert in einen negativen Term eingesetzt und das Vorzeichen verfehlt; das Vorzeichen einer Variablen beim Rückwärtseinsetzen übersehen; beim Auflösen der ersten Gleichung das Vorzeichen vertauscht; die Lösungsgerade mit dem falschen Vorzeichen der Steigung gezeichnet. [iqb 2025MgrundlegendAAGLAA12-a, 2025MerhoehtAAGLAA121-a, 2017MerhoehtAAGLAA111-a, 2021MgrundlegendAAGLAA211-a]
119  - Sek II, Lösungsvielfalt verkannt: das unterbestimmte System für eindeutig lösbar gehalten oder die Ganzzahligkeit einer Variablen übersehen; nur eingesetzt und die Eindeutigkeit nicht begründet; die Nichtnegativität der Variablen nicht herangezogen und die Aussage für falsch gehalten; die Variablen als Prozentzahlen der Zutaten statt als Anteile der Säfte gedeutet. [iqb 2026MgrundlegendAAGLAA12, 2023MgrundlegendAAGLAA111-a, 2024MerhoehtAAGLAA122-b, 2024MerhoehtAAGLAA122-a]
120
121  ### Für schwache Schüler
122  Mindeststoff (D/E) [RLP]: keiner – das Thema beginnt auf F (grafisch, systematisches Probieren, Sachverhalte darstellen; Oberschule 9–10 regulär) und G (rechnerisch); das Additionsverfahren steht im RLP erst auf H. Mindeststoff der Prüfungsvorbereitung (P10, FOR) [P10]: Einheit 4 Anzahl-und-Preis-System aufstellen, Variablen und Gleichung deuten, Lösung zuordnen; Einheit 2 Einsetzungsverfahren mit Vorzahl 1 (y = n − x) – das einzige Verfahren in den Originalen; Einheit 1 als Anschauung (Lösung ist ein Punkt) und systematisches Probieren als Ersatzweg (2016). Vorrat: Einheit 3 (Gymnasium regulär), Sonderfälle rechnerisch, Brüche, Verfahren vergleichen; drei Variablen (H) seit dem Sek-II-Teil in Einheit 5. Mindeststoff Sek II (GK-Kern Q1/Q3 / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q1 „Gauß-Verfahren“, „Lösbarkeit eines linearen Gleichungssystems (eine Lösung, keine Lösung, unendlich viele Lösungen)“, „lineare Gleichungssysteme in Anwendungssituationen“ und Q3 „bis zu drei Variablen“ – Einheit 5 vollständig, dazu die Sek-II-Zeilen der Einheiten 1, 3 und 4 (Lösungsgerade, Sonderfälle, Deuten); kein LK-Zusatz. Ohne Hilfsmittel (Anlage OHiMi 2.1, Prüfungsteil A): „Lösbarkeit und Lösungsmenge“, „graphisches Lösen mit zwei Gleichungen und zwei Variablen“ – die Kästen 1 und 5 vollständig, aus Kasten 3 die Sonderfälle; alle vierzehn Sek-II-Zeilen sind Teil A. Vorrat des Sek-II-Teils (Ermessen): das Gauß-Verfahren als Algorithmus mit Koeffizientenmatrix (der Plan nennt es, der Pool verlangt nur gestaffelte Systeme und einzelne Additionsschritte). RLP FOS (fhr): kein Bestand – das Gleichungssystem ist dort Werkzeug der Rekonstruktion (rekonstruktion-von-funktionsgleichungen.md), Einheit 5 ist für fhr Vorrat.
123  Grundvorstellung (Blatt 0) [RLP F, MO]: Zwei Unbekannte brauchen zwei Angaben – „Anna und Ben haben zusammen 11 Bonbons. Wie viele kann jeder haben? Schreib drei Möglichkeiten in die Tabelle. Jetzt weißt du außerdem: Anna hat einen Bonbon mehr als Ben. Welche Möglichkeit bleibt übrig?“ Wer nach der ersten Angabe schon eine einzige Zahl festlegt oder bei der zweiten Angabe von vorn rät, braucht das vor den Verfahren: Die erste Gleichung lässt viele Paare zu, die zweite wählt eines aus. [P10 2016-OS-K6d Fehlerquelle „nur eine Gleichung aufstellen und probieren“]
124  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, FD]:
125  - Grafisch (Einheit 1): Zahlenpaar prüfen – Lösung von I, II, beiden (Vorstufe) → Lösungspaare einer Gleichung in eine Tabelle (4×) → Gleichung nach y umstellen → Gerade zeichnen → zwei Geraden zeichnen und Schnittpunkt ablesen → Probe in beiden Gleichungen → Lösung an einem gegebenen Bild ablesen → Sonderfälle parallel und identisch → systematisches Probieren mit Tabelle → Prüfungshöhe: Zimmer und Betten (16 Zimmer, 66 Betten, Drei- und Fünf-Bett-Zimmer) durch Probieren oder grafisch lösen und begründen, dass es keine andere Möglichkeit gibt (P10-Form 2016-OS-K6d, Stern; im Original auch rechnerisch).
126  - Einsetzen (Einheit 2; LISUM-PH führt es in der Jahrgangsstufe acht als „nur Gym“ – hier für alle Bildungsgänge, weil die P10 es verlangt): Gleichung mit Vorzahl 1 ankreuzen (Vorstufe) → I ist nach y aufgelöst, in II einsetzen (4×) → I nach y umstellen (Vorzahl 1) → nach x umstellen → Klammer mit Zahl davor → Minus vor der Klammer → Dezimalzahlen (Geld) → negative Lösung → Gleichsetzen bei zwei Gleichungen y = … → Probe in beiden Gleichungen und Zahlenpaar angeben → Prüfungshöhe: Preise aus einem gegebenen System mit Dezimalzahlen (x + y = 63; 9x + 3y = 352,20) durch Einsetzen, Antwort mit Zuordnung (P10-Form 2022-OS-K7b, Stern).
127  - Addition (Einheit 3, GYM): gleiche Vorzahl oder Gegenzahl ankreuzen (Vorstufe) → Gegenzahlen, addieren (4×) → gleiche Vorzahlen, subtrahieren → eine Gleichung vervielfachen → beide vervielfachen → negative Zahlen → Dezimalzahlen (Vorrat) → Sonderfall keine oder unendlich viele Lösungen (Vorrat) → Verfahren wählen und begründen → Prüfungshöhe: kein P10-Original; Zielmarke nach RLP H und LISUM-PH Jahrgangsstufe neun (Gymnasium): ein System, in dem eine Gleichung vervielfacht werden muss, mit dem Additionsverfahren lösen, in beiden Gleichungen prüfen und die Wahl des Verfahrens begründen. Die ganze Kette trägt GYM: das Additionsverfahren steht amtlich erst in Niveaustufe H der Gymnasialreihe der Jahrgangsstufe neun, kein P10-Original nutzt es, und für die Prüfungsvorbereitung reicht das Einsetzen.
128  - Sachaufgaben (Einheit 4): Unbekannte benennen, Anzahlen und Beträge markieren (Vorstufe) → aus zwei Sätzen „zusammen …“ die Gleichungen aufstellen, nicht lösen (4×) → Anzahl-und-Preis mit Dezimalzahlen → Anzahl-und-Bestand (Zimmer, Räder) → Zahlenrätsel mit Summe und Differenz → Variablen einer gegebenen Gleichung benennen → Gleichung als Satz formulieren → aufstellen, lösen, zuordnen, Antwortsatz → Prüfungshöhe: Rosen und Tulpen – System aus „zusammen 3,80 €“ und „sechs Rosen und fünf Tulpen 21,20 €“ aufstellen; „r + t = 13“ als Satz deuten und das System mit Stückpreisen lösen (P10-Form 2024-OS-K7a/b, Stern).
129  - Grafisch, Sek II (Einheit 1): Schnittpunkt oder keiner? ankreuzen (Vorstufe) → die Lösungsmenge eines Systems, dessen zweite Gleichung ein Vielfaches der ersten ist, als Gerade zeichnen und die Lösung zu einem vorgegebenen Wert angeben (Grundfall, viermal; iqb 2021MgrundlegendAAGLAA211-a) → Prüfungshöhe: eine vorgegebene Lösung durch Einsetzen bestätigen und begründen, dass es keine weitere gibt, weil die Gleichungen nicht äquivalent sind (iqb 2023MgrundlegendAAGLAA111-a, Teil A, Niveau I – die Höhe liegt im Begründen, nicht im Rechnen).
130  - Addition, Sek II (Einheit 3): Gleiche Vorzahl oder Gegenzahl? ankreuzen (Vorstufe) → Gleichungen mit Gegenzahlen addieren und die Sonderfälle wahre und falsche Aussage erkennen (Grundfall, viermal) → eine Gleichung als Vielfaches der linken Seite einer anderen mit passender rechter Seite ergänzen (unendlich viele Lösungen) → Prüfungshöhe: Koeffizienten so wählen, dass das System keine Lösung hat, und den Widerspruch über den Additionsschritt zeigen (iqb 2021MgrundlegendAAGLAA211-b, Teil A, Niveau II).
131  - Sachaufgaben, Sek II (Einheit 4): Was ist unbekannt? ankreuzen (Vorstufe) → die Gleichungen eines gegebenen Systems mit zwei Variablen als Sätze lesen (Grundfall, viermal) → ein System mit drei Variablen als Summe der Anteile und Bilanz einer Zutat lesen → Prüfungshöhe: das Mischungssystem dreier Säfte im Sachzusammenhang deuten, Variablen als Anteile benennen (iqb 2024MerhoehtAAGLAA122-a, Teil A, Niveau II).
132  - Drei Variablen und Lösungsvielfalt (Einheit 5): „Wie viele Lösungen?“ und „Parameter im Koeffizienten?“ ankreuzen (Vorstufe) → eine vorgegebene Lösung in alle Gleichungen einsetzen und die Gültigkeit zeigen (Grundfall, viermal; iqb 2025MgrundlegendAAGLAA12-a) → ein gestaffeltes System durch Rückwärtseinsetzen lösen, auch nach dem Einsetzen eines Parameterwerts (iqb 2025MerhoehtAAGLAA121-a) → ein System mit drei Variablen durch Subtrahieren zweier Gleichungen und Einsetzen lösen (iqb 2017MerhoehtAAGLAA111-a) → die drei Fälle der Lösbarkeit rechnerisch: eine Gleichung als Vielfaches oder Kombination der anderen erkennen (iqb 2025MgrundlegendAAGLAA12-b, 2017MerhoehtAAGLAA111-b) → unendlich viele Lösungen als Schar mit Parameter schreiben und eine Lösung unter Zusatzbedingungen auswählen (iqb 2026MgrundlegendAAGLAA12) → ein erweitertes System: die dritte Gleichung mit Parameter an der eindeutigen Lösung prüfen (iqb 2023MgrundlegendAAGLAA111-b) → Fallunterscheidung am parameterabhängigen Koeffizienten (iqb 2023MerhoehtAAGLAA111, 2025MerhoehtAAGLAA121-b) → Prüfungshöhe: eine Aussage über die Lösungsschar über eine Ungleichung im Parameter und die Nichtnegativität der Variablen nachweisen (iqb 2024MerhoehtAAGLAA122-b, Teil A, Anforderungsbereich III, Niveau III).
133
134  ### Prüfungsform (P10)
135  Thema „Lineare Gleichungssysteme“ mit drei Typen und vier Aufgabenstämmen (2016 Ausflug d, 2021 Gleichungen b, 2022 Bäume, 2024 Blumenstrauß), zusammen sechs Teilaufgaben [P10]: „Lineares Gleichungssystem aufstellen“ (2024-OS-K7a, Niveau I, zwei Punkte: Rose und Tulpe 3,80 €, sechs Rosen und fünf Tulpen 21,20 €, x und y vorgegeben; 2021-OS-K7b und 2016-OS-K6d als Aufstellen und Lösen in einer Teilaufgabe, vier Punkte). „Lineares Gleichungssystem lösen“ (2022-OS-K7b, Stern, Niveau II: x + y = 63 und 9x + 3y = 352,20, Einsetzen von y = 63 − x, Ergebnis 27,20 € und 35,80 €; als Nebentyp 2024-OS-K7b Stern, 2021-OS-K7b, 2016-OS-K6d). „Gleichung im Sachzusammenhang deuten“ (2022-OS-K7a, Niveau I: Bedeutung von x und y bei gegebenem System; 2024-OS-K7b, Stern: „r + t = 13“ als Satz; außerhalb des Themas 2021-OS-K6c Kerze y = −0,2x + 40 → lineare-funktionen.md, 2019-OS-K7b Ferkel f(x) = 10 · 1,04^x → potenz-exponentialfunktionen.md, 2018-OS-K7c Ereignis zu einer Rechnung → wahrscheinlichkeit.md). Muster: immer Anzahl-und-Preis oder Anzahl-und-Bestand, zwei Summenangaben, Lösung ganzzahlig oder in Cent glatt, Einsetzen mit Vorzahl 1; nie grafisch, nie Additionsverfahren, nie Sonderfälle; Hilfsmittel ja. Der Bestand ist dünn: „Lineares Gleichungssystem lösen“ nur einmal als Haupttyp – Prüfungsblatt-Prompt-Hefte zu diesem Thema haben wenige Originale (Fehlbestand).
136  Zuordnung: Einheit 1 – kein eigener P10-Typ (grafisch und Probieren, RLP F); Einheit 2 – Lineares Gleichungssystem lösen; Einheit 3 – kein P10-Typ (Additionsverfahren); Einheit 4 – Lineares Gleichungssystem aufstellen, Gleichung im Sachzusammenhang deuten; Einheit 5 – kein P10-Typ (Sek-II-Einheit, Entscheidung 37; ihre Typen stehen unter „Prüfungsform (fhr / abi / iqb)“).
137  Zielmarke: Einheit 2 Preise aus x + y = 63 und 9x + 3y = 352,20; Einheit 4 Rosen und Tulpen: System aufstellen, „r + t = 13“ deuten, Lösung acht Rosen und fünf Tulpen; Einheit 1 Zimmer und Betten durch Probieren mit Begründung; Einheit 3 (GYM, am 10f gesetzt) ein System mit einer zu vervielfachenden Gleichung mit dem Additionsverfahren lösen und die Verfahrenswahl begründen – kein P10-Original, Marke nach RLP H und LISUM-PH Jg. 9 Gymnasium.
138
139  ### Prüfungsform (fhr / abi / iqb)
140  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich; die Geltungsdateien abi-*-geltung.md führen das Thema Lineare Gleichungssysteme für alle vier Zielprüfungen mit „ja“ – der abi-Katalog trägt gleichwohl keine Zeile (die Landeshefte prüfen Gleichungssysteme nur eingebettet: Schnittmengen, Rekonstruktion, Matrizen). Für fhr ist der Pool keine Vorgabe; der RLP FOS 2019 führt das Gleichungssystem als Werkzeug der Rekonstruktion, der fhr-Katalog trägt keine Zeile. Die Rohdatei zählt für die Sekundarstufe II 14 Zeilen mit 12 Haupttypen (iqb 14 Zeilen, 12 Typen), Jahre 2017–2026; die 6 msa-Originale stehen unter „Prüfungsform (P10)“. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix; Leitidee der Zeilen Analytische Geometrie nach iqb.md § 6).
141  fhr: kein Bestand, keine Zeile – Gleichungssysteme kommen im fhr-Katalog nur als Rechenschritt der Rekonstruktion vor (rekonstruktion-von-funktionsgleichungen.md).
142  abi: kein Bestand, keine Zeile – kein Landesheft 2017–2026 stellt ein Gleichungssystem für sich.
143  iqb (14 Zeilen, 12 Typen; Pool 2017 und 2021–2026, grundlegend 7 und erhöht 7 Zeilen, alle Teil A) [iqb-Katalog]: Lösbarkeit eines Gleichungssystems mit Parameter beurteilen (2, E5) · Lösungsanzahl eines gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung begründen (2, E5) · je 1: Aussage über die Lösungsmenge eines Gleichungssystems mit Nichtnegativität nachweisen (E5) · Eindeutigkeit der Lösung eines Gleichungssystems durch Einsetzen und Vergleich begründen (E1) · Gestaffeltes Gleichungssystem für einen Parameterwert lösen (E5) · Koeffizienten für ein unlösbares Gleichungssystem angeben und begründen (E3) · Lineares Gleichungssystem im Sachzusammenhang interpretieren (E4) · Lineares Gleichungssystem mit drei Variablen lösen (E5) · Lösung eines Gleichungssystems durch Einsetzen nachweisen (E5) · Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen (E5) · Lösungsanzahl eines erweiterten Gleichungssystems in Abhängigkeit vom Parameter angeben (E5) · Lösungsmenge eines Gleichungssystems mit zwei Variablen als Gerade zeichnen und eine Lösung angeben (E1). Muster: Das Gleichungssystem ist im Pool eine hilfsmittelfreie Kurzaufgabe des Sachgebiets AG/LA (Prüfungsteil A nach [IQB-STR 1], ein bis fünf Punkte), fast immer als Zweierschritt: a) ein leichter Rechen- oder Nachweisschritt (Lösung einsetzen, gestaffelt lösen, Lösungsgerade zeichnen – Anforderungsbereich I), b) die Lösbarkeit mit Parameter (Fallunterscheidung, Kombination erkennen, erweitertes System – Anforderungsbereich II bis III); zwei Stämme stehen als Aufgabe ohne Teilaufgaben (2026MgrundlegendAAGLAA12 mit fünf Punkten – die Schar mit Zusatzbedingungen –, 2023MerhoehtAAGLAA111 mit fünf Punkten – die Fallunterscheidung). Grundlegend 7 (2021MgrundlegendAAGLAA211-a, 2021MgrundlegendAAGLAA211-b, 2023MgrundlegendAAGLAA111-a, 2023MgrundlegendAAGLAA111-b, 2025MgrundlegendAAGLAA12-a, 2025MgrundlegendAAGLAA12-b, 2026MgrundlegendAAGLAA12), erhöht 7 (2017MerhoehtAAGLAA111-a, 2017MerhoehtAAGLAA111-b, 2023MerhoehtAAGLAA111, 2024MerhoehtAAGLAA122-a, 2024MerhoehtAAGLAA122-b, 2025MerhoehtAAGLAA121-a, 2025MerhoehtAAGLAA121-b); die Grundkurspools prüfen die zwei Variablen und die Schar, die erhöhten Pools die Parameter im Koeffizienten, die Sachdeutung und die Nichtnegativität. Amtlicher Anforderungsbereich in allen 14 Zeilen (höchster Bereich: I 4, II 6, III 4); Niveau I 5, II 4, III 5. Keine Dubletten in Landesheften. Vier Dateien liegen im Pool wortgleich ein zweites Mal vor (Dateidubletten ohne Zeile, iqb.md § 4). Kontexte: fast ohne Sachbezug – nur die Fruchtsaftmischung 2024.
144  Zielmarke (Sek II): Einheit 1 – iqb: die Lösungsgerade mit vorgegebenem y (2021MgrundlegendAAGLAA211-a, drei Punkte, Niveau I) und die Eindeutigkeit über nicht äquivalente Gleichungen (2023MgrundlegendAAGLAA111-a, Niveau I). Einheit 3 – iqb: Koeffizienten für ein unlösbares System mit Widerspruch (2021MgrundlegendAAGLAA211-b, Niveau II). Einheit 4 – iqb: die Mischung dreier Säfte als Gleichungssystem deuten (2024MerhoehtAAGLAA122-a, Niveau II). Einheit 5 – iqb: die Schar mit Vorzeichen- und Ganzzahligkeitsbedingung (2026MgrundlegendAAGLAA12, fünf Punkte, Niveau III), die Fallunterscheidung am Koeffizienten (2023MerhoehtAAGLAA111, fünf Punkte; 2025MerhoehtAAGLAA121-b, Niveau III), die Nichtnegativität in der Lösungsschar (2024MerhoehtAAGLAA122-b, Anforderungsbereich III, Niveau III) und als Basismarke das gestaffelte System für einen Parameterwert (2025MerhoehtAAGLAA121-a, Niveau I); fhr und abi: keine Zeile.
````

## 2 Originale (23)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2024-OS-K7a (msa-katalog-kontext.csv)

jahr 2024 · papier OS · punkte 2 · format Kurzantwort · antwort Term
- gegeben: Geschäft A: Rose + Tulpe = 3,80 €; 6 Rosen + 5 Tulpen = 21,20 €; x Preis pro Rose, y Preis pro Tulpe
- gesucht: Gleichungen I und II
- verfahren: je Angabe eine Gleichung
- fehlerquelle: Anzahlen und Preise vertauschen (x + y = 21,20)

### 2021-OS-K7b (msa-katalog-kontext.csv)

jahr 2021 · papier OS · punkte 4 · format Rechnung · antwort Term|Zahl
- gegeben: Familie Beyer (2 Erwachsene, 2 Kinder) zahlt 77,80 €; Familie Gouvan (1 Erwachsener, 3 Kinder) zahlt 64,90 €
- gesucht: zwei Gleichungen|Preis für Erwachsene und für Kinder
- verfahren: I 2e + 2k = 77,80, II e + 3k = 64,90; e = 64,90 − 3k in I: 129,80 − 4k = 77,80 → k = 13
- fehlerquelle: Gleichungen mit vertauschten Anzahlen; Ergebnisse den Personen falsch zuordnen

### 2016-OS-K6d (msa-katalog-kontext.csv)

jahr 2016 · papier OS · punkte 4 · format Rechnung · antwort Zahl|Zahl
- gegeben: 16 Zimmer, 66 Betten; Drei- und Fünf-Bett-Zimmer
- gesucht: Anzahl der Drei- und Fünf-Bett-Zimmer
- verfahren: x + y = 16; 3x + 5y = 66; Einsetzen: 3(16 − y) + 5y = 66
- fehlerquelle: Zahlen vertauschen (9 Drei-Bett: 27 + 35 = 62); nur eine Gleichung aufstellen und probieren ohne Kommentar

### 2022-OS-K7b (msa-katalog-kontext.csv)

jahr 2022 · papier OS · punkte 3 · format Rechnung · antwort Zahl
- gegeben: ein Apfelbaum und ein Pflaumenbaum zusammen 63,00 €; 9 Apfelbäume und 3 Pflaumenbäume 352,20 €; Gleichungen I x + y = 63, II 9x + 3y = 352,20
- gesucht: Preis eines Apfelbaums und eines Pflaumenbaums
- verfahren: y = 63 − x in II: 9x + 189 − 3x = 352,20 → 6x = 163,20
- fehlerquelle: Ergebnisse vertauschen; Probe in II vergessen

### 2024-OS-K7b (msa-katalog-kontext.csv)

jahr 2024 · papier OS · punkte 4 · format Kurzantwort|Rechnung · antwort Text|Zahl
- gegeben: Geschäft B: Rose 2,30 €, Tulpe 1,70 €; Filips System I. 2,30r + 1,70t = 26,90, II. r + t = 13 (r Rosen, t Tulpen)
- gesucht: Satz zu Gleichung II|Lösung des Systems
- verfahren: II: r = 13 − t in I einsetzen: 2,30(13 − t) + 1,70t = 26,90; 29,9 − 0,6t = 26,90; t = 5, r = 8
- fehlerquelle: II als „13 € für Rose und Tulpe“ deuten; Rechenfehler beim Ausmultiplizieren

### 2022-OS-K7a (msa-katalog-kontext.csv)

jahr 2022 · papier OS · punkte 2 · format Kurzantwort · antwort Text
- gegeben: ein Apfelbaum und ein Pflaumenbaum zusammen 63,00 €; 9 Apfelbäume und 3 Pflaumenbäume 352,20 €; Gleichungen I x + y = 63, II 9x + 3y = 352,20
- gesucht: Bedeutung von x und y
- verfahren: Koeffizienten 9 und 3 mit den Stückzahlen abgleichen
- fehlerquelle: x und y als Anzahl der Bäume deuten

### 2021-OS-K6c (msa-katalog-kontext.csv)

jahr 2021 · papier OS · punkte 3 · format Kurzantwort · antwort Text
- gegeben: Gleichung y = −0,2x + 40 beschreibt das Abbrennen einer 40 cm hohen Kerze; Bedeutung von −0,2 vorgegeben (Abnahme 0,2 cm je Minute)
- gesucht: Bedeutung von y, x und 40
- verfahren: Variablen und Achsenabschnitt dem Sachverhalt zuordnen
- fehlerquelle: x und y vertauschen; 40 als Brenndauer deuten

### 2019-OS-K7b (msa-katalog-kontext.csv)

jahr 2019 · papier OS · punkte 3 · format Tabelle · antwort Text
- gegeben: Ferkel 10 kg, wöchentlich +4 %; Funktionsgleichung f(x) = 10 · 1,04^x
- gesucht: Bedeutung von 10, 1,04 und x
- verfahren: Bestandteile mit Anfangsmasse, Wachstumsfaktor (100 % + 4 %) und Zeit abgleichen
- fehlerquelle: 1,04 als „4 %“ oder als Zunahme in kg deuten

### 2018-OS-K7c (msa-katalog-kontext.csv)

jahr 2018 · papier OS · punkte 4 · format Kurzantwort|Rechnung|Kurzantwort · antwort Text|Zahl|Text
- gegeben: 16 Pfannkuchen (14 Marmelade M, 2 Senf S); zwei nacheinander zufällig ohne Zurücklegen; Rechnung P(E) = 2/16 · 1/15 + 14/16 · 13/15
- gesucht: alle Ergebnisse mit mindestens einem Senf-Pfannkuchen|P(beide Marmelade)|Ereignis E zur Rechnung in Worten
- verfahren: Ergebnisse (S;M), (M;S), (S;S); P(M;M) = 14/16 · 13/15; E: beide gleich (beide Senf oder beide Marmelade)
- fehlerquelle: (S;M) und (M;S) als ein Ergebnis zählen; zweiter Faktor 14/16 statt 13/15; E als „mindestens ein Senf“ deuten (das wäre 1 − P(M;M))

### 2026MgrundlegendAAGLAA12 (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: lineares Gleichungssystem I: −4x + z = 4, II: 2y − z = 4, III: 4y − 2z = 8; betrachtet werden nur Lösungen (x; y; z), bei denen x, y und z negativ und ganzzahlig sind
- gesucht: die Lösung mit dem größten Wert für y
- verfahren: II und III sind Vielfache, das System hat unendlich viele Lösungen; mit z = t folgt x = t/4 − 1 und y = t/2 + 2; alle drei negativ heißt t < −4, ganzzahlig heißt t Vielfaches von 4; größtes y bei t = −8
- fehlerquelle: das System für eindeutig lösbar halten oder die Ganzzahligkeit von x übersehen und t = −6 nehmen

### 2023MerhoehtAAGLAA111 (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 5 · format Rechnung · antwort Text|Term
- gegeben: I 2x + z = 0, II −y + 2z = 0, III 2y + bz = 1 mit reellen x, y, z und Parameter b
- gesucht: Anzahl der Lösungen in Abhängigkeit von b, gegebenenfalls die Lösungen
- verfahren: II und III zu (4 + b) · z = 1 kombinieren; b = −4 liefert 0 = 1, sonst z und daraus y und x
- fehlerquelle: durch (4 + b) teilen, ohne b = −4 auszuschließen

### 2021MgrundlegendAAGLAA211-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Zeichnen|Kurzantwort · antwort Grafik|Zahl
- gegeben: I −x + y = −3, II 2x − 2y = 6 mit reellen x, y; unendlich viele Lösungen
- gesucht: grafische Darstellung der Lösungen; die Lösung mit y = 1
- verfahren: Gerade y = x − 3 zeichnen, y = 1 einsetzen
- fehlerquelle: Gerade mit Steigung −1 zeichnen

### 2021MgrundlegendAAGLAA211-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Kurzantwort|Begründung · antwort Zahl|Text
- gegeben: I −x + y = −3; II* a · x − 3y = b mit reellen a, b
- gesucht: Werte von a und b, für die I und II* keine Lösung haben, mit Begründung
- verfahren: II* als Vielfaches der linken Seite von I mit unpassender rechter Seite wählen
- fehlerquelle: a = −3 wählen (dann eindeutig lösbar)

### 2023MgrundlegendAAGLAA111-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Gleichungssystem I 3x − y = 4, II −3x − 15y = 12 mit reellen x, y
- gesucht: Begründung, dass es nur die Lösung x = 1 und y = −1 hat
- verfahren: Lösung in beide Gleichungen einsetzen; da die Gleichungen nicht äquivalent sind, gibt es keine weitere
- fehlerquelle: nur einsetzen und die Eindeutigkeit nicht begründen

### 2023MgrundlegendAAGLAA111-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: I und II mit der einzigen Lösung (1; −1), erweitert um III −2x + y = t mit reellem t
- gesucht: Anzahl der Lösungen des erweiterten Systems in Abhängigkeit von t, mit Begründung
- verfahren: die einzige Lösung von I und II in III einsetzen: III ist genau für t = −3 erfüllt
- fehlerquelle: für t = −3 unendlich viele Lösungen erwarten

### 2025MgrundlegendAAGLAA12-a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 1 · format Begründung · antwort Text
- gegeben: lineares Gleichungssystem I: 2x − y − 2z = 11, II: x + 4z = −6
- gesucht: Nachweis, dass x = 2, y = −3, z = −2 eine Lösung ist
- verfahren: Werte in I und II einsetzen
- fehlerquelle: Vorzeichen beim Einsetzen von y = −3 in −y verfehlen

### 2025MgrundlegendAAGLAA12-b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 4 · format Begründung · antwort Text
- gegeben: I: 2x − y − 2z = 11, II: x + 4z = −6, III: 3x − y + 2z = a; Aussage: es gibt ein reelles a, für das das System aus I, II und III unendlich viele Lösungen hat
- gesucht: Beurteilung der Aussage
- verfahren: I + II ergibt 3x − y + 2z = 5, also stimmt III für a = 5 mit I + II überein; für jedes z liefern II und I Werte für x und y, die dann auch III erfüllen
- fehlerquelle: das System für a = 5 als widersprüchlich halten oder für alle a eindeutig lösbar erklären

### 2017MerhoehtAAGLAA111-a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Gleichungssystem 3x1 − 2x2 = 13; x2 + 2x3 = 5; x2 + x3 = 3
- gesucht: Lösungsmenge
- verfahren: Zweite minus dritte Gleichung liefert x3, dann x2, dann x1
- fehlerquelle: Vorzeichen beim Auflösen von 3x1 − 2x2 = 13

### 2017MerhoehtAAGLAA111-b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Zahl|Text
- gegeben: Gleichungssystem 3x1 + 2x2 + x3 = 4; 3x1 + 2x2 = 5; 3x1 + 2x2 + p · x3 = 4 mit p ∈ IR
- gesucht: ein Wert von p mit unendlich vielen Lösungen; Nachweis, dass es keinen Wert von p mit genau einer Lösung gibt
- verfahren: Für p = 1 stimmen erste und dritte Gleichung überein; für p ≠ 1 liefert die Differenz x3 = 0 und damit den Widerspruch 4 = 5 zwischen erster und zweiter Gleichung
- fehlerquelle: nur p = 1 prüfen und den allgemeinen Fall p ≠ 1 nicht ausführen

### 2024MerhoehtAAGLAA122-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: LGS (1) 5x + 10y + 20z = 15, (2) x + y + z = 1; Mischung aus F_x (5 % Orangensaft), F_y (10 %), F_z (20 %) zu 15 %
- gesucht: Interpretation des Gleichungssystems im Sachzusammenhang
- verfahren: (2) als Summe der Anteile gleich 1, (1) als Bilanz der Orangensaftanteile lesen
- fehlerquelle: x, y, z als Prozentzahlen der Orangensaftanteile deuten

### 2024MerhoehtAAGLAA122-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Lösungsmenge des LGS {(−1 + 2s; 2 − 3s; s) | s reell}; Aussage: der Anteil von F_z am neuen Saft ist mindestens doppelt so groß wie der von F_x
- gesucht: Nachweis, dass die Aussage wahr ist
- verfahren: 2x ≤ z in s ausdrücken; die Bedingung y ≥ 0 (Anteil) liefert dieselbe Schranke s ≤ 2/3
- fehlerquelle: die Nichtnegativität von y nicht heranziehen und die Aussage für falsch halten

### 2025MerhoehtAAGLAA121-a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: lineares Gleichungssystem mit Parameter a: I x + 2y = a, II −y + 4z = 2, III (4 − a²) · z = 2 + a
- gesucht: Lösung für a = 0
- verfahren: a = 0 einsetzen, aus III z, aus II y, aus I x
- fehlerquelle: in II das Vorzeichen von y übersehen und y = 4 erhalten

### 2025MerhoehtAAGLAA121-b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: I x + 2y = a, II −y + 4z = 2, III (4 − a²) · z = 2 + a; Aussage: es gibt einen Wert von a ohne Lösung und einen Wert von a mit unendlich vielen Lösungen
- gesucht: Begründung der Aussage
- verfahren: aus II und I folgen y und x eindeutig aus z, die Lösungsanzahl entspricht der von III; 4 − a² faktorisieren: für a = 2 wird III zu 0 = 4, für a = −2 zu 0 = 0
- fehlerquelle: III durch 4 − a² teilen, ohne den Fall a = ±2 zu unterscheiden

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2021-OS-K7a

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
