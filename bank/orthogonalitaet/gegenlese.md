# Gegenlese: orthogonalitaet

Datum: Sun Sep 27 21:40:59 UTC 2026
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 164
Korrekturen: 1

## Punkt 1 – Lösung und pruef
- orthogonalitaet-e1-k5-s1-v1: korrigiert: $(1 | 3 | 2) \circ (3 | -1 | 0)$ → $(1 | 2 | 2) \circ (2 | -1 | 0)$ – für $S(1|1|1)$, $A(2|3|3)$, $B(3|0|1)$ ist $\overrightarrow{SA} = (1|2|2)$ und $\overrightarrow{SB} = (2|-1|0)$; die genannten Vektoren passten nicht zu den Punkten und nicht zur Zeile „2 − 2 + 0“; pruef 0 bleibt

## Punkt 2 – Eindeutigkeit und Angaben
- orthogonalitaet-zone-f4-v1: „Gib den Faktor an“ legt die Richtung nicht fest – $\frac{1}{2}$ ist ebenso richtig wie $2$ – Fragesatz ergänzen: „Gib den Faktor $k$ mit $(2 | 6 | -4) = k \cdot (1 | 3 | -2)$ an.“
- orthogonalitaet-zone-f4-v2: wie f4-v1, $-\frac{1}{3}$ ebenso richtig wie $-3$ – „Gib den Faktor $k$ mit $(-3 | 0 | 6) = k \cdot (1 | 0 | -2)$ an.“
- orthogonalitaet-zone-f4-v3: wie f4-v1, $\frac{2}{3}$ ebenso richtig wie $1{,}5$ – „Gib den Faktor $k$ mit $(1{,}5 | -3 | 4{,}5) = k \cdot (1 | -2 | 3)$ an.“
- orthogonalitaet-e2-k2-s3-v3: nicht eindeutig lösbar – $\overrightarrow{BA} \circ \overrightarrow{BC} = (-6|0|0) \circ (0|y|2) = 0$ für jedes $y$, verlangt ist aber „Bestimme $y$“; die Lösung wählt $y = 4$ willkürlich, $|BC|$ hängt davon ab – Punkte so ändern, dass $y$ aus einer Gleichung folgt, z. B. $A(0 | 3 | 3)$, $B(6 | 0 | 3)$, $C(8 | y | 5)$: $(-6|3|0) \circ (2|y|2) = -12 + 3y = 0$, $y = 4$, $|BC| = \sqrt{24} \approx 4{,}9$ m
- orthogonalitaet-e3-k2-s3-v1: der Mast zeigt von $F(0|3|2)$ in Richtung $(2|0|-8)$, also mit fallendem $z$ in den Hang hinein ($F + (2|0|-8) = (2|3|-6)$ liegt unter der Hangebene) – Richtung $(-2 | 0 | 8) = -2 \cdot (1 | 0 | -4)$ angeben, Lösung mit Faktor $-2$

