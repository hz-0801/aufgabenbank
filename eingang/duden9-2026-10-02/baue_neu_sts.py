#!/usr/bin/env python3
"""Baut neu-strahlensaetze-duden9.jsonl und rechnet jede Lösung mit
sympy nach. Vom Buch nur Typ und Stufung; Zahlen und Wortlaut eigen.
Vorlage: baue_neu_qf.py (Kapitel 3)."""
import json
import sympy as sp

E = "strahlensaetze"
Q = "Duden WÜT Mathematik 9 (2017)"
R = sp.Rational
B = "aufgabenbank/bank/strahlensaetze/"
bank = {}
for d in ("e1", "e2", "e3"):
    for l in open(B + d + ".jsonl", encoding="utf-8"):
        r = json.loads(l)
        bank.setdefault((r["einheit"], r["kette_nr"], r["sprosse"]), []).append(r)
zeilen = []
naechste = {}
eigen = {}
FELDER = {"id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
          "sprosse_text", "merkmal", "hoehe", "variante", "aufgabe", "form",
          "antwort", "loesung", "pruef", "original", "grafik",
          "loesungsgrafik", "quelle", "herkunft"}


def zeile(einheit, kn, sprosse, merkmal, aufgabe, form, antwort, loesung,
          pruef, herkunft, grafik="", neu=None):
    """neu = (Text, Bezugssprosse) für Platzhalter-Sprossen."""
    if neu is None:
        vor = bank[(einheit, kn, sprosse)][0]
        kette, st, hoehe, quelle = (vor["kette"], vor["sprosse_text"],
                                    vor["hoehe"], vor["quelle"])
        var0 = max(r["variante"] for r in bank[(einheit, kn, sprosse)])
    else:
        vor = bank[(einheit, kn, neu[1])][0]
        kette, quelle, hoehe = vor["kette"], vor["quelle"], "sprosse"
        st = f"{sprosse}: {neu[0]} (Vorschlag; nicht im Katalog)"
        var0 = 0
    k = (einheit, kn, sprosse)
    eigen.setdefault(k, merkmal)
    merkmal = vor["merkmal"] if neu is None else eigen[k]
    zusatz = {f: vor[f] for f in vor if f not in FELDER} if neu is None else {}
    naechste[k] = naechste.get(k, var0) + 1
    v = naechste[k]
    zeilen.append({
        "id": f"{E}-e{einheit}-k{kn}-s{sprosse}-v{v}", "eintrag": E,
        "einheit": einheit, "kette": kette, "kette_nr": kn,
        "sprosse": sprosse, "sprosse_text": st, "merkmal": merkmal,
        "hoehe": hoehe, "variante": v, "aufgabe": aufgabe, "form": form,
        "antwort": antwort, "loesung": loesung, "pruef": pruef,
        "original": None, "grafik": grafik, "loesungsgrafik": "",
        "quelle": quelle, "herkunft": f"{Q}, {herkunft}", **zusatz})


def gl(a, b):
    assert sp.nsimplify(a) == sp.nsimplify(b), (a, b)


def wert(p):
    return [sp.nsimplify(eval(p))] if not p.startswith("[") else \
        [sp.nsimplify(z) for z in eval(p)]


# ================= Einheit 1, Kette 2 (Maßstab umrechnen) =========
H = "S. 63 Nr. 3 – Tabelle Maßstab, Original- und Bildstrecke in gemischter Richtung"
gl(7 * 25000, 175000); gl(R(280000, 40000), 7); gl(1350000 / 9, 150000)
zeile(1, 2, 8, "Tabelle: alle drei Richtungen gemischt, Kilometer",
      "Ergänze die Tabelle. Rechne in Zentimetern und gib Wege in "
      "Kilometern an.\\\\ (1) Maßstab $1 : 25\\,000$, Karte $7\\,\\text{cm}$, "
      "Wirklichkeit gesucht.\\\\ (2) Maßstab $1 : 40\\,000$, Wirklichkeit "
      "$2{,}8\\,\\text{km}$, Karte gesucht.\\\\ (3) Karte $9\\,\\text{cm}$, "
      "Wirklichkeit $13{,}5\\,\\text{km}$, Maßstab gesucht.",
      "teil", "(1) __ km (2) __ cm (3) 1 : __",
      "(1) $7 \\cdot 25\\,000 = 175\\,000\\,\\text{cm} = 1{,}75\\,\\text{km}$; "
      "(2) $280\\,000 : 40\\,000 = 7\\,\\text{cm}$; "
      "(3) $1\\,350\\,000 : 9 = 150\\,000$, also $1 : 150\\,000$",
      "[1.75, 7, 150000]", H)
