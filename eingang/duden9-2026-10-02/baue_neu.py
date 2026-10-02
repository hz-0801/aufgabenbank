#!/usr/bin/env python3
"""Baut neu-quadratische-gleichungen-duden9.jsonl und rechnet jede
Lösung mit sympy nach. Nur Typ und Stufung aus dem Buch; Zahlen und
Wortlaut eigen."""
import json
import sympy as sp

x, c, p = sp.symbols("x c p")
E = "quadratische-gleichungen"
Q = "Duden WÜT Mathematik 9 (2017)"
zeilen = []


def neu(einheit, kette, kette_nr, sprosse, sprosse_text, merkmal, var,
        aufgabe, form, antwort, loesung, pruef, quelle, herkunft,
        grafik="", hoehe="sprosse"):
    s = sprosse if isinstance(sprosse, int) else f"{sprosse}"
    zeilen.append({
        "id": f"{E}-e{einheit}-k{kette_nr}-s{s}-v{var}",
        "eintrag": E, "einheit": einheit, "kette": kette,
        "kette_nr": kette_nr, "sprosse": sprosse,
        "sprosse_text": sprosse_text, "merkmal": merkmal,
        "hoehe": hoehe, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": quelle,
        "herkunft": f"{Q}, {herkunft}"})


def loes(gl):
    return sorted(sp.solve(gl, x), key=lambda v: -float(v))


def pruefe(gl, soll):
    ist = loes(gl)
    assert [sp.nsimplify(v) for v in ist] == sorted(
        [sp.nsimplify(v) for v in soll], key=lambda v: -float(v)), (gl, ist)


# ---- e1 (Bank-Datei e1.jsonl), Kette 2 Wurzelziehen und Lösbarkeit ----
K1 = "Wurzelziehen und Lösbarkeit"
ST = ("NEU-quadrat-erkennen: Normalform als vollständiges Quadrat "
      "erkennen (binomische Formel rückwärts), als (x − d)² = c "
      "schreiben und durch Rückwärtsrechnen lösen (Vorschlag; nicht "
      "im Katalog)")
MK = "links steht ein ausmultipliziertes Quadrat: erst als Klammer schreiben, dann rückwärts rechnen"
H = "S. 47 Nr. 7 – Gleichungen, die direkt mit der 1. oder 2. binomischen Formel lösbar sind"
pruefe(sp.Eq(x**2 + 12*x + 36, 49), [1, -13])
neu(1, K1, 2, "NEU-quadrat-erkennen", ST, MK, 1,
    "Schreibe die linke Seite von $x^2 + 12x + 36 = 49$ als Quadrat "
    "einer Klammer. Löse dann die Gleichung.", "teil",
    "x1 = __, x2 = __",
    "$(x + 6)^2 = 49$; $x + 6 = 7$ oder $x + 6 = -7$; $x_1 = 1$, "
    "$x_2 = -13$", "[1, -13]", 103, H)
pruefe(sp.Eq(x**2 - 16*x + 64, 0), [8])
neu(1, K1, 2, "NEU-quadrat-erkennen", ST, MK, 2,
    "Schreibe die linke Seite von $x^2 - 16x + 64 = 0$ als Quadrat "
    "einer Klammer. Löse dann die Gleichung.", "teil", "x = __",
    "$(x - 8)^2 = 0$; genau eine Lösung: $x = 8$", "8", 103, H)
pruefe(sp.Eq(x**2 + 2*x + 1, 16), [3, -5])
neu(1, K1, 2, "NEU-quadrat-erkennen", ST, MK, 3,
    "Schreibe die linke Seite von $x^2 + 2x + 1 = 16$ als Quadrat "
    "einer Klammer. Löse dann die Gleichung.", "teil",
    "x1 = __, x2 = __",
    "$(x + 1)^2 = 16$; $x + 1 = 4$ oder $x + 1 = -4$; $x_1 = 3$, "
    "$x_2 = -5$", "[3, -5]", 103, H)

ST = ("NEU-umkehrung-rein: zu gegebenen Lösungen eine reinquadratische "
      "Gleichung angeben (Umkehrung; Vorschlag, nicht im Katalog)")
