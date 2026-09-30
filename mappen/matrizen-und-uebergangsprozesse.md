# Mappe: matrizen-und-uebergangsprozesse

Eintrag: hz-0801/mathe-nachhilfe, katalog/matrizen-und-uebergangsprozesse.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:10 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Matrizen und Übergangsprozesse
  3
  4  ### Verortung
  5  Matrizen als Rechenobjekte und als Modelle: das Rechnen (Zeile mal Spalte, Formate, Potenzen, Inverse, fehlende Kommutativität, Vertauschungs- und Permutationsmatrizen), die Vektoren unter Matrizen (M … (gekürzt, 2459 Zeichen)
  6  [GOST] Befund: Der RLP GOST Brandenburg kennt das Thema nicht – Suchprotokoll `_suche_quelle.py` in `quellen/quelle-rlp-gost-bb-2022-mathematik.txt`: „Matri“ 0 Treffer, „Übergangsprozess“ 0, „Verflech … (gekürzt, 1478 Zeichen)
  7  [FOS] Kein Bestand: „Matri“ hat im RLP FOS 2019 keinen Treffer; keine fhr-Zeile in themen.csv.
  8  [LS-AA] Das Lehrwerk führt kein Matrizen-Kapitel; der Fahrplan ordnet die Berliner L1-Zeile (Zeile 1583 der Textfassung, einziger „Matri“-Treffer) dem Kapitel Gleichungssysteme zu. Zuordnung: die Einheiten stützen sich auf kein Lehrwerkskapitel – die Systematik ist aus der Rohdatei und den Gegenstandsklassen gebaut (Ermessen, siehe Offene Punkte; dieselbe Lage wie bei scharen-von-geraden-und-ebenen.md). Stundenangaben stehen nicht im Fahrplan.
  9
 10  ### Lerneinheiten
 11  1. Matrizen als Rechenobjekte – Produkt, Potenz, Inverse: Zeile mal Spalte (Matrix mal Vektor, Matrix mal Matrix), Formate und Bildbarkeit von Produkten, Potenzen als wiederholtes Produkt (nie element … (gekürzt, 660 Zeichen)
 12    Marken: BE Q3 · BB – · GK · keine Prüfungsaufgabe
 13  2. Vektoren unter Matrizen – Fixvektoren und Struktur: M · v = t · v (Gleichungssystem, Lösungsmenge als Vielfache, Fallunterscheidung), Fixvektoren (t gleich eins), Parameter aus Matrix-Vektor-Gleich … (gekürzt, 721 Zeichen)
 14    Marken: BE Q3 · BB – · GK · keine Prüfungsaufgabe
 15  3. Verflechtung – mehrstufige Produktion: Rohstoffe, Zwischenprodukte, Endprodukte; die Stufenmatrizen und die Gesamtmatrix als Produkt (Eintrag = Summe der Pfadprodukte, Nulleintrag = kein Pfad), Dia … (gekürzt, 646 Zeichen)
 16    Marken: BE Q3 · BB – · GK · keine Prüfungsaufgabe
 17  4. Übergangsmodell – Diagramm, Matrix und Schritte: die Übergangsmatrix (Spalten = Ausgangszustand, Zeilen = Zielzustand, Spaltensumme eins bei erhaltener Gesamtheit), Übergangsdiagramm zeichnen, ausw … (gekürzt, 636 Zeichen)
 18    Marken: BE Q3 · BB – · GK · keine Prüfungsaufgabe
 19  5. Stationär und langfristig – Fixvektoren und Grenzen: die stationäre Verteilung über M · v = v (mit fester Gesamtzahl als Gleichungssystem), absorbierende Zustände, Gleichgewicht der Wechselzahlen,  … (gekürzt, 614 Zeichen)
 20    Marken: BE – · BB – · Kursart – · keine Prüfungsaufgabe
 21  Warum fünf: Die Gegenstandsklassen der Typenliste (Matrizenalgebra, Verflechtung, Übergangsprozess – Entscheidung 24 nennt dieses Thema als Anlassfall des Klassenschnitts) geben die Dreiteilung vor; d … (gekürzt, 817 Zeichen)
 22
 23  ### Typen je Lerneinheit
 24  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
 25  Einheit 1: Matrizenalgebra: Matrix-Vektor-Produkt berechnen (4) · Matrizenalgebra: Inverse Matrix über A · B = E bestimmen (3) · Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln (2) · Matrizenalgebra: Einträge einer Faktormatrix aus dem Produkt mit einer bekannten Matrix bestimmen (1) · Matrizenalgebra: Faktor aus M² als Vielfachem der Einheitsmatrix ermitteln (1) · Matrizenalgebra: Fehlende Einträge einer Matrixpotenz über Zeile mal Spalte und Spaltensumme berechnen (1) · Matrizenalgebra: Ganzzahlige Einträge einer Matrix aus ihrem Quadrat bestimmen (1) · Matrizenalgebra: Parameter aus der Gültigkeit der binomischen Formel für zwei Matrizen bestimmen (1) · Matrizenalgebra: Parameter für gleiche Spur von Matrix und Inverser bestimmen (1) · Matrizenalgebra: Quadrat einer Matrix mit Parameter berechnen (1; Ermessen, siehe Offene Punkte) — Nachweis: Matrizenalgebra: Definiertheit von Summe und Produkt zweier Matrizen über die Formate entscheiden (1; Ermessen, siehe Offene Punkte) · Matrizenalgebra: Hohe Potenz einer Vertauschungsmatrix über das Quadrat gleich Einheitsmatrix bestimmen (1; Ermessen, siehe Offene Punkte) · Matrizenalgebra: Quadrat einer Summe zweier Matrizen mit C · D = −D · C vereinfachen (1) — Deutung: Matrizenalgebra: Aufbau von Vertauschungsmatrizen mit vorgegebener Wirkung beschreiben (1) · Matrizenalgebra: Inverse einer Vertauschungsmatrix angeben (1) · Matrizenalgebra: Mögliche Formate einer Matrix aus der Bildbarkeit eines Produkts beschreiben (1) · Matrizenalgebra: Wirkung einer Permutationsmatrix beschreiben und Einträge aus M · A · M = A bestimmen (1). Dazu: Fehler finden (elementweise quadriert; Zeile mit Zeile multipliziert; die binomische Formel für Matrizen als allgemeingültig angesehen; die Inverse als Kehrwert-Matrix oder die Spur der Inversen als Kehrwert der Spur angesetzt; nur die Zeilen statt Zeilen und Spalten umsortiert; das Format nur ausgeschlossen statt beschrieben) · Begründen (warum A · B und B · A verschieden sein können; warum M² = E hohe Potenzen auf M oder E zurückführt).
 26  Einheit 2: Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen (5) · Matrizenalgebra: Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen (3) · Matrizenalgebra: Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen (2) · Matrizenalgebra: Abbildungsmatrix aus einer geometrischen Bedingung an den Bildpunkt bestimmen (1) · Matrizenalgebra: Alle Vektoren mit M · v = t · v durch Fallunterscheidung bestimmen (1) · Matrizenalgebra: Kollinearität von M · x − x mit einem Vektor untersuchen (1) · Matrizenalgebra: Parameter einer Matrix aus der Orthogonalität von v und M · v bestimmen (1) · Matrizenalgebra: Parameter einer Matrix aus einer Matrix-Vektor-Gleichung untersuchen (1) · Matrizenalgebra: Parameterbereich für endliche Grenzwerte der Matrixpotenzen über eine Potenzfolge bestimmen (1) — Nachweis: Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen (2) · Matrizenalgebra: Bedingung für eine selbstinverse Matrix mit Parametern herleiten (1) · Matrizenalgebra: Beziehung zwischen den Komponenten eines Fixvektors über das Gleichungssystem N · u = u nachweisen (1) · Matrizenalgebra: Existenz mehrerer Lösungen von M · a = 0 begründen (1) · Matrizenalgebra: Konstanten Faktor der Komponentensumme von Q · u über die Spaltensummen nachweisen (1) · Matrizenalgebra: Orthogonalität einer Matrix über das Produkt mit der Transponierten nachweisen (1) · Matrizenalgebra: Unlösbarkeit einer Matrix-Vektor-Gleichung über eine Nullzeile begründen (1) · Matrizenalgebra: Nullvektor als einzige Lösung von M · u = 0 nachweisen (1) — Deutung: Matrizenalgebra: Abbildungsmatrix als Spiegelung an einer Koordinatenachse deuten (1) · Matrizenalgebra: Existenz von Matrizen mit vorgegebener Eigenschaft über ein Gleichungssystem beurteilen (1) · Matrizenalgebra: Matrix mit vorgegebener Eigenschaft angeben (1). Dazu: Fehler finden (nur eine Lösung oder nur den Nullvektor gefunden; die Fallunterscheidung nach der Nullkomponente ausgelassen; die überzählige Gleichung nicht geprüft oder als Widerspruch gelesen; mit einer Zahlenmatrix statt allgemein gerechnet; die Spaltensummen nicht eingesetzt; nur eine Vorzeichenlösung genommen) · Begründen (warum die Lösungen von M · v = t · v Vielfache bilden; warum die überzählige Gleichung die Probe ist).
 27  Einheit 3: Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix berechnen (4) · Verflechtung: Maximale Kostensteigerung eines Rohstoffs aus einer Kostenschranke bestimmen (2) · Verflechtung: Maximale Produktionsmenge aus dem Rohstoffvorrat ermitteln (2) · Verflechtung: Produktionsmengen aus dem Rohstoffverbrauch über ein Gleichungssystem ermitteln (2) · Verflechtung: Rohstoffmenge aus den übrigen Rohstoffen über die Gesamtmatrix bestimmen (2) · Verflechtung: Bedarf eines neuen Endprodukts an Zwischenprodukten aus der Produktgleichung der Matrizen ermitteln (1) · Verflechtung: Höchstmenge aus einer Kostenschranke bei festem Mengenverhältnis ermitteln (1) · Verflechtung: Matrixeintrag aus Mengenbedingungen ermitteln (1) · Verflechtung: Produktionsmenge aus einer Anteilsbedingung an den Rohstoffverbrauch bei festem Lagerverbrauch ermitteln (1) · Verflechtung: Unbekannte Bedarfe im Diagramm aus der Gesamtmatrix bestimmen (1) · Verflechtung: Verflechtungsmatrix aus Sachbedingungen und Matrixprodukt bestimmen (1) — Nachweis: Verflechtung: Eintrag der Gesamtmatrix aus dem Diagramm bestätigen und Nulleintrag begründen (2) · Verflechtung: Format der Bedarfsmatrix aus der Anzahl der Stufenprodukte begründen (2) — Deutung: Verflechtung: Gesamtmatrix im Sachzusammenhang deuten (2) · Verflechtung: Fehlenden Eintrag des Diagramms aus der Bedarfsmatrix angeben und deuten (1) · Verflechtung: Kostengleichung mit Zeilenvektor, Matrix und Auftragsvektor erläutern und lösen (1) · Verflechtung: Matrix-Vektor-Gleichung mit konkreten Zahlen im Sachzusammenhang deuten (1) · Verflechtung: Nichtinvertierbarkeit der Gesamtmatrix im Sachzusammenhang deuten (1) · Verflechtung: Rohstoffbedarf in Abhängigkeit von einem Matrixparameter als Gerade darstellen und erläutern (1) · Verflechtung: Verflechtungsdiagramm zu einer Matrix zeichnen (1) · Verflechtung: Verflechtungsmatrix aus dem Diagramm angeben (1). Dazu: Fehler finden (mit der falschen Stufenmatrix oder mit einer Stufe allein gerechnet; einen Pfad mitgezählt, der nicht existiert; das Mengenverhältnis umgekehrt; den ersten statt des knappsten Rohstoffs genommen; den Preisanstieg linear statt exponentiell angesetzt; den Zeilenvektor als Mengen statt als Stückkosten gedeutet) · Begründen (warum die Gesamtmatrix das Produkt der Stufenmatrizen ist; warum ein Nulleintrag „kein Pfad“ heißt).
 28  Einheit 4: Übergangsprozess: Verteilung nach einem Übergang berechnen (4) · Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen (3) · Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen (3) · Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen (3) · Übergangsprozess: Spanne einer Komponente nach einem Schritt bei teilweise bekannter Verteilung ermitteln (2) · Übergangsprozess: Bereich eines Anteils in Abhängigkeit vom Matrixparameter über die Randwerte ermitteln (2) · Übergangsprozess: Matrixparameter aus einer Komponente nach einem Schritt bestimmen (2) · Übergangsprozess: Anteil nach zwei Übergängen aus dem Diagramm berechnen (1) · Übergangsprozess: Eintrag von M² berechnen und Zeile von M² im Sachzusammenhang deuten (1) · Übergangsprozess: Größtmögliche Anzahl im Vorquartal über die inverse Matrix und Nichtnegativität bestimmen (1) · Übergangsprozess: Matrixeintrag aus einer Potenz der inversen Matrix bestimmen (1) · Übergangsprozess: Matrixparameter aus einer Komponente nach zwei Schritten bestimmen (1) · Übergangsprozess: Matrixparameter aus einer Überlebensrate über zwei Stufen bestimmen (1) · Übergangsprozess: Mögliche Übergangsmatrix aus Ausgabe- und Rückgabezahlen zweier Stationen mit freiem Parameter ermitteln (1) · Übergangsprozess: Quadrat der Übergangsmatrix aus dem Diagramm berechnen (1) · Übergangsprozess: Quadrat der Übergangsmatrix berechnen und M² · v als Zustand nach zwei Schritten deuten (1) · Übergangsprozess: Unbekannte Komponente der Ausgangsverteilung aus dem Ergebnisvektor über ein Gleichungssystem ermitteln (1) · Übergangsprozess: Verhältnis der Anfangsbestände aus einer Gleichverteilung nach einem Übergang bestimmen (1) — Nachweis: Übergangsprozess: Unmöglichkeit einer Verteilung über eine negative Vorgängerkomponente begründen (2) · Übergangsprozess: Fehler in einem Übergangsdiagramm gegen die Matrix begründen (1) · Übergangsprozess: Gleichung aus gleichen Komponentensummen von Ausgabe- und Rückgabevektor nachweisen und deuten (1) — Deutung: Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen (11) · Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten (8) · Übergangsprozess: Term mit Matrixpotenz und Zugang im Sachzusammenhang auswählen und deuten (2) · Übergangsprozess: Gleichungssystem für die Verteilung vor einem Übergang aufstellen (2) · Übergangsprozess: Zustand mit dem kleinsten Wechselanteil aus der Matrix ablesen (2) · Übergangsprozess: Aussage über eine Komponente nach einem Übergang bei gleicher Ausgangsverteilung beurteilen (1) · Übergangsprozess: Aussage über eine gleichbleibende Komponente aus einer Matrixzeile beurteilen (1) · Übergangsprozess: Aussagen über Anteile nach zwei Übergängen mit M² beurteilen (1) · Übergangsprozess: Diagramm der zeitlichen Entwicklung eines Zustands aus dem Übergangsdiagramm auswählen und begründen (1) · Übergangsprozess: Geänderte Übergangsmatrix aus zwei Vorschlägen nach dem beschriebenen Wechselverhalten auswählen und begründen (1) · Übergangsprozess: Komponentensumme eines Produkts mit der diagonalfreien Matrix als Wechslerzahl deuten (1) · Übergangsprozess: Matrix bei geänderter Reihenfolge der Zustände angeben (1) · Übergangsprozess: Matrixeintrag und Spaltensumme eins im Sachzusammenhang deuten (1) · Übergangsprozess: Potenz der Übergangsmatrix als mehrschrittigen Übergang deuten (1) · Übergangsprozess: Rückrechnung eines Verteilungsvektors über die Inverse von M² beschreiben (1) · Übergangsprozess: Spielregel zu den Übergangswahrscheinlichkeiten eines Feldes angeben (1) · Übergangsprozess: Term für die Verteilung mit zwischenzeitlichem Abgang über Diagonalmatrix und Matrixpotenzen angeben (1) · Übergangsprozess: Zeile der Übergangsmatrix aus dem Diagramm angeben (1) · Übergangsprozess: Übergangsdiagramm zur Matrix auswählen und fehlende Werte angeben (1) · Übergangsprozess: Übergangsgleichung mit Matrix aus dem Diagramm aufstellen und Variablen deuten (1) · Übergangsprozess: Übergangsmatrix aus dem Diagramm unter zwei Darstellungen auswählen und ergänzen (1) · Übergangsprozess: Übergangsmatrix aus dem Übergangsdiagramm aufstellen (1) · Übergangsprozess: Aussage über laufende gegenüber einmaliger Entnahme im Sachzusammenhang beurteilen (1). Dazu: Fehler finden (Zeilen und Spalten vertauscht – das Kernfehlmuster des Themas; die Pfeilrichtung nach Zeilen statt Spalten; die Zugänge einer Zeile mit den Abgängen einer Spalte verwechselt; die Schrittzahl falsch gezählt oder den Zugang an die falsche Stelle des Terms gesetzt; vorwärts statt rückwärts gerechnet; die Summenbedingung der Gesamtheit vergessen) · Begründen (warum die Spalten die Ausgangszustände tragen und die Spaltensumme eins die Erhaltung; warum M² der Übergang über zwei Schritte ist).
 29  Einheit 5: Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen (3) · Übergangsprozess: Zeitpunkt für das Unter- oder Überschreiten einer Schranke über einen konstanten Faktor bestimmen (3) · Übergangsprozess: Stationäre Verteilung mit vorgegebener Gesamtzahl berechnen und einen Anteil beurteilen (2) · Übergangsprozess: Anteil oder Anzahl zu entfernender Individuen für einen stationären Zustand berechnen (2) · Übergangsprozess: Kleinsten Zeitpunkt für das Unterschreiten eines Anteils aus dem Matrixterm bestimmen (1) · Übergangsprozess: Parameter einer Übergangsmatrix aus einer Zykluslänge bestimmen (1) · Übergangsprozess: Wechselzahlen nach einem Übergang berechnen und Gleichgewicht deuten (1) — Nachweis: Übergangsprozess: Wachstumsfaktor je Schritt aus zwei Zuständen im Abstand mehrerer Schritte nachweisen (3; Ermessen, siehe Offene Punkte) · Übergangsprozess: Exponentielles Wachstum aus einem Eigenvektor begründen und Kurve zuordnen (1) · Übergangsprozess: Konstante prozentuale Abnahme einer Gruppe ohne Zugänge aus der Matrix begründen (1) · Übergangsprozess: Monotone Entwicklung der Anteile aus der Übergangstabelle begründen (1) · Übergangsprozess: Unmöglichkeit eines konstanten Zustands über eine negative Lösung begründen (1) · Übergangsprozess: Nichtnegativen stationären Vektor für alle Parameterwerte nachweisen und ein ganzzahliges Beispiel deuten (1; Ermessen, siehe Offene Punkte) — Deutung: Übergangsprozess: Eignung eines Populationsmodells zur langfristigen Beschreibung beurteilen (2) · Übergangsprozess: Einträge der Grenzmatrix im Sachzusammenhang deuten (2) · Übergangsprozess: Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix beschreiben (2) · Übergangsprozess: Entwicklung einer Population aus einer Potenz der inversen Matrix beschreiben (1) · Übergangsprozess: Langfristige Verteilung aus dem Übergangsdiagramm beschreiben (1) · Übergangsprozess: Potenz der Übergangsmatrix gleich Einheitsmatrix als Zyklus deuten (1) · Übergangsprozess: Stationäre Verteilung bei absorbierendem Zustand angeben (1) · Übergangsprozess: Übergangsverhalten einer parametrisierten Matrix nach Fällen im Sachzusammenhang beschreiben (1). Dazu: Fehler finden (den Fixvektor nur bis auf Vielfache bestimmt und die Gesamtzahl vergessen; alle drei Gleichungen aufgestellt und sich verloren; eine stationäre Verteilung mit lauter positiven Anteilen vermutet, obwohl ein Zustand absorbiert; den Zeitpunkt nicht aufgerundet oder um eins verfehlt; den Faktor rückwärts als Faktor vorwärts gelesen; nur den Faktor genannt, ohne die Fälle zu unterscheiden) · Begründen (warum die Gesamtzahl eine Gleichung des Fixvektorsystems ersetzt; warum ein konstanter Faktor je Schritt eine Exponentialentwicklung liefert).
 30  Zählung: 17 + 20 + 21 + 44 + 21 = 123 Haupttypen, 23 + 28 + 31 + 77 + 32 = 191 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: Pool 2017 grundlegend Teil A, erhöht Teil B; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2018 erhöht und 2017 grundlegend Teil B CAS) samt den Typumbenennungen des Abgleichlaufs 27).
 31
 32  ### Voraussetzungen (Blatt 0)
 33  Fertigkeiten (je Zeile: was, wofür):
 34  - Lineare Gleichungssysteme mit zwei und drei Unbekannten lösen, auch unterbestimmte (Parameter frei wählen) und überbestimmte (überzählige Gleichung als Probe) – das Werkzeug fast jeder Einheit. Sek-I-Thema lineare-gleichungssysteme.md (kanonisch). [GOST Eingangsvoraussetzung L1 „lösen lineare (2,2)- und (3,3)-Gleichungssysteme“; BE Q3 L1 „algorithmisches Lösungsverfahren“]
 35  - Vektoren als Listen lesen und schreiben (Zustands-, Mengen-, Kostenvektoren), Komponenten adressieren – die Modellsprache der Einheiten 3 bis 5. Sek-II-Nachbarthema vektoren-und-rechenoperationen.md; amtlich die Berliner L1-Zeile. [BE Q3 L1 „einfache Sachverhalte mit Tupeln (Listen, Vektoren) bzw. Matrizen … beschreiben“]
 36  - Anteile, Prozentsätze und Anzahlen ineinander umrechnen (Bleibe- und Wechselanteile, Gegenanteil) – die Deutungen der Einheiten 4 und 5. Sek-I-Thema prozentrechnung.md. [RLP E–F Prozentrechnung; GOST Eingangsvoraussetzung L4 „Prozentdarstellungen“]
 37  - Potenzen mit Basis unter eins fallen, Exponentialungleichungen durch Probieren oder Logarithmieren lösen, Ergebnisse sinnvoll aufrunden – die Zeitpunkte der Einheit 5. Sek-I-Thema potenz-exponentialfunktionen.md (Logarithmus als Vorrat). [GOST-OHiMi 2.1 „Logarithmen“, „einfache Exponentialgleichungen“]
 38  - Diagramme lesen und zeichnen (Knoten, Pfeile, Punktdiagramme, Kurvenformen unterscheiden) – Übergangs- und Verflechtungsdiagramme, Kurvenzuordnungen. Sek-I-Thema daten.md. [GOST Eingangsvoraussetzung L5 „Säulen- und Kreisdiagramme“ sinngemäß; Pool-Praxis]
 39  - Terme mit einer Unbekannten aufstellen und gegen Schranken auswerten (linear, mit Randwerten) – Spannen, Engpässe, Kostenschranken. Sek-I-Themen lineare-gleichungen.md, prozentrechnung.md. [GOST-OHiMi 2.1]
 40  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 41  - „Von wo nach wo?“ – zu Matrixeinträgen ankreuzen, aus welcher Spalte (Ausgang) in welche Zeile (Ziel) sie führen, und den Eintrag im Diagramm als Pfeil wiederfinden; nichts rechnen. Vor Einheit 3 bis 5. [Rohdatei: das Kernfehlmuster „Zeilen und Spalten vertauscht“; iqb 2026MerhoehtAAGLAA11-a, 2019MgrundlegendBAGLAA1WTR-1a]
 42  - „Rechnen oder deuten?“ – ankreuzen, ob ein Produkt auszurechnen ist oder ein vorgelegter Term, ein Eintrag oder eine Gleichung im Sachzusammenhang zu deuten; nichts rechnen. Vor allen Einheiten. [Rohdatei: Berechnungs- gegen Deutungstypen; iqb 2020MgrundlegendBAGLAA1WTR-1a, 2022MgrundlegendBAGLAA1WTR-1c]
 43
 44  ### Merkkasten
 45  Einheit 1 (Matrizen als Rechenobjekte):
 46      Produkt: Zeile mal Spalte – der Eintrag in Zeile i und Spalte j ist das Produkt der i-ten Zeile des linken mit der j-ten Spalte des rechten Faktors; bildbar nur, wenn die Spaltenzahl links zur Zeilenzahl rechts passt.
 47        M = ((0 | 1 | 0), (0 | 0 | 1), (1 | 0 | 0)), v = (1 | 2 | 3): M · v = (2 | 3 | 1) – die Vertauschungsmatrix schiebt die Einträge zyklisch.
 48      Potenzen: M² = M · M, nie elementweise; ein einzelner Eintrag von M² kommt aus Zeile mal Spalte, bei stochastischen Matrizen ergänzt die Spaltensumme eins fehlende Einträge.
 49      Inverse: A · A⁻¹ = E; über den Ansatz A · B = E als Gleichungssystem, bei Diagonal- und Vertauschungsformen über Kehrwerte und Rückvertauschung.
 50        A = ((7 | 4), (2 | 0)): aus A · B = E vier Gleichungen für die Einträge von B.
 51      Keine Kommutativität: im Allgemeinen ist A · B ≠ B · A – ausmultiplizieren heißt (A + B)² = A² + A · B + B · A + B², die binomische Formel gilt nur, wenn A und B vertauschbar sind; vertauschbare Matrizen findet der allgemeine Ansatz mit Produktvergleich.
 52      Auswendig (Teil A): der ganze Kasten – die Aufgabengruppe AG/LA 1 prüft das Rechnen in Prüfungsteil A ohne Hilfsmittel (Belege 2020MgrundlegendAAGLAA111-a, 2018MgrundlegendAAGLAA111-a, 2019MgrundlegendAAGLAA12-a, 2025MerhoehtAAGLAA122); eine Anlagen- oder Formelsammlungsstütze gibt es nicht (Befund Plan) – begründetes Ermessen mit Poolbeleg.
 53      Formelsammlung: keine – die IQB-Formelsammlung führt keine Matrizen – [FS] offen
 54  Quelle: eigene Formulierung nach der Poolpraxis der Alternative A1 [IQB-STR 1]; Zahlenbeispiele aus dem Pool (2020MgrundlegendAAGLAA111-a, 2018MgrundlegendAAGLAA111-a, wörtlich); kein Lehrwerkskapitel (LS-AA führt keine Matrizen).
 55
 56  Einheit 2 (Vektoren unter Matrizen):
 57      M · v = t · v: das Produkt komponentenweise gleichsetzen – ein Gleichungssystem; die Lösungen bilden Vielfache eines Vektors, und Fälle (eine Komponente null?) gehören dazu.
 58        M = ((1 | 3), (1 | −1)), M · v = 2 · v: beide Gleichungen liefern v₁ = 3 · v₂ – alle Vielfachen von (3 | 1).
 59      Fixvektoren: t gleich eins (M · v = v) – die Verteilung, die die Matrix nicht ändert.
 60      Stochastisch: Einträge nicht negativ, jede Spaltensumme eins – eine stochastische Matrix erhält die Komponentensumme jedes Vektors; der Nachweis läuft allgemein über a + c = 1 und b + d = 1, nicht am Zahlenbeispiel.
 61      Überzählige Gleichung: liefert das System mehr Gleichungen als Unbekannte, sind die Werte aus zwei Gleichungen zu bestimmen und in der dritten zu prüfen – sie ist Probe, kein Widerspruch.
 62      Mit der Inversen: Gleichungen mit A⁻¹ löst man durch Multiplizieren mit A und Ausnutzen von A · v = k · v – die Inverse selbst wird nicht berechnet.
 63      Auswendig (Teil A): „M · v = t · v“, „Fixvektoren“ und „Stochastisch“ – die Klassiker der Aufgabengruppe AG/LA 1 in Teil A (Belege 2023MgrundlegendAAGLAA12, 2022MerhoehtAAGLAA112-b, 2022MerhoehtAAGLAA12-a, 2020MerhoehtAAGLAA12); begründetes Ermessen mit Poolbeleg (kein Planinhalt).
 64      Formelsammlung: keine – [FS] offen
 65  Quelle: eigene Formulierung nach der Poolpraxis der Alternative A1 [IQB-STR 1] und [IQB-VER 3.1] (Abbildungsmatrizen nicht vorausgesetzt – die Begriffe stehen in der Aufgabe); Zahlenbeispiel aus dem Pool (2022MerhoehtAAGLAA112-b, wörtlich).
 66
 67  Einheit 3 (Verflechtung):
 68      Zwei Stufen: Rohstoffe r, Zwischenprodukte z, Endprodukte e mit r = A · z und z = B · e; die Gesamtmatrix A · B ordnet Endproduktmengen direkt Rohstoffmengen zu.
 69      Pfade: jeder Eintrag der Gesamtmatrix ist die Summe der Pfadprodukte über die Zwischenstufe; ein Nulleintrag heißt: kein Pfad vom Rohstoff zum Produkt.
 70      Formate: die Zeilenzahl kommt von der Ausgangsstufe (Rohstoffe), die Spaltenzahl von der Zielstufe (Produkte) – Formate lassen sich aus den Stufengrößen begründen, Produkte nur bilden, wenn sie passen.
 71      Vorwärts und rückwärts: Bedarf = Matrix mal Produktionsvektor; aus bekanntem Verbrauch liefert das Gleichungssystem die Produktionsmengen.
 72      Engpass und Kosten: die maximale Menge bestimmt der knappste Rohstoff (jede Zeile gegen den Vorrat); Kosten stehen als Zeilenvektor mal Matrix mal Auftragsvektor, Schranken führen auf Ungleichungen – Preisanstiege sind exponentiell, nicht linear.
 73      Auswendig (Teil A): „Zwei Stufen“, „Pfade“ und „Formate“ – Teil-A-Belege 2021MgrundlegendAAGLAA111-a, 2021MerhoehtAAGLAA113-b, 2024MgrundlegendAAGLAA111-a, 2024MerhoehtAAGLAA11-a; begründetes Ermessen mit Poolbeleg (kein Planinhalt).
 74      Formelsammlung: keine – [FS] offen
 75  Quelle: eigene Formulierung nach der Poolpraxis der Alternative A1 [IQB-STR 1]; ohne wörtliches Zahlenbeispiel (die Diagramm- und Matrixdaten der Poolzeilen sind zu umfangreich für einen Kasten – Ermessen).
 76
 77  Einheit 4 (Übergangsmodell):
 78      Übergangsmatrix: die Spalte sagt, woher, die Zeile, wohin – der Eintrag in Zeile i und Spalte j ist der Anteil, der von Zustand j nach Zustand i wechselt; die Diagonale trägt die Bleiber, die Spaltensumme eins die Erhaltung der Gesamtheit.
 79        Zwei Baumärkte: von A bleiben siebzig Prozent, von B achtzig: M = ((0,7 | 0,2), (0,3 | 0,8)) – erst die Spalten füllen, dann die Zeilen lesen.
 80      Diagramm: Pfeile sind Einträge, Schleifen die Diagonale; beim Zeichnen spaltenweise vorgehen, beim Prüfen jeden Pfeil gegen den Eintrag halten.
 81      Schritte: v nach einem Schritt ist M · v, nach zwei Schritten M² · v (M² ist selbst die Übergangsmatrix über zwei Schritte); rückwärts rechnet die Inverse; ein Zugang z zum Zeitpunkt k steht im Term an der Stelle k – P · (P · v + z) heißt: erst ein Schritt, dann Zugabe, dann noch ein Schritt.
 82      Rückwärtsfragen: unbekannte Komponenten oder Matrixparameter kommen aus einer Zeile des Produkts als Gleichung; Ergebnisse an der Gesamtzahl und an der Nichtnegativität prüfen.
 83      Auswendig (Teil A): „Übergangsmatrix“, „Diagramm“ und „Schritte“ – die Teil-A-Klassiker der Aufgabengruppe AG/LA 1 (Belege 2017MerhoehtAAGLAA112-a, 2019MgrundlegendAAGLAA11-a, 2022MgrundlegendAAGLAA11-a, 2018MerhoehtAAGLAA111-a); begründetes Ermessen mit Poolbeleg (kein Planinhalt).
 84      Formelsammlung: keine – [FS] offen
 85  Quelle: eigene Formulierung nach der Poolpraxis der Alternative A1 [IQB-STR 1] und dem Berliner Zusatzkurs ma-Z7 („Darstellung der Übergangswahrscheinlichkeiten durch Graphen und Matrizen“) als loser amtlicher Stütze; Zahlenbeispiel aus dem Pool (2018MgrundlegendBAGLAA1WTR-1a, wörtlich, in Zahlwörtern angesetzt).
 86
 87  Einheit 5 (Stationär und langfristig):
 88      Fixvektor: M · v = v – die Verteilung, die sich nicht mehr ändert; bei fester Gesamtzahl ersetzt die Summenbedingung eine der Gleichungen (eine ist stets überflüssig).
 89      Absorbierend: hat ein Zustand keine Abgänge, sammelt sich dort auf lange Sicht alles – die stationäre Verteilung liegt ganz in ihm; Übergänge nur in eine Richtung machen die Entwicklung monoton.
 90      Zyklen: Mⁿ = E heißt: nach n Schritten ist jede Verteilung wieder die alte; Mⁿ = c · E: alle Anzahlen ändern sich je n Schritte um den Faktor c – die Fälle c kleiner, gleich und größer eins trennen Schrumpfen, Kreislauf und Wachsen.
 91      Exponentiell: aus P · v = r · v folgt, dass die Verteilung je Schritt den Faktor r trägt (Potenzentwicklung); ein konstanter Faktor je Schritt führt bei Schwellenfragen auf eine Exponentialungleichung – Zeitpunkt aufrunden und „erstmals“ prüfen.
 92      Grenzmatrix: gleiche Spalten heißen: die langfristigen Anteile hängen nicht vom Start ab – die Einträge sind die Anteile je Zustand.
 93      Auswendig (Teil A): „Fixvektor“ und „Zyklen“ – Teil-A-Belege 2018MerhoehtAAGLAA111-c, 2018MgrundlegendAAGLAA112-c, 2019MgrundlegendAAGLAA12-b, 2026MerhoehtAAGLAA11-b; „Exponentiell“ und „Grenzmatrix“ sind Prüfungshöhe derselben Poolpraxis; begründetes Ermessen mit Poolbeleg (kein Planinhalt; der Berliner Zusatzkurs nennt „Grenzwahrscheinlichkeiten“).
 94      Formelsammlung: keine – [FS] offen
 95  Quelle: eigene Formulierung nach der Poolpraxis der Alternative A1 [IQB-STR 1] und dem Zusatzkurs ma-Z7 („Grenzwahrscheinlichkeiten“) als loser amtlicher Stütze; ohne wörtliches Zahlenbeispiel (Ermessen).
 96
 97  ### Typische Fehler
 98  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 154 Zeilen des Themas in abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Didaktik der Linearen Algebra, die Muster sind allein aus den Katalogzeilen belegt.
 99  - Zeilen und Spalten vertauscht – das Kernfehlmuster des Themas: die Matrix transponiert aufgestellt oder gelesen, die Pfeilrichtung des Diagramms nach Zeilen statt Spalten, die Zugänge einer Zeile mit den Abgängen einer Spalte verwechselt, Zeile und Spalte beim Produkt oder beim Deuten vertauscht, nur die Zeilen statt Zeilen und Spalten umsortiert. [iqb 2026MerhoehtAAGLAA11-a, 2025MerhoehtAAGLAA11-b, 2024MgrundlegendAAGLAA111-a, 2024MerhoehtAAGLAA11-b, 2022MgrundlegendAAGLAA11-a, 2022MerhoehtAAGLAA111-a, 2022MerhoehtAAGLAA111-c, 2021MgrundlegendAAGLAA111-a, 2020MgrundlegendAAGLAA111-a, 2020MerhoehtAAGLAA11-a, 2020MerhoehtAAGLAA11-b, 2019MgrundlegendAAGLAA11-a, 2018MerhoehtAAGLAA111-a, 2018MerhoehtAAGLAA112-a, 2017MerhoehtAAGLAA112-a, 2023MerhoehtAAGLAA112-b, 2026MgrundlegendBAGLAA1WTR-1a, 2026MgrundlegendBAGLAA1WTR-1b, 2026MgrundlegendBAGLAA1MMS-1a, 2026MerhoehtBAGLAA1WTR-2b, 2026MerhoehtBAGLAA1MMS-2b, 2025MgrundlegendBAGLAA1WTR-1a, 2024MgrundlegendBAGLAA1WTR-1a, 2024MgrundlegendBAGLAA1WTR-1b, 2024MerhoehtBAGLAA1WTR-1a, 2023MgrundlegendBAGLAA1WTR-2c, 2022MerhoehtBAGLAA1WTR-2a, 2022MgrundlegendBAGLAA1WTR-1a, 2021MgrundlegendBAGLAA1WTR-1a, 2020MgrundlegendBAGLAA1WTR-1b, 2019MgrundlegendBAGLAA1WTR-1a, 2019MgrundlegendBAGLAA1WTR-1b, 2019MgrundlegendBAGLAA1WTR-1c, 2018MgrundlegendBAGLAA1WTR-1e]
