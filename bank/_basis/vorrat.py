#!/usr/bin/env python3
"""Basisvorrat schreiben (Teil 2 des Auftrags vom 28.09.).

Liest bank/_basis/typen.csv (von typen.py) und schreibt je Eintrag
bank/_basis/<eintrag>.jsonl: je Basis-Typ zehn Aufgaben in
Prüfungsform, Felder nach bank.md, hoehe "basis", sprosse 1,
original = jüngstes Original des Typs. Die Aufgaben stehen unten in
AUFGABEN, von Hand geschrieben (Zahlen, Kontexte, Formulierungen);
das Skript setzt nur die Felder zusammen. „{K}“ im Aufgabentext
entfällt seit v0.7 (Lehrer 02.10.): keine Prüfkennung in den Daten, damit
sie nie auf einem Zettel erscheint; das Original steht im Feld original.
Bündel (v0.7): bei sechs Typen ist die Hälfte der Varianten (1, 3, 5, 7, 9)
eine Aufgabe mit Teilen a), b), c) zu einer Vorgabe (BUENDEL).

Aufruf: python3 bank/_basis/vorrat.py [--nur <eintrag>]
Danach: python3 werkzeuge/bank-pruef.py _basis
"""
import csv
import json
import sys
from pathlib import Path

import sympy as _sp

ORDNER = Path(__file__).resolve().parent
MERKMAL = "Basisaufgabe in Prüfungsform, ohne Rechner"


def A(aufgabe, loesung, pruef="", form="teil", antwort="__", grafik=""):
    return {"aufgabe": aufgabe, "form": form, "antwort": antwort,
            "loesung": loesung, "pruef": pruef, "grafik": grafik}


def X(aufgabe, optionen, loesung, pruef="", grafik=""):
    """Ankreuzen: je \\kreuz eine Zeile."""
    kreuze = "".join(f"\\\\ \\kreuz{{{o}}}" for o in optionen)
    return A(aufgabe + kreuze, loesung, pruef, "ankreuzen", "", grafik)


# --- Hilfen ------------------------------------------------------------

def dez(x):
    """Zahl mit Dezimalkomma für LaTeX, ohne überflüssige Nullen."""
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    if s == "-0":
        s = "0"
    return s.replace(".", "{,}")


def pz(x):
    return dez(x) + "\\,\\%"


def eur(x, stellen=None):
    if stellen:
        return f"{x:.{stellen}f}".replace(".", "{,}") + "\\,€"
    return dez(x) + "\\,€"


# Würfelnetz: Gegenfläche durch Falten (Rahmen n, r, u je Feld)
def gegenflaechen(netz):
    zeilen = netz.split("/")
    feld = {(i, j): c for i, z in enumerate(zeilen) for j, c in enumerate(z)
            if c != "."}
    start = next(iter(sorted(feld)))
    rahmen = {start: ((0, 0, -1), (1, 0, 0), (0, 1, 0))}
    neg = lambda v: tuple(-x for x in v)
    offen = [start]
    while offen:
        p = offen.pop()
        n, r, u = rahmen[p]
        for (di, dj), f in {(0, 1): lambda: (r, neg(n), u),
                            (0, -1): lambda: (neg(r), n, u),
                            (-1, 0): lambda: (u, r, neg(n)),
                            (1, 0): lambda: (neg(u), r, n)}.items():
            q = (p[0] + di, p[1] + dj)
            if q in feld and q not in rahmen:
                rahmen[q] = f()
                offen.append(q)
    assert len(rahmen) == 6, netz
    normale = {rahmen[p][0]: feld[p] for p in feld}
    assert len(normale) == 6, netz
    return {feld[p]: normale[neg(rahmen[p][0])] for p in feld}


def netzgrafik(netz):
    zeilen = netz.split("/")
    breite = max(len(z) for z in zeilen)
    reihen = [" & ".join((z.ljust(breite, "."))[j].replace(".", "")
                         for j in range(breite)) for z in zeilen]
    return ("$\\begin{array}{" + "c" * breite + "} "
            + " \\\\ ".join(reihen) + " \\end{array}$")


# Labels im Koordinatensystem (−5..5) wie mathblatt.sty setzen und, wenn zwei
# zu nah liegen, das Label einer Geraden bzw. Funktion an eine freie Stelle
# rücken (optionales Argument [x] von \\gerade, \\funktion, \\funktionab).
import math as _m


def _wert(term, x):
    t = term.replace("\\x", f"({x})").replace("^", "**")
    return eval(t, {"abs": abs})


def _funklabel(term, von, bis):
    d = (bis - von) / 40
    x = bis
    for _ in range(40):
        try:
            y = _wert(term, x)
        except ZeroDivisionError:
            y = 99
        if -4.7 < y < 4.7:
            return (x, y)
        x -= d
    return None


def _geradelabel(m, n, x=4.4):
    y = m * x + n
    if y > 5:
        return ((5 - n) / m, 5)
    if y < -5:
        return ((-5 - n) / m, -5)
    return (x, y)


def ksys_labels(teile):
    """teile: Bausteinaufrufe im ksys; gibt sie mit [x] zurück, wo nötig."""
    import re as _re
    punkte, art = [], []
    for t in teile:
        m = _re.match(r"\\gerade\{([-\d.]+)\}\{([-\d.]+)\}", t)
        if m:
            mm, nn = float(m.group(1)), float(m.group(2))
            punkte.append(_geradelabel(mm, nn))
            art.append(("g", mm, nn))
            continue
        m = _re.match(r"\\parabel\{([-\d.]+)\}\{([-\d.]+)\}\{([-\d.]+)\}", t)
        if m:
            a, d, e = (float(v) for v in m.groups())
            punkte.append(_funklabel(f"{a}*(\\x-({d}))^2+({e})", -5, 5))
            art.append(("p",))
            continue
        m = _re.match(r"\\funktionab\{([^}]*)\}\{\w\}\{([-\d.]+)\}\{([-\d.]+)\}", t)
        if m:
            punkte.append(_funklabel(m.group(1), float(m.group(2)),
                                     float(m.group(3))))
            art.append(("fab", m.group(1), float(m.group(2))))
            continue
        m = _re.match(r"\\funktion\{([^}]*)\}", t)
        punkte.append(_funklabel(m.group(1), -5, 5))
        art.append(("f", m.group(1)))

    frei_von = [(4.8, 0), (0, 4.8)]   # Achsenbeschriftungen x und y

    def nah(i, p):
        return (any(j != i and q and _m.dist(p, q) < 1.8
                    for j, q in enumerate(punkte))
                or any(_m.dist(p, q) < 1.2 for q in frei_von))
    neu = list(teile)
    for i, a in enumerate(art):
        if not nah(i, punkte[i]) or a[0] == "p":
            continue
        for x in (3.5, 2.5, 1.5, -3.5, -2.5, 0.5, -1.5, -4.2):
            if a[0] == "g":
                p = (x, a[1] * x + a[2])
                if not -4.3 < p[1] < 4.3:
                    continue
            elif a[0] == "f":
                p = _funklabel(a[1], -5, x)
            else:
                if x <= a[2]:
                    continue
                p = _funklabel(a[1], a[2], x)
            if p and not nah(i, p) and abs(p[0]) > 0.4 and abs(p[1]) > 0.4:
                punkte[i] = p
                name = teile[i].split("{")[0]
                neu[i] = name + f"[{x}]" + teile[i][len(name):]
                break
    return neu


# --- Aufgaben je Typ (zehn Varianten) ------------------------------------

AUFGABEN = {}

# T1 Bruchteil einer Fläche bestimmen – 2026-FOR-B1b (Ankreuzen, Figuren)
def _t1():
    K, R, B = "\\kreissektor[0.8]", "\\bruchrechteck[2.5]", "\\bruchkreis[0.8]"
    daten = [  # (Bruch z, n, Figuren P..S, richtig, Begründung)
        (1, 4, [f"{B}{{1}}{{3}}", f"{R}{{2}}{{8}}", f"{K}{{120}}{{}}",
                f"{R}{{2}}{{5}}"], "Q", "$\\frac{2}{8} = \\frac{1}{4}$"),
        (2, 3, [f"{R}{{2}}{{5}}", f"{B}{{3}}{{5}}", f"{K}{{240}}{{}}",
                f"{B}{{3}}{{4}}"], "R", "$\\frac{240}{360} = \\frac{2}{3}$"),
        (3, 8, [f"{B}{{3}}{{8}}", f"{R}{{3}}{{5}}", f"{K}{{90}}{{}}",
                f"{R}{{3}}{{10}}"], "P",
         "$\\frac{3}{8}$ – dort sind $3$ von $8$ gleichen Teilen grau"),
        (1, 2, [f"{K}{{150}}{{}}", f"{R}{{3}}{{6}}", f"{B}{{2}}{{5}}",
                f"{R}{{2}}{{6}}"], "Q", "$\\frac{3}{6} = \\frac{1}{2}$"),
        (3, 4, [f"{B}{{3}}{{5}}", f"{K}{{270}}{{}}", f"{R}{{4}}{{6}}",
                f"{R}{{3}}{{8}}"], "Q", "$\\frac{270}{360} = \\frac{3}{4}$"),
        (2, 5, [f"{K}{{144}}{{}}", f"{B}{{2}}{{6}}", f"{R}{{5}}{{10}}",
                f"{R}{{2}}{{4}}"], "P", "$\\frac{144}{360} = \\frac{2}{5}$"),
        (1, 8, [f"{R}{{1}}{{6}}", f"{B}{{1}}{{4}}", f"{K}{{45}}{{}}",
                f"{R}{{1}}{{10}}"], "R", "$\\frac{45}{360} = \\frac{1}{8}$"),
        (5, 6, [f"{K}{{300}}{{}}", f"{R}{{5}}{{8}}", f"{B}{{4}}{{5}}",
                f"{R}{{4}}{{6}}"], "P", "$\\frac{300}{360} = \\frac{5}{6}$"),
        (3, 10, [f"{B}{{3}}{{8}}", f"{K}{{108}}{{}}", f"{R}{{3}}{{9}}",
                 f"{K}{{30}}{{}}"], "Q",
         "$\\frac{108}{360} = \\frac{3}{10}$"),
        (3, 5, [f"{R}{{6}}{{10}}", f"{K}{{200}}{{}}", f"{B}{{3}}{{6}}",
                f"{R}{{3}}{{4}}"], "P", "$\\frac{6}{10} = \\frac{3}{5}$"),
    ]
    aus = []
    for z, n, fig, richtig, grund in daten:
        grafik = " \\quad ".join(f"{b} {f}" for b, f in zip("PQRS", fig))
        aus.append(X(f"Bei welcher Figur ist genau $\\frac{{{z}}}{{{n}}}$ "
                     f"grau? {{K}}", list("PQRS"),
                     f"{richtig}, denn {grund}", f"[{z}, {n}]", grafik))
    return aus


AUFGABEN["Bruchteil einer Fläche bestimmen"] = _t1()


# T2 Zahlen in verschiedenen Darstellungen vergleichen – 2023-OS-B1f
def _t2():
    daten = [  # (frage, Werte als LaTeX, Lösung, pruef)
        ("kleinste", ["3{,}3", "0{,}33", "0{,}3^2", "33\\,\\%"],
         "$0{,}3^2 = 0{,}09$; die anderen sind $3{,}3$ und zweimal $0{,}33$",
         "0.3**2"),
        ("kleinste", ["6{,}6", "0{,}6^2", "0{,}66", "66\\,\\%"],
         "$0{,}6^2 = 0{,}36$; die anderen sind $6{,}6$ und zweimal $0{,}66$",
         "0.6**2"),
        ("größte", ["0{,}2", "2\\,\\%", "0{,}2^2", "\\frac{1}{4}"],
         "$\\frac{1}{4} = 0{,}25$; die anderen sind $0{,}2$, $0{,}02$ und "
         "$0{,}04$", "0.25"),
        ("kleinste", ["0{,}8", "8\\,\\%", "0{,}8^2", "\\frac{3}{4}"],
         "$8\\,\\% = 0{,}08$; die anderen sind $0{,}8$, $0{,}64$ und "
         "$0{,}75$", "0.08"),
        ("größte", ["1{,}2^2", "1{,}4", "140\\,\\%", "1{,}3"],
         "$1{,}2^2 = 1{,}44$; die anderen sind $1{,}4$, $1{,}4$ und $1{,}3$",
         "1.2**2"),
        ("kleinste", ["0{,}5", "0{,}5^2", "5\\,\\%", "\\frac{1}{5}"],
         "$5\\,\\% = 0{,}05$; die anderen sind $0{,}5$, $0{,}25$ und $0{,}2$",
         "0.05"),
        ("größte", ["0{,}9^2", "0{,}85", "88\\,\\%", "\\frac{7}{8}"],
         "$88\\,\\% = 0{,}88$; die anderen sind $0{,}81$, $0{,}85$ und "
         "$0{,}875$", "0.88"),
        ("kleinste", ["2{,}2", "0{,}22", "22\\,\\%", "0{,}2^2"],
         "$0{,}2^2 = 0{,}04$; die anderen sind $2{,}2$ und zweimal $0{,}22$",
         "0.2**2"),
        ("größte", ["0{,}1", "0{,}1^2", "10\\,\\%", "\\frac{1}{8}"],
         "$\\frac{1}{8} = 0{,}125$; die anderen sind $0{,}1$, $0{,}01$ und "
         "$0{,}1$", "0.125"),
        ("kleinste", ["1{,}5", "150\\,\\%", "1{,}2^2", "1{,}4"],
         "$1{,}4$; die anderen sind $1{,}5$, $1{,}5$ und $1{,}2^2 = 1{,}44$",
         "1.4"),
    ]
    return [A(f"Welcher Wert ist der {f}: " + "; ".join(f"${w}$" for w in ws)
              + "? {K}", l, p) for f, ws, l, p in daten]


AUFGABEN["Zahlen in verschiedenen Darstellungen vergleichen"] = _t2()


# T3 Prozentwert berechnen – 2026-FOR-B1a („30 % von 70 €“)
def _t3():
    daten = [(20, 45), (30, 60), (25, 64), (10, 37), (40, 35), (15, 80),
             (70, 50), (5, 140), (60, 25), (75, 48)]
    aus = []
    for p, g in daten:
        w = p * g / 100
        aus.append(A(f"${pz(p)}$ von ${eur(g)}$ {{K}}",
                     f"${dez(p / 100)} \\cdot {g} = {eur(w, 2 if w % 1 else None)}$",
                     f"{p / 100}*{g}", antwort="__ €"))
    # Bündel (v0.7): je Zeile ein anderer gesuchter Wert (W, p, G)
    tab = [((80, 25), (40, 10), (10, 7)), ((60, 20), (60, 15), (50, 18)),
           ((90, 10), (30, 6), (25, 5)), ((46, 50), (90, 9), (20, 8)),
           ((40, 75), (48, 12), (10, "4.5"))]
    for i, ((g1, p1), (g2, w2), (p3, w3)) in enumerate(tab):
        w1 = _sp.Rational(g1 * p1, 100)
        p2 = _sp.Rational(w2 * 100, g2)
        g3 = _sp.Rational(str(w3)) * 100 / p3
        assert w1.is_Integer and p2.is_Integer and g3.is_Integer
        grafik = ("$\\begin{array}{c|c|c|c} & G & p & W \\\\ "
                  f"a) & {g1}\\,€ & {p1}\\,\\% & ? \\\\ "
                  f"b) & {g2}\\,€ & ? & {w2}\\,€ \\\\ "
                  f"c) & ? & {p3}\\,\\% & {eur(float(w3), 2 if float(w3) % 1 else None)} \\end{{array}}$")
        aus[2 * i] = A("Ergänze die Tabelle ($G$ Grundwert, $p$ Prozentsatz, "
                       "$W$ Prozentwert).",
                       f"a) $W = {w1}\\,€$ b) $p = {p2}\\,\\%$ "
                       f"c) $G = {g3}\\,€$", f"[{w1}, {p2}, {g3}]",
                       antwort="a) $W =$ __ € b) $p =$ __ % c) $G =$ __ €",
                       grafik=grafik)
    return aus


AUFGABEN["Prozentwert berechnen"] = _t3()


# T4 Termwert berechnen – 2026-FOR-B1g („5 · (x − 3) für x = −2“)
def _t4():
    daten = [(4, -2, -3), (2, -7, -1), (7, -1, -2), (3, 4, -6), (-2, -3, -1),
             (5, 2, -5), (4, -6, -2), (6, 1, -4), (-3, 2, -5), (8, -4, -1)]
    aus = []
    for a, b, x in daten:
        klammer = f"x {'+' if b > 0 else '-'} {abs(b)}"
        innen = x + b
        einsetz = f"{x} {'+' if b > 0 else '-'} {abs(b)}"
        wert = a * innen
        aus.append(A(f"Berechne den Wert von ${a} \\cdot ({klammer})$ für "
                     f"$x = {x}$. {{K}}",
                     f"${a} \\cdot ({einsetz}) = {a} \\cdot ({innen}) = {wert}$",
                     f"{a}*({x}{'+' if b > 0 else '-'}{abs(b)})"))
    return aus


AUFGABEN["Termwert berechnen"] = _t4()


# T5 Winkelfunktion Seitenverhältnis angeben – 2025-OS-B1g
def _t5():
    lage = {"A": [(0, 0), (4, 0), (0, 3)],        # rechter Winkel bei A
            "B": [(0, 0), (4, 0), (4, 3)],        # bei B
            "C": [(0, 0), (5, 0), (1.8, 2.4)]}    # bei C
    daten = [  # (rechter Winkel, Winkel bei, Funktion, Seiten a b c)
        ("B", "A", "sin", "k m n"), ("A", "C", "cos", "p q r"),
        ("C", "B", "tan", "s t u"), ("B", "C", "cos", "g h i"),
        ("A", "B", "tan", "d e f"), ("C", "A", "sin", "x y z"),
        ("B", "A", "tan", "r s t"), ("A", "B", "sin", "k l m"),
        ("C", "B", "cos", "e f g"), ("A", "C", "tan", "m n o"),
    ]
    griech = {"A": "\\alpha", "B": "\\beta", "C": "\\gamma"}
    aus = []
    for nr, (rw, bei, fn, seiten) in enumerate(daten):
        s = dict(zip("ABC", seiten.split()))       # Seite gegenüber der Ecke
        dritte = ({"A", "B", "C"} - {rw, bei}).pop()
        geg, an, hyp = s[bei], s[dritte], s[rw]
        bruch = {"sin": (geg, hyp), "cos": (an, hyp), "tan": (geg, an)}[fn]
        pkt = lage[rw] if rw != "C" else lage["C"]
        # Ecken so legen, dass der rechte Winkel an der gewählten Ecke liegt
        if rw == "A":
            ecken = {"A": (0, 0), "B": (3, 0), "C": (0, 2.2)}
        elif rw == "B":
            ecken = {"A": (0, 0), "B": (3, 0), "C": (3, 2.2)}
        else:
            ecken = {"A": (0, 0), "B": (3.75, 0), "C": (1.35, 1.8)}
        del pkt
        wink = ["", "", ""]
        wink["ABC".index(bei)] = griech[bei]
        koord = "".join("{(" + ",".join(dez(c).replace("{,}", ".")
                                        for c in ecken[e]) + ")}"
                        for e in "ABC")
        grafik = (f"\\dreieck{koord}{{{s['A']}}}{{{s['B']}}}{{{s['C']}}}"
                  f"{{{wink[0]}}}{{{wink[1]}}}{{{wink[2]}}}")
        g = griech[bei]
        if nr % 2 == 0:  # Bündel (v0.7): zu einem Winkel sin, cos und tan
            b = {"sin": (geg, hyp), "cos": (an, hyp), "tan": (geg, an)}
            aus.append(A(
                f"Rechter Winkel bei ${rw}$. Trage die Brüche ein.",
                " ".join(f"{t}) $\\mathrm{{{f}}}\\,{g} = \\frac{{{b[f][0]}}}"
                         f"{{{b[f][1]}}}$" for t, f in zip("abc", b)),
                "", antwort=" ".join(f"{t}) $\\mathrm{{{f}}}\\,{g} =$ __"
                                     for t, f in zip("abc", b)),
                grafik=grafik))
            continue
        aus.append(A(f"Rechter Winkel bei ${rw}$. Trage den Bruch ein. {{K}}",
                     f"$\\mathrm{{{fn}}}\\,{g} = \\frac{{{bruch[0]}}}"
                     f"{{{bruch[1]}}}$", "", antwort=f"$\\mathrm{{{fn}}}\\,{g} =$ __",
                     grafik=grafik))
    return aus