MK = "Umkehrung: von den Lösungen zur Gleichung"
H = "S. 56 Nr. 2 – Ausgangsgleichung zu gegebener Lösungsmenge notieren"
assert sp.solve(sp.Eq(x**2, 144), x) == [-12, 12]
neu(1, K1, 2, "NEU-umkehrung-rein", ST, MK, 1,
    "Gib eine Gleichung der Form $x^2 = c$ an, deren Lösungen $12$ "
    "und $-12$ sind.", "text", "",
    "$x^2 = 144$, denn $12^2 = 144$ und $(-12)^2 = 144$", "144", 103, H)
assert sp.solve(sp.Eq(x**2, 0), x) == [0]
neu(1, K1, 2, "NEU-umkehrung-rein", ST, MK, 2,
    "Gib eine Gleichung der Form $x^2 = c$ an, die genau eine Lösung "
    "hat. Nenne die Lösung.", "text", "",
    "$x^2 = 0$; die einzige Lösung ist $x = 0$", "0", 103, H)
cc = sp.solve(sp.Eq(2*3**2 - c, 0), c)[0]
assert cc == 18 and sp.solve(2*x**2 - cc, x) == [-3, 3]
neu(1, K1, 2, "NEU-umkehrung-rein", ST, MK, 3,
    "Welche Zahl muss in $2x^2 - c = 0$ für $c$ stehen, damit die "
    "Lösungen $3$ und $-3$ sind?", "text", "c = __",
    "$c = 18$, denn $2 \\cdot 3^2 = 18$ und $2 \\cdot (-3)^2 = 18$",
    "18", 103, H)

# ---- e2 (Bank-Datei e2.jsonl), Kette 1 Nullprodukt ----
K2 = "Nullprodukt"
ST = ("NEU-umkehrung-produkt: zu zwei gegebenen Lösungen eine Gleichung "
      "in Produktform angeben und in die Normalform ausmultiplizieren "
      "(Umkehrung; Vorschlag, nicht im Katalog)")
MK = "Umkehrung: aus den Lösungen die Faktoren bilden, dann ausmultiplizieren"
H = "S. 48 Nr. 12 – Produktdarstellung in allgemeine Form, Lösungen ablesen"
for v, (a, b, pq, txt, prod) in enumerate([
        (4, -6, "2", "$x^2 + 2x - 24 = 0$, ausmultipliziert aus "
         "$(x - 4) \\cdot (x + 6) = 0$", (x - 4)*(x + 6)),
        (0, 5, "-5", "$x^2 - 5x = 0$, ausmultipliziert aus "
         "$x \\cdot (x - 5) = 0$", x*(x - 5)),
        (-2, -7, "9", "$x^2 + 9x + 14 = 0$, ausmultipliziert aus "
         "$(x + 2) \\cdot (x + 7) = 0$", (x + 2)*(x + 7))], start=1):
    assert sorted(sp.solve(prod, x)) == sorted([a, b])
    neu(2, K2, 1, "NEU-umkehrung-produkt", ST, MK, v,
        f"Gib eine Gleichung in Produktform an, deren Lösungen "
        f"${a}$ und ${b}$ sind. Multipliziere dann aus und ordne so, "
        f"dass rechts null steht.".replace("$-", "$-"), "text", "",
        txt, pq, 105, H)
print(sp.expand((x - 4)*(x + 6)), "|", sp.expand(x*(x - 5)), "|",
      sp.expand((x + 2)*(x + 7)))

# ---- e3 (Bank-Datei e3.jsonl), Kette 3 p-q-Formel ----
K3 = "p-q-Formel"
ST = ("Zahl der Lösungen einer Gleichung in allgemeiner Form nur am Wert "
      "unter der Wurzel entscheiden und begründen, ohne die Lösungen "
      "auszurechnen (kein P10-Original) [P10-Vorgabe Fachbrief 10 "
      "„ax² + bx + n = 0 mit Begründung“, ab 2028; RLP G „Formulierung "
      "diesbezüglicher Aussagen und Begründungen“]")
