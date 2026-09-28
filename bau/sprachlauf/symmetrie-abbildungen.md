# Sprachlauf symmetrie-abbildungen

Stand 2026-09-28 (Gruppe 4). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 6341a45. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py symmetrie-abbildungen`: Abweichungen: 0, Warnungen: 0

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 51 | 3 | 54 |
| e2.jsonl | 76 | 11 | 87 |
| e3.jsonl | 50 | 4 | 54 |
| zone.jsonl | 25 | 5 | 30 |
| gesamt | 202 | 23 | 225 |

Geänderte Sprossen: 81. Die Beispiele sind je Sprosse
die erste geänderte Zeile, gleichmäßig über die Sprossen verteilt.

## Entscheidungen

- Fast alle Zeilen haben ein Koordinatensystem oder eine Figur als Grafik.
  Der Satz nennt sie jetzt: „Das Koordinatensystem zeigt …“, „… im Bild“
  (Regel 5). Aufträge ohne Lage („Spiegle das Dreieck ABC an der Geraden a.“)
  bekommen einen Lagesatz davor.
- Fehler finden stand als „Finde den Fehler. <Lage>“; jetzt Lage zuerst,
  dann „Finde den Fehler und beschreibe, wie es richtig geht.“ (Zeichen-
  und Zählfehler ohne Rechnung) bzw. „… schreibe die Aussage/den Punkt
  richtig.“; beim Linienzählen „… und rechne richtig.“
- „Begründe: <Aussage>“ und „Begründe, warum …“ ohne Behauptung einer Person
  werden „Erkläre, warum …“ (Regel 6).
- „Welcher? Kreuze an.“ und „Frage? Kreuze an.“ werden „Kreuze an, …“; bei
  Messaufgaben mit Ankreuzen bleibt „Prüfe durch Messen, … Kreuze an.“,
  weil der Messauftrag vor dem Ankreuzen steht.
- „Kathete“ ist kein Übungswort der Sprosse: „an einer seiner kurzen Seiten
  gespiegelt. Diese Seiten heißen Katheten.“
- Fachwörter Rechtsachse, Hochachse, Quadrant, Symmetrieachse,
  punktsymmetrisch, Zentrum, Verschiebungspfeil, deckungsgleich bleiben.

## 10 Beispiele

1. `symmetrie-abbildungen-e1-k1-s0-v1` – „Erst rechts, dann hoch“ – zu gegebenen Punktpaaren nur den Weg mit zw

   vorher: Zeichne vom Ursprung aus nur den Weg zu $(4|1)$ mit zwei Pfeilen ein: erst nach rechts, dann nach oben. Setze keinen Punkt.

   nachher: Zeichne im Koordinatensystem den Weg vom Ursprung zu $(4|1)$ mit zwei Pfeilen ein. Gehe erst nach rechts, dann nach oben. Setze keinen Punkt.

2. `symmetrie-abbildungen-e1-k2-s8-v1` – Prüfungshöhe: unter vier Punkten den ankreuzen, der auf der Rechtsachs

   vorher: Genau einer der vier Punkte liegt auf der Rechtsachse (x-Achse). Welcher? (P10 2020 OS) \\ \kreuz{$A(6|4)$} \\ \kreuz{$B(0|4)$} \\ \kreuz{$C(-6|-4)$} \\ \kreuz{$D(6|0)$}

   nachher: Genau einer der vier Punkte liegt auf der Rechtsachse (x-Achse). Kreuze diesen Punkt an. (P10 2020 OS) \\ \kreuz{$A(6|4)$} \\ \kreuz{$B(0|4)$} \\ \kreuz{$C(-6|-4)$} \\ \kreuz{$D(6|0)$}

3. `symmetrie-abbildungen-e2-k2-s0-v1` – „passt die Faltung“ und „wie viele Achsen“ ankreuzen

   vorher: Passen beim Falten an der eingezeichneten Geraden beide Hälften genau aufeinander? \\ \kreuz{ja} \\ \kreuz{nein}

   nachher: Die Figur im Bild wird an der eingezeichneten Geraden gefaltet. Kreuze an, ob beide Hälften genau aufeinanderpassen. \\ \kreuz{ja} \\ \kreuz{nein}

4. `symmetrie-abbildungen-e2-k2-s10-v1` – Zahl der Symmetrieachsen eines Drachenvierecks als erste Teilleistung 

   vorher: Ein Kinderdrache hat die Form des Drachenvierecks ABCD. Seine Leisten sind die Diagonalen: AC ist 40\,cm, BD ist 70\,cm lang, sie kreuzen sich rechtwinklig. Wie viele Symmetrieachsen hat das Drachenviereck? Kreuze an. (P10 2025 OS) \\ \kreuz{0} \\ \kreuz{1} \\ \kreuz{2} \\ \kreuz{3} \\ \kreuz{4}

   nachher: Ein Kinderdrache hat die Form des Drachenvierecks ABCD. Seine Leisten sind die Diagonalen: AC ist 40\,cm, BD ist 70\,cm lang. Sie kreuzen sich rechtwinklig. Kreuze an, wie viele Symmetrieachsen das Drachenviereck hat. (P10 2025 OS) \\ \kreuz{0} \\ \kreuz{1} \\ \kreuz{2} \\ \kreuz{3} \\ \kreuz{4}

5. `symmetrie-abbildungen-e2-k3-s8-v2` – Prüfungshöhe: ein Dreieck liegt mit einer Seite auf der Spiegelgeraden

   vorher: Für ein Fensterbild wird ein Dreieck mit den Seiten 3\,cm, 4\,cm und 6\,cm an der 6\,cm langen Seite gespiegelt. Welches Viereck entsteht aus Dreieck und Spiegelbild? (P10 2018 OS)

   nachher: Für ein Fensterbild hat man ein Dreieck mit den Seiten 3\,cm, 4\,cm und 6\,cm. Es wird an der 6\,cm langen Seite gespiegelt. Welches Viereck bilden Dreieck und Spiegelbild zusammen? (P10 2018 OS)

6. `symmetrie-abbildungen-e3-k1-s1-v1` – Figur mit einem Pfeil verschieben, Kästchen abzählen

   vorher: Der Verschiebungspfeil führt von P nach Q. Verschiebe das Dreieck ABC mit diesem Pfeil.

   nachher: Im Koordinatensystem führt ein Verschiebungspfeil von P nach Q. Verschiebe das Dreieck ABC mit diesem Pfeil.

7. `symmetrie-abbildungen-e3-k1-s10-v1` – Prüfungshöhe: zu einem Figurenpaar die Abbildung benennen und begründe

   vorher: Welche Abbildung führt das Dreieck ABC in A'B'C' über? Begründe, warum AB und A'B' gleich lang sind.

   nachher: Das Koordinatensystem zeigt die Dreiecke ABC und A'B'C'. Welche Abbildung führt ABC in A'B'C' über? Begründe, warum AB und A'B' gleich lang sind.

8. `symmetrie-abbildungen-zone-f1-v4` – Kästchen im Raster abzählen und Strecken auf dem Karo abtragen

   vorher: Eine Strecke beginnt auf der 2. Karolinie und endet auf der 9. Karolinie. Wie viele Kästchen lang?

   nachher: Eine Strecke beginnt auf der 2. Karolinie und endet auf der 9. Karolinie. Wie viele Kästchen ist sie lang?

9. `symmetrie-abbildungen-zone-f4-v1` – Vierecksarten und Dreiecksarten an ihren Eigenschaften erkennen und be

   vorher: Wie heißt dieses Viereck?

   nachher: Wie heißt das Viereck im Bild?

10. `symmetrie-abbildungen-zone-f7-v3` – Strecken messen und gleich lange Strecken abtragen

   vorher: Miss die Seite c auf den Millimeter genau.

   nachher: Miss die Seite c des Dreiecks im Bild auf den Millimeter genau.
