#!/usr/bin/env python3
"""Baut neu-pyt-duden9.jsonl (pythagoras, trigonometrie) und rechnet
jede Lösung mit sympy nach. Vom Buch nur Typ und Stufung; Zahlen und
Wortlaut eigen. Vorlage: baue_neu_qf.py. Kette, sprosse_text, merkmal,
hoehe, quelle werden bei vorhandenen Sprossen aus der Bank übernommen
(das Prüfskript verlangt sie je Sprosse einheitlich)."""
import json
import math
import sympy as sp

Q = "Duden WÜT Mathematik 9 (2017)"
R = sp.Rational
B = "aufgabenbank/bank/"
zeilen = []
_bank = {}


def bank(E, e):
    if (E, e) not in _bank:
        _bank[(E, e)] = [json.loads(l) for l in open(f"{B}{E}/e{e}.jsonl")]
    return _bank[(E, e)]


def vorlage(E, e, k, s):
    g = [r for r in bank(E, e) if r["kette_nr"] == k and r["sprosse"] == s]
    assert g, (E, e, k, s)
    return g[0], len(g)


_zaehl = {}


def neu(E, e, k, s, aufgabe, form, antwort, loesung, pruef, herkunft,
        grafik="", neu_text=None, neu_merkmal=None):
    if neu_text is None:                       # vorhandene Sprosse
        v, n = vorlage(E, e, k, s)
        kette, st, mk, h, q = (v["kette"], v["sprosse_text"], v["merkmal"],
                               v["hoehe"], v["quelle"])
    else:                                      # NEU-Sprosse
        v = next(r for r in bank(E, e) if r["kette_nr"] == k)
        kette, st, mk, h, q, n = v["kette"], neu_text, neu_merkmal, \
            "sprosse", v["quelle"], 0
    key = (E, e, k, s)
    _zaehl[key] = _zaehl.get(key, n) + 1
    var = _zaehl[key]
    zeilen.append({
        "id": f"{E}-e{e}-k{k}-s{s}-v{var}", "eintrag": E, "einheit": e,
        "kette": kette, "kette_nr": k, "sprosse": s, "sprosse_text": st,
        "merkmal": mk, "hoehe": h, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": q,
        "herkunft": f"{Q}, {herkunft}"})


def wurzel_ok(q2, wert):
    assert sp.sqrt(sp.nsimplify(q2)) == sp.nsimplify(wert), (q2, wert)


def tz(n):
    return f"{n:,}".replace(",", "\\,")


def dz(x):
    return str(x).replace(".", "{,}")


def rund(x, st=1):
    return round(float(x) + 1e-12, st)


a, b, c, d, e_, f, k, l, m = sp.symbols("a b c d e f k l m", positive=True)
P = "pythagoras"
T = "trigonometrie"

# ================= pythagoras e1 k2 s8: Gleichungen prüfen ===========
H = "S. 82 Nr. 13 – zu einem Dreieck mit fremden Buchstaben mehrere (auch umgeformte) Gleichungen prüfen"
GILT = "\\kreuz{gilt} \\kreuz{gilt nicht}"
hyp = sp.Eq(m**2, k**2 + l**2)
tests = [(sp.Eq(m**2, k**2 + l**2), True), (sp.Eq(k**2, m**2 - l**2), True),
         (sp.Eq(l**2, k**2 - m**2), False), (sp.Eq(m**2 - k**2, l**2), True),
         (sp.Eq(k**2 + m**2, l**2), False)]
for g, soll in tests:
    diff = sp.simplify((g.lhs - g.rhs).subs(m**2, k**2 + l**2))
    assert (diff == 0) == soll, g
neu(P, 1, 2, 8,
    "Die Figur zeigt ein rechtwinkliges Dreieck. Prüfe jede Gleichung: "
    "Gilt sie für dieses Dreieck? \\\\ "
    f"(1) $m^2 = k^2 + l^2$ {GILT} \\\\ (2) $k^2 = m^2 - l^2$ {GILT} \\\\ "
    f"(3) $l^2 = k^2 - m^2$ {GILT} \\\\ (4) $m^2 - k^2 = l^2$ {GILT} \\\\ "
    f"(5) $k^2 + m^2 = l^2$ {GILT}", "ankreuzen", "",
    "(1) gilt, (2) gilt, (3) gilt nicht, (4) gilt, (5) gilt nicht – "
    "$m$ ist die Hypotenuse; (2) und (4) sind nur umgestellt",
    "", H, grafik="\\dreieckrw{5}{3.57}{$k$}{$l$}{$m$}")