100  - Elementweise gerechnet, Rechenregeln verfehlt: Potenzen als komponentenweise Quadrate oder dritte Potenzen, Zeile mit Zeile multipliziert, die binomische Formel als allgemeingültig angesehen oder mit dem Faktor zwei angewendet, beim vollständigen Ausmultiplizieren verrechnet, nur triviale vertauschbare Matrizen gefunden, die Inverse mit einer Formel statt über M² = E, die Spur der Inversen als Kehrwert, Mᵀ · M mit M · M verwechselt, die Potenz nicht aufgelöst, die falsche Matrix als Inverse angegeben, Diagonaleinsen mit der Einheitsmatrix verwechselt, die Zuordnung der Produktgleichungen vertauscht, das Format nur ausgeschlossen statt beschrieben, Vorzeichen der Kehrwerte verfehlt, eine Matrix mit Nullzeile als orthogonal angegeben. [iqb 2026MerhoehtAAGLAA11-b, 2022MgrundlegendAAGLAA11-b, 2022MerhoehtAAGLAA112-a, 2019MgrundlegendAAGLAA12-a, 2018MgrundlegendAAGLAA112-b, 2022MgrundlegendBAGLAA1WTR-1d, 2018MgrundlegendAAGLAA12-a, 2018MgrundlegendAAGLAA12-b, 2025MerhoehtAAGLAA122, 2024MerhoehtAAGLAA121, 2021MerhoehtAAGLAA122, 2022MgrundlegendAAGLAA12, 2021MerhoehtAAGLAA111, 2019MerhoehtAAGLAA12-a, 2019MerhoehtAAGLAA12-b, 2020MgrundlegendAAGLAA111-b, 2020MgrundlegendAAGLAA111-c, 2018MgrundlegendAAGLAA111-a, 2018MgrundlegendAAGLAA111-b, 2020MgrundlegendAAGLAA112-a, 2026MerhoehtAAGLAA122-a]
101  - Lösungsmengen verkürzt: nur eine Lösung oder nur den Nullvektor gefunden, die Fallunterscheidung nach der Nullkomponente ausgelassen, Vielfache oder die zweiparametrige Lösungsmenge unterschlagen, nur eine Vorzeichenlösung genommen und die Aussage falsch beurteilt, die überzählige Gleichung als Widerspruch statt als Probe gelesen, Ganzzahligkeitsfälle verloren, den Vektor mit seiner Bedingung verwechselt. [iqb 2023MgrundlegendAAGLAA12, 2024MgrundlegendAAGLAA12-a, 2024MgrundlegendAAGLAA12-b, 2022MerhoehtAAGLAA112-b, 2022MerhoehtAAGLAA12-a, 2020MgrundlegendAAGLAA112-b, 2020MgrundlegendAAGLAA12, 2026MerhoehtAAGLAA122-b, 2025MgrundlegendAAGLAA11, 2026MgrundlegendBAGLAA1WTR-1d, 2018MerhoehtAAGLAA111-c, 2026MerhoehtAAGLAA121-a, 2026MerhoehtAAGLAA121-b]
102  - Stationäres verfehlt: den Fixvektor nur bis auf Vielfache bestimmt und die Gesamtzahl vergessen, alle Gleichungen aufgestellt und sich verloren, den falschen Matrixeintrag geändert, die Verbleibrate nicht angepasst, die Spaltensummen nicht auf eins gesetzt, beide Komponenten konstant gefordert, einen Fixvektor gesucht, wo keiner existiert, eine stationäre Verteilung mit lauter positiven Anteilen vermutet, die Bleibenden statt der Wechsler berechnet, die Wechselanteile vertauscht. [iqb 2025MerhoehtBAGLAA1WTR-1b, 2021MgrundlegendBAGLAA1WTR-1b, 2025MgrundlegendBAGLAA1WTR-1c, 2026MgrundlegendBAGLAA1MMS-1e, 2019MgrundlegendBAGLAA1WTR-1f, 2018MerhoehtBAGLAA1WTR-2c, 2018MerhoehtBAGLAA1WTR-2d, 2019MerhoehtAAGLAA11-a, 2018MgrundlegendBAGLAA1WTR-1b, 2018MgrundlegendBAGLAA1WTR-1a]
103  - Zeitrichtung und Schrittzahl: vorwärts statt rückwärts gerechnet oder den Faktor der Inversen vorwärts gelesen, die Inverse nur einmal angewendet, Ein- und Ausgangsvektor vertauscht, die Abnahme auf den falschen Wert bezogen, die Zulässigkeit der Rückrechnung nicht geprüft, die Reihenfolge der Stufenmatrizen vertauscht, im zweiten Schritt wieder vom Anfang ausgegangen, die Tage zwischen Entnahme und Rückgabe falsch gezählt, den Zugang an die falsche Stelle des Terms gesetzt, einen Pfad vergessen, die Potenz als Vielfaches der Kundenzahl gedeutet, die Zwischenzeitpunkte mitbehauptet, quadrieren wollen statt einen Eintrag zu berechnen, nur die Summe geprüft. [iqb 2018MgrundlegendBAGLAA1WTR-1c, 2023MerhoehtAAGLAA12-b, 2018MerhoehtAAGLAA112-b, 2019MgrundlegendBAGLAA1WTR-1d, 2020MgrundlegendBAGLAA1WTR-1a, 2021MgrundlegendBAGLAA1WTR-1d, 2025MerhoehtBAGLAA1WTR-1c, 2026MgrundlegendBAGLAA1MMS-1c, 2018MerhoehtBAGLAA1WTR-2a, 2018MerhoehtBAGLAA1WTR-2b, 2024MgrundlegendBAGLAA1WTR-1d, 2022MgrundlegendBAGLAA1WTR-1f, 2026MgrundlegendBAGLAA1WTR-1c, 2019MgrundlegendAAGLAA11-b, 2018MgrundlegendBAGLAA1WTR-1f, 2018MgrundlegendAAGLAA112-c, 2023MerhoehtAAGLAA12-a]
104  - Schranken und Rundung: nicht aufgerundet oder den Zeitpunkt um eins verfehlt, die negative Lösung nicht verworfen, den ersten statt des knappsten Rohstoffs genommen, die falsche Zielgröße abgegeben, den Preisanstieg linear statt exponentiell angesetzt, die Summenbedingung beim Variieren vergessen, den Anteil nur für einen Parameterwert berechnet. [iqb 2024MerhoehtBAGLAA1WTR-1d, 2026MgrundlegendBAGLAA1MMS-1d, 2021MgrundlegendBAGLAA1WTR-1f, 2019MerhoehtAAGLAA11-b, 2024MerhoehtBAGLAA1WTR-1b, 2026MerhoehtBAGLAA1WTR-2c, 2026MerhoehtBAGLAA1MMS-2c, 2026MerhoehtBAGLAA1WTR-2d, 2026MerhoehtBAGLAA1MMS-2d, 2024MgrundlegendBAGLAA1WTR-1c, 2018MgrundlegendBAGLAA1WTR-1g]
105  - Am Beispiel statt allgemein, Fälle übersehen: mit einer Zahlenmatrix statt allgemein gerechnet, nur ein Zahlenbeispiel geprüft, die Spaltensummen nicht eingesetzt, nur den Faktor genannt ohne Fallunterscheidung, einen Randfall ausgeschlossen oder übersehen, nur die übereinstimmenden Einträge geprüft, den späteren Zeitpunkt nicht kontrolliert, sich im Gleichungssystem verloren, Bedingungen gesucht, die herausfallen, die Gleichverteilung falsch angesetzt, eine Restgruppe vergessen, die Kurvenform falsch zugeordnet. [iqb 2022MerhoehtAAGLAA12-b, 2025MgrundlegendBAGLAA1WTR-1b, 2024MerhoehtBAGLAA1WTR-1c, 2018MerhoehtAAGLAA111-b, 2022MgrundlegendBAGLAA1WTR-1e, 2019MgrundlegendAAGLAA12-b, 2022MerhoehtBAGLAA1WTR-2c, 2022MerhoehtBAGLAA1WTR-2d, 2021MgrundlegendBAGLAA1WTR-1e, 2020MerhoehtAAGLAA12, 2017MerhoehtAAGLAA112-b, 2023MgrundlegendAAGLAA112-a, 2023MgrundlegendAAGLAA112-b, 2021MgrundlegendBAGLAA1WTR-1c, 2022MerhoehtBAGLAA1WTR-2b, 2026MgrundlegendBAGLAA1MMS-1b, 2026MgrundlegendBAGLAA1WTR-1e]
106  - Verflechtung: Stufen und Wege verfehlt: mit der falschen Stufenmatrix oder einer Stufe allein gerechnet, einen nicht existierenden Pfad mitgezählt, das Mengenverhältnis umgekehrt, den Eintrag aus der falschen Matrix gelesen, den bekannten Wert an der falschen Stelle eingesetzt, die Hin- statt der Rückrichtung gedeutet, Unbekannte für nötig gehalten, die eine Zeile genügt, den Bedarf über die feste statt die parametrisierte Matrix berechnet, im Sachzusammenhang gerechnet statt begründet, den Weg über die Zwischenstufe ausgelassen, die Bedarfe aus dem Diagramm statt aus der Matrix zusammengesetzt, die falsche Tabelle genommen, den Lagerbestand ignoriert, den Zeilenvektor als Mengen gedeutet, das Größenverhältnis falsch herum angesetzt. [iqb 2024MerhoehtAAGLAA11-a, 2021MgrundlegendAAGLAA111-b, 2021MerhoehtAAGLAA113-a, 2021MerhoehtAAGLAA113-b, 2024MgrundlegendAAGLAA111-b, 2023MgrundlegendBAGLAA1WTR-2a, 2023MgrundlegendBAGLAA1WTR-2b, 2023MerhoehtBAGLAA1WTR-1a, 2023MerhoehtBAGLAA1WTR-1b, 2023MerhoehtBAGLAA1WTR-1c, 2023MerhoehtBAGLAA1WTR-1d, 2023MerhoehtBAGLAA1WTR-1e, 2020MgrundlegendBAGLAA1WTR-1a, 2020MgrundlegendBAGLAA1WTR-1c, 2020MgrundlegendBAGLAA1WTR-1d, 2025MerhoehtBAGLAA1MMS-2a, 2025MerhoehtBAGLAA1MMS-2b, 2025MerhoehtBAGLAA1MMS-2c, 2026MerhoehtBAGLAA1WTR-2a, 2026MerhoehtBAGLAA1MMS-2a]
107  - Deutung am Übergangsmodell verfehlt: den Gegenanteil statt des Anteils angegeben, Bleiber und Wechsler verwechselt, fremde Pfeile mitgelesen, Anteile als Wahrscheinlichkeiten einer einzelnen Runde gedeutet, eine Null falsch gelesen, Anzahl statt Anteil abgegeben, einen Term als Gesamtzahl gedeutet, den Rest über die falsche Zeile berechnet, die falsche Zeile verwendet, eine Gleichung ausrechnen wollen statt Komponentensummen zu vergleichen, die Spiegelachse vertauscht, den Faktor der Streckung falsch herum genommen. [iqb 2018MgrundlegendAAGLAA112-a, 2018MgrundlegendBAGLAA1WTR-1b, 2023MerhoehtAAGLAA112-a, 2023MerhoehtAAGLAA112-c, 2025MerhoehtBAGLAA1WTR-1a, 2022MgrundlegendBAGLAA1WTR-1b, 2022MgrundlegendBAGLAA1WTR-1c, 2018MgrundlegendBAGLAA1WTR-1d, 2018MgrundlegendBAGLAA1WTR-1h, 2019MgrundlegendBAGLAA1WTR-1e, 2018MerhoehtAAGLAA12-a, 2018MerhoehtAAGLAA12-b, 2022MerhoehtAAGLAA111-b]
108
109  ### Für schwache Schüler
110  Mindeststoff (GK-Kern Q3 / Niveaustufe H / RLP FOS) [GOST, IQB-STR, IQB-VER]: Einen amtlichen Plan-Mindeststoff gibt es nicht – das Thema steht in keinem Kern der beiden Länder (Befund Plan); der Maßstab ist die Poolpraxis der Aufgabengruppe AG/LA 1. Als Kern für jeden Schüler, der das Thema lernt: die Kästen eins (Produkt, Potenz, Inverse), zwei (M · v = t · v, stochastische Matrizen) und vier (Übergangsmatrix, Diagramm, Schritte) – sie tragen die Teil-A-Zeilen beider Niveaus; Kasten drei (Verflechtung) und fünf (stationär, langfristig) tragen die Teil-B-Arbeit. Ohne Hilfsmittel (Prüfungsteil A): 73 der 154 Zeilen liegen in Teil A – die Rechen- und Deutungsgrundfälle müssen ohne Rechner sitzen, eine Formelsammlungsstütze gibt es nicht (die IQB-Formelsammlung führt keine Matrizen). Vorrat (Ermessen nach dem Niveau der Rohdatei): die Struktur- und Existenzaufgaben der Einheit 2 (orthogonal, selbstinvers, Grenzverhalten), die Kosten- und Engpassketten der Einheit 3, die Term- und Fallbeschreibungen der Einheit 5. Niveaustufe H der E-Phase [RLP]: kein Sek-I-Bestand zu Matrizen. RLP FOS (fhr): kein Bestand, keine Zeile. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung keine Matrizenrechnung im Grundteil – kein zusätzlicher Posten.
111  Grundvorstellung (Blatt 0) [Poolpraxis, MO]: Die Übergangsmatrix ist eine Maschine „von Spalte nach Zeile“ – jede Spalte verteilt ihren Bestand auf die Zeilen. „Hier sind zwei Schalen A und B mit Bohnen, kein Term. Regel je Runde: von den Bohnen in A wandert ein Viertel nach B, der Rest bleibt; von den Bohnen in B wandert die Hälfte nach A, der Rest bleibt. Spiele zwei Runden mit einer Startfüllung deiner Wahl und protokolliere die Stände. Woher weißt du bei jeder Bohne, wohin sie darf – entscheidet ihre Herkunft oder ihr Ziel? Was bleibt in jeder Runde gleich, egal wie du startest? Und gibt es eine Startfüllung, bei der sich nach einer Runde nichts geändert hat – wie würdest du sie suchen?“ Wer die Regel vom Ziel her liest (die Zeilen als Herkunft), wer die Gesamtzahl aus dem Blick verliert oder wer die Gleichgewichtsfrage durch Probieren einzelner Bohnen beantworten will, braucht das vor jeder Matrix: Die Spalte sagt, woher, die Zeile, wohin, die Spaltensumme eins erhält die Gesamtheit, und das Gleichgewicht ist eine Gleichung, keine Stichprobe. Verständnis, nicht Verfahren; eine amtliche Eingangsvoraussetzung gibt es nicht – die Vorstellung ist Ermessen mit Poolbeleg, das Kernfehlmuster (Zeilen und Spalten vertauscht) ist das bestbelegte des Themas. [Poolpraxis AG/LA 1; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Zeilen und Spalten vertauschen“, iqb 2017MerhoehtAAGLAA112-a; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
112  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [Rohdatei; Sprossenfolge Ermessen, das Lehrwerk führt kein Matrizen-Kapitel]:
113  - Matrizen als Rechenobjekte (Einheit 1): „Rechnen oder deuten?“ ankreuzen (Vorstufe) → Matrix mal Vektor über Zeile mal Spalte (Grundfall, viermal; iqb 2020MgrundlegendAAGLAA111-a, 2024MgrundlegendBAGLAA1WTR-1b, 2026MgrundlegendBAGLAA1MMS-1b, 2026MgrundlegendBAGLAA1WTR-1b, Teil A und B) → Formate und Bildbarkeit begründen (iqb 2018MgrundlegendAAGLAA111-b, Teil A) → Quadrat und einzelne Potenzeinträge (iqb 2019MgrundlegendAAGLAA12-a, 2022MgrundlegendBAGLAA1WTR-1d) → die Inverse über den Produktansatz, Kehrwerte und Rückvertauschung (iqb 2018MgrundlegendAAGLAA111-a, 2020MgrundlegendAAGLAA112-a, 2020MgrundlegendAAGLAA111-b, Teil A) → Vertauschungs- und Permutationsmatrizen beschreiben und nutzen (iqb 2020MgrundlegendAAGLAA111-c, 2024MerhoehtAAGLAA121, 2019MerhoehtAAGLAA12-b, Teil A) → Einträge aus Produktgleichungen bestimmen (iqb 2018MerhoehtBAGLAA1WTR-2a, 2020MgrundlegendAAGLAA12, 2022MgrundlegendBAGLAA1WTR... siehe Muster; 2019MgrundlegendAAGLAA... Quadrat mit Parameter) → Prüfungshöhe: vertauschbare Matrizen allgemein ermitteln und die binomische Formel prüfen (iqb 2021MerhoehtAAGLAA122, 2025MerhoehtAAGLAA122, 2018MgrundlegendAAGLAA12-a, 2018MgrundlegendAAGLAA12-b, Teil A) und die Spur gegen die Inverse (iqb 2021MerhoehtAAGLAA111, Teil A).
114  - Vektoren unter Matrizen (Einheit 2): „Für alle oder am Beispiel?“ – ankreuzen, ob eine Aussage allgemein (mit Variablen, Spaltensummen) zu zeigen ist oder ein Zahlenbeispiel genügt; nichts rechnen (Vorstufe) → einen Fixvektor über das Gleichungssystem bestimmen (Grundfall, viermal; iqb 2020MgrundlegendAAGLAA112-b, 2022MerhoehtAAGLAA12-a, Teil A) → alle Lösungen von M · v = t · v als Vielfache, mit Fallunterscheidung (iqb 2022MerhoehtAAGLAA112-b, 2023MgrundlegendAAGLAA12, 2024MgrundlegendAAGLAA12-b, 2024MgrundlegendAAGLAA12-a, Teil A) → Parameter aus Matrix-Vektor-Gleichungen mit Probe (iqb 2026MerhoehtAAGLAA121-a, 2025MgrundlegendAAGLAA11, 2025MerhoehtAAGLAA11-b, Teil A) → die stochastische Erhaltung allgemein nachweisen (iqb 2020MerhoehtAAGLAA12, 2022MerhoehtAAGLAA12-b, 2024MerhoehtBAGLAA1WTR-1c, Teil A und B) → definierte Begriffe auswerten: orthogonal, selbstinvers (iqb 2019MerhoehtAAGLAA12-a, 2022MgrundlegendAAGLAA12, 2026MerhoehtAAGLAA122-a, 2026MerhoehtAAGLAA122-b, Teil A) → Kern und Unlösbarkeit über Zeilen begründen (iqb 2023MgrundlegendAAGLAA112-a, 2023MgrundlegendAAGLAA112-b, Teil A) → Prüfungshöhe: die Gleichung mit der Inversen über die Eigenvektorbeziehung lösen (iqb 2026MerhoehtAAGLAA121-b, Teil A, Niveau III), das Grenzverhalten der Potenzfolge (iqb 2022MerhoehtBAGLAA1WTR-2c) und die Abbildungsmatrizen der Ebene (iqb 2018MerhoehtAAGLAA12-a, 2018MerhoehtAAGLAA12-b, Teil A).
115  - Verflechtung (Einheit 3): „Von wo nach wo?“ ankreuzen (Vorstufe) → den Rohstoffbedarf als Matrix mal Produktionsvektor berechnen (Grundfall, viermal; iqb 2024MerhoehtAAGLAA11-a, 2025MerhoehtBAGLAA1MMS-2a, 2026MerhoehtBAGLAA1MMS-2a, 2026MerhoehtBAGLAA1WTR-2a, Teil A und B) → Diagramm und Matrix ineinander übersetzen (iqb 2021MgrundlegendAAGLAA111-a, 2024MgrundlegendAAGLAA111-a, 2023MerhoehtBAGLAA1WTR-1a, Teil A) → Formate begründen und die passende Stufenmatrix auswählen (iqb 2020MgrundlegendBAGLAA1WTR-1b, 2023MgrundlegendBAGLAA1WTR-2c) → die Gesamtmatrix als Produkt: Einträge über Pfade bestätigen, Nulleinträge begründen, deuten (iqb 2020MgrundlegendBAGLAA1WTR-1c, 2023MgrundlegendBAGLAA1WTR-2a, 2026MerhoehtBAGLAA1WTR-2b, 2026MerhoehtBAGLAA1MMS-2b, 2020MgrundlegendBAGLAA1WTR-1a) → rückwärts: Produktionsmengen und fehlende Bedarfe über Gleichungssysteme (iqb 2021MgrundlegendAAGLAA111-b, 2021MerhoehtAAGLAA113-a, 2021MerhoehtAAGLAA113-b, 2020MgrundlegendBAGLAA1WTR-1d, 2024MgrundlegendAAGLAA111-b, 2024MerhoehtAAGLAA11-b, 2023MerhoehtBAGLAA1WTR-1b, Teil A und B) → Engpässe und Kosten: knappster Rohstoff, Kostenschranken, Preisanstieg (iqb 2026MerhoehtBAGLAA1WTR-2c, 2026MerhoehtBAGLAA1MMS-2c, 2023MgrundlegendBAGLAA1WTR-2b, 2026MerhoehtBAGLAA1WTR-2d, 2026MerhoehtBAGLAA1MMS-2d) → Prüfungshöhe: die Kostengleichung mit Zeilenvektor erläutern und lösen (iqb 2025MerhoehtBAGLAA1MMS-2b, Niveau III), die neue Endproduktspalte über die Produktgleichung (iqb 2023MerhoehtBAGLAA1WTR-1d, Niveau III), die Anteilsbedingung mit Lagerverbrauch (iqb 2025MerhoehtBAGLAA1MMS-2c, Niveau III), der Parameter-Bedarf als Gerade (iqb 2023MerhoehtBAGLAA1WTR-1e, Niveau III) und die Nichtinvertierbarkeit deuten (iqb 2023MerhoehtBAGLAA1WTR-1c, Niveau III).
116  - Übergangsmodell (Einheit 4): „Von wo nach wo?“ ankreuzen und „Ein Schritt, mehrere oder rückwärts?“ – zu Termen ankreuzen, wie viele Übergänge sie beschreiben und ob vorwärts oder rückwärts (Inverse) gerechnet wird, und wo ein Zugang eingeschoben ist; nichts rechnen (Vorstufe, Grundvorstellung) → das Übergangsdiagramm aus Tabelle oder Matrix zeichnen (Grundfall, viermal; iqb 2018MerhoehtAAGLAA111-a, 2018MgrundlegendBAGLAA1WTR-1a, 2019MgrundlegendBAGLAA1WTR-1b, 2021MgrundlegendBAGLAA1WTR-1a, 2022MerhoehtBAGLAA1WTR-2a, 2024MgrundlegendBAGLAA1WTR-1a, 2024MerhoehtBAGLAA1WTR-1a, 2026MgrundlegendBAGLAA1MMS-1a, 2026MgrundlegendBAGLAA1WTR-1a) → die Matrix aus dem Diagramm aufstellen, auswählen und ergänzen (iqb 2017MerhoehtAAGLAA112-a, 2019MgrundlegendAAGLAA11-a, 2022MgrundlegendAAGLAA11-a, 2022MgrundlegendBAGLAA1WTR-1a, 2020MgrundlegendBAGLAA... Auswahlformen, 2023MerhoehtAAGLAA112-b, Teil A) → Einträge, Zeilen und Spaltensummen deuten (iqb 2018MgrundlegendAAGLAA112-a, 2019MgrundlegendBAGLAA1WTR-1a, 2020MerhoehtAAGLAA11-a, 2022MerhoehtAAGLAA111-a, 2025MgrundlegendBAGLAA1WTR-1a, 2025MerhoehtBAGLAA1WTR-1a, 2018MgrundlegendBAGLAA1WTR-1e, 2023MerhoehtAAGLAA112-c) → Schritte rechnen: ein Schritt mit Anteil, zwei Schritte mit M², Zustände nacheinander (iqb 2022MgrundlegendBAGLAA1WTR-1b, 2018MgrundlegendBAGLAA1WTR-1d, 2019MgrundlegendAAGLAA11-b, 2018MerhoehtAAGLAA112-a, 2018MerhoehtBAGLAA1WTR-2b, 2018MgrundlegendAAGLAA112-b, 2022MgrundlegendAAGLAA11-b, 2022MgrundlegendBAGLAA1WTR-1e) → rückwärts und mit Zugängen: Inverse, Terme mit Abgang, Gleichungssysteme für Vorzustände (iqb 2021MgrundlegendBAGLAA1WTR-1d, 2018MgrundlegendBAGLAA1WTR-1c, 2018MerhoehtAAGLAA112-b, 2025MerhoehtBAGLAA1WTR-1c, 2022MgrundlegendBAGLAA1WTR-1f, 2024MgrundlegendBAGLAA1WTR-1d, 2026MgrundlegendBAGLAA1WTR-1c, 2019MgrundlegendBAGLAA1WTR-1d, 2023MerhoehtAAGLAA12-a, 2022MerhoehtBAGLAA1WTR-2b) → unbekannte Komponenten, Parameter und Spannen (iqb 2018MgrundlegendBAGLAA1WTR-1h, 2024MerhoehtBAGLAA1WTR-1b, 2022MerhoehtAAGLAA111-b, 2021MgrundlegendBAGLAA1WTR-1c, 2024MgrundlegendBAGLAA1WTR-1c, 2019MgrundlegendBAGLAA1WTR-1f, 2018MgrundlegendBAGLAA1WTR-1g, 2019MgrundlegendBAGLAA1WTR-1e) → Prüfungshöhe: die Unmöglichkeit einer Verteilung über die negative Vorgängerkomponente (iqb 2026MgrundlegendBAGLAA1MMS-1c, Niveau III), das Fehlerdiagramm gegen die Matrix (iqb 2026MerhoehtAAGLAA11-a, Teil A), das Entwicklungsdiagramm über die ersten Schritte auswählen (iqb 2017MerhoehtAAGLAA112-b, Teil A, Niveau III), die geänderte Matrix nach beschriebenem Verhalten (iqb 2021MgrundlegendBAGLAA1WTR-1e), die Wechslerzahl über die diagonalfreie Matrix (iqb 2022MgrundlegendBAGLAA1WTR-1c, Niveau III), die Spielregel (iqb 2023MerhoehtAAGLAA112-a), die Reihenfolge der Zustände (iqb 2022MerhoehtAAGLAA111-c) und die Beurteilungen mit Matrixzeilen und M² (iqb 2019MgrundlegendBAGLAA1WTR-1c, 2025MgrundlegendBAGLAA1WTR-1b, 2022MgrundlegendBAGLAA... Aussagen, 2019MgrundlegendAAGLAA... Übergangsgleichung).
117  - Stationär und langfristig (Einheit 5): „Ein Schritt, mehrere oder rückwärts?“ – zu Termen ankreuzen, wie viele Übergänge sie beschreiben und ob vorwärts oder rückwärts (Inverse) gerechnet wird, und wo ein Zugang eingeschoben ist; nichts rechnen (Vorstufe) → einen Fixvektor mit fester Gesamtzahl berechnen (Grundfall, viermal; iqb 2021MgrundlegendBAGLAA1WTR-1b, 2025MerhoehtBAGLAA1WTR-1b) → die stationäre Verteilung bei absorbierendem Zustand angeben und die Monotonie begründen (iqb 2018MerhoehtAAGLAA111-c, 2018MerhoehtAAGLAA111-b, 2019MerhoehtAAGLAA11-a, Teil A) → Matrix- und Bestandsparameter aus der Fixbedingung (iqb 2020MerhoehtAAGLAA11-b, 2025MgrundlegendBAGLAA1WTR-1c, 2026MgrundlegendBAGLAA1MMS-1e, 2018MerhoehtBAGLAA1WTR-2c) → Gleichgewicht und Eingriffe: Wechselzahlen, zu entfernender Anteil (iqb 2018MgrundlegendBAGLAA1WTR-1b, 2018MerhoehtBAGLAA1WTR-2d) → Zyklen: Potenz gleich Einheitsmatrix, Zykluslängen-Parameter, Fallbeschreibungen (iqb 2018MgrundlegendAAGLAA112-c, 2026MerhoehtAAGLAA11-b, 2019MgrundlegendAAGLAA12-b, 2023MerhoehtAAGLAA12-b, Teil A) → exponentielle Entwicklung: Faktor je Schritt, Zeitpunkte über die Ungleichung, Kurve zuordnen (iqb 2019MerhoehtAAGLAA11-b, 2019MerhoehtAAGLAA11-a, 2024MerhoehtBAGLAA1WTR-1d, 2021MgrundlegendBAGLAA1WTR-1f, 2026MgrundlegendBAGLAA1MMS-1d, 2026MgrundlegendBAGLAA1WTR-1d, 2026MgrundlegendBAGLAA1WTR-1e) → Prüfungshöhe: die Grenzmatrix deuten (iqb 2023MerhoehtAAGLAA112-c, Teil A) und das parametrisierte Übergangsverhalten nach Fällen beschreiben (iqb 2022MerhoehtBAGLAA1WTR-2d, Niveau III).
118
119  ### Prüfungsform (fhr / abi / iqb)
120  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – aber die Auswahl-Einschränkung der Geltungsdateien abi-*-geltung.md führt dieses Thema für alle vier Zielprüfungen (be-gk, be-lk, bb-gk, bb-ea) mit „nein“: Berlin und Brandenburg wählen im Sachgebiet Analytische Geometrie/Lineare Algebra die Alternative A2 (Analytische Geometrie), die Alternative A1 (Lineare Algebra) wird nicht entnommen; entsprechend gibt es keine einzige abi-Zeile. Die Prüfungsrelevanz ist geklärt (befund-geltung-2026-09-21.md § 1, Stand 21.09.2026): Die Prüfungsschwerpunkte 2027 führen unter Geometrie die Parametergleichung einer Geraden, neu ergänzt um den Zusammenhang zwischen Geraden und Punktmengen – Matrizen kommen nicht vor; seit 2025 entfällt zudem die Wahl zwischen Analytischer Geometrie und Stochastik im Prüfungsteil 2, so dass kein Platz für A1 bleibt; die Angleichung ab 2030 betrifft die Funktionalitäten der digitalen Hilfsmittel, nicht die Themen. Für den Unterrichtszweck (Oberstufenklausuren anderer Kurse, Wiederholung, Studienvorbereitung) gilt der Eintrag unabhängig davon. Für fhr ist der Pool keine Vorgabe; kein Bestand. Die Rohdatei zählt 191 Zeilen mit 123 Haupttypen (alle iqb), Jahre 2017–2026 – das größte Einzelthema des Sek-II-Katalogs und zugleich das mit der feinsten Typenstreuung (1,6 Zeilen je Typ). Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (das Thema führt die Gegenstandsklassen „Matrizenalgebra“, „Verflechtung“ und „Übergangsprozess“ als Präfix vor dem Doppelpunkt – der Anlassfall der Entscheidung 24). Pool-Sachgebiet: Alternative A1 „Lineare Algebra“ der Aufgabengruppe AG/LA [IQB-STR 1], Kennungen mit AGLAA1.
121  fhr: kein Bestand, keine Zeile – der RLP FOS 2019 kennt keine Matrizen.
122  abi: keine Zeile – kein Landesheft Berlins oder Brandenburgs prüft die Alternative A1; das Thema ist der einzige Sek-II-Volleintrag ohne abi-Bestand (Geltung viermal „nein“).
123  iqb (191 Zeilen, 123 Typen; Pool 2017–2026, grundlegend 91 und erhöht 100 Zeilen, Teil A 75 und Teil B 116 Zeilen, davon 12 MMS und 25 CAS, Alternative A1) [iqb-Katalog]: Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen (11, E4) · Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten (8, E4) · Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen (5, E2) · Matrizenalgebra: Matrix-Vektor-Produkt berechnen (4, E1) · Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix berechnen (4, E3) · Übergangsprozess: Verteilung nach einem Übergang berechnen (4, E4) · Matrizenalgebra: Inverse Matrix über A · B = E bestimmen (3, E1) · Matrizenalgebra: Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen (3, E2) · Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen (3, E4) · Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen (3, E5) · Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen (3, E4) · Übergangsprozess: Wachstumsfaktor je Schritt aus zwei Zuständen im Abstand mehrerer Schritte nachweisen (3, E5) · Übergangsprozess: Zeitpunkt für das Unter- oder Überschreiten einer Schranke über einen konstanten Faktor bestimmen (3, E5) · Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen (3, E4) · Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln (2, E1) · Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen (2, E2) · Matrizenalgebra: Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen (2, E2) · Verflechtung: Eintrag der Gesamtmatrix aus dem Diagramm bestätigen und Nulleintrag begründen (2, E3) · Verflechtung: Format der Bedarfsmatrix aus der Anzahl der Stufenprodukte begründen (2, E3) · Verflechtung: Gesamtmatrix im Sachzusammenhang deuten (2, E3) · Verflechtung: Maximale Kostensteigerung eines Rohstoffs aus einer Kostenschranke bestimmen (2, E3) · Verflechtung: Maximale Produktionsmenge aus dem Rohstoffvorrat ermitteln (2, E3) · Verflechtung: Produktionsmengen aus dem Rohstoffverbrauch über ein Gleichungssystem ermitteln (2, E3) · Verflechtung: Rohstoffmenge aus den übrigen Rohstoffen über die Gesamtmatrix bestimmen (2, E3) · Übergangsprozess: Anteil oder Anzahl zu entfernender Individuen für einen stationären Zustand berechnen (2, E5) · Übergangsprozess: Bereich eines Anteils in Abhängigkeit vom Matrixparameter über die Randwerte ermitteln (2, E4) · Übergangsprozess: Eignung eines Populationsmodells zur langfristigen Beschreibung beurteilen (2, E5) · Übergangsprozess: Einträge der Grenzmatrix im Sachzusammenhang deuten (2, E5) · Übergangsprozess: Gleichungssystem für die Verteilung vor einem Übergang aufstellen (2, E4) · Übergangsprozess: Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix beschreiben (2, E5) · Übergangsprozess: Matrixparameter aus einer Komponente nach einem Schritt bestimmen (2, E4) · Übergangsprozess: Spanne einer Komponente nach einem Schritt bei teilweise bekannter Verteilung ermitteln (2, E4) · Übergangsprozess: Stationäre Verteilung mit vorgegebener Gesamtzahl berechnen und einen Anteil beurteilen (2, E5) · Übergangsprozess: Term mit Matrixpotenz und Zugang im Sachzusammenhang auswählen und deuten (2, E4) · Übergangsprozess: Unmöglichkeit einer Verteilung über eine negative Vorgängerkomponente begründen (2, E4) · Übergangsprozess: Zustand mit dem kleinsten Wechselanteil aus der Matrix ablesen (2, E4) · je 1: Matrizenalgebra: Abbildungsmatrix als Spiegelung an einer Koordinatenachse deuten (E2) · Matrizenalgebra: Abbildungsmatrix aus einer geometrischen Bedingung an den Bildpunkt bestimmen (E2) · Matrizenalgebra: Alle Vektoren mit M · v = t · v durch Fallunterscheidung bestimmen (E2) · Matrizenalgebra: Aufbau von Vertauschungsmatrizen mit vorgegebener Wirkung beschreiben (E1) · Matrizenalgebra: Bedingung für eine selbstinverse Matrix mit Parametern herleiten (E2) · Matrizenalgebra: Beziehung zwischen den Komponenten eines Fixvektors über das Gleichungssystem N · u = u nachweisen (E2) · Matrizenalgebra: Definiertheit von Summe und Produkt zweier Matrizen über die Formate entscheiden (E1) · Matrizenalgebra: Einträge einer Faktormatrix aus dem Produkt mit einer bekannten Matrix bestimmen (E1) · Matrizenalgebra: Existenz mehrerer Lösungen von M · a = 0 begründen (E2) · Matrizenalgebra: Existenz von Matrizen mit vorgegebener Eigenschaft über ein Gleichungssystem beurteilen (E2) · Matrizenalgebra: Faktor aus M² als Vielfachem der Einheitsmatrix ermitteln (E1) · Matrizenalgebra: Fehlende Einträge einer Matrixpotenz über Zeile mal Spalte und Spaltensumme berechnen (E1) · Matrizenalgebra: Ganzzahlige Einträge einer Matrix aus ihrem Quadrat bestimmen (E1) · Matrizenalgebra: Hohe Potenz einer Vertauschungsmatrix über das Quadrat gleich Einheitsmatrix bestimmen (E1) · Matrizenalgebra: Inverse einer Vertauschungsmatrix angeben (E1) · Matrizenalgebra: Kollinearität von M · x − x mit einem Vektor untersuchen (E2) · Matrizenalgebra: Konstanten Faktor der Komponentensumme von Q · u über die Spaltensummen nachweisen (E2) · Matrizenalgebra: Matrix mit vorgegebener Eigenschaft angeben (E2) · Matrizenalgebra: Mögliche Formate einer Matrix aus der Bildbarkeit eines Produkts beschreiben (E1) · Matrizenalgebra: Nullvektor als einzige Lösung von M · u = 0 nachweisen (E2) · Matrizenalgebra: Orthogonalität einer Matrix über das Produkt mit der Transponierten nachweisen (E2) · Matrizenalgebra: Parameter aus der Gültigkeit der binomischen Formel für zwei Matrizen bestimmen (E1) · Matrizenalgebra: Parameter einer Matrix aus der Orthogonalität von v und M · v bestimmen (E2) · Matrizenalgebra: Parameter einer Matrix aus einer Matrix-Vektor-Gleichung untersuchen (E2) · Matrizenalgebra: Parameter für gleiche Spur von Matrix und Inverser bestimmen (E1) · Matrizenalgebra: Parameterbereich für endliche Grenzwerte der Matrixpotenzen über eine Potenzfolge bestimmen (E2) · Matrizenalgebra: Quadrat einer Matrix mit Parameter berechnen (E1) · Matrizenalgebra: Quadrat einer Summe zweier Matrizen mit C · D = −D · C vereinfachen (E1) · Matrizenalgebra: Unlösbarkeit einer Matrix-Vektor-Gleichung über eine Nullzeile begründen (E2) · Matrizenalgebra: Wirkung einer Permutationsmatrix beschreiben und Einträge aus M · A · M = A bestimmen (E1) · Verflechtung: Bedarf eines neuen Endprodukts an Zwischenprodukten aus der Produktgleichung der Matrizen ermitteln (E3) · Verflechtung: Fehlenden Eintrag des Diagramms aus der Bedarfsmatrix angeben und deuten (E3) · Verflechtung: Höchstmenge aus einer Kostenschranke bei festem Mengenverhältnis ermitteln (E3) · Verflechtung: Kostengleichung mit Zeilenvektor, Matrix und Auftragsvektor erläutern und lösen (E3) · Verflechtung: Matrix-Vektor-Gleichung mit konkreten Zahlen im Sachzusammenhang deuten (E3) · Verflechtung: Matrixeintrag aus Mengenbedingungen ermitteln (E3) · Verflechtung: Nichtinvertierbarkeit der Gesamtmatrix im Sachzusammenhang deuten (E3) · Verflechtung: Produktionsmenge aus einer Anteilsbedingung an den Rohstoffverbrauch bei festem Lagerverbrauch ermitteln (E3) · Verflechtung: Rohstoffbedarf in Abhängigkeit von einem Matrixparameter als Gerade darstellen und erläutern (E3) · Verflechtung: Unbekannte Bedarfe im Diagramm aus der Gesamtmatrix bestimmen (E3) · Verflechtung: Verflechtungsdiagramm zu einer Matrix zeichnen (E3) · Verflechtung: Verflechtungsmatrix aus Sachbedingungen und Matrixprodukt bestimmen (E3) · Verflechtung: Verflechtungsmatrix aus dem Diagramm angeben (E3) · Übergangsprozess: Anteil nach zwei Übergängen aus dem Diagramm berechnen (E4) · Übergangsprozess: Aussage über eine Komponente nach einem Übergang bei gleicher Ausgangsverteilung beurteilen (E4) · Übergangsprozess: Aussage über eine gleichbleibende Komponente aus einer Matrixzeile beurteilen (E4) · Übergangsprozess: Aussage über laufende gegenüber einmaliger Entnahme im Sachzusammenhang beurteilen (E4) · Übergangsprozess: Aussagen über Anteile nach zwei Übergängen mit M² beurteilen (E4) · Übergangsprozess: Diagramm der zeitlichen Entwicklung eines Zustands aus dem Übergangsdiagramm auswählen und begründen (E4) · Übergangsprozess: Eintrag von M² berechnen und Zeile von M² im Sachzusammenhang deuten (E4) · Übergangsprozess: Entwicklung einer Population aus einer Potenz der inversen Matrix beschreiben (E5) · Übergangsprozess: Exponentielles Wachstum aus einem Eigenvektor begründen und Kurve zuordnen (E5) · Übergangsprozess: Fehler in einem Übergangsdiagramm gegen die Matrix begründen (E4) · Übergangsprozess: Geänderte Übergangsmatrix aus zwei Vorschlägen nach dem beschriebenen Wechselverhalten auswählen und begründen (E4) · Übergangsprozess: Gleichung aus gleichen Komponentensummen von Ausgabe- und Rückgabevektor nachweisen und deuten (E4) · Übergangsprozess: Größtmögliche Anzahl im Vorquartal über die inverse Matrix und Nichtnegativität bestimmen (E4) · Übergangsprozess: Kleinsten Zeitpunkt für das Unterschreiten eines Anteils aus dem Matrixterm bestimmen (E5) · Übergangsprozess: Komponentensumme eines Produkts mit der diagonalfreien Matrix als Wechslerzahl deuten (E4) · Übergangsprozess: Konstante prozentuale Abnahme einer Gruppe ohne Zugänge aus der Matrix begründen (E5) · Übergangsprozess: Langfristige Verteilung aus dem Übergangsdiagramm beschreiben (E5) · Übergangsprozess: Matrix bei geänderter Reihenfolge der Zustände angeben (E4) · Übergangsprozess: Matrixeintrag aus einer Potenz der inversen Matrix bestimmen (E4) · Übergangsprozess: Matrixeintrag und Spaltensumme eins im Sachzusammenhang deuten (E4) · Übergangsprozess: Matrixparameter aus einer Komponente nach zwei Schritten bestimmen (E4) · Übergangsprozess: Matrixparameter aus einer Überlebensrate über zwei Stufen bestimmen (E4) · Übergangsprozess: Monotone Entwicklung der Anteile aus der Übergangstabelle begründen (E5) · Übergangsprozess: Mögliche Übergangsmatrix aus Ausgabe- und Rückgabezahlen zweier Stationen mit freiem Parameter ermitteln (E4) · Übergangsprozess: Nichtnegativen stationären Vektor für alle Parameterwerte nachweisen und ein ganzzahliges Beispiel deuten (E5) · Übergangsprozess: Parameter einer Übergangsmatrix aus einer Zykluslänge bestimmen (E5) · Übergangsprozess: Potenz der Übergangsmatrix als mehrschrittigen Übergang deuten (E4) · Übergangsprozess: Potenz der Übergangsmatrix gleich Einheitsmatrix als Zyklus deuten (E5) · Übergangsprozess: Quadrat der Übergangsmatrix aus dem Diagramm berechnen (E4) · Übergangsprozess: Quadrat der Übergangsmatrix berechnen und M² · v als Zustand nach zwei Schritten deuten (E4) · Übergangsprozess: Rückrechnung eines Verteilungsvektors über die Inverse von M² beschreiben (E4) · Übergangsprozess: Spielregel zu den Übergangswahrscheinlichkeiten eines Feldes angeben (E4) · Übergangsprozess: Stationäre Verteilung bei absorbierendem Zustand angeben (E5) · Übergangsprozess: Term für die Verteilung mit zwischenzeitlichem Abgang über Diagonalmatrix und Matrixpotenzen angeben (E4) · Übergangsprozess: Unbekannte Komponente der Ausgangsverteilung aus dem Ergebnisvektor über ein Gleichungssystem ermitteln (E4) · Übergangsprozess: Unmöglichkeit eines konstanten Zustands über eine negative Lösung begründen (E5) · Übergangsprozess: Verhältnis der Anfangsbestände aus einer Gleichverteilung nach einem Übergang bestimmen (E4) · Übergangsprozess: Wechselzahlen nach einem Übergang berechnen und Gleichgewicht deuten (E5) · Übergangsprozess: Zeile der Übergangsmatrix aus dem Diagramm angeben (E4) · Übergangsprozess: Übergangsdiagramm zur Matrix auswählen und fehlende Werte angeben (E4) · Übergangsprozess: Übergangsgleichung mit Matrix aus dem Diagramm aufstellen und Variablen deuten (E4) · Übergangsprozess: Übergangsmatrix aus dem Diagramm unter zwei Darstellungen auswählen und ergänzen (E4) · Übergangsprozess: Übergangsmatrix aus dem Übergangsdiagramm aufstellen (E4) · Übergangsprozess: Übergangsverhalten einer parametrisierten Matrix nach Fällen im Sachzusammenhang beschreiben (E5). Muster: In Teil A (75 Zeilen, ein bis fünf Punkte) prüft die Aufgabengruppe AG/LA 1 die Matrizenalgebra fast vollständig (die Kästen eins und zwei mit ihren Struktur- und Definitionsaufgaben – jedes Jahr eine Rechen- und eine Deutungsaufgabe, 2017 grundlegend die Formate von Summe und Produkt und die Inverse über B · C = E: 2017MgrundlegendAAGLAA11-a, 2017MgrundlegendAAGLAA11-b) und die kleinen Übergangsmodelle (Diagramm, Matrix, wenige Schritte, Zyklen); in Teil B (116 Zeilen, ein bis sieben Punkte, davon 12 MMS- und 25 CAS-Zeilen) trägt je Jahrgang eine große Sachaufgabe entweder das Übergangsmodell (Wolfspopulation 2017 mit Diagramm, Eintragsdeutung, Überlebensrate, Rückrechnung, Wachstumsfaktor, Schranke und Modellkritik: 2017MerhoehtBAGLAA1WTR-1a, 2017MerhoehtBAGLAA1WTR-1b, 2017MerhoehtBAGLAA1WTR-1c, 2017MerhoehtBAGLAA1WTR-1d, 2017MerhoehtBAGLAA1WTR-1e, 2017MerhoehtBAGLAA1WTR-1f, 2017MerhoehtBAGLAA1WTR-1g, 2017MerhoehtBAGLAA1WTR-1h; Baumärkte 2018, Tretbootverleih 2019, Taxi 2021, Transport und Lampen 2022, E-Scooter und Tierpopulationen 2024–2026) oder die Verflechtung (Molkerei 2020/2023, Zwischenprodukt-Produktionen 2023–2026) – mit sechs bis neun zusammenhängenden Teilaufgaben vom Diagramm über Schritte und Rückrechnung bis zu Fixvektor, Engpass oder langfristigem Verhalten; das Springkraut 2018 verbindet beide Welten (Stufenmatrizen als Produkt); die zweite erhöhte Teil-B-Aufgabe 2017 stellt die Fixvektor-Struktur ohne Sachzusammenhang (2017MerhoehtBAGLAA1WTR-2a, 2017MerhoehtBAGLAA1WTR-2b, Anforderungsbereich III). Die CAS-Stapel (Teil B CAS, 25 Zeilen) bringen dieselben Muster mit dem Rechner als Werkzeug für Inverse, Potenzen und Gleichungssysteme: erhöht 2018 die Baumärkte mit dem Gleichungssystem für den Vormonat, der Rückrechnung über die Inverse, der Unmöglichkeit über die negative Vorgängerkomponente nach fünf Rückschritten, der Grenzmatrix, dem kleinsten Wechselanteil und der Rabattmatrix mit Parameter (Parameterprobe, Bereich eines Anteils über die Randwerte und – neu – der nichtnegative stationäre Vektor für alle Parameterwerte mit ganzzahligem Beispiel, Anforderungsbereich III): 2018MerhoehtBAGLAA1CAS1-1a, 2018MerhoehtBAGLAA1CAS1-1b, 2018MerhoehtBAGLAA1CAS1-1c, 2018MerhoehtBAGLAA1CAS1-1d, 2018MerhoehtBAGLAA1CAS1-1e, 2018MerhoehtBAGLAA1CAS1-1f, 2018MerhoehtBAGLAA1CAS1-1g, 2018MerhoehtBAGLAA1CAS1-1h; dazu die Taufliegen mit Eintragsdeutung, Zuständen über Matrixpotenzen, wöchentlichem Wachstumsfaktor, Entnahme nach jedem Schritt (neu: die Beurteilung laufender gegenüber einmaliger Entnahme – die eigene Rechnung bestätigt das Urteil, nicht die amtliche Begründung für die Vollinsekten), der Entnahmezahl für einen stationären Zustand, dem Eigenschaftsvektor mit Faktor und dem Dreiwochenzyklus N³ als Vielfachem der Einheitsmatrix: 2018MerhoehtBAGLAA1CAS2-1a, 2018MerhoehtBAGLAA1CAS2-1b, 2018MerhoehtBAGLAA1CAS2-1c, 2018MerhoehtBAGLAA1CAS2-2a, 2018MerhoehtBAGLAA1CAS2-2b, 2018MerhoehtBAGLAA1CAS2-2c, 2018MerhoehtBAGLAA1CAS2-3a, 2018MerhoehtBAGLAA1CAS2-3b; grundlegend 2017 die Wolfspopulation der erhöhten WTR-Aufgabe (2017MgrundlegendBAGLAA1CAS-1a, 2017MgrundlegendBAGLAA1CAS-1c, 2017MgrundlegendBAGLAA1CAS-1e und 2017MgrundlegendBAGLAA1CAS-1f wortgleich mit den Teilaufgaben a, d, e und f dort, 2017MgrundlegendBAGLAA1CAS-1g abgewandelt aus h, dazu 2017MgrundlegendBAGLAA1CAS-1b und 2017MgrundlegendBAGLAA1CAS-1d – poolinterne Wiederkehr in einer anderen Trägeraufgabe, keine Landesdublette) und die Fixvektor-Struktur mit der Matrix der zweiten erhöhten Aufgabe (neu: der Nullvektor als einzige Lösung von N · u = 0, dann alle Fixvektoren mit Betragsbedingung: 2017MgrundlegendBAGLAA1CAS-2a, 2017MgrundlegendBAGLAA1CAS-2b). Amtlicher Anforderungsbereich in allen 191 Zeilen (höchster Bereich: I 56, II 91, III 44); Niveau I 58, II 95, III 38. Kontexte: Baumärkte, Tretbootverleih, Taxi- und Transportunternehmen, E-Scooter, Stromanbieter, Pay-TV, Lampen-Farbwechsel, Brettspiel, Tier- und Insektenpopulationen (Wölfe, Taufliegen, Springkraut, Käfer, Vögel, Ratten, Apfelbäume), mehrstufige Produktionen. Keine Zeile kehrt in einem Landesheft wieder (keine Dubletten – die Länder entnehmen die Alternative A1 nicht).
124  Zielmarke: Einheit 1 – die vertauschbaren Matrizen mit binomischer Gleichung (2025MerhoehtAAGLAA122, Teil A, Niveau III) und die ganzzahligen Einträge aus dem Quadrat (2020MgrundlegendAAGLAA12, Teil A, Niveau III). Einheit 2 – die Gleichung mit der Inversen über die Eigenvektorbeziehung (2026MerhoehtAAGLAA121-b, Teil A, Niveau III), die orthogonalen Matrizen mit Wurzelvorgabe (2026MerhoehtAAGLAA122-b, Teil A, Niveau III) und das Grenzverhalten der Potenzfolge (2022MerhoehtBAGLAA1WTR-2c, Niveau III). Einheit 3 – die Kostengleichung mit Zeilenvektor (2025MerhoehtBAGLAA1MMS-2b, Niveau III) und die neue Endproduktspalte über die Produktgleichung (2023MerhoehtBAGLAA1WTR-1d, Niveau III). Einheit 4 – der Term mit zwischenzeitlichem Abgang über die Diagonalmatrix (2022MgrundlegendBAGLAA1WTR-1f, Niveau III), die Auswahl des Freitagsterms (2024MgrundlegendBAGLAA1WTR-1d, Niveau III) und die Unmöglichkeit über die negative Vorgängerkomponente (2026MgrundlegendBAGLAA1MMS-1c, Niveau III). Einheit 5 – das parametrisierte Übergangsverhalten nach Fällen mit Grenzmatrix (2022MerhoehtBAGLAA1WTR-2d, Niveau III), die Entwicklung aus der Potenz der Inversen (2023MerhoehtAAGLAA12-b, Teil A, Niveau III) und der Zyklus aus M³ (2026MerhoehtAAGLAA11-b, Teil A, Niveau II).
````

## 2 Originale (189)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2017MgrundlegendAAGLAA11-a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Matrizen A = ((2; 2), (3; 0), (0; 1)) mit drei Zeilen und zwei Spalten und B = ((3; 0), (1; 2)) (zeilenweise)
- gesucht: Entscheidung mit Begründung, ob A + B und A · B definiert sind
- verfahren: Formate vergleichen: für die Summe gleiche Formate, für das Produkt Spaltenzahl von A gleich Zeilenzahl von B
- fehlerquelle: das Produkt wegen verschiedener Formate für nicht definiert halten

### 2017MgrundlegendAAGLAA11-b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: B = ((3; 0), (1; 2)) (zeilenweise); C = ((a; b), (c; d))
- gesucht: Werte von a, b, c und d mit B · C = ((1; 0), (0; 1))
- verfahren: B · C ausmultiplizieren und eintragsweise mit der Einheitsmatrix gleichsetzen; die vier linearen Gleichungen lösen
- fehlerquelle: C · B statt B · C ausmultiplizieren oder Zeile mal Spalte vertauschen

### 2017MerhoehtBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (x; 0; 0), (0; 0,7; 0,8)) (Zeilen)
- gesucht: Darstellung der Entwicklung der Population in einem Übergangsdiagramm
- verfahren: Für jeden von null verschiedenen Eintrag einen Pfeil vom Spalten- zum Zeilenzustand mit dem Eintrag beschriften
- fehlerquelle: Zeilen und Spalten vertauschen (Pfeil R → J mit 0,7)

### 2017MerhoehtBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 1 · format Kurzantwort · antwort Text
- gegeben: Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (x; 0; 0), (0; 0,7; 0,8)) (Zeilen)
- gesucht: Bedeutung von x im Sachzusammenhang
- verfahren: Der Eintrag in Zeile J, Spalte W gibt den Übergang von Welpen zu Jungtieren an
- fehlerquelle: x als Geburtenrate deuten