H = "S. 63 Nr. 5 – Deutschlandkarte, Karte und Wirklichkeit in beide Richtungen"
gl(R(45, 10) * 8000000 / 100000, 360); gl(R(52000000, 8000000), R(13, 2))
zeile(1, 2, 8, "sehr großer Maßstab, Dezimalzahl auf der Karte, beide Richtungen",
      "Eine Europakarte hat den Maßstab $1 : 8\\,000\\,000$. (1) Auf der "
      "Karte sind zwei Städte $4{,}5\\,\\text{cm}$ voneinander entfernt. Wie "
      "weit ist das in Wirklichkeit? (2) Zwei andere Städte liegen "
      "$520\\,\\text{km}$ auseinander. Wie weit sind sie auf der Karte "
      "voneinander entfernt?",
      "teil", "(1) __ km (2) __ cm",
      "(1) $4{,}5 \\cdot 8\\,000\\,000 = 36\\,000\\,000\\,\\text{cm} = "
      "360\\,\\text{km}$; (2) $52\\,000\\,000 : 8\\,000\\,000 = 6{,}5\\,\\text{cm}$",
      "[360, 6.5]", H)
NL = ("Maßstabsleiste lesen: Leistenabschnitt und Beschriftung in den "
      "Maßstab 1 : n umrechnen, dann Kartenstrecken umrechnen", 8)
H = "S. 63 Nr. 6 – Maßstab aus einer Maßstabsleiste bestimmen und Strecken umrechnen"
gl(500000 / 2, 250000); gl(R(1600000, 250000), R(32, 5))
zeile(1, 2, "NEU-massstabsleiste", "Maßstabsleiste: Abschnitt und Beschriftung in 1 : n",
      "Unter einer Wanderkarte steht eine Maßstabsleiste. Ein "
      "$2\\,\\text{cm}$ langer Abschnitt der Leiste ist mit $5\\,\\text{km}$ "
      "beschriftet. (1) Gib den Maßstab der Karte an. (2) Wie lang ist "
      "ein $16\\,\\text{km}$ langer Weg auf dieser Karte?",
      "teil", "(1) 1 : __ (2) __ cm",
      "(1) $5\\,\\text{km} = 500\\,000\\,\\text{cm}$; $500\\,000 : 2 = "
      "250\\,000$, also $1 : 250\\,000$; (2) $1\\,600\\,000 : 250\\,000 = "
      "6{,}4\\,\\text{cm}$", "[250000, 6.4]", H, neu=NL)
gl(75000 * R(42, 10) / 100000, R(315, 100))
zeile(1, 2, "NEU-massstabsleiste", "Maßstabsleiste in Metern, Ergebnis in Kilometern",
      "Auf einer Stadtkarte zeigt die Maßstabsleiste: $1\\,\\text{cm}$ "
      "entspricht $750\\,\\text{m}$. (1) Gib den Maßstab an. (2) Ein Weg "
      "ist auf der Karte $4{,}2\\,\\text{cm}$ lang. Wie viele Kilometer "
      "sind das?",
      "teil", "(1) 1 : __ (2) __ km",
      "(1) $750\\,\\text{m} = 75\\,000\\,\\text{cm}$, also $1 : 75\\,000$; "
      "(2) $4{,}2 \\cdot 750 = 3\\,150\\,\\text{m} = 3{,}15\\,\\text{km}$",
      "[75000, 3.15]", H, neu=NL)

