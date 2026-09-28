# Zweitlesung daten

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 538
(e1 88, e2 59, e3 54, e4 79, e5 87, e6 41, e7 75, zone 55) · Stand: Commit 6ef64d5

Prüfung: Jede Zeile gelesen; jedes Zahlenergebnis aus dem Aufgabentext
eigens nachgerechnet (Python/sympy, unabhängig vom Feld pruef), dazu
eindeutige Lösbarkeit, Passung zu sprosse_text und merkmal, genau eine
richtige Option beim Ankreuzen, echter Fehler bei Fehler finden.
werkzeuge/bank-pruef.py meldet 0 Abweichungen, 0 Warnungen; die Befunde
unten liegen außerhalb dessen, was das Skript prüft (es vergleicht pruef
mit loesung, nicht mit der Aufgabe).

Befunde: 63 Zeilen, davon 3 rechnerisch [R].

## Befunde

e1-k1-s0-v2: Das Ganze (24) steht nicht im Text, es muss addiert werden; das widerspricht dem merkmal „nur finden, nicht rechnen“ – Gesamtzahl im Text nennen (z. B. „von 24 Spielen“) oder die Zeile in Kette 2 verschieben.
e1-k1-s0-v3: Das Ganze (20) muss erst addiert werden, entgegen dem merkmal „nicht rechnen“ – eine Summenzeile in die Tabelle aufnehmen oder die Zeile nach k2-s0 verschieben.
e1-k1-s11-v2: Beim Volleyball gibt es kein Unentschieden, der Kontext ist also unrealistisch; außerdem trägt die abgewandelte Aufgabe die Quellenangabe „(P10 2015 OS)“ – eine Sportart mit Unentschieden wählen (z. B. Fußball) und die Quellenangabe weglassen oder als „nach“ kennzeichnen.
e1-k2-s0-v1: „Unterstreiche es“ geht nicht, weil das Ganze (880) nicht im Text steht, sondern berechnet werden muss – „Unterstreiche es“ streichen oder „Berechne es“ schreiben.
e1-k2-s4-v2: Das Ergebnis ist nicht endlich (0,5066…), eine Rundungsvorgabe fehlt – „auf drei Stellen gerundet“ ergänzen.
e1-k3-s1-v1: Welche Klasse 161 ist, hängt von der Randregel ab (anderswo im Eintrag, z. B. k2-s2-v3, gilt 0 < x ≤ 20), und die Aufgabe nennt sie nicht – „Klassen jeweils von … bis unter …“ vorgeben oder „Lege eine Randregel fest und begründe“ fordern.
e1-k3-s1-v2: Hier ist dieselbe Mehrdeutigkeit: Die Zuordnung von 30 hängt von der nicht genannten Randregel ab – Randregel „bis unter“ in der Aufgabe vorgeben.
e1-k7-s2-v2: Die Aufgabe (Summe der relativen Häufigkeiten ist eins) passt nicht zur sprosse_text „warum relative Häufigkeiten zwei Klassen vergleichbar machen“ – ersetzen durch eine Vergleichsbegründung oder die Zeile zu k1-s7 verschieben.
e1-k7-s3-v1: Ein Säulendiagramm aus absoluten Anzahlen passt nicht zur sprosse_text „als Dezimalzahl und in Prozent (Taschenrechner, runden)“ – zusätzlich die relativen Häufigkeiten in Prozent (gerundet, 38 ist der Nenner) verlangen oder die sprosse_text an „Darstellungswechsel“ anpassen.
e1-k7-s3-v2: Alle Werte gehen glatt auf (Nenner 40), es braucht weder Taschenrechner noch Runden, anders als die sprosse_text verlangt – Anzahlen so wählen, dass gerundet werden muss (z. B. Gesamtzahl 42).
e1-k7-s3-v3: Die Lösung „3,5 cm des Streifens“ setzt einen 10 cm langen Streifen voraus, den der Aufgabentext nicht nennt – die Streifenlänge in der Aufgabe angeben oder die Lösung als „35 % des Streifens“ formulieren.
e1-k7-s4-v3: „Tore je Spiel“ ist eine Quote und keine relative Häufigkeit, denn Tore sind kein Teil der Spiele (es wären auch mehr Tore als Spiele möglich) – Kontext wählen, bei dem die Anzahl ein Teil des Ganzen ist (z. B. Treffer von Torschüssen).
e2-k2-s9-v2: Rostock $209$ liegt bei yfein=2 zwischen zwei Hilfslinien und ist nicht genau zeichenbar; zudem 10 Hilfslinien je Schritt – Rostock auf $208$ oder $210$ setzen bzw. yfein=5/ystep=20 mit passenden Werten wählen.
e2-k2-s11-v3: Apfel und Birne haben beide $84$, die Zuordnung von B und E ist nicht eindeutig; außerdem fehlt das Zeichnen, das das Merkmal verlangt – einen der beiden Werte ändern (z. B. Birne $60$) und eine Säule zeichnen lassen.
e2-k2-s11-v4: Hamster und Vogel haben beide $60$, Zuordnung von B und D nicht eindeutig; Zeichnen fehlt wie in v3 – einen Wert ändern und eine Säule ergänzen lassen.
e2-k3-s1-v1: Die Grafik gibt die Einteilung (bis $30$, Schritt $6$) schon vor, „Wähle eine Einteilung“ läuft ins Leere, und die Lösung nennt nur eine von mehreren richtigen Skalen – leeres Achsenkreuz ohne Zahlen vorgeben und in der Lösung „z. B.“ mit Kriterium (größter Wert passt, gleichmäßige Schritte).
e2-k3-s1-v2: Wie v1 Skala vorgegeben; zusätzlich sind $340$, $410$, $290$, $470$ auf einer reinen Hunderterteilung ohne Hilfslinien nicht genau abtragbar – Skala offen lassen, Lösung z. B. Zehner- oder Zwanziger-Hilfslinien nennen.
e2-k3-s1-v3: $12{,}5$; $9{,}8$; $11{,}2$ sind bei Zweierschritten ohne Hilfslinien nicht genau zeichenbar, Skala zudem vorgegeben – Werte auf die Teilung abstimmen oder feinere Einteilung als Lösung angeben.
e2-k4-s3-v1: sprosse_text „Diagramm aus einer Tabelle zeichnen (Skala wählen)“ passt nicht zur Aufgabe (Diagramm → Tabelle, kein Zeichnen) und nicht zum Merkmal Darstellungswechsel – sprosse_text der Pflichtsprosse auf „Darstellungswechsel“ korrigieren (gilt für k4-s3-v1 bis v3).
e2-k4-s3-v2: gleiche sprosse_text-Abweichung (Säulen → Balken ist kein Zeichnen aus Tabelle mit Skalenwahl) – wie k4-s3-v1 korrigieren.
e2-k4-s4-v3: Aus dem Monatsend-Kontostand ist nur die Nettoänderung ablesbar, nicht was „ausgegeben“ wurde – fragen „In welchem Monat sank der Kontostand, und um wie viel?“.
e3-k1-s10-v5: [R] Jünger als 40 sind 6 von 13 (27, 34, 29, 38, 31, 36), nicht 5 – Lösung auf 6 : 13 ≈ 46,2 % und Winkel ≈ 166° korrigieren, pruef entsprechend [6, 6/13*100, 6/13*360].
e3-k3-s2-v2: Aufgabe (Winkelsumme 360°) passt nicht zum sprosse_text „warum 1 % genau 3,6° sind“ – sprosse_text allgemeiner fassen (z. B. „Begründen: Vollwinkel, Prozent und Streifen“) oder Aufgabe auf 1 % = 3,6° zuschneiden.
e3-k3-s2-v3: Aufgabe (10-cm-Streifen) passt nicht zum sprosse_text „warum 1 % genau 3,6° sind“ – wie bei v2 sprosse_text allgemeiner fassen.
e3-k3-s3-v1: Aufgabe (Winkel → Prozent) passt nicht zum sprosse_text „Anteil in Prozent → Streifenabschnitt“ – sprosse_text auf den Darstellungswechsel allgemein fassen (Kreis, Streifen, Prozent, Tabelle).
e3-k3-s3-v2: Aufgabe (Streifen → Winkel) passt nicht zum sprosse_text „Anteil in Prozent → Streifenabschnitt“ – wie bei v1 sprosse_text allgemeiner fassen.
e4-k1-s7-v3: „(zwei Stellen)“ ist mehrdeutig (Nachkommastellen oder gültige Ziffern) – „auf zwei Nachkommastellen gerundet“ schreiben.
e4-k1-s8-v2: Merkmal verlangt einen Wert aus dem Text, hier stehen alle Werte im Diagramm; die Angabe „900 Jugendliche befragt“ ist nur Beiwerk – Merkmal anpassen oder einen Balken leer lassen und seinen Wert in den Text setzen.
e4-k1-s8-v3: Merkmal verlangt einen Wert aus dem Text, hier stehen alle Werte im Diagramm; zudem sind die Monatskürzel J/M/A mehrdeutig (Juni/Juli, März/Mai, April/August) – einen Wert in den Text verlegen und Kürzel eindeutig machen (Jan, Feb, …).
e4-k1-s10-v3: „in 8 Jahren zusammen 2 120 Mitglieder“ ist sachlich schief (Mitglieder werden nicht über Jahre aufsummiert) – etwa „Die Mitgliederzahlen der 8 Jahre ergeben zusammen 2 120“ schreiben.
e4-k1-s12-v2: Aussage 2 (ein Viertel mehr) betrifft keine Kenngröße, passt nicht zum Merkmal „Aussage zu einer Kenngröße“ – Aussage 2 durch eine Kenngrößenaussage (z. B. Mittelwert oder Median) ersetzen.
e4-k2-s1-v1: Rundungsvorgabe für σ fehlt, loesung rundet auf zwei Nachkommastellen – „auf zwei Nachkommastellen runden“ in die Aufgabe (gilt ebenso für k2-s1-v2 bis v5).
e4-k2-s1-v2: Rundungsvorgabe für σ fehlt (σ ≈ 3,16) – Rundung in der Aufgabe angeben.
e4-k2-s1-v3: Rundungsvorgabe für σ fehlt (σ ≈ 31,09) – Rundung in der Aufgabe angeben.
e4-k2-s1-v4: Rundungsvorgabe für σ fehlt (σ ≈ 7,90) – Rundung in der Aufgabe angeben.
e4-k2-s1-v5: Rundungsvorgabe für σ fehlt (σ ≈ 1,30) – Rundung in der Aufgabe angeben.
e4-k2-s2-v1: Rundungsvorgabe für σ fehlt (σ ≈ 3,46) – Rundung in der Aufgabe angeben.
e4-k2-s2-v2: Rundungsvorgabe fehlt für x̄ ≈ 2,67 und σ ≈ 0,53 – Rundung in der Aufgabe angeben.
e4-k2-s2-v3: Rundungsvorgabe für σ fehlt (σ ≈ 6,98) – Rundung in der Aufgabe angeben.
e4-k2-s4-v1: Rundungsvorgabe für x̄ ≈ 534,33 und σ ≈ 75,03 fehlt – Rundung in der Aufgabe angeben.
e4-k2-s4-v2: Rundungsvorgabe für σ ≈ 5,57 fehlt, und „Sollmenge 80 cm“ passt nicht zu Längen – Rundung angeben, „Solllänge“ schreiben.
e4-k4-s4-v2: sprosse_text „sinnvoll runden (Zuschauer je Spiel)“ passt nicht zur Aufgabe (fehlende Note, kein Runden, keine Zuschauer) – sprosse_text der Pflichtsprosse an das Merkmal „Anwendung“ angleichen.
e4-k4-s4-v3: sprosse_text „sinnvoll runden (Zuschauer je Spiel)“ passt nicht zur Aufgabe (Bus, kein Runden) – sprosse_text an das Merkmal „Anwendung“ angleichen.
e5-k1-s10-v4: Prozentangabe „gut 10 %“ und „dreimal so warm“ bei °C sind sachlich schief, weil die Celsius-Skala keinen echten Nullpunkt hat – Größe durch eine Verhältnisgröße ersetzen (z. B. Besucher, Preis) oder die Prozentangabe streichen und nur „um 2 Grad“ stehen lassen.
e5-k3-s1-v1: [R] Der Unterschied 3 füllt bei der Achse 50 bis 56 genau die halbe Höhe, nicht „fast“; dazu Tippfehler „von $= 3$“ – „fast“ streichen, „von $3$“ schreiben.
e5-k3-s1-v3: Erste Lösungsoption (Achse ab 0) widerspricht der Frage, weil kleine Unterschiede dann gerade nicht sichtbar sind; pruef 0 prüft nichts Sinnvolles – Lösung auf die gekennzeichnete gedehnte Achse (Bruchmarke, Hinweis) plus Wertebeschriftung stützen, pruef streichen.
e5-k4-s1-v2: Aufgabe fragt „Warum täuscht das Diagramm?“, aber es gibt weder Grafik noch Angaben zum Diagramm; dass die Achse nicht bei 0 beginnt, kann der Schüler nicht wissen – Angabe ergänzen (z. B. „Die y-Achse beginnt bei 90.“) oder Grafik beigeben.
e6-k1-s4-v2: [R] Mittelwert ist exakt $35{,}45$ min, Abweichung $10{,}45$ min; die Lösung schreibt „$= 35{,}5$“ und „$= 10{,}5$“, die Aufgabe nennt keine Rundung – exakte Werte angeben oder Rundungsvorgabe in die Aufgabe (σ ≈ $19{,}18$).
e6-k1-s5-v3: Relative Häufigkeiten ($8/90$ usw.) sind nicht endlich, die Aufgabe nennt keine Rundungsvorgabe – „auf zwei Nachkommastellen runden“ ergänzen.
e6-k1-s8-v2: Sprosse und Merkmal verlangen die Deutung als untere Schranke, die Variante führt auf eine obere Schranke – als bewusste Umkehrung im Merkmal zulassen oder Term mit unteren Grenzen bauen.
e6-k2-s3-v2: sprosse_text „Mittelwert aus Häufigkeitstabelle“ passt nicht zur Aufgabe (Diagramm relativer Häufigkeiten zeichnen, kein Mittelwert) – sprosse_text der Pflichtsprosse auf Darstellungswechsel korrigieren.
e6-k2-s4-v3: sprosse_text „Fehlenden Wert aus vorgegebenem Mittelwert bestimmen“, die Aufgabe hat aber keinen fehlenden Wert (Mittelwert aus Klassen, Bestehensquote) – sprosse_text anpassen oder einen gesuchten Wert einbauen.
e7-k2-s1-v2: Die Zahl 8 steht in der Tafel zweimal (Mädchen mit Handy, Jungen ohne Handy), deshalb hat v2 dieselbe Lösung wie v1 (8/46), und wer die falsche Zelle nimmt, kommt trotzdem auf das richtige Ergebnis – andere Zelle fragen (z. B. Jungen mit Handy, 14/46) oder die Tafelwerte ändern.
e7-k2-s2-v1: 4/23 bricht als Dezimalzahl nicht ab, die Aufgabe nennt aber keine Rundung (Lösung: 0,174 bzw. 17,4 %) – „auf drei Dezimalen bzw. eine Nachkommastelle in Prozent runden“ ergänzen.
e7-k2-s3-v1: Keine Rundungsvorgabe, obwohl das Ergebnis nicht abbricht (33,3 %) – „auf eine Nachkommastelle runden“ ergänzen.
e7-k2-s3-v2: Keine Rundungsvorgabe, obwohl das Ergebnis nicht abbricht (46,2 %) – „auf eine Nachkommastelle runden“ ergänzen.
e7-k2-s3-v3: Keine Rundungsvorgabe, obwohl das Ergebnis nicht abbricht (35,3 %) – „auf eine Nachkommastelle runden“ ergänzen.
e7-k2-s4-v1: Keine Rundungsvorgabe, obwohl das Ergebnis nicht abbricht (36,4 %) – „auf eine Nachkommastelle runden“ ergänzen.
e7-k2-s4-v2: Keine Rundungsvorgabe, obwohl das Ergebnis nicht abbricht (31,4 %) – „auf eine Nachkommastelle runden“ ergänzen.
e7-k2-s6-v3: Merkmal und Sprosse verlangen Anteile innerhalb einer Zeile, die Aufgabe nimmt aber die Spalte „Rad“ – auf eine Zeile umstellen (z. B. Zeile „Mädchen“: 60/138 und 78/138) oder die Variante zur Spaltenkontrolle umwidmen.
e7-k2-s10-v2: Die Begründung in der Lösung ist unlogisch („obwohl dort auch die absolute Zahl größer ist“), denn eine größere absolute Zahl spricht nicht gegen einen größeren Anteil – „obwohl“ durch „und“ ersetzen oder den Nebensatz streichen.
e7-k3-s3-v1: Die Lösung gibt keinen Mustertext, sondern nur einen Platzhalter („so viele Mädchen …“) – als Muster z. B. „Von 46 Kindern sind 24 Mädchen; 22 Kinder haben ein Handy, darunter 8 Mädchen.“ eintragen.
e7-k3-s4-v3: Passt nicht zum Merkmal: Es wird keine Behauptung geprüft, gefragt ist nur ein Anteil an allen und eine Division (die Angaben zu den Mädchen braucht man gar nicht) – eine Alltagsbehauptung einbauen, die man nur mit Zeilen- oder Spaltenanteilen prüfen kann.

Sauber: 475 Zeilen ohne Befund

## Abgleich

Kein Abgleich möglich: bank/daten/gegenlese.md liegt beim Pull vor dem Commit (11:22 UTC, main f1e89c7) nicht im Repo, auch nicht in der Git-Geschichte. Alle Befunde oben sind damit Befunde nur dieses Lesers; der Abgleich folgt, sobald ein Erstleser gegenlese.md anlegt.