### 2017MerhoehtBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (x; 0; 0), (0; 0,7; 0,8)) (Zeilen); 72 % der Tiere sterben innerhalb der ersten zwei Lebensjahre
- gesucht: Wert von x
- verfahren: 28 % überleben die ersten zwei Lebensjahre und werden Rudelführerinnen: x · 0,7 = 0,28
- fehlerquelle: 0,72 statt 0,28 ansetzen oder 0,7 und x addieren

### 2017MerhoehtBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (x; 0; 0), (0; 0,7; 0,8)) (Zeilen); x = 0,4; zu Beobachtungsbeginn gehören 39 Rudelführerinnen zur Population, ein Jahr später 55
- gesucht: Anzahl der Jungtiere zu Beobachtungsbeginn
- verfahren: Dritte Zeile von v_1 = L · v_0: 0,7 · J + 0,8 · 39 = 55
- fehlerquelle: die überlebenden Rudelführerinnen nicht berücksichtigen (J = 55/0,7)

### 2017MerhoehtBAGLAA1WTR-1e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; die Entwicklung im Zwei-Jahres-Rhythmus beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen); sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165), die Population besteht aus 938 Tieren
- gesucht: Anzahl der Welpen, Jungtiere und Rudelführerinnen acht Jahre nach Beobachtungsbeginn
- verfahren: v_8 = M · v_6 zeilenweise berechnen
- fehlerquelle: M zweimal anwenden, weil acht Jahre zwei Schritte nach sechs Jahren sind