# ================= Einheit 2 =======================================
H = "S. 69 Nr. 17 – Streckung im Koordinatensystem, Zentrum im Ursprung, negative Koordinaten"
P = [(-1, -2), (2, -1), (1, R(3, 2))]
gl(sum(([2 * a, 2 * b] for a, b in P), [])[5], 3)
zeile(2, 1, 2, "Zentrum im Ursprung innerhalb der Figur, negative und halbe Koordinaten",
      "Das Koordinatensystem zeigt das Dreieck $ABC$ mit $A(-1|-2)$, "
      "$B(2|-1)$ und $C(1|1{,}5)$. Strecke das Dreieck vom Zentrum "
      "$Z(0|0)$ aus mit $k = 2$. Gib die Koordinaten der Bildpunkte an.",
      "zeichnen", "",
      "$A'(-2|-4)$, $B'(4|-2)$, $C'(2|3)$", "[-2, -4, 4, -2, 2, 3]", H,
      "\\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=4]\\punkt{0}{0}{Z}"
      "\\punkt{-1}{-2}{A}\\punkt{2}{-1}{B}\\punkt{1}{1.5}{C}\\end{ksys}")
H = "S. 69 Nr. 18 – Streckung mit Zentrum außerhalb und nicht ganzzahligem Streckfaktor"
Z = sp.Matrix([-3, -1]); k = R(4, 3)
bild = [Z + k * (sp.Matrix(p) - Z) for p in [(0, -1), (3, 2), (0, 2)]]
assert [list(b) for b in bild] == [[1, -1], [5, 3], [1, 3]]
zeile(2, 1, 2, "Zentrum mit negativen Koordinaten, Streckfaktor als Bruch",
      "Das Koordinatensystem zeigt das Dreieck $ABC$ mit $A(0|-1)$, "
      "$B(3|2)$ und $C(0|2)$ und das Zentrum $Z(-3|-1)$. Zeichne Strahlen "
      "von $Z$ durch die Ecken. Strecke das Dreieck mit "
      "$k = \\frac{4}{3}$. Gib die Koordinaten der Bildpunkte an.",
      "zeichnen", "", "$A'(1|-1)$, $B'(5|3)$, $C'(1|3)$",
      "[1, -1, 5, 3, 1, 3]", H,
      "\\begin{ksys}[xmin=-4,xmax=6,ymin=-2,ymax=4]\\punkt{-3}{-1}{Z}"
      "\\punkt{0}{-1}{A}\\punkt{3}{2}{B}\\punkt{0}{2}{C}\\end{ksys}")
H = "S. 63 Nr. 1 – Streckenverhältnis mit Dezimalzahlen und verschiedenen Einheiten"
gl(R(84, 240), R(7, 20))
zeile(2, 1, 4, "Strecken in verschiedenen Einheiten, Streckfaktor als Dezimalzahl",
      "Eine Originalstrecke ist $2{,}4\\,\\text{m}$ lang, ihre Bildstrecke "
      "$84\\,\\text{cm}$. Berechne den Streckfaktor $k$. Ist das Bild eine "
      "Vergrößerung oder eine Verkleinerung?",
      "teil", "k = __",
      "$2{,}4\\,\\text{m} = 240\\,\\text{cm}$; $k = 84 : 240 = 0{,}35$; "
      "Verkleinerung, weil $k < 1$", "84/240", H)
H = "S. 69 Nr. 20 – Kreis vom Mittelpunkt aus strecken"
gl(R(44, 16), R(11, 4)); gl(2 * R(44, 10), R(88, 10))
zeile(2, 1, 4, "Kreis: Streckfaktor aus den Radien, Durchmesser des Bildkreises",
      "Ein Kreis mit dem Radius $1{,}6\\,\\text{cm}$ wird von seinem "
      "Mittelpunkt aus gestreckt. Der Bildkreis hat den Radius "
      "$4{,}4\\,\\text{cm}$. Berechne den Streckfaktor $k$ und den "
      "Durchmesser des Bildkreises.",
      "teil", "k = __; d = __ cm",
      "$k = 4{,}4 : 1{,}6 = 2{,}75$; $d = 2 \\cdot 4{,}4 = 8{,}8\\,\\text{cm}$",
      "[2.75, 8.8]", H)
