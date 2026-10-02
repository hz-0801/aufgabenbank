#!/usr/bin/env python3
"""Baut neu-quadratische-funktionen-duden9.jsonl und rechnet jede
Lösung mit sympy nach. Vom Buch nur Typ und Stufung; Zahlen und
Wortlaut eigen."""
import json
import sympy as sp

x = sp.symbols("x")
E = "quadratische-funktionen"
Q = "Duden WÜT Mathematik 9 (2017)"
R = sp.Rational
zeilen = []

K1 = "Normalparabel und Streckfaktor"
K2 = "Scheitelpunktform"
K3 = "Normalform"
K4 = "Nullstellen und Schnittpunkte"


def neu(einheit, kette, sprosse, sprosse_text, merkmal, var, aufgabe,
        form, antwort, loesung, pruef, quelle, herkunft, grafik="",
        hoehe="sprosse"):
    zeilen.append({
        "id": f"{E}-e{einheit}-k1-s{sprosse}-v{var}",
        "eintrag": E, "einheit": einheit, "kette": kette,
        "kette_nr": 1, "sprosse": sprosse,
        "sprosse_text": sprosse_text, "merkmal": merkmal,
        "hoehe": hoehe, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": quelle,
        "herkunft": f"{Q}, {herkunft}"})


def scheitel(f):
    """Scheitel (d, e) eines quadratischen Terms."""
    d = sp.solve(sp.diff(f, x), x)[0]
    return d, sp.simplify(f.subs(x, d))


def gleich(a, b):
    assert sp.simplify(a - b) == 0, (a, b)


def nullst(f):
    return sorted(sp.solveset(f, x, domain=sp.S.Reals), reverse=True)


# ---------------- e1, Kette 1 ----------------
ST0 = "Gerade oder Parabel ankreuzen (Vorstufe)"
MK0 = "linear oder quadratisch erkennen, nichts rechnen"
H = "S. 28 Nr. 1 – Funktionsgleichungen in ungeordneter Form als quadratisch erkennen"
assert sp.degree(6 + 2*x - x**2, x) == 2 and sp.degree(3*x - 7 + 4*x, x) == 1
neu(1, K1, 0, ST0, MK0, 5,
    "Kreuze an, ob der Graph von $f(x) = 6 + 2x - x^2$ eine Gerade oder "
    "eine Parabel ist. \\kreuz{Gerade} \\kreuz{Parabel}", "ankreuzen", "",
    "Parabel", "", 101, H, hoehe="vorstufe")
neu(1, K1, 0, ST0, MK0, 6,
    "Kreuze an, ob der Graph von $f(x) = 3x - 7 + 4x$ eine Gerade oder "
    "eine Parabel ist. \\kreuz{Gerade} \\kreuz{Parabel}", "ankreuzen", "",
    "Gerade", "", 101, H, hoehe="vorstufe")

ST1 = "Wertetabelle zu x² ausfüllen, auch negative x (4×)"
xs = [R(-5, 2), R(-3, 2), R(-1, 2), R(1, 2), R(3, 2), R(5, 2)]
assert [v**2 for v in xs] == [R(25, 4), R(9, 4), R(1, 4), R(1, 4), R(9, 4), R(25, 4)]
neu(1, K1, 1, ST1, "Quadrieren in der Tabelle, auch negative x", 6,
    "Fülle die Wertetabelle zu $f(x) = x^2$ aus.\n"
    "\\wertetabelle{x}{f(x)}{-2{,}5,-1{,}5,-0{,}5,0{,}5,1{,}5,2{,}5}",
    "tabelle", "",
    "$6{,}25$; $2{,}25$; $0{,}25$; $0{,}25$; $2{,}25$; $6{,}25$",
    "[6.25, 2.25, 0.25, 0.25, 2.25, 6.25]", 101,
    "S. 28 Nr. 2 – Wertetabelle mit halben x-Werten, auch negativ",
    hoehe="grundfall")

STT = ("NEU-tabelle-verschoben: Wertetabelle zu x² + e ausfüllen und mit "
       "der zu x² vergleichen – jeder Wert um e verschoben, Scheitel "
       "(0 | e) (Vorschlag; nicht im Katalog)")