### 2017MerhoehtBAGLAA1WTR-1f (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Rechnung · antwort Text
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; die Entwicklung im Zwei-Jahres-Rhythmus beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen); sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165), die Population besteht aus 938 Tieren; v_10 ≈ (2168; 629; 598) und v_12 ≈ (4126; 1195; 1138); aus diesen Vektoren soll ein Faktor ermittelt werden, mit dem die Anzahl jeder Altersgruppe von einem Jahr zum nächsten zunimmt
- gesucht: rechnerischer Nachweis, dass dieser Faktor für jede der drei Altersgruppen etwa 1,38 beträgt
- verfahren: 1,38^2 · v_10 berechnen und mit v_12 vergleichen (oder die Quotienten der Komponenten und ihre Wurzeln)
- fehlerquelle: den Quotienten 4126/2168 ≈ 1,90 als Faktor je Jahr angeben

### 2017MerhoehtBAGLAA1WTR-1g (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Rechnung|Kurzantwort · antwort Zahl|Text
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; die Entwicklung im Zwei-Jahres-Rhythmus beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen); sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165), die Population besteht aus 938 Tieren; die Anzahl jeder Altersgruppe nimmt je Jahr etwa mit dem Faktor 1,38 zu; Gleichung 938 · 1,38^(t − 6) = 45000 mit t ∈ [6; +∞[
- gesucht: Lösung der Gleichung; Interpretation der Zahl 45000 im Sachzusammenhang unter Verwendung der Lösung
- verfahren: 1,38^(t − 6) = 45000/938, t − 6 = ln(45000/938)/ln(1,38); 45000 ist die Gesamtzahl der Tiere zum Zeitpunkt t
- fehlerquelle: 45000 als Zahl der Welpen deuten oder t − 6 als Antwort geben

### 2017MerhoehtBAGLAA1WTR-1h (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; die Entwicklung im Zwei-Jahres-Rhythmus beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen); sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165), die Population besteht aus 938 Tieren; das Modell liefert ein Wachstum aller Altersgruppen mit dem Faktor 1,38 je Jahr
- gesucht: Beurteilung des verwendeten Modells hinsichtlich seiner Eignung zur langfristigen Beschreibung der Entwicklung der Population
- verfahren: Unbegrenztes exponentielles Wachstum ist in einem abgeschlossenen Gebiet unrealistisch; die Umweltbedingungen und damit die Übergänge ändern sich
- fehlerquelle: das Modell wegen der Rundungen statt wegen des unbegrenzten Wachstums kritisieren

### 2017MerhoehtBAGLAA1WTR-2a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 4 · format Begründung|Rechnung · antwort Zahl|Text
- gegeben: Betrachtet werden 3x3-Matrizen N und Vektoren u = (u1; u2; u3) mit u ≠ (0; 0; 0), für die N · u = u gilt; N^(−1) ist die inverse Matrix zu einer der Matrizen N; Gleichungen (N · N^(−1)) · u = a · u und (N + N^(−1)) · u = a · u
- gesucht: Prüfung für jede der beiden Gleichungen, ob es einen Wert von a ∈ IR gibt, für den sie erfüllt ist
- verfahren: N · N^(−1) = E liefert u = a · u, also a = 1; aus N · u = u folgt durch Multiplikation mit N^(−1) N^(−1) · u = u, also (N + N^(−1)) · u = 2u und a = 2
- fehlerquelle: N^(−1) konkret berechnen wollen oder a = 0 wegen u = a · u zulassen

### 2017MerhoehtBAGLAA1WTR-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Betrachtet werden 3x3-Matrizen N und Vektoren u = (u1; u2; u3) mit u ≠ (0; 0; 0), für die N · u = u gilt; N = ((0; 0; 4), (0,25; 0; 0), (0; 0,4; 0,6)) (Zeilen)
- gesucht: Nachweis, dass für diese Matrix u2 = u3 gilt
- verfahren: Die dritte Zeile von N · u = u lautet 0,4u2 + 0,6u3 = u3, also 0,4u2 = 0,4u3
- fehlerquelle: die erste Zeile allein betrachten und u1 = 4u3 als Ergebnis angeben

### 2018MerhoehtBAGLAA1CAS1-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Drei Baumärkte A, B, C in einer Stadt; das Übergangsdiagramm beschreibt das Wechselverhalten der Kunden von einem Monat zum nächsten zunächst so: A bleibt 0,3, A → B 0,5, A → C 0,2; B bleibt 0,5, B → A 0,4, B → C 0,1; C bleibt 0,5, C → A 0,2, C → B 0,3; in einem Monat hat A 3500, B 4840 und C 1660 Kunden
- gesucht: die Anzahlen der Kunden der drei Baumärkte im vorhergehenden Monat
- verfahren: Aus dem Diagramm die Matrix mit den Spalten (0,3; 0,5; 0,2), (0,4; 0,5; 0,1), (0,2; 0,3; 0,5) bilden; das Gleichungssystem für den Vormonat aufstellen und lösen
- fehlerquelle: die Matrix zeilen- statt spaltenweise aus dem Diagramm ablesen (Übergänge vertauscht)

### 2018MerhoehtBAGLAA1CAS1-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); in einem auf die Maßnahmen folgenden Sommermonat hat A 3539, B 5281 und C 1180 Kunden
- gesucht: Nachweis, dass die Maßnahmen der Baumärkte A und B höchstens vier Monate zurückliegen
- verfahren: Vom Sommermonat aus mit M^−1 zurückrechnen: vier Rückschritte liefern noch nichtnegative Anzahlen, der fünfte eine negative Komponente; das Modell mit M kann also nicht schon fünf Monate gegolten haben
- fehlerquelle: mit M statt mit M^−1 rechnen, also vorwärts statt zurück

### 2018MerhoehtBAGLAA1CAS1-1c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); in einem auf die Maßnahmen folgenden Sommermonat hat A 3539, B 5281 und C 1180 Kunden
- gesucht: die prozentualen Anteile der Kunden der drei Baumärkte an der Gesamtzahl im Monat vor dem Sommermonat
- verfahren: M^−1 · (3539; 5281; 1180) berechnen und jede Komponente durch die Gesamtzahl 10000 teilen
- fehlerquelle: die Anteile des Sommermonats statt des Vormonats angeben

### 2018MerhoehtBAGLAA1CAS1-1d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); das Wechselverhalten der Kunden bleibt konstant
- gesucht: wie sich die prozentualen Anteile der Kunden der drei Baumärkte nach den Maßnahmen langfristig entwickeln würden
- verfahren: M^n für großes n mit dem Rechner berechnen (oder den Fixvektor mit Summe 1 bestimmen); die gleichen Spalten geben die langfristigen Anteile
- fehlerquelle: eine Zeile statt einer Spalte der Grenzmatrix als Verteilung lesen

### 2018MerhoehtBAGLAA1CAS1-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 2 · format Kurzantwort · antwort Text|Zahl
- gegeben: Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25))
- gesucht: der Baumarkt, bei dem der Anteil der Kunden, die nach Beginn der Maßnahmen von einem Monat zum nächsten zu einem anderen Baumarkt wechseln, am kleinsten ist, und dieser Anteil
- verfahren: Den größten Diagonaleintrag von M suchen (0,72 bei B); der Wechselanteil ist 1 − 0,72
- fehlerquelle: den Bleibeanteil 72 % statt des Wechselanteils nennen

### 2018MerhoehtBAGLAA1CAS1-1f (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); Baumarkt C fürchtet, den notwendigen Anteil von 25 % der Kunden nicht zu erreichen, und führt Rabattaktionen durch; ab dem Monat, in dem sie beginnen, gilt N = ((0,63; 0,18; 0,4 · (1 − p)), (0,27; 0,72; 0,6 · (1 − p)), (0,1; 0,1; p)) mit 0 <= p <= 1; in einem Monat nach Beginn der Aktionen hat A 3400, B 5200 und C 1400 Kunden, im folgenden Monat hat A 3022 Kunden
- gesucht: ob diese Kundenzahl mit dem Modell mit der Matrix N in Einklang steht
- verfahren: Die erste Komponente von N · (3400; 5200; 1400) gleich 3022 setzen, nach p auflösen und mit dem Bereich 0 <= p <= 1 vergleichen
- fehlerquelle: p = 1,1 als Lösung annehmen, ohne den Bereich des Parameters zu prüfen