## Punkt 3 – Sprosse und Merkmal
- orthogonalitaet-e1-k1-s0-v1: doppelt zu orthogonalitaet-e3-k1-s0-v1 (Gerade senkrecht zur Ebene, gleiche drei Optionen, gleiche Antwort) – in e1 durch ein anderes Paar ersetzen, z. B. „Zeige, dass $\vec n$ auf der Geraden $g$ senkrecht steht“ (zwei Richtungen)
- orthogonalitaet-e1-k1-s0-v3: doppelt zu orthogonalitaet-e3-k1-s0-v2 (Parameter für senkrechte Ebenen, gleiche Optionen, gleiche Antwort) – in e1 ein anderes Ebenenpaar-Beispiel ohne Parameter nehmen, z. B. „Untersuche, ob die Ebenen $E$ und $F$ senkrecht zueinander stehen“
- orthogonalitaet-e1-k3-s0-v1: Aufgabenstamm „Zeige, dass das Dreieck $ABC_t$ für jedes $t$ bei $A$ rechtwinklig ist.“ wortgleich in orthogonalitaet-e2-k1-s0-v2 – Stamm in einer der beiden Zeilen ändern (anderer Scheitel oder Kontext, etwa Geradenschar senkrecht zu einer festen Geraden)
- orthogonalitaet-e1-k4-s5-v3: Sprosse und Merkmal verlangen den Nachweis an allen drei Ecken, die Aufgabe prüft nur $B$ ($7 - 36 = -29$) – entweder alle drei Ecken verlangen (bei $A$: $(\sqrt7|6|0) \circ (0|12|0) = 72$, bei $C$: $(0|-12|0) \circ (\sqrt7|-6|0) = 72$) oder die Zeile einer Sprosse „an einer Ecke“ zuordnen
- orthogonalitaet-e1-k4-s5-v4: wie v3, nur Ecke $B$ ($5 - 6 = -1$) – alle drei Ecken verlangen (bei $A$: $(\sqrt5|2|0) \circ (0|5|0) = 10$, bei $C$: $(0|-5|0) \circ (\sqrt5|-3|0) = 15$)
- orthogonalitaet-e1-k5-s3-v1: Sprosse „Rechten Winkel und Kathetenlängen“, gefragt ist aber nur die Hypotenuse $|AC| = \sqrt{250}$ – die Katheten $|BA| = 13$ dm und $|BC| = 9$ dm erfragen (Hypotenuse höchstens zusätzlich)
- orthogonalitaet-e1-k5-s3-v3: wie v1, gefragt ist die Hypotenuse $|AC| = \sqrt{58}$ – Längen von Balken ($7$ m) und Stütze ($3$ m) erfragen
- orthogonalitaet-e2-k2-s3-v1: fast doppelt zu orthogonalitaet-e2-k1-s4-v3 (Quader $9 \times 12$ statt $12 \times 9$, beide $h = 15$ und $V = 1620$) – andere Grundmaße wählen, z. B. $8 \times 15$: $h = 17$ dm, $V = 2040$ dm³
- orthogonalitaet-e2-k2-s3-v2: passt nicht zur Sprosse (Quaderhöhe aus senkrechten Raumdiagonalen samt Volumen oder Oberfläche) – Zeltseile sind ein Parameter-Grundfall der Kette; durch eine Quader-Sachaufgabe ersetzen (z. B. Karton, Schrank mit senkrechten Diagonalstreben)
- orthogonalitaet-e2-k2-s3-v3: passt nicht zur Sprosse (kein Quader, keine Raumdiagonalen) – durch eine Quader-Sachaufgabe mit Oberfläche ersetzen
- orthogonalitaet-e3-k2-s3-v3: Sprosse „Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor“, die Aufgabe prüft Ebene gegen Ebene über das Skalarprodukt der Normalenvektoren – eine Gerade/Richtung gegen eine Ebene nehmen, z. B. eine Querstrebe in Richtung $(2 | -4 | 0)$ gegen die Glaswand $x - 2y = 4$
- orthogonalitaet-e4-k3-s3-v1: Sprosse „maximaler Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe“, die Aufgabe ist ein Punkt-Gerade-Abstand ohne Dreieck und Winkel – durch eine Blickwinkel- oder Spitzenwinkel-Sachaufgabe ersetzen (wie v2, mit eigenen Zahlen)
- orthogonalitaet-e4-k3-s3-v2: gleiche Daten wie orthogonalitaet-e4-k1-s2-v1 ($C(-3|0|2)$, $D(3|0|2)$, $F_k(0|k|12-2k)$, $k = 4$), nur eingekleidet – eigene Zahlen, z. B. $C(-2|0|1)$, $D(2|0|1)$, $F_k(0|k|10-2k)$ mit $0 < k \le 5$: $(0|k|9-2k) \circ (0|1|-2) = 5k - 18 = 0$, $k = 3{,}6$
- orthogonalitaet-e4-k3-s3-v3: passt nicht zur Sprosse (Punkt-Gerade-Abstand statt Spitzenwinkel) und hat dieselben Daten wie orthogonalitaet-e4-k1-s1-v4 ($P(4|0|1)$, $g$ mit Richtung $(2|2|1)$, $F(2|2|1)$, $\sqrt8$) – durch eine Spitzenwinkel-Sachaufgabe mit eigenen Zahlen ersetzen

