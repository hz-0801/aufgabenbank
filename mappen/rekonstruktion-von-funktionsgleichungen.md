# Mappe: rekonstruktion-von-funktionsgleichungen

Eintrag: hz-0801/mathe-nachhilfe, katalog/rekonstruktion-von-funktionsgleichungen.md
Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26T16:47:30+02:00, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:43 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Rekonstruktion von Funktionsgleichungen
 3
 4  ### Verortung
 5  Die Steckbriefaufgabe: eine Funktion ist gesucht, ihre Eigenschaften sind gegeben – Punkte, Nullstellen, Symmetrie, Extrem- und Wendepunkte, Tangenten, knickfreie Übergänge, Perioden, Flächeninhalte.  … (gekürzt, 2850 Zeichen)
 6  [GOST] Q1 „Analysis; Lineare Algebra“, GK-Kern (BB S. 23): L4-Zeile „Funktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammenhänge nutzen“ mit dem Inhalt „Rekonstruktion von Funktionsgl … (gekürzt, 1522 Zeichen)
 7  [FOS] Doppelt verankert: Abschlussprofil „ganzrationale Funktionen … nutzen (z. B. in Fragestellungen zu Sachsituationen, die auf Rekonstruktion von Funktionsgleichungen, Extremalprobleme etc. führen) … (gekürzt, 977 Zeichen)
 8  [LS-AA] Qualifikationsphase Kapitel V „Lineare Gleichungssysteme“: 1 Das Gauß-Verfahren · 2 Lösungsmenge linearer Gleichungssysteme · 4 Bestimmen ganzrationaler Funktionen (Zeile 316 der Textfassung)  … (gekürzt, 879 Zeichen)
 9
