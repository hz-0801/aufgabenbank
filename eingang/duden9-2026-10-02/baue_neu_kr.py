#!/usr/bin/env python3
"""Baut neu-kreis-duden9.jsonl (kreis) und rechnet jede Lösung mit
sympy/math nach. Vom Buch nur Typ und Stufung; Zahlen und Wortlaut
eigen. Vorlage: baue_neu_pyt.py. Kette, sprosse_text, merkmal, hoehe,
quelle werden bei vorhandenen Sprossen aus der Bank übernommen.
Kastenzahlen des Katalogs (5; 15,7; 2; 12,6; 31,4; 10; 3; 28,3; 8;
50,3; 78,5; 5; 72°; 62,8; 32,6) bewusst vermieden."""
import json
import math
import sympy as sp

Q = "Duden WÜT Mathematik 9 (2017)"
B = "aufgabenbank/bank/"
E = "kreis"
pi = sp.pi
zeilen = []
_bank = {}


def bank(e):
    if e not in _bank:
        _bank[e] = [json.loads(l) for l in open(f"{B}{E}/e{e}.jsonl")]
    return _bank[e]


_zaehl = {}


def neu(e, k, s, aufgabe, form, antwort, loesung, pruef, herkunft,
        grafik="", neu_text=None, neu_merkmal=None, neu_kette=None):
    if neu_text is None:
        g = [r for r in bank(e) if r["kette_nr"] == k and r["sprosse"] == s]
        assert g, (e, k, s)
        v, n = g[0], len(g)
        kette, st, mk, h, q = (v["kette"], v["sprosse_text"], v["merkmal"],
                               v["hoehe"], v["quelle"])
    else:
        vv = [r for r in bank(e) if r["kette_nr"] == k]
        kette = vv[0]["kette"] if vv else neu_kette
        q = (vv or bank(e))[0]["quelle"]
        st, mk, h, n = neu_text, neu_merkmal, "sprosse", 0
    key = (e, k, s)
    _zaehl[key] = _zaehl.get(key, n) + 1
    var = _zaehl[key]
    # Lösung gegen pruef: jeder pruef-Wert muss nachgerechnet sein
    werte = eval(pruef, {"math": math}) if pruef else []
    zeilen.append({
        "id": f"{E}-e{e}-k{k}-s{s}-v{var}", "eintrag": E, "einheit": e,
        "kette": kette, "kette_nr": k, "sprosse": s, "sprosse_text": st,
        "merkmal": mk, "hoehe": h, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": q,
        "herkunft": f"{Q}, {herkunft}"})
    return werte


def chk(ausdruck, soll, st=1):
    """sympy-Wert gerundet gegen die Zahl der Lösung"""
    w = float(sp.N(ausdruck, 30))
    assert round(w + 1e-12, st) == soll, (ausdruck, w, soll)


RUND1 = "Rechne mit der $\\pi$-Taste. Runde auf eine Stelle nach dem Komma."

# ===== e1 k2 s3 Dezimalzahlen mit Runden: Einheiten wechseln =========
H = "S. 91 Nr. 3 – Umfang und Fläche aus r oder d, Maße in mm, dm, km; sinnvoll runden"
chk(pi * 28, 88.0)
neu(1, 2, 3,
    "Ein runder Brunnenrand hat den Durchmesser $d = 0{,}028$ km. Rechne "
    "zuerst in Meter um. Wie lang ist der Umfang in Meter? " + RUND1,
    "teil", "d = __ m, u ≈ __ m",
    "$d = 28$ m; $u = \\pi \\cdot 28 \\approx 88{,}0$ m",
    "[28, math.pi*28]", H)
chk(2 * pi * sp.Rational(65, 10), 40.8)
neu(1, 2, 3,
    "Ein Kreis hat den Radius $r = 65$ mm. Berechne den Umfang in "
    "Zentimeter. " + RUND1, "teil", "r = __ cm, u ≈ __ cm",
    "$r = 6{,}5$ cm; $u = 2 \\cdot \\pi \\cdot 6{,}5 \\approx 40{,}8$ cm",
    "[6.5, 2*math.pi*6.5]", H)