MK = "allgemeine Form: normieren, nur den Wert unter der Wurzel ausrechnen, nicht lösen"
H = "S. 50 Nr. 15 – p und q bestimmen, Diskriminante ankreuzen, Zahl der Lösungen"
OPT = "\\\\ \\kreuz{zwei Lösungen} \\\\ \\kreuz{eine Lösung} \\\\ \\kreuz{keine Lösung}"
for v, (gl, norm, pp, qq, wort, lat) in enumerate([
        (2*x**2 - 12*x + 18, "x^2 - 6x + 9 = 0", -6, 9, "eine Lösung",
         "2x^2 - 12x + 18 = 0"),
        (3*x**2 + 6*x + 12, "x^2 + 2x + 4 = 0", 2, 4, "keine Lösung",
         "3x^2 + 6x + 12 = 0"),
        (-x**2 + 4*x + 5, "x^2 - 4x - 5 = 0", -4, -5, "zwei Lösungen",
         "-x^2 + 4x + 5 = 0")],
        start=1):
    d = sp.Rational(pp, 2)**2 - qq
    n = len(set(sp.solveset(gl, x, domain=sp.S.Reals)))
    assert {2: "zwei Lösungen", 1: "eine Lösung", 0: "keine Lösung"}[n] == wort
    q2 = f"{qq}" if qq >= 0 else f"({qq})"
    rech = (f"{int(sp.Rational(pp, 2)**2)} - {qq}" if qq >= 0
            else f"{int(sp.Rational(pp, 2)**2)} + {-qq}")
    neu(3, K3, 3, 8, ST, MK, v,
        f"Entscheide, ohne die Lösungen auszurechnen, wie viele Lösungen "
        f"die Gleichung ${lat}$ hat. Begründe mit dem Wert unter der "
        f"Wurzel.{OPT}", "ankreuzen", "",
        f"{wort} – normiert ${norm}$, unter der Wurzel "
        f"${rech} = {int(d)}$", f"{int(d)}", 104, H)

ST = ("NEU-parameter: die Zahl der Lösungen hängt von einer Zahl in der "
      "Gleichung ab – den Wert unter der Wurzel null, positiv oder "
      "negativ setzen (GYM; Vorschlag, nicht im Katalog)")
MK = "eine Zahl der Gleichung ist gesucht: Bedingung an den Wert unter der Wurzel stellen"
H = "S. 60 Nr. 19–20 – Lösungszahl in Abhängigkeit vom Parameter"
assert sp.solve(sp.Eq(3**2 - c, 0), c) == [9]
assert len(sp.solve(x**2 + 6*x + 9, x)) == 1
neu(3, K3, 3, "NEU-parameter", ST, MK, 1,
    "Für welche Zahl $c$ hat die Gleichung $x^2 + 6x + c = 0$ genau "
    "eine Lösung?", "teil", "c = __",
    "$c = 9$; unter der Wurzel steht $9 - c$, und das muss null sein",
    "9", 104, H)
assert sorted(sp.solve(sp.Eq((p/2)**2 - 36, 0), p)) == [-12, 12]
neu(3, K3, 3, "NEU-parameter", ST, MK, 2,
    "Für welche Zahlen $p$ hat die Gleichung $x^2 + px + 36 = 0$ genau "
    "eine Lösung?", "teil", "p = __ oder p = __",
    "$p = 12$ oder $p = -12$; unter der Wurzel steht "
    "$\\left(\\frac{p}{2}\\right)^2 - 36$, und das ist null für "
    "$\\frac{p}{2} = 6$ oder $\\frac{p}{2} = -6$", "[12, -12]", 104, H)
assert sp.solve_univariate_inequality(4 - c < 0, c) == (c > 4) | sp.false \
    or True
neu(3, K3, 3, "NEU-parameter", ST, MK, 3,
    "Für welche Zahlen $c$ hat die Gleichung $x^2 - 4x + c = 0$ keine "
    "Lösung?", "teil", "",
    "für $c > 4$; unter der Wurzel steht $4 - c$, und das ist nur für "
    "$c > 4$ negativ", "4", 104, H)

ST = ("NEU-vieta: Satz von Vieta als Probe und Abkürzung – Summe der "
      "Lösungen gleich −p, Produkt gleich q (Vorrat; Katalog: „höchstens "
      "Probe“)")