AUFGABEN["Winkelfunktion Seitenverhältnis angeben"] = _t5()


# T6 Lineare Gleichung lösen – 2024-OS-B1d („2 · (x − 6,5) = 0“)
def _t6():
    daten = [  # (Gleichung, Lösungsweg, x)
        ("3 \\cdot (x - 4{,}5) = 0", "$x - 4{,}5 = 0$, also $x = 4{,}5$", 4.5),
        ("5 \\cdot (x - 2) = 15", "$x - 2 = 3$, also $x = 5$", 5),
        ("4 \\cdot (x + 3) = 8", "$x + 3 = 2$, also $x = -1$", -1),
        ("2 \\cdot (x - 5) + 7 = 7", "$2 \\cdot (x - 5) = 0$, also $x = 5$", 5),
        ("6 \\cdot (x - 1{,}5) = 0", "$x - 1{,}5 = 0$, also $x = 1{,}5$", 1.5),
        ("3 \\cdot (x - 2) = 12", "$x - 2 = 4$, also $x = 6$", 6),
        ("2 \\cdot (x + 4) - 3 = 5", "$2 \\cdot (x + 4) = 8$, $x + 4 = 4$, "
         "also $x = 0$", 0),
        ("7 \\cdot (x - 3) = -14", "$x - 3 = -2$, also $x = 1$", 1),
        ("5 \\cdot (x + 3{,}5) = 0", "$x + 3{,}5 = 0$, also $x = -3{,}5$", -3.5),
        ("4 \\cdot (x - 1) + 2 = 10", "$4 \\cdot (x - 1) = 8$, $x - 1 = 2$, "
         "also $x = 3$", 3),
    ]
    return [A(f"Löse die Gleichung ${g}$. {{K}}", l, str(x), antwort="x = __")
            for g, l, x in daten]


AUFGABEN["Lineare Gleichung lösen"] = _t6()


# T7 Term zu Sachtext angeben – 2023-OS-B1h (Ankreuzen)
def _t7():
    daten = [
        ("Die Summe aus dem Doppelten einer Zahl $x$ und 5 wird verdreifacht.",
         ["$(2x + 5) : 3$", "$2x + 5 \\cdot 3$", "$3 \\cdot (2x + 5)$",
          "$2x \\cdot 5 + 3$"], 2, "Term"),
        ("Die Differenz aus dem Fünffachen einer Zahl $a$ und 6 wird halbiert.",
         ["$2 \\cdot (5a - 6)$", "$5a - 6 : 2$", "$(5a - 6) : 2$",
          "$5a : 6 - 2$"], 2, "Term"),
        ("Das Vierfache einer Zahl $x$ wird um 7 vermindert.",
         ["$4 \\cdot (x - 7)$", "$7 - 4x$", "$4x - 7$", "$4x - 7x$"], 2, "Term"),
        ("Das Sechsfache einer Zahl $b$ wird um 9 vergrößert.",
         ["$6 \\cdot (b + 9)$", "$6b + 9$", "$9b + 6$", "$6 + 9b$"], 1, "Term"),
        ("Die Summe aus einer Zahl $n$ und 8 wird mit 5 multipliziert.",
         ["$5n + 8$", "$5 \\cdot (n + 8)$", "$n + 8 \\cdot 5$",
          "$(n + 5) \\cdot 8$"], 1, "Term"),
        ("Das Dreifache einer Zahl $x$ wird von 20 subtrahiert.",
         ["$3x - 20$", "$20 - 3x$", "$3 \\cdot (20 - x)$", "$20x - 3$"], 1,
         "Term"),
        ("Die Summe aus einer Zahl $a$ und 6 wird verdoppelt.",
         ["$2a + 6$", "$2 \\cdot (a + 6)$", "$a + 6 \\cdot 2$",
          "$2 \\cdot a \\cdot 6$"], 1, "Term"),
        ("Die Hälfte einer Zahl $x$ wird um 3 vergrößert.",
         ["$(x + 3) : 2$", "$x : 2 + 3$", "$2x + 3$", "$x : 3 + 2$"], 1,
         "Term"),
        ("Die Differenz aus dem Siebenfachen einer Zahl $y$ und 2 wird "
         "vervierfacht.",
         ["$(7y - 2) : 4$", "$7y - 2 \\cdot 4$", "$4 \\cdot (7y - 2)$",
          "$7y \\cdot 4 - 2$"], 2, "Term"),
        ("Das Dreifache einer Zahl $x$ vermindert um 11 ist gleich 25.",
         ["$3 \\cdot (x - 11) = 25$", "$3x - 11 = 25$", "$11 - 3x = 25$",
          "$3x = -11 + 25$"], 1, "Gleichung"),
    ]
    aus = []
    for text, opt, i, art in daten:
        aus.append(X(f"{text} Welche{'r' if art == 'Term' else ''} {art} "
                     f"passt? {{K}}", opt, opt[i]))
    return aus


AUFGABEN["Term zu Sachtext angeben"] = _t7()


# T8 Zehnerpotenzschreibweise umwandeln – 2025-OS-B1d
def _t8():
    daten = [("62\\,000", "6{,}2", 4), ("3\\,900\\,000", "3{,}9", 6),
             ("0{,}0045", "4{,}5", -3), ("510", "5{,}1", 2),
             ("27\\,000\\,000", "2{,}7", 7), ("0{,}08", "8", -2),
             ("940\\,000", "9{,}4", 5), ("0{,}00036", "3{,}6", -4),
             ("1\\,200", "1{,}2", 3), ("0{,}7", "7", -1)]
    wort = {1: "eine Stelle", 2: "zwei Stellen", 3: "drei Stellen",
            4: "vier Stellen", 5: "fünf Stellen", 6: "sechs Stellen",
            7: "sieben Stellen"}
    aus = []
    for zahl, m, e in daten:
        richtung = "nach links" if e > 0 else "nach rechts"
        aus.append(A(f"${zahl} = {m} \\cdot 10^{{\\square}}$ – welche Hochzahl? "
                     "{K}", f"${e}$ – das Komma wandert {wort[abs(e)]} "
                     f"{richtung}", str(e)))
    return aus


AUFGABEN["Zehnerpotenzschreibweise umwandeln"] = _t8()


# T9 Lösung durch Einsetzen prüfen – 2025-OS-B1h (Ankreuzen)
def _t9():
    daten = [(6, -8, [2, 4, -2, -8]), (4, -3, [1, 3, -3, -4]),
             (-3, 10, [2, 5, -5, 10]), (9, -20, [4, 5, -5, -20]),
             (-2, 3, [1, 3, -3, -2]), (7, -12, [3, 4, -4, -12]),
             (-5, 6, [1, -6, 6, 5]), (3, 10, [-2, 2, 5, 10]),
             (10, -21, [3, 7, -7, -21]), (-4, 12, [2, 4, -2, -6])]
    aus = []
    for b, c, opt in daten:
        treffer = [x for x in opt if x * (x + b) == c]
        assert len(treffer) == 1, (b, c, treffer)
        x = treffer[0]
        vz = "+" if b > 0 else "-"
        xs = f"({x})" if x < 0 else f"{x}"
        aus.append(X(f"Welcher Wert erfüllt $x \\cdot (x {vz} {abs(b)}) = {c}$? "
                     "{K}", [f"$x = {o}$" for o in opt],
                     f"$x = {x}$, denn ${xs} \\cdot ({x} {vz} {abs(b)}) = {xs} "
                     f"\\cdot {'(' + str(x + b) + ')' if x + b < 0 else x + b} = {c}$",
                     str(x)))
    return aus


AUFGABEN["Lösung durch Einsetzen prüfen"] = _t9()


# T10 Wahrscheinlichkeit einstufig – 2014-OS-B1d
AUFGABEN["Wahrscheinlichkeit einstufig"] = [
    A("Ein Spielwürfel wird einmal geworfen. Wie groß ist die "
      "Wahrscheinlichkeit für eine Zahl größer als 4? {K}",
      "$\\frac{2}{6} = \\frac{1}{3}$ (die 5 und die 6)", "[1, 3]"),
    A("Ein Spielwürfel wird einmal geworfen. Wie groß ist die "
      "Wahrscheinlichkeit, weder eine 2 noch eine 5 zu werfen? {K}",
      "$\\frac{4}{6} = \\frac{2}{3}$ (die 1, 3, 4 und 6)", "[2, 3]"),
    A("Ein Glücksrad hat 8 gleich große Felder mit den Zahlen 1 bis 8. Wie "
      "groß ist die Wahrscheinlichkeit für eine gerade Zahl? {K}",
      "$\\frac{4}{8} = \\frac{1}{2}$ (2, 4, 6, 8)", "[1, 2]"),
    A("In einem Beutel liegen 3 rote, 4 blaue und 5 grüne Kugeln. Eine Kugel "
      "wird gezogen. Wie groß ist die Wahrscheinlichkeit, dass sie nicht grün "
      "ist? {K}", "$\\frac{7}{12}$ (7 von 12 Kugeln sind rot oder blau)",
      "[7, 12]"),
    A("Ein Spielwürfel wird einmal geworfen. Wie groß ist die "
      "Wahrscheinlichkeit, keine 6 zu werfen? {K}",
      "$\\frac{5}{6}$ (die 1 bis 5)", "[5, 6]"),
    A("Ein Glücksrad hat 10 gleich große Felder mit den Zahlen 1 bis 10. Wie "
      "groß ist die Wahrscheinlichkeit für eine durch 3 teilbare Zahl? {K}",
      "$\\frac{3}{10}$ (3, 6, 9)", "[3, 10]"),
    A("In einer Lostrommel sind 20 Lose, davon 4 Gewinne. Wie groß ist die "
      "Wahrscheinlichkeit, mit einem Los zu gewinnen? {K}",
      "$\\frac{4}{20} = \\frac{1}{5}$", "[1, 5]"),
    A("In einer Tüte sind 6 rote und 2 gelbe Bonbons. Lea nimmt ohne "
      "hinzusehen eines. Wie groß ist die Wahrscheinlichkeit für ein gelbes? "
      "{K}", "$\\frac{2}{8} = \\frac{1}{4}$", "[1, 4]"),
    A("Ein Würfel mit acht Flächen trägt die Zahlen 1 bis 8. Wie groß ist die "
      "Wahrscheinlichkeit, eine Zahl größer als 5 zu werfen? {K}",
      "$\\frac{3}{8}$ (6, 7, 8)", "[3, 8]"),
    A("Zehn Karten tragen die Zahlen 1 bis 10. Eine Karte wird gezogen. Wie "
      "groß ist die Wahrscheinlichkeit, weder die 1 noch die 10 zu ziehen? {K}",
      "$\\frac{8}{10} = \\frac{4}{5}$", "[4, 5]"),
]


def _t10b():
    """Bündel (v0.7): ein Zufallsgerät, drei Ereignisse."""
    from fractions import Fraction
    daten = [
        ("Ein Spielwürfel wird einmal geworfen.", 6,
         [("eine 6", {6}), ("eine gerade Zahl", {2, 4, 6}),
          ("eine Zahl größer als 4", {5, 6})]),
        ("Ein Glücksrad hat 8 gleich große Felder mit den Zahlen 1 bis 8.", 8,
         [("die 8", {8}), ("eine ungerade Zahl", {1, 3, 5, 7}),
          ("eine Zahl kleiner als 3", {1, 2})]),
        ("Ein Spielwürfel wird einmal geworfen.", 6,
         [("keine 6", {1, 2, 3, 4, 5}), ("eine 1 oder eine 2", {1, 2}),
          ("eine Zahl kleiner als 7", {1, 2, 3, 4, 5, 6})]),
        ("Ein Glücksrad hat 10 gleich große Felder mit den Zahlen 1 bis 10.",
         10, [("die 10", {10}), ("eine Zahl größer als 6", {7, 8, 9, 10}),
              ("eine durch 5 teilbare Zahl", {5, 10})]),
        ("Zwölf Karten tragen die Zahlen 1 bis 12. Eine wird gezogen.", 12,
         [("die 7", {7}), ("eine gerade Zahl", set(range(2, 13, 2))),
          ("eine Zahl größer als 9", {10, 11, 12})]),
    ]
    aus = []
    for text, n, ereig in daten:
        teile, los, pr = [], [], []
        for t, (was, menge) in zip("abc", ereig):
            assert menge <= set(range(1, n + 1))
            q = Fraction(len(menge), n)
            assert _sp.Rational(len(menge), n) == _sp.Rational(q.numerator,
                                                              q.denominator)
            teile.append(f"{t}) {was}")
            roh = f"\\frac{{{len(menge)}}}{{{n}}}"
            if q == 1:
                los.append(f"{t}) ${roh} = 1$")
                pr.append("1")
            elif q.denominator == n:
                los.append(f"{t}) ${roh}$")
                pr.append(f"[{q.numerator}, {q.denominator}]")
            else:
                los.append(f"{t}) ${roh} = \\frac{{{q.numerator}}}"
                           f"{{{q.denominator}}}$")
                pr.append(f"[{q.numerator}, {q.denominator}]")
        aus.append(A(f"{text} Gib die Wahrscheinlichkeit an für "
                     + ", ".join(teile[:2]) + " und " + teile[2] + ".",
                     " ".join(los), "[" + ", ".join(pr) + "]",
                     antwort="a) __ b) __ c) __"))
    return aus


for _i, _b in enumerate(_t10b()):
    AUFGABEN["Wahrscheinlichkeit einstufig"][2 * _i] = _b


# T11 Bruchteil einer Größe berechnen – 2018-OS-B1a („3/4 von 1,2 kg“)
AUFGABEN["Bruchteil einer Größe berechnen"] = [
    A("Wie viel Gramm sind $\\frac{2}{3}$ von $1{,}5$ kg? {K}",
      "$1{,}5$ kg $= 1\\,500$ g, $1\\,500 : 3 \\cdot 2 = 1\\,000$ g",
      "1500/3*2", antwort="__ g"),
    A("$\\frac{3}{4}$ von $2$ m – wie viel Meter? {K}",
      "$2 : 4 \\cdot 3 = 1{,}5$ m", "2/4*3", antwort="__ m"),
    A("$\\frac{2}{5}$ von $3$ l – wie viel Liter? {K}",
      "$3 : 5 \\cdot 2 = 1{,}2$ l", "3/5*2", antwort="__ l"),
    A("$\\frac{5}{6}$ von $1{,}2$ kg – wie viel Kilogramm? {K}",
      "$1{,}2 : 6 \\cdot 5 = 1$ kg", "1.2/6*5", antwort="__ kg"),
    A("$\\frac{3}{10}$ von $4$ kg – wie viel Kilogramm? {K}",
      "$4 : 10 \\cdot 3 = 1{,}2$ kg", "4/10*3", antwort="__ kg"),
    A("Wie viel Meter sind $\\frac{3}{4}$ von $1{,}6$ km? {K}",
      "$1{,}6$ km $= 1\\,600$ m, $1\\,600 : 4 \\cdot 3 = 1\\,200$ m",
      "1600/4*3", antwort="__ m"),
    A("$\\frac{2}{3}$ von $45$ min – wie viele Minuten? {K}",
      "$45 : 3 \\cdot 2 = 30$ min", "45/3*2", antwort="__ min"),
    A("$\\frac{4}{5}$ von $2{,}5$ l – wie viel Liter? {K}",
      "$2{,}5 : 5 \\cdot 4 = 2$ l", "2.5/5*4", antwort="__ l"),
    A("Wie viel Gramm sind $\\frac{1}{4}$ von $3{,}6$ kg? {K}",
      "$3{,}6$ kg $= 3\\,600$ g, $3\\,600 : 4 = 900$ g", "3600/4",
      antwort="__ g"),
    A("Ein Regenfass fasst $400$ l und ist zu $\\frac{3}{4}$ gefüllt. Wie "
      "viel Liter passen noch hinein? {K}",
      "gefüllt $400 : 4 \\cdot 3 = 300$ l, frei $400 - 300 = 100$ l",
      "[300, 400-300]", antwort="__ l"),
]


# T12 Exponent einer Potenz bestimmen – 2024-OS-B1g („4^x = 256“)
def _t12():
    daten = [(2, 5), (3, 4), (5, 2), (2, 6), (10, 4), (3, 3), (6, 2), (2, 7),
             (5, 4), (7, 2)]
    wort = {2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs",
            7: "sieben"}
    aus = []
    for b, x in daten:
        w = b ** x
        wt = f"{w:,}".replace(",", "\\,")
        kette = ", ".join(f"{b ** k:,}".replace(",", "\\,")
                          for k in range(1, x + 1))
        aus.append(A(f"${b}^x = {wt}$ – welche Zahl ist $x$? {{K}}",
                     f"${kette}$: {wort[x]} Faktoren, also $x = {x}$", str(x),
                     antwort="x = __"))
    return aus


AUFGABEN["Exponent einer Potenz bestimmen"] = _t12()


# T13 Grundwert berechnen – 2025-OS-B1a („Rabatt 6 €, das sind 20 %“)
def _t13():
    daten = [("einer Jacke", "spart Tom", 8, 20), ("eines Rucksacks",
             "spart Ben", 9, 25), ("eines Kopfhörers", "spart Ida", 12, 10),
             ("eines Spiels", "spart Can", 7, 50), ("eines Fahrradhelms",
             "spart Mia", 30, 60), ("einer Lampe", "spart Ole", 15, 75),
             ("einer Tasche", "spart Eda", 3, 5), ("eines Paars Schuhe",
             "spart Jan", 18, 40), ("einer Uhr", "spart Lina", 21, 70),
             ("eines Zelts", "spart Noah", 24, 30)]
    aus = []
    for ding, wer, w, p in daten:
        g = w * 100 // p
        aus.append(A(f"Beim Kauf {ding} {wer} ${eur(w)}$, das sind ${pz(p)}$ "
                     f"des alten Preises. Wie hoch war der alte Preis? {{K}}",
                     (f"${w} \\cdot {100 // p} = {eur(g)}$" if 100 % p == 0
                      else f"${w} : {p} \\cdot 100 = {eur(g)}$")
                     + f" (nicht ${pz(p)}$ von ${eur(w)}$)",
                     f"{w}*100/{p}", antwort="__ €"))
    return aus


AUFGABEN["Grundwert berechnen"] = _t13()