MKT = "neben x² ein Summand e: jeder Wert verschiebt sich um e"
H = "S. 28 Nr. 2 – Wertetabellen zu x² + c und x² − c ausfüllen und zeichnen"
g = x**2 + 3
assert [g.subs(x, v) for v in (-2, -1, 0, 1, 2)] == [7, 4, 3, 4, 7]
assert scheitel(g) == (0, 3)
neu(1, K1, "NEU-tabelle-verschoben", STT, MKT, 1,
    "Fülle die Wertetabelle zu $g(x) = x^2 + 3$ aus.\n"
    "\\wertetabelle{x}{g(x)}{-2,-1,0,1,2}\n"
    "Vergleiche mit $f(x) = x^2$: Um wie viel unterscheidet sich jeder "
    "Wert? Gib den Scheitel von $g$ an.", "tabelle",
    "Unterschied __, S(__|__)",
    "$7$; $4$; $3$; $4$; $7$; Unterschied $g(x) - f(x) = 3$; "
    "Scheitel $S(0|3)$", "[7, 4, 3, 4, 7, 3, 0, 3]", 101, H)
g = x**2 - 2
assert [g.subs(x, v) for v in (-3, R(-3, 2), 0, R(3, 2), 3)] == [7, R(1, 4), -2, R(1, 4), 7]
neu(1, K1, "NEU-tabelle-verschoben", STT, MKT, 2,
    "Fülle die Wertetabelle zu $g(x) = x^2 - 2$ aus.\n"
    "\\wertetabelle{x}{g(x)}{-3,-1{,}5,0,1{,}5,3}\n"
    "Vergleiche mit $f(x) = x^2$: Um wie viel unterscheidet sich jeder "
    "Wert? Gib den Scheitel von $g$ an.", "tabelle",
    "Unterschied __, S(__|__)",
    "$7$; $0{,}25$; $-2$; $0{,}25$; $7$; Unterschied $g(x) - f(x) = -2$; "
    "Scheitel $S(0|{-2})$", "[7, 0.25, -2, 0.25, 7, -2, 0, -2]", 101, H)

ST6 = "Öffnung und Breite an a erkennen (nach unten, schmaler, breiter)"
MK6 = "nur a ansehen: Vorzeichen für die Öffnung, Betrag für die Breite"
H = "S. 31 Nr. 7 – Öffnung und Streckung/Stauchung ankreuzen, a als Bruch"
for v, (term, a, los) in enumerate([
        ("\\frac{1}{3}x^2", R(1, 3), "nach oben, breiter als die Normalparabel"),
        ("-\\frac{5}{2}x^2", R(-5, 2), "nach unten, schmaler als die Normalparabel")], 4):
    assert (a > 0) == ("oben" in los) and (abs(a) < 1) == ("breiter" in los)
    neu(1, K1, 6, ST6, MK6, v,
        f"Kreuze an, wie die Parabel zu $f(x) = {term}$ geöffnet ist. "
        "Kreuze auch an, ob sie schmaler oder breiter als die "
        "Normalparabel ist. \\kreuz{nach oben} \\kreuz{nach unten} \\\\ "
        "\\kreuz{schmaler} \\kreuz{breiter}", "ankreuzen", "", los, "",
        101, H)

# ---------------- e2, Kette 1 ----------------
ST2 = "d oder e negativ"
MK2 = "Vorzeichen: Plus in der Klammer oder Minus hinten"
H = "S. 31 Nr. 4 – Scheitel ablesen, Sonderfall ohne Summand oder ohne Klammer, Dezimalzahlen"
assert scheitel((x + R(7, 2))**2) == (R(-7, 2), 0)
neu(2, K2, 2, ST2, MK2, 4,
    "Gib den Scheitel der Parabel $f(x) = (x + 3{,}5)^2$ an.", "teil",
    "S(__|__)", "$S(-3{,}5|0)$", "[-3.5, 0]", 102, H)
assert scheitel(x**2 - R(9, 2)) == (0, R(-9, 2))
neu(2, K2, 2, ST2, MK2, 5,
    "Gib den Scheitel der Parabel $f(x) = x^2 - 4{,}5$ an.", "teil",
    "S(__|__)", "$S(0|{-4{,}5})$", "[0, -4.5]", 102, H)