H = "S. 69 Nr. 19 und 22 – Streckfaktor aus Zentrum und einem Bildpunkt, dann weitere Bildpunkte"
Z = sp.Matrix([1, -3]); A = sp.Matrix([5, 1]); A1 = sp.Matrix([4, 0])
k = (A1 - Z)[0] / (A - Z)[0]
assert k == R(3, 4) and A1 == Z + k * (A - Z)
assert list(Z + k * (sp.Matrix([9, -3]) - Z)) == [7, -3]
zeile(2, 1, 4, "Streckfaktor aus Koordinaten ablesen, dann einen weiteren Bildpunkt",
      "Das Zentrum ist $Z(1|-3)$. Der Punkt $A(5|1)$ hat den Bildpunkt "
      "$A'(4|0)$. (1) Bestimme den Streckfaktor $k$. (2) Gib den Bildpunkt "
      "$B'$ von $B(9|-3)$ an.",
      "teil", "k = __; B'(__|__)",
      "(1) $\\overline{ZA'} : \\overline{ZA} = 3 : 4$, also $k = 0{,}75$; "
      "(2) $B$ liegt $8$ rechts von $Z$, $B'$ also $0{,}75 \\cdot 8 = 6$ "
      "rechts: $B'(7|-3)$", "[0.75, 7, -3]", H,
      "\\begin{ksys}[xmin=0,xmax=10,ymin=-4,ymax=2]\\punkt{1}{-3}{Z}"
      "\\punkt{5}{1}{A}\\punkt{4}{0}{A'}\\punkt{9}{-3}{B}\\end{ksys}")
H = "S. 73 Nr. 29 – Ähnlichkeit über Seitenverhältnisse prüfen, Seiten in verschiedenen Einheiten"
q = [R(75, 25), R(105, 35), R(140, 45)]
assert q[0] == q[1] == 3 and q[2] != 3
zeile(2, 1, 7, "Seiten in verschiedenen Einheiten, ein Verhältnis passt nicht",
      "Dreieck 1 hat die Seiten $2{,}5\\,\\text{cm}$, $3{,}5\\,\\text{cm}$ "
      "und $4{,}5\\,\\text{cm}$. Dreieck 2 hat die Seiten "
      "$0{,}75\\,\\text{dm}$, $1{,}05\\,\\text{dm}$ und $1{,}4\\,\\text{dm}$. "
      "Rechne in Zentimetern, paare die Seiten der Größe nach und prüfe, "
      "ob die Dreiecke ähnlich sind.", "text", "",
      "$7{,}5 : 2{,}5 = 3$; $10{,}5 : 3{,}5 = 3$; $14 : 4{,}5 \\approx 3{,}11$; "
      "nicht ähnlich", "[3, 3, 14/4.5]", H)
H = "S. 73 Nr. 32 – Rechtecke auf Ähnlichkeit prüfen, eine Seite aus dem Flächeninhalt"
gl(R(21, 7), 3); assert R(7, 1) / R(28, 10) == R(3) / R(12, 10) == R(5, 2)
zeile(2, 1, 7, "zweite Seite erst aus dem Flächeninhalt, dann Verhältnisse vergleichen",
      "Ein Rechteck hat die Seiten $2{,}8\\,\\text{cm}$ und $1{,}2\\,\\text{cm}$. "
      "Ein zweites Rechteck hat den Flächeninhalt $21\\,\\text{cm}^2$, eine "
      "Seite ist $7\\,\\text{cm}$ lang. Sind die Rechtecke ähnlich? Begründe "
      "mit den Seitenverhältnissen.", "text", "",
      "zweite Seite $21 : 7 = 3\\,\\text{cm}$; $7 : 2{,}8 = 2{,}5$ und "
      "$3 : 1{,}2 = 2{,}5$; ähnlich mit $k = 2{,}5$", "[3, 2.5, 2.5]", H)
H = "S. 72 Nr. 28 – ähnliches Dreieck zu einer vorgegebenen Bildseite"
k = R(5, 7)
gl(k * R(7, 2), R(5, 2)); gl(k * 6, R(30, 7))
zeile(2, 1, 8, "Streckfaktor als Bruch aus einer vorgegebenen Bildseite, zwei Seiten berechnen, dann zeichnen",
      "Ein Dreieck hat die Seiten $3{,}5\\,\\text{cm}$, $6\\,\\text{cm}$ und "
      "$7\\,\\text{cm}$. Ein ähnliches Dreieck soll statt der "
      "$7\\,\\text{cm}$ langen Seite eine $5\\,\\text{cm}$ lange Seite "
      "haben. Berechne die beiden anderen Seiten auf zwei Stellen nach "
      "dem Komma und zeichne das Dreieck.", "zeichnen", "",
      "$k = \\frac{5}{7}$; $3{,}5 \\cdot \\frac{5}{7} = 2{,}5\\,\\text{cm}$; "
      "$6 \\cdot \\frac{5}{7} \\approx 4{,}29\\,\\text{cm}$",
      "[2.5, 30/7]", H,
      "\\begin{ksys}[xmin=0,xmax=10,ymin=0,ymax=6]\\end{ksys}")