# T14 Prozent und Anteil umwandeln – 2022-OS-B1f (Ankreuzen)
def _t14():
    zahl = [
        ("Jeder zehnte Besucher gewinnt einen Preis", [1, 10, 20, 90], 10,
         "\\frac{1}{10} = \\frac{10}{100}"),
        ("Jedes zweite Kind hat ein Haustier", [2, 20, 50, 200], 50,
         "\\frac{1}{2} = \\frac{50}{100}"),
        ("3 von 4 Plätzen sind belegt", [3, 34, 60, 75], 75,
         "\\frac{3}{4} = \\frac{75}{100}"),
        ("Jede fünfzigste Schraube ist fehlerhaft", [2, 5, 20, 50], 2,
         "\\frac{1}{50} = \\frac{2}{100}"),
        ("Zwei von fünf Schülern fahren mit dem Bus", [2, 25, 40, 52], 40,
         "\\frac{2}{5} = \\frac{40}{100}"),
        ("Jede fünfundzwanzigste Tulpe blüht nicht", [4, 25, 40, 75], 4,
         "\\frac{1}{25} = \\frac{4}{100}"),
        ("3 von 10 Losen gewinnen", [3, 13, 30, 70], 30,
         "\\frac{3}{10} = \\frac{30}{100}"),
        ("Jeder achte Gast bestellt Tee", [8, 12.5, 18, 80], 12.5,
         "\\frac{1}{8} = 0{,}125"),
    ]
    aus = []
    for text, opt, r, grund in zahl:
        aus.append(X(f"{text} – wie viel Prozent? Kreuze an. {{K}}",
                     [f"${pz(o)}$" for o in opt], f"${pz(r)}$ (${grund}$)",
                     str(r)))
    aus.insert(4, X(
        "Nur $7\\,\\%$ der Samen keimen nicht. Welche Aussage passt? {K}",
        ["7 von 10 Samen keimen nicht.", "Jeder 7. Samen keimt nicht.",
         "7 von 100 Samen keimen nicht."], "7 von 100 Samen keimen nicht."))
    aus.insert(7, X(
        "$25\\,\\%$ der Besucher kommen mit dem Rad. Welche Aussage passt? {K}",
        ["Jeder 25. Besucher kommt mit dem Rad.",
         "Jeder vierte Besucher kommt mit dem Rad.",
         "2 von 5 Besuchern kommen mit dem Rad."],
        "Jeder vierte Besucher kommt mit dem Rad."))
    return aus


AUFGABEN["Prozent und Anteil umwandeln"] = _t14()


# T15 Symmetrieachsen bestimmen – 2022-OS-B1i (Ankreuzen 0 bis 5)
def _t15():
    daten = [
        ("Eine Tischplatte ist ein Rechteck (kein Quadrat).", 2,
         "\\rechteck{2.8}{1.6}"),
        ("Eine Fliese hat die Form einer Raute (kein Quadrat).", 2,
         "\\raute{2.8}{1.6}"),
        ("Ein Drachen hat die Form eines Drachenvierecks (keine Raute).", 1,
         "\\drachen{2.4}{1.8}{0.3}"),
        ("Ein Blech hat die Form eines Parallelogramms (kein Rechteck, keine "
         "Raute).", 0, "\\parallelogramm{2.6}{1.5}{60}"),
        ("Ein Warnschild ist ein gleichseitiges Dreieck.", 3,
         "\\dreieck{(0,0)}{(2.4,0)}{(1.2,2.08)}{}{}{}{}{}{}"),
        ("Eine Giebelwand ist ein gleichschenkliges Dreieck (nicht "
         "gleichseitig).", 1, "\\dreieck{(0,0)}{(3,0)}{(1.5,1.1)}{}{}{}{}{}{}"),
        ("Ein Beet ist ein Trapez mit zwei rechten Winkeln.", 0,
         "\\viereck{(0,0)}{(3,0)}{(1.9,1.5)}{(0,1.5)}"),
        ("Ein Tisch hat die Form eines regelmäßigen Fünfecks.", 5, ""),
        ("Ein Untersetzer ist ein Quadrat.", 4, "\\rechteck{1.6}{1.6}"),
        ("Ein Fensterbogen hat die Form eines Halbkreises.", 1, ""),
    ]
    return [X(f"{t} Wie viele Symmetrieachsen hat die Figur? Kreuze an. {{K}}",
              [str(i) for i in range(6)], str(n), str(n), g)
            for t, n, g in daten]


AUFGABEN["Symmetrieachsen bestimmen"] = _t15()


# T16 Winkel an geschnittenen Parallelen bestimmen – 2015-OS-B1d
def _t16():
    # \parallelenpaar{t}{#2}{#3}{#4}{#5}: #2/#4 = t (rechts über der oberen/
    # unteren Parallele), #3/#5 = 180 − t (links darüber)
    daten = [(62, 2, 5), (48, 3, 4), (70, 2, 4), (55, 4, 3), (65, 5, 2),
             (40, 2, 5), (75, 3, 5), (58, 4, 2), (50, 5, 4), (72, 3, 2)]
    aus = []
    for nr, (t, geg, ges) in enumerate(daten):
        wert = {2: t, 3: 180 - t, 4: t, 5: 180 - t}
        if nr % 2 == 0:  # Bündel (v0.7): drei Winkel aus einem gegebenen
            assert wert[2] + wert[3] == 180
            lab = {k: "" for k in wert}
            lab[geg] = f"{wert[geg]}^\\circ"
            gr = [k for k in (2, 3, 4, 5) if k != geg]
            for k, n in zip(gr, ("\\alpha", "\\beta", "\\gamma")):
                lab[k] = n
            grafik = "\\parallelenpaar{%d}{%s}{%s}{%s}{%s}" % (
                t, lab[2], lab[3], lab[4], lab[5])
            aus.append(A(
                "Die beiden waagerechten Geraden sind parallel. Bestimme "
                "$\\alpha$, $\\beta$ und $\\gamma$.",
                " ".join(f"{b}) ${lab[k]} = {wert[k]}^\\circ$"
                         for b, k in zip("abc", gr)),
                "[" + ", ".join(str(wert[k]) for k in gr) + "]",
                antwort=" ".join(f"{b}) ${lab[k]} =$ __°"
                                 for b, k in zip("abc", gr)),
                grafik=grafik))
            continue
        lab = {2: "", 3: "", 4: "", 5: ""}
        lab[geg] = f"{wert[geg]}^\\circ"
        lab[ges] = "\\alpha"
        grafik = "\\parallelenpaar{%d}{%s}{%s}{%s}{%s}" % (
            t, lab[2], lab[3], lab[4], lab[5])
        a = wert[ges]
        if a == wert[geg]:
            weg = f"$\\alpha = {a}^\\circ$ (Stufen- oder Wechselwinkel)"
            pr = str(a)
        else:
            weg = (f"$\\alpha = 180^\\circ - {wert[geg]}^\\circ = {a}^\\circ$ "
                   "(Stufenwinkel, dann Nebenwinkel)")
            pr = f"180-{wert[geg]}"
        aus.append(A("Die beiden waagerechten Geraden sind parallel. Wie groß "
                     "ist $\\alpha$? {K}", weg, pr, antwort="$\\alpha =$ __°",
                     grafik=grafik))
    return aus


AUFGABEN["Winkel an geschnittenen Parallelen bestimmen"] = _t16()


# T17 Winkel im Viereck berechnen – 2026-FOR-B1i (Parallelogramm)
def _t17():
    namen = ["\\alpha", "\\beta", "\\gamma", "\\delta"]
    wort = ["links unten", "rechts unten", "rechts oben", "links oben"]
    daten = [(68, 0, 1), (57, 0, 3), (72, 0, 2), (64, 0, 1), (70, 1, 0),
             (81, 0, 1), (66, 0, 2), (59, 0, 3), (77, 0, 1), (56, 1, 3)]
    aus = []
    for alpha, geg, ges in daten:
        w = [alpha, 180 - alpha, alpha, 180 - alpha]
        lab = ["", "", "", ""]
        lab[geg] = f"{w[geg]}^\\circ"
        lab[ges] = namen[ges]
        grafik = ("\\parallelogramm[winkel={" + ",".join(lab) + "}]"
                  f"{{3}}{{1.8}}{{{alpha}}}")
        n = namen[ges]
        if w[ges] == w[geg]:
            weg = (f"${n} = {w[ges]}^\\circ$ (gegenüberliegende Winkel sind "
                   "gleich groß)")
            pr = str(w[ges])
        else:
            weg = f"${n} = 180^\\circ - {w[geg]}^\\circ = {w[ges]}^\\circ$"
            pr = f"180-{w[geg]}"
        aus.append(A(f"Ein Parallelogramm hat {wort[geg]} einen Winkel von "
                     f"${w[geg]}^\\circ$. Wie groß ist der Winkel ${n}$ "
                     f"{wort[ges]}? {{K}}", weg, pr, antwort=f"${n} =$ __°",
                     grafik=grafik))
    return aus


AUFGABEN["Winkel im Viereck berechnen"] = _t17()


# T18 Zahl zu Bedingung angeben – 2015-OS-B1b / 2014-OS-B1c
AUFGABEN["Zahl zu Bedingung angeben"] = [
    A("Gib eine Zahl an, die größer ist als $-75$. {K}",
      "z. B. $-70$; richtig ist jede Zahl rechts von $-75$, auch $0$, nicht "
      "$-80$", "-70"),
    A("Gib eine Zahl an, die kleiner ist als $-30$. {K}",
      "z. B. $-40$; richtig ist jede Zahl links von $-30$, nicht $-20$",
      "-40"),
    A("Gib eine Zahl an, die zwischen $-2$ und $-1$ liegt. {K}",
      "z. B. $-1{,}5$; richtig ist jede Zahl größer als $-2$ und kleiner als "
      "$-1$", "-1.5"),
    A("Gib eine Zahl an, die zwischen $\\frac{1}{4}$ und $\\frac{1}{2}$ "
      "liegt. {K}", "z. B. $0{,}3$; richtig ist jede Zahl zwischen $0{,}25$ "
      "und $0{,}5$", "0.3"),
    A("Gib eine Zahl an, die zwischen $0{,}6$ und $0{,}7$ liegt. {K}",
      "z. B. $0{,}65$; richtig ist jede Zahl größer als $0{,}6$ und kleiner "
      "als $0{,}7$", "0.65"),
    A("Gib eine Zahl an, die kleiner ist als $-\\frac{1}{2}$. {K}",
      "z. B. $-1$; richtig ist jede Zahl links von $-0{,}5$, nicht $0$",
      "-1"),
    A("Gib eine Zahl an, die zwischen $-0{,}4$ und $-0{,}3$ liegt. {K}",
      "z. B. $-0{,}35$; richtig ist jede Zahl größer als $-0{,}4$ und kleiner "
      "als $-0{,}3$", "-0.35"),
    A("Ein U-Boot soll tiefer tauchen als $-120$ m. Nenne eine mögliche "
      "Position in m. {K}", "z. B. $-150$ m; richtig ist jede Zahl kleiner als "
      "$-120$, nicht $-100$", "-150", antwort="__ m"),
    A("Gib eine Zahl an, die zwischen $\\frac{2}{3}$ und $\\frac{3}{4}$ "
      "liegt. {K}", "z. B. $0{,}7$; richtig ist jede Zahl zwischen "
      "$0{,}\\overline{6}$ und $0{,}75$", "0.7"),
    A("In der Nacht soll es kälter als $-8$ °C werden. Nenne eine mögliche "
      "Temperatur. {K}", "z. B. $-10$ °C; richtig ist jede Zahl kleiner als "
      "$-8$, nicht $-5$", "-10", antwort="__ °C"),
]


# T19 Antiproportionale Zuordnung Dreisatz – 2014-GYM-B1c
def _t19():
    daten = [("Ein Heuvorrat reicht für {a} Kühe {b} Tage. Wie viele Tage "
              "reicht er für {c} Kühe?", 5, 12, 6, "Tage", "Kuhtage"),
             ("{a} Maler streichen ein Haus in {b} Tagen. Wie viele Tage "
              "brauchen {c} Maler?", 3, 8, 4, "Tage", "Malertage"),
             ("{a} Pumpen leeren ein Becken in {b} Stunden. Wie lange brauchen "
              "{c} Pumpen?", 6, 10, 5, "h", "Pumpenstunden"),
             ("Für einen Ausflug braucht man {a} Busse mit je {b} Plätzen. Wie "
              "viele Plätze müsste jeder Bus haben, wenn nur {c} Busse "
              "fahren?", 3, 40, 2, "Plätze", "Plätze"),
             ("{a} Helfer bauen eine Bühne in {b} Stunden auf. Wie lange "
              "brauchen {c} Helfer?", 8, 3, 6, "h", "Helferstunden"),
             ("{a} Bagger heben eine Grube in {b} Tagen aus. Wie viele Tage "
              "brauchen {c} Bagger?", 2, 9, 3, "Tage", "Baggertage"),
             ("Ein Futtervorrat reicht für {a} Schafe {b} Tage. Wie viele "
              "Tage reicht er für {c} Schafe?", 9, 20, 12, "Tage",
              "Schaftage"),
             ("{a} Drucker drucken einen Stapel in {b} Minuten. Wie lange "
              "brauchen {c} Drucker?", 4, 15, 6, "min", "Druckerminuten"),
             ("Ein Wasservorrat reicht für {a} Personen {b} Tage. Wie viele "
              "Tage reicht er für {c} Personen?", 4, 6, 3, "Tage",
              "Personentage"),
             ("{a} Arbeiter pflastern einen Platz in {b} Tagen. Wie viele "
              "Tage brauchen {c} Arbeiter?", 12, 5, 10, "Tage",
              "Arbeitertage")]
    aus = []
    for text, a, b, c, einheit, wort in daten:
        erg = a * b // c
        assert a * b % c == 0
        aus.append(A(text.format(a=a, b=b, c=c) + " {K}",
                     f"${a} \\cdot {b} = {a * b}$ {wort}; ${a * b} : {c} = "
                     f"{erg}$ {einheit}", f"{a}*{b}/{c}",
                     antwort=f"__ {einheit}"))
    return aus


AUFGABEN["Antiproportionale Zuordnung Dreisatz"] = _t19()


# T20 Dreiecksungleichung anwenden – 2020-OS-B1i (Ankreuzen)
def _t20():
    aus = []
    for ding, s1, s2, s3, wert, einh in [
            ("Ein Dreieck ABC", "a", "b", "c", 9, "cm"),
            ("Ein dreieckiges Segel ABC", "c", "a", "b", 4, "m"),
            ("Ein Dreieck ABC", "b", "a", "c", 7, "cm"),
            ("Ein dreieckiger Garten ABC", "a", "b", "c", 20, "m"),
            ("Ein Dreieck ABC", "c", "a", "b", 11, "cm")]:
        opt = [f"${s2} + {s3} > {wert}$ {einh}", f"${s2} + {s3} = {wert}$ {einh}",
               f"${s2} + {s3} < {wert}$ {einh}"]
        aus.append(X(f"{ding} hat die Seite ${s1} = {wert}$ {einh}. Was gilt "
                     f"für die Summe der beiden anderen Seiten ${s2}$ und "
                     f"${s3}$? {{K}}", opt, opt[0]))
    for tripel, richtig in [
            (["$2$ cm, $3$ cm, $6$ cm", "$4$ cm, $5$ cm, $8$ cm",
              "$3$ cm, $4$ cm, $7$ cm"], 1),
            (["$5$ cm, $5$ cm, $10$ cm", "$2$ cm, $7$ cm, $4$ cm",
              "$6$ cm, $3$ cm, $8$ cm"], 2),
            (["$3$ m, $3$ m, $5$ m", "$1$ m, $2$ m, $4$ m",
              "$2$ m, $6$ m, $3$ m"], 0),
            (["$4$ cm, $9$ cm, $4$ cm", "$6$ cm, $7$ cm, $12$ cm",
              "$5$ cm, $2$ cm, $8$ cm"], 1),
            (["$8$ cm, $1$ cm, $6$ cm", "$3$ cm, $9$ cm, $5$ cm",
              "$7$ cm, $7$ cm, $2$ cm"], 2)]:
        aus.append(X("Aus welchen drei Stäben kann man ein Dreieck legen? "
                     "{K}", tripel, tripel[richtig]))
    # abwechselnd Seite und Stäbe
    return [aus[i] for i in (0, 5, 1, 6, 2, 7, 3, 8, 4, 9)]


AUFGABEN["Dreiecksungleichung anwenden"] = _t20()


# T21 Figur nach Spiegelung benennen – 2018-OS-B1h (Kurzantwort, Text)
AUFGABEN["Figur nach Spiegelung benennen"] = [
    A("Ein Dreieck mit drei verschieden langen Seiten liegt mit einer Seite "
      "auf der Geraden $g$ und wird an $g$ gespiegelt. Welches Viereck bilden "
      "Dreieck und Spiegelbild? {K}", "Drachenviereck", form="text",
      antwort=""),
    A("Ein rechtwinkliges Dreieck liegt mit einer Kathete auf der Geraden $g$ "
      "und wird an $g$ gespiegelt. Welche Figur bilden Dreieck und "
      "Spiegelbild? {K}", "gleichschenkliges Dreieck", form="text",
      antwort=""),
    A("Ein gleichschenkliges Dreieck liegt mit der Basis auf der Geraden $g$ "
      "und wird an $g$ gespiegelt. Welches Viereck entsteht? {K}", "Raute",
      form="text", antwort=""),
    A("Ein Rechteck liegt mit einer Seite auf der Geraden $g$ und wird an $g$ "
      "gespiegelt. Welche Figur bilden Rechteck und Spiegelbild? {K}",
      "Rechteck (doppelt so lang)", form="text", antwort=""),
    A("Ein gleichschenklig-rechtwinkliges Dreieck liegt mit der längsten "
      "Seite auf der Geraden $g$ und wird an $g$ gespiegelt. Welches Viereck "
      "entsteht? {K}", "Quadrat", form="text", antwort=""),
    A("Ein Quadrat liegt mit einer Seite auf der Geraden $g$ und wird an $g$ "
      "gespiegelt. Welche Figur bilden Quadrat und Spiegelbild? {K}",
      "Rechteck (kein Quadrat)", form="text", antwort=""),
    A("Ein Halbkreis liegt mit seinem Durchmesser auf der Geraden $g$ und "
      "wird an $g$ gespiegelt. Welche Figur entsteht? {K}", "Kreis",
      form="text", antwort=""),
    A("Ein Trapez mit zwei rechten Winkeln liegt mit der Seite zwischen den "
      "rechten Winkeln auf der Geraden $g$ und wird an $g$ gespiegelt. "
      "Welches Viereck entsteht? {K}", "gleichschenkliges Trapez",
      form="text", antwort=""),
    A("Ein gleichseitiges Dreieck liegt mit einer Seite auf der Geraden $g$ "
      "und wird an $g$ gespiegelt. Welches Viereck entsteht? {K}",
      "Raute", form="text", antwort=""),
    A("Ein rechtwinkliges Dreieck mit verschieden langen Katheten liegt mit "
      "der längsten Seite auf der Geraden $g$ und wird an $g$ gespiegelt. "
      "Welches Viereck entsteht? {K}", "Drachenviereck (mit zwei rechten "
      "Winkeln)", form="text", antwort=""),
]


# T22 Gegenfläche im Würfelnetz bestimmen – 2016-OS-B1j
def _t22():
    daten = [  # (Netz zeilenweise mit /, unten, Kontext)
        ("A.../BCDE/F...", "C", "Der Würfel wird auf die Fläche {u} "
         "gestellt."),
        (".P../QRST/..U.", "T", "Die Fläche {u} ist der Boden einer "
         "Schachtel."),
        ("K.../LMN./..OP", "K", "Der Würfel wird auf die Fläche {u} "
         "gestellt."),
        ("..G./DEF./.H../.I..", "D", "Die Fläche {u} ist der Boden."),
        ("AB../.CD./..EF", "A", "Der Würfel wird auf die Fläche {u} "
         "gestellt."),
        ("..RW/.ST./UV..", "U", "Die Fläche {u} ist der Deckel einer "
         "Schachtel; welche ist der Boden?"),
        ("X.../YZWV/...Q", "W", "Der Würfel wird auf die Fläche {u} "
         "gestellt."),
        (".M../NOPL/.K..", "N", "Die Fläche {u} ist der Boden."),
        ("BC../.DEF/.G..", "B", "Der Würfel wird auf die Fläche {u} "
         "gestellt."),
        (".H../EFGI/..J.", "E", "Die Fläche {u} ist der Deckel; welche "
         "ist der Boden?"),
    ]
    aus = []
    for netz, u, text in daten:
        geg = gegenflaechen(netz)
        o = geg[u]
        t = text.format(u=u)
        frage = "" if "?" in t else " Welche Fläche liegt oben?"
        aus.append(A("Das Netz aus sechs Quadraten (je Buchstabe ein Quadrat) "
                     f"wird zu einem Würfel gefaltet. {t}{frage} "
                     "{K}", f"{o} ({o} und {u} liegen sich gegenüber)",
                     grafik=netzgrafik(netz)))
    return aus