ST4 = "Parabel aus der Gleichung skizzieren (Scheitel setzen, Punkte wie bei der Normalparabel)"
f = (x - R(3, 2))**2 - 2
assert [f.subs(x, v) for v in (R(1, 2), R(5, 2), R(-1, 2), R(7, 2))] == [-1, -1, 2, 2]
neu(2, K2, 4, ST4, "zeichnen statt ablesen: Scheitel setzen, Normalparabel-Schritte", 4,
    "Skizziere die Parabel zu $f(x) = (x - 1{,}5)^2 - 2$ im "
    "Koordinatensystem.", "zeichnen", "",
    "Scheitel $S(1{,}5|{-2})$, dann $1$ nach rechts $1$ nach oben, $2$ "
    "nach rechts $4$ nach oben, nach links genauso: $(0{,}5|{-1})$, "
    "$(2{,}5|{-1})$, $(-0{,}5|2)$, $(3{,}5|2)$", "", 102,
    "S. 31 Nr. 8 – Graph zur Scheitelpunktform zeichnen, Scheitel mit Dezimalzahlen",
    grafik="\\begin{ksys}[xmin=-2,xmax=5,ymin=-3,ymax=5]\n\\end{ksys}")

STS = ("NEU-steigen-fallen: angeben, für welche x die Parabel fällt und "
       "für welche sie steigt – am Scheitel wechselt es (Vorschlag; nicht "
       "im Katalog)")
MKS = "Scheitel als Umkehrstelle: links und rechts davon Fallen und Steigen angeben"
H = "S. 32 Nr. 10 – Monotonieverhalten nach Skizze angeben (auch S. 33 Nr. 11)"
f = (x + 4)**2 - 3
assert scheitel(f) == (-4, -3) and sp.diff(f, x).subs(x, -5) < 0
neu(2, K2, "NEU-steigen-fallen", STS, MKS, 1,
    "Gib an, für welche $x$ der Graph von $f(x) = (x + 4)^2 - 3$ fällt "
    "und für welche $x$ er steigt.", "teil",
    "fällt für x __, steigt für x __",
    "Scheitel $S(-4|{-3})$, nach oben geöffnet: fällt für $x < -4$, "
    "steigt für $x > -4$", "[-4, -3]", 102, H)
f = -(x - 2)**2 + 5
assert scheitel(f) == (2, 5) and sp.diff(f, x).subs(x, 1) > 0
neu(2, K2, "NEU-steigen-fallen", STS, MKS, 2,
    "Gib an, für welche $x$ der Graph von $f(x) = -(x - 2)^2 + 5$ steigt "
    "und für welche $x$ er fällt.", "teil",
    "steigt für x __, fällt für x __",
    "Scheitel $S(2|5)$, nach unten geöffnet: steigt für $x < 2$, fällt "
    "für $x > 2$", "[2, 5]", 102, H)
f = -(x - 1)**2 + 2
assert scheitel(f) == (1, 2)
neu(2, K2, "NEU-steigen-fallen", STS, MKS, 3,
    "Das Koordinatensystem zeigt eine Parabel. In welchem Bereich steigt "
    "der Graph, in welchem fällt er?", "teil",
    "steigt für x __, fällt für x __",
    "Scheitel $S(1|2)$, nach unten geöffnet: steigt für $x < 1$, fällt "
    "für $x > 1$", "[1, 2]", 102, H,
    grafik="\\begin{ksys}[xmin=-2,xmax=4,ymin=-3,ymax=3,ablesen]\n"
    "\\parabel{-1}{1}{2}{f}\n\\end{ksys}")

ST5 = "Gleichung aus dem Scheitel aufstellen"
MK5 = "Umkehrung: vom Scheitel zur Gleichung"
H = "S. 31 Nr. 5 – Gleichung zum Scheitel, Scheitel auf einer Achse, Dezimal- und Bruchzahl"
assert scheitel((x + R(9, 2))**2) == (R(-9, 2), 0)
neu(2, K2, 5, ST5, MK5, 4,
    "Eine Normalparabel ist nach oben geöffnet. Ihr Scheitel ist "
    "$S(-4{,}5|0)$. Stelle ihre Gleichung auf.", "teil", "f(x) = __",
    "$f(x) = (x + 4{,}5)^2$", "4.5", 102, H)
assert scheitel(x**2 + R(2, 3)) == (0, R(2, 3))
neu(2, K2, 5, ST5, MK5, 5,
    "Eine Normalparabel ist nach oben geöffnet. Ihr Scheitel ist "
    "$S(0|\\tfrac{2}{3})$. Stelle ihre Gleichung auf.",
    "teil", "f(x) = __", "$f(x) = x^2 + \\frac{2}{3}$", "[2, 3]", 102, H)