# e2 k1 s3
chk(pi * sp.Rational(42, 10)**2, 55.4)
neu(2, 1, 3,
    "Ein Kreis hat den Durchmesser $d = 0{,}84$ dm. Berechne seine Fläche "
    "in cm². " + RUND1, "teil", "r = __ cm, A ≈ __ cm²",
    "$d = 8{,}4$ cm, $r = 4{,}2$ cm; $A = \\pi \\cdot 4{,}2^2 \\approx "
    "55{,}4$ cm²", "[8.4, 4.2, math.pi*4.2**2]", H)
chk(pi * sp.Rational(45, 10)**2, 63.6)
neu(2, 1, 3,
    "Ein rundes Becken hat den Radius $r = 0{,}0045$ km. Berechne seine "
    "Fläche in m². " + RUND1, "teil", "r = __ m, A ≈ __ m²",
    "$r = 4{,}5$ m; $A = \\pi \\cdot 4{,}5^2 \\approx 63{,}6$ m²",
    "[4.5, math.pi*4.5**2]", H)

# ===== e2 k1 s5 Tabelle mit Halbkreis, gegeben A oder Halbkreis ======
H = "S. 91 Nr. 4 – Tabelle r, d, u, A und Halbkreisfläche; gegeben ist die Fläche oder die Halbkreisfläche"
r1 = sp.sqrt(200 / pi)
chk(r1, 8.0); chk(2 * r1, 16.0); chk(2 * pi * r1, 50.1)
neu(2, 1, 5,
    "In der Tabelle ist die Fläche gegeben. Ergänze die Tabelle, auch die "
    "Fläche des Halbkreises. " + RUND1, "tabelle", "",
    "$r \\approx 8{,}0$ cm, $d \\approx 16{,}0$ cm, $u \\approx 50{,}1$ cm, "
    "Halbkreis $= 100$ cm²",
    "[math.sqrt(200/math.pi), 2*math.sqrt(200/math.pi), "
    "2*math.pi*math.sqrt(200/math.pi), 100]", H,
    grafik="\\sachtabelle{ccccc}{$r$ & $d$ & $u$ & $A$ & Halbkreis}"
           "{\\leerzelle & \\leerzelle & \\leerzelle & $200$ cm² & \\leerzelle}")
r2 = sp.sqrt(60 / pi)
chk(r2, 4.4); chk(2 * r2, 8.7); chk(2 * pi * r2, 27.5)
neu(2, 1, 5,
    "In der Tabelle ist nur die Fläche des Halbkreises gegeben. Ergänze "
    "die Tabelle. " + RUND1, "tabelle", "",
    "$A = 60$ m², $r \\approx 4{,}4$ m, $d \\approx 8{,}7$ m, "
    "$u \\approx 27{,}5$ m",
    "[60, math.sqrt(60/math.pi), 2*math.sqrt(60/math.pi), "
    "2*math.pi*math.sqrt(60/math.pi)]", H,
    grafik="\\sachtabelle{ccccc}{$r$ & $d$ & $u$ & $A$ & Halbkreis}"
           "{\\leerzelle & \\leerzelle & \\leerzelle & \\leerzelle & $30$ m²}")

# ===== e1 k2 s7 Sachaufgabe Rad: rückwärts, Zoll, Geschwindigkeit =====
H = "S. 92 Nr. 6 – Umdrehungen aus der Strecke (rückwärts), Raddurchmesser auch in Zoll"
chk(pi * 50, 157.1); chk(240000 / (pi * 50), 1528, 0)
neu(1, 2, 7,
    "Ein Kinderrad hat den Durchmesser $50$ cm. Wie viele Umdrehungen macht "
    "es auf einem Schulweg von $2{,}4$ km? Runde auf ganze Umdrehungen.",
    "teil", "≈ __ Umdrehungen",
    "$u = \\pi \\cdot 50 \\approx 157{,}1$ cm; $2{,}4$ km $= 240\\,000$ cm; "
    "$240\\,000 : 157{,}1 \\approx 1\\,528$ Umdrehungen",
    "[math.pi*50, 240000/(math.pi*50)]", H)