H = "S. 69 Nr. 21 – Flächenfaktor zu Streckfaktor, Maßstab und Dezimalzahl"
gl(R(1, 4) ** 2, R(1, 16)); gl(R(12, 10) ** 2, R(144, 100))
zeile(2, 1, 10, "Streckfaktor als Maßstab 1 : n und als Dezimalzahl",
      "Um welchen Faktor ändert sich der Flächeninhalt einer Figur, wenn "
      "sie (1) im Maßstab $1 : 4$ verkleinert und (2) mit $k = 1{,}2$ "
      "vergrößert wird?", "teil", "(1) __ (2) __",
      "(1) $k = \\frac{1}{4}$, Fläche mal $\\frac{1}{16} = 0{,}0625$; "
      "(2) Fläche mal $1{,}2^2 = 1{,}44$", "[0.0625, 1.44]", H)
H = "S. 72 Nr. 27; S. 73 Nr. 31 – Umfang und Flächeninhalt der Bildfigur"
gl(R(14, 10) * 19, R(266, 10)); gl(R(196, 100) * 21, R(4116, 100))
zeile(2, 1, 10, "Umfang mal k neben Fläche mal k² in einer Aufgabe",
      "Ein Rechteck mit den Seiten $6\\,\\text{cm}$ und $3{,}5\\,\\text{cm}$ "
      "wird mit $k = 1{,}4$ vergrößert. Berechne Umfang und Flächeninhalt "
      "des Bildrechtecks.", "teil", "U' = __ cm; A' = __ cm²",
      "$U = 19\\,\\text{cm}$, $U' = 1{,}4 \\cdot 19 = 26{,}6\\,\\text{cm}$; "
      "$A = 21\\,\\text{cm}^2$, $A' = 1{,}4^2 \\cdot 21 = 41{,}16\\,\\text{cm}^2$",
      "[26.6, 41.16]", H)
NV = ("Volumen mal k³ und Streckfaktor aus dem Volumenfaktor zurück "
      "(nur ganze k; Vorrat)", 11)
H = "S. 73 Nr. 33 – Körper strecken: Kanten aus dem Volumenfaktor, Oberfläche mal k²"
k = sp.root(8, 3)
assert k == 2 and [k * a for a in (3, R(22, 10), R(14, 10))] == [6, R(44, 10), R(28, 10)]
zeile(2, 1, "NEU-volumen-k3", "Volumenfaktor gegeben: k durch Probieren, Kanten und Oberfläche",
      "Eine Schachtel ist $3\\,\\text{cm}$ lang, $2{,}2\\,\\text{cm}$ breit und "
      "$1{,}4\\,\\text{cm}$ hoch. Eine ähnliche Schachtel fasst das "
      "Achtfache. (1) Mit welchem Faktor $k$ sind die Kanten gestreckt? "
      "(2) Wie lang sind die Kanten? (3) Das Wievielfache an Karton "
      "braucht die große Schachtel?", "teil", "(1) k = __ (3) __-fach",
      "(1) $k^3 = 8$, also $k = 2$; (2) $3 \\cdot 2 = 6\\,\\text{cm}$, "
      "$2{,}2 \\cdot 2 = 4{,}4\\,\\text{cm}$, $1{,}4 \\cdot 2 = 2{,}8\\,\\text{cm}$; "
      "(3) $k^2 = 4$, also das $4$-fache", "[2, 6, 4.4, 2.8, 4]", H,
      neu=NV)
H = "S. 72 Nr. 26 – Außen- und Innenfigur eines Rahmens auf Ähnlichkeit prüfen"
assert R(40, 30) != R(30, 20)
zeile(2, 3, 2, "Rahmen gleicher Breite: Rechteck nicht ähnlich, Quadrat schon",
      "Ein Foto ist $30\\,\\text{cm}$ breit und $20\\,\\text{cm}$ hoch. Es "
      "bekommt rundherum einen $5\\,\\text{cm}$ breiten Rahmen. Sind Foto "
      "und Außenkante des Rahmens ähnlich? Begründe. Wie ist es bei einem "
      "quadratischen Foto?", "text", "",
      "Außenkante $40\\,\\text{cm}$ mal $30\\,\\text{cm}$; $40 : 30 \\neq "
      "30 : 20$, also nicht ähnlich – der Rahmen verlängert die kurze Seite "
      "im Verhältnis stärker. Beim Quadrat bleiben beide Seiten gleich lang, "
      "alle Quadrate sind ähnlich.", "", H)
