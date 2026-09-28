# Zweitlesung binomialverteilung

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 282
(zone 37, e1 40, e2 48, e3 56, e4 51, e5 50)

Prüfung: Jede Zeile gelesen; jede Lösungszahl aus dem Aufgabentext neu gerechnet mit einem eigenen sympy-Skript (exakte Binomialwahrscheinlichkeiten, Einzel- und kumulierte Werte, Nachbarwerte bei Probier- und Schrankenaufgaben, Logarithmus- und Wurzelansätze, Modalwerte, Symmetrieaufgaben), außerdem alle Tabellenwerte der `\sachtabelle`-Grafiken (e2-k1-s9-v1 bis v4) und die Säulenhöhen der Diagramme in e5 (s1, s4, s5, s6, s8) gegen die zugehörige Binomialverteilung. Alle 225 Zeilen mit pruef-Zahl stimmen nach Rundung mit der eigenen Rechnung überein; ebenso die im Text genannten Kontrollwerte (Ungleichungen in e3-k1-s9-v5/v6 gelten: 0,6198 > 0,6 und 0,7406 > 0,7). Die 20 Ankreuzzeilen haben je genau eine richtige Option, loesung nennt sie wortgleich. In den 16 Fehler-finden-Zeilen ist der eingebaute Fehler wirklich falsch und die Richtigrechnung stimmt. `python3 werkzeuge/bank-pruef.py binomialverteilung`: 0 Abweichungen, 0 Warnungen. Kein Rechenfehler gefunden; die Befunde betreffen Merkmal und Sprosse sowie zwei Darstellungsfragen. Nebenbei: die sprosse_text der Prüfungshöhen (e1-k1-s7, e3-k1-s9, e4-k1-s9, e5-k1-s8) tragen nur den ersten Teil der Katalogsprosse; die Varianten zu den weiteren Originalen passen zum Katalog und zum merkmal, darum kein Zeilenbefund.

## Befunde

e1-k2-s3-v1: [M] sprosse_text „Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen“, gefragt ist aber „mindestens ein laufendes Triebwerk“ über das Gegenereignis 1 − 0,001² – Frage auf „genau ein Triebwerk fällt aus“ umstellen oder Sprosse ändern.

e1-k2-s3-v3: [M] drei Schrauben, „höchstens eine fehlerhaft“ – weder zwei Versuche noch „genau ein Treffer“, das ist Stoff aus e1-k1-s4 bzw. Einheit 2 – auf zwei Versuche und genau einen Treffer zurückführen.

e2-k1-s1-v1, e2-k1-s1-v2, e2-k1-s1-v3, e2-k1-s1-v4, e2-k1-s1-v5: [M] Der Grundfall heißt „den Term für P(X = k) ohne Rechnung hinschreiben“, die Aufgaben verlangen aber „Gib den Term an und berechne ihn“; das Ausrechnen ist das Merkmal der nächsten Sprosse (e2-k1-s2) – „und berechne ihn“ streichen, loesung nur mit dem Term (pruef dann z. B. die Parameter).

e2-k1-s5-v2: [M] Verfremdung zu schwach: Original 2026MgrundlegendAStochastik12-a ist „Münze fünfmal, höchstens einmal Wappen“, die Variante „Münze sechsmal, höchstens einmal Zahl“ – gleicher Kontext, nur n und Seite getauscht – anderen Kontext wählen (Glücksrad, Würfel mit p ≠ 1/2 o. Ä.).

e3-k4-s4-v2, e3-k4-s4-v3: [M] sprosse_text „Kumulierte Binomialsumme als Sachaussage formulieren“, die Aufgaben verlangen aber Diagramm → kumulierte Wahrscheinlichkeit (v2) bzw. Stäbe markieren (v3); keine Sachaussage – sprosse_text an den Darstellungswechsel anpassen oder eine Variante „Summe → Satz im Sachzusammenhang“ aufnehmen.

e4-k1-s1-v2: [E] loesung schreibt `1 - \frac{5}{6}^n`; ohne Klammer hängt das n neben dem Bruch und liest sich mehrdeutig (auch als 5/6ⁿ) – `\left(\frac{5}{6}\right)^n` setzen.

e4-k3-s3-v3: [M] sprosse_text „Anzahl von Versuchen … für mindestens einen Treffer über das Gegenereignis bestimmen“, gesucht ist aber eine Grenze k (Beratungstermine) bei festem n = 50 durch Probieren – gehört zu e4-k1-s4; durch eine Planungsfrage nach n mit „mindestens einmal“ ersetzen.

e5-k1-s4-v1: [E] loesung: „in Abbildung 3 ist allein die Säule bei 3 fast halb so hoch“ – unklar, gemeint ist „fast 50 Prozent hoch“ – so formulieren.

e5-k3-s4-v1, e5-k3-s4-v2, e5-k3-s4-v3: [M] sprosse_text „Verteilung der Gegenzufallsgröße im Diagramm darstellen“, keine der drei Varianten enthält eine Gegenzufallsgröße (Münze zeichnen, Diagramm → Tabelle, Tabelle → p) – sprosse_text auf „Darstellungswechsel Tabelle und Säulendiagramm“ ändern oder mindestens eine Variante mit Y = n − X.

