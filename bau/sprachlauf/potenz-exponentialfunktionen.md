# Sprachlauf potenz-exponentialfunktionen

Stand 2026-09-28 (Gruppe 2). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand b1d04f6. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py potenz-exponentialfunktionen`: 0 Abweichungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 92 | 3 | 95 |
| e2.jsonl | 65 | 9 | 74 |
| e3.jsonl | 77 | 2 | 79 |
| e4.jsonl | 36 | 7 | 43 |
| e5.jsonl | 91 | 20 | 111 |
| zone.jsonl | 36 | 26 | 62 |
| gesamt | 397 | 67 | 464 |

Geänderte Sprossen: 140. Die 10 Beispiele sind je
Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen
verteilt (Zone zuerst, dann e1 …).

## Entscheidungen

- Doppelpunkt „:“ als Division nur in zone-f7-v2 behalten („Schreibe die
  Division $84 : 28$ als Bruch.“), weil dort das Umschreiben in einen Bruch
  die Aufgabe ist. Sonst Bruch: zone-f7-v1/v3 ($\frac{63}{45}$,
  $\frac{63}{36}$) und die Rechnung in e5-k4-s1-v3 ($\frac{125}{3}$).
- Originale (O): Die Mappe gibt für diese Kennungen keinen Wortlaut, nur
  gegeben/gesucht. Die Zeilen sind daher nur in kurze Sätze zerlegt; die
  Aufträge der Vorlage („Weise nach“, „Ergänze“, „Stelle … dar“,
  „Entscheide für jeden Graphen“) und die Prüfkennung an ihrem Platz
  bleiben.
- Grafikzeilen nennen die Darstellung: „Das Koordinatensystem zeigt drei
  Graphen $f$, $g$ und $h$.“, bei Skalen „Der Zahlenstrahl ist in
  Hunderterschritten beschriftet.“ (die Grafik ist ein \zahlenstrahl).
  Tabellenzeilen beginnen mit „Die Tabelle zeigt, wie … wächst/abnimmt.“
- Fachwörter der Sprossen (Differenz, Quotient, Faktor, Verdopplungszeit,
  Halbwertszeit, Ursprung, Quadrant) bleiben; wo sie zuerst geübt werden,
  steht eine Erklärung dabei („Rechne dazu immer neuer Wert minus alter
  Wert.“, „die Halbwertszeit (die Zeit, bis nur noch die Hälfte da
  ist)“, „dritten Quadranten (unten links)“). Neue Zahlen durfte eine
  Erklärung nicht bringen; deshalb z. B. kein „$(0 | 0)$“ neben
  „Ursprung“, sondern „ganz unten links“.
- Nackte Funktionsangaben („$f(x) = x^3$. Berechne …“) beginnen jetzt mit
  „Die Funktion lautet …“, Ja/Nein-Fragen zur Punktprobe mit „Prüfe mit
  einer Rechnung, ob …“.
- Behauptungen ohne Sprecher („Behauptung: „…““, „Aussage: …“) werden zu
  „Jemand sagt: „…“ Prüfe mit einer Rechnung, ob das stimmt.“; der Streit
  zweier Schüler (e3-k3-s2-v3) und die „Mitschülerin“ (e4-k2-s2-v2)
  bekommen einen Namen und die feste Begründen-Form.
- Rundungsangaben ausgeschrieben („Runde auf zwei Stellen nach dem
  Komma.“); „(drei Stellen)“ in e2-k2-s7-v2 als drei Stellen nach dem
  Komma gelesen, passend zur Lösung ($2{,}166$; $2{,}058$).
- Wo die Multimengenprobe eine Zahl zweimal verlangt, steht sie zweimal im
  Satz (e1-k4-s4-v3: beide Waldstücke mit „$4\,000$ Bäume“).
- Unverändert: e3-k1-s6-v3, e3-k3-s3-v2, e5-k1-s7 und weitere schon
  klare Zeilen (Würfel, reine Rechnungen, „Fülle die Wertetabelle …
  aus.“).

## 10 Beispiele

1. `potenz-exponentialfunktionen-zone-f1-v1` – Erhöhung und Senkung um p Prozent als Faktor

   vorher: Ein Ticket kostet $50\,€$. Der Preis steigt um $10\,\%$. Neuer Preis?

   nachher: Ein Ticket kostet $50\,€$. Der Preis steigt um $10\,\%$. Wie hoch ist der neue Preis?

2. `potenz-exponentialfunktionen-zone-f7-v1` – Division zweier Tabellenwerte als Quotient schreiben und deu

   vorher: In einer Tabelle steht $45$, darunter $63$. Berechne den Quotienten $63 : 45$.

   nachher: In einer Tabelle steht der Wert $45$. Darunter steht der Wert $63$. Berechne den Quotienten $\frac{63}{45}$.

3. `potenz-exponentialfunktionen-e1-k1-s0-v1` – „gleicher Betrag oder gleicher Prozentsatz“ und „Differenz o

   vorher: „Jedes Jahr kommen $50\,€$ auf das Sparbuch.“ Was bleibt jedes Jahr gleich? \\ \kreuz{der Betrag} \\ \kreuz{der Prozentsatz}

   nachher: Auf ein Sparbuch kommen jedes Jahr $50\,€$ dazu. Kreuze an, was jedes Jahr gleich bleibt. \\ \kreuz{der Betrag} \\ \kreuz{der Prozentsatz}

4. `potenz-exponentialfunktionen-e1-k2-s6-v1` – fallender Graph bei Abnahme

   vorher: Ein Auto verliert jedes Jahr $20\,\%$ seines Werts. Welcher Graph passt? \\ \kreuz{$f$} \\ \kreuz{$g$} \\ \kreuz{$h$}

   nachher: Ein Auto verliert jedes Jahr $20\,\%$ seines Werts. Kreuze an, welcher Graph im Koordinatensystem zum Wert des Autos passt. \\ \kreuz{$f$} \\ \kreuz{$g$} \\ \kreuz{$h$}

5. `potenz-exponentialfunktionen-e2-k1-s5-v1` – mehrere Quotienten bilden und vergleichen, Ergebnis in einem

   vorher: Bilde alle Quotienten benachbarter Werte und schreibe das Ergebnis in einem Satz. \wertetabelle[150,180,216,259{,}2]{Jahr}{Anzahl}{0,1,2,3}

   nachher: Die Tabelle zeigt, wie sich eine Anzahl entwickelt. Berechne die Quotienten von Wert zu Wert. Teile dazu immer den neuen Wert durch den alten. Schreibe das Ergebnis in einem Satz auf. \wertetabelle[150,180,216,259{,}2]{Jahr}{Anzahl}{0,1,2,3}

6. `potenz-exponentialfunktionen-e3-k1-s0-v1` – „welcher Schritt ist null“ ankreuzen (Vorstufe)

   vorher: Ein Bestand wird ab $2016$ jedes Jahr größer. Welcher Schritt $t$ gehört zum Jahr $2021$? \\ \kreuz{$t = 2021$} \\ \kreuz{$t = 5$} \\ \kreuz{$t = 6$}

   nachher: Ein Bestand wird ab $2016$ jedes Jahr größer. Kreuze an, welcher Schritt $t$ zum Jahr $2021$ gehört. \\ \kreuz{$t = 2021$} \\ \kreuz{$t = 5$} \\ \kreuz{$t = 6$}

7. `potenz-exponentialfunktionen-e3-k2-s8-v1` – Prüfungshöhe: Wert nach vielen Schritten mit der Potenz und

   vorher: Die Zahl der Hefezellen in einer Probe wächst exponentiell mit $N(t) = 64 \cdot 1{,}25^t$ ($t$ in Stunden). Aussage: „Nach $30$ Stunden sind es mehr als $50\,000$ Zellen.“ Prüfe die Aussage rechnerisch. (P10 2025 OS)

   nachher: Die Zahl der Hefezellen in einer Probe wächst exponentiell. Es gilt $N(t) = 64 \cdot 1{,}25^t$ mit $t$ in Stunden. Eine Aussage lautet: „Nach $30$ Stunden sind es mehr als $50\,000$ Zellen.“ Prüfe die Aussage mit einer Rechnung. (P10 2025 OS)

8. `potenz-exponentialfunktionen-e4-k2-s2-v1` – Begründen (warum es genügt, den doppelten Wert einmal zu suc

   vorher: Begründe, warum es genügt, den doppelten Wert einmal zu suchen, um die Verdopplungszeit zu bestimmen – egal, von welchem Punkt des Graphen aus.

   nachher: Du willst am Graphen die Verdopplungszeit bestimmen. Dafür suchst du den doppelten Wert nur einmal. Begründe, warum das von jedem Punkt des Graphen aus genügt.

9. `potenz-exponentialfunktionen-e5-k2-s6-v1` – beim Exponenten drei mit der dritten Wurzel am Taschenrechne

   vorher: $f(x) = x^3$. Für welches $x$ ist $f(x) = 125$?

   nachher: Die Funktion lautet $f(x) = x^3$. Für welche Zahl $x$ gilt $f(x) = 125$?

10. `potenz-exponentialfunktionen-e5-k4-s4-v1` – Sachaufgabe (Volumen eines Würfels aus der Kante, Kante aus

   vorher: Das Volumen einer Kugel hängt vom Radius ab: $V(r) = \frac{4}{3} \pi r^3$. Ein Ballon wird von $10\,\mathrm{cm}$ auf $20\,\mathrm{cm}$ Radius aufgeblasen. Um welchen Faktor wächst sein Volumen? Begründe mit dem Exponenten.

   nachher: Für das Volumen einer Kugel mit dem Radius $r$ gilt $V(r) = \frac{4}{3} \pi r^3$. Ein Ballon wird aufgeblasen. Sein Radius wächst von $10\,\mathrm{cm}$ auf $20\,\mathrm{cm}$. Um welchen Faktor wächst sein Volumen? Begründe mit dem Exponenten.
