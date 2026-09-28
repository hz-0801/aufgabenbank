# Sprachlauf zuordnungen

Stand 2026-09-28 (Sprachlauf Gruppe 3). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 8f035a6. Nur das Feld aufgabe ist geändert;
`python3 werkzeuge/bank-pruef.py zuordnungen`: 0 Abweichungen, 1 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 42 | 22 | 64 |
| e2.jsonl | 25 | 35 | 60 |
| e3.jsonl | 19 | 19 | 38 |
| e4.jsonl | 38 | 37 | 75 |
| zone.jsonl | 8 | 15 | 23 |
| gesamt | 132 | 128 | 260 |

Geänderte Sprossen: 49. Die 10 Beispiele sind je Sprosse die erste
geänderte Zeile, gleichmäßig über die Sprossen verteilt (Zone zuerst).

## 10 Beispiele vorher/nachher

1. `zuordnungen-zone-f1-v3` – Punkte im Koordinatensystem eintragen und ablesen (erster Qu

   vorher: Lies ab: Welche Koordinaten hat der Punkt C?

   nachher: Das Koordinatensystem zeigt den Punkt C. Lies ab, welche Koordinaten der Punkt C hat.

2. `zuordnungen-zone-f4-v3` – Bruchteil einer Größe (die Hälfte, ein Viertel von 12 €)

   vorher: Ein Viertel von 3 € – wie viel?

   nachher: Berechne ein Viertel von 3 €.

3. `zuordnungen-e1-k2-s1-v1` – unter zwei angebotenen Einteilungen die passende ankreuzen

   vorher: Die Werte gehen bis 60 km, die Achse hat 15 Kästchen. Welche Einteilung passt? \\ \kreuz{1 Kästchen = 1 km} \\ \kreuz{1 Kästchen = 5 km}

   nachher: Die Werte einer Tabelle gehen bis 60 km. Die Achse hat 15 Kästchen. Kreuze an, welche Einteilung passt. \\ \kreuz{1 Kästchen = 1 km} \\ \kreuz{1 Kästchen = 5 km}

4. `zuordnungen-e1-k3-s1-v1` – Formel aus Tabelle (y = 4 · x)

   vorher: Die Tabelle gehört zu einer proportionalen Zuordnung (x: Anzahl Hefte, y: Preis in €). Wie lautet die Formel?

   nachher: Die Tabelle zeigt eine proportionale Zuordnung. x ist die Anzahl der Hefte, y ist der Preis in €. Schreibe die Formel für y auf.

5. `zuordnungen-e2-k1-s0-v1` – „Was ist hier eine Portion?“ – die Bezugseinheit benennen (e

   vorher: Äpfel: 3 kg kosten 4,50 €. Was ist hier eine Portion?

   nachher: 3 kg Äpfel kosten 4,50 €. Was ist hier eine Portion?

6. `zuordnungen-e2-k8-s1-v1` – Fehler finden (Wert für eine Portion falsch; addiert statt m

   vorher: 3 kg Kartoffeln kosten 7,20 €. Tim rechnet für 1 kg: 7,20 € − 3 = 4,20 €. Finde den Fehler und rechne richtig.

   nachher: 3 kg Kartoffeln kosten 7,20 €. Tim soll ausrechnen, was 1 kg kostet. Er rechnet so: 7,20 € − 3 = 4,20 €. Finde den Fehler und rechne richtig.

7. `zuordnungen-e3-k1-s5-v2` – Sachtext

   vorher: Familie Berg fährt eine Radtour mit 15 km/h und braucht 4 Stunden. Im nächsten Jahr fährt sie dieselbe Strecke mit E-Bikes im Schnitt 20 km/h. Wie lange braucht sie dann?

   nachher: Familie Berg fährt eine Radtour mit 15 km/h und braucht 4 Stunden. Im nächsten Jahr fährt sie dieselbe Strecke mit E-Bikes. Dann fährt sie im Schnitt 20 km/h. Wie lange braucht sie dann?

8. `zuordnungen-e4-k1-s0-v1` – „null Kilogramm kosten null Euro?“ – ja bei proportional, ne

   vorher: Taxi: 4 € Grundgebühr und 2 € je km. Kostet eine Fahrt von 0 km auch 0 €? \\ \kreuz{ja} \\ \kreuz{nein}

   nachher: Eine Taxifahrt kostet 4 € Grundgebühr und 2 € je km. Kreuze an, ob eine Fahrt von 0 km auch 0 € kostet. \\ \kreuz{ja} \\ \kreuz{nein}

9. `zuordnungen-e4-k2-s5-v1` – gemischte Tabellen (proportional, antiproportional, keins)

   vorher: Welcher Zuordnungstyp liegt in der Tabelle vor? Prüfe erst die Quotienten, dann die Produkte. \\ \kreuz{proportional} \\ \kreuz{antiproportional} \\ \kreuz{keins von beiden}

   nachher: Die Tabelle zeigt eine Zuordnung. Prüfe erst die Quotienten $\frac{y}{x}$, dann die Produkte x · y. Kreuze an, welcher Zuordnungstyp vorliegt. \\ \kreuz{proportional} \\ \kreuz{antiproportional} \\ \kreuz{keins von beiden}

10. `zuordnungen-e4-k5-s3-v1` – proportional, antiproportional oder keins von beiden (Tabell

   vorher: Ein Brunnen liefert 5 l Wasser je Minute. Zeichne den Graphen Zeit in min → Wasser in l für 0 bis 4 Minuten und nenne den Zuordnungstyp.

   nachher: Ein Brunnen liefert 5 l Wasser je Minute. Nach rechts kommt die Zeit in min, nach oben das Wasser in l. Zeichne den Graphen für 0 bis 4 Minuten und nenne den Zuordnungstyp.

## Fälle, in denen die Regeln nicht reichten

1. `zuordnungen-e1-k4-s1-v1`: Der erste Entwurf „Lea soll am Graphen ablesen …“
   löste in bank-pruef eine Abweichung aus (Ableseauftrag ohne grafik; die
   Zeile hat keine Grafik). Entscheidung: umformuliert zu „Lea will wissen, wie
   weit sie nach 2 Stunden ist. Im Graphen liegt der Punkt dafür 5 Kästchen
   hoch. …“. Das Wort „ablesen“ darf in einer Zeile ohne grafik auch dann
   nicht stehen, wenn es gar kein Auftrag an den Schüler ist.
2. Pfeilschreibweise „Zeit → Weg“ (z. B. e2-k6-s1, e4-k5-s3-v1, e1-k4-s3-v3):
   Die Regeln sagen nichts dazu. Entscheidung: In Zeichenaufträgen ersetzt
   durch einen festen Satz „Nach rechts kommt …, nach oben …“; in
   Begründen-/Ankreuzzeilen durch Wörter („der Preis proportional zur
   Mietdauer“, „die Füllhöhe im Lauf der Zeit“). In den kreuz-Optionen und
   in unveränderten Zeilen blieb „→“ nicht stehen, weil es dort nicht vorkam.
3. Quotient „y : x“ (e4-k2-s1, e4-k2-s5): Das Zeichen ist hier nicht das
   Thema, also nach Regel 4 als Bruch `$\frac{y}{x}$` geschrieben. Die
   Pfeilrechnungen im Dreisatz („: 4“, „: 8“ in e2-k3-s0 und e2-k8-s2) blieben,
   weil die Sprosse genau dieses Zeichen am Pfeil übt. Die Fehlerrechnung von
   Pia (e4-k5-s1-v2) steht jetzt als `$\frac{1\,200}{4} = 300$`, damit
   Regel 4 auch für Fehler-finden-Rechnungen gilt.