AUFGABEN["Gegenfläche im Würfelnetz bestimmen"] = _t22()


# T23 Gleichschenkliges Dreieck erkennen – 2023-OS-B1g
def _t23():
    daten = [(65, "5"), (75, "8"), (55, "4"), (80, "9"), (50, "3{,}5"),
             (72, "6{,}5"), (35, "2"), (45, "5{,}5"), (68, "4{,}5"), (62, "10")]
    aus = []
    for w, s in daten:
        g = 180 - 2 * w
        aus.append(A(f"Im Dreieck ABC ist $\\alpha = \\beta = {w}^\\circ$ und "
                     f"AC = ${s}$ cm. Gib die Länge von BC und die Größe von "
                     f"$\\gamma$ an. {{K}}",
                     f"BC = AC = ${s}$ cm (gleiche Winkel bei A und B); "
                     f"$\\gamma = 180^\\circ - 2 \\cdot {w}^\\circ = {g}^\\circ$",
                     f"[{s.replace('{,}', '.')}, 180-2*{w}]",
                     antwort="BC = __ cm, $\\gamma =$ __°"))
    return aus


AUFGABEN["Gleichschenkliges Dreieck erkennen"] = _t23()


# T24 Graph einer linearen Funktion erkennen – 2025-OS-B1f
def _t24():
    daten = [
        ["\\parabel{1}{1}{-3}{A}", "\\gerade{0.5}{-2}{B}",
         "\\funktionab{3/\\x}{C}{0.6}{5}", "\\funktion{abs(\\x)-3}{D}"],
        ["\\funktion{abs(\\x+1)+1}{A}", "\\funktionab{-2/\\x}{B}{0.4}{5}",
         "\\parabel{-1}{0}{3}{C}", "\\gerade{-1}{2}{D}"],
        ["\\gerade{2}{-1}{A}", "\\parabel{0.5}{-2}{-4}{B}",
         "\\funktion{0.1*\\x^3}{C}", "\\funktion{-abs(\\x-2)+3}{D}"],
        ["\\funktionab{4/\\x}{A}{0.8}{5}", "\\funktion{abs(\\x-3)-1}{B}",
         "\\gerade{-0.5}{-1}{C}", "\\parabel{1}{3}{-2}{D}"],
        ["\\parabel{-0.5}{1}{4}{A}", "\\gerade{1}{1}{B}",
         "\\funktion{-abs(\\x+2)+2}{C}", "\\funktionab{1/\\x}{D}{0.2}{5}"],
        ["\\gerade{-2}{-1}{A}", "\\funktion{0.2*\\x^3}{B}",
         "\\funktion{abs(\\x)+1}{C}", "\\parabel{2}{-1}{-4}{D}"],
        ["\\parabel{1}{-2}{0}{A}", "\\funktionab{-4/\\x}{B}{0.8}{5}",
         "\\funktion{abs(\\x-1)-4}{C}", "\\gerade{0.25}{3}{D}"],
        ["\\funktion{-0.1*\\x^3}{A}", "\\parabel{-1}{2}{2}{B}",
         "\\gerade{3}{-4}{C}", "\\funktion{abs(\\x+3)}{D}"],
        ["\\funktion{abs(\\x-2)+2}{A}", "\\gerade{-1.5}{0}{B}",
         "\\parabel{0.5}{0}{-3}{C}", "\\funktionab{2/\\x}{D}{0.4}{5}"],
        ["\\gerade{0.5}{2}{A}", "\\funktionab{-1/\\x}{B}{0.2}{5}",
         "\\parabel{-2}{-1}{1}{C}", "\\funktion{-abs(\\x)+4}{D}"],
    ]
    aus = []
    for g in daten:
        r = "ABCD"[[i for i, t in enumerate(g) if t.startswith("\\gerade")][0]]
        grafik = ("\\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5,ablesen] "
                  + " ".join(ksys_labels(g)) + " \\end{ksys}")
        aus.append(X("Welcher Graph gehört zu einer linearen Funktion? Kreuze "
                     "an. {K}", list("ABCD"),
                     f"{r} (eine Gerade ohne Knick)", "", grafik))
    return aus


AUFGABEN["Graph einer linearen Funktion erkennen"] = _t24()


# T25 Graph nach Eigenschaft auswählen – 2016-OS-B1c
def _t25():
    daten = [
        ("Welche Gerade steigt?", [(-2, 1), (0.5, -1)], "g",
         "von links nach rechts gelesen geht sie nach oben"),
        ("Welche Gerade fällt?", [(1, 2), (-1.5, -1)], "g",
         "von links nach rechts gelesen geht sie nach unten"),
        ("Welche Gerade geht durch den Ursprung?", [(2, 0), (2, -3), (-1, 2)],
         "f", "sie schneidet die y-Achse bei 0"),
        ("Welche Gerade ist steiler?", [(0.5, 1), (3, -2)], "g",
         "sie steigt je Kästchen nach rechts um drei nach oben"),
        ("Welche Gerade schneidet die y-Achse unterhalb der x-Achse?",
         [(-1, 3), (1, -2)], "g", "sie schneidet die y-Achse bei $-2$"),
        ("Welche Gerade verläuft parallel zur x-Achse?",
         [(0, 2), (1, 1), (-0.5, -2)], "f", "sie hat die Steigung 0"),
        ("Welche Gerade fällt?", [(-2, 4), (2, -1), (0.5, 0)], "f",
         "von links nach rechts gelesen geht sie nach unten"),
        ("Welche Gerade steigt am stärksten?", [(1, 0), (2, -2), (0.5, 1)],
         "g", "sie hat die größte Steigung, 2"),
        ("Welche Gerade hat die Steigung 1?", [(1, -1), (2, 1)], "f",
         "ein Kästchen nach rechts, ein Kästchen nach oben"),
        ("Welche Gerade fällt am stärksten?", [(-0.5, 1), (-3, 2), (1, -3)],
         "g", "sie hat die Steigung $-3$"),
    ]
    aus = []
    for frage, geraden, r, grund in daten:
        namen = "fgh"[:len(geraden)]
        grafik = ("\\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5,ablesen] "
                  + " ".join(ksys_labels([
                      f"\\gerade{{{dez(m).replace('{,}', '.')}}}{{{n}}}{{{b}}}"
                      for (m, n), b in zip(geraden, namen)]))
                  + " \\end{ksys}")
        aus.append(X(f"{frage} Kreuze an. {{K}}", list(namen),
                     f"{r} ({grund})", "", grafik))
    return aus


AUFGABEN["Graph nach Eigenschaft auswählen"] = _t25()


# T26 Kantenzahl eines Körpers angeben – 2019-OS-B1f
AUFGABEN["Kantenzahl eines Körpers angeben"] = [
    A("Ein Spielwürfel ist ein Würfel. Gib an, wie viele Kanten er hat. {K}",
      "$12$ Kanten ($4$ oben, $4$ unten, $4$ senkrecht)", "12",
      antwort="__ Kanten"),
    A("Eine Schokoladenpackung hat die Form eines Prismas mit dreieckiger "
      "Grundfläche. Gib an, wie viele Kanten sie hat. {K}",
      "$3 + 3 + 3 = 9$ Kanten ($3$ oben, $3$ unten, $3$ Seitenkanten)",
      "3+3+3", antwort="__ Kanten"),
    A("Ein Turmdach hat die Form einer Pyramide mit fünfeckiger Grundfläche. "
      "Gib an, wie viele Kanten diese Pyramide hat. {K}",
      "$5 + 5 = 10$ Kanten ($5$ Grundkanten, $5$ Seitenkanten)", "5+5",
      antwort="__ Kanten"),
    A("Ein Bleistift hat die Form eines Prismas mit sechseckiger "
      "Grundfläche. Gib an, wie viele Kanten dieses Prisma hat. {K}",
      "$6 + 6 + 6 = 18$ Kanten", "6+6+6", antwort="__ Kanten"),
    A("Ein Prisma hat eine fünfeckige Grundfläche. Gib an, wie viele Kanten "
      "es hat. {K}", "$5 + 5 + 5 = 15$ Kanten ($5$ oben, $5$ unten, $5$ "
      "Seitenkanten)", "5+5+5", antwort="__ Kanten"),
    A("Ein Kirchturmdach ist eine Pyramide mit achteckiger Grundfläche. Gib "
      "an, wie viele Kanten diese Pyramide hat. {K}",
      "$8 + 8 = 16$ Kanten", "8+8", antwort="__ Kanten"),
    A("Ein Schuhkarton hat die Form eines Quaders. Gib an, wie viele Kanten "
      "er hat. {K}", "$4 + 4 + 4 = 12$ Kanten (nicht $8$ Ecken)", "4+4+4",
      antwort="__ Kanten"),
    A("Eine Säule hat die Form eines Prismas mit achteckiger Grundfläche. Gib "
      "an, wie viele Kanten dieses Prisma hat. {K}",
      "$8 + 8 + 8 = 24$ Kanten", "8+8+8", antwort="__ Kanten"),
    A("Ein Blumentopf hat die Form eines Pyramidenstumpfs mit quadratischer "
      "Grundfläche. Gib an, wie viele Kanten er hat. {K}",
      "$4 + 4 + 4 = 12$ Kanten ($4$ unten, $4$ oben, $4$ schräge)", "4+4+4",
      antwort="__ Kanten"),
    A("Eine Pyramide hat eine zehneckige Grundfläche. Gib an, wie viele "
      "Kanten sie hat. {K}", "$10 + 10 = 20$ Kanten ($10$ Grundkanten, $10$ "
      "Seitenkanten)", "10+10", antwort="__ Kanten"),
]


# T27 Kreissektor Anteil berechnen – 2025-OS-B1e (ohne Rechner: glatte Winkel)
def _t27():
    daten = [(90, ""), (72, "Auf dem grauen Teil eines runden Beets wachsen "
             "Rosen."), (36, ""), (108, "Ein Glücksrad ist zum Teil grau."),
             (144, ""), (270, "Von einer runden Pizza ist der graue Teil "
             "übrig."), (54, ""), (216, "Eine runde Torte ist zum Teil mit "
             "Schokolade überzogen (grau)."), (18, ""), (180, "Eine runde "
             "Uhr ist zum Teil grau.")]
    aus = []
    for w, kontext in daten:
        p = w * 100 // 360
        assert w * 100 % 360 == 0
        text = (kontext + " " if kontext else
                "Im Bild ist ein Kreisausschnitt grau gefärbt. ")
        aus.append(A(f"{text}Der Mittelpunktswinkel des grauen Teils "
                     f"beträgt ${w}^\\circ$. "
                     "Wie viel Prozent der Kreisfläche sind grau? {K}",
                     f"${w} : 360 = {dez(w / 360)} = {p}\\,\\%$",
                     f"{w}/360*100", antwort="__ %",
                     grafik=f"\\kreissektor[1.2]{{{w}}}{{${w}^\\circ$}}"))
    return aus


AUFGABEN["Kreissektor Anteil berechnen"] = _t27()


# T28 Lage eines Punktes zu den Achsen erkennen – 2020-OS-B1b
def _t28():
    daten = [
        ("Genau einer der vier Punkte liegt auf der x-Achse. Welcher?",
         ["P(5|6)", "Q(0|6)", "R(5|0)", "S(-5|-6)"], 2),
        ("Genau einer der vier Punkte liegt auf der y-Achse. Welcher?",
         ["A(2|6)", "B(0|6)", "C(6|0)", "D(-2|-6)"], 1),
        ("Genau einer der vier Punkte liegt auf der x-Achse. Welcher?",
         ["K(-8|0)", "L(0|-8)", "M(-8|-8)", "N(8|8)"], 0),
        ("Genau einer der vier Punkte liegt auf der y-Achse. Welcher?",
         ["E(0|-3)", "F(-3|1)", "G(3|-3)", "H(-3|3)"], 0),
        ("Genau einer der vier Punkte liegt auf der x-Achse. Welcher?",
         ["A(1|1)", "B(8|0)", "C(1|8)", "D(-8|1)"], 1),
        ("Genau einer der vier Punkte liegt auf der y-Achse. Welcher?",
         ["P(7|2)", "Q(-7|2)", "R(0|-9)", "S(2|-7)"], 2),
        ("Genau einer der vier Punkte liegt auf beiden Achsen. Welcher?",
         ["A(0|5)", "B(5|0)", "C(0|0)", "D(5|5)"], 2),
        ("Genau einer der vier Punkte liegt auf der x-Achse. Welcher?",
         ["F(0|9)", "G(9|1)", "H(-9|0)", "J(1|9)"], 2),
        ("Genau einer der vier Punkte liegt auf der y-Achse. Welcher?",
         ["M(0|-7)", "N(-7|-1)", "P(7|-7)", "Q(-3|7)"], 0),
        ("Genau einer der vier Punkte liegt auf keiner der beiden Achsen. "
         "Welcher?", ["A(0|6)", "B(-7|0)", "C(0|-9)", "D(3|-5)"], 3),
    ]
    aus = []
    for frage, pkt, r in daten:
        opt = [f"${p}$" for p in pkt]
        aus.append(X(f"{frage} {{K}}", opt, opt[r]))
    return aus


AUFGABEN["Lage eines Punktes zu den Achsen erkennen"] = _t28()


# T29 Mitte zweier Zahlen bestimmen – 2020-OS-B1f
def _t29():
    daten = [(-0.4, -0.3), (-2.1, -2), (0.7, 0.8), (-1, -0.9), (-3, -2),
             (-0.2, 0.4), (1.5, 1.6), (-5, 1), (-0.9, -0.8), (-4.6, -4.5)]
    aus = []
    for a, b in daten:
        m = (a + b) / 2
        bb = f"({dez(b)})" if b < 0 else dez(b)
        aus.append(A(f"Welche Zahl liegt genau in der Mitte zwischen ${dez(a)}$ "
                     f"und ${dez(b)}$? {{K}}",
                     f"$({dez(a)} + {bb}) : 2 = {dez(round(m, 4))}$",
                     f"({a}+{b})/2".replace("+-", "-")))
    return aus


AUFGABEN["Mitte zweier Zahlen bestimmen"] = _t29()


# T30 Prozentsatz berechnen – 2014-OS-B1e (Zinssatz aus Guthaben und Zinsen)
def _t30():
    daten = [("Ein Sparguthaben von {g} bringt in einem Jahr {w} Zinsen. Wie "
              "hoch ist der Zinssatz?", 5000, 150, "€"),
             ("Von {g} Schülern kommen {w} mit dem Rad. Wie viel Prozent sind "
              "das?", 400, 36, ""),
             ("In einer Lostrommel sind {g} Lose, {w} davon gewinnen. Wie viel "
              "Prozent sind das?", 80, 12, ""),
             ("Ein Guthaben von {g} bringt in einem Jahr {w} Zinsen. Wie hoch "
              "ist der Zinssatz?", 2000, 70, "€"),
             ("Von {g} Äpfeln sind {w} faul. Wie viel Prozent sind das?", 250,
              10, ""),
             ("Ein Dorf hat {g} Einwohner, {w} sind neu zugezogen. Wie viel "
              "Prozent sind das?", 1500, 30, ""),
             ("Von {g} Plätzen im Kino sind {w} besetzt. Wie viel Prozent sind "
              "das?", 60, 45, ""),
             ("Ein Guthaben von {g} bringt in einem Jahr {w} Zinsen. Wie hoch "
              "ist der Zinssatz?", 800, 12, "€"),
             ("In einem Test hat Aylin {w} von {g} Fragen richtig. Wie viel "
              "Prozent sind das?", 50, 43, ""),
             ("Ein Joghurt wiegt {g} und enthält {w} Fett. Wie viel Prozent "
              "Fett sind das?", 200, 5, "g")]
    aus = []
    for text, g, w, e in daten:
        def fmt(x):
            s = f"{x:,}".replace(",", "\\,")
            if e == "€":
                return f"${s}\\,€$"
            return f"${s}$ {e}" if e else f"${s}$"
        p = w * 100 / g
        gt = f"{g:,}".replace(",", "\\,")
        aus.append(A(text.format(g=fmt(g), w=fmt(w)) + " {K}",
                     f"${w} : {gt} = {dez(w / g)} = {pz(p)}$",
                     f"{w}/{g}*100", antwort="__ %"))
    return aus


AUFGABEN["Prozentsatz berechnen"] = _t30()


# T31 Punktprobe durchführen – 2023-OS-B1i (Ankreuzen)
def _t31():
    daten = [(2, -1, [1, 4, -2], 2, -3), (-3, 4, [1, -2, 3], 0, 9),
             (4, -3, [-1, 2, 3], 1, 8), (-2, -3, [2, -1, -4], 2, 6),
             (3, -5, [2, -1, 4], 0, 3), (-4, 2, [1, -2, 3], 1, 9),
             (5, -2, [3, -1, 2], 2, 9), (-1, 6, [2, -3, 5], 0, 3),
             (6, -4, [1, 2, -1], 2, -2), (-8, 1, [1, -1, 2], 1, 7)]
    aus = []
    for m, n, xs, falsch, yf in daten:
        pkt = []
        for i, x in enumerate(xs):
            y = yf if i == falsch else m * x + n
            assert (y == m * x + n) == (i != falsch)
            pkt.append((x, y))
        opt = [f"$({x}|{y})$" for x, y in pkt]
        x, y = pkt[falsch]
        mt = {1: "", -1: "-"}.get(m, str(m))
        term = f"{mt}x {'+' if n > 0 else '-'} {abs(n)}"
        aus.append(X(f"Gegeben ist $f(x) = {term}$. Welcher Punkt liegt nicht "
                     "auf der Geraden? Kreuze an. {K}", opt,
                     f"$({x}|{y})$, denn $f({x}) = {m * x + n}$",
                     f"[{x}, {y}]"))
    return aus


AUFGABEN["Punktprobe durchführen"] = _t31()


# T32 Rechteckseite aus Umfang berechnen – 2018-OS-B1f
def _t32():
    daten = [("Ein Rechteck hat den Umfang {u} und die Seite $a = {av}$ {e}. Wie "
              "lang ist die Seite $b$?", 30, 9, "cm"),
             ("Ein rechteckiges Foto hat einen Umfang von {u}, eine Seite ist "
              "{a2} lang. Wie lang ist die andere Seite?", 24, 7, "cm"),
             ("Ein rechteckiger Spielplatz ist mit {u} Zaun eingefasst und "
              "{a2} lang. Wie breit ist er?", 40, 12, "m"),
             ("Ein Rechteck hat den Umfang {u} und die Seite $a = {av}$ {e}. Wie "
              "lang ist die Seite $b$?", 18, 5, "m"),
             ("Um ein rechteckiges Beet laufen {u} Kantensteine, es ist {a2} "
              "lang. Wie breit ist das Beet?", 50, 15, "m"),
             ("Ein Rechteck hat den Umfang {u} und die Seite $a = {av}$ {e}. Wie "
              "lang ist die Seite $b$?", 22, 6.5, "cm"),
             ("Ein rechteckiges Tischtuch hat einen Umfang von {u}, eine Seite "
              "ist {a2} lang. Wie lang ist die andere Seite?", 36, 10, "dm"),
             ("Ein rechteckiger Rahmen hat einen Umfang von {u}, eine Seite "
              "ist {a2} lang. Wie lang ist die andere Seite?", 44, 13, "cm"),
             ("Ein Rechteck hat den Umfang {u} und die Seite $a = {av}$ {e}. Wie "
              "lang ist die Seite $b$?", 16, 4.5, "cm"),
             ("Ein rechteckiges Feld ist mit {u} Band abgesteckt und {a2} "
              "lang. Wie breit ist es?", 60, 18, "m")]
    aus = []
    for text, u, a, e in daten:
        b = u / 2 - a
        aus.append(A(text.format(u=f"${u}$ {e}", av=dez(a), e=e,
                                 a2=f"${dez(a)}$ {e}") + " {K}",
                     f"${u} : 2 = {dez(u / 2)}$; ${dez(u / 2)} - {dez(a)} = "
                     f"{dez(b)}$ {e}", f"{u}/2-{a}", antwort=f"__ {e}"))
    return aus


