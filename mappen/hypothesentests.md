# Mappe: hypothesentests

Eintrag: hz-0801/mathe-nachhilfe, katalog/hypothesentests.md
Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26T16:47:30+02:00, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:42 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Hypothesentests
 3
 4  ### Verortung
 5  Der einseitige Signifikanztest an der Binomialverteilung: die Entscheidungsregel bestimmen (unter der Nullhypothese ist die Trefferzahl binomialverteilt, der Ablehnungsbereich liegt auf der Seite der  … (gekürzt, 1614 Zeichen)
 6  [GOST] Q4, 4. Kurshalbjahr (BB S. 30), nur „Zusätzlich im Leistungskursfach“: L5-Zeile „Hypothesentests bei Binomialverteilungen interpretieren und die Unsicherheit und Genauigkeit der Ergebnisse begr … (gekürzt, 1573 Zeichen)
 7  [FOS] Kein Stoff: der RLP FOS 2019 führt weder Hypothesentests noch Signifikanz (Suchprotokoll: „Hypothese“, „Signifikanz“ in der Textfassung ohne Treffer); keine fhr-Zeile.
 8  [LS-AA] Qualifikationsphase Kapitel IX „Testen mit der Binomialverteilung“: 1 „Einseitiger Hypothesentest“, 2 „Fehler beim Testen von Hypothesen“, 3 „Wahl der Nullhypothese“, 4 „Zweiseitiger Hypothesentest“. Zuordnung: Einheit 1 = IX 1; Einheit 2 = IX 3; Einheit 3 = IX 2; IX 4 (zweiseitig) trägt keine Katalogzeile – wie die Alternativtests des Plans (Befund). Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Entscheidungsregel bestimmen: die Nullhypothese liefert p und die Binomialverteilung der Testgröße, die Alternative die Seite des Ablehnungsbereichs (rechtsseitig bei „mehr als“, linksseitig bei „weniger als“); die Grenze über kumulierte Wahrscheinlichkeiten so wählen, dass das Signifikanzniveau eingehalten wird – und die Minimalität am Nachbarwert belegen (die Lücke im vorgelegten Lösungsweg ist genau dieser fehlende Nachbarwert). (Q4 LK; Prüfform jedes Testjahrs) ← Eingabe „entscheidungsregel“, „ablehnungsbereich“, „signifikanztest“, „signifikanzniveau“
12    Marken: BE Q4 · BB Q4 · nur LK · Abitur LK
13  2. Die Nullhypothese wählen: aus der Sicht des Entscheiders – kontrolliert ist allein der Fehler erster Art, sein Risiko ist durch das Signifikanzniveau begrenzt; die teure oder riskante Konsequenz wird deshalb an die Ablehnung der Nullhypothese geknüpft, und die Überlegung wird im Sachzusammenhang benannt. (Q4 LK; BE Kap. 4 „kein sicheres Urteil“) ← Eingabe „nullhypothese wählen“, „warum diese hypothese“, „fehler kontrolliert“
14    Marken: BE Q4 · BB Q4 · nur LK · Abitur LK
15  3. Fehlerarten und Güte: den Fehler zweiter Art für selbst gewählte Anteile berechnen (p dort wählen, wo die Nullhypothese falsch ist), einordnen und im Sachzusammenhang beschreiben; Mindestanteile für eine Fehlerschranke; die Gütekurve lesen (Ablehnwahrscheinlichkeit in Abhängigkeit von p – Fehler zweiter Art als Gegenwahrscheinlichkeit, Fehler erster Art an der Grenze) und den Stichprobenumfang beurteilen (größeres n verkleinert den Fehler zweiter Art). (Q4 LK; Prüfungshöhe) ← Eingabe „fehler zweiter art“, „fehler erster art“, „gütekurve“, „stichprobenumfang test“
16    Marken: BE Q4 · BB Q4 · nur LK · Abitur LK
17  Warum drei: Die Entscheidungsregel (dreizehn Zeilen) ist die Rechenroutine und jährliche Prüfform; die Wahl der Nullhypothese (sieben Zeilen, ein Typ) ist die Argumentationsfigur, die das Lehrwerk als … (gekürzt, 808 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; abitur-Typen wörtlich aus abitur/abitur-typen.csv.
21  Einheit 1: Entscheidungsregel eines einseitigen Signifikanztests bestimmen (10) · Ablehnungsgrenze bei größerem Stichprobenumfang ohne höheren Fehler erster Art bestimmen (1; Ermessen, siehe Offene Punkte) — Nachweis: Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen (2) — kein Deutungstyp. Dazu: Fehler finden (rechts- statt linksseitig getestet; die Grenze um eins verfehlt, weil das knapp überschrittene Niveau in Kauf genommen wurde; die Minimalität nicht oder in der falschen Richtung belegt) · Begründen (warum die Seite des Ablehnungsbereichs aus der Alternative folgt; warum der Nachbarwert zur Begründung der Grenze gehört).
22  Einheit 2: kein Berechnungstyp — kein Nachweistyp — Deutung: Wahl der Nullhypothese aus der Sicht des Entscheiders begründen (7). Dazu: Fehler finden (den Fehler zweiter Art als kontrolliert angesehen oder als Grund der Wahl genannt; die Überlegung ohne Bezug zum begrenzten Risiko formuliert) · Begründen (warum nur der Fehler erster Art durch das Signifikanzniveau begrenzt ist; wem welcher Irrtum schadet).
23  Einheit 3: Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen (3) · Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben (2) · Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln (2) · Stichprobenumfang eines Tests aus Ablehnungsgrenze und Fehler erster Art am Graphen ermitteln (1) — Nachweis: Untere Schranke für den Stichprobenumfang eines Tests über den Fehler erster Art am Graphen begründen (1) — Deutung: Fehlentscheidungen eines Tests im Sachzusammenhang beschreiben (1; Ermessen, siehe Offene Punkte) · Nutzen eines größeren Stichprobenumfangs über den Fehler zweiter Art an den Gütekurven begründen (1). Dazu: Fehler finden (p auf der Seite gewählt, wo die Nullhypothese wahr ist – dort gibt es keinen Fehler zweiter Art; den Fehler erster Art als zweiten gerechnet; das Komplement des Annahmebereichs verfehlt; am Graphen die falsche Stelle abgelesen; die Monotonie in n in der falschen Richtung) · Begründen (warum der Fehler zweiter Art vom gewählten p abhängt und nahe eins liegen kann; warum größeres n ihn verkleinert).
24  Zählung: 3 + 1 + 7 = 11 Haupttypen, 13 + 7 + 11 = 31 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: CAS-Nachtrag 2018 und Pool 2017 erhöht Teil B, WTR und CAS; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2018 erhöht Teil B CAS)).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Kumulierte Binomialwahrscheinlichkeiten berechnen und lesen – das Rechenwerkzeug jeder Entscheidungsregel. Sek-II-Nachbarthema binomialverteilung.md. [GOST Q2 L5 „Punkt- und Intervallwahrscheinlichkeiten“]
29  - Gegenereignis und Komplementärsummen („mindestens“ gegen „höchstens“) – die Übersetzung der Bereiche in Einheit 1 und 3. Sek-I-Thema wahrscheinlichkeit.md, Sek-II-Nachbarthema binomialverteilung.md. [GOST-OHiMi 2.4]
30  - Erwartungswert n · p als Orientierung, auf welcher Seite der Ablehnungsbereich liegt. Sek-II-Nachbarthema kenngroessen-von-verteilungen.md (dasselbe Bündel). [GOST Q2 L2]
31  - Funktionsgraphen ablesen und deuten (Werte, Monotonie) – die Gütekurven der Einheit 3. Sek-I-Thema lineare-funktionen.md (Grundfertigkeit Graphenlesen). [GOST Eingangsvoraussetzung L4]
32  - Den Rechner für kumulierte Verteilungswahrscheinlichkeiten einsetzen – alle Zeilen liegen in Teil B (Werkzeugwissen; die Befehle stehen in keiner Formelsammlung). [IQB-STR 1: Teil B mit WTR]
33  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
34  - „Welche Richtung?“ – zu Nullhypothesen und Alternativen ankreuzen, ob rechtsseitig (Alternative „mehr als“) oder linksseitig (Alternative „weniger als“) abgelehnt wird; nichts rechnen. Vor Einheit 1. [Rohdatei-Fehlerquelle „rechtsseitig statt linksseitig“; abi 2025-bebb-lk-B4e]
35  - „Welcher Fehler?“ – zu Irrtumsbeschreibungen ankreuzen, ob Fehler erster Art (Nullhypothese zutreffend, aber abgelehnt) oder zweiter Art (Nullhypothese falsch, aber beibehalten) gemeint ist; nichts rechnen. Vor Einheit 2 und 3. [BE Kap. 4 „benennen und im Kontext deuten“]
36  - „Wo darf p liegen?“ – ankreuzen, für welche Anteile ein Fehler zweiter Art überhaupt möglich ist (nur dort, wo die Nullhypothese falsch ist); nichts rechnen. Vor Einheit 3. [Rohdatei-Fehlerquelle „p auf der falschen Seite“; iqb 2026MerhoehtBStochastikWTR2-2b]
37
38  ### Merkkasten
39  Einheit 1 (Entscheidungsregel):
40      Schema: die Nullhypothese liefert die Trefferwahrscheinlichkeit und damit die Binomialverteilung der Testgröße; die Alternative liefert die Seite – abgelehnt wird dort, wo das Stichprobenergebnis für die Alternative spricht.
41      Grenze: die kumulierte Wahrscheinlichkeit des Ablehnungsbereichs unter der Nullhypothese darf das Signifikanzniveau nicht überschreiten – und beim nächsten Wert überschreitet sie es (Minimalität am Nachbarwert belegen, sonst ist die Regel nicht begründet).
42        Beispiel Optiker: Nullhypothese p ≤ 0,3, n = 100, Niveau 5 % – gesucht ist die kleinste Trefferzahl k, ab der P(X ≥ k) höchstens 0,05 beträgt; wer die Grenze eine Stufe zu früh zieht, nimmt gut 5,3 % Irrtumsrisiko in Kauf.
43      Formulieren: die Regel als Anweisung aussprechen („wird … erreicht oder überschritten, wird die Nullhypothese abgelehnt, sonst nicht“).
44      Auswendig (Teil A): Begriffe und Logik (Nullhypothese, Signifikanzniveau, Ablehnungsbereich, Entscheidungsregel) – begründetes Ermessen: [GOST-OHiMi 2.4 LK] kündigt „inhaltliche Betrachtungen zu Hypothesentests“ hilfsmittelfrei an, der Katalog hat bisher keine Teil-A-Zeile; alle Rechnungen sind Teil-B-Stoff mit WTR.
45      Formelsammlung: [FS-IQB] führt im Abschnitt „Signifikanztest“ nur die Begriffe (Fehlerarten, Signifikanzniveau; Textfassung 427–432), kein Testschema und keine Entscheidungsregel – das Schema muss sitzen, die kumulierten Wahrscheinlichkeiten kommen aus dem Rechner – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
46  Quelle: eigene Formulierung nach [GOST Q4 LK] „Signifikanzniveau, Ablehnungsbereich und Entscheidungsregel“; Zahlenbeispiel aus abi 2018-bb-ea-B4.2d; [LS-AA QP IX 1].
47
48  Einheit 2 (Wahl der Nullhypothese):
49      Leitgedanke: kontrolliert ist allein der Fehler erster Art – seine Wahrscheinlichkeit ist durch das Signifikanzniveau begrenzt; der Fehler zweiter Art bleibt unkontrolliert und kann groß sein.
50      Deshalb: der Entscheider knüpft die teure oder riskante Konsequenz an die Ablehnung der Nullhypothese – dann ist das Risiko, sie irrtümlich auszulösen, durch das Niveau begrenzt (der teure Wechsel nur bei nachgewiesener Verbesserung, die Abschaltung nur bei nachgewiesenem Erfolgseinbruch).
51      Benennen: die Überlegung im Sachzusammenhang aussprechen – welcher Irrtum wem schadet und welcher durch das Niveau klein gehalten wird.
52      Auswendig (Teil A): der ganze Kasten – die Argumentationsfigur ist der Kern der „inhaltlichen Betrachtungen“ der Anlage [GOST-OHiMi 2.4 LK] und wörtlich das, was [BE Kap. 4] verlangt („kein sicheres Urteil“, Fehlerarten „benennen und im Kontext deuten“).
53      Formelsammlung: [FS-IQB „Signifikanztest“] definiert Fehler erster und zweiter Art und das Signifikanzniveau (Textfassung 427–432) – die Wahlfigur selbst steht nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
54  Quelle: eigene Formulierung nach [BE Kap. 4] (Zeilen 1404–1407) und der Rohdatei (fünf Zeilen des Wahltyps); ohne Zahlenbeispiel (die Figur ist zahlenfrei; Ermessen); [LS-AA QP IX 3].
55
56  Einheit 3 (Fehlerarten und Güte):
57      Fehler erster Art: die Nullhypothese trifft zu und wird trotzdem abgelehnt – die Wahrscheinlichkeit ist durch das Niveau begrenzt und an der Grenze der Nullhypothese am größten.
58      Fehler zweiter Art: die Nullhypothese ist falsch und wird trotzdem beibehalten – seine Wahrscheinlichkeit ist die Annahmebereichs-Wahrscheinlichkeit unter einem selbst gewählten p aus der Alternative; sie hängt von diesem p ab und kann nahe eins liegen.
59      Erst wählen, dann rechnen: p dort wählen, wo die Nullhypothese falsch ist – auf der anderen Seite gibt es keinen Fehler zweiter Art, sondern den ersten.
60      Gütekurve: der Graph zeigt die Ablehnwahrscheinlichkeit in Abhängigkeit von p – der Fehler zweiter Art ist eins minus abgelesener Wert, der Fehler erster Art wird an der Grenze der Nullhypothese abgelesen; größerer Stichprobenumfang macht die Kurve steiler und den Fehler zweiter Art kleiner.
61      Auswendig (Teil A): die beiden Fehlerarten benennen und im Kontext deuten – [BE Kap. 4] verlangt es wörtlich; die Rechnungen sind Teil-B-Stoff.
62      Formelsammlung: [FS-IQB „Signifikanztest“] definiert beide Fehlerarten und das Signifikanzniveau (Textfassung 427–432) – in Teil B nachschlagbar; Gütekurven und Rechenwege stehen nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
63  Quelle: eigene Formulierung nach [GOST Q4 LK] „Fehler 1. und 2. Art“, „Unsicherheit der Ergebnisse“ und [BE Kap. 4]; ohne Zahlenbeispiel (die Regeln sind zahlenfrei formuliert; Ermessen); [LS-AA QP IX 2].
64
65  ### Typische Fehler
66  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 22 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
67  - Richtung vertauscht: rechts- statt linksseitig getestet oder umgekehrt – die Seite folgt aus der Alternative, nicht aus der Nullhypothese. [abi 2023-bebb-lk-B4i, 2025-bebb-lk-B4e; iqb 2018MerhoehtBStochastikWTR1-1c, 2025MerhoehtBStochastikWTR2-2c]
68  - Grenze um eins verfehlt: den Wert mit knapp überschrittenem Niveau noch in den Ablehnungsbereich genommen; die Minimalität der Grenze nicht belegt oder den Nachbarwert in der falschen Richtung geprüft. [abi 2018-bb-ea-B4.2d, 2024-bebb-lk-B4e; iqb 2026MerhoehtBStochastikWTR2-2a, 2024MerhoehtBStochastikWTR1-2b]
69  - Fehlerarten verwechselt: den Fehler zweiter Art als kontrolliert angesehen oder als Grund der Nullhypothesen-Wahl genannt; p auf der Seite gewählt, wo die Nullhypothese wahr ist, und damit den Fehler erster Art gerechnet; beim Fehler zweiter Art das Komplement des Annahmebereichs verfehlt. [abi 2022-bebb-lk-B4h, 2024-bebb-lk-B4d, 2023-bebb-lk-B4j, 2024-bebb-lk-B4f, 2025-bebb-lk-B4f; iqb 2022MerhoehtBStochastikWTR1-2b, 2024MerhoehtBStochastikWTR1-2a, 2024MerhoehtBStochastikWTR1-2c, 2025MerhoehtBStochastikWTR2-2d, 2026MerhoehtBStochastikWTR2-2b, 2023MerhoehtBStochastikWTR2-2c, 2018MerhoehtBStochastikWTR1-1d]
70  - Graphen falsch gelesen: den Fehler erster Art an der falschen Stelle oder am falschen Rand des Ablehnungsbereichs abgelesen; die Monotonie in n in der falschen Richtung angesetzt. [abi 2022-bebb-lk-B4g; iqb 2022MerhoehtBStochastikWTR1-2a]
71
72  ### Für schwache Schüler
73  Mindeststoff (GK-Kern Q2/Q4 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: keiner – das Thema ist LK-Zusatz beider Länder, die Geltungsdateien führen es nur für die beiden Leistungskurs-Zielprüfungen mit „ja“, und alle Zeilen sind erhöht bzw. Leistungskurs; der Grundkurs trägt nur die Vorstufe (k-σ-Regeln, Signifikanzbegriff – ohne Katalogzeile, das Schätzumfeld liegt bei konfidenzintervalle.md). RLP FOS (fhr): kein Stoff, keine Zeile. Mindeststoff innerhalb des LK: Einheit 1 und 2 (Entscheidungsregel als jährliche Prüfform, Wahltyp als stehende Argumentationsfigur); Einheit 3 ist Prüfungshöhe (die Fehlerrechnungen tragen die höchsten Anforderungsbereiche). Niveaustufe H der E-Phase [RLP]: kein Bezug – die Sek-I-Pläne kennen keine beurteilende Statistik; Blatt-0-Stoff sind kumulierte Wahrscheinlichkeiten und Gegenereignis. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung keine beurteilende Statistik – deckt sich mit der LK-Einordnung, kein zusätzlicher Posten.
74  Grundvorstellung (Blatt 0) [BE Kap. 4 „kein sicheres Urteil“, MO]: Ein Test beweist nichts – er kontrolliert nur, wie oft man höchstens irrt, wenn man einer Behauptung widerspricht. „Eine Firma behauptet, höchstens jeder zwanzigste Riegel sei zu leicht. Du wiegst eine Stichprobe und findest auffällig viele leichte Riegel, kein Term: Ab wann würdest du widersprechen – beim ersten leichten Riegel, bei ein paar mehr als erwartet, oder erst, wenn dein Ergebnis unter der Behauptung sehr unwahrscheinlich wäre? Kannst du dich irren, obwohl du sorgfältig rechnest? Und wer trägt den Schaden, wenn du irrtümlich widersprichst – und wer, wenn du irrtümlich schweigst?“ Wer vom Test ein sicheres Urteil erwartet oder beide Irrtümer für gleich kontrolliert hält, braucht das vor jeder Rechnung: begrenzt ist nur der Irrtum beim Widersprechen, und die Grenze legt man vorher fest. Verständnis, nicht Verfahren; die Vorstellung ist amtlich ([BE Kap. 4] wörtlich), die Aufgabenform ist Ermessen. [GOST Q4 LK „Unsicherheit der Ergebnisse“; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Fehler zweiter Art als kontrolliert angesehen“; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
75  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
76  - Entscheidungsregel (Einheit 1): „Welche Richtung?“ ankreuzen (Vorstufe) → die Regel rechtsseitig bestimmen: kleinste Trefferzahl mit eingehaltenem Niveau (Grundfall, viermal; abi 2018-bb-ea-B4.2d) → die Regel linksseitig: größte Trefferzahl unterhalb der Grenze (abi 2023-bebb-lk-B4i, iqb 2018MerhoehtBStochastikWTR1-1c, 2026MerhoehtBStochastikWTR2-2a) → die Grenze am Nachbarwert absichern (abi 2025-bebb-lk-B4e, iqb 2025MerhoehtBStochastikWTR2-2c) → Prüfungshöhe: die Lücke in einem vorgelegten Lösungsweg benennen und den fehlenden Nachbarwert ergänzen (abi 2024-bebb-lk-B4e, iqb 2024MerhoehtBStochastikWTR1-2b, Niveau II bis III).
77  - Wahl der Nullhypothese (Einheit 2): „Welcher Fehler?“ ankreuzen (Vorstufe, Grundvorstellung) → die Figur am teuren Wechsel: nur bei nachgewiesener Verbesserung handeln (Grundfall, viermal; iqb 2018MerhoehtBStochastikWTR1-1d) → die Figur an der laufenden Entscheidung: Abschalten nur bei nachgewiesenem Einbruch (abi 2024-bebb-lk-B4d, iqb 2024MerhoehtBStochastikWTR1-2a) → Prüfungshöhe: zwischen zwei möglichen Nullhypothesen die gewählte aus der Schadenslage begründen (abi 2022-bebb-lk-B4h, iqb 2022MerhoehtBStochastikWTR1-2b, Anforderungsbereich III).
78  - Fehlerarten und Güte (Einheit 3): „Wo darf p liegen?“ ankreuzen (Vorstufe) → den Fehler zweiter Art für ein selbst gewähltes p berechnen und im Sachzusammenhang deuten (Grundfall, viermal; abi 2023-bebb-lk-B4j) → am Graphen der Ablehnwahrscheinlichkeit ablesen: eins minus Wert (iqb 2026MerhoehtBStochastikWTR2-2b) → den Nachweis führen, dass der Fehler zweiter Art sehr groß sein kann (abi 2024-bebb-lk-B4f, iqb 2024MerhoehtBStochastikWTR1-2c) → den Mindestanteil für eine Fehlerschranke ermitteln und den Fehler beschreiben (abi 2025-bebb-lk-B4f, iqb 2025MerhoehtBStochastikWTR2-2d) → Prüfungshöhe: Stichprobenumfang und Gütekurven – Umfang aus Grenze und Fehler erster Art, Schranke über die Monotonie, Kosten-Nutzen-Abwägung (abi 2022-bebb-lk-B4g, iqb 2022MerhoehtBStochastikWTR1-2a, 2023MerhoehtBStochastikWTR2-2c, Niveau III).
79
80  ### Prüfungsform (fhr / abi / iqb)
81  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md: be-lk und bb-ea „ja“, be-gk und bb-gk „nein“ (abitur-vokabular.md führt das Thema unter „nur auf erhöhtem Niveau geprüft“). Für fhr gibt es keinen Stoff und keine Zeile. Die Rohdatei zählt 31 Zeilen mit 11 Haupttypen (abi 11 Zeilen, 6 Typen; iqb 20 Zeilen, 10 Typen; 5 abitur-Typen in beiden Abiturprofilen), Jahre 2017–2026; alle Zeilen liegen in Teil B mit WTR oder CAS. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
82  abi (11 Zeilen, 6 Typen; Landeshefte bb-ea 2018 und bebb-lk 2022–2025, davon 1 aus der CAS-Fassung 2018) [abi-Katalog]: Entscheidungsregel eines einseitigen Signifikanztests bestimmen (4, E1) · Wahl der Nullhypothese aus der Sicht des Entscheiders begründen (2, E2) · Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen (2, E3) · je 1: Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen (E1) · Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben (E3) · Untere Schranke für den Stichprobenumfang eines Tests über den Fehler erster Art am Graphen begründen (E3). Muster: Alle elf Zeilen liegen in Teil B der Leistungskurs-Hefte (zwei bis fünf Punkte), seit 2022 in jedem bebb-lk-Heft als Schlussteil der Stochastik-Aufgabe; die Optiker-Regel 2018 steht wortgleich auch in der CAS-Fassung, dort ohne Tafel der summierten Binomialverteilung (2018-bb-ea-cas-B4.2d, fünf Punkte, Niveau III; seit dem Nachzug 2026-09-28). Sechs Zeilen sind wortgleiche Pooldubletten (2022-bebb-lk-B4h, 2024-bebb-lk-B4d, 2024-bebb-lk-B4e, 2024-bebb-lk-B4f, 2025-bebb-lk-B4e, 2025-bebb-lk-B4f), eine ist abgewandelt (2022-bebb-lk-B4g aus 2022MerhoehtBStochastikWTR1-2a: das Heft verlangt nur die Schranke für den Umfang, der Pool den Umfang selbst – die erste abgewandelte Poolzeile des Bündels); landeseigen sind 2018-bb-ea-B4.2d mit seiner CAS-Fassung 2018-bb-ea-cas-B4.2d, 2023-bebb-lk-B4i und 2023-bebb-lk-B4j. Niveau II 6, III 5. Kontexte: Optiker-Kunden, Fitnessarmbänder, Gewinnspiel-Buchungen, Zeitungs-Abonnenten, Radausflügler.
83  iqb (20 Zeilen, 10 Typen; Pool 2017–2026, ausschließlich erhöht, alle in Teil B, davon 7 CAS) [iqb-Katalog]: Entscheidungsregel eines einseitigen Signifikanztests bestimmen (6, E1) · Wahl der Nullhypothese aus der Sicht des Entscheiders begründen (5, E2) · Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln (2, E3) · je 1: Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen (E1) · Ablehnungsgrenze bei größerem Stichprobenumfang ohne höheren Fehler erster Art bestimmen (E1) · Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen (E3) · Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben (E3) · Fehlentscheidungen eines Tests im Sachzusammenhang beschreiben (E3) · Nutzen eines größeren Stichprobenumfangs über den Fehler zweiter Art an den Gütekurven begründen (E3) · Stichprobenumfang eines Tests aus Ablehnungsgrenze und Fehler erster Art am Graphen ermitteln (E3). Muster: Jedes Testjahr stellt eine mehrteilige Kette in Teil B (seit dem Nachzug 2026-09-28 mit dem Jahrgang 2017: Saatgut in der WTR-Fassung mit der Entscheidungsregel 2017MerhoehtBStochastikWTR-1f; in der CAS-Fassung die Haushaltsgrößen mit Nullhypothesen-Wahl samt Regel 2017MerhoehtBStochastikCAS1-6 und die Teststreifen mit beschriebenen Fehlentscheidungen 2017MerhoehtBStochastikCAS2-3a und der Ablehnungsgrenze bei doppeltem Umfang ohne höheres Irrtumsrisiko 2017MerhoehtBStochastikCAS2-3b; 2018 Kunststoffteile, 2022 Fitnessarmbänder, 2023 Gewinnspiel, 2024 Zeitungs-Abos, 2025 Radausflügler, 2026 Alleinfahrende; zwei bis fünf Punkte je Teil): erst Entscheidungsregel oder Nullhypothesen-Wahl, dann eine Fehler- oder Güteform. Seit dem Nachzug 2026-09-29 mit der CAS-Fassung 2018 (vier Zeilen): die Kunststoffteile mit fünfhundert statt zweihundert Teilen – die linksseitige Regel mit kumulierten Werten aus dem Rechner (2018MerhoehtBStochastikCAS1-1c, fünf Punkte, Niveau II) und die Nullhypothesen-Wahl wortgleich mit dem WTR-Zweig 2018MerhoehtBStochastikWTR1-1d (2018MerhoehtBStochastikCAS1-1d, drei Punkte, Niveau III nach dem amtlichen Bereich, die WTR-Zeile behält ihre eigene Schätzung); dazu die Kassiererin, die gefälschte Geldscheine ertasten will – die rechtsseitige Regel bei zehn Scheinen (2018MerhoehtBStochastikCAS2-4a, fünf Punkte, Niveau II) und der Fehler zweiter Art für ein selbst gewähltes p am Graphen der Ablehnwahrscheinlichkeit (2018MerhoehtBStochastikCAS2-4b, drei Punkte, Niveau III). Amtlicher Anforderungsbereich in allen 20 Zeilen (höchster Bereich: II 10, III 10); Niveau II 11, III 9. 6 Poolzeilen kehren wortgleich in Landesheften wieder, eine abgewandelt (die Dubletten- und Abwandlungsliste der abi-Zeile).
84  Zielmarke: Einheit 1 – abi: die Entscheidungsregel mit Niveaubegründung (2018-bb-ea-B4.2d, fünf Punkte, Niveau III); iqb: die Regel an der Mindest-Nullhypothese (2026MerhoehtBStochastikWTR2-2a, fünf Punkte, Niveau II) und die Ablehnungsgrenze bei doppeltem Umfang ohne höheren Fehler erster Art (2017MerhoehtBStochastikCAS2-3b, vier Punkte, Niveau III). Einheit 2 – abi und iqb: die Wahl zwischen zwei Nullhypothesen aus der Schadenslage (2022-bebb-lk-B4h, 2022MerhoehtBStochastikWTR1-2b, Anforderungsbereich III). Einheit 3 – abi: der Nachweis, dass der Fehler zweiter Art sehr groß sein kann (2024-bebb-lk-B4f, Niveau III); iqb: der Stichprobenumfang am Gütegraphen (2022MerhoehtBStochastikWTR1-2a, fünf Punkte, Niveau III) und die Kosten-Nutzen-Abwägung über die Gütekurven (2023MerhoehtBStochastikWTR2-2c, Anforderungsbereich III).
````

## 2 Originale (24)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2018-bb-ea-cas-B4.2d (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea-cas · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen sind. Ein Optiker vermutet, dass mehr als 30 % der jungen Erwachsenen aus dem Landkreis Kunden in seinem Geschäft sind. Sollte das nicht der Fall sein, erwägt er eine Werbeaktion mit Flyern. Um unnötige Kosten zu vermeiden, soll die Nullhypothese, dass höchstens 30 % der jungen Erwachsenen Kunden bei diesem Optiker sind, mit einer Stichprobe von 100 jungen Erwachsenen auf einem Signifikanzniveau von 5 % getestet werden.
- gesucht: die zugehörige Entscheidungsregel
- verfahren: Unter der Nullhypothese ist die Trefferzahl X binomialverteilt mit 100 Versuchen und der Trefferwahrscheinlichkeit 0,3. Der Test ist rechtsseitig, weil die Alternative mehr als 30 % lautet. Mit dem CAS die kleinste Trefferzahl k suchen, für die P(X ≥ k) höchstens 5 % beträgt.
- fehlerquelle: die Grenze bei 38 ziehen, weil P(X ≥ 38) nur knapp über 5 % liegt, oder linksseitig testen

### 2022-bebb-lk-B4h (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: Alternative Nullhypothese „Anteil höchstens 7 %“
- gesucht: Überlegung des Händlers für die gewählte H₀ mit Begründung
- verfahren: Kontrollierten Fehler dem für den Händler schädlichen Irrtum zuordnen
- fehlerquelle: Fehler zweiter Art als kontrolliert ansehen

### 2024-bebb-lk-B4d (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Anteil zufriedener Abonnenten derzeit 60 %; Nullhypothese „Anteil höchstens 60 %“, Stichprobe 200, Signifikanzniveau 5 %; Entscheidung über den dauerhaften Einsatz des Algorithmus
- gesucht: mögliche Überlegung des Managements zur Wahl dieser Nullhypothese
- verfahren: den durch das Signifikanzniveau begrenzten Fehler benennen
- fehlerquelle: den Fehler zweiter Art als Grund nennen

### 2024-bebb-lk-B4e (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 4 · format Begründung|Rechnung · antwort Text
- gegeben: Ablehnungsbereich {132; …; 200}; Lösungsschritte: Y Anzahl der zufriedenen Abonnenten, P(Y ≥ 132) ≈ 0,047 (n = 200, p = 0,6)
- gesucht: Begründung, warum die Schritte nicht ausreichen, und Ergänzung
- verfahren: Minimalität der Grenze über P(Y ≥ 131) belegen
- fehlerquelle: P(Y ≥ 133) prüfen (falsche Richtung)

### 2024-bebb-lk-B4f (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 4 · format Rechnung · antwort Text
- gegeben: Ablehnungsbereich {132; …; 200}
- gesucht: Nachweis, dass der Fehler zweiter Art mehr als 90 % betragen könnte
- verfahren: p knapp über 0,6 wählen, P(Y ≤ 131) berechnen
- fehlerquelle: p ≤ 0,6 wählen (dann kein Fehler zweiter Art)

### 2025-bebb-lk-B4e (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 5 · format Rechnung · antwort Text
- gegeben: Nullhypothese: Anteil der Radausflügler höchstens 14 %; Signifikanzniveau 8 %; Stichprobe 500; Busse laufen nur bei Ablehnung weiter
- gesucht: Entscheidungsregel
- verfahren: kumulierte Wahrscheinlichkeiten von oben an der Grenze vergleichen
- fehlerquelle: linksseitig testen

### 2025-bebb-lk-B4f (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 5 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: Test mit n = 200; Ablehnung bei mehr als 35 Radausflüglern; Fehler zweiter Art höchstens 15 %; Busse laufen nur bei Ablehnung weiter
- gesucht: Mindestanteil auf ganze Prozent und Bedeutung des Fehlers zweiter Art
- verfahren: P_p(Y ≤ 35) für p in ganzen Prozent, kleinstes p mit ≤ 15 %; deuten
- fehlerquelle: Fehler zweiter Art als P(Y > 35) unter p = 0,14 rechnen (das ist der Fehler erster Art)

### 2022-bebb-lk-B4g (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 4 · format Begründung · antwort Text
- gegeben: Signifikanztest mit H₀: Anteil fehlerhafter Armbänder mindestens 7 %; Ablehnung bei höchstens vier fehlerhaften Armbändern; Graph des Fehlers erster Art in Abhängigkeit von p
- gesucht: Begründung, dass der Stichprobenumfang sicher größer als 100 ist
- verfahren: Wert bei p = 0,07 unter 0,1 ablesen; für n = 100 wäre er 0,16; mit n fällt P(Y ≤ 4)
- fehlerquelle: Fehler erster Art am rechten Rand des Ablehnungsbereichs suchen; Richtung der Monotonie in n

### 2022MerhoehtBStochastikWTR1-2a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: H₀: Anteil fehlerhafter Armbänder mindestens 7 %; Ablehnung bei höchstens vier fehlerhaften; Graph des Fehlers erster Art in Abhängigkeit von p
- gesucht: Stichprobenumfang
- verfahren: Fehler erster Art bei p = 0,07 ablesen, P(Y ≤ 4) für Nachbarwerte von n vergleichen
- fehlerquelle: Fehler erster Art an der falschen Stelle (p ≠ 0,07) ablesen

### 2018-bb-ea-B4.2d (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen sind. Ein Optiker vermutet, dass mehr als 30 % der jungen Erwachsenen aus dem Landkreis Kunden in seinem Geschäft sind. Sollte das nicht der Fall sein, erwägt er eine Werbeaktion mit Flyern. Um unnötige Kosten zu vermeiden, soll die Nullhypothese, dass höchstens 30 % der jungen Erwachsenen Kunden bei diesem Optiker sind, mit einer Stichprobe von 100 jungen Erwachsenen auf einem Signifikanzniveau von 5 % getestet werden.
- gesucht: die zugehörige Entscheidungsregel
- verfahren: Unter der Nullhypothese ist die Trefferzahl binomialverteilt mit 100 Versuchen und der Trefferwahrscheinlichkeit 0,3. Der Test ist rechtsseitig, weil die Alternative mehr als 30 % lautet. Gesucht ist die kleinste Trefferzahl, ab der die Wahrscheinlichkeit für mindestens so viele Treffer höchstens 5 % beträgt; gleichwertig die kleinste Zahl, bis zu deren Vorgänger die summierte Wahrscheinlichkeit mindestens 0,95 erreicht.
- fehlerquelle: die Grenze bei 38 ziehen, weil die summierte Wahrscheinlichkeit bis 37 schon nahe bei 0,95 liegt, und damit ein Niveau von 5,3 % in Kauf nehmen

### 2023-bebb-lk-B4i (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung · antwort Text
- gegeben: p Buchungswahrscheinlichkeit nach dem Gewinnspiel; Verlängerung lohnt für p ≥ 3 %; H₀: p ≥ 3 % auf dem Signifikanzniveau 5 %; n = 800
- gesucht: Entscheidungsregel
- verfahren: größtes k mit P₀,₀₃⁸⁰⁰(X ≤ k) ≤ 0,05
- fehlerquelle: rechtsseitig testen; k = 16 (0,054 > 0,05) nehmen

### 2023-bebb-lk-B4j (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Wiederholung mit n = 600; H₀ wird abgelehnt, wenn weniger als 11 Personen eine Reise buchen
- gesucht: Fehler 2. Art für zwei geeignete Werte von p; Deutung im Sachzusammenhang
- verfahren: p < 0,03 wählen, P(X ≥ 11) berechnen; als Verlängerung trotz Verlusten deuten
- fehlerquelle: Werte p ≥ 0,03 wählen; X ≤ 10 statt X ≥ 11 rechnen

### 2017MerhoehtBStochastikWTR-1f (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 5 · format Rechnung · antwort Zahl|Text
- gegeben: Der Großhändler behauptet, die Keimwahrscheinlichkeit eines Samenkorns der Stufe B habe sich durch eine Weiterentwicklung auf mehr als 70 % erhöht; die Nullhypothese „Die Wahrscheinlichkeit für das Keimen eines Samenkorns der Qualitätsstufe B ist höchstens 70 %.“ soll auf einem Signifikanzniveau von 5 % getestet werden; dazu werden 100 Samenkörner gesät
- gesucht: Entscheidungsregel des Tests
- verfahren: Z Anzahl der keimenden, binomialverteilt mit n = 100, p = 0,7; kleinstes k mit P(Z > k) <= 0,05 suchen
- fehlerquelle: den Ablehnungsbereich links ansetzen oder k = 76 wählen

### 2017MerhoehtBStochastikCAS1-6 (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 6 · format Kurzantwort|Rechnung · antwort Text|Zahl
- gegeben: Anteile der Haushalte in Deutschland 2013 nach Größe: 1-Personen-Haushalte 40,5 %, 2-Personen-Haushalte 34,5 %, 3-Personen-Haushalte 12,5 %, 4-Personen-Haushalte 9,2 %, Haushalte mit mindestens 5 Personen 3,3 %; 2014 wurde vermutet, dass der tatsächliche Anteil der 1-Personen-Haushalte größer als 2013 ist; Test mit einer Stichprobe von 500 Haushalten auf dem Signifikanzniveau 5 %; möglichst vermieden werden soll, irrtümlich davon auszugehen, dass die Vermutung zutrifft
- gesucht: passende Nullhypothese und zugehörige Entscheidungsregel
- verfahren: Die Vermutung wird Gegenhypothese, H0: p <= 0,405; Z ~ B(500; 0,405), kleinstes k mit P(Z >= k) <= 0,05
- fehlerquelle: die Vermutung als Nullhypothese wählen und linksseitig testen

### 2017MerhoehtBStochastikCAS2-3a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Kurzantwort · antwort Text
- gegeben: Teststreifen mit Indikator: bei weniger als 15 mg ist ein Streifen unbrauchbar; Ziel des Herstellers: höchstens 10 % unbrauchbar; Qualitätskontrolle mit einer Stichprobe von 100 Streifen, nur bei mindestens 16 unbrauchbaren wird das Herstellungsverfahren verbessert
- gesucht: Beschreibung der Fehlentscheidungen, die bei dieser Qualitätskontrolle auftreten können
- verfahren: Beide Kombinationen aus wahrem Anteil und Entscheidung benennen, die nicht zusammenpassen
- fehlerquelle: die Fehler auf einzelne Streifen statt auf die Entscheidung über das Verfahren beziehen

### 2017MerhoehtBStochastikCAS2-3b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Teststreifen mit Indikator: bei weniger als 15 mg ist ein Streifen unbrauchbar; Ziel des Herstellers: höchstens 10 % unbrauchbar; Qualitätskontrolle mit einer Stichprobe von 100 Streifen, nur bei mindestens 16 unbrauchbaren wird das Herstellungsverfahren verbessert; künftig wird eine Stichprobe von 200 Teststreifen genommen; die Wahrscheinlichkeit für eine unnötige Verbesserung soll sich dadurch nicht erhöhen
- gesucht: Mindestanzahl unbrauchbarer Teststreifen, ab der man sich nun für die Verbesserung entscheidet
- verfahren: α alt = P(Y >= 16) für Y ~ B(100; 0,1); kleinstes k mit P(Y >= k) <= α alt für Y ~ B(200; 0,1)
- fehlerquelle: die Grenze einfach verdoppeln (32) oder das Signifikanzniveau 5 % statt der alten Irrtumswahrscheinlichkeit nehmen

### 2018MerhoehtBStochastikCAS1-1c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 5 · format Rechnung · antwort Text
- gegeben: Ein Unternehmen stellt Kunststoffteile her; erfahrungsgemäß sind 4 % der hergestellten Teile fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten kann als binomialverteilt angenommen werden; nach einem Wechsel des Granulats vermutet der Produktionsleiter, dass sich der Anteil der fehlerhaften Teile reduziert hat; getestet wird die Nullhypothese „Der Anteil der fehlerhaften Teile beträgt mindestens 4 %.“ auf der Grundlage einer Stichprobe von 500 Teilen auf einem Signifikanzniveau von 5 %
- gesucht: zugehörige Entscheidungsregel
- verfahren: Größtes k mit P(X <= k) <= 0,05 für X ~ B(500; 0,04)
- fehlerquelle: rechtsseitig testen, weil die Nullhypothese „mindestens“ enthält

### 2018MerhoehtBStochastikWTR1-1d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Kunststoffteile, 4 % fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten ist binomialverteilt; H0: Anteil mindestens 4 %; das neue Granulat ist teurer
- gesucht: Überlegung, die zur Wahl der Nullhypothese geführt haben könnte, mit Begründung
- verfahren: Der teure Wechsel soll nur bei nachgewiesener Verbesserung erfolgen; das Risiko, irrtümlich eine Reduktion anzunehmen, ist durch α begrenzt
- fehlerquelle: mit dem Fehler zweiter Art argumentieren

### 2018MerhoehtBStochastikCAS1-1d (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Kunststoffteile, 4 % fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten ist binomialverteilt; H0: Anteil mindestens 4 %, getestet mit einer Stichprobe von 500 Teilen auf dem Signifikanzniveau 5 %; das neue Granulat ist teurer
- gesucht: Überlegung, die zur Wahl der Nullhypothese geführt haben könnte, mit Begründung
- verfahren: Der teure Wechsel soll nur bei nachgewiesener Verbesserung erfolgen; das Risiko, irrtümlich eine Reduktion anzunehmen, ist durch α begrenzt
- fehlerquelle: mit dem Fehler zweiter Art argumentieren

### 2018MerhoehtBStochastikCAS2-4a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 5 · format Rechnung · antwort Text
- gegeben: Eine Kassiererin behauptet, nur durch Tasten und Betrachten erkennen zu können, ob ein Geldschein echt oder gefälscht ist; ein Kollege legt ihr testweise zehn Geldscheine vor, sie entscheidet für jeden, ob er echt oder gefälscht ist; wird die Nullhypothese „Die Wahrscheinlichkeit dafür, dass sich die Kassiererin korrekt entscheidet, beträgt höchstens 50 %.“ auf einem Signifikanzniveau von 5 % abgelehnt, gibt der Kollege seine Zweifel auf
- gesucht: zugehörige Entscheidungsregel
- verfahren: Kleinstes k mit P(Z >= k) <= 0,05 für Z ~ B(10; 0,5)
- fehlerquelle: k = 8 wählen, weil 0,055 gerundet 5 % ergibt

### 2018MerhoehtBStochastikCAS2-4b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Eine Kassiererin behauptet, nur durch Tasten und Betrachten erkennen zu können, ob ein Geldschein echt oder gefälscht ist; ein Kollege legt ihr testweise zehn Geldscheine vor, sie entscheidet für jeden, ob er echt oder gefälscht ist; wird die Nullhypothese „Die Wahrscheinlichkeit dafür, dass sich die Kassiererin korrekt entscheidet, beträgt höchstens 50 %.“ auf einem Signifikanzniveau von 5 % abgelehnt, gibt der Kollege seine Zweifel auf; bei einem weiteren Test mit unveränderter Nullhypothese und unverändertem Signifikanzniveau werden n Scheine vorgelegt; p ist die Wahrscheinlichkeit einer richtigen Entscheidung bei einem Schein; Abbildung 2 zeigt für ein bestimmtes n die Wahrscheinlichkeit, dass das Testergebnis im Ablehnungsbereich liegt, in Abhängigkeit von p
- gesucht: für ein geeignet gewähltes Beispiel mithilfe von Abbildung 2 die Wahrscheinlichkeit für den zugehörigen Fehler zweiter Art
- verfahren: Ein p > 0,5 wählen (dann ist die Nullhypothese falsch), die Ablehnwahrscheinlichkeit an der Kurve ablesen und den Fehler zweiter Art als Gegenwahrscheinlichkeit bilden
- fehlerquelle: p <= 0,5 wählen, wo die Nullhypothese wahr ist, oder den abgelesenen Wert selbst als Fehler zweiter Art angeben

### 2026MerhoehtBStochastikWTR2-2a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 5 · format Rechnung · antwort Text
- gegeben: Nullhypothese: Anteil der Alleinfahrenden mindestens 75 %; Signifikanzniveau 5 %; Stichprobe 400
- gesucht: Entscheidungsregel
- verfahren: kumulierte Binomialwahrscheinlichkeiten an der Grenze vergleichen
- fehlerquelle: 286 in den Ablehnungsbereich nehmen

### 2022MerhoehtBStochastikWTR1-2b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Text
- gegeben: Alternative Nullhypothese „Anteil höchstens 7 %“
- gesucht: Überlegung des Händlers für die gewählte H₀ mit Begründung
- verfahren: Kontrollierten Fehler dem für den Händler schädlichen Irrtum zuordnen
- fehlerquelle: Fehler zweiter Art als kontrolliert ansehen

### 2023MerhoehtBStochastikWTR2-2c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 5 · format Kurzantwort|Begründung · antwort Text
- gegeben: p Buchungswahrscheinlichkeit; Verlängerung lohnt für p ≥ 2 %; H₀: p ≥ 2 % auf 5 %; größerer Stichprobenumfang teurer; Abbildung der Ablehnwahrscheinlichkeit für n₁ < n₂
- gesucht: Bedingung, unter der sich der größere Umfang lohnen könnte, begründet mit Abbildung und Fehler zweiter Art
- verfahren: Fehler zweiter Art als irrtümliche Verlängerung deuten, an einem p < 0,02 die Kurven vergleichen, gegen die Testkosten abwägen
- fehlerquelle: Fehler erster Art (irrtümliches Nichtverlängern) heranziehen

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2026MerhoehtBStochastikWTR2-2b, 2018MerhoehtBStochastikWTR1-1c, 2025MerhoehtBStochastikWTR2-2c, 2024MerhoehtBStochastikWTR1-2b, 2024MerhoehtBStochastikWTR1-2a, 2024MerhoehtBStochastikWTR1-2c, 2025MerhoehtBStochastikWTR2-2d

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