## Punkt 4 – Schreibform
- orthogonalitaet-e2-k1-s5-v2: „$+ -1 \cdot -3$“, „$1x + 3y +0$“ ist keine korrekte Schreibweise – „$+ (-1) \cdot (-3) = x + 3y = 0$“
- orthogonalitaet-e2-k1-s5-v3: „$+ -2(y - 0)$“, „$3x + -2y -6$“ – „$- 2y + 0 \cdot 2 = 3x - 2y - 6 = 0$“
- orthogonalitaet-e4-k1-s1-v2: „$3 - 1\lambda$“ und „$\sqrt{25} \approx 5$“ (Wert ist exakt) – „$3 - \lambda = 0$“ und „$\sqrt{25} = 5$“
- orthogonalitaet-e4-k1-s1-v3: „$\sqrt{9} \approx 3$“ (Wert ist exakt) – „$\sqrt{9} = 3$“

## Punkt 5 – Ankreuzen
- orthogonalitaet-e1-k3-s0-v3: Zur Aufgabe „jede Gerade der Schar $g_a$ senkrecht zu $E$“ ist die richtige Option „für alle – das Skalarprodukt muss für jeden Wert null sein“; Gerade gegen Ebene prüft man aber über die Kollinearität mit dem Normalenvektor (e1-k1-s0-v1), die Option bestätigt damit das Kernfehlmuster des Eintrags – Aufgabenstamm auf zwei Richtungen ändern, z. B. „Begründe, dass jede Gerade der Schar $g_a$ senkrecht zur Geraden $h$ steht.“

## Punkt 6 – Fehler finden
- orthogonalitaet-e4-k3-s1-v1: Kims Aussage „Fläche am kleinsten, wenn $|RT_\lambda|$ am kleinsten“ ist im gleichschenkligen Fall richtig ($|RT_\lambda|^2 = |RM|^2 + |MT_\lambda|^2$ mit festem $|RM|$); die Aufgabe nennt die Gleichschenkligkeit nicht, dann aber ist die „richtige“ Höhe $|MT_\lambda|$ falsch (Höhe ist der Abstand zur Geraden $RS$) – Voraussetzung „jeder Punkt $T_\lambda$ hat von $R$ und $S$ denselben Abstand“ ergänzen und Kim das Muster wörtlich begehen lassen: „Kim setzt den Flächeninhalt als $\frac{1}{2} \cdot |RS| \cdot |RT_\lambda|$ an.“ (Endpunktabstand statt Höhe)

## Entscheidungen
- Doppelungen (Regel „Keine Aufgabe doppelt“) stehen unter Punkt 3 bei der Zeile, die geändert werden sollte; die Partnerzeile gilt als sauber.
- Fehler-finden-Zeilen, die die Punkte einer Grundfall- oder Sprossenzeile derselben Einheit übernehmen (e1-k5-s1-v1 bis v3, e2-k2-s1-v1 bis v3, e3-k2-s1-v1 und v3), sind nicht als Befund geführt: Die Aufgabe (Fehler benennen) ist eine andere, und „eigene Zahlen“ meint laut Regel Zahlen nicht aus dem Katalog.
- Varianten, deren Unterschiede dem Katalog folgen (Sprosse nennt mehrere Originale, z. B. e1-k4-s2 mit und ohne Oberflächenanhang, e3-k1-s3 mit und ohne Koordinatengleichung), sind nicht als Merkmalsabweichung geführt; geführt ist eine Abweichung nur, wenn die Aufgabe dem Sprossentext widerspricht.
- Mehrere ids in einer Zeile nur, wenn alle Varianten einer Sprosse gleich betroffen sind; sonst eine Zeile je id.

Sauber: 139 Zeilen ohne Befund