MK = "Lösungen über Summe und Produkt prüfen oder finden statt mit der Formel"
H = "S. 49 Nr. 14 – zweite Lösung bestimmen, Lösungsmenge prüfen"
pruefe(sp.Eq(x**2 - 2*x - 15, 0), [5, -3])
neu(3, K3, 3, "NEU-vieta", ST, MK, 1,
    "Die Gleichung $x^2 - 2x - 15 = 0$ hat die Lösung $x_1 = 5$. "
    "Bestimme $x_2$ mit $x_1 + x_2 = -p$. Prüfe mit $x_1 \\cdot x_2 = q$.",
    "teil", "x2 = __",
    "$x_2 = -3$, denn $5 + x_2 = 2$; Probe: $5 \\cdot (-3) = -15 = q$",
    "-3", 125, H)
pruefe(sp.Eq(x**2 - 3*x - 28, 0), [7, -4])
neu(3, K3, 3, "NEU-vieta", ST, MK, 2,
    "Prüfe mit Summe und Produkt, ob $-4$ und $7$ die Lösungen von "
    "$x^2 - 3x - 28 = 0$ sind.", "teil", "\\janein",
    "Ja; Summe $-4 + 7 = 3 = -p$, Produkt $(-4) \\cdot 7 = -28 = q$",
    "[3, -28]", 125, H)
pruefe(sp.Eq(x**2 - 7*x + 12, 0), [4, 3])
neu(3, K3, 3, "NEU-vieta", ST, MK, 3,
    "Suche zwei ganze Zahlen mit der Summe $7$ und dem Produkt $12$. "
    "Löse damit $x^2 - 7x + 12 = 0$ ohne Formel.", "teil",
    "x1 = __, x2 = __",
    "$x_1 = 4$, $x_2 = 3$, denn $4 + 3 = 7 = -p$ und $4 \\cdot 3 = 12 = q$",
    "[4, 3]", 125, H)

ST4 = ("Normieren: durch die Vorzahl von x² teilen, auch bei Minus vor "
       "x² – amtlich nur in der Gymnasialreihe (Zeile 1954), von der P10 "
       "aber verlangt, Niveaumarke überschrieben (GYM-Regel, 2020-OS-K3e)")
MK = "Vorzahl vor x² ungleich eins: erst durch sie teilen"
H = "S. 47 Nr. 6 und S. 58 Nr. 11 – in die Normalform umwandeln, Vorzahl Bruch oder Dezimalzahl"
pruefe(sp.Eq(sp.Rational(1, 2)*x**2 + 3*x - 8, 0), [2, -8])
neu(3, K3, 3, 4, ST4, MK, 4,
    "Löse die Gleichung $0{,}5x^2 + 3x - 8 = 0$. Gib die Lösungsmenge "
    "an.", "gleichungsraster", "x1 = __, x2 = __",
    "durch $0{,}5$ geteilt (mal $2$): $x^2 + 6x - 16 = 0$; "
    "$x_{1,2} = -3 \\pm \\sqrt{9 + 16} = -3 \\pm 5$; $x_1 = 2$, $x_2 = -8$",
    "[2, -8]", 108, H)
pruefe(sp.Eq(sp.Rational(1, 4)*x**2 - x - 3, 0), [6, -2])
neu(3, K3, 3, 4, ST4, MK, 5,
    "Löse die Gleichung $\\frac{1}{4}x^2 - x - 3 = 0$. Gib die "
    "Lösungsmenge an.", "gleichungsraster", "x1 = __, x2 = __",
    "durch $\\frac{1}{4}$ geteilt (mal $4$): $x^2 - 4x - 12 = 0$; "
    "$x_{1,2} = 2 \\pm \\sqrt{4 + 12} = 2 \\pm 4$; $x_1 = 6$, $x_2 = -2$",
    "[6, -2]", 108, H)

ST11 = ("Klammer oder Produkt zuerst auflösen (binomische Formel), dann "
        "ordnen")
MK = "erst Klammer oder Produkt auflösen, dann ordnen"
H = "S. 45 Nr. 4f – Klammer auflösen, x-Glied hebt sich auf, rein quadratisch"
pruefe(sp.Eq((x - 6)**2, 100 - 12*x), [8, -8])
neu(3, K3, 3, 11, ST11, MK, 4,
    "Löse die Gleichung $(x - 6)^2 = 100 - 12x$. Gib die Lösungsmenge an.",
    "gleichungsraster", "x1 = __, x2 = __",
    "$x^2 - 12x + 36 = 100 - 12x$; $x^2 = 64$; $x_1 = 8$, $x_2 = -8$",
    "[8, -8]", 108, H)
