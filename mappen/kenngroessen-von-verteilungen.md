# Mappe: kenngroessen-von-verteilungen

Eintrag: hz-0801/mathe-nachhilfe, katalog/kenngroessen-von-verteilungen.md
Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26T16:47:30+02:00, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:42 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Kenngrößen von Verteilungen
  3
  4  ### Verortung
  5  Die Kenngrößen von Wahrscheinlichkeitsverteilungen: der Erwartungswert als gewichtete Summe (vorwärts berechnen und als Durchschnitt auf lange Sicht deuten, Auszahlung gegen Gewinn und Einsatz abgrenz … (gekürzt, 2013 Zeichen)
  6  [GOST] Q2, 2. Kurshalbjahr „Analysis; Stochastik“ (BB S. 25 ff.), Grund- und Leistungskursfach: L2-Zeile „Erwartungswert und Standardabweichung diskreter Zufallsgrößen bestimmen und deuten“ mit den In … (gekürzt, 1978 Zeichen)
  7  [FOS] Pflichtthema 4 „Stochastik“, Baustein Wahrscheinlichkeitsrechnung (S. 28): „Erwartungswert von Zufallsvariablen bestimmen (z. B. den Einsatz für ein ‚faires‘ Spiel)“ (Zeilen 1188–1189 der Textfa … (gekürzt, 709 Zeichen)
  8  [LS-AA] Einführungsphase Kapitel V „Schlüsselkonzept: Binomialverteilung“, Unterkapitel 4 „Die Binomialverteilung – Erwartungswert“; Qualifikationsphase Kapitel VIII „Grundlagen der Wahrscheinlichkeit … (gekürzt, 750 Zeichen)
  9
 10  ### Lerneinheiten
 11  1. Erwartungswert berechnen und deuten: die Verteilung beschaffen (Tabelle, Sachtext, Baumpfade, Kosten je Ausgang; fehlende Wahrscheinlichkeit über die Summe 1), die gewichtete Summe bilden (bei Anzahlen n · p), das Ergebnis deuten – Durchschnitt auf lange Sicht, Auszahlung gegen Gewinn und Einsatz abgrenzen, Summanden eines vorgelegten Terms erläutern, prozentuale Abweichung einer Beobachtung vom Erwartungswert. (Q2 BB, GK-Kern; OHiMi 2.4 „Erwartungswert von Zufallsgrößen“; FOS Pflichtthema 4) ← Eingabe „erwartungswert“, „mittlerer gewinn“, „auf lange sicht“, „durchschnittliche kosten“
 12    Marken: BE Q2/4 · BB Q2 · GK · Abitur GK · Abitur LK · FHR
 13  2. Rückwärts – unbekannte Größen aus Erwartungswertbedingungen: das faire Spiel (Erwartungswert der Auszahlung gleich Einsatz, Gewinnerwartung null), unbekannte Auszahlungen, Kugel- und Würfelbeschriftungen, Anzahlen und Wahrscheinlichkeiten aus der Bedingung bestimmen (linear, quadratisch, Ungleichung, mit der Summenbedingung als zweiter Gleichung), Sonderformen: Wertebereich, Maximum, Verhältnis, Untersuchung mehrerer Bedingungen zugleich. (Q2 BB; Prüfungshöhe des Pools in Teil A, jährlich) ← Eingabe „faires spiel“, „einsatz bestimmen“, „auszahlung gesucht“, „erwartungswert gegeben“
 14    Marken: BE Q4 · BB Q2 · GK · Abitur GK · Abitur LK
 15  3. Varianz und Standardabweichung: die allgemeinen Formeln (gewichtete quadrierte Abweichung, Wurzel), die Binomialformeln μ = n · p und σ = √(n · p · (1 − p)) vorwärts und rückwärts (Parameter aus Kenngrößen, Symmetrie liefert p), Argumente über die Formel (Parabel in p, Symmetrie von p und Gegenwahrscheinlichkeit, Wachstum mit der Wurzel aus n). (BB Q2 GK-Kern, BE Q4 GK binomial bzw. LK allgemein; [IQB-VER 4] vorausgesetzt) ← Eingabe „standardabweichung“, „varianz“, „sigma“, „streuung“
 16    Marken: BE Q2/4 · BB Q2 · GK · Abitur GK
 17  4. Kenngrößen am Säulendiagramm: den ganzzahligen Erwartungswert an der höchsten Säule ablesen und daraus p, n oder Verhältnisse bestimmen, die Parität von n aus zwei gleich hohen Säulen begründen, ein Sigma-Intervall auf ganze Werte übertragen und die Wahrscheinlichkeit als Summe der Säulenhöhen ablesen. (GOST-Inhalt „Eigenschaften auf der Grundlage graphischer Darstellungen“; OHiMi 2.4 „Histogramme“; alle Zeilen Teil A, gehäuft seit 2024) ← Eingabe „höchste säule“, „diagramm erwartungswert“, „sigma-intervall“, „säulendiagramm binomial“
 18    Marken: BE Q4 · BB Q2 · GK · Abitur GK · Abitur LK
 19  Warum vier: Der Vorwärts- und der Rückwärtsblock (einundzwanzig und siebenunddreißig Zeilen) trennen die Fehlmuster – dort die Einsatzdeutung, hier der Gleichungsansatz mit Lösungssiebung; die Streuun … (gekürzt, 987 Zeichen)
 20
 21  ### Typen je Lerneinheit
 22  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; fhr-Typen wörtlich aus fhr/fhr-typen.csv, abitur-Typen aus abitur/abitur-typen.csv.
 23  Einheit 1: Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen (6) · Erwartungswert berechnen (2; fhr) · Prozentuale Abweichung einer Anzahl vom Erwartungswert berechnen (2) · Erwartungswert aus einer Verteilung mit fehlender Wahrscheinlichkeit berechnen (1) · Erwartungswert der Kosten pro Stück aus einer Wahrscheinlichkeitstabelle berechnen (1) · Erwartungswert eines Spielgewinns über die Pfade eines Baumdiagramms berechnen (1) · Erwartungswert der Augensumme aus dem Erwartungswert der Trefferzahl berechnen (1) · Erwartungswert einer weiteren Runde mit dem sicheren Betrag vergleichen und eine Empfehlung begründen (1) · Gesamtzahl der Gruppen aus der Personenzahl und der mittleren Gruppengröße unter einer vereinfachenden Annahme schätzen (1; Ermessen, siehe Offene Punkte) — kein Nachweistyp — Deutung: Erwartungswert der Auszahlung mit dem Einsatz vergleichen (3) · Summand eines Erwartungswertterms im Sachzusammenhang deuten (2). Dazu: Fehler finden (Auszahlung als Gewinn gedeutet, Einsatz nicht gegengerechnet; falsche Gewichte; fehlende Wahrscheinlichkeit nicht ergänzt; Selbstkosten mit entgangenem Gewinn verwechselt; Abweichung auf die falsche Bezugsgröße bezogen) · Begründen (warum der Erwartungswert kein möglicher Wert sein muss; warum „im Mittel gewinnbringend“ nichts über ein einzelnes Spiel sagt).
 24  Einheit 2: Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (21) · Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten (3) · Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen (2) · Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen (2) · Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen (2) · Verhältnis zweier Auszahlungen aus dem Ausgleich der Erwartungswerte berechnen (1) · Kugelzahl für den größten Erwartungswert der Auszahlung ermitteln (1) · Kugelbeschriftung aus dem Erwartungswert der Summe beim Ziehen ohne Zurücklegen berechnen (1) · Mindestanzahl aus einer Erwartungswertbedingung n · p > c ermitteln (1) · Wertebereich des Erwartungswerts aus Ungleichungen für die Wahrscheinlichkeiten bestimmen (1) — Nachweis: Untere Schranke für eine Kugelbeschriftung aus dem Erwartungswert der Summe ohne Rechnung begründen (1) — Deutung: Aussage über gleiche Erwartungswerte aufeinanderfolgender Parameterwerte über eine Gleichung beurteilen (1). Dazu: Fehler finden (Fairness als Gewinnerwartung null statt Auszahlungserwartung gleich Einsatz angesetzt; Reihenfolgen-Faktor vergessen; mit statt ohne Zurücklegen gerechnet; unzulässige Lösung mitgenommen oder die verlangte negative übersehen; falsch auf- oder abgerundet) · Begründen (warum „Einsätze und Auszahlungen gleichen sich aus“ eine Gleichung liefert; warum die Summenbedingung die zweite Gleichung ist).
 25  Einheit 3: Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen (3) · Stichprobenumfang aus einer vorgegebenen Standardabweichung der Binomialverteilung berechnen (2) · Standardabweichung einer Binomialverteilung aus n und Erwartungswert berechnen (1) · Parameter n aus Erwartungswert und Symmetrie einer Binomialverteilung ermitteln (1) · Verhältnis der Varianzen zweier Binomialverteilungen aus dem Erwartungswert im Diagramm bestimmen (1) — Nachweis: Standardabweichung über einen Summanden der Varianz abschätzen (1) · Gleiche Standardabweichung zweier komplementärer Zufallsgrößen begründen (1) · Unmöglichkeit einer Standardabweichung bei gegebener Versuchszahl über das Maximum von p · (1 − p) begründen (1) — Deutung: Monotonie der Varianz einer Binomialverteilung in p über die Parabel begründen (1) · Achsen des Graphen der Standardabweichung in Abhängigkeit von p skalieren und erläutern (1). Dazu: Fehler finden (σ statt σ² in die Formel gesetzt; die Wurzel nur über einen Teil des Produkts gezogen; Varianz als Standardabweichung angegeben; n verdoppelt statt vervierfacht; mit gleichen Erwartungswerten statt mit der Symmetrie der Formel argumentiert) · Begründen (warum die Varianz in p eine Parabel ist und was ihr Scheitel bedeutet; warum ein einzelner Summand die Varianz nach unten abschätzt).
 26  Einheit 4: Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln (4) · Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln (2) — Nachweis: Parität von n aus zwei gleich hohen Säulen der Verteilung begründen (2) — kein Deutungstyp. Dazu: Fehler finden (p aus der Höhe statt aus der Lage der höchsten Säule abgelesen; Säulenhöhen statt Lage der Maxima verglichen; Intervallgrenzen gerundet statt die eingeschlossenen ganzen Werte bestimmt) · Begründen (warum der ganzzahlige Erwartungswert an der höchsten Säule liegt; warum ein Doppelmaximum den Erwartungswert zwischen die Säulen legt).
 27  Zählung: 11 + 12 + 10 + 3 = 36 Haupttypen, 21 + 37 + 13 + 8 = 79 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: Pool 2017 grundlegend Teil A und B, erhöht Teil B, CAS; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2018 erhöht Teil B CAS)).
 28
 29  ### Voraussetzungen (Blatt 0)
 30  Fertigkeiten (je Zeile: was, wofür):
 31  - Verteilungstabelle einer Zufallsgröße aufstellen und lesen – die Datengrundlage aller Einheiten. Sek-II-Nachbarthema zufallsgroessen-und-verteilungen.md (Bündel des Vorgängers). [GOST Q2 L4 „Wahrscheinlichkeitsverteilung einer Zufallsgröße in Tabellen und Diagrammen“]
 32  - Pfadregeln und Gegenereignis (mit und ohne Zurücklegen) – die Verteilungen der Einheiten 1 und 2 entstehen aus mehrstufigen Experimenten. Sek-I-Thema wahrscheinlichkeit.md. [GOST-OHiMi 2.4 „Baumdiagramm, Pfadregeln“]
 33  - Bernoulli-Kette erkennen – die Binomialformen der Einheiten 3 und 4. Sek-II-Nachbarthema binomialverteilung.md. [GOST Q2 L5 „Bernoulli-Kette“]
 34  - Brüche gewichten und addieren, Prozentrechnung – gewichtete Summen und prozentuale Abweichungen der Einheit 1. Sek-I-Themen bruchrechnung.md, prozentrechnung.md. [GOST Eingangsvoraussetzung L1]
 35  - Lineare und quadratische Gleichungen sowie einfache Ungleichungen lösen, Lösungen sieben – die Rückwärtsaufgaben der Einheit 2. Sek-I-Themen lineare-gleichungen.md, quadratische-gleichungen.md. [GOST-OHiMi 2.1]
 36  - Wurzelterme bilden und vergleichen – die Standardabweichung der Einheit 3 als Wurzel der Varianz. Sek-I-Thema potenzen-wurzeln.md. [GOST-OHiMi 2.1]
 37  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 38  - „Auszahlung oder Gewinn?“ – zu Spielbeschreibungen ankreuzen, ob die Zufallsgröße die Auszahlung oder den Gewinn nach Abzug des Einsatzes beschreibt; nichts rechnen. Vor Einheit 1 und 2. [Rohdatei-Fehlerquelle „Einsatz nicht abgezogen“; abi 2018-be-gk-B3.1d, iqb 2018MgrundlegendAStochastik12-b]
 39  - „Vorwärts oder rückwärts?“ – ankreuzen, ob der Erwartungswert zu berechnen ist (Verteilung gegeben) oder eine Unbekannte aus einer Erwartungswertbedingung (Erwartungswert gegeben); nichts rechnen. Vor Einheit 2. [Rohdatei: Typen „berechnen“ gegen „bestimmen“; abi 2019-be-gk-B4.2c gegen 2025-bebb-lk-A1.4b]
 40  - „Welche Formel für die Standardabweichung?“ – ankreuzen, ob die Zufallsgröße binomialverteilt ist (Produktformel unter der Wurzel) oder allgemein (gewichtete quadrierte Abweichungen); nichts rechnen. Vor Einheit 3. [iqb 2021MerhoehtAStochastik12-a gegen 2023MgrundlegendAStochastik11-b]
 41
 42  ### Merkkasten
 43  Einheit 1 (Erwartungswert berechnen und deuten):
 44      Formel: jeden Wert der Zufallsgröße mit seiner Wahrscheinlichkeit gewichten und aufsummieren; fehlende Wahrscheinlichkeiten vorher über die Summe 1 ergänzen; für binomialverteilte Anzahlen kurz μ = n · p.
 45        Beispiel Hoffest-Glücksrad: Kosten je Dreh 15 · 0,05 + 1,50 · 1/3 = 1,25 Euro – der Hauptgewinn zählt mit seiner kleinen, der Gutschein mit seiner großen Wahrscheinlichkeit.
 46      Deuten: der Erwartungswert ist der mittlere Wert je Durchführung auf lange Sicht – keine Vorhersage für ein einzelnes Spiel, und er muss kein möglicher Wert der Zufallsgröße sein.
 47      Auszahlung gegen Gewinn: Gewinn ist Auszahlung minus Einsatz – wer auf lange Sicht gewinnt, entscheidet der Vergleich des Auszahlungs-Erwartungswerts mit dem Einsatz, nie die Auszahlung allein.
 48      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] führt „Erwartungswert von Zufallsgrößen“ als hilfsmittelfreien Stoff (Teil-A-Belege 2018MerhoehtAStochastik2-a, 2024MgrundlegendAStochastik12-b); für fhr ist die gewichtete Summe der Prüfstoff des Pflichtthemas.
 49      Formelsammlung: [FS-IQB 1.4] „Zufallsgrößen“ führt die Erwartungswertformel samt Varianz und Standardabweichung – in Teil B nachschlagbar, für Teil A auswendig – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 50  Quelle: eigene Formulierung nach [GOST Q2 L2] „Erwartungswert und Standardabweichung diskreter Zufallsgrößen bestimmen und deuten“ und [FS-IQB 1.4]; Zahlenbeispiel aus abi 2018-bb-ea-A1.3b; [LS-AA QP VIII 2].
 51
 52  Einheit 2 (Rückwärts – unbekannte Größen):
 53      Ansatz: „auf lange Sicht gleichen sich Einsätze und Auszahlungen aus“ heißt Erwartungswert der Auszahlung gleich Einsatz – gleichwertig Gewinnerwartung null; „im Mittel mindestens“ wird zur Ungleichung.
 54      Weg: die Verteilungstabelle in der Unbekannten aufstellen (Werte oder Wahrscheinlichkeiten tragen die Unbekannte), den Erwartungswertterm bilden, die Bedingung einsetzen, lösen.
 55      Sieben: unzulässige Lösungen verwerfen (negative Wahrscheinlichkeiten, unmögliche Anzahlen); verlangt die Aufgabe eine negative Größe, ist die negative Lösung die richtige; Anzahlen je nach Frage auf- oder abrunden.
 56      Nebenbedingungen: die Summe aller Wahrscheinlichkeiten ist eins – bei zwei Unbekannten die zweite Gleichung; Reihenfolgen zählen doppelt.
 57      Auswendig (Teil A): der ganze Kasten – die Rückwärtsform ist die jährliche Teil-A-Prüfform des Themas (Belege 2025MerhoehtAStochastik11-b, 2023MerhoehtAStochastik11-b, 2020MerhoehtAStochastik12-b); der Ansatz steht in keiner Formelsammlung.
 58      Formelsammlung: [FS-IQB 1.4] nur die Erwartungswertformel; Fairness-Ansatz und Lösungssiebung stehen nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 59  Quelle: eigene Formulierung nach [FOS Pflichtthema 4] „den Einsatz für ein ‚faires‘ Spiel“ und der Rohdatei (zwanzig Zeilen des Bedingungstyps); ohne Zahlenbeispiel (die Rückrichtung ist zahlenfrei formuliert; Ermessen); [LS-AA QP VIII 2].
 60
 61  Einheit 3 (Varianz und Standardabweichung):
 62      Allgemein: die Varianz ist die Summe der quadrierten Abweichungen vom Erwartungswert, gewichtet mit den Wahrscheinlichkeiten; die Standardabweichung ist ihre Wurzel – erst quadrieren und gewichten, dann wurzeln.
 63      Binomial: μ = n · p und σ = √(n · p · (1 − p)) – die Wurzel gehört über das ganze Produkt; nützlich als σ² = μ · (1 − p).
 64        Beispiel: μ = 20 und σ = 2 liefern 4 = 20 · (1 − p), also p = 0,8 und n = 25.
 65      Rückwärts: aus zwei Kenngrößen die Parameter (σ² durch μ teilen liefert die Gegenwahrscheinlichkeit); eine symmetrische Binomialverteilung hat p = 0,5, dann folgt n aus μ = n · p.
 66      Argumentieren: die Varianz ist in p eine nach unten geöffnete Parabel mit Scheitel bei p = 0,5 – daraus folgen Monotonie und gleiche Streuung für p und die Gegenwahrscheinlichkeit; σ wächst mit der Wurzel aus n (doppeltes σ braucht vierfaches n).
 67      Auswendig (Teil A): μ = n · p und σ = √(n · p · (1 − p)) – begründetes Ermessen: die Anlage ohne Hilfsmittel nennt nur den Erwartungswert, der Pool prüft die Formeln hilfsmittelfrei (Belege 2021MerhoehtAStochastik12-a, 2024MerhoehtAStochastik11-a, 2018MerhoehtAStochastik11-b).
 68      Formelsammlung: [FS-IQB 1.4] führt Varianz, Standardabweichung und die beiden Binomialformeln – in Teil B nachschlagbar – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 69  Quelle: eigene Formulierung nach [GOST Q2 L4/L5] „Kenngrößen von Wahrscheinlichkeitsverteilungen: Erwartungswert, Varianz, Standardabweichung“, [IQB-VER 4] (Varianz und Standardabweichung vorausgesetzt) und [FS-IQB 1.4]; Zahlenbeispiel aus abi 2026-bb-gk-A1.9a; [LS-AA EP V 4].
 70
 71  Einheit 4 (Kenngrößen am Säulendiagramm):
 72      Höchste Säule: ist der Erwartungswert einer Binomialverteilung ganzzahlig, liegt er an der höchsten Säule – dort μ ablesen und über μ = n · p nach p oder n auflösen; verglichen wird die Lage der Maxima, nie die Säulenhöhe.
 73        Beispiel: höchste Säule bei k = 4 und n = 20 liefern p = 0,2.
 74      Doppelmaximum: zwei gleich hohe höchste Säulen heißen, das Maximum liegt dazwischen und der Erwartungswert ist nicht ganzzahlig – bei p = 0,5 ist n · 0,5 dann keine ganze Zahl, n also ungerade.
 75      Sigma-Intervall: die Grenzen aus μ und σ ausrechnen, die ganzen Werte im Intervall bestimmen (Grenzen nicht runden – nehmen, was dazwischen liegt) und deren Säulenhöhen addieren.
 76      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] „Darstellung von Zufallsgrößen in Histogrammen“; alle Zeilen der Einheit sind hilfsmittelfreie Teil-A-Aufgaben (Belege 2026MgrundlegendAStochastik11-a, 2025MgrundlegendAStochastik21-a).
 77      Formelsammlung: [FS-IQB 1.4] die μ- und σ-Formeln; die Ableseregeln stehen nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 78  Quelle: eigene Formulierung nach [GOST Q2 L2] Inhalt „Eigenschaften auf der Grundlage graphischer Darstellungen“ und [GOST-OHiMi 2.4]; Zahlenbeispiel aus abi 2026-bb-gk-A1.6a; [LS-AA QP VIII 6].
 79
 80  ### Typische Fehler
 81  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 73 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
 82  - Auszahlung als Gewinn gedeutet: den Einsatz nicht gegengerechnet und den Erwartungswert der Auszahlung als Gewinn gelesen; einen positiven Erwartungswert als sicheren Gewinn gedeutet; den Ausgang „null“ als Auszahlung des sicheren Betrags gewertet; beim fairen Spiel Gewinnerwartung null mit Auszahlungserwartung gleich Einsatz verwechselt. [abi 2018-be-gk-B3.1d, 2023-bebb-gk-B4.2b; iqb 2018MgrundlegendAStochastik12-b, 2024MgrundlegendAStochastik12-b, 2021MerhoehtAStochastik13-b, 2018MerhoehtBStochastikWTR1-2b, 2023MerhoehtBStochastikWTR1-3b, 2023MgrundlegendBStochastikWTR3-2b; fhr 2019-C-3d]
 83  - Verteilung falsch aufgestellt: den Reihenfolgen-Faktor vergessen (gemischte Pfade nur einmal gezählt); die Urnen ohne ihre Auswahlwahrscheinlichkeit gewichtet; mit statt ohne Zurücklegen gerechnet (den Nenner im zweiten Zug nicht verringert); die fehlende Wahrscheinlichkeit nicht über die Summe ergänzt; mehrere gleiche Seiten als eine Zahl gewichtet; beim Oder-Ereignis den Schnitt doppelt gezählt; Fälle zusammengeworfen. [abi 2017-bb-ea-A1.3b, 2018-be-gk-B3.1e, 2021-be-gk-A1.6b, 2025-bebb-lk-A1.4b, 2026-bb-ea-A1.9b; iqb 2017MerhoehtAStochastik2-b, 2019MgrundlegendBStochastikWTR2-2c, 2019MgrundlegendBStochastikWTR3-2c, 2020MerhoehtAStochastik12-b, 2020MerhoehtAStochastik13-b, 2021MerhoehtAStochastik22, 2018MerhoehtAStochastik2-a, 2021MgrundlegendBStochastikWTR1-1e, 2023MgrundlegendAStochastik12-b, 2023MgrundlegendAStochastik2, 2025MgrundlegendAStochastik22-b, 2025MerhoehtAStochastik11-b, 2026MerhoehtAStochastik23-b]
 84  - Kosten- und Bezugsfehler im Sachzusammenhang: Selbstkosten mit entgangenem Gewinn verwechselt; Kosten nur in den bezahlten Fällen angesetzt; nach den Kosten gefragt, den Saldo geliefert; Cent und Euro gemischt; die prozentuale Abweichung auf hundert statt auf den Erwartungswert bezogen; den Tagesbezug verfehlt (Gesamtsumme statt Erwartungswert je Tag); falsch gerundet (ab- statt aufgerundet oder umgekehrt); kumulierte statt Einzelwahrscheinlichkeiten eingesetzt; nur eine Sorte Treffer gezählt; mit dem falschen Bruch gerechnet; den Reihenfolgen-Faktor eines vorgelegten Terms als Auszahlung gedeutet. [abi 2017-bb-ea-B4.1c, 2018-bb-ea-A1.3b, 2019-be-gk-B4.2c, 2021-be-gk-B4i, 2022-bebb-gk-B4c, 2022-bebb-lk-B4l, 2023-bebb-lk-B4g; iqb 2023MgrundlegendBStochastikWTR3-2a, 2021MgrundlegendBStochastikWTR2-1g, 2022MgrundlegendBStochastikWTR1-1b, 2023MerhoehtBStochastikWTR2-2a, 2023MerhoehtBStochastikWTR3-1b, 2023MgrundlegendBStochastikWTR2-1d, 2025MgrundlegendBStochastikWTR3-1e; fhr 2021-B-3e]
 85  - Gleichung falsch angesetzt oder Lösungen nicht gesiebt: die unzulässige Lösung mitgenommen oder die verlangte negative übersehen; nur die Randfälle statt aller Zwischenwerte genannt; Werte durchprobiert ohne Eindeutigkeitsnachweis; die sichtbaren Würfelseiten beim Erwartungswert vergessen; mit dem Mittelwert statt dem Erwartungswert argumentiert; die Auszahlung als feste Zahl statt als Parameter angesetzt; den falschen Summanden der Bedingung gewichtet. [abi 2018-be-gk-B3.1e, 2023-bebb-gk-B4.2c, 2023-bebb-lk-A1.7b, 2024-bebb-gk-B4.2c, 2024-bebb-lk-A1.10a; iqb 2023MerhoehtAStochastik11-b, 2018MerhoehtAStochastik2-b, 2023MerhoehtBStochastikWTR1-3c, 2024MerhoehtAStochastik22, 2019MgrundlegendBStochastikWTR3-2b, 2022MerhoehtAStochastik21, 2023MgrundlegendAStochastik11-a, 2024MgrundlegendBStochastikWTR1-2c]
 86  - Streuungsformeln verwechselt: σ statt σ² in die Formel gesetzt; die Wurzel nur über einen Teil des Produkts gezogen; die Varianz als Standardabweichung angegeben; das Verhältnis der Standardabweichungen statt der Varianzen gebildet; n verdoppelt statt vervierfacht; mit gleichen Erwartungswerten statt mit der Symmetrie der Formel argumentiert; die Varianz vollständig berechnen wollen, obwohl Werte fehlen; nur Zahlenbeispiele statt des Parabelarguments; die Achse über ein Maximum skaliert, das auf keiner Gitterlinie liegt; die Symmetrie nicht in p übersetzt. [abi 2026-bb-gk-A1.9a; iqb 2026MgrundlegendAStochastik22, 2021MerhoehtAStochastik12-a, 2018MgrundlegendBStochastikWTR1-2, 2020MgrundlegendBStochastikWTR2-1d, 2024MerhoehtAStochastik11-a, 2023MgrundlegendAStochastik11-b, 2022MgrundlegendBStochastikWTR2-3b, 2024MgrundlegendBStochastikWTR2-3, 2018MerhoehtAStochastik11-b]
 87  - Diagramm falsch gelesen: p aus der Höhe statt aus der Lage der höchsten Säule abgelesen; die Säulenhöhen statt der Lage der Maxima verglichen; aus der Lage der Symmetrieachse auf ein gerades n geschlossen; die Intervallgrenzen gerundet statt die eingeschlossenen ganzen Werte bestimmt; die Standardabweichung fürs Intervall falsch berechnet. [abi 2026-bb-gk-A1.6a, 2025-bebb-gk-A1.9a, 2026-bb-ea-A1.4b; iqb 2026MgrundlegendAStochastik11-a, 2024MerhoehtAStochastik11-b, 2025MerhoehtAStochastik12-b, 2025MgrundlegendAStochastik21-a, 2026MerhoehtAStochastik11-b]
 88
 89  ### Für schwache Schüler
 90  Mindeststoff (GK-Kern Q2/Q4 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: Einheit 1 (Brandenburg Q2 „bestimmen und deuten“, Anlage ohne Hilfsmittel; Berlin über die Binomialverteilung in Q4), die Grundformen der Einheit 2 (die Fairness-Gleichung – jährlich grundlegend geprüft), die Binomialformeln der Einheit 3 und die Grundformen der Einheit 4 (höchste Säule, Doppelmaximum – im Pool und seit dem jüngsten Jahrgang auch im Grundkurs-Landesheft). Vorrat für den GK (Ermessen nach dem Niveau der Rohdatei): die Sonderformen der Einheit 2 (Wertebereich, Maximum, Würfelbeschriftung, Verhältnis) und die Argumentformen der Einheit 3 (Parabel, Symmetrie, Achsenskalierung). RLP FOS (fhr): Einheit 1 ist Pflicht- und Prüfstoff (gewichtete Summe mit Anschlussrechnung, beide Zeilen als anspruchsvollste Stochastik-Teilaufgabe ihres Hefts); die Einheiten 2 bis 4 sind für fhr Vorrat – das „faire Spiel“ steht als Beispiel im Plan, ist aber ungeprüft. Niveaustufe H der E-Phase [RLP]: die Sek-I-Pläne kennen den Erwartungswert nicht (Suchprotokoll der Verortung); Blatt-0-Stoff sind Pfadregeln, Anteile und das arithmetische Mittel – das Lehrwerk zieht den Begriff gleichwohl in die Sekundarstufe I vor [LS-AA Kl. 8 VIII 5–6]. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung Erwartungswert und Standardabweichung diskreter Zufallsgrößen – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
 91  Grundvorstellung (Blatt 0) [GOST Q2 L2 „deuten“, MO]: Der Erwartungswert ist der Durchschnitt je Durchführung auf lange Sicht – nicht das, was beim nächsten Mal passiert. „Ein Spiel kostet zwei Euro Einsatz; meistens gehst du leer aus, hin und wieder werden fünf Euro ausgezahlt, ganz selten zwanzig. Spiele es in Gedanken hundertmal durch, kein Term: Was sagt dir am Ende, ob sich das Spiel lohnt – dein bestes Spiel, dein schlechtestes oder der Durchschnitt je Spiel? Warum kann ein Spiel mit möglichem Hauptgewinn trotzdem ein Verlustgeschäft sein? Und wenn ein Spiel ‚fair‘ ist – heißt das, dass am Ende niemand verloren hat?“ Wer vom besten Fall auf das Spiel schließt oder „fair“ mit „niemand verliert“ verwechselt, braucht das vor jeder Formel: eine Verteilung wird durch ihren Durchschnitt auf Dauer beschrieben, und der entsteht aus Wert mal Häufigkeit. Verständnis, nicht Verfahren; die Vorstellung ist amtlich („bestimmen und deuten“), die Aufgabenform ist Ermessen. [GOST Q2 L2; FOS „bestimmen und deuten“; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Erwartungswert als Gewinn je Spiel gedeutet“, iqb 2018MgrundlegendAStochastik12-b; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
 92  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
 93  - Erwartungswert berechnen und deuten (Einheit 1): „Auszahlung oder Gewinn?“ ankreuzen (Vorstufe, Grundvorstellung) → den Erwartungswert aus einer fertigen Verteilungstabelle bilden, fehlende Wahrscheinlichkeiten über die Summe ergänzen (Grundfall, viermal; iqb 2018MerhoehtAStochastik2-a, 2021MgrundlegendBStochastikWTR1-1e) → die Verteilung erst beschaffen: Werte aus dem Sachtext, Pfade des Baums, Kosten je Ausgang (fhr 2019-C-3d, abi 2018-bb-ea-A1.3b, iqb 2019MgrundlegendBStochastikWTR2-2c) → mit dem Einsatz vergleichen und im Sachzusammenhang deuten (abi 2018-be-gk-B3.1d, 2023-bebb-gk-B4.2b, iqb 2024MgrundlegendAStochastik12-b) → die fhr-Anschlussrechnung: Überschuss und Stückzahlen aus dem Mittelwert (fhr 2021-B-3e) → Prüfungshöhe: Summanden eines vorgelegten Erwartungswertterms deuten und eine Abbruch-Empfehlung begründen (abi 2023-bebb-gk-B4.2a, iqb 2023MerhoehtBStochastikWTR1-3b, Niveau II bis III).
 94  - Rückwärts (Einheit 2): „Vorwärts oder rückwärts?“ ankreuzen (Vorstufe) → die Fairness-Gleichung linear: Erwartungswert der Auszahlung gleich Einsatz (Grundfall, viermal; abi 2025-bebb-lk-A1.4b, iqb 2021MerhoehtAStochastik13-b, 2020MerhoehtAStochastik12-b) → die Verteilung in der Unbekannten aufstellen: Beschriftungen, Urnen, ohne Zurücklegen (abi 2026-bb-ea-A1.9b, iqb 2019MgrundlegendBStochastikWTR3-2c, 2025MgrundlegendAStochastik22-b) → quadratische Bedingungen und Lösungen sieben (abi 2018-be-gk-B3.1e, 2023-bebb-gk-B4.2c, iqb 2023MerhoehtAStochastik11-b) → Sonderformen: Ungleichung für Mindestanzahlen, Wertebereich aus Schranken (iqb 2023MerhoehtBStochastikWTR3-1b, 2018MerhoehtAStochastik2-b) → Prüfungshöhe: mehrere Bedingungen zugleich untersuchen und Schranken ohne Rechnung begründen (abi 2024-bebb-lk-A1.10a, iqb 2019MgrundlegendBStochastikWTR3-2b, Niveau III).
 95  - Streuung (Einheit 3): „Welche Formel für die Standardabweichung?“ ankreuzen (Vorstufe) → die Binomialformeln vorwärts: Standardabweichung aus n und Erwartungswert (Grundfall, viermal; iqb 2021MerhoehtAStochastik12-a) → rückwärts: Parameter aus Erwartungswert und Standardabweichung, Symmetrie liefert p (abi 2026-bb-gk-A1.9a, iqb 2018MerhoehtAStochastik11-b) → die allgemeine Varianz: einen Summanden als Abschätzung nutzen (iqb 2023MgrundlegendAStochastik11-b) → mit der Formel argumentieren: Parabel, Symmetrie, Vervierfachung (iqb 2022MgrundlegendBStochastikWTR2-3b, 2024MerhoehtAStochastik11-a, 2020MgrundlegendBStochastikWTR2-1d) → Prüfungshöhe: den Graphen der Standardabweichung in Abhängigkeit von p skalieren und erläutern (die Achsenskalierungs-Zeile des Pools – Beleg im Muster, die Kennung endet auf eine Ziffer und bleibt außerhalb der Sprossen).
 96  - Diagramm (Einheit 4): die Grundvorstellung als Vorstufe → den ganzzahligen Erwartungswert an der höchsten Säule ablesen und p oder die Sektorenzahl bestimmen (Grundfall, viermal; abi 2026-bb-gk-A1.6a, iqb 2026MgrundlegendAStochastik11-a, 2024MerhoehtAStochastik11-b) → zwei Verteilungen über die Lage der Maxima vergleichen (iqb 2025MerhoehtAStochastik12-b) → die Parität von n aus dem Doppelmaximum begründen (abi 2025-bebb-gk-A1.9a, iqb 2025MgrundlegendAStochastik21-a) → Prüfungshöhe: das Sigma-Intervall auf ganze Werte übertragen und die Säulenhöhen addieren (abi 2026-bb-ea-A1.4b, iqb 2026MerhoehtAStochastik11-b, Niveau III).
 97
 98  ### Prüfungsform (fhr / abi / iqb)
 99  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; maßgeblich sind RLP FOS 2019 (Pflichtthema 4) und der fhr-Katalog. Die Rohdatei zählt 79 Zeilen mit 36 Haupttypen (fhr 2 Zeilen, 1 Typ; abi 23 Zeilen, 13 Typen; iqb 54 Zeilen, 35 Typen; 13 abitur-Typen in beiden Abiturprofilen), Jahre 2017–2026 – nach Zeilen das größte Stochastik-Thema neben binomialverteilung.md. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
100  fhr (2 Zeilen, 1 Typ; FHR-Prüfungen 2019 und 2021) [fhr-Katalog]: Erwartungswert berechnen (2, E1). Muster: Beide Zeilen sind Schlussteile der Stochastik-Aufgabe mit drei und vier Punkten und höchster Niveauschätzung: die gewichtete Summe wird gebildet und trägt eine Anschlussrechnung (Überschuss des Standbetreibers aus fünfhundert Spielen 2019, Einnahmen und Mindestanzahl der Mittagsmenüs 2021 – die Anschlüsse sind als Nebentypen erfasst). Kontexte: Jahrmarkt, Gastronomie.
101  abi (23 Zeilen, 13 Typen; Landeshefte 2017–2026 aller vier Zielprüfungen) [abi-Katalog]: Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (7, E2) · Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen (5, E1) · je 1: Erwartungswert der Auszahlung mit dem Einsatz vergleichen (E1) · Summand eines Erwartungswertterms im Sachzusammenhang deuten (E1) · Prozentuale Abweichung einer Anzahl vom Erwartungswert berechnen (E1) · Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten (E2) · Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen (E2) · Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen (E2) · Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen (E2) · Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen (E3) · Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln (E4) · Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln (E4) · Parität von n aus zwei gleich hohen Säulen der Verteilung begründen (E4). Muster: Elf der 23 Zeilen liegen in Teil A (darunter alle Diagramm- und Parameterformen der Jahrgänge 2023–2026), zwölf in Teil B als Schlussglied der Glücksspiel-Aufgabe (zwei bis sechs Punkte). 15 der 23 Zeilen sind wortgleiche Pooldubletten (2017-bb-ea-A1.3b, 2021-be-gk-B4i, 2022-bebb-gk-B4c, 2023-bebb-gk-B4.2a, 2023-bebb-gk-B4.2c, 2023-bebb-lk-A1.7b, 2023-bebb-lk-B4g, 2024-bebb-gk-B4.2c, 2024-bebb-lk-A1.10a, 2025-bebb-gk-A1.9a, 2025-bebb-lk-A1.4b, 2026-bb-gk-A1.6a, 2026-bb-gk-A1.9a, 2026-bb-ea-A1.4b, 2026-bb-ea-A1.9b); landeseigen sind vor allem die frühen Hefte und die Berliner Spielaufgaben (2017-bb-ea-B4.1c, 2018-bb-ea-A1.3b, 2018-be-gk-B3.1d, 2018-be-gk-B3.1e, 2019-be-gk-B4.2c, 2021-be-gk-A1.6b, 2022-bebb-lk-B4l, 2023-bebb-gk-B4.2b). Niveau I 3, II 10, III 10. Kontexte: Glücksräder, Würfel- und Urnenspiele, Hoffest, Imbiss, Paketzentrum, Smartphone-Spiel.
102  iqb (54 Zeilen, 35 Typen; Pool 2017–2026, grundlegend 28 und erhöht 26 Zeilen, Teil A 29 und Teil B 25 Zeilen, davon 3 CAS) [iqb-Katalog]: Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (14, E2) · Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln (3, E4) · Erwartungswert der Auszahlung mit dem Einsatz vergleichen (2, E1) · Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten (2, E2) · Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen (2, E3) · Stichprobenumfang aus einer vorgegebenen Standardabweichung der Binomialverteilung berechnen (2, E3) · je 1: Summand eines Erwartungswertterms im Sachzusammenhang deuten (E1) · Erwartungswert aus einer Verteilung mit fehlender Wahrscheinlichkeit berechnen (E1) · Erwartungswert der Kosten pro Stück aus einer Wahrscheinlichkeitstabelle berechnen (E1) · Erwartungswert eines Spielgewinns über die Pfade eines Baumdiagramms berechnen (E1) · Erwartungswert der Augensumme aus dem Erwartungswert der Trefferzahl berechnen (E1) · Erwartungswert einer weiteren Runde mit dem sicheren Betrag vergleichen und eine Empfehlung begründen (E1) · Gesamtzahl der Gruppen aus der Personenzahl und der mittleren Gruppengröße unter einer vereinfachenden Annahme schätzen (E1) · Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen (E1) · Prozentuale Abweichung einer Anzahl vom Erwartungswert berechnen (E1) · Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen (E2) · Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen (E2) · Verhältnis zweier Auszahlungen aus dem Ausgleich der Erwartungswerte berechnen (E2) · Kugelzahl für den größten Erwartungswert der Auszahlung ermitteln (E2) · Kugelbeschriftung aus dem Erwartungswert der Summe beim Ziehen ohne Zurücklegen berechnen (E2) · Mindestanzahl aus einer Erwartungswertbedingung n · p > c ermitteln (E2) · Wertebereich des Erwartungswerts aus Ungleichungen für die Wahrscheinlichkeiten bestimmen (E2) · Aussage über gleiche Erwartungswerte aufeinanderfolgender Parameterwerte über eine Gleichung beurteilen (E2) · Untere Schranke für eine Kugelbeschriftung aus dem Erwartungswert der Summe ohne Rechnung begründen (E2) · Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen (E2) · Standardabweichung einer Binomialverteilung aus n und Erwartungswert berechnen (E3) · Parameter n aus Erwartungswert und Symmetrie einer Binomialverteilung ermitteln (E3) · Verhältnis der Varianzen zweier Binomialverteilungen aus dem Erwartungswert im Diagramm bestimmen (E3) · Standardabweichung über einen Summanden der Varianz abschätzen (E3) · Gleiche Standardabweichung zweier komplementärer Zufallsgrößen begründen (E3) · Unmöglichkeit einer Standardabweichung bei gegebener Versuchszahl über das Maximum von p · (1 − p) begründen (E3) · Monotonie der Varianz einer Binomialverteilung in p über die Parabel begründen (E3) · Achsen des Graphen der Standardabweichung in Abhängigkeit von p skalieren und erläutern (E3) · Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln (E4) · Parität von n aus zwei gleich hohen Säulen der Verteilung begründen (E4). Muster: 29 der 54 Zeilen liegen in Teil A – der größte hilfsmittelfreie Bestand eines Stochastik-Themas: jedes Pooljahr stellt die Erwartungswert-Rückwärtsform hilfsmittelfrei, seit 2024 kommen die Diagrammformen der Einheit 4 dazu. Seit dem Nachzug 2026-09-28 mit dem Jahrgang 2017: die Binomialparameter aus Erwartungswert und Varianz in Teil A (2017MgrundlegendAStochastik11-b, drei Punkte), die Versuchszahl zur Standardabweichung drei und ihre Unmöglichkeit bei neun Versuchen über das Maximum von p · (1 − p) (2017MgrundlegendBStochastikWTR2-2a, 2017MgrundlegendBStochastikWTR2-2b, je drei Punkte) und in der CAS-Fassung die Zahl der Haushalte aus der mittleren Haushaltsgröße (2017MerhoehtBStochastikCAS1-5, vier Punkte, Anforderungsbereich III – die gewichtete Summe als Mittelwert einer Verteilung mit Anschlussrechnung, eine Aufgabe ohne Teilaufgabenbuchstaben). Seit dem Nachzug 2026-09-29 aus der erhöhten CAS-Fassung 2018, beide ohne CAS-Anteil: die Auszahlung bei drei verschiedenen Farben am Glücksrad aus dem Ausgleich von Einsätzen und Auszahlungen (2018MerhoehtBStochastikCAS1-2b, drei Punkte, Niveau II – wortgleich mit dem WTR-Zweig 2018MerhoehtBStochastikWTR1-2b) und der erwartete Wert eines zufällig gezogenen gefälschten Geldscheins aus der Häufigkeitsverteilung der aussortierten Scheine (2018MerhoehtBStochastikCAS2-3a, drei Punkte, Anforderungsbereich I – die erste iqb-Zeile des Vorwärtstyps, der bisher nur in Landesheften stand). Grundlegend 28, erhöht 26 – die Kenngrößen sind Stoff beider Niveaus. Amtlicher Anforderungsbereich in allen 54 Zeilen (höchster Bereich: I 5, II 30, III 19); Niveau I 6, II 28, III 20. 15 Poolzeilen kehren wortgleich in Landesheften wieder (die Dublettenliste der abi-Zeile), keine abgewandelt. Kontexte: Glücksspiele aller Art, Joghurtbecher-Sammelmotive, Paketzentrum, Postzustellung, Olivenöl-Abfüllung, Brotaufstrich, Spendengala, Haushaltsstatistik, Falschgeld.
103  Zielmarke: Einheit 1 – fhr: die Menü-Mischkalkulation mit Mindestanzahl (2021-B-3e, vier Punkte, Niveau III); abi: die Selbstkosten-Falle am Glücksrad (2017-bb-ea-B4.1c, Niveau III); iqb: die Abbruch-Empfehlung über den Erwartungswert der weiteren Runde (2023MerhoehtBStochastikWTR1-3b, Teil B). Einheit 2 – abi: die quadratische Fairness-Gleichung (2018-be-gk-B3.1e, sechs Punkte, Niveau III) und das Kugelverhältnis (2023-bebb-gk-B4.2c, Niveau III); iqb: die Würfelbeschriftung mit drei Bedingungen (2024MerhoehtAStochastik22, Teil A, Niveau III). Einheit 3 – abi: die Parameter aus μ und σ (2026-bb-gk-A1.9a, Teil A, Niveau II); iqb: die Achsenskalierung des σ-Graphen (2024MgrundlegendBStochastikWTR2-3, Teil B, Anforderungsbereich III). Einheit 4 – abi und iqb: das Sigma-Intervall am Säulendiagramm (2026-bb-ea-A1.4b, 2026MerhoehtAStochastik11-b, Teil A, Niveau III).
````

## 2 Originale (35)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2017-bb-ea-A1.3b (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Drei Urnen mit den Inhalten der Abbildung: A mit zwei weißen und zwei schwarzen, B mit zwei weißen und einer schwarzen, C mit zwei weißen Kugeln. Spielregel: Es wird ein Einsatz von 1 Euro eingezahlt, danach wird eine der drei Urnen zufällig ausgewählt und aus dieser eine Kugel zufällig gezogen. Nur bei einer schwarzen Kugel wird ein bestimmter Geldbetrag ausgezahlt.
- gesucht: Höhe des Geldbetrags, damit Einsätze und Auszahlungen auf lange Sicht ausgeglichen sind
- verfahren: Wahrscheinlichkeit für Schwarz über die drei gleich wahrscheinlichen Urnen: 1/3 · (2/4 + 1/3 + 0) = 5/18. Fairness bedeutet, dass der erwartete Gewinn null ist: Auszahlung · 5/18 = 1 Euro.
- fehlerquelle: die Wahrscheinlichkeiten der drei Urnen addieren, ohne sie vorher mit 1/3 zu gewichten, oder die leere Urne C auslassen

### 2021-be-gk-B4i (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Bonuspunkte beim täglichen Start: 10 mit 50 %, 20 mit 40 %, 50 mit 10 %; die Wahrscheinlichkeiten für 10 und 20 werden so geändert, dass in 200 Tagen im Mittel 3 000 Bonuspunkte anfallen (50 bleibt bei 10 %)
- gesucht: die beiden geänderten Wahrscheinlichkeiten
- verfahren: Erwartungswert 15 pro Tag ansetzen, P(20) = 0,9 − P(10)
- fehlerquelle: den Erwartungswert 3000 statt 15 je Tag ansetzen

### 2022-bebb-gk-B4c (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Paketzentrum: 10 % der Pakete haben das Ziel A, 7 % das Ziel B; Anlage mit Tabelle der summierten Binomialverteilung; unter 100 Paketen haben genau neun das Ziel B
- gesucht: prozentuale Abweichung dieser Anzahl vom Erwartungswert
- verfahren: Erwartungswert 7, Differenz durch 7
- fehlerquelle: Abweichung auf 100 statt auf 7 beziehen

### 2023-bebb-gk-B4.2a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: In einem Behälter befinden sich vier weiße und fünf schwarze Kugeln. Der Spieler bezahlt einen Einsatz von 2 Euro, der neben dem Behälter ausgelegt wird; er zieht zweimal nacheinander eine Kugel mit Zurücklegen; nach jedem Zug wird der ausliegende Betrag verdoppelt, wenn eine weiße Kugel gezogen wird, sonst halbiert; nach dem Spiel erhält der Spieler den ausliegenden Betrag. Der Term 8 · (4/9)² + 2 · 2 · 4/9 · 5/9 + 1/2 · (5/9)² gibt den Erwartungswert für den Betrag in Euro an, den der Spieler nach dem Spiel erhält.
- gesucht: Bedeutung des zweiten der drei Summanden im Sachzusammenhang mit Erläuterung
- verfahren: Faktoren als Auszahlung 2 Euro (einmal verdoppelt, einmal halbiert), zwei Reihenfolgen weiß-schwarz und schwarz-weiß, Wahrscheinlichkeiten 4/9 und 5/9 deuten.
- fehlerquelle: den Faktor 2 für die Reihenfolgen als Auszahlung deuten

### 2023-bebb-gk-B4.2c (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: In einem Behälter befinden sich vier weiße und fünf schwarze Kugeln. Der Spieler bezahlt einen Einsatz von 2 Euro, der neben dem Behälter ausgelegt wird; er zieht zweimal nacheinander eine Kugel mit Zurücklegen; nach jedem Zug wird der ausliegende Betrag verdoppelt, wenn eine weiße Kugel gezogen wird, sonst halbiert; nach dem Spiel erhält der Spieler den ausliegenden Betrag. Das Verhältnis der Anzahlen weißer und schwarzer Kugeln ist frei wählbar; Spieler und Spielleiter sollen die gleiche Gewinnerwartung haben.
- gesucht: Verhältnis der Anzahlen der weißen und schwarzen Kugeln
- verfahren: Erwartungswert mit p (Anteil weiß) ansetzen, gleich dem Einsatz 2 setzen, quadratische Gleichung lösen (p = 1/3, p = −1 entfällt), p in ein Anzahlverhältnis übersetzen.
- fehlerquelle: gleiche Gewinnerwartung als E = 0 statt E = Einsatz ansetzen

### 2023-bebb-lk-A1.7b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Kugeln dreimal 2 und zweimal a (a < 0), zweimal Ziehen mit Zurücklegen; X ist das Produkt der gezogenen Zahlen; E(X) = 4
- gesucht: Wert von a
- verfahren: Werte 4, 2a, a² mit 9/25, 12/25, 4/25 ansetzen, E(X) = 4 nach a lösen, negative Lösung wählen
- fehlerquelle: a = 2 als Lösung nehmen und a < 0 übersehen

### 2023-bebb-lk-B4g (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Gewinnspiel mit 1 bis 5 Strandkörben; bei 1 Strandkorb Sachgewinne; Tabelle der Gutscheine; Erwartungswert des Gewinns 43,5 Cent je Person
- gesucht: Nachweis P(1 Strandkorb) > 1 − 0,001; Erwartungswert des Gewinns bei einem Strandkorb
- verfahren: Gegenwahrscheinlichkeit der Gutscheine; Erwartungswertgleichung nach dem Sachgewinn-Erwartungswert x auflösen
- fehlerquelle: Cent und Euro mischen

### 2024-bebb-gk-B4.2c (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 4 · format Rechnung · antwort Term
- gegeben: anderes Glücksrad mit Sektoren 5 und 2, P(5) = q je Drehung; Rabatt = Produkt der beiden Zahlen; auf lange Sicht im Mittel 9 % Rabatt; Gleichung 9q² + 12q − 5 = 0
- gesucht: Nachweis, dass die Gleichung den Wert q für den mittleren Rabatt 9 % liefert
- verfahren: Erwartungswert des Rabatts als Funktion von q aufstellen, gleich 9 setzen, umformen
- fehlerquelle: Rabatt 10 nur einmal (ohne Faktor 2 für die beiden Reihenfolgen) zählen

### 2024-bebb-lk-A1.10a (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 5 · format Rechnung · antwort Text
- gegeben: Würfel mit sichtbaren Seiten 5, 5, 1; drei unsichtbare Seiten sollen mit Zahlen aus 3, 4, 5, 6 beschriftet werden (Wiederholung erlaubt); Bedingungen: Erwartungswert beim einmaligen Werfen 4, genau drei verschiedene Zahlen auf dem Würfel, P(zweimal dieselbe Zahl bei zwei Würfen) = 1/2
- gesucht: Untersuchung, ob eine Beschriftung alle drei Eigenschaften erfüllt
- verfahren: aus E = 4 die Summe 24, also 13 für die verdeckten Seiten; Kandidaten mit genau drei verschiedenen Zahlen prüfen; für 3, 5, 5 die Wahrscheinlichkeit gleicher Zahlen ausrechnen
- fehlerquelle: die sichtbaren Seiten beim Erwartungswert vergessen (Summe 13 auf sechs Seiten verteilen)

### 2025-bebb-gk-A1.9a (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: binomialverteilte Zufallsgröße X mit unbekanntem n und p = 0,5, Säulendiagramm mit zwei gleich hohen höchsten Säulen bei 10 und 11; P(X = 10) = P(X = 11)
- gesucht: Begründung, dass n nicht gerade ist
- verfahren: das Maximum liegt zwischen 10 und 11, also ist E(X) = n · 0,5 = 10,5 nicht ganzzahlig
- fehlerquelle: aus der Symmetrie um 10,5 auf n = 20 schließen

### 2025-bebb-lk-A1.4b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Würfel zweimal geworfen; Einsatz 2 €; Auszahlung 0 € bei keiner 3, 5 € bei genau einer 3, x € bei zwei Dreien; auf lange Sicht gleichen sich Einsätze und Auszahlungen aus
- gesucht: Wert von x
- verfahren: Erwartungswert der Auszahlung 1/36 · x + 10/36 · 5 gleich 2 setzen
- fehlerquelle: P(genau eine 3) = 5/36 ansetzen (nur eine Reihenfolge)

### 2026-bb-gk-A1.6a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Säulendiagramm der Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße X mit n = 20 und unbekanntem p; höchste Säule bei k = 4; der Erwartungswert von X ist ganzzahlig
- gesucht: Wert von p
- verfahren: der ganzzahlige Erwartungswert liegt an der höchsten Säule, also 20 · p = 4
- fehlerquelle: p aus der Höhe der höchsten Säule (0,22) ablesen

### 2026-bb-gk-A1.9a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 5 · format Rechnung · antwort Term
- gegeben: binomialverteilte Zufallsgröße X mit Erwartungswert μ = 20 und Standardabweichung σ = 2
- gesucht: parameterfreier Term für P(X = 21)
- verfahren: aus σ^2 = n · p · (1 − p) = μ · (1 − p) folgt 4 = 20 · (1 − p), also p = 0,8 und n = μ/p = 25; dann Bernoulli-Formel für k = 21
- fehlerquelle: σ statt σ^2 in die Formel setzen und 2 = 20 · (1 − p) rechnen

### 2026-bb-ea-A1.4b (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: X binomialverteilt mit n = 36 und p = 0,5; Säulendiagramm der Verteilung mit Höhen etwa 0,13 bei k = 18 und 0,125 bei k = 17 und 19; μ Erwartungswert, σ Standardabweichung
- gesucht: Näherungswert für P(μ − 0,5 · σ <= X <= μ + 0,5 · σ)
- verfahren: μ = 36 · 0,5 = 18 und σ = √(18 · 0,5) = 3 berechnen; das Intervall [16,5; 19,5] enthält k = 17, 18, 19; deren Säulenhöhen addieren
- fehlerquelle: σ = √(n · p) = √18 rechnen oder die Grenzen 16,5 und 19,5 auf k = 16 bis 20 runden

### 2026-bb-ea-A1.9b (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: fünf Kugeln, drei mit a, zwei mit b, a + b = 17, natürliche Zahlen; zwei Kugeln werden gleichzeitig entnommen; X ist die Summe der beiden Zahlen; E(X) = 16
- gesucht: a und b
- verfahren: P(2a) = 3/5 · 2/4, P(a + b) = 2 · 3/5 · 2/4, P(2b) = 2/5 · 1/4; Erwartungswert mit b = 17 − a aufstellen und nach a auflösen
- fehlerquelle: P(a + b) nur mit einer Reihenfolge ansetzen (3/10 statt 6/10)

### 2017-bb-ea-B4.1c (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Eine Bratwurst kostet 1,50 €, der Betreiber erzielt dabei 0,30 € Gewinn je verkaufter Wurst. Er stellt ein Glücksrad aus schwarzen und weißen Sektoren auf; die weißen Sektoren nehmen zusammen einen Winkel von 36° ein. Wer Weiß dreht, erhält die Wurst kostenlos.
- gesucht: Betrag, auf den sich der Gewinn pro abgegebener Bratwurst durch die Aktion verringert
- verfahren: P(weiß) = 36°/360° = 0,1. Bei Weiß entgehen dem Betreiber die Selbstkosten von 1,50 € − 0,30 € = 1,20 €. Erwartungswert des Gewinns: 0,9 · 0,30 € + 0,1 · (−1,20 €).
- fehlerquelle: bei einer kostenlos abgegebenen Wurst nur den entgangenen Gewinn von 0,30 € statt der Selbstkosten von 1,20 € ansetzen

### 2018-bb-ea-A1.3b (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ein Landwirt plant für sein Hoffest ein Glücksrad aus blauen, gelben und roten Sektoren von je 6°. Ein Dreh kostet einen Euro. Gelb bringt einen Gutschein für eine Packung Bio-Eier, blau als Hauptgewinn einen Ökokorb, bei rot geht man leer aus. Eine Packung Bio-Eier kostet den Landwirt 1,50 €, ein Ökokorb 15 €. Die Wahrscheinlichkeit für den Hauptgewinn soll 5 % betragen, die Chance auf einen Gutschein ein Drittel.
- gesucht: Kosten, die dem Landwirt pro Dreh auf lange Sicht entstehen
- verfahren: Die Kosten je Dreh als Zufallsgröße auffassen: 15 € bei blau, 1,50 € bei gelb, 0 € bei rot. Den Erwartungswert als Summe der mit den Wahrscheinlichkeiten gewichteten Werte bilden: 15 · 0,05 + 1,50 · 1/3 + 0.
- fehlerquelle: die Einnahme von einem Euro gegenrechnen und 0,25 € angeben, obwohl nach den Kosten und nicht nach dem Saldo gefragt ist

### 2018-be-gk-B3.1d (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 2 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Der Einsatz beträgt 1 € je Spiel. Mit der Wahrscheinlichkeit 0,4 werden 2 € ausgezahlt, sonst ist der Einsatz verloren.
- gesucht: Nachweis, dass das Spiel aus Sicht des Anbieters auf lange Sicht gewinnbringend ist
- verfahren: Den Erwartungswert der Auszahlung bilden: 0,4 · 2 € = 0,80 €. Er ist kleiner als der Einsatz von 1 €, der Anbieter nimmt also im Mittel 0,20 € je Spiel ein.
- fehlerquelle: den Einsatz von 1 € nicht gegenrechnen und die Auszahlung allein als Gewinn deuten

### 2018-be-gk-B3.1e (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 6 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Zu den 4 weißen Kugeln kommen 11 weitere weiße, zu den 2 schwarzen kommen x schwarze. Es werden weiterhin zwei Kugeln mit einem Griff gezogen; gewonnen wird nur, wenn keine schwarze Kugel dabei ist. Das Spiel ist fair, wenn die Gewinnwahrscheinlichkeit q = 0,5 beträgt.
- gesucht: Nachweis, dass x = 2 nicht zu q = 0,5 führt; Anzahl der zuzugebenden schwarzen Kugeln für ein faires Spiel
- verfahren: Mit 15 weißen und 2 + x schwarzen Kugeln, also 17 + x insgesamt, ist q(x) = 15/(17 + x) · 14/(16 + x). Für x = 2 ergibt das 35/57 ≈ 0,614, also nicht 0,5. Die Gleichung q(x) = 0,5 führt auf (17 + x) · (16 + x) = 420, also x² + 33x − 148 = 0 mit der brauchbaren Lösung x = 4.
- fehlerquelle: beim Ziehen ohne Zurücklegen im zweiten Faktor den Nenner nicht um eins verringern, oder die negative Lösung der quadratischen Gleichung mitnehmen

### 2019-be-gk-B4.2c (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Sven und Tom würfeln täglich mit einem fairen Würfel: zuerst Sven, dann Tom; ist Svens Augenzahl kleiner als Toms, bringt Sven den Müll hinunter, sonst Tom; im nächsten Monat wird 30-mal gewürfelt, p = 5/12 für Sven (aus b)
- gesucht: Erwartungswert dafür, wie oft Sven im nächsten Monat den Müll hinunterbringt
- verfahren: E(X) = n · p
- fehlerquelle: mit 1/2 statt 5/12 rechnen

### 2021-be-gk-A1.6b (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Zwei Laplace-Würfel; X = 0, wenn rot < blau, X = 1 bei gleichen Augenzahlen, X = 2, wenn rot > blau; aus a P(blau > rot) = 15/36
- gesucht: Erwartungswert von X
- verfahren: Verteilung von X (15, 6, 15 von 36) und E(X) = Summe x · P(X = x)
- fehlerquelle: P(X = 2) = 21/36 (mit Gleichstand) ansetzen

### 2022-bebb-lk-B4l (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Glücksrad mit Sonne (S, p = 0,7) und Mond (M, 0,3), siebenmal gedreht, Anordnung aus sieben Symbolen; Gutscheine 2, 10, 100, 1 000 Euro bei 4, 5, 6, 7 Monden; der Markt will je Spiel durchschnittlich mindestens 20 Cent gewinnen
- gesucht: der nötige Mindesteinsatz
- verfahren: Erwartungswert der Gutscheinauszahlung, plus 0,20 €
- fehlerquelle: kumulierte statt Einzelwahrscheinlichkeiten; 20 Cent als 20 € oder als Prozent lesen

### 2023-bebb-gk-B4.2b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: In einem Behälter befinden sich vier weiße und fünf schwarze Kugeln. Der Spieler bezahlt einen Einsatz von 2 Euro, der neben dem Behälter ausgelegt wird; er zieht zweimal nacheinander eine Kugel mit Zurücklegen; nach jedem Zug wird der ausliegende Betrag verdoppelt, wenn eine weiße Kugel gezogen wird, sonst halbiert; nach dem Spiel erhält der Spieler den ausliegenden Betrag. Erwartungswert der Auszahlung 8 · (4/9)² + 2 · 2 · 4/9 · 5/9 + 1/2 · (5/9)² (aus a). Aussage: Bei sehr häufiger Durchführung des Spiels ist der erwartete Gewinn für den Spieler geringer als für den Spielleiter.
- gesucht: Beurteilung der Aussage
- verfahren: Term ausrechnen: E ≈ 2,72 Euro; der Spieler erhält im Mittel mehr als seinen Einsatz von 2 Euro, sein erwarteter Gewinn ist etwa 0,72 Euro je Spiel, der des Spielleiters etwa −0,72 Euro.
- fehlerquelle: den Erwartungswert der Auszahlung mit dem Gewinn verwechseln und E > 0 als Gewinn deuten

### 2017MgrundlegendAStochastik11-b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: X binomialverteilt mit den Parametern n und p, Erwartungswert 6, Varianz 3,6
- gesucht: Werte von n und p
- verfahren: n · p = 6 in n · p · (1 − p) = 3,6 einsetzen, 1 − p = 0,6 und damit p und n bestimmen
- fehlerquelle: 3,6 als Standardabweichung statt als Varianz verwenden

### 2017MgrundlegendBStochastikWTR2-2a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: binomialverteilte Zufallsgrößen, die für eine Trefferwahrscheinlichkeit p mit 0 <= p <= 1 die Anzahl der Treffer bei n Versuchen angeben; die Standardabweichung der Zufallsgrößen ist 3; Trefferwahrscheinlichkeit 25 %
- gesucht: die zugehörige Anzahl der Versuche
- verfahren: √(n · 0,25 · 0,75) = 3 quadrieren und nach n auflösen
- fehlerquelle: Standardabweichung und Varianz verwechseln (n = 16)

### 2017MgrundlegendBStochastikWTR2-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: binomialverteilte Zufallsgrößen, die für eine Trefferwahrscheinlichkeit p mit 0 <= p <= 1 die Anzahl der Treffer bei n Versuchen angeben; die Standardabweichung der Zufallsgrößen ist 3; Anzahl der Versuche 9
- gesucht: Begründung, dass es keinen Wert von p geben kann, für den die Anzahl der Versuche 9 ist
- verfahren: √(9 · p · (1 − p)) = 3 ⇔ p · (1 − p) = 1; p · (1 − p) ist für 0 <= p <= 1 höchstens 1/4, also gibt es keine Lösung
- fehlerquelle: die quadratische Gleichung p^2 − p + 1 = 0 lösen wollen, ohne die fehlende reelle Lösung zu deuten

### 2017MerhoehtBStochastikCAS1-5 (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Anteile der Haushalte in Deutschland 2013 nach Größe: 1-Personen-Haushalte 40,5 %, 2-Personen-Haushalte 34,5 %, 3-Personen-Haushalte 12,5 %, 4-Personen-Haushalte 9,2 %, Haushalte mit mindestens 5 Personen 3,3 %; 2013 lebten in Deutschland insgesamt etwa 80 Millionen Menschen
- gesucht: Näherungswert für die Gesamtzahl der Haushalte 2013 mit Erläuterung des Vorgehens
- verfahren: Vereinfachend 5 Personen je Haushalt der letzten Gruppe; (1 · 0,405 + 2 · 0,345 + 3 · 0,125 + 4 · 0,092 + 5 · 0,033) · x = 80 000 000 nach x lösen
- fehlerquelle: 80 Millionen durch die Zahl der Größenklassen teilen oder die Annahme für die letzte Gruppe nicht nennen

### 2018MerhoehtBStochastikCAS1-2b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Glücksrad mit den Sektoren Blau 180°, Rot 120°, Grün 60°; Einsatz 5 Euro für drei Drehungen; dreimal die gleiche Farbe: 10 Euro Auszahlung; drei verschiedene Farben: anderer Betrag; sonst nichts; P(dreimal gleiche Farbe) = 1/6; Einsätze und Auszahlungen gleichen sich auf lange Sicht aus
- gesucht: Auszahlung bei drei verschiedenen Farben
- verfahren: Erwartungswert des Gewinns gleich null setzen
- fehlerquelle: Einsatz bei den Auszahlungen nicht abziehen

### 2018MerhoehtBStochastikWTR1-2b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Glücksrad mit den Sektoren Blau 180°, Rot 120°, Grün 60°; Einsatz 5 Euro für drei Drehungen; dreimal die gleiche Farbe: 10 Euro Auszahlung; drei verschiedene Farben: anderer Betrag; sonst nichts; P(dreimal gleiche Farbe) = 1/6; Einsätze und Auszahlungen gleichen sich auf lange Sicht aus
- gesucht: Auszahlung bei drei verschiedenen Farben
- verfahren: Erwartungswert des Gewinns gleich null setzen
- fehlerquelle: Einsatz bei den Auszahlungen nicht abziehen

### 2018MerhoehtBStochastikCAS2-3a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: In der ersten Hälfte des Jahres 2015 hat die Europäische Zentralbank von etwa 17 Milliarden im Umlauf befindlichen Geldscheinen insgesamt 454000 gefälschte Scheine aussortiert; Verteilung nach Abbildung 1: 5 €: 6800, 10 €: 10800, 20 €: 248500, 50 €: 142000, 100 €: 38600, 200 €: 5000, 500 €: 2300; einer der aussortierten gefälschten Scheine wird zufällig ausgewählt; X beschreibt seinen Wert in Euro
- gesucht: Erwartungswert von X
- verfahren: Werte mit den Anzahlen gewichten, summieren und durch 454000 teilen
- fehlerquelle: das arithmetische Mittel der sieben Scheinwerte bilden oder durch 17 Milliarden teilen

### 2021-B-3e (fhr-katalog.csv)

jahr 2021 · papier B · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Vorspeise und Nachspeise kosten je 2 €, Lasagne 5 € und Backfisch 8 €; Hauptgänge werden zu gleichen Anteilen gewählt; betrachtet werden 150 verkaufte Mittagsmenüs; gefordert sind mindestens 2000 Euro Einnahmen
- gesucht: Höhe der Einnahmen bei 150 verkauften Mittagsmenüs|Anzahl der Menüs für mindestens 2000 Euro Einnahmen
- verfahren: den mittleren Preis eines Menüs als Summe aus fester Vorspeise, gewichtetem Hauptgang und fester Nachspeise bilden, mit 150 multiplizieren und anschließend 2000 Euro durch den mittleren Preis teilen und aufrunden
- fehlerquelle: 190 Menüs angeben, weil auf die nächste ganze Zahl abgerundet statt aufgerundet wird

### 2023MerhoehtBStochastikWTR1-3b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Rechnung|Begründung · antwort Zahl
- gegeben: zweiter Spieler hat Summe 60; sofort beenden oder genau einmal weiterdrehen
- gesucht: Erwartungswert der Auszahlung bei einer weiteren Drehung; Empfehlung mit Begründung
- verfahren: Erwartungswert über die zehn gleich wahrscheinlichen Ausgänge, mit 60 vergleichen
- fehlerquelle: Ausgang „0“ als Auszahlung 60 statt 0 werten

### 2024MerhoehtAStochastik22 (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 5 · format Rechnung · antwort Text
- gegeben: Würfel mit sichtbaren Seiten 5, 5, 1; drei unsichtbare Seiten sollen mit Zahlen aus 3, 4, 5, 6 beschriftet werden (Wiederholung erlaubt); Bedingungen: Erwartungswert beim einmaligen Werfen 4, genau drei verschiedene Zahlen auf dem Würfel, P(zweimal dieselbe Zahl bei zwei Würfen) = 1/2
- gesucht: Untersuchung, ob eine Beschriftung alle drei Eigenschaften erfüllt
- verfahren: aus E = 4 die Summe 24, also 13 für die verdeckten Seiten; Kandidaten mit genau drei verschiedenen Zahlen prüfen; für 3, 5, 5 die Wahrscheinlichkeit gleicher Zahlen ausrechnen
- fehlerquelle: die sichtbaren Seiten beim Erwartungswert vergessen (Summe 13 auf sechs Seiten verteilen)

### 2024MgrundlegendBStochastikWTR2-3 (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 5 · format Eintragen|Begründung · antwort Grafik
- gegeben: binomialverteilte Zufallsgrößen mit n = 15000 und p; Abbildung: σ in Abhängigkeit von p ohne Achsenwerte
- gesucht: Skalierung beider Achsen mit Erläuterung
- verfahren: p-Achse 0 bis 1 aus dem Bogen, σ für einen Gitterwert von p berechnen
- fehlerquelle: σ-Achse über das Maximum skalieren, das auf keiner Gitterlinie liegt

### 2026MerhoehtAStochastik11-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: X binomialverteilt mit n = 36 und p = 0,5; Säulendiagramm der Verteilung mit Höhen etwa 0,13 bei k = 18 und 0,125 bei k = 17 und 19; μ Erwartungswert, σ Standardabweichung
- gesucht: Näherungswert für P(μ − 0,5 · σ <= X <= μ + 0,5 · σ)
- verfahren: μ = 36 · 0,5 = 18 und σ = √(18 · 0,5) = 3 berechnen; das Intervall [16,5; 19,5] enthält k = 17, 18, 19; deren Säulenhöhen addieren
- fehlerquelle: σ = √(n · p) = √18 rechnen oder die Grenzen 16,5 und 19,5 auf k = 16 bis 20 runden

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2018MgrundlegendAStochastik12-b, 2021MerhoehtAStochastik12-a, 2023MgrundlegendAStochastik11-b, 2018MerhoehtAStochastik2-a, 2024MgrundlegendAStochastik12-b, 2025MerhoehtAStochastik11-b, 2023MerhoehtAStochastik11-b, 2020MerhoehtAStochastik12-b, 2024MerhoehtAStochastik11-a, 2018MerhoehtAStochastik11-b, 2026MgrundlegendAStochastik11-a, 2025MgrundlegendAStochastik21-a, 2021MerhoehtAStochastik13-b, 2023MgrundlegendBStochastikWTR3-2b, 2019-C-3d, 2017MerhoehtAStochastik2-b, 2019MgrundlegendBStochastikWTR2-2c, 2019MgrundlegendBStochastikWTR3-2c, 2020MerhoehtAStochastik13-b, 2021MerhoehtAStochastik22, 2021MgrundlegendBStochastikWTR1-1e, 2023MgrundlegendAStochastik12-b, 2023MgrundlegendAStochastik2, 2025MgrundlegendAStochastik22-b, 2026MerhoehtAStochastik23-b, 2023MgrundlegendBStochastikWTR3-2a, 2021MgrundlegendBStochastikWTR2-1g, 2022MgrundlegendBStochastikWTR1-1b, 2023MerhoehtBStochastikWTR2-2a, 2023MerhoehtBStochastikWTR3-1b, 2023MgrundlegendBStochastikWTR2-1d, 2025MgrundlegendBStochastikWTR3-1e, 2018MerhoehtAStochastik2-b, 2023MerhoehtBStochastikWTR1-3c, 2019MgrundlegendBStochastikWTR3-2b, 2022MerhoehtAStochastik21, 2023MgrundlegendAStochastik11-a, 2024MgrundlegendBStochastikWTR1-2c, 2026MgrundlegendAStochastik22, 2018MgrundlegendBStochastikWTR1-2, 2020MgrundlegendBStochastikWTR2-1d, 2022MgrundlegendBStochastikWTR2-3b, 2024MerhoehtAStochastik11-b, 2025MerhoehtAStochastik12-b

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