### 2018MerhoehtBAGLAA1CAS1-1g (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); Baumarkt C fürchtet, den notwendigen Anteil von 25 % der Kunden nicht zu erreichen, und führt Rabattaktionen durch; ab dem Monat, in dem sie beginnen, gilt N = ((0,63; 0,18; 0,4 · (1 − p)), (0,27; 0,72; 0,6 · (1 − p)), (0,1; 0,1; p)) mit 0 <= p <= 1; im Monat vor Beginn der Aktionen hat A 3530, B 5294 und C 1176 Kunden (zusammen 10000)
- gesucht: in welchem Bereich der prozentuale Anteil der Kunden von C im folgenden Monat liegen kann
- verfahren: Dritte Komponente von N · (3530; 5294; 1176) als Term in p berechnen, durch 10000 teilen und die Randwerte p = 0 und p = 1 einsetzen
- fehlerquelle: nur einen Wert von p einsetzen oder den Anteil an der Summe der ersten beiden Komponenten bilden

### 2018MerhoehtBAGLAA1CAS1-1h (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 5 · format Begründung|Rechnung · antwort Text|Zahl
- gegeben: Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); Baumarkt C fürchtet, den notwendigen Anteil von 25 % der Kunden nicht zu erreichen, und führt Rabattaktionen durch; ab dem Monat, in dem sie beginnen, gilt N = ((0,63; 0,18; 0,4 · (1 − p)), (0,27; 0,72; 0,6 · (1 − p)), (0,1; 0,1; p)) mit 0 <= p <= 1
- gesucht: Nachweis, dass es für jedes p mit 0 <= p <= 1 einen Vektor v_p mit nichtnegativen Komponenten und der Spaltensumme 10000 gibt, für den N · v_p = v_p gilt; für ein geeignet gewähltes p ein solcher Vektor mit ganzzahligen Komponenten und seine Bedeutung im Sachzusammenhang
- verfahren: N · (x; y; 10000 − x − y) = (x; y; 10000 − x − y) nach x und y lösen; für 0 <= p <= 1 ist p − 1 <= 0 und 10p − 11 < 0, also x, y >= 0, und 10000/(11 − 10p) > 0; p = 0,1 liefert ganze Zahlen
- fehlerquelle: nur für einzelne p rechnen statt allgemein oder die Nichtnegativität für den ganzen Bereich nicht begründen

### 2018MerhoehtBAGLAA1CAS2-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; Entwicklung von einer Woche n zur nächsten nach v_(n+1) = L · v_n mit L = ((0; 0; 200), (0,03; 0; 0), (0; 0,11; 0,7)); zu Beginn der Beobachtung besteht die Population nur aus 230 Vollinsekten
- gesucht: Bedeutung der Matrixeinträge 200 und 0,11 im Sachzusammenhang
- verfahren: 200 steht in der Zeile E und der Spalte V, 0,11 in der Zeile V und der Spalte P
- fehlerquelle: Zeile und Spalte vertauschen und 0,11 als Anteil der Vollinsekten deuten, die zu Puppen werden

### 2018MerhoehtBAGLAA1CAS2-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 2 · format Begründung · antwort Text
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; Entwicklung von einer Woche n zur nächsten nach v_(n+1) = L · v_n mit L = ((0; 0; 200), (0,03; 0; 0), (0; 0,11; 0,7)); zu Beginn der Beobachtung besteht die Population nur aus 230 Vollinsekten
- gesucht: Nachweis, dass sechs Wochen nach Beobachtungsbeginn etwa 336 und zehn Wochen danach etwa 652 Vollinsekten zur Population gehören
- verfahren: v_0 = (0; 0; 230) aufstellen und L^6 · v_0 sowie L^10 · v_0 mit dem Rechner berechnen
- fehlerquelle: den Anfangsvektor als (230; 0; 0) ansetzen

### 2018MerhoehtBAGLAA1CAS2-1c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 5 · format Begründung|Rechnung · antwort Text|Zahl
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; Entwicklung von einer Woche n zur nächsten nach v_(n+1) = L · v_n mit L = ((0; 0; 200), (0,03; 0; 0), (0; 0,11; 0,7)); zu Beginn der Beobachtung besteht die Population nur aus 230 Vollinsekten; nach 6 Wochen etwa 336, nach 10 Wochen etwa 652 Vollinsekten; Vermutung: ab sechs Wochen nach Beobachtungsbeginn nimmt die Anzahl der Vollinsekten innerhalb von jeweils vier Wochen um etwa 92 % zu
- gesucht: Nachweis, dass die Vermutung zwischen 6 und 10 sowie zwischen 10 und 14 Wochen näherungsweise zutrifft; passend zur Vermutung die durchschnittliche wöchentliche Zunahme der Anzahl der Vollinsekten in Prozent
- verfahren: L^14 · v_0 berechnen; die Quotienten V_10/V_6 und V_14/V_10 mit 1,92 vergleichen; wöchentlicher Faktor als vierte Wurzel aus 1,92
- fehlerquelle: 92 % durch 4 teilen (23 % je Woche) statt die vierte Wurzel aus 1,92 zu ziehen

### 2018MerhoehtBAGLAA1CAS2-2a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; Entwicklung von einer Woche n zur nächsten nach v_(n+1) = L · v_n mit L = ((0; 0; 200), (0,03; 0; 0), (0; 0,11; 0,7)); einer zweiten Population werden am Ende jeder Woche a Vollinsekten entnommen, ihre Entwicklung folgt v_(n+1) = L · v_n − (0; 0; a); zu Beginn besteht die Population nur aus 4000 Puppen; am Ende jeder Woche werden 10 Vollinsekten entnommen
- gesucht: Zusammensetzung der Population zwei Wochen nach Beobachtungsbeginn
- verfahren: Zweimal v_(n+1) = L · v_n − (0; 0; 10) anwenden
- fehlerquelle: die Entnahme vor statt nach der Multiplikation abziehen

### 2018MerhoehtBAGLAA1CAS2-2b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; Entwicklung von einer Woche n zur nächsten nach v_(n+1) = L · v_n mit L = ((0; 0; 200), (0,03; 0; 0), (0; 0,11; 0,7)); einer zweiten Population werden am Ende jeder Woche a Vollinsekten entnommen, ihre Entwicklung folgt v_(n+1) = L · v_n − (0; 0; a); Aussage: Entnimmt man der Population während eines Zeitraums von fünf Wochen am Ende jeder Woche 10 Vollinsekten, führt dies zur gleichen Zusammensetzung, wie wenn erst nach Ablauf des gesamten Zeitraums 50 Vollinsekten entnommen werden
- gesucht: Beurteilung der Aussage
- verfahren: Bei einmaliger Entnahme am Ende entwickelt sich die Population fünf Wochen ungestört nach L; bei wöchentlicher Entnahme fehlen die entnommenen Tiere in den folgenden Wochen bei der Eiablage und beim Überleben – die Zusammensetzungen unterscheiden sich
- fehlerquelle: wegen 5 · 10 = 50 die Aussage für richtig halten, ohne die Wirkung auf die Vermehrung zu bedenken

### 2018MerhoehtBAGLAA1CAS2-2c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; Entwicklung von einer Woche n zur nächsten nach v_(n+1) = L · v_n mit L = ((0; 0; 200), (0,03; 0; 0), (0; 0,11; 0,7)); einer zweiten Population werden am Ende jeder Woche a Vollinsekten entnommen, ihre Entwicklung folgt v_(n+1) = L · v_n − (0; 0; a); zur Population sollen dauerhaft 20000 Eier und 600 Puppen gehören
- gesucht: Anzahl der Vollinsekten in der Population und Anzahl der Vollinsekten, die am Ende jeder Woche entnommen werden müssen
- verfahren: Stationären Zustand ansetzen: L · (20000; 600; V) − (0; 0; a) = (20000; 600; V); erste Zeile 200V = 20000, dritte Zeile 66 + 0,7V − a = V
- fehlerquelle: die Entnahme a in der Gleichung vergessen oder mit positivem Vorzeichen ansetzen

### 2018MerhoehtBAGLAA1CAS2-3a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; eine dritte Population entwickelt sich nach v_(n+1) = M · v_n mit M = ((0; 0; 100), (0,09; 0; 0), (0; 0,15; 0,9)); es gibt Zusammensetzungen mit drei Eigenschaften: die Anzahlen der Eier und der Vollinsekten stehen im Verhältnis b : 1; die Anzahl der Puppen ist viermal so groß wie die Anzahl der Vollinsekten; die Anzahlen der Eier, Puppen und Vollinsekten wachsen von einer Woche zur nächsten jeweils mit einem konstanten Faktor c
- gesucht: die Werte von b und c
- verfahren: Ansatz v = (b · x; 4x; x), M · v = c · v: dritte Zeile 0,15 · 4x + 0,9x = c · x liefert c = 1,5; erste Zeile 100x = c · b · x liefert b = 200/3; zweite Zeile 0,09 · b · x = 6x als Probe
- fehlerquelle: das Verhältnis b : 1 als (x; 4x; b · x) umgekehrt ansetzen

### 2018MerhoehtBAGLAA1CAS2-3b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Begründung · antwort Text
- gegeben: Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten; eine dritte Population entwickelt sich nach v_(n+1) = M · v_n mit M = ((0; 0; 100), (0,09; 0; 0), (0; 0,15; 0,9)); ein Insektizid bewirkt, dass von einer Woche zur nächsten stets alle Vollinsekten sterben; die Überlebenschancen der Eier und Puppen und die Fruchtbarkeit der Vollinsekten bleiben unverändert; Aussage: im Rhythmus von drei Wochen betrachtet steigen die Anzahl der Eier, die Anzahl der Puppen und die Anzahl der Vollinsekten jeweils exponentiell an
- gesucht: Beurteilung der Aussage
- verfahren: In M den Eintrag 0,9 durch 0 ersetzen; N^3 = 1,35 · E berechnen, also v_(n+3) = 1,35 · v_n und nach 3x Wochen der Faktor 1,35^x
- fehlerquelle: die Matrix M unverändert verwenden oder den Überlebensanteil der Vollinsekten auf 0 setzen, aber auch die Fruchtbarkeit streichen

### 2017MgrundlegendBAGLAA1CAS-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (0,4; 0; 0), (0; 0,7; 0,8)) (Zeilen)
- gesucht: Darstellung der Entwicklung der Population in einem Übergangsdiagramm
- verfahren: Für jeden von null verschiedenen Eintrag einen Pfeil vom Spalten- zum Zeilenzustand mit dem Eintrag beschriften
- fehlerquelle: Zeilen und Spalten vertauschen (Pfeil R → J mit 0,7)

### 2017MgrundlegendBAGLAA1CAS-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (0,4; 0; 0), (0; 0,7; 0,8)) (Zeilen); zu Beobachtungsbeginn gehören 39 Rudelführerinnen zur Population, ein Jahr später 55
- gesucht: Anzahl der Jungtiere zu Beobachtungsbeginn
- verfahren: Dritte Zeile von v_1 = L · v_0: 0,7 · J + 0,8 · 39 = 55
- fehlerquelle: die überlebenden Rudelführerinnen nicht berücksichtigen (J = 55/0,7)

### 2017MgrundlegendBAGLAA1CAS-1e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 1 · format Rechnung · antwort Zahl
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; von da an beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen) die Entwicklung im Zwei-Jahres-Rhythmus; sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165)
- gesucht: Anzahl der Welpen, Jungtiere und Rudelführerinnen acht Jahre nach Beobachtungsbeginn
- verfahren: v_8 = M · v_6 zeilenweise oder mit dem Rechner
- fehlerquelle: M zweimal anwenden, weil acht Jahre zwei Jahre nach sechs Jahren sind

### 2017MgrundlegendBAGLAA1CAS-1f (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 2 · format Rechnung · antwort Text
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; von da an beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen) die Entwicklung im Zwei-Jahres-Rhythmus; sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165); v_10 ≈ (2168; 629; 598) und v_12 ≈ (4126; 1195; 1138); aus diesen Vektoren soll ein Faktor ermittelt werden, mit dem die Anzahl jeder Altersgruppe von einem Jahr zum nächsten zunimmt
- gesucht: rechnerischer Nachweis, dass dieser Faktor für jede der drei Altersgruppen etwa 1,38 beträgt
- verfahren: 1,38^2 · v_10 berechnen und mit v_12 vergleichen (oder die Quotienten der Komponenten und ihre Wurzeln)
- fehlerquelle: den Quotienten 4126/2168 ≈ 1,90 als Faktor je Jahr angeben

### 2017MgrundlegendBAGLAA1CAS-1g (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 2 · format Begründung · antwort Text
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; von da an beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen) die Entwicklung im Zwei-Jahres-Rhythmus; sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165); das Modell liefert ein Wachstum aller Altersgruppen mit einem Faktor von etwa 1,38 je Jahr
- gesucht: Beurteilung der Beschreibung der Entwicklung durch die Matrix M hinsichtlich ihrer Eignung zur langfristigen Beschreibung
- verfahren: Unbegrenztes exponentielles Wachstum ist in einem abgeschlossenen Gebiet unrealistisch; die Umweltbedingungen und damit die Übergänge ändern sich
- fehlerquelle: das Modell wegen der Rundungen statt wegen des unbegrenzten Wachstums kritisieren

### 2017MgrundlegendBAGLAA1CAS-1b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 2 · format Kurzantwort · antwort Zahl|Text
- gegeben: Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (0,4; 0; 0), (0; 0,7; 0,8)) (Zeilen)
- gesucht: Eintrag der Matrix L, der die Überlebensrate der Welpen angibt; Änderung dieses Eintrags bei einer Erhöhung der Sterblichkeitsrate der Welpen
- verfahren: Der Übergang W → J steht in Zeile 2, Spalte 1; eine höhere Sterblichkeit heißt eine kleinere Überlebensrate
- fehlerquelle: den Eintrag 3 (Geburten) oder 0,8 (Rudelführerinnen) nennen

### 2017MgrundlegendBAGLAA1CAS-1d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach Beobachtungsbeginn ändern sich die Umweltbedingungen; von da an beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen) die Entwicklung im Zwei-Jahres-Rhythmus; sechs Jahre nach Beobachtungsbeginn ist v_6 = (600; 173; 165)
- gesucht: Anzahl der Welpen, Jungtiere und Rudelführerinnen vier Jahre nach Beobachtungsbeginn
- verfahren: Aus v_6 = M · v_4 folgt v_4 = M^(−1) · v_6; mit dem Rechner auswerten
- fehlerquelle: M · v_6 statt M^(−1) · v_6 rechnen oder die Einjahresmatrix L verwenden

### 2017MgrundlegendBAGLAA1CAS-2a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 2 · format Begründung · antwort Text
- gegeben: Matrix N = ((0; 0; 4), (0,25; 0; 0), (0; 0,4; 0,6)) (Zeilen) und Vektoren u = (u1; u2; u3)
- gesucht: Nachweis, dass es keinen Vektor u ≠ 0 mit N · u = 0 gibt
- verfahren: Das Gleichungssystem N · u = 0 mit dem Rechner lösen (oder det N ≠ 0): einzige Lösung ist der Nullvektor
- fehlerquelle: nur einen Vektor u ≠ 0 mit N · u ≠ 0 angeben

### 2017MgrundlegendBAGLAA1CAS-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Matrix N = ((0; 0; 4), (0,25; 0; 0), (0; 0,4; 0,6)) (Zeilen) und Vektoren u = (u1; u2; u3); für einen Vektor u gilt |u|^2 = 1800
- gesucht: Lösungen der Gleichung N · u = u
- verfahren: (N − E) · u = 0 lösen: u = t · (4; 1; 1) mit t ∈ IR; (4t)^2 + t^2 + t^2 = 1800 liefert t = ±10
- fehlerquelle: nur die positive Lösung angeben oder die Betragsbedingung als 4t + t + t = 1800 lesen

### 2025MerhoehtAAGLAA122 (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 5 · format Rechnung · antwort Text
- gegeben: A = ((0; 1), (0; 0)) und X = ((a; b), (c; d)) mit reellen a, b, c, d; Gleichung (X + A) · (X + A) = X² + 2 · A · X + A²
- gesucht: Bedingungen an a, b, c, d, unter denen die Gleichung gilt
- verfahren: (X + A)² ausmultiplizieren, ohne die Reihenfolge zu vertauschen; die Gleichung reduziert sich auf X · A = A · X; beide Produkte berechnen und vergleichen
- fehlerquelle: die binomische Formel für Matrizen als allgemeingültig ansehen und keine Bedingung finden

### 2020MgrundlegendAAGLAA12 (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: M = ((0; 0; c), (a; 0; 0), (d; b; 0)) mit ganzzahligen a, b, c, d; M · M = ((−10; 2; 0), (0; 0; 6), (3; 0; −10))
- gesucht: alle Zahlentupel (a; b; c; d)
- verfahren: M² ausrechnen, Einträge vergleichen, Ganzzahligkeit nutzen
- fehlerquelle: nur eine der beiden Lösungen finden oder b = ±2 zulassen (dann a nicht ganzzahlig)

### 2026MerhoehtAAGLAA121-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Rechnung · antwort Term
- gegeben: A = ((6; −2; 0), (4; 0; 0), (−4; 4; −2)); v_a = (1; 1; 0) mit A · v_a = 4 · v_a; für jedes reelle c gibt es ein reelles b mit A^(−1) · (b · v_a) = c · v_a; A^(−1) soll nicht berechnet werden
- gesucht: b in Abhängigkeit von c
- verfahren: beide Seiten mit A multiplizieren: b · v_a = A · (c · v_a) = c · (A · v_a) = c · 4 · v_a; weil v_a nicht der Nullvektor ist, folgt b = 4c
- fehlerquelle: b = c/4 angeben, weil die Inverse den Faktor umkehrt, ohne die Gleichung umzuformen

### 2026MerhoehtAAGLAA122-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Begründung|Rechnung · antwort Text
- gegeben: M = ((a; b), (c; d)) orthogonal, wenn M · M^T = ((1; 0), (0; 1)); Aussage: es gibt orthogonale Matrizen der Form M mit a = d = 1/3 · √5, die ungleich sind
- gesucht: Beurteilung der Aussage
- verfahren: M · M^T mit a = d = √5/3 ausmultiplizieren: 5/9 + b^2 = 1, (√5/3) · b + (√5/3) · c = 0, c^2 + 5/9 = 1; daraus b = 2/3 und c = −2/3 oder b = −2/3 und c = 2/3
- fehlerquelle: aus b^2 = 4/9 nur b = 2/3 nehmen und die Aussage für falsch halten

### 2022MerhoehtBAGLAA1WTR-2c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung|Begründung · antwort Text
- gegeben: F_a = ((a; a; 0), (a; a; 0), (1 − 2a; 1 − 2a; 1)), a ≥ 0; F_a^k mit Einträgen 1/2 · 2^k a^k, 1 − 2^k a^k und 0, 1
- gesucht: a, für die sich jeder Eintrag von F_a^k für k → ∞ einem endlichen Wert nähert
- verfahren: 2^k a^k = (2a)^k nach dem Wert von 2a untersuchen
- fehlerquelle: a = 1/2 ausschließen (Grenzwert 1 ist endlich)

### 2025MerhoehtBAGLAA1MMS-2b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea-mms · punkte 6 · format Begründung|Rechnung · antwort Text|Zahl
- gegeben: Zweistufige Produktion: aus Rohstoffen R₁–R₄ drei Zwischenprodukte Z₁–Z₃, daraus Endprodukte E₁–E₃; Tabellen: Zwischenprodukte je ME Endprodukt (Z₁: 3, 0, 0; Z₂: 1, 4, 0; Z₃: 0, 5, 2) und Rohstoffe je ME Endprodukt (R₁: 9, 12, 0; R₂: 3, 42, 12; R₃: 0, 20, 8; R₄: 0, 10, 4); Auftrag: je 10 ME der drei Endprodukte; Fertigungskosten der Zwischenprodukte für den Auftrag 1250 GE; Gleichung (2z z 2z) · (3 0 0 / 1 4 0 / 0 5 2) · (10; 10; 10) = 1250
- gesucht: Erläuterung der Gleichung im Sachzusammenhang; Lösung und ihre Deutung
- verfahren: Matrixprodukt als Zwischenproduktmengen, Zeilenvektor als Stückkosten (Z₁, Z₃ doppelt so teuer wie Z₂) deuten, nach z lösen
- fehlerquelle: den Zeilenvektor als Mengen statt als Stückkosten deuten

### 2023MerhoehtBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: C* = C mit vierter Spalte (u; v; 0,06) für das neue Endprodukt E₄ aus den beiden Zwischenprodukten
- gesucht: Summe der Mengeneinheiten der Zwischenprodukte je ME von E₄
- verfahren: B* mit Spalte (x; y) ansetzen, C* = A · B*, dritte Zeile auswerten
- fehlerquelle: u und v für nötig halten, obwohl die dritte Zeile genügt

### 2022MgrundlegendBAGLAA1WTR-1f (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 5 · format Kurzantwort · antwort Term
- gegeben: Transportunternehmen mit 150 Fahrzeugen an den Standorten A, B, C; Verteilung (a; b; c) abends; Übergang v_(n+1) = M · v_n mit M = ((0,7; 0,5; 0,1), (0,2; 0,2; 0,6), (0,1; 0,3; 0,3)); Mittwochmorgen verlassen 10 % der Fahrzeuge in B und drei Fahrzeuge in A die Standorte für die Woche; gesucht die Verteilung am Freitagabend aus der Verteilung v am Sonntagabend
- gesucht: ein Term für die Verteilung am Freitagabend in Abhängigkeit von v
- verfahren: Tage zählen (2 Übergänge bis Dienstag, 3 bis Freitag), Abgang als Diagonalmatrix und Vektor dazwischen
- fehlerquelle: Anzahl der Übergänge falsch zählen; den Abgang vor M² setzen

### 2024MgrundlegendBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 5 · format Begründung|Kurzantwort · antwort Text
- gegeben: Dienstagabend: 20 % der E-Scooter aus C entnommen, nach 48 Stunden nach C zurückgebracht; d Verteilung vor der Entnahme; Vektoren f = M·M·(M·diag(0; 0; 0,2)·d + diag(1; 1; 0,8)·d), g = M·(M·M·diag(1; 1; 0,8)·d + diag(0; 0; 0,2)·d), h = M·(M·M·(d − 0,2d) + (0; 0; 20))
- gesucht: welcher Vektor den Freitagabend beschreibt; Szenarien für die beiden anderen
- verfahren: Reihenfolge Entnahme – zwei Tage – Rückgabe – ein Tag mit den Termen vergleichen
- fehlerquelle: Anzahl der Tage zwischen Entnahme und Rückgabe falsch zählen

### 2026MgrundlegendBAGLAA1MMS-1c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga-mms · punkte 2 · format Begründung · antwort Text
- gegeben: Aussage: am Ende des Jahres nach Beobachtungsbeginn ist (3204; 2004; 792) die Kundenverteilung
- gesucht: Begründung, dass die Aussage im Modell falsch ist
- verfahren: Vorgängerverteilung aus P · v₀ = v₁ berechnen, negative Komponente als Widerspruch
- fehlerquelle: Summe 6000 prüfen und für ausreichend halten

### 2022MerhoehtBAGLAA1WTR-2d (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 5 · format Begründung · antwort Text
- gegeben: F_a für a ≤ 1/2 beschreibt Farbwechsel; für a < 1/2 gilt F_a^k → ((0; 0; 0), (0; 0; 0), (1; 1; 1))
- gesucht: Beschreibung der Farbwechsel in Abhängigkeit von a
- verfahren: Spalten von F_a als Abgänge deuten, Fälle a = 0, 0 < a < 1/2, a = 1/2 trennen, Grenzmatrix als Endzustand
- fehlerquelle: Fall a = 1/2 (kein Abfluss nach Blau) übersehen

### 2023MerhoehtAAGLAA12-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Kurzantwort · antwort Text
- gegeben: v_(n−1) = M⁻¹ · v_n; (M⁻¹)³ = ((1/(20c); 0; 0), (0; 1/(20c); 0), (0; 0; 1/(20c))) mit c > 0
- gesucht: Beschreibung der Entwicklung der Population mit fortschreitender Zeit in Abhängigkeit von c, einschließlich der Größe
- verfahren: (M⁻¹)³ = 1/(20c) · E heißt: drei Monate zurück ist jede Anzahl durch 20c geteilt, also drei Monate vorwärts mit 20c multipliziert; Fälle nach 20c gegen 1
- fehlerquelle: den Faktor 1/(20c) als Wachstumsfaktor vorwärts lesen (Richtung vertauscht)

### 2026MerhoehtAAGLAA11-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: v_(n+1) = M · v_n mit M = ((0; 0; 2), (r; 0; 0), (0; 0,6; 0)), r reell, v_0 ungleich Nullvektor; nach drei Tagen stimmt die Verteilung mit der zu Beobachtungsbeginn überein
- gesucht: Wert von r
- verfahren: M^3 berechnen: M^2 = ((0; 1,2; 0), (0; 0; 2r), (0,6r; 0; 0)), M^3 = 1,2r · E; aus v_3 = M^3 · v_0 = v_0 und v_0 ungleich Nullvektor folgt 1,2r = 1
- fehlerquelle: M^3 als komponentenweise dritte Potenz der Einträge bilden

### 2017MerhoehtAAGLAA112-a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Kurzantwort · antwort Term
- gegeben: Übergangsdiagramm für das Wechseln von Ratten zwischen vier Räumen R1 bis R4 (Anteile je Beobachtungsschritt wie in der Skizze)
- gesucht: zugehörige Übergangsmatrix
- verfahren: Anteile spaltenweise nach Ausgangsraum eintragen
- fehlerquelle: Zeilen und Spalten vertauschen