ST6b = "Gleichung aus dem Graphen aufstellen (Scheitel ablesen, Öffnung prüfen, nach unten: Minus vor der Klammer)"
MK6b = "Graph lesen: Scheitel und Öffnung, nach unten Minus vor der Klammer"
neu(2, K2, 6, ST6b, MK6b, 4,
    "Das Koordinatensystem zeigt zwei verschobene Normalparabeln $f$ und "
    "$g$. Stelle beide Gleichungen auf.", "teil",
    "f(x) = __, g(x) = __",
    "$f$: $S(0|{-2})$: $f(x) = x^2 - 2$; $g$: $S(0|1)$: $g(x) = x^2 + 1$",
    "[0, -2, 0, 1]", 102,
    "S. 28 Nr. 3 – mehrere nach oben oder unten verschobene Normalparabeln in einem Bild",
    grafik="\\begin{ksys}[xmin=-3,xmax=3,ymin=-3,ymax=6,ablesen]\n"
    "\\parabel{1}{0}{-2}{f}\n\\parabel{1}{0}{1}{g}\n\\end{ksys}")
neu(2, K2, 6, ST6b, MK6b, 5,
    "Das Koordinatensystem zeigt die Parabeln $f$ und $g$. Sie sind aus "
    "der Normalparabel durch Verschieben und Spiegeln entstanden. Stelle "
    "beide Gleichungen auf.", "teil", "f(x) = __, g(x) = __",
    "$f$: $S(-1|3)$, nach unten geöffnet: $f(x) = -(x + 1)^2 + 3$; $g$: "
    "$S(2|{-1})$, nach oben geöffnet: $g(x) = (x - 2)^2 - 1$",
    "[-1, 3, 2, -1]", 102,
    "S. 32 Nr. 9 – Gleichungen verschobener und gespiegelter Normalparabeln aus einem Bild",
    grafik="\\begin{ksys}[xmin=-4,xmax=5,ymin=-2,ymax=5,ablesen]\n"
    "\\parabel{-1}{-1}{3}{f}\n\\parabel{1}{2}{-1}{g}\n\\end{ksys}")

ST12 = ("Merkmale einer gestreckten oder gestauchten Parabel bestimmen, "
        "indem die Strategien der Normalparabel übertragen werden (ohne "
        "Original; Zielmarke nach RLP und LISUM-PH, zweiter Block beider "
        "Reihen)")
MK12 = "Streckfaktor vor der Klammer: Scheitel, Öffnung, Breite und der Schritt eine Einheit neben dem Scheitel"
H = "S. 33 Nr. 11 – Eigenschaften gestreckter Parabeln, Faktor als Dezimal- oder Bruchzahl (auch S. 31 Nr. 6b)"
f = -R(3, 2)*x**2 + 4
assert scheitel(f) == (0, 4) and f.subs(x, 1) == R(5, 2)
neu(2, K2, 12, ST12, MK12, 4,
    "Betrachte die Parabel zu $f(x) = -1{,}5x^2 + 4$. Gib ihren Scheitel "
    "an. Ist sie nach oben oder nach unten geöffnet? Ist sie schmaler "
    "oder breiter als die Normalparabel? Gib auch den Punkt der Parabel "
    "an, der eine Einheit rechts vom Scheitel liegt.", "teil",
    "S(__|__), Punkt (__|__)",
    "$S(0|4)$, nach unten geöffnet, schmaler; Punkt $(1|2{,}5)$",
    "[0, 4, 1, 2.5]", 102, H)
f = R(1, 4)*(x - 2)**2 - 3
assert scheitel(f) == (2, -3) and f.subs(x, 3) == R(-11, 4)
neu(2, K2, 12, ST12, MK12, 5,
    "Betrachte die Parabel zu $f(x) = \\frac{1}{4}(x - 2)^2 - 3$. Gib "
    "ihren Scheitel an. Ist sie nach oben oder nach unten geöffnet? Ist "
    "sie schmaler oder breiter als die Normalparabel? Gib auch den Punkt "
    "der Parabel an, der eine Einheit rechts vom Scheitel liegt.", "teil",
    "S(__|__), Punkt (__|__)",
    "$S(2|{-3})$, nach oben geöffnet, breiter; Punkt $(3|{-2{,}75})$",
    "[2, -3, 3, -2.75]", 102, H)

# ---------------- e3, Kette 1 ----------------
STQ = ("NEU-quadr-ergaenzung: Scheitelpunktform aus der Normalform ohne "
       "Graph – erst ein vollständiges Quadrat erkennen, dann quadratisch "
       "ergänzen (Vorrat, H, GYM 9; Vorschlag – der Katalog nennt die "
       "Ergänzung als Typ, aber ohne Sprosse)")
