# Mappe: unabhaengigkeit

Eintrag: hz-0801/mathe-nachhilfe, katalog/unabhaengigkeit.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:14 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Unabhängigkeit
 3
 4  ### Verortung
 5  Die stochastische Unabhängigkeit zweier Ereignisse: die Prüfung über die Produktregel P(A ∩ B) = P(A) · P(B) oder gleichwertig über den Vergleich einer bedingten mit der unbedingten Wahrscheinlichkeit … (gekürzt, 2030 Zeichen)
 6  [GOST] Q2, 2. Kurshalbjahr (BB S. 27), Grund- und Leistungskursfach: L5-Zeile „Teilvorgänge mehrstufiger Zufallsexperimente auf stochastische Unabhängigkeit anhand einfacher Beispiele untersuchen“ mit … (gekürzt, 1156 Zeichen)
 7  [FOS] Pflichtthema 4 „Stochastik“ (S. 28): „bedingte Wahrscheinlichkeiten (Unabhängigkeit von Ereignissen, Vierfeldertafel/Doppelbaum)“ (Zeilen 1185–1187 der Textfassung) – Pflichtstoff, und die zentralen FHR-Prüfungen stellen die Unabhängigkeitsprüfung seit 2023 in jedem Jahrgang (2023-A, 2024-B, 2025-A, 2026-C), stets als Kette „Tafel oder Anzahlen bestimmen, dann Produktregel prüfen“ mit drei bis fünf Punkten.
 8  [LS-AA] Qualifikationsphase Kapitel VIII 4 „Stochastische Unabhängigkeit“ – die Lehrwerkseinheit zum Thema, unmittelbar nach der bedingten Wahrscheinlichkeit. Zuordnung: Einheit 1 = QP VIII 4; Einheit 2 und 3 folgen der Rohdatei (Rückrichtungen und Argument ohne eigenes Kapitel). Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Unabhängigkeit prüfen: die Produktregel P(A ∩ B) = P(A) · P(B) an Anteilen oder absoluten Häufigkeiten prüfen (Tafel oder Anzahlen erst beschaffen – die fhr-Kette), gleichwertig der Vergleich einer bedingten mit der unbedingten Wahrscheinlichkeit oder zweier bedingter Anteile, das Ergebnis im Sachzusammenhang deuten (abhängig heißt: das Merkmal ist in den Gruppen verschieden häufig). (Q2, GK-Kern; OHiMi 2.4 „stochastische Unabhängigkeit“; FOS Pflichtthema 4) ← Eingabe „unabhängig prüfen“, „stochastisch unabhängig“, „produktregel“, „abhängig oder unabhängig“