### 2020MgrundlegendAAGLAA111-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 1 · format Rechnung · antwort Term
- gegeben: Vertauschungsmatrix (je Zeile und Spalte genau eine 1) M = ((0; 1; 0), (0; 0; 1), (1; 0; 0)); v = (1; 2; 3)
- gesucht: Vektor M · v
- verfahren: multiplizieren
- fehlerquelle: Spalten statt Zeilen mit v multiplizieren ((3; 1; 2))

### 2024MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: M · (300; 200; 400) = (a; b; c)
- gesucht: b und seine Bedeutung
- verfahren: zweite Zeile von M mit dem Vektor multiplizieren
- fehlerquelle: Spalte statt Zeile nehmen

### 2026MgrundlegendBAGLAA1MMS-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga-mms · punkte 2 · format Rechnung · antwort Zahl
- gegeben: P wie in a; Ende eines Jahres 2500 in A, 1900 in B, Rest in C
- gesucht: Kundenverteilung am Ende des nächsten Jahres
- verfahren: Restgruppe bilden, Matrix mal Vektor
- fehlerquelle: 1600 vergessen und mit Nullvektor-Komponente rechnen

### 2026MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: P aus a; Anfang April 1000 Eier, 2000 Larven, 3000 Käfer
- gesucht: Zusammensetzung Anfang Mai
- verfahren: P · v
- fehlerquelle: Zeile mal Spalte vertauschen

### 2018MgrundlegendAAGLAA111-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Kurzantwort · antwort Text
- gegeben: A ist eine 2×2-Matrix; für C ist C · A bildbar, A · C nicht
- gesucht: alle möglichen Formen von C
- verfahren: Formatbedingung für beide Produkte auswerten
- fehlerquelle: nur „C ist keine 2×2-Matrix“ antworten

### 2019MgrundlegendAAGLAA12-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 1 · format Kurzantwort · antwort Term
- gegeben: Population (E; L; K) aus Eiern, Larven, Käfern; Übergang je Monat durch M = ((0; 0; a), (1/4; 0; 0), (0; 1/2; 0)) mit a > 0
- gesucht: Matrix M²
- verfahren: M · M ausmultiplizieren
- fehlerquelle: Einträge elementweise quadrieren

### 2022MgrundlegendBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Transportunternehmen mit 150 Fahrzeugen an den Standorten A, B, C; Verteilung (a; b; c) abends; Übergang v_(n+1) = M · v_n mit M = ((0,7; 0,5; 0,1), (0,2; 0,2; 0,6), (0,1; 0,3; 0,3)); M² = ((0,6; 0,48; 0,4), (0,24; 0,32; r), (0,16; 0,2; s))
- gesucht: die Werte von r und s
- verfahren: Zeile 2 mal Spalte 3 von M; s über die Spaltensumme
- fehlerquelle: Zeile mit Zeile multiplizieren

### 2018MgrundlegendAAGLAA111-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: A = ((7; 4), (2; 0)), B = ((a; b), (c; d)); A · B = E
- gesucht: Werte von a, b, c, d
- verfahren: Produkt ausrechnen, vier Gleichungen lösen
- fehlerquelle: Produkt B · A statt A · B ansetzen (hier gleiches Ergebnis, aber falsche Zuordnung der Gleichungen)

### 2020MgrundlegendAAGLAA112-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Kurzantwort · antwort Zahl
- gegeben: A = ((0; 1/2; 0), (0; 0; −1/5), (−10; 0; 0)); A⁻¹ = ((0; 0; c), (a; 0; 0), (0; b; 0))
- gesucht: Werte von a, b, c
- verfahren: Produkt mit E vergleichen oder Kehrwerte
- fehlerquelle: Vorzeichen bei b und c

### 2020MgrundlegendAAGLAA111-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Kurzantwort · antwort Term
- gegeben: M = ((0; 1; 0), (0; 0; 1), (1; 0; 0))
- gesucht: inverse Matrix zu M
- verfahren: Vertauschung umkehren
- fehlerquelle: M selbst als Inverse angeben (M³ = E, nicht M²)

### 2020MgrundlegendAAGLAA111-c (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Vertauschungsmatrizen N (3×3); N · v hat gegenüber v genau zwei vertauschte Einträge
- gesucht: Beschreibung des Aufbaus aller solchen N
- verfahren: Rolle der Diagonaleinträge deuten
- fehlerquelle: „zwei Einsen auf der Diagonale“ (das wäre die Einheitsmatrix)

### 2024MerhoehtAAGLAA121 (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 5 · format Kurzantwort|Rechnung · antwort Text|Zahl
- gegeben: M = ((1; 0; 0), (0; 0; 1), (0; 1; 0)); A = ((0; a; 2), (b; 2c; d), (1; 2d − b; c − a)) mit reellen a, b, c, d
- gesucht: Beschreibung der Änderung einer beliebigen 3×3-Matrix bei Multiplikation mit M von rechts bzw. von links|Werte a, b, c, d mit M · A · M = A
- verfahren: M vertauscht die letzten beiden Spalten (rechts) bzw. Zeilen (links); A muss unter beiden Vertauschungen unverändert bleiben, Einträge vergleichen
- fehlerquelle: M · A · M vollständig ausmultiplizieren und sich verrechnen

### 2019MerhoehtAAGLAA12-b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Definition der Orthogonalität aus a; Matrix ((0; 1), (1; 0))^101
- gesucht: ob diese Matrix orthogonal ist
- verfahren: Potenz über V² = E auf V zurückführen, dann V^T · V prüfen
- fehlerquelle: die Potenz nicht auflösen und die Orthogonalität nur behaupten

### 2018MerhoehtBAGLAA1WTR-2a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Indisches Springkraut: Zustand (S; P) mit Samen S und Pflanzen P; Frühjahr bis Herbst F · u mit F = ((f1; f2), (0; 0)), Herbst bis Frühjahr H · v mit H = ((0,3; 0), (0,01; 0)); Frühjahr zu Frühjahr J · u mit J = ((0,3; 150), (0,01; 5))
- gesucht: Werte von f1 und f2
- verfahren: H · F = J ausmultiplizieren und vergleichen
- fehlerquelle: F · H statt H · F bilden (Reihenfolge der Schritte)

### 2021MerhoehtAAGLAA122 (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 5 · format Rechnung · antwort Term
- gegeben: A = ((1; 2), (0; 1)); für B gilt A · B = B · A
- gesucht: alle Matrizen B, die die Bedingung erfüllen
- verfahren: B allgemein ansetzen, Produkte gleichsetzen, Bedingungen ablesen
- fehlerquelle: nur B = A oder B = E angeben

### 2018MgrundlegendAAGLAA12-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: A = ((1; 1), (0; 0)), B = ((0; 1), (0; b)); A² + 2 · A · B + B² = ((1; 3 + 3b), (0; b²)) vorgegeben; (A + B)² = A² + 2 · A · B + B² gilt nur für einen Wert von b
- gesucht: dieser Wert von b
- verfahren: (A + B)² ausrechnen und mit dem vorgegebenen Term vergleichen
- fehlerquelle: (A + B)² über die binomische Formel berechnen – dann ist die Gleichung trivial und b bleibt offen

### 2018MgrundlegendAAGLAA12-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Begründung · antwort Term
- gegeben: 2×2-Matrizen C und D mit C · D = −D · C
- gesucht: (C + D)² als Summe dargestellt und so weit wie möglich vereinfacht
- verfahren: Produkt ausmultiplizieren, Mittelterme mit der Bedingung aufheben
- fehlerquelle: binomische Formel mit 2 · C · D anwenden

### 2021MerhoehtAAGLAA111 (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Spur einer quadratischen Matrix als Summe der Hauptdiagonale (mit Beispiel); M_k = ((1; 0), (−k; k)) mit k ≠ 0
- gesucht: alle k, für die M_k und die inverse Matrix dieselbe Spur haben
- verfahren: Inverse bestimmen, Spuren gleichsetzen
- fehlerquelle: Spur der Inversen als Kehrwert der Spur ansetzen

### 2020MgrundlegendAAGLAA112-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 3 · format Rechnung · antwort Term
- gegeben: A wie in a; es gibt v ≠ 0 mit A · v = v
- gesucht: ein solcher Vektor
- verfahren: Gleichungssystem aufstellen, z frei wählen
- fehlerquelle: das System als eindeutig lösbar behandeln und nur v = 0 finden

### 2022MerhoehtAAGLAA12-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 2 · format Rechnung · antwort Term
- gegeben: stochastische Matrix M = ((0,4; 0,3), (0,6; 0,7)) (Spaltensummen 1, Einträge nicht negativ)
- gesucht: ein Vektor v ≠ 0 mit M · v = v
- verfahren: Gleichungssystem lösen, Vielfaches wählen
- fehlerquelle: v_y = 2 v_x und v = (2; 1) vertauschen

### 2022MerhoehtAAGLAA112-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung · antwort Term
- gegeben: M = ((1; 3), (1; −1))
- gesucht: alle Vektoren v mit M · v = 2 · v
- verfahren: Gleichungssystem aufstellen, beide Gleichungen auf v1 = 3v2 bringen
- fehlerquelle: nur die eine Lösung (3; 1) angeben

### 2023MgrundlegendAAGLAA12 (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 5 · format Rechnung · antwort Term
- gegeben: M = ((2; 0), (3; 1)); gesucht sind alle Vektoren (a; b) ≠ (0; 0), für die ein reelles t mit M · (a; b) = t · (a; b) existiert
- gesucht: alle diese Vektoren
- verfahren: Produkt gleichsetzen; aus I 2a = ta folgt a = 0 oder t = 2; beide Fälle in II einsetzen
- fehlerquelle: I durch a teilen, ohne a = 0 zu betrachten, und die Vektoren (0; b) verlieren

### 2024MgrundlegendAAGLAA12-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Rechnung · antwort Term
- gegeben: M = ((1; 0; 0), (1; 1; −1), (1; 0; 0))
- gesucht: alle Vektoren b mit M · b = b
- verfahren: M · (x; y; z) = (x; x + y − z; x) mit (x; y; z) gleichsetzen; die zweite Koordinate liefert x = z, die dritte ebenfalls, y bleibt frei
- fehlerquelle: nur einen Fixvektor angeben statt der zweiparametrigen Lösungsmenge

### 2024MgrundlegendAAGLAA12-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: M = ((1; 0; 0), (1; 1; −1), (1; 0; 0))
- gesucht: Begründung, dass es mehr als einen Vektor a mit M · a = (0; 0; 0) gibt
- verfahren: das Gleichungssystem liefert x = 0 und y = z; neben dem Nullvektor erfüllt jeder Vektor (0; s; s) die Bedingung
- fehlerquelle: nur den Nullvektor finden, weil x = 0 auf y = z = 0 übertragen wird

### 2026MerhoehtAAGLAA121-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: A = ((6; −2; 0), (4; 0; 0), (−4; 4; −2)); v_a = (a; 1; 0) mit reellem a; es gilt A · v_a = 4 · v_a
- gesucht: Wert von a
- verfahren: A · v_a = (6a − 2; 4a; −4a + 4) mit 4 · v_a = (4a; 4; 0) vergleichen; die zweite Komponente liefert 4a = 4
- fehlerquelle: aus der ersten Komponente 6a − 2 = 4a rechnen und den Wert nicht an den übrigen Komponenten prüfen

### 2025MgrundlegendAAGLAA11 (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 5 · format Rechnung · antwort Zahl|Text
- gegeben: M = ((0; b; 0), (1; 0; a), (0; 0,5; 1 − a)) mit reellen a und b; v = (1; 2; 4)
- gesucht: Untersuchung, ob es Werte von a und b gibt, sodass M · v = v gilt
- verfahren: M · v = (2b; 1 + 4a; 5 − 4a) mit v gleichsetzen: I 2b = 1, II 1 + 4a = 2, III 5 − 4a = 4; aus I und II folgen b und a, III bestätigt
- fehlerquelle: die dritte Gleichung nicht prüfen oder aus III einen zweiten Wert für a ableiten

### 2025MerhoehtAAGLAA11-b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: v = (6; a) mit a = 5; M = ((0; b), (2; 0)) mit reellem b
- gesucht: Wert von b, sodass v und M · v orthogonal sind
- verfahren: M · v berechnen, Skalarprodukt mit v gleich 0 setzen und nach b auflösen
- fehlerquelle: Zeilen und Spalten der Matrix beim Produkt vertauschen (M · v = (12; 5b))

### 2020MerhoehtAAGLAA12 (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 5 · format Begründung · antwort Text
- gegeben: spaltenstochastisch: Einträge ≥ 0, jede Spaltensumme 1; M = ((a; b), (c; d)) spaltenstochastisch
- gesucht: Nachweis, dass M² spaltenstochastisch ist
- verfahren: M² berechnen, Nichtnegativität und Spaltensummen mit a + c = 1, b + d = 1 zeigen
- fehlerquelle: die Spaltensummen ausmultipliziert stehen lassen, ohne a + c = 1 einzusetzen

### 2022MerhoehtAAGLAA12-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: N stochastische 2×2-Matrix; u Vektor mit Komponentensumme 5
- gesucht: Nachweis, dass N · u ebenfalls die Komponentensumme 5 hat
- verfahren: N und u allgemein ansetzen, Summe der Komponenten von N · u nach u_x und u_y sortieren, Spaltensummen 1 einsetzen
- fehlerquelle: mit einer Zahlenmatrix statt allgemein rechnen

### 2024MerhoehtBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Rechnung · antwort Text
- gegeben: Q = ((0,2; 0,3; 0,2), (0,7; 0; 0), (0; 0,6; 0,7)); Aussage: für jeden Vektor u ist die Komponentensumme von Q · u das 0,9-Fache der Komponentensumme von u
- gesucht: Nachweis der Aussage
- verfahren: Q · u mit allgemeinem u, Komponenten addieren
- fehlerquelle: nur ein Zahlenbeispiel

### 2019MerhoehtAAGLAA12-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Definition: M^T durch Vertauschen von b und c; M orthogonal, wenn M^T · M = E; M = ((3/5; −4/5), (4/5; 3/5))
- gesucht: Nachweis, dass M orthogonal ist
- verfahren: M^T bilden und M^T · M ausrechnen
- fehlerquelle: M · M statt M^T · M berechnen

### 2022MgrundlegendAAGLAA12 (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 5 · format Rechnung · antwort Text|Zahl
- gegeben: M = ((a; b), (c; −a)) mit reellen a, b, c; M heißt selbstinvers, wenn M⁻¹ = M
- gesucht: Nachweis, dass b · c ≤ 1 gilt, wenn M selbstinvers ist; für a = 5 je ein Wert von b und c mit M selbstinvers
- verfahren: M⁻¹ = M in M² = E übersetzen, M² ausrechnen, bc = 1 − a² und a² ≥ 0; a = 5 einsetzen
- fehlerquelle: die Inverse mit der Formel berechnen und mit M vergleichen statt M² = E zu nutzen

### 2026MerhoehtAAGLAA122-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 1 · format Kurzantwort · antwort Term
- gegeben: für M = ((a; b), (c; d)) ist M^T = ((a; c), (b; d)) die transponierte Matrix; M heißt orthogonal, wenn M · M^T = ((1; 0), (0; 1))
- gesucht: eine orthogonale Matrix der Form M mit a, b, c, d aus {0; 1}, die nicht die Einheitsmatrix ist
- verfahren: eine Matrix wählen, deren Zeilen die Länge 1 haben und zueinander senkrecht sind, etwa die Vertauschung der beiden Einheitsvektoren
- fehlerquelle: eine Matrix mit einer Nullzeile angeben, deren Produkt mit der Transponierten nicht die Einheitsmatrix ist

### 2023MgrundlegendAAGLAA112-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: M = ((1; 0; −3), (0; 1; −2), (0; 0; 0))
- gesucht: Entscheidung mit Begründung, ob es einen Vektor u mit M · u = (3; 2; 1) gibt
- verfahren: dritte Zeile von M betrachten
- fehlerquelle: ein Gleichungssystem aufstellen und sich in den ersten beiden Zeilen verlieren

### 2023MgrundlegendAAGLAA112-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 3 · format Rechnung · antwort Text
- gegeben: M = ((1; 0; −3), (0; 1; −2), (0; 0; 0)); v = M · (a; b; c) − (a; b; c) mit c ≠ 0; w = (3; 2; 1)
- gesucht: für welche reellen a, b, c die Vektoren v und w kollinear sind
- verfahren: v ausrechnen; es bleibt −c · w
- fehlerquelle: Bedingungen an a und b suchen, obwohl sie herausfallen

### 2018MerhoehtAAGLAA12-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Rechnung|Begründung · antwort Term
- gegeben: jede 2×2-Matrix M ordnet P(a | b) über M · (a; b) = (a'; b') den Bildpunkt P' zu; M = ((−1; 0), (0; 1))
- gesucht: Koordinaten von P' in a und b und Begründung, dass die Zuordnung eine Spiegelung an der y-Achse ist
- verfahren: Produkt ausrechnen, Koordinatenänderung deuten
- fehlerquelle: Spiegelung an der x-Achse nennen

### 2018MerhoehtAAGLAA12-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung · antwort Term
- gegeben: P*(a* | b*) Spiegelpunkt von P an der x-Achse; P* soll Mittelpunkt der Strecke von O nach P' sein
- gesucht: Matrix M, die P auf P' abbildet
- verfahren: P* bestimmen, P' als 2 · P*, Matrix ablesen
- fehlerquelle: P' als Mittelpunkt von O und P* nehmen (Faktor 1/2 statt 2)

### 2024MerhoehtAAGLAA11-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 1 · format Rechnung · antwort Zahl
- gegeben: Produktionsprozess mit r = ((5; 4), (12; 10)) · e (Rohstoffe aus Endprodukten) und z = ((2; 1), (1; 1), (2; 2)) · e (Zwischenprodukte aus Endprodukten); Mengeneinheiten
- gesucht: Mengeneinheiten jedes Rohstoffs für 2 ME des ersten und 2 ME des zweiten Endprodukts
- verfahren: Matrix mit (2; 2) multiplizieren
- fehlerquelle: die Zwischenproduktmatrix verwenden

### 2025MerhoehtBAGLAA1MMS-2a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea-mms · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Zweistufige Produktion: aus Rohstoffen R₁–R₄ drei Zwischenprodukte Z₁–Z₃, daraus Endprodukte E₁–E₃; Tabellen: Zwischenprodukte je ME Endprodukt (Z₁: 3, 0, 0; Z₂: 1, 4, 0; Z₃: 0, 5, 2) und Rohstoffe je ME Endprodukt (R₁: 9, 12, 0; R₂: 3, 42, 12; R₃: 0, 20, 8; R₄: 0, 10, 4); Auftrag: je 10 ME der drei Endprodukte
- gesucht: benötigte ME des Rohstoffs R₂
- verfahren: Zeile R₂ mit dem Auftragsvektor multiplizieren
- fehlerquelle: die Zwischenprodukttabelle statt der Rohstofftabelle nehmen

### 2026MerhoehtBAGLAA1MMS-2a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: R · z = r mit R = ((5; 4; 5), (4; 5; 6), (5; 6; 6)); Z · e = z mit Z = ((2; 3), (3; 2), (2; 2)); je eine ME von E1 und E2
- gesucht: ME der drei Zwischenprodukte und des Rohstoffs R1
- verfahren: Z · (1; 1), dann erste Zeile von R mal z
- fehlerquelle: R mit e statt mit z multiplizieren

### 2026MerhoehtBAGLAA1WTR-2a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: R · z = r mit R = ((5; 4; 5), (4; 5; 6), (5; 6; 6)); Z · e = z mit Z = ((2; 3), (3; 2), (2; 2)); je eine ME von E1 und E2
- gesucht: ME der drei Zwischenprodukte und des Rohstoffs R1
- verfahren: Z · (1; 1), dann erste Zeile von R mal z
- fehlerquelle: R mit e statt mit z multiplizieren

### 2021MgrundlegendAAGLAA111-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Kurzantwort · antwort Term
- gegeben: Rohstoffe R1, R2, Zwischenprodukte Z1, Z2, Z3, Endprodukte E1, E2 mit Bedarfen im Diagramm; r = ((1; 6), (2; 4)) · e
- gesucht: Matrix M mit z = M · e
- verfahren: Bedarf an Zwischenprodukten je Endprodukt aus dem Diagramm ablesen
- fehlerquelle: Matrix transponiert angeben (2×3)

### 2024MgrundlegendAAGLAA111-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Produktionsprozess Rohstoffe R1, R2 zu Endprodukten E1, E2 mit ((x; 4), (6; y)) · (e1; e2) = (r1; r2); Einträge der Vektoren sind Mengeneinheiten
- gesucht: beschriftetes Verflechtungsdiagramm
- verfahren: je Matrixeintrag einen Pfeil vom Rohstoff der Zeile zum Endprodukt der Spalte mit dem Eintrag beschriften
- fehlerquelle: Zeilen und Spalten vertauschen (4 an R1→E2)

### 2023MerhoehtBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Kurzantwort · antwort Zahl
- gegeben: A = ((0,5; 0), (0; 0,8), (0,04; 0,04)) Rohstoffe je Zwischenprodukt, B = ((1; 0,4; 0), (0; 0,7; 1,2)) Zwischenprodukte je Endprodukt, C = ((0,5; 0,2; 0), (0; 0,56; 0,96), (0,04; 0,044; 0,048)) Rohstoffe je Endprodukt; Pfeil R₁ → Z₁ mit s
- gesucht: Wert und Bedeutung von s
- verfahren: Eintrag der Matrix A ablesen
- fehlerquelle: Eintrag aus C statt A lesen

### 2020MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Kurzantwort|Begründung · antwort Text
- gegeben: Herstellungsprozess: aus den Rohstoffen R₁, R₂, R₃ werden die Zwischenprodukte Z₁, Z₂ und daraus die Endprodukte E₁, E₂, E₃ hergestellt; Bedarf je Mengeneinheit laut Diagramm: Z₁ braucht 2 R₁, 1 R₃; Z₂ braucht 1 R₁, 1 R₂, 2 R₃; E₁ braucht 3 Z₁; E₂ braucht 1 Z₁ und 5 Z₂; E₃ braucht 7 Z₁ und 1 Z₂; Gleichungen (r₁; r₂; r₃) = A · (z₁; z₂) und (z₁; z₂) = B · (e₁; e₂; e₃); drei Matrizen zur Auswahl: I (3 0 / 1 5 / 7 1), II (3 1 7 / 0 5 1), III (3 1 7 / 0 5 1 / 0 0 0)
- gesucht: die Matrix, die B darstellt, mit Begründung
- verfahren: Format aus der Gleichung ableiten (2 × 3), passende Matrix wählen
- fehlerquelle: Matrix I (transponiert) wählen, weil sie die Pfeile zeilenweise wiedergibt

### 2023MgrundlegendBAGLAA1WTR-2c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Kurzantwort|Begründung · antwort Text
- gegeben: Veränderter Prozess; Matrix L (Rohstoffe je Zwischenprodukt) hat vier Zeilen und vier Spalten; weiterhin zwei Getränke
- gesucht: Zeilen- und Spaltenzahl der Matrix N (Zwischenprodukte je Getränk) mit Begründung
- verfahren: Spaltenzahl von L als Zahl der Zwischenprodukte lesen, Getränkezahl als Spaltenzahl von N
- fehlerquelle: Zeilen und Spalten vertauscht

### 2020MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Herstellungsprozess: aus den Rohstoffen R₁, R₂, R₃ werden die Zwischenprodukte Z₁, Z₂ und daraus die Endprodukte E₁, E₂, E₃ hergestellt; Bedarf je Mengeneinheit laut Diagramm: Z₁ braucht 2 R₁, 1 R₃; Z₂ braucht 1 R₁, 1 R₂, 2 R₃; E₁ braucht 3 Z₁; E₂ braucht 1 Z₁ und 5 Z₂; E₃ braucht 7 Z₁ und 1 Z₂; Gleichungen (r₁; r₂; r₃) = A · (z₁; z₂) und (z₁; z₂) = B · (e₁; e₂; e₃); A · B = (6 7 15 / a 5 1 / 9 13 23)
- gesucht: Begründung im Sachzusammenhang, dass a = 0 gilt
- verfahren: a als Bedarf an R₂ für eine Mengeneinheit E₁ deuten und den Pfad R₂ → Z₂ → E₁ als nicht vorhanden erkennen
- fehlerquelle: a durch Ausrechnen des Matrixprodukts bestimmen statt im Sachzusammenhang zu begründen

### 2023MgrundlegendBAGLAA1WTR-2a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 4 · format Rechnung|Begründung · antwort Zahl
- gegeben: Diagramm Rohstoffe R₁–R₄ → Zwischenprodukte Z₁–Z₃ → Getränke M₁, M₂; Gesamtmatrix K = ((0,51; 0,53), (0,22; x), (0,16; y), (0,11; 0,21)) Rohstoffe je Getränk
- gesucht: Bestätigung x = 0,26; Begründung y = 0
- verfahren: Bedarf von R₂ für M₂ über Z₂ und Z₃ summieren; für y die Pfade von R₃ nach M₂ betrachten
- fehlerquelle: Pfad R₂ → Z₁ → M₂ mitgezählt, obwohl Z₁ nicht in M₂ eingeht

### 2026MerhoehtBAGLAA1WTR-2b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 1 · format Kurzantwort · antwort Text
- gegeben: R · Z = ((32; 33), (35; 34), (40; 39))
- gesucht: Bedeutung der Matrix
- verfahren: Gesamtmatrix als Rohstoff-Endprodukt-Verflechtung deuten
- fehlerquelle: Zeilen und Spalten vertauscht deuten

