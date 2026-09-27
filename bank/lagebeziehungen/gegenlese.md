# Gegenlese: lagebeziehungen

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 146 (zone 27, e1 36, e2 26, e3 31, e4 26)
Korrekturen: 1

Jede Lösung aus der Aufgabe neu gerechnet (Python/sympy):
Punktproben, Parameterproben, allgemeiner Geradenpunkt, Scharfälle,
Pyramidenscharen, Schattenpunkte, Netzhöhen, Auftreffzeiten. Alle
Zahlen und pruef-Werte stimmen; korrigiert ist eine falsche Aussage
in einer Lösung.

Selbst entschieden (nicht geregelt): Eine sachlich falsche Aussage
in der loesung bei richtigem Zahlenergebnis gilt als Punkt 1 und
wird korrigiert, wenn die Korrektur eindeutig ist. Die
Modellkennung steht nicht im Kopf, weil die Sitzung keine
Modellkennung in Repo-Dateien schreiben darf.

## Punkt 1 – Lösung und pruef

lagebeziehungen-e3-k1-s4-v2: korrigiert – „(Normalenvektor gleich Richtungsvektor der Achse)“ war falsch: L: z = 2 hat den Normalenvektor (0 | 0 | 1), die Achse die Richtung (0 | 0 | 2). Jetzt „(der Normalenvektor $(0 | 0 | 1)$ ist ein Vielfaches des Richtungsvektors der Achse)“; H(1 | 1 | 2) und pruef unverändert.

## Punkt 2 – eindeutig lösbar

(keine Befunde)

## Punkt 3 – Sprosse und Merkmal

lagebeziehungen-zone-f5-v2: Die sehr leichten Zeilen der Fertigkeit unterscheiden sich in der Aufgabenart (v1 Term vereinfachen, v2 Gleichung lösen); „$3a - 6 = 0$“ ist fast dieselbe Aufgabe wie zone-f4-v1 „$3k + 6 = 0$“ – v2 als zweite Term-Aufgabe (etwa „$3(a - 1) + a$ – vereinfacht?“ → „$4a - 3$“), merkmal auf „Term mit Parameter vereinfachen“ festlegen.
lagebeziehungen-e3-k1-s3-v3: v1/v2 sind Entscheidungen (z-Koordinaten hängen nicht von t ab bzw. sind gleich), v3 verlangt t aus „$t + 1 = 5$“ mit Antwort „t = __“ – anderer Schritt, andere Antwortform – v3 wie v1 bauen (feste z-Koordinaten, Entscheidung begründen).
lagebeziehungen-e4-k2-s1-v3: sprosse_text „… Länge eines Schattens … beschreiben“, v1/v2 „Beschreibe“; v3 verlangt „Berechne“ mit Vektorbetrag $|\vec{FQ}| = \sqrt{3}$ – Operator und Anforderung wechseln, der Betrag steht nicht unter den Voraussetzungen des Eintrags – v3 als Beschreibungsaufgabe mit eigenem Kontext stellen.

## Punkt 4 – Schreibform

(keine Befunde)

## Punkt 5 – Ankreuzen

(keine Befunde)

## Punkt 6 – Fehler finden

lagebeziehungen-e2-k2-s1-v1: Muster „den falschen Punkt eingesetzt“ setzt voraus, dass der falsche Punkt zur Situation gehört (im Original zwei Quaderecken); Q(1 | 2 | 2) steht nicht in den Angaben, nur in Janas Rechnung – Q in die Angaben aufnehmen („Ein Körper hat die Ecken $P(2 | 4 | 1)$ und $Q(1 | 2 | 2)$; $E_k$ soll die Ecke $P$ enthalten.“). Rechnung und k = 1 richtig.

Sauber: 141 Zeilen ohne Befund