chk(pi * sp.Rational(6604, 100), 207.5)
chk(1500000 / (pi * sp.Rational(6604, 100)), 7230, 0)
neu(1, 2, 7,
    "Ein Fahrrad hat Räder mit $26$ Zoll Durchmesser ($1$ Zoll $= 2{,}54$ "
    "cm). Wie oft dreht sich ein Rad auf einer Tour von $15$ km? Runde auf "
    "ganze Umdrehungen.", "teil", "d = __ cm, ≈ __ Umdrehungen",
    "$d = 26 \\cdot 2{,}54 = 66{,}04$ cm; $u = \\pi \\cdot 66{,}04 \\approx "
    "207{,}5$ cm; $1\\,500\\,000 : 207{,}5 \\approx 7\\,230$ Umdrehungen",
    "[66.04, math.pi*66.04, 1500000/(math.pi*66.04)]", H)
H = "S. 92 Nr. 8 – Geschwindigkeit aus Raddurchmesser und Zahl der Umdrehungen in einer Zeit"
w = pi * 48 * 1500 / 100000
chk(pi * 48, 150.8); chk(w, 2.26, 2); chk(w * 30, 68, 0)
neu(1, 2, 7,
    "Das Rad eines Motorrollers hat den Durchmesser $48$ cm. In $2$ Minuten "
    "dreht es sich $1\\,500$-mal. Wie schnell fährt der Roller in km/h? "
    "Runde auf ganze km/h.", "teil", "≈ __ km/h",
    "$u = \\pi \\cdot 48 \\approx 150{,}8$ cm; Weg in $2$ Minuten "
    "$\\approx 2{,}26$ km; eine Stunde hat $30$-mal $2$ Minuten: "
    "$\\approx 68$ km/h",
    "[math.pi*48, math.pi*48*1500/100000, math.pi*48*1500/100000*30]", H)

# ===== e1 k2 s6 Halbkreisbogen: Tischrand =============================
H = "S. 92 Nr. 7b – Rand einer Platte aus Rechteck und zwei Halbkreisen, daraus die Zahl der Plätze"
rand = sp.Rational(48, 10) + pi * sp.Rational(11, 10)
chk(pi * sp.Rational(11, 10), 3.46, 2); chk(rand, 8.26, 2); chk(rand / sp.Rational(7, 10), 11.8)
neu(1, 2, 6,
    "Ein Konferenztisch besteht aus einem Rechteck, $2{,}40$ m lang, und an "
    "beiden schmalen Seiten je einem Halbkreis mit dem Durchmesser "
    "$1{,}10$ m. Wie lang ist der Rand des Tisches? Für eine Person "
    "rechnet man $70$ cm Rand. Wie viele Personen haben Platz?", "teil",
    "Rand ≈ __ m, __ Personen",
    "zwei Halbkreisbögen ergeben einen ganzen Kreis: $\\pi \\cdot 1{,}10 "
    "\\approx 3{,}46$ m; zwei gerade Seiten $2 \\cdot 2{,}40 = 4{,}80$ m; Rand "
    "$\\approx 8{,}26$ m; $8{,}26 : 0{,}70 \\approx 11{,}8$; Personen $= 11$",
    "[math.pi*1.1, 4.8, 4.8+math.pi*1.1, (4.8+math.pi*1.1)/0.7, 11]", H)

# ===== e3 k1 s4/s5 Bogen und Ausschnitt aus d, Winkel über 180° =======
H = "S. 94 Nr. 10 – Bogenlänge und Ausschnittsfläche aus dem Durchmesser, auch mit Mittelpunktswinkel über 180°"
chk(sp.Rational(240, 360) * 2 * pi * sp.Rational(9, 2), 18.8)
neu(3, 1, 4,
    "Ein Kreisausschnitt gehört zu einem Kreis mit dem Durchmesser $d = 9$ "
    "cm. Sein Mittelpunktswinkel ist $\\alpha = 240^\\circ$. Wie lang ist "
    "der Bogen? " + RUND1, "teil", "r = __ cm, b ≈ __ cm",
    "$r = 4{,}5$ cm; $b = \\frac{240}{360} \\cdot 2 \\cdot \\pi \\cdot 4{,}5 "
    "\\approx 18{,}8$ cm", "[4.5, 240/360*2*math.pi*4.5]", H)
