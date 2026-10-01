#!/usr/bin/env python3
"""Rechenprobe für muster.tex: jede Lösung wird mit sympy nachgerechnet.

- \\rk{Term}{Lösung}: Term und Lösung müssen gleichwertig sein (bei
  „A = B“ in der Lösung jeder Teil).
- \\rw{Term}{Einsetzung}{Lösung}: Wert des Terms nach Einsetzen.
- % pruef: <Python-Ausdruck mit ==>: Rechenprobe für Textaufgaben.
Aufruf: python3 pruef.py [muster.tex]; Ausgabe je Fehler eine Zeile,
am Ende die Zahl der Proben. Rückgabewert 1 bei einem Fehler.
"""
import re
import sys

from sympy import Rational, Symbol, nsimplify, simplify, symbols  # noqa: F401
from sympy.parsing.sympy_parser import (implicit_multiplication_application,
                                        parse_expr, standard_transformations)

TRANS = standard_transformations + (implicit_multiplication_application,)
NAMEN = {c: Symbol(c) for c in "abcdsxyz"}
NAMEN["Rational"] = Rational


def argumente(text, pos, anzahl):
    """Liest ab pos optional [..] und dann anzahl {..}-Argumente."""
    args = []
    while text[pos] == " ":
        pos += 1
    if text[pos] == "[":
        pos = text.index("]", pos) + 1
    for _ in range(anzahl):
        while text[pos] in " \n":
            pos += 1
        assert text[pos] == "{", text[pos:pos + 40]
        tiefe, start = 0, pos
        while True:
            c = text[pos]
            if c == "\\":
                pos += 2
                continue
            if c == "{":
                tiefe += 1
            elif c == "}":
                tiefe -= 1
                if tiefe == 0:
                    break
            pos += 1
        args.append(text[start + 1:pos])
        pos += 1
    return args, pos


def frac(s):
    while "\\frac" in s:
        i = s.index("\\frac")
        (z, n), ende = argumente(s, i + 5, 2)
        s = s[:i] + "((" + z + ")/(" + n + "))" + s[ende:]
    return s


def sympy_term(tex):
    s = tex.replace("{,}", ".").replace("\\cdot", "*").replace(":", "/")
    for alt in ("\\,", "\\;", "\\ ", "\\left", "\\right"):
        s = s.replace(alt, "")
    s = s.replace("\\{", "(").replace("\\}", ")").replace("[", "(").replace("]", ")")
    s = frac(s)
    s = s.replace("^", "**").replace("{", "(").replace("}", ")")
    return nsimplify(parse_expr(s, local_dict=dict(NAMEN), transformations=TRANS), rational=True)


def main():
    pfad = sys.argv[1] if len(sys.argv) > 1 else "muster.tex"
    text = open(pfad, encoding="utf-8").read()
    # nur der Dokumentteil
    text = text[text.index("\\begin{document}"):]
    fehler = proben = 0
    for m in re.finditer(r"\\rk(?=[\[{ ])", text):
        (term, lsg), _ = argumente(text, m.end(), 2)
        t = sympy_term(term)
        for teil in lsg.split("="):
            proben += 1
            if simplify(t - sympy_term(teil)) != 0:
                fehler += 1
                print(f"FEHLER rk: {term} = {lsg} (Teil {teil!r})")
    for m in re.finditer(r"\\rw(?=[\[{ ])", text):
        (term, einsetz, lsg), _ = argumente(text, m.end(), 3)
        werte = {}
        for teil in einsetz.replace("\\ ", "").split(","):
            if "=" not in teil:
                continue
            v, w = teil.split("=")
            werte[Symbol(v.strip())] = sympy_term(w)
        proben += 1
        if simplify(sympy_term(term).subs(werte) - sympy_term(lsg)) != 0:
            fehler += 1
            print(f"FEHLER rw: {term} für {einsetz} = {lsg}")
    for m in re.finditer(r"^% pruef: (.*)$", text, re.M):
        ausdruck = m.group(1)
        links, rechts = ausdruck.split("==")
        proben += 1
        ln = parse_expr(links, local_dict=dict(NAMEN), transformations=standard_transformations)
        rn = parse_expr(rechts, local_dict=dict(NAMEN), transformations=standard_transformations)
        if simplify(nsimplify(ln) - nsimplify(rn)) != 0:
            fehler += 1
            print(f"FEHLER pruef: {ausdruck}")
    print(f"{proben} Proben, {fehler} Fehler")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
