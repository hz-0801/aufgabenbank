# Sprachlauf lineare-gleichungen

Stand 2026-09-28 (Gruppe 2). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py lineare-gleichungen`: 0 Abweichungen in zone, e1–e4 (1 vorbestehende in weg.jsonl, siehe unten).

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 48 | 0 | 48 |
| e2.jsonl | 47 | 0 | 47 |
| e3.jsonl | 36 | 0 | 36 |
| e4.jsonl | 40 | 0 | 40 |
| zone.jsonl | 28 | 0 | 28 |
| gesamt | 199 | 0 | 199 |

Geänderte Sprossen: 79. Die 10 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1 …).

## Entscheidungen

- Alle 199 Zeilen mit Feld aufgabe neu gefasst (zone, e1–e4). weg.jsonl
  hat kein Feld aufgabe (nur Lösungswege) und bleibt unberührt; weil
  seine ids mit zone.jsonl übereinstimmen, lief apply/bericht mit einer
  Kopie von sl.py, die Zeilen ohne aufgabe überspringt.
- „:“ als Bruch: $x : 4 = 5$, $x : 3 = 8$, $x : 4 = 3$, $24 : x = 3$,
  $x : 4 = 9$ stehen jetzt als $\frac{…}{…}$. „:“ bleibt, wo die
  Rechenart selbst Thema ist: Umkehroperation benennen (e1-k1-s0,
  „$:\,5$“), Teilen negativer Zahlen (zone-f2-v4, $-21 : (-7)$) und in
  der Umformungsangabe hinter dem Strich („$\mid :3$“, e2-k4-s3,
  e2-k4-s4-v2). Die Kreuz-Optionen mit „:“ (e4-k1-s1) bleiben wortgleich.
- „($x$: die gesuchte Zahl)“ wird überall der Satz „$x$ ist die
  gesuchte Zahl.“ (bzw. „$x$ ist die Strecke in km.“) und steht vor
  der Aufforderung. Wortlaut-Sätze in Anführung beginnen mit „Der Satz
  heißt: „…““.
- Einheitliche Satzformen: „Prüfe, ob $z$ die Gleichung … löst.“ (e1-k2),
  „Löse die Gleichung. $…$“ bzw. „Löse die Gleichung und mache die
  Probe. $…$“ (e2-k3, e3). loesung zeigt nie eine Menge, daher nirgends
  „Gib die Lösungsmenge an.“
- Fehler finden immer als „<Name> soll … Er/Sie rechnet so: …“ mit
  „Finde den Fehler und rechne richtig.“; wo eine Gleichung aus Text
  falsch aufgestellt ist (e4-k3-s1/s2) „… und schreibe die Gleichung
  richtig.“, bei Pauls Aussage „Die Lösung ist 0.“ „… und schreibe die
  Aussage richtig.“
- Sprosse „Was steht bei x?“ (e2-k1-s0): „Was steht in der Gleichung …
  beim $x$?“ mit Hinweis „Achte auf das Vorzeichen.“; bei $\frac{x}{3}$
  „Rechenzeichen“, weil die Antwort „$:3$“ ist.
- „zweischrittig“ ist kein Schülerwort: „eine Gleichung, die man in zwei
  Schritten löst“. Fachwörter Umformung, Hauptnenner, Probe, Basis,
  Schenkel bleiben, weil die Sprossen sie üben.
- bank-pruef meldet vor und nach dem Lauf dieselbe eine Abweichung
  („weg.jsonl: Dateiname“, vorbestehend, nicht durch den Sprachlauf);
  in zone und e1–e4 0 Abweichungen, 0 Warnungen.

## 10 Beispiele

1. `lineare-gleichungen-zone-f1-v1` – Punkt vor Strich (3 · 4 − 5)

   vorher: $2 + 4 \cdot 5$

   nachher: Berechne. $2 + 4 \cdot 5$

2. `lineare-gleichungen-zone-f3-v3` – Terme zusammenfassen (gleichartige Glieder mit x, Zahl und x

   vorher: $2x + 5 + 3x - 1$

   nachher: Fasse zusammen: $2x + 5 + 3x - 1$

3. `lineare-gleichungen-zone-f4-v4` – Brüche: Hauptnenner, Bruch mal Zahl

   vorher: Hauptnenner von $\frac{1}{4}$ und $\frac{1}{6}$?

   nachher: Finde den Hauptnenner der Brüche $\frac{1}{4}$ und $\frac{1}{6}$.

4. `lineare-gleichungen-e1-k2-s3-v1` – wA/fA entscheiden gemischt

   vorher: $3x + 4 = 25$ – ist $8$ Lösung?

   nachher: Prüfe, ob $8$ die Gleichung $3x + 4 = 25$ löst.

5. `lineare-gleichungen-e1-k4-s2-v1` – Probe weggelassen oder mit falscher Seite gerechnet.

   vorher: Mira löst $4x + 6 = 30$ und erhält 9. Eine Probe macht sie nicht. Finde den Fehler.

   nachher: Mira soll die Gleichung $4x + 6 = 30$ lösen. Sie erhält 9 und macht keine Probe. Finde den Fehler und rechne richtig.

6. `lineare-gleichungen-e2-k3-s2-v1` – einschrittig mal/geteilt

   vorher: $6x = 54$

   nachher: Löse die Gleichung. $6x = 54$

7. `lineare-gleichungen-e2-k4-s3-v1` – Nur ein Glied dividiert

   vorher: Sara rechnet: \rechnung{3x + 9 &= 21 &&\mid :3 \\ x + 9 &= 7} Finde den Fehler.

   nachher: Sara soll die Gleichung $3x + 9 = 21$ lösen. Sie rechnet so: \rechnung{3x + 9 &= 21 &&\mid :3 \\ x + 9 &= 7} Finde den Fehler und rechne richtig.

8. `lineare-gleichungen-e3-k1-s7-v1` – Prüfungshöhe: Klammer und x beidseitig.

   vorher: $5(x - 2) = 3x + 4$ – löse und mache die Probe.

   nachher: Löse die Gleichung und mache die Probe. $5(x - 2) = 3x + 4$

9. `lineare-gleichungen-e4-k1-s3-v1` – zweischrittig

   vorher: Das Dreifache einer Zahl, vermehrt um 8, ergibt 44. Gleichung und Zahl? ($x$: die gesuchte Zahl)

   nachher: Das Dreifache einer Zahl, vermehrt um 8, ergibt 44. $x$ ist die gesuchte Zahl. Stelle eine Gleichung auf und berechne die Zahl.

10. `lineare-gleichungen-e4-k3-s5-v1` – Gleichung aus Sachverhalt aufstellen und lösen (P10-Form)

   vorher: Eine Taxifahrt kostet 4 € Grundpreis und 2,20 € je Kilometer. Frau Kaya zahlt 37 €. Wie lang war die Fahrt? ($x$: Strecke in km)

   nachher: Eine Taxifahrt kostet 4 € Grundpreis und 2,20 € je Kilometer. Frau Kaya zahlt 37 €. $x$ ist die Strecke in km. Wie lang war die Fahrt?