chk(sp.Rational(300, 360) * pi * sp.Rational(8, 10)**2, 1.68, 2)
neu(3, 1, 5,
    "Ein Kreisausschnitt gehört zu einem Kreis mit dem Durchmesser "
    "$d = 1{,}6$ m. Sein Mittelpunktswinkel ist $\\alpha = 300^\\circ$. Wie "
    "groß ist seine Fläche? Rechne mit der $\\pi$-Taste. Runde auf zwei "
    "Stellen nach dem Komma.", "teil", "r = __ m, A ≈ __ m²",
    "$r = 0{,}8$ m; $A = \\frac{300}{360} \\cdot \\pi \\cdot 0{,}8^2 "
    "\\approx 1{,}68$ m²", "[0.8, 300/360*math.pi*0.8**2]", H)
chk(sp.Rational(15, 360) * pi * 22**2, 63.4)
neu(3, 1, 5,
    "Ein schmaler Kreisausschnitt hat den Radius $r = 2{,}2$ dm und den "
    "Mittelpunktswinkel $\\alpha = 15^\\circ$. Berechne seine Fläche in "
    "cm². " + RUND1, "teil", "r = __ cm, A ≈ __ cm²",
    "$r = 22$ cm; $A = \\frac{15}{360} \\cdot \\pi \\cdot 22^2 \\approx "
    "63{,}4$ cm²", "[22, 15/360*math.pi*22**2]", H)

# ===== e3 k1 s3 Winkel aus Anteil: gleichmäßige Einteilung ===========
H = "S. 95 Nr. 13 – Mittelpunktswinkel aus einer gleichmäßigen Einteilung des Kreises"
assert sp.Rational(360, 20) == 18 and 5 * 18 == 90
neu(3, 1, 3,
    "Ein Riesenrad hat $20$ Gondeln, gleichmäßig auf dem Kreis verteilt. "
    "Wie groß ist der Mittelpunktswinkel zwischen zwei benachbarten "
    "Gondeln? Wie groß ist er zwischen der ersten und der sechsten Gondel?",
    "teil", "__ °, __ °",
    "$360^\\circ : 20 = 18^\\circ$; von der ersten zur sechsten Gondel sind "
    "es $5$ Abstände: $5 \\cdot 18^\\circ = 90^\\circ$", "[18, 90]", H)

# ===== e3 k1 s2 Prozent: zwei gleiche Sektoren ========================
H = "S. 95 Nr. 12c – Anteil mehrerer gleicher Sektoren an der Kreisfläche in Prozent, erst schätzen"
chk(sp.Rational(100, 360) * 100, 27.8)
neu(3, 1, 2,
    "Im Bild sind zwei gleich große, gegenüberliegende Ausschnitte grau, "
    "jeder mit dem Mittelpunktswinkel $50^\\circ$. Schätze zuerst. "
    "Berechne dann: Wie viel Prozent der Kreisfläche sind grau? Runde auf "
    "eine Stelle nach dem Komma.", "teil", "≈ __ %",
    "zusammen $100^\\circ$; $100 : 360 \\approx 0{,}278 = 27{,}8\\,\\%$",
    "[100, 100/360*100]", H,
    grafik="\\begin{kreis}[2] \\mittelpunkt{M} \\sektor{0}{50}{} "
           "\\sektor{180}{230}{} \\end{kreis}")

# ===== NEU e1 k2 umfangsaenderung (nach s7) ===========================
STU = ("NEU-umfangsaenderung: Abstand zweier Kreise aus dem Unterschied der "
       "Umfänge (Unterschied der Radien = Unterschied der Umfänge : 2π) und "
       "umgekehrt; der Unterschied hängt nicht von der Größe des Kreises ab "
       "(Vorrat; Vorschlag; nicht im Katalog)")
MKU = "zwei Kreise vergleichen: nur der Unterschied zählt, nicht der Radius"
H = "S. 91 Nr. 5 – Band um den Äquator um 1 m verlängert: Abstand aus dem Unterschied der Umfänge"
chk(70 / (2 * pi), 11.1); chk(100 / (2 * pi), 15.9); chk(30 / (2 * pi), 4.8)
neu(1, 2, "NEU-umfangsaenderung",
    "Um einen Fußball mit dem Umfang $70$ cm liegt eine Schnur straff an. "
    "Die Schnur wird um $30$ cm verlängert und überall im gleichen Abstand "
    "um den Ball gelegt. Wie groß ist der Abstand zwischen Ball und "
    "Schnur? Schätze zuerst. " + RUND1, "teil", "Abstand ≈ __ cm",
    "$r_1 = 70 : (2\\pi) \\approx 11{,}1$ cm; $r_2 = 100 : (2\\pi) \\approx "
    "15{,}9$ cm; Abstand $= 30 : (2\\pi) \\approx 4{,}8$ cm",
    "[70/(2*math.pi), 100/(2*math.pi), 30/(2*math.pi)]", H,
    neu_text=STU, neu_merkmal=MKU)
