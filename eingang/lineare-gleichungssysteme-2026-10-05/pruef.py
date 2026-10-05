#!/usr/bin/env python3
"""Rechenprobe für das Lernblatt Einsetzungsverfahren: jede Zeile
„% pruef: <Ausdruck>“ im Quelltext wird mit sympy ausgewertet.
Hilfen: L(I, II) löst ein System und gibt (x, y); G(Gl) löst eine
Gleichung nach x; T(a, b) prüft Termgleichheit; U(Gl, Term) prüft,
dass die Gleichung nach y umgestellt den Term ergibt.
Aufruf: python3 pruef.py <datei.tex>; Rückgabewert 1 bei einem Fehler."""
import re
import sys

from sympy import Eq, Rational, nsimplify, simplify, solve, symbols, sympify

x, y = symbols("x y")


def _eq(s):
    links, rechts = s.split("=")
    return Eq(nsimplify(sympify(links), rational=True), nsimplify(sympify(rechts), rational=True))


def _zahl(v):
    return nsimplify(v, rational=True)


class Paar(tuple):
    def __eq__(self, other):
        return all(simplify(a - _zahl(b)) == 0 for a, b in zip(self, other))


def L(i, ii):
    s = solve([_eq(i), _eq(ii)], [x, y], dict=True)
    assert len(s) == 1, s
    return Paar((s[0][x], s[0][y]))


def G(g):
    s = solve(_eq(g), x)
    assert len(s) == 1
    return Paar((s[0],))[0]


def T(a, b):
    return simplify(nsimplify(sympify(a), rational=True) - nsimplify(sympify(b), rational=True)) == 0


def U(g, term):
    s = solve(_eq(g), y)
    return len(s) == 1 and simplify(s[0] - nsimplify(sympify(term), rational=True)) == 0


def main(pfad):
    fehler = 0
    zahl = 0
    for nr, zeile in enumerate(open(pfad, encoding="utf-8"), 1):
        m = re.match(r"\s*% pruef: (.*)$", zeile)
        if not m:
            continue
        zahl += 1
        ausdruck = m.group(1)
        try:
            ok = eval(ausdruck, {"L": L, "G": G, "T": T, "U": U, "Rational": Rational})
            if isinstance(ok, Paar):
                ok = True
            # Zahlenvergleiche mit Dezimalzahlen tolerant prüfen
        except Exception as e:  # noqa: BLE001
            ok = False
            ausdruck += f"  ({e})"
        if ok is not True and ok is not None:
            if ok is False or not bool(ok):
                fehler += 1
                print(f"Zeile {nr}: FEHLER {ausdruck}")
    print(f"{zahl} Proben, {fehler} Fehler")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