MKQ = "ohne Graph: Normalform rechnerisch in die Scheitelpunktform bringen"
H = "S. 34 Nr. 14 – Normalform in die Scheitelpunktform umformen, Scheitel angeben (Wissen S. 30)"
gleich(x**2 + 10*x + 25, (x + 5)**2)
neu(3, K3, "NEU-quadr-ergaenzung", STQ, MKQ, 1,
    "Schreibe $f(x) = x^2 + 10x + 25$ als Quadrat einer Klammer. Gib den "
    "Scheitel der Parabel an.", "gleichungsraster", "f(x) = __, S(__|__)",
    "$f(x) = (x + 5)^2$; $S(-5|0)$", "[-5, 0]", 103, H)
gleich(x**2 - 8*x + 19, (x - 4)**2 + 3)
neu(3, K3, "NEU-quadr-ergaenzung", STQ, MKQ, 2,
    "Bringe $f(x) = x^2 - 8x + 19$ mit quadratischer Ergänzung in die "
    "Scheitelpunktform. Gib den Scheitel an.", "gleichungsraster",
    "f(x) = __, S(__|__)",
    "$f(x) = x^2 - 8x + 16 - 16 + 19 = (x - 4)^2 + 3$; $S(4|3)$",
    "[4, 3]", 103, H)
gleich(x**2 + 3*x + 1, (x + R(3, 2))**2 - R(5, 4))
neu(3, K3, "NEU-quadr-ergaenzung", STQ, MKQ, 3,
    "Bringe $f(x) = x^2 + 3x + 1$ mit quadratischer Ergänzung in die "
    "Scheitelpunktform. Gib den Scheitel an.", "gleichungsraster",
    "f(x) = __, S(__|__)",
    "$f(x) = x^2 + 3x + 2{,}25 - 2{,}25 + 1 = (x + 1{,}5)^2 - 1{,}25$; "
    "$S(-1{,}5|{-1{,}25})$", "[-1.5, -1.25]", 103, H)

# ---------------- e4, Kette 1 ----------------
STN = "Wert unter der Wurzel null: genau eine Nullstelle, Gegenprobe am Scheitel auf der x-Achse"
MKN = "unter der Wurzel steht null: nur eine Nullstelle, der Scheitel liegt auf der x-Achse"
H = "S. 33 Nr. 12 – Nullstellen bestimmen, Fall eine Nullstelle (Wissen Diskriminante)"
for v, (p, q, s) in enumerate([(-10, 25, 5), (8, 16, -4)], 1):
    f = x**2 + p*x + q
    assert nullst(f) == [s] and scheitel(f) == (s, 0)
    pt = f"{p:+d}".replace("+", "+ ").replace("-", "- ")
    w = R(-p, 2)
    ss = f"S({s}|0)"
    neu(4, K4, 4, STN, MKN, v,
        f"Die Parabel $f(x) = x^2 {pt}x + {q}$ hat den Scheitel ${ss}$. "
        "Berechne ihre Nullstellen mit der p-q-Formel. Wie passt das "
        "Ergebnis zum Scheitel?", "gleichungsraster", "x = __",
        f"$0 = x^2 {pt}x + {q}$; $x = {w} \\pm \\sqrt{{{w**2} - {q}}} = "
        f"{w} \\pm 0$; genau eine Nullstelle $x = {s}$; der Scheitel liegt "
        "auf der $x$-Achse, die Parabel berührt sie dort", f"{s}", 104, H)
f = x**2 + 12*x + 36
assert nullst(f) == [-6] and scheitel(f) == (-6, 0)
neu(4, K4, 4, STN, MKN, 3,
    "Berechne die Nullstellen von $f(x) = x^2 + 12x + 36$. Wo liegt der "
    "Scheitel der Parabel?", "gleichungsraster", "x = __, S(__|__)",
    "$0 = x^2 + 12x + 36$; $x = -6 \\pm \\sqrt{36 - 36} = -6 \\pm 0$; "
    "genau eine Nullstelle $x = -6$; der Scheitel liegt auf der "
    "$x$-Achse: $S(-6|0)$", "[-6, -6, 0]", 104, H)