AUFGABEN["Rechteckseite aus Umfang berechnen"] = _t32()


# T33 Term vereinfachen – 2025-GYM-B2a („6x − 3x² − 4x, Wert für x = 2“)
def _t33():
    daten = [  # (Term, Vereinfachung, Weg, Variable, Wert, Rechnung, pruef)
        ("7x - 2x^2 - 3x", "7x - 3x = 4x", "4x - 2x^2", "x", 1,
         "4 \\cdot 1 - 2 \\cdot 1^2 = 4 - 2 = 2", "4*1-2*1**2"),
        ("9y - y^2 - 4y", "9y - 4y = 5y", "5y - y^2", "y", 3,
         "5 \\cdot 3 - 3^2 = 15 - 9 = 6", "5*3-3**2"),
        ("5a + 2a^2 - 8a", "5a - 8a = -3a", "2a^2 - 3a", "a", 2,
         "2 \\cdot 2^2 - 3 \\cdot 2 = 8 - 6 = 2", "2*2**2-3*2"),
        ("12x - 4x^2 - 9x", "12x - 9x = 3x", "3x - 4x^2", "x", 1,
         "3 \\cdot 1 - 4 \\cdot 1^2 = 3 - 4 = -1", "3*1-4*1**2"),
        ("3b^2 + 6b - 2b^2", "3b^2 - 2b^2 = b^2", "b^2 + 6b", "b", -1,
         "(-1)^2 + 6 \\cdot (-1) = 1 - 6 = -5", "(-1)**2+6*(-1)"),
        ("10m - 3m^2 - 6m", "10m - 6m = 4m", "4m - 3m^2", "m", 2,
         "4 \\cdot 2 - 3 \\cdot 2^2 = 8 - 12 = -4", "4*2-3*2**2"),
        ("4x^2 - 5x + 2x", "-5x + 2x = -3x", "4x^2 - 3x", "x", 3,
         "4 \\cdot 3^2 - 3 \\cdot 3 = 36 - 9 = 27", "4*3**2-3*3"),
        ("11n - 2n^2 - 8n", "11n - 8n = 3n", "3n - 2n^2", "n", -2,
         "3 \\cdot (-2) - 2 \\cdot (-2)^2 = -6 - 8 = -14",
         "3*(-2)-2*(-2)**2"),
        ("2k - 5k^2 + 6k", "2k + 6k = 8k", "8k - 5k^2", "k", 1,
         "8 \\cdot 1 - 5 \\cdot 1^2 = 8 - 5 = 3", "8*1-5*1**2"),
        ("6z - z^2 - 10z", "6z - 10z = -4z", "-4z - z^2", "z", -3,
         "-4 \\cdot (-3) - (-3)^2 = 12 - 9 = 3", "-4*(-3)-(-3)**2"),
    ]
    aus = []
    for t, zus, erg, v, w, r, p in daten:
        aus.append(A(f"Vereinfache den Term ${t}$ und berechne seinen Wert für "
                     f"${v} = {w}$. {{K}}",
                     f"${zus}$, Term ${erg}$; für ${v} = {w}$: ${r}$", p,
                     antwort=""))
    return aus


AUFGABEN["Term durch Zusammenfassen gleichartiger Glieder vereinfachen"] = _t33()


# T34 Trigonometrische Gleichung nach Seite umstellen – 2020-OS-B1j
def _t34():
    wert = {("sin", 30): ("0{,}5", 0.5), ("cos", 60): ("0{,}5", 0.5),
            ("tan", 45): ("1", 1), ("sin", 90): ("1", 1)}
    daten = [("sin", 30, "5", "unten"), ("cos", 60, "9", "unten"),
             ("tan", 45, "11", "unten"), ("sin", 30, "2{,}5", "unten"),
             ("cos", 60, "3", "unten"), ("sin", 30, "12", "oben"),
             ("cos", 60, "10", "oben"), ("tan", 45, "8", "oben"),
             ("sin", 90, "7", "unten"), ("sin", 30, "4{,}5", "unten")]
    aus = []
    for f, w, z, lage in daten:
        wt, wv = wert[(f, w)]
        zv = float(z.replace("{,}", "."))
        fn = f"\\mathrm{{{f}}}\\,{w}^\\circ"
        rad = f"math.{f}(math.radians({w}))"
        if lage == "unten":
            gl = f"{fn} = \\frac{{{z}}}{{x}}"
            x = zv / wv
            weg = f"$x = {z} : {fn} = {z} : {wt} = {dez(x)}$"
            p = f"{zv}/{rad}"
        else:
            gl = f"{fn} = \\frac{{x}}{{{z}}}"
            x = zv * wv
            weg = f"$x = {z} \\cdot {fn} = {z} \\cdot {wt} = {dez(x)}$"
            p = f"{zv}*{rad}"
        # v0.7 (Lehrer 02.10.): nur umstellen, kein Zahlenwert
        del weg, p, x
        op = ":" if lage == "unten" else "\\cdot"
        aus.append(A(f"${gl}$. Stelle nach $x$ um.",
                     f"$x = {z} {op} {fn}$", f"{zv:g}",
                     antwort="$x =$ __"))
    return aus


AUFGABEN["Trigonometrische Gleichung nach Seite umstellen"] = _t34()


# T35 Uhrzeit aus Startzeit und Dauer berechnen – 2021-OS-B1a
def _t35():
    daten = [("Ein Zug fährt um {s} Uhr ab und ist {d} unterwegs. Wann kommt "
              "er an?", 8, 45, 2, 30),
             ("Ein Film beginnt um {s} Uhr und dauert {d}. Wann ist er zu "
              "Ende?", 13, 50, 1, 25),
             ("Ein Bus fährt um {s} Uhr ab, die Fahrt dauert {d}. Wann kommt "
              "er an?", 10, 27, 3, 48),
             ("Eine Wanderung beginnt um {s} Uhr und dauert {d}. Wann endet "
              "sie?", 7, 55, 0, 45),
             ("Ein Flug startet um {s} Uhr und dauert {d}. Wann landet das "
              "Flugzeug?", 15, 36, 2, 44),
             ("Ein Konzert beginnt um {s} Uhr und dauert {d}. Wann ist es zu "
              "Ende?", 21, 40, 1, 35),
             ("Eine Fähre legt um {s} Uhr ab und ist {d} unterwegs. Wann "
              "kommt sie an?", 6, 18, 4, 52),
             ("Ein Radrennen startet um {s} Uhr, der Sieger braucht {d}. Wann "
              "kommt er ins Ziel?", 12, 49, 2, 26),
             ("Ein Zug fährt um {s} Uhr ab und ist {d} unterwegs. Wann kommt "
              "er an?", 9, 5, 3, 58),
             ("Ein Theaterstück beginnt um {s} Uhr und dauert {d}. Wann ist es "
              "zu Ende?", 17, 44, 1, 29)]
    aus = []
    for text, h, m, dh, dm in daten:
        ende = h * 60 + m + dh * 60 + dm
        eh, em = divmod(ende, 60)
        zw = h + dh
        d = (f"${dh}$ h ${dm}$ min" if dh else f"${dm}$ min")
        s = f"{h}:{m:02d}"
        if dh:
            weg = (f"{s} Uhr $+ {dh}$ h $=$ {zw}:{m:02d} Uhr, $+ {dm}$ min $=$ "
                   f"{eh}:{em:02d} Uhr")
            p = f"[{zw}, ({h}*60+{m}+{dh}*60+{dm})//60]"
        else:
            weg = f"{s} Uhr $+ {dm}$ min $=$ {eh}:{em:02d} Uhr"
            p = f"[({h}*60+{m}+{dm})//60]"
        aus.append(A(text.format(s=s, d=d) + " {K}", weg, p,
                     antwort="__ Uhr"))
    return aus


AUFGABEN["Uhrzeit aus Startzeit und Dauer berechnen"] = _t35()


# T36 Volumen Würfel berechnen – 2026-FOR-B1f
def _t36():
    daten = [("Ein Würfel hat die Kantenlänge $4$ cm. Gib sein Volumen an.",
              4, "cm"),
             ("Ein Würfel hat die Kantenlänge $5$ cm. Gib sein Volumen an.",
              5, "cm"),
             ("Ein würfelförmiger Karton ist $10$ cm lang, breit und hoch. Gib "
              "sein Volumen an.", 10, "cm"),
             ("Ein würfelförmiger Container hat die Kantenlänge $6$ m. Gib "
              "sein Volumen an.", 6, "m"),
             ("Ein würfelförmiges Becken ist innen $2$ m lang, breit und tief. "
              "Wie viel Wasser passt hinein?", 2, "m"),
             ("Ein Würfel hat die Kantenlänge $7$ cm. Gib sein Volumen an.",
              7, "cm"),
             ("Ein Holzwürfel hat die Kantenlänge $9$ cm. Gib sein Volumen "
              "an.", 9, "cm"),
             ("Eine würfelförmige Kiste hat die Kantenlänge $0{,}5$ m. Gib ihr "
              "Volumen an.", 0.5, "m"),
             ("Ein Würfel aus Ton hat die Kantenlänge $20$ cm. Gib sein "
              "Volumen an.", 20, "cm"),
             ("Ein Würfel hat die Kantenlänge $11$ cm. Gib sein Volumen an.",
              11, "cm")]
    aus = []
    for text, a, e in daten:
        v = a ** 3
        at = dez(a)
        vt = f"{v:,.3f}".rstrip("0").rstrip(".").replace(",", "\\,").replace(
            ".", "{,}") if a % 1 else f"{v:,}".replace(",", "\\,")
        aus.append(A(f"{text} {{K}}",
                     f"${at} \\cdot {at} \\cdot {at} = {vt}$ {e}³ (nicht "
                     f"${at} \\cdot {at} = {dez(a * a)}$)", f"{a}**3",
                     antwort=f"__ {e}³"))
    return aus


AUFGABEN["Volumen Würfel berechnen"] = _t36()


# T37 Vorzeichenregel anwenden – 2015-OS-B1g (Ankreuzen)
def _t37():
    opt = ["immer positiv", "immer negativ", "Das kann man nicht entscheiden."]
    daten = [("Eine negative Zahl wird mit einer positiven Zahl multipliziert.",
              1),
             ("Eine positive Zahl wird durch eine negative Zahl geteilt.", 1),
             ("Eine negative Zahl wird durch eine negative Zahl geteilt.", 0),
             ("Zwei negative Zahlen werden addiert.", 1),
             ("Eine positive und eine negative Zahl werden addiert.", 2),
             ("Von einer negativen Zahl wird eine positive Zahl subtrahiert.",
              1),
             ("Drei negative Zahlen werden miteinander multipliziert.", 1),
             ("Eine negative Zahl wird mit sich selbst multipliziert.", 0),
             ("Von einer negativen Zahl wird eine negative Zahl subtrahiert.",
              2),
             ("Von einer positiven Zahl wird eine negative Zahl subtrahiert.",
              0)]
    return [X(f"{t} Das Ergebnis ist … {{K}}", opt, opt[r]) for t, r in daten]


AUFGABEN["Vorzeichenregel anwenden"] = _t37()


# T38 Wert nach prozentualer Erhöhung berechnen – 2024-OS-B1e
def _t38():
    daten = [("Eine Kinokarte kostet {g} und wird um {p} teurer.", 4, 25),
             ("Ein Buch kostet {g} und wird um {p} teurer.", 8, 50),
             ("Eine Brezel kostet {g} und wird um {p} teurer.", 2.5, 20),
             ("Ein Monatsticket kostet {g} und wird um {p} teurer.", 30, 10),
             ("Ein Heft kostet {g} und wird um {p} teurer.", 1.6, 25),
             ("Eine Pizza kostet {g} und wird um {p} teurer.", 12, 5),
             ("Ein Kurs kostet {g} und wird um {p} teurer.", 40, 15),
             ("Ein Eintritt kostet {g} und wird um {p} teurer.", 7.5, 20),
             ("Eine Jahreskarte kostet {g} und wird um {p} teurer.", 60, 30),
             ("Ein Döner kostet {g} und wird um {p} teurer.", 5.2, 50)]
    aus = []
    for text, g, p in daten:
        neu = g * (100 + p) / 100
        auf = g * p / 100
        z = 2 if (g % 1 or neu % 1 or auf % 1) else None
        fak = dez((100 + p) / 100)
        aus.append(A(text.format(g=f"${eur(g, z)}$", p=f"${pz(p)}$")
                     + " Wie hoch ist der neue Preis? {K}",
                     f"${dez(g) if not z else f'{g:.2f}'.replace('.', '{,}')} "
                     f"\\cdot {fak} = {eur(neu, z)}$ (nicht nur "
                     f"${eur(auf, z)}$)", f"{g}*{(100 + p) / 100}",
                     antwort="__ €"))
    return aus


AUFGABEN["Wert nach prozentualer Erhöhung berechnen"] = _t38()