12    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK · FHR
13  2. Rückwärts – aus der Unabhängigkeit bestimmen: den bedingten Anteil angeben, für den Unabhängigkeit herrscht (gleich dem unbedingten – ohne Rechnung), Parameter aus der Produktregel (Tafel, Baum), P(A) aus Unabhängigkeit, einer Beziehung zwischen P(A) und P(B) und einer Schnittbedingung (quadratische Gleichung), den unabhängigen zweiten Fehler aus der Vereinigung (Additionssatz mit Produkt). (Q2; Prüfungshöhe) ← Eingabe „parameter unabhängigkeit“, „p aus unabhängigkeit“, „unabhängige fehler“
14    Marken: BE Q2 · BB Q2 · GK · Abitur LK
15  3. Unabhängigkeit als Argument: die Ausgleichs-Fehlvorstellung widerlegen – ein hinter der Erwartung zurückgebliebener Anteil wird nicht durch die nächsten Versuche „ausgeglichen“, weil die Einzelwahrscheinlichkeit bei jeder Wiederholung gleich bleibt und die Versuche unabhängig sind (das empirische Gesetz der großen Zahlen ist keine Ausgleichspflicht). (Q2; BE Kap. 4 „inhaltliches Verständnis“) ← Eingabe „ausgleich zufall“, „muss sich ausgleichen“, „gesetz der großen zahlen“
16    Marken: BE Q2 · BB Q2 · GK · Abitur GK
17  Warum drei: Die Prüfregel (Einheit 1, sechzehn Zeilen samt der fhr-Kette) ist der Kern; die Rückrichtungen (acht Zeilen, fünf Typen) und die Argumentform (drei Zeilen, ein Typ – aber das einzige „inha … (gekürzt, 789 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; fhr-Typen wörtlich aus fhr/fhr-typen.csv, abitur-Typen aus abitur/abitur-typen.csv.
21  Einheit 1: Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen (7) · Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen (3) · Stochastische Unabhängigkeit prüfen (2; fhr) · Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten (2) · Vierfeldertafel vervollständigen (2; fhr) — kein Nachweistyp — kein Deutungstyp. Dazu: Fehler finden (Unabhängigkeit mit Unvereinbarkeit verwechselt – ein nichtleerer Schnitt ist kein Abhängigkeitsbeweis; die Richtung der bedingten Anteile vertauscht; einen bedingten Anteil auf die falsche Gesamtheit bezogen und damit die Tafel falsch gefüllt; P(A ∩ B) mit P_A(B) verwechselt; die Produktregel mit den falschen Werten geprüft) · Begründen (warum Produktregel und Anteilsvergleich dieselbe Prüfung sind; warum „abhängig“ nur „verschieden häufig“ heißt und keine Ursache behauptet).
22  Einheit 2: Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen (3) · Gleichung für p aus der Unabhängigkeit zweier Ereignisse im Baumdiagramm aufstellen (1) · Parameter für die Unabhängigkeit zweier Ereignisse aus der Vierfeldertafel ermitteln (1) · Wahrscheinlichkeit eines Fehlers aus der Vereinigung zweier unabhängiger Fehler berechnen (1) — kein Nachweistyp — Deutung: Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen (2). Dazu: Fehler finden (P(A und nicht B) als Differenz oder Produkt der Randwahrscheinlichkeiten angesetzt; beim Additionssatz die Schnittmenge vergessen; die Nulllösung als Wahrscheinlichkeit angegeben; die falsche Zahl als unabhängigkeitsstiftenden Anteil gewählt; die Bedingung P(E ∩ G) mit P_E(G) verwechselt) · Begründen (warum Unabhängigkeit P(A ∩ ¬B) = P(A) · (1 − P(B)) liefert; warum der bedingte Anteil bei Unabhängigkeit gleich dem unbedingten ist).
23  Einheit 3: kein Berechnungstyp — kein Nachweistyp — Deutung: Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen (3). Dazu: Fehler finden (das empirische Gesetz der großen Zahlen als Ausgleichspflicht der nächsten Versuche gelesen; mit der Seltenheit der langen Serie argumentiert statt mit der Konstanz der Einzelwahrscheinlichkeit) · Begründen (warum die Wahrscheinlichkeit des nächsten Versuchs nicht von den bisherigen abhängt; was das Gesetz der großen Zahlen tatsächlich sagt – Stabilisierung der relativen Häufigkeit, keine Kompensation).
24  Zählung: 5 + 5 + 1 = 11 Haupttypen, 16 + 8 + 3 = 27 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal.
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Vierfeldertafel füllen (Ränder, Felder, bedingte Angaben) – die Datengrundlage der Prüfungen in Einheit 1 und der fhr-Kette. Sek-II-Nachbarthema vierfeldertafel.md (dasselbe Bündel). [GOST Q2 L5 „Vierfeldertafel“; FOS Pflichtthema 4]
29  - Bedingte Wahrscheinlichkeit als Quotient bilden – der Anteilsvergleich in Einheit 1 und 2. Sek-II-Nachbarthema bedingte-wahrscheinlichkeit-und-bayes.md (dasselbe Bündel). [GOST-OHiMi 2.4 „bedingte Wahrscheinlichkeit“, „Multiplikationssatz“]
30  - Anteile aus absoluten Häufigkeiten bilden und kürzen – die fhr-Prüfungen und die Häufigkeitszeilen. Sek-I-Themen prozentrechnung.md, bruchrechnung.md. [GOST Eingangsvoraussetzung L4]
31  - Pfadterme mit Parameter im Baumdiagramm (Ast als Faktor, Pfad als Produkt, Randwahrscheinlichkeit als Pfadsumme) – die Baumaufgaben der Einheit 2. Sek-II-Nachbarthema zufallsexperimente-und-pfadregeln.md Einheit 6 und 8. [GOST Eingangsvoraussetzung L5]
32  - Pfadregeln und Gegenereignis mit und ohne Zurücklegen – die Vorstellung „ohne Zurücklegen ändert sich p“ der Einheit 3. Sek-I-Thema wahrscheinlichkeit.md Einheit 3 und 4. [GOST Eingangsvoraussetzung L5]
33  - Lineare und quadratische Gleichungen aufstellen und lösen, Lösungen sieben (Nulllösung verwerfen) – die Rückrichtungen der Einheit 2. Sek-I-Themen lineare-gleichungen.md, quadratische-gleichungen.md. [GOST-OHiMi 2.1]
34  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
35  - „Prüfen oder nutzen?“ – ankreuzen, ob die Unabhängigkeit zu prüfen ist (Produktregel anwenden) oder vorausgesetzt wird und etwas anderes gesucht ist (Gleichung aufstellen); nichts rechnen. Vor Einheit 1 und 2. [Rohdatei: Typen „untersuchen“ gegen „bestimmen“; abi 2025-bebb-lk-A1.10a, iqb 2023MgrundlegendBStochastikWTR1-2e]
36
37  ### Merkkasten
38  Einheit 1 (Unabhängigkeit prüfen):
39      Produktregel: A und B sind stochastisch unabhängig genau dann, wenn P(A ∩ B) = P(A) · P(B) – alle drei Zahlen beschaffen (Tafel, Anzahlen), Produkt bilden, vergleichen; schon eine kleine Abweichung heißt abhängig.
40        Von achtzig Gästen sind dreißig erwachsen, sechzig mit Saunatarif, fünfundzwanzig beides: geprüft wird, ob das Produkt der beiden Anteile den Schnittanteil trifft.
41      Gleichwertig: A und B sind unabhängig genau dann, wenn P_B(A) = P(A) – das Wissen um B ändert die Wahrscheinlichkeit von A nicht; ebenso, wenn das Merkmal in Gruppe und Gegengruppe gleich häufig ist.
42      Nicht verwechseln: Unvereinbarkeit (A ∩ B ist leer) ist etwas anderes als Unabhängigkeit – unvereinbare Ereignisse mit positiven Wahrscheinlichkeiten sind immer abhängig.
43      Deuten: „abhängig“ heißt nur, dass das Merkmal in den Gruppen verschieden häufig ist – keine Aussage über Ursache und Wirkung.
44      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] „stochastische Unabhängigkeit“ neben Quotient und Multiplikationssatz (Teil-A-Beleg 2018MerhoehtAStochastik12-b); für fhr ist die Kette Tafel → Produktregel die jährliche Prüfform.
45      Formelsammlung: [FS-IQB 1.4] führt die Äquivalenzen ausdrücklich („Die folgenden Aussagen … sind äquivalent: A und B sind stochastisch unabhängig, P_B(A) = P(A), P_A(B) = P(B)“) – in Teil B nachschlagbar, für Teil A auswendig – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
46  Quelle: eigene Formulierung nach [GOST Q2 L5] „stochastische Abhängigkeit und Unabhängigkeit von Ereignissen“, [GOST-OHiMi 2.4] und [FS-IQB 1.4]; Zahlenbeispiel aus fhr 2023-A-3e (in Zahlwörtern); [LS-AA QP VIII 4].
47
48  Einheit 2 (Rückwärts):
49      Ohne Rechnung: unabhängig heißt, der bedingte Anteil ist gleich dem unbedingten – der gesuchte Anteil ist einfach der Gesamtanteil, die Begründung ist die Gleichheit der Anteile in beiden Gruppen.
50      Parameter: die Produktregel als Gleichung im Parameter ansetzen (Tafel: P(A) · P(B) = P(A ∩ B); Baum: P_E(G) = P(G) mit Pfadtermen) – Nulllösungen und unzulässige Werte verwerfen.
51      Mit Schnittbedingung: aus Unabhängigkeit folgt auch P(A ∩ ¬B) = P(A) · (1 − P(B)); zusammen mit einer Beziehung zwischen P(A) und P(B) entsteht eine quadratische Gleichung.
52      Vereinigung: für unabhängige Fehler gilt der Additionssatz mit Produkt, P(A ∪ B) = P(A) + P(B) − P(A) · P(B) – daraus lässt sich der zweite Fehler bestimmen (oder über die Gegenereignisse).
53      Auswendig (Teil A): „Ohne Rechnung“ und „Parameter“ – dieselben Anlagenzeilen rückwärts gelesen (Teil-A-Belege 2021MerhoehtAStochastik11-b, 2023MerhoehtAStochastik12-b, 2025MerhoehtAStochastik23); „Mit Schnittbedingung“ und „Vereinigung“ sind Prüfungshöhe.
54      Formelsammlung: [FS-IQB 1.4] Äquivalenzen; der Additionssatz steht in der Anlage, nicht in der Formelsammlung – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
55  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] und [FS-IQB 1.4]; ohne Zahlenbeispiel (die Rückrichtungen sind zahlenfrei formuliert; Ermessen); [LS-AA QP VIII 4].
56
57  Einheit 3 (Unabhängigkeit als Argument):
58      Kein Ausgleich: bleibt ein Anteil hinter der Erwartung zurück, müssen die nächsten Versuche nichts „ausgleichen“ – die Einzelwahrscheinlichkeit ist bei jeder Wiederholung gleich, die Versuche sind unabhängig, der Zufall hat kein Gedächtnis.
59      Was stattdessen gilt: das empirische Gesetz der großen Zahlen sagt, dass sich die relative Häufigkeit auf lange Sicht bei der Wahrscheinlichkeit stabilisiert – durch das Gewicht der vielen weiteren Versuche, nicht durch eine Gegenbewegung.
60      Sauber argumentieren: mit der Konstanz der Einzelwahrscheinlichkeit und der Unabhängigkeit – nicht mit der Seltenheit der bisherigen Serie.
61      Auswendig (Teil A): der ganze Kasten – das „inhaltliche Verständnis des Begriffs der stochastischen Unabhängigkeit“ [BE Kap. 4] ist genau diese Argumentation; Teil-A-Beleg 2017MerhoehtAStochastik11-c.
62      Formelsammlung: keine – Argumentationsfiguren stehen nicht in der Formelsammlung – [FS] offen
63  Quelle: eigene Formulierung nach [GOST Q2 L5] „Beziehung zwischen relativer Häufigkeit und Wahrscheinlichkeit“ (Simulationszeile) und BE Kap. 4; ohne Zahlenbeispiel; [LS-AA QP VIII 4].
64
65  ### Typische Fehler
66  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 27 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
67  - Datengrundlage falsch beschafft: einen bedingten Anteil auf die falsche Gesamtheit bezogen (Schnitt als Anteil der Teilgruppe angesetzt), Gruppenzahlen falsch zugeordnet und damit falsche Randsummen erhalten – das Kernfehlmuster der fhr-Kette. [fhr 2023-A-3e, 2024-B-3e, 2025-A-3d, 2026-C-3e]
68  - Prüfregel verfehlt: Unabhängigkeit mit Unvereinbarkeit verwechselt (ein nichtleerer Schnitt als Abhängigkeit gedeutet); P_A(B) mit P(A ∩ B) oder P_B(A) mit P_A(B) verwechselt; die Richtung der bedingten Anteile vertauscht; sich beim Produktvergleich verrechnet; den Schnitt mit drei statt zwei Ergebnissen angesetzt; Paare doppelt oder einfach gezählt. [abi 2024-bebb-gk-B4.1d, 2019-be-gk-B4.1d, 2022-bebb-gk-B4i; iqb 2018MerhoehtBStochastikWTR2-1c, 2024MgrundlegendBStochastikWTR1-1d, 2019MgrundlegendBStochastikWTR1-1d, 2022MgrundlegendBStochastikWTR1-1f, 2020MgrundlegendBStochastikWTR2-2b, 2018MerhoehtAStochastik12-b, 2023MerhoehtBStochastikWTR1-2]
69  - Deutung stehen geblieben: die Ungleichung nur wiederholt, ohne die Terme als bedingten und unbedingten Anteil zu deuten. [abi 2022-bebb-lk-B4c; iqb 2022MerhoehtBStochastikWTR1-1c]
70  - Rückwärts verfehlt: P(A und nicht B) als Differenz oder als Produkt der Randwahrscheinlichkeiten angesetzt; beim Additionssatz die Schnittmenge vergessen; die Nulllösung als Wahrscheinlichkeit angegeben; den falschen Anteil als unabhängigkeitsstiftend gewählt; P(E ∩ G) mit P_E(G) verwechselt; die Division durch die Gegenwahrscheinlichkeit ausgelassen. [abi 2025-bebb-lk-A1.10a, 2024-bebb-lk-A1.9b, 2023-bebb-lk-B4e; iqb 2025MerhoehtAStochastik23, 2021MerhoehtAStochastik11-b, 2023MerhoehtAStochastik12-b, 2023MerhoehtBStochastikWTR2-1c, 2023MgrundlegendBStochastikWTR1-2e]
71  - Ausgleichs-Fehlvorstellung: das empirische Gesetz der großen Zahlen als Ausgleichspflicht gelesen; mit der Seltenheit der Serie argumentiert statt mit der Konstanz der Einzelwahrscheinlichkeit. [abi 2021-be-gk-B4c; iqb 2017MerhoehtAStochastik11-c, 2021MgrundlegendBStochastikWTR2-1b]
72
73  ### Für schwache Schüler
74  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q2 Brandenburg und Berlin: Einheit 1 („stochastische Abhängigkeit und Unabhängigkeit von Ereignissen“) und Einheit 3 (das von Berlin verlangte inhaltliche Verständnis); kein LK-Zusatz. Ohne Hilfsmittel (Anlage OHiMi 2.4, Prüfungsteil A): die Produktregel und die Äquivalenz zum Anteilsvergleich – Kasten eins vollständig. RLP FOS (fhr): Einheit 1 ist Pflicht- und Prüfstoff (die Kette Tafel → Produktregel, jährlich seit 2023, durchweg die anspruchsvollste Stochastik-Teilaufgabe des FHR-Hefts – alle vier Zeilen tragen die höchste Niveauschätzung); Einheit 2 und 3 sind für fhr Vorrat. Vorrat für GK (Ermessen nach dem Niveau der Rohdatei): die Rückrichtungen der Einheit 2, besonders die quadratische Schnittbedingung. Niveaustufe H der E-Phase [RLP]: die Sek-I-Pläne kennen die Unabhängigkeit nicht als Begriff – Blatt-0-Stoff sind die Pfadregeln. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung die stochastische Unabhängigkeit – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
75  Grundvorstellung (Blatt 0) [GOST Q2 L5, BE Kap. 4, MO]: Unabhängig heißt: das Wissen um das eine Ereignis ändert die Chance des anderen nicht – der Zufall hat kein Gedächtnis. „Wirf eine Münze, bis dreimal hintereinander Wappen gefallen ist (oder stell es dir vor), kein Term. Wie wahrscheinlich ist beim nächsten Wurf Zahl – hat die Münze die Serie ‚gespeichert‘? Warum fühlt es sich trotzdem so an, als sei Zahl jetzt ‚dran‘? Und nun die Karten aus der Vierfeldertafel-Übung: wenn unter den roten Karten genauso viele markiert sind wie unter den schwarzen – hilft dir dann die Farbe beim Raten, ob eine gezogene Karte markiert ist? Wann würde sie helfen?“ Wer der Münze ein Gedächtnis gibt oder Hilfe von einem Merkmal erwartet, das in beiden Gruppen gleich häufig ist, braucht das vor jeder Formel: Unabhängigkeit heißt gleiche Anteile in den Gruppen, und vergangene Würfe ändern keine Wahrscheinlichkeiten. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q2-Kern; BE Kap. 4 verlangt sie wörtlich), die Aufgabenform ist Ermessen. [GOST Q2 L5; BE Kap. 4 „inhaltliches Verständnis des Begriffs der stochastischen Unabhängigkeit“; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Ausgleichspflicht“, iqb 2017MerhoehtAStochastik11-c; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
76  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
77  - Unabhängigkeit prüfen (Einheit 1): „Welche drei Zahlen braucht die Produktregel?“ – zu Aufgaben ankreuzen, wo P(A), P(B) und P(A ∩ B) stehen (Tafel, Text, Anzahlen) und ob sie erst zu beschaffen sind; „Unabhängig oder unvereinbar?“ – zu Formulierungen ankreuzen, ob Unabhängigkeit (Produktregel) oder Unvereinbarkeit (leerer Schnitt) gemeint ist; nichts rechnen (Vorstufe, Grundvorstellung) → die Produktregel an einer fertigen Tafel prüfen (Grundfall, viermal; abi 2024-bebb-gk-B4.1d, iqb 2024MgrundlegendBStochastikWTR1-1d, 2018MerhoehtBStochastikWTR2-1c) → die fhr-Kette: Anzahlen oder Tafel erst beschaffen, dann prüfen (fhr 2023-A-3e, 2024-B-3e, 2025-A-3d, 2026-C-3e – die Tafelzeilen der FHR-Hefte gehören zur Kette) → über den Vergleich bedingter und unbedingter Anteile prüfen und deuten (abi 2019-be-gk-B4.1d, iqb 2019MgrundlegendBStochastikWTR1-1d) → zwei bedingte Anteile vergleichen (abi 2022-bebb-gk-B4i, iqb 2022MgrundlegendBStochastikWTR1-1f, 2020MgrundlegendBStochastikWTR2-2b) → an zweistufigen Experimenten mit Abzählen prüfen (iqb 2018MerhoehtAStochastik12-b, 2023MerhoehtBStochastikWTR1-2, Teil A und B) → Prüfungshöhe: die vorgelegte Ungleichung als Abhängigkeitsbegründung deuten (abi 2022-bebb-lk-B4c, iqb 2022MerhoehtBStochastikWTR1-1c, Niveau III).
78  - Rückwärts (Einheit 2): „Prüfen oder nutzen?“ ankreuzen (Vorstufe) → den Anteil für Unabhängigkeit ohne Rechnung angeben und begründen (Grundfall, viermal; abi 2023-bebb-lk-B4e, iqb 2023MerhoehtBStochastikWTR2-1c) → den Parameter aus der Produktregel an der Tafel (iqb 2021MerhoehtAStochastik11-b, Teil A) → die Gleichung für p im Baum aufstellen (iqb 2023MerhoehtAStochastik12-b, Teil A) → P(B) aus Unabhängigkeit und Schnittanteil über die Division (iqb 2023MgrundlegendBStochastikWTR1-2e) → den unabhängigen zweiten Fehler aus der Vereinigung (abi 2024-bebb-lk-A1.9b, Teil A) → Prüfungshöhe: P(A) aus Beziehung und Schnittbedingung über die quadratische Gleichung (abi 2025-bebb-lk-A1.10a, iqb 2025MerhoehtAStochastik23, Teil A, Niveau III).
79  - Als Argument (Einheit 3): die Grundvorstellung als Vorstufe → die Ausgleichs-Aussage an einem Glücksrad widerlegen (Grundfall, viermal; iqb 2017MerhoehtAStochastik11-c, Teil A) → Prüfungshöhe: die Aussage im Binomialkontext widerlegen, ohne die Seltenheit der Serie zu bemühen (abi 2021-be-gk-B4c, iqb 2021MgrundlegendBStochastikWTR2-1b, Niveau II).
80
81  ### Prüfungsform (fhr / abi / iqb)
82  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; maßgeblich sind RLP FOS 2019 (Pflichtthema 4) und der fhr-Katalog. Die Rohdatei zählt 27 Zeilen mit 11 Haupttypen (fhr 4 Zeilen, 2 Typen; abi 8 Zeilen, 7 Typen; iqb 15 Zeilen, 8 Typen; 6 abitur-Typen in beiden Abiturprofilen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
83  fhr (4 Zeilen, 2 Typen; FHR-Prüfungen 2023–2026) [fhr-Katalog]: Stochastische Unabhängigkeit prüfen (2, E1) · Vierfeldertafel vervollständigen (2, E1). Muster: Seit 2023 stellt jedes FHR-Heft die Unabhängigkeitsprüfung als Schlussteil der Stochastik-Aufgabe (drei bis fünf Punkte): erst werden Anzahlen oder eine Vierfeldertafel aus dem Sachtext bestimmt (Sauna 2023, Schulweg und ÖPNV 2024, Cannabis-Befragung 2025, T-Shirt-Verkauf 2026), dann die Produktregel geprüft – alle vier Zeilen tragen die höchste Niveauschätzung des Themas; die Tafel- und Anzahlbestimmung ist Teil der Kette, nicht eigener Posten (deshalb liegen die fhr-Tafelzeilen hier und nicht bei vierfeldertafel.md).
84  abi (8 Zeilen, 7 Typen; Landeshefte be-gk, bebb-gk, bebb-lk 2019–2025) [abi-Katalog]: Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen (2, E1) · je 1: Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen (E2) · Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen (E3) · Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten (E1) · Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen (E1) · Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen (E2) · Wahrscheinlichkeit eines Fehlers aus der Vereinigung zweier unabhängiger Fehler berechnen (E2). Muster: Sechs der acht Zeilen liegen in Teil B als Schlussglied der Vierfeldertafel- oder Baumaufgabe (zwei bis fünf Punkte), zwei in Teil A (die Rückrichtungen 2024-bebb-lk-A1.9b und 2025-bebb-lk-A1.10a, drei und fünf Punkte). 7 der 8 Zeilen sind wortgleiche Pooldubletten (2019-be-gk-B4.1d, 2021-be-gk-B4c, 2022-bebb-gk-B4i, 2022-bebb-lk-B4c, 2023-bebb-lk-B4e, 2024-bebb-gk-B4.1d, 2025-bebb-lk-A1.10a), Landeszusatz die Fehler-Vereinigung 2024-bebb-lk-A1.9b. Niveau I 1, II 6, III 1.
85  iqb (15 Zeilen, 8 Typen; Pool 2017–2025, grundlegend 6 und erhöht 9 Zeilen, Teil A 5 und Teil B 10 Zeilen) [iqb-Katalog]: Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen (5, E1) · Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen (2, E3) · Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen (2, E1) · Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen (2, E2) · je 1: Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen (E2) · Gleichung für p aus der Unabhängigkeit zweier Ereignisse im Baumdiagramm aufstellen (E2) · Parameter für die Unabhängigkeit zweier Ereignisse aus der Vierfeldertafel ermitteln (E2) · Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten (E1). Muster: In Teil B schließt die Unabhängigkeitsprüfung die Vierfeldertafel-Kontexte ab (Bildschirme 2018, Fahrprüfung 2019, Briefe 2020, Werbeabteilung/Smartphone-Spiel 2021, Pakete/Fitnessarmband 2022, Geräte/Lastenräder 2023–2024); Teil A stellt die Abzähl- und Rückwärtsformen (2017MerhoehtAStochastik11-c, 2018MerhoehtAStochastik12-b, 2021MerhoehtAStochastik11-b, 2023MerhoehtAStochastik12-b, 2025MerhoehtAStochastik23). Amtlicher Anforderungsbereich in allen 15 Zeilen (höchster Bereich: I 3, II 10, III 2); Niveau I 3, II 10, III 2. Kontexte: Glücksrad, Bildschirme, Fahrprüfungen, Briefe, Smartphone-Spiel, Pakete, Geräte, Lastenräder. 7 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste), keine abgewandelt.
86  Zielmarke: Einheit 1 – fhr: die volle Kette aus Anzahlbestimmung und Produktregel (2026-C-3e, vier Punkte; 2024-B-3e, fünf Punkte); abi: der Anteilsvergleich mit Deutung (2019-be-gk-B4.1d, Niveau II) und die Termdeutung (2022-bebb-lk-B4c, Niveau III); iqb: die Abzählprüfung am zweistufigen Experiment (2023MerhoehtBStochastikWTR1-2, Niveau II). Einheit 2 – abi: die quadratische Rückrichtung in Teil A (2025-bebb-lk-A1.10a, Niveau III) und die Fehler-Vereinigung (2024-bebb-lk-A1.9b, Niveau II); iqb: die Baumgleichung für p (2023MerhoehtAStochastik12-b, Teil A, Niveau II). Einheit 3 – abi: die Ausgleichs-Aussage im Binomialkontext (2021-be-gk-B4c, Niveau II); iqb: das Glücksrad in Teil A (2017MerhoehtAStochastik11-c, Niveau II).
````

## 2 Originale (27)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2024-bebb-lk-A1.9b (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: ein Gerät ist defekt, wenn Fehler A oder Fehler B auftritt; P(defekt) = 0,2; A und B stochastisch unabhängig; P(A) = 0,1, P(B) = p_B
- gesucht: p_B
- verfahren: P(A ∪ B) = P(A) + P(B) − P(A) · P(B) gleich 0,2 setzen und nach p_B auflösen
- fehlerquelle: P(A) + P(B) = 0,2 ansetzen (Schnittmenge vergessen, p_B = 0,1)

### 2025-bebb-lk-A1.10a (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: zwei stochastisch unabhängige Ereignisse A und B mit P(B) = P(A) + 0,6 und P(A und nicht B) = 0,04
- gesucht: P(A)
- verfahren: mit x = P(A): P(nicht B) = 1 − (x + 0,6) = 0,4 − x; Unabhängigkeit liefert x · (0,4 − x) = 0,04; quadratische Gleichung lösen
- fehlerquelle: P(A und nicht B) = P(A) − P(B) oder P(A) · P(B) ansetzen

### 2019-be-gk-B4.1d (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Fahrprüfungen einer Region: 13 879 Prüflinge, davon 2 482 mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; Ereignisse A: mindestens 30 Jahre alt, B: Prüfung bestanden
- gesucht: ob P_A(B) und P(B) übereinstimmen; ob A und B stochastisch unabhängig sind; Deutung im Sachzusammenhang
- verfahren: Beide Wahrscheinlichkeiten als Quotienten berechnen und vergleichen
- fehlerquelle: P_A(B) mit P(A ∩ B) verwechseln

### 2021-be-gk-B4c (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 2 · format Begründung · antwort Text
- gegeben: Smartphone-Spiel: jeden Sonntag zehn Versuche, je Versuch mit 40 % ein Stern; X = Anzahl der Sterne bei zehn Versuchen, binomialverteilt (n = 10, p = 0,4); Aussage eines Spielers: nach dreimal acht Sternen sei die Chance auf acht Sterne an diesem Sonntag deutlich kleiner
- gesucht: Beurteilung der Aussage
- verfahren: Unabhängigkeit der Sonntage
- fehlerquelle: mit der Seltenheit von viermal acht Sternen argumentieren

### 2022-bebb-gk-B4i (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 3 · format Rechnung · antwort Text
- gegeben: Vierfeldertafel aus h
- gesucht: ob der Anteil der Pakete mit Ziel A unter den schweren ebenso groß ist wie unter den nicht schweren
- verfahren: Beide bedingten Anteile berechnen und vergleichen
- fehlerquelle: P_Z(S) mit P_S(Z) verwechseln

### 2022-bebb-lk-B4c (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Begründung · antwort Text
- gegeben: 0,23 ≠ 0,59 · 0,23 + 0,19
- gesucht: Begründung, dass D und F stochastisch abhängig sind
- verfahren: Beide Terme als bedingten und unbedingten Anteil der Armbandnutzer deuten
- fehlerquelle: Ungleichung nur wiederholen, ohne die Terme zu deuten

### 2023-bebb-lk-B4e (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 3 · format Kurzantwort|Begründung · antwort Zahl
- gegeben: Baumdiagramm wie in a mit unbekanntem a
- gesucht: a für stochastische Unabhängigkeit von W und Z, Begründung ohne Rechnung
- verfahren: Bedingte Anteile gleichsetzen
- fehlerquelle: a = 0,45 (Anteil der Weiblichen) angeben

### 2024-bebb-gk-B4.1d (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 3 · format Rechnung · antwort Text
- gegeben: Vierfeldertafel aus b
- gesucht: ob T und M stochastisch unabhängig sind
- verfahren: Produkt der Randwahrscheinlichkeiten mit dem Schnitt vergleichen
- fehlerquelle: Unabhängigkeit mit Unvereinbarkeit verwechseln

### 2017MerhoehtAStochastik11-c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: P(gelb) = 50 % je Drehung; nach 100 Drehungen mit deutlich weniger als 50 % gelb folgert Felix, dass bei den nächsten 100 Drehungen der Anteil deutlich größer als 50 % sein muss
- gesucht: Beurteilung der Aussage
- verfahren: Die Wahrscheinlichkeit für gelb ist bei jeder Drehung gleich groß und hängt nicht von früheren Drehungen ab
- fehlerquelle: das empirische Gesetz der großen Zahlen als Ausgleichspflicht der nächsten Versuche lesen

### 2018MerhoehtAStochastik12-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: A: (1; 3), (2; 2) oder (3; 1) wird erzielt; B: beim ersten Drehen eine 2
- gesucht: ob A und B stochastisch unabhängig sind
- verfahren: P(A), P(B), P(A ∩ B) berechnen und Produktregel prüfen
- fehlerquelle: A ∩ B mit drei Ergebnissen ansetzen

### 2021MerhoehtAStochastik11-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Tafel aus a; für einen Wert von p sind A und B stochastisch unabhängig
- gesucht: dieser Wert von p
- verfahren: Produktformel ansetzen
- fehlerquelle: p = 0 als Lösung angeben

### 2023MerhoehtAStochastik12-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Rechnung · antwort Term
- gegeben: Baumdiagramm aus a; E: erste Drehung ergibt 2; G: Gewinn; E und G sind stochastisch unabhängig
- gesucht: eine Gleichung in p, aus der p berechnet werden kann
- verfahren: P_E(G) aus dem Teilbaum nach der ersten 2 (nur die Folge 2, 2 gewinnt: p²), P(G) aus den Pfaden (2, 2, 2) und (3, 3); gleichsetzen
- fehlerquelle: P(E ∩ G) = p³ mit P_E(G) verwechseln

### 2025MerhoehtAStochastik23 (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: zwei stochastisch unabhängige Ereignisse A und B mit P(B) = P(A) + 0,6 und P(A und nicht B) = 0,04
- gesucht: P(A)
- verfahren: mit x = P(A): P(nicht B) = 1 − (x + 0,6) = 0,4 − x; Unabhängigkeit liefert x · (0,4 − x) = 0,04; quadratische Gleichung lösen
- fehlerquelle: P(A und nicht B) = P(A) − P(B) oder P(A) · P(B) ansetzen

### 2026-C-3e (fhr-katalog.csv)

jahr 2026 · papier C · punkte 4 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Preistabelle: reduzierter Verkaufspreis 15,99 € (PG 1) mit Anzahl 24, 23,99 € (PG 2) mit Anzahl 10, 31,99 € (PG 3) mit Anzahl 6; insgesamt 40 T-Shirts; von den 24 T-Shirts der PG 1 kauften 16 Frauen; 6 Männer kauften teurere T-Shirts, also nicht aus PG 1; Ereignis F ein T-Shirt wird von einer Frau gekauft, Ereignis G ein T-Shirt der PG 1 wird gekauft
- gesucht: Anzahl der an Frauen und an Männer verkauften T-Shirts|Prüfung, ob F und G stochastisch unabhängig sind
- verfahren: Vierfeldertafel mit den Randsummen 24, 16 und 40 füllen; dann P(G) · P(F) mit P(G und F) vergleichen
- fehlerquelle: die 6 Männer der PG 1 zuordnen und dadurch falsche Randsummen erhalten

### 2024-B-3e (fhr-katalog.csv)

jahr 2024 · papier B · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: FOS-Klasse mit 24 Personen, ein Viertel davon mit kurzem Schulweg von unter 20 min, alle anderen mit langem Schulweg; von den Personen mit langem Schulweg nutzen 12 den ÖPNV; ein Drittel der gesamten Klasse nutzt keinen ÖPNV; eine Person der Klasse wird zufällig ausgewählt; Ereignisse kurzer Schulweg und ÖPNV-Nutzung
- gesucht: Anzahl der Personen mit kurzem Schulweg, die den ÖPNV nutzen|Prüfung, ob zwischen den Ereignissen kurzer Schulweg und ÖPNV-Nutzung eine stochastische Abhängigkeit besteht
- verfahren: aus einem Drittel von 24 die 8 Personen ohne und damit 16 mit ÖPNV bestimmen, davon die 12 mit langem Schulweg abziehen; dann P(ÖPNV und kurzer Schulweg) mit dem Produkt P(ÖPNV) · P(kurzer Schulweg) vergleichen
- fehlerquelle: die 12 ÖPNV-Nutzer auf die ganze Klasse beziehen statt nur auf die Personen mit langem Schulweg

### 2023MerhoehtBStochastikWTR1-2 (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 5 · format Rechnung|Begründung · antwort Text
- gegeben: zweimal drehen; C: Summe kleiner als 4; D: Produkt ist 2 oder 3
- gesucht: ob C und D stochastisch unabhängig sind
- verfahren: Günstige Paare zählen, P(D | C) mit P(D) oder P(C ∩ D) mit P(C) · P(D) vergleichen
- fehlerquelle: Paare (1;2) und (2;1) nur einmal zählen

### 2024MgrundlegendBStochastikWTR1-1d (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Rechnung · antwort Text
- gegeben: Vierfeldertafel aus b
- gesucht: ob T und M stochastisch unabhängig sind
- verfahren: P_T(M) mit P(M) vergleichen
- fehlerquelle: P(T ∩ M) ≠ 0 als Abhängigkeit deuten

### 2018MerhoehtBStochastikWTR2-1c (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 3 · format Rechnung · antwort Text
- gegeben: Vierfeldertafel aus b (D 10,7 %, N 3,0 %, D∩N 1,0 %)
- gesucht: ob die beiden Defekte unabhängig voneinander auftreten
- verfahren: Produkt der Randwahrscheinlichkeiten mit dem Schnitt vergleichen
- fehlerquelle: Unabhängigkeit mit Unvereinbarkeit verwechseln

### 2023-A-3e (fhr-katalog.csv)

jahr 2023 · papier A · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: 80 Happy-Hour-Gäste, davon 30 Erwachsene und 60 mit Saunatarif, darunter nach Teilaufgabe a 25 Erwachsene mit Saunatarif; für eine beliebige Person bedeutet Ereignis C sie hat den Erwachsenentarif bezahlt und Ereignis D sie hat den Saunabesuch gewählt
- gesucht: Prüfung, ob die Ereignisse C und D stochastisch unabhängig sind
- verfahren: P(C), P(D) und P(C und D) als Anteile an 80 bestimmen und das Produkt der Einzelwahrscheinlichkeiten mit der Wahrscheinlichkeit des Schnittereignisses vergleichen
- fehlerquelle: P(C und D) auf die 60 Saunagäste beziehen und 25/60 ansetzen

### 2025-A-3d (fhr-katalog.csv)

jahr 2025 · papier A · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: von den 50 Befragten haben 20 Cannabis konsumiert; die 50 werden nach der Altersstruktur in die Gruppen Jung (unter 28 Jahre) und Alt (ab 28 Jahre) unterteilt; die Gruppe Jung hat 38 Personen, darunter 16 Cannabiskonsumenten
- gesucht: Nachweis, dass die Ereignisse Alter und Cannabiskonsum stochastisch abhängig sind
- verfahren: P(C), P(Jung) und P(C und Jung) als Anteile an 50 bestimmen und das Produkt der Einzelwahrscheinlichkeiten mit der Wahrscheinlichkeit des Schnittereignisses vergleichen
- fehlerquelle: die 16 Konsumenten auf die 38 Personen der Gruppe Jung beziehen und P(C und Jung) = 16/38 setzen

### 2019MgrundlegendBStochastikWTR1-1d (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 5 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Fahrprüfungen einer Region: 13 879 Prüflinge, 2 482 davon mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; A: Prüfling mindestens 30, B: Prüfung bestanden
- gesucht: ob P_A(B) und P(B) übereinstimmen; ob A und B unabhängig sind, mit Deutung
- verfahren: Beide Wahrscheinlichkeiten berechnen und vergleichen
- fehlerquelle: P_B(A) statt P_A(B) berechnen

### 2022MgrundlegendBStochastikWTR1-1f (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Rechnung · antwort Text
- gegeben: Vierfeldertafel aus h
- gesucht: ob der Anteil der Pakete mit Ziel A unter den schweren ebenso groß ist wie unter den nicht schweren
- verfahren: Beide bedingten Anteile berechnen und vergleichen
- fehlerquelle: P_Z(S) mit P_S(Z) verwechseln

### 2020MgrundlegendBStochastikWTR2-2b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Rechnung · antwort Text
- gegeben: Große Firma versendet einen Teil ihrer Briefe mit Q (95 % am ersten Werktag zugestellt), den anderen Teil mit einem anderen Unternehmen; Baumdiagramm (Abb. 1): Q mit 0,6, dann E (zugestellt) 0,95 und Ē 0,05; nicht Q mit 0,4, dann E und Ē mit a; ein Brief wird zufällig ausgewählt; a = 0,25; Ereignisse „Brief wird von Q befördert“ und „Brief wird am ersten Werktag zugestellt“
- gesucht: Prüfung auf stochastische Unabhängigkeit
- verfahren: Zustellwahrscheinlichkeiten bei Q und beim anderen Unternehmen vergleichen
- fehlerquelle: Produktregel mit P(Q ∩ E) = 0,6 · 0,95 gegen P(Q) · P(E) rechnen und sich verrechnen

### 2022MerhoehtBStochastikWTR1-1c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: 0,23 ≠ 0,59 · 0,23 + 0,19
- gesucht: Begründung, dass D und F stochastisch abhängig sind
- verfahren: Beide Terme als bedingten und unbedingten Anteil der Armbandnutzer deuten
- fehlerquelle: Ungleichung nur wiederholen, ohne die Terme zu deuten

### 2023MerhoehtBStochastikWTR2-1c (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Kurzantwort|Begründung · antwort Zahl
- gegeben: Baumdiagramm wie in a mit unbekanntem a
- gesucht: a für stochastische Unabhängigkeit von W und Z, Begründung ohne Rechnung
- verfahren: Bedingte Anteile gleichsetzen
- fehlerquelle: a = 0,45 (Anteil der Weiblichen) angeben

### 2023MgrundlegendBStochastikWTR1-2e (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: M₁, M₂ unabhängig; P(M₁) = 1 %; P(¬M₁ ∩ M₂) = 3 % aus d
- gesucht: P(M₂)
- verfahren: Unabhängigkeit ausnutzen: P(M₂) = P(¬M₁ ∩ M₂) / P(¬M₁)
- fehlerquelle: P(M₂) = 3 % ohne Division durch 0,99

### 2021MgrundlegendBStochastikWTR2-1b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Smartphone-Spiel: jeden Sonntag zehn Versuche, je Versuch mit 40 % ein Stern; X = Anzahl der Sterne bei zehn Versuchen, binomialverteilt (n = 10, p = 0,4); Aussage eines Spielers: nach acht Sternen an drei Sonntagen sei die Chance auf acht Sterne an diesem Sonntag deutlich kleiner
- gesucht: Beurteilung der Aussage
- verfahren: Konstanz der Trefferwahrscheinlichkeit und Unabhängigkeit der Sonntage nennen
- fehlerquelle: mit der Seltenheit von viermal acht Sternen argumentieren

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
