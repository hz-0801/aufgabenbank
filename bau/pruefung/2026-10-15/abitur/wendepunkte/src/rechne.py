# AA70 Wendepunkte – andere Zahlen nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x, t = symbols('x t', real=True)
def p(*a): print(*a)
def wp(f, v=x):
    return [(s, simplify(f.subs(v, s)), N(f.subs(v, s), 4), diff(f, v, 3).subs(v, s)) for s in solve(diff(f, v, 2), v)]
# B1/B2 2022-A1.2a/b: Graph (hilfsmittelfrei, nur Abbildung) – f' Nullstellen 0,3 1,5 1,9 und Fast-Sattel bei 0,9
fp = (x - Rational(3, 10))*(x - Rational(3, 2))*(x - Rational(19, 10))*((x - Rational(9, 10))**2 + Rational(1, 50))
F = integrate(fp, x); k = Rational(35, 100)/(F.subs(x, Rational(3, 2)) - F.subs(x, Rational(3, 10)))
f = expand(k*(F - F.subs(x, Rational(3, 10))) - Rational(1, 10))
co = [round(float(c), 4) for c in Poly(f, x).all_coeffs()]
p('B1 Koeffizienten (pgf):', co)
g = sum(c*x**(len(co) - 1 - i) for i, c in enumerate(co))
p('B1 Extremstellen', [round(float(r), 3) for r in Poly(diff(g, x), x).nroots() if abs(im(r)) < 1e-9])
ws = [round(float(r), 3) for r in Poly(diff(g, x, 2), x).nroots() if abs(im(r)) < 1e-9]
p('B1 Wendestellen', ws, 'Werte', [round(float(g.subs(x, s)), 3) for s in ws], "f' dort", [round(float(diff(g, x).subs(x, s)), 3) for s in ws])
p('B1 f(0,3)', round(float(g.subs(x, 0.3)), 3), "f'(0,3)", round(float(diff(g, x).subs(x, 0.3)), 4))
# B3 2022-B2.1l Tauchroboter h = 1/8 t (t-36)^2
h = t*(t - 36)**2/8; p('B3', wp(h, t), diff(h, t).subs(t, 24))
# B4 2023-B2.2c
f = x**3 - 9*x**2 + 24*x - 16; p('B4', wp(f))
# B5 2026-B2.1c  f = 2/3 x^4 + 4/3 x^3 + 2
f = Rational(2, 3)*x**4 + Rational(4, 3)*x**3 + 2; p('B5', factor(diff(f, x, 2)), wp(f))
# B6 2024-B2.1c  f = (x-3)e^(-x/3+2)
f = (x - 3)*exp(-x/3 + 2); f2 = diff(f, x, 2)
p('B6', simplify(f2 - (x/9 - 1)*exp(-x/3 + 2)) == 0, solve(f2, x), f.subs(x, 9), N(f.subs(x, 9), 4), f2.subs(x, 8) < 0, f2.subs(x, 10) > 0)
# B7 2023-B2.1f  f = 0,5(x²-9)e^x
f = Rational(1, 2)*(x**2 - 9)*exp(x); f2 = diff(f, x, 2)
p('B7', simplify(f2 - (x**2/2 + 2*x - Rational(7, 2))*exp(x)) == 0, [(s, N(s, 4), N(f.subs(x, s), 4)) for s in solve(f2, x)])
# Mehr
f = x**3/8 - x**2 + 2*x; p('M1', wp(f))
f = (-x**2/5 + 3*x)*exp(-x/5); f2 = factor(diff(f, x, 2)); p('M2', f2, [(N(s, 4), N(f.subs(x, s), 4)) for s in solve(f2, x)])
f = -Rational(2, 100)*(x - 6)*(x + 2)**2; p('M3', solve(diff(f, x, 2), x), diff(f, x).subs(x, Rational(2, 3)))
f = -x**3/540 + x**2/18 + 1; s = solve(diff(f, x, 2), x)[0]; m = diff(f, x).subs(x, s)
p('M4', s, f.subs(x, s), N(f.subs(x, s), 3), m, N(atan(m)*180/pi, 4))
g = -x*(x - 6)*(x - 12)/36 + 12; p('M5', wp(g), N(g.subs(x, 6 - 2*sqrt(3)), 3), N(g.subs(x, 6 + 2*sqrt(3)), 3), diff(g, x).subs(x, 6))
f = (x**3 - 12*x**2 + 32*x)/8; p('M6', wp(f), diff(f, x).subs(x, 4), factor(f))