# T39 Wertetabelle einer Funktion zuordnen – 2026-FOR-B1e (Ankreuzen)
def _t39():
    X5 = [-2, -1, 0, 1, 2]
    X4 = [-4, -2, 0, 2, 4]
    daten = [  # (Term, xs, f, Ablenker, richtig an Stelle, Begründung, pruef)
        ("2x^2", X5, lambda x: 2 * x * x, [lambda x: 2 * x,
         lambda x: (2 * x) ** 2], 2, "$2 \\cdot 2^2 = 8$ – erst quadrieren, "
         "dann malnehmen", "2*2**2"),
        ("5x^2", X5, lambda x: 5 * x * x, [lambda x: (5 * x) ** 2,
         lambda x: 5 * x], 0, "$5 \\cdot 2^2 = 20$ – erst quadrieren, dann "
         "malnehmen", "5*2**2"),
        ("0{,}5x^2", X4, lambda x: x * x // 2, [lambda x: (x // 2) ** 2,
         lambda x: x // 2], 1, "$0{,}5 \\cdot 4^2 = 8$ – erst quadrieren, "
         "dann malnehmen", "0.5*4**2"),
        ("-x^2", X5, lambda x: -x * x, [lambda x: x * x, lambda x: -x], 2,
         "$-(2^2) = -4$ – erst quadrieren, dann das Minus", "-(2**2)"),
        ("x^2 + 1", X5, lambda x: x * x + 1, [lambda x: (x + 1) ** 2,
         lambda x: x + 1], 0, "$2^2 + 1 = 5$ – erst quadrieren, dann "
         "addieren", "2**2+1"),
        ("x^2 - 3", X5, lambda x: x * x - 3, [lambda x: (x - 3) ** 2,
         lambda x: x - 3], 1, "$2^2 - 3 = 1$ – erst quadrieren, dann "
         "subtrahieren", "2**2-3"),
        ("-2x^2", X5, lambda x: -2 * x * x, [lambda x: (2 * x) ** 2,
         lambda x: -2 * x], 2, "$-2 \\cdot 2^2 = -8$ – erst quadrieren, dann "
         "malnehmen", "-2*2**2"),
        ("(x + 1)^2", X5, lambda x: (x + 1) ** 2, [lambda x: x * x + 1,
         lambda x: x + 1], 1, "$(1 + 1)^2 = 4$ – erst die Klammer, dann "
         "quadrieren", "(1+1)**2"),
        ("10x^2", X5, lambda x: 10 * x * x, [lambda x: (10 * x) ** 2,
         lambda x: 10 * x], 0, "$10 \\cdot 2^2 = 40$ – erst quadrieren, dann "
         "malnehmen", "10*2**2"),
        ("-0{,}5x^2", X4, lambda x: -(x * x) // 2, [lambda x: x * x // 2,
         lambda x: -(x // 2)], 2, "$-0{,}5 \\cdot 4^2 = -8$ – erst "
         "quadrieren, dann malnehmen", "-0.5*4**2"),
    ]
    aus = []
    for term, xs, f, abl, stelle, grund, p in daten:
        fs = abl[:]
        fs.insert(stelle, f)
        tabs = []
        for b, g in zip("ABC", fs):
            werte = ",".join(str(g(x)) for x in xs)
            tabs.append(f"{b}: \\wertetabelle[{werte}]{{x}}{{y}}"
                        f"{{{','.join(str(x) for x in xs)}}}")
        aus.append(X(f"Welche Wertetabelle gehört zu $y = {term}$? {{K}}",
                     list("ABC"), f"Tabelle {'ABC'[stelle]}: {grund}", p,
                     " ".join(tabs)))
    return aus


AUFGABEN["Wertetabelle einer Funktion zuordnen"] = _t39()


# T40 Wurzel eines Quadrats berechnen – 2015-OS-B1j (Ankreuzen)
def _t40():
    aus = []
    for z in [5, 9, 11, 6, 12, 8, 15, 3, 10, 20]:
        w = f"\\sqrt{{(-{z})^2}}"
        opt = [f"${w} = -{z}$", f"${w} = {z}$", f"${w}$ ist nicht definiert"]
        aus.append(X("Welche Aussage ist wahr? Kreuze an. {K}", opt,
                     f"${w} = {z}$, denn erst das Quadrat: $(-{z})^2 = {z * z}$, "
                     "und die Wurzel ist nie negativ", str(z)))
    return aus


AUFGABEN["Wurzel eines Quadrats berechnen"] = _t40()


# T41 y-Achsenabschnitt ablesen – 2024-OS-B1i (Zeichnen im ksys)
def _t41():
    aus = []
    for m, n in [(2, 1), (-1, 2), (0.5, 3), (-2, -2), (1, -4), (-3, 4),
                 (0.25, -2), (-0.5, -3), (1.5, 1), (-1, -1)]:
        mt = dez(m)
        term = (("" if m == 1 else "-" if m == -1 else mt) + "x"
                + (f" + {dez(n)}" if n > 0 else f" - {dez(-n)}"))
        aus.append(A("Schnittpunkt mit der y-Achse: Markiere ihn an der "
                     f"Geraden $y = {term}$. {{K}}", f"$(0|{n})$",
                     f"[0, {n}]", form="zeichnen", antwort="",
                     grafik=("\\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5,"
                             f"ablesen] \\gerade{{{mt.replace('{,}', '.')}}}"
                             f"{{{n}}}{{g}} \\end{{ksys}}")))
    return aus


AUFGABEN["y-Achsenabschnitt ablesen"] = _t41()


# --- Erweiterung 02.10.2026 (Lehrer): alle Basistypen der P10 ---------------
# Ziel je Typ: ZIEL (Ankreuz- und Kurzaufgaben in Prüfungsform). Jedes
# Ergebnis wird hier mit sympy nachgerechnet (assert), bevor es in den Text
# geht. Distraktoren aus dem Feld fehlerquelle der Originale.
import sympy as _sp
from fractions import Fraction as _F
from statistics import median as _median

ZIEL = {"Bruchteil einer Fläche bestimmen": 20, "Lineare Gleichung lösen": 20,
        "Term zu Figur angeben": 20, "Pythagoras Gleichung zuordnen": 20}
for _t in ["Zeiteinheiten umrechnen", "Eigenschaft einer Figur zuordnen",
           "Größen vergleichen", "Umfang Rechteck berechnen",
           "Median bestimmen", "Proportionale Zuordnung Dreisatz",
           "Rechteckseite aus Fläche berechnen",
           "Fehlenden Wert aus Mittelwert bestimmen",
           "Satz des Pythagoras formulieren",
           "Portionen aus Gesamtmenge berechnen", "Scheitelpunkt ablesen",
           "Arithmetisches Mittel berechnen",
           "Quadratseite aus Fläche berechnen"]:
    ZIEL[_t] = 10
for _t in ["Winkel über Scheitel- oder Nebenwinkel bestimmen",
           "Zufallsgerät zu Wahrscheinlichkeit entwerfen",
           "Spannweite berechnen", "Strecke aus Teilstrecken berechnen",
           "Körper aus Netz oder Schrägbild benennen",
           "Ergebnismenge aufzählen", "Scheitelpunktform aufstellen",
           "Parabel verschieben"]:
    ZIEL[_t] = 5


def _q(x):
    """exakter Wert (sympy Rational) aus Zahl oder Text."""
    return _sp.nsimplify(str(x), rational=True)


def _gleich(a, b):
    assert _sp.simplify(_q(a) - _q(b)) == 0, (a, b)


def _w(x, e=""):
    """Zahl für LaTeX; Euro-Beträge mit zwei Nachkommastellen."""
    x = _q(x)
    if e == "€" and not x.is_Integer:
        return f"{float(x):.2f}".replace(".", "{,}")
    return _zahl(x)


def _rot(opt, i, k):
    """Optionen um k Stellen drehen; gibt (Optionen, Lösungstext)."""
    k %= len(opt)
    neu = opt[k:] + opt[:k]
    return neu, neu.index(opt[i])


def _zahl(x):
    """Zahl als LaTeX mit Dezimalkomma; Tausender mit Leerzeichen."""
    x = _q(x)
    if x.is_Integer and abs(x) >= 10000:
        s = f"{int(x):,}".replace(",", "\\,")
        return s
    return dez(float(x))


# T1b Bruchteil einer Fläche bestimmen (Varianten 11–20): Kurzantwort zu
# einer Figur – Anteil als Bruch (gekürzt) oder in Prozent. Fehlerquelle der
# Originale: grau zu weiß statt grau zu allen, Felder falsch zählen.
def _t1b():
    daten = [  # (Kontext, Figur, z, n, Prozent?)
        ("Ein Fenster besteht aus gleich großen Scheiben; die grauen sind "
         "aus Milchglas.", "\\bruchrechteck[4]{6}{10}", 6, 10, True),
        ("Eine Pizza ist in gleich große Stücke geschnitten; die grauen "
         "Stücke sind schon gegessen.", "\\bruchkreis[0.9]{6}{8}", 6, 8, False),
        ("Ein Beet ist in gleich große Streifen geteilt; auf den grauen "
         "wachsen Kräuter.", "\\bruchrechteck[4]{4}{5}", 4, 5, True),
        ("Ein Glücksrad hat gleich große Felder; die grauen sind Gewinnfelder.",
         "\\bruchkreis[0.9]{4}{6}", 4, 6, False),
        ("Eine Tafel Schokolade hat gleich große Stücke; die grauen sind "
         "schon weg.", "\\bruchrechteck[5]{10}{12}", 10, 12, False),
        ("Eine runde Torte ist in gleich große Stücke geteilt; die grauen "
         "sind verkauft.", "\\bruchkreis[0.9]{3}{10}", 3, 10, True),
        ("Ein Zaun hat gleich breite Felder; die grauen sind schon "
         "gestrichen.", "\\bruchrechteck[4]{8}{10}", 8, 10, False),
        ("Eine Uhr ist in gleich große Abschnitte geteilt; die grauen "
         "zeigen die Schulzeit.", "\\bruchkreis[0.9]{5}{8}", 5, 8, False),
        ("Ein Regal hat gleich große Fächer; die grauen sind belegt.",
         "\\bruchrechteck[5]{12}{16}", 12, 16, True),
        ("Ein runder Tisch ist in gleich große Felder geteilt; die "
         "grauen sind gedeckt.", "\\bruchkreis[0.9]{2}{5}", 2, 5, True),
    ]
    aus = []
    for text, fig, z, n, proz in daten:
        f = _F(z, n)
        if proz:
            p = _q(z) / n * 100
            assert p.is_Integer
            aus.append(A(f"{text} Wie viel Prozent der Fläche sind grau? {{K}}",
                         f"${z}$ von ${n}$ gleichen Teilen: "
                         f"$\\frac{{{z}}}{{{n}}} = {int(p)}\\,\\%$",
                         f"{z}/{n}*100", antwort="__ %", grafik=fig))
        else:
            gek = (f"$\\frac{{{z}}}{{{n}}} = "
                   f"\\frac{{{f.numerator}}}{{{f.denominator}}}$")
            if f.denominator == n:
                gek = f"$\\frac{{{z}}}{{{n}}}$"
            wie = "gekürzten " if f.denominator != n else ""
            aus.append(A(f"{text} Welcher Anteil der Fläche ist grau? Gib ihn "
                         f"als {wie}Bruch an. {{K}}",
                         f"{gek} (${z}$ von ${n}$ gleichen Teilen)",
                         f"[{f.numerator}, {f.denominator}]", grafik=fig))
    return aus


# T6b Lineare Gleichung lösen (Varianten 11–20)
def _t6b():
    daten = [(4, -2.5, 0, 0), (3, 2, 0, 21), (2, -7, 0, -4), (5, -6, 4, 4),
             (6, 1, 0, 30), (2, 5.5, 0, 0), (3, -9, -2, 1), (8, -2, 0, 40),
             (4, 6, 0, 12), (9, -3, 5, 14)]
    x = _sp.Symbol("x")
    aus = []
    for a, b, c, d in daten:
        bq, cq, dq = _q(b), _q(c), _q(d)
        los = _sp.solve(_sp.Eq(a * (x + bq) + cq, dq), x)
        assert len(los) == 1
        r = los[0]
        kl = f"x {'+' if b > 0 else '-'} {dez(abs(b))}"
        g = f"{a} \\cdot ({kl})"
        if c:
            g += f" {'+' if c > 0 else '-'} {abs(c)}"
        g += f" = {d}"
        schritte = []
        if c:
            schritte.append(f"${a} \\cdot ({kl}) = {_zahl(dq - cq)}$")
        rest = (dq - cq) / a
        schritte.append(f"${kl} = {_zahl(rest)}$")
        weg = ", ".join(schritte) + f", also $x = {_zahl(r)}$"
        aus.append(A(f"Löse die Gleichung ${g}$. {{K}}", weg,
                     str(float(r)) if not r.is_Integer else str(int(r)),
                     antwort="x = __"))
    return aus


# T42 Term zu Figur angeben – 2025-OS-B1i (Ankreuzen / Kurzantwort)
def _t42():
    R = "\\rechteck[punkte=,seiten={%s}]{%s}{%s}"
    ank = [  # (Figur, Frage, Optionen, richtig)
        (R % ("x,y,,", 3, 1.8), "den Umfang $u$",
         ["$u = x \\cdot y$", "$u = 2 \\cdot x + 2 \\cdot y$", "$u = x + y$",
          "$u = 4 \\cdot x$"], 1),
        (R % ("s,,,", 2, 2), "den Flächeninhalt $A$ des Quadrats",
         ["$A = 4 \\cdot s$", "$A = s^2$", "$A = 2 \\cdot s$", "$A = s + s$"],
         1),
        ("\\dreieckrw{3.5}{2.5}{p}{q}{r}", "den Flächeninhalt $A$",
         ["$A = p \\cdot q$", "$A = p \\cdot q : 2$", "$A = p \\cdot r : 2$",
          "$A = (p + q) : 2$"], 1),
        (R % ("a,b,,", 3.4, 1.6), "den Umfang $u$",
         ["$u = a \\cdot b$", "$u = a + b + a + b$", "$u = a + b$",
          "$u = 2 \\cdot a + b$"], 1),
        (R % ("e,,,", 2, 2), "den Umfang $u$ des Quadrats",
         ["$u = e^2$", "$u = 4 \\cdot e$", "$u = 2 \\cdot e$",
          "$u = e + 4$"], 1),
        ("\\dreieckrw{3.5}{2.5}{a}{b}{c}", "den Umfang $u$",
         ["$u = a \\cdot b : 2$", "$u = a + b + c$",
          "$u = a \\cdot b \\cdot c$", "$u = a + b$"], 1),
        (R % ("m,n,,", 3.2, 1.5), "den Flächeninhalt $A$",
         ["$A = 2 \\cdot (m + n)$", "$A = m + n$", "$A = m \\cdot n : 2$",
          "$A = m \\cdot n$"], 3),
        (R % ("3a,a,,", 3.6, 1.2), "den Flächeninhalt $A$",
         ["$A = 4 \\cdot a$", "$A = 3 \\cdot a^2$", "$A = 8 \\cdot a$",
          "$A = 3 + a^2$"], 1),
        (R % ("2k,k,,", 3.2, 1.6), "den Umfang $u$",
         ["$u = 2 \\cdot k^2$", "$u = 3 \\cdot k$", "$u = 6 \\cdot k$",
          "$u = 4 \\cdot k$"], 2),
        ("\\dreieck{(0,0)}{(3.5,0)}{(1,2)}{r}{s}{t}{}{}{}",
         "den Umfang $u$ des Dreiecks",
         ["$u = r \\cdot s \\cdot t$", "$u = 3 \\cdot r$",
          "$u = (r + s) \\cdot t$", "$u = r + s + t$"], 3),
    ]
    kurz = [  # (Figur, Größe, Lösung, Weg, pruef)
        (R % ("d,,,", 2, 2), "den Umfang $u$ des Quadrats",
         "$u = 4 \\cdot d$", "vier gleich lange Seiten", "4"),
        (R % ("k,l,,", 3.4, 1.6), "den Flächeninhalt $A$",
         "$A = k \\cdot l$", "Länge mal Breite", ""),
        ("\\dreieckrw{3}{2.2}{m}{n}{o}", "den Flächeninhalt $A$",
         "$A = m \\cdot n : 2$",
         "die Katheten $m$ und $n$ stehen senkrecht aufeinander; die "
         "Hypotenuse $o$ gehört nicht in die Formel", "2"),
        (R % ("a,b,,", 3.5, 2), "den Umfang $u$",
         "$u = 2 \\cdot a + 2 \\cdot b$",
         "je zwei Seiten sind gleich lang", "[2, 2]"),
        (R % ("3x,x,,", 3.6, 1.2), "den Umfang $u$",
         "$u = 8 \\cdot x$", "$3x + x + 3x + x = 8x$", "8"),
        (R % ("2a,a,,", 3.2, 1.6), "den Flächeninhalt $A$",
         "$A = 2 \\cdot a^2$", "$2a \\cdot a = 2a^2$", "[2, 2]"),
        (R % ("t,,,", 2, 2), "den Flächeninhalt $A$ des Quadrats",
         "$A = t^2$", "Seite mal Seite", ""),
        ("\\dreieck{(0,0)}{(3,0)}{(1.5,2.2)}{s}{s}{b}{}{}{}",
         "den Umfang $u$", "$u = 2 \\cdot s + b$",
         "zwei Schenkel $s$ und die Basis $b$", "2"),
        ("\\dreieckrw{3.4}{2}{x}{y}{z}", "den Umfang $u$",
         "$u = x + y + z$", "alle drei Seiten addieren", ""),
        (R % ("y,3,,", 3.2, 1.5), "den Flächeninhalt $A$ (Breite $3$)",
         "$A = 3 \\cdot y$", "Länge mal Breite", "3"),
    ]
    aus = []
    for k, (fig, was, opt, i) in enumerate(ank):
        o, j = _rot(opt, i, k)
        aus.append(X(f"Welche Formel beschreibt {was}? {{K}}", o, o[j],
                     grafik=fig))
    for fig, was, los, weg, pr in kurz:
        aus.append(A(f"Gib eine Formel für {was} der Figur an. {{K}}",
                     f"{los} ({weg})", pr, antwort="__", grafik=fig))
    return aus


# T43 Pythagoras Gleichung zuordnen – 2026-FOR-B1j (Ankreuzen)
def _t43():
    saetze = [("p", "q", "r", 3.5, 2.5), ("e", "f", "g", 3, 2.2),
              ("k", "l", "m", 4, 2), ("r", "s", "t", 2.5, 3),
              ("b", "c", "a", 3.5, 2), ("s", "t", "u", 3, 3),
              ("f", "g", "h", 4, 2.5), ("a", "c", "b", 2.6, 3.2),
              ("m", "n", "p", 3.6, 2.4), ("h", "k", "l", 3, 2)]
    aus = []
    for n, (k1, k2, h, w, hh) in enumerate(saetze):
        fig = f"\\dreieckrw{{{w}}}{{{hh}}}{{{k1}}}{{{k2}}}{{{h}}}"
        if n % 2 == 0:
            opt = [f"${h}^2 = {k1}^2 + {k2}^2$", f"${k1}^2 = {k2}^2 + {h}^2$",
                   f"${h}^2 = {k1}^2 - {k2}^2$", f"${h} = {k1} + {k2}$"]
            aus.append(X("Welche Gleichung gilt in diesem rechtwinkligen "
                         "Dreieck? {K}", *_x(opt, 0, n),
                         grafik=fig))
            opt = [f"${k1} = \\sqrt{{{h}^2 - {k2}^2}}$",
                   f"${k1} = \\sqrt{{{h}^2 + {k2}^2}}$",
                   f"${k1} = {h}^2 - {k2}^2$",
                   f"${k1} = \\sqrt{{{k2}^2 - {h}^2}}$"]
            aus.append(X(f"Mit welcher Gleichung berechnet man ${k1}$? {{K}}",
                         *_x(opt, 0, n + 1), grafik=fig))
        else:
            opt = [f"${h} = \\sqrt{{{k1}^2 - {k2}^2}}$",
                   f"${h} = \\sqrt{{{k1}^2 + {k2}^2}}$",
                   f"${h} = {k1}^2 + {k2}^2$", f"${h} = {k1} + {k2}$"]
            aus.append(X(f"Mit welcher Gleichung berechnet man ${h}$? {{K}}",
                         *_x(opt, 1, n), grafik=fig))
            opt = [f"${k2}^2 = {h}^2 + {k1}^2$", f"${k2}^2 = {h}^2 - {k1}^2$",
                   f"${k2}^2 = {k1}^2 - {h}^2$", f"${k2} = {h} - {k1}$"]
            aus.append(X(f"Welche Gleichung gilt für die Kathete ${k2}$? {{K}}",
                         *_x(opt, 1, n + 2), grafik=fig))
    return aus


def _x(opt, i, k):
    o, j = _rot(opt, i, k)
    return o, o[j]


# T44 Zeiteinheiten umrechnen – 2025-OS-B1b (Kurzantwort / Ankreuzen)
def _t44():
    kurz = [  # (Text, Wert, Faktor, Zieleinheit, Antwort)
        ("Ein Training dauert $0{,}2$ h. Gib die Dauer in Minuten an.",
         "0.2", 60, "min"),
        ("Eine Ampel bleibt $3$ min rot. Gib die Zeit in Sekunden an.",
         "3", 60, "s"),
    ]
    # Bündel (v0.7): eine Dauer in zwei Einheiten
    buendel = [  # (Satz, Wert, Faktor, klein, groß)
        ("Eine Busfahrt dauert $2{,}5$ h.", "2.5", 60, "min", "h"),
        ("Eine Wanderung dauert $4{,}25$ h.", "4.25", 60, "min", "h"),
        ("Ein Kuchen backt $1{,}2$ h.", "1.2", 60, "min", "h"),
        ("Ein Zeltlager dauert $2{,}5$ Tage.", "2.5", 24, "h", "Tage"),
        ("Eine Autofahrt dauert $3{,}2$ h.", "3.2", 60, "min", "h"),
    ]
    wort = {"min": "Minuten", "h": "Stunden", "Tage": "Tagen"}
    bnd = []
    for satz, w, f, kl, gr in buendel:
        r = _q(w) * f
        assert r.is_Integer
        ganz, rest = divmod(int(r), f)
        assert _q(ganz) + _sp.Rational(rest, f) == _q(w)
        bnd.append(A(f"{satz} Gib die Dauer an a) in {wort[kl]}, b) in "
                     f"{wort[gr]} und {wort[kl]}.",
                     f"a) ${dez(float(w))} \\cdot {f} = {_zahl(r)}$ {kl} "
                     f"b) ${ganz}$ {gr} ${rest}$ {kl}",
                     f"[{r}]",
                     antwort=f"a) __ {kl} b) __ {gr} __ {kl}"))
    aus = []
    for text, w, f, e in kurz:
        r = _q(w) * f
        aus.append(A(f"{text} {{K}}",
                     f"${dez(float(w))} \\cdot {f} = {_zahl(r)}$ {e}",
                     f"{w}*{f}", antwort=f"__ {e}"))
    ank = [  # (Text, Optionen, richtig, Rechnung, Kontrolle)
        ("Ein Film dauert $1{,}75$ h. Wie viele Minuten sind das?",
         ["$95$ min", "$105$ min", "$115$ min", "$175$ min"], 1,
         "$1{,}75 \\cdot 60 = 105$", ("1.75*60", 105)),
        ("Eine Pause dauert $45$ min. Wie viele Stunden sind das?",
         ["$0{,}45$ h", "$4{,}5$ h", "$0{,}75$ h", "$0{,}5$ h"], 2,
         "$45 : 60 = 0{,}75$", ("45/60", "0.75")),
        ("Eine Zugfahrt dauert $135$ min. Wie viele Stunden sind das?",
         ["$1{,}35$ h", "$2{,}25$ h", "$2{,}15$ h", "$1{,}75$ h"], 1,
         "$135 : 60 = 2{,}25$", ("135/60", "2.25")),
    ]
    for text, opt, i, weg, (p, soll) in ank:
        _gleich(_sp.sympify(p), soll)
        aus.append(X(f"{text} Kreuze an. {{K}}", opt, f"{opt[i]}: {weg}", p))
    gemischt = []
    for b, e in zip(bnd, aus):
        gemischt += [b, e]
    return gemischt


# T45 Eigenschaft einer Figur zuordnen – 2026-FOR-B1c (Ankreuzen)
def _t45():
    daten = [
        ("Rechteck", ["sind die Diagonalen gleich lang",
                      "stehen die Diagonalen senkrecht aufeinander",
                      "sind alle Seiten gleich lang"], 0),
        ("Raute", ["sind alle Winkel rechte Winkel",
                   "sind alle Seiten gleich lang",
                   "sind die Diagonalen gleich lang"], 1),
        ("Quadrat", ["gibt es genau eine Symmetrieachse",
                     "sind zwei Winkel stumpf",
                     "sind die Diagonalen gleich lang und stehen senkrecht "
                     "aufeinander"], 2),
        ("Drachenviereck", ["stehen die Diagonalen senkrecht aufeinander",
                            "sind gegenüberliegende Seiten parallel",
                            "sind alle Seiten gleich lang"], 0),
        ("gleichseitigen Dreieck", ["gibt es einen rechten Winkel",
                                     "ist jeder Winkel $60^\\circ$ groß",
                                     "ist ein Winkel stumpf"], 1),
        ("Parallelogramm", ["sind die Diagonalen gleich lang",
                            "sind alle Winkel gleich groß",
                            "halbieren sich die Diagonalen gegenseitig"], 2),
        ("rechtwinkligen Dreieck", ["liegt die längste Seite dem rechten "
                                     "Winkel gegenüber",
                                     "sind zwei Seiten gleich lang",
                                     "ist ein Winkel stumpf"], 0),
        ("gleichschenkligen Dreieck", ["sind alle Seiten gleich lang",
                                        "sind zwei Winkel gleich groß",
                                        "gibt es einen rechten Winkel"], 1),
        ("Viereck", ["gibt es ein Paar paralleler Seiten",
                     "sind zwei Seiten gleich lang",
                     "beträgt die Summe der Innenwinkel $360^\\circ$"], 2),
        ("Dreieck", ["beträgt die Summe der Innenwinkel $180^\\circ$",
                     "ist ein Winkel ein rechter Winkel",
                     "sind zwei Seiten gleich lang"], 0),
    ]
    assert _sp.Integer(180) - 60 - 60 == 60
    aus = []
    for fig, opt, i in daten:
        aus.append(X(f"Kreuze die richtige Ergänzung an: „In jedem {fig} "
                     "…“ {K}", ["… " + o + "." for o in opt],
                     f"… {opt[i]}."))
    return aus


# T46 Größen vergleichen – 2026-FOR-B1d (Eintragen <, =, >)
def _t46():
    daten = [  # (links Wert, Einheit, rechts Wert, Einheit, Faktor l→r)
        ("0.8", "km", "80", "m", 1000), ("1.5", "kg", "1500", "g", 1000),
        ("0.3", "l", "30", "ml", 1000), ("45", "mm", "4.5", "dm", "1/100"),
        ("2.4", "t", "240", "kg", 1000), ("0.05", "m", "5", "cm", 100),
        ("7", "dm", "0.07", "m", "1/10"), ("120", "cm", "12", "m", "1/100"),
        ("650", "g", "0.65", "kg", "1/1000"), ("2.5", "h", "250", "min", 60),
    ]
    aus = []
    for l, el, r, er, f in daten:
        lw = _q(l) * _q(f)
        rw = _q(r)
        z = "<" if lw < rw else ">" if lw > rw else "="
        ld, rd = dez(float(l)), dez(float(r))
        aus.append(A(f"Vergleiche ${ld}$ {el} und ${rd}$ {er}. Setze das "
                     "richtige Zeichen ein: $<$, $=$ oder $>$. {K}",
                     f"${ld}$ {el} $= {_zahl(lw)}$ {er}, also "
                     f"${ld}$ {el} ${z}$ ${rd}$ {er}",
                     f"{l}*{f}", antwort=f"${ld}$ {el} __ ${rd}$ {er}"))
    return aus


# T47 Umfang Rechteck berechnen – 2026-FOR-B1h (Kurzantwort)
def _t47():
    daten = [("Ein Beet", "4.5", "2", "m"), ("Ein Bilderrahmen", "30", "20", "cm"),
             ("Eine Tischplatte", "1.2", "0.8", "m"),
             ("Ein Spielfeld", "40", "25", "m"),
             ("Eine Briefmarke", "3", "2.5", "cm"),
             ("Ein Handy", "15", "7.5", "cm"), ("Eine Weide", "60", "35", "m"),
             ("Eine Tafel", "3.6", "1.2", "m"),
             ("Ein Sandkasten", "2.25", "1.75", "m"),
             ("Ein Fenster", "1.3", "0.9", "m")]
    aus = []
    for was, a, b, e in daten:
        u = 2 * (_q(a) + _q(b))
        aus.append(A(f"{was} ist rechteckig, ${dez(float(a))}$ {e} lang und "
                     f"${dez(float(b))}$ {e} breit. Berechne den Umfang. {{K}}",
                     f"$u = 2 \\cdot ({dez(float(a))} + {dez(float(b))}) = "
                     f"{_zahl(u)}$ {e}", f"2*({a}+{b})", antwort=f"u = __ {e}"))
    return aus


# T48 Median bestimmen – 2024-OS-B1h (Kurzantwort)
def _t48():
    daten = [
        ("Tore in fünf Spielen", ["3", "1", "4", "0", "2"], ""),
        ("Wartezeiten an der Kasse in Minuten", ["12", "7", "9", "15", "7",
                                                  "10"], "min"),
        ("Punkte in einem Test", ["18", "25", "21", "16", "23", "19", "22"],
         "Punkte"),
        ("Preise für eine Kugel Eis in Euro", ["1.5", "1.2", "1.8", "1.4"],
         "€"),
        ("Schlafdauer in Stunden", ["8", "7", "9", "6", "7"], "h"),
        ("Körpergrößen in Zentimetern", ["162", "175", "168", "171", "159",
                                         "180"], "cm"),
        ("Wurfweiten in Metern", ["24", "31", "27", "19", "35", "28", "22"],
         "m"),
        ("Laufzeiten in Sekunden", ["14", "12", "15", "13"], "s"),
        ("Taschengeld im Monat in Euro", ["20", "15", "30", "25", "10"], "€"),
        ("Seitenzahlen von Büchern", ["240", "180", "320", "210", "260",
                                      "190"], "Seiten"),
    ]
    aus = []
    for was, werte, e in daten:
        q = [_q(w) for w in werte]
        m = _sp.nsimplify(_median(q))
        s = sorted(q)
        liste = "; ".join(f"${_w(w, e)}$" for w in werte)
        geo = "; ".join(f"${_w(w, e)}$" for w in s)
        if len(q) % 2:
            weg = f"geordnet {geo}; der mittlere Wert ist ${_zahl(m)}$"
        else:
            a, b = s[len(s) // 2 - 1], s[len(s) // 2]
            weg = (f"geordnet {geo}; $({_w(a, e)} + {_w(b, e)}) : 2 "
                   f"= {_w(m, e) if e == '€' and len(str(m)) < 5 else _zahl(m)}$")
        aus.append(A(f"{was}: {liste}. Bestimme den Median. {{K}}",
                     weg + (f" {e}" if e else ""), str(float(m)),
                     antwort=f"__ {e}".rstrip()))
    return aus


# T49 Proportionale Zuordnung Dreisatz – 2023-OS-B1a (Kurzantwort)
def _t49():
    daten = [  # (Satz mit {a} {b}, a, b, Frage mit {c}, c, Einheit)
        ("{a} Brötchen kosten {b} €.", "4", "1.6",
         "Wie viel kosten {c} Brötchen?", "7", "€"),
        ("{a} l Benzin kosten {b} €.", "5", "9",
         "Wie viel kosten {c} l?", "8", "€"),
        ("Ein Drucker druckt {b} Seiten in {a} min.", "2", "12",
         "Wie viele Seiten druckt er in {c} min?", "5", "Seiten"),
        ("{a} m Stoff kosten {b} €.", "3", "21",
         "Wie viel kosten {c} m?", "5", "€"),
        ("Für {a} Kekse braucht man {b} g Mehl.", "10", "250",
         "Wie viel Mehl braucht man für {c} Kekse?", "24", "g"),
        ("Ein Wasserhahn füllt {b} l in {a} min.", "4", "6",
         "Wie viele Liter sind es in {c} min?", "10", "l"),
        ("Für {a} h Arbeit bekommt Lea {b} €.", "3", "42",
         "Wie viel bekommt sie für {c} h?", "5", "€"),
        ("{a} kg Kartoffeln kosten {b} €.", "2", "3.4",
         "Wie viel kosten {c} kg?", "6", "€"),
        ("Ein Auto braucht für {a} km {b} l Benzin.", "150", "9",
         "Wie viel braucht es für {c} km?", "250", "l"),
        ("{a} Hefte kosten {b} €.", "8", "12",
         "Wie viel kosten {c} Hefte?", "3", "€"),
    ]
    aus = []
    for satz, a, b, frage, c, e in daten:
        aq, bq, cq = _q(a), _q(b), _q(c)
        r = bq / aq * cq
        eins = bq / aq
        f = (lambda x: f"${dez(float(x))}$")
        wert = (eur(float(r), 2) + "$" if e == "€"
                else f"{_zahl(r)}$ {e}")
        text = (satz.format(a=f(aq), b=f"${_w(bq, e)}$") + " "
                + frage.format(c=f(cq)) + " {K}")
        weg = (f"Für $1$: ${_w(bq, e)} : {_zahl(aq)} = {_w(eins, e)}$; "
               f"${_w(eins, e)} \\cdot {_zahl(cq)} = {wert}")
        aus.append(A(text, weg, f"{b}/{a}*{c}", antwort=f"__ {e}"))
    return aus


# T50 Rechteckseite aus Fläche berechnen – 2023-OS-B1c (Kurzantwort)
def _t50():
    daten = [("Ein rechteckiges Beet", "24", "4", "m"),
             ("Ein rechteckiges Spielfeld", "1800", "30", "m"),
             ("Ein rechteckiges Foto", "150", "10", "cm"),
             ("Eine rechteckige Tischplatte", "1.2", "1.5", "m"),
             ("Eine rechteckige Platte", "3600", "40", "mm"),
             ("Eine rechteckige Terrasse", "27", "4.5", "m"),
             ("Ein rechteckiges Plakat", "3000", "50", "cm"),
             ("Ein rechteckiges Grundstück", "600", "20", "m"),
             ("Eine rechteckige Heftseite", "630", "21", "cm"),
             ("Eine rechteckige Garage", "15", "2.5", "m")]
    aus = []
    for was, A_, b, e in daten:
        r = _q(A_) / _q(b)
        aus.append(A(f"{was} hat den Flächeninhalt ${_zahl(A_)}$ {e}² und "
                     f"ist ${dez(float(b))}$ {e} breit. Wie lang ist es? {{K}}",
                     f"${_zahl(A_)} : {dez(float(b))} = {_zahl(r)}$ {e}",
                     f"{A_}/{b}", antwort=f"__ {e}"))
    return aus


# T51 Fehlenden Wert aus Mittelwert bestimmen – 2022-OS-B1d (Eintragen)
def _t51():
    daten = [  # (Text, Werte mit None, Mittel, Einheit)
        ("Vier Schüler haben im Test diese Punkte", [18, 22, None, 20], 21,
         "Punkte"),
        ("Ein Eiscafé verkauft von Montag bis Freitag so viele Becher",
         [30, 45, 40, None, 35], 38, "Becher"),
        ("Eine Mannschaft schießt in fünf Spielen diese Tore",
         [2, 0, 3, None, 1], 2, "Tore"),
        ("Ein Museum zählt an drei Tagen diese Besucher", [120, 150, None],
         140, "Besucher"),
        ("In sechs Monaten fällt so viel Regen (in mm)",
         [40, 55, 35, 60, 50, None], 50, "mm"),
        ("Ein Bote liefert an vier Tagen so viele Pakete", [85, 90, None, 70],
         80, "Pakete"),
        ("Tim läuft an fünf Tagen so viele Tausend Schritte",
         [8, 11, 9, 12, None], 9, "Tausend"),
        ("Vier Kürbisse wiegen (in kg)", [6, 9, None, 7], 8, "kg"),
        ("Mia läuft vier Runden in diesen Zeiten (in Minuten)",
         [12, 15, 13, None], 14, "min"),
        ("Fünf Klassen sammeln diese Spenden (in €)", [60, 80, 75, None, 90],
         75, "€"),
    ]
    aus = []
    for text, werte, m, e in daten:
        n = len(werte)
        bek = [w for w in werte if w is not None]
        fehlt = n * m - sum(bek)
        _gleich(_sp.Rational(sum(bek) + fehlt, n), m)
        assert fehlt != m and fehlt >= 0
        liste = "; ".join("__" if w is None else f"${w}$" for w in werte)
        aus.append(A(f"{text}: {liste}. Der Durchschnitt beträgt ${m}$. "
                     f"Ergänze den fehlenden Wert. {{K}}",
                     f"${n} \\cdot {m} = {n * m}$; ${n * m} - "
                     f"{sum(bek)} = {fehlt}$",
                     f"{n}*{m}-{sum(bek)}", antwort=f"__ {e}"))
    return aus


# T52 Satz des Pythagoras formulieren – 2022-OS-B1g (Ankreuzen)
def _t52():
    daten = [
        ("Im Dreieck $ABC$ liegt der rechte Winkel bei $C$. Welche Gleichung "
         "gilt?", ["$a^2 = b^2 + c^2$", "$a^2 + b^2 = c^2$", "$a + b = c$"], 1),
        ("Im Dreieck $ABC$ liegt der rechte Winkel bei $A$. Welche Gleichung "
         "gilt?", ["$b^2 + c^2 = a^2$", "$a^2 + b^2 = c^2$",
                   "$b \\cdot c = a^2$"], 0),
        ("Wo liegt im rechtwinkligen Dreieck die Hypotenuse?",
         ["am rechten Winkel", "immer unten", "dem rechten Winkel gegenüber"],
         2),
        ("Welche Aussage gilt in jedem rechtwinkligen Dreieck?",
         ["Die Katheten sind zusammen so lang wie die Hypotenuse.",
          "Die Hypotenuse ist die längste Seite.",
          "Eine Kathete ist länger als die Hypotenuse."], 1),
        ("Im Dreieck $ABC$ liegt der rechte Winkel bei $B$. Welche Gleichung "
         "gilt?", ["$a^2 - c^2 = b^2$", "$a^2 + b^2 = c^2$",
                   "$a^2 + c^2 = b^2$"], 2),
        ("Im Dreieck $PQR$ liegt der rechte Winkel bei $Q$; die Seiten heißen "
         "$p$, $q$, $r$ (gegenüber $P$, $Q$, $R$). Welche Gleichung gilt?",
         ["$p^2 + r^2 = q^2$", "$p^2 + q^2 = r^2$", "$p + r = q$"], 0),
        ("Welche Aussage ist der Satz des Pythagoras?",
         ["Die beiden Kathetenquadrate sind zusammen doppelt so groß wie das "
          "Hypotenusenquadrat.",
          "Das Hypotenusenquadrat ist so groß wie ein Kathetenquadrat.",
          "Das Quadrat über der Hypotenuse hat denselben Flächeninhalt wie "
          "die beiden Kathetenquadrate zusammen."], 2),
        ("Für welche Dreiecke gilt der Satz des Pythagoras?",
         ["für jedes rechtwinklige Dreieck", "für jedes gleichseitige Dreieck",
          "für jedes Dreieck"], 0),
        ("Im Dreieck $EFG$ liegt der rechte Winkel bei $E$; die Seiten heißen "
         "$e$, $f$, $g$ (gegenüber $E$, $F$, $G$). Welche Gleichung gilt?",
         ["$e^2 + f^2 = g^2$", "$f^2 + g^2 = e^2$", "$e = f + g$"], 1),
        ("Welche Seiten heißen im rechtwinkligen Dreieck Katheten?",
         ["die beiden längsten Seiten", "die beiden Seiten am rechten Winkel",
          "die Seite gegenüber dem rechten Winkel"], 1),
    ]
    a, b, c = _sp.symbols("a b c", positive=True)
    assert _sp.simplify((3**2 + 4**2) - 5**2) == 0
    return [X(f"{t} Kreuze an. {{K}}", o, o[i]) for t, o, i in daten]


# T53 Portionen aus Gesamtmenge berechnen – 2022-OS-B1h (Kurzantwort)
def _t53():
    daten = [  # (Text, gesamt groß, Einheit groß, Faktor, Einheit klein,
               #  Portion, Antworteinheit)
        ("In einer Kanne sind $2$ l Saft. Ein Becher fasst $250$ ml. Wie "
         "viele Becher kann man füllen?", "2", "l", 1000, "ml", 250, "Becher"),
        ("Ein Bäcker hat $3$ kg Mehl. Für einen Kuchen braucht er $500$ g. "
         "Für wie viele Kuchen reicht das Mehl?", "3", "kg", 1000, "g", 500,
         "Kuchen"),
        ("Ein Band ist $1{,}2$ m lang. Es wird in Stücke von $15$ cm "
         "geschnitten. Wie viele Stücke entstehen?", "1.2", "m", 100, "cm", 15,
         "Stücke"),
        ("Ein Topf enthält $4{,}5$ l Suppe. Ein Teller fasst $300$ ml. Wie "
         "viele Teller kann man füllen?", "4.5", "l", 1000, "ml", 300,
         "Teller"),
        ("Für ein Grillfest gibt es $2{,}4$ kg Hackfleisch. Ein Burger braucht "
         "$120$ g. Wie viele Burger kann man machen?", "2.4", "kg", 1000, "g",
         120, "Burger"),
        ("Eine Übungsstunde dauert $1$ h. Eine Aufgabe dauert $4$ min. Wie "
         "viele Aufgaben schafft man?", "1", "h", 60, "min", 4, "Aufgaben"),
        ("Eine Flasche enthält $0{,}75$ l Sirup. Für ein Glas braucht man "
         "$25$ ml. Für wie viele Gläser reicht der Sirup?", "0.75", "l", 1000,
         "ml", 25, "Gläser"),
        ("Eine Stoffbahn ist $5$ m lang. Sie wird in Stücke von $25$ cm "
         "geschnitten. Wie viele Stücke entstehen?", "5", "m", 100, "cm", 25,
         "Stücke"),
        ("Ein Korb enthält $3{,}6$ kg Äpfel. Eine Tüte fasst $450$ g. Wie "
         "viele Tüten kann man füllen?", "3.6", "kg", 1000, "g", 450, "Tüten"),
        ("In einer Packung sind $2{,}4$ l Milch. Eine Tasse fasst $200$ ml. "
         "Wie viele Tassen kann man füllen?", "2.4", "l", 1000, "ml", 200,
         "Tassen"),
    ]
    aus = []
    for text, g, eg, f, ek, p, e in daten:
        gk = _q(g) * f
        r = gk / p
        assert r.is_Integer
        aus.append(A(f"{text} {{K}}",
                     f"${dez(float(g))}$ {eg} $= {_zahl(gk)}$ {ek}; "
                     f"${_zahl(gk)} : {p} = {int(r)}$",
                     f"{g}*{f}/{p}", antwort=f"__ {e}"))
    return aus


def _ks(*teile):
    return ("\\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5,ablesen] "
            + " ".join(teile) + " \\end{ksys}")


def _pt(x, y):
    return f"({x}|{y})".replace("-", "-")


# T54 Scheitelpunkt ablesen – 2021-OS-B1d (Ankreuzen am Graphen)
def _t54():
    daten = [(1, 2, -3), (1, -1, 3), (-1, 3, 1), (1, -4, -3), (-1, 1, 4),
             (-1, -2, 3), (-1, 0, 3), (-1, 2, 2), (1, 4, -1), (1, -1, -4)]
    aus = []
    for k, (a, d, e) in enumerate(daten):
        kand = []
        for p in [(d, e), (e, d), (-d, e), (d, -e), (-d, -e), (-e, -d)]:
            if p not in kand:
                kand.append(p)
        opt = [f"$S{_pt(*p)}$" for p in kand[:4]]
        o, j = _rot(opt, 0, k)
        # Kontrolle: Scheitel ist Extremstelle von a(x-d)^2+e
        x = _sp.Symbol("x")
        f = a * (x - d) ** 2 + e
        assert _sp.solve(_sp.diff(f, x), x) == [d] and f.subs(x, d) == e
        aus.append(X("Gib den Scheitelpunkt der Parabel an. Kreuze an. {K}",
                     o, o[j], f"[{d}, {e}]",
                     _ks(f"\\parabel{{{a}}}{{{d}}}{{{e}}}{{}}")))
    return aus


# T55 Arithmetisches Mittel berechnen – 2021-OS-B1f (Kurzantwort)
def _t55():
    daten = [
        ("Eine Radtour dauert drei Tage. Gefahren werden", ["42", "35", "49"],
         "km", "Strecke pro Tag"),
        ("In vier Spielen erzielt Ben", ["12", "18", "9", "21"], "Punkte",
         "Punktzahl"),
        ("Lena hat diese Noten", ["2", "3", "1", "2", "2"], "",
         "Note"),
        ("Ein Heft kostet in vier Läden", ["2.4", "3.1", "2.8", "3.3"], "€",
         "Preis"),
        ("An der Bushaltestelle wartet Ali", ["5", "9", "7", "11"], "min",
         "Wartezeit"),
        ("Drei Hunde wiegen", ["12", "30", "18"], "kg", "Masse"),
        ("Über $100$ m läuft Kim", ["13.4", "14.1", "13.8", "14.3"], "s",
         "Zeit"),
        ("Ein Kino zählt an fünf Abenden", ["250", "310", "190", "330", "270"],
         "Besucher", "Besucherzahl"),
        ("Drei Apfelbäume tragen", ["6", "14", "10"], "kg", "Ernte"),
        ("Sechs Kinder bekommen im Monat", ["15", "25", "20", "30", "35", "25"],
         "€", "Taschengeld"),
    ]
    aus = []
    for text, werte, e, was in daten:
        q = [_q(w) for w in werte]
        m = sum(q) / len(q)
        assert (m * 100).is_Integer
        liste = "; ".join(f"${_w(w, e)}$" for w in werte)
        summe = sum(q)
        aus.append(A(f"{text} {liste}{(' ' + e) if e else ''}. Berechne das "
                     f"arithmetische Mittel ({was}). {{K}}",
                     f"${_w(summe, e)} : {len(q)} = {_w(m, e)}$"
                     + (f" {e}" if e else ""),
                     f"({'+'.join(werte)})/{len(werte)}",
                     antwort=f"__ {e}".rstrip()))
    # Bündel (v0.7): zu einer Liste Mittelwert, Median und Spannweite
    bd = [("Bei fünf Würfen erzielt Mia", ["2", "6", "1", "6", "5"], "",
           "Augenzahlen"),
          ("Drei Kürbisse wiegen", ["8", "26", "14"], "kg", ""),
          ("In vier Spielen erzielt Tom", ["10", "22", "14", "6"], "",
           "Punkte"),
          ("Fünf Kinder sparen im Monat", ["10", "4", "25", "8", "13"], "€",
           ""),
          ("An vier Tagen fallen", ["3", "0", "7", "2"], "mm", "Regen")]
    for i, (text, werte, e, nach) in enumerate(bd):
        q = [_q(w) for w in werte]
        m = sum(q) / len(q)
        med = _q(_median(sorted(q)))
        r = max(q) - min(q)
        assert (m * 100).is_Integer and med == _sp.Rational(
            sorted(q)[(len(q) - 1) // 2] + sorted(q)[len(q) // 2], 2)
        assert m != med
        ein = f" {e}" if e else ""
        liste = "; ".join(f"${_w(w, e)}$" for w in werte)
        aus[2 * i] = A(
            f"{text} {liste}{ein}{(' ' + nach) if nach else ''}. Bestimme "
            "a) das arithmetische Mittel, b) den Median, c) die Spannweite.",
            f"a) ${_w(sum(q), e)} : {len(q)} = {_w(m, e)}${ein} "
            f"b) $\\mathrm{{Median}} = {_w(med, e)}${ein} "
            f"c) ${_w(max(q), e)} - {_w(min(q), e)} = {_w(r, e)}${ein}",
            f"[{m}, {med}, {r}]",
            antwort=f"a) __{ein} b) __{ein} c) __{ein}")
    return aus


# T56 Quadratseite aus Fläche berechnen – 2020-OS-B1d (Kurzantwort)
def _t56():
    daten = [("Eine quadratische Fliese", "49", "cm"),
             ("Ein quadratisches Beet", "81", "m"),
             ("Ein quadratisches Kissen", "1600", "cm"),
             ("Eine quadratische Tischdecke", "0.25", "m"),
             ("Ein quadratischer Platz", "400", "m"),
             ("Ein quadratischer Aufkleber", "64", "mm"),
             ("Ein quadratischer Teppich", "1.44", "m"),
             ("Ein quadratisches Bild", "121", "cm"),
             ("Ein quadratischer Garten", "900", "m"),
             ("Eine quadratische Terrasse", "2.25", "m")]
    aus = []
    for was, A_, e in daten:
        s = _sp.sqrt(_q(A_))
        assert s.is_Rational
        aus.append(A(f"{was} hat den Flächeninhalt ${_zahl(A_)}$ {e}². Wie "
                     f"lang ist eine Seite? {{K}}",
                     f"${_zahl(s)} \\cdot {_zahl(s)} = {_zahl(A_)}$, also "
                     f"${_zahl(s)}$ {e}", f"{A_}**0.5", antwort=f"__ {e}"))
    return aus


# T57 Winkel über Scheitel- oder Nebenwinkel bestimmen – 2019-OS-B1a
def _t57():
    # \geradenkreuzung{t}{rechts oben}{links oben}{links unten}{rechts unten}:
    # rechts oben und links unten = t, die beiden anderen 180 − t
    daten = [(40, 2, 4), (55, 3, 2), (70, 4, 3), (25, 5, 3), (65, 2, 5)]
    aus = []
    for t, geg, ges in daten:
        wert = {2: t, 3: 180 - t, 4: t, 5: 180 - t}
        lab = {2: "", 3: "", 4: "", 5: ""}
        lab[geg] = f"{wert[geg]}^\\circ"
        lab[ges] = "\\varepsilon"
        a = wert[ges]
        if a == wert[geg]:
            weg = f"$\\varepsilon = {a}^\\circ$ (Scheitelwinkel)"
            pr = str(a)
        else:
            assert a + wert[geg] == 180
            weg = (f"$\\varepsilon = 180^\\circ - {wert[geg]}^\\circ = "
                   f"{a}^\\circ$ (Nebenwinkel)")
            pr = f"180-{wert[geg]}"
        aus.append(A("Zwei Geraden schneiden sich. Wie groß ist "
                     "$\\varepsilon$? {K}", weg, pr,
                     antwort="$\\varepsilon =$ __°",
                     grafik="\\geradenkreuzung{%d}{%s}{%s}{%s}{%s}" % (
                         t, lab[2], lab[3], lab[4], lab[5])))
    return aus


# T58 Zufallsgerät zu Wahrscheinlichkeit entwerfen – 2019-OS-B1g
def _t58():
    daten = [
        ("Ein Glücksrad hat $8$ gleich große Felder. Die Wahrscheinlichkeit "
         "für Blau soll $25\\,\\%$ sein. Wie viele Felder müssen blau sein?",
         "8*25/100", 2, "$25\\,\\% = \\frac{1}{4}$; $\\frac{1}{4} \\cdot 8 = 2$",
         "Felder"),
        ("In einer Urne liegen $6$ rote Kugeln. Wie viele weiße Kugeln muss "
         "man dazulegen, damit $P(\\text{rot}) = \\frac{3}{4}$ ist?",
         "6*4/3-6", 2, "$6$ rote sind $\\frac{3}{4}$ von $8$ Kugeln, also "
         "$8 - 6 = 2$ weiße", "Kugeln"),
        ("Ein Stapel hat $12$ Karten. Die Wahrscheinlichkeit, einen Joker zu "
         "ziehen, soll $\\frac{1}{4}$ sein. Wie viele Joker braucht man?",
         "12/4", 3, "$12 : 4 = 3$", "Joker"),
        ("In einer Tüte sind $5$ grüne Bonbons und noch andere. Die "
         "Wahrscheinlichkeit für Grün soll $\\frac{1}{3}$ sein. Wie viele "
         "andere Bonbons müssen in der Tüte sein?", "5*3-5", 10,
         "$5$ grüne sind $\\frac{1}{3}$ von $15$, also $15 - 5 = 10$ andere",
         "Bonbons"),
        ("Ein Glücksrad hat $10$ gleich große Felder. Die Wahrscheinlichkeit "
         "für einen Gewinn soll $60\\,\\%$ sein. Wie viele Gewinnfelder "
         "braucht man?", "10*60/100", 6, "$10 \\cdot 0{,}6 = 6$",
         "Felder"),
    ]
    aus = []
    for text, p, soll, weg, e in daten:
        _gleich(_sp.sympify(p), soll)
        aus.append(A(f"{text} {{K}}", weg, p, antwort=f"__ {e}"))
    return aus


# T59 Spannweite berechnen – 2019-OS-B1i (Kurzantwort)
def _t59():
    daten = [("Eine Tafel Schokolade kostet in vier Läden",
              ["1.29", "0.99", "1.59", "1.19"], "€"),
             ("Fünf Kinder sind so groß", ["158", "171", "164", "149", "166"],
              "cm"),
             ("Vier Läufer brauchen über $100$ m", ["12.8", "13.4", "12.5",
                                                    "13.1"], "s"),
             ("Fünf Spieler erzielen", ["34", "47", "29", "41", "38"],
              "Punkte"),
             ("Vier Koffer wiegen", ["18.5", "21", "19.5", "23"], "kg")]
    aus = []
    for text, werte, e in daten:
        q = [_q(w) for w in werte]
        sp = max(q) - min(q)
        liste = "; ".join(f"${dez(float(w))}$" for w in werte)
        rt = (eur(float(sp), 2) + "$" if e == "€"
              else f"{_zahl(sp)}$ {e}")
        aus.append(A(f"{text}: {liste} {e}. Gib die Spannweite an. {{K}}",
                     f"größter minus kleinster Wert: ${dez(float(max(q)))} - "
                     f"{dez(float(min(q)))} = " + rt,
                     f"{max(werte, key=float)}-{min(werte, key=float)}",
                     antwort=f"__ {e}"))
    return aus


# T60 Strecke aus Teilstrecken berechnen – 2018-OS-B1b (Kurzantwort)
def _t60():
    daten = [
        ("Ein Brett ist $3$ m lang. Davon werden $4$ Stücke von je $45$ cm "
         "abgesägt. Wie lang ist der Rest?", "300-4*45", 120, "cm",
         "$3$ m $= 300$ cm; $300 - 4 \\cdot 45 = 300 - 180 = 120$ cm"),
        ("Eine Schnur ist $2{,}5$ m lang. Davon werden $6$ Stücke von je "
         "$25$ cm abgeschnitten. Wie lang ist der Rest?", "250-6*25", 100,
         "cm", "$2{,}5$ m $= 250$ cm; $250 - 6 \\cdot 25 = 250 - 150 = 100$ cm"),
        ("Ein Wanderweg ist $12$ km lang. Drei Abschnitte von je $2{,}5$ km "
         "sind geschafft. Wie weit ist es noch?", "12-3*2.5", "4.5", "km",
         "$12 - 3 \\cdot 2{,}5 = 12 - 7{,}5 = 4{,}5$ km"),
        ("Ein Rohr ist $4$ m lang. Davon werden $3$ Teile von je $80$ cm "
         "abgeschnitten. Wie lang ist der Rest?", "400-3*80", 160, "cm",
         "$4$ m $= 400$ cm; $400 - 3 \\cdot 80 = 400 - 240 = 160$ cm"),
        ("Von einer Stoffrolle mit $10$ m werden $7$ Stücke von je $1{,}2$ m "
         "verkauft. Wie viel Stoff bleibt?", "10-7*1.2", "1.6", "m",
         "$10 - 7 \\cdot 1{,}2 = 10 - 8{,}4 = 1{,}6$ m"),
    ]
    aus = []
    for text, p, soll, e, weg in daten:
        _gleich(_sp.nsimplify(p, rational=True), soll)
        aus.append(A(f"{text} {{K}}", weg, p, antwort=f"__ {e}"))
    return aus


# T61 Körper aus Netz oder Schrägbild benennen – 2018-OS-B1i (Ankreuzen)
def _t61():
    daten = [("Netz", "\\netzquader{2}{1}{1.5}{}{}{}",
              ["Würfel", "Quader", "Prisma mit dreieckiger Grundfläche"], 1),
             ("Netz", "\\netzzylinder{0.7}{2.4}{}{}",
              ["Kegel", "Zylinder", "Prisma"], 1),
             ("Netz", "\\netzpyramide{2}{1.8}{}{}",
              ["Prisma", "Quader", "Pyramide"], 2),
             ("Schrägbild", "\\kegel{1.2}{2.5}{}{}{}",
              ["Pyramide", "Kegel", "Zylinder"], 1),
             ("Netz", "\\netzwuerfel{1.2}{}",
              ["Würfel", "Pyramide", "Zylinder"], 0)]
    return [X(f"Zu welchem Körper gehört das {art}? Kreuze an. {{K}}", o, o[i],
              grafik=g) for art, g, o, i in daten]


# T62 Ergebnismenge aufzählen – 2017-OS-B1f (Kurzantwort)
def _t62():
    daten = [
        ("Man wirft eine Münze (Zahl oder Wappen) und einen Spielwürfel. Wie "
         "viele verschiedene Ergebnisse gibt es?", 2, 6,
         "$2 \\cdot 6 = 12$ (Z1 bis Z6 und W1 bis W6)"),
        ("Ein Glücksrad mit den Farben Rot, Gelb und Blau wird zweimal "
         "gedreht. Wie viele verschiedene Ergebnisse gibt es?", 3, 3,
         "$3 \\cdot 3 = 9$ (RR, RG, RB, GR, GG, GB, BR, BG, BB)"),
        ("Jonas hat $3$ T-Shirts und $2$ Hosen. Wie viele verschiedene "
         "Kombinationen aus T-Shirt und Hose kann er anziehen?", 3, 2,
         "$3 \\cdot 2 = 6$"),
        ("Eine Münze wird dreimal geworfen. Wie viele verschiedene "
         "Ergebnisse gibt es?", 4, 2,
         "$2 \\cdot 2 \\cdot 2 = 8$ (ZZZ, ZZW, ZWZ, ZWW, WZZ, WZW, WWZ, WWW)"),
        ("Ein Zahlenschloss hat zwei Räder mit den Ziffern $0$ bis $4$. Wie "
         "viele verschiedene Zahlencodes gibt es?", 5, 5, "$5 \\cdot 5 = 25$"),
    ]
    aus = []
    for text, a, b, weg in daten:
        r = 8 if a == 4 else a * b
        aus.append(A(f"{text} {{K}}", weg, "2*2*2" if a == 4 else f"{a}*{b}",
                     antwort="__ Ergebnisse"))
        assert str(r) in weg
    return aus


def _sp_term(d, e):
    kl = "x" if d == 0 else f"(x {'-' if d > 0 else '+'} {abs(d)})^2"
    if d == 0:
        kl = "x^2"
    return kl + ("" if e == 0 else f" {'+' if e > 0 else '-'} {abs(e)}")


# T63 Scheitelpunktform aufstellen – 2016-OS-B1g (Ankreuzen)
def _t63():
    daten = [(2, -5), (-4, 3), (4, 2), (-1, -6), (5, -2)]
    x = _sp.Symbol("x")
    aus = []
    for k, (d, e) in enumerate(daten):
        opt = [f"$y = {_sp_term(d, e)}$", f"$y = {_sp_term(-d, e)}$",
               f"$y = {_sp_term(d, -e)}$", f"$y = {_sp_term(e, d)}$"]
        f = (x - d) ** 2 + e
        assert f.subs(x, d) == e and _sp.solve(_sp.diff(f, x), x) == [d]
        o, j = _rot(opt, 0, k + 1)
        aus.append(X(f"Eine verschobene Normalparabel hat den Scheitelpunkt "
                     f"$S({d}|{e})$. Welche Gleichung gehört zu ihr? "
                     "Kreuze an. {K}", o, o[j]))
    return aus


# T64 Parabel verschieben – 2015-OS-B1i (Kurzantwort)
def _t64():
    daten = [  # (Text, Start-Scheitel, Verschiebung (dx, dy), Graph?)
        ("Die Normalparabel wird um $3$ Einheiten nach links verschoben.",
         (0, 0), (-3, 0), True),
        ("Die Normalparabel wird um $4$ Einheiten nach oben verschoben.",
         (0, 0), (0, 4), True),
        ("Die Normalparabel wird um $1$ Einheit nach rechts und um $2$ "
         "Einheiten nach unten verschoben.", (0, 0), (1, -2), True),
        ("Die Parabel im Bild wird um $2$ Einheiten nach links verschoben.",
         (1, 3), (-2, 0), True),
        ("Die Parabel mit $y = x^2 + 2$ wird um $3$ Einheiten nach rechts "
         "verschoben.", (0, 2), (3, 0), False),
    ]
    x = _sp.Symbol("x")
    aus = []
    for text, (d, e), (dx, dy), graph in daten:
        nd, ne = d + dx, e + dy
        f = (x - dx - d) ** 2 + e + dy  # verschobener Graph
        assert f.subs(x, nd) == ne
        aus.append(A(f"{text} Gib den Scheitelpunkt der neuen Parabel an. {{K}}",
                     f"$S({d}|{e})$ wandert nach $S({nd}|{ne})$",
                     f"[{nd}, {ne}]", antwort="S( __ | __ )",
                     grafik=_ks(f"\\parabel{{1}}{{{d}}}{{{e}}}{{}}")
                     if graph else ""))
    return aus


AUFGABEN["Bruchteil einer Fläche bestimmen"] += _t1b()
AUFGABEN["Lineare Gleichung lösen"] += _t6b()
AUFGABEN["Term zu Figur angeben"] = _t42()
AUFGABEN["Pythagoras Gleichung zuordnen"] = _t43()
AUFGABEN["Zeiteinheiten umrechnen"] = _t44()
AUFGABEN["Eigenschaft einer Figur zuordnen"] = _t45()
AUFGABEN["Größen vergleichen"] = _t46()
AUFGABEN["Umfang Rechteck berechnen"] = _t47()
AUFGABEN["Median bestimmen"] = _t48()
AUFGABEN["Proportionale Zuordnung Dreisatz"] = _t49()
AUFGABEN["Rechteckseite aus Fläche berechnen"] = _t50()
AUFGABEN["Fehlenden Wert aus Mittelwert bestimmen"] = _t51()
AUFGABEN["Satz des Pythagoras formulieren"] = _t52()
AUFGABEN["Portionen aus Gesamtmenge berechnen"] = _t53()
AUFGABEN["Scheitelpunkt ablesen"] = _t54()
AUFGABEN["Arithmetisches Mittel berechnen"] = _t55()
AUFGABEN["Quadratseite aus Fläche berechnen"] = _t56()
AUFGABEN["Winkel über Scheitel- oder Nebenwinkel bestimmen"] = _t57()
AUFGABEN["Zufallsgerät zu Wahrscheinlichkeit entwerfen"] = _t58()
AUFGABEN["Spannweite berechnen"] = _t59()
AUFGABEN["Strecke aus Teilstrecken berechnen"] = _t60()
AUFGABEN["Körper aus Netz oder Schrägbild benennen"] = _t61()
AUFGABEN["Ergebnismenge aufzählen"] = _t62()
AUFGABEN["Scheitelpunktform aufstellen"] = _t63()
AUFGABEN["Parabel verschieben"] = _t64()


# --- Schreiben ---------------------------------------------------------------

def main(argv):
    nur = argv[argv.index("--nur") + 1] if "--nur" in argv else None
    with open(ORDNER / "typen.csv", encoding="utf-8", newline="") as h:
        typen = list(csv.DictReader(h, delimiter=";"))
    je = {}
    for t in typen:
        je.setdefault(t["eintrag"], []).append(t)
    fehlt = [t["typ"] for t in typen if t["typ"] not in AUFGABEN]
    if fehlt:
        raise SystemExit("keine Aufgaben für: " + ", ".join(fehlt))
    for eintrag, reihe in sorted(je.items()):
        if nur and eintrag != nur:
            continue
        reihe.sort(key=lambda t: int(t["kette_nr"]))
        zeilen = []
        for t in reihe:
            auf = AUFGABEN[t["typ"]]
            assert len(auf) == ZIEL.get(t["typ"], 10), (t["typ"], len(auf))
            for v, a in enumerate(auf, 1):
                z = {"id": f"{eintrag}-basis-k{t['kette_nr']}-v{v}",
                     "eintrag": eintrag, "einheit": int(t["einheit"]),
                     "kette": t["typ"], "kette_nr": int(t["kette_nr"]),
                     "sprosse": 1, "sprosse_text": t["typ"],
                     "merkmal": MERKMAL, "hoehe": "basis", "variante": v,
                     "aufgabe": a["aufgabe"].replace(" {K}", "")
                                            .replace("{K}", "").strip(),
                     "form": a["form"], "antwort": a["antwort"],
                     "loesung": a["loesung"], "pruef": a["pruef"],
                     "original": {"id": t["original"], "jahr": int(t["jahr"]),
                                  "papier": t["papier"]},
                     "grafik": a["grafik"], "loesungsgrafik": "",
                     "quelle": int(t["quelle"])}
                zeilen.append(json.dumps(z, ensure_ascii=False))
        (ORDNER / f"{eintrag}.jsonl").write_text("\n".join(zeilen) + "\n",
                                                encoding="utf-8")
        print(f"{eintrag}.jsonl: {len(zeilen)} Zeilen")


if __name__ == "__main__":
    main(sys.argv)