10  ### Lerneinheiten
11  1. Ansatz und Punktbedingungen – aufstellen ohne Ableitung: den Ansatz nach Grad und Funktionsklasse wählen; durch Symmetrie verkürzen (nur gerade oder nur ungerade Exponenten); Produktansatz aus abge … (gekürzt, 891 Zeichen)
12    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
13  2. Bedingungen mit Ableitung – Wort für Wort übersetzen: Extrempunkt heißt Wert und Ableitung null, Wendepunkt zweite Ableitung null, Tangente Wert und Steigung an der Berührstelle, parallel gleiche S … (gekürzt, 753 Zeichen)
14    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
15  3. Sonderansätze und Modellkritik – Sinus, Kosinus, Parabelprofile: a · sin(b · x) aus Extremstellen und Funktionswerten (Amplitude als halbe Differenz der Extremwerte, Frequenz aus halber Periode ode … (gekürzt, 840 Zeichen)
16    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK
17  Warum drei und nach der Art der Bedingungen: Die Rohdatei trennt selbst zwischen Systemen aus reinen Punkt- und Symmetriebedingungen (die fhr-Kette), Systemen mit Ableitungsbedingungen (die abi-Sachmo … (gekürzt, 867 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
21  Einheit 1: Funktionsgleichung mit Symmetriebedingung über LGS (4) · Funktionsgleichung aus drei Punkten über LGS (3) · Zwei linear eingehende Parameter eines Funktionsterms aus zwei Punkten bestimmen (3) · Ganzrationale Funktion dritten Grades aus drei Nullstellen und einem Punkt rekonstruieren (1) · Geradengleichung aus zwei Punkten bestimmen (1) · Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen (1) · Parameter einer Logarithmusfunktion aus Asymptote und Punkt ermitteln (1) — Nachweis: Lineare Funktion durch zwei Punkte nachweisen (1) — Deutung: Markante Punkte im Sachzusammenhang markieren und ablesen (1). Dazu: Fehler finden (den vollen Ansatz gewählt, obwohl die Symmetrie ihn verkürzt; den y-Achsenabschnitt nicht direkt abgelesen; mit zwei Punkten ein unterbestimmtes System gebaut; den Punkt ungenau aus dem Bild abgelesen) · Begründen (warum die Symmetrie Koeffizienten streicht; warum jede Bedingung genau eine Gleichung liefert).
22  Einheit 2: Funktionsgleichung aus knickfreiem Übergang rekonstruieren (5) · Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren (4) · Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren (3) · Parameter einer Exponentialfunktion aus der Änderungsrate zum Anfangszeitpunkt bestimmen (2) · Funktionsgleichung aus der Ableitung und einer Tangente über die Integrationskonstante rekonstruieren (1) · Funktionsgleichung mit Extremalbedingung über LGS (1) · Ganzrationale Funktion aus Symmetrie und Randbedingungen rekonstruieren (1) · Quadratische Funktion aus senkrechtem Schnitt mit einer Geraden und einer Extrempunktbedingung ermitteln (1) · Zwei Parameter einer Exponentialfunktion aus Funktionswert und Änderungsrate an einer Stelle bestimmen (1). Dazu: Fehler finden (den Hochpunkt nur als Punkt eingesetzt und die Ableitungsbedingung vergessen; knickfrei nur über den Funktionswert angesetzt; die Tangente falsch übersetzt; die Integrationskonstante vergessen; den Steigungswinkel ohne Tangens als Anstieg genommen) · Begründen (warum ein Wortpaar wie Hochpunkt zwei Gleichungen liefert; warum die Zahl der Bedingungen zur Zahl der Koeffizienten passen muss).
23  Einheit 3: Maximum eines Parabelmodells aus einem Zeitraum ohne Durchschnittswachstum und einer Differenzbedingung ermitteln (1) · Parameter einer Sinusfunktion aus Extremstelle und Funktionswert bestimmen (1) · Parameter einer Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten bestimmen (1) · Sinusfunktion mit gleichen Nullstellen und gleichem Flächeninhalt wie ein Graph bestimmen (1) · Steigung einer aus Periode und Extrempunkt rekonstruierten Kosinusfunktion allgemein bestimmen (1) · Zwei Parameter einer Funktion aus einer vorgegebenen Bogenlängenformel und einem Punkt bestimmen (1; Ermessen, siehe Offene Punkte) — Nachweis: Existenz einer quadratischen Funktion zu vier Wert- und Steigungsbedingungen über das überbestimmte Gleichungssystem untersuchen (1; Ermessen, siehe Offene Punkte) · Parabel ohne lineares Glied aus dem knickfreien Übergang begründen und Parameter aus einem Flächeninhalt berechnen (1) · Unmöglichkeit einer einzigen Parabel für ein knickfreies Profil mit zwei waagerechten Tangenten begründen (1) · Unmöglichkeit waagerechter Tangenten an den Rändern über die Ableitung mit Parametern begründen (1). Dazu: Fehler finden (die halbe Periode als ganze genommen; die Amplitude als ganze Differenz der Extremwerte angesetzt; die Fläche nicht in Längeneinheiten des Modells umgerechnet; die Unmöglichkeit nur mit einem Punktargument begründet) · Begründen (warum der Abstand aufeinanderfolgender Extremstellen die halbe Periode ist; warum eine Parabel keinen Krümmungswechsel hat).
24  Zählung: 9 + 9 + 10 = 28 Haupttypen, 16 + 19 + 10 = 45 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: Heft 2017-be-gk, Pool 2017 erhöht Teil B; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2018 erhöht und 2017 grundlegend Teil B CAS, Berliner CAS-Heft 2018 GK) samt der Typumbenennung des Abgleichlaufs 27).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Lineare Gleichungssysteme lösen: Einsetzungs- und Additionsverfahren, bis vier Gleichungen – das Lösungswerkzeug aller Einheiten. Sek-I-Thema lineare-gleichungssysteme.md. [FOS „Lösen von linearen Gleichungssystemen mit bis zu vier Variablen/Gleichungen“; fhr 2019-C-2a]
29  - Lineare Funktionen: Steigung aus zwei Punkten, y-Achsenabschnitt – die Geradenzeilen in Einheit eins und die Tangentenbedingungen in Einheit zwei. Sek-I-Thema lineare-funktionen.md. [GOST BE Einführungsphase „ermitteln die Funktionsgleichungen von linearen … Funktionen aus gegebenen Punkten“]
30  - Parabelformen kennen: allgemeine Form, Scheitelform, Produktform – die Ansatzwahl in Einheit eins. Sek-I-Thema quadratische-funktionen.md. [GOST Eingangsvoraussetzung L4 „Darstellungen quadratischer Funktionen, u. a. als Produkt von Linearfaktoren“]
31  - Symmetrie am Term erkennen: gerade und ungerade Exponenten – die Ansatzverkürzung in Einheit eins. Sek-II-Nachbarthema funktionsklassen-und-eigenschaften.md Einheit vier. [FOS „Symmetrie bezüglich y-Achse und Koordinatenursprung“; fhr 2021-A-2a]
32  - Ableitungsregeln anwenden – die Steigungsbedingungen in Einheit zwei. Sek-II-Nachbarthema ableitungsregeln.md. [Klarstellung Geometrie sinngemäß: Blatt-0-Fertigkeit aus dem Sek-II-Nachbarthema derselben Stufe]
33  - Sinus- und Kosinusgraph mit Periode und Amplitude – die Ansätze in Einheit drei. Sek-I-Thema trigonometrische-funktionen.md. [GOST Eingangsvoraussetzung L4 „charakterisieren und interpretieren die Verläufe der Funktionen f(x) = sin(x), f(x) = cos(x) …“]
34  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
35  - „Wie viele Unbekannte, wie viele Bedingungen?“ – zu Aufgabentexten die Koeffizienten des Ansatzes und die gegebenen Bedingungen zählen und ankreuzen, ob es passt; nichts rechnen. Vor Einheit eins. [Rohdatei-Fehlerquelle „unterbestimmtes System“, fhr 2023-A-2a]
36  - „Welche Gleichung steckt in diesem Wort?“ – zu Begriffen (Hochpunkt, Nullstelle, Tangente, knickfrei, parallel) ankreuzen, wie viele Gleichungen sie liefern; nichts rechnen. Vor Einheit zwei. [Rohdatei-Fehlerquelle „Hochpunkt nur als Punkt eingesetzt“, fhr 2025-A-2a; abi 2023-bebb-gk-B2.2k]
37  - „Wie weit bis zum nächsten Hochpunkt?“ – an Sinusgraphen Periode und Amplitude ablesen und ankreuzen, welcher Abstand die halbe und welcher die ganze Periode ist; nichts rechnen. Vor Einheit drei. [Rohdatei-Fehlerquelle „Abstand der Extremstellen als ganze Periode“, iqb 2022MerhoehtBAnalysisWTR1-2a]
38
39  ### Merkkasten
40  Einheit 1 (Ansatz und Punktbedingungen):
41      Ansatz wählen: Grad n hat n + 1 Koeffizienten; Symmetrie verkürzt – achsensymmetrisch nur gerade, punktsymmetrisch nur ungerade Exponenten; abgelesene Nullstellen erlauben den Produktansatz mit Streckfaktor.
42      Jede Bedingung eine Gleichung: Punkte einsetzen, das LGS lösen; den y-Achsenabschnitt sofort ablesen.
43        Quadratisch durch P(0 | −10), Q(1 | 6), R(4 | 6): c = −10 direkt, dann zwei Gleichungen für a und b.
44      Sonderansätze: Gerade aus zwei Punkten (Steigung als Differenzenquotient); a · bˣ (a aus dem Wert an der Stelle null); ln(x − a) + b (a aus der senkrechten Asymptote).
45      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.2] „Rekonstruktion von Funktionsgleichungen aus graphischen Darstellungen bzw. Funktionseigenschaften“; Teil-A-Belege 2022MgrundlegendAAnalysis12-a, 2026MerhoehtAAnalysis13-b.
46      Formelsammlung: keine – Ansätze stehen nicht in der Formelsammlung – [FS] offen
47  Quelle: eigene Formulierung nach [FOS] „Rekonstruktion aus gegebenen Punkten“ und [GOST-OHiMi 2.2]; Zahlenbeispiel aus dem fhr-Heft (2026-C-2c, wörtlich die Punkte); [LS-AA QP V 4].
48
49  Einheit 2 (Bedingungen mit Ableitung):
50      Übersetzungstabelle: Punkt → Funktionswert; Nullstelle → Wert null; Extrempunkt → Wert und Ableitung null; Wendepunkt → zweite Ableitung null; Tangente → Wert und Steigung an der Berührstelle; parallel → gleiche Steigung; senkrecht → negativer Kehrwert; knickfrei → gleicher Wert und gleiche Steigung; Steigungswinkel → Anstieg über den Tangens.
51        Hochpunkt H(5 | 220): zwei Gleichungen, k(5) = 220 und k'(5) = 0.
52      Rückwärts aus der Ableitung: f durch Integration mit Konstante ansetzen, die Konstante aus einem Punkt.
53      Zählen: erst die Gleichungen sammeln, dann lösen – so viele Gleichungen wie Koeffizienten.
54      Auswendig (Teil A): die Übersetzungstabelle – [GOST-OHiMi 2.2] „Rekonstruktion … aus Funktionseigenschaften“; Teil-A-Belege 2020-be-gk-A1.2a, 2023-bebb-lk-A1.4b.
55      Formelsammlung: keine – die Ableitungsregeln liegen bei ableitungsregeln.md – [FS] offen
56  Quelle: eigene Formulierung nach [FOS] „Rekonstruktion unter Ausnutzung weiterer Eigenschaften, z. B. Symmetrie, Anstieg, Extrem-, Wende- und Sattelstellen“; Zahlenbeispiel aus dem Landesheft (2023-bebb-gk-B2.2k, wörtlich der Hochpunkt); [LS-AA QP V 4].
57
58  Einheit 3 (Sonderansätze und Modellkritik):
59      a · sin(b · x): die Amplitude ist die halbe Differenz von Hoch- und Tiefwert; b kommt aus der Periode p über b = zwei Pi durch p; der Abstand aufeinanderfolgender Extremstellen ist die halbe Periode, von der Nullstelle zur Extremstelle eine Viertelperiode.
60        E₁(−2 | −1) und E₂(2 | 3): Amplitude 2, halbe Periode 4, also b = π/4.
61      Fläche als Bedingung: der Streckfaktor kommt aus dem Integral über eine Halbwelle.
62      Modellkritik: eine Parabel hat genau einen Scheitel und wechselt die Krümmung nicht – zwei waagerechte Tangenten oder ein Krümmungswechsel schließen sie aus; waagerechte Tangente auf der y-Achse erzwingt die Form ohne lineares Glied.
63      Auswendig (Teil A): „a · sin(b · x)“ und „Modellkritik“ – [GOST-OHiMi 2.2] Rekonstruktion aus Funktionseigenschaften; Teil-A-Belege 2025MerhoehtAAnalysis13-b, 2023MerhoehtAAnalysis22.
64      Formelsammlung: keine – Periodenformeln stehen nicht im Teil 1 der Formelsammlung – [FS] offen
65  Quelle: eigene Formulierung nach [GOST Q1 L4] „Sinus- und Kosinusfunktionen: Einfluss der Parameter auf den Verlauf der Funktionsgraphen“ (Deutungsrichtung umgekehrt: vom Verlauf zu den Parametern); Zahlenbeispiel aus dem Pool (2022MerhoehtBAnalysisWTR1-2a, wörtlich die Extrempunkte); kein Lehrwerksbeleg (Ermessen – der Fahrplan führt keine trigonometrische Steckbriefeinheit).
66
67  ### Typische Fehler
68  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 35 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nur, wo die Kataloge das Muster stützen.
69  - Ansatz zu groß gewählt: den vollen Ansatz trotz Symmetrie, mit zwei Punkten ein unterbestimmtes System, fünf Koeffizienten beim achsensymmetrischen vierten Grad. [fhr 2026-B-2a, 2025-C-2d, 2023-A-2a, 2021-A-2a, 2019-C-2a]
70  - Ablesbares nicht abgelesen: den y-Achsenabschnitt als LGS-Unbekannte mitgeschleppt statt aus dem Punkt auf der y-Achse zu nehmen. [fhr 2026-C-2c, 2023-C-2b]
71  - Wortbedingungen halbiert: den Hoch- oder Scheitelpunkt nur als Punkt eingesetzt und die Ableitungsbedingung vergessen, knickfrei nur über den Funktionswert angesetzt. [fhr 2025-A-2a; abi 2023-bebb-gk-B2.2k, 2021-be-gk-B2.1k, 2022-bebb-gk-B2.2k, 2018-be-gk-B1.1e]
72  - Tangente und Gerade falsch übersetzt: den Funktionswert an der Berührstelle ohne den Achsenabschnitt der Tangente, Parallelität als gleicher y-Achsenabschnitt, den rechten Winkel ohne negativen Kehrwert, beim senkrechten Anstieg das Vorzeichen vergessen, die Integrationskonstante weggelassen. [abi 2020-be-gk-A1.2a, 2022-bebb-lk-B2.1i, 2023-bebb-lk-A1.4b; iqb 2020MgrundlegendAAnalysis12, 2022MerhoehtAAnalysis2; fhr 2022-C-2b]
73  - Wert statt Ableitung: die Steigungsbedingung in die Funktion statt in die Ableitung eingesetzt, die Änderungsrate als Funktionswert angesetzt, den Steigungswinkel ohne Tangens übernommen. [abi 2019-be-gk-B2.1c, 2026-bb-ea-B2.1g, 2018-bb-ea-B2.2h]
74  - Trigonometrische Parameter verrechnet: den Abstand aufeinanderfolgender Extremstellen als ganze Periode, die Viertelperiode als Periode, die Amplitude als ganze Differenz oder gleich dem Parameter der Aufgabe, die Kosinuswerte an null und Pi halbe verwechselt. [iqb 2022MerhoehtBAnalysisWTR1-2a, 2022MgrundlegendBAnalysisWTR1-1g, 2018MerhoehtBAnalysisWTR1-1g, 2023MerhoehtAAnalysis22, 2025MerhoehtAAnalysis13-b; abi 2025-bebb-lk-A1.2b]
75  - Am Bild vorbeigelesen: den Punkt ungenau abgelesen und mit dem Näherungswert gerechnet, den Verschiebungsparameter mit falschem Vorzeichen aus dem Term genommen, trotz ablesbarer Nullstellen den allgemeinen Ansatz gewählt. [iqb 2022MgrundlegendAAnalysis12-a, 2026MerhoehtAAnalysis13-b, 2018MerhoehtBAnalysisWTR1-1a]
76  - Maßstab und Modell: mit Durchmessern statt Radien angesetzt, die Fläche nicht in Flächeneinheiten des Koordinatensystems umgerechnet, die Höhe als Funktionswert statt als Abstand zweier Graphen gedeutet, die Scheitelstelle aus der falschen Zeitraummitte. [fhr 2020-C-2a; abi 2023-bebb-lk-B2.1m, 2018-be-gk-B1.1e, 2026-bb-ea-B2.1i]
77  - Begründung zu dünn: die Unmöglichkeit nur mit „passt nicht durch die Punkte“ statt über Scheitel oder Krümmung, den Geradennachweis mit nur einem Punkt. [abi 2023-bebb-lk-B2.1l, 2022-bebb-gk-B2.2g; FD Vollrath/Weigand zum Beweisbedürfnis am Beispiel]
78
79  ### Für schwache Schüler
80  Mindeststoff (GK-Kern Q1 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: „Rekonstruktion von Funktionsgleichungen“ steht in der L4-Planzeile der Q1 – Einheit 1 vollständig und die Übersetzungstabelle der Einheit 2 an ganzrationalen Funktionen und der e-Funktion; ohne Hilfsmittel (Anlage OHiMi 2.2, Prüfungsteil A) die Rekonstruktion „aus graphischen Darstellungen bzw. Funktionseigenschaften“ – der Kern beider Kästen. RLP FOS (fhr) [FOS Pflichtthema 1 und 2]: Parabelgleichungen aus Punkten mit LGS, ganzrationale Gleichungen bis zum fünften Grad aus Punkten, Symmetrie, Anstieg und Extremstellen, LGS bis vier Gleichungen – Einheit 1 vollständig, Einheit 2 als Extremalbedingung. Niveaustufe H der E-Phase [RLP H, LS-AA]: die Gerade aus zwei Punkten und die Parabel aus drei Punkten als Sek-I-Vorlauf der Einheit 1. Vorrat: die trigonometrischen und logarithmischen Ansätze und die Modellkritik der Einheit 3 (GK-Schüler nach dem Niveau der Rohdatei, fhr gar nicht), die Integrationskonstanten-Zeile der Einheit 2. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog verlangt das Aufstellen linearer und quadratischer Funktionen aus Bedingungen – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
81  Grundvorstellung (Blatt 0) [GOST-OHiMi 2.2, GOST BE Einführungsphase, MO]: Der Steckbrief: die Funktion ist die Gesuchte, jede Eigenschaft ein Hinweis, jeder Hinweis eine Gleichung. „Hier ist ein gezeichneter Graph mit Gitter, kein Term. Sammle mit dem Finger alle Hinweise, die du ablesen kannst: wo er die Achsen schneidet, wo er einen Hochpunkt hat, ob er symmetrisch ist. Zähle die Hinweise – und sage, wie viele Zahlen im gesuchten Term frei sind. Reichen deine Hinweise? Welcher Hinweis liefert zwei Gleichungen auf einmal?“ Wer sofort einen Term rät oder Bedingungen doppelt zählt, braucht das vor jeder Rechnung: erst sammeln und zählen, dann übersetzen, zuletzt lösen. Verständnis, nicht Verfahren; amtlich in der Vorstellung (OHiMi „aus graphischen Darstellungen“, BE „ermitteln die Funktionsgleichungen … aus gegebenen Punkten“), Ermessen in der Aufgabenform. [MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „unterbestimmtes System“, fhr 2023-A-2a; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
82  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, FOS, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
83  - Ansatz und Punktbedingungen (Einheit 1): „Wie viele Unbekannte, wie viele Bedingungen?“ ankreuzen (Vorstufe, Grundvorstellung) → die Gerade aus zwei Punkten bestimmen (Grundfall, viermal; fhr 2022-C-2b) und eine vorgegebene Gerade durch zwei Punkte nachweisen (abi 2022-bebb-gk-B2.2g) → die Parabel aus drei Punkten über das LGS, den y-Achsenabschnitt zuerst (fhr 2019-C-2a, 2023-C-2b, 2026-C-2c) → den Ansatz durch Symmetrie verkürzen: quadratisch, dritten und vierten Grades (fhr 2020-C-2a, 2023-A-2a, 2026-B-2a, 2025-C-2d) → den Produktansatz aus abgelesenen Nullstellen mit Streckfaktor (iqb 2018MerhoehtBAnalysisWTR1-1a) → Sonderansätze: Exponentialfunktion aus zwei Punkten, Logarithmusfunktion aus Asymptote und Punkt, Linearkombination aus zwei Punkten (iqb 2022MgrundlegendAAnalysis12-a, 2026MerhoehtAAnalysis13-b, 2025MerhoehtAAnalysis13-b; abi 2025-bebb-lk-A1.2b) → markante Punkte im Sachzusammenhang ablesen und notieren (fhr 2025-C-2d) → Prüfungshöhe: der achsensymmetrische vierte Grad mit Tiefpunkt (fhr 2021-A-2a, Niveau III); fhr-Zielmarke: die symmetrieverkürzte Parabel im Sachmodell (fhr 2020-C-2a, Niveau II).
84  - Bedingungen mit Ableitung (Einheit 2): „Welche Gleichung steckt in diesem Wort?“ ankreuzen (Vorstufe) → die Extremalbedingung ergänzen: Wert und Ableitung null (Grundfall, viermal; fhr 2025-A-2a; abi 2021-be-gk-B2.1k) → dritten Grades aus Wert- und Steigungsbedingungen: Wachstum, Heizung, Nullstelle mit Steigung (abi 2019-be-gk-B2.1c, 2023-bebb-gk-B2.2k, 2022-bebb-lk-B2.1i) → quadratisch aus Tangente oder Ursprung und Bedingungen (abi 2020-be-gk-A1.2a; iqb 2020MgrundlegendAAnalysis12, 2022MerhoehtAAnalysis2) → den knickfreien Übergang doppelt übersetzen: Wert und Steigung (abi 2018-be-gk-B1.1e, 2022-bebb-gk-B2.2k) → Symmetrie und Randwinkel verbinden (abi 2018-bb-ea-B2.2h) → aus der Ableitung zurück: Integration mit Konstante, Konstante aus dem Berührpunkt (abi 2023-bebb-lk-A1.4b) → die Änderungsrate zum Anfangszeitpunkt als Ableitungsgleichung (abi 2026-bb-ea-B2.1g) → Prüfungshöhe: der Brückenquerschnitt mit Steigungswinkeln über den Tangens (abi 2018-bb-ea-B2.2h, Niveau II) und der senkrechte Schnitt mit Extrempunktbedingung (iqb 2022MerhoehtAAnalysis2, Niveau III); fhr-Zielmarke: die Extremalbedingung im Wurfmodell (fhr 2025-A-2a, Niveau II).
85  - Sonderansätze und Modellkritik (Einheit 3): „Wie weit bis zum nächsten Hochpunkt?“ ankreuzen (Vorstufe) → die Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten: Amplitude und halbe Periode (Grundfall, viermal; iqb 2022MerhoehtBAnalysisWTR1-2a) → aus Extremstelle und Funktionswert: Viertelperiode (iqb 2022MgrundlegendBAnalysisWTR1-1g) → mit Flächenbedingung: der Streckfaktor aus dem Integral (iqb 2018MerhoehtBAnalysisWTR1-1g) → die Modellparabel über die Symmetrie eines Zeitraums und eine Differenzbedingung (abi 2026-bb-ea-B2.1i) → die Ansatzform begründen: Parabel ohne lineares Glied, Parameter aus dem Flächeninhalt mit Maßstab (abi 2023-bebb-lk-B2.1m) → Prüfungshöhe: die Unmöglichkeit einer einzigen Parabel über Scheitel oder Krümmungswechsel (abi 2023-bebb-lk-B2.1l, Niveau II) und die allgemeine Kosinusrekonstruktion mit Parameter (iqb 2023MerhoehtAAnalysis22, Niveau III); fhr-Zielmarke: keine – der RLP FOS kennt weder trigonometrische Ansätze noch Modellkritik.
86
87  ### Prüfungsform (fhr / abi / iqb)
88  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md. Für fhr ist der Pool keine Vorgabe: dort gelten RLP FOS 2019 und der fhr-Katalog. Die Rohdatei zählt 45 Zeilen mit 28 Haupttypen (fhr 10 Zeilen, 5 Typen; abi 18 Zeilen, 12 Typen; iqb 17 Zeilen, 15 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; das Thema ist selbst der Gegenstand und führt keine Gegenstandsklassen, die Typnamen stehen ohne Präfix).
89  fhr (10 Zeilen; fhr-Thema „Funktionsgleichung bestimmen“) [FOS, fhr-Katalog]: Funktionsgleichung mit Symmetriebedingung über LGS (4, E1) · Funktionsgleichung aus drei Punkten über LGS (3, E1) · je 1: Funktionsgleichung mit Extremalbedingung über LGS (E2) · Geradengleichung aus zwei Punkten bestimmen (E1) · Markante Punkte im Sachzusammenhang markieren und ablesen (E1). Muster: Die Rekonstruktion ist die Standard-Eröffnung der Sachaufgabe im Wahlteil – ein Bauwerk oder Gerät wird durch eine quadratische oder ganzrationale Funktion modelliert, deren Gleichung zuerst zu bestimmen ist, mit Kontrollergebnis für den Weiterbau (See 2019-C-2a, Lautsprecher 2020-C-2a, Bootsrumpf 2021-A-2a, Hoftor 2023-C-2b, Ballwurf 2025-A-2a, Tunnel 2025-C-2d, Fahrradanhänger 2026-B-2a, Zaunprofil 2026-C-2c), dazu die innermathematische Variante (2023-A-2a) und die Gerade als Nebenrechnung (2022-C-2b). Vier bis sieben Punkte je Zeile. Niveau II 9, III 1 (2021-A-2a, vierter Grad symmetrisch mit Tiefpunkt).
90  abi (18 Zeilen, 12 Typen; Landeshefte be-gk, bb-ea, bebb-gk, bebb-lk 2017–2026, davon 1 aus der Berliner CAS-Fassung be-gk 2018) [abi-Katalog]: Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren (4, E2) · Funktionsgleichung aus knickfreiem Übergang rekonstruieren (3, E2) · Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren (2, E2) · je 1: Existenz einer quadratischen Funktion zu vier Wert- und Steigungsbedingungen über das überbestimmte Gleichungssystem untersuchen (E3) · Funktionsgleichung aus der Ableitung und einer Tangente über die Integrationskonstante rekonstruieren (E2) · Ganzrationale Funktion aus Symmetrie und Randbedingungen rekonstruieren (E2) · Lineare Funktion durch zwei Punkte nachweisen (E1) · Maximum eines Parabelmodells aus einem Zeitraum ohne Durchschnittswachstum und einer Differenzbedingung ermitteln (E3) · Parabel ohne lineares Glied aus dem knickfreien Übergang begründen und Parameter aus einem Flächeninhalt berechnen (E3) · Parameter einer Exponentialfunktion aus der Änderungsrate zum Anfangszeitpunkt bestimmen (E2) · Zwei linear eingehende Parameter eines Funktionsterms aus zwei Punkten bestimmen (E1) · Unmöglichkeit einer einzigen Parabel für ein knickfreies Profil mit zwei waagerechten Tangenten begründen (E3). Muster: In Teil B liefert die Rekonstruktion das zweite Modell einer laufenden Sachaufgabe – das veränderte Brückenteil der Holzeisenbahn dritten Grades mit Extrempunkten in beiden Ecken (2017-be-gk-B1.1f), die Parabel, die die Dachkante in zwei Punkten berühren soll – vier Bedingungen für drei Koeffizienten, die vierte widerlegt die Existenz (2017-be-gk-B1.2f, Niveau III) –, Flugbahn an der Skisprunganlage (2018-be-gk-B1.1e; in der CAS-Fassung mit Landepunkt und Schnittwinkel am Aufsprunghang in einer Teilaufgabe, elf Punkte, 2018-be-gk-cas-B1.1f), Gartenbrücke (2018-bb-ea-B2.2h), Baum B (2019-be-gk-B2.1c), neue Parabelbegrenzung (2021-be-gk-B2.1k), Bauteilkurve und Gerade (2022-bebb-gk-B2.2k und 2022-bebb-gk-B2.2g), Heizungsstart (2023-bebb-gk-B2.2k), Dammprofil mit Begründung und Maßstabsfläche (2023-bebb-lk-B2.1l/m), Weltbevölkerungsmodelle (2026-bb-ea-B2.1g/i), dritter Grad aus vier Bedingungen (2022-bebb-lk-B2.1i); Teil A prüft die Kurzformen (2020-be-gk-A1.2a, 2023-bebb-lk-A1.4b, 2025-bebb-lk-A1.2b). Zwei der 18 Zeilen sind wortgleiche Pooldubletten (2020-be-gk-A1.2a, 2025-bebb-lk-A1.2b), keine abgewandelt. Niveau I 2, II 12, III 4.
91  iqb (17 Zeilen, 15 Typen; Pool 2017–2026, grundlegend 4 und erhöht 13 Zeilen, Teil A 6 und Teil B 11 Zeilen, davon 5 CAS) [iqb-Katalog]: Zwei linear eingehende Parameter eines Funktionsterms aus zwei Punkten bestimmen (2, E1) · Funktionsgleichung aus knickfreiem Übergang rekonstruieren (2, E2) · je 1: Ganzrationale Funktion dritten Grades aus drei Nullstellen und einem Punkt rekonstruieren (E1) · Parameter einer Exponentialfunktion aus der Änderungsrate zum Anfangszeitpunkt bestimmen (E2) · Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen (E1) · Parameter einer Logarithmusfunktion aus Asymptote und Punkt ermitteln (E1) · Parameter einer Sinusfunktion aus Extremstelle und Funktionswert bestimmen (E3) · Parameter einer Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten bestimmen (E3) · Quadratische Funktion aus senkrechtem Schnitt mit einer Geraden und einer Extrempunktbedingung ermitteln (E2) · Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren (E2) · Sinusfunktion mit gleichen Nullstellen und gleichem Flächeninhalt wie ein Graph bestimmen (E3) · Steigung einer aus Periode und Extrempunkt rekonstruierten Kosinusfunktion allgemein bestimmen (E3) · Unmöglichkeit waagerechter Tangenten an den Rändern über die Ableitung mit Parametern begründen (E3) · Zwei Parameter einer Exponentialfunktion aus Funktionswert und Änderungsrate an einer Stelle bestimmen (E2) · Zwei Parameter einer Funktion aus einer vorgegebenen Bogenlängenformel und einem Punkt bestimmen (E3). Muster: Teil A stellt die Rekonstruktion als eigenständige Kurzaufgabe mit drei bis fünf Punkten, je einen Ansatz pro Aufgabe (Exponentialfunktion am Graphen 2022MgrundlegendAAnalysis12-a, Parabel mit Tangente 2020MgrundlegendAAnalysis12, rechter Winkel und Extrempunkt 2022MerhoehtAAnalysis2, allgemeiner Kosinus 2023MerhoehtAAnalysis22, Linearkombination 2025MerhoehtAAnalysis13-b, Logarithmus mit Asymptote 2026MerhoehtAAnalysis13-b); Teil B hängt sie an laufende Kurven (dritter Grad aus Nullstellen und die Sinus-Näherung mit Flächenbedingung 2018MerhoehtBAnalysisWTR1-1a/1g, Sinus-Näherung am Wendepunkt 2022MgrundlegendBAnalysisWTR1-1g, Extrempunkt-Steckbrief 2022MerhoehtBAnalysisWTR1-2a; aus den Stapeln 2017 die Profillinie a − c · e^(−x²) mit zwei linear eingehenden Parametern und die Unmöglichkeit waagerechter Randtangenten für jede Parameterwahl 2017MerhoehtBAnalysisWTR3-2h, 2017MerhoehtBAnalysisWTR3-2i, und das Likörglas aus zwei Parabeln mit knickfreiem Übergang an der Wendestelle 2017MerhoehtBAnalysisCAS2-4, Niveau III; aus den CAS-Stapeln 2017 grundlegend und 2018 erhöht die Abkühlkurve 23 + b · e^(c · t) aus Temperatur und momentaner Änderungsrate zu Beginn des Abkühlens über ein Gleichungssystem 2017MgrundlegendBAnalysisCAS-1e, der knickfreie Übergang einer Wurfparabel in eine gebrochenrationale Flugkurve allein aus gleichem Wert und gleicher Steigung 2018MerhoehtBAnalysisCAS1-3a, der Parameter k aus der Gleichheit zweier momentaner Änderungsraten beim Glukosewert 2018MerhoehtBAnalysisCAS2-2f und das Hängebrückenseil aus vorgegebener Längenformel und Befestigungspunkt, die Längengleichung am Rechner gelöst, 2018MerhoehtBAnalysisCAS3-2e). Zwei Poolzeilen kehren wortgleich in Landesheften wieder (2020MgrundlegendAAnalysis12 → 2020-be-gk-A1.2a, 2025MerhoehtAAnalysis13-b → 2025-bebb-lk-A1.2b). Niveau I 1, II 12, III 4.
92  Zielmarke: Einheit 1 – fhr: die symmetrieverkürzte Parabel im Sachmodell (2020-C-2a, Niveau II); abi: die Linearkombination aus zwei Punkten (2025-bebb-lk-A1.2b, Niveau II); iqb: der Logarithmus aus Asymptote und Punkt (2026MerhoehtAAnalysis13-b, Niveau II). Einheit 2 – fhr: die Extremalbedingung im Wurfmodell (2025-A-2a, Niveau II); abi: der knickfreie Übergang an der Skisprunganlage (2018-be-gk-B1.1e, Niveau II); iqb: der senkrechte Schnitt mit Extrempunktbedingung (2022MerhoehtAAnalysis2, Niveau III). Einheit 3 – fhr: keine; abi: die Unmöglichkeit einer einzigen Parabel (2023-bebb-lk-B2.1l, Niveau II) und die Existenzfrage am überbestimmten System (2017-be-gk-B1.2f, Niveau III); iqb: die allgemeine Kosinusrekonstruktion (2023MerhoehtAAnalysis22, Niveau III).
````

## 2 Originale (42)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2019-C-2a (fhr-katalog.csv)

jahr 2019 · papier C · punkte 6 · format Rechnung · antwort Term
- gegeben: die Uferlinie eines Sees wird durch die Graphen zweier ganzrationaler Funktionen beschrieben, eine Längeneinheit entspricht 2 km; der nördliche Bereich liegt auf Gf mit f(x) = x^3 − (1/2)x^2 − 4x − 2, der südliche auf Gg; von der quadratischen Funktion g ist bekannt, dass ihr Graph die y-Achse bei y = −4 schneidet und die Punkte P(−1; −5) und Q(−2; −4) auf Gg liegen; zur Kontrolle ist g(x) = x^2 + 2x − 4 angegeben
- gesucht: Funktionsgleichung von g
- verfahren: den allgemeinen Ansatz g(x) = ax^2 + bx + c aufstellen, die drei bekannten Punkte einsetzen und das lineare Gleichungssystem lösen
- fehlerquelle: den y-Achsenschnitt nicht als dritte Bedingung nutzen und mit zwei Gleichungen für drei Unbekannte enden

### 2020-C-2a (fhr-katalog.csv)

jahr 2020 · papier C · punkte 4 · format Rechnung · antwort Term
- gegeben: ein gewölbter Lautsprecher hat eine Höhe von 18 cm, einen maximalen Durchmesser von 10 cm und an Ober- und Unterseite je 6 cm Durchmesser; die Mantelfläche entsteht durch Rotation des Graphen Gf um die x-Achse; eine Einheit im Koordinatensystem entspricht einem Zentimeter; Gf ist der zur y-Achse symmetrische Graph einer quadratischen Funktion; zur Kontrolle ist f(x) = −(2/81)x^2 + 5 angegeben
- gesucht: Funktionsgleichung von f
- verfahren: wegen der Achsensymmetrie den Ansatz f(x) = ax^2 + b wählen, aus dem maximalen Durchmesser f(0) = 5 und aus dem Randdurchmesser f(9) = 3 aufstellen und das Gleichungssystem nach a und b lösen
- fehlerquelle: mit den Durchmessern 10 und 6 statt mit den Radien 5 und 3 ansetzen

### 2021-A-2a (fhr-katalog.csv)

jahr 2021 · papier A · punkte 7 · format Rechnung · antwort Term
- gegeben: der untere Teil des Querschnitts wird durch den Graphen Gf einer Funktion vierten Grades beschrieben; Gf ist achsensymmetrisch zur y-Achse und verläuft durch P(0; −1,5) sowie den Tiefpunkt T(1; −2); als Kontrolle ist f(x) = 0,5x^4 − x^2 − 1,5 genannt
- gesucht: eine zugehörige Funktionsgleichung für f
- verfahren: wegen der Achsensymmetrie den Ansatz mit nur geraden Exponenten aufstellen, die Ableitung bilden und aus dem Punkt P, dem Funktionswert im Tiefpunkt und der Bedingung, dass die Ableitung dort null ist, ein Gleichungssystem für die drei Koeffizienten aufstellen und lösen
- fehlerquelle: den allgemeinen Ansatz vierten Grades mit fünf Koeffizienten wählen und die Achsensymmetrie nicht als Vereinfachung nutzen

### 2023-C-2b (fhr-katalog.csv)

jahr 2023 · papier C · punkte 7 · format Rechnung · antwort Term
- gegeben: Herr Meier will ein Hoftor nachbauen und hat dazu eine Projektskizze angefertigt; die Parabelbögen und Rahmenteile werden aus Metallprofilen gefertigt, deren Dicke vernachlässigt wird, die Trennung der beiden Torhälften bleibt unberücksichtigt; eine Einheit im Koordinatensystem entspricht einem Meter am Tor; der obere Parabelbogen Gf gehört zu f(x) = −0,15x^2 + 1,2x − 0,6; für den unteren Parabelbogen Gg sind die Punkte P(0; 3), Q(4; 0,6) und R(8; 3) festgelegt; zur Kontrolle ist g(x) = 0,15x^2 − 1,2x + 3 angegeben
- gesucht: Gleichung der quadratischen Funktion g aus den drei Punkten
- verfahren: den Ansatz g(x) = ax^2 + bx + c aufstellen, die drei Punkte einsetzen und das lineare Gleichungssystem lösen
- fehlerquelle: den Punkt P(0; 3) nicht zuerst nutzen und c unnötig mitschleppen

### 2025-A-2a (fhr-katalog.csv)

jahr 2025 · papier A · punkte 6 · format Rechnung · antwort Term
- gegeben: die Flugbahn des Balls wird durch eine quadratische Funktion f beschrieben; Abwurf im Punkt A(0; 2), Hochpunkt der Flugbahn in B(3; 3,8); eine Einheit im Koordinatensystem entspricht einem Meter, der Hallenboden liegt auf der x-Achse
- gesucht: Funktionsgleichung von f
- verfahren: f(x) = ax^2 + bx + c ansetzen, A und B einsetzen, die Bedingung f'(3) = 0 ergänzen und das LGS lösen
- fehlerquelle: den Hochpunkt nur als Punkt einsetzen und die Bedingung f'(3) = 0 vergessen

### 2025-C-2d (fhr-katalog.csv)

jahr 2025 · papier C · punkte 4 · format Eintragen|Rechnung · antwort Zahl|Term
- gegeben: für die weitere Nutzung wird ein zusätzlicher Belüftungstunnel benötigt; er soll den Querschnitt einer achsensymmetrischen quadratischen Funktion g bekommen und dieselbe Höhe 1,2 m und Breite 1 m wie der historische Tunnel erhalten; Abbildung 2 zeigt das Koordinatensystem
- gesucht: drei markante Punkte des neuen Tunnelquerschnitts mit ihren Koordinaten|Gleichung einer passenden Funktion g durch alle drei Punkte
- verfahren: die beiden Randpunkte auf der x-Achse und den höchsten Punkt auf der y-Achse markieren, aus der Achsensymmetrie b = 0 setzen, mit dem höchsten Punkt c bestimmen und mit einem Randpunkt a berechnen
- fehlerquelle: den vollständigen Ansatz mit b ungleich null aufstellen und die Symmetrie nicht nutzen

### 2026-B-2a (fhr-katalog.csv)

jahr 2026 · papier B · punkte 5 · format Rechnung · antwort Term
- gegeben: eine Schul-AG entwickelt einen Fahrradanhänger in Wohnwagenform; die obere gekrümmte Begrenzung der Seitenwand wird durch Gf beschrieben, die untere durch die x-Achse im zweiten Quadranten, nach rechts begrenzt eine Senkrechte durch B; eine Einheit im Koordinatensystem entspricht 0,5 m in der Wirklichkeit; f ist ganzrational dritten Grades, Gf liegt punktsymmetrisch zum Koordinatenursprung und verläuft durch C(−2; 2) und D(−4; 1,6)
- gesucht: eine passende Funktionsgleichung für f
- verfahren: aus der Punktsymmetrie den Ansatz f(x) = ax^3 + bx aufstellen, beide Punkte einsetzen und das entstehende LGS lösen
- fehlerquelle: den vollständigen Ansatz mit vier Koeffizienten wählen, statt ihn über die Punktsymmetrie zu verkürzen

### 2026-C-2c (fhr-katalog.csv)

jahr 2026 · papier C · punkte 6 · format Rechnung · antwort Term
- gegeben: Graph Gg einer quadratischen Funktion g durch P(0; −10), Q(1; 6) und R(4; 6)
- gesucht: eine Funktionsgleichung für g
- verfahren: allgemeinen Ansatz g(x) = ax^2 + bx + c aufstellen, die drei Punkte einsetzen und das lineare Gleichungssystem lösen; alternativ über die Scheitelpunktform
- fehlerquelle: das absolute Glied nicht direkt aus P(0; −10) ablesen und das LGS unnötig aufblähen

### 2023-A-2a (fhr-katalog.csv)

jahr 2023 · papier A · punkte 5 · format Rechnung · antwort Term
- gegeben: der Graph Gg einer quadratischen Funktion g verläuft symmetrisch zur y-Achse; die Punkte A(2; −6) und B(6; 10) liegen auf Gg
- gesucht: eine zugehörige Funktionsgleichung der Funktion g
- verfahren: wegen der Achsensymmetrie den verkürzten Ansatz g(x) = ax^2 + b wählen, beide Punkte einsetzen und das lineare Gleichungssystem lösen
- fehlerquelle: den vollen Ansatz ax^2 + bx + c verwenden und mit nur zwei Punkten ein unterbestimmtes System erhalten

### 2022-C-2b (fhr-katalog.csv)

jahr 2022 · papier C · punkte 4 · format Rechnung|Kurzantwort · antwort Term|Zahl
- gegeben: von der linearen Funktion g ist bekannt, dass ihr Graph durch P(0; 20) und Q(4; 0) verläuft; als Kontrolle ist g(x) = −5x + 20 genannt
- gesucht: Funktionsgleichung von g|Anstieg einer beliebigen Funktion h, deren Graph senkrecht zum Graphen von g verläuft
- verfahren: den Anstieg als Quotient der Koordinatendifferenzen berechnen, den y-Achsenabschnitt aus P ablesen und die Gleichung notieren; dann den negativen Kehrwert des Anstiegs bilden
- fehlerquelle: beim senkrechten Anstieg nur den Kehrwert ohne Vorzeichenwechsel bilden und −0,2 angeben

### 2017-be-gk-B1.1f (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 9 · format Rechnung · antwort Term
- gegeben: Ein verändertes Brückenteil der Holzeisenbahn soll 25 cm lang sein, links 1,5 cm und rechts 11,5 cm hoch; in beiden oberen Eckpunkten sollen wieder die Extrempunkte liegen. Die linke untere Ecke liegt im Koordinatenursprung, 1 LE = 1 cm. Das Profil wird durch g mit g(x) = ax³ + bx² + c modelliert.
- gesucht: Funktionsgleichung von g
- verfahren: Bedingungen: g(0) = 1,5 liefert c = 1,5; g′(0) = 0 gilt für den Ansatz ohne linearen Term von selbst; g′(25) = 0 und g(25) = 11,5 ergeben 1875a + 50b = 0 und 15 625a + 625b = 10. Aus der ersten b = −37,5a, eingesetzt −7812,5a = 10.
- fehlerquelle: die Bedingung g′(0) = 0 als eigene Gleichung für einen nicht vorhandenen linearen Koeffizienten ansetzen oder die Höhe rechts als g(25) = 10 statt 11,5 nehmen

### 2017-be-gk-B1.2f (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 7 · format Kurzantwort|Rechnung|Begründung · antwort Term|Text
- gegeben: Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. f′(x) = (−x² + 4x − 3) · e^(−x), also f′(0) = −3 und f′(1) = 0. Der Graph einer quadratischen Funktion p soll in den Punkten R(0 | 1) und S(1 | 0) tangential zum Graphen von f verlaufen.
- gesucht: vier Bedingungen für p; Untersuchung, ob es eine solche Funktion p gibt
- verfahren: Ansatz p(x) = ax² + bx + c. Bedingungen p(0) = 1, p′(0) = −3, p(1) = 0, p′(1) = 0. Die ersten drei liefern c = 1, b = −3, a = 2; die vierte prüfen: p′(1) = 2a + b = 1 ≠ 0.
- fehlerquelle: nur drei Bedingungen verwenden und die gefundene Parabel als Lösung angeben, ohne die vierte zu prüfen

### 2018-be-gk-B1.1e (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 6 · format Rechnung · antwort Term
- gegeben: Anlaufbahn h mit h(x) = 0,05x² + 54 und Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m. Die Flugbahn des Springers ist eine quadratische Funktion f; im Punkt S(0 | 54) geht die Anlaufbahn ohne Knick in die Flugbahn über. Bei x = 60 m hat der Springer eine vertikale Höhe von 4,72 m über dem Aufsprunghang. Als Kontrolle ist f(x) = −0,008x² + 54 angegeben.
- gesucht: Funktionsgleichung der Flugbahn f
- verfahren: Ansatz f(x) = ax² + bx + c. Knickfreier Übergang in S heißt f(0) = h(0) = 54, also c = 54, und f'(0) = h'(0) = 0, also b = 0. Die dritte Bedingung ist f(60) − g(60) = 4,72 mit g(60) = 20,48; daraus 3600a + 54 = 25,2 und a = −0,008.
- fehlerquelle: die Höhe 4,72 m als Funktionswert f(60) statt als Abstand zum Aufsprunghang deuten, oder den knickfreien Übergang nur über den Funktionswert und nicht über die Steigung ansetzen

### 2018-be-gk-cas-B1.1f (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 11 · format Rechnung · antwort Term|Zahl
- gegeben: Anlaufbahn h mit h(x) = 0,05x² + 54 und Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m. Die Flugbahn des Springers ist eine quadratische Funktion f; im Punkt S(0 | 54) geht die Anlaufbahn ohne Knick in die Flugbahn über. Bei x = 60 m hat der Springer eine vertikale Höhe von 4,72 m über dem Aufsprunghang. Kontrollangabe: f(x) = −0,008x² + 54 und L(73,9 | 10,3).
- gesucht: Funktionsgleichung der Flugbahn f; Koordinaten des Landepunkts L auf dem Aufsprunghang; Winkel zwischen Flugbahn und Aufsprunghang im Punkt L
- verfahren: Ansatz f(x) = ax² + bx + c; aus f(0) = h(0) und f′(0) = h′(0) folgen c = 54 und b = 0, aus f(60) − g(60) = 4,72 mit g(60) = 20,48 folgt a = −0,008. Dann f(x) = g(x) mit dem CAS (oder über u = x²) lösen, die positive Lösung nehmen und y berechnen. Den Winkel in L aus den Steigungen f′(x_L) und g′(x_L) über die Steigungswinkel (Differenz) oder die Tangensformel bestimmen.
- fehlerquelle: die Höhe 4,72 m als Funktionswert f(60) statt als Abstand zum Hang deuten oder den Winkel als Differenz der Steigungen statt der Steigungswinkel berechnen

### 2018-bb-ea-B2.2h (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 6 · format Rechnung · antwort Term
- gegeben: Über den Gartenteich führt eine Brücke. Sie soll in einem neuen x-y-Koordinatensystem durch eine ganzrationale Funktion 4. Grades modelliert werden, die symmetrisch zur y-Achse verläuft. Die Brücke hat eine Spannweite von 4 Metern, ist in der Mitte 0,5 Meter hoch über der x-Achse und hat an den beiden Enden einen Steigungswinkel von 45° bzw. −45°.
- gesucht: Gleichung dieser Funktion vierten Grades
- verfahren: Die Achsensymmetrie lässt nur gerade Exponenten zu: Ansatz p(x) = ax⁴ + bx² + c. Die Mitte liegt bei x = 0, also c = 0,5. Die Spannweite 4 legt die Enden auf x = ±2 mit p(2) = 0. Der Steigungswinkel −45° am rechten Ende bedeutet p′(2) = tan(−45°) = −1. Aus 16a + 4b = −0,5 und 32a + 4b = −1 folgen a und b.
- fehlerquelle: den Steigungswinkel unmittelbar als Anstieg einsetzen, statt über den Tangens zu gehen, oder am rechten Ende mit +1 statt −1 rechnen

### 2019-be-gk-B2.1c (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 5 · format Rechnung · antwort Term
- gegeben: Baum B: g(t) = a · t³ + b · t² (t Jahre, g(t) cm); nach 5 Jahren 500 cm hoch, Wachstumsgeschwindigkeit dann 150 cm/Jahr; Kontrollergebnis g(t) = −2t³ + 30t²
- gesucht: Funktionsgleichung von g
- verfahren: g'(t) = 3at² + 2bt; Bedingungen g(5) = 500 und g'(5) = 150 als LGS lösen
- fehlerquelle: die Steigungsbedingung in g statt in g' einsetzen

### 2021-be-gk-B2.1k (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 4 · format Rechnung · antwort Term
- gegeben: Parabel q mit q(0) = 0 und Hochpunkt H_q(2 | 2,2) als neue untere Begrenzung
- gesucht: Funktionsgleichung von q
- verfahren: Ansatz ax² + bx, Bedingungen q(2) = 2,2 und q'(2) = 0
- fehlerquelle: Scheitelpunktform ohne die Nullstellenbedingung ansetzen

### 2022-bebb-gk-B2.2k (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Größeres Bauteil: oberer Rand zwischen R(2 | 1) und S(4 | 4) gerade, links und rechts knickfreie Kurven mit Übergängen bei (0 | 0), R, S und (5 | 5); Kurvenstück von (0 | 0) bis R als Graph von k(x) = a · x⁴ + b · x²
- gesucht: Nachweis, dass k verwendet werden kann; Werte von a und b
- verfahren: Bedingungen k(2) = 1 und k'(2) = 1,5 (Steigung von RS) als Gleichungssystem; k'(0) = 0 erfüllt
- fehlerquelle: knickfrei nur als „Punkt liegt auf beiden Kurven“ deuten

### 2022-bebb-gk-B2.2g (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Rechnung · antwort Text
- gegeben: Gerade g durch C(0,4 | −0,4) und D(2 | 1,2)
- gesucht: Nachweis, dass g(x) = x − 0,8 die Gleichung von g ist
- verfahren: Beide Punkte einsetzen oder Steigung und Achsenabschnitt bestimmen
- fehlerquelle: nur einen Punkt prüfen

### 2023-bebb-gk-B2.2k (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 6 · format Rechnung · antwort Term
- gegeben: Für eine neue Heizung wird der Temperaturverlauf der Startphase durch eine ganzrationale Funktion k vom Grad 3 beschrieben mit I k(0) = 20, II k'(0) = 130, III H(5 | 220) ist Hochpunkt des Graphen von k.
- gesucht: Funktionsgleichung von k
- verfahren: Ansatz k(x) = ax³ + bx² + cx + d, k'(x) = 3ax² + 2bx + c; aus I und II folgen d = 20 und c = 130; aus k(5) = 220 und k'(5) = 0 folgt 125a + 25b = −450 und 75a + 10b = −130, also a = 2, b = −28.
- fehlerquelle: den Hochpunkt nur als k(5) = 220 übersetzen und k'(5) = 0 vergessen

### 2023-bebb-lk-B2.1l (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 3 · format Begründung · antwort Text
- gegeben: Profil auf [0; 5] laut Abbildung 3 knickfrei an G_0,5 (Hochpunkt (0 | 2)) anschließend und bei x = 5 waagerecht in den Boden auslaufend
- gesucht: Begründung, dass eine einzige quadratische Parabel auf [0; 5] nicht möglich ist
- verfahren: Zwei Stellen mit waagerechter Tangente (0 und 5) gegen den einen Scheitel einer Parabel; oder Krümmungswechsel gegen konstante Krümmungsrichtung
- fehlerquelle: nur mit „passt nicht durch die Punkte“ argumentieren

### 2026-bb-ea-B2.1g (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Weltbevölkerung in Mrd. seit 2023 (x Jahre): Modell A linear von 8 (2023) auf 13 (2075), Modell B b(x) = 11 − 3 · e^(kx), Modell C Parabel (Abbildung mit den drei Kurven); b(x) = 11 − 3 · e^(kx); Zuwachs bei x = 0: 0,1 Mrd. pro Jahr; Kontrolle k = −1/30
- gesucht: der Wert von k
- verfahren: b'(0) = 0,1 nach k auflösen
- fehlerquelle: b(0) statt b'(0) ansetzen

### 2022-bebb-lk-B2.1i (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 7 · format Rechnung · antwort Term
- gegeben: g ganzrational dritten Grades; Graph durch den Ursprung; Nullstelle −2 mit Steigung −5; Tangente in (2 | g(2)) parallel zu y = −9x + 9; Kontrolle g(x) = −3/4 x³ − 1/2 x² + 2x
- gesucht: eine Funktionsgleichung von g
- verfahren: vier Bedingungen in a, b, c, d aufstellen und das Gleichungssystem lösen
- fehlerquelle: Parallelität als gleicher y-Achsenabschnitt deuten; Vorzeichen bei g'(−2)

### 2020-be-gk-A1.2a (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 5 · format Rechnung · antwort Term
- gegeben: quadratische Funktion f durch den Ursprung; Tangente in (2; f(2)) mit y = 4x − 2
- gesucht: Funktionsterm von f
- verfahren: drei Bedingungen aufstellen und lösen
- fehlerquelle: f(2) = 4 statt 6 ansetzen (Achsenabschnitt der Tangente übersehen)

### 2023-bebb-lk-A1.4b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 3 · format Rechnung · antwort Term
- gegeben: f'(x) = 3x · (4 − x) = 12x − 3x²; t(x) = 9x + 1 ist Tangente an den Graphen von f
- gesucht: eine mögliche Funktionsgleichung von f
- verfahren: Berührstelle aus f' = 9, f durch Integration mit Konstante, Konstante aus f(x₀) = t(x₀)
- fehlerquelle: Integrationskonstante vergessen; y-Achsenabschnitt 1 der Tangente als f(0) nehmen

### 2025-bebb-lk-A1.2b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: f(x) = 3 · cos(x); g(x) = a · f(x) + b · x mit reellen a und b; die Punkte (0; −3) und (π/2; 3π/4) liegen auf dem Graphen von g
- gesucht: a und b
- verfahren: beide Punkte einsetzen: 3a · cos(0) + b · 0 = −3 liefert a; 3a · cos(π/2) + b · π/2 = 3π/4 liefert b
- fehlerquelle: cos(π/2) mit 1 oder cos(0) mit 0 verwechseln

### 2022MgrundlegendAAnalysis12-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: f: x ↦ a · b^x mit a, b > 0; Graph in der Abbildung durch (0; 0,5) und (1; 2)
- gesucht: Werte von a und b
- verfahren: f(0) = a ablesen, dann f(1) = a · b nach b auflösen
- fehlerquelle: Punkt (−1; 1/8) ungenau ablesen und damit rechnen

### 2020MgrundlegendAAnalysis12 (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 5 · format Rechnung · antwort Term
- gegeben: quadratische Funktion f durch den Ursprung; Tangente in (2; f(2)) mit y = 4x − 2
- gesucht: Funktionsterm von f
- verfahren: drei Bedingungen aufstellen und lösen
- fehlerquelle: f(2) = 4 statt 6 ansetzen (Achsenabschnitt der Tangente übersehen)

### 2022MerhoehtAAnalysis2 (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 5 · format Rechnung · antwort Term
- gegeben: quadratische Funktion g; der Graph schneidet y = 1/4 x + 1 im Punkt (0; 1) unter einem rechten Winkel; x- und y-Koordinate des Extrempunkts stimmen überein
- gesucht: Gleichung von g
- verfahren: c aus dem Punkt, b aus der Orthogonalität der Steigungen, a aus der Extrempunktbedingung
- fehlerquelle: rechten Winkel als g'(0) = 1/4 oder −1/4 ansetzen

### 2023MerhoehtAAnalysis22 (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Kosinusfunktion f in IR mit Periode p; (p/2; p) ist Hochpunkt, (p/4; p/2) Wendepunkt
- gesucht: Steigung des Graphen an der Stelle p/4
- verfahren: aus Hoch- und Wendepunkt Amplitude p/2 und Mittellinie p/2 ablesen, Minimum im Ursprung: f(x) = −p/2 · cos(2π/p · x) + p/2; ableiten und p/4 einsetzen
- fehlerquelle: Amplitude p statt p/2 ansetzen

### 2025MerhoehtAAnalysis13-b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: f(x) = 3 · cos(x); g(x) = a · f(x) + b · x mit reellen a und b; die Punkte (0; −3) und (π/2; 3π/4) liegen auf dem Graphen von g
- gesucht: a und b
- verfahren: beide Punkte einsetzen: 3a · cos(0) + b · 0 = −3 liefert a; 3a · cos(π/2) + b · π/2 = 3π/4 liefert b
- fehlerquelle: cos(π/2) mit 1 oder cos(0) mit 0 verwechseln

### 2026MerhoehtAAnalysis13-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: g(x) = ln(x − a) + b mit ganzzahligen a und b und größtmöglicher Definitionsmenge; der Graph verläuft durch (−1; −1); Abbildung mit dem Graphen von g, senkrechte Asymptote bei x = −2
- gesucht: a und b
- verfahren: Definitionsbereich ]a; ∞[ mit der Asymptote im Bild vergleichen: a = −2; dann (−1; −1) einsetzen: ln 1 + b = −1
- fehlerquelle: a = 2 setzen, weil der Term x − a lautet

### 2018MerhoehtBAnalysisWTR1-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 4 · format Rechnung · antwort Term
- gegeben: Abbildung 1: Graph einer ganzrationalen Funktion dritten Grades mit Nullstellen 0, 5, 10 durch (1 | 2); Kontrolle f(x) = 1/18 (x³ − 15x² + 50x)
- gesucht: ein Funktionsterm von f
- verfahren: Produktansatz mit den drei Nullstellen, a aus f(1) = 2
- fehlerquelle: Ansatz mit allgemeinen Koeffizienten und Gleichungssystem statt Produktform

### 2022MgrundlegendBAnalysisWTR1-1g (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: f(x) = 1/80 x⁵ − 1/6 x³ + x, definiert in IR; Abbildung 1 zeigt G_f; W(2 | f(2)) ist Wendepunkt; g(x) = a · sin(bx), a, b > 0, auf [−2; 2] Näherung von f; 2 ist Extremstelle von g; g(2) = f(2)
- gesucht: die passenden Werte von a und b
- verfahren: b aus der Lage des ersten Hochpunkts, a aus dem Funktionswert
- fehlerquelle: Periode 2 statt Viertelperiode 2 ansetzen (b = π)

### 2022MerhoehtBAnalysisWTR1-2a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: s(x) = a · sin(b · x) + 1; E₁(−2 | −1) und E₂(2 | 3) direkt aufeinanderfolgende Extrempunkte; Kontrolle a = 2, b = π/4
- gesucht: a und b
- verfahren: Amplitude als halbe Differenz der Extremwerte, b aus der Periode
- fehlerquelle: Abstand der Extremstellen als ganze Periode nehmen

### 2017MerhoehtBAnalysisWTR3-2h (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Rechnung · antwort Term|Zahl
- gegeben: Die Profillinie soll nun durch q(x) = a − c · e^(−x^2), a, c ∈ IR+, x ∈ [−3; 3] beschrieben werden; der Graph von q soll durch den Ursprung verlaufen, die y-Koordinaten seiner Randpunkte sollen mit denen des Graphen von p(x) = −1/48 · (x^4 − 18x^2) übereinstimmen (p(±3) = 27/16)
- gesucht: Werte von a und c
- verfahren: q(0) = a − c = 0 und q(3) = a − c · e^(−9) = 27/16 (wegen der Symmetrie genügt ein Rand); aus a = c folgt a · (1 − e^(−9)) = 27/16
- fehlerquelle: e^(−0) = 0 setzen und so a = 0 erhalten

### 2017MerhoehtBAnalysisWTR3-2i (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: q(x) = a − c · e^(−x^2), a, c ∈ IR+, x ∈ [−3; 3]
- gesucht: Begründung, dass a und c nicht so gewählt werden können, dass der Graph von q zu seinen Randpunkten hin parallel zur x-Achse ausläuft
- verfahren: q'(x) = 2cx · e^(−x^2); an x = ±3 ist das Produkt wegen c > 0 und e^(−9) > 0 von null verschieden
- fehlerquelle: nur einen konkreten Wert von c untersuchen

### 2017MerhoehtBAnalysisCAS2-4 (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 7 · format Rechnung · antwort Term
- gegeben: f_2(x) = −3/256 · x^4 + 3/8 · x^2 (Likörglas); der Längsschnitt soll für 0 <= x <= 4 durch zwei quadratische Funktionen p1 und p2 beschrieben werden: die Scheitelpunkte ihrer Graphen liegen im Tiefpunkt bzw. im Hochpunkt des Graphen von f_2; die Graphen gehen ohne Knick ineinander über, und zwar an der x-Koordinate des Wendepunkts des Graphen von f_2
- gesucht: Funktionsgleichungen von p1 und p2
- verfahren: Tiefpunkt (0; 0), Hochpunkt (4; 3) und Wendestelle 4/3 · √3 von f_2 bestimmen; Ansatz p1(x) = ax^2 und p2(x) = −b(x − 4)^2 + 3; p1 = p2 und p1' = p2' an der Wendestelle liefern a und b
- fehlerquelle: nur gleiche Funktionswerte an der Übergangsstelle fordern und die Steigungsbedingung vergessen

### 2017MgrundlegendBAnalysisCAS-1e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: In einem Produktionsprozess werden Flüssigkeiten erhitzt, eine Zeit lang bei konstanter Temperatur gehalten und anschließend wieder abgekühlt; bei einem durchgehend gesteuerten Vorgang beschreibt f(t) = 23 + 20 · t · e^(−t/10) (t in Minuten seit Beginn, f(t) in °C) den Temperaturverlauf während des Erhitzens und des Abkühlens modellhaft; betrachtet wird nun ein Vorgang, bei dem die Steuerung zwanzig Minuten nach Beginn abgeschaltet wird; das anschließende Abkühlen beschreibt für t >= 20 die Funktion h mit h(t) = 23 + b · e^(c · t) und b, c ∈ IR; zu Beginn des Abkühlens soll die Temperatur 77 °C und die momentane Änderungsrate der Temperatur −3,5 °C pro Minute betragen
- gesucht: passende Werte von b und c
- verfahren: h(20) = 77 und h'(20) = b · c · e^(20c) = −3,5 ansetzen; aus b · e^(20c) = 54 folgt 54c = −3,5, also c = −7/108, dann b = 54 · e^(−20c)
- fehlerquelle: den Beginn des Abkühlens bei t = 0 statt bei t = 20 ansetzen oder die Änderungsrate positiv einsetzen

### 2018MerhoehtBAnalysisCAS1-3a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Papierflieger: Koordinatensystem mit der x-Achse entlang des horizontalen Bodens und der y-Achse durch den Abwurfpunkt; x ist die horizontale Entfernung vom Abwurfpunkt, der Funktionswert die Flughöhe, jeweils in Metern; die Größe der Papierflieger wird vernachlässigt; f_4(x) = −1/4 · x^2 + x + 2 (Funktion der Schar f_r(x) = −1/r · x^2 + 4/r · x + 2 für r = 4); Flugkurve vom Typ S: im ersten Teil durch f_4 beschrieben, ab einer horizontalen Entfernung von 0,5 m vom Abwurfpunkt durch s(x) = a/(x − 1,5) + b mit a, b ∈ IR; die Flugkurve hat keinen Knick; der Papierflieger steigt, bis er einen Steigungswinkel von 85° erreicht, und stürzt dann vertikal ab; zur Kontrolle: a = −0,75, b = 1,6875
- gesucht: die Werte von a und b
- verfahren: s(0,5) = f_4(0,5) und s'(0,5) = f_4'(0,5) mit s'(x) = −a/(x − 1,5)^2 aufstellen: −a + b = 2,4375 und −a = 0,75
- fehlerquelle: nur gleiche Funktionswerte fordern oder beim Ableiten von a/(x − 1,5) das Vorzeichen verlieren

### 2018MerhoehtBAnalysisCAS2-2f (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Gegeben ist die in IR definierte Funktion f mit f(x) = −1/10^6 · x^4 + 4/9375 · x^3 − 13/250 · x^2 + 8/5 · x + 140; mit einem CGM-Gerät wird der Glukosewert eines Patienten ständig gemessen: f beschreibt für 0 <= x <= 240 modellhaft seine Entwicklung, x ist die seit Beobachtungsbeginn vergangene Zeit in Minuten, f(x) der Glukosewert in mg/dl; zum Zeitpunkt 240 Minuten nimmt der Patient Traubenzucker zu sich, die anschließende Entwicklung soll im Modell durch eine Funktion g beschrieben werden; Bedingung: Glukosewert und momentane Änderungsrate zum Zeitpunkt 240 Minuten sollen unabhängig davon sein, ob sie mit f oder mit g ermittelt werden; dazu werden zunächst die in IR definierten Funktionen h_k mit h_k(x) = 50 − 50 · (k · x + 1)^2 · e^(−k · x), k ∈ IR+, betrachtet
- gesucht: Wert von k, für den die momentane Änderungsrate von h_k zum Zeitpunkt 0 mit der momentanen Änderungsrate von f zum Zeitpunkt 240 Minuten übereinstimmt
- verfahren: h_k'(0) = f'(240) aufstellen und nach k lösen
- fehlerquelle: h_k(0) = f(240) statt der Ableitungen gleichsetzen

### 2018MerhoehtBAnalysisCAS3-2e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Hängebrücke (Abbildung 1, schematisch) im Koordinatensystem mit 1 LE = 1 m, Materialstärken vernachlässigt: zwei vertikale Pfeiler bei x = −250 und x = 250 (Länge der Brücke 500 m), waagerechte Fahrbahn 12 m über der x-Achse (y = 12), das Drahtseil ist an den Pfeilern in 72,8 m Höhe über der x-Achse befestigt (Befestigungspunkte (−250; 72,8) und (250; 72,8)) und hängt symmetrisch zur y-Achse durch; gegeben sind die in IR definierten Funktionen g_r mit g_r(x) = r · x^2 + 20, r ∈ IR; ein zwischen den Befestigungspunkten unbelastet hängendes Drahtseil könnte mit einer der in IR definierten Funktionen h_s,t mit h_s,t(x) = s/2 · (e^(x/s) + e^(−x/s)) + t, s ∈ IR mit s ≠ 0, t ∈ IR, beschrieben werden (Hinweis: 1/2 · (e^x + e^(−x)) heißt in einigen CAS cosh(x), 1/2 · (e^x − e^(−x)) heißt sinh(x)); das belastete Drahtseil ist 514,5 m lang, das unbelastete soll die gleiche Länge haben; die Länge des Graphen von h_s,t zwischen (−v; h_s,t(−v)) und (v; h_s,t(v)) mit v ∈ IR+ ist s · (e^(v/s) − e^(−v/s)); für das unbelastete Seil ist s > 0; zur Kontrolle: s ≈ 601,9, t ≈ −581,8
- gesucht: die Werte von s und t für die Funktion h_s,t, die das unbelastete Drahtseil beschreiben könnte
- verfahren: Mit v = 250: s · (e^(250/s) − e^(−250/s)) = 514,5 mit dem Rechner nach s > 0 lösen; dann h_s,t(250) = 72,8 nach t auflösen
- fehlerquelle: die halbe Brückenlänge nicht als v einsetzen (v = 500) oder t vor s bestimmen wollen

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2018MerhoehtBAnalysisWTR1-1g, 2023-bebb-lk-B2.1m, 2026-bb-ea-B2.1i

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