tests = [(sp.Eq(f**2, d**2 + e_**2), True), (sp.Eq(-d**2 - e_**2, -f**2), True),
         (sp.Eq(d**2, e_**2 - f**2), False), (sp.Eq(e_**2, f**2 - d**2), True),
         (sp.Eq(f, d + e_), False)]
for g, soll in tests:
    diff = sp.simplify((g.lhs**2 - g.rhs**2 if g.lhs == f else g.lhs - g.rhs)
                       .subs(f**2, d**2 + e_**2))
    assert (diff == 0) == soll, g
neu(P, 1, 2, 8,
    "Die Figur zeigt ein rechtwinkliges Dreieck. Prüfe jede Gleichung: "
    "Gilt sie für dieses Dreieck? \\\\ "
    f"(1) $f^2 = d^2 + e^2$ {GILT} \\\\ (2) $-d^2 - e^2 = -f^2$ {GILT} \\\\ "
    f"(3) $d^2 = e^2 - f^2$ {GILT} \\\\ (4) $e^2 = f^2 - d^2$ {GILT} \\\\ "
    f"(5) $f = d + e$ {GILT}", "ankreuzen", "",
    "(1) gilt, (2) gilt (beide Seiten mal $-1$ ergibt (1)), (3) gilt "
    "nicht, (4) gilt, (5) gilt nicht – $f$ ist die Hypotenuse",
    "", H, grafik="\\dreieckrw{5}{3.57}{$d$}{$e$}{$f$}")

# ================= pythagoras e2 k3 s3: Kathete, gemischte Einheiten ==
H = "S. 79 Nr. 1 – Kathete aus Hypotenuse und Kathete, Maße in verschiedenen Einheiten"
for (ct, at, bt, c_, a_, q2, erg, ant, einh) in [
        ("1{,}3$ m", "50$ cm", "b", 130, 50, 14400, "120$ cm $= 1{,}2", "b² = __ cm², b = __ cm", "m"),
        ("2{,}9$ km", "2\\,100$ m", "b", 2900, 2100, 4000000, "2\\,000$ m $= 2", "b² = __ m², b = __ m", "km")]:
    assert c_**2 - a_**2 == q2 and sp.sqrt(q2) == int(erg.split("$")[0].replace("\\,", ""))
    neu(P, 2, 3, 3,
        f"In einem rechtwinkligen Dreieck ist $c = {ct} die Hypotenuse und "
        f"$a = {at} eine Kathete. Rechne zuerst beide Längen in dieselbe "
        f"Einheit um. Berechne dann die Kathete $b$.", "teil", ant,
        f"$c = {tz(c_)}$, $a = {tz(a_)}$ in der kleineren Einheit; "
        f"$b^2 = {c_}^2 - {a_}^2 = {tz(q2)}$; $b = {erg}$ {einh}", f"[{q2}, {math.sqrt(q2)}]", H)
q2 = 610**2 - 60**2
assert q2 == 368500
neu(P, 2, 3, 3,
    "In einem rechtwinkligen Dreieck ist $c = 6{,}1$ dm die Hypotenuse und "
    "$a = 60$ mm eine Kathete. Rechne zuerst in Millimeter um. Berechne "
    "dann die Kathete $b$. Runde auf ganze Millimeter.", "teil",
    "b² = __ mm², b ≈ __ mm",
    "$c = 610$ mm; $b^2 = 610^2 - 60^2 = 368\\,500$; $b \\approx 607$ mm",
    "[368500, 607]", H)

# ================= pythagoras e2 NEU-gemischt-tabelle ================
STG = ("NEU-gemischt-tabelle: Hypotenuse oder Kathete gemischt in einer "
       "Tabelle – Dreieck mit fremden Buchstaben, rechter Winkel an einer "
       "genannten Ecke, Einheiten wechseln; je Spalte selbst entscheiden: "
       "plus oder minus (Vorschlag; nicht im Katalog)")
MKG = "Hypotenuse aus der Ecke des rechten Winkels bestimmen, dann je Spalte plus oder minus"
H = "S. 79 Nr. 2 – Tabelle: im Dreieck RST mit rechtem Winkel bei T je Spalte die fehlende Seite, Hypotenuse oder Kathete gemischt, Skizze"
for (v1, v2, v3) in [((2.4, 1.0), (3.3, 6.5), (9, 41))]:
    pass