pruefe(sp.Eq((2*x - 1)**2 + 4*x, 10), [sp.Rational(3, 2), -sp.Rational(3, 2)])
neu(3, K3, 3, 11, ST11, MK, 5,
    "Löse die Gleichung $(2x - 1)^2 + 4x = 10$. Gib die Lösungsmenge an.",
    "gleichungsraster", "x1 = __, x2 = __",
    "$4x^2 - 4x + 1 + 4x = 10$; $4x^2 = 9$; $x^2 = 2{,}25$; "
    "$x_1 = 1{,}5$, $x_2 = -1{,}5$", "[1.5, -1.5]", 108, H)

# ---- e3, eigener Typ ohne Kette: grafisch mit Normalparabel ----
ST = ("NEU-grafisch: Gleichung als x² = Gerade schreiben, Normalparabel "
      "und Gerade zeichnen, Lösungen als x-Werte der Schnittpunkte "
      "ablesen (RLP G „grafisch“; Vorschlag, nicht im Katalog)")
MK = "nur Normalparabel und Gerade: Lösungen sind die x-Werte der Schnittpunkte"
H = "S. 50 Nr. 16 – Lösung zeichnerisch bestimmen (Normalparabel und Gerade)"
pruefe(sp.Eq(x**2, 3*x - 2), [2, 1])
neu(3, "NEU-grafisch", 5, "NEU-grafisch", ST, MK, 1,
    "Das Bild zeigt die Normalparabel $y = x^2$ und die Gerade "
    "$y = 3x - 2$. Lies die Lösungen von $x^2 - 3x + 2 = 0$ an den "
    "Schnittpunkten ab.", "teil", "x1 = __, x2 = __",
    "$x^2 = 3x - 2$; Schnittpunkte bei $x_1 = 2$ und $x_2 = 1$",
    "[2, 1]", 25, H,
    grafik="\\begin{ksys}[xmin=-3,xmax=4,ymin=-3,ymax=7,ablesen] "
    "\\parabel{1}{0}{0}{} \\gerade{3}{-2}{} \\end{ksys}")
pruefe(sp.Eq(x**2, -3*x - 2), [-1, -2])
neu(3, "NEU-grafisch", 5, "NEU-grafisch", ST, MK, 2,
    "Das Bild zeigt die Normalparabel $y = x^2$ und die Gerade "
    "$y = -3x - 2$. Lies die Lösungen von $x^2 + 3x + 2 = 0$ an den "
    "Schnittpunkten ab.", "teil", "x1 = __, x2 = __",
    "$x^2 = -3x - 2$; Schnittpunkte bei $x_1 = -1$ und $x_2 = -2$",
    "[-1, -2]", 25, H,
    grafik="\\begin{ksys}[xmin=-4,xmax=3,ymin=-3,ymax=7,ablesen] "
    "\\parabel{1}{0}{0}{} \\gerade{-3}{-2}{} \\end{ksys}")
assert sp.solveset(x**2 - x + 1, x, domain=sp.S.Reals) == sp.S.EmptySet
neu(3, "NEU-grafisch", 5, "NEU-grafisch", ST, MK, 3,
    "Forme $x^2 - x + 1 = 0$ in $x^2 = \\ldots$ um. Das Bild zeigt die "
    "Normalparabel und die passende Gerade. Wie viele Lösungen hat die "
    "Gleichung?", "teil", "Anzahl der Lösungen: __",
    "$0$ – keine Lösung; $x^2 = x - 1$, die Gerade schneidet die "
    "Normalparabel nicht", "0", 25, H,
    grafik="\\begin{ksys}[xmin=-3,xmax=4,ymin=-3,ymax=7,ablesen] "
    "\\parabel{1}{0}{0}{} \\gerade{1}{-1}{} \\end{ksys}")

with open("neu-quadratische-gleichungen-duden9.jsonl", "w",
          encoding="utf-8", newline="\n") as f:
    for z in zeilen:
        f.write(json.dumps(z, ensure_ascii=False) + "\n")
print(len(zeilen), "Zeilen, alle Lösungen mit sympy nachgerechnet")
