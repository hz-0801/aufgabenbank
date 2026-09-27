# Gegenlese: binomialverteilung

Datum: 2026-09-27  
Modell: Claude in Claude Code (Web-Sitzung); die genaue Modellkennung darf laut Sitzungsvorgabe nicht ins Repo, sie steht im Chatbericht  
Geprüfte Zeilen: 282  
Korrekturen: 0

## Festlegungen dieser Gegenlese

- Jede Zeile einzeln nachgerechnet (Python mit sympy/scipy), aus dem Aufgabentext; bank.md nur für die Felder, stand.md nicht gelesen.
- Korrigiert wird nur, wenn loesung selbst rechnerisch falsch ist und die Korrektur eindeutig in loesung/pruef liegt. Ein unvollständiges pruef bei richtiger loesung ist ein Befund unter Punkt 1, keine Korrektur.
- Widerspricht die Lösung einer Grafik oder dem Aufgabentext und ließe sich das an Aufgabe, Grafik oder Lösung beheben, ist die Korrektur nicht eindeutig: Befund, keine Änderung.
- Korrigierte Zeilen stehen unter Punkt 1 mit „korrigiert“ und zählen nicht als sauber. Eine Zeile mit mehreren Befunden steht unter jedem Punkt einmal.
- e2-k2-s1-v1 nicht korrigiert: Das Endergebnis 0,1608 stimmt, nur der gerundete Zwischenschritt 10 · 0,0161 passt nicht dazu; welche Seite angepasst wird, ist nicht eindeutig.

## Befunde

### 1 Lösung und pruef

- binomialverteilung-e2-k2-s1-v1: Zwischenschritt „10 · 0,0161 ≈ 0,1608“ rechnerisch inkonsistent (10 · 0,0161 = 0,161); Endwert 0,1608 und pruef stimmen – „= 10 · 125/7776 ≈ 0,1608“ schreiben oder den Zwischenwert weglassen
- binomialverteilung-e5-k1-s7-v3: Begründung „8 liegt näher am Maximum als 2“ trägt nicht: bei p = 0,51 liegt das Maximum bei 5, beide Abstand 3 – Begründen über $\binom{10}{8}=\binom{10}{2}$ und $p^6 > (1-p)^6 \Leftrightarrow p > 0{,}5$

### 2 Eindeutig lösbar

- binomialverteilung-e2-k1-s6-v3: Mehrdeutig: wegen (9 über 5) = (9 über 4) passt auch n = 9, k = 4, p = 0,55. Anders als v1/v2 ist p nicht vorgegeben – Trefferwahrscheinlichkeit 0,45 vorgeben oder beide Deutungen als richtig zulassen
- binomialverteilung-e3-k1-s9-v3: Rundung nicht vorgegeben; mit gerundetem Zwischenwert 0,0345 ergibt sich 0,8225 statt 0,8226 – Rundung angeben und in der Lösung „mit ungerundetem Zwischenergebnis weiterrechnen“ vermerken
- binomialverteilung-e3-k1-s9-v4: Rundung nicht vorgegeben; mit gerundetem Zwischenwert 0,0755 ergibt sich 0,8093 statt 0,8091 – Rundung angeben und in der Lösung „mit ungerundetem Zwischenergebnis weiterrechnen“ vermerken
- binomialverteilung-e3-k4-s2-v3: k ist nicht als ganze Zahl erklärt; für nicht ganzzahliges k (etwa 7,5) ist die Aussage falsch – „für eine ganze Zahl k“ ergänzen
- binomialverteilung-e4-k1-s9-v7: Auch p = 0 und p = 1 erfüllen $P(X=1)=P(X=2)$; die Lösung teilt stillschweigend durch $p(1-p)^2$ – Im Text „mit 0 < p < 1“ ergänzen
- binomialverteilung-e4-k1-s9-v8: Auch p = 0 und p = 1 erfüllen die Gleichung (beide Seiten null); p = 2/3 ist so nicht eindeutig – Im Text „mit 0 < p < 1“ ergänzen
- binomialverteilung-e4-k1-s9-v9: Auch p = 1 erfüllt $P(X=0)=P(X=1)$ (beide null); Lösung teilt durch $(1-p)^5$ – Im Text „mit 0 < p < 1“ ergänzen

### 3 Sprosse und Merkmal