assert sp.sqrt(R(24, 10)**2 + 1) == R(26, 10)
assert sp.sqrt(R(65, 10)**2 - R(33, 10)**2) == R(56, 10)
assert sp.sqrt(41**2 - 9**2) == 40
neu(P, 2, 3, "NEU-gemischt-tabelle",
    "Im Dreieck $KLM$ liegt bei $L$ ein rechter Winkel. Überlege "
    "zuerst, welche Seite die Hypotenuse ist. Berechne in jeder Spalte die "
    "fehlende Seite. \\\\ (a) $KL = 2{,}4$ cm, $LM = 1{,}0$ cm, $KM = $ ? "
    "\\\\ (b) $LM = 3{,}3$ dm, $KM = 6{,}5$ dm, $KL = $ ? \\\\ "
    "(c) $KL = 9$ cm, $KM = 4{,}1$ dm, $LM = $ ?", "teil",
    "(a) KM = __ cm (b) KL = __ dm (c) LM = __ cm",
    "Hypotenuse ist $KM$ (gegenüber $L$); (a) $KM = 2{,}6$ cm; "
    "(b) Kathete gesucht: $KL^2 = 42{,}25 - 10{,}89$, $KL = 5{,}6$ dm; "
    "(c) $KM = 41$ cm, $LM^2 = 1\\,681 - 81$, $LM = 40$ cm",
    "[2.6, 5.6, 40]", H, neu_text=STG, neu_merkmal=MKG)
assert sp.sqrt(R(16, 10)**2 + R(63, 10)**2) == R(65, 10)
assert sp.sqrt(R(85, 10)**2 - R(77, 10)**2) == R(36, 10)
assert sp.sqrt(13**2 - 12**2) == 5
neu(P, 2, 3, "NEU-gemischt-tabelle",
    "Im Dreieck $PQR$ liegt bei $P$ ein rechter Winkel. Überlege "
    "zuerst, welche Seite die Hypotenuse ist. Berechne in jeder Spalte die "
    "fehlende Seite. \\\\ (a) $PQ = 1{,}6$ m, $PR = 6{,}3$ m, $QR = $ ? "
    "\\\\ (b) $QR = 8{,}5$ cm, $PQ = 7{,}7$ cm, $PR = $ ? \\\\ "
    "(c) $PR = 12$ dm, $QR = 1{,}3$ m, $PQ = $ ?", "teil",
    "(a) QR = __ m (b) PR = __ cm (c) PQ = __ dm",
    "Hypotenuse ist $QR$ (gegenüber $P$); (a) $QR = 6{,}5$ m; "
    "(b) Kathete gesucht: $PR^2 = 72{,}25 - 59{,}29$, $PR = 3{,}6$ cm; "
    "(c) $QR = 13$ dm, $PQ^2 = 169 - 144$, $PQ = 5$ dm",
    "[6.5, 3.6, 5]", H, neu_text=STG, neu_merkmal=MKG)

# ================= pythagoras e2 k3 s8: Umkehrung, Einheiten, Ecke ====
H = "S. 83 Nr. 17 – Umkehrung: Seiten in verschiedenen Einheiten, ggf. die Ecke des rechten Winkels angeben"
assert 7**2 + 24**2 == 25**2
neu(P, 2, 3, 8,
    "Im Dreieck $ABC$ ist $AB = 2{,}5$ dm, $BC = 7$ cm und $AC = 24$ cm. "
    "Ist das Dreieck rechtwinklig? Wenn ja: An welcher Ecke liegt der "
    "rechte Winkel?", "teil", "",
    "in cm: $AB = 25$ ist die längste Seite; $7^2 + 24^2 = 625$ und "
    "$25^2 = 625$, gleich – rechtwinklig, der rechte Winkel liegt bei $C$ "
    "(gegenüber $AB$)", "[625, 625]", H)
assert 60**2 + 90**2 == 11700 and 110**2 == 12100
neu(P, 2, 3, 8,
    "Im Dreieck $ABC$ ist $AB = 1{,}1$ m, $BC = 60$ cm und $AC = 0{,}9$ m. "
    "Ist das Dreieck rechtwinklig? Wenn ja: An welcher Ecke liegt der "
    "rechte Winkel?", "teil", "",
    "in cm: $AB = 110$ ist die längste Seite; $60^2 + 90^2 = 11\\,700$, "
    "aber $110^2 = 12\\,100$ – nicht rechtwinklig", "[11700, 12100]", H)
assert 20**2 + 21**2 == 29**2
neu(P, 2, 3, 8,
    "Im Dreieck $ABC$ ist $AB = 2{,}0$ dm, $AC = 21$ cm und $BC = 0{,}29$ m. "
    "Ist das Dreieck rechtwinklig? Wenn ja: An welcher Ecke liegt der "
    "rechte Winkel?", "teil", "",
    "in cm: $BC = 29$ ist die längste Seite; $20^2 + 21^2 = 841$ und "
    "$29^2 = 841$, gleich – rechtwinklig, der rechte Winkel liegt bei $A$ "
    "(gegenüber $BC$)", "[841, 841]", H)