STK = "Wert unter der Wurzel negativ: keine Nullstelle, Gegenprobe an der Lage des Scheitels"
MKK = "unter der Wurzel steht eine negative Zahl: keine Nullstelle, der Scheitel liegt über der x-Achse"
H = "S. 33 Nr. 12 – Nullstellen bestimmen, Fall keine Nullstelle (Wissen Diskriminante)"
for v, (p, q) in enumerate([(-4, 7), (6, 14), (10, 27)], 1):
    f = x**2 + p*x + q
    d, e = scheitel(f)
    w = R(-p, 2)
    dis = w**2 - q
    assert nullst(f) == [] and dis < 0 and e > 0
    pt = f"{p:+d}".replace("+", "+ ").replace("-", "- ")
    es = f"{d}|{e}" if d >= 0 else f"{d}|{e}"
    neu(4, K4, 5, STK, MKK, v,
        f"Die Parabel $f(x) = x^2 {pt}x + {q}$ hat den Scheitel "
        f"$S({es})$. Berechne ihre Nullstellen mit der p-q-Formel. Wie "
        "passt das Ergebnis zum Scheitel?", "gleichungsraster", "",
        f"$0 = x^2 {pt}x + {q}$; $x = {w} \\pm \\sqrt{{{w**2} - {q}}}$; "
        f"Wert unter der Wurzel: ${w**2} - {q} = {dis}$; keine Nullstelle, "
        f"denn aus ${dis}$ gibt es keine Wurzel; der Scheitel liegt über "
        "der $x$-Achse und die Parabel ist nach oben geöffnet",
        f"{dis}", 104, H)

STX = ("NEU-extremwert: größter Flächeninhalt eines Rechtecks bei festem "
       "Umfang – Flächenterm aufstellen, Scheitel in der Mitte der "
       "Nullstellen (Vorrat, GYM 9; Vorschlag; nicht im Katalog)")
MKX = "Term selbst aus der Sache aufstellen; der Scheitel ist der größte Wert"
H = "S. 34 Nr. 15 – Extremwertaufgabe: Rechteck mit festem Zaun, größte Fläche (Wissen Extremwertaufgaben)"
A = x*(12 - x)
assert nullst(A) == [12, 0] and scheitel(A) == (6, 36)
neu(4, K4, "NEU-extremwert", STX, MKX, 1,
    "Ein rechteckiges Beet wird mit $24\\,$m Kantenstein ganz umrandet. "
    "Eine Seite ist $x$ m lang. Stelle den Flächeninhalt $A(x)$ auf. Für "
    "welches $x$ ist das Beet am größten? Wie groß ist es dann?", "teil",
    "x = __ m, A = __ m²",
    "andere Seite $12 - x$; $A(x) = x(12 - x) = -x^2 + 12x$; Nullstellen "
    "$x = 0$ und $x = 12$, der Scheitel liegt in der Mitte: $x = 6$; "
    "$A(6) = 36$; Das Beet ist mit $6\\,$m mal $6\\,$m am größten, es hat "
    "dann $36\\,$m².", "[6, 36]", 104, H)
A = x*(16 - 2*x)
assert nullst(A) == [8, 0] and scheitel(A) == (4, 32)
neu(4, K4, "NEU-extremwert", STX, MKX, 2,
    "Ein rechteckiger Auslauf liegt an einer Hauswand. Die drei übrigen "
    "Seiten werden mit $16\\,$m Zaun begrenzt. Die beiden Seiten, die von "
    "der Wand weggehen, sind je $x$ m lang. Stelle den Flächeninhalt "
    "$A(x)$ auf. Für welches $x$ ist der Auslauf am größten? Wie groß ist "
    "er dann?", "teil", "x = __ m, A = __ m²",
    "Seite an der Wand $16 - 2x$; $A(x) = x(16 - 2x) = -2x^2 + 16x$; "
    "Nullstellen $x = 0$ und $x = 8$, der Scheitel liegt in der Mitte: "
    "$x = 4$; $A(4) = 32$; Die beiden Seiten von der Wand weg sind je "
    "$4\\,$m lang, die Seite an der Wand $8\\,$m; der Auslauf hat dann "
    "$32\\,$m².", "[4, 32]", 104, H)

with open("neu-quadratische-funktionen-duden9.jsonl", "w",
          encoding="utf-8", newline="\n") as fh:
    for z in zeilen:
        fh.write(json.dumps(z, ensure_ascii=False) + "\n")
print(len(zeilen), "Zeilen, alle Lösungen mit sympy nachgerechnet")