- binomialverteilung-e1-k1-s7-v3: Zufallsgröße mit gleicher Verteilung konstruieren ist ein anderer Aufgabentyp als die Sprosse (Aussagen beurteilen, dritten Ausgang finden); Merkmal wechselt gegenüber v1/v2 – Durch Variante im Typ von v1/v2 ersetzen oder als eigene Sprosse führen
- binomialverteilung-e1-k1-s7-v4: Zufallsgröße mit gleicher Verteilung konstruieren ist ein anderer Aufgabentyp als die Sprosse (Aussagen beurteilen, dritten Ausgang finden); Merkmal wechselt gegenüber v1/v2 – Durch Variante im Typ von v1/v2 ersetzen oder als eigene Sprosse führen
- binomialverteilung-e1-k2-s3-v1: Sprosse verlangt „genau ein Treffer bei zwei Versuchen“; gerechnet wird „mindestens einer“ über das Gegenereignis – Frage auf genau ein ausfallendes Triebwerk umstellen oder Sachkontext mit genau einem Treffer wählen
- binomialverteilung-e1-k2-s3-v3: Drei Versuche und „höchstens einer“ statt „genau ein Treffer bei zwei Versuchen“ laut Sprosse – Auf zwei Versuche und genau einen Treffer umstellen
- binomialverteilung-e2-k1-s1-v1: Sprosse: Term „ohne Rechnung hinschreiben“; Aufgabe verlangt zusätzlich „berechne ihn“; das ist erst Sprosse 2 – „und berechne ihn“ streichen, Lösung auf den Term beschränken
- binomialverteilung-e2-k1-s1-v2: Sprosse: Term „ohne Rechnung hinschreiben“; Aufgabe verlangt zusätzlich „berechne ihn“; das ist erst Sprosse 2 – „und berechne ihn“ streichen, Lösung auf den Term beschränken
- binomialverteilung-e2-k1-s1-v3: Sprosse: Term „ohne Rechnung hinschreiben“; Aufgabe verlangt zusätzlich „berechne ihn“; das ist erst Sprosse 2 – „und berechne ihn“ streichen, Lösung auf den Term beschränken
- binomialverteilung-e2-k1-s1-v4: Sprosse: Term „ohne Rechnung hinschreiben“; Aufgabe verlangt zusätzlich „berechne ihn“; das ist erst Sprosse 2 – „und berechne ihn“ streichen, Lösung auf den Term beschränken
- binomialverteilung-e2-k1-s1-v5: Sprosse: Term „ohne Rechnung hinschreiben“; Aufgabe verlangt zusätzlich „berechne ihn“; das ist erst Sprosse 2 – „und berechne ihn“ streichen, Lösung auf den Term beschränken
- binomialverteilung-e2-k1-s9-v3: Einzelwahrscheinlichkeit per Bernoulli-Formel, nicht als Differenz zweier Tabellenwerte wie in der Sprosse; Typ wechselt gegenüber v1/v2 – Einzelwert aus der Y-Tabelle als Differenz bestimmen lassen oder als eigene Sprosse führen
- binomialverteilung-e2-k1-s9-v4: Einzelwahrscheinlichkeit per Bernoulli-Formel, nicht als Differenz zweier Tabellenwerte wie in der Sprosse; Typ wechselt gegenüber v1/v2 – Einzelwert aus der Y-Tabelle als Differenz bestimmen lassen oder als eigene Sprosse führen
- binomialverteilung-e2-k1-s9-v5: Keine Tabelle, keine Differenz: Vergleich über den Erwartungswert passt nicht zur Sprosse; Merkmal wechselt gegenüber v1/v2 – Als eigene Sprosse führen oder durch Tabellen-Differenz-Variante ersetzen
- binomialverteilung-e2-k1-s9-v6: Keine Tabelle, keine Differenz: Vergleich über den Erwartungswert passt nicht zur Sprosse; Merkmal wechselt gegenüber v1/v2 – Als eigene Sprosse führen oder durch Tabellen-Differenz-Variante ersetzen
- binomialverteilung-e3-k1-s9-v7: Ansatz 1 − 0,85^n mit gesuchtem n ist Umkehraufgabe (Einheit 4), keine Verkettung zweier Modelle bzw. geteilte Kette wie in Sprosse/Merkmal – Durch Variante mit verketteten Modellen oder geteilter Kette ersetzen oder nach E4 verschieben
- binomialverteilung-e3-k1-s9-v8: Ansatz 1 − 0,88^n mit gesuchtem n ist Umkehraufgabe (Einheit 4), keine Verkettung zweier Modelle bzw. geteilte Kette wie in Sprosse/Merkmal – Durch Variante mit verketteten Modellen oder geteilter Kette ersetzen oder nach E4 verschieben
- binomialverteilung-e4-k1-s2-v3: Variante fragt nach höchstens n und rundet ab; Sprosse und übrige Varianten verlangen Mindestanzahl und Aufrunden – Als Mindestanzahl-Frage mit Aufrunden stellen oder in eine eigene Sprosse verschieben
- binomialverteilung-e4-k3-s3-v3: Sprosse verlangt Versuchsanzahl für mindestens einen Treffer; Aufgabe sucht eine Grenze k bei festem n = 50 – Durch eine Planungsaufgabe „Mindestanzahl n für mindestens einen Treffer“ ersetzen
- binomialverteilung-e5-k3-s4-v1: Sprosse verlangt die Gegenzufallsgröße; Aufgabe zeichnet nur die Verteilung von X – Aus gegebener Verteilung von X das Diagramm von n − X zeichnen lassen
- binomialverteilung-e5-k3-s4-v2: Keine Gegenzufallsgröße; Diagramm in Tabelle übertragen, andere Richtung als v1 – An die Sprosse „Gegenzufallsgröße im Diagramm darstellen“ anpassen
- binomialverteilung-e5-k3-s4-v3: Keine Gegenzufallsgröße und kein Diagramm; es wird p aus einer Tabelle bestimmt – An die Sprosse „Gegenzufallsgröße im Diagramm darstellen“ anpassen

### 4 Schreibform

- binomialverteilung-e1-k1-s5-v2: Lösungssatz logisch schief: „weil … niemand doppelt befragt wird, ohne dass sich der Anteil ändert“ klingt, als begründe das Nicht-Zurücklegen das gleiche p – Umformulieren: „Obwohl niemand doppelt befragt wird, ändert sich der Anteil bei sehr vielen Pendlern kaum.“
- binomialverteilung-e4-k1-s1-v2: Potenz eines Bruchs ohne Klammer: $\frac{5}{6}^n$ ist als Schreibweise mehrdeutig – $\left(\frac{5}{6}\right)^n$ schreiben
- binomialverteilung-e5-k1-s4-v1: Lösungssatz unklar: „allein die Säule bei 3 fast halb so hoch“; Bezug fehlt – Formulieren: „allein die Säule bei 3 hat fast 50 Prozent“

### 5 Ankreuzen

- keine

### 6 Fehler finden

- keine

Sauber: 250 Zeilen ohne Befund