# ================= pythagoras e2 NEU-hoehensatz-kathetensatz ==========
STH = ("NEU-hoehensatz-kathetensatz: Höhe aus den Hypotenusenabschnitten "
       "(h² = p · q) oder Kathete aus Hypotenuse und Abschnitt (a² = c · p) "
       "(Vorrat, nur GYM; Vorschlag; im Katalog unter „Nicht aufgenommen“)")
MKH = "Abschnitte p und q statt zweier Seiten; Produkt statt Summe der Quadrate"
H = "S. 82 Nr. 11/12 – aus zwei Stücken (p, q, h, c) die übrigen Seiten und die Höhe mit Höhen- und Kathetensatz"
p_, q_ = R(18, 10), R(32, 10)
assert sp.sqrt(p_ * q_) == R(24, 10) and sp.sqrt((p_ + q_) * p_) == 3 \
    and sp.sqrt((p_ + q_) * q_) == 4
neu(P, 2, 3, "NEU-hoehensatz-kathetensatz",
    "Im Dreieck $ABC$ liegt bei $C$ ein rechter Winkel. Die Höhe $h$ teilt "
    "die Hypotenuse in $p = 1{,}8$ cm (bei $B$) und $q = 3{,}2$ cm (bei $A$). "
    "Berechne $h$ mit dem Höhensatz und die Katheten $a$ und $b$ mit dem "
    "Kathetensatz.", "teil", "h = __ cm, a = __ cm, b = __ cm",
    "$h^2 = p \\cdot q = 5{,}76$, $h = 2{,}4$ cm; $c = p + q = 5$ cm; "
    "$a^2 = c \\cdot p = 9$, $a = 3$ cm; $b^2 = c \\cdot q = 16$, "
    "$b = 4$ cm", "[5.76, 2.4, 5, 9, 3, 16, 4]", H, neu_text=STH,
    neu_merkmal=MKH)
h_, p_ = 10, 5
q_ = R(h_**2, p_)
assert q_ == 20 and (p_ + q_) * p_ == 125 and (p_ + q_) * q_ == 500
neu(P, 2, 3, "NEU-hoehensatz-kathetensatz",
    "Im Dreieck $ABC$ liegt bei $C$ ein rechter Winkel. Die Höhe auf die "
    "Hypotenuse ist $h = 10$ cm lang, der Hypotenusenabschnitt bei $B$ ist "
    "$p = 5$ cm. Berechne $q$, die Hypotenuse $c$ und die Katheten $a$ und "
    "$b$. Runde auf eine Stelle nach dem Komma.", "teil",
    "q = __ cm, c = __ cm, a ≈ __ cm, b ≈ __ cm",
    "$q = h^2 : p = 100 : 5 = 20$ cm; $c = 25$ cm; $a^2 = 25 \\cdot 5 = 125$, "
    "$a \\approx 11{,}2$ cm; $b^2 = 25 \\cdot 20 = 500$, $b \\approx 22{,}4$ cm",
    f"[20, 25, 125, {rund(sp.sqrt(125))}, 500, {rund(sp.sqrt(500))}]", H,
    neu_text=STH, neu_merkmal=MKH)

# ================= pythagoras e3 k2 s8: Koordinaten mit Dezimalen =====
H = "S. 79 Nr. 3 – Abstand zweier Punkte, auch negative Koordinaten mit Dezimalstellen"
assert R(45, 10)**2 + 6**2 == R(5625, 100)
neu(P, 3, 2, 8,
    "Gegeben sind die Punkte $P(-1{,}5 | 2)$ und $Q(3 | -4)$. Berechne die "
    "Länge der Strecke $PQ$.", "teil", "PQ = __",
    "x-Unterschied $4{,}5$, y-Unterschied $6$; $PQ^2 = 56{,}25$, $PQ = 7{,}5$",
    "[56.25, 7.5]", H)
assert 4**2 + 2**2 == 20
neu(P, 3, 2, 8,
    "Gegeben sind die Punkte $R(-2{,}5 | -1{,}5)$ und $S(1{,}5 | 0{,}5)$. "
    "Berechne die Länge der Strecke $RS$. Runde auf eine Stelle nach dem "
    "Komma.", "teil", "RS ≈ __",
    "x-Unterschied $4$, y-Unterschied $2$; $RS^2 = 20$, $RS \\approx 4{,}5$",
    f"[20, {rund(sp.sqrt(20))}]", H)

