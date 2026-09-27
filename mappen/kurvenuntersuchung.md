# Mappe: kurvenuntersuchung

Eintrag: hz-0801/mathe-nachhilfe, katalog/kurvenuntersuchung.md
Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26T16:47:30+02:00, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:42 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Kurvenuntersuchung
  3
  4  ### Verortung
  5  Anwenden der ersten, zweiten und dritten Ableitung auf den Graphen: Monotonie, Extrempunkte, Krümmung und Wendepunkte, der Zusammenhang zwischen Funktions- und Ableitungsgraph und die Deutung dieser P … (gekürzt, 1557 Zeichen)
  6  [GOST] Q1, 1. Kurshalbjahr „Analysis; Lineare Algebra“ (BB S. 23–25), Grund- und Leistungskursfach, Funktionsklassen Potenzfunktionen mit ganzzahligem Exponenten, ganzrationale Funktionen, natürliche  … (gekürzt, 2699 Zeichen)
  7  [FOS] L4 (S. 24): „die Ableitung zur Bestimmung von Monotonieverhalten, Extrempunkten, Krümmungsverhalten und Wendepunkten von Funktionen nutzen (notwendige/hinreichende Bedingung und inhaltliche Begr … (gekürzt, 1121 Zeichen)
  8  [LS-AA] Einführungsphase Kapitel IV „Extremstellen und Wendestellen“: 1 Monotonie · 2 Lokale Extremstellen · 3 Der Nachweis von Extremstellen · 4 Die Bedeutung der zweiten Ableitung – Wendestellen · 5 … (gekürzt, 2449 Zeichen)
  9
 10  ### Lerneinheiten
 11  1. Monotonie und erste Ableitung – Vorzeichen von f' in einem Intervall lesen und daraus steigt/fällt schließen; Nullstellen von f' als Grenzen der Monotonieintervalle; Intervalle abgeschlossen angeben; Nachweis am Term, dass f' nie negativ wird (Quadrat, e-Faktor, positive Summe) und der Graph deshalb auf ganz ℝ monoton ist; daraus folgern, dass es keinen Extrempunkt gibt. (Q1, GK-Kern; FOS „Monotonie und 1. Ableitung“) ← Eingabe „monotonie“, „monotonieintervalle“, „steigt oder fällt“, „monoton steigend“
 12    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK
 13  2. Extrempunkte – notwendige Bedingung f'(x₀) = 0, hinreichende Bedingung über das Vorzeichen von f'' oder den Vorzeichenwechsel von f'; Hoch- und Tiefpunkt mit beiden Koordinaten; Sattelpunkt als Ste … (gekürzt, 633 Zeichen)
 14    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
 15  3. Krümmung und Wendepunkte – f'' als Steigungsfunktion von f'; Links- und Rechtskrümmung über das Vorzeichen von f''; Wendepunkt als Krümmungswechsel, Nachweis über f''(x₀) = 0 und f'''(x₀) ≠ 0 oder Vorzeichenwechsel von f''; Krümmungsintervalle; Wendetangente als Tangente im Wendepunkt (Steigung f'(x₀)); Wendepunkt an vorgegebener Stelle nachweisen gegen Wendepunkte berechnen; Sattelpunkt als Wendepunkt mit waagerechter Tangente. (Q1, GK-Kern; FOS „Krümmung und 2. Ableitung“, „Wendepunkte und Sattelpunkte“) ← Eingabe „wendepunkt“, „wendestelle“, „krümmung“, „linksgekrümmt“, „wendetangente“
 16    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
 17  4. Graph und Ableitungsgraph – qualitativ, ohne oder mit wenig Rechnung: aus dem Graphen von f das Vorzeichen und die Nullstellen von f' lesen, Ableitungswert und Wendestelle am Graphen ablesen; Graph … (gekürzt, 818 Zeichen)
 18    Marken: BE Q1/2 · BB Q1 · GK · Abitur GK · Abitur LK
 19  5. Kurvenuntersuchung im Sachzusammenhang – Sachfragen übersetzen: größter oder kleinster Wert → Hoch- oder Tiefpunkt einschließlich Randvergleich; stärkste Zunahme oder Abnahme → Wendepunkt als Extre … (gekürzt, 780 Zeichen)
 20    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
 21  Niveaustufung: fhr = Einheit 1 bis 3 rechnerisch mit ganzrationalen Funktionen ohne Produkt- und Kettenregel, Einheit 4 und 5 nur in Ansätzen; GK = alle fünf, mit Produkten aus Polynom und e-Funktion; LK = zusätzlich Wurzel-, ln-, sin/cos-Funktionen und Ortskurven (Ortskurven ohne Prüfungsbeleg in der Rohdatei – Vermerk „kein Original“).
 22
 23  ### Typen je Lerneinheit
 24  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
 25  Einheit 1: Extremstellen berechnen und Monotonieverhalten angeben (1) · Monotonieintervalle und Wertebereich einer Differenzfunktion auf einem Intervall über die Ableitung ermitteln (1) — Nachweis: Monotonie über das Vorzeichen der Ableitung am Term nachweisen (4) · Fehlende Extrempunkte über eine positive Ableitung begründen (2) — Deutung: Monotonieverhalten aus einem bekannten Extrempunkt angeben (1) · Länge der Monotoniebereiche zweier Modellfunktionen vergleichen und eine Aussage beurteilen (1). Dazu: Fehler finden (Monotonie nach dem Vorzeichen von f'' statt f' angegeben; Intervallgrenzen bei null statt an der Extremstelle; f'(x₀) = 0 an einer Stelle als Gegenargument gegen die Monotonie) · Begründen (warum ein Quadrat plus eine positive Zahl nie null wird; warum aus f' > 0 überall folgt, dass es keinen Extrempunkt gibt).
 26  Einheit 2: Extrem- und Sattelpunkte über zweite Ableitung (17) · Extrempunkt eines Produkts aus Polynom und e-Funktion berechnen (12) · Lage und Art aller lokalen Extrempunkte bestimmen (10) · Stellen mit maximalem Funktionswert einschließlich Rand bestimmen (2) · Abstand zweier Extrempunkte verschiedener Graphen mit einer Schranke vergleichen (1) · Abstand zweier Extrempunkte über die Punktsymmetrie berechnen (1) · Extrempunkte berechnen und ihre Verbindungsgerade als Winkelhalbierende nachweisen (1) · Extremstellen aus den Nullstellen der Ableitung berechnen (1) · Nullstellen einer e-Funktion nachweisen und Tiefstelle berechnen (1) · Nullstellen und Extremstelle einer Parabel berechnen (1) · Wertebereich einer ganzrationalen Funktion über den globalen Tiefpunkt ermitteln (1) — Nachweis: Extrempunkt an vorgegebener Stelle nachweisen (9) · Achsenschnittpunkte angeben und Hochpunkt aus der gegebenen Ableitung begründen (2) · Gegebene Stelle als Extremstelle nachweisen (2) · Anstieg null nachweisen und fehlende Extremstelle über die doppelte Nullstelle der Ableitung ohne Rechnung begründen (1) · Berührung des Graphen mit der x-Achse über die Extrempunkte begründen (1) · Einzigen Tiefpunkt über die streng monotone Ableitung nachweisen und berechnen (1) · Extremstelle einer Logarithmusfunktion über die Ableitung oder die Symmetrie begründen (1) · Extremstelle über den Vorzeichenwechsel der Ableitung in ein Intervall einschließen (1) · Größten Funktionswert über Monotonie, Grenzverhalten und Symmetrie begründen und Wertemenge angeben (1) · Hochpunkt mit vorgegebenen Koordinaten und waagerechte Tangente im Ursprung rechnerisch nachweisen (1) · Tiefpunkt angeben und Fehlen weiterer Extrempunkte über die Ableitung nachweisen (1) · Extremstelle zwischen zwei Stellen mit gleichem Funktionswert ohne Rechnung begründen (1) · Lage eines Graphen zwischen zwei Geraden auf einem Intervall über die Differenzfunktionen nachweisen (1; Ermessen, siehe Offene Punkte) — Deutung: Aussagen zu Stellen mit waagerechter Tangente beurteilen (2) · Abstand zwischen Parabel und waagerechter Gerade über den Scheitel beschreiben (1) · Aussagen über Funktions- und Ableitungswert nahe dem Tiefpunkt ohne Rechnung beurteilen (1). Dazu: Fehler finden (positives f'' als Hochpunkt gedeutet; Lösung x = 0 beim Ausklammern verloren; Extremstelle statt Extremwert angegeben; e-Faktor null gesetzt) · Begründen (warum f'(x₀) = 0 allein nicht reicht – Sattelstelle; warum am Rand eines Intervalls ein größter Wert ohne waagerechte Tangente liegen kann).
 27  Einheit 3: Wendepunkte über zweite Ableitung (11) · Wendepunkte über die zweite Ableitung berechnen (5) · Krümmungsverhalten angeben (3) · Krümmungsverhalten aus der zweiten Ableitung deuten (2; Ermessen, siehe Offene Punkte) · Gerade durch die beiden Wendepunkte aufstellen und parallele Gerade mit genau einem gemeinsamen Punkt einzeichnen (1) — Nachweis: Wendepunkt an vorgegebener Stelle nachweisen und Wendetangente aufstellen (2) · Existenz eines Wendepunkts aus Tiefpunkt und Grenzverhalten über eine Skizze begründen (1) · Punktprobe am Graphen (1; fhr 2023-C-1d: Punkt auf dem Graphen und Wendepunkt prüfen – Ermessen, siehe Offene Punkte) · Wendepunkt mit vorgegebenen Koordinaten über die zweite Ableitung nachweisen und den symmetrischen Wendepunkt angeben (1) · Wendepunkt über den Vorzeichenwechsel der zweiten Ableitung aus der Kettenregel am Graphen nachweisen (1) · Wendestelle nachweisen und Winkel der Wendetangente mit der x-Achse über die Steigung −1 zeigen (1) · Wendestellen einer Sinusfunktion als ganzzahlig nachweisen und die beiden Wendetangentensteigungen zeigen (1) · Zweite Ableitung nachweisen und Wendepunkt an vorgegebener Stelle zeigen (1) — Deutung: Anzahl der Schnittpunkte von Geraden durch den Wendepunkt mit dem Graphen nach der Steigung unterscheiden (1). Dazu: Fehler finden (Links- und Rechtskrümmung vertauscht; f''' vergessen; Wendestelle ohne Funktionswert; Sattelpunkt als bloßer Wendepunkt) · Begründen (warum f'' das Vorzeichen wechseln muss, damit ein Wendepunkt vorliegt; warum die Wendetangente den Graphen dort durchsetzt).
 28  Einheit 4: Graphen einer Funktion in ein Koordinatensystem einzeichnen (8) — Nachweis: Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen (2) · Gemeinsamen Punkt zweier Graphen über gleiche Flächeninhalte indirekt begründen (1; Ermessen, siehe Offene Punkte) · Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen und Steigung und Achsenabschnitt angeben (1; Ermessen, siehe Offene Punkte) — Deutung: Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (2) · Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen (1) · Graphen skizzieren und Aussage über die Anzahl gemeinsamer Punkte von Tangente und Graph beurteilen (1) · Lage eines Punktes aus Bedingungen an Funktionswert und Ableitung am Graphen beschreiben (1) · Lage zweier Graphen aus dem Graphen ihrer Differenzfunktion beschreiben (1) · Wendepunkt mit negativer Steigung am Graphen markieren und begründen (1) · Werte für einen Ableitungswert und eine Wendestelle am Graphen ablesen (1). Dazu: Fehler finden (Graph von f' als Graph von f gelesen; an der Wendestelle ein Extrempunkt gezeichnet; Ableitungswert als Funktionswert abgelesen) · Begründen (warum die Nullstellen von f' unter den Hoch- und Tiefpunkten von f liegen; warum der Graph von f' einen Grad einfacher ist).
 29  Einheit 5: Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen (5) · Maximalen Neigungswinkel über die Wendestelle berechnen (5) · Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen (2) · Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen (2) · Funktionswert im Sachzusammenhang deuten (1) · Maße und Masse eines umschließenden Quaders eines Rotationskörpers aus Hochpunkt und Bereich mit Maßstab berechnen (1) · Maximale Höhe im Sachzusammenhang berechnen (1) · Steilsten Anstieg über den Wendepunkt bestimmen (1) · Volumen eines umschließenden Quaders aus den Achsenschnittpunkten mit Maßstab berechnen (1) — Nachweis: Maximum eines Bestands an vorgegebener Stelle im Sachzusammenhang nachweisen (2) — Deutung: Verlauf eines Graphen im Sachzusammenhang beschreiben (5) · Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten (4) · Gewinnbereich als Bereich zwischen den Schnittstellen von Erlösgerade und Kostengraph zeichnerisch bestimmen (2) · Ableitungswert an der Wendestelle als stärksten Anstieg der Rate im Sachzusammenhang deuten (1) · Aufgabenstellung zu Extremstellen und Wertedifferenz aus dem Lösungsweg formulieren und erläutern (1) · Differenzfunktion und ihr Maximum aus einem Lösungsweg im Sachzusammenhang deuten (1) · Funktionswert an der Stelle stärkster Abnahme am Graphen ablesen (1) · Mittleren Wert einer periodisch schwankenden Größe am Graphen ablesen (1; Ermessen, siehe Offene Punkte). Dazu: Fehler finden (Wendepunkt als Richtungswechsel oder als Beginn der Abnahme gedeutet; Nullstelle von f' statt f'' für die stärkste Abnahme; Maßstab vergessen; flacher Abschnitt als Abnahme gelesen) · Begründen (warum der größte Wert auf einem Bereich am Rand liegen kann; warum die Einheit von f' aus den Einheiten von f und x folgt).
 30  Zählung: 6 + 27 + 14 + 11 + 18 = 76 Haupttypen, 10 + 75 + 32 + 20 + 37 = 174 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: CAS-Nachtrag 2018, Heft 2017-be-gk, Pool 2017 Teil B; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags: Pool 2018 erhöht und 2017 grundlegend Teil B CAS, Berliner CAS-Hefte 2017/2018 GK).
 31
 32  ### Voraussetzungen (Blatt 0)
 33  Fertigkeiten (je Zeile: was, wofür):
 34  - Ableitungen bilden: Potenz-, Faktor- und Summenregel für ganzrationale Funktionen; GK und LK zusätzlich Produkt- und Kettenregel für Produkte aus Polynom und e-Funktion – für jede notwendige und hinreichende Bedingung, Einheit 1 bis 5. Thema ableitungsregeln.md. [GOST Q1 L4 „Funktionen ableiten, auch unter Verwendung der Konstanten-, Potenz-, Faktor-, Summen-, Produkt- und Kettenregel“; FOS Pflichtthema 2 „Ableitungsregeln: Konstanten-, Faktor-, Summen- und Potenzregel“, „höhere Ableitungen“; FS-IQB 1.2 Ableitungsregeln]
 35  - Gleichungen lösen: linear, quadratisch mit Lösungsformel, Ausklammern und Nullprodukt, bei Grad vier und fünf Ausklammern von x oder x² und Polynomdivision mit einer gegebenen Lösung; GK zusätzlich e^x-Faktoren als nullstellenfrei erkennen – Nullstellen von f' und f'', Einheit 1 bis 3 und 5. Thema gleichungen-loesen.md. [GOST Q1 L1 „lineare, allgemeine quadratische und biquadratische Gleichungen sowie Gleichungen höheren Grades (unter Verwendung der Polynomdivision und der Linearfaktorzerlegung)“; FOS Pflichtthema 1 „Lösungsverfahren ganzrationaler Gleichungen“; GOST-OHiMi 2.1 „Gleichungen durch Faktorisieren lösen“]
 36  - Funktionswerte berechnen und Punktprobe – Koordinaten der gefundenen Punkte, Nachweis vorgegebener Punkte, Einheit 2, 3 und 5. Thema Lineare Funktionen (lineare-funktionen.md, Sek I, Einheit 3); der fhr-Typ „Punktprobe am Graphen“ ist hier Einheit 3 zugeordnet. [GOST Eingangsvoraussetzung L4; FOS Pflichtthema 1 „Funktionsdarstellungen (Wertetabelle, Funktionsgleichung, Graph)“]
 37  - Ableitung als Tangentensteigung und lokale Änderungsrate deuten (Grundvorstellung) – Einheit 4 komplett, Sachdeutung in Einheit 5. Thema ableitung-und-aenderungsrate.md. [GOST Eingangsvoraussetzung L4 „beschreiben qualitativ das Änderungsverhalten eines Funktionsgraphen durch eine Skizze des Graphen der Änderungsfunktion und begründen den Verlauf“; GOST Q1 L4 „die Ableitung insbesondere als lokale Änderungsrate deuten“; FOS „Tangentenanstieg“, „graphisches Differenzieren“]
 38  - Charakteristische Punkte (Achsenschnitt-, Hoch-, Tief-, Wendepunkte) am Graphen ganzrationaler Funktionen ablesen und im Sachzusammenhang deuten – Ausgangspunkt aller Einheiten. Sek-I-Thema quadratische-funktionen.md (Scheitel), RLP H. [GOST Eingangsvoraussetzung L4, wörtlich „bestimmen charakteristische Punkte (z. B. Achsenschnittpunkte, Hochpunkte, Tiefpunkte, Wendepunkte) aus Funktionsgraphen ganzrationaler Funktionen und deuten sie in Sachzusammenhängen“; RLP H „Beschreiben des Änderungsverhaltens ausgewählter ganzrationaler Funktionen durch eine Skizze der Ableitungsfunktion und Angeben markanter Punkte“]
 39  - Verlauf quadratischer und kubischer Graphen grob skizzieren (Öffnung, Symmetrie, Grenzverhalten) – Plausibilitätskontrolle für die berechneten Punkte, Einheit 2 bis 4. Sek-I-Thema quadratische-funktionen.md; funktionsklassen-und-eigenschaften.md. **Ermessen:** keine amtliche Eingangsvoraussetzung nennt die Skizze als Kontrolle; gesetzt, weil die belegten Fehlmuster „Hoch- und Tiefpunkt vertauscht“ und „Lösung x = null beim Ausklammern verloren“ an einer groben Skizze auffallen. [Ermessen; RLP G „Form des Graphen“ und „Öffnungsrichtung, Scheitelpunkt“ für quadratische Funktionen]
 40  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 41  - „Gegeben oder gesucht?“ – zu Aufgabentexten ankreuzen, ob die Stelle genannt ist (nachweisen: Werte einsetzen, „Zeigen Sie, dass bei … ein Hochpunkt liegt“) oder gefunden werden muss (berechnen: Ableitung null setzen, „Bestimmen Sie die Extrempunkte“); nichts rechnen. Vor Einheit 2 und 3. [Rohdatei: Typen „… an vorgegebener Stelle nachweisen“ gegen „… berechnen“; GOST Q1 L4 „notwendige und hinreichende Bedingung“]
 42  - „Welcher Nachweis?“ – zu Aufgaben ankreuzen, welcher Art-Nachweis verlangt oder möglich ist: Vorzeichen von f'', Vorzeichenwechsel von f', Begründung aus Abbildung oder Sachzusammenhang, oder gar keiner („die hinreichende Bedingung muss nicht untersucht werden“); nichts rechnen. Vor Einheit 2 und 3. [GOST Q1 L4 „notwendige und hinreichende Bedingung und inhaltliche Begründung für die Existenz“; abi 2018-be-gk-B1.2d, 2019-be-gk-B2.2b mit dem Erlass der hinreichenden Bedingung]
 43  - „Was heißt das mathematisch?“ – Sachfragen übersetzen und ankreuzen: stärkste Zunahme oder Abnahme → Wendepunkt bzw. Extremum der Ableitung; größter oder kleinster Wert → globales Maximum oder Minimum einschließlich Rand; ändert sich gerade nicht → Ableitung null; nichts rechnen. Vor Einheit 5. [GOST Q1 L4 „Randextrema“, „Änderungsrate im Sachzusammenhang“; iqb 2022MerhoehtBAnalysisWTR1-1b, 2018MgrundlegendBAnalysisWTR-2f]
 44
 45  ### Merkkasten
 46  Einheit 1 (Monotonie und erste Ableitung):
 47      Monotonie: Wo die Ableitung positiv ist, steigt der Graph; wo sie negativ ist, fällt er. Die Bereiche findet man, indem man die Nullstellen von f' berechnet und dazwischen das Vorzeichen prüft.
 48        f(x) = x² − 4x, f'(x) = 2x − 4: für x < 2 ist f' negativ, f fällt; für x > 2 ist f' positiv, f steigt.
 49      Nachweis am Term: Sieht man dem Term von f' an, dass er nie negativ wird (Quadrat, e-Faktor, positive Summe), ist der Graph auf ganz ℝ monoton steigend – ohne Nullstellen zu berechnen.
 50        f(x) = x³ + 3x: f'(x) = 3x² + 3 > 0 für alle x, also streng monoton steigend.
 51        f(x) = e^(0,5x): f'(x) = 0,5 · e^(0,5x) > 0.
 52      Schreibweise: „f ist auf [a; b] monoton steigend“ – die Intervallgrenzen sind die Nullstellen von f', die Intervalle werden abgeschlossen angegeben.
 53      Auswendig (Teil A): „Monotonie“ und „Nachweis am Term“ – die Anlage ohne Hilfsmittel [GOST-OHiMi 2.2] führt „Monotonie“ unter den Funktionseigenschaften, der Nachweis am Term ist ihre Anwendung ohne Rechner; die „Schreibweise“ ist Konvention, keine Anlagenforderung.
 54      Formelsammlung: Analysis – Ableitung, Ableitungsregeln [FS-IQB 1.2]; ein Monotoniekriterium steht nicht in der Formelsammlung – [FS] offen
 55  Quelle: eigene Formulierung nach [GOST Q1 L4] „Zusammenhang zwischen Monotonie und erster Ableitung“ und [FOS] „Monotonie und 1. Ableitung“; Zahlenbeispiele eigen (Ermessen); [LS-AA EP IV 1, QP I 5].
 56
 57  Einheit 2 (Extrempunkte):
 58      Notwendig: In einem Hoch- oder Tiefpunkt ist die Tangente waagerecht, also f'(x₀) = 0. Umgekehrt gilt das nicht – an einer Sattelstelle ist f' auch null.
 59      Hinreichend: f'(x₀) = 0 und f''(x₀) < 0 → Hochpunkt; f'(x₀) = 0 und f''(x₀) > 0 → Tiefpunkt. Ist f''(x₀) = 0, entscheidet der Vorzeichenwechsel von f': von + nach − Hochpunkt, von − nach + Tiefpunkt, kein Wechsel Sattelpunkt.
 60        f(x) = x³ − 3x: f'(x) = 3x² − 3 = 0 ⇔ x = −1 oder x = 1; f''(x) = 6x; f''(−1) = −6 < 0 → H(−1 | 2); f''(1) = 6 > 0 → T(1 | −2).
 61        f(x) = x³: f'(0) = 0 und f''(0) = 0, aber f'(x) = 3x² wechselt bei 0 das Vorzeichen nicht → Sattelpunkt S(0 | 0).
 62      Immer den Funktionswert dazu: Ein Punkt hat zwei Koordinaten – die Stelle aus f' = 0, den Wert aus f.
 63      Größter Wert auf einem Intervall: lokale Hochpunkte und die beiden Randwerte vergleichen (Randextrema).
 64        f(x) = x³ − 3x auf [−2; 3]: H(−1 | 2), Randwert f(3) = 18 → größter Wert 18 am rechten Rand, kein Hochpunkt.
 65      Auswendig (Teil A): „Notwendig“ und „Hinreichend“ mit dem Sattelpunkt-Fall – [GOST-OHiMi 2.2] „Extrempunkte und Wendepunkte (notwendiges und hinreichendes Kriterium)“; „Immer den Funktionswert dazu“ ist Arbeitsregel, „Größter Wert auf einem Intervall“ (Randextrema) steht im Plan, nicht in der Anlage.
 66      Formelsammlung: Analysis – Ableitung [FS-IQB 1.2]; notwendige und hinreichende Bedingung stehen nicht in der Formelsammlung, die Anlage ohne Hilfsmittel [GOST-OHiMi 2.2] verlangt sie auswendig – [FS] offen
 67  Quelle: eigene Formulierung nach [GOST Q1 L4] „lokale und globale Extrema, Sattelpunkte“, „notwendige und hinreichende Bedingung“, „Randextrema“ und [FOS] „lokale Extrempunkte“, „Sattelpunkte“; Zahlenbeispiele eigen (Ermessen; f(x) = x³ − 3x ist die Funktion von iqb 2026MgrundlegendAAnalysis11, dort mit Hochpunkt bei −1 vorgegeben – hier als Kastenzahl gesperrt); [LS-AA EP IV 2–3, QP I 6].
 68
 69  Einheit 3 (Krümmung und Wendepunkte):
 70      Krümmung: Ist f'' positiv, ist der Graph linksgekrümmt (die Steigung nimmt zu, Bauch nach unten); ist f'' negativ, rechtsgekrümmt (die Steigung nimmt ab). f'' ist die Ableitung von f' und sagt, ob f' steigt oder fällt.
 71      Wendepunkt: Dort wechselt die Krümmung. Notwendig f''(x₀) = 0, hinreichend f'''(x₀) ≠ 0 (oder Vorzeichenwechsel von f''). Koordinaten wieder mit f.
 72        f(x) = x³ − 3x: f''(x) = 6x = 0 ⇔ x = 0; f'''(x) = 6 ≠ 0 → W(0 | 0). Für x < 0 rechtsgekrümmt, für x > 0 linksgekrümmt.
 73      Wendetangente: die Tangente im Wendepunkt, Steigung f'(x₀) – in der Umgebung die steilste Stelle des Graphen.
 74        f'(0) = −3 → Wendetangente t(x) = −3x.
 75      Sattelpunkt: ein Wendepunkt mit waagerechter Tangente – f'(x₀) = 0, f''(x₀) = 0, f'''(x₀) ≠ 0.
 76        f(x) = x⁴ − 4x³: f''(x) = 12x² − 24x = 12x · (x − 2) = 0 ⇔ x = 0 oder x = 2; f'''(0) = −24 ≠ 0 und f'''(2) = 24 ≠ 0; f'(0) = 0 → Sattelpunkt S(0 | 0), zweiter Wendepunkt W(2 | −16).
 77      Auswendig (Teil A): „Krümmung“, „Wendepunkt“ und „Sattelpunkt“ – [GOST-OHiMi 2.2] „Krümmungsverhalten“, „Extrempunkte und Wendepunkte (notwendiges und hinreichendes Kriterium)“; die „Wendetangente“ ist die Tangente im Wendepunkt und gehört als Tangentengleichung zu tangente-normale-schnittwinkel.md (dort in der Auswendig-Zeile von Kasten 1 markiert).
 78      Formelsammlung: Analysis – Ableitung [FS-IQB 1.2]; Krümmung und Wendepunktkriterium stehen nicht in der Formelsammlung – [FS] offen
 79  Quelle: eigene Formulierung nach [GOST Q1 L4] „Zusammenhang zwischen Krümmungsverhalten und zweiter Ableitung“, „Wendepunkte, Sattelpunkte“, „zweite Ableitung als Steigungsfunktion der ersten Ableitung“ und [FOS] „Krümmung und 2. Ableitung“, „Wendepunkte und Sattelpunkte“; Zahlenbeispiele eigen (Ermessen); [LS-AA EP IV 4, QP I 5–6].
 80
 81  Einheit 4 (Graph und Ableitungsgraph):
 82      Übersetzungstabelle f ↔ f' ↔ f'':
 83        f steigt ↔ f' > 0 · f fällt ↔ f' < 0
 84        Hoch- oder Tiefpunkt von f ↔ Nullstelle von f' mit Vorzeichenwechsel
 85        Wendepunkt von f ↔ Hoch- oder Tiefpunkt von f' ↔ Nullstelle von f''
 86        f linksgekrümmt ↔ f' steigt ↔ f'' > 0
 87      Grad: Der Graph von f' ist um einen Grad einfacher – aus der Parabel wird eine Gerade, aus der Kurve dritten Grades eine Parabel.
 88        f(x) = x²: f'(x) = 2x ist eine Gerade durch den Ursprung; der Tiefpunkt von f bei 0 ist die Nullstelle von f'.
 89        f(x) = x³ − 3x: f'(x) = 3x² − 3 ist eine Parabel mit den Nullstellen −1 und 1 (Extremstellen von f) und dem Tiefpunkt bei 0 (Wendestelle von f).
 90      Skizze aus Eigenschaften: erst die gegebenen Punkte eintragen (Nullstellen, Hoch-, Tief-, Wendepunkte), dann mit dem Grenzverhalten verbinden; an einer Wendestelle keinen Extrempunkt zeichnen – dort ist der Graph am steilsten.
 91      Auswendig (Teil A): „Übersetzungstabelle“ und „Skizze aus Eigenschaften“ – [GOST-OHiMi 2.2] „Bestimmung des qualitativen Verlaufs des Funktionsgraphen der Ableitungsfunktion aus dem Funktionsgraphen der Funktion (und umgekehrt)“, „qualitative Beschreibung des Verlaufs des Funktionsgraphen“; „Grad“ folgt aus der Potenzregel (Ableitungsregeln, ableitungsregeln.md).
 92      Formelsammlung: Analysis – Ableitung [FS-IQB 1.2]; die Übersetzungstabelle steht nicht in der Formelsammlung – [FS] offen
 93  Quelle: eigene Formulierung nach [GOST Q1 L4] „den Ableitungsgraphen aus dem Funktionsgraphen entwickeln“ mit den drei Zusammenhängen und [GOST-OHiMi 2.2] „Bestimmung des qualitativen Verlaufs des Funktionsgraphen der Ableitungsfunktion aus dem Funktionsgraphen der Funktion (und umgekehrt)“; [FOS] „grafische Darstellung“, „graphisches Differenzieren“; Zahlenbeispiele eigen (Ermessen); [LS-AA EP II 3, EP IV 5, QP IV 6].
 94
 95  Einheit 5 (Kurvenuntersuchung im Sachzusammenhang):
 96      Übersetzen: „größter oder kleinster Wert“ → Hoch- oder Tiefpunkt von f, an den Rändern des Bereichs mit den Randwerten vergleichen · „ändert sich gerade nicht“ → f' = 0 · „nimmt am stärksten zu“ → Wendepunkt im steigenden Bereich (Hochpunkt von f') · „nimmt am stärksten ab“ → Wendepunkt im fallenden Bereich (Tiefpunkt von f') · „wächst immer langsamer“ → f' > 0 und f'' < 0.
 97      Einheiten: f' hat die Einheit von f je Einheit von x (Meter je Sekunde, Stück je Tag).
 98        B(t) = −t³ + 12t² (Bestand in Stück, t in Tagen, 0 ≤ t ≤ 8): B'(t) = −3t² + 24t; B''(t) = −6t + 24 = 0 ⇔ t = 4 → nach 4 Tagen wächst der Bestand am stärksten, mit B'(4) = 48 Stück je Tag; der größte Bestand liegt am Rand bei t = 8 mit B(8) = 256 Stück.
 99      Antwortsatz: Zahl mit Einheit und Bedeutung – „Nach 4 Tagen ist die Zunahme mit 48 Stück je Tag am größten.“ Ohne Sachbezug ist die Antwort unvollständig.
100      Auswendig (Teil A): keine – die zitierten Anlagenpunkte [GOST-OHiMi 2.2] betreffen Eigenschaften und Graphen, nicht den Sachzusammenhang; „Übersetzen“, „Einheiten“ und „Antwortsatz“ sind Arbeitsregeln für Teil B, gestützt auf die Kriterien von Einheit zwei und drei.
101      Formelsammlung: Analysis – Ableitung [FS-IQB 1.2]; [FS] offen
102  Quelle: eigene Formulierung nach [GOST Q1 L4] „lokale Änderungsrate auch in Sachzusammenhängen“, „Ableitungsfunktion auch in Sachzusammenhängen“, „Randextrema“ und [FOS] „Modellierung von Verläufen und Formen durch ganzrationale Funktionen im Sachzusammenhang“; Übersetzungsliste aus den Sachfragen der Rohdatei (Tauchroboter, Hormonspiegel, Laktat, Zuflussrate); Zahlenbeispiel eigen (Ermessen); [LS-AA EP IV 6].
103
104  ### Typische Fehler
105  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 150 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nur, wo die Kataloge das Muster stützen.
106  - Hinreichende Bedingung weggelassen: nur f'(x₀) = 0 gezeigt und die Art nicht begründet – das häufigste Muster in allen drei Profilen. [abi 2021-be-gk-A1.3a, 2024-bebb-gk-B2.1b, 2023-bebb-lk-A1.2b; iqb 2020MgrundlegendAAnalysis11-a, 2026MgrundlegendAAnalysis11-a, 2020MgrundlegendBAnalysisWTR1-1b, 2022MgrundlegendBAnalysisWTR2-1a, 2022MgrundlegendBAnalysisWTR2-2a; beim Wendepunkt abi 2021-be-gk-B2.1d, 2022-bebb-lk-B2.2d, iqb 2018MgrundlegendBAnalysisWTR-1a, 2018MerhoehtBAnalysisWTR1-1b, fhr 2019-C-1d, 2024-C-1e]
107  - Funktionswert statt Ableitung: f(x₀) berechnet und als Nachweis angesehen, oder die erste statt der zweiten Ableitung eingesetzt. [abi 2025-bebb-lk-A1.1a; iqb 2025MerhoehtAAnalysis12-a; fhr 2023-C-1d; FD Verwechslung von Funktions- und Ableitungswert, Vollrath/Weigand]
108  - Beim Ausklammern die Lösung x = 0 verloren oder durch x dividiert; beim Wurzelziehen nur die positive Lösung genommen. [fhr 2023-A-1b, 2022-C-1c, 2019-C-1c, 2024-B-2b, 2024-B-1e, 2024-C-1d; abi 2023-bebb-gk-A1.3a, 2024-bebb-gk-B2.2c, 2022-bebb-gk-B2.2b; FD Nullprodukt, Malle]
109  - Vorzeichen von f'' falsch gedeutet: positives f'' als Hochpunkt, Links- und Rechtskrümmung vertauscht, Hoch- und Tiefpunkt vertauscht. [fhr 2026-B-1d, 2022-B-1c, 2022-B-1d, 2025-A-1c, 2024-B-1f, 2022-C-1d, 2026-B-1e]
110  - Ableitungsstufe verwechselt: Art des Extrempunkts am Vorzeichen von f' statt f'' beurteilt, Monotonie nach f'' statt f' angegeben, f'' als Ableitung von f statt von f' gebildet. [fhr 2025-A-1e, 2020-A-1c, 2021-A-1c; abi 2026-bb-gk-B2.1c]
111  - Sattelstelle übersehen: bei f''(x₀) = 0 auf einen Extrempunkt geschlossen ohne f''' oder Vorzeichenwechsel; doppelte Nullstelle von f' als Extremstelle geführt; von f'(x₀) = 0 unbesehen auf eine Extremstelle geschlossen; die Sattelstelle als bloßen Wendepunkt gezählt. [fhr 2026-C-1e, 2025-C-1d, 2019-A-1c, 2021-B-2c, 2026-C-1f, 2021-B-2d, 2020-C-1c, 2019-A-1d; abi 2022-bebb-lk-B2.1g, 2022-bebb-lk-B2.1h; iqb 2024MgrundlegendBAnalysisWTR2-1a, 2021MgrundlegendBAnalysisWTR-1a]
112  - Stelle statt Wert: die Extremstelle als maximale Höhe angegeben, die Wendestelle ohne Funktionswert, f'(x₀) als y-Koordinate, Differenz der Extremstellen statt der Funktionswerte. [fhr 2024-C-2d, 2023-C-2a, 2023-A-2e, 2024-C-1e, 2024-B-2b; abi 2023-bebb-gk-B2.2c; iqb 2023MgrundlegendBAnalysisWTR2-2b; FD Argument-Wert-Verwechslung, Vollrath/Weigand]
113  - Ableitungsfehler bei Produkten mit e-Funktion: Produktregel weggelassen, innere Ableitung vergessen, den e-Faktor als möglichen Nullfaktor behandelt. Gehört zu ableitungsregeln.md, schlägt aber in jeder GK-Extrempunktrechnung durch. [abi 2018-be-gk-B1.2d, 2019-be-gk-B2.2b, 2021-be-gk-B2.2d, 2023-bebb-gk-B2.1f, 2024-bebb-gk-B2.1c, 2025-bebb-gk-B2.2b, 2025-bebb-lk-B2.2g, 2024-bebb-gk-A1.7a; iqb 2021MgrundlegendAAnalysis2-a, 2025MerhoehtBAnalysisWTR2-1a, 2025MgrundlegendBAnalysisWTR2-1b, 2022MerhoehtBAnalysisWTR1-2c]
114  - Stärkste Abnahme mit f' statt f'' gesucht (Nullstelle von f' als stärkste Abnahme, Maximum statt Wendepunkt); Wendepunkt als Richtungswechsel, als Beginn der Abnahme oder als Zeitpunkt des Höchstwerts gedeutet; Wendepunkt im steigenden statt im fallenden Bereich gewählt. [abi 2018-be-gk-B1.1d, 2019-be-gk-B2.2c, 2022-bebb-gk-B2.1l; iqb 2022MerhoehtBAnalysisWTR1-1b, 2019MgrundlegendBAnalysisWTR1-1c, 2022MgrundlegendBAnalysisWTR2-2c, 2024MgrundlegendBAnalysisWTR1-2b, 2023MgrundlegendBAnalysisWTR2-2a, 2023MgrundlegendBAnalysisWTR1-2b, 2025MerhoehtBAnalysisMMS1-2b; fhr 2021-B-2d]
115  - Rand und Bereich vergessen: beim größten Wert nur die Nullstellen der Ableitung untersucht, Randwerte nicht verglichen; eine Lösung außerhalb des Sachbereichs nicht verworfen; das Maximum am falschen Rand angenommen. [abi 2018-bb-ea-B2.1g, 2025-bebb-lk-B2.2g, 2021-be-gk-B2.1g, 2018-be-gk-B1.1d; fhr 2026-B-2c, 2019-C-2b; iqb 2018MgrundlegendBAnalysisWTR-2f, 2018MerhoehtBAnalysisWTR1-2e, 2020MgrundlegendBAnalysisWTR2-1a, 2024MgrundlegendBAnalysisWTR1-1b]
116  - Graph und Ableitungsgraph verwechselt: Werte von g statt g' berechnet, den Graphen von f' als f gezeichnet, Extremstellen von f nicht als Nullstellen von f' gezeichnet, f'(x₀) als Funktionswert abgelesen, Hochpunkt von g als Extrempunkt von f gedeutet; an einer Wendestelle ein Extrempunkt statt eines Wendepunkts gezeichnet. [abi 2019-be-gk-B2.1f, 2020-be-gk-B2.1e, 2020-be-gk-B2.2d, 2022-bebb-gk-A1.2a, 2023-bebb-gk-B2.1d, 2023-bebb-lk-A1.1b; iqb 2019MerhoehtAAnalysis2-a, 2019MerhoehtAAnalysis2-b, 2023MerhoehtAAnalysis11-b; FD Graph-als-Bild und Zuordnungs- gegen Kovariationsaspekt, Vollrath/Weigand]
117  - Verlauf im Sachzusammenhang falsch gelesen: einen flachen Abschnitt als Abnahme gedeutet, obwohl der Graph nirgends fällt; Wertebereich oder Wertemenge ohne das Grenzverhalten angegeben. [iqb 2018MgrundlegendBAnalysisWTR-2b, 2018MerhoehtBAnalysisWTR1-2b, 2025MgrundlegendBAnalysisWTR2-2a; abi 2025-bebb-gk-B2.2e, 2026-bb-ea-B2.1c]
118  - Maßstab und Einheiten: Koordinaten als Zentimeter genommen, Maße in Längeneinheiten gelassen, Radius statt Durchmesser als Breite, Halbkreise bei der Breite vergessen, ein Wert als Meter gedeutet, der ein Zeitvorsprung ist. [abi 2023-bebb-gk-B2.1k, 2024-bebb-gk-B2.1h, 2026-bb-gk-B2.1f; iqb 2026MgrundlegendBAnalysisMMS2-1e, 2024MgrundlegendBAnalysisWTR2-2c; fhr 2020-A-2b]
119  - Intervalle unvollständig: nur zwei statt aller Krümmungs- oder Monotonieintervalle, das unbeschränkte Intervall vergessen, offene statt abgeschlossene Intervalle, Vorzeichen nicht an Probestellen geprüft, Grenze bei null statt an der Extremstelle. [fhr 2019-A-1e, 2024-B-1f, 2025-A-1c, 2020-C-1d; iqb 2025MgrundlegendBAnalysisWTR1-1a; abi 2023-bebb-gk-B2.1e]
120  - Existenz nicht begründet: „genau einen“ ohne Argument, Monotonie über eine Definitionslücke hinweg behauptet, gerechnet statt begründet (h'' berechnet, Nullstelle exakt gesucht), f'(x₀) = 0 an einer einzelnen Stelle als Gegenargument gegen die Monotonie gewertet. [abi 2022-bebb-lk-B2.1b, 2018-bb-ea-B2.2c, 2021-be-gk-B2.2e, 2019-be-gk-A1.1b; iqb 2026MgrundlegendBAnalysisWTR1-1a, 2020MgrundlegendAAnalysis11-b]
121
122  ### Für schwache Schüler
123  Mindeststoff (GK-Kern Q1 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q1 (Funktionsklassen ganzrational, Potenz- und natürliche Exponentialfunktionen): Einheit 1 Monotonie über das Vorzeichen von f' („Zusammenhang zwischen Monotonie und erster Ableitung“); Einheit 2 lokale und globale Extrema mit notwendiger und hinreichender Bedingung, Sattelpunkte, Randextrema; Einheit 3 Wendepunkte und Krümmungsverhalten über f''; Einheit 4 Ableitungsgraph aus dem Funktionsgraphen entwickeln mit den drei Zusammenhängen; Einheit 5 Änderungsrate und Ableitungsfunktion im Sachzusammenhang. Ohne Hilfsmittel (Anlage OHiMi 2.2, Prüfungsteil A): Extrempunkte und Wendepunkte mit notwendigem und hinreichendem Kriterium, Monotonie, Krümmungsverhalten, qualitativer Verlauf, Ableitungsgraph aus dem Funktionsgraphen und umgekehrt. LK-Zusatz (für GK Vorrat): Wurzel-, ln-, sin/cos-Funktionen, Funktionsscharen, Ortskurven von Extrem- und Wendepunkten (kein Original in der Rohdatei), graphisches Ableiten. Niveaustufe H der E-Phase [RLP H]: „Beschreiben des Änderungsverhaltens ausgewählter ganzrationaler Funktionen durch eine Skizze der Ableitungsfunktion und Angeben markanter Punkte (z. B. Hoch-, Tief-, Wendepunkte)“ – das ist Blatt-0-Stoff (Voraussetzung fünf), kein Mindeststoff dieses Eintrags. RLP FOS (fhr) [FOS Pflichtthema 2 „Funktionsuntersuchungen“]: „Monotonie und 1. Ableitung, lokale Extrempunkte, Krümmung und 2. Ableitung, Wendepunkte und Sattelpunkte, grafische Darstellung“ – Einheit 1 bis 3 rechnerisch mit ganzrationalen Funktionen bis zum fünften Grad ohne Produkt- und Kettenregel; Einheit 4 nur „grafische Darstellung“ und „graphisches Differenzieren“, Einheit 5 nur „Modellierung von Verläufen und Formen durch ganzrationale Funktionen im Sachzusammenhang“ – beide in Ansätzen. Vorrat: alles außerhalb dieser Listen, für fhr insbesondere die e-Funktions-Produkte, für GK ln, sin und Wurzel. COSH [COSH, nachrangig]: der Mindestanforderungskatalog führt Monotonie, Extrema, Wendepunkte und Kurvendiskussion unter Analysis – deckt sich mit dem FOS-Mindeststoff, kein zusätzlicher Posten.
124  Grundvorstellung (Blatt 0) [GOST Eingangsvoraussetzung L4, MO]: Die Ableitung ist die Steigung, die man am Graphen abliest – nicht eine zweite Funktion, die man nur ausrechnet. „Hier ist der Graph einer Funktion, kein Term. Lege ein Lineal als Tangente an und wandere von links nach rechts. Sage an jeder markierten Stelle laut: steigt, fällt oder waagerecht – und ob es gerade steiler oder flacher wird. Trage darunter für jede Stelle nur ein Zeichen ein: plus, minus oder null. Wo wechselt das Zeichen? Was ist an diesen Stellen mit dem Graphen? Und wo ist der Graph am steilsten?“ Wer an einem Hochpunkt „plus“ einträgt, weil der Wert dort groß ist, wer am steilsten Stück „null“ schreibt oder wer Steigung und Höhe nicht auseinanderhält, braucht das vor jeder Rechnung: Der Wert von f sagt, wie hoch – der Wert von f' sagt, wie steil. Verständnis, nicht Verfahren; Ermessen in der Aufgabenform, amtlich in der Vorstellung. [GOST Eingangsvoraussetzung L4 „Änderungsverhalten … Skizze des Graphen der Änderungsfunktion“; MO-Logik: Vorstellung vor Verfahren; abi 2022-bebb-gk-A1.2a Fehlerquelle „Ableitungswert als Funktionswert abgelesen“; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
125  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei, FD; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
126  - Monotonie (Einheit 1): „steigt, fällt, waagerecht“ am Graphen ankreuzen (Vorstufe, Grundvorstellung) → zu einer gegebenen Ableitung das Vorzeichen in einem Intervall angeben und daraus steigt oder fällt ablesen (Grundfall, viermal, Ableitung als Gerade oder Parabel gegeben) → Ableitung selbst bilden, Nullstellen berechnen und die Monotonieintervalle mit abgeschlossenen Grenzen angeben (ganzrational dritten Grades, zwei Nullstellen) → drei Intervalle bei zwei Extremstellen, Vorzeichen je Intervall an einer Probestelle prüfen → Monotonie aus einem bekannten Extrempunkt angeben, ohne zu rechnen (abi 2023-bebb-gk-B2.1e) → Nachweis am Term: die Ableitung als Quadrat oder e-Term erkennen und „für alle x größer null“ begründen (GK; iqb 2026MgrundlegendBAnalysisWTR1-1a, abi 2024-bebb-gk-A1.7a) → daraus folgern, dass es keinen Extrempunkt gibt (abi 2018-bb-ea-B2.2c, iqb 2019MerhoehtAAnalysis2-a) → Prüfungshöhe: Monotonieintervalle und Wertebereich einer Differenzfunktion auf einem Intervall über die Ableitung ermitteln und die Länge der Monotoniebereiche zweier Modellfunktionen vergleichen (abi 2021-be-gk-B2.1g, iqb 2023MgrundlegendBAnalysisWTR2-2d, Niveau II bis III); fhr-Zielmarke: Monotonieintervalle im Anschluss an die Extrempunktberechnung angeben (fhr 2021-A-1c, 2024-C-1d, 2025-C-1d).
127  - Extrempunkte berechnen (Einheit 2): „gegeben oder gesucht“ und „welcher Nachweis“ ankreuzen (Vorstufe) → Ableitung null setzen und die Stellen einer quadratischen Ableitung mit der Lösungsformel berechnen (Grundfall, viermal, ganzrational dritten Grades) → Art über das Vorzeichen von f'' entscheiden und den Funktionswert berechnen, den Punkt mit beiden Koordinaten schreiben → Ableitung durch Ausklammern von x lösen und die Stelle null nicht verlieren (ganzrational vierten Grades; fhr 2023-A-1b, 2022-C-1c, abi 2024-bebb-gk-B2.2c) → Ausklammern von x² und die Sattelstelle über f''' erkennen (fhr 2025-C-1d) → eine gegebene Extremstelle zum Abspalten nutzen, Polynomdivision (fhr 2023-C-1c) → Produkt aus Polynom und e-Funktion: Produktregel, e-Faktor als nullstellenfrei erkennen, nur den Polynomfaktor null setzen (GK; abi 2025-bebb-gk-B2.2b, 2019-be-gk-B2.2b) → Art aus Abbildung oder Sachzusammenhang begründen, wenn die hinreichende Bedingung erlassen ist (abi 2018-be-gk-B1.2d, iqb 2020MgrundlegendBAnalysisWTR2-1a) → größten Wert auf einem Intervall mit den Randwerten vergleichen (abi 2018-bb-ea-B2.1g, 2025-bebb-lk-B2.2g) → Wertebereich aus dem globalen Tiefpunkt und dem Grenzverhalten (abi 2022-bebb-lk-B2.1h) → Prüfungshöhe: Lage und Art aller lokalen Extrempunkte eines Produkts aus Polynom und e-Funktion bestimmen (abi 2021-be-gk-B2.2d, Niveau II, sechs Punkte); fhr-Zielmarke: Art und Koordinaten aller Extrempunkte einer Funktion fünften Grades mit Sattelpunkt und Monotonieverhalten (fhr 2025-C-1d, 2026-C-1e, Niveau II bis III).
128  - Extrempunkte nachweisen (Einheit 2): „gegeben oder gesucht“ ankreuzen (Vorstufe) → für eine genannte Stelle f' bilden und f' an der Stelle gleich null zeigen (Grundfall, viermal) → f'' an der Stelle auswerten und die Art benennen → den Funktionswert des vorgegebenen Punktes bestätigen (abi 2021-be-gk-B2.1c) → den Vorzeichenwechsel von f' statt f'' als Nachweis führen (iqb 2020MgrundlegendAAnalysis11-a, abi 2022-bebb-gk-B2.1a) → mit der gegebenen Angabe „f'' ungleich null“ die hinreichende Bedingung schließen (abi 2025-bebb-lk-A1.1a, iqb 2025MerhoehtAAnalysis12-a) → Sattelstelle ausschließen oder nachweisen: doppelte Nullstelle von f' ohne Vorzeichenwechsel, f''' ungleich null (abi 2022-bebb-lk-B2.1g, fhr 2021-B-2c) → „genau einen“ Tiefpunkt über die streng monotone Ableitung begründen (LK; abi 2022-bebb-lk-B2.1b) → Extremstelle ohne Rechnung in ein Intervall einschließen über die Vorzeichen von f' an den Intervallenden (abi 2019-be-gk-A1.1b) → Prüfungshöhe: Extremstelle einer Logarithmusfunktion über die Ableitung oder die Symmetrie begründen (LK; abi 2023-bebb-lk-A1.2b) und Aussagen zu Stellen mit waagerechter Tangente allgemein beurteilen (fhr 2020-C-1c, 2019-A-1c, Niveau III).
129  - Wendepunkte und Krümmung (Einheit 3): „welcher Nachweis“ ankreuzen (Vorstufe) → zweite und dritte Ableitung einer ganzrationalen Funktion bilden (Grundfall, viermal) → f'' null setzen, die Wendestelle berechnen, f''' ungleich null zeigen, den Funktionswert berechnen (kubisch, eine Wendestelle; fhr 2023-A-2e, 2024-C-1e) → zwei Wendestellen durch Wurzelziehen oder Ausklammern (Grad vier; fhr 2019-C-1d, 2026-B-1e) → Krümmungsintervalle: Wendestellen als Grenzen, Vorzeichen von f'' an Probestellen, links- und rechtsgekrümmt zuordnen, unbeschränkte Intervalle nicht vergessen (fhr 2019-A-1e, 2024-B-1f, 2025-A-1c) → Wendetangente mit der Steigung f' an der Wendestelle aufstellen (fhr 2021-B-1d, iqb 2018MgrundlegendBAnalysisWTR-1a) → Wendepunkt an vorgegebener Stelle nachweisen und den Funktionswert bestätigen (fhr 2023-C-1d, abi 2024-bebb-gk-B2.1c) → Wendepunkt, der zugleich Sattelpunkt ist: zusätzlich f' gleich null zeigen (fhr 2024-B-1e, 2026-C-1f) → Produkt aus Polynom und e-Funktion: f'' mit Produkt- und Kettenregel, Nullstellen des Polynomfaktors (GK; abi 2023-bebb-gk-B2.1f) → zweiten Wendepunkt über die Punktsymmetrie angeben (LK; abi 2022-bebb-lk-B2.2d) → Prüfungshöhe: Existenz eines Wendepunkts ohne Rechnung aus Tiefpunkt und Grenzverhalten mit einer Skizze begründen (abi 2021-be-gk-B2.2e, Niveau III) und einen Wendepunkt über den Vorzeichenwechsel von f'' aus der Kettenregel am Graphen nachweisen (LK; iqb 2019MerhoehtAAnalysis2-b, Niveau III); fhr-Zielmarke: Wendepunkte einer Funktion fünften Grades mit Polynomdivision und die Krümmungsintervalle mit Begründung (fhr 2026-C-1f, 2020-C-1d, Niveau II bis III).
130  - Graph und Ableitungsgraph (Einheit 4): „steigt, fällt, waagerecht“ und die Vorzeichenleiste (Vorstufe, Grundvorstellung) → zu einem gezeichneten Graphen von f die Nullstellen von f' markieren und das Vorzeichen von f' je Abschnitt eintragen (Grundfall, viermal) → Werte für einen Ableitungswert und eine Wendestelle am Graphen ablesen (abi 2022-bebb-gk-A1.2a) → einen Punkt mit vorgegebenen Bedingungen an f' und f'' auf dem Graphen markieren und begründen (abi 2022-bebb-gk-A1.2b) → Graphen von f und f' aus berechneten Punkten in ein vorgegebenes Koordinatensystem einzeichnen, Extremstellen von f als Nullstellen von f' (abi 2020-be-gk-B2.2d, 2019-be-gk-B2.1f) → einen möglichen Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren, die Wendestelle als Extremstelle von f' lesen (abi 2023-bebb-lk-A1.1b, iqb 2023MerhoehtAAnalysis11-b) → den Mindestgrad aus den Eigenschaften der Ableitung begründen (abi 2023-bebb-lk-A1.1a) → die Lage zweier Graphen aus dem Graphen ihrer Differenz beschreiben (iqb 2018MgrundlegendBAnalysisWTR-1f) → Prüfungshöhe: Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen (abi 2024-bebb-gk-B2.1d, Niveau III) und eine Aussage über gemeinsame Punkte von Tangente und Graph an der eigenen Skizze beurteilen (abi 2023-bebb-gk-B2.2e, Niveau III); fhr-Zielmarke: keine – der RLP FOS führt nur „grafische Darstellung“ und „graphisches Differenzieren“, die Rohdatei kein fhr-Original in dieser Einheit.
131  - Sachzusammenhang (Einheit 5): „was heißt das mathematisch“ ankreuzen (Vorstufe) → den Verlauf eines abgebildeten Graphen abschnittweise in Worten des Sachzusammenhangs beschreiben: steigt, fällt, flach, Sättigung (Grundfall, viermal; iqb 2018MgrundlegendBAnalysisWTR-2b, 2025MgrundlegendBAnalysisWTR2-2a) → den Wendepunkt am Graphen als Zeitpunkt stärkster Zunahme oder Abnahme deuten (iqb 2022MgrundlegendBAnalysisWTR2-2c, 2024MgrundlegendBAnalysisWTR1-2b) → den Funktionswert an der Stelle stärkster Abnahme ablesen (iqb 2023MgrundlegendBAnalysisWTR1-2b) → den größten Wert berechnen: f' null, Funktionswert, Antwort mit Einheit (fhr 2023-C-2a, 2024-C-2d) → das Maximum an vorgegebener Stelle nachweisen und den Wert berechnen (abi 2022-bebb-gk-B2.1j) → die stärkste Abnahme rechnen: f'' null setzen, Lösung im Sachbereich wählen, Wert von f und f' mit Einheit (abi 2019-be-gk-B2.2c, iqb 2019MgrundlegendBAnalysisWTR1-1c) → Randwerte und Bereichsgrenzen beachten, Lösungen außerhalb verwerfen (fhr 2026-B-2c, iqb 2018MgrundlegendBAnalysisWTR-2f) → Maßstab: Koordinaten in Längen umrechnen, Breite aus den Nullstellen, Höhe aus dem Hochpunkt (fhr 2020-A-2b, abi 2026-bb-gk-B2.1f, iqb 2026MgrundlegendBAnalysisMMS2-1e) → Prüfungshöhe: einen fremden Lösungsweg (Differenzfunktion, Extremwertschritte) im Sachzusammenhang deuten oder dazu die Aufgabenstellung formulieren (iqb 2024MgrundlegendBAnalysisWTR2-2c, 2023MgrundlegendBAnalysisWTR2-2b, Niveau II) und den Ableitungswert an der Wendestelle als stärksten Anstieg einer Rate deuten (iqb 2025MerhoehtBAnalysisMMS1-2b); fhr-Zielmarke: steilster Anstieg eines Dachs über den Wendepunkt (fhr 2021-B-2d, Niveau III).
132
133  ### Prüfungsform (fhr / abi / iqb)
134  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md. Für fhr ist der Pool keine Vorgabe: dort gelten RLP FOS 2019 und der fhr-Katalog. Die Rohdatei zählt 174 Zeilen mit 76 Haupttypen (fhr 39 Zeilen, 9 Typen; abi 68 Zeilen, 41 Typen; iqb 67 Zeilen, 41 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (gemeinsame Liste abi/iqb).
135  fhr (39 Zeilen; fhr-Themen „Extrem- und Sattelpunkte“ 23, „Wendepunkte“ 13, „Monotonie und Krümmung“ 3) [FOS, fhr-Katalog]: Extrem- und Sattelpunkte über zweite Ableitung (17, E2) · Wendepunkte über zweite Ableitung (11, E3) · Krümmungsverhalten angeben (3, E3) · Aussagen zu Stellen mit waagerechter Tangente beurteilen (2, E2) · Gegebene Stelle als Extremstelle nachweisen (2, E2) · Funktionswert im Sachzusammenhang deuten (1, E5) · Maximale Höhe im Sachzusammenhang berechnen (1, E5) · Punktprobe am Graphen (1, E3) · Steilsten Anstieg über den Wendepunkt bestimmen (1, E5). Muster: zwei Rechentypen tragen 28 von 39 Zeilen – in jedem Jahrgang 2019–2026 eine Extrempunkt- und eine Wendepunktaufgabe an einer ganzrationalen Funktion dritten bis fünften Grades, sieben bis elf Punkte, mit Nachweis über f'' bzw. f''', oft mit Monotonie- oder Krümmungsintervallen als Anhang; Sattelpunkte als Erschwernis (2019-A, 2021-B, 2024-B, 2025-C, 2026-C); dazu der Nachweis an genannter Stelle mit den weiteren Tiefpunkten (2021-B-1c) und die Auswahl des Wendepunkts unter vier vorgegebenen Punkten (2021-A-1d); Niveau II, Niveau III bei Polynomdivision, Sattelpunkt und den beiden Aussagenaufgaben.
136  abi (68 Zeilen, 41 Typen; Landeshefte be-gk, bb-ea, bb-gk, bebb-gk, bebb-lk 2017–2026, davon 7 aus den CAS-Fassungen bb-ea 2018 und be-gk 2017 und 2018) [abi-Katalog]: Lage und Art aller lokalen Extrempunkte bestimmen (9, E2) · Extrempunkt eines Produkts aus Polynom und e-Funktion berechnen (6, E2) · Wendepunkte über die zweite Ableitung berechnen (5, E3) · Graphen einer Funktion in ein Koordinatensystem einzeichnen (4, E4) · Extrempunkt an vorgegebener Stelle nachweisen (3, E2) · Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen (3, E5) · Maximalen Neigungswinkel über die Wendestelle berechnen (2, E5) · Monotonie über das Vorzeichen der Ableitung am Term nachweisen (2, E1) · Stellen mit maximalem Funktionswert einschließlich Rand bestimmen (2, E2) · je 1: Abstand zweier Extrempunkte verschiedener Graphen mit einer Schranke vergleichen (E2) · Achsenschnittpunkte angeben und Hochpunkt aus der gegebenen Ableitung begründen (E2) · Anstieg null nachweisen und fehlende Extremstelle über die doppelte Nullstelle der Ableitung ohne Rechnung begründen (E2) · Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen (E4) · Aussagen über Funktions- und Ableitungswert nahe dem Tiefpunkt ohne Rechnung beurteilen (E2) · Einzigen Tiefpunkt über die streng monotone Ableitung nachweisen und berechnen (E2) · Existenz eines Wendepunkts aus Tiefpunkt und Grenzverhalten über eine Skizze begründen (E3) · Extrempunkte berechnen und ihre Verbindungsgerade als Winkelhalbierende nachweisen (E2) · Extremstelle einer Logarithmusfunktion über die Ableitung oder die Symmetrie begründen (E2) · Extremstelle über den Vorzeichenwechsel der Ableitung in ein Intervall einschließen (E2) · Extremstellen aus den Nullstellen der Ableitung berechnen (E2) · Fehlende Extrempunkte über eine positive Ableitung begründen (E1) · Graphen skizzieren und Aussage über die Anzahl gemeinsamer Punkte von Tangente und Graph beurteilen (E4) · Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (E4) · Größten Funktionswert über Monotonie, Grenzverhalten und Symmetrie begründen und Wertemenge angeben (E2) · Lage eines Graphen zwischen zwei Geraden auf einem Intervall über die Differenzfunktionen nachweisen (E2) · Lage eines Punktes aus Bedingungen an Funktionswert und Ableitung am Graphen beschreiben (E4) · Maximum eines Bestands an vorgegebener Stelle im Sachzusammenhang nachweisen (E5) · Maße und Masse eines umschließenden Quaders eines Rotationskörpers aus Hochpunkt und Bereich mit Maßstab berechnen (E5) · Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen (E4) · Mittleren Wert einer periodisch schwankenden Größe am Graphen ablesen (E5) · Monotonieintervalle und Wertebereich einer Differenzfunktion auf einem Intervall über die Ableitung ermitteln (E1) · Monotonieverhalten aus einem bekannten Extrempunkt angeben (E1) · Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen (E5) · Verlauf eines Graphen im Sachzusammenhang beschreiben (E5) · Volumen eines umschließenden Quaders aus den Achsenschnittpunkten mit Maßstab berechnen (E5) · Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten (E5) · Wendepunkt mit negativer Steigung am Graphen markieren und begründen (E4) · Wendepunkt mit vorgegebenen Koordinaten über die zweite Ableitung nachweisen und den symmetrischen Wendepunkt angeben (E3) · Werte für einen Ableitungswert und eine Wendestelle am Graphen ablesen (E4) · Wertebereich einer ganzrationalen Funktion über den globalen Tiefpunkt ermitteln (E2) · Zweite Ableitung nachweisen und Wendepunkt an vorgegebener Stelle zeigen (E3). Muster: Teil B (mit Hilfsmitteln) trägt 60 von 68 Zeilen, meist an Produkten aus Polynom und e-Funktion mit vorgegebener Ableitung – darunter Lage und Art aller Extrempunkte am Skisprunghang, an einer Funktion dritten Grades und an der ausmultiplizierten Form (2018-be-gk-B1.1c, 2023-bebb-gk-B2.2b, 2020-be-gk-B2.2c), die Extrempunkte mit der Winkelhalbierenden als Verbindungsgerade (2025-bebb-gk-B2.1b), der Abstand zweier Hochpunkte gegen eine Schranke (2021-be-gk-B2.1f), der Winkel an der Wendestelle aus zwei Teilwinkeln (2021-be-gk-B2.2l, Niveau III) und die Sensorlage der Modelleisenbahn (2026-bb-gk-B2.1h); aus dem Heft 2017-be-gk das Brückenteil der Holzeisenbahn mit den Extrempunkten als Eckpunkten und dem größten Anstiegswinkel gegen die Schranke 32° (2017-be-gk-B1.1a, 2017-be-gk-B1.1c) und der Graph der Dachkante ohne vorgegebenes Koordinatensystem (2017-be-gk-B1.2b); nur in der CAS-Fassung 2018 die Stellen größten Radius einschließlich des Rands (2018-bb-ea-cas-B2.1g, Niveau III); in den Berliner CAS-Fassungen 2017 und 2018 dieselben Brücken-, Skisprung- und Höhenprofilaufgaben ohne vorgegebene Ableitung – Lage und Art aller Extrempunkte samt Zuordnung zu Eck- bzw. Tiefpunkt (2017-be-gk-cas-B1.1a, 2018-be-gk-cas-B1.1c) und der höchste Punkt des Höhenprofils ohne Verzicht auf die hinreichende Bedingung (2018-be-gk-cas-B1.2d) –, zwei Landes-Dubletten nur mit anderer Punktzahl (größter Anstiegswinkel 2017-be-gk-cas-B1.1c, stärkstes Gefälle 2018-be-gk-cas-B1.1d) und ohne WTR-Gegenstück der Nachweis, dass die Brückenkante auf [0; 20] im Streifen zwischen zwei Geraden liegt, mit dem kleinsten vertikalen Abstand (2017-be-gk-cas-B1.1e, zehn Punkte, Niveau II); Teil A (ohne Hilfsmittel, 8 Zeilen, zwei bis drei Punkte) prüft den Nachweis an vorgegebener Stelle, den Monotonienachweis am Term, das Ablesen und Markieren am Graphen und die Skizze aus Eigenschaften – genau die OHiMi-Inhalte. Ein Viertel der Zeilen sind Begründungs- und Beurteilungsaufgaben ohne Rechnung (Niveau III bei 2021-be-gk-B2.2e, 2023-bebb-gk-B2.2e, 2024-bebb-gk-B2.1d, 2018-bb-ea-B2.1g, 2021-be-gk-B2.2l, 2018-bb-ea-cas-B2.1g). Niveau I 12, II 50, III 6.
137  iqb (67 Zeilen, 41 Typen; Pool 2017–2026, grundlegend 39 und erhöht 28 Zeilen, Teil A 11 und Teil B 56 Zeilen, davon 3 MMS und 12 CAS) [iqb-Katalog]: Extrempunkt an vorgegebener Stelle nachweisen (6, E2) · Extrempunkt eines Produkts aus Polynom und e-Funktion berechnen (6, E2) · Graphen einer Funktion in ein Koordinatensystem einzeichnen (4, E4) · Verlauf eines Graphen im Sachzusammenhang beschreiben (4, E5) · Maximalen Neigungswinkel über die Wendestelle berechnen (3, E5) · Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten (3, E5) · Gewinnbereich als Bereich zwischen den Schnittstellen von Erlösgerade und Kostengraph zeichnerisch bestimmen (2, E5) · Krümmungsverhalten aus der zweiten Ableitung deuten (2, E3) · Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen (2, E5) · Monotonie über das Vorzeichen der Ableitung am Term nachweisen (2, E1) · Wendepunkt an vorgegebener Stelle nachweisen und Wendetangente aufstellen (2, E3) · Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen (2, E5) · je 1: Ableitungswert an der Wendestelle als stärksten Anstieg der Rate im Sachzusammenhang deuten (E5) · Abstand zweier Extrempunkte über die Punktsymmetrie berechnen (E2) · Abstand zwischen Parabel und waagerechter Gerade über den Scheitel beschreiben (E2) · Achsenschnittpunkte angeben und Hochpunkt aus der gegebenen Ableitung begründen (E2) · Anzahl der Schnittpunkte von Geraden durch den Wendepunkt mit dem Graphen nach der Steigung unterscheiden (E3) · Aufgabenstellung zu Extremstellen und Wertedifferenz aus dem Lösungsweg formulieren und erläutern (E5) · Berührung des Graphen mit der x-Achse über die Extrempunkte begründen (E2) · Differenzfunktion und ihr Maximum aus einem Lösungsweg im Sachzusammenhang deuten (E5) · Extremstelle zwischen zwei Stellen mit gleichem Funktionswert ohne Rechnung begründen (E2) · Extremstellen berechnen und Monotonieverhalten angeben (E1) · Fehlende Extrempunkte über eine positive Ableitung begründen (E1) · Funktionswert an der Stelle stärkster Abnahme am Graphen ablesen (E5) · Gemeinsamen Punkt zweier Graphen über gleiche Flächeninhalte indirekt begründen (E4) · Gerade durch die beiden Wendepunkte aufstellen und parallele Gerade mit genau einem gemeinsamen Punkt einzeichnen (E3) · Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (E4) · Hochpunkt mit vorgegebenen Koordinaten und waagerechte Tangente im Ursprung rechnerisch nachweisen (E2) · Lage und Art aller lokalen Extrempunkte bestimmen (E2) · Lage zweier Graphen aus dem Graphen ihrer Differenzfunktion beschreiben (E4) · Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen und Steigung und Achsenabschnitt angeben (E4) · Länge der Monotoniebereiche zweier Modellfunktionen vergleichen und eine Aussage beurteilen (E1) · Maximum eines Bestands an vorgegebener Stelle im Sachzusammenhang nachweisen (E5) · Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen (E4) · Nullstellen einer e-Funktion nachweisen und Tiefstelle berechnen (E2) · Nullstellen und Extremstelle einer Parabel berechnen (E2) · Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen (E5) · Tiefpunkt angeben und Fehlen weiterer Extrempunkte über die Ableitung nachweisen (E2) · Wendepunkt über den Vorzeichenwechsel der zweiten Ableitung aus der Kettenregel am Graphen nachweisen (E3) · Wendestelle nachweisen und Winkel der Wendetangente mit der x-Achse über die Steigung −1 zeigen (E3) · Wendestellen einer Sinusfunktion als ganzzahlig nachweisen und die beiden Wendetangentensteigungen zeigen (E3). Muster: der Pool prüft die Kurvenuntersuchung selten als Ganzes und fast nie als „Untersuchen Sie“; die Zeilen sind kurze Nachweise (zwei bis vier Punkte) an vorgegebener Stelle, Deutungen am Graphen und Sachzusammenhänge (Tauchroboter, Temperatur, Phosphor, Laktat, Kosten und Erlös); elf Zeilen sind wortgleiche Dubletten in abi (2022-bebb-gk-B2.1a/j/l, 2023-bebb-lk-A1.1a/b, 2025-bebb-gk-B2.2b/e, 2025-bebb-lk-A1.1a, 2022-bebb-lk-B2.2c, 2026-bb-gk-B2.1f und ihre iqb-Gegenstücke). Erhöhtes Niveau bringt die LK-Klassen (Sinusfunktion 2022MerhoehtBAnalysisWTR1-2c, f' = e^g 2019MerhoehtAAnalysis2). Einzeln, bis zum Nachzug 2026-09-28 ohne id im Eintrag: der Abstand der Extrempunkte über die Punktsymmetrie (2026MgrundlegendAAnalysis11-b), die Geraden durch den Wendepunkt nach der Steigung (2018MerhoehtAAnalysis12-b), der Neigungswinkel der Rutsche (2024MerhoehtBAnalysisWTR3-1c), die Parabel mit Nullstellen, Extremstelle und Abstand zur Geraden (2023MgrundlegendBAnalysisWTR1-1a, 2023MgrundlegendBAnalysisWTR1-1b), der Tiefpunkt an vorgegebener Stelle (2023MgrundlegendBAnalysisWTR2-1b), die Wendetangente mit 45° (2026MgrundlegendBAnalysisMMS2-1c), die Monotonie mit ergänzten Achsen (2022MerhoehtBAnalysisWTR2-1c), der Gewinnbereich (2018MgrundlegendBAnalysisWTR-2e, 2018MerhoehtBAnalysisWTR1-2d) und die Gerade durch die beiden Wendepunkte (2021MgrundlegendBAnalysisWTR-1b); aus den Stapeln 2017 die Flusssenke mit Wassertiefe und größtem Neigungswinkel (2017MgrundlegendBAnalysisWTR-1e, 2017MgrundlegendBAnalysisWTR-1h), das Schiff mit tiefstem Kielpunkt und steilster Stelle (2017MerhoehtBAnalysisCAS1-2b, 2017MerhoehtBAnalysisCAS1-2c) und Cocktail- und Sektglas mit konvexem Bereich, Formvergleich und gezeichneten Graphen (2017MerhoehtBAnalysisCAS2-2b, 2017MerhoehtBAnalysisCAS2-3a, 2017MerhoehtBAnalysisCAS2-3c); aus den CAS-Stapeln des Nachzugs 2026-09-29 drei Skizzen – ein Scharmitglied (2018MerhoehtBAnalysisCAS1-1a), eine Wurzelfunktion samt Symmetrie für alle Parameter (2018MerhoehtBAnalysisCAS3-1a) und der Temperaturverlauf mit Deutung für große Zeiten (2017MgrundlegendBAnalysisCAS-1c), alle Niveau I –, das Glukosemodell vierten Grades mit Lage und Art aller Extrempunkte (2018MerhoehtBAnalysisCAS2-1a) und der Schluss ohne Rechnung, dass zwischen zwei Stellen gleichen Werts eine Extremstelle liegt (2018MerhoehtBAnalysisCAS2-1d, Niveau III), das Vorzeichen des Parameters aus der Linkskrümmung des Hängeseils (2018MerhoehtBAnalysisCAS3-2d) und der einzige Extrempunkt des Temperaturmodells mit Messwertvergleich (2017MgrundlegendBAnalysisCAS-1b). Niveau I 25, II 36, III 6.
138  Zielmarke: Einheit 1 – fhr: Monotonieintervalle als Anhang der Extrempunktaufgabe (2021-A-1c, 2024-C-1d, 2025-C-1d, Niveau II); abi/iqb: Monotonienachweis am Term in Teil A (2024-bebb-gk-A1.7a, 2026MgrundlegendBAnalysisWTR1-1a, Niveau I) und Monotonieintervalle einer Differenzfunktion (2021-be-gk-B2.1g, Niveau II). Einheit 2 – fhr: Art und Koordinaten aller Extrempunkte einer Funktion vierten oder fünften Grades mit Sattelpunkt (2025-C-1d, 2026-C-1e, 2023-C-1c, Niveau II bis III); abi: Lage und Art aller lokalen Extrempunkte eines e-Funktions-Produkts (2021-be-gk-B2.2d) und Hochpunkt mit Produktregel (2019-be-gk-B2.2b, 2025-bebb-gk-B2.2b); iqb: Extrempunkt an vorgegebener Stelle in Teil A (2020MgrundlegendAAnalysis11-a, 2026MgrundlegendAAnalysis11-a, Niveau I) und die Extremstelle zwischen zwei Stellen gleichen Werts ohne Rechnung (2018MerhoehtBAnalysisCAS2-1d, Niveau III). Einheit 3 – fhr: Wendepunkte mit f''' und Krümmungsintervalle (2026-C-1f, 2020-C-1d, 2024-B-1e); abi: Wendepunkte eines e-Funktions-Produkts (2023-bebb-gk-B2.1f) und Existenzbegründung mit Skizze (2021-be-gk-B2.2e, Niveau III); iqb: Wendepunkt an vorgegebener Stelle mit Wendetangente (2018MgrundlegendBAnalysisWTR-1a, 2018MerhoehtBAnalysisWTR1-1b). Einheit 4 – fhr: kein Original; abi: Skizze aus Eigenschaften und Aussage beurteilen (2023-bebb-gk-B2.2e, 2023-bebb-lk-A1.1b), Graphen von f und f' einzeichnen (2020-be-gk-B2.2d); iqb: Skizze und Mindestgrad in Teil A (2023MerhoehtAAnalysis11-a/b). Einheit 5 – fhr: maximale Höhe und steilster Anstieg (2023-C-2a, 2024-C-2d, 2021-B-2d); abi: stärkste Abnahme über f'' (2018-be-gk-B1.1d, 2019-be-gk-B2.2c); iqb: Wendepunkt deuten (2022MgrundlegendBAnalysisWTR2-2c, 2023MgrundlegendBAnalysisWTR2-2a) und Lösungsweg im Sachzusammenhang deuten (2024MgrundlegendBAnalysisWTR2-2c).
````

## 2 Originale (84)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2021-B-1c (fhr-katalog.csv)

jahr 2021 · papier B · punkte 8 · format Rechnung · antwort Zahl
- gegeben: f(x) = 0,2x^4 − 4,45x^2 + 20; x aus IR
- gesucht: Nachweis, dass x = 0 eine Extremstelle von f ist|alle weiteren Extremstellen|vollständige Koordinaten der Tiefpunkte von Gf
- verfahren: erste und zweite Ableitung bilden, x = 0 in beide einsetzen und über das Vorzeichen der zweiten Ableitung die Extremstelle nachweisen, dann x ausklammern und die beiden weiteren Stellen berechnen, dort die zweite Ableitung prüfen und die Funktionswerte bestimmen
- fehlerquelle: beim Ausklammern die Lösung x = 0 als weitere Extremstelle mitzählen, obwohl sie schon nachgewiesen wurde

### 2021-A-1d (fhr-katalog.csv)

jahr 2021 · papier A · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR; zur Auswahl stehen W1(−1/3; 925/108), W2(7/3; 1445/108), W3(8/3; 400/27) und W4(8/3; 350/11)
- gesucht: Prüfung, welcher der vier Punkte der Wendepunkt des Graphen ist, mit mathematischer Begründung
- verfahren: die Wendestelle aus der zweiten Ableitung bestimmen, über die von null verschiedene dritte Ableitung den Wendepunkt bestätigen und den Funktionswert berechnen, dann mit den vier Kandidaten vergleichen
- fehlerquelle: W4 wählen, weil die x-Koordinate stimmt, und den Funktionswert nicht nachrechnen

### 2018-be-gk-B1.1c (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 6 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m; der Hang beginnt am Punkt C(0 | 50). Der Punkt U liegt an der tiefsten Stelle des Aufsprunghangs. Als Kontrollergebnis ist g'(x) = 1/1000 · (1/500 · x³ − 20x) angegeben.
- gesucht: Lage und Art aller lokalen Extrempunkte des Graphen von g; Entscheidung, welcher Extrempunkt dem Punkt U entspricht
- verfahren: g'(x) = 0 setzen und x ausklammern: x · (x² − 10 000) = 0 liefert x = −100, x = 0 und x = 100. Mit der zweiten Ableitung g''(x) = 1/1000 · (3/500 · x² − 20) die Art bestimmen: g''(0) < 0 ergibt einen Hochpunkt, g''(±100) > 0 je einen Tiefpunkt. Der Aufsprunghang beginnt bei C, liegt also rechts der y-Achse; U ist der Tiefpunkt bei x = 100.
- fehlerquelle: nur die Nullstellen der Ableitung angeben, ohne die Art über die zweite Ableitung zu bestimmen, oder den Tiefpunkt bei x = −100 übersehen

### 2023-bebb-gk-B2.2b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 6 · format Rechnung · antwort Zahl
- gegeben: Die Funktion f mit f(x) = x³ − 12x² + 45x − 50, x ∈ IR, auch schreibbar als f(x) = (x − 5) · (x² − 7x + 10).
- gesucht: Lage und Art aller Extrempunkte des Graphen von f
- verfahren: f'(x) = 0 ⇔ x² − 8x + 15 = 0 ⇔ x = 3 oder x = 5; f''(3) = −6 < 0 (Hochpunkt), f''(5) = 6 > 0 (Tiefpunkt); Funktionswerte f(3) = 4, f(5) = 0.
- fehlerquelle: die Art ohne zweite Ableitung oder Vorzeichenwechsel angeben; Funktionswerte vergessen

### 2020-be-gk-B2.2c (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 9 · format Rechnung · antwort Zahl
- gegeben: f(x) = −1/100 x³ + 3/50 x² + 3/20 x + 2/25 (ausmultiplizierte Form aus b)
- gesucht: Lage und Art der Extrempunkte des Graphen von f
- verfahren: f' = 0 lösen, f'' an den Stellen auswerten, Funktionswerte berechnen
- fehlerquelle: beim Normieren der quadratischen Gleichung die Vorzeichen kippen

### 2025-bebb-gk-B2.1b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 7 · format Rechnung · antwort Zahl|Text
- gegeben: f(x) = 2/25 x³ − 3/2 x, definiert in IR, Graph G_f; G_f hat genau zwei Extrempunkte
- gesucht: Koordinaten der Extrempunkte; Nachweis, dass die Gerade durch sie die Winkelhalbierende des II. und IV. Quadranten ist
- verfahren: f' = 0, Art über f'', Funktionswerte; Steigung −1 und Ursprung
- fehlerquelle: Winkelhalbierende des I. und III. Quadranten (y = x) angeben

### 2021-be-gk-B2.1f (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 4 · format Rechnung · antwort Text
- gegeben: f(x) = 1/12 x³ − x² + 3x und p(x) = −x² + 3,8x − 1,36, beide in IR; Graphen G_f und G_p (Parabel); Hochpunkt H(2 | 8/3) von G_f; der Scheitel von G_p ist ein Hochpunkt (ohne Nachweis)
- gesucht: Nachweis, dass der Abstand der beiden Hochpunkte größer als 5/12 ist
- verfahren: Scheitel von p über p' = 0, Abstand zu H berechnen und mit 5/12 vergleichen
- fehlerquelle: nur die Differenz der y-Werte 5/12 als Abstand nehmen (dann gleich, nicht größer)

### 2021-be-gk-B2.2l (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 6 · format Rechnung · antwort Zahl|Text
- gegeben: f(x) = (−1/10 x² + 2x) · e^(−0,1x) und h(x) = −3/4 x · e^(−0,1x), beide in IR; Graphen G und H; f''(x) = (−1/1000 x² + 3/50 x − 3/5) · e^(−0,1x); R(x_R | f(x_R)) mit x_R < 20 ist der Punkt, in dem G die Krümmungsart ändert; Kontrolle R(12,68 | 2,61); α ≈ 2,75° aus k
- gesucht: Nachweis, dass der Winkel δ = ∠S₂S₁R höchstens 18° beträgt
- verfahren: Wendestelle aus f'' = 0 (kleinere Lösung), Steigungswinkel der Sehne S₁R über den Tangens, δ als Summe mit dem Neigungswinkel der Linie S₁S₂
- fehlerquelle: δ nur als β nehmen und α vergessen (S₂ liegt unter der x-Achse)

### 2026-bb-gk-B2.1h (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Schienenverlauf einer Modelleisenbahn in der Draufsicht, symmetrisch zur x- und zur y-Achse; oberer Verlauf auf [−2; 0] durch G mit g(x) = 1/3 x³ + x² modelliert, A(−2 | 4/3); oberer und unterer Verlauf durch zwei Halbkreise verbunden, waagerecht anschließend; 1 LE = 1 m (Abbildung 3); Sensor in Q(x_Q | y_Q) mit y_Q = −g(−x_Q) und g'(−x_Q) = 0, x_Q ≠ 0
- gesucht: Beschreibung der Lage des Sensors mit Abbildung 3
- verfahren: Extremstelle von g bei −2, Spiegelung an beiden Achsen
- fehlerquelle: x_Q = −2 nehmen (Vorzeichen in −x_Q)

### 2017-be-gk-B1.1a (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 9 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Bauelements wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke des Bauteils liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. In den oberen Eckpunkten A und B geht die Oberkante ohne Knick in die waagerechten Anschlussschienen über. Kontrollangabe: f′(x) = −3/500 · x² + 3/25 · x sowie A(0 | f(0)) bzw. B(20 | f(20)).
- gesucht: Extrempunkte von f mit Nachweis ihrer Art; Begründung, warum die Extrempunkte mit den Eckpunkten A und B übereinstimmen müssen
- verfahren: f′(x) = 0 setzen und x ausklammern: x · (−3/500 · x + 3/25) = 0 liefert x = 0 und x = 20. Mit f″(x) = −3/250 · x + 3/25 die Art bestimmen: f″(0) > 0 Tiefpunkt, f″(20) < 0 Hochpunkt. Knickfreier Übergang in waagerechte Schienen heißt Steigung null in A und B, also f′ = 0 dort – die Eckpunkte sind die Stellen mit waagerechter Tangente.
- fehlerquelle: nur die Nullstellen der Ableitung angeben, ohne die Art über f″ nachzuweisen, oder den knickfreien Übergang nur über gleiche Höhe statt über gleiche Steigung begründen

### 2017-be-gk-B1.1c (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 6 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Bauelements wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke des Bauteils liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. f′(x) = −3/500 · x² + 3/25 · x. Für batteriebetriebene Lokomotiven darf der Anstiegswinkel an keiner Stelle größer als 32° sein; ein Nachweis mit hinreichender Bedingung ist nicht verlangt.
- gesucht: Punkt mit dem größten Anstieg; maximaler Anstiegswinkel und Entscheidung, ob das 32°-Kriterium erfüllt ist
- verfahren: Der größte Anstieg liegt, wo f′ maximal ist: f″(x) = −3/250 · x + 3/25 = 0 liefert x = 10. Den Punkt über f(10) angeben, die Steigung f′(10) berechnen und über tan α = f′(10) den Winkel bestimmen; mit 32° vergleichen.
- fehlerquelle: die Steigung 0,6 direkt mit 32 vergleichen, ohne sie in einen Winkel umzurechnen, oder den Hochpunkt als Punkt größten Anstiegs nennen

### 2017-be-gk-B1.2b (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. Bekannt sind der Schnittpunkt (0 | 1) mit der y-Achse und der Tiefpunkt T(1 | 0).
- gesucht: Graph von f im Intervall [0; 2]
- verfahren: Eine Wertetabelle mit Schrittweite 0,25 oder 0,5 anlegen, die markanten Punkte (0 | 1) und T(1 | 0) eintragen und den Graphen glatt verbinden.
- fehlerquelle: den Graphen bei x = 1 mit einem Knick statt mit waagerechter Tangente zeichnen oder unter die x-Achse führen

### 2018-bb-ea-cas-B2.1g (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea-cas · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Die Funktion f_0,65 mit f_0,65(x) = (x² + 0,65) · e^(0,5 − x) aus der Schar; ihr Graph schließt über [0; 3] mit der x-Achse eine Fläche ein (Abbildung 2). Durch Rotation dieser Fläche um die x-Achse entsteht ein Körper, der modellhaft einer liegenden, nach links geöffneten Vase entspricht; 1 LE = 1 dm. Die Vase nimmt an zwei verschiedenen Stellen einen maximalen Radius von ca. 1,07 dm an.
- gesucht: die beiden Stellen, an denen der Radius maximal ist, rechnerisch ermittelt
- verfahren: Der Radius an der Stelle x ist f_0,65(x). Nullstellen der Ableitung bestimmen: x² − 2x + 0,65 = 0 liefert x = 1 ± √0,35, davon ist x ≈ 0,41 ein lokales Minimum und x ≈ 1,59 ein lokales Maximum. Zusätzlich die Randwerte bei x = 0 und x = 3 vergleichen; der linke Rand liefert denselben gerundeten Radius wie das lokale Maximum.
- fehlerquelle: nur die Nullstellen der Ableitung untersuchen und die Randstelle x = 0 übersehen

### 2017-be-gk-cas-B1.1a (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 8 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. In den oberen Eckpunkten A und B geht die Oberkante ohne Knick in die waagerechten Anschlussschienen über. Kontrollangabe: A(0 | f(0)) bzw. B(20 | f(20)).
- gesucht: Extrempunkte von f mit Nachweis ihrer Art; Begründung, warum die Extrempunkte mit den Eckpunkten A und B übereinstimmen müssen
- verfahren: f′(x) = −3/500 · x² + 3/25 · x selbst bilden (von Hand oder mit dem CAS), null setzen und x ausklammern: x · (−3/500 · x + 3/25) = 0 liefert x = 0 und x = 20. Mit f″(x) = −3/250 · x + 3/25 die Art bestimmen: f″(0) > 0 Tiefpunkt, f″(20) < 0 Hochpunkt. Knickfreier Übergang in waagerechte Schienen heißt Steigung null in A und B, also f′ = 0 dort – die Eckpunkte sind die Stellen mit waagerechter Tangente.
- fehlerquelle: die Ableitung falsch bilden (etwa 3/50 · x statt 3/25 · x) oder die Art nicht über f″ nachweisen, oder den knickfreien Übergang nur über gleiche Höhe statt über gleiche Steigung begründen

### 2018-be-gk-cas-B1.1c (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 7 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m; der Hang beginnt am Punkt C(0 | 50). Der Punkt U liegt an der tiefsten Stelle des Aufsprunghangs.
- gesucht: Lage und Art aller lokalen Extrempunkte des Graphen von g; Entscheidung, welcher Extrempunkt dem Punkt U entspricht; mittlere Steigung des Aufsprunghangs zwischen C und U
- verfahren: g′(x) = 1/1000 · (1/500 · x³ − 20x) selbst bilden (oder mit dem CAS), null setzen und x ausklammern: x · (x² − 10 000) = 0 liefert x = −100, x = 0 und x = 100. Mit g″(x) = 1/1000 · (3/500 · x² − 20) die Art bestimmen: g″(0) < 0 Hochpunkt, g″(±100) > 0 je ein Tiefpunkt. Der Aufsprunghang beginnt bei C, liegt also rechts der y-Achse; U ist der Tiefpunkt bei x = 100. Die mittlere Steigung zwischen C(0 | 50) und U(100 | 0) als Differenzenquotient.
- fehlerquelle: den Tiefpunkt bei x = −100 übersehen, beim Ableiten den Vorfaktor 1/1000 verlieren oder die mittlere Steigung ohne Vorzeichen angeben

### 2018-be-gk-cas-B1.2d (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6, 1 LE = 1 km. Aus b ist f′(x) = (0,5 − 0,5x) · e^(−0,5x) bekannt.
- gesucht: Koordinaten des höchsten Punktes des Höhenprofils
- verfahren: f'(x) = 0 setzen; da e^(−0,5x) stets positiv ist, bleibt 0,5 − 0,5x = 0, also x = 1. Den Funktionswert f(1) = 2 · e^(−0,5) berechnen. Dass es ein Maximum ist, zeigt der Vorzeichenwechsel von f′ von plus nach minus bei x = 1 oder f″(1) < 0.
- fehlerquelle: den Exponentialfaktor als möglichen Nullfaktor behandeln und eine zweite Lösung angeben

### 2017-be-gk-cas-B1.1c (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke des Bauteils liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. f′(x) = −3/500 · x² + 3/25 · x. Für batteriebetriebene Lokomotiven darf der Anstiegswinkel an keiner Stelle größer als 32° sein; ein Nachweis mit hinreichender Bedingung ist nicht verlangt.
- gesucht: Punkt mit dem größten Anstieg; maximaler Anstiegswinkel und Entscheidung, ob das 32°-Kriterium erfüllt ist
- verfahren: Der größte Anstieg liegt, wo f′ maximal ist: f″(x) = −3/250 · x + 3/25 = 0 liefert x = 10. Den Punkt über f(10) angeben, die Steigung f′(10) berechnen und über tan α = f′(10) den Winkel bestimmen; mit 32° vergleichen.
- fehlerquelle: die Steigung 0,6 direkt mit 32 vergleichen, ohne sie in einen Winkel umzurechnen, oder den Hochpunkt als Punkt größten Anstiegs nennen

### 2018-be-gk-cas-B1.1d (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000) und g'(x) = 1/1000 · (1/500 · x³ − 20x), 1 LE = 1 m. Der Punkt K ist die Stelle des Aufsprunghangs mit dem stärksten Gefälle; für die x-Koordinate genügt die notwendige Bedingung.
- gesucht: Koordinaten des Punktes K
- verfahren: Das stärkste Gefälle liegt dort, wo g' minimal wird, also bei g''(x) = 0. Aus 3/500 · x² − 20 = 0 folgt x² = 10 000/3 und im Bereich des Hangs x = 100/√3 ≈ 57,7. Den zugehörigen Funktionswert durch Einsetzen in g bestimmen.
- fehlerquelle: die erste statt der zweiten Ableitung null setzen, oder die negative Lösung x = −57,7 angeben, die nicht auf dem Aufsprunghang liegt

### 2017-be-gk-cas-B1.1e (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 10 · format Begründung|Rechnung · antwort Text|Zahl
- gegeben: Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. Um Material zu sparen, wird das Brückenteil aus zwei Holzbrettern hergestellt; das eine Brett wird von den Geraden g_u(x) = 45/100 · x − 2 und g_o(x) = 45/100 · x + 1 begrenzt.
- gesucht: Nachweis, dass der Graph von f für x ∈ [0; 20] vollständig in dem Bereich zwischen g_u und g_o liegt; die Stelle im Bereich 0 < x < 20, an der der vertikale Abstand der Geraden g_u zum Graphen von f am geringsten ist, und dieser minimale Abstand
- verfahren: Die Differenzen g_o(x) − f(x) = x · (x − 15)²/500 und d(x) = f(x) − g_u(x) = −x³/500 + 3/50 · x² − 9/20 · x + 3 bilden (mit dem CAS faktorisieren). Die erste ist für x ≥ 0 nicht negativ (null nur bei 0 und 15, dort berührt f die Gerade g_o). Für die zweite d′(x) = −3/500 · (x − 5) · (x − 15) = 0 lösen: lokales Minimum bei x = 5 mit d(5) = 2 > 0, lokales Maximum bei x = 15; mit den Randwerten d(0) = 3 und d(20) = 2 ist d auf [0; 20] positiv. Die Stelle 5 liefert den kleinsten vertikalen Abstand im Inneren.
- fehlerquelle: den Nachweis nur an einzelnen Stellen führen, den Randwert d(20) = 2 mit dem inneren Minimum verwechseln oder den Abstand senkrecht zur Geraden statt vertikal messen

### 2021-be-gk-B2.2e (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 3 · format Begründung|Zeichnen · antwort Text|Grafik
- gegeben: h(x) = −3/4 x · e^(−0,1x) mit lim h = 0 (x → +∞), lim h = +∞ (x → −∞), h'(x) = (3/40 x − 3/4) · e^(−0,1x)
- gesucht: Begründung mithilfe einer Skizze, dass H einen Wendepunkt besitzt
- verfahren: Tiefpunkt bei x = 10 im IV. Quadranten; danach steigt H gegen 0 – ohne Krümmungswechsel unmöglich
- fehlerquelle: h'' berechnen statt zu begründen

### 2023-bebb-gk-B2.2e (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 4 · format Zeichnen|Begründung · antwort Grafik|Text
- gegeben: Die Funktion f mit f(x) = x³ − 12x² + 45x − 50, x ∈ IR, auch schreibbar als f(x) = (x − 5) · (x² − 7x + 10). Bekannt aus b und c: H(3 | 4), T(5 | 0), W(4 | 2); Aussage: Jede Tangente an den Graphen von f hat zwei gemeinsame Punkte mit dem Graphen von f.
- gesucht: Skizze des Graphen für 0 ≤ x ≤ 7; Beurteilung der Aussage mithilfe der Skizze
- verfahren: Graph durch (0 | −50), steigend zum Hochpunkt (3 | 4), fallend über den Wendepunkt (4 | 2) zum Tiefpunkt (5 | 0), dann steigend (f(7) = 20). Die Tangente im Wendepunkt hat nur W mit dem Graphen gemeinsam, die Aussage ist falsch; die Tangenten in H und T (y = 4 bzw. y = 0) haben je zwei gemeinsame Punkte.
- fehlerquelle: die Aussage mit der Tangente in S (zwei Punkte, siehe d) bestätigen statt ein Gegenbeispiel suchen

### 2024-bebb-gk-B2.1d (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 6 · format Begründung · antwort Text
- gegeben: f(x) = (x − 2) · e^(−x/2 + 3), definiert in IR, mit f'(x) = (−x/2 + 2) · e^(−x/2 + 3); Abbildung 1 zeigt G_f und G_f'; Wendepunkt (6 | 4); Aussage I: die Gerade durch A(2 | 0) und B(6 | f(6)) ist senkrecht zur am stärksten fallenden Tangente; Aussage II: jede Parallele zur x-Achse y = k mit k ≤ −1 hat mit G_f' keine gemeinsamen Punkte
- gesucht: Entscheidung je Aussage mit Begründung
- verfahren: I: Steigung der stärksten Tangente ist f'(6) = −1, Steigung AB = 1, Produkt −1; II: f' nimmt bei 6 das Minimum −1 an, y = −1 berührt G_f'
- fehlerquelle: bei II den Randfall k = −1 übersehen

### 2018-bb-ea-B2.1g (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 7 · format Rechnung · antwort Zahl
- gegeben: Die Funktion f_0,65 mit f_0,65(x) = (x² + 0,65) · e^(0,5 − x) aus der Schar; ihr Graph schließt über [0; 3] mit der x-Achse eine Fläche ein (Abbildung 2). Durch Rotation dieser Fläche um die x-Achse entsteht ein Körper, der modellhaft einer liegenden, nach links geöffneten Vase entspricht; 1 LE = 1 dm. Die Vase nimmt an zwei verschiedenen Stellen einen maximalen Radius von ca. 1,07 dm an.
- gesucht: die beiden Stellen, an denen der Radius maximal ist
- verfahren: Der Radius an der Stelle x ist f_0,65(x). Nullstellen der Ableitung bestimmen: x² − 2x + 0,65 = 0 liefert x = 1 ± √0,35, davon ist x ≈ 0,41 ein lokales Minimum und x ≈ 1,59 ein lokales Maximum. Zusätzlich die Randwerte bei x = 0 und x = 3 vergleichen; der linke Rand liefert denselben Radius wie das lokale Maximum.
- fehlerquelle: nur die Nullstellen der Ableitung untersuchen und die Randstelle x = 0 übersehen

### 2022-bebb-gk-B2.1a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 5 · format Kurzantwort|Begründung · antwort Zahl|Text
- gegeben: f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x)
- gesucht: Schnittpunkte des Graphen mit den Koordinatenachsen; Begründung, dass der Graph einen Hochpunkt hat, und dessen Koordinaten
- verfahren: x + 2 = 0 und f(0); Nullstelle von f' mit Vorzeichenwechsel von + nach −, f(−1)
- fehlerquelle: Hochpunkt ohne Vorzeichenwechsel oder zweite Ableitung begründen

### 2023-bebb-lk-A1.1a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 2 · format Begründung · antwort Text
- gegeben: ganzrationale, nicht lineare Funktion f in IR: Nullstelle x1; f'(x2) = 0 und f''(x2) ≠ 0; f' hat ein Minimum an der Stelle x3; Lage von x1, x2, x3 in der Abbildung
- gesucht: Begründung, dass der Grad von f mindestens 3 ist
- verfahren: aus dem Minimum von f' folgt Grad von f' mindestens 2, also Grad von f mindestens 3
- fehlerquelle: mit der Nullstelle x1 oder der Extremstelle x2 allein argumentieren (Grad 2 reicht dafür)

### 2025-bebb-gk-B2.2b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: f(x) = (2 − x) · e^x
- gesucht: Koordinaten des Hochpunkts
- verfahren: Produktregel, f' = 0, einsetzen
- fehlerquelle: Produktregel ohne die Ableitung von 2 − x

### 2025-bebb-lk-A1.1a (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 2 · format Rechnung · antwort Text
- gegeben: f(x) = 1/4 x³ − 3x, definiert in IR; es gilt f''(2) ≠ 0
- gesucht: Nachweis, dass 2 eine Extremstelle von f ist
- verfahren: f' bilden und f'(2) = 0 zeigen; zusammen mit f''(2) ≠ 0 folgt die Extremstelle
- fehlerquelle: f(2) = −4 berechnen und als Nachweis ansehen

### 2022-bebb-lk-B2.2c (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 5 · format Rechnung|Zeichnen · antwort Grafik
- gegeben: f und f' wie in a, b; Abbildung 1 ohne Achsen
- gesucht: Monotonieverhalten rechnerisch; Koordinatenachsen mit Skalierung in Abbildung 1
- verfahren: Nullstellen von f' und Vorzeichen, Achsen durch den Symmetriepunkt legen, Skalierung über (1 | 1)
- fehlerquelle: Achsen so legen, dass der Ursprung nicht auf dem Graphen liegt

### 2026-bb-gk-B2.1f (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Rechnung · antwort Text
- gegeben: Schienenverlauf einer Modelleisenbahn in der Draufsicht, symmetrisch zur x- und zur y-Achse; oberer Verlauf auf [−2; 0] durch G mit g(x) = 1/3 x³ + x² modelliert, A(−2 | 4/3); oberer und unterer Verlauf durch zwei Halbkreise verbunden, waagerecht anschließend; 1 LE = 1 m (Abbildung 3)
- gesucht: Nachweis, dass der Schienenverlauf auf eine Platte 2,7 m × 6,7 m passt
- verfahren: Höhe 2 · 4/3, Breite 2 · (2 + 4/3)
- fehlerquelle: Halbkreise bei der Breite vergessen (Breite 4)

### 2022MerhoehtBAnalysisWTR1-2c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 4 · format Rechnung · antwort Term
- gegeben: Wendepunkte sind die Punkte mit y-Koordinate 1
- gesucht: Nachweis ganzzahliger Wendestellen; Steigung dort −π/2 oder +π/2
- verfahren: s(x) = 1 lösen, Ableitung an den Wendestellen auswerten
- fehlerquelle: innere Ableitung π/4 vergessen

### 2026MgrundlegendAAnalysis11-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: f(x) = x^3 − 3x, definiert in IR; Graph G; G ist symmetrisch zum Koordinatenursprung; G hat einen Hochpunkt mit der x-Koordinate −1
- gesucht: Abstand zwischen Hoch- und Tiefpunkt von G
- verfahren: f(−1) = 2 berechnen, Hochpunkt H(−1; 2); wegen der Punktsymmetrie ist der Tiefpunkt T(1; −2); Abstand als Länge der Strecke HT, gleich dem Doppelten des Abstands von H zum Ursprung
- fehlerquelle: den Tiefpunkt neu über die Ableitung berechnen statt die Symmetrie zu nutzen, oder nur den Abstand von H zum Ursprung angeben

### 2018MerhoehtAAnalysis12-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Kurzantwort · antwort Text
- gegeben: Gf mit Wendepunkt W(1 | 0) und Wendetangente der Steigung 1 (aus a); Geraden durch W mit positiver Steigung m
- gesucht: Anzahl der Schnittpunkte dieser Geraden mit Gf in Abhängigkeit von m
- verfahren: am Graphen: Geraden flacher als die Wendetangente schneiden dreimal, steilere nur in W
- fehlerquelle: m = 1 zum Fall „drei Schnittpunkte“ zählen

### 2024MerhoehtBAnalysisWTR3-1c (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Rechnung · antwort Text
- gegeben: f'(x) = −0,3x · e^{−0,1x}, f''(x) = 0,03 · (x − 10) · e^{−0,1x}; Kriterium II: nirgends Neigung über 60°
- gesucht: rechnerische Prüfung von Kriterium II
- verfahren: Wendestelle aus f'' = 0, Winkel aus f'(10)
- fehlerquelle: Winkel am Anfang (f'(0) = 0) prüfen

### 2023MgrundlegendBAnalysisWTR1-1a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: r(x) = −(x² − x − 1) in IR; Graph in Abbildung 1
- gesucht: Nullstellen und Extremstelle von r
- verfahren: Quadratische Gleichung lösen, Extremstelle als Mitte der Nullstellen
- fehlerquelle: Vorzeichen beim Auflösen der Klammer

### 2023MgrundlegendBAnalysisWTR1-1b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: r wie in a; Gerade y = 4
- gesucht: Vorgehen zur Berechnung des Abstands zwischen Graph von r und Gerade
- verfahren: y-Koordinate des Hochpunkts bestimmen und von 4 subtrahieren
- fehlerquelle: Abstand an einer beliebigen Stelle statt am Hochpunkt

### 2023MgrundlegendBAnalysisWTR2-1b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 4 · format Rechnung · antwort Term
- gegeben: f wie in a; zwei Extrempunkte
- gesucht: Nachweis eines Tiefpunkts an der Stelle √12
- verfahren: Erste Ableitung an der Stelle √12 gleich null, zweite Ableitung positiv
- fehlerquelle: (√12)² falsch berechnet

### 2026MgrundlegendBAnalysisMMS2-1c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga-mms · punkte 3 · format Rechnung · antwort Term
- gegeben: G hat genau einen Wendepunkt; Behauptung: Wendestelle −2/3, Wendetangente schließt mit der x-Achse 45° ein
- gesucht: Nachweis beider Aussagen
- verfahren: Zweite Ableitung an der Stelle −2/3 null, erste Ableitung dort −1
- fehlerquelle: Steigung −1 nicht mit 45° in Verbindung bringen

### 2022MerhoehtBAnalysisWTR2-1c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 5 · format Rechnung|Zeichnen · antwort Grafik
- gegeben: f und f' wie in a, b; Abbildung 1 ohne Achsen
- gesucht: Monotonieverhalten rechnerisch; Koordinatenachsen mit Skalierung in Abbildung 1
- verfahren: Nullstellen von f' und Vorzeichen, Achsen durch den Symmetriepunkt legen, Skalierung über (1 | 1)
- fehlerquelle: Achsen so legen, dass der Ursprung nicht auf dem Graphen liegt

### 2018MgrundlegendBAnalysisWTR-2e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 4 · format Zeichnen|Kurzantwort · antwort Grafik|Zahl
- gegeben: Kostenfunktion K(x) = x³ − 12x² + 50x + 20, 0 ≤ x ≤ 9, K(x) in 1000 Euro für die Produktion von x Kubikmetern einer Flüssigkeit; Abbildung 3 zeigt den Graphen von K; E(x) = 23x, G = E − K
- gesucht: Graph von E in Abbildung 3; Bereich der verkauften Menge mit Gewinn, aus der Darstellung
- verfahren: Gerade durch (0 | 0) und (9 | 207) einzeichnen; zwischen den Schnittpunkten liegt E über K
- fehlerquelle: den Bereich links von 4 mitnehmen

### 2018MerhoehtBAnalysisWTR1-2d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 4 · format Zeichnen|Kurzantwort · antwort Grafik|Zahl
- gegeben: Kostenfunktion K(x) = x³ − 12x² + 50x + 20, 0 ≤ x ≤ 9, K(x) in 1000 Euro für die Produktion von x Kubikmetern einer Flüssigkeit; Abbildung 2 zeigt den Graphen von K; E(x) = 23x, G = E − K
- gesucht: Graph von E in Abbildung 2; Bereich der verkauften Menge mit Gewinn
- verfahren: Gerade einzeichnen, Schnittstellen ablesen
- fehlerquelle: Bereich links von 4 mitnehmen

### 2021MgrundlegendBAnalysisWTR-1b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 7 · format Rechnung|Zeichnen · antwort Term|Grafik
- gegeben: f(x) = −5/16 x⁴ + 5x³, in IR definiert; die Abbildung zeigt den Graphen von f
- gesucht: Gleichung der Geraden g durch die beiden Wendepunkte; in der Abbildung eine zu g parallele Gerade, die für 0 ≤ x ≤ 8 mit dem Graphen genau einen Punkt gemeinsam hat
- verfahren: Wendestellen berechnen, g aus (0 | 0) und (8 | 1280); Parallele als Tangente an den Bogen zwischen den Wendepunkten einzeichnen
- fehlerquelle: Vorzeichenwechsel von f'' bei 0 nicht prüfen; Parallele durch beide Randpunkte zeichnen

### 2017MgrundlegendBAnalysisWTR-1e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Querschnitt einer Senke mit Fluss: Profillinie f(x) = −5x^2 · e^x + 1 für −6 <= x <= 0; linke Uferzone waagerecht in Höhe f(−6) links von x = −6, rechte Uferzone waagerecht in Höhe 1 rechts von x = 0 (Strecken parallel zur x-Achse, lückenlos an den Graphen anschließend); die Wasseroberfläche ist ein Abschnitt der x-Achse; 1 LE = 1 m; gegeben f'(x) = −5x · (2 + x) · e^x, f''(x) = −10e^x − 20x · e^x − 5x^2 · e^x und die Stammfunktion F(x) = x − 5 · (x^2 − 2x + 2) · e^x; Abbildung 1
- gesucht: Tiefe des Wassers an der tiefsten Stelle der Senke
- verfahren: An der Abbildung die Tiefstelle zwischen −2,5 und −1,5 eingrenzen, dort f'(x) = 0 mit der faktorisierten Ableitung lösen (x = −2) und f(−2) berechnen; die Wasseroberfläche liegt auf der x-Achse
- fehlerquelle: die Nullstelle x = 0 der Ableitung (Rand der Senke) als Tiefstelle nehmen oder die Tiefe von der Uferzone aus messen

### 2017MgrundlegendBAnalysisWTR-1h (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Querschnitt einer Senke mit Fluss: Profillinie f(x) = −5x^2 · e^x + 1 für −6 <= x <= 0; linke Uferzone waagerecht in Höhe f(−6) links von x = −6, rechte Uferzone waagerecht in Höhe 1 rechts von x = 0 (Strecken parallel zur x-Achse, lückenlos an den Graphen anschließend); die Wasseroberfläche ist ein Abschnitt der x-Achse; 1 LE = 1 m; gegeben f'(x) = −5x · (2 + x) · e^x, f''(x) = −10e^x − 20x · e^x − 5x^2 · e^x und die Stammfunktion F(x) = x − 5 · (x^2 − 2x + 2) · e^x; betrachtet wird die Profillinie zwischen dem tiefsten Punkt der Senke (x = −2) und ihrem rechten Rand (x = 0)
- gesucht: Größe des größten Neigungswinkels der Profillinie gegenüber der Horizontalen in diesem Bereich
- verfahren: Die Stelle größter Steigung ist Wendestelle: f''(x) = 0 ⇔ x^2 + 4x + 2 = 0, im Bereich x = −2 + √2; dort tan α = f'(−2 + √2)
- fehlerquelle: die Lösung −2 − √2 außerhalb des Bereichs nehmen oder tan α mit f statt mit f' ansetzen

### 2017MerhoehtBAnalysisCAS1-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Längsschnitt eines Schiffs mit horizontalem Deck; im Koordinatensystem mit Ursprung an der Bugspitze B und x-Achse entlang der Decklinie beschreibt k(x) = −0,3x^2 · e^(−0,2x) für 0 <= x <= 20 die Kiellinie; 1 LE = 1 m
- gesucht: Höhendifferenz in Metern zwischen dem tiefsten Punkt des Kiels und dem Endpunkt des Kiels am Heck
- verfahren: k'(x) = 0 im Inneren liefert x = 10 (Minimum); k(20) − k(10) berechnen
- fehlerquelle: den Betrag k(10) als Höhendifferenz angeben und den Endpunkt am Heck vergessen

### 2017MerhoehtBAnalysisCAS1-2c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Längsschnitt eines Schiffs mit horizontalem Deck; im Koordinatensystem mit Ursprung an der Bugspitze B und x-Achse entlang der Decklinie beschreibt k(x) = −0,3x^2 · e^(−0,2x) für 0 <= x <= 20 die Kiellinie; 1 LE = 1 m; der Kiel hat in einem Punkt seinen größten Neigungswinkel gegen die Horizontale
- gesucht: Größe dieses Neigungswinkels
- verfahren: Nach der Abbildung liegt der Punkt zwischen Bug und tiefstem Punkt; k''(x) = 0 für 0 < x < 10 liefert x = 10 − 5√2; tan α = k'(10 − 5√2)
- fehlerquelle: die zweite Wendestelle 10 + 5√2 nehmen oder den Winkel an der Bugspitze berechnen

### 2017MerhoehtBAnalysisCAS2-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Cocktailglas der Serie: Längsschnitt f_3(x) = −9/512 · x^4 + 27/32 · x^2 für −2√6 <= x <= 2√6, Rotationsachse auf der y-Achse, 1 LE = 1 cm; die Form eines Glases heißt in einem Bereich konvex, wenn der zugehörige Graph dort linksgekrümmt ist
- gesucht: x-Koordinaten des Bereichs, in dem das Cocktailglas konvex ist
- verfahren: f_3''(x) = 0 lösen; nach der Abbildung (oder f_3''(0) > 0) ist der untere Bereich zwischen den Wendestellen konvex
- fehlerquelle: die Bereiche außerhalb der Wendestellen als konvex angeben

### 2017MerhoehtBAnalysisCAS2-3a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Kurzantwort · antwort Text
- gegeben: Sektglas der Serie (12 cm hoch, Randdurchmesser 6 cm, k ≈ 4,06); ein Hochpunkt des Graphen der zugehörigen Funktion hat die Koordinaten x ≈ 5,7 und y ≈ 25,2, ein Wendepunkt x ≈ 3,3 und y ≈ 14,0; Cocktailglas f_3 für −2√6 <= x <= 2√6 mit Hochpunkten am Rand und Wendestellen ±2√2 im Glas
- gesucht: zwei wesentliche Unterschiede der Form des Sektglases zur Form des Cocktailglases im Sachzusammenhang unter Berücksichtigung der gegebenen Punkte
- verfahren: Beim Sektglas liegen Hochpunkt und Wendepunkt außerhalb von −3 <= x <= 3: der Rand läuft nicht waagerecht aus, und das Glas ist durchgehend konvex; das Cocktailglas endet im Hochpunkt und hat einen konkaven oberen Bereich
- fehlerquelle: Höhe und Breite vergleichen, ohne die gegebenen Punkte auf den Bereich des Glases zu beziehen

### 2017MerhoehtBAnalysisCAS2-3c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Das Sektglas steht mit vertikaler Rotationsachse und wird mit Flüssigkeit gefüllt; für −3 <= x <= 3 wird sein Längsschnitt näherungsweise durch p(x) = 4/3 · x^2 beschrieben; r(h) = 1/2 · √(3h), h ∈ IR0+
- gesucht: die Graphen von p und von r jeweils in ein geeignetes Koordinatensystem
- verfahren: Wertetabellen anlegen, Achsen passend skalieren und beide Graphen zeichnen
- fehlerquelle: r(h) als gespiegelte Parabel über die ganze h-Achse zeichnen

### 2018MerhoehtBAnalysisCAS1-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Für r ∈ IR, r ≠ 0, ist die Schar der in IR definierten Funktionen f_r mit f_r(x) = −1/r · x^2 + 4/r · x + 2 gegeben; r = 6
- gesucht: Skizze des Graphen von f_6 in einem Koordinatensystem
- verfahren: f_6(x) = −1/6 · x^2 + 2/3 · x + 2 aufstellen; Scheitel, Nullstellen und y-Achsenabschnitt berechnen oder eine Wertetabelle mit dem Rechner anlegen und die Parabel skizzieren
- fehlerquelle: die Parabel nach oben geöffnet zeichnen, weil der Faktor −1/r übersehen wird

### 2018MerhoehtBAnalysisCAS3-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Zeichnen|Begründung · antwort Grafik|Text
- gegeben: Für k ∈ IR+ ist die Schar der in IR definierten Funktionen f_k mit f_k(x) = √(k · x^2 + 400) gegeben; f_5(x) = √(5x^2 + 400)
- gesucht: Skizze des Graphen von f_5 und dessen Symmetrie; Begründung, dass der Graph von f_k für jedes k dieselbe Symmetrie hat
- verfahren: Wertetabelle von f_5 und Graph skizzieren; x kommt im Term nur als x^2 vor, also f_k(−x) = f_k(x) für alle x und alle k
- fehlerquelle: die Symmetrie nur am Graphen von f_5 ablesen und für f_k nicht allgemein begründen

### 2017MgrundlegendBAnalysisCAS-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 4 · format Zeichnen|Kurzantwort · antwort Grafik|Text
- gegeben: In einem Produktionsprozess werden Flüssigkeiten erhitzt, eine Zeit lang bei konstanter Temperatur gehalten und anschließend wieder abgekühlt; bei einem durchgehend gesteuerten Vorgang beschreibt f(t) = 23 + 20 · t · e^(−t/10) (t in Minuten seit Beginn, f(t) in °C) den Temperaturverlauf während des Erhitzens und des Abkühlens modellhaft
- gesucht: Skizze des Graphen von f für 0 <= t <= 80; Beschreibung des Verlaufs für große t und Deutung im Sachzusammenhang
- verfahren: Graph mit dem Rechner darstellen und skizzieren; 20 · t · e^(−t/10) geht für große t gegen 0, der Graph nähert sich y = 23; die Flüssigkeit kühlt auf 23 °C ab
- fehlerquelle: den Graphen gegen 0 statt gegen 23 laufen lassen

### 2018MerhoehtBAnalysisCAS2-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Gegeben ist die in IR definierte Funktion f mit f(x) = −1/10^6 · x^4 + 4/9375 · x^3 − 13/250 · x^2 + 8/5 · x + 140; zur Kontrolle: die Extremstellen sind 20, 100 und 200
- gesucht: Koordinaten und Art der Extrempunkte des Graphen von f
- verfahren: f'(x) = 0 lösen, das Vorzeichen von f'' an den drei Stellen bestimmen, Funktionswerte berechnen
- fehlerquelle: nur die Extremstellen ohne y-Koordinaten angeben oder die Art ohne zweite Ableitung aus der Kontrollangabe raten

### 2018MerhoehtBAnalysisCAS2-1d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Gegeben ist die in IR definierte Funktion f mit f(x) = −1/10^6 · x^4 + 4/9375 · x^3 − 13/250 · x^2 + 8/5 · x + 140; für 50 < x < 130 gibt es ein Paar von x-Werten im Abstand 60 mit übereinstimmenden Funktionswerten (x ≈ 69,2 und x ≈ 129,2)
- gesucht: Begründung, dass sich daraus schließen lässt, dass f für 50 < x < 130 mindestens eine Extremstelle hat
- verfahren: Eine ganzrationale, nicht konstante Funktion, die an zwei Stellen denselben Wert annimmt, muss dazwischen die Richtung wechseln; dort liegt eine Extremstelle
- fehlerquelle: mit der Extremstelle 100 aus Teilaufgabe 1 a statt mit den Informationen aus 1 c argumentieren

### 2018MerhoehtBAnalysisCAS3-2d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: Hängebrücke (Abbildung 1, schematisch) im Koordinatensystem mit 1 LE = 1 m, Materialstärken vernachlässigt: zwei vertikale Pfeiler bei x = −250 und x = 250 (Länge der Brücke 500 m), waagerechte Fahrbahn 12 m über der x-Achse (y = 12), das Drahtseil ist an den Pfeilern in 72,8 m Höhe über der x-Achse befestigt (Befestigungspunkte (−250; 72,8) und (250; 72,8)) und hängt symmetrisch zur y-Achse durch; gegeben sind die in IR definierten Funktionen g_r mit g_r(x) = r · x^2 + 20, r ∈ IR; ein zwischen den Befestigungspunkten unbelastet hängendes Drahtseil könnte mit einer der in IR definierten Funktionen h_s,t mit h_s,t(x) = s/2 · (e^(x/s) + e^(−x/s)) + t, s ∈ IR mit s ≠ 0, t ∈ IR, beschrieben werden (Hinweis: 1/2 · (e^x + e^(−x)) heißt in einigen CAS cosh(x), 1/2 · (e^x − e^(−x)) heißt sinh(x))
- gesucht: ob s für die Funktion h_s,t, die das unbelastete Drahtseil beschreiben könnte, positiv oder negativ ist, mit Begründung
- verfahren: Das durchhängende Seil verlangt einen linksgekrümmten Graphen; h_s,t''(x) = (e^(x/s) + e^(−x/s))/(2s) hat einen positiven Zähler, ist also genau für s > 0 positiv
- fehlerquelle: beim Ableiten den inneren Faktor 1/s vergessen und das Vorzeichen von s nicht aus der Krümmung erschließen

### 2017MgrundlegendBAnalysisCAS-1b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 4 · format Begründung|Rechnung · antwort Text|Zahl
- gegeben: In einem Produktionsprozess werden Flüssigkeiten erhitzt, eine Zeit lang bei konstanter Temperatur gehalten und anschließend wieder abgekühlt; bei einem durchgehend gesteuerten Vorgang beschreibt f(t) = 23 + 20 · t · e^(−t/10) (t in Minuten seit Beginn, f(t) in °C) den Temperaturverlauf während des Erhitzens und des Abkühlens modellhaft; Messwerte (Zeit in Minuten: Temperatur in °C): 0: 23,0; 2: 54,0; 4: 76,9; 10: 76,8; 15: 77,3; 20: 76,8; 40: 37,9; 60: 26,0; 80: 23,2
- gesucht: Nachweis, dass der Graph von f genau einen Extrempunkt hat; Vergleich der zugehörigen Temperatur mit den Messwerten
- verfahren: f'(t) = 2 · (10 − t) · e^(−t/10) ist nur für t = 10 null, f''(10) ≠ 0; f(10) berechnen und mit den Messwerten (höchstens 77,3 °C) vergleichen
- fehlerquelle: nur f'(10) = 0 zeigen, ohne weitere Nullstellen der Ableitung auszuschließen, oder f(10) nur mit dem Messwert bei t = 10 vergleichen

### 2021-A-1c (fhr-katalog.csv)

jahr 2021 · papier A · punkte 8 · format Rechnung|Kurzantwort · antwort Zahl|Text
- gegeben: f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR
- gesucht: Koordinaten und Art aller Extrempunkte von Gf|Monotonieverhalten
- verfahren: die erste Ableitung null setzen, durch −0,75 teilen und mit der Lösungsformel die beiden Stellen berechnen, dort das Vorzeichen der zweiten Ableitung prüfen, die Funktionswerte bestimmen und die drei Monotonieintervalle angeben
- fehlerquelle: die Monotonieintervalle nach dem Vorzeichen der zweiten statt der ersten Ableitung angeben

### 2024-C-1d (fhr-katalog.csv)

jahr 2024 · papier C · punkte 7 · format Rechnung|Kurzantwort · antwort Zahl|Text
- gegeben: f(x) = (1/4)x^3 − (23/4)x + 7; x aus IR
- gesucht: Koordinaten und Art aller Extrempunkte von Gf|Monotonieverhalten
- verfahren: f'(x) = 0 setzen und die Stellen durch Wurzelziehen bestimmen, das Vorzeichen von f'' an diesen Stellen prüfen, die Funktionswerte berechnen und daraus die Monotonieintervalle ableiten
- fehlerquelle: beim Wurzelziehen nur die positive Lösung angeben und den Hochpunkt verlieren

### 2025-C-1d (fhr-katalog.csv)

jahr 2025 · papier C · punkte 11 · format Rechnung|Kurzantwort · antwort Zahl|Text
- gegeben: f(x) = −(1/4)x^5 + 2x^3; x aus IR
- gesucht: vollständige Koordinaten und Art der beiden Extrempunkte|Nachweis und Koordinaten des Sattelpunktes|Monotonieverhalten von Gf
- verfahren: f'(x) = 0 durch Ausklammern von x^2 lösen, die drei Stellen in f'' einsetzen, bei f''(0) = 0 über f'''(0) ungleich null den Sattelpunkt nachweisen, die Funktionswerte berechnen und aus dem Vorzeichen von f' die Monotonieintervalle angeben
- fehlerquelle: die doppelte Nullstelle x = 0 von f' als Extremstelle deuten, ohne f''' zu prüfen

### 2024-bebb-gk-A1.7a (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 2 · format Rechnung · antwort Text
- gegeben: f(x) = e^(0,5x) − e, definiert in IR, Graph G
- gesucht: Nachweis, dass G streng monoton steigend verläuft
- verfahren: f' bilden und Vorzeichen begründen
- fehlerquelle: innere Ableitung 0,5 vergessen (ändert das Vorzeichen nicht)

### 2026MgrundlegendBAnalysisWTR1-1a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: f(x) = 1/4 x³ + 1/4 in IR, Graph G
- gesucht: Nachweis, dass G monoton steigend ist
- verfahren: f' bilden, Vorzeichen begründen
- fehlerquelle: f'(0) = 0 als Gegenargument werten

### 2021-be-gk-B2.1g (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 6 · format Rechnung · antwort Zahl
- gegeben: f(x) = 1/12 x³ − x² + 3x und p(x) = −x² + 3,8x − 1,36, beide in IR; Graphen G_f und G_p (Parabel); auf 0,4 ≤ x ≤ 3,4 liegt G_f oberhalb von G_p; d(x) = f(x) − p(x) ist der senkrechte Abstand
- gesucht: Intervalle, in denen d steigt bzw. fällt; Wertebereich von d
- verfahren: d' = 0, Vorzeichen von d'; Minimum und Randwerte vergleichen
- fehlerquelle: das Maximum am linken Rand statt am rechten Rand annehmen

### 2026-C-1e (fhr-katalog.csv)

jahr 2026 · papier C · punkte 8 · format Rechnung|Kurzantwort · antwort Zahl|Text
- gegeben: f(x) = −6x^5 + 18,75x^4 + 20x^3 − 90x^2; x aus IR; die Stellen x1 = −1,5; x2 = 0 und x3 = 2
- gesucht: Nachweis, dass der Anstieg an diesen Stellen Null ist|Art der Punkte mit vollständigen Koordinaten|Monotonieverhalten von f
- verfahren: f' an den drei Stellen auswerten; das Vorzeichen von f'' entscheidet über Hoch- und Tiefpunkt, bei f'' = 0 entscheidet f''' ungleich Null über den Sattelpunkt; Funktionswerte einsetzen; Monotonie aus dem Vorzeichen von f' zwischen den Stellen
- fehlerquelle: bei f'' = 0 auf einen Extrempunkt schließen statt f''' zu prüfen

### 2023-C-1c (fhr-katalog.csv)

jahr 2023 · papier C · punkte 9 · format Rechnung · antwort Zahl
- gegeben: f(x) = x^5 − 3x^4 − 9x^3 + 27x^2; x aus IR; zwei Extremstellen sind bereits gegeben: xE1 = 0 und xE2 = 3
- gesucht: die beiden weiteren Extremstellen von f|Koordinaten und Art aller vier Extrempunkte von Gf
- verfahren: f' gleich null setzen, x ausklammern, den kubischen Faktor durch (x − 3) dividieren und die verbleibende quadratische Gleichung mit der Lösungsformel lösen; die Art über das Vorzeichen von f'' bestimmen und die Funktionswerte berechnen
- fehlerquelle: die gegebene Extremstelle 3 nicht zum Abspalten nutzen und an der Gleichung vierten Grades scheitern

### 2021-be-gk-B2.2d (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 6 · format Rechnung · antwort Zahl
- gegeben: f(x) = (−1/10 x² + 2x) · e^(−0,1x) und h(x) = −3/4 x · e^(−0,1x), beide in IR; Graphen G und H; ohne Nachweis: f''(x) = (−1/1000 x² + 3/50 x − 3/5) · e^(−0,1x)
- gesucht: Koordinaten und Art der lokalen Extrempunkte von G
- verfahren: f' bilden, quadratische Gleichung lösen, f'' auswerten, Funktionswerte
- fehlerquelle: Kettenregel beim Ableiten des e-Faktors vergessen

### 2019-be-gk-B2.2b (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 7 · format Rechnung · antwort Zahl
- gegeben: Hormonspiegel h(t) = 8t · e^(−0,04t) + 50, t ≥ 0 Zeit in Tagen ab Behandlungsbeginn, h(t) Anteil am Sollwert in Prozent (Ausgangswert 50 %); Kontrollergebnis h'(t) = (8 − 0,32t) · e^(−0,04t)
- gesucht: Zeitpunkt des maximalen Hormonspiegels und dessen Wert (Verwendung der notwendigen Bedingung genügt)
- verfahren: Ableiten mit Produkt- und Kettenregel, ersten Faktor null setzen, Funktionswert berechnen
- fehlerquelle: Kettenregel beim Ableiten von e^(−0,04t) vergessen

### 2020MgrundlegendAAnalysis11-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 3 · format Rechnung · antwort Text
- gegeben: f(x) = x³ − 12x + 16 in IR
- gesucht: Nachweis, dass −2 und 2 die Extremstellen von f sind
- verfahren: f' null setzen, Vorzeichenwechsel prüfen
- fehlerquelle: hinreichende Bedingung vergessen

### 2026MgrundlegendAAnalysis11-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: f(x) = x^3 − 3x, definiert in IR; Graph G
- gesucht: Nachweis, dass G einen Hochpunkt mit der x-Koordinate −1 hat
- verfahren: erste und zweite Ableitung bilden, f'(−1) = 0 und f''(−1) < 0 zeigen
- fehlerquelle: nur f'(−1) = 0 zeigen und die hinreichende Bedingung weglassen

### 2026-C-1f (fhr-katalog.csv)

jahr 2026 · papier C · punkte 7 · format Rechnung · antwort Zahl
- gegeben: f(x) = −6x^5 + 18,75x^4 + 20x^3 − 90x^2; x aus IR; Gf hat im Intervall −3 <= x <= 3 drei Stellen mit Wechsel der Krümmungsart, eine davon ist ganzzahlig
- gesucht: Koordinaten der Wendepunkte von Gf
- verfahren: f'' = 0 setzen, die ganzzahlige Nullstelle x = 2 nutzen und durch Polynomdivision oder Hornerschema abspalten, die restliche quadratische Gleichung lösen, f''' ungleich Null prüfen und die Funktionswerte berechnen
- fehlerquelle: die dritte Wendestelle bei x = 2 als Wendepunkt angeben statt als Sattelpunkt zu erkennen

### 2020-C-1d (fhr-katalog.csv)

jahr 2020 · papier C · punkte 9 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: f(x) = x^4 − (82/9)x^2 + 1; x aus IR
- gesucht: Koordinaten aller Wendepunkte von Gf|Krümmungsintervalle des Graphen|Begründung der Art der Krümmung
- verfahren: f'' gleich null setzen, beide Wendestellen berechnen, mit f''' ungleich null bestätigen und die Funktionswerte bestimmen; danach die drei Intervalle angeben und das Vorzeichen von f'' an je einer Probestelle prüfen
- fehlerquelle: die Krümmung nur aus der Lage der Wendestellen ableiten, ohne das Vorzeichen von f'' an Probestellen zu prüfen

### 2024-B-1e (fhr-katalog.csv)

jahr 2024 · papier B · punkte 7 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: f(x) = 1/5 x^5 − 1/5 x^4 − 2x^3; x aus IR; die Ableitungen aus Teilaufgabe d: f'(x) = x^4 − 4/5 x^3 − 6x^2, f''(x) = 4x^3 − 12/5 x^2 − 12x, f'''(x) = 12x^2 − 24/5 x − 12
- gesucht: Nachweis, dass Gf Wendepunkte besitzt|Koordinaten der Wendepunkte|Nachweis, dass einer der Wendepunkte gleichzeitig ein Sattelpunkt ist
- verfahren: f'' gleich null setzen, x ausklammern und den quadratischen Faktor mit der Lösungsformel lösen, die Wendestellen mit f''' ungleich null bestätigen und die Funktionswerte berechnen; für den Sattelpunkt zusätzlich f'(0) = 0 zeigen
- fehlerquelle: beim Ausklammern die Wendestelle x = 0 verlieren und damit den Sattelpunkt übersehen

### 2023-bebb-gk-B2.1f (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Die in IR definierte Funktion f mit f(x) = 0,5 · (x² − 4) · e^x, ihr Graph G; die erste Ableitung ist f'(x) = (0,5x² + x − 2) · e^x. G besitzt zwei Wendepunkte.
- gesucht: Koordinaten beider Wendepunkte, auf zwei Nachkommastellen gerundet
- verfahren: f' mit der Produktregel ableiten: f''(x) = (x + 1) · e^x + (0,5x² + x − 2) · e^x = (0,5x² + 2x − 1) · e^x; f''(x) = 0 ⇔ x² + 4x − 2 = 0 ⇔ x = −2 ± √6; Existenz der beiden Wendepunkte ist vorgegeben; Funktionswerte berechnen und runden.
- fehlerquelle: beim Ableiten des Produkts den Faktor e^x nur einmal berücksichtigen

### 2018MgrundlegendBAnalysisWTR-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 6 · format Rechnung · antwort Term
- gegeben: f(x) = 1/8 · (x³ − 15x² + 50x), x ∈ IR; Abbildung 1 zeigt den Graphen G_f; Punkt W(5 | 0)
- gesucht: Nachweis, dass W ein Wendepunkt ist; Gleichung der Tangente in W
- verfahren: f'' und f''' bilden, f''(5) = 0 und f'''(5) = 3/4 ≠ 0; f(5) = 0, f'(5) = −25/8, Tangente aufstellen
- fehlerquelle: f''(5) = 0 ohne hinreichende Bedingung als Nachweis werten

### 2018MerhoehtBAnalysisWTR1-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 6 · format Rechnung · antwort Term
- gegeben: f(x) = 1/18 · (x³ − 15x² + 50x), ganzrational dritten Grades, G_f schneidet die x-Achse bei 0, 5 und 10 und geht durch (1 | 2); Abbildung 1 zeigt G_f; Punkt W(5 | 0)
- gesucht: Nachweis, dass W ein Wendepunkt ist; Gleichung der Tangente in W
- verfahren: f''(5) = 0 und f'''(5) = 1/3 ≠ 0; f(5) = 0, f'(5) = −25/18
- fehlerquelle: hinreichende Bedingung weglassen

### 2023-bebb-lk-A1.1b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: Eigenschaften aus a: Nullstelle x1, f'(x2) = 0 mit f''(x2) ≠ 0, Minimum von f' bei x3; Abbildung mit x1, x2, x3
- gesucht: Skizze eines möglichen Graphen von f in der Abbildung
- verfahren: Graph durch (x1; 0) steigend, Hochpunkt (oder Tiefpunkt) über x2, Wendepunkt über x3 mit dort minimaler Steigung, danach wieder steigend
- fehlerquelle: bei x3 einen Extrempunkt statt eines Wendepunkts zeichnen

### 2020-be-gk-B2.2d (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 4 · format Zeichnen · antwort Grafik
- gegeben: f(x) = −1/100 x³ + 3/50 x² + 3/20 x + 2/25 (ausmultiplizierte Form aus b); f'(x) = −3/100 x² + 3/25 x + 3/20; Bereich −2 ≤ x ≤ 8; leeres Koordinatensystem in der Anlage
- gesucht: Graphen von f und f' im Bereich −2 ≤ x ≤ 8
- verfahren: Nullstellen, Extrempunkte und Randwerte eintragen und verbinden; f' als Parabel durch die Extremstellen von f
- fehlerquelle: Extremstellen von f nicht als Nullstellen von f' zeichnen

### 2023MerhoehtAAnalysis11-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: ganzrationale, nicht lineare Funktion f in IR: Nullstelle x1; f'(x2) = 0 und f''(x2) ≠ 0; f' hat ein Minimum an der Stelle x3; Lage von x1, x2, x3 in der Abbildung
- gesucht: Begründung, dass der Grad von f mindestens 3 ist
- verfahren: aus dem Minimum von f' folgt Grad von f' mindestens 2, also Grad von f mindestens 3
- fehlerquelle: mit der Nullstelle x1 oder der Extremstelle x2 allein argumentieren (Grad 2 reicht dafür)

### 2023-C-2a (fhr-katalog.csv)

jahr 2023 · papier C · punkte 3 · format Kurzantwort|Rechnung · antwort Zahl
- gegeben: Herr Meier will ein Hoftor nachbauen und hat dazu eine Projektskizze angefertigt; die Parabelbögen und Rahmenteile werden aus Metallprofilen gefertigt, deren Dicke vernachlässigt wird, die Trennung der beiden Torhälften bleibt unberücksichtigt; eine Einheit im Koordinatensystem entspricht einem Meter am Tor; der obere Parabelbogen Gf gehört zu f(x) = −0,15x^2 + 1,2x − 0,6
- gesucht: Höhe des geplanten Tores|Koordinaten des Hochpunktes von Gf
- verfahren: f' bilden, gleich null setzen, die Stelle in f einsetzen und den Funktionswert als Torhöhe in Metern deuten
- fehlerquelle: die Extremstelle x = 4 statt des Funktionswerts als Höhe angeben

### 2024-C-2d (fhr-katalog.csv)

jahr 2024 · papier C · punkte 4 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: die Flugbahn des Balls wird im ersten Quadranten durch g(x) = −0,1x^2 + x + 1,2; x aus IR beschrieben; die y-Achse gibt die Flughöhe in Metern an, die x-Achse verläuft auf der Erdoberfläche und gibt die Entfernung von der Abwurfstelle in Metern an; der Abwurf erfolgt an der Stelle x = 0
- gesucht: Höhe des Balls beim Abwurf|maximale Flughöhe
- verfahren: den Funktionswert an der Stelle x = 0 als Abwurfhöhe angeben; dann g'(x) = 0 setzen und den Funktionswert an der Extremstelle berechnen
- fehlerquelle: die Extremstelle x = 5 selbst als maximale Höhe angeben

### 2021-B-2d (fhr-katalog.csv)

jahr 2021 · papier B · punkte 4 · format Rechnung · antwort Zahl
- gegeben: f(x) = −3x^4 + 8x^3 − 6x^2 + 1 beschreibt die rechte Dachhälfte zwischen A(0; 1) und B(1; 0); aus Sicherheitsgründen darf das Dach nicht zu steil abfallen
- gesucht: steilster Anstieg der rechten Dachhälfte
- verfahren: erkennen, dass der Anstieg im Wendepunkt am größten ist, die zweite Ableitung null setzen, die Sattelstelle x = 1 verwerfen, für die verbleibende Stelle die dritte Ableitung prüfen und den Ableitungswert dort berechnen
- fehlerquelle: die Sattelstelle x = 1 als Wendestelle behalten und den Anstieg null als steilsten Anstieg angeben

### 2018-be-gk-B1.1d (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000) und g'(x) = 1/1000 · (1/500 · x³ − 20x), 1 LE = 1 m. Der Punkt K ist die Stelle des Aufsprunghangs mit dem stärksten Gefälle; für die x-Koordinate genügt die notwendige Bedingung.
- gesucht: Koordinaten des Punktes K
- verfahren: Das stärkste Gefälle liegt dort, wo g' minimal wird, also bei g''(x) = 0. Aus 3/500 · x² − 20 = 0 folgt x² = 10 000/3 und im Bereich des Hangs x = 100/√3 ≈ 57,7. Den zugehörigen Funktionswert durch Einsetzen in g bestimmen.
- fehlerquelle: die erste statt der zweiten Ableitung null setzen, oder die negative Lösung x = −57,7 angeben, die nicht auf dem Aufsprunghang liegt

### 2019-be-gk-B2.2c (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Hormonspiegel h(t) = 8t · e^(−0,04t) + 50, t ≥ 0 Zeit in Tagen ab Behandlungsbeginn, h(t) Anteil am Sollwert in Prozent (Ausgangswert 50 %); ohne Nachweis: h''(t) = (−0,64 + 0,0128t) · e^(−0,04t); h'(t) = (8 − 0,32t) · e^(−0,04t) aus b
- gesucht: Zeitpunkt, an dem der Hormonspiegel am stärksten fällt (notwendige Bedingung genügt); Hormonspiegel und lokale Änderungsrate zu diesem Zeitpunkt
- verfahren: h''(t) = 0 lösen (erster Faktor), dann h(50) und h'(50) berechnen
- fehlerquelle: die Nullstelle von h' (Maximum) statt von h'' nehmen

### 2022MgrundlegendBAnalysisWTR2-2c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Tauchroboter, vertikale Bewegung für 0 ≤ t ≤ 30 mit h(t) = 9/40 t³ − 27/2 t² + 405/2 t, t Zeit in Minuten, h(t) Abstand von der Wasseroberfläche in Metern; Abbildung des Graphen
- gesucht: Bedeutung des Wendepunkts für die Bewegung
- verfahren: Wendepunkt bei t = 20 deuten
- fehlerquelle: Wendepunkt als Richtungswechsel deuten

### 2023MgrundlegendBAnalysisWTR2-2a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Kurzantwort|Begründung · antwort Text
- gegeben: g(x) = −1/27x(x − 6)(x − 12) + 14 für 0 ≤ x < 12, x Zeit in Monaten, g(x) Tagesdurchschnittstemperatur in °C; Graph in der Abbildung; g entsteht aus f durch die drei Schritte
- gesucht: Wendestelle von g; Bedeutung für den Temperaturverlauf
- verfahren: Wendestelle als verschobener Wendepunkt (6) angeben und als Zeitpunkt der stärksten Zunahme deuten
- fehlerquelle: Wendestelle als Zeitpunkt der höchsten Temperatur deuten

### 2024MgrundlegendBAnalysisWTR2-2c (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 4 · format Kurzantwort · antwort Text
- gegeben: Lösungsweg: d(x) = f(x) − h(x); d'(x) = 0 hat für 0 < x < x_s nur die Lösung x1 ≈ 3,64; d''(x1) ≈ −0,13 < 0; d(x1) ≈ 0,37
- gesucht: Bedeutung von d(x) für 0 < x < x_s und Deutung von 0,37
- verfahren: d als Vorsprung, Extremwertschritte als Maximum deuten
- fehlerquelle: 0,37 als Vorsprung in Metern deuten

Nicht in den Prüfungsdateien gefunden: 2017-be-gk

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2023-C-1d, 2018-be-gk-B1.2d, 2022MerhoehtBAnalysisWTR1-1b, 2018MgrundlegendBAnalysisWTR-2f, 2021-be-gk-A1.3a, 2024-bebb-gk-B2.1b, 2023-bebb-lk-A1.2b, 2020MgrundlegendBAnalysisWTR1-1b, 2022MgrundlegendBAnalysisWTR2-1a, 2022MgrundlegendBAnalysisWTR2-2a, 2021-be-gk-B2.1d, 2022-bebb-lk-B2.2d, 2019-C-1d, 2024-C-1e, 2025MerhoehtAAnalysis12-a, 2023-A-1b, 2022-C-1c, 2019-C-1c, 2024-B-2b, 2023-bebb-gk-A1.3a, 2024-bebb-gk-B2.2c, 2022-bebb-gk-B2.2b, 2026-B-1d, 2022-B-1c, 2022-B-1d, 2025-A-1c, 2024-B-1f, 2022-C-1d, 2026-B-1e, 2025-A-1e, 2020-A-1c, 2026-bb-gk-B2.1c, 2019-A-1c, 2021-B-2c, 2020-C-1c, 2019-A-1d, 2022-bebb-lk-B2.1g, 2022-bebb-lk-B2.1h, 2024MgrundlegendBAnalysisWTR2-1a, 2021MgrundlegendBAnalysisWTR-1a, 2023-A-2e, 2023-bebb-gk-B2.2c, 2023MgrundlegendBAnalysisWTR2-2b, 2024-bebb-gk-B2.1c, 2025-bebb-lk-B2.2g, 2021MgrundlegendAAnalysis2-a, 2025MerhoehtBAnalysisWTR2-1a, 2025MgrundlegendBAnalysisWTR2-1b, 2022-bebb-gk-B2.1l, 2019MgrundlegendBAnalysisWTR1-1c, 2024MgrundlegendBAnalysisWTR1-2b, 2023MgrundlegendBAnalysisWTR1-2b, 2025MerhoehtBAnalysisMMS1-2b, 2026-B-2c, 2019-C-2b, 2018MerhoehtBAnalysisWTR1-2e, 2020MgrundlegendBAnalysisWTR2-1a, 2024MgrundlegendBAnalysisWTR1-1b, 2019-be-gk-B2.1f, 2020-be-gk-B2.1e, 2022-bebb-gk-A1.2a, 2023-bebb-gk-B2.1d, 2019MerhoehtAAnalysis2-a, 2019MerhoehtAAnalysis2-b, 2023MerhoehtAAnalysis11-b, 2018MgrundlegendBAnalysisWTR-2b, 2018MerhoehtBAnalysisWTR1-2b, 2025MgrundlegendBAnalysisWTR2-2a, 2025-bebb-gk-B2.2e, 2026-bb-ea-B2.1c, 2023-bebb-gk-B2.1k, 2024-bebb-gk-B2.1h, 2026MgrundlegendBAnalysisMMS2-1e, 2020-A-2b, 2019-A-1e, 2025MgrundlegendBAnalysisWTR1-1a, 2023-bebb-gk-B2.1e, 2022-bebb-lk-B2.1b, 2018-bb-ea-B2.2c, 2019-be-gk-A1.1b, 2020MgrundlegendAAnalysis11-b, 2023MgrundlegendBAnalysisWTR2-2d, 2021-be-gk-B2.1c, 2021-B-1d, 2022-bebb-gk-A1.2b, 2018MgrundlegendBAnalysisWTR-1f, 2022-bebb-gk-B2.1j, 2022MerhoehtBAnalysisWTR3-1c, 2018MerhoehtBAnalysisWTR1-1h, 2023-bebb-gk-B2.2h

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
