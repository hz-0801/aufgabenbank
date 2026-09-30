# Mappe: binomialverteilung

Eintrag: hz-0801/mathe-nachhilfe, katalog/binomialverteilung.md
Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19 (2026-09-30T08:03:34Z, „Katalog: Vorschläge vom 30.09. eingesetzt (24 Zeilen in 17 Einträgen, Marke „kein P10-Stoff“ in _vorlage.md)“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:05 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Binomialverteilung
  3
  4  ### Verortung
  5  Die Anzahl der Treffer bei n unabhängigen Wiederholungen eines Zufallsexperiments mit zwei Ausgängen: Bernoulli-Experiment und Bernoulli-Kette erkennen, die Bernoulli-Formel für Einzelwahrscheinlichke … (gekürzt, 2632 Zeichen)
  6  [GOST] Q2, 2. Kurshalbjahr „Analysis; Stochastik“ (BB S. 26–28), Grund- und Leistungskursfach: L4/L5-Zeile „die Binomialverteilung und ihre Kenngrößen nutzen und die Binomialverteilung zur Beschreibun … (gekürzt, 4081 Zeichen)
  7  [FOS] Kap. 3 Leitidee L5 (S. 24): „Wahrscheinlichkeiten von (mehrstufigen) Zufallsversuchen berechnen“, „den Erwartungswert einer Zufallsvariablen ermitteln“; Kap. 4 Pflichtthema 4 „Stochastik“ (S. 28 … (gekürzt, 860 Zeichen)
  8  [LS-AA] Einführungsphase Kapitel V „Schlüsselkonzept: Binomialverteilung“: 1 Bernoulli-Experimente · 2 Binomialkoeffizienten · 3 Die Formel von Bernoulli · 4 Die Binomialverteilung – Erwartungswert ·  … (gekürzt, 2770 Zeichen)
  9
 10  ### Lerneinheiten
 11  1. Bernoulli-Experiment und Bernoulli-Kette – das Modell erkennen: genau zwei Ausgänge (Treffer mit p, Niete mit 1 − p), feste Anzahl n, gleichbleibendes p, Unabhängigkeit; die Zufallsgröße X „Anzahl  … (gekürzt, 703 Zeichen)
 12    Marken: BE Q4 · BB Q2 · GK · Abitur GK · Abitur LK
 13  2. Bernoulli-Formel – Einzelwahrscheinlichkeit P(X = k): der Binomialkoeffizient als Anzahl der Anordnungen der k Treffer unter n Versuchen (Taste nCr), Potenzen p^k und (1 − p)^(n − k); Term angeben  … (gekürzt, 646 Zeichen)
 14    Marken: BE Q4 · BB Q2 · GK · Abitur GK · Abitur LK
 15  3. Kumulierte Wahrscheinlichkeiten – höchstens, mindestens, Intervall: den Wortlaut in P(X ≤ k) übersetzen („weniger als“, „mehr als“, „mindestens … und höchstens …“), Gegenereignis 1 − P(X ≤ k − 1),  … (gekürzt, 934 Zeichen)
 16    Marken: BE Q4 · BB Q2 · GK · Abitur GK · Abitur LK
 17  4. Umkehraufgaben – n, p oder k gesucht: „Dreimal-mindestens“ über das Gegenereignis, 1 − (1 − p)^n ≥ Schranke, Logarithmieren mit Umkehr des Ungleichheitszeichens und Aufrunden; Trefferwahrscheinlich … (gekürzt, 919 Zeichen)
 18    Marken: BE Q4 · BB Q2 · GK · Abitur GK · Abitur LK
 19  5. Verteilung im Diagramm – die Gestalt der Binomialverteilung: Säulenhöhe als P(X = k), Summe aller Säulen 1, Wertebereich 0 bis n; Erwartungswert μ = n · p als Lage der höchsten Säule (Modalwert), V … (gekürzt, 911 Zeichen)
 20    Marken: BE Q4 · BB Q2 · GK · Abitur GK · Abitur LK
 21  Niveaustufung: fhr = kein Stoff; GK = alle fünf Einheiten (der RLP GOST kennt für dieses Thema keinen LK-Zusatz); LK = dieselben fünf Einheiten auf erhöhtem Anforderungsniveau – längere Verkettungen (Einheit 3 Prüfungshöhe), algebraische Umkehraufgaben ohne Rechner (Einheit 4: 2025MerhoehtAStochastik21, 2019MerhoehtAStochastik11-b) und allgemeine Widerlegungen (2022-bebb-lk-B4f); die GK/LK-Grenze kommt hier allein aus dem Niveau der Poolzeilen, nicht aus dem Plan (Formbefund, siehe Offene Punkte).
 22
 23  ### Typen je Lerneinheit
 24  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
 25  Einheit 1: Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen (3) — Nachweis: Ungeeignetheit des Binomialmodells begründen (4) · Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen (3) · Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen (2) — Deutung: Aussagen über Bernoulli-Experiment und Bernoulli-Kette im Sachzusammenhang beurteilen (1) · Zufallsgröße mit gleicher Binomialverteilung in einem anderen Experiment angeben (1). Dazu: Fehler finden (Binomialverteilung bejaht, weil es nur zwei Ausgänge gibt, obwohl ohne Zurücklegen aus einer kleinen Gesamtheit gezogen wird; bei zwei Versuchen nur einen Pfad gerechnet; die Unabhängigkeit nicht genannt) · Begründen (warum eine große Gesamtheit das Zurücklegen ersetzt; warum ein Spiel mit drei möglichen Ausgängen keine Bernoulli-Kette liefert).
 26  Einheit 2: Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln (18) · Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen (13; Ermessen, siehe Offene Punkte) · Einzelwahrscheinlichkeit einer Binomialverteilung aus n und Erwartungswert berechnen (1) · Stichprobenumfang aus dem Erwartungswert berechnen und Einzelwahrscheinlichkeit ermitteln (1) — Deutung: Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben (7). Dazu: Fehler finden (Binomialkoeffizient weggelassen, nur das Produkt der Einzelwahrscheinlichkeiten; Exponenten von p und 1 − p vertauscht; Trefferdefinition beim Zählen der Nieten nicht mitgewechselt; kumulierte statt Einzelwahrscheinlichkeit am Rechner) · Begründen (warum jeder Pfad mit k Treffern dieselbe Wahrscheinlichkeit hat; warum die Potenz für „alle Treffer“ keinen Binomialkoeffizienten braucht).
 27  Einheit 3: Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln (23) · Wahrscheinlichkeit für eine Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden (3) · Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen (2) · Wahrscheinlichkeit einer prozentualen Abweichung vom Erwartungswert nach beiden Seiten berechnen (2) · Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen (2) · Wahrscheinlichkeit für zwei gleichzeitige Ereignisse über die Aufteilung einer Bernoulli-Kette in zwei Abschnitte berechnen (2) · Bedingte Restwahrscheinlichkeit nach bekannten Ergebnissen über die Binomialverteilung berechnen (1) · Kumulierte Binomialwahrscheinlichkeit und Pfadwahrscheinlichkeit einer festen Anfangsfolge berechnen (1) · Wahrscheinlichkeit eines zweistufigen Prüfplans über Binomialwahrscheinlichkeiten berechnen (1) · Wahrscheinlichkeit für zwei unabhängige Spieler als Produkt binomialer Wahrscheinlichkeiten berechnen (1) — Nachweis: Summenbedingung bei wiederholtem Wurf in eine Binomialwahrscheinlichkeit übersetzen und nachweisen (1) · Summenterme der Binomialverteilung auf ein vorgegebenes Mindestens-Ereignis prüfen und begründen (1) — Deutung: Kumulierte Binomialsumme als Sachaussage formulieren (14) · Sachaussage zu einer Ungleichung mit Binomialsumme formulieren (2) · Aufgabenstellung zu einer Potenz der Gegenwahrscheinlichkeit formulieren und Ansatz erläutern (1). Dazu: Fehler finden („mehr als k“ als X ≥ k gelesen; „weniger als k“ als P(X ≤ k); beim Intervall die falsche untere Grenze abgezogen; ein Prozentanteil als Anzahl genommen; im Summenterm Treffer und Niete vertauscht; die Summe als „genau k“ gedeutet) · Begründen (warum „mindestens k“ über das Gegenereignis „höchstens k − 1“ läuft; warum sich eine Anteilsbedingung erst in eine ganze Zahl übersetzen lässt).
 28  Einheit 4: Anzahl von Versuchen einer Bernoulli-Kette für mindestens einen Treffer über das Gegenereignis bestimmen (10) · Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln (9) · Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen (4) · Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln (3) · Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln (3) · Kleinste Umgebungsbreite unterhalb des Erwartungswerts für eine Mindestwahrscheinlichkeit ermitteln (1) · Parameter n und p aus einem Verhältnis zweier Einzelwahrscheinlichkeiten und dem Erwartungswert berechnen (1; Ermessen, siehe Offene Punkte) · Stichprobenumfang zu einer vorgegebenen Einzelwahrscheinlichkeit mit dem Rechner suchen (1) · Trefferwahrscheinlichkeit aus einer Gleichung zweier Einzelwahrscheinlichkeiten berechnen (1; Ermessen, siehe Offene Punkte) · Trefferwahrscheinlichkeit aus einer kumulierten Wahrscheinlichkeit auf ganze Prozent durch Probieren ermitteln (1) · Trefferzahlen mit einer Einzelwahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln (1; Ermessen, siehe Offene Punkte) — Nachweis: Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen (2) · Behauptung zur Monotonie einer Wahrscheinlichkeit an Beispielwerten prüfen (1) — Deutung: Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen (2) · Wirkung eines kleineren Stichprobenumfangs auf eine Annahmewahrscheinlichkeit ohne Rechnung beurteilen (1). Dazu: Fehler finden (beim Teilen durch einen negativen Logarithmus das Ungleichheitszeichen nicht gedreht; abgerundet statt aufgerundet; die n-te Wurzel als Division durch n; die Grenze k ohne den zweiten Nachbarwert angegeben; n aus n · p = μ statt durch Probieren) · Begründen (warum (1 − p)^n mit wachsendem n fällt; warum ein Wert, der die Schranke gerade nicht erreicht, mit belegt werden muss).
 29  Einheit 5: Modalwert einer Binomialverteilung bestimmen (5) · Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen (3; Ermessen, siehe Offene Punkte) · Achsen eines Verteilungsdiagramms über Erwartungswert und größte Einzelwahrscheinlichkeit skalieren (1) · Einzelwahrscheinlichkeit aus dem Diagramm kumulierter Wahrscheinlichkeiten ermitteln (1) · Obere Grenze einer im Diagramm markierten kumulierten Wahrscheinlichkeit über den Erwartungswert ermitteln (1) · Wahrscheinlichkeit eines symmetrischen Intervalls über die Symmetrie der Binomialverteilung berechnen (1) — Nachweis: Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen (5) · Aussage über eine Summe von Wahrscheinlichkeiten am Säulendiagramm entscheiden (1) · Binomialverteilung über den Widerspruch zwischen Symmetrie und einer Einzelwahrscheinlichkeit ausschließen (1; Ermessen, siehe Offene Punkte) — Deutung: Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen (4) · Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern (4) · Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen (2) · Wahrscheinlichkeit eines Intervalls aus dem Säulendiagramm einer Verteilung ablesen (2) · Aussagen über Verteilungen verschiedener Gruppen am Säulendiagramm beurteilen (1) · Aussagen über kumulierte Wahrscheinlichkeit und Trefferwahrscheinlichkeit aus dem Säulendiagramm einer Binomialverteilung beurteilen (1) · Bedingung an p für das Verhältnis zweier symmetrisch liegender Einzelwahrscheinlichkeiten angeben (1) · Verteilung der Gegenzufallsgröße im Diagramm darstellen (1). Dazu: Fehler finden (das Maximum bei n/2 statt bei n · p vermutet; ein Diagramm nur nach der Form beurteilt, ohne die Summe der Säulen zu prüfen; bei der Gegenzufallsgröße die Säule bei k statt bei n − k gelesen; die Symmetrieachse auf eine ganze Zahl statt auf die Mitte zweier Werte gelegt; Wertebereich mit n + 1 Werten als n gelesen) · Begründen (warum die Säulen sich zu eins addieren müssen; warum die Verteilung nur für p = 0,5 symmetrisch ist).
 30  Zählung: 6 + 5 + 15 + 15 + 17 = 58 Haupttypen, 14 + 40 + 57 + 41 + 35 = 187 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: CAS-Nachtrag 2017, Heft 2017-be-gk, Pool 2017 grundlegend Teil A und B, erhöht Teil B, WTR und CAS; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2018 erhöht und 2017 grundlegend Teil B CAS, Berliner CAS-Hefte 2017/2018 GK) samt den Typumbenennungen der Abgleichläufe 27/28).
 31
 32  ### Voraussetzungen (Blatt 0)
 33  Fertigkeiten (je Zeile: was, wofür):
 34  - Baumdiagramm und Pfadregeln mit Zurücklegen: Produkt entlang des Pfades, Summe über mehrere Pfade, „mindestens einmal“ über das Gegenereignis – Grundlage der Bernoulli-Kette und der Formel, Einheit 1 und 2, das Gegenereignis auch in Einheit 3 und 4. Thema wahrscheinlichkeit.md (Sek I, Einheit 3). [GOST Eingangsvoraussetzung L5 „bestimmen Wahrscheinlichkeiten mithilfe der Laplace-Regel, Baumdiagrammen sowie Pfadregeln und wenden diese an“; RLP G „Baumdiagrammen, Pfadregeln, Vierfeldertafeln, Gegenwahrscheinlichkeiten und dem Urnenmodell“; LS-AA Kl. 8 VIII 3–4]
 35  - Ziehen mit und ohne Zurücklegen unterscheiden (Urnenmodell): bleibt p gleich oder ändert es sich von Zug zu Zug – für die Bernoulli-Bedingung in Einheit 1. Thema wahrscheinlichkeit.md Einheit 4; Gegenstück hypergeometrische-verteilung.md. [GOST Q2 L5 „Zufallsexperimente mit nur zwei möglichen Ausgängen im Urnenmodell: Ziehen ohne Zurücklegen, Ziehen mit Zurücklegen“; RLP G „mit und ohne Zurücklegen“]
 36  - Binomialkoeffizient (n über k) als Anzahl der Auswahlen von k aus n, mit der Rechnertaste nCr und für kleine Zahlen im Kopf; Fakultät – Anzahl der Anordnungen in der Bernoulli-Formel, Einheit 2, und beim Lesen von Summentermen in Einheit 3. Sek-II-Nachbarthema kombinatorik.md Einheit 2 (Binomialkoeffizient mit Eigenschaften) und Einheit 1 (Fakultät). [GOST Eingangsvoraussetzung L5 „nutzen Binomialkoeffizienten und Fakultäten zur Berechnung von Wahrscheinlichkeiten in Anwendungskontexten“; RLP H „Bestimmen von Anzahlen mithilfe von Fakultäten und Binomialkoeffizienten“; GOST-OHiMi 2.4 Kombinationen ohne Wiederholung mit Eigenschaften; FS-IQB 1.4 Binomialkoeffizient]
 37  - Potenzen mit einer Basis zwischen null und eins: sie werden mit wachsendem Exponenten kleiner; Potenzgesetz für das Produkt gleicher Basen; n-te Wurzel als Umkehrung des Potenzierens; Exponentialgleichung durch Logarithmieren lösen, Logarithmus einer Zahl unter eins ist negativ – Einheit 4 und die Aussagen über die Abhängigkeit von n. Themen potenz-exponentialfunktionen.md (Sek I, Logarithmus als Vorrat), reelle-zahlen.md (Potenz- und Wurzelgesetze), gleichungen-loesen.md (Sek II, einfache Exponentialgleichungen). [GOST Eingangsvoraussetzung L4 „verwenden Prozentdarstellungen, Potenzen, Wurzeln und Logarithmen zur Lösung inner- und außermathematischer Probleme“; GOST-OHiMi 2.1 „Logarithmen“, „einfache Exponentialgleichungen“; FS-IQB 1.1 Potenzen und Logarithmen]
 38  - Anteile, Prozente und Anzahlen ineinander umrechnen und eine Ungleichung nach der gesuchten Größe umformen (Ungleichheitszeichen dreht beim Teilen durch eine negative Zahl), Ergebnis nach dem Sinn auf- oder abrunden – Einheit 3 und 4. Themen prozentrechnung.md, lineare-gleichungen.md (Sek I). [RLP E–F Prozentrechnung; GOST Eingangsvoraussetzung L4 „Prozentdarstellungen“; GOST-OHiMi 2.1 Gleichungen]
 39  - Säulendiagramm lesen (Höhe am Gitter ablesen, Säulen addieren) und zeichnen; Summenzeichen lesen (untere und obere Grenze, Laufvariable) – Einheit 3 und 5. Thema daten.md (Sek I, Diagramme lesen und beurteilen). [GOST Eingangsvoraussetzung L5 „Säulen- und Kreisdiagramme“; GOST-OHiMi 2.4 „Darstellung von Zufallsgrößen in Histogrammen“; IQB-VER 1 „mit der Summenschreibweise unter Verwendung des Symbols Σ umgehen können“]
 40  - Erwartungswert μ = n · p berechnen und als mittlere Trefferzahl deuten – Lage des Maximums und Mitte einer Umgebung, Einheit 4 und 5. Nachbarthema kenngroessen-von-verteilungen.md (dasselbe Kurshalbjahr; im Lehrwerk EP V 4 Teil desselben Kapitels). [GOST Q2 L2 „Erwartungswert und Standardabweichung diskreter Zufallsgrößen bestimmen und deuten“, L4/L5 „Kenngrößen von Wahrscheinlichkeitsverteilungen: Erwartungswert“; GOST-OHiMi 2.4 „Erwartungswert von Zufallsgrößen“; FS-IQB 1.4 μ = n · p]
 41  - Rechnerfunktionen für die Binomialverteilung (Einzelwahrscheinlichkeit und kumulierte Wahrscheinlichkeit, je nach Gerät binompdf und binomcdf) bedienen oder die Tabelle der summierten Binomialverteilung lesen (Spalte p, Zeile k; bei p über ein Halb Treffer und Niete tauschen) – Werkzeug für Einheit 2 bis 5, Prüfungsteil B. **Ermessen:** keine amtliche Eingangsvoraussetzung nennt die Rechnerbedienung; gesetzt, weil vierunddreißig Zeilen der Rohdatei den Rechner voraussetzen (Typen „… mit dem Rechner ermitteln“) und Berlin vom Taschenrechner verlangt, dass „Werte der Binomialverteilungen ermittelt werden können“ (abitur-vokabular.md, Abschnitt Geltung, Anmerkung). [Ermessen; Rohdatei; abitur-vokabular.md Abschnitt Geltung]
 42  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 43  - „Treffer oder Niete gezählt?“ – bei Summentermen und Diagrammen ankreuzen, ob p den Treffer oder die Niete des Sachzusammenhangs meint und ob X oder n − X gezählt wird; nichts rechnen. Vor Einheit 3 und 5. [Rohdatei-Fehlerquelle „Erfolg und Misserfolg vertauscht“; iqb 2020MgrundlegendBStochastikWTR2-1c, 2024MerhoehtBStochastikWTR2-1d, 2024MerhoehtAStochastik23-a; abi 2026-bb-gk-B4c]
 44
 45  ### Merkkasten
 46  Einheit 1 (Bernoulli-Experiment und Bernoulli-Kette):
 47      Bernoulli-Experiment: ein Zufallsexperiment mit genau zwei Ausgängen – Treffer mit der Wahrscheinlichkeit p, Niete mit 1 − p.
 48      Bernoulli-Kette der Länge n: dasselbe Bernoulli-Experiment n-mal hintereinander, unabhängig und mit demselben p. Die Anzahl der Treffer X heißt dann binomialverteilt mit den Parametern n und p, kurz X ~ B(n; p).
 49        Ein Würfel wird viermal geworfen, Treffer ist „Sechs“: n = 4, p = 1/6.
 50        Aus 10 Kugeln werden 3 ohne Zurücklegen gezogen: p ändert sich von Zug zu Zug – keine Bernoulli-Kette (hypergeometrische Verteilung).
 51      Prüfliste: zwei Ausgänge? feste Anzahl n? p immer gleich (mit Zurücklegen oder Gesamtheit sehr groß)? Versuche unabhängig? Erst wenn alles „ja“ ist, gilt das Binomialmodell.
 52      Kleine Ketten am Baum: genau ein Treffer bei zwei Versuchen hat zwei Pfade, TN und NT, also P = 2 · p · (1 − p).
 53        p = 0,3: P(genau ein Treffer) = 2 · 0,3 · 0,7 = 0,42.
 54      Auswendig (Teil A): „Bernoulli-Experiment“, „Bernoulli-Kette“ mit der „Prüfliste“ und „Kleine Ketten am Baum“ – [GOST-OHiMi 2.4] „Ansätze zur Berechnung von Wahrscheinlichkeiten für binomialverteilte … Zufallsgrößen“, „Baumdiagramm, Pfadregeln“; die Schreibweise X ~ B(n; p) ist Konvention.
 55      Formelsammlung: Stochastik [FS-IQB 1.4] führt Binomialkoeffizient, Bernoulli-Formel, μ und σ; eine Definition von Bernoulli-Experiment und Bernoulli-Kette steht nicht darin – [FS] Abgleich am PDF offen
 56  Quelle: eigene Formulierung nach [GOST Q2 L4/L5] „Bernoulli-Experiment“, „Bernoulli-Kette“, „Ziehen mit Zurücklegen (Binomialverteilung)“ und [GOST-OHiMi 2.4] „Baumdiagramm, Pfadregeln“; Zahlenbeispiele eigen (Ermessen); [LS-AA EP V 1].
 57
 58  Einheit 2 (Bernoulli-Formel):
 59      P(X = k) = (n über k) · p^k · (1 − p)^(n − k): der Binomialkoeffizient zählt, auf wie viele Arten die k Treffer auf die n Versuche verteilt sein können (Taste nCr); jeder dieser Pfade hat die Wahrscheinlichkeit p^k · (1 − p)^(n − k).
 60        n = 5, p = 0,3, k = 2: P(X = 2) = (5 über 2) · 0,3² · 0,7³ = 10 · 0,09 · 0,343 ≈ 0,3087.
 61      Sonderfälle ohne Binomialkoeffizient: kein Treffer (1 − p)^n, alle Treffer p^n.
 62        n = 5, p = 0,3: P(X = 0) = 0,7⁵ ≈ 0,168; P(X = 5) = 0,3⁵ ≈ 0,0024.
 63      Term angeben heißt: den Term hinschreiben, nicht ausrechnen – Prüfungsteil A.
 64        n = 8, p = 1/4, k = 3: P(X = 3) = (8 über 3) · (1/4)³ · (3/4)⁵.
 65      Rechner: die Funktion für die Einzelwahrscheinlichkeit (binompdf) mit n, p und k.
 66      Auswendig (Teil A): die Bernoulli-Formel (erste Zeile), „Sonderfälle ohne Binomialkoeffizient“ und „Term angeben“ – [GOST-OHiMi 2.4] „Binomialverteilung: P(X = k) = …“ und „Kombinationen ohne Wiederholung“ mit den Eigenschaften des Binomialkoeffizienten; „Rechner“ nicht (Hilfsmittel, Teil B).
 67      Formelsammlung: Stochastik – Binomialverteilung [FS-IQB 1.4] „Für eine binomialverteilte Zufallsgröße X gilt: P(X = k) = (n über k) · p^k · (1 − p)^(n−k)“ und Binomialkoeffizient (n über k) = n! / (k! · (n − k)!); die Anlage ohne Hilfsmittel [GOST-OHiMi 2.4] verlangt die Formel auswendig – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 68  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] Bernoulli-Formel und Eigenschaften des Binomialkoeffizienten, [GOST Q2 L4/L5] „Punkt- und Intervallwahrscheinlichkeiten für die Anzahl an Erfolgen“; Zahlenbeispiele eigen (Ermessen; keine Zahl aus einer Rohdateizeile übernommen); [LS-AA EP V 2–3, QP VIII 5].
 69
 70  Einheit 3 (Kumulierte Wahrscheinlichkeiten):
 71      Übersetzen: „höchstens k“ → P(X ≤ k) · „weniger als k“ → P(X ≤ k − 1) · „mindestens k“ → P(X ≥ k) = 1 − P(X ≤ k − 1) · „mehr als k“ → 1 − P(X ≤ k) · „mindestens a und höchstens b“ → P(X ≤ b) − P(X ≤ a − 1) · „genau k“ → P(X ≤ k) − P(X ≤ k − 1).
 72        n = 20, p = 0,3: P(X ≤ 4) ≈ 0,2375; P(X ≥ 5) = 1 − 0,2375 = 0,7625; P(3 ≤ X ≤ 8) = P(X ≤ 8) − P(X ≤ 2) ≈ 0,8867 − 0,0355 = 0,8512.
 73      Der Rechner liefert P(X ≤ k) (binomcdf); die Tabelle der summierten Binomialverteilung ebenso – bei p über 0,5 Treffer und Niete tauschen und die Tabelle für 1 − p lesen.
 74      Anteile werden erst zu Anzahlen: „mehr als 40 % von 20“ heißt X > 8, also X ≥ 9 – die Grenze ist eine ganze Zahl.
 75      Summenzeichen lesen: Σ von k = 0 bis 8 über (20 über k) · 0,3^k · 0,7^(20 − k) ist P(X ≤ 8); „1 − Σ …“ ist das Gegenereignis. Die untere und die obere Grenze der Summe sagen, welches Ereignis gemeint ist; p sagt, was als Treffer zählt.
 76      Auswendig (Teil A): „Übersetzen“ als Ansatz (Gegenereignis, Differenz, Anteile zu Anzahlen) – [GOST-OHiMi 2.4] „Ansätze zur Berechnung von Wahrscheinlichkeiten für binomialverteilte … Zufallsgrößen“; kumulierte Werte („Der Rechner liefert …“, Tabelle) nennt die Anlage nicht – Teil B; „Summenzeichen lesen“ ist vorausgesetzte Schreibweise ([IQB-VER 1]), keine Anlagenforderung.
 77      Formelsammlung: keine Formel für kumulierte Wahrscheinlichkeiten in [FS-IQB 1.4] (nur die Einzelformel); die Werte kommen vom Rechner oder aus der Tabelle – [FS] offen
 78  Quelle: eigene Formulierung nach [GOST Q2 L4/L5] „Punkt- und Intervallwahrscheinlichkeiten für die Anzahl an Erfolgen“, „Binomialverteilung im Histogramm, auch kumulative Darstellungen“ und [IQB-VER 1] Summenschreibweise; Übersetzungsliste aus den Fehlerquellen der Rohdatei (Grenzen, Anteile, Treffer und Niete); Zahlenbeispiele eigen (Ermessen); [LS-AA EP V 5, QP VIII 7].
 79
 80  Einheit 4 (Umkehraufgaben):
 81      Mindestanzahl bei „mindestens ein Treffer“: P(mindestens einer) = 1 − (1 − p)^n soll die Schranke erreichen. Umstellen auf (1 − p)^n ≤ Rest, dann logarithmieren – beim Teilen durch den negativen Logarithmus dreht sich das Ungleichheitszeichen – und auf die nächste ganze Zahl aufrunden.
 82        p = 0,3, Schranke 0,95: 0,7^n ≤ 0,05 ⇔ n ≥ ln 0,05 / ln 0,7 ≈ 8,4, also n = 9 (Probe: 0,7⁸ ≈ 0,058, 0,7⁹ ≈ 0,040).
 83      Trefferwahrscheinlichkeit bei „kein Treffer“: (1 − p)^n ≥ q ⇔ 1 − p ≥ q^(1/n) ⇔ p ≤ 1 − q^(1/n) – die n-te Wurzel, keine Division.
 84        (1 − p)^10 ≥ 0,6: p ≤ 1 − 0,6^(1/10) ≈ 0,050, also höchstens etwa 5 %.
 85      Grenze k, Umgebung um μ, Umfang n oder p durch Probieren: am Rechner die Werte der Reihe nach prüfen und beide Nachbarn hinschreiben – den letzten, der die Schranke verfehlt, und den ersten, der sie erreicht.
 86        n = 50, p = 0,2, kleinstes k mit P(X ≤ k) ≥ 0,9: P(X ≤ 13) ≈ 0,889 < 0,9 und P(X ≤ 14) ≈ 0,939 ≥ 0,9, also k = 14.
 87      Abhängigkeit von n: (1 − p)^n wird mit jedem weiteren Versuch um den Faktor 1 − p kleiner, 1 − (1 − p)^n also größer – eine Aussage darüber wird allgemein begründet, nicht nur an Zahlen.
 88      Auswendig (Teil A): die Ansätze „Mindestanzahl …“ (Gegenereignis als Potenz), „Trefferwahrscheinlichkeit …“ (Wurzel) und „Abhängigkeit von n“ – [GOST-OHiMi 2.4] „Ansätze zur Berechnung von Wahrscheinlichkeiten für binomialverteilte … Zufallsgrößen“, das Auflösen über [GOST-OHiMi 2.1] „Logarithmen“, „einfache Exponentialgleichungen“; „Grenze k, Umgebung um μ, Umfang n oder p durch Probieren“ nicht – Rechnerarbeit, Teil B.
 89      Formelsammlung: Potenzen und Logarithmen [FS-IQB 1.1] (log_a(b^r) = r · log_a b) für das Logarithmieren; für den Ansatz selbst keine Formel – [FS] offen
 90  Quelle: eigene Formulierung nach [GOST-OHiMi 2.1] „Logarithmen“, „einfache Exponentialgleichungen“ und [GOST Q2 L4/L5] „Binomialverteilung zur Beschreibung stochastischer Situationen nutzen“; Wege aus der Rohdatei (Landeshefte: Logarithmus; Pool: Probieren mit Nachbarwerten); Zahlenbeispiele eigen (Ermessen); [LS-AA EP V 7, QP VIII 7].
 91
 92  Einheit 5 (Verteilung im Diagramm):
 93      Säulendiagramm: über jedem k von 0 bis n steht eine Säule der Höhe P(X = k); alle Höhen zusammen ergeben 1; außerhalb von 0 bis n gibt es keine Säule.
 94      Höchste Säule: beim Erwartungswert μ = n · p, wenn er ganzzahlig ist, sonst bei einem seiner beiden Nachbarn (Modalwert). Kleines p: Maximum links, Ausläufer nach rechts; großes p: spiegelbildlich; p = 0,5: symmetrisch zu n/2.
 95        n = 10, p = 0,3: μ = 3, höchste Säule bei k = 3 mit P(X = 3) ≈ 0,267.
 96      Gegenzufallsgröße: Y = n − X zählt die Nieten und ist B(n; 1 − p)-verteilt; P(X = k) = P(Y = n − k) – das Diagramm von Y ist das von X gespiegelt.
 97        X ~ B(10; 0,3), Y = 10 − X ~ B(10; 0,7): P(X = 3) = P(Y = 7) ≈ 0,267.
 98      Kumulierte Darstellung: die Säulen zeigen P(X ≤ k), steigen an und enden bei 1; die Differenz zweier benachbarter Säulen ist eine Einzelwahrscheinlichkeit.
 99      Auswendig (Teil A): „Säulendiagramm“, „Höchste Säule“ und „Gegenzufallsgröße“ – [GOST-OHiMi 2.4] „Darstellung von Zufallsgrößen in Histogrammen“, „Erwartungswert von Zufallsgrößen“; die „Kumulierte Darstellung“ nennt die Anlage nicht ausdrücklich, nur der Plan [GOST Q2 L4/L5] „auch kumulative Darstellungen“ – der Pool prüft sie dennoch in Teil A.