### 2026MerhoehtBAGLAA1MMS-2b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 1 · format Kurzantwort · antwort Text
- gegeben: R · Z = ((32; 33), (35; 34), (40; 39))
- gesucht: Bedeutung der Matrix
- verfahren: Gesamtmatrix als Rohstoff-Endprodukt-Verflechtung deuten
- fehlerquelle: Zeilen und Spalten vertauscht deuten

### 2020MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 1 · format Kurzantwort · antwort Text
- gegeben: Herstellungsprozess: aus den Rohstoffen R₁, R₂, R₃ werden die Zwischenprodukte Z₁, Z₂ und daraus die Endprodukte E₁, E₂, E₃ hergestellt; Bedarf je Mengeneinheit laut Diagramm: Z₁ braucht 2 R₁, 1 R₃; Z₂ braucht 1 R₁, 1 R₂, 2 R₃; E₁ braucht 3 Z₁; E₂ braucht 1 Z₁ und 5 Z₂; E₃ braucht 7 Z₁ und 1 Z₂; Gleichungen (r₁; r₂; r₃) = A · (z₁; z₂) und (z₁; z₂) = B · (e₁; e₂; e₃); Gleichung (3; 3; 6) = A · (0; 3)
- gesucht: Bedeutung der Gleichung im Sachzusammenhang
- verfahren: Vektor (0; 3) als Bestellung von 3 Mengeneinheiten Z₂ lesen, linke Seite als Rohstoffbedarf
- fehlerquelle: Ein- und Ausgangsvektor vertauschen

### 2021MgrundlegendAAGLAA111-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: r = ((1; 6), (2; 4)) · e; verbraucht 28 Mengeneinheiten R1 und 40 Mengeneinheiten R2
- gesucht: hergestellte Mengeneinheiten von E1 und E2
- verfahren: Gleichungssystem aufstellen und lösen
- fehlerquelle: Matrix mit r statt e multiplizieren

### 2021MerhoehtAAGLAA113-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Rohstoffe R1, R2, R3, Zwischenprodukte Z1, Z2, Z3, Endprodukte E1, E2; r = ((4; 0), (12; 4), (8; 12)) · e; verbraucht 8 Mengeneinheiten R1, 28 Mengeneinheiten R2 und r3 Mengeneinheiten R3, nichts bleibt übrig
- gesucht: Wert von r3
- verfahren: e1 und e2 aus den ersten beiden Zeilen, r3 aus der dritten
- fehlerquelle: r3 aus dem Diagramm statt aus der Matrix zusammensetzen

### 2021MerhoehtAAGLAA113-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Diagramm mit unbekannten Bedarfen a (R1 → Z1) und b (R2 → Z1); Gesamtmatrix ((4; 0), (12; 4), (8; 12))
- gesucht: Werte von a und b
- verfahren: Einträge der Gesamtmatrix über die Wege R1 → Z1 → E1 und R2 → (Z1, Z2) → E1 aufstellen
- fehlerquelle: b aus 2b = 12 ohne den Weg über Z2 berechnen

### 2020MgrundlegendBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Herstellungsprozess: aus den Rohstoffen R₁, R₂, R₃ werden die Zwischenprodukte Z₁, Z₂ und daraus die Endprodukte E₁, E₂, E₃ hergestellt; Bedarf je Mengeneinheit laut Diagramm: Z₁ braucht 2 R₁, 1 R₃; Z₂ braucht 1 R₁, 1 R₂, 2 R₃; E₁ braucht 3 Z₁; E₂ braucht 1 Z₁ und 5 Z₂; E₃ braucht 7 Z₁ und 1 Z₂; Gleichungen (r₁; r₂; r₃) = A · (z₁; z₂) und (z₁; z₂) = B · (e₁; e₂; e₃); A · B = (6 7 15 / 0 5 1 / 9 13 23); Vorrat 510 R₁, 150 R₂, 840 R₃; nur E₁ und E₂ werden hergestellt
- gesucht: Mengeneinheiten von E₁ und E₂, die die Rohstoffe vollständig aufbrauchen
- verfahren: Gleichungssystem aus A · B · (e₁; e₂; 0) = Vorrat aufstellen und lösen
- fehlerquelle: mit A oder B allein statt mit A · B rechnen

### 2024MgrundlegendAAGLAA111-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: ((x; 4), (6; y)) · (e1; e2) = (r1; r2); von E1 wird doppelt so viel produziert wie von E2; die eingesetzte Menge von R1 ist viermal so groß wie die produzierte Menge von E1
- gesucht: Wert von x
- verfahren: e1 = 2e2 und r1 = 4e1 = 8e2 in die erste Zeile x · e1 + 4 · e2 = r1 einsetzen und nach x auflösen
- fehlerquelle: „viermal so groß“ als r1 = e1/4 ansetzen

### 2024MerhoehtAAGLAA11-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Rechnung · antwort Term
- gegeben: r = ((5; 4), (12; 10)) · e und z = ((2; 1), (1; 1), (2; 2)) · e; für je 1 ME der drei Zwischenprodukte ist gleich viel des ersten Rohstoffs nötig; für 1 ME des ersten und des zweiten Zwischenprodukts je 2 ME des zweiten Rohstoffs
- gesucht: Matrix M mit r = M · z
- verfahren: M mit den Unbekannten a (erste Zeile) und b ansetzen, M · Z = R lösen
- fehlerquelle: M als 3×2-Matrix ansetzen

### 2023MerhoehtBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Produktion: e₁ ME von E₁, 10 ME von E₂, 25 ME von E₃; Verbrauch 6 ME von R₁
- gesucht: benötigte Mengeneinheiten von R₃
- verfahren: Erste Zeile von C liefert e₁, dritte Zeile den Bedarf an R₃
- fehlerquelle: e₁ als 6 einsetzen

### 2026MerhoehtBAGLAA1WTR-2c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: je 429 ME der drei Rohstoffe; nur E2 wird gefertigt
- gesucht: maximale Anzahl ME von E2
- verfahren: Rohstoffbedarf je ME E2 mit dem Vorrat vergleichen, engster Rohstoff
- fehlerquelle: 429/33 = 13 nehmen (erster statt engster Rohstoff)

### 2026MerhoehtBAGLAA1MMS-2c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: N = R · Z = ((32; 33), (35; 34), (40; 39)); von jedem Rohstoff 1298 ME vorhanden; doppelt so viele ME von E2 wie von E1
- gesucht: maximale Anzahl ME von E2 für diesen Auftrag
- verfahren: Endproduktvektor (e; 2e) ansetzen, Rohstoffbedarf N · (e; 2e) als Terme in e, jede Komponente höchstens 1298, kleinste Schranke nehmen, e2 = 2e
- fehlerquelle: e = 11 als Antwort geben statt e2 = 22; die Schranke aus der ersten Zeile (98e) nehmen

### 2023MgrundlegendBAGLAA1WTR-2b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: K wie in a mit x = 0,26, y = 0; Kosten je ME Rohstoff 0,1; 0,1; 0,5; 0,3 GE; dreimal so viele ME von M₁ wie von M₂; Gesamtkosten höchstens 3500 GE
- gesucht: Höchstmengen von M₁ und M₂
- verfahren: Produktionsvektor mit einer Unbekannten ansetzen, Rohstoffbedarf und Kosten als Term in m₂, Schranke auflösen
- fehlerquelle: Verhältnis 3 : 1 umgekehrt angesetzt

### 2026MerhoehtBAGLAA1WTR-2d (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 6 · format Rechnung · antwort Zahl
- gegeben: Kosten je ME 5, 6, 7 GE; R1, R2 steigen 3 % je Jahr; Gesamtkosten der Rohstoffe für E1 dürfen in fünf Jahren um höchstens 20 % steigen
- gesucht: maximaler jährlicher prozentualer Anstieg für R3
- verfahren: Kostenterm heute und in fünf Jahren aufstellen, Ungleichung nach dem Wachstumsfaktor lösen
- fehlerquelle: Anstieg linear (5 · 3 %) statt exponentiell ansetzen

### 2026MerhoehtBAGLAA1MMS-2d (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Kosten je ME 5, 6, 7 GE; R1, R2 steigen 3 % je Jahr; Gesamtkosten der Rohstoffe für E1 dürfen in fünf Jahren um höchstens 20 % steigen
- gesucht: maximaler jährlicher prozentualer Anstieg für R3
- verfahren: Kostenterm heute und in fünf Jahren aufstellen, Ungleichung nach dem Wachstumsfaktor lösen
- fehlerquelle: Anstieg linear (5 · 3 %) statt exponentiell ansetzen

### 2025MerhoehtBAGLAA1MMS-2c (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea-mms · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Zweistufige Produktion: aus Rohstoffen R₁–R₄ drei Zwischenprodukte Z₁–Z₃, daraus Endprodukte E₁–E₃; Tabellen: Zwischenprodukte je ME Endprodukt (Z₁: 3, 0, 0; Z₂: 1, 4, 0; Z₃: 0, 5, 2) und Rohstoffe je ME Endprodukt (R₁: 9, 12, 0; R₂: 3, 42, 12; R₃: 0, 20, 8; R₄: 0, 10, 4); Auftrag: je 10 ME der drei Endprodukte; Lager 400 ME R₃ und 200 ME R₄ (werden vollständig verbraucht), R₁ und R₂ unbegrenzt; anderer Auftrag: 10 ME E₂, 25 ME E₃, e₁ ME E₁; Anteil von R₁ an allen Rohstoffen 25 %
- gesucht: Anzahl der ME von E₁ dieses Auftrags
- verfahren: r₁ und r₂ als Terme in e₁ aus der Rohstofftabelle, Anteilsgleichung mit 600 für R₃ und R₄ lösen
- fehlerquelle: R₃ und R₄ aus der Tabelle mit e₁ berechnen statt den Lagerbestand 600 zu nehmen

### 2023MerhoehtBAGLAA1WTR-1e (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Zeichnen|Begründung · antwort Grafik
- gegeben: B_t = ((1; t; 0), (0; 1,1 − t; 1,2)), t ∈ [0; 1,1]; Produktion 10 ME E₁, 15 ME E₂, 25 ME E₃
- gesucht: Bedarf an R₂ in Abhängigkeit von t grafisch; Erläuterung
- verfahren: Zwischenproduktbedarf mit B_t berechnen, R₂ nur über Z₂ mit Faktor 0,8, linearen Term zeichnen
- fehlerquelle: Bedarf über C statt über A · B_t berechnen (C gilt nur für t = 0,4)

### 2023MerhoehtBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: C ist nicht invertierbar
- gesucht: eine Bedeutung im Sachzusammenhang
- verfahren: Fehlende Inverse als fehlende eindeutige Rückrechnung deuten
- fehlerquelle: Aussage über die Hinrichtung (Bedarf berechnen) statt über die Rückrechnung

### 2018MerhoehtAAGLAA111-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Zustände A und B mit Anteilen a_n, b_n; Übergangstabelle: A → A 0,7, A → B 0,3, B → A 0, B → B 1; v_(n+1) = M · v_n
- gesucht: zugehöriges Übergangsdiagramm
- verfahren: Tabelleneinträge als Schleifen und Pfeile eintragen
- fehlerquelle: Zeilen und Spalten der Tabelle vertauschen (Pfeil B → A mit 0,3)

### 2018MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Zwei Baumärkte A und B: 70 % bzw. 80 % der Kunden kaufen im nächsten Monat wieder beim selben Baumarkt, die übrigen wechseln
- gesucht: Übergangsdiagramm für das Wechseln der Kunden von einem Monat zum nächsten
- verfahren: Zwei Knoten mit Schleifen 0,7 und 0,8, Pfeile mit 0,3 und 0,2
- fehlerquelle: Wechselanteile 0,3 und 0,2 vertauschen

### 2019MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: Tretbootverleih mit den Stationen N, S, W; Ausgaben a = (n; s; w), Rückgaben r = (n; s; w) je Tag; r = M · a mit M = (0,6 0,1 0,2 / 0,1 0,75 0,05 / 0,3 0,15 0,75)
- gesucht: Übergangsdiagramm zu r = M · a
- verfahren: Einträge spaltenweise als Pfeile eintragen
- fehlerquelle: Pfeilrichtung nach Zeilen statt Spalten

### 2021MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: Taxiunternehmen A, B, C; Kundenverteilung als Vektor (a; b; c); Übergang von Monat n zum nächsten v_(n+1) = M · v_n mit M = (0,1 0,1 0,7 / 0,3 0,8 0,2 / 0,6 0,1 0,1); M⁻¹ = 1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5); feste Gruppe von 7000 Kunden
- gesucht: Übergangsdiagramm der Kundenverteilung von einem Monat zum nächsten
- verfahren: Einträge der Matrix spaltenweise als Pfeile zwischen A, B, C eintragen
- fehlerquelle: Zeilen und Spalten vertauschen (A → C mit 0,7 statt 0,6)

### 2022MerhoehtBAGLAA1WTR-2a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: 4500 Lampen in Rot, Grün, Blau; v_{n+1} = N · v_n mit N = ((0,4; 0,2; 0,2), (0,3; 0,2; 0,5), (0,3; 0,6; 0,3)) (zeilenweise)
- gesucht: Übergangsdiagramm
- verfahren: Einträge n_ij als Pfeil von j nach i
- fehlerquelle: Zeilen als Abgänge lesen

### 2024MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: v_{n+1} = M · v_n mit M = ((0,7; 0,1; 0,2), (0,2; 0,8; 0,2), (0,1; 0,1; 0,6)); 900 E-Scooter in Bereichen A, B, C
- gesucht: Übergangsdiagramm
- verfahren: Matrixspalten als ausgehende Pfeile
- fehlerquelle: Zeilen statt Spalten als Herkunft

### 2024MerhoehtBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: v_{n+1} = P · v_n mit P = ((k; 0,4; 0,05), (0,8; 0; 0), (0; 0,6; 0,4)), k ≥ 0; Komponenten J, M, A
- gesucht: Übergangsdiagramm
- verfahren: Matrixspalten als ausgehende Pfeile
- fehlerquelle: Zeilen als Herkunft

### 2026MgrundlegendBAGLAA1MMS-1a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga-mms · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: 6000 Kunden in Gruppen A, B, C; v_{n+1} = P · v_n mit P = ((0,6; 0; 0), (0,3; 0,6; 0,2), (0,1; 0,4; 0,8)) (zeilenweise)
- gesucht: Übergangsdiagramm
- verfahren: Einträge p_ij als Übergang von Spalte j nach Zeile i als Pfeile zeichnen
- fehlerquelle: Zeilen und Spalten vertauscht

### 2026MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Zeichnen · antwort Grafik
- gegeben: v = (E; L; K) Eier, Larven, Käfer am Monatsanfang; v_(n+1) = P · v_n mit P = ((0; 0; 20), (0,6; 0; 0), (0; 0,4; 0,8))
- gesucht: Übergangsdiagramm
- verfahren: Matrixeinträge als Pfeile zwischen E, L, K eintragen
- fehlerquelle: Zeilen und Spalten vertauschen (Pfeil E → K mit 20)

### 2019MgrundlegendAAGLAA11-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 3 · format Kurzantwort · antwort Term
- gegeben: Vögel brüten jährlich in Gebiet A oder B; Übergangsdiagramm mit 0,9 (A bleibt), 0,1 (A → B), 0,2 (B → A), 0,8 (B bleibt)
- gesucht: Gleichung mit einer Matrix für die Änderung der Verteilung von einem Jahr zum nächsten und Bedeutung aller Variablen
- verfahren: Matrix aus dem Diagramm ablesen, Vektorgleichung aufstellen, Variablen benennen
- fehlerquelle: Matrix transponiert aufstellen (Zeilensumme 1)

### 2022MgrundlegendAAGLAA11-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Kurzantwort · antwort Text|Zahl
- gegeben: drei Stromanbieter A, B, C; Übergangsdiagramm je Quartal in der Abbildung; v_(n+1) = M · v_n mit Kundenzahlen (a_n; b_n; c_n); zwei Darstellungen I und II der Matrix mit Unbekannten x und y
- gesucht: die zutreffende Darstellung sowie x und y
- verfahren: erste Spalte mit den Abgängen von A vergleichen (0,4; 0,4; 0,2), fehlende Einträge aus dem Diagramm
- fehlerquelle: Zeilen und Spalten vertauschen (Darstellung II)

### 2022MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Kurzantwort · antwort Text|Zahl
- gegeben: Transportunternehmen mit 150 Fahrzeugen an den Standorten A, B, C; Verteilung (a; b; c) abends; Übergang v_(n+1) = M · v_n mit M = ((0,7; 0,5; 0,1), (0,2; 0,2; 0,6), (0,1; 0,3; 0,3)); Diagramme I und II mit Platzhaltern p und q
- gesucht: das passende Diagramm und die Werte von p und q
- verfahren: Einträge von M mit den Pfeilen vergleichen
- fehlerquelle: Zeilen statt Spalten als Abgänge lesen

### 2023MerhoehtAAGLAA112-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 1 · format Kurzantwort · antwort Term
- gegeben: Übergangsdiagramm; Modell v_(n+1) = M · v_n mit Vektoren (a; b; c) der Anteile auf A, B, C
- gesucht: zweite Zeile von M
- verfahren: Übergänge nach B ablesen: von A 1/2, von B 2/3, von C 0
- fehlerquelle: die Abgänge von B (Spalte) statt der Zugänge nach B (Zeile) angeben

### 2018MgrundlegendAAGLAA112-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: Vektor (J; H; E) für Jungtiere, heranwachsende und erwachsene Tiere; P = ((0; 0; 200), (0,05; 0; 0), (0; 0,1; 0)) je Jahr
- gesucht: Prozentsatz der Jungtiere, die das erste Lebensjahr nicht überleben
- verfahren: Übergangsanteil 0,05 ablesen, Gegenanteil bilden
- fehlerquelle: 5 % angeben (Überlebende statt Nichtüberlebende)

### 2019MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Tretbootverleih mit den Stationen N, S, W; Ausgaben a = (n; s; w), Rückgaben r = (n; s; w) je Tag; r = M · a mit M = (0,6 0,1 0,2 / 0,1 0,75 0,05 / 0,3 0,15 0,75)
- gesucht: Bedeutung des Eintrags 0,05 und der Spaltensummen 1
- verfahren: Eintrag nach Zeile und Spalte zuordnen, Spaltensumme als Rückgabe aller Boote deuten
- fehlerquelle: Zeile und Spalte vertauschen (an S ausgegeben, an W zurück)

### 2020MerhoehtAAGLAA11-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 1 · format Kurzantwort · antwort Text
- gegeben: Jungbäume J, mäßigtragende M, guttragende G; Übergangsdiagramm je Jahr in der Abbildung
- gesucht: Bedeutung der Zahlen 0,1 und 0,9 im Sachzusammenhang
- verfahren: Pfeile von G lesen
- fehlerquelle: Pfeilrichtung vertauschen (90 % der mäßigtragenden werden guttragend)

### 2022MerhoehtAAGLAA111-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 1 · format Kurzantwort · antwort Text
- gegeben: Vektoren (A; E; L) für ausgewachsene Insekten, Eier, Larven; v_(n+1) = M · v_n mit M = ((0,5; 0; 0,3), (30; 0; 0), (0; 0,2; 0)) je Woche
- gesucht: Bedeutung des Eintrags 0,2 im Sachzusammenhang
- verfahren: Position des Eintrags (Zeile L, Spalte E) deuten
- fehlerquelle: Zeile und Spalte vertauschen (20 % der Larven werden Eier)

### 2025MgrundlegendBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 1 · format Kurzantwort · antwort Text
- gegeben: v_{n+1} = M · v_n mit M = ((0; 0,1; 1,5), (0,4; 0; 0), (0; 0,9; 0,7)), Komponenten b (Babys), j (Jungtiere), e (erwachsene Tiere)
- gesucht: Bedeutung des Eintrags 0,9
- verfahren: Position in der Matrix deuten
- fehlerquelle: Eintrag als Anteil der Erwachsenen deuten (Zeile und Spalte vertauscht)

### 2025MerhoehtBAGLAA1WTR-1a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: v_{n+1} = M · v_n mit M = ((0,6; 0,1; 0), (0,3; 0,8; 0,5), (0,1; 0,1; 0,5)), Komponenten k, p, s (Kino, Premium, Sport); 3000 Kunden, Wechsel je Quartal
- gesucht: Bedeutung der Einträge 0 und 0,8
- verfahren: Positionen deuten
- fehlerquelle: 0 als Wechsel von K zu S lesen

### 2018MgrundlegendBAGLAA1WTR-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Kurzantwort · antwort Text|Zahl
- gegeben: Drei Baumärkte A, B, C; Kundenverteilung als Vektor (a; b; c), Übergang je Monat M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); im Sommermonat A 3700, B 5100, C 1200 Kunden
- gesucht: Baumarkt mit dem kleinsten Anteil wechselnder Kunden und dieser Anteil
- verfahren: Größten Diagonaleintrag suchen, Komplement bilden
- fehlerquelle: Spalten- und Zeilensummen verwechseln

### 2023MerhoehtAAGLAA112-c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Grenzmatrix zu M mit Zeilen (0,24; 0,24; 0,24), (0,36; 0,36; 0,36), (0,4; 0,4; 0,4)
- gesucht: Bedeutung der drei verschiedenen Einträge im Sachzusammenhang
- verfahren: Einträge als langfristige Anteile bzw. Wahrscheinlichkeiten je Feld lesen
- fehlerquelle: die Einträge als Übergangswahrscheinlichkeiten einer Runde deuten

### 2022MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Transportunternehmen mit 150 Fahrzeugen an den Standorten A, B, C; Verteilung (a; b; c) abends; Übergang v_(n+1) = M · v_n mit M = ((0,7; 0,5; 0,1), (0,2; 0,2; 0,6), (0,1; 0,3; 0,3)); Sonntagabend 20 Fahrzeuge in A, 60 in B, 70 in C
- gesucht: prozentualer Anteil der Fahrzeuge in A am Montagabend
- verfahren: Erste Zeile von M mit dem Vektor multiplizieren, durch 150 teilen
- fehlerquelle: Anzahl 51 statt Anteil abgeben

### 2018MgrundlegendBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Drei Baumärkte A, B, C; Kundenverteilung als Vektor (a; b; c), Übergang je Monat M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); im Sommermonat A 3700, B 5100, C 1200 Kunden; im Folgemonat hat A 3609 Kunden
- gesucht: Kundenzahlen von B und C im Folgemonat; prozentualer Anteil von C an allen Kunden
- verfahren: Zweite Matrixzeile auswerten, C als Rest zu 10 000, Anteil bilden
- fehlerquelle: C über die dritte Zeile mit Rundungsfehler statt als Rest berechnen (auch 1180)

### 2019MgrundlegendAAGLAA11-b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Übergangsdiagramm aus a; in einem Jahr brüten alle Vögel in A
- gesucht: prozentualer Anteil der Vögel, die zwei Jahre später in A brüten
- verfahren: beide Pfade A → A → A und A → B → A addieren (oder M² · (1; 0))
- fehlerquelle: Pfad über B vergessen (81 %)

### 2018MerhoehtAAGLAA112-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung · antwort Term
- gegeben: Zustände A und B; Diagramm: A bleibt 0,5, A → B 0,5, B → A 1; v_(n+1) = M · v_n
- gesucht: M²
- verfahren: M ablesen, M · M ausrechnen
- fehlerquelle: M transponiert ablesen

### 2018MerhoehtBAGLAA1WTR-2b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Indisches Springkraut: Zustand (S; P) mit Samen S und Pflanzen P; Frühjahr bis Herbst F · u mit F = ((f1; f2), (0; 0)), Herbst bis Frühjahr H · v mit H = ((0,3; 0), (0,01; 0)); Frühjahr zu Frühjahr J · u mit J = ((0,3; 150), (0,01; 5)); zu Frühjahrsbeginn 1000 Samen, keine Pflanzen
- gesucht: Samen und Pflanzen zu Beginn des nächsten und des übernächsten Frühjahrs
- verfahren: J zweimal anwenden
- fehlerquelle: im zweiten Schritt wieder vom Anfangszustand ausgehen

### 2018MgrundlegendAAGLAA112-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Rechnung|Kurzantwort · antwort Term
- gegeben: P = ((0; 0; 200), (0,05; 0; 0), (0; 0,1; 0)); v_(n+1) = P · v_n
- gesucht: P² und Bedeutung von P² · v_n
- verfahren: P · P ausrechnen, Produkt mit v_n als zwei Jahresschritte deuten
- fehlerquelle: Einträge elementweise quadrieren

### 2022MgrundlegendAAGLAA11-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Rechnung|Kurzantwort · antwort Zahl|Text
- gegeben: M aus a (erste Zeile 0,4; 0,1; 0,2; erste Spalte 0,4; 0,4; 0,2)
- gesucht: Eintrag der ersten Zeile und ersten Spalte von M²; Bedeutung der dritten Zeile von M²
- verfahren: erste Zeile mit erster Spalte multiplizieren; dritte Zeile als Zugänge nach C über zwei Quartale deuten
- fehlerquelle: Eintrag von M² als 0,4² rechnen

### 2022MgrundlegendBAGLAA1WTR-1e (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 5 · format Begründung|Rechnung · antwort Text
- gegeben: Transportunternehmen mit 150 Fahrzeugen an den Standorten A, B, C; Verteilung (a; b; c) abends; Übergang v_(n+1) = M · v_n mit M = ((0,7; 0,5; 0,1), (0,2; 0,2; 0,6), (0,1; 0,3; 0,3)); M² aus d; A₁: alle 150 in B am Dienstag ⇒ Donnerstag 32 % in B; A₂: keins in C am Dienstag ⇒ Donnerstag mindestens 24 % in B
- gesucht: Beurteilung beider Aussagen
- verfahren: A₁ mit der zweiten Zeile von M² nachrechnen; A₂ über 0,24a + 0,32b ≥ 0,24(a + b) begründen
- fehlerquelle: A₂ nur an einem Zahlenbeispiel prüfen; M statt M² verwenden