chk(pi * sp.Rational(365, 10), 114.67, 2); chk(pi * sp.Rational(377, 10), 118.44, 2)
chk(pi * sp.Rational(12, 10), 3.77, 2)
neu(1, 2, "NEU-umfangsaenderung",
    "Auf einer Laufbahn ist die Kurve ein Halbkreis. Die innere Bahn hat "
    "dort den Radius $36{,}5$ m, die nächste Bahn liegt $1{,}2$ m weiter "
    "außen. Wie viel länger ist der Halbkreisbogen der äußeren Bahn? Runde "
    "auf zwei Stellen nach dem Komma. Begründe, warum man den Radius "
    "$36{,}5$ m dafür eigentlich nicht braucht.", "teil",
    "länger um ≈ __ m",
    "innen $\\pi \\cdot 36{,}5 \\approx 114{,}67$ m, außen $\\pi \\cdot 37{,}7 "
    "\\approx 118{,}44$ m; Unterschied $\\pi \\cdot 1{,}2 \\approx 3{,}77$ m – "
    "es zählt nur der Abstand der Bahnen, bei jedem Radius gleich",
    "[math.pi*36.5, math.pi*37.7, math.pi*1.2]", H,
    neu_text=STU, neu_merkmal=MKU)

# ===== NEU e1 k3 gerade-kreis (nach s1) ===============================
STG = ("NEU-gerade-kreis: Lage einer Geraden zum Kreis – Passante, Tangente, "
       "Sekante, dazu Sehne und Berührradius; Entscheidung über die Zahl der "
       "gemeinsamen Punkte oder den Abstand vom Mittelpunkt (Vorrat; "
       "Vorschlag; nicht im Katalog)")
MKG = "Lage einer Geraden zum Kreis an der Zahl der gemeinsamen Punkte benennen"
H = "S. 90 Wissen und S. 91 Nr. 2 – Punkte, Strecken und Geraden am Kreis den Begriffen Passante, Sekante, Tangente, Sehne, Berührradius zuordnen"
neu(1, 3, "NEU-gerade-kreis",
    "Ordne jedem Satz den passenden Begriff zu: Tangente, Sehne, Passante, "
    "Sekante. \\\\ (a) Die Gerade schneidet den Kreis in zwei Punkten. "
    "\\\\ (b) Die Gerade berührt den Kreis in genau einem Punkt. \\\\ "
    "(c) Die Gerade hat mit dem Kreis keinen Punkt gemeinsam. \\\\ "
    "(d) Die Strecke verbindet zwei Punkte der Kreislinie.", "text", "",
    "(a) Sekante (b) Tangente (c) Passante (d) Sehne", "", H,
    neu_text=STG, neu_merkmal=MKG)
neu(1, 3, "NEU-gerade-kreis",
    "Ein Kreis hat den Radius $4$ cm. Eine Gerade hat vom Mittelpunkt den "
    "Abstand (a) $2{,}5$ cm, (b) $4$ cm, (c) $5{,}5$ cm. Ist sie eine "
    "Sekante, eine Tangente oder eine Passante? Wie viele Punkte hat sie "
    "mit dem Kreis gemeinsam?", "teil", "(a) __ (b) __ (c) __",
    "(a) Abstand kleiner als der Radius: Sekante, zwei Punkte (b) Abstand "
    "gleich dem Radius: Tangente, ein Punkt (c) Abstand größer: Passante, "
    "kein Punkt", "", H, neu_text=STG, neu_merkmal=MKG)

# ===== NEU e3 k1 kreisabschnitt (nach s6) =============================
STA = ("NEU-kreisabschnitt: Kreisabschnitt (Segment) zwischen Bogen und "
       "Sehne beim rechten Mittelpunktswinkel – Viertelkreis minus "
       "Dreieck; Blatt- und Sichelflächen daraus (Vorrat; Vorschlag; nicht "
       "im Katalog)")