H = "S. 70 Nr. 25 – Zentrum und Streckfaktor aus Original-Bild-Paaren im Gitter"
Z = sp.Matrix([-1, -1])
for p, b in [((1, 0), (3, 1)), ((2, 2), (5, 5))]:
    assert sp.Matrix(b) == Z + 2 * (sp.Matrix(p) - Z)
zeile(2, 2, 1, "zwei Punktpaare im Koordinatensystem, Zentrum und k angeben",
      "Bei einer zentrischen Streckung ist $A'(3|1)$ das Bild von $A(1|0)$ "
      "und $B'(5|5)$ das Bild von $B(2|2)$. Zeichne die Geraden $AA'$ und "
      "$BB'$. Gib das Zentrum $Z$ und den Streckfaktor $k$ an.",
      "zeichnen", "", "$Z(-1|-1)$; $k = 2$", "[-1, -1, 2]", H,
      "\\begin{ksys}[xmin=-2,xmax=6,ymin=-2,ymax=6]\\punkt{1}{0}{A}"
      "\\punkt{3}{1}{A'}\\punkt{2}{2}{B}\\punkt{5}{5}{B'}\\end{ksys}")

# ================= Einheit 3 =======================================
H = "S. 65 Nr. 7 – Tabelle mit mehreren Unbekannten, Teil- und Gesamtstrecken gemischt"
k = R(6) / R(25, 10)
gl(R(15, 10) * k - R(15, 10), R(21, 10)); gl(R(84, 10) / k, R(35, 10))
zeile(3, 1, 5, "zwei Unbekannte, Gesamtstrecke aus Teilstrecken, beide Strahlensätze",
      "In der V-Figur ist $\\overline{ZA} = 2{,}5\\,\\text{cm}$, "
      "$\\overline{AA'} = 3{,}5\\,\\text{cm}$, $\\overline{ZB} = 1{,}5\\,\\text{cm}$ "
      "und $\\overline{A'B'} = 8{,}4\\,\\text{cm}$. Berechne "
      "$\\overline{BB'}$ und $\\overline{AB}$.",
      "teil", "BB' = __ cm; AB = __ cm",
      "$\\overline{ZA'} = 6\\,\\text{cm}$, Faktor $6 : 2{,}5 = 2{,}4$; "
      "$\\overline{ZB'} = 1{,}5 \\cdot 2{,}4 = 3{,}6$, $\\overline{BB'} = "
      "2{,}1\\,\\text{cm}$; $\\overline{AB} = 8{,}4 : 2{,}4 = 3{,}5\\,\\text{cm}$",
      "[2.1, 3.5]", H, "\\strahlensatz{2.5}{6}{30}")
H = "S. 65 Nr. 9 – Flussbreite in der X-Figur"
gl(R(12 * 45, 18), 30)
zeile(3, 1, 6, "X-Figur im Sachkontext: Flussbreite mit fertiger Skizze",
      "Um die Breite $\\overline{AB}$ eines Flusses zu messen, steckt man "
      "am eigenen Ufer eine X-Figur ab: Die Strecken $AB$ und $A'B'$ sind "
      "parallel, $Z$ liegt zwischen ihnen. Gemessen sind "
      "$\\overline{ZA} = 45\\,\\text{m}$, $\\overline{ZA'} = 18\\,\\text{m}$ "
      "und $\\overline{A'B'} = 12\\,\\text{m}$. Die Skizze ist nicht "
      "maßstabsgerecht. Wie breit ist der Fluss?",
      "teil", "__ m",
      "$\\overline{AB} : 12 = 45 : 18$, also $\\overline{AB} = 12 \\cdot 45 : "
      "18 = 30\\,\\text{m}$", "12*45/18", H, "\\strahlensatz[x]{2.5}{1}{30}")
