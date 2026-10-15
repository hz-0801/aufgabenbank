# AA100 Gleichungen und Ungleichungen – andere Zahlen nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x, t, k, u = symbols('x t k u', real=True)
def p(*a): print(*a)
# B1 2022-B2.1d
f = (x + 3)*exp(-x); fp = diff(f, x); p('B1', solve(Eq(f, fp), x))
# B2 2025-A1.7a  f = -x² + 6x - 4
f = -x**2 + 6*x - 4; fp = diff(f, x); p('B2', fp, solve(Eq(f/x, fp), x), solve(f, x), 'Scheitel', solve(fp, x), f.subs(x, 3))
# B3 2025-B2.2g  a(x) = 3000(1 - e^(-x²/8))
a = 2400*(1 - exp(-x**2/4)); s = nsolve(a.subs(x, x + 2) - a - 800, x, 2); p('B3', s, N(a.subs(x, s)), N(a.subs(x, s + 2)), [N(a.subs(x, v), 4) for v in (2, 4, 6)])
p('B3 eindeutig >0:', [round(float(a.subs(x, v + 2) - a.subs(x, v) - 800), 1) for v in (0, 0.5, 1, 1.5, 2, 2.5, 3, 4)], 'Wendestelle', solve(diff(a, x, 2), x))
# B4 2023-B2.2g  f - g
f = x**3 - 9*x**2 + 24*x - 16; g = x**3/4 - 3*x**2 + 12*x - 16; p('B4', factor(f - g), solve_univariate_inequality(f - g > 0, x))
# B5 2024-B2.2h  f = x⁴ - 6x² + 5, p = -5x² + 5, |p - f| <= 2 · 1/4 für x >= 1 (Kritiker 15.10.)
f = x**4 - 6*x**2 + 5; pp = -5*x**2 + 5
d = expand(f - pp); p('B5', d, solve(Eq(d, Rational(1, 2)), x), N(sqrt((1 + sqrt(3))/2), 4), solve(Eq(u**2 - u, Rational(1, 2)), u))
# Mehr
f = (-x**2/5 + 3*x)*exp(-x/5); h = -x*exp(-x/5); p('M1', solve(Eq(f, h), x), N(f.subs(x, 20), 4))
g = x**2 - 5; h = -x**2 + 2*x + 7; p('M2', solve(Eq(g, h), x))
hk = k*t*exp(-t/20) + 40; p('M3', solve(Eq(hk.subs(t, 60), 80), k), N(Rational(2, 3)*exp(3), 4))
