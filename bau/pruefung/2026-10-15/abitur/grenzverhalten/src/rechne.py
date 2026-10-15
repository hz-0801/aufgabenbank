# AA10 Grenzverhalten und Symmetrie – andere Zahlen nachgerechnet (sympy), Zeilen in
# mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x, t = symbols('x t', real=True)
def p(*a): print(*a)
L = lambda f, s: (limit(f, x, s))
# B1 2022-B2.2a
f = -x**3/18 + x**2/3; p('B1', L(f, oo), L(f, -oo))
# B2 2026-B2.1a  (f = 2/3 x^4 + 4/3 x^3 + 2; Wendestellen -1, 0; f'(-1) = 4/3)
f = Rational(2, 3)*x**4 + Rational(4, 3)*x**3 + 2; fp = diff(f, x)
p('B2', fp, L(fp, -oo), L(fp, oo), solve(diff(f, x, 2), x), fp.subs(x, -1))
# B3 2022-B2.1b
f = (x + 3)*exp(-x); p('B3', L(f, oo), simplify(diff(f, x) + (x + 2)*exp(-x)) == 0)
# B4 2023-B2.1a  f = 1/3(x²-9)e^(x/2)
f = Rational(1, 3)*(x**2 - 9)*exp(x/2); p('B4', L(f, oo), L(f, -oo))
# B5 2025-B2.2a
f = (3 - x)*exp(x); p('B5', solve(f, x), L(f, -oo), L(f, oo), 'HP', solve(diff(f, x), x), f.subs(x, 2), N(f.subs(x, 2), 3))
# B6 2024-A1.1a
f = x**3 - 9*x; p('B6', simplify(f.subs(x, -x) + f) == 0)
# B7 2024-B2.2a
f = Rational(1, 2)*x**4 - 3*x**2 + Rational(5, 2); p('B7', simplify(f.subs(x, -x) - f) == 0)
# B8 2025-B2.1a  (Extrempunkte (-3|3), (3|-3) auf y = -x wie im Original)
f = x**3/18 - Rational(3, 2)*x; p('B8', simplify(f.subs(x, -x) + f) == 0, solve(f, x), N(3*sqrt(3), 3),
  [(s, f.subs(x, s)) for s in solve(diff(f, x), x)])
# Mehr
p('M1', L((x + 1)*exp(-x/3), oo), (x + 1)*exp(-x/3) > 0)
f = (8*x - 2)*exp(-x); p('M2', L(f, oo), L(f, -oo))
f = (-x**2/5 + 3*x)*exp(-x/5); p('M3', L(f, oo), L(f, -oo))
h = 6*t*exp(-t/20) + 40; p('M4', limit(h, t, oo), h.subs(t, 0))
f = -Rational(2, 100)*(x - 6)*(x + 2)**2; p('M5', expand(f), L(f, oo), L(f, -oo))
f = Rational(1, 4)*(x**3 + 3*x**2 - 4*x - 12); p('M6', factor(f), L(f, -oo))
f = Rational(1, 8)*x*(4 - x)*exp(x); p('M7', L(f, -oo), f.subs(x, -1) < 0)
f = x**3/50 - x/2; p('M8', simplify(f.subs(x, -x) + f) == 0, solve(f, x), diff(f, x, 2).subs(x, 0))