100      Formelsammlung: Stochastik [FS-IQB 1.4] μ = n · p; Regeln zu Lage des Maximums, Symmetrie und Gegenzufallsgröße stehen nicht in der Formelsammlung – [FS] offen
101  Quelle: eigene Formulierung nach [GOST Q2 L4/L5] „Binomialverteilung im Histogramm, auch kumulative Darstellungen“, [GOST Q2 L2] „Eigenschaften auf der Grundlage graphischer Darstellungen“ und [GOST-OHiMi 2.4] „Darstellung von Zufallsgrößen in Histogrammen“; Merkmale aus den Rohdateitypen (Lage des Maximums, Summe 1, Wertebereich, Symmetrie, Gegenzufallsgröße); Zahlenbeispiele eigen (Ermessen); [LS-AA EP V 4, QP VIII 6].
102
103  ### Typische Fehler
104  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 155 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
105  - Grenzen falsch eingeschlossen: „mehr als k“ als X ≥ k, „weniger als k“ als X ≤ k, „mindestens k“ über P(X ≤ k) statt P(X ≤ k − 1), beim Intervall die falsche Grenze abgezogen, strikte Ungleichungen am Diagramm mitgezählt – das häufigste Muster in beiden Profilen. [abi 2018-be-gk-B3.2a, 2022-bebb-lk-B4k, 2022-bebb-lk-B4d, 2023-bebb-lk-B4a, 2026-bb-gk-B4b, 2026-bb-ea-B4a, 2023-bebb-gk-A1.7a, 2021-be-gk-B4a, 2020-be-gk-B4.2a, 2025-bebb-gk-B4d, 2024-bebb-lk-B4c; iqb 2026MgrundlegendBStochastikWTR1-1b, 2026MgrundlegendBStochastikWTR2-1c, 2026MerhoehtBStochastikWTR1-1a, 2026MerhoehtBStochastikWTR2-1a, 2025MgrundlegendBStochastikWTR2-1c, 2025MgrundlegendBStochastikWTR3-1d, 2024MerhoehtBStochastikWTR2-1c, 2023MgrundlegendBStochastikWTR2-1b, 2023MerhoehtBStochastikWTR1-1, 2022MerhoehtBStochastikWTR1-1d, 2022MerhoehtBStochastikWTR2-1e, 2021MgrundlegendBStochastikWTR2-1a, 2020MgrundlegendBStochastikWTR1-1a, 2018MgrundlegendBStochastikWTR2-1a, 2018MerhoehtBStochastikWTR2-1a, 2018MgrundlegendBStochastikWTR1-1d, 2025MgrundlegendBStochastikWTR1-1d, 2021MgrundlegendBStochastikWTR3-1c, 2024MerhoehtBStochastikWTR1-1c]
106  - Anteil und Anzahl verwechselt: „mindestens 6 %“ als X ≥ 6, „höchstens 70 %“ als X ≤ 70, „5 % Abweichung“ als fünf Personen, „mehr als 3 % der Kartons“ falsch in eine Anzahl übersetzt, die Schranke nicht auf die nächste ganze Zahl gehoben (46 statt 47), „mindestens viermal so viele“ als das Vierfache des Erwarteten. [iqb 2018MerhoehtBStochastikWTR1-1a, 2024MgrundlegendBStochastikWTR2-2a, 2019MgrundlegendBStochastikWTR1-1a, 2023MerhoehtBStochastikWTR3-1c, 2025MerhoehtBStochastikWTR1-1c, 2025MerhoehtBStochastikWTR2-1b, 2023MgrundlegendBStochastikWTR2-2b, 2023MgrundlegendBStochastikWTR3-1d; abi 2025-bebb-lk-B4b, 2023-bebb-lk-B4a, 2023-bebb-gk-B4.1d]
107  - Treffer und Niete vertauscht: mit p statt 1 − p gerechnet, die Trefferdefinition beim Zählen der Nieten nicht mitgewechselt, im Summenterm p auf das falsche Merkmal bezogen („mindestens 75 am Gymnasium“, „0,23 als Zufriedenheitsanteil“), Exponenten von p und 1 − p vertauscht, mit dem Anteil der Nieten weitergerechnet. [abi 2018-bb-ea-B4.2b, 2017-bb-ea-B4.2d, 2018-be-gk-B3.2d, 2023-bebb-gk-B4.1e, 2020-be-gk-B4.2c; iqb 2018MerhoehtBStochastikWTR1-1b, 2023MgrundlegendBStochastikWTR3-1e, 2024MerhoehtBStochastikWTR2-1d, 2021MgrundlegendBStochastikWTR3-1d, 2022MerhoehtBStochastikWTR2-1d, 2020MgrundlegendBStochastikWTR1-1c, 2020MgrundlegendBStochastikWTR2-1c, 2018MgrundlegendBStochastikWTR3-2b, 2020MerhoehtAStochastik11-a]
108  - Anordnungen vergessen: nur das Produkt der Einzelwahrscheinlichkeiten ohne Binomialkoeffizienten, bei zwei Versuchen nur ein Pfad, der Faktor für die Anordnungen bei drei Versuchen oder für die Position des einen Wappens weggelassen, P(X = 5)² statt einer zweiten Binomialverteilung mit Auswahl der Spieler. [abi 2018-bb-ea-B4.1b, 2026-bb-ea-A1.4a, 2026-bb-gk-A1.3a, 2024-bebb-lk-A1.9a, 2023-bebb-lk-A1.8a, 2021-be-gk-B4d; iqb 2026MgrundlegendAStochastik12-a, 2026MerhoehtAStochastik11-a, 2026MerhoehtAStochastik22-a, 2024MgrundlegendAStochastik12-a, 2023MerhoehtAStochastik22-a, 2017MerhoehtAStochastik11-b, 2019MerhoehtAStochastik11-b, 2021MgrundlegendBStochastikWTR2-1c]
109  - Einzel- und kumulierte Wahrscheinlichkeit verwechselt: die kumulierte Rechnerfunktion für „genau k“, die Summe als „genau k“ oder „mindestens k“ gedeutet, die Säule statt der Summe der Säulen genommen, P(X ≤ 2) als P(X = 2) abgelesen, die Summe über fünf Säulen mit P(X ≥ 16) verwechselt, eine Pfadwahrscheinlichkeit als Binomialwahrscheinlichkeit für genau drei Treffer gedeutet. [abi 2025-bebb-lk-B4a, 2019-be-gk-B4.2e, 2020-be-gk-B4.2b, 2026-bb-gk-A1.6b; iqb 2025MerhoehtBStochastikWTR2-1a, 2022MgrundlegendBStochastikWTR2-2a, 2026MgrundlegendBStochastikWTR2-1d, 2020MgrundlegendBStochastikWTR1-1b, 2026MgrundlegendAStochastik11-b, 2019MerhoehtAStochastik11-a, 2025MgrundlegendBStochastikWTR3-1c, 2025MerhoehtAStochastik12-a, 2019MgrundlegendBStochastikWTR2-1a]
110  - Gegenereignis nicht genutzt oder falsch gebildet: „höchstens eins“ als „genau eins“, P(mindestens einer) als lange Summe statt 1 − P(keiner), (1 − p)^n als Wahrscheinlichkeit für mindestens einen Treffer gedeutet, „Tom mindestens einmal“ als „Tom genau einmal“, beim symmetrischen Intervall nur einen Rand abgezogen, P(X ≤ 1900) für „mindestens 100 nicht zugestellt“. [abi 2018-be-gk-B3.1b, 2018-be-gk-B3.1c, 2019-be-gk-B4.2d; iqb 2020MgrundlegendAStochastik2-b, 2021MerhoehtAStochastik12-b, 2020MgrundlegendBStochastikWTR2-1b, 2023MerhoehtBStochastikWTR3-1a]
111  - Ungleichung und Wurzel: beim Teilen durch den negativen Logarithmus das Ungleichheitszeichen nicht gedreht, abgerundet statt aufgerundet, die n-te Wurzel als Division durch n ausgeführt, beim Wurzelziehen p und 1 − p verwechselt. [abi 2017-bb-ea-B4.2b, 2023-bebb-gk-B4.1f, 2022-bebb-gk-B4d, 2019-be-gk-B4.1b, 2020-be-gk-B4.1c, 2021-be-gk-B4e, 2018-be-gk-B3.2d, 2022-bebb-gk-B4e; iqb 2018MgrundlegendBStochastikWTR2-1d, 2022MgrundlegendBStochastikWTR1-1c]
112  - Schranke ohne Nachbarwerte, Kurzschluss über den Erwartungswert: k = 103 statt 104 (Schranke nicht überschritten), k = 114 statt 113 (≤ statt <), n = 200 aus 0,8n = 160, n = 90 aus 30/p, p = 30 % aus E(X) = 3, das Sigma-Intervall ohne Prüfung angegeben, eine symmetrische statt der einseitigen Umgebung gerechnet, mit p = 0,04 statt 0,96 nach dem Trefferwechsel. [abi 2025-bebb-gk-B4d, 2023-bebb-lk-B4h; iqb 2025MgrundlegendBStochastikWTR1-1d, 2022MerhoehtBStochastikWTR2-1e, 2019MgrundlegendBStochastikWTR1-1b, 2022MgrundlegendBStochastikWTR2-2b, 2021MgrundlegendBStochastikWTR2-1d, 2023MerhoehtBStochastikWTR2-2b, 2019MgrundlegendBStochastikWTR3-1d, 2024MgrundlegendBStochastikWTR2-2b, 2018MerhoehtBStochastikWTR1-1b]
113  - Modell nicht geprüft: Binomialverteilung wegen „zwei Ausgänge“ bejaht, obwohl ohne Zurücklegen aus vierzig Geräten gezogen wird; die feste Fehlerquote als konstantes p gelesen; mit „zu wenige Versuche“ statt mit der veränderlichen Wahrscheinlichkeit argumentiert; nur „zwei Ausgänge“ genannt, Unabhängigkeit und Konstanz von p nicht; ein Spiel mit drittem Ausgang als Bernoulli-Kette bejaht; ein Ereignis mit der falschen Wahrscheinlichkeit für die gleichverteilte Zufallsgröße gewählt. [abi 2018-be-gk-B3.2g, 2022-bebb-gk-B4a; iqb 2018MgrundlegendBStochastikWTR1-1e, 2018MgrundlegendBStochastikWTR2-1g, 2018MerhoehtBStochastikWTR2-1d, 2023MgrundlegendBStochastikWTR2-1a, 2020MgrundlegendBStochastikWTR2-1a, 2018MgrundlegendBStochastikWTR3-2d, 2024MerhoehtAStochastik23-b]
114  - Diagramm falsch gelesen: das Maximum bei n/2 statt bei n · p vermutet, ein Diagramm nach der Form gewählt, ohne die Summe der Säulen zu prüfen, die Lage des Maximums als einziges Merkmal geprüft, bei der Gegenzufallsgröße die Säule bei k statt bei n − k gelesen oder das Diagramm unverändert abgezeichnet, die Symmetrieachse auf eine ganze Zahl statt auf die Mitte gelegt, die Symmetrie nicht genutzt, Säulen ohne Achsenwerte abgezählt, den Erwartungswert an eine beliebige Säule geschrieben, die Breite einer Verteilung als kleinere Wahrscheinlichkeit gedeutet, aus fünf Werten n = 5 statt n = 4 gelesen. [abi 2020-be-gk-B4.2d, 2023-bebb-gk-A1.7b, 2026-bb-gk-B4c, 2026-bb-ea-B4b, 2022-bebb-lk-A1.8b, 2025-bebb-gk-A1.9b; iqb 2020MgrundlegendBStochastikWTR1-1d, 2021MgrundlegendAStochastik12-b, 2019MgrundlegendAStochastik12-b, 2018MerhoehtAStochastik11-a, 2017MerhoehtAStochastik12-b, 2026MgrundlegendBStochastikWTR1-1c, 2026MerhoehtBStochastikWTR1-1b, 2024MerhoehtAStochastik23-a, 2021MgrundlegendAStochastik2-b, 2025MgrundlegendAStochastik21-b, 2020MerhoehtAStochastik11-b, 2020MerhoehtAStochastik11-c, 2025MgrundlegendBStochastikWTR2-1d, 2022MgrundlegendBStochastikWTR2-3a, 2021MgrundlegendBStochastikWTR1-1c]
115  - Gerechnet statt begründet, Beispiel statt allgemein: Wahrscheinlichkeiten ausgerechnet, obwohl die Begründung über den Erwartungswert verlangt war; eine Aussage nur an einem Zahlenbeispiel geprüft; für einzelne n gerechnet statt über das Potenzgesetz; der Erwartungswert ohne Prüfung der Nachbarwerte als Modalwert genommen; eine größere Stichprobe pauschal als besser angesehen. [abi 2018-bb-ea-B4.2c, 2025-bebb-gk-B4c, 2018-be-gk-B3.2c, 2022-bebb-lk-B4f, 2018-be-gk-B3.2b; iqb 2025MgrundlegendBStochastikWTR1-1c, 2018MgrundlegendBStochastikWTR2-1c, 2022MerhoehtBStochastikWTR1-1f, 2018MgrundlegendBStochastikWTR2-1b, 2023MgrundlegendBStochastikWTR1-2b]
116  - Verkettete Modelle falsch zusammengesetzt: zwei abhängige Ereignisse als unabhängig multipliziert, den Rest der Kette vergessen, für den Rest mit n statt n − 1 gerechnet, den zweiten Prüfschritt ohne den Faktor des ersten addiert, zwei Spieler als einen Spieler mit doppelter Versuchszahl, alle Würfe als zufällig angesetzt, obwohl ein Teil schon feststand. [abi 2022-bebb-lk-B4m, 2018-be-gk-B3.1b, 2021-be-gk-B4b; iqb 2023MgrundlegendBStochastikWTR1-2a, 2023MgrundlegendBStochastikWTR2-2b, 2023MerhoehtBStochastikWTR3-1c]
117  - Parameter falsch abgelesen oder nicht gekürzt: p = 1/6 statt 1/3, weil zwei Seiten die Sechs zeigen; n = 3 statt 5 aus den Exponenten eines Terms; p = 2 aus E(X) = 2; (1 − p)^n nicht durch (1 − p)^(n − 1) gekürzt; (5 über 4) = 5 vergessen. [abi 2020-be-gk-B4.1a; iqb 2021MgrundlegendAStochastik2-a, 2020MgrundlegendAStochastik2-a, 2025MerhoehtAStochastik21, 2019MerhoehtAStochastik11-b]
118  - Tabelle falsch gelesen: F(9) statt F(8) für „weniger als 9“, die Tabelle für p = 0,8 nicht über das Gegenereignis mit p = 0,2 gelesen, P(X ≤ 17) statt P(X ≤ 16) abgezogen, P(X ≤ 5) statt P(X ≤ 4). [abi 2022-bebb-gk-B4b, 2019-be-gk-B4.1a, 2020-be-gk-B4.2a, 2021-be-gk-B4a; iqb 2022MgrundlegendBStochastikWTR1-1a]
119
120  ### Für schwache Schüler
121  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q2 Brandenburg (Berlin Q4), Grund- und Leistungskursfach ohne LK-Zusatz: Einheit 1 „Bernoulli-Experiment“, „Bernoulli-Kette“, Urnenmodell „Ziehen mit Zurücklegen (Binomialverteilung)“ gegen „Ziehen ohne Zurücklegen“; Einheit 2 „Punkt-… wahrscheinlichkeiten für die Anzahl an Erfolgen“; Einheit 3 „… und Intervallwahrscheinlichkeiten“, „kumulative Darstellungen“; Einheit 4 „die Binomialverteilung zur Beschreibung stochastischer Situationen nutzen“ (die Umkehraufgaben nennt kein Plan wörtlich; sie sind Anwendung dieser Zeile); Einheit 5 „Binomialverteilung im Histogramm“, „Eigenschaften auf der Grundlage graphischer Darstellungen“, Erwartungswert als Kenngröße. Ohne Hilfsmittel (Anlage OHiMi 2.4, Prüfungsteil A): Bernoulli-Formel, Binomialkoeffizient mit Eigenschaften, Histogramme, Ansätze zur Berechnung von Wahrscheinlichkeiten binomialverteilter Zufallsgrößen, Erwartungswert – nicht: kumulierte Werte, Logarithmus. LK-Zusatz: keiner (die Q4-Zusätze Hypothesentests und Normalverteilung liegen bei den Nachbarthemen). Vorrat, weil der Plan keine Grenze zieht (Ermessen nach dem Niveau der Rohdatei): die Prüfungshöhe-Sprossen jeder Einheit – verkettete Binomialmodelle (Einheit 3), algebraische Umkehraufgaben und allgemeine Widerlegungen (Einheit 4), Symmetrie mit kumulierten Werten und Konstruktion einer gleichverteilten Zufallsgröße (Einheit 5 und 1). Niveaustufe H der E-Phase [RLP H]: „Bestimmen von Anzahlen mithilfe von Fakultäten und Binomialkoeffizienten“, „Nutzen von Wahrscheinlichkeiten zum Vorhersagen von relativen und absoluten Häufigkeiten“; G: Pfadregeln, Gegenwahrscheinlichkeiten, Urnenmodell „mit und ohne Zurücklegen“ – Blatt-0-Stoff (Voraussetzungen eins bis drei), kein Mindeststoff dieses Eintrags. RLP FOS (fhr): kein Stoff – das Thema hat keine fhr-Zeile. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung unter Stochastik Zufallsgrößen, Erwartungswert und Binomialverteilung – wenn das zutrifft, deckt es sich mit dem GK-Kern, kein zusätzlicher Posten.
122  Grundvorstellung (Blatt 0) [GOST Eingangsvoraussetzung L5, MO]: Die Anzahl der Treffer ist eine Zufallsgröße, die man am Baum abzählt – nicht eine Formel, in die man einsetzt. „Hier ist ein Baumdiagramm mit drei Stufen für ein Glücksrad: Treffer oder Niete, bei jeder Drehung dieselbe Trefferwahrscheinlichkeit. Male alle Pfade mit genau zwei Treffern an. Wie viele sind es? Haben sie dieselbe Wahrscheinlichkeit – warum? Wie viele Pfade haben genau einen Treffer, wie viele keinen? Steht die Anzahl der Treffer vor dem Drehen fest, oder fällt sie zufällig aus? Welche Werte kann sie annehmen? Trage für jeden möglichen Wert einen Strich je Pfad ein.“ Wer TNT und TTN für denselben Pfad hält, wer P(genau zwei Treffer) als p mal p ohne die Niete und ohne die Anzahl der Pfade schreibt oder wer der Trefferzahl nur einen Wert zugesteht, braucht das vor jeder Formel: Der Binomialkoeffizient zählt die Pfade, die Potenzen gehören zu einem einzelnen Pfad, und die Anzahl der Treffer ist das, was gezählt wird. Verständnis, nicht Verfahren; Ermessen in der Aufgabenform, amtlich in der Vorstellung. [GOST Eingangsvoraussetzung L5 „Baumdiagrammen sowie Pfadregeln“, „nutzen Binomialkoeffizienten und Fakultäten zur Berechnung von Wahrscheinlichkeiten“; GOST Q2 L4 „Zufallsgrößen als Zuordnung von Ergebnissen von Zufallsexperimenten“; MO-Logik: Vorstellung vor Verfahren; abi 2018-bb-ea-B4.1b Fehlerquelle „den Binomialkoeffizienten weglassen und nur das Produkt der Einzelwahrscheinlichkeiten angeben“; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
123  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
124  - Modell erkennen (Einheit 1): „Bernoulli oder nicht?“ – zu Aufgabentexten ankreuzen: zwei Ausgänge? feste Anzahl? p bei jedem Versuch gleich (mit Zurücklegen oder sehr große Gesamtheit)? unabhängig? – und bei „nein“ die verletzte Bedingung nennen; nichts rechnen (Vorstufe) → ein Bernoulli-Experiment erkennen, den Treffer festlegen und p nennen (Grundfall, viermal: Münze, Würfel, Glücksrad, Anteil in einer großen Bevölkerung) → die Kette beschreiben: n und p aus dem Text, X als „Anzahl der Treffer“, Schreibweise X ~ B(n; p) → genau ein Treffer bei zwei Versuchen über die zwei Pfade (abi 2024-bebb-lk-A1.9a, iqb 2024MgrundlegendAStochastik12-a) → mindestens zwei Treffer bei drei Versuchen als Summe zweier Fälle mit dem Anordnungsfaktor (abi 2023-bebb-lk-A1.8a, iqb 2023MerhoehtAStochastik22-a) → die Bernoulli-Bedingungen im Sachzusammenhang begründen: zwei Ausgänge, feste Anzahl, gleiches p, Unabhängigkeit; die sehr große Gesamtheit als Ersatz für das Zurücklegen (abi 2022-bebb-gk-B4a, iqb 2020MgrundlegendBStochastikWTR2-1a, 2023MgrundlegendBStochastikWTR2-1a) → die Ungeeignetheit begründen: kleine Gesamtheit ohne Zurücklegen, p ändert sich, der Wertebereich passt nicht zur Zahl der vorhandenen Treffer (abi 2018-be-gk-B3.2g, iqb 2018MgrundlegendBStochastikWTR1-1e, 2018MgrundlegendBStochastikWTR2-1g) → Prüfungshöhe: Aussagen über Bernoulli-Experiment und Bernoulli-Kette beurteilen und den dritten Ausgang finden (iqb 2018MgrundlegendBStochastikWTR3-2d, Niveau III) und zu einer gegebenen Verteilung eine gleichverteilte Zufallsgröße in einem anderen Experiment konstruieren (iqb 2024MerhoehtAStochastik23-b, Niveau III).
125  - Bernoulli-Formel (Einheit 2): „Genau, höchstens oder mindestens?“ – zu Ereignissen die Grenze ankreuzen: genau k als Einzelwahrscheinlichkeit; höchstens, weniger als, mindestens, mehr als kumuliert, mit der richtigen ganzen Zahl k und mit oder ohne Gegenereignis; nichts rechnen (Vorstufe) → den Term für P(X = k) ohne Rechnung hinschreiben (Grundfall, viermal, kleine n) → die ganze Verteilung für kleines n: alle Einzelwahrscheinlichkeiten P(X = k) von k gleich null bis k gleich n der Reihe nach, Kontrolle: die Summe ist eins → den Binomialkoeffizienten mit der Rechnertaste und im Kopf bestimmen und den Term ausrechnen → die Sonderfälle „alle Treffer“ und „kein Treffer“ als Potenz ohne Binomialkoeffizient (abi 2018-bb-ea-B4.2b, 2020-be-gk-B4.1a) → die Trefferdefinition wechseln und mit den Nieten rechnen (abi 2018-bb-ea-B4.2b) → „höchstens einmal“ als Summe zweier Terme (abi 2026-bb-gk-A1.3a, iqb 2026MgrundlegendAStochastik12-a) → Platzhalter in einem vorgegebenen Term aus den Exponenten lesen (iqb 2021MgrundlegendAStochastik2-a) → die Rechnerfunktion für die Einzelwahrscheinlichkeit bei großem n (abi 2025-bebb-lk-B4a, iqb 2025MerhoehtBStochastikWTR2-1a) → k aus einem Anzahlverhältnis, p oder n aus dem Erwartungswert vor der Formel (abi 2020-be-gk-B4.2c, iqb 2020MgrundlegendAStochastik2-a, 2022MgrundlegendBStochastikWTR2-2a) → Prüfungshöhe: die Einzelwahrscheinlichkeit als Differenz zweier Tabellenwerte neben einer kumulierten (abi 2022-bebb-gk-B4b, 2019-be-gk-B4.1a, Niveau I bis II) und zwei Einzelwahrscheinlichkeiten über den Erwartungswert vergleichen (abi 2018-bb-ea-B4.2c, Niveau III, fünf Punkte).
126  - Kumulierte Wahrscheinlichkeiten (Einheit 3): „Mit oder ohne Gegenereignis?“ – zu Ereignissen ankreuzen, ob P(X ≤ k) unmittelbar aus der Tabelle kommt (höchstens, weniger als) oder über eins minus P(X ≤ k) (mindestens, mehr als), und welches ganzzahlige k gilt; nichts rechnen (Vorstufe) → den Wortlaut in P(X ≤ k) übersetzen: höchstens, weniger als, mindestens, mehr als (Grundfall, viermal) → den Wert mit der Rechnerfunktion oder aus der Tabelle holen (abi 2026-bb-gk-B4b, iqb 2026MgrundlegendBStochastikWTR1-1b) → das Gegenereignis für „mindestens“ und „mehr als“ (iqb 2020MgrundlegendBStochastikWTR1-1a, abi 2022-bebb-lk-B4k) → das Intervall als Differenz zweier kumulierter Werte mit richtig gesetzter unterer Grenze (abi 2018-be-gk-B3.2a, iqb 2024MerhoehtBStochastikWTR2-1c) → Anteile in Anzahlen umrechnen: „mehr als die Hälfte“, „höchstens siebzig Prozent“ (abi 2023-bebb-lk-B4a, iqb 2024MgrundlegendBStochastikWTR2-2a, 2025MerhoehtBStochastikWTR1-1c) → eine Verhältnis- oder Summenbedingung in eine Ungleichung für X übersetzen (abi 2023-bebb-gk-B4.1d, iqb 2018MgrundlegendBStochastikWTR3-2b) → die Abweichung vom Erwartungswert als Intervall oder als einseitige Schranke (iqb 2019MgrundlegendBStochastikWTR1-1a, abi 2025-bebb-lk-B4b) → einen Summenterm in eine Sachaussage übersetzen: Grenzen, p, Gegenereignis (abi 2023-bebb-gk-B4.1e, iqb 2026MgrundlegendBStochastikWTR2-1d, 2021MgrundlegendBStochastikWTR3-1d) → Prüfungshöhe: zwei Binomialmodelle verketten – die Fehlerwahrscheinlichkeit einer Einheit als p der zweiten Verteilung, ein zweistufiger Prüfplan, eine in Abschnitte geteilte Kette (abi 2021-be-gk-B4d, 2022-bebb-lk-B4m; iqb 2023MerhoehtBStochastikWTR3-1c, 2023MgrundlegendBStochastikWTR1-2a, Niveau II bis III) und eine Ungleichung mit Binomialsumme als Sachaussage formulieren (iqb 2024MgrundlegendAStochastik21-b, 2020MgrundlegendAStochastik2-b, Niveau III).
127  - Umkehraufgaben (Einheit 4): „Was ist gesucht?“ – zu Aufgaben ankreuzen, ob eine Wahrscheinlichkeit gesucht ist oder n, p oder k, und welcher Weg passt: Logarithmus (Mindestanzahl bei „mindestens einmal“), Wurzel (p bei „kein Treffer“), Probieren mit Nachbarwerten am Rechner (Grenze k, Umgebung, n bei „mehr als k Treffern“); nichts rechnen (Vorstufe) → den Ansatz für „mindestens ein Treffer“ aufstellen: Gegenereignis „kein Treffer“ als Potenz der Nietenwahrscheinlichkeit, Wahrscheinlichkeit für mindestens einen Treffer als eins minus diese Potenz (Grundfall, viermal) → nach n auflösen: logarithmieren, das Ungleichheitszeichen drehen, aufrunden (abi 2017-bb-ea-B4.2b, 2023-bebb-gk-B4.1f) → p aus der Wahrscheinlichkeit für „kein Treffer“ über die n-te Wurzel (abi 2022-bebb-gk-B4e, iqb 2018MgrundlegendBStochastikWTR2-1d) → das kleinste oder größte k gegen eine Schranke mit beiden Nachbarwerten am Rechner (abi 2025-bebb-gk-B4d, iqb 2022MerhoehtBStochastikWTR2-1e) → den kleinsten Radius einer Umgebung um den Erwartungswert, symmetrisch oder einseitig (abi 2023-bebb-lk-B4h, iqb 2019MgrundlegendBStochastikWTR3-1d, 2024MgrundlegendBStochastikWTR2-2b) → n durch Probieren für „mehr als k Treffer“ oder „mindestens drei Treffer“ (abi 2024-bebb-lk-B4c, iqb 2019MgrundlegendBStochastikWTR1-1b, 2018MerhoehtBStochastikWTR1-1b) → p durch Probieren auf ganze Prozent oder n zu einer vorgegebenen Einzelwahrscheinlichkeit (iqb 2021MgrundlegendBStochastikWTR2-1d, 2022MgrundlegendBStochastikWTR2-2b) → Aussagen über die Abhängigkeit von n beurteilen: eine Potenz mit Basis unter eins fällt, an Beispielen prüfen und allgemein begründen (abi 2018-be-gk-B3.2c, 2018-be-gk-B3.1c; iqb 2023MgrundlegendBStochastikWTR1-2b) → Prüfungshöhe: p aus einer Gleichung zweier Einzelwahrscheinlichkeiten und n und p aus einem Verhältnis und dem Erwartungswert ohne Rechner (iqb 2019MerhoehtAStochastik11-b, 2025MerhoehtAStochastik21, Niveau II bis III) und die Halbierungsaussage über das Potenzgesetz allgemein widerlegen (abi 2022-bebb-lk-B4f, iqb 2022MerhoehtBStochastikWTR1-1f, Niveau III).
128  - Verteilung im Diagramm (Einheit 5): „Treffer oder Niete gezählt?“ ankreuzen (Vorstufe, Grundvorstellung) → Säulenhöhen als Einzelwahrscheinlichkeiten ablesen und benachbarte Säulen zu einer Intervallwahrscheinlichkeit addieren (abi 2023-bebb-gk-A1.7a, 2026-bb-gk-A1.6b; Grundfall, viermal) → den Erwartungswert berechnen und die höchste Säule finden, den Modalwert angeben, Achsen skalieren (abi 2018-be-gk-B3.2b, iqb 2020MerhoehtAStochastik11-b, 2025MgrundlegendBStochastikWTR2-1d) → eine Aussage über die Stelle des Maximums über den Erwartungswert beurteilen, ohne Wahrscheinlichkeiten zu rechnen (abi 2025-bebb-gk-B4c, 2020-be-gk-B4.2d) → unpassende Diagramme ausschließen: Lage des Maximums, Summe eins, Wertebereich (abi 2023-bebb-gk-A1.7b, iqb 2021MgrundlegendAStochastik12-b, 2018MerhoehtAStochastik11-a) → die Gegenzufallsgröße: Diagramm spiegeln, die Säule bei n minus k lesen (abi 2026-bb-gk-B4c, iqb 2024MerhoehtAStochastik23-a) → die kumulierte Darstellung: letzte Säule eins, Einzelwahrscheinlichkeit als Differenz (iqb 2019MerhoehtAStochastik11-a) → die Symmetrie für p gleich ein Halb nutzen: symmetrisches Intervall, Verschiebung des Maximums mit p (iqb 2021MerhoehtAStochastik12-b, 2020MerhoehtAStochastik11-c) → Prüfungshöhe: eine Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen (abi 2025-bebb-gk-A1.9b, iqb 2021MgrundlegendAStochastik2-b, Niveau III), Aussagen an mehreren Verteilungen beurteilen (iqb 2022MgrundlegendBStochastikWTR2-3a, 2021MgrundlegendBStochastikWTR1-1c) und eine Binomialverteilung über Symmetrie, Wertebereich und eine Einzelwahrscheinlichkeit ausschließen (abi 2022-bebb-lk-A1.8b).
129
130  ### Prüfungsform (fhr / abi / iqb)
131  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen (be-gk, be-lk, bb-gk, bb-ea) mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; das Thema ist dort kein Stoff (RLP FOS 2019), themen.csv führt keine fhr-Zeile. Die Rohdatei zählt 187 Zeilen mit 58 Haupttypen (abi 71 Zeilen, 31 Typen; iqb 116 Zeilen, 53 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
132  fhr: kein Stoff, keine Zeile – RLP FOS 2019 Pflichtthema 4 „Stochastik“ endet bei Pfadregeln, Erwartungswert und Binomialkoeffizient; die fhr-Zeilen dazu liegen bei zufallsexperimente-und-pfadregeln.md, kenngroessen-von-verteilungen.md und kombinatorik.md.
133  abi (71 Zeilen, 31 Typen; Landeshefte bb-ea, be-gk, bebb-gk, bebb-lk, bb-gk 2017–2026, davon 8 aus CAS-Fassungen: 2 aus bb-ea 2017, 4 aus be-gk 2017, 2 aus be-gk 2018) [abi-Katalog]: Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen (10, E2) · Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln (9, E2) · Anzahl von Versuchen einer Bernoulli-Kette für mindestens einen Treffer über das Gegenereignis bestimmen (8, E4) · Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln (7, E3) · Kumulierte Binomialsumme als Sachaussage formulieren (4, E3) · Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen (2, E5) · Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln (2, E4) · Modalwert einer Binomialverteilung bestimmen (2, E5) · Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben (2, E2) · Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen (2, E4) · Wahrscheinlichkeit für zwei gleichzeitige Ereignisse über die Aufteilung einer Bernoulli-Kette in zwei Abschnitte berechnen (2, E3) · Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern (2, E5) · je 1: Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen (E4) · Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen (E4) · Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen (E3) · Behauptung zur Monotonie einer Wahrscheinlichkeit an Beispielwerten prüfen (E4) · Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen (E1) · Binomialverteilung über den Widerspruch zwischen Symmetrie und einer Einzelwahrscheinlichkeit ausschließen (E5) · Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen (E5) · Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln (E4) · Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln (E4) · Trefferzahlen mit einer Einzelwahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln (E4) · Ungeeignetheit des Binomialmodells begründen (E1) · Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen (E5) · Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen (E3) · Wahrscheinlichkeit eines Intervalls aus dem Säulendiagramm einer Verteilung ablesen (E5) · Wahrscheinlichkeit für eine Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden (E3) · Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen (E1) · Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen (E1) · Wahrscheinlichkeit für zwei unabhängige Spieler als Produkt binomialer Wahrscheinlichkeiten berechnen (E3) · Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen (E5). Muster: Teil B (mit Hilfsmitteln) trägt 62 von 71 Zeilen – in jedem Heft eine Stochastik-Aufgabe mit drei bis sieben Teilaufgaben zur Binomialverteilung, zwei bis fünf Punkte je Zeile; seit dem Nachzug 2026-09-28 mit dem Berliner Grundkursheft 2017 (zwei Ketten: die Smartphones mit Bernoulli-Formel, Summenterm und Mindestanzahl, 2017-be-gk-B3.1e, 2017-be-gk-B3.1f, 2017-be-gk-B3.1g; Würfel und Glücksrad mit zwei Bernoulli-Rechnungen bis n = 30 und der geteilten Kette für Gewinn und Extrapreis, 2017-be-gk-B3.2c, 2017-be-gk-B3.2d, 2017-be-gk-B3.2e) und der CAS-Fassung 2017 (die umgekehrte Mindestanzahl und die Einzelwahrscheinlichkeit der Lesung, 2017-bb-ea-cas-B4.2b, 2017-bb-ea-cas-B4.2d); seit dem Nachzug 2026-09-29 dazu die Berliner CAS-Fassungen 2017 und 2018 mit sechs Zeilen: an den Smartphones der Modalwert unter zweihundertfünfzig Geräten aus Werk A und der Mindestumfang für fünfhundert fehlerfreie Geräte aus Werk C, beide wortgleich aus dem grundlegenden CAS-Pool 2017 (2017-be-gk-cas-B3.1e, Niveau I; 2017-be-gk-cas-B3.1g, Niveau III – das WTR-Heft stellt an beiden Stellen andere Aufträge); am Glücksrad die Bernoulli-Rechnung als Landesdublette der WTR-Zeile, nur mit vier statt fünf Punkten und ohne Tafel (2017-be-gk-cas-B3.2c), und neu das Auszählen der Trefferzahlen einer zweiten Binomialverteilung, deren Einzelwahrscheinlichkeit über zehn Prozent liegt (2017-be-gk-cas-B3.2d, vier Punkte, Niveau II, neuer Typ); 2018 die Spielwahrscheinlichkeiten als Landesdublette der WTR-Zeile mit geänderter Zahl im Ereignis B, Punkte gleich (2018-be-gk-cas-B3.1b), und die kumulierten Bildschirm-Wahrscheinlichkeiten wortgleich aus dem Pool (2018-be-gk-cas-B3.2a, Dublette von 2018MgrundlegendBStochastikWTR2-1a, das WTR-Heft 2018-be-gk-B3.2a hat Ereignis B abgewandelt); bis 2022 mit einer Tabelle der summierten Binomialverteilung als Anlage (acht Zeilen lesen aus der Tabelle: 2018-be-gk-B3.2a, 2019-be-gk-B4.1a, 2020-be-gk-B4.2a, 2021-be-gk-B4a/b/d, 2022-bebb-gk-B4b, 2022-bebb-lk-B4d), seit 2023 nur Rechner. Teil A (9 Zeilen, 2022–2026, ein bis drei Punkte) prüft Term angeben, kleine Ketten über Pfade, Symmetrie und Diagramme – die OHiMi-Inhalte. 38 der 71 Zeilen stammen aus dem Pool (29 wortgleiche Dubletten, 9 abgewandelte – seit dem Nachzug 2026-09-28 dazu 2017-be-gk-B3.1f und 2017-be-gk-B3.1g wortgleich, 2017-be-gk-B3.1e abgewandelt aus dem grundlegenden Pool 2017; seit dem Nachzug 2026-09-29 2017-be-gk-cas-B3.1e, 2017-be-gk-cas-B3.1g und 2018-be-gk-cas-B3.2a wortgleich), zwei sind Landesdubletten der Berliner WTR-Hefte (2017-be-gk-cas-B3.2c, 2018-be-gk-cas-B3.1b); Landeszusätze sind vor allem die Zeilen „Anzahl von Versuchen … über das Gegenereignis“ mit Logarithmus (2017–2023; die Pooldublette 2017-be-gk-B3.1g ausgenommen) und die Tabellenaufgaben. Niveau I 22, II 41, III 8 (2017-be-gk-B3.1g, 2017-be-gk-cas-B3.1g, 2018-bb-ea-B4.2c, 2018-be-gk-B3.2d, 2022-bebb-lk-B4f, 2022-bebb-lk-B4m, 2024-bebb-lk-B4c – seit Abgleichlauf 26 III statt II –, 2025-bebb-gk-A1.9b).
134  iqb (116 Zeilen, 53 Typen; Pool 2017–2026, grundlegend 70 und erhöht 46 Zeilen, Teil A 28 und Teil B 88 Zeilen, davon 11 CAS) [iqb-Katalog]: Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln (16, E3) · Kumulierte Binomialsumme als Sachaussage formulieren (10, E3) · Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln (9, E2) · Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln (7, E4) · Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben (5, E2) · Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen (4, E5) · Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen (3, E2) · Modalwert einer Binomialverteilung bestimmen (3, E5) · Ungeeignetheit des Binomialmodells begründen (3, E1) · Anzahl von Versuchen einer Bernoulli-Kette für mindestens einen Treffer über das Gegenereignis bestimmen (2, E4) · Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen (2, E5) · Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen (2, E1) · Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen (2, E5) · Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln (2, E4) · Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln (2, E4) · Sachaussage zu einer Ungleichung mit Binomialsumme formulieren (2, E3) · Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen (2, E4) · Wahrscheinlichkeit einer prozentualen Abweichung vom Erwartungswert nach beiden Seiten berechnen (2, E3) · Wahrscheinlichkeit für eine Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden (2, E3) · Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen (2, E1) · Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern (2, E5) · je 1: Achsen eines Verteilungsdiagramms über Erwartungswert und größte Einzelwahrscheinlichkeit skalieren (E5) · Aufgabenstellung zu einer Potenz der Gegenwahrscheinlichkeit formulieren und Ansatz erläutern (E3) · Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen (E4) · Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen (E4) · Aussage über eine Summe von Wahrscheinlichkeiten am Säulendiagramm entscheiden (E5) · Aussagen über Bernoulli-Experiment und Bernoulli-Kette im Sachzusammenhang beurteilen (E1) · Aussagen über Verteilungen verschiedener Gruppen am Säulendiagramm beurteilen (E5) · Aussagen über kumulierte Wahrscheinlichkeit und Trefferwahrscheinlichkeit aus dem Säulendiagramm einer Binomialverteilung beurteilen (E5) · Bedingte Restwahrscheinlichkeit nach bekannten Ergebnissen über die Binomialverteilung berechnen (E3) · Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen (E3) · Bedingung an p für das Verhältnis zweier symmetrisch liegender Einzelwahrscheinlichkeiten angeben (E5) · Einzelwahrscheinlichkeit aus dem Diagramm kumulierter Wahrscheinlichkeiten ermitteln (E5) · Einzelwahrscheinlichkeit einer Binomialverteilung aus n und Erwartungswert berechnen (E2) · Kleinste Umgebungsbreite unterhalb des Erwartungswerts für eine Mindestwahrscheinlichkeit ermitteln (E4) · Kumulierte Binomialwahrscheinlichkeit und Pfadwahrscheinlichkeit einer festen Anfangsfolge berechnen (E3) · Obere Grenze einer im Diagramm markierten kumulierten Wahrscheinlichkeit über den Erwartungswert ermitteln (E5) · Parameter n und p aus einem Verhältnis zweier Einzelwahrscheinlichkeiten und dem Erwartungswert berechnen (E4) · Stichprobenumfang aus dem Erwartungswert berechnen und Einzelwahrscheinlichkeit ermitteln (E2) · Stichprobenumfang zu einer vorgegebenen Einzelwahrscheinlichkeit mit dem Rechner suchen (E4) · Summenbedingung bei wiederholtem Wurf in eine Binomialwahrscheinlichkeit übersetzen und nachweisen (E3) · Summenterme der Binomialverteilung auf ein vorgegebenes Mindestens-Ereignis prüfen und begründen (E3) · Trefferwahrscheinlichkeit aus einer Gleichung zweier Einzelwahrscheinlichkeiten berechnen (E4) · Trefferwahrscheinlichkeit aus einer kumulierten Wahrscheinlichkeit auf ganze Prozent durch Probieren ermitteln (E4) · Verteilung der Gegenzufallsgröße im Diagramm darstellen (E5) · Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen (E3) · Wahrscheinlichkeit eines Intervalls aus dem Säulendiagramm einer Verteilung ablesen (E5) · Wahrscheinlichkeit eines symmetrischen Intervalls über die Symmetrie der Binomialverteilung berechnen (E5) · Wahrscheinlichkeit eines zweistufigen Prüfplans über Binomialwahrscheinlichkeiten berechnen (E3) · Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen (E1) · Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen (E5) · Wirkung eines kleineren Stichprobenumfangs auf eine Annahmewahrscheinlichkeit ohne Rechnung beurteilen (E4) · Zufallsgröße mit gleicher Binomialverteilung in einem anderen Experiment angeben (E1). Muster: In Teil B (mit Hilfsmitteln; Prüfungsteile nach [IQB-STR 1], Stochastik 15 bzw. 20 Bewertungseinheiten) beginnt fast jede Stochastik-Aufgabe des Pools mit ein bis zwei Wahrscheinlichkeiten am Rechner (kumuliert 16, einzeln 9 Zeilen, ein bis fünf Punkte, Anforderungsbereich I), dann folgen das Deuten eines Summenterms (10), eine Umkehraufgabe mit Nachbarwerten (Grenze k, Umgebung um μ, Umfang n; 13) oder eine Begründung am Modell; verkettete Modelle und Restwahrscheinlichkeiten tragen den Anforderungsbereich III (2023MerhoehtBStochastikWTR3-1c, 2023MgrundlegendBStochastikWTR2-2b). Teil A (28 Zeilen, ein bis fünf Punkte) prüft Term angeben (5), kleine Ketten über Pfade (3), Diagramme mit Symmetrie und Gegenzufallsgröße (9, seit dem Nachzug 2026-09-28 dazu das Intervall am Säulendiagramm 2017MgrundlegendAStochastik11-a), unpassende Diagramme (4), Sachaussagen zu Ungleichungen (2) und algebraische Umkehraufgaben (2), dazu je einmal eine Einzelwahrscheinlichkeit aus n und Erwartungswert und die Konstruktion einer gleichverteilten Zufallsgröße. Den Logarithmus-Weg stellt der Pool ab 2018 nicht; „Dreimal-mindestens“ kommt dort nur als Deutung eines Terms vor (2020MgrundlegendAStochastik2-b, 2023MerhoehtBStochastikWTR3-1a) – der grundlegende Pool 2017 (seit dem Nachzug im Eintrag) fragt die Mindestanzahl über das Gegenereignis dagegen zweimal (2017MgrundlegendBStochastikWTR1-2e, 2017MgrundlegendBStochastikWTR2-1c, je vier Punkte, Anforderungsbereich III). Der Jahrgang 2017 stellt sonst die Standardformen: Modalwert, Summenterm und Mindestanzahl an den Smartphones (2017MgrundlegendBStochastikWTR1-2c, 2017MgrundlegendBStochastikWTR1-2d, 2017MgrundlegendBStochastikWTR1-2e), Einzelwahrscheinlichkeiten an der Fahrzeugstatistik (2017MgrundlegendBStochastikWTR2-1a) und am Saatgut (2017MerhoehtBStochastikWTR-1c), in der CAS-Fassung die Haushaltsgrößen mit Einzelwahrscheinlichkeit, Summenterm und Mindestumfang (2017MerhoehtBStochastikCAS1-1a, 2017MerhoehtBStochastikCAS1-1b, 2017MerhoehtBStochastikCAS1-4) und die beidseitige prozentuale Abweichung in der Studie (2017MerhoehtBStochastikCAS2-2). Seit dem Nachzug 2026-09-29 mit sieben Zeilen der CAS-Fassungen (erhöht 2018, grundlegend 2017): Einzel- neben kumulierter Wahrscheinlichkeit an den Kunststoffteilen und an den nicht umlauffähigen Geldscheinen (2018MerhoehtBStochastikCAS1-1a, 2018MerhoehtBStochastikCAS2-1a, drei Punkte, Niveau I), der Mindestumfang durch Probieren mit dem Rechner an beiden Kontexten und an den Smartphones (2018MerhoehtBStochastikCAS1-1b, 2018MerhoehtBStochastikCAS2-1b, 2017MgrundlegendBStochastikCAS-2e, je vier Punkte, Anforderungsbereich III – die grundlegende CAS-Fassung fragt statt der Mindestanzahl über das Gegenereignis nach fünfhundert fehlerfreien Geräten) sowie Modalwert und Summenterm an den Smartphones, wortgleich mit dem WTR-Zweig (2017MgrundlegendBStochastikCAS-2c, 2017MgrundlegendBStochastikCAS-2d). Amtlicher Anforderungsbereich in allen 116 Zeilen; Niveau I 41, II 56, III 19 – seit Abgleichlauf 26 stehen fünf Umkehrzeilen auf III statt II (2017MgrundlegendBStochastikWTR1-2e, 2017MgrundlegendBStochastikWTR2-1c, 2017MerhoehtBStochastikCAS1-4, 2018MerhoehtBStochastikWTR1-1b, 2024MerhoehtBStochastikWTR1-1c: Mindestanzahl oder Mindestumfang für eine Mindestwahrscheinlichkeit, Deutungsliste (f)). Kontexte: Bildschirme, Pakete, Lehrkräfte, Briefe, Smartphone-Spiel, Würfelnetze, Flaschen und Säcke, Haushalte, Kunden, Smartphones, Fahrzeuge, Saatgut, Studie, Kunststoffteile, Geldscheine. 29 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste; 2018MgrundlegendBStochastikWTR2-1a wortgleich in der Berliner CAS-Fassung, abgewandelt im WTR-Heft), 9 abgewandelt.
135  Zielmarke: Einheit 1 – abi: Ungeeignetheit des Modells begründen (2018-be-gk-B3.2g, Niveau II) und Bernoulli-Bedingungen begründen (2022-bebb-gk-B4a); iqb: Aussagen über Bernoulli-Experiment und Bernoulli-Kette beurteilen (2018MgrundlegendBStochastikWTR3-2d, Niveau III) und eine gleichverteilte Zufallsgröße konstruieren (2024MerhoehtAStochastik23-b, Niveau III); Teil A beider Profile: mindestens zwei Treffer bei drei Versuchen nachweisen (2023-bebb-lk-A1.8a, 2023MerhoehtAStochastik22-a). Einheit 2 – abi: Einzelwahrscheinlichkeit mit Vergleich über den Erwartungswert (2018-bb-ea-B4.2c, Niveau III) und Formel neben Tabelle (2019-be-gk-B4.1a); iqb: Term angeben in Teil A (2026MgrundlegendAStochastik12-a, 2021MgrundlegendAStochastik2-a, Niveau I bis II) und Einzel- neben kumulierter Wahrscheinlichkeit mit Anteilsangabe (2018MerhoehtBStochastikWTR1-1a). Einheit 3 – abi: Gewinn und Extrapreis über die geteilte Kette (2022-bebb-lk-B4m, Niveau III) und Anzahlverhältnis (2023-bebb-gk-B4.1d); iqb: zwei Binomialmodelle verketten (2023MerhoehtBStochastikWTR3-1c, Niveau III), Restwahrscheinlichkeit nach bekannten Würfen (2023MgrundlegendBStochastikWTR2-2b, Niveau III), Ungleichung als Sachaussage (2024MgrundlegendAStochastik21-b, Niveau III). Einheit 4 – abi: Mindestanzahl mit Logarithmus (2017-bb-ea-B4.2b, 2023-bebb-gk-B4.1f, Niveau II) und p über die Wurzel (2018-be-gk-B3.2d, Niveau III); iqb: n und p aus Verhältnis und Erwartungswert (2025MerhoehtAStochastik21), Mindestumfang durch Probieren (2019MgrundlegendBStochastikWTR1-1b, Niveau III), Halbierung widerlegen (2022MerhoehtBStochastikWTR1-1f). Einheit 5 – abi: Symmetrie und kumulierte Werte (2025-bebb-gk-A1.9b, Niveau III), Widerspruch zur Symmetrie (2022-bebb-lk-A1.8b), unpassende Diagramme (2023-bebb-gk-A1.7b); iqb: Symmetrie um die Mitte zweier Werte (2021MgrundlegendAStochastik2-b, Niveau III), Aussagen an mehreren Verteilungen (2022MgrundlegendBStochastikWTR2-3a), Achsen skalieren (2025MgrundlegendBStochastikWTR2-1d).
````

## 2 Originale (130)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2017-be-gk-B3.1e (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Von im Werk A hergestellten Geräten werden 20 zufällig ausgewählt.
- gesucht: Wahrscheinlichkeit dafür, dass darunter kein fehlerhaftes Gerät ist
- verfahren: Anzahl X der fehlerhaften Geräte ist binomialverteilt mit n = 20 und p = 0,05; P(X = 0) = 0,95^20.
- fehlerquelle: mit dem Fehleranteil 3 % aller Geräte statt 5 % aus Werk A rechnen oder 1 − 0,95^20 angeben

### 2017-be-gk-B3.1f (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 4 · format Kurzantwort · antwort Zahl|Text
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Term 200 · 0,98^s · 0,02 + 0,98^200.
- gesucht: ein Wert von s, für den mit dem Term im Sachzusammenhang die Wahrscheinlichkeit eines Ereignisses berechnet werden kann; Beschreibung des zugehörigen Ereignisses
- verfahren: 0,02 ist der Fehleranteil in Werk D; 0,98^200 = P(X = 0) und 200 · 0,02 · 0,98^199 = P(X = 1) für n = 200, also s = 199 und die Summe P(X ≤ 1).
- fehlerquelle: s = 200 wählen oder das Ereignis als „genau eines fehlerhaft“ beschreiben

### 2017-be-gk-B3.1g (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Es werden im Werk C hergestellte Geräte zufällig ausgewählt.
- gesucht: Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 95 % mindestens ein fehlerhaftes Gerät befindet
- verfahren: Über das Gegenereignis 1 − 0,96^n ≥ 0,95 ansetzen und durch Logarithmieren oder Probieren nach n auflösen.
- fehlerquelle: n ≈ 73,4 abrunden oder mit 0,04^n statt 0,96^n ansetzen

### 2017-be-gk-B3.2c (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze. Lisa dreht das Glücksrad G1 zehnmal. C1: G1 zeigt genau viermal Rot. C2: G1 zeigt mindestens fünfmal Rot. Kontrollangabe: P(C2) ≈ 0,3669.
- gesucht: Wahrscheinlichkeiten der Ereignisse C1 und C2
- verfahren: X: Anzahl Rot, binomialverteilt mit n = 10 und p = 0,4. P(C1) = P(X = 4) mit der Bernoulli-Formel oder als Differenz P(X ≤ 4) − P(X ≤ 3) aus der Tabelle; P(C2) = 1 − P(X ≤ 4).
- fehlerquelle: P(X ≥ 5) als 1 − P(X ≤ 5) ablesen oder p = 0,5 annehmen, weil Rot und Blau gleich viele Felder haben

### 2017-be-gk-B3.2d (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze. Das zehnmalige Drehen von G1 wird 30-mal durchgespielt; C2: G1 zeigt dabei mindestens fünfmal Rot, P(C2) ≈ 0,3669. Tom behauptet, die Wahrscheinlichkeit, dass C2 in genau der Hälfte aller Fälle eintritt, liege unter 5 %.
- gesucht: Prüfung der Behauptung
- verfahren: Y: Anzahl der Durchgänge mit C2, binomialverteilt mit n = 30 und p = 0,3669. P(Y = 15) = (30 über 15) · 0,3669^15 · 0,6331^15 berechnen und mit 0,05 vergleichen.
- fehlerquelle: mit p = 0,4 (Rot bei einer Drehung) statt mit P(C2) rechnen oder P(Y ≤ 15) statt P(Y = 15) bilden

### 2017-be-gk-B3.2e (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze. Das Glücksrad G1 (Rot mit Wahrscheinlichkeit 0,4) soll 20-mal gedreht werden.
- gesucht: Wahrscheinlichkeit dafür, dass unter den ersten zehn Drehungen genau fünfmal Rot und insgesamt höchstens neunmal Rot das Ergebnis ist
- verfahren: Die Kette in die ersten und die letzten zehn Drehungen teilen: in den ersten genau 5 Treffer, in den letzten dann höchstens 4. Beide Abschnitte sind unabhängig und binomialverteilt mit n = 10, p = 0,4; P(X = 5) · P(X ≤ 4) aus der Tabelle bilden.
- fehlerquelle: für die zweiten zehn Drehungen höchstens neun Treffer ansetzen oder mit n = 20 und P(X ≤ 9) rechnen

### 2017-bb-ea-cas-B4.2b (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea-cas · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 72,6 % der deutschen Bevölkerung ab 14 Jahre lesen in ihrer Freizeit gern, die übrigen 27,4 % nicht.
- gesucht: Größte Anzahl zufällig ausgewählter Personen, für die die Wahrscheinlichkeit, wenigstens eine Person zu finden, die in ihrer Freizeit nicht gern liest, unter 98 % liegt
- verfahren: Gegenereignis: alle Ausgewählten lesen gern. Aus 1 − 0,726ⁿ < 0,98 folgt 0,726ⁿ > 0,02, also n < ln 0,02 / ln 0,726 ≈ 12,22; abrunden und mit n = 12 und n = 13 prüfen.
- fehlerquelle: wie bei der Mindestanzahl aufrunden oder beim Logarithmieren mit negativem Logarithmus das Ungleichheitszeichen nicht umdrehen

### 2017-bb-ea-cas-B4.2d (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea-cas · punkte 4 · format Rechnung|Kurzantwort · antwort Term|Zahl
- gegeben: Ein Buchhändler organisiert eine Lesung in einem Saal mit 175 Plätzen. Da im Mittel 6 % der bestellten Karten storniert werden, lässt er 180 Kartenreservierungen annehmen. k ist die Anzahl der stornierten Karten.
- gesucht: Term für P(k), mit dem die Wahrscheinlichkeit für genau k Stornierungen berechnet werden kann; größter Wert dieser Wahrscheinlichkeit
- verfahren: Bernoulli-Kette mit n = 180 und p = 0,06: P(k) = C(180; k) · 0,06^k · 0,94^(180 − k). Der größte Wert liegt beim Modalwert in der Nähe des Erwartungswerts n · p = 10,8; die Werte um 10 und 11 mit dem CAS vergleichen.
- fehlerquelle: den größten Wert beim gerundeten Erwartungswert 11 vermuten oder die Stornierungen mit p = 0,94 als Treffer ansetzen

### 2017-be-gk-cas-B3.1e (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Von im Werk A hergestellten Geräten werden 250 zufällig ausgewählt; X: Anzahl der fehlerhaften, binomialverteilt mit n = 250 und p = 0,05.
- gesucht: die Anzahl fehlerhafter Geräte, die darunter mit der größten Wahrscheinlichkeit auftritt
- verfahren: Erwartungswert 250 · 0,05 = 12,5 ist nicht ganzzahlig; P(X = 12) und P(X = 13) berechnen und vergleichen.
- fehlerquelle: 12,5 oder aufgerundet 13 als Anzahl angeben

### 2017-be-gk-cas-B3.1g (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Es werden im Werk C hergestellte Geräte zufällig ausgewählt.
- gesucht: Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 90 % mindestens 500 Geräte befinden, die nicht fehlerhaft sind
- verfahren: X: Anzahl der nicht fehlerhaften Geräte, binomialverteilt mit p = 0,96; das kleinste n mit P(X >= 500) >= 0,9 durch Probieren mit dem Rechner suchen.
- fehlerquelle: mit p = 0,04 (fehlerhaft) rechnen oder n aus dem Erwartungswert 500/0,96 ≈ 521 bestimmen

### 2017-be-gk-cas-B3.2c (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze. Lisa dreht das Glücksrad G1 zehnmal. C1: G1 zeigt genau viermal Rot. C2: G1 zeigt mindestens fünfmal Rot. Kontrollangabe: P(C2) ≈ 0,3669.
- gesucht: Wahrscheinlichkeiten der Ereignisse C1 und C2
- verfahren: X: Anzahl Rot, binomialverteilt mit n = 10 und p = 0,4. P(C1) = P(X = 4) mit der Bernoulli-Formel oder dem Rechner; P(C2) = 1 − P(X ≤ 4) mit dem Rechner.
- fehlerquelle: P(X ≥ 5) als 1 − P(X ≤ 5) ablesen oder p = 0,5 annehmen, weil Rot und Blau gleich viele Felder haben

### 2017-be-gk-cas-B3.2d (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 4 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze. Lisa dreht das Glücksrad G1 zehnmal; C2: G1 zeigt mindestens fünfmal Rot, P(C2) ≈ 0,3669. Tom spielt das zehnmalige Drehen in Gedanken 30-mal durch und bestimmt die Wahrscheinlichkeit dafür, dass C2 genau i-mal eintritt (i = 0; 1; …; 30). Er behauptet, dass für genau fünf Werte von i diese Wahrscheinlichkeit größer als 10 % ist.
- gesucht: Prüfung der Behauptung
- verfahren: Y: Anzahl der Durchgänge mit C2, binomialverteilt mit n = 30 und p = P(C2) ≈ 0,3669. Mit dem CAS die Einzelwahrscheinlichkeiten P(Y = i) für i = 0 bis 30 tabellieren und die Werte über 0,1 zählen; die Verteilung steigt bis i = 11 (Erwartungswert ≈ 11) und fällt danach, es genügt also, die Werte um den Erwartungswert und ihre Nachbarn zu prüfen.
- fehlerquelle: mit p = 0,4 (Rot bei einer Drehung) statt mit P(C2) rechnen oder kumulierte statt Einzelwahrscheinlichkeiten mit 10 % vergleichen

### 2018-be-gk-cas-B3.1b (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Ein Spieler spielt das Spiel mit der Gewinnwahrscheinlichkeit p = 0,4 zehnmal; nach jedem Spiel werden die Kugeln zurückgelegt. Ereignis A: genau 4 der 10 Spiele gewonnen. Ereignis B: das erste Spiel gewonnen und von den übrigen 9 noch mindestens vier.
- gesucht: Wahrscheinlichkeiten der Ereignisse A und B
- verfahren: A mit der Binomialformel für n = 10, p = 0,4 und k = 4 berechnen. B in zwei unabhängige Teile zerlegen: das erste Spiel gewinnen mit 0,4, und von den übrigen 9 Spielen mindestens vier gewinnen, also P(Y ≥ 4) = 1 − P(Y ≤ 3) mit n = 9 (kumuliert, mit dem Rechner); die beiden Wahrscheinlichkeiten multiplizieren.
- fehlerquelle: bei B mit n = 10 statt mit n = 9 für den zweiten Teil rechnen oder mindestens vier als mehr als vier lesen

### 2018-be-gk-cas-B3.2a (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Im Mittel ist einer von fünf Bildschirmen fehlerhaft, die Anzahl fehlerhafter Geräte unter zufällig ausgewählten ist binomialverteilt mit p = 0,2. Ereignis A: von 50 zufällig ausgewählten Bildschirmen sind höchstens 8 fehlerhaft. Ereignis B: von 200 zufällig ausgewählten Bildschirmen sind mehr als 30 und weniger als 50 fehlerhaft.
- gesucht: Wahrscheinlichkeiten der Ereignisse A und B
- verfahren: A ist P(X ≤ 8) mit n = 50; B ist P(31 ≤ Y ≤ 49) = P(Y ≤ 49) − P(Y ≤ 30) mit n = 200; beide kumulierten Werte mit dem Rechner.
- fehlerquelle: bei mehr als 30 und weniger als 50 die Grenzen einschließen und P(Y ≤ 50) − P(Y ≤ 30) oder P(Y ≤ 49) − P(Y ≤ 29) rechnen

### 2018MgrundlegendBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Flachbildschirme, im Mittel einer von fünf fehlerhaft; die Anzahl fehlerhafter Geräte unter zufällig ausgewählten ist binomialverteilt (p = 0,2)
- gesucht: P(A): von 50 höchstens 8 fehlerhaft; P(B): von 200 mehr als 30 und weniger als 50 fehlerhaft
- verfahren: P(X ≤ 8) mit n = 50; P(X ≤ 49) − P(X ≤ 30) mit n = 200
- fehlerquelle: bei B die Grenzen 30 und 50 einschließen

### 2018-be-gk-B3.2a (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Im Mittel ist einer von fünf Bildschirmen fehlerhaft, die Anzahl fehlerhafter Geräte ist binomialverteilt mit p = 0,2. Es werden 50 Bildschirme zufällig ausgewählt. Ereignis A: höchstens 8 fehlerhaft. Ereignis B: mehr als 10 und weniger als 15 fehlerhaft.
- gesucht: Wahrscheinlichkeiten der Ereignisse A und B
- verfahren: A ist P(X ≤ 8) und wird direkt aus der Tabelle abgelesen. B ist P(11 ≤ X ≤ 14) = P(X ≤ 14) − P(X ≤ 10); beide Werte ablesen und subtrahieren.
- fehlerquelle: bei mehr als 10 und weniger als 15 die Grenzen einschließen und P(X ≤ 15) − P(X ≤ 9) rechnen

### 2019-be-gk-B4.1a (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: In einem Land besitzen 80 % der Erwachsenen einen Führerschein; 100 Erwachsene werden zufällig ausgewählt, die Anzahl X der Führerscheinbesitzer darunter gilt als binomialverteilt; Tabelle der summierten Binomialverteilung n = 100 in der Anlage
- gesucht: P(E1): genau 80 Führerscheinbesitzer; P(E2): höchstens 75 Führerscheinbesitzer
- verfahren: E1 mit der Bernoulli-Formel; E2 aus der Tabelle über das Gegenereignis (Anzahl ohne Führerschein ≥ 25 bei p = 0,2)
- fehlerquelle: die Tabelle für p = 0,8 nicht „von unten“ lesen (1 − Tabellenwert)

### 2020-be-gk-B4.2a (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: In einem großen Unternehmen ist 1/3 der Beschäftigten weiblich; 50 Beschäftigte werden zufällig ausgewählt, die Anzahl X der weiblichen darunter ist binomialverteilt (n = 50, p = 1/3); Tabelle in der Anlage
- gesucht: P(mindestens 17 weibliche unter den 50)
- verfahren: 1 − F(50; 1/3; 16) aus der Tabelle
- fehlerquelle: P(X ≤ 17) statt P(X ≤ 16) abziehen

### 2021-be-gk-B4a (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Smartphone-Spiel: jeden Sonntag zehn Versuche, je Versuch mit 40 % ein Stern; X = Anzahl der Sterne bei zehn Versuchen, binomialverteilt (n = 10, p = 0,4); Tabelle in der Anlage
- gesucht: P(A): mehr als sechs Sterne; P(B): mindestens fünf, höchstens acht Sterne
- verfahren: Kumulierte Werte aus der Tabelle kombinieren
- fehlerquelle: P(X ≤ 5) statt P(X ≤ 4) abziehen

### 2022-bebb-gk-B4b (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Paketzentrum: 10 % der Pakete haben das Ziel A, 7 % das Ziel B; Anlage mit Tabelle der summierten Binomialverteilung; 100 zufällig ausgewählte Pakete
- gesucht: P(genau neun mit Ziel B); P(weniger als neun mit Ziel B)
- verfahren: Werte aus der Tabelle (p = 0,07, n = 100)
- fehlerquelle: P(X < 9) als F(9) lesen

### 2022-bebb-lk-B4d (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: 100 zufällig ausgewählte Kunden; p = 0,59
- gesucht: Wahrscheinlichkeit, dass höchstens 50 % Datenschutzbedenken haben
- verfahren: summierte Binomialverteilung aus der Tabelle oder am Rechner
- fehlerquelle: X < 50 oder Gegenereignis (mehr als 50 %) gerechnet

### 2018-bb-ea-B4.2c (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen sind. Ereignis C: von 20 zufällig ausgewählten Personen sind genau neun Brillenträger. Ereignis D: von 20 zufällig ausgewählten Personen sind genau zwölf Brillenträger.
- gesucht: Wahrscheinlichkeit des Ereignisses C|Begründung mit Hilfe des Erwartungswertes, ob die Wahrscheinlichkeit von D größer oder kleiner ist als die von C
- verfahren: P(C) mit der Binomialformel für 20 Versuche, die Trefferwahrscheinlichkeit 0,625 und neun Treffer berechnen. Für den Vergleich den Erwartungswert 20 · 0,625 = 12,5 bilden. Die Binomialverteilung hat ihr Maximum beim Erwartungswert und fällt zu beiden Seiten ab; zwölf liegt mit Abstand 0,5 viel näher daran als neun mit Abstand 3,5, also ist P(D) größer als P(C).
- fehlerquelle: P(D) ausrechnen und vergleichen, obwohl die Begründung ausdrücklich über den Erwartungswert verlangt ist

### 2018-be-gk-B3.2d (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Nach einer Verbesserung soll die Wahrscheinlichkeit dafür, dass unter 25 zufällig ausgewählten Bildschirmen keiner fehlerhaft ist, mindestens 10 Prozent betragen.
- gesucht: höchster Anteil fehlerhafter Geräte nach der Verbesserung
- verfahren: Ansatz (1 − p)²⁵ ≥ 0,1 aufstellen und die 25. Wurzel ziehen: 1 − p ≥ 0,1^(1/25) ≈ 0,9120, also p ≤ 0,0880.
- fehlerquelle: beim Ziehen der Wurzel das Ungleichheitszeichen falsch umdrehen oder p und 1 − p verwechseln

### 2022-bebb-lk-B4f (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Rechnung|Begründung · antwort Text
- gegeben: Aussage: bei 2n Kunden ist P(niemand hat Bedenken) halb so groß wie bei n Kunden
- gesucht: ob es ein n > 0 gibt, für das die Aussage richtig ist
- verfahren: Beide Wahrscheinlichkeiten als Potenzen von 0,41 vergleichen
- fehlerquelle: für einzelne n rechnen statt allgemein

### 2022-bebb-lk-B4m (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Glücksrad mit Sonne (S, p = 0,7) und Mond (M, 0,3), siebenmal gedreht, Anordnung aus sieben Symbolen; Gewinn bei mehr als drei Monden; Extrapreis bei genau zwei Sonnen an den vorderen fünf Stellen
- gesucht: P(Gewinn und Extrapreis)
- verfahren: Extrapreis legt drei Monde vorn fest; Gewinn braucht dann mindestens einen Mond unter den letzten zwei; Produkt
- fehlerquelle: Ereignisse als unabhängig multiplizieren (P(Gewinn) · P(Extrapreis)); die letzten zwei Drehungen vergessen

### 2024-bebb-lk-B4c (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 30 % der Abonnenten älter als 40; mit mindestens 99 % mehr als fünf Ältere unter n Ausgewählten
- gesucht: kleinstes n
- verfahren: P(X > 5) für n = 39 und 40 vergleichen
- fehlerquelle: P(X ≥ 5) statt P(X > 5)

### 2025-bebb-gk-A1.9b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: X binomialverteilt mit p = 0,5, symmetrisch um 10,5; P(X >= 9) ≈ 0,81 und P(X = 12) ≈ 0,14
- gesucht: Näherungswert für P(X = 10) unter Verwendung dieser Werte
- verfahren: wegen der Symmetrie P(X = 9) = P(X = 12) ≈ 0,14 und P(X >= 11) = 0,5; P(X = 10) = P(X >= 9) − P(X = 9) − P(X >= 11)
- fehlerquelle: P(X >= 11) mit 0,81 − 0,14 verwechseln oder die Symmetrie nicht nutzen

### 2023MerhoehtBStochastikWTR3-1c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Karton fehlerhaft, wenn mehr als eine Flasche unter 600 ml; Lieferung 150 Kartons
- gesucht: Wahrscheinlichkeit, dass mehr als 3 % der Kartons fehlerhaft sind
- verfahren: Fehlerwahrscheinlichkeit eines Kartons binomial, dann Binomialverteilung über die Kartons mit Z ≥ 5
- fehlerquelle: „mehr als 3 %“ als Z ≥ 4 oder Y ≥ 1 statt Y ≥ 2

### 2023MgrundlegendBStochastikWTR2-2b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 7500 Würfe, davon 1500 mit 285-mal „6“ bekannt; p(„6“) = 1/6
- gesucht: Wahrscheinlichkeit, dass bei höchstens 17 % der 7500 Würfe die „6“ erzielt wird
- verfahren: Bedingung 285 + k ≤ 0,17 · 7500 nach k auflösen, Binomialverteilung für die restlichen 6000 Würfe
- fehlerquelle: alle 7500 Würfe als zufällig ansetzen (P(Z ≤ 1275) statt P(Y ≤ 990))

### 2017MgrundlegendAStochastik11-a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Abbildung der Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße X mit den Parametern n und p
- gesucht: P(5 <= X <= 7) mithilfe der Abbildung
- verfahren: Die Höhen der Säulen bei 5, 6 und 7 ablesen und addieren
- fehlerquelle: die Säule bei 7 oder bei 5 weglassen (strikte statt nicht strikte Ungleichung)

### 2020MgrundlegendAStochastik2-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 3 · format Kurzantwort · antwort Text
- gegeben: X2 binomialverteilt mit n2 und p2 = 0,2; Ansatz 1 − 0,8^(n2) < 0,3
- gesucht: eine Aufgabenstellung, die sich mit diesem Ansatz lösen lässt
- verfahren: Term als Wahrscheinlichkeit für mindestens einen Treffer deuten, Ungleichung als Bedingung an n
- fehlerquelle: 0,8^n als Wahrscheinlichkeit für mindestens einen Treffer deuten

### 2023MerhoehtBStochastikWTR3-1a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: Karton mit zwölf Flaschen; P(Flasche unter 600 ml) = 1,5 %; Rechnung 0,985¹² ≈ 83,4 %
- gesucht: passende Aufgabenstellung; Erläuterung des Ansatzes
- verfahren: 0,985 als Gegenwahrscheinlichkeit je Flasche, Potenz 12 als alle Flaschen des Kartons
- fehlerquelle: „höchstens eine Flasche zu wenig“ formulieren (das wäre der Karton ohne Fehler, ein anderer Term)

### 2017MgrundlegendBStochastikWTR1-2e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; es werden im Werk C hergestellte Geräte zufällig ausgewählt
- gesucht: Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 95 % mindestens ein fehlerhaftes Gerät befindet
- verfahren: Über das Gegenereignis 1 − 0,96^n ≥ 0,95 ansetzen und durch Logarithmieren oder Probieren nach n auflösen
- fehlerquelle: n ≈ 73,4 abrunden oder mit 0,04^n statt 0,96^n ansetzen

### 2017MgrundlegendBStochastikWTR2-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 20 % aller Pkw eines bestimmten Herstellers sind Dieselfahrzeuge; die Anzahl der Dieselfahrzeuge in einer Stichprobe gilt als binomialverteilt
- gesucht: Mindestanzahl zufällig ausgewählter Pkw des Herstellers, damit die Wahrscheinlichkeit, dass darunter mindestens ein Dieselfahrzeug ist, mindestens 95 % beträgt
- verfahren: Über das Gegenereignis 1 − 0,8^n ≥ 0,95 ansetzen und nach n auflösen
- fehlerquelle: n ≈ 13,4 abrunden

### 2017MgrundlegendBStochastikWTR1-2c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; von im Werk A hergestellten Geräten werden 250 zufällig ausgewählt; X: Anzahl der fehlerhaften, binomialverteilt mit n = 250 und p = 0,05
- gesucht: die Anzahl fehlerhafter Geräte, die darunter mit der größten Wahrscheinlichkeit auftritt
- verfahren: Erwartungswert 250 · 0,05 = 12,5 ist nicht ganzzahlig; P(X = 12) und P(X = 13) berechnen und vergleichen
- fehlerquelle: 12,5 oder aufgerundet 13 als Anzahl angeben

### 2017MgrundlegendBStochastikWTR1-2d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 4 · format Kurzantwort · antwort Zahl|Text
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; Term 200 · 0,98^s · 0,02 + 0,98^200
- gesucht: ein Wert von s, für den mit dem Term im Sachzusammenhang die Wahrscheinlichkeit eines Ereignisses berechnet werden kann, und Beschreibung des zugehörigen Ereignisses
- verfahren: 0,02 ist der Fehleranteil in Werk D; 0,98^200 = P(X = 0) und 200 · 0,02 · 0,98^199 = P(X = 1) für n = 200, also s = 199 und die Summe P(X ≤ 1)
- fehlerquelle: s = 200 wählen oder das Ereignis als „genau eines fehlerhaft“ beschreiben

### 2017MgrundlegendBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: 20 % aller Pkw eines bestimmten Herstellers sind Dieselfahrzeuge; die Anzahl der Dieselfahrzeuge in einer Stichprobe gilt modellhaft als binomialverteilt; 25 Pkw des Herstellers werden zufällig ausgewählt, davon sind drei rot; A: unter den ausgewählten Pkw sind genau acht Dieselfahrzeuge; B: unter den ausgewählten Pkw sind mindestens fünf Dieselfahrzeuge
- gesucht: Wahrscheinlichkeiten der Ereignisse A und B
- verfahren: X: Anzahl der Dieselfahrzeuge, B(25; 0,2); P(X = 8) und P(X ≥ 5) = 1 − P(X ≤ 4) mit dem Rechner
- fehlerquelle: P(X ≥ 5) als 1 − P(X ≤ 5) rechnen

### 2017MerhoehtBStochastikWTR-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ein Großhändler bietet Samenkörner für Salatgurken in zwei Qualitätsstufen an: ein Samenkorn der Stufe A keimt mit 95 %, eines der Stufe B mit 70 %; ein Gemüseanbaubetrieb kauft Samenkörner beider Stufen, davon 65 % der Stufe A, und sät alle; E: von 200 gesäten Samenkörnern der Qualitätsstufe B keimen genau 140; F: von 200 gesäten Samenkörnern der Qualitätsstufe B keimen mehr als 130 und weniger als 150
- gesucht: Wahrscheinlichkeiten der Ereignisse E und F
- verfahren: X binomialverteilt mit n = 200 und p = 0,7; P(X = 140) und P(131 <= X <= 149) = P(X <= 149) − P(X <= 130)
- fehlerquelle: P(X <= 150) − P(X <= 130) mit den Grenzen 150 und 130 einschließlich rechnen

### 2017MerhoehtBStochastikCAS1-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Anteile der Haushalte in Deutschland 2013 nach Größe: 1-Personen-Haushalte 40,5 %, 2-Personen-Haushalte 34,5 %, 3-Personen-Haushalte 12,5 %, 4-Personen-Haushalte 9,2 %, Haushalte mit mindestens 5 Personen 3,3 %; für eine Umfrage 2013 werden 100 Haushalte zufällig ausgewählt; A: genau vierzig 1-Personen-Haushalte; B: mindestens die Hälfte der ausgewählten Haushalte sind Mehrpersonenhaushalte
- gesucht: Wahrscheinlichkeiten der Ereignisse A und B
- verfahren: X ~ B(100; 0,405): P(X = 40); Y ~ B(100; 0,595) für die Mehrpersonenhaushalte: P(Y >= 50)
- fehlerquelle: für B die Wahrscheinlichkeit der Mehrpersonenhaushalte als 1 − 0,033 statt 1 − 0,405 nehmen

### 2017MerhoehtBStochastikCAS1-1b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Anteile der Haushalte in Deutschland 2013 nach Größe: 1-Personen-Haushalte 40,5 %, 2-Personen-Haushalte 34,5 %, 3-Personen-Haushalte 12,5 %, 4-Personen-Haushalte 9,2 %, Haushalte mit mindestens 5 Personen 3,3 %; 100 Haushalte werden zufällig ausgewählt; Term 1 − (0,967^100 + 100 · 0,033 · 0,967^99)
- gesucht: Bedeutung des Terms im Sachzusammenhang
- verfahren: 0,033 ist der Anteil der Haushalte mit mindestens 5 Personen; die Summe ist P(X = 0) + P(X = 1), der Term also P(X >= 2)
- fehlerquelle: „höchstens einer“ statt „mindestens zwei“ angeben

### 2017MerhoehtBStochastikCAS1-4 (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Anteile der Haushalte in Deutschland 2013 nach Größe: 1-Personen-Haushalte 40,5 %, 2-Personen-Haushalte 34,5 %, 3-Personen-Haushalte 12,5 %, 4-Personen-Haushalte 9,2 %, Haushalte mit mindestens 5 Personen 3,3 %; Anteil der 2-Personen-Haushalte 34,5 %
- gesucht: wie viele Haushalte man 2013 mindestens hätte auswählen müssen, damit darunter mit einer Wahrscheinlichkeit von mindestens 95 % mehr als zwanzig 2-Personen-Haushalte sind
- verfahren: Für Y ~ B(n; 0,345) das kleinste n mit P(Y > 20) >= 0,95 durch Probieren mit dem Rechner suchen
- fehlerquelle: P(Y >= 20) statt P(Y > 20) ansetzen

### 2017MerhoehtBStochastikCAS2-2 (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Bei 1 % der Bevölkerung Deutschlands liegt eine Glutenunverträglichkeit vor; für eine Studie werden 20 000 Personen zufällig ausgewählt; X ist die Anzahl der ausgewählten Personen mit Glutenunverträglichkeit
- gesucht: in einem geeigneten Modell die Wahrscheinlichkeit, dass X um mehr als 10 % vom Erwartungswert abweicht
- verfahren: X ~ B(20 000; 0,01), E(X) = 200; mehr als 10 % Abweichung heißt X < 180 oder X > 220; 1 − P(180 <= X <= 220)
- fehlerquelle: die Grenzen 180 und 220 dem Abweichungsbereich zuschlagen

### 2018MerhoehtBStochastikCAS1-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ein Unternehmen stellt Kunststoffteile her; erfahrungsgemäß sind 4 % der hergestellten Teile fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten kann als binomialverteilt angenommen werden; 800 Teile werden zufällig ausgewählt; A: genau 30 der Teile sind fehlerhaft; B: mindestens 5 % der Teile sind fehlerhaft
- gesucht: Wahrscheinlichkeiten der Ereignisse A und B
- verfahren: Einzel- und kumulierte Wahrscheinlichkeit mit n = 800, p = 0,04; 5 % von 800 sind 40
- fehlerquelle: „mindestens 5 %“ als X >= 5 lesen oder P(X > 40) statt P(X >= 40) berechnen

### 2018MerhoehtBStochastikCAS2-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Wird den Tageseinnahmen eines Cafés ein Geldschein zufällig entnommen, so ist er mit der Wahrscheinlichkeit 2 % nicht mehr umlauffähig; unter den Tageseinnahmen befinden sich insgesamt 200 Geldscheine
- gesucht: Wahrscheinlichkeit, dass darunter ausschließlich umlauffähige Scheine sind; Wahrscheinlichkeit, dass darunter höchstens zwei nicht mehr umlauffähige Scheine sind
- verfahren: Y ~ B(200; 0,02) für die nicht mehr umlauffähigen Scheine: P(Y = 0) und P(Y <= 2)
- fehlerquelle: P(Y < 2) statt P(Y <= 2) berechnen

### 2018MerhoehtBStochastikCAS1-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Unternehmen stellt Kunststoffteile her; erfahrungsgemäß sind 4 % der hergestellten Teile fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten kann als binomialverteilt angenommen werden
- gesucht: Mindestanzahl zufällig auszuwählender Teile, damit davon mit einer Wahrscheinlichkeit von mindestens 95 % mindestens 100 Teile keinen Fehler haben
- verfahren: Y ~ B(n; 0,96) für die fehlerfreien Teile; das kleinste n mit P(Y >= 100) >= 0,95 durch Probieren mit dem Rechner suchen
- fehlerquelle: mit p = 0,04 (fehlerhaft) statt 0,96 rechnen oder n = 100 annehmen

### 2018MerhoehtBStochastikCAS2-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Wird den Tageseinnahmen eines Cafés ein Geldschein zufällig entnommen, so ist er mit der Wahrscheinlichkeit 2 % nicht mehr umlauffähig
- gesucht: Anzahl der Geldscheine, die mindestens zu den Tageseinnahmen gehören müssen, damit darunter mit einer Wahrscheinlichkeit von mehr als 90 % mindestens vier nicht mehr umlauffähige Scheine sind
- verfahren: Für Y ~ B(n; 0,02) das kleinste n mit P(Y >= 4) > 0,9 durch Probieren mit dem Rechner suchen
- fehlerquelle: über den Erwartungswert n · 0,02 = 4 den Wert n = 200 ansetzen oder P(Y > 4) prüfen

### 2017MgrundlegendBStochastikCAS-2e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; es werden im Werk C hergestellte Geräte zufällig ausgewählt
- gesucht: Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 90 % mindestens 500 Geräte befinden, die nicht fehlerhaft sind
- verfahren: X: Anzahl der nicht fehlerhaften Geräte, binomialverteilt mit p = 0,96; das kleinste n mit P(X >= 500) >= 0,9 durch Probieren mit dem Rechner suchen
- fehlerquelle: mit p = 0,04 (fehlerhaft) rechnen oder n aus dem Erwartungswert 500/0,96 ≈ 521 bestimmen

### 2017MgrundlegendBStochastikCAS-2c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; von im Werk A hergestellten Geräten werden 250 zufällig ausgewählt; X: Anzahl der fehlerhaften, binomialverteilt mit n = 250 und p = 0,05
- gesucht: die Anzahl fehlerhafter Geräte, die darunter mit der größten Wahrscheinlichkeit auftritt
- verfahren: Erwartungswert 250 · 0,05 = 12,5 ist nicht ganzzahlig; P(X = 12) und P(X = 13) berechnen und vergleichen
- fehlerquelle: 12,5 oder aufgerundet 13 als Anzahl angeben

### 2017MgrundlegendBStochastikCAS-2d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 4 · format Kurzantwort · antwort Zahl|Text
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; Term 200 · 0,98^s · 0,02 + 0,98^200
- gesucht: ein Wert von s, für den mit dem Term im Sachzusammenhang die Wahrscheinlichkeit eines Ereignisses berechnet werden kann, und Beschreibung des zugehörigen Ereignisses
- verfahren: 0,02 ist der Fehleranteil in Werk D; 0,98^200 = P(X = 0) und 200 · 0,02 · 0,98^199 = P(X = 1) für n = 200, also s = 199 und die Summe P(X ≤ 1)
- fehlerquelle: s = 200 wählen oder das Ereignis als „genau eines fehlerhaft“ beschreiben

### 2018MerhoehtBStochastikWTR1-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Kunststoffteile, 4 % fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten ist binomialverteilt
- gesucht: Mindestanzahl zufällig ausgewählter Teile, sodass mit mindestens 95 % mindestens drei fehlerfrei sind
- verfahren: n = 3 und n = 4 mit Y ~ B(n; 0,96) prüfen
- fehlerquelle: mit p = 0,04 (fehlerhaft) statt 0,96 rechnen

### 2024MerhoehtBStochastikWTR1-1c (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 30 % der Abonnenten älter als 40; mit mindestens 99 % mehr als fünf Ältere unter n Ausgewählten
- gesucht: kleinstes n
- verfahren: P(X > 5) für n = 39 und 40 vergleichen
- fehlerquelle: P(X ≥ 5) statt P(X > 5)

### 2018-be-gk-B3.2g (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 2 · format Begründung · antwort Text
- gegeben: Von vierzig geprüften Bildschirmen, unter denen sechs fehlerhaft sind, werden nacheinander zehn zufällig ausgewählt.
- gesucht: Beurteilung, ob die Anzahl fehlerhafter Bildschirme unter den ausgewählten binomialverteilt ist
- verfahren: Prüfen, ob die Bedingungen einer Bernoulli-Kette erfüllt sind. Es wird aus einer festen Menge ohne Zurücklegen gezogen, die Wahrscheinlichkeit für ein fehlerhaftes Gerät ändert sich also von Zug zu Zug; bei zehn aus vierzig ist der Anteil zu groß, um das zu vernachlässigen.
- fehlerquelle: aus der festen Fehlerquote 6/40 auf eine konstante Trefferwahrscheinlichkeit schließen

### 2022-bebb-gk-B4a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: Paketzentrum: 10 % der Pakete haben das Ziel A, 7 % das Ziel B; Anlage mit Tabelle der summierten Binomialverteilung; 100 zufällig ausgewählte Pakete werden auf das Ziel B untersucht
- gesucht: Begründung, dass die Binomialverteilung verwendet werden kann
- verfahren: Bernoulli-Bedingungen nennen, Konstanz von p über die große Gesamtzahl
- fehlerquelle: nur „zwei Ausgänge“ nennen

### 2018MgrundlegendBStochastikWTR3-2d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Zwölfseitiger Spielwürfel, alle Seiten gleich wahrscheinlich, nach dem abgebildeten Netz neun Seiten mit 1 und drei Seiten mit 2 beschriftet; je Spiel wird viermal geworfen; Aussagen: (1) Ein Wurf mit Betrachtung der Zahl ist ein Bernoulli-Experiment; (2) bei mehreren Spielen jeweils festzuhalten, ob Trost- oder Hauptpreis vergeben wird, ist eine Bernoulli-Kette
- gesucht: Beurteilung beider Aussagen
- verfahren: (1) zwei mögliche Ergebnisse; (2) ein Spiel hat neben Trost- und Hauptpreis ein drittes Ergebnis (kein Preis, etwa Summe 5)
- fehlerquelle: (2) bejahen, weil nur zwei Preise genannt werden

### 2024MerhoehtAStochastik23-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: X binomialverteilt mit n = 4 und p = 1/4 (Tetraeder); anderes Experiment: ein roter und ein grüner Würfel (1 bis 6) werden viermal gleichzeitig geworfen
- gesucht: eine Zufallsgröße Z zu diesem Experiment mit derselben Verteilung wie X, mit Begründung
- verfahren: ein Ereignis je Doppelwurf mit Wahrscheinlichkeit 1/4 finden (9 von 36 Paaren) und Z als Anzahl der Würfe mit diesem Ereignis definieren
- fehlerquelle: ein Ereignis mit Wahrscheinlichkeit 1/6 (Pasch) wählen

### 2023-bebb-lk-A1.8a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 2 · format Rechnung · antwort Text
- gegeben: drei Kugeln werden nacheinander gewählt: bei Augenzahl 1 oder 2 gelb, sonst schwarz
- gesucht: Nachweis, dass mindestens zwei schwarze Kugeln mit Wahrscheinlichkeit 20/27 im Behälter liegen
- verfahren: P(genau 2) + P(genau 3) mit p = 2/3
- fehlerquelle: den Faktor 3 für die Anordnungen vergessen

### 2023MerhoehtAStochastik22-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Rechnung · antwort Text
- gegeben: drei Kugeln werden nacheinander gewählt: bei Augenzahl 1 oder 2 gelb, sonst schwarz
- gesucht: Nachweis, dass mindestens zwei schwarze Kugeln mit Wahrscheinlichkeit 20/27 im Behälter liegen
- verfahren: P(genau 2) + P(genau 3) mit p = 2/3
- fehlerquelle: den Faktor 3 für die Anordnungen vergessen

### 2026MgrundlegendAStochastik12-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Kurzantwort · antwort Term
- gegeben: eine Münze mit Zahl und Wappen wird fünfmal geworfen; Ergebnisse sind Abfolgen wie ZWZZW; Ereignis A: es wird höchstens einmal Wappen erzielt
- gesucht: Term, mit dem P(A) berechnet werden kann
- verfahren: P(kein Wappen) + P(genau einmal Wappen) mit (1/2)^5 und 5 · 1/2 · (1/2)^4
- fehlerquelle: den Faktor 5 für die Position des Wappens vergessen

### 2021MgrundlegendAStochastik2-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Kurzantwort · antwort Term
- gegeben: X binomialverteilt mit p = 1/4; Gleichung P(X = □) = (□ über 3) · (□)² · (1/4)³ mit Platzhaltern
- gesucht: vervollständigte Gleichung
- verfahren: Anzahl der Treffer 3 aus (1/4)³, n = 3 + 2, Nietenwahrscheinlichkeit 3/4
- fehlerquelle: n = 3 oder (1/4)² einsetzen

### 2018MerhoehtBStochastikWTR1-1a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Kunststoffteile, 4 % fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten ist binomialverteilt; 50 Teile zufällig ausgewählt
- gesucht: P(A): genau zwei fehlerhaft; P(B): mindestens 6 % fehlerhaft
- verfahren: Einzel- und kumulierte Wahrscheinlichkeit mit n = 50, p = 0,04
- fehlerquelle: „mindestens 6 %“ als X ≥ 6 lesen

### 2023-bebb-gk-B4.1d (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich. 100 Lehrkräfte werden zufällig ausgewählt.
- gesucht: Wahrscheinlichkeit, dass unter den 100 die Anzahl derer, die nicht am Gymnasium arbeiten, mindestens viermal so groß ist wie die Anzahl derer, die am Gymnasium arbeiten
- verfahren: X: Anzahl nicht am Gymnasium, binomialverteilt mit n = 100, p = 0,75; Bedingung X ≥ 4 · (100 − X) ⇔ X ≥ 80; P(X ≥ 80) = 1 − P(X ≤ 79) mit dem Rechner.
- fehlerquelle: X ≥ 75 (viermal so viele wie erwartet) statt X ≥ 80 ansetzen

### 2024MgrundlegendAStochastik21-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Kurzantwort · antwort Text
- gegeben: Gleichung 0,891 + 0,1 · 0,05 = 0,896; Ungleichung: Summe von k = 90 bis 100 über (100 über k) · 0,896^k · 0,104^(100 − k) > 0,5
- gesucht: eine Aussage im Sachzusammenhang, die sich aus Gleichung und Ungleichung ergibt
- verfahren: 0,896 als Wahrscheinlichkeit erkennen, dass ein Gerät als fehlerfrei eingestuft wird (beide Pfade); die Summe als P(X ≥ 90) für 100 Geräte lesen
- fehlerquelle: 0,896 als Anteil fehlerfreier Geräte deuten

### 2017-bb-ea-B4.2b (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 72,6 % der deutschen Bevölkerung ab 14 Jahre lesen in ihrer Freizeit gern, die übrigen 27,4 % nicht.
- gesucht: Mindestanzahl der Personen, die befragt werden müssten, um mit einer Mindestwahrscheinlichkeit von 98 % wenigstens eine Person zu finden, die nicht gern liest
- verfahren: Gegenereignis: alle Befragten lesen gern. Aus 1 − 0,726ⁿ ≥ 0,98 folgt 0,726ⁿ ≤ 0,02, also n ≥ ln 0,02 / ln 0,726; aufrunden.
- fehlerquelle: beim Logarithmieren einer Ungleichung mit negativem Logarithmus das Ungleichheitszeichen nicht umdrehen oder abrunden

### 2023-bebb-gk-B4.1f (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich. Lehrkräfte werden zufällig ausgewählt (Anteil am Gymnasium 25 %).
- gesucht: Mindestanzahl der Lehrkräfte, damit mit einer Wahrscheinlichkeit von mindestens 95 % mindestens eine davon an einem Gymnasium arbeitet
- verfahren: P(mindestens eine) = 1 − 0,75^n ≥ 0,95 ⇔ 0,75^n ≤ 0,05; logarithmieren (Ungleichung dreht sich, ln 0,75 < 0) oder Werte probieren: 0,75^10 ≈ 0,056, 0,75^11 ≈ 0,042.
- fehlerquelle: beim Logarithmieren das Ungleichheitszeichen nicht umdrehen; auf 10 abrunden

### 2025MerhoehtAStochastik21 (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: X binomialverteilt mit n und p, p < 1; P(X = 1) ist vierzehnmal so groß wie P(X = 0); E(X) = 10
- gesucht: Werte von p und n
- verfahren: beide Wahrscheinlichkeiten mit der Bernoulli-Formel ansetzen, durch (1 − p)^(n − 1) kürzen, n · p durch 10 ersetzen, p bestimmen und dann n aus n · p = 10
- fehlerquelle: (1 − p)^n nicht kürzen und mit n als Exponent stecken bleiben

### 2019MgrundlegendBStochastikWTR1-1b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Land mit 80 % Führerscheinbesitz unter Erwachsenen; 200 zufällig ausgewählte Erwachsene, X = Anzahl mit Führerschein, binomialverteilt (n = 200, p = 0,8)
- gesucht: Mindestanzahl Erwachsener, damit mit mindestens 90 % mehr als 160 einen Führerschein besitzen
- verfahren: P(X > 160) für wachsendes n berechnen, bis 90 % erreicht sind
- fehlerquelle: n aus 0,8n = 160 zu 200 schließen

### 2022MerhoehtBStochastikWTR1-1f (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung|Begründung · antwort Text
- gegeben: Aussage: bei 2n Kunden ist P(niemand hat Bedenken) halb so groß wie bei n Kunden
- gesucht: ob es ein n > 0 gibt, für das die Aussage richtig ist
- verfahren: Beide Wahrscheinlichkeiten als Potenzen von 0,41 vergleichen
- fehlerquelle: für einzelne n rechnen statt allgemein

### 2022-bebb-lk-A1.8b (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Begründung · antwort Text
- gegeben: X mit Werten 0 bis 4, symmetrische Verteilung, P(X = 2) = 0,6
- gesucht: Nachweis, dass X nicht binomialverteilt sein kann
- verfahren: n = 4 und p = 0,5 aus den Vorgaben, P(X = 2) = 0,375 im Widerspruch zu 0,6 (oder: maximal 6p²(1 − p)² ≤ 0,375)
- fehlerquelle: n = 5 (fünf Werte) statt n = 4 ansetzen

### 2023-bebb-gk-A1.7b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 3 · format Begründung · antwort Text
- gegeben: Zufallsgröße Y ist binomialverteilt mit n = 12 und p = 0,25; drei Abbildungen mit Säulendiagrammen, genau eine zeigt die Verteilung von Y.
- gesucht: begründete Entscheidung, welche Abbildung die Verteilung von Y zeigt
- verfahren: Erwartungswert 12 · 0,25 = 3: das Maximum muss bei k = 3 liegen (schließt Abb. 1 mit Maximum bei 5 aus); die Säulenhöhen müssen sich zu 1 addieren (in Abb. 3 ist allein die Säule bei 3 über 0,5 und die Summe weit über 1). Abb. 2 erfüllt beides.
- fehlerquelle: Abb. 3 wählen, weil das Maximum bei 3 liegt, ohne die Summe zu prüfen

### 2021MgrundlegendAStochastik2-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: symmetrische Verteilung von Y im Diagramm (Symmetrie um 13,5); P(Y ≤ 15) ≈ 0,78, P(Y = 12) ≈ 0,13
- gesucht: P(Y = 14) aus diesen Werten
- verfahren: Symmetrie liefert P(Y = 15) und P(Y ≤ 13) = 0,5, dann Differenz
- fehlerquelle: Symmetrieachse bei 14 statt 13,5 annehmen

### 2022MgrundlegendBStochastikWTR2-3a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Wahrscheinlichkeitsverteilungen für die Anzahl der Erkrankten unter je 1000 Infizierten in drei Risikogruppen A, B, C (Abbildung); Aussage I: für B und C sind die Wahrscheinlichkeiten für genau 99 Erkrankte etwa gleich; Aussage II: die Ausbruchswahrscheinlichkeit ist für C geringer als für A und B
- gesucht: Beurteilung beider Aussagen
- verfahren: Säulenhöhen bei 99 vergleichen; Lage der Verteilungen mit p verknüpfen
- fehlerquelle: Breite der Verteilung als kleinere Wahrscheinlichkeit deuten

### 2025MgrundlegendBStochastikWTR2-1d (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 4 · format Rechnung|Eintragen · antwort Zahl
- gegeben: Abbildung der Verteilung von X ohne Achsenwerte
- gesucht: je ein geeigneter Wert auf beiden Achsen
- verfahren: Erwartungswert und zugehörige Wahrscheinlichkeit berechnen und eintragen
- fehlerquelle: 15 an eine beliebige Säule schreiben

### 2018-bb-ea-B4.1b (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Eine Umfrage ergab, dass zu medizinischen Fragen 73 % der Bevölkerung das Internet nutzen. 55 % der Internetnutzer nutzen Medinet, einen Ratgeber bei medizinischen Fragen, der nur im Internet verfügbar ist. Zwölf Personen werden zufällig ausgewählt.
- gesucht: Wahrscheinlichkeit dafür, dass sich unter den zwölf Personen genau zehn befinden, die das Internet nutzen
- verfahren: Die Auswahl als Bernoulli-Kette der Länge 12 mit der Trefferwahrscheinlichkeit 0,73 auffassen und die Binomialformel für zehn Treffer anwenden.
- fehlerquelle: den Binomialkoeffizienten weglassen und nur das Produkt der Einzelwahrscheinlichkeiten angeben

### 2024-bebb-lk-A1.9a (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Geräte einer großen Serie; ein zufällig ausgewähltes Gerät ist mit p = 0,2 defekt; zwei Geräte werden zufällig ausgewählt
- gesucht: P(genau eines der beiden Geräte ist defekt)
- verfahren: zwei Pfade (defekt–heil, heil–defekt) addieren
- fehlerquelle: Faktor 2 für die Reihenfolge vergessen (0,16)

### 2024MgrundlegendAStochastik12-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Rechnung · antwort Text
- gegeben: Glücksrad mit gleich großen Sektoren, 10 % davon grün; zweimal drehen
- gesucht: Nachweis, dass die Wahrscheinlichkeit für genau einmal grün 18 % beträgt
- verfahren: beide Pfade grün–nicht grün und nicht grün–grün addieren
- fehlerquelle: nur einen Pfad rechnen (0,09)

### 2020MgrundlegendBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Postunternehmen Q befördert jährlich etwa 60 Millionen Briefe und stellt 95 % aller Briefe am ersten Werktag nach der Einlieferung zu; für 2000 zufällig ausgewählte Briefe wird untersucht, ob sie am ersten Werktag zugestellt werden
- gesucht: Begründung, dass die Binomialverteilung für Vorhersagen geeignet ist
- verfahren: Bernoulli-Bedingungen im Sachzusammenhang nennen
- fehlerquelle: die Unabhängigkeit bzw. gleiche Wahrscheinlichkeit trotz Ziehens ohne Zurücklegen nicht begründen

### 2023MgrundlegendBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Würfelnetz mit Zahlen 2, 4, 2, 4 und 2, 2; 30 Würfe; X Anzahl der „4“
- gesucht: Begründung, dass X binomialverteilt mit p = 1/3 ist
- verfahren: Bernoulli-Bedingungen nennen und p aus dem Netz ablesen
- fehlerquelle: Unabhängigkeit der Würfe nicht genannt

### 2018MgrundlegendBStochastikWTR1-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Gruppe von zehn Jugendlichen, vier nutzen nur Smartphones, sechs nur Tablets; drei werden zufällig ausgewählt
- gesucht: Begründung, dass die Binomialverteilung für die Anzahl der Smartphone-Nutzer unter den Ausgewählten nicht geeignet ist
- verfahren: Auswahl ist Ziehen ohne Zurücklegen aus einer kleinen Gesamtheit, die Trefferwahrscheinlichkeit bleibt nicht konstant
- fehlerquelle: mit „zu wenige Versuche“ argumentieren

### 2018MgrundlegendBStochastikWTR2-1g (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Von 40 geprüften Bildschirmen, unter denen 6 fehlerhaft sind, werden 10 zufällig ausgewählt
- gesucht: Beurteilung, ob die Anzahl fehlerhafter Bildschirme unter den ausgewählten binomialverteilt ist
- verfahren: Bei Binomialverteilung wären 7 fehlerhafte unter den 10 möglich, es gibt aber nur 6
- fehlerquelle: Binomialverteilung wegen „fehlerhaft oder nicht“ bejahen

### 2018-bb-ea-B4.2b (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen sind. Ereignis A: von acht zufällig ausgewählten Personen sind alle Brillenträger. Ereignis B: von 20 zufällig ausgewählten Personen sind genau drei keine Brillenträger.
- gesucht: Wahrscheinlichkeiten der Ereignisse A und B
- verfahren: Für A ist die Trefferzahl gleich der Kettenlänge, also einfach 0,625 hoch 8. Für B die Trefferdefinition wechseln: Treffer ist jetzt kein Brillenträger mit der Wahrscheinlichkeit 0,375, gesucht sind genau drei Treffer bei 20 Versuchen. Gleichwertig lässt sich mit genau 17 Brillenträgern rechnen.
- fehlerquelle: bei B mit der Trefferwahrscheinlichkeit 0,625 und drei Treffern rechnen, also die Trefferdefinition nicht mitwechseln

### 2020-be-gk-B4.1a (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Zwei Würfel mit gleich wahrscheinlichen Seiten: 5er-Würfel mit den Seiten 5, 6, 1, 2, 5, 4 (P(5) = 1/3, P(4) = P(6) = P(1) = P(2) = 1/6), 6er-Würfel mit den Seiten 6, 1, 2, 4, 6, 5 (P(6) = 1/3, P(5) = P(4) = P(1) = P(2) = 1/6); der 6er-Würfel wird 10-mal geworfen
- gesucht: P(A): genau 4-mal eine 6; P(B): keine 6
- verfahren: Bernoulli-Formel mit p = 1/3
- fehlerquelle: p = 1/6 statt 1/3 (zwei Seiten zeigen die 6)

### 2026-bb-gk-A1.3a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Kurzantwort · antwort Term
- gegeben: eine Münze mit Zahl und Wappen wird fünfmal geworfen; Ergebnisse sind Abfolgen wie ZWZZW; Ereignis A: es wird höchstens einmal Wappen erzielt
- gesucht: Term, mit dem P(A) berechnet werden kann
- verfahren: P(kein Wappen) + P(genau einmal Wappen) mit (1/2)^5 und 5 · 1/2 · (1/2)^4
- fehlerquelle: den Faktor 5 für die Position des Wappens vergessen

### 2025-bebb-lk-B4a (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 1 · format Rechnung · antwort Zahl
- gegeben: 14 % Radausflügler, Anzahl binomialverteilt; Stichprobe 300
- gesucht: P(genau 36 Radausflügler)
- verfahren: P(X = 36) am Rechner
- fehlerquelle: kumulierte statt Einzelwahrscheinlichkeit

### 2025MerhoehtBStochastikWTR2-1a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 1 · format Rechnung · antwort Zahl
- gegeben: 14 % Radausflügler, Anzahl binomialverteilt; Stichprobe 300
- gesucht: P(genau 36 Radausflügler)
- verfahren: P(X = 36) am Rechner
- fehlerquelle: kumulierte statt Einzelwahrscheinlichkeit

### 2020-be-gk-B4.2c (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: In einem großen Unternehmen ist 1/3 der Beschäftigten weiblich; 50 Beschäftigte werden zufällig ausgewählt, die Anzahl X der weiblichen darunter ist binomialverteilt (n = 50, p = 1/3)
- gesucht: Wahrscheinlichkeit, dass die Anzahl der nicht weiblichen viermal so groß ist wie die der weiblichen
- verfahren: Anzahl 10 weibliche aus a + 4a = 50, dann P(X = 10)
- fehlerquelle: P(X = 40) (nicht weibliche) mit p = 1/3 berechnen

### 2020MgrundlegendAStochastik2-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: X1 binomialverteilt mit n1 = 4 und p1; E(X1) = 2
- gesucht: P(X1 = 4)
- verfahren: p aus dem Erwartungswert, dann p⁴
- fehlerquelle: (4 über 4) vergessen ist unschädlich; p = 2 aus E = 2 lesen

### 2022MgrundlegendBStochastikWTR2-2a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Anzahl der Infizierten unter den Teilnehmenden binomialverteilt mit p = 1/3; Erwartungswert 200
- gesucht: Anzahl der Teilnehmenden; Wahrscheinlichkeit für genau 200 Infizierte
- verfahren: n aus n · p = 200, dann Binomialwahrscheinlichkeit
- fehlerquelle: kumulierte statt Einzelwahrscheinlichkeit

### 2026-bb-gk-B4b (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: X binomialverteilt mit n = 10, p = 0,75
- gesucht: P(X < 8)
- verfahren: kumulierte Wahrscheinlichkeit am Rechner
- fehlerquelle: P(X ≤ 8) rechnen (≈ 75,6 %)

### 2026MgrundlegendBStochastikWTR1-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: X binomialverteilt mit n = 10, p = 0,75
- gesucht: P(X < 8)
- verfahren: kumulierte Wahrscheinlichkeit am Rechner
- fehlerquelle: P(X ≤ 8) rechnen (≈ 75,6 %)

### 2020MgrundlegendBStochastikWTR1-1a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Großes Unternehmen, 29 % der Beschäftigten sind weiblich; 40 Beschäftigte werden zufällig ausgewählt, die Anzahl X der weiblichen darunter ist binomialverteilt (n = 40, p = 0,29)
- gesucht: P(mindestens 12 weibliche unter den 40)
- verfahren: 1 − P(X ≤ 11) mit dem Rechner
- fehlerquelle: P(X ≤ 12) statt P(X ≤ 11) abziehen

### 2022-bebb-lk-B4k (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Glücksrad mit Sonne (S, p = 0,7) und Mond (M, 0,3), siebenmal gedreht, Anordnung aus sieben Symbolen; Gewinn bei mehr als drei Monden
- gesucht: P(Gewinn)
- verfahren: 1 − F(7; 0,3; 3) mit dem Rechner (n = 7 nicht in der Anlage)
- fehlerquelle: „mehr als drei“ als X ≥ 3 lesen

### 2024MerhoehtBStochastikWTR2-1c (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: 300 zufällig ausgewählte Haushalte; Anteil Lastenrad 8 %
- gesucht: P(mehr als 20 und höchstens 30 mit Lastenrad)
- verfahren: Differenz kumulierter Wahrscheinlichkeiten
- fehlerquelle: 20 einschließen

### 2023-bebb-lk-B4a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Gruppe der Personen mit Urlaubsreise 2022: 45 % weiblich; unter den weiblichen 80 % zufrieden, unter den nicht weiblichen der Anteil a; 200 zufällig ausgewählte Personen; A: mehr als die Hälfte weiblich; B: höchstens 40 % weiblich
- gesucht: P(A) und P(B)
- verfahren: Binomialverteilung n = 200, p = 0,45 mit dem Rechner
- fehlerquelle: „mehr als die Hälfte“ als X ≥ 100 lesen

### 2024MgrundlegendBStochastikWTR2-2a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: X Anzahl unter 900 Personen, die ein Software-Problem selbst lösen, binomialverteilt mit p = 0,68
- gesucht: P(höchstens 70 % der 900)
- verfahren: 0,7 · 900 = 630, P(X ≤ 630)
- fehlerquelle: P(X ≤ 70)

### 2025MerhoehtBStochastikWTR1-1c (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: 160 Personen; Anzahl in Großstadt binomialverteilt mit p = 0,75
- gesucht: P(weniger als drei Viertel in einer Großstadt)
- verfahren: P(X ≤ 119) am Rechner
- fehlerquelle: P(X ≤ 120) ≈ 0,54

### 2018MgrundlegendBStochastikWTR3-2b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Zwölfseitiger Spielwürfel, alle Seiten gleich wahrscheinlich, nach dem abgebildeten Netz neun Seiten mit 1 und drei Seiten mit 2 beschriftet; je Spiel wird viermal geworfen; Hauptpreis bei Summe mindestens 7
- gesucht: Nachweis, dass im Mittel etwa bei einem von zwanzig Spielen ein Hauptpreis vergeben wird
- verfahren: Summe ≥ 7 heißt höchstens eine 1 unter vier Würfen; P(X ≤ 1) mit X ~ B(4; 0,75)
- fehlerquelle: Summe ≥ 7 als „mindestens drei Zweien“ mit falscher Trefferwahrscheinlichkeit rechnen

### 2019MgrundlegendBStochastikWTR1-1a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Land mit 80 % Führerscheinbesitz unter Erwachsenen; 200 zufällig ausgewählte Erwachsene, X = Anzahl mit Führerschein, binomialverteilt (n = 200, p = 0,8)
- gesucht: Wahrscheinlichkeit, dass X vom Erwartungswert um höchstens 5 % abweicht
- verfahren: Intervall [160 − 8; 160 + 8] bilden und kumuliert berechnen
- fehlerquelle: 5 % als 5 Personen lesen oder nur eine Seite rechnen

### 2025-bebb-lk-B4b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: X wie in a
- gesucht: P(Anzahl um mindestens 10 % größer als der Erwartungswert)
- verfahren: μ berechnen, 1,1μ aufrunden, P(X ≥ 47)
- fehlerquelle: X ≥ 46 rechnen (46 < 46,2)

### 2023-bebb-gk-B4.1e (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich. 100 Lehrkräfte werden zufällig ausgewählt; Term Σ von k = 75 bis 100 über C(100; k) · 0,75^k · 0,25^(100−k).
- gesucht: Bedeutung des Terms im Sachzusammenhang
- verfahren: Summe als P(X ≥ 75) mit p = 0,75 (nicht am Gymnasium) erkennen und übersetzen.
- fehlerquelle: „mindestens 75 am Gymnasium“ (Erfolg und Misserfolg vertauscht)

### 2026MgrundlegendBStochastikWTR2-1d (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Kurzantwort · antwort Text
- gegeben: 20 Lieder, p = 0,32; Aussage Summe k = 0 bis 8 von (20 über k) · 0,32^k · 0,68^(20 − k) ≈ 0,843
- gesucht: Bedeutung der Aussage im Sachzusammenhang
- verfahren: Summe als P(X ≤ 8) lesen
- fehlerquelle: „genau acht“ statt „höchstens acht“

### 2021MgrundlegendBStochastikWTR3-1d (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Großes Unternehmen: 77 % aller Beschäftigten sind mit ihrem Gehalt zufrieden; 5 % aller Beschäftigten sind in der Werbeabteilung und nicht zufrieden; 12 % aller Beschäftigten gehören zur Werbeabteilung; Term 1 − Σ_(i=0)^400 (600 über i) · 0,23ⁱ · 0,77^(600−i)
- gesucht: Bedeutung des Terms im Sachzusammenhang
- verfahren: Erfolgswahrscheinlichkeit 0,23 als „nicht zufrieden“ erkennen, Summe als kumulierte Wahrscheinlichkeit, 1 − … als Gegenereignis
- fehlerquelle: 0,23 als Zufriedenheitsanteil lesen

### 2021-be-gk-B4d (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Smartphone-Spiel: jeden Sonntag zehn Versuche, je Versuch mit 40 % ein Stern; X = Anzahl der Sterne bei zehn Versuchen, binomialverteilt (n = 10, p = 0,4); vier Spieler machen je zehn Versuche
- gesucht: Wahrscheinlichkeit, dass genau zwei der vier Spieler jeweils genau fünf Sterne gewinnen
- verfahren: P(X = 5) als Trefferwahrscheinlichkeit einer Binomialverteilung mit n = 4
- fehlerquelle: P(X = 5)² ohne Binomialkoeffizient und Gegenwahrscheinlichkeit

### 2023MgrundlegendBStochastikWTR1-2a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 96 % der Säcke einwandfrei; Schritt 1: 50 Säcke, höchstens zwei mangelhaft ⇒ Vertrag; genau drei mangelhaft ⇒ Schritt 2: 25 Säcke, höchstens ein mangelhaft ⇒ Vertrag; sonst kein Vertrag
- gesucht: Wahrscheinlichkeit für den Vertragsabschluss
- verfahren: Direkter Abschluss plus Pfad über genau drei Mängel und zweiten Schritt, beide binomial
- fehlerquelle: zweiten Schritt ohne Faktor P(X = 47) addieren

### 2022-bebb-gk-B4e (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Paketzentrum: 10 % der Pakete haben das Ziel A, 7 % das Ziel B; Anlage mit Tabelle der summierten Binomialverteilung; 20 Pakete zufällig ausgewählt; P(keines mit Ziel C) ≈ 54 %
- gesucht: Anteil der Pakete mit Ziel C unter allen Paketen
- verfahren: (1 − p)^20 = 0,54 nach p auflösen
- fehlerquelle: 0,54/20 rechnen

### 2018MgrundlegendBStochastikWTR2-1d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Flachbildschirme, im Mittel einer von fünf fehlerhaft; die Anzahl fehlerhafter Geräte unter zufällig ausgewählten ist binomialverteilt (p = 0,2); nach einer Verbesserung soll P(keiner von 25 fehlerhaft) ≥ 10 % sein
- gesucht: höchstzulässiger Anteil fehlerhafter Geräte nach der Verbesserung
- verfahren: (1 − x)^25 ≥ 0,1 nach x auflösen
- fehlerquelle: die 25. Wurzel als Division durch 25 ausführen

### 2025-bebb-gk-B4d (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: X wie in c; P(X ≤ k) soll mehr als 90 % betragen
- gesucht: kleinstmögliches k
- verfahren: kumulierte Wahrscheinlichkeiten um 90 % vergleichen
- fehlerquelle: k = 103 angeben (Schranke nicht überschritten)

### 2022MerhoehtBStochastikWTR2-1e (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Befragung wie in d; Schranke 25 %
- gesucht: größtes k mit P(X < k) < 25 %
- verfahren: Kumulierte Wahrscheinlichkeiten um μ − 0,67σ probieren
- fehlerquelle: k = 114 (Grenze mit ≤ statt <)

### 2023-bebb-lk-B4h (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 80 000 Teilnehmer; X Anzahl mit zwei Strandkörben, p = 8 · 10⁻⁴; Intervall [μ − c; μ + c] mit Wahrscheinlichkeit mindestens 80 %
- gesucht: kleinster ganzzahliger Wert von c
- verfahren: μ berechnen, symmetrische Intervalle mit wachsendem c am Rechner prüfen
- fehlerquelle: c über die Sigma-Regel ohne Nachbarwertprüfung

### 2019MgrundlegendBStochastikWTR3-1d (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: 200 zufällig ausgewählte befragte Männer; X = Anzahl mit Anzeichen spielsüchtigen Verhaltens, binomialverteilt mit p = 0,025
- gesucht: kleinstes um E(X) symmetrisches Intervall, in dem X mit mehr als 90 % liegt
- verfahren: E(X) = 5, Umgebungen [5 − r; 5 + r] mit wachsendem r prüfen
- fehlerquelle: Sigma-Umgebung mit σ ≈ 2,2 ohne Prüfung angeben

### 2024MgrundlegendBStochastikWTR2-2b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: X wie in a; Bedingung P(μ − k ≤ X ≤ μ) ≥ 30 %
- gesucht: μ und kleinstes natürliches k
- verfahren: μ berechnen, Intervalle nach unten verlängern
- fehlerquelle: symmetrische Umgebung μ ± k rechnen

### 2021MgrundlegendBStochastikWTR2-1d (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Smartphone-Spiel: jeden Sonntag zehn Versuche, je Versuch mit 40 % ein Stern; X = Anzahl der Sterne bei zehn Versuchen, binomialverteilt (n = 10, p = 0,4); nach einer Änderung von p beträgt P(höchstens drei Sterne bei zehn Versuchen) etwa 62 %
- gesucht: die geänderte Wahrscheinlichkeit p auf ganze Prozent
- verfahren: P(X ≤ 3) für Werte von p mit dem Rechner berechnen, bis etwa 62 % erreicht sind
- fehlerquelle: p aus E(X) = 3 zu 30 % schließen

### 2022MgrundlegendBStochastikWTR2-2b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: zweite Studie, Anzahl der Infizierten binomialverteilt mit p = 1/3; P(X = 30) ≈ 3,6 %
- gesucht: eine mögliche Anzahl der Teilnehmenden
- verfahren: n variieren, bis P(X = 30) ≈ 0,036
- fehlerquelle: n = 90 aus 30/p ansetzen und nicht prüfen

### 2018-be-gk-B3.2c (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 3 · format Begründung · antwort Text
- gegeben: Die Anzahl fehlerhafter Bildschirme ist binomialverteilt mit p = 0,2. Zu beurteilen ist die Aussage, dass die Wahrscheinlichkeit dafür, dass alle Geräte fehlerfrei sind, geringer wird, wenn eine Stichprobe um einen zufällig ausgewählten Bildschirm ergänzt wird.
- gesucht: Beurteilung der Aussage
- verfahren: Bei n Geräten ist die Wahrscheinlichkeit 0,8ⁿ, bei n + 1 Geräten 0,8^(n+1) = 0,8 · 0,8ⁿ. Da mit 0,8 multipliziert wird, ist der Wert kleiner; die Aussage trifft zu.
- fehlerquelle: die Aussage nur an einem Zahlenbeispiel prüfen und den allgemeinen Grund nicht nennen

### 2018-be-gk-B3.1c (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Das Spiel hat die Gewinnwahrscheinlichkeit p = 0,4 und wird n-mal gespielt. Ereignis C: wenigstens eins von n Spielen wird gewonnen. Eine Spielerin behauptet, P(C) werde kleiner, wenn n größer wird.
- gesucht: Entscheidung über die Behauptung anhand zweier berechneter Wahrscheinlichkeiten
- verfahren: P(C) über das Gegenereignis kein Gewinn bestimmen: P(C) = 1 − 0,6ⁿ. Zwei Werte berechnen, etwa n = 1 mit 0,4 und n = 10 mit etwa 0,994; da 0,6ⁿ mit wachsendem n kleiner wird, wächst P(C). Die Behauptung ist damit widerlegt.
- fehlerquelle: P(C) als Summe der Einzelwahrscheinlichkeiten aufschreiben und im Rechenaufwand steckenbleiben, statt das Gegenereignis zu nutzen

### 2023MgrundlegendBStochastikWTR1-2b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: zweiter Schritt mit 15 statt 25 Säcken, sonst gleiche Bedingungen
- gesucht: ob das für den Großhändler von Vorteil sein könnte, ohne Rechnung
- verfahren: Wahrscheinlichkeit für höchstens einen Mangel wächst bei kleinerer Stichprobe
- fehlerquelle: größere Stichprobe pauschal als besser ansehen

### 2019MerhoehtAStochastik11-b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Y binomialverteilt mit n = 5 und p > 0; P(Y = 4) = 10 · P(Y = 5)
- gesucht: Wert von p
- verfahren: beide Wahrscheinlichkeiten als Terme in p, Gleichung lösen
- fehlerquelle: (5 über 4) = 5 vergessen

### 2023-bebb-gk-A1.7a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 2 · format Kurzantwort · antwort Zahl
- gegeben: Abbildung der Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße X (Säulen für k = 0 bis 9, Maximum bei k = 3 mit etwa 0,26).
- gesucht: Näherungswert für P(3 < X < 6)
- verfahren: Die Säulen für k = 4 und k = 5 ablesen und addieren.
- fehlerquelle: die Säulen für k = 3 und k = 6 mitzählen (P(3 ≤ X ≤ 6) ≈ 0,58)

### 2026-bb-gk-A1.6b (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 3 · format Kurzantwort · antwort Zahl
- gegeben: Säulendiagramm von P(X = k) für X binomialverteilt mit n = 20 und p = 0,2: Säulenhöhen etwa 0,01, 0,06, 0,14, 0,205, 0,22, 0,175 für k = 0 bis 5; Bedingungen P(X = v) ≈ 0,175 und 0,15 < P(X <= w) < 0,25
- gesucht: natürliche Zahlen v und w
- verfahren: v an der Säule mit Höhe 0,175 ablesen; für w die Säulen von k = 0 an addieren, bis die Summe zwischen 0,15 und 0,25 liegt
- fehlerquelle: für w die Säule mit Höhe zwischen 0,15 und 0,25 nehmen statt die Summe zu bilden

### 2018-be-gk-B3.2b (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Die Anzahl fehlerhafter Geräte unter 250 zufällig ausgewählten Bildschirmen ist binomialverteilt mit p = 0,2.
- gesucht: Anzahl fehlerhafter Bildschirme, die mit der größten Wahrscheinlichkeit auftritt
- verfahren: Den Erwartungswert 250 · 0,2 = 50 bestimmen und die Einzelwahrscheinlichkeiten in seiner Umgebung vergleichen; alternativ über (n + 1) · p = 50,2 und Abrunden.
- fehlerquelle: den Erwartungswert angeben, ohne zu prüfen, ob die Nachbarwerte kleinere Wahrscheinlichkeiten haben

### 2020MerhoehtAStochastik11-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Diagramm der Verteilung von X ohne Achsenwerte; die grauen Säulen stellen P(X ≤ k) dar und enden bei der höchsten Säule
- gesucht: Wert von k
- verfahren: Erwartungswert berechnen, mit der höchsten Säule identifizieren
- fehlerquelle: Säulen abzählen wollen (keine Achsenwerte)

### 2025-bebb-gk-B4c (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: X Anzahl überbelegter Haushalte unter 1000, binomialverteilt mit p = 0,0918; Aussage: die Verteilung nimmt für 90 den größten Wert an
- gesucht: Beurteilung ohne Berechnung von Wahrscheinlichkeiten
- verfahren: Erwartungswert berechnen und mit 90 vergleichen
- fehlerquelle: Wahrscheinlichkeiten doch berechnen

### 2020-be-gk-B4.2d (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 3 · format Begründung · antwort Text
- gegeben: In einem großen Unternehmen ist 1/3 der Beschäftigten weiblich; 50 Beschäftigte werden zufällig ausgewählt, die Anzahl X der weiblichen darunter ist binomialverteilt (n = 50, p = 1/3)
- gesucht: Begründung ohne Wahrscheinlichkeitsrechnung, dass die Verteilung von X für 16 oder 17 den größten Wert hat
- verfahren: Erwartungswert berechnen; das Maximum liegt bei einer der beiden benachbarten ganzen Zahlen
- fehlerquelle: das Maximum bei n/2 = 25 vermuten

### 2021MgrundlegendAStochastik12-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: 36 Würfe; X Anzahl der Würfe ohne 6, binomialverteilt mit p = 25/36; Abb. 1 bis 3
- gesucht: je Abbildung eine Begründung, dass sie nicht die Verteilung von X zeigt
- verfahren: je ein Merkmal prüfen: Lage des Maximums, Summe, Wertebereich
- fehlerquelle: Abb. 2 nur wegen der Form ablehnen

### 2018MerhoehtAStochastik11-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: X binomialverteilt mit n = 10, p = 0,8; drei Säulendiagramme, eines zeigt die Verteilung von X
- gesucht: die beiden Diagramme, die X nicht darstellen, mit Begründung
- verfahren: Wertebereich und Summe prüfen
- fehlerquelle: Abb. 1 wegen der Lage des Maximums bei 8 für richtig halten

### 2026-bb-gk-B4c (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: Abbildung: Verteilung von Y mit n = 10, p = 0,25; X Anzahl der Sammler mit p = 0,75
- gesucht: Erläuterung, wie man mit der Abbildung P(X = 6) ermittelt
- verfahren: X = 6 Sammler heißt Y = 4 Nichtsammler
- fehlerquelle: Säule bei k = 6 ablesen

### 2024MerhoehtAStochastik23-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 2 · format Zeichnen · antwort Grafik
- gegeben: Tetraeder mit Zahlen 1 bis 4, gleich wahrscheinlich, viermal geworfen; X zählt die Würfe mit 1, Verteilung in Abbildung 1; Y zählt die Würfe ohne 1
- gesucht: Wahrscheinlichkeitsverteilung von Y in Abbildung 2
- verfahren: Y = 4 − X, also die Säulen von Abbildung 1 in umgekehrter Reihenfolge eintragen
- fehlerquelle: Abbildung 1 unverändert abzeichnen

### 2019MerhoehtAStochastik11-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 2 · format Rechnung|Eintragen · antwort Zahl
- gegeben: Diagramm mit kumulierten Werten P(X ≤ k) einer Binomialverteilung mit n = 5 für k = 0 bis 4
- gesucht: Säule für k = 5 und P(X = 2)
- verfahren: Säule der Höhe 1 ergänzen, Differenz zweier kumulierter Werte ablesen
- fehlerquelle: P(X ≤ 2) = 0,5 als P(X = 2) ablesen

### 2021MerhoehtAStochastik12-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: X ~ B(100; 0,5); P(X ≥ 61) ≈ 2 %
- gesucht: P(40 ≤ X ≤ 60) aus diesem Wert
- verfahren: beide Ränder abziehen
- fehlerquelle: 98 % angeben (nur einen Rand abziehen)

### 2020MerhoehtAStochastik11-c (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 2 · format Kurzantwort · antwort Term
- gegeben: Y binomialverteilt mit n = 40 und p_Y, 0 < p_Y < 1
- gesucht: alle p_Y mit P(Y = 10) > P(Y = 30)
- verfahren: Lage von 10 und 30 zur Mitte 20 mit p vergleichen
- fehlerquelle: p > 0,5 angeben

### 2021MgrundlegendBStochastikWTR1-1c (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 4 · format Begründung · antwort Text
- gegeben: Joghurtbecher auf Paletten zu je 20 Bechern; unter jedem Deckel genau eines von sechs Motiven; gegenwärtig wird jedes Motiv zufällig (je 1/6) ausgewählt; drei Becher werden nacheinander geöffnet; geplante Änderung: Motiv 6 künftig mit Wahrscheinlichkeit p; X = Anzahl der Becher mit Motiv 6 auf einer Palette (n = 20); die Abbildung zeigt für einen Wert von p die Wahrscheinlichkeitsverteilung von X; Aussage I: P(weniger als zwei Becher mit Motiv 6) > 50 %; Aussage II: p > 1/6
- gesucht: Beurteilung beider Aussagen
- verfahren: Säulenanteile für k < 2 abschätzen; Lage des Maximums mit n · p vergleichen
- fehlerquelle: Aussage II mit der Säule zu k = 2 statt mit dem Erwartungswert 20p begründen wollen

Nur außerhalb von „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ genannt, nicht aufgenommen: 2020MgrundlegendBStochastikWTR2-1c, 2024MerhoehtBStochastikWTR2-1d, 2026-bb-ea-B4a, 2026MgrundlegendBStochastikWTR2-1c, 2026MerhoehtBStochastikWTR1-1a, 2026MerhoehtBStochastikWTR2-1a, 2025MgrundlegendBStochastikWTR2-1c, 2025MgrundlegendBStochastikWTR3-1d, 2023MgrundlegendBStochastikWTR2-1b, 2023MerhoehtBStochastikWTR1-1, 2022MerhoehtBStochastikWTR1-1d, 2021MgrundlegendBStochastikWTR2-1a, 2018MerhoehtBStochastikWTR2-1a, 2018MgrundlegendBStochastikWTR1-1d, 2025MgrundlegendBStochastikWTR1-1d, 2021MgrundlegendBStochastikWTR3-1c, 2025MerhoehtBStochastikWTR2-1b, 2023MgrundlegendBStochastikWTR3-1d, 2017-bb-ea-B4.2d, 2023MgrundlegendBStochastikWTR3-1e, 2022MerhoehtBStochastikWTR2-1d, 2020MgrundlegendBStochastikWTR1-1c, 2020MerhoehtAStochastik11-a, 2026-bb-ea-A1.4a, 2026MerhoehtAStochastik11-a, 2026MerhoehtAStochastik22-a, 2017MerhoehtAStochastik11-b, 2021MgrundlegendBStochastikWTR2-1c, 2019-be-gk-B4.2e, 2020-be-gk-B4.2b, 2020MgrundlegendBStochastikWTR1-1b, 2026MgrundlegendAStochastik11-b, 2025MgrundlegendBStochastikWTR3-1c, 2025MerhoehtAStochastik12-a, 2019MgrundlegendBStochastikWTR2-1a, 2018-be-gk-B3.1b, 2019-be-gk-B4.2d, 2020MgrundlegendBStochastikWTR2-1b, 2022-bebb-gk-B4d, 2019-be-gk-B4.1b, 2020-be-gk-B4.1c, 2021-be-gk-B4e, 2022MgrundlegendBStochastikWTR1-1c, 2023MerhoehtBStochastikWTR2-2b, 2018MerhoehtBStochastikWTR2-1d, 2026-bb-ea-B4b, 2020MgrundlegendBStochastikWTR1-1d, 2019MgrundlegendAStochastik12-b, 2017MerhoehtAStochastik12-b, 2026MgrundlegendBStochastikWTR1-1c, 2026MerhoehtBStochastikWTR1-1b, 2025MgrundlegendAStochastik21-b, 2025MgrundlegendBStochastikWTR1-1c, 2018MgrundlegendBStochastikWTR2-1c, 2018MgrundlegendBStochastikWTR2-1b, 2021-be-gk-B4b, 2022MgrundlegendBStochastikWTR1-1a

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
