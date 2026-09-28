# Zweitlesung flaecheninhalt-durch-integration

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 216
(zone 26, e1 36, e2 37, e3 39, e4 34, e5 44)

Prüfung: Alle 216 Zeilen einzeln gelesen (Skript-Ausgabe je Zeile mit
id, Sprosse, Merkmal, Aufgabe, Lösung, pruef, Grafik, Original). Von
den 159 Zeilen mit pruef wurden 137 Integrale, Stammfunktionen,
Schnittstellen, Parameterterme und Näherungswerte mit sympy
nachgerechnet (Skript im Scratchpad), die übrigen 22 – Nullstellen
der Zone, Dreiecks- und Trapezformeln, Rechteck-plus-Dreieck-
Gleichungen – im Kopf; die Rundungen der Dezimalwerte wurden
numerisch geprüft. Die 27 Ankreuzzeilen: je Zeile die Optionen gegen
die Lösung gehalten (genau eine trifft wortgleich, die anderen sind
falsch), bei den Bildzeilen die Lage der Graphen aus dem Term
bestimmt. Die 16 Fehler-finden-Zeilen: die vorgelegte Rechnung
nachvollzogen (der Fehler ist wirklich falsch), die Richtigrechnung
nachgerechnet, das Muster gegen „Typische Fehler“ der Mappe
gehalten. Die 15 Begründen-Zeilen inhaltlich gelesen. Nebenprüfung
per Skript: $-Zeichen, Klammern und geschweifte Klammern paarig,
keine doppelte Aufgabe, keine doppelte id, pflicht-Schlüssel nur bei
hoehe pflicht; Grafikbereiche gegen die Funktionswerte an den
Intervallgrenzen geprüft; die 14 Originale der Prüfungshöhe in der
Mappe nachgelesen (Verfremdung). bank-pruef.py v0.5: 0 Abweichungen,
0 Warnungen in allen sechs Dateien.

## Befunde

Kein Rechenfehler, keine falsche Lösung, keine falsche Ankreuzoption.
Alle Befunde sind Zweifelsfälle:

e1-k1-s5-v1 fraglich: $f(x) = -0{,}5x^2 + 8$ ist die am Ursprung
gespiegelte Kastenfunktion $\frac12 x^2 - 8$ (Merkkasten Einheit 1):
gleiche Nullstellen $\pm 4$, gleicher Betrag $\frac{128}{3}$ – die
Sperre trifft dem Wortlaut nach nicht, dem Sinn nach schon.
Vorschlag: andere Zahlen, etwa $-0{,}5x^2 + 4{,}5$ (Nullstellen
$\pm 3$, Fläche $18$, Wand $= 4{,}5 - 2 = 2{,}5\,\text{m}^2$).

e2-k2-s1-v3 fraglich: dieselbe gespiegelte Kastenfunktion
$-0{,}5x^2 + 8$ mit $\pm 4$ und $\frac{128}{3}$ – Vorschlag: andere
Zahlen, etwa $-0{,}5x^2 + 4{,}5$ mit $g(x) = 2 - 0{,}5x^2$ (dann
$18 - \frac{16}{3} = \frac{38}{3}$).

e1-k2-s3-v2 fraglich: Typname der Anwendung nennt „senkrechte
Gerade“ und „Maßstab“; die Werbefläche hat Nullstellen als Grenzen
und den Maßstab $1$ – Vorschlag: eine senkrechte Grenze (etwa nur
der Bogen von $x = 0$ bis $x = 4$) und einen echten Maßstab (eine
Einheit $= 0{,}5$ m).

e1-k2-s3-v3 fraglich: wie v2 – der Graben läuft von Nullstelle zu
Nullstelle, Maßstab $1$ – Vorschlag: Grenze $x = 3$ als Böschungs-
kante oder Maßstab $2$ m je Einheit (dann $\frac{8}{3} \cdot 4$).

e2-k1-s7-v4 fraglich: die Schnittstellen $2$ und $6$ sind die des
Originals 2023-C-2d, und $g = -f + \text{const}$ ist derselbe Aufbau
(im Original $f = -0{,}15x^2 + 1{,}2x - 0{,}6$, $g = 0{,}15x^2 -
1{,}2x + 3$); nur die Vorfaktoren sind anders – Vorschlag: andere
Schnittstellen, etwa $1$ und $5$ mit $f = -0{,}25x^2 + 1{,}5x +
0{,}5$, $g = 0{,}25x^2 - 1{,}5x + 3$ (Fläche $\frac{16}{3}$ bleibt).

e3-k1-s1-v3 fraglich: „Fläche zwischen dem Graphen von $f(x) =
0{,}25x^2$, der y-Achse und der Geraden $y = 4$“ – links und rechts
der y-Achse liegt je ein solches Stück (je $\frac{32}{3}$); die
Lösung nimmt eines, beide zusammen wären $\frac{64}{3}$ – Vorschlag:
„im ersten Quadranten“ ergänzen.

e3-k1-s3-v3 fraglich: Maßstab „eine Längeneinheit entspricht $5$ cm,
eine Flächeneinheit $25\,\text{cm}^2$“ ist das Zahlenpaar des
Kastenbeispiels (fünf Meter, fünfundzwanzig Quadratmeter) in
anderer Einheit – Vorschlag: $4$ cm ($16\,\text{cm}^2$, Schnitt
$124{,}8\,\text{cm}^2$).

e4-k1-s5-v3 fraglich: merkmal sagt „ohne Rechnung: Stetigkeit und
Monotonie“, die Aufgabe rechnet mit der Stammfunktion und einer
Schranke ($1 - e^{-b} < 1$); der Typ „Existenz … über die
Stammfunktion begründen“ steht zwar in der Mappe, die Variante
unterscheidet sich aber nicht nur in Zahlen und Kontext von v1/v2 –
Vorschlag: merkmal um „oder Schranke aus der Stammfunktion“
erweitern, sonst so lassen.

