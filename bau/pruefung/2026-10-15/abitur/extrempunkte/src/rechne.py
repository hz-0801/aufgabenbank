# AA50 Extrempunkte – andere Zahlen nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x, t, u = symbols('x t u', real=True)
def p(*a): print(*a)
def ext(f, v=x):
    fp, fpp = diff(f, v), diff(f, v, 2)
    return [(s, simplify(f.subs(v, s)), N(f.subs(v, s), 4), 'H' if fpp.subs(v, s) < 0 else 'T' if fpp.subs(v, s) > 0 else '?')
            for s in solve(fp, v)]
# B1 2022-B2.1j Tauchroboter h = 1/8 t (t-36)^2, 0<=t<=36 (Original 9/40 t (t-30)^2, Max 900 m bei 10)
h = t*(t - 36)**2/8; p('B1', expand(h), 'WP', solve(diff(h, t, 2), t), 'h18', h.subs(t, 18), 'Weg', 2*h.subs(t, 12) - h.subs(t, 18), diff(h, t), diff(h, t).subs(t, 12), diff(h, t, 2).subs(t, 12), h.subs(t, 12))
# B2 2023-B2.1c f = 1/3(x²-9)e^(x/2), Stelle -2+√13 (eine Zahlenwahl je Aufgabe wie B2.1g–m)
f = Rational(1, 3)*(x**2 - 9)*exp(x/2); fp = diff(f, x); s = -2 + sqrt(13)
p('B2', simplify(fp - (x**2/6 + 2*x/3 - Rational(3, 2))*exp(x/2)) == 0, simplify(fp.subs(x, s)), simplify(f.subs(x, s)), N(f.subs(x, s), 4), N(s, 4))
# B3 2022-B2.1a (Nebenplatz) f = (x+3)e^-x, f' = -(x+2)e^-x
f = (x + 3)*exp(-x); fp = diff(f, x); p('B3', simplify(fp + (x + 2)*exp(-x)) == 0, solve(fp, x), f.subs(x, -2), N(exp(2), 4), fp.subs(x, -3) > 0, fp.subs(x, -1) < 0)
# B4 2023-A1.3a
f = x**3 + 3*x**2; p('B4', solve(diff(f, x), x))
# B5 2022-B2.2b
f = -x**3/3 + x**2; p('B5', ext(f))
# B6 2023-B2.2b
f = x**3 - 9*x**2 + 24*x - 16; p('B6', ext(f), factor(f))
# B7 2024-B2.2c
f = Rational(1, 2)*x**4 - 3*x**2 + Rational(5, 2); p('B7', ext(f))
# B8 2025-B2.1b
f = x**3/18 - Rational(3, 2)*x; p('B8', ext(f), 'Gerade durch beide: y = -x')
# B9 2025-B2.2b
f = (3 - x)*exp(x); p('B9', factor(diff(f, x)), ext(f))
# B10 2024-B2.1b
f = (x - 3)*exp(-x/3 + 2); fp = diff(f, x); p('B10', simplify(fp - (2 - x/3)*exp(-x/3 + 2)) == 0, solve(fp, x), f.subs(x, 6), fp.subs(x, 5) > 0, fp.subs(x, 7) < 0)
# Mehr
g = Rational(1, 1000)*(Rational(1, 1600)*x**4 - 8*x**2 + 25600)
p('M1', factor(diff(g, x)), ext(g))
f = (x + 1)*exp(-x/3); p('M2', factor(diff(f, x)), ext(f))
h = 6*t*exp(-t/20) + 40; p('M3', factor(diff(h, t)), ext(h, t))
f = -Rational(2, 100)*(x - 6)*(x + 2)**2; p('M4', ext(f))
f = x**3 - 6*x**2 + 32; p('M5', diff(f, x).subs(x, 4), diff(f, x, 2).subs(x, 4), f.subs(x, 4))
f = x**3/8 - x**2 + 2*x; p('M6', diff(f, x).subs(x, Rational(4, 3)), diff(f, x, 2).subs(x, Rational(4, 3)), f.subs(x, Rational(4, 3)), ext(f))
f = (-x**2/5 + 3*x)*exp(-x/5); fp = diff(f, x); p('M7', factor(fp), ext(f))
f = x**3 - 12*x; p('M8', diff(f, x).subs(x, -2), diff(f, x, 2).subs(x, -2), f.subs(x, -2))
f = x**3 - 27*x + 54; p('M9', solve(diff(f, x), x), [diff(f, x, 2).subs(x, s) for s in (-3, 3)], factor(f))
