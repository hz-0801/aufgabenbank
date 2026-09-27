# Zweitlesung linearkombination-und-lineare-abhaengigkeit

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne Kenntnis
von gegenlese.md) · geprüfte Zeilen: 58 (e1 18, e2 22, zone 18)

Prüfung: jede Rechnung mit numpy nachgerechnet (Kollinearität und
Faktor, Ansatz dreier Vektoren, Differenzvektoren, Parameterpunkte,
Gleichungssysteme), bank-pruef.py 0 Abweichungen, 0 Warnungen; dazu
Eindeutigkeit, Passung zu sprosse_text und merkmal, Ankreuzoptionen,
eingebaute Fehler, Verfremdung der Originale.

## Befunde

linearkombination-und-lineare-abhaengigkeit-e1-k1-s0-v1 bis v4:
Die Optionen `\kreuz{ja} \kreuz{nein}` stehen in einer Zeile;
bank.md verlangt je `\kreuz` eine Zeile – Vorschlag: `\\` zwischen
die beiden Kreuze. Inhaltlich richtig; in v3 ist der Faktor negativ
($\vec{a} = -5 \cdot \vec{b}$), die Gegenrichtung ist aber erst
Sprosse 2 – für die Vorstufe „nur hinsehen" ein positiver Faktor
wie $(0 | 5 | -5)$ und $(0 | 1 | -1)$ passt besser.

linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v3: $\vec{u} =
(3 | 0 | 6)$, $\vec{v} = (1 | 0 | 2)$ – wer den Faktor aus der
Nullkomponente holen will ($0 = k \cdot 0$), findet keinen; das ist
eine kleine Falle im Grundfall, wo merkmal „Faktor aus einer
Komponente" heißt – Vorschlag: Nullkomponente in Sprosse 2 (dort
steht der Nullvektor) und hier $(3 | 9 | 6)$, $(1 | 3 | 2)$.

linearkombination-und-lineare-abhaengigkeit-e1 (Einheit gesamt):
keine Pflichtelemente (fehler, begruenden); bank.md verlangt sie je
Einheit, „wo die Typen sie tragen" – Kollinearität trägt beides
(Fehler: Faktor nur an zwei Komponenten geprüft; Begründen: warum
der Nullvektor zu jedem Vektor kollinear ist) – Vorschlag: Kette k2
mit 3 fehler und 3 begruenden ergänzen.

linearkombination-und-lineare-abhaengigkeit-e2-k1-s2-v3: Die
Sprosse heißt „die Intervallbedingung als Streckeneigenschaft
deuten", merkmal „Parametergrenzen als Endpunkte, außerhalb nur
Gerade"; die Zeile fragt Punkt und Teilverhältnis für $0{,}75$ und
$0{,}25$, prüft also nicht das Intervall – Rechnung stimmt
($X(2 | 3 | 1)$, $1 : 3$) – Vorschlag: zusätzlich fragen, ob
$\vec{OX} = 1{,}25 \cdot \vec{OA} - 0{,}25 \cdot \vec{OB}$ noch auf
der Strecke liegt.

linearkombination-und-lineare-abhaengigkeit-e2-k2-s1-v2, -v3: pruef
"0" bzw. "1" sind Platzhalter, keine Lösungszahl (die Ziffern der
Lösung sind die Intervallgrenzen); ehrlicher wäre "" – bank.md
erlaubt "" aber nur ohne Ziffer – Vorschlag: bank.md um den Fall
„Ziffern nur in Intervallgrenzen oder Bezeichnern" ergänzen, dann
"".

linearkombination-und-lineare-abhaengigkeit-zone-f4-v1 bis v4: Die
Fertigkeit „Vielfache und Verhältnisse erkennen" kommt laut Katalog
aus zuordnungen.md (Sek I); die vier Zeilen fragen aber „Ist
$(3 | 6)$ ein Vielfaches von $(1 | 2)$? Faktor?" und in v3 sogar
ein Tripel mit Faktor $-1{,}5$ – das ist der Grundfall der Einheit
1 in Kurzform, die Zone soll keinen Begriff des Themas
vorwegnehmen – Vorschlag: proportionale Zahlenpaare in Sek-I-Form
(„3 Stück kosten 6 €, 5 Stück 10 € – gleicher Faktor?", Tabelle
mit einer falschen Spalte), v3 mit negativem Faktor streichen.

Sauber: 46 Zeilen ohne Befund (alle Rechnungen stimmen; alle
Ankreuzzeilen haben genau eine richtige Option; die drei
Fehler-finden-Zeilen tragen echte Fehler, alle aus dem Muster der
„Typischen Fehler"; das Zone-Paar f1-v5/v6 stimmt; die vier
Prüfungshöhen verfremden beide Originale mit anderen Punkten und
Kontexten bei gleichem Verfahren).

## Abgleich mit gegenlese.md

Erstleser: 20 Zeilen mit Befund, keine Korrektur. Zweitleser: 12
Zeilen mit Befund. Beide: alle Rechnungen richtig.

Beide: e1-k1-s0-v3 (negativer Faktor in der Vorstufe; der Erstleser
nennt zusätzlich v1, dort ist $\vec{b} = -2 \cdot \vec{a}$ ebenfalls
negativ – zutreffend, vom Zweitleser übersehen); e1-k1-s1-v3 (der
Erstleser wegen offener Richtung des Faktors und Bruchfaktor, der
Zweitleser wegen der Nullkomponente – beide Gründe gelten, die
Zeile ist neu zu setzen); e2-k1-s2-v3 (Teilverhältnis steht nicht
in Sprosse und Merkmal); zone-f4-v3 und -v4 (Vorwegnahme des
Grundfalls von Einheit 1; der Zweitleser sieht das auch bei v1 und
v2, weil schon „Vielfaches von $(1 | 2)$" die Vektorform ist).

Nur Erstleser, alle zutreffend und zu übernehmen: e1-k1-s1-v5
(Richtung des Faktors offen, Dezimalfaktor als eigenes Merkmal);
e2-k1-s1-v1 bis v5 (welcher Koeffizient ersetzt wird, ist offen –
„Setze $p = 1 - q$ ein" in die Aufgabe); e1-k1-s2-v1 bis v3
(Varianten tragen verschiedene Merkmale); e2-k1-s2-v1 und -v2 (drei
Typen in einer Sprosse); zone-f1-v5 (Fehler finden einzeilig statt
senkrecht); e1-k1-s3-v2 (Schluss auf „unabhängig" braucht die
Nichtkollinearität von $\vec{a}$, $\vec{b}$); e1-k1-s4-v2 (Ansatz
fehlt).

Nur Zweitleser: e1-k1-s0-v1 bis v4 (Kreuze in einer Zeile statt je
Zeile); zone-f4-v1 und -v2 (siehe oben).

Widerspruch: Fehlende Pflichtelemente in Einheit 1 – der Erstleser
zählt sie zum Bestand (stand.md), der Zweitleser führt sie als
Befund, weil bank.md sie je Einheit verlangt; in der Sache einig,
nur der Ort unterscheidet sich. pruef "0"/"1" in e2-k2-s1-v2/-v3 –
der Erstleser wertet Zahlen aus dem Lösungstext als passend, der
Zweitleser als Platzhalter, der eine Regel in bank.md braucht.