# ================= pythagoras e3 k2 s14: Würfel =======================
H = "S. 79 Nr. 4 – Flächendiagonale und Raumdiagonale eines Würfels"
for (a_, ein) in [(6, "cm"), (40, "mm")]:
    fd2, rd2 = 2 * a_**2, 3 * a_**2
    neu(P, 3, 2, 14,
        f"Ein Würfel hat die Kantenlänge ${a_}$ {ein}. Die Figur zeigt den "
        "Würfel. Berechne zuerst die Diagonale einer Seitenfläche, dann die "
        "Raumdiagonale. Runde auf eine Stelle nach dem Komma.", "teil",
        f"Flächendiagonale ≈ __ {ein}, Raumdiagonale ≈ __ {ein}",
        f"Flächendiagonale$^2 = {a_}^2 + {a_}^2 = {tz(fd2)}$, "
        f"Flächendiagonale $\\approx {dz(rund(sp.sqrt(fd2)))}$ {ein}; "
        f"Raumdiagonale$^2 = {tz(fd2)} + {a_}^2 = {tz(rd2)}$, "
        f"Raumdiagonale $\\approx {dz(rund(sp.sqrt(rd2)))}$ {ein}",
        f"[{fd2}, {rund(sp.sqrt(fd2))}, {rd2}, {rund(sp.sqrt(rd2))}]", H,
        grafik="\\quader{3}{3}{3}{}{}{}")

# ================= pythagoras e3 k2 s6: Rechteck aus dem Umfang =======
H = "S. 79 Nr. 7b – Rechteck aus Umfang und Seitenunterschied, dann Diagonale und Fläche"
x = sp.symbols("x")
s1 = sp.solve(2 * (x + x + 7) - 46, x)[0]
assert s1 == 8 and sp.sqrt(8**2 + 15**2) == 17
neu(P, 3, 2, 6,
    "Ein Rechteck hat den Umfang $46$ cm. Eine Seite ist $7$ cm länger als "
    "die andere. Bestimme zuerst die beiden Seiten. Berechne dann den "
    "Flächeninhalt und die Länge der Diagonale.", "teil",
    "Seiten __ cm und __ cm, A = __ cm², d = __ cm",
    "$2 \\cdot (x + x + 7) = 46$, $x = 8$; Seiten $8$ cm und $15$ cm; "
    "$A = 120$ cm²; $d^2 = 64 + 225 = 289$, $d = 17$ cm",
    "[8, 120, 289, 17]", H)

# ================= pythagoras e3 NEU-quadrat-diagonale ================
STQ = ("NEU-quadrat-diagonale: Seite des Quadrats aus der Diagonalen – "
       "beide Katheten gleich, a² + a² = d², dann Umfang und Fläche; "
       "größter quadratischer Balken aus einem runden Stamm (Vorschlag; "
       "nicht im Katalog)")
MKQ = "rückwärts: zwei gleiche unbekannte Katheten, 2a² = d²"
H = "S. 79 Nr. 7a und Nr. 6 – Quadrat aus der Diagonalen; größtes Quadrat im Kreis"
a2 = sp.solve(2 * x**2 - 100, x)[1]**2
assert a2 == 50
neu(P, 3, 2, "NEU-quadrat-diagonale",
    "Die Diagonale eines Quadrats ist $10$ cm lang. Berechne die Seitenlänge "
    "$a$, den Umfang und den Flächeninhalt. Runde auf eine Stelle nach dem "
    "Komma.", "teil", "a ≈ __ cm, U ≈ __ cm, A = __ cm²",
    "$a^2 + a^2 = 10^2$, $2a^2 = 100$, $a^2 = 50$; $a \\approx 7{,}1$ cm; "
    "$U = 4a \\approx 28{,}3$ cm; $A = a^2 = 50$ cm²",
    f"[50, {rund(sp.sqrt(50))}, {rund(4 * sp.sqrt(50))}, 50]", H,
    neu_text=STQ, neu_merkmal=MKQ)
assert sp.Rational(40**2, 2) == 800
neu(P, 3, 2, "NEU-quadrat-diagonale",
    "Aus einem runden Baumstamm mit $40$ cm Durchmesser soll ein Balken mit "
    "quadratischem Querschnitt gesägt werden, so groß wie möglich. Die "
    "Diagonale des Quadrats ist dann der Durchmesser. Wie lang ist eine "
    "Seite, wie groß ist die Querschnittsfläche?", "teil",
    "a ≈ __ cm, A = __ cm²",
    "$2a^2 = 40^2 = 1\\,600$, $a^2 = 800$; $a \\approx 28{,}3$ cm; "
    "Querschnittsfläche $A = a^2 = 800$ cm²",
    f"[1600, 800, {rund(sp.sqrt(800))}, 800]", H,
    neu_text=STQ, neu_merkmal=MKQ)

