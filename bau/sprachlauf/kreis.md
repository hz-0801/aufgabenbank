# Sprachlauf kreis

Stand 2026-09-28 (Gruppe 4). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand ef14d32. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py kreis`: Abweichungen: 0, Warnungen: 0

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 53 | 2 | 55 |
| e2.jsonl | 46 | 3 | 49 |
| e3.jsonl | 35 | 9 | 44 |
| zone.jsonl | 24 | 2 | 26 |
| gesamt | 158 | 16 | 174 |

Geänderte Sprossen: 63. Die Beispiele sind je Sprosse
die erste geänderte Zeile, gleichmäßig über die Sprossen verteilt.

## Entscheidungen

- „Kreis mit $d = …$ – wie lang ist der Umfang?“ wird „Ein Kreis hat den
  Durchmesser $d = …$. Wie lang ist sein Umfang?“ (Radius und Fläche ebenso).
- „Rechne mit der $\pi$-Taste und runde auf eine Stelle.“ wird zwei Sätze:
  „Rechne mit der $\pi$-Taste. Runde auf eine Stelle nach dem Komma.“
  (Regel 2: „auf eine Stelle“ allein ist zu knapp); ebenso „zwei Stellen“,
  „auf eine Stelle gerundet“ und „; runde auf eine Stelle“. In Originalen
  steht der Rundungssatz vor der Prüfkennung.
- „Rand oder Fläche? Kreuze an.“ wird „Kreuze an, ob es um den Rand (Umfang)
  oder um die Fläche geht.“, weil die Optionen „Umfang/Fläche“ heißen.
- Division als Bruch: „$u : d$“ wird $\frac{u}{d}$, ebenso in den Rechnungen
  der Fehleraufgaben e3-k3-s1 und in zone-f2-v2.
- „Sektor“ wird beim ersten Auftreten erklärt („ein Teil, ein Sektor“);
  sonst „Teil des Kreises“.
- Fachwörter Radius, Durchmesser, Umfang, Kreisausschnitt,
  Mittelpunktswinkel, Bogen, Kreisring bleiben (Sprossen üben sie).

## 10 Beispiele

1. `kreis-e1-k1-s0-v1` – „Rand oder Fläche?“ – zu jeder Frage ankreuzen: Umfang (Reifen, Borte,

   vorher: Ein runder Tisch bekommt rundherum eine Kante aus Holzleiste. Rand oder Fläche? Kreuze an.\\ \kreuz{Umfang}\\ \kreuz{Fläche}

   nachher: Ein runder Tisch bekommt rundherum eine Kante aus Holzleiste. Kreuze an, ob es um den Rand (Umfang) oder um die Fläche geht.\\ \kreuz{Umfang}\\ \kreuz{Fläche}

2. `kreis-e1-k2-s6-v1` – Halbkreisbogen

   vorher: Ein Weg führt im Halbkreis um einen Teich, der Durchmesser des Halbkreises ist $d = 12$ m. Wie lang ist der Weg? Rechne mit der $\pi$-Taste und runde auf eine Stelle.

   nachher: Ein Weg führt im Halbkreis um einen Teich. Der Durchmesser des Halbkreises ist $d = 12$ m. Wie lang ist der Weg? Rechne mit der $\pi$-Taste. Runde auf eine Stelle nach dem Komma.

3. `kreis-e1-k6-s2-v1` – Begründen (warum u : d bei jedem Kreis gleich ist)

   vorher: Begründe, warum man bei jedem Kreis für $u : d$ ungefähr dasselbe Ergebnis erhält.

   nachher: Erkläre, warum man bei jedem Kreis für $\frac{u}{d}$ ungefähr dasselbe Ergebnis erhält.

4. `kreis-e2-k1-s4-v1` – Halbkreis, Viertelkreis

   vorher: Eine Bühne hat die Form eines Halbkreises mit $r = 6$ m. Wie groß ist ihre Fläche? Rechne mit der $\pi$-Taste und runde auf eine Stelle.

   nachher: Eine Bühne hat die Form eines Halbkreises mit $r = 6$ m. Wie groß ist ihre Fläche? Rechne mit der $\pi$-Taste. Runde auf eine Stelle nach dem Komma.

5. `kreis-e2-k5-s1-v1` – Fehler finden (d in die Formel; 2 · π · r als Fläche; r² als 2 · r)

   vorher: Ein Kreis hat den Durchmesser $d = 12$ cm. Max rechnet die Fläche: \rechnung{A &= \pi \cdot 12^2 \\ A &\approx 452{,}4 \text{ cm}^2} Wo ist der Fehler?

   nachher: Ein Kreis hat den Durchmesser $d = 12$ cm. Max soll die Fläche berechnen. Er rechnet so: \rechnung{A &= \pi \cdot 12^2 \\ A &\approx 452{,}4 \text{ cm}^2} Finde den Fehler und rechne richtig.

6. `kreis-e3-k1-s2-v1` – beliebiger Winkel als Prozent mit Runden

   vorher: Ein Kreisausschnitt hat den Mittelpunktswinkel $\alpha = 100^\circ$. Wie viel Prozent des Kreises sind das? Runde auf eine Stelle.

   nachher: Ein Kreisausschnitt hat den Mittelpunktswinkel $\alpha = 100^\circ$. Wie viel Prozent des Kreises sind das? Runde auf eine Stelle nach dem Komma.

7. `kreis-e3-k3-s1-v1` – Fehler finden (mit dem Restwinkel gerechnet; α : 180; Umfang ohne die 

   vorher: Im Bild ist ein Ausschnitt mit $110^\circ$ grau, der Rest ist weiß. Jana berechnet den grauen Anteil: \rechnung{250^\circ : \text{Vollwinkel} &\approx 0{,}694 \\ &= 69{,}4\,\%} Wo ist der Fehler?

   nachher: Im Bild ist ein Ausschnitt mit $110^\circ$ grau, der Rest ist weiß. Jana soll den grauen Anteil berechnen. Sie rechnet so: \rechnung{\frac{250^\circ}{\text{Vollwinkel}} &\approx 0{,}694 \\ &= 69{,}4\,\%} Finde den Fehler und rechne richtig.

8. `kreis-zone-f1-v5` – Fläche und Umfang unterscheiden; Einheiten cm, cm², m, m²

   vorher: Ein Beet ist $6$ m lang und $4$ m breit. Es bekommt rundherum einen Zaun. Paul rechnet: \rechnung{6 \cdot 4 &= 24 \\ \text{Zaun} &= 24 \text{ m}} Wo ist der Fehler?

   nachher: Ein Beet ist $6$ m lang und $4$ m breit. Es bekommt rundherum einen Zaun. Paul soll die Länge des Zauns berechnen. Er rechnet so: \rechnung{6 \cdot 4 &= 24 \\ \text{Zaun} &= 24 \text{ m}} Finde den Fehler und rechne richtig.

9. `kreis-zone-f4-v1` – Quadrieren und Wurzelziehen (4,5²; √20,25)

   vorher: $7^2$ – wie viel?

   nachher: Berechne. $7^2$

10. `kreis-zone-f6-v3` – Anteil als Bruch und Prozentsatz bilden (Mittelpunktswinkel zum Vollwi

   vorher: $17$ von $45$ – wie viel Prozent? Runde auf eine Stelle.

   nachher: Wie viel Prozent sind $17$ von $45$? Runde auf eine Stelle nach dem Komma.
