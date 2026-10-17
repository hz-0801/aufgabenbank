# Probe: Lernblatt nach Buch (Mathematik plus 6, 2.1)

Start 11:52, Ende 12:27 (17.10.2026). Setzer tisch-alt, Kennung B7N
(nur Probe, nicht im Register), Teil L1n. Blatt 4 Seiten, Lösung 1 Seite.
Bank und Katalog nicht committet; Bauskript im Scratchpad.

## Folge → Registerzeile

| Blatt | Folge | Inhalt (eigen) |
|---|---|---|
| 1 | 0 Wissen-Lückentext | 6 Lückensätze + drei Beispielterme |
| 2 | 1 gleichnamig, kürzen | Päckchen a)–f), a) grau |
| 3 | 2 Additionsmauern | 4 Mauern, a) grau gefüllt, c) d) rückwärts |
| 4 | 3 geteilte Figuren | 2 Kreise, 2 Rechtecke (TikZ), je + und − |
| 5 | 4 ungleichnamig | Päckchen a)–f), Hauptnenner, a) grau |
| 6 | 5 passt das? | Beet: 2/3 Kartoffeln + 1/2 Bohnen = 7/6 |
| 7 | 6 Bruchteile einer Menge | 60 Teebeutel, 1/5 + 1/4, a)–c) |
| 8 | 7 Zeichen-Rätsel | ∘ △ ∼ ∥ = 1/2, 1/3, 1/4, 1/6; f) selbst erfinden |

## Abweichungen

- Kein vorgerechnetes Beispiel als Kasten: der Setzer kennt im
  tisch-alt nur das graue a). Nr. 1 trägt die Beispiele als Zeile im Kopf.
- Wissen-Kasten ist eine normale Nummer (Päckchen aus Lückensätzen),
  kein Rahmen; Lücken stehen nicht untereinander, sondern 2×2.
- Nr. 6 (Sache Beet) steht ohne Text über dem Bild; Bild links,
  Text rechts (Setzer-Form gzwei); die Nummer 6 steht allein oben.
- Nr. 6 setzt der Setzer als Einzelaufgabe mit Karo, keine Linie für
  „Was meinst du dazu?“.
- Zeichen: nur LaTeX-Symbole (∘ △ ∼ ∥), weil bank-pruef \tikz in
  aufgabe als fremden Baustein meldet; eigene Hieroglyphen-artige
  Zeichen wären nur als grafik möglich.
- Schwere: Nr. 6 (Folge 5) trägt stufe ziel statt Schwere 2; das
  Feld kennt nur basis/kern/ziel.
- Kein Vorrat (Auftrag), kein Kritiker.

## Prüfmeldungen

- bank-pruef bruchrechnung: 0 Abweichungen, 7 Warnungen (Mengen je
  Sprosse über Soll, Formprobe P6 doppelt – Folge der Zusatzzeilen).
- loesung-pruef: 0 Meldungen (Katalog und die neuen Bankzeilen über
  setzer.weg).
- sympy: jede Summe, Mauer, Figur, Sachzahl, Zeichenaufgabe.
- Bildkontrolle pdftoppm -r 60: alle 5 Seiten; Mauern und Figuren
  passen zu den Zahlen, nichts abgeschnitten.