# ================= pythagoras e3 k2 s2 und s1: Wäscheleine ============
H = "S. 82 Nr. 16a – gespannte Leine mit Durchhang in der Mitte: Schenkel aus halbem Abstand und Durchhang"
assert R(24, 10)**2 + R(7, 10)**2 == R(625, 100)
neu(P, 3, 2, 2,
    "Zwei Pfosten stehen $4{,}8$ m auseinander. Dazwischen hängt eine Leine, "
    "die in der Mitte $0{,}7$ m durchhängt. Jede Hälfte der Leine ist "
    "gerade. Wie lang ist die Leine? Um wie viel ist sie länger als der "
    "Abstand der Pfosten?", "teil", "Leine = __ m, länger um __ cm",
    "halber Abstand $2{,}4$ m; Hälfte$^2 = 2{,}4^2 + 0{,}7^2 = 6{,}25$, "
    "Hälfte $= 2{,}5$ m; Leine $= 5$ m; Unterschied $= 20$ cm",
    "[6.25, 2.5, 5, 20]", H)
H = "S. 82 Nr. 16b – Leine um einen Prozentsatz dehnbar: größter Durchhang als Höhe im gleichschenkligen Dreieck"
L = 4 * R(104, 100)
hh = sp.sqrt((L / 2)**2 - 2**2)
assert L == R(416, 100)
neu(P, 3, 2, 1,
    "Eine Leine ist zwischen zwei Pfosten im Abstand von $4$ m straff "
    "gespannt. Sie lässt sich um $4\\,\\%$ dehnen. Wie tief kann sie in der "
    "Mitte höchstens durchhängen? Runde auf ganze Zentimeter.", "teil",
    "Durchhang ≈ __ cm",
    "gedehnte Länge $4 \\cdot 1{,}04 = 4{,}16$ m, Hälfte $2{,}08$ m; "
    "$h^2 = 2{,}08^2 - 2^2 = 0{,}3264$; $h \\approx 0{,}57$ m $= 57$ cm",
    f"[4.16, 0.3264, {round(float(hh), 2)}, {round(float(hh) * 100)}]", H)

# ================= pythagoras e3 NEU-tangente-kreis ===================
STK = ("NEU-tangente-kreis: Sichtweite bis zum Horizont – der Sehstrahl "
       "berührt die Erdkugel, rechter Winkel zwischen Radius und Sehstrahl, "
       "(r + h)² = r² + s² (Vorrat, GYM; Vorschlag; nicht im Katalog)")
MKK = "rechter Winkel aus Tangente und Radius, nicht aus der Figur"
H = "S. 80 Nr. 8 – Sichtweite zum Horizont aus Höhe und Erdradius (Tangente am Kreis)"
s2 = R(637005, 100)**2 - 6370**2
assert s2 == R(6370025, 10000)
neu(P, 3, 2, "NEU-tangente-kreis",
    "Ein Leuchtturm ist $50$ m hoch. Wie weit kann man von seiner Spitze "
    "aus bei klarer Sicht bis zum Horizont sehen? Der Erdradius beträgt "
    "etwa $6\\,370$ km. Der Sehstrahl berührt die "
    "Erde, am Berührpunkt steht er senkrecht auf dem Radius. Runde auf "
    "eine Stelle nach dem Komma.", "teil", "s ≈ __ km",
    "Hypotenuse $6\\,370{,}05$ km (Radius plus Turmhöhe), Kathete "
    "$6\\,370$ km; $s^2 = 6\\,370{,}05^2 - 6\\,370^2 \\approx 637$; "
    "$s \\approx 25{,}2$ km",
    f"[{round(float(s2))}, {rund(sp.sqrt(s2))}]", H,
    neu_text=STK, neu_merkmal=MKK)

# ================= trigonometrie e1 k3 s0: Begriffe ergänzen ==========
H = "S. 85 Nr. 20 – Begriffe am Dreieck ergänzen: rechter Winkel, Hypotenuse, An- und Gegenkathete zu jedem Winkel"
neu(T, 1, 3, 0,
    "Die Figur zeigt ein Dreieck mit rechtem Winkel bei $A$. Ergänze: "
    "(a) Die Hypotenuse ist … (b) Die Gegenkathete zu $\\varepsilon$ ist … "
    "(c) Die Ankathete zu $\\varepsilon$ ist … (d) Die Gegenkathete zu "
    "$\\delta$ ist … (e) Die Ankathete zu $\\delta$ ist … (f) Gibt es eine "
    "Gegenkathete zum rechten Winkel?", "text", "",
    "(a) $k$ (b) $l$ (c) $m$ (d) $m$ (e) $l$ (f) nein – gegenüber dem "
    "rechten Winkel liegt die Hypotenuse; Gegen- und Ankathete gibt es nur "
    "zu den spitzen Winkeln", "", H,
    grafik="\\dreieck{(0,0)}{(6,0)}{(0,3.5)}{k}{l}{m}{}{\\varepsilon}{\\delta}")