MKA = "Fläche zwischen Bogen und Sehne: Ausschnitt minus Dreieck"
H = "S. 94 Nr. 11 – Sichelfläche: Kreisabschnitt als Viertelkreis minus Dreieck"
chk(sp.Rational(49, 4) * pi, 38.5); chk(sp.Rational(49, 4) * pi - sp.Rational(49, 2), 14.0)
neu(3, 1, "NEU-kreisabschnitt",
    "Ein Viertelkreis hat den Radius $7$ cm. Eine Sehne verbindet die "
    "beiden Enden des Bogens. Der Kreisabschnitt liegt zwischen Bogen und "
    "Sehne. Berechne seine Fläche: Viertelkreis minus Dreieck. " + RUND1,
    "teil", "A ≈ __ cm²",
    "Viertelkreis $\\frac{1}{4} \\cdot \\pi \\cdot 7^2 \\approx 38{,}5$ cm²; "
    "Dreieck $\\frac{1}{2} \\cdot 7 \\cdot 7 = 24{,}5$ cm²; Kreisabschnitt "
    "$\\approx 14{,}0$ cm²",
    "[49/4*math.pi, 24.5, 49/4*math.pi-24.5]", H,
    neu_text=STA, neu_merkmal=MKA)
chk(36 * pi - 72, 41.1); chk(72 * pi - 144, 82.2)
neu(3, 1, "NEU-kreisabschnitt",
    "In ein Quadrat mit der Seite $12$ cm werden zwei Viertelkreise "
    "gezeichnet: einer um die linke untere Ecke, einer um die rechte obere "
    "Ecke, beide mit dem Radius $12$ cm. Zwischen den beiden Bögen entsteht "
    "ein Blatt. Wie groß ist seine Fläche? " + RUND1, "teil",
    "A ≈ __ cm²",
    "Das Blatt besteht aus zwei Kreisabschnitten; einer: $\\frac{1}{4} \\cdot "
    "\\pi \\cdot 12^2 - \\frac{1}{2} \\cdot 12 \\cdot 12 \\approx 41{,}1$ cm²; "
    "Blatt $\\approx 82{,}2$ cm²", "[36*math.pi-72, 72*math.pi-144]", H,
    neu_text=STA, neu_merkmal=MKA)

# ===== NEU e3 k1 kreisring-rueckwaerts (nach s7) ======================
STR = ("NEU-kreisring-rueckwaerts: Kreisring rückwärts – aus äußerem Umfang "
       "und Ringfläche beide Radien, oder aus innerem Radius und Ringfläche "
       "die Breite des Rings (Vorrat; Vorschlag; nicht im Katalog)")
MKR = "rückwärts: erst den bekannten Kreis, dann über die Ringfläche den anderen Radius"
H = "S. 92 Nr. 9 – Kreisring rückwärts: aus äußerem Umfang und Ringfläche den inneren und äußeren Radius"
ra = 50 / (2 * pi)
chk(ra, 8.0); chk(pi * ra**2, 198.9); chk(pi * ra**2 - 120, 78.9)
chk(sp.sqrt((pi * ra**2 - 120) / pi), 5.0)
neu(3, 1, "NEU-kreisring-rueckwaerts",
    "Ein Kreisring hat außen den Umfang $50$ cm. Seine Fläche ist "
    "$120$ cm². Berechne den äußeren und den inneren Radius. " + RUND1,
    "teil", "außen ≈ __ cm, innen ≈ __ cm",
    "$r_2 = 50 : (2\\pi) \\approx 8{,}0$ cm; großer Kreis $\\approx "
    "198{,}9$ cm²; kleiner Kreis $\\approx 198{,}9 - 120 = 78{,}9$ cm²; "
    "$r_1 = \\sqrt{78{,}9 : \\pi} \\approx 5{,}0$ cm",
    "[50/(2*math.pi), 625/math.pi, 625/math.pi-120, "
    "math.sqrt((625/math.pi-120)/math.pi)]", H,
    neu_text=STR, neu_merkmal=MKR)