### 2021MgrundlegendBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Taxiunternehmen A, B, C; Kundenverteilung als Vektor (a; b; c); Übergang von Monat n zum nächsten v_(n+1) = M · v_n mit M = (0,1 0,1 0,7 / 0,3 0,8 0,2 / 0,6 0,1 0,1); M⁻¹ = 1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5); feste Gruppe von 7000 Kunden; im Mai hat A 2800, B 2400, C 1800 Kunden
- gesucht: Verteilung im April und prozentuale Abnahme der Kunden von C von April zu Mai
- verfahren: Maivektor mit M⁻¹ multiplizieren, Abnahme von C auf den Aprilwert beziehen
- fehlerquelle: Abnahme auf den Maiwert beziehen (94 %)

### 2018MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Kurzantwort · antwort Term
- gegeben: Drei Baumärkte A, B, C; Kundenverteilung als Vektor (a; b; c), Übergang je Monat M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); im Sommermonat A 3700, B 5100, C 1200 Kunden
- gesucht: Gleichungssystem für die Kundenzahlen im Monat vor dem Sommermonat
- verfahren: M · v = Sommerverteilung zeilenweise ausschreiben
- fehlerquelle: M auf die Sommerverteilung anwenden (Folgemonat statt Vormonat)

### 2018MerhoehtAAGLAA112-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: M² aus a
- gesucht: Verfahren, um aus v_(n+2) den Vektor v_n zu bestimmen
- verfahren: Inverse von M² bilden und anwenden
- fehlerquelle: durch M² „dividieren“ wollen oder M⁻¹ nur einmal anwenden

### 2025MerhoehtBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 6 · format Rechnung · antwort Zahl
- gegeben: 1/4 · ((7; −1; 1), (−2; 6; −6), (−1; −1; 9)) · M = E; zu Quartalsbeginn gleich viele Kunden mit K wie mit P
- gesucht: größtmögliche Anzahl der K-Kunden im vorausgegangenen Quartal
- verfahren: Verteilung parametrisieren, mit der Inversen zurückrechnen, Zulässigkeit als Ungleichungen, Maximum
- fehlerquelle: x = 1500 als Maximum nehmen (dann s im Vorquartal negativ)

### 2026MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Kurzantwort · antwort Text
- gegeben: v = (1000; 2000; 3000) Anfang April, z = (0; 0; 1000); Terme f = P · P · (v + z), g = P · P · v + z, h = P · (P · v + z); Anfang Mai werden 1000 Käfer hinzugefügt
- gesucht: welcher Term die Zusammensetzung Anfang Juni beschreibt und die Bedeutung eines anderen
- verfahren: Position der Zugabe zwischen den Matrixschritten deuten
- fehlerquelle: g wählen (Zugabe wird nicht mehr transformiert)

### 2019MgrundlegendBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Tretbootverleih mit den Stationen N, S, W; Ausgaben a = (n; s; w), Rückgaben r = (n; s; w) je Tag; r = M · a mit M = (0,6 0,1 0,2 / 0,1 0,75 0,05 / 0,3 0,15 0,75); an einem Dienstag an N 40 Ausgaben und 40 Rückgaben, Rückgaben an S 37, an W 63
- gesucht: Anzahl der an S ausgegebenen Boote
- verfahren: Gleichungssystem aus r = M · a aufstellen und nach s lösen
- fehlerquelle: Rückgabevektor als Ausgabevektor einsetzen

### 2023MerhoehtAAGLAA12-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Population (E; L; K) mit v_(n−1) = M⁻¹ · v_n, M⁻¹ = ((0; 1/b; 0), (0; 0; 1/c), (1/a; 0; 0)); (M⁻¹)² = ((0; 0; 3/c), (1/(60c); 0; 0), (0; 1/20; 0))
- gesucht: Wert von a
- verfahren: den Eintrag (2; 1) von (M⁻¹)² als Produkt 1/c · 1/a berechnen und mit 1/(60c) vergleichen
- fehlerquelle: die Matrix quadrieren wollen statt einen Eintrag zu berechnen

### 2022MerhoehtBAGLAA1WTR-2b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: 1000 Lampen blau; nach dem Wechsel je 1500 rot, grün, blau
- gesucht: Verhältnis rot zu grün vor dem Wechsel
- verfahren: Matrixgleichung mit Unbekannten r, g aufstellen, zwei Gleichungen lösen
- fehlerquelle: Gleichverteilung als 1500 vor dem Wechsel ansetzen

### 2018MgrundlegendBAGLAA1WTR-1h (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Matrix N wie in g; in einem Monat A 3556, B 5326, C 1118 Kunden, im Folgemonat C 1112 Kunden
- gesucht: zugehöriger Wert von p
- verfahren: Dritte Zeile von N auf den Vektor anwenden und gleich 1112 setzen
- fehlerquelle: die erste Zeile statt der dritten verwenden

### 2024MerhoehtBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Start 200 junge Tiere; nach zwei Jahren 66 junge Tiere
- gesucht: Wert von k
- verfahren: P² · v_0 berechnen, erste Komponente gleich 66
- fehlerquelle: k = −0,1 nicht verwerfen

### 2022MerhoehtAAGLAA111-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: zu Beginn 30 ausgewachsene Insekten, 10 Eier, L Larven; eine Woche später unverändert 30 ausgewachsene Insekten
- gesucht: Anzahl der Larven zu Beginn
- verfahren: erste Zeile von M · v = 30 nach L auflösen
- fehlerquelle: die Eier (Spalte E, Eintrag 0 in der A-Zeile) mit einrechnen

### 2021MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Taxiunternehmen A, B, C; Kundenverteilung als Vektor (a; b; c); Übergang von Monat n zum nächsten v_(n+1) = M · v_n mit M = (0,1 0,1 0,7 / 0,3 0,8 0,2 / 0,6 0,1 0,1); M⁻¹ = 1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5); feste Gruppe von 7000 Kunden; in einem Monat hat A 2000 Kunden
- gesucht: alle möglichen Anzahlen der Kunden von B im folgenden Monat
- verfahren: Anzahl von B im Folgemonat als Term in b aufstellen und b von 0 bis 5000 laufen lassen
- fehlerquelle: nur einen Beispielwert für b einsetzen

### 2024MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: am Ende eines Tages ein Drittel der 900 E-Scooter in A
- gesucht: Mindest- und Höchstzahl in A am Ende des nächsten Tages
- verfahren: Verteilung parametrisieren, a' als Term in b, Randwerte
- fehlerquelle: b und c unabhängig variieren (Summe 900 vergessen)

### 2019MgrundlegendBAGLAA1WTR-1f (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 4 · format Rechnung · antwort Term
- gegeben: Nebensaison nur Stationen N und S; Mittwoch: an N 15 Ausgaben und 8 Rückgaben, an S 10 Ausgaben und 17 Rückgaben
- gesucht: eine Matrix, die den Zusammenhang zwischen Ausgaben und Rückgaben darstellen kann
- verfahren: Matrix mit Spaltensummen 1 ansetzen, Gleichungssystem lösen, einen Parameter frei wählen
- fehlerquelle: die Spaltensummen nicht auf 1 setzen und vier Unbekannte erhalten

### 2018MgrundlegendBAGLAA1WTR-1g (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Nach Beginn von Rabattaktionen gilt die Matrix N = ((0,63; 0,18; 0,4 · (1 − p)), (0,27; 0,72; 0,6 · (1 − p)), (0,1; 0,1; p)), p ∈ [0; 1]; in einem Monat hat A 3650,38 − 470,6 · p und B 5467,27 − 705,9 · p Kunden, zusammen sind es 10 000
- gesucht: Bereich, in dem der prozentuale Anteil der Kunden von C in diesem Monat liegen kann
- verfahren: C = 10 000 − A − B = 882,35 + 1176,5p; linear in p, also Randwerte p = 0 und p = 1 einsetzen und durch 10 000 teilen
- fehlerquelle: den Anteil nur für einen p-Wert berechnen; Monotonie nicht begründen

### 2019MgrundlegendBAGLAA1WTR-1e (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 3 · format Rechnung|Begründung · antwort Text
- gegeben: Tretbootverleih mit den Stationen N, S, W; Ausgaben a = (n; s; w), Rückgaben r = (n; s; w) je Tag; r = M · a mit M = (0,6 0,1 0,2 / 0,1 0,75 0,05 / 0,3 0,15 0,75); Samstag: Ausgaben (a; b; a + b), Rückgaben (a + 2; b; c)
- gesucht: Nachweis von c = a + b − 2 und Deutung im Sachzusammenhang
- verfahren: Komponentensummen gleichsetzen; Differenz an W deuten
- fehlerquelle: die Gleichung über M · a ausrechnen wollen

### 2026MerhoehtAAGLAA11-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 1 · format Begründung · antwort Text
- gegeben: Population in drei Stadien A, B, C; Verteilung v_n = (A; B; C); Übergang von einem Tag zum nächsten v_(n+1) = M · v_n mit M = ((0; 0; 2), (r; 0; 0), (0; 0,6; 0)), r reell; v_0 ungleich Nullvektor; das abgebildete Übergangsdiagramm
- gesucht: Begründung, dass das Übergangsdiagramm fehlerhaft ist
- verfahren: Einträge der Matrix mit den Pfeilen vergleichen: M sagt A nach B mit r, B nach C mit 0,6, C nach A mit 2; im Diagramm sind die Pfeile zwischen A und C mit 2 und 0 vertauscht beschriftet
- fehlerquelle: Zeilen und Spalten der Matrix vertauscht lesen und das Diagramm für richtig halten

### 2017MerhoehtAAGLAA112-b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: Übergangsdiagramm aus a; zu Beginn 50 Ratten in R1, die anderen Räume leer; drei Abbildungen mit möglichen Verläufen der Anzahl in R1
- gesucht: die passende Abbildung mit Begründung
- verfahren: Erste Schritte durchrechnen: Zeitpunkt 1 alle in R2, Zeitpunkt 2 keine in R2 (35 in R1, 15 in R3), Zeitpunkt 3 keine in R1; nur Abbildung II zeigt 0 zum Zeitpunkt 3
- fehlerquelle: Abbildung I wählen, weil der Wert 35 zum Zeitpunkt 2 passt, ohne den Zeitpunkt 3 zu prüfen

### 2021MgrundlegendBAGLAA1WTR-1e (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Kurzantwort|Begründung · antwort Text
- gegeben: Taxiunternehmen A, B, C; Kundenverteilung als Vektor (a; b; c); Übergang von Monat n zum nächsten v_(n+1) = M · v_n mit M = (0,1 0,1 0,7 / 0,3 0,8 0,2 / 0,6 0,1 0,1); M⁻¹ = 1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5); feste Gruppe von 7000 Kunden; geändertes Wechselverhalten: der Bleibeanteil bei B sinkt, die zusätzlich wechselnden Kunden gehen je zur Hälfte zu A und C; die Wechselanteile von A und C bleiben, diese Kunden wechseln aber nicht mehr zu B; zur Auswahl P = (0,1 0,18 0,9 / 0 0,68 0 / 0,9 0,14 0,1) und Q = (0,1 0,18 0,9 / 0 0,64 0 / 0,9 0,18 0,1)
- gesucht: die Matrix, die das geänderte Wechselverhalten beschreibt, mit Begründung
- verfahren: Zweite Spalte beider Matrizen gegen die Bedingung „hälftig auf A und C“ prüfen
- fehlerquelle: nur die Nullen in der zweiten Zeile prüfen, die beide Matrizen erfüllen

### 2022MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 4 · format Begründung · antwort Text
- gegeben: Transportunternehmen mit 150 Fahrzeugen an den Standorten A, B, C; Verteilung (a; b; c) abends; Übergang v_(n+1) = M · v_n mit M = ((0,7; 0,5; 0,1), (0,2; 0,2; 0,6), (0,1; 0,3; 0,3)); Gleichung ((0; 0,5; 0,1), (0,2; 0; 0,6), (0,1; 0,3; 0)) · (20; 60; 70) = (a₁; b₁; c₁)
- gesucht: Deutung des Terms a₁ + b₁ + c₁ ohne Rechnung, mit Begründung
- verfahren: Matrix als M ohne Diagonale erkennen, Diagonale als Verbleib deuten
- fehlerquelle: Term als Gesamtzahl aller Fahrzeuge deuten

### 2023MerhoehtAAGLAA112-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Brettspiel mit drei Feldern, je Runde ein Würfelwurf je Figur; Übergangsdiagramm mit den Wahrscheinlichkeiten in der Abbildung
- gesucht: eine mögliche Spielregel (bezogen auf die Augenzahl) für eine Figur auf Feld B
- verfahren: 2/3 und 1/3 auf sechs Augenzahlen aufteilen
- fehlerquelle: die Pfeile von A nach B mitlesen (Regel für Figuren auf A)

### 2022MerhoehtAAGLAA111-c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 2 · format Kurzantwort · antwort Term
- gegeben: M für die Reihenfolge (A; E; L); neue Reihenfolge (E; L; A) mit w_(n+1) = N · w_n
- gesucht: Matrix N
- verfahren: jeden Übergang (Quelle → Ziel) an die neue Position schreiben
- fehlerquelle: nur die Zeilen, nicht die Spalten umsortieren

### 2019MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Tretbootverleih mit den Stationen N, S, W; Ausgaben a = (n; s; w), Rückgaben r = (n; s; w) je Tag; r = M · a mit M = (0,6 0,1 0,2 / 0,1 0,75 0,05 / 0,3 0,15 0,75); Aussage: werden an allen drei Stationen gleich viele Boote ausgegeben, so ist an W die Anzahl der Rückgaben 20 % höher als die der Ausgaben
- gesucht: Beurteilung der Aussage
- verfahren: Dritte Zeile von M mit (w; w; w) multiplizieren
- fehlerquelle: die Spalte W statt der Zeile W summieren (Summe 1)

### 2025MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: M wie in a; Aussage: sind im Jahr n dreimal so viele erwachsene Tiere wie Jungtiere, so gibt es im nächsten Jahr genauso viele erwachsene Tiere wie im Jahr n
- gesucht: Beurteilung der Aussage
- verfahren: dritte Zeile von M auf (x; y; 3y) anwenden
- fehlerquelle: mit konkreten Zahlen rechnen, ohne die Allgemeinheit zu zeigen

### 2021MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Taxiunternehmen A, B, C; Kundenverteilung als Vektor (a; b; c); Übergang von Monat n zum nächsten v_(n+1) = M · v_n mit M = (0,1 0,1 0,7 / 0,3 0,8 0,2 / 0,6 0,1 0,1); M⁻¹ = 1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5); feste Gruppe von 7000 Kunden; es gibt eine unveränderliche Verteilung mit 1600 Kunden von A
- gesucht: diese Verteilung
- verfahren: Erste Zeile von M · v = v mit a = 1600 und c = 5400 − b nach b lösen
- fehlerquelle: alle drei Gleichungen aufstellen und sich in der Auflösung verlieren

### 2025MerhoehtBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 5 · format Rechnung · antwort Text
- gegeben: M wie in a; 3000 Kunden; Verteilung, die sich nicht mehr ändert
- gesucht: ob dabei mehr als 60 % der Kunden P haben
- verfahren: Fixvektorgleichung mit s = 3000 − k − p, zwei Gleichungen lösen
- fehlerquelle: Fixvektor nur bis auf Vielfache bestimmen und die 3000 vergessen

### 2018MerhoehtAAGLAA111-c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 1 · format Kurzantwort · antwort Term
- gegeben: M aus der Übergangstabelle
- gesucht: eine Zustandsverteilung v mit M · v = v
- verfahren: Verteilung ganz in B wählen
- fehlerquelle: Gleichungssystem aufstellen und an 0,7a = a scheitern (a = 0)

### 2018MerhoehtAAGLAA111-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Übergangstabelle aus a; Startverteilung mit 0 < a_0 < 1 und 0 < b_0 < 1
- gesucht: Begründung, dass mit wachsendem n eine Koordinate von v_n kleiner und die andere größer wird
- verfahren: aus der Tabelle die Einbahnrichtung A → B ablesen
- fehlerquelle: nur mit Zahlenbeispielen rechnen, ohne die Richtung der Übergänge zu nennen

### 2019MerhoehtAAGLAA11-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Zustände A und B mit Anteilen a_n, b_n > 0 zum Zeitpunkt 0; Diagramm: A bleibt mit 1/2, A → B mit 1/2, B bleibt mit 1; M = ((1/2; 0), (1/2; 1))
- gesucht: Beschreibung der langfristigen Entwicklung der Verteilung mithilfe der Abbildung
- verfahren: Halbierung des A-Anteils je Schritt, B nimmt alles auf
- fehlerquelle: stationäre Verteilung mit beiden Anteilen größer null vermuten

### 2020MerhoehtAAGLAA11-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: v_(n+1) = A · v_n mit (J; M; G); Zusammensetzung mit k Jungbäumen, 300 mäßigtragenden und 180 guttragenden Bäumen bleibt unverändert
- gesucht: Werte von r, s und k
- verfahren: Matrix aufstellen, A · v = v zeilenweise lösen
- fehlerquelle: Zeilen und Spalten der Matrix vertauschen

### 2025MgrundlegendBAGLAA1WTR-1c (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: beobachtete, unveränderliche Population mit 500 Babys und 600 erwachsenen Tieren; neues Modell: nur der Eintrag für die Fortpflanzungsrate der erwachsenen Tiere (Zeile b, Spalte e) wird geändert
- gesucht: Wert des neuen Eintrags
- verfahren: M mit Unbekannter a, Fixvektorgleichung mit unbekanntem j, Gleichungssystem lösen
- fehlerquelle: falschen Eintrag ändern (0,7 statt 1,5) oder j unbekannt lassen

### 2026MgrundlegendBAGLAA1MMS-1e (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Es gibt eine unveränderliche Verteilung mit viermal so vielen Kunden in C wie in B; Übergangsrate B → C wird angepasst, andere Raten zwischen verschiedenen Gruppen unverändert
- gesucht: Übergangsrate von B nach C im angepassten Modell
- verfahren: Angepasste Matrix mit x und 1 − x, Fixvektor (6000 − 5b; b; 4b) ansetzen, Gleichungssystem lösen
- fehlerquelle: Verbleibrate von B nicht auf 1 − x anpassen

### 2018MerhoehtBAGLAA1WTR-2c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 4 · format Rechnung|Begründung · antwort Text
- gegeben: Indisches Springkraut: Zustand (S; P) mit Samen S und Pflanzen P; Frühjahr bis Herbst F · u mit F = ((f1; f2), (0; 0)), Herbst bis Frühjahr H · v mit H = ((0,3; 0), (0,01; 0)); Frühjahr zu Frühjahr J · u mit J = ((0,3; 150), (0,01; 5)); zu Frühjahrsbeginn Samen und Pflanzen vorhanden
- gesucht: ob die Pflanzenzahl bis zum nächsten Frühjahr unverändert bleiben kann
- verfahren: Zweite Zeile von J · (S; P) = (…; P) nach S auflösen
- fehlerquelle: beide Komponenten konstant fordern (Fixvektor)

### 2018MgrundlegendBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Zwei Baumärkte A und B: 70 % bzw. 80 % der Kunden kaufen im nächsten Monat wieder beim selben Baumarkt, die übrigen wechseln; in einem Monat hat A 4000 und B 6000 Kunden
- gesucht: Anzahl der Wechsler je Baumarkt im Folgemonat mit Deutung
- verfahren: 0,3 · 4000 und 0,2 · 6000 berechnen und vergleichen
- fehlerquelle: die Bleibenden statt der Wechsler berechnen

### 2018MerhoehtBAGLAA1WTR-2d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 7 · format Rechnung · antwort Zahl
- gegeben: Indisches Springkraut: Zustand (S; P) mit Samen S und Pflanzen P; Frühjahr bis Herbst F · u mit F = ((f1; f2), (0; 0)), Herbst bis Frühjahr H · v mit H = ((0,3; 0), (0,01; 0)); Frühjahr zu Frühjahr J · u mit J = ((0,3; 150), (0,01; 5)); zu Frühjahrsbeginn wird ein Anteil der Pflanzen entfernt, sodass der Zustand zum nächsten Frühjahr mit dem vor dem Entfernen übereinstimmt
- gesucht: Anteil der zu entfernenden Pflanzen in Prozent
- verfahren: J · (S; P4) = (S; P3) als Gleichungssystem, S eliminieren, P4/P3 = 7/50
- fehlerquelle: Fixvektor von J suchen (existiert nicht)

### 2018MgrundlegendAAGLAA112-c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Kurzantwort · antwort Text
- gegeben: P³ = E (Einheitsmatrix)
- gesucht: Deutung im Sachzusammenhang
- verfahren: P³ · v = v als Rückkehr zur Ausgangszusammensetzung nach drei Jahren deuten
- fehlerquelle: „die Population bleibt konstant“ (auch die Zwischenjahre) behaupten

### 2019MgrundlegendAAGLAA12-b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 4 · format Kurzantwort · antwort Text
- gegeben: M aus a; M³ = a/8 · E (Einheitsmatrix mit Faktor a/8)
- gesucht: Deutung der Gleichung im Sachzusammenhang und langfristige Entwicklung der Population in Abhängigkeit von a
- verfahren: Faktor a/8 je drei Monate deuten, drei Fälle a < 8, a = 8, a > 8
- fehlerquelle: nur „Faktor a/8“ nennen, ohne die Fälle zu unterscheiden

### 2019MerhoehtAAGLAA11-b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: M = ((1/2; 0), (1/2; 1)); Term M · (a_n; b_n); Anteil in A soll bis zum Zeitpunkt n auf weniger als 10 % des Anfangswerts abnehmen
- gesucht: kleinster solcher Wert von n
- verfahren: aus M · v den Faktor 1/2 für a_n ablesen, Potenzen mit 0,1 vergleichen
- fehlerquelle: n = 3 angeben (1/8 ist nicht kleiner als 1/10)

### 2024MerhoehtBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: andere Population mit Matrix Q; Größe = Summe aller Tiere
- gesucht: nach wie vielen Jahren die Größe erstmals unter 20 % des Anfangswerts liegt
- verfahren: Faktor 0,9 je Jahr, Exponentialungleichung
- fehlerquelle: 15 statt 16 (nicht aufrunden)

### 2021MgrundlegendBAGLAA1WTR-1f (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 4 · format Kurzantwort|Rechnung · antwort Text|Zahl
- gegeben: Taxiunternehmen A, B, C; Kundenverteilung als Vektor (a; b; c); Übergang von Monat n zum nächsten v_(n+1) = M · v_n mit M = (0,1 0,1 0,7 / 0,3 0,8 0,2 / 0,6 0,1 0,1); M⁻¹ = 1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5); feste Gruppe von 7000 Kunden; geändertes Wechselverhalten: der Bleibeanteil bei B sinkt, die zusätzlich wechselnden Kunden gehen je zur Hälfte zu A und C; die Wechselanteile von A und C bleiben, diese Kunden wechseln aber nicht mehr zu B; zur Auswahl P = (0,1 0,18 0,9 / 0 0,68 0 / 0,9 0,14 0,1) und Q = (0,1 0,18 0,9 / 0 0,64 0 / 0,9 0,18 0,1); ab der Änderung nimmt die Kundenzahl von B stetig ab
- gesucht: wie sich die Abnahme in der gewählten Matrix zeigt; Monat, in dem die Kundenzahl von B erstmals unter 1 % des Werts unmittelbar vor der Änderung liegt
- verfahren: Zweite Zeile von Q deuten (nur 0,64 · b, keine Zugänge), 0,64ⁿ < 0,01 nach n lösen
- fehlerquelle: n = 10 angeben (dort noch 1,15 %)

### 2026MgrundlegendBAGLAA1MMS-1d (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga-mms · punkte 4 · format Begründung|Rechnung · antwort Zahl
- gegeben: P wie in a; Anzahl in A erstmals unter zwei Prozent des Anfangswerts
- gesucht: Begründung der Abnahme um 40 %; Anzahl der vergangenen Jahre
- verfahren: Erste Zeile von P deuten, 0,6ⁿ < 0,02 lösen und aufrunden
- fehlerquelle: n = 7 statt 8 (erstmals unterschritten)

### 2026MgrundlegendBAGLAA1WTR-1d (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: v0 = (10000; 3000; K0), P · v0 = r · v0 mit K0 natürlich und r > 1
- gesucht: r und K0
- verfahren: Gleichungssystem aus den Komponenten lösen
- fehlerquelle: dritte Gleichung als Widerspruch lesen statt als Probe

### 2026MgrundlegendBAGLAA1WTR-1e (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: P · v0 = r · v0 mit r = 2 (aus d); Punkte (n | K_n); Kurven I (fallend), II (linear), III (exponentiell)
- gesucht: die Kurve, auf der die Punkte liegen, mit Begründung
- verfahren: K_n = K0 · r^n herleiten, Wachstumsart benennen
- fehlerquelle: Kurve II wählen (Zunahme, aber linear gedacht)

Nur außerhalb von „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ genannt, nicht aufgenommen: 2022MerhoehtAAGLAA112-a, 2018MgrundlegendBAGLAA1WTR-1f

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