neu(T, 1, 3, 0,
    "Die Figur zeigt ein Dreieck mit rechtem Winkel bei $C$. Ergänze: "
    "(a) Die Hypotenuse ist … (b) Die Gegenkathete zu $\\varphi$ ist … "
    "(c) Die Ankathete zu $\\varphi$ ist … (d) Die Gegenkathete zu "
    "$\\varepsilon$ ist … (e) Die Ankathete zu $\\varepsilon$ ist … (f) Gibt es eine "
    "Ankathete zum rechten Winkel?", "text", "",
    "(a) $z$ (b) $x$ (c) $y$ (d) $y$ (e) $x$ (f) nein – beide Katheten "
    "liegen am rechten Winkel; An- und Gegenkathete gibt es nur zu den "
    "spitzen Winkeln", "", H,
    grafik="\\dreieck{(0,0)}{(5,0)}{(1.8,2.4)}{x}{y}{z}{\\varphi}{\\varepsilon}{}")

# ================= trigonometrie e1 k3 s1: Lücken in Gleichungen ======
H = "S. 85 Nr. 21 – Gleichungen zum Dreieck vervollständigen, auch den Winkel oder die Funktion ergänzen"
# Dreieck A(0,0) B(5,0) C(5,3): r = BC, t = AC (Hyp.), s = AB; α bei A, β bei C
neu(T, 1, 3, 1,
    "Die Figur zeigt ein Dreieck mit rechtem Winkel bei $B$. Ergänze den "
    "fehlenden Winkel oder die fehlende Funktion: \\\\ "
    "(a) $\\mathrm{sin}$ __ $= \\frac{r}{t}$ \\quad (b) $\\mathrm{cos}$ __ "
    "$= \\frac{r}{t}$ \\quad (c) __ $\\alpha = \\frac{s}{t}$ \\quad "
    "(d) $\\mathrm{tan}$ __ $= \\frac{s}{r}$", "teil", "",
    "(a) $\\alpha$ (b) $\\beta$ (c) $\\mathrm{cos}$ (d) $\\beta$", "", H,
    grafik="\\dreieck{(0,0)}{(5,0)}{(5,3)}{r}{t}{s}{\\alpha}{}{\\beta}")
# Dreieck A(0,0) B(4,0) C(0,3): u = BC (Hyp.), v = AC, w = AB; β bei B, γ bei C
neu(T, 1, 3, 1,
    "Die Figur zeigt ein Dreieck mit rechtem Winkel bei $A$. Ergänze den "
    "fehlenden Winkel oder die fehlende Funktion: \\\\ "
    "(a) $\\mathrm{sin}$ __ $= \\frac{w}{u}$ \\quad (b) __ $\\beta = "
    "\\frac{w}{u}$ \\quad (c) $\\mathrm{tan}$ __ $= \\frac{v}{w}$ \\quad "
    "(d) __ $\\gamma = \\frac{v}{u}$", "teil", "",
    "(a) $\\gamma$ (b) $\\mathrm{cos}$ (c) $\\beta$ (d) $\\mathrm{cos}$",
    "", H, grafik="\\dreieck{(0,0)}{(4,0)}{(0,3)}{u}{v}{w}{}{\\beta}{\\gamma}")

# ================= trigonometrie e2 k1 s5: alle Stücke ================
H = "S. 85 Nr. 23 – fehlende Stücke im Dreieck mit γ = 90°, zuerst die Winkel, Einheiten gemischt"
be = math.degrees(math.asin(4.8 / 8))
assert sp.sqrt(64 - R(48, 10)**2) == R(64, 10)
neu(T, 2, 1, 5,
    "Im Dreieck $ABC$ ist $\\gamma = 90^\\circ$, $b = 4{,}8$ cm und "
    "$c = 0{,}8$ dm. Berechne zuerst die Winkel $\\beta$ und $\\alpha$, dann "
    "die Seite $a$.", "teil",
    "$\\beta \\approx$ __ $^\\circ$, $\\alpha \\approx$ __ $^\\circ$, a = __ cm",
    "$c = 8$ cm; $\\mathrm{sin}\\,\\beta = \\frac{4{,}8}{8} = 0{,}6$, "
    f"$\\beta \\approx {str(round(be, 1)).replace('.', '{,}')}^\\circ$; "
    f"$\\alpha \\approx {str(round(90 - be, 1)).replace('.', '{,}')}^\\circ$; "
    "$a^2 = 64 - 23{,}04 = 40{,}96$, $a = 6{,}4$ cm",
    "[math.degrees(math.asin(0.6)), 90-math.degrees(math.asin(0.6)), 40.96, 6.4]", H)
