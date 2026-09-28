# Zweitlesung grenzwerte-und-verhalten-im-unendlichen

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 136 (zone 31, e1 36,
e2 42, e3 27)

Prüfung: Jede Zeile gelesen und die Lösung nachgerechnet; ein
sympy-Skript im Scratchpad (nachrechnen.py) trägt alle Terme von
Hand ein und prüft Grenzwerte beider Richtungen, Nullstellen,
Funktionswerte, Ableitungen, Symmetrie (f(−x) − f(x)), die Seite
der Annäherung an die x-Achse, Parameterfälle (a, k positiv und
negativ) sowie Achsenbereiche und Extremwerte der sieben Grafiken:
159 Proben, 0 Abweichungen. Begründen- und Textzeilen inhaltlich
gelesen, alle 22 Originale der Mappe gegen die Verfremdung
gehalten. `python3 werkzeuge/bank-pruef.py
grenzwerte-und-verhalten-im-unendlichen`: „Abweichungen: 0,
Warnungen: 0". Ankreuzen-Zeilen geprüft: 26 (zone 8, e1 9, e2 5,
e3 4), je genau eine richtige Option, Lösung wortgleich;
Fehler-finden-Zeilen geprüft: 10 (zone 1, e1 3, e2 3, e3 3), der
eingebaute Fehler ist jeweils falsch, die richtige Rechnung stimmt.

## Befunde

e2-k1-s4-v3: übt nicht das Merkmal der Sprosse. Die Sprosse heißt
„Vorzeichen des Polynoms auf der wachsenden Seite"; die Aufgabe
fragt für 0,2x(4 − x)·e^x nur x → −∞, also die Seite, auf der der
e-Faktor verschwindet (Annäherung von unten). Die wachsende Seite
x → +∞ mit x(4 − x) < 0, f → −∞ kommt nicht vor. Das Original
2020MgrundlegendBAnalysisWTR2-1b fragt ebenfalls nur x → −∞, die
Zuordnung zur Sprosse ist also Katalogsache – Vorschlag für die
Bank: beide Richtungen verlangen („und gib das Verhalten für
x → +∞ an"), Lösung um „für x → +∞: f(x) → −∞, weil x(4 − x)
dort negativ ist" ergänzen.

e1-k3-s2-v3: Begründen auf Blatt-0-Niveau. „Warum werden die Werte
von x³ für x → −∞ negativ" ist die Zone-Fertigkeit 1 (ungerade
Potenz einer negativen Zahl), nicht eine der beiden Begründungen,
die der Katalog für Einheit 1 nennt (Z. 21: warum nur der Leitterm
zählt; warum ein negativer Leitkoeffizient bei geradem Grad beide
Seiten nach unten schickt). Vorschlag: „Begründe, warum bei
f(x) = 2x³ − 7x die beiden Seiten in entgegengesetzte Richtungen
laufen" (Lösung: ungerade Potenz behält das Vorzeichen von x, der
Leitterm 2x³ ist links negativ, rechts positiv).