e4-k1-s6-v2 fraglich: die Abbildung endet bei xmax $= 3$, das
Intervall von $k$ bis $k + 4$ reicht für $k > -1$ bis $x = 4$ (bei
$k = 0$ liegt ein Viertel außerhalb); die Lösung $k = -2$ ist im
Bild vollständig sichtbar, der Ausschluss der übrigen $k$ nicht –
Vorschlag: $-3 \le k \le -1$ statt $-3 \le k \le 0$, oder xmax $= 4$
mit ymin $= -8$ ($f(4) = -7$).

e4-k2-s3-v2 fraglich: Typname „Senkrechte Gerade zur Halbierung
über den Flächenterm“, die Lösung kommt ohne Flächenterm über die
Symmetrie zu $t = 4$ – die Anwendung übt nicht den Handgriff des
Typs. Vorschlag: unsymmetrische Rate, etwa $r(t) = 6 - 0{,}75t$ auf
$0 \le t \le 8$ (Gesamt $24$, Hälfte bei $6t - 0{,}375t^2 = 12$,
$t = 8 - \sqrt{32} \approx 2{,}34$).

e5-k1-s0-v1, e5-k1-s0-v2, e5-k1-s0-v3, e5-k1-s0-v4 fraglich: die
Aufgabe stellt zwei Fragen („Vorzeichen des Werts? Ist der Wert der
Flächeninhalt?“), Ankreuzoptionen gibt es nur für die erste; die
zweite hat weder Option noch Antwortfeld, obwohl der Katalog beides
verlangt („ob der Wert positiv, negativ oder null ist und ob er der
Fläche entspricht“) – Vorschlag: antwort „Flächeninhalt? \janein“
oder zwei Kreuzreihen.

e5-k1-s4-v3 fraglich: merkmal „orientierte Integrale vergleichen“,
die Variante vergleicht $f(4)$ und $f(1)$ über das Vorzeichen von
$f'$ (Hauptsatz); der Typ „Integrale der Ableitung … vergleichen“
steht in der Mappe, aber v3 fragt nicht nach Integralen – Vorschlag:
Optionen als Integrale fassen („Integral von $1$ bis $4$ über $f'$
ist negativ/null/positiv“) oder merkmal erweitern.

Sauber: 201 Zeilen ohne Befund

(216 minus 15 Zeilen mit Befund; 12 Befundabsätze, der Absatz zu
e5-k1-s0 nennt vier ids, jede zählt einmal.)

## Abgleich

Erstlesung: gegenlese.md vom 2026-09-27 (Claude Code, Web-Sitzung),
216 Zeilen, 2 Befunde, 0 Korrekturen; auch dort kein Rechenfehler.

- Beide Leser: keiner.
- Nur Zweitleser: e1-k1-s5-v1 und e2-k2-s1-v3 (gespiegelte
  Kastenfunktion), e1-k2-s3-v2 und e1-k2-s3-v3 (Typname senkrechte
  Gerade/Maßstab), e2-k1-s7-v4 (Schnittstellen wie im Original),
  e3-k1-s1-v3 (zwei spiegelgleiche Flächen), e3-k1-s3-v3 (Maßstab
  5/25 wie im Kasten), e4-k1-s5-v3 (Merkmal „ohne Rechnung“),
  e4-k1-s6-v2 (Abbildung endet vor dem Intervall), e4-k2-s3-v2
  (Halbierung ohne Flächenterm), e5-k1-s0-v1 bis v4 (zweite Frage
  ohne Antwortfeld), e5-k1-s4-v3 (Merkmal Integrale vergleichen).
- Nur Erstleser:
  - e3-k2-s4-v1 (Lage des Rechtecks „plus 2·3“ nicht festgelegt):
    Zustimmung – der Term nennt nur Breite und Höhe, die
    Lösungsgrafik setzt das Rechteck rechts an $x = 2$ mit Höhe
    $f(2) = 3$, das ist die naheliegende, aber nicht die einzige
    Lesart; der Vorschlag „Integral von $2$ bis $4$ über $3$“ legt
    es fest. Ich hatte es übersehen.
  - e4-k2-s1-v2 („falsche“ Antwort rechnerisch richtig, nur der
    Operator verletzt): teils – ich hatte den Punkt geprüft und
    verworfen, weil die Mappe genau dieses Muster als typischen
    Fehler führt (Zeile 97: „ein konkretes Beispiel ausgerechnet,
    wo das Argument am Graphen verlangt war“; Typen Einheit 4:
    „ein konkretes Beispiel ausgerechnet, wo eine Existenzbegründung
    verlangt war“), die Zeile also dem Katalog folgt; der Erstleser
    hat recht, dass der Fehler nur im Operator liegt und die Zeile
    dadurch schwächer trägt als v1 und v3. Sein Vorschlag „genau ein
    b“ macht den Fehler inhaltlich, überschneidet sich dann aber mit
    v3 (Eindeutigkeit fehlt); ich würde die Zeile lassen und den
    Operatorbezug in der Lösung so lassen, wie er steht.

Zahlen: Zweitleser 12 Befunde, Erstleser 2, gemeinsam 0, nur
Zweitleser 12.
Gezählt wurden Befundabsätze, nicht ids (der Absatz zu e5-k1-s0
nennt vier ids); „gemeinsam“ heißt dieselbe id mit demselben
Stichwort, alle meine Befunde sind als fraglich gekennzeichnet.