al = math.degrees(math.atan(35 / 120))
assert sp.sqrt(35**2 + 120**2) == 125
neu(T, 2, 1, 5,
    "Im Dreieck $ABC$ ist $\\gamma = 90^\\circ$, $a = 0{,}35$ m und "
    "$b = 120$ cm. Berechne zuerst die Winkel $\\alpha$ und $\\beta$, dann "
    "die Seite $c$.", "teil",
    "$\\alpha \\approx$ __ $^\\circ$, $\\beta \\approx$ __ $^\\circ$, c = __ cm",
    "$a = 35$ cm; $\\mathrm{tan}\\,\\alpha = \\frac{35}{120}$, "
    f"$\\alpha \\approx {str(round(al, 1)).replace('.', '{,}')}^\\circ$; "
    f"$\\beta \\approx {str(round(90 - al, 1)).replace('.', '{,}')}^\\circ$; "
    "$c^2 = 1\\,225 + 14\\,400 = 15\\,625$, $c = 125$ cm",
    "[math.degrees(math.atan(35/120)), 90-math.degrees(math.atan(35/120)), 15625, 125]", H)

# ================= trigonometrie e2 k1 s9: Dachsparren ================
H = "S. 85 Nr. 24 – Dachsparren mit Überstand: erst den Überstand abziehen, dann Neigungswinkel und Giebelbreite"
w = math.degrees(math.asin(3.4 / 5.7))
hb = math.sqrt(5.7**2 - 3.4**2)
neu(T, 2, 1, 9,
    "Ein Satteldach ist im Giebel ein gleichschenkliges Dreieck mit der "
    "Höhe $3{,}40$ m. Jeder Sparren ist $6{,}20$ m lang und steht unten "
    "$50$ cm über die Hauswand hinaus. Berechne den Neigungswinkel "
    "$\\alpha$ des Dachs und die Breite des Giebels.", "teil",
    "$\\alpha \\approx$ __ $^\\circ$, Breite ≈ __ m",
    "Sparren bis zur Wand $6{,}20 - 0{,}50 = 5{,}70$ m; "
    "$\\mathrm{sin}\\,\\alpha = \\frac{3{,}40}{5{,}70}$, "
    f"$\\alpha \\approx {str(round(w, 1)).replace('.', '{,}')}^\\circ$; "
    f"halbe Breite $\\approx {str(round(hb, 2)).replace('.', '{,}')}$ m; "
    f"Breite $\\approx {str(round(2 * hb, 1)).replace('.', '{,}')}$ m",
    f"[math.degrees(math.asin(3.4/5.7)), {round(hb, 2)}, {round(2 * hb, 1)}]", H)

# ================= trigonometrie e3 k1 s0: Giebel nachfahren ==========
H = "S. 85 Nr. 24 – im Giebel das rechtwinklige Teildreieck finden (Höhe einzeichnen)"
neu(T, 3, 1, 0,
    "Die Figur zeigt den Giebel eines Hauses als gleichschenkliges Dreieck. "
    "Zeichne die Höhe von der Spitze auf die Grundseite ein. Fahre das "
    "linke Teildreieck mit dem Stift nach. Schreibe an seine Seiten H "
    "(Hypotenuse), G (Gegenkathete) oder A (Ankathete). Schau dabei vom "
    "Winkel $\\alpha$ aus.", "text", "",
    "linkes Teildreieck aus linkem Sparren, Höhe und halber Grundseite: "
    "Sparren H, Höhe G, halbe Grundseite A", "", H,
    grafik="\\dreieck{(0,0)}{(6,0)}{(3,2.2)}{}{}{}{\\alpha}{}{}")

with open("neu-pyt-duden9.jsonl", "w", encoding="utf-8", newline="\n") as fh:
    for z in zeilen:
        fh.write(json.dumps(z, ensure_ascii=False) + "\n")
from collections import Counter
print(len(zeilen), "Zeilen, Lösungen nachgerechnet")
for kk, n in Counter((z["eintrag"], z["einheit"], z["sprosse"]) for z in zeilen).items():
    print(kk, n)