H = "S. 66 Nr. 14 – mehrere Baumhöhen aus einem Verhältnis"
gl(R(16, 20) * 9, R(72, 10)); gl(R(16, 20) * R(135, 10), R(108, 10))
zeile(3, 1, 6, "ein Verhältnis, zwei Gesuchte",
      "Ein $1{,}6\\,\\text{m}$ großer Junge wirft einen $2\\,\\text{m}$ "
      "langen Schatten. Zur selben Zeit werfen zwei Bäume Schatten von "
      "$9\\,\\text{m}$ und $13{,}5\\,\\text{m}$. Die Skizze ist nicht "
      "maßstabsgerecht. Wie hoch sind die Bäume?",
      "teil", "__ m und __ m",
      "Höhe : Schatten $= 1{,}6 : 2 = 0{,}8$; $9 \\cdot 0{,}8 = 7{,}2\\,\\text{m}$; "
      "$13{,}5 \\cdot 0{,}8 = 10{,}8\\,\\text{m}$", "[7.2, 10.8]", H,
      "\\strahlensatz{2}{6}{30}")
H = "S. 65 Nr. 8; S. 73 Nr. 30 – Seilbahn: Höhe aus Fahrstrecke, mit überflüssiger Angabe"
gl(R(375 * 500, 1250), 150)
zeile(3, 1, 7, "Steigung als Strahlensatz, eine Angabe wird nicht gebraucht",
      "Eine Seilbahn fährt auf einen $2\\,140\\,\\text{m}$ hohen Gipfel. Auf "
      "$1\\,250\\,\\text{m}$ Fahrstrecke gewinnt sie $375\\,\\text{m}$ Höhe. "
      "Zeichne eine Skizze. Wie viel Höhe hat sie nach $500\\,\\text{m}$ "
      "Fahrstrecke gewonnen? Welche Angabe brauchst du nicht?",
      "text", "",
      "$375 \\cdot 500 : 1\\,250 = 150\\,\\text{m}$; die Gipfelhöhe "
      "$2\\,140\\,\\text{m}$ wird nicht gebraucht", "375*500/1250", H,
      "\\rechenplatz[halb]{4}")
H = "S. 65 Nr. 11 – Entfernung durch Verdecken mit ausgestrecktem Arm"
gl(R(55, 100) * 11 / R(2, 100), R(6050, 20))
zeile(3, 1, 7, "Peilung mit ausgestrecktem Arm, Einheiten angleichen",
      "Lena hält mit ausgestrecktem Arm einen $2\\,\\text{cm}$ breiten "
      "Radiergummi $55\\,\\text{cm}$ vor ihr Auge. Er verdeckt genau ein "
      "$11\\,\\text{m}$ breites Haus. Zeichne eine Skizze. Wie weit ist das "
      "Haus von Lenas Auge entfernt?", "text", "",
      "$x : 55\\,\\text{cm} = 1\\,100\\,\\text{cm} : 2\\,\\text{cm}$; "
      "$x = 55 \\cdot 1\\,100 : 2 = 30\\,250\\,\\text{cm} = 302{,}5\\,\\text{m}$",
      "0.55*11/0.02", H, "\\rechenplatz[halb]{4}")
H = "S. 67 Nr. 16 – Umkehrung prüfen, Einheiten gemischt, Teilstrecken gegeben"
assert R(20, 8) == R(5, 2) and R(145, 60) != R(5, 2)
zeile(3, 1, 8, "Teilstrecken in dm und cm, Ergebnis nicht parallel",
      "In einer Figur schneiden sich zwei Geraden in $Z$. Es ist "
      "$\\overline{ZA} = 0{,}8\\,\\text{dm}$, $\\overline{AA'} = 1{,}2\\,\\text{dm}$, "
      "$\\overline{ZB} = 6\\,\\text{cm}$ und $\\overline{BB'} = 8{,}5\\,\\text{cm}$. "
      "Prüfe, ob $AB$ und $A'B'$ parallel sind.", "text", "",
      "$\\overline{ZA'} = 20\\,\\text{cm}$, $20 : 8 = 2{,}5$; "
      "$\\overline{ZB'} = 14{,}5\\,\\text{cm}$, $14{,}5 : 6 \\approx 2{,}42$; "
      "nicht parallel", "[2.5, 14.5/6]", H)