rb = sp.sqrt(81 + 100 / pi)
chk(81 * pi, 254.47, 2); chk(81 * pi + 100, 354.47, 2); chk(rb, 10.62, 2); chk(rb - 9, 1.62, 2)
neu(3, 1, "NEU-kreisring-rueckwaerts",
    "Um eine runde Rasenfläche mit dem Radius $9$ m wird außen ein "
    "gepflasterter Ring gelegt. Der Ring soll $100$ m² groß werden. Wie "
    "groß ist der äußere Radius? Wie breit ist der Ring? Rechne mit der "
    "$\\pi$-Taste. Runde auf zwei Stellen nach dem Komma.", "teil",
    "r ≈ __ m, Breite ≈ __ m",
    "Rasen $\\pi \\cdot 9^2 \\approx 254{,}47$ m²; großer Kreis $\\approx "
    "354{,}47$ m²; $r_2 = \\sqrt{354{,}47 : \\pi} \\approx 10{,}62$ m; "
    "Ring $\\approx 1{,}62$ m breit",
    "[81*math.pi, 81*math.pi+100, math.sqrt(81+100/math.pi), "
    "math.sqrt(81+100/math.pi)-9]", H,
    neu_text=STR, neu_merkmal=MKR)

# ===== NEU e3 neue Kette 4 umfangswinkel ==============================
STW = ("NEU-umfangswinkel: Umfangswinkel und Mittelpunktswinkel über "
       "demselben Bogen (Umfangswinkel = halber Mittelpunktswinkel), Thales "
       "als Sonderfall, gegenüberliegende Winkel im Sehnenviereck (nur "
       "Gymnasium; Vorschlag; in winkel-dreiecke.md unter „nicht "
       "aufgenommen“)")
MKW = "Winkel am Kreis: Umfangswinkel aus dem Mittelpunktswinkel halbieren"
H = "S. 94 Wissen und S. 95 Nr. 13–16 – Umfangswinkel und Mittelpunktswinkel über einem Bogen, Halbkreis, Sehnenviereck"
assert sp.Rational(124, 2) == 62 and sp.Rational(180, 2) == 90
neu(3, 4, "NEU-umfangswinkel",
    "Die Punkte $A$, $B$ und $C$ liegen auf einem Kreis mit dem Mittelpunkt "
    "$M$. Der Mittelpunktswinkel $AMB$ über dem Bogen $AB$ "
    "ist $124^\\circ$; $C$ liegt auf dem anderen Bogen. Wie groß ist der "
    "Umfangswinkel $ACB$? Wie groß wäre er, wenn $AB$ ein "
    "Durchmesser ist?", "teil", "__ °, __ °",
    "Umfangswinkel $= 124^\\circ : 2 = 62^\\circ$; ist $AB$ ein Durchmesser, "
    "ist der Mittelpunktswinkel $= 180^\\circ$ und der Umfangswinkel "
    "$= 90^\\circ$ (Thales)", "[62, 180, 90]", H,
    neu_text=STW, neu_merkmal=MKW, neu_kette="Winkel am Kreis")
assert 180 - 73 == 107
neu(3, 4, "NEU-umfangswinkel",
    "Die Punkte $A$, $B$, $C$, $D$ liegen in dieser Reihenfolge auf einem "
    "Kreis (Sehnenviereck). Der Innenwinkel bei $A$ ist $73^\\circ$. Wie "
    "groß ist der Innenwinkel bei $C$? Begründe mit den "
    "Mittelpunktswinkeln über den beiden Bögen von $B$ nach $D$.", "teil",
    "__ °",
    "Mittelpunktswinkel zum Winkel bei $A$: $2 \\cdot 73^\\circ = 146^\\circ$; "
    "die beiden Mittelpunktswinkel ergeben zusammen $360^\\circ$, der "
    "andere ist $360^\\circ - 146^\\circ = 214^\\circ$; Winkel bei $C = 214^\\circ : 2 = 107^\\circ$ – "
    "gegenüberliegende Winkel ergeben zusammen $180^\\circ$",
    "[146, 214, 107]", H,
    neu_text=STW, neu_merkmal=MKW, neu_kette="Winkel am Kreis")

with open("neu-kreis-duden9.jsonl", "w", encoding="utf-8", newline="\n") as fh:
    for z in zeilen:
        fh.write(json.dumps(z, ensure_ascii=False) + "\n")
from collections import Counter
print(len(zeilen), "Zeilen, Lösungen nachgerechnet")
for kk, n in Counter((z["einheit"], z["kette_nr"], z["sprosse"]) for z in zeilen).items():
    print(kk, n)
