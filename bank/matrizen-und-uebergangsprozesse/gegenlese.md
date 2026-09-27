# Gegenlese: matrizen-und-uebergangsprozesse

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 215 (zone 27, e1 34, e2 36, e3 37, e4 39, e5 42)
Korrekturen: 0
Grundlage: Aufgaben selbst nachgerechnet (Python/sympy); bank.md für die Felder; mappen/matrizen-und-uebergangsprozesse.md für Sprossenfolge, Schreibform und Typische Fehler.

## Befunde

### 1 Lösung und pruef
matrizen-und-uebergangsprozesse-e4-k1-s5-v2: Die Lösung lässt den Zugang abstrakt („mit dem Zugang z“), obwohl die Aufgabe ihn festlegt (50 Tiere im ersten Gebiet); z kommt im Aufgabentext nicht vor – loesung „$M \cdot (M \cdot v + (50 | 0))$ – erst ein Schritt, dann der Zugang, dann der zweite Schritt“, pruef [50, 0]
### 2 Eindeutigkeit und Angaben
matrizen-und-uebergangsprozesse-e2-k1-s7-v3, matrizen-und-uebergangsprozesse-e2-k1-s7-v4: $M^T$ steht ohne Erklärung in der Definition von „orthogonal“ (in e2-k1-s5-v2 ist sie erklärt) – den Klammersatz „($M^T$ entsteht aus M durch Vertauschen von Zeilen und Spalten)“ ergänzen
matrizen-und-uebergangsprozesse-e3-k1-s7-v1: Anders als in allen übrigen Verflechtungszeilen sind Zeilen und Spalten von B nicht benannt (die 2×2-Matrix lässt sich auch transponiert lesen); außerdem braucht ein Tisch laut B 0 Platten – „(Zeilen Z1, Z2; Spalten E1, E2)“ ergänzen und B so wählen, dass jeder Tisch eine Platte hat
### 3 Sprosse und Merkmal
matrizen-und-uebergangsprozesse-e4-k1-s0-v3, matrizen-und-uebergangsprozesse-e5-k1-s0-v2: Die Aufgabe steht doppelt: zwei Schritte rückwärts ($M^{-1} \cdot M^{-1} \cdot v$ bzw. $(M^{-1})^2 \cdot v$) mit denselben drei Optionen – in e5 eine andere Schrittzahl oder einen gemischten Term nehmen (etwa $(M^{-1})^3 \cdot v$ mit angepassten Optionen)
matrizen-und-uebergangsprozesse-e5-k3-s3-v3: Die Anwendung ist eine eingekleidete Rechnung ohne Entscheidung (Schwelle über Faktor, „nach wie vielen Jahren“), gleich gebaut wie e5-k1-s6-v2 – eine Entscheidungsfrage stellen (etwa: reicht das Budget bis Jahr X, wann muss man spätestens handeln) oder einen anderen Kontext mit Abwägung
### 4 Schreibform
matrizen-und-uebergangsprozesse-e4-k1-s7-v3, matrizen-und-uebergangsprozesse-e4-k1-s7-v4: Die Lösung verlangt eine Diagonalmatrix D für den prozentualen Abzug; kein Merkkasten und keine Variante der Kette führt das ein (e4-k1-s5 nennt „Terme mit Abgang“, übt aber nur Zugang, Rückrechnung und Inverse) – eine Variante in e4-k1-s5 mit prozentualem Abgang über D ergänzen oder D im Aufgabentext einführen
### 5 Ankreuzen
matrizen-und-uebergangsprozesse-e3-k1-s0-v3: Der Distraktor „von Z3 nach E2“ nennt ein Zwischenprodukt, das es laut Aufgabe nicht gibt (B hat nur Z1, Z2) – er fällt ohne Verständnis weg; den Distraktor durch einen Fehler mit vorhandenen Knoten ersetzen (etwa „von Z1 nach E3“) oder B mit drei Zwischenprodukten ansetzen
### 6 Fehler finden
keine

## Entscheidungen

- E (Einheitsmatrix), $A^{-1}$ und $v_n$ gelten als Schreibweise des Merkkastens bzw. als in der Aufgabe eingeführt, nicht als unerklärte Buchstaben.
- Sprossen, deren Katalogtext mehrere Teilformen nennt (etwa e1-k1-s4, e3-k1-s6, e4-k1-s5, e5-k1-s6), verteilen die Teilformen auf die Varianten; das ist nicht als Merkmalswechsel zwischen Varianten gewertet.
- Prüfungshöhe: sprosse_text nennt nur den ersten Teil der Zielmarke, auch bei Zeilen zu weiteren Originalen (stand.md Entscheidung 3, dort als Katalogbefund geführt); nicht als Befund gezählt.
- pruef "" bei Lösungen, die nur einen Term mit Exponent tragen (e1-k1-s5-v3, e4-k2-s1-v3), hingenommen: keine Ergebniszahl.
- Alle 215 Lösungen rechnerisch bestätigt; keine Zeile brauchte eine Korrektur.

Sauber: 205 Zeilen ohne Befund