Sauber: 266 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e1-k2-s3-v1: gefragt ist „mindestens ein Triebwerk“ über das Gegenereignis, die Sprosse verlangt „genau ein Treffer bei zwei Versuchen“.
- e1-k2-s3-v3: drei Versuche und „höchstens eine“ passen nicht zur Sprosse „genau ein Treffer bei zwei Versuchen“.
- e2-k1-s1-v1 bis v5: „und berechne ihn“ nimmt das Merkmal der Sprosse 2 vorweg; die Sprosse verlangt den Term ohne Rechnung.
- e4-k3-s3-v3: gesucht ist eine Grenze k bei festem n, nicht die Anzahl der Versuche für „mindestens einen Treffer“.
- e5-k3-s4-v1 bis v3: keine Variante enthält die Gegenzufallsgröße, die sprosse_text nennt.
- e4-k1-s1-v2: `\frac{5}{6}^n` ohne Klammer ist mehrdeutig.
- e5-k1-s4-v1: „fast halb so hoch“ ist unklar, gemeint ist „fast 50 Prozent“.

Nur Erstleser:
- e2-k2-s1-v1 (10 · 0,0161 ≈ 0,1608 inkonsistent): bestätigt – 10 · 0,0161 = 0,161; der Endwert stimmt, der gerundete Zwischenwert passt nicht dazu. Ich hatte die Zeile nur auf den Endwert geprüft.
- e5-k1-s7-v3 (Begründung über „8 liegt näher am Maximum“): bestätigt – bei p knapp über 0,5 (etwa 0,51) liegt der Modalwert bei 5, beide Stellen sind gleich weit weg; die Aussage stimmt, die Begründung trägt aber nicht. Tragfähig ist p⁶ > (1 − p)⁶ bei gleichen Binomialkoeffizienten.
- e2-k1-s6-v3 (mehrdeutig wegen (9 über 5) = (9 über 4)): bestätigt – n = 9, k = 4, p = 0,55 ergibt denselben Term; ohne vorgegebenes p sind zwei Antworten richtig.
- e3-k1-s9-v3, e3-k1-s9-v4 (Rundung nicht vorgegeben, Zwischenrundung verschiebt die vierte Stelle): bestätigt, klein – die Aufgaben nennen keine Rundung; mit gerundetem Zwischenwert 0,8225 bzw. 0,8093.
- e3-k4-s2-v3 (k nicht als ganze Zahl erklärt): bestätigt, klein – die Aussage gilt nur für ganzzahliges k; im Sachzusammenhang naheliegend, aber nicht gesagt.
- e4-k1-s9-v7, v8, v9 (p = 0 bzw. p = 1 erfüllen die Gleichung auch): bestätigt – v7 und v8 werden von p = 0 und p = 1 erfüllt, v9 von p = 1; „0 < p < 1“ fehlt im Text, das Original 2025MerhoehtAStochastik21 nennt p < 1.
- e4-k1-s2-v3 (größtes n, abrunden, gegen „aufrunden“ der Sprosse): knapp bestätigt – die Rundungsrichtung ist der Kern der Sprosse; das merkmal („auf eine ganze Zahl runden“) deckt die Variante, sprosse_text nicht. Die Variante passt eher zu einem eigenen Original (2017-bb-ea-cas-B4.2b), das der Katalog hier nicht nennt.
- e1-k1-s5-v2 (Lösungssatz „weil … niemand doppelt befragt wird, ohne dass …“ schief): bestätigt – ich hatte den Satz als holprig bemerkt, aber nicht aufgenommen. Die Logik ist verdreht („obwohl“ statt „weil“).
- e1-k1-s7-v3, v4 (Zufallsgröße mit gleicher Verteilung konstruieren): nicht bestätigt – die Katalogsprosse der Prüfungshöhe (Mappe, Zeile 127) enthält ausdrücklich „… und zu einer gegebenen Verteilung eine gleichverteilte Zufallsgröße … konstruieren (iqb 2024MerhoehtAStochastik23-b)“; merkmal nennt es ebenfalls. Nur sprosse_text ist auf den ersten Teil verkürzt.
- e2-k1-s9-v3, v4 (Bernoulli-Formel statt Tabellendifferenz): nicht bestätigt – beide verfremden 2019-be-gk-B4.1a, das genau so aufgebaut ist (Einzelwert mit der Bernoulli-Formel, kumulierter Wert aus der Tabelle über das Gegenereignis); das Original steht in der Katalogsprosse.
- e2-k1-s9-v5, v6 (Vergleich über den Erwartungswert): nicht bestätigt – die Katalogsprosse (Zeile 128) nennt „zwei Einzelwahrscheinlichkeiten über den Erwartungswert vergleichen (abi 2018-bb-ea-B4.2c)“.
- e3-k1-s9-v7, v8 (Ansatz 1 − 0,85ⁿ ist Einheit-4-Stoff): als Bankbefund nicht bestätigt – der Katalog führt 2020MgrundlegendAStochastik2-b unter der Prüfungshöhe von Einheit 3 („Ungleichung mit Binomialsumme als Sachaussage formulieren“, Zeile 129); die Bank folgt ihm. Die inhaltliche Beobachtung ist richtig, gehört aber als Katalogbefund nach stand.md.

Nur Zweitleser:
- e2-k1-s5-v2: Verfremdung zu schwach – Münze sechsmal, höchstens einmal Zahl gegen das Original Münze fünfmal, höchstens einmal Wappen; gleicher Kontext.
- e3-k4-s4-v2, v3: sprosse_text „Kumulierte Binomialsumme als Sachaussage formulieren“, die Aufgaben verlangen Diagramm → kumulierte Wahrscheinlichkeit bzw. Stäbe markieren.

Widersprüche: Der Erstleser wertet e1-k1-s7-v3/v4, e2-k1-s9-v3 bis v6 und e3-k1-s9-v7/v8 als Merkmalsfehler; ich halte sie für katalogtreu, weil die Katalogsprossen der Prüfungshöhen mehrere Originale bündeln und die Bank nur den ersten Teil in sprosse_text übernommen hat. Behoben wäre das über einen vollständigen sprosse_text, nicht über neue Aufgaben.
