# Sprachlauf reelle-zahlen

Stand 2026-09-28 (Sprachlauf Gruppe 3). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand f2ac52e. Nur das Feld aufgabe ist geändert;
`python3 werkzeuge/bank-pruef.py reelle-zahlen`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 48 | 6 | 54 |
| e2.jsonl | 54 | 0 | 54 |
| e3.jsonl | 54 | 0 | 54 |
| zone.jsonl | 33 | 0 | 33 |
| gesamt | 189 | 6 | 195 |

Geänderte Sprossen: 76. Die 10 Beispiele sind je Sprosse die erste
geänderte Zeile, gleichmäßig über die Sprossen verteilt (Zone zuerst).

## 10 Beispiele vorher/nachher

1. `reelle-zahlen-zone-f1-v1` – Bruch in Dezimalzahl umwandeln (Division), abbrechende und p

   vorher: $\frac{3}{4}$ – als Dezimalzahl?

   nachher: Schreibe den Bruch $\frac{3}{4}$ als Dezimalzahl.

2. `reelle-zahlen-zone-f3-v4` – Quadratwurzel als Umkehrung des Quadrierens, Quadratzahlen b

   vorher: $\sqrt{-9}$ – welche Zahl?

   nachher: Welche Zahl ist $\sqrt{-9}$?

3. `reelle-zahlen-zone-f6-v1` – Potenz als Malkette mit Basis und Exponent, Potenz ausrechne

   vorher: $3^3$ – als Malkette und ausgerechnet?

   nachher: Schreibe $3^3$ als Malkette und rechne aus.

4. `reelle-zahlen-zone-f7-v4` – Brüche als Exponenten lesen und mit Brüchen rechnen

   vorher: $\frac{1}{4} + \frac{1}{4}$ – ausgerechnet?

   nachher: Berechne $\frac{1}{4} + \frac{1}{4}$.

5. `reelle-zahlen-e1-k1-s7-v1` – exakt und gerundet nebeneinander (Wurzel als Ergebnis stehen

   vorher: Ein Quadrat hat den Flächeninhalt $7\,\text{cm}^2$. Seitenlänge exakt und auf zwei Stellen gerundet?

   nachher: Ein Quadrat hat den Flächeninhalt $7\,\text{cm}^2$. Wie lang ist eine Seite? Gib den Wert genau als Wurzel an. Runde ihn dann auf zwei Stellen nach dem Komma.

6. `reelle-zahlen-e2-k1-s0-v1` – „gleiche Basis oder gleicher Exponent“ und „mal oder plus“ a

   vorher: $7^3 \cdot 7^5$ – welches Gesetz passt? \\ \kreuz{gleiche Basis} \\ \kreuz{gleicher Exponent} \\ \kreuz{keins: ausrechnen}

   nachher: Kreuze an, welches Potenzgesetz zu $7^3 \cdot 7^5$ passt. \\ \kreuz{gleiche Basis} \\ \kreuz{gleicher Exponent} \\ \kreuz{keins: ausrechnen}

7. `reelle-zahlen-e2-k1-s8-v1` – Terme mit einer Variablen

   vorher: $x^5 \cdot x^2$ – vereinfacht?

   nachher: Vereinfache $x^5 \cdot x^2$.

8. `reelle-zahlen-e2-k3-s3-v1` – Produkt gleicher Basen als Malkette schreiben, Faktoren zähl

   vorher: Ein Speicherbaustein fasst $2^{30}$ Byte. Ein Laufwerk enthält $2^8$ solcher Bausteine. Wie viele Byte fasst das Laufwerk? Gib eine Zweierpotenz an.

   nachher: Ein Speicherbaustein fasst $2^{30}$ Byte. Ein Laufwerk enthält $2^8$ solcher Bausteine. Wie viele Byte fasst das Laufwerk? Schreibe das Ergebnis als Potenz mit der Basis $2$.

9. `reelle-zahlen-e3-k1-s8-v1` – Potenzgesetze auf Wurzeln übertragen

   vorher: $5^{\frac{1}{2}} \cdot 5^{\frac{1}{2}}$ – Ergebnis?

   nachher: Berechne $5^{\frac{1}{2}} \cdot 5^{\frac{1}{2}}$.

10. `reelle-zahlen-e3-k2-s4-v1` – teilweises Wurzelziehen: Quadratzahl als Faktor abspalten

   vorher: Ein quadratisches Grundstück hat $800\,\text{m}^2$. Gib die Seitenlänge exakt und möglichst einfach sowie gerundet an.

   nachher: Ein quadratisches Grundstück ist $800\,\text{m}^2$ groß. Wie lang ist eine Seite? Gib den Wert genau und so einfach wie möglich an. Gib auch einen gerundeten Wert an.

## Fälle, in denen die Regeln nicht reichten

1. e2-k1-s3-*, s5-v2/v3, s6-v2/v3, s7-v2/v3, s8-v2, s9-v2, s12-v2, e2-k1-s0-v2,
   e3-k1-s10-v2 – Division mit „:“ zwischen Potenzen bzw. Wurzeln ($7^8 : 7^3$,
   $\sqrt{a} : \sqrt{b} = \sqrt{a : b}$). Entscheidung: „:“ bleibt. Die Sprossen
   üben das Quotientengesetz selbst, und die loesung schreibt durchgehend „:“
   ($(15 : 5)^3$, $8x^6 : (4x)$); ein Bruch in aufgabe und „:“ in loesung würde
   nicht zusammenpassen. Falls der Chat Brüche will, müsste loesung mitgezogen werden.
2. e1-k1-s0-v3/v4 – alte Frage „Bruch oder nicht?“ passte nicht zu den Optionen
   (bricht ab / periodisch / weder noch). Neu gefragt, was die Optionen verlangen
   („Kreuze an, ob die Zahl abbricht, periodisch ist oder weder noch.“); die Idee
   „rational“ steckt nur noch im Sprossentext. Optionen wörtlich unverändert.
3. „Zehntel/Hundertstel“ und „exakt“: In e1-k1-s5 (Zahlenstrahl) steht jetzt
   „zwei Zahlen mit einer Stelle nach dem Komma“ statt „Zehnteln“; in e1-k1-s9
   (Einschachtelung, Vorrat H/GYM) blieben „Zehnteln/Hundertsteln“, weil die Sprosse
   genau das übt. „exakt“ wurde überall zu „genau (als Wurzel)“; e3-k2-s4-v1 fragt
   „einen gerundeten Wert“ ohne Stellenzahl, weil die alte aufgabe keine nannte
   (loesung rundet auf eine Stelle).