e3-k1-s1-v1: dieselbe Funktion 2e^{−x} + 4 mit derselben Frage
(was bleibt für x → +∞) steht schon in e1-k1-s0-v4 (Erkennungs-
schritt „Wer gewinnt?", dort als Ankreuzen). Doppel über Einheiten
hinweg – Vorschlag: e3-k1-s1-v1 auf 3e^{−x} + 5 (Lösung 5,
Asymptote y = 5, pruef 5). Unschädlich, aber der Vollständigkeit
halber: (x − 1)·e^x steht in e2-k2-s2-v1 und e2-k2-s4-v1 zweimal
mit verschiedener Frage.

e1-k2-s3-v2, e2-k1-s4-v1: sehr nah am Original. In e1-k2-s3-v2 ist
der Leitterm 1/8·x⁴ wortgleich der des Originals 2022-bebb-lk-B2.1a
(f_0(x) = 1/8x⁴ + 2x) – und der Leitterm ist genau das, was die
Sprosse abfragt (Bruchkoeffizient). Vorschlag: 1/6·x⁴ oder
1/10·x⁴. In e2-k1-s4-v1 unterscheidet sich 0,5·(x² − 9)·e^x vom
Original 2023-bebb-gk-B2.1a 0,5·(x² − 4)·e^x nur in der 9; die
Falle bleibt gleich, aber „andere Zahlen" ist knapp erfüllt –
Vorschlag: 0,25·(x² − 9)·e^x oder (x² − 9)·e^{0,5x}. Das Prüfskript
sperrt nur ganze Terme, deshalb schlägt es hier nicht an.

e2-k1-s5-v3, e3-k2-s3-v1: Kontext passt nicht zum Term. In
e2-k1-s5-v3 bleibt die Heizung eingeschaltet („Nach dem
Einschalten einer Heizung"), das Rohr kühlt aber laut Term wieder
auf 18 °C ab – Vorschlag: „Ein Rohr wird kurz aufgeheizt und dann
sich selbst überlassen" (so wie es e2-k2-s3-v3 mit dem Motor
löst). In e3-k2-s3-v1 hat der Kuchen zu Beginn T(0) = 180 °C; das
ist die Ofentemperatur, ein Kuchen kommt mit rund 100 °C aus dem
Ofen – Vorschlag: T(t) = 20 + 80e^{−0,05t}.

e1-k2-s4-v1, e1-k2-s4-v2, e1-k2-s4-v3, e2-k1-s2-v1, e2-k1-s2-v2,
e2-k1-s2-v3, e2-k1-s6-v1, e2-k1-s6-v2, e2-k1-s6-v3 (Kleinigkeit):
die Aufgabe nennt „für x → −∞ und x → +∞", das Antwortgerüst und
die Lösung führen +∞ zuerst. Jede Lücke ist beschriftet, also
lösbar, aber auf dem Blatt springt die Reihenfolge – Vorschlag:
im Aufgabentext die Reihenfolge des Gerüsts (+∞, dann −∞) nehmen.

e3 (ohne id): kein Pflichtelement darstellung, laut stand.md
Entscheidung. Die Einheit trägt es aber: waagerechte Asymptote am
Graphen ablesen und den Term dazu ankreuzen (a·e^{−kx} + c mit
verschiedenem c und Vorzeichen von a), Graph zu 3e^{−x} − 2
skizzieren, Sättigungskurve lesen. Vorschlag: 3 Zeilen
k2-s4 nachziehen wie in e1 und e2 (ankreuzen, zeichnen, teil).

Sauber: 120 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k1-s5-v3 (Kontext Heizung passt nicht zur
Abkühlung auf 18 °C); e2-k1-s4-v3 (fragt nur die verschwindende
Seite x → −∞, Merkmal ist die wachsende Seite; der Erstleser
merkt zusätzlich form text statt teil an – teile ich).
Nur Zweitleser: e1-k3-s2-v3 (Begründen auf Blatt-0-Niveau);
e3-k1-s1-v1 (Doppel 2e^{−x} + 4 mit e1-k1-s0-v4); e1-k2-s3-v2,
e2-k1-s4-v1 (zu nah am Original: Leitterm 1/8x⁴ wortgleich, nur
eine Zahl geändert); e3-k2-s3-v1 (Kuchen mit 180 °C); e1-k2-s4-v1
bis v3, e2-k1-s2-v1 bis v3, e2-k1-s6-v1 bis v3 (Reihenfolge der
Richtungen in Aufgabe und Gerüst vertauscht); e3 ohne
Pflichtelement darstellung.
Nur Erstleser: e3-k2-s3-v3 („erreicht höchstens" setzt ein
Maximum voraus, die Lösung sagt „nie erreicht") – richtig,
übersehen; die vorgeschlagene Frage „Welcher Geschwindigkeit
nähert er sich auf Dauer" ist besser. zone-f1-v5 (keine negative
Basis) – teile ich nicht: Katalog Z. 28 nennt in derselben
Fertigkeit ausdrücklich „große Zahlen einsetzen und die
Größenordnung vergleichen (x⁴ gegen x²)", der Fallstrick übt
genau das; x = −10 wäre eine unschädliche Verschärfung, kein
Muss. e1-k1-s0-v3 (e^{−x} schon in Einheit 1) – teile ich nicht:
Katalog Z. 36 legt den Erkennungsschritt „Wer gewinnt?" mit
Leitterm, e-Faktor und konstantem Summanden vor Einheit 1 bis 3,
bank.md stellt ihn einmal in die erste Einheit seines Bereichs;
die Mischung ist Katalogvorgabe, und Zone f3-v4 hat e^{−x}
vorbereitet. Wer die e-Funktion vor Einheit 2 fernhalten will,
muss den Katalog ändern, nicht die Bank.
Widerspruch: zone-f1-v5 – der Erstleser sieht die Fertigkeit
„negative Basis" verfehlt, ich sehe den Größenordnungsvergleich
derselben Katalogzeile getroffen; e1-k1-s0-v3 – der Erstleser
hält e^{−x} in Einheit 1 für verfrüht, ich halte die Mischung für
die Vorgabe von Katalog Z. 36.