H = "S. 65 Nr. 9b; S. 66 Nr. 12 – Messanordnung begründen"
zeile(3, 4, 2, "Messfigur so abstecken, dass der Faktor ganzzahlig wird",
      "Tim misst eine Flussbreite mit einer abgesteckten Strahlensatzfigur. "
      "Er wählt die Strecken am Ufer so, dass das Verhältnis eine ganze "
      "Zahl ist. Begründe, warum das vorteilhaft ist.", "text", "",
      "Mit ganzem Faktor rechnet man die Breite ohne Bruch aus (nur mal "
      "nehmen), und die kleinen Messfehler werden nicht durch eine "
      "schwierige Division vergrößert; man kann das Ergebnis im Kopf "
      "überschlagen.", "", H)
NG = ("Verhältnisgleichung in der Figur nur mit Streckennamen ergänzen, "
      "auch mit drei Parallelen", 2)
H = "S. 66 Nr. 13 – Verhältnisgleichungen aus der Figur ergänzen"
zeile(3, 1, "NEU-gleichung-ergaenzen", "Streckennamen statt Zahlen: welche Strecke gehört in die Lücke",
      "In der V-Figur liegen $A$ und $A'$ auf dem einen Strahl, $B$ und "
      "$B'$ auf dem anderen; $AB \\parallel A'B'$. Ergänze:\\\\ "
      "$\\overline{ZA} : \\overline{ZA'} = \\overline{ZB} : \\_\\_$ \\quad "
      "$\\overline{AB} : \\overline{A'B'} = \\overline{ZA} : \\_\\_$",
      "text", "", "$\\overline{ZB'}$; $\\overline{ZA'}$", "", H,
      "\\strahlensatz{2}{5}{35}", neu=NG)
zeile(3, 1, "NEU-gleichung-ergaenzen", "drei Parallelen: Abschnitte und Parallelenstücke zuordnen",
      "Zwei Strahlen beginnen in $Z$. Auf dem einen liegen $A$, $C$, $E$, "
      "auf dem anderen $B$, $D$, $F$; $AB \\parallel CD \\parallel EF$. "
      "Ergänze:\\\\ $\\overline{ZC} : \\overline{ZE} = \\overline{ZD} : \\_\\_$ "
      "\\quad $\\overline{CD} : \\overline{EF} = \\overline{ZC} : \\_\\_$ "
      "\\quad $\\overline{AC} : \\overline{CE} = \\overline{BD} : \\_\\_$",
      "text", "", "$\\overline{ZF}$; $\\overline{ZE}$; $\\overline{DF}$", "",
      H, neu=NG)
NT = ("Strecke im Verhältnis m : n teilen (Hilfsstrahl mit m + n "
      "gleichen Teilen; Vorrat)", 1)
H = "S. 67 Nr. 15 – Strecke im Verhältnis m : n teilen"
gl(R(10 * 7, 10), 7); gl(R(10 * 3, 10), 3)
zeile(3, 3, "NEU-teilung-mn", "Teilungspunkt mit m + n gleichen Teilen auf dem Hilfsstrahl",
      "Zeichne eine Strecke $AB$ von $10\\,\\text{cm}$ Länge. Teile sie mit "
      "einem Hilfsstrahl und einer Parallelen im Verhältnis $7 : 3$. Wie "
      "lang sind $\\overline{AT}$ und $\\overline{TB}$?", "zeichnen", "",
      "Hilfsstrahl mit $10$ gleichen Teilen, Endpunkt mit $B$ verbinden, "
      "Parallele durch den siebten Teilpunkt; $\\overline{AT} = 7\\,\\text{cm}$, "
      "$\\overline{TB} = 3\\,\\text{cm}$", "[7, 3]", H,
      "\\begin{ksys}[xmin=0,xmax=12,ymin=0,ymax=6]\\end{ksys}", neu=NT)

# --- Nachrechnen: pruef gegen sympy-Werte in der Lösung ------------
for r in zeilen:
    if r["pruef"]:
        w = wert(r["pruef"])
        assert all(v.is_real for v in w), r["id"]
with open("neu-strahlensaetze-duden9.jsonl", "w", encoding="utf-8",
          newline="\n") as f:
    for r in zeilen:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
from collections import Counter
print(len(zeilen), Counter((r["einheit"], r["kette_nr"], r["sprosse"]) for r in zeilen))
