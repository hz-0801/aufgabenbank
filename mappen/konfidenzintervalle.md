# Mappe: konfidenzintervalle

Eintrag: hz-0801/mathe-nachhilfe, katalog/konfidenzintervalle.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:08 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Konfidenzintervalle
 3
 4  ### Verortung
 5  Das Konfidenzintervall zum Stichprobenanteil: die Überdeckungsdeutung (zu jedem Stichprobenergebnis gehört das Intervall der p-Werte, mit denen es verträglich ist; die Sicherheitswahrscheinlichkeit sa … (gekürzt, 1650 Zeichen)
 6  [GOST] Kein namentlicher Planinhalt: weder der Brandenburger noch der Berliner Plan führt Konfidenz-, Vertrauens- oder Prognoseintervalle (Suchprotokoll: „Konfidenz“, „Vertrauens“, „Prognose“ in beide … (gekürzt, 1083 Zeichen)
 7  [FOS] Kein Stoff: der RLP FOS 2019 führt weder Konfidenzintervalle noch beurteilende Statistik (Suchprotokoll: „Konfidenz“, „Vertrauens“ in der Textfassung ohne Treffer); keine fhr-Zeile.
 8  [LS-AA] Kein Kapitel: der Fahrplan führt kein Konfidenz- oder Schätzintervall-Kapitel (Suchprotokoll: „Konfidenz“, „Vertrauens“ ohne Treffer; die „Schätzen“-Treffer liegen sämtlich in der Sekundarstufe I bei Größen und Maßstäben). Die Sprossen stützen sich allein auf die Rohdatei – wie bei scharen-von-geraden-und-ebenen.md, dem anderen Thema ohne Lehrwerkskapitel.
 9
10  ### Lerneinheiten
11  1. Das Intervall lesen und deuten: die Überdeckungsdeutung (verträglich heißt: der angenommene Anteil wird vom Intervall überdeckt – nicht „p liegt mit dieser Sicherheit im Intervall“), im Diagramm vi … (gekürzt, 688 Zeichen)
12    Marken: BE Q4 · BB Q4 · GK · keine Prüfungsaufgabe
13  2. Mit der Näherungsformel rechnen: die Grenzgleichung nach p lösen (quadratisch – zwei Lösungen sind die zwei Grenzen), rückwärts aus einer Grenze das Stichprobenergebnis bestimmen, den kleinsten Stichprobenumfang ermitteln, ab dem ein beobachteter Anteil mit einer Annahme unverträglich ist. (Pool erhöht, Teil B; [FS-IQB] liefert die Gleichung) ← Eingabe „konfidenzintervall berechnen“, „grenzen bestimmen“, „mindestumfang unverträglich“
14    Marken: BE Q4 · BB Q4 · GK · keine Prüfungsaufgabe
15  3. Argumente über Formel und Verträglichkeit: die Länge des Intervalls bei doppeltem Umfang (Faktor eins durch Wurzel zwei – kürzer, nicht halb so lang), Aussagen über eine Grenze aus der Lage des Stichprobenanteils, Verträglichkeit zweier Annahmen mit demselben Anteil über Schwellen für den Stichprobenumfang. (Pool erhöht, Teil B; Prüfungshöhe) ← Eingabe „intervalllänge stichprobenumfang“, „verträglich unverträglich n“, „konfidenzintervall begründen“
16    Marken: BE Q4 · BB Q4 · GK · keine Prüfungsaufgabe
17  Warum drei: Das Lesen mit der Überdeckungsdeutung (sechs Zeilen) ist der Kern – der Pool prüft die Deutung inzwischen sogar direkt über die Binomialverteilung der Überdeckungszahl; das Formelrechnen ( … (gekürzt, 704 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; abitur-Typen wörtlich aus abitur/abitur-typen.csv.
21  Einheit 1: Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen (2) — Nachweis: Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen (2) — Deutung: Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben (2). Dazu: Fehler finden (die Senkrechte beim vermuteten p statt der Waagerechten beim Stichprobenanteil geschnitten; die inneren statt der äußeren Grenzgraphen verwendet; einen Anteil gewählt, den alle Intervalle treffen; „genau k“ als „mindestens k“ gerechnet) · Begründen (warum die Überdeckungszahl binomialverteilt ist und was ihre Trefferwahrscheinlichkeit ist; warum „Sicherheit“ eine Aussage über viele Intervalle ist, nicht über das eine).
22  Einheit 2: Grenzen eines Konfidenzintervalls aus dem Stichprobenergebnis über die Näherungsformel berechnen und im Diagramm zuordnen (1) · Konfidenzintervall aus dem Diagramm identifizieren und Stichprobenergebnis aus der Grenze berechnen (1) · Kleinsten Stichprobenumfang für die Unverträglichkeit eines Anteils mit einer Annahme über die Näherungsformel ermitteln (1) · Verträglichkeit einer vermuteten Trefferwahrscheinlichkeit über das 1,96σ-Intervall um den Erwartungswert prüfen (1; Ermessen, siehe Offene Punkte) — kein Nachweistyp — kein Deutungstyp. Dazu: Fehler finden (die Gleichung in h statt in p gelöst – die bequeme Näherung liefert andere Grenzen; die Grenze mit dem Umfang multipliziert statt erst h aus der Grenzgleichung bestimmt; die Anzahl statt des Anteils in die Formel gesetzt) · Begründen (warum die Grenzgleichung zwei Lösungen hat und beide Grenzen sind; warum Unverträglichkeit eine Ungleichung in n ist).
23  Einheit 3: kein Berechnungstyp — Nachweis: Länge eines Konfidenzintervalls bei doppeltem Stichprobenumfang über den Faktor 1/√2 begründen (1) · Obere Grenze eines Konfidenzintervalls über den Stichprobenanteil begründen und Verträglichkeit einer Annahme beschreiben (1) — Deutung: Verträglichkeit zweier Annahmen mit demselben Stichprobenanteil über den Stichprobenumfang beurteilen (1). Dazu: Fehler finden (die Länge als proportional zu eins durch n angenommen; die obere Grenze über eine vermeintliche Symmetrie rechnen wollen; die Richtung der Ungleichungen in n vertauscht) · Begründen (warum der Stichprobenanteil im Intervall liegt; warum wachsendes n das Intervall enger macht und eine Annahme herausfallen kann, während die andere drin bleibt).
24  Zählung: 3 + 4 + 3 = 10 Haupttypen, 6 + 4 + 3 = 13 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeile vom 28.09.2026: Pool 2017 erhöht Teil B, WTR).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Relative Häufigkeit und Anteil aus einer Stichprobe bilden – der Einstieg jeder Zeile. Sek-I-Thema prozentrechnung.md. [GOST GK Q4 „Schätzung von Wahrscheinlichkeiten aus relativen Häufigkeiten“]
29  - Die Sigma-Regeln und ihre c-Werte – die Sicherheitswahrscheinlichkeiten der Grenzgleichung. Sek-II-Nachbarthema normalverteilung-und-sigma-regeln.md (dasselbe Bündel). [FS-IQB „Sigma-Regeln“]
30  - Binomialverteilung ansetzen und Punktwahrscheinlichkeiten berechnen – die Überdeckungszahl der Einheit 1. Sek-II-Nachbarthema binomialverteilung.md. [GOST Q2 L5]
31  - Quadratische Gleichungen und Wurzelgleichungen lösen, Lösungen deuten – die Grenzgleichung der Einheit 2. Sek-I-Thema quadratische-gleichungen.md, Sek-II-Thema gleichungen-loesen.md. [GOST-OHiMi 2.1]
32  - Ungleichungen in n lösen und runden – Mindestumfänge und n-Schwellen der Einheiten 2 und 3. Sek-II-Thema gleichungen-loesen.md. [GOST-OHiMi 2.1]
33  - Graphen zweier Funktionen ablesen (Schnitt mit Waagerechten und Senkrechten) – die Grenzfunktionen der Einheit 1. Sek-I-Thema lineare-funktionen.md (Grundfertigkeit Graphenlesen). [GOST Eingangsvoraussetzung L4]
34  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt): keine eigenen – seit 27.09.2026 gestrichen, weil die Vorstufen der Ketten denselben Handgriff verlangen.
35
36  ### Merkkasten
37  Einheit 1 (Lesen und Überdeckung):
38      Was das Intervall ist: zu jedem Stichprobenergebnis gehört das Intervall aller p-Werte, mit denen das Ergebnis verträglich ist – eine Spanne statt eines Punktwerts.
39      Was „Sicherheit“ heißt: auf lange Sicht überdecken etwa fünfundneunzig von hundert solcher Intervalle den wahren Anteil – nicht: „p liegt mit dieser Wahrscheinlichkeit im Intervall“; p ist fest, die Intervalle streuen.
40      Im Diagramm: eine Senkrechte bei p zählt, mit wie vielen Ergebnissen p verträglich ist; die Zahl der überdeckenden Intervalle ist binomialverteilt – Trefferwahrscheinlichkeit ist die Sicherheitswahrscheinlichkeit.
41      An den Grenzfunktionen: die Waagerechte beim Stichprobenanteil schneidet die beiden Grenzgraphen – die Schnittstellen sind die Intervallgrenzen; bei mehreren Kurvenpaaren gehören die äußeren zur höheren Sicherheit.
42      Auswendig (Teil A): die Überdeckungsdeutung – begründetes Ermessen: das Thema hat keine Teil-A-Zeile (alle dreizehn Zeilen Teil B), aber die Deutung trägt jede Teilaufgabe und der Pool prüft sie inzwischen direkt (die Überdeckungszahl-Aufgaben).
43      Formelsammlung: [FS-IQB „Prognoseintervall und Konfidenzintervall“] führt die Grenzgleichung, nicht die Deutung – die muss sitzen – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
44  Quelle: eigene Formulierung nach der Rohdatei (die Überdeckungszahl-Aufgaben des Pooljahrs 2026) und [FS-IQB]; ohne Zahlenbeispiel (die Deutung ist zahlenfrei; Ermessen); kein Lehrwerkskapitel.
45
46  Einheit 2 (Näherungsformel):
47      Die Gleichung: |h − p| = c · √(p · (1 − p)/n) – sie steht wörtlich in der Formelsammlung; nach p gelöst (quadratisch) liefert sie die beiden Grenzen des Konfidenzintervalls.
48        Beispiel: 356 Treffer unter 500 geben h = 0,712; mit c = 1,96 (Sicherheitswahrscheinlichkeit 95 %) wird die Gleichung nach p gelöst – wer stattdessen h ± 1,96 · √(h(1 − h)/500) rechnet, bekommt andere Grenzen (die bequeme, hier falsche Näherung).
49      Die c-Werte: 1,64 gehört zu 90 %, 1,96 zu 95 % – die Zuordnung kommt aus den Sigma-Regeln, sie steht nicht beim Konfidenzabschnitt.
50      Rückwärts: aus einer Grenze die Gleichung nach h auflösen und mit n multiplizieren (erst h, dann Anzahl); Unverträglichkeit heißt |h − p| > c · √(p(1 − p)/n) – nach n auflösen und je nach Frage auf- oder abrunden.
51      Auswendig (Teil A): nur die c-Zuordnung über die Sigma-Regeln – die Gleichung selbst ist in Teil B nachschlagbar.
52      Formelsammlung: [FS-IQB] Abschnitt „Prognoseintervall und Konfidenzintervall“ (Textfassung Zeilen 415–424) mit Prognoseintervall und Grenzgleichung – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
53  Quelle: eigene Formulierung nach [FS-IQB] und der Rohdatei; Zahlenbeispiel aus iqb 2026MerhoehtBStochastikMMS3-2a; kein Lehrwerkskapitel.
54
55  Einheit 3 (Argumente):
56      Länge: die Intervalllänge ist das Doppelte von c · √(h(1 − h)/n) – bei doppeltem Umfang schrumpft sie um den Faktor eins durch Wurzel zwei: kürzer, aber nicht halb so lang.
57      Lage: der Stichprobenanteil liegt immer im Intervall – aus seiner Lage folgen Aussagen über die Grenzen (liegt h über einer Annahme, ist auch die obere Grenze größer als diese Annahme).
58      Verträglichkeit und n: gleiche Mitte, engeres Intervall – mit wachsendem n kann eine Annahme unverträglich werden, während eine andere verträglich bleibt; die Grenzgleichungen liefern die Schwellen für n, auf die Richtung der Ungleichungen achten.
59      Auswendig (Teil A): der Längenfaktor und die Lageregel – begründetes Ermessen wie in Kasten eins; die Schwellenrechnungen sind Teil-B-Stoff.
60      Formelsammlung: [FS-IQB] nur die Grenzgleichung; Längenfaktor und Lageregel folgen aus ihr, stehen aber nicht ausformuliert darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
61  Quelle: eigene Formulierung nach der Rohdatei (Längen-, Lage- und Schwellenaufgaben); ohne Zahlenbeispiel (die Regeln sind zahlenfrei formuliert; Ermessen); kein Lehrwerkskapitel.
62
63  ### Typische Fehler
64  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 12 Zeilen des Themas in abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
65  - Diagramm falsch geschnitten: die Senkrechte beim vermuteten p statt der Waagerechten beim Stichprobenanteil verwendet (liefert nur zufällig Ähnliches); die inneren statt der äußeren Grenzgraphen genommen (falsche Sicherheitswahrscheinlichkeit); einen Anteil gewählt, den alle Intervalle treffen, statt genau die verlangte Zahl. [iqb 2025MerhoehtBStochastikWTR3-2c, 2018MerhoehtBStochastikWTR2-1f, 2026MerhoehtBStochastikWTR3-2b, 2026MerhoehtBStochastikMMS3-2b]
66  - Überdeckungszahl falsch angesetzt: „genau k“ als „mindestens k“ gerechnet. [iqb 2026MerhoehtBStochastikWTR3-2c, 2026MerhoehtBStochastikMMS3-2c]
67  - Formel falsch besetzt: die Gleichung in h statt in p gelöst (die bequeme Näherung mit h unter der Wurzel); die Grenze mit dem Umfang multipliziert, statt erst h aus der Grenzgleichung zu bestimmen; die Anzahl statt des Anteils eingesetzt. [iqb 2026MerhoehtBStochastikMMS3-2a, 2026MerhoehtBStochastikWTR3-2a, 2023MerhoehtBStochastikWTR1-4b]
68  - Argument verfehlt: die Länge als proportional zu eins durch n angenommen (statt eins durch Wurzel n); die obere Grenze über eine vermeintliche Symmetrie rechnen wollen, statt die Lage des Stichprobenanteils zu nutzen; die Richtung der Ungleichungen in n vertauscht. [iqb 2018MerhoehtBStochastikWTR2-1g, 2023MerhoehtBStochastikWTR1-4a, 2025MerhoehtBStochastikWTR3-2d]
69
70  ### Für schwache Schüler
71  Mindeststoff (GK-Kern Q2/Q4 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: keiner – das Thema steht in keinem Rahmenlehrplan namentlich, die Geltungsdateien führen es viermal mit „nein“, und der Pool stellt es ausschließlich erhöht in Teil B; die Grundkurs-Q4-Zeilen zum Schließen aus Stichproben sind Vorstufe ohne Katalogzeile. RLP FOS (fhr): kein Stoff, keine Zeile. Wer das Thema dennoch lernt (erhöhtes Niveau mit Blick auf den Pool): Einheit 1 zuerst – die Überdeckungsdeutung und das Ablesen tragen jede Aufgabe; die Formelroutine der Einheit 2 folgt, die Argumente der Einheit 3 sind Prüfungshöhe. Niveaustufe H der E-Phase [RLP]: kein Bezug; Blatt-0-Stoff sind Anteile, Sigma-Regeln und Gleichungslösen. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung keine beurteilende Statistik – kein zusätzlicher Posten.
72  Grundvorstellung (Blatt 0) [Rohdatei, MO]: Eine Stichprobe liefert keine Wahrheit, sondern eine Spanne – und die „Sicherheit“ beschreibt das Verfahren, nicht das einzelne Intervall. „Zwanzig Klassen befragen je hundert Menschen zur selben Frage, kein Term. Jede Klasse gibt statt einer einzigen Zahl eine Spanne an, in der der wahre Anteil ‚gut passt‘. Warum sind die Spannen verschieden, obwohl alle denselben Anteil suchen? Müssen alle Spannen den wahren Anteil enthalten – und was bedeutet es, wenn eine danebenliegt? Und wird die Spanne halb so breit, wenn eine Klasse doppelt so viele Menschen befragt?“ Wer erwartet, dass jede Spanne trifft, oder die Sicherheit dem einzelnen Intervall zuschreibt, braucht das vor jeder Formel: das Verfahren trifft meistens, welches Intervall danebenliegt, weiß niemand – und mehr Daten machen die Spanne enger, aber nur mit der Wurzel. Verständnis, nicht Verfahren; die Vorstellung folgt der Rohdatei (die Überdeckungszahl-Aufgaben prüfen sie direkt), die Aufgabenform ist Ermessen. [MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „p wählen, das alle Intervalle trifft“; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
73  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [Rohdatei; kein Lehrwerkskapitel – Sprossenfolge Ermessen]:
74  - Lesen und Überdeckung (Einheit 1): „Was heißt verträglich?“ – zu Deutungssätzen ankreuzen, ob sie die Überdeckungsdeutung tragen (viele Intervalle, ein fester Anteil wird überdeckt) oder die falsche Sicherheitsdeutung („p liegt mit … Prozent im Intervall“); nichts rechnen (Vorstufe, Grundvorstellung) → das Intervall an den Grenzfunktionen ablesen: Waagerechte beim Stichprobenanteil, äußere Graphen zur höheren Sicherheit (Grundfall, viermal; iqb 2018MerhoehtBStochastikWTR2-1f) → eine Vermutung auf Verträglichkeit prüfen und beurteilen (iqb 2025MerhoehtBStochastikWTR3-2c) → im Diagramm vieler Intervalle einen Anteil mit genau der verlangten Trefferzahl finden (iqb 2026MerhoehtBStochastikWTR3-2b, 2026MerhoehtBStochastikMMS3-2b) → Prüfungshöhe: die Überdeckungszahl als binomialverteilt begründen und eine Wahrscheinlichkeit berechnen (iqb 2026MerhoehtBStochastikWTR3-2c, 2026MerhoehtBStochastikMMS3-2c, Niveau III).
75  - Näherungsformel (Einheit 2): „Formel vorwärts oder rückwärts?“ – ankreuzen, ob aus Stichprobenanteil und Umfang die Grenzen gesucht sind oder aus einer Grenze das Stichprobenergebnis bzw. der Umfang; nichts rechnen (Vorstufe) → die Grenzen aus Stichprobenergebnis und Umfang berechnen und im Diagramm zuordnen (Grundfall, viermal; iqb 2026MerhoehtBStochastikMMS3-2a) → rückwärts: aus einer Grenze das Stichprobenergebnis bestimmen (iqb 2026MerhoehtBStochastikWTR3-2a) → Prüfungshöhe: den kleinsten Umfang für Unverträglichkeit über die Ungleichung ermitteln (iqb 2023MerhoehtBStochastikWTR1-4b, Niveau III).
76  - Argumente (Einheit 3): „Was ändert n?“ – zu Aussagen über den Stichprobenumfang ankreuzen, ob sie stimmen (größeres n macht das Intervall enger, aber nicht proportional); nichts rechnen (Vorstufe) → aus der Lage des Stichprobenanteils eine Grenzaussage begründen und die Verträglichkeit beschreiben (Grundfall, viermal; iqb 2023MerhoehtBStochastikWTR1-4a) → den Längenfaktor bei doppeltem Umfang aus der Formel begründen (iqb 2018MerhoehtBStochastikWTR2-1g) → Prüfungshöhe: die Verträglichkeit zweier Annahmen über die n-Schwellen beurteilen (iqb 2025MerhoehtBStochastikWTR3-2d, Niveau III).
77
78  ### Prüfungsform (fhr / abi / iqb)
79  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, und die führen Konfidenzintervalle für alle vier Zielprüfungen mit „nein“ (kein Papier der Prüfungsschwerpunkte 2027 nennt sie; Vokabular-Recherche vom 14.09.2026 nach „Konfidenz“, „Vertrauens“, „Schätz“). Kein Landesheft hat je eine Konfidenzzeile gestellt; der Pool prüft seit 2017 erhöht in Teil B – das Thema wird wie matrizen-und-uebergangsprozesse.md als Typenquelle erfasst und über die Geltung gefiltert; die Relevanz künftiger Jahrgänge ist geklärt: In den Prüfungsschwerpunkten 2027 ist „Schätzen von Wahrscheinlichkeiten aus relativen Häufigkeiten (k−σ−Regeln, 1/√n−Gesetz)“ gestrichen, in Leistungs- wie Grundkurs – der unmittelbare Nachbar der Konfidenzintervalle fällt weg, aufgenommen wird nichts (befund-geltung-2026-09-21.md § 2). Für fhr gibt es keinen Stoff und keine Zeile; abi hat keine Zeile. Die Rohdatei zählt 13 Zeilen mit 10 Haupttypen (nur iqb), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
80  iqb (13 Zeilen, 10 Typen; Pool 2017–2026, ausschließlich erhöht, alle in Teil B) [iqb-Katalog]: Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben (2, E1) · Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen (2, E1) · Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen (2, E1) · je 1: Grenzen eines Konfidenzintervalls aus dem Stichprobenergebnis über die Näherungsformel berechnen und im Diagramm zuordnen (E2) · Konfidenzintervall aus dem Diagramm identifizieren und Stichprobenergebnis aus der Grenze berechnen (E2) · Kleinsten Stichprobenumfang für die Unverträglichkeit eines Anteils mit einer Annahme über die Näherungsformel ermitteln (E2) · Länge eines Konfidenzintervalls bei doppeltem Stichprobenumfang über den Faktor 1/√2 begründen (E3) · Obere Grenze eines Konfidenzintervalls über den Stichprobenanteil begründen und Verträglichkeit einer Annahme beschreiben (E3) · Verträglichkeit einer vermuteten Trefferwahrscheinlichkeit über das 1,96σ-Intervall um den Erwartungswert prüfen (E2) · Verträglichkeit zweier Annahmen mit demselben Stichprobenanteil über den Stichprobenumfang beurteilen (E3). Muster: Fünf Pooljahre stellen das Thema als Teil einer Teil-B-Kette (2017 Saatgut – seit dem Nachzug 2026-09-28: die vermutete Keimwahrscheinlichkeit über das 1,96σ-Intervall um den Erwartungswert gegen die beobachtete Keimzahl geprüft, 2017MerhoehtBStochastikWTR-1g, drei Punkte, Niveau II, die Prognoseform ohne Grenzgleichung –, 2018 Flachbildschirme, 2023 zehnseitiger Holzkörper, 2025 Radausflügler, 2026 Alleinfahrende; zwei bis fünf Punkte je Teilaufgabe); das Pooljahr 2026 liegt doppelt vor – WTR- und MMS-Fassung mit zwei wortgleichen Teilaufgaben und je einer eigenen Rechenform (die ersten MMS-Zeilen des Bündels). Keine Zeile kehrt in einem Landesheft wieder (keine Dubletten, keine Abwandlungen – einzig dieses Stochastik-Thema ohne Landesspur). Amtlicher Anforderungsbereich in allen 13 Zeilen (höchster Bereich: II 8, III 5); Niveau II 8, III 5.
81  Zielmarke: Einheit 1 – die Überdeckungszahl als Binomialgröße mit Nachweis (2026MerhoehtBStochastikWTR3-2c, drei Punkte, Niveau III) und das grafische Intervall mit Beurteilung (2025MerhoehtBStochastikWTR3-2c, fünf Punkte, Niveau II). Einheit 2 – der kleinste Umfang für Unverträglichkeit (2023MerhoehtBStochastikWTR1-4b, vier Punkte, Niveau III) und die Grenzenrechnung der MMS-Fassung (2026MerhoehtBStochastikMMS3-2a, Niveau II). Einheit 3 – die n-Schwellen-Beurteilung (2025MerhoehtBStochastikWTR3-2d, fünf Punkte, Niveau III) und der Längenfaktor (2018MerhoehtBStochastikWTR2-1g, Niveau III).
````

## 2 Originale (13)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2017MerhoehtBStochastikWTR-1g (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Rechnung · antwort Zahl|Text
- gegeben: Für eine Qualitätsstufe C wird eine Keimwahrscheinlichkeit von 60 % vermutet; von 50 gesäten Samenkörnern keimen 27; eine Wahrscheinlichkeit von 60 % ist bei einer Sicherheitswahrscheinlichkeit von 95 % mit dieser Anzahl verträglich, wenn 27 im Intervall [μ − 1,96σ; μ + 1,96σ] liegt, μ und σ von B(50; 0,6)
- gesucht: Untersuchung, ob die vermutete Wahrscheinlichkeit von 60 % mit 27 keimenden Samenkörnern verträglich ist
- verfahren: μ = 50 · 0,6 = 30, σ = √(50 · 0,6 · 0,4) ≈ 3,46; Intervallgrenzen berechnen und 27 einordnen
- fehlerquelle: die relative Häufigkeit 0,54 statt der Anzahl 27 mit dem Intervall vergleichen

### 2026MerhoehtBStochastikWTR3-2c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Begründung|Rechnung · antwort Text
- gegeben: 20 weitere Stichproben (n = 500), Konfidenzintervalle zu 95 %, p konstant; Y Anzahl der Intervalle, die p überdecken; Aussage: P(genau 19) < 42 %
- gesucht: Verteilung von Y mit Erläuterung und Nachweis der Aussage
- verfahren: Y binomialverteilt mit n = 20, q = 0,95; P(Y = 19) berechnen
- fehlerquelle: P(Y ≥ 19) statt P(Y = 19)

### 2025MerhoehtBStochastikWTR3-2c (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 5 · format Rechnung|Begründung · antwort Text
- gegeben: Vermutung p = 20 %; Stichprobe 900 mit 153 Radausflüglern; Graphen von g1(p) = p − 1,64 √(p(1 − p)/900) und g2(p) = p + 1,64 √(p(1 − p)/900); Sicherheitswahrscheinlichkeit 90 %
- gesucht: Konfidenzintervall grafisch und Beurteilung der Vermutung
- verfahren: h berechnen, Waagerechte mit beiden Graphen schneiden, 0,2 prüfen
- fehlerquelle: Senkrechte bei p = 0,17 statt Waagerechte bei h = 0,17 (liefert [0,15; 0,19] nur zufällig ähnlich)

### 2023MerhoehtBStochastikWTR1-4b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Annahme p = 0,1; beobachtet genau 15 % „0“; Sicherheitswahrscheinlichkeit 95 %
- gesucht: kleinste Anzahl von Würfen, bei der 15 % nicht mit p = 0,1 verträglich sind
- verfahren: Abstand 0,05 mit 1,96 · √(p(1 − p)/n) vergleichen, n suchen
- fehlerquelle: Anzahl statt Anteil in die Formel setzen

### 2026MerhoehtBStochastikMMS3-2a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 3 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: 20 Stichproben vom Umfang 500; Konfidenzintervall zu 95 % aus |h − p| = 1,96 · √(p(1 − p)/n); Abbildung 2 mit den Intervallen 1 bis 20; in einer Stichprobe fahren 356 Personen allein
- gesucht: Grenzen des zugehörigen Konfidenzintervalls auf Tausendstel genau, rechnerisch; seine Nummer
- verfahren: h = 0,712 einsetzen, Gleichung nach p lösen (zwei Lösungen), Intervall im Diagramm suchen
- fehlerquelle: Näherung h ± 1,96 · √(h(1 − h)/n) statt der Gleichung in p (liefert 0,672 und 0,752)

### 2025MerhoehtBStochastikWTR3-2d (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 5 · format Begründung · antwort Text
- gegeben: Stichprobenanteil h = 0,17, Sicherheitswahrscheinlichkeit 90 %; Aussage: obwohl 0,17 in der Mitte zwischen 0,14 und 0,20 liegt, kann p = 0,14 unverträglich und p = 0,20 verträglich sein; Rechnungen I: 0,17 = 0,14 + 1,64 √(0,14 · 0,86/n) ⇒ n ≈ 359,8; II: 0,17 = 0,20 − 1,64 √(0,2 · 0,8/n) ⇒ n ≈ 478,2
- gesucht: Beurteilung der Aussage mit beiden Rechnungen
- verfahren: beide Gleichungen als Schwellen für n deuten, Schnittbereich angeben
- fehlerquelle: Richtung der Ungleichungen in n vertauschen

### 2018MerhoehtBStochastikWTR2-1g (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung|Begründung · antwort Text
- gegeben: Flachbildschirme, im Mittel einer von fünf fehlerhaft; zweite Stichprobe vom Umfang 2n, ebenfalls 15 % fehlerhaft; gleiche Sicherheitswahrscheinlichkeit
- gesucht: Begründung, dass das Konfidenzintervall kürzer, aber nicht halb so lang ist
- verfahren: Länge 2k√(h(1 − h)/n) mit 2n vergleichen: Faktor 1/√2
- fehlerquelle: Länge als proportional zu 1/n annehmen

### 2018MerhoehtBStochastikWTR2-1f (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Flachbildschirme, im Mittel einer von fünf fehlerhaft; große Stichprobe mit 15 % fehlerhaften; Graphen A, B, C, D der Funktionen f_k(p) = p − k · √(p(1 − p)/n) und g_k(p) = p + k · √(p(1 − p)/n) für die Sicherheitswahrscheinlichkeiten 90 % und 95 %
- gesucht: Konfidenzintervall zu 95 %; Entscheidung, ob die Aussage „einer von fünf fehlerhaft“ gestützt wird
- verfahren: Die äußeren Graphen (größeres k) bei 0,15 schneiden und die p-Werte ablesen
- fehlerquelle: die inneren Graphen B und C (90 %) verwenden

### 2026MerhoehtBStochastikWTR3-2b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Kurzantwort|Begründung · antwort Zahl
- gegeben: Abbildung 2 mit 20 Konfidenzintervallen
- gesucht: ein p, das mit genau 19 der 20 Ergebnisse verträglich ist, mit Begründung
- verfahren: Senkrechte suchen, die genau 19 Intervalle schneidet
- fehlerquelle: p wählen, das alle 20 Intervalle trifft

### 2026MerhoehtBStochastikMMS3-2b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 2 · format Kurzantwort|Begründung · antwort Zahl
- gegeben: Abbildung 2 mit 20 Konfidenzintervallen
- gesucht: ein p, das mit genau 19 der 20 Ergebnisse verträglich ist, mit Begründung
- verfahren: Senkrechte suchen, die genau 19 Intervalle schneidet
- fehlerquelle: p wählen, das alle 20 Intervalle trifft

### 2026MerhoehtBStochastikMMS3-2c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 3 · format Begründung|Rechnung · antwort Text
- gegeben: 20 weitere Stichproben (n = 500), Konfidenzintervalle zu 95 %, p konstant; Y Anzahl der Intervalle, die p überdecken; Aussage: P(genau 19) < 42 %
- gesucht: Verteilung von Y mit Erläuterung und Nachweis der Aussage
- verfahren: Y binomialverteilt mit n = 20, q = 0,95; P(Y = 19) berechnen
- fehlerquelle: P(Y ≥ 19) statt P(Y = 19)

### 2026MerhoehtBStochastikWTR3-2a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: 20 Konfidenzintervalle (95 %) aus Stichproben vom Umfang 500 nach |h − p| = 1,96 √(p(1 − p)/n); eines hat die obere Grenze 0,75
- gesucht: Nummer dieses Intervalls und passende Anzahl der Alleinfahrenden in der Stichprobe
- verfahren: Intervall ablesen, h aus der Grenzgleichung, mal 500
- fehlerquelle: 0,75 · 500 = 375 als Anzahl nehmen

### 2023MerhoehtBStochastikWTR1-4a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: zehnseitiger Holzkörper 0 bis 9; 80 Würfe, zwölfmal „0“; Konfidenzintervall zur Sicherheitswahrscheinlichkeit 95 % mit unterer Grenze etwa 0,09
- gesucht: Begründung, dass die obere Grenze größer als 0,1 ist; Bedeutung für die Annahme p = 10 %
- verfahren: Stichprobenanteil als Punkt im Intervall, Vergleich mit 0,1
- fehlerquelle: obere Grenze über die Symmetrie um 0,15 rechnen wollen

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
