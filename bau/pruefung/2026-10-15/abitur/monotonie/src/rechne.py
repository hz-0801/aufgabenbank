# AA60 Monotonie – andere Zahlen nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x = symbols('x', real=True)
def p(*a): print(*a)
# B1 2023-B2.1e  f = 1/3(x²-9)e^(x/2)
f = Rational(1, 3)*(x**2 - 9)*exp(x/2); fp = diff(f, x); p('B1', solve(fp, x), N(-2 + sqrt(13), 4), fp.subs(x, 1) < 0, fp.subs(x, 2) > 0)
# B2 2024-A1.7a  f = e^(0,25x) - e
f = exp(x/4) - E; p('B2', diff(f, x), solve(f, x))
# B3 2026-A1.7a  Graph von f' = 3(x+2)e^-(x+1): einzige Nullstelle -2, Hochpunkt (-1|3)
g = 3*(x + 2)*exp(-(x + 1)); p('B3', solve(g, x), solve(diff(g, x), x), g.subs(x, -1), N(g.subs(x, 4), 3), N(g.subs(x, -3), 3))
# B4 2022-B2.1c  f = (x+3)e^-x, f' = -(x+2)e^-x: Graph I = f', Graph II = f
f = (x + 3)*exp(-x); fp = diff(f, x); p('B4', solve(fp, x), solve(diff(fp, x), x), N(fp.subs(x, -1), 3), N(f.subs(x, -2), 3))
# B5 2023-B2.2f  g = 1/4 (x-4)^3 = 1/4 x³ - 3x² + 12x - 16, g' = 3/4 (x-4)²
g = x**3/4 - 3*x**2 + 12*x - 16; p('B5', factor(g), factor(diff(g, x)), solve(diff(g, x), x))
# B6 2023-B2.1d  Tiefpunkt bei -2+√13; Aussagen an -1,9+√13
f = Rational(1, 3)*(x**2 - 9)*exp(x/2); fp = diff(f, x); s = -2 + sqrt(13); s2 = Rational(-19, 10) + sqrt(13)
p('B6', N(f.subs(x, s), 4), N(f.subs(x, s2), 4), N(fp.subs(x, s2), 4), N(f.subs(x, -2 - sqrt(13)), 3))
# B7 2026-B2.1h  g = 8/3 x³ + 4x² auf [-1; 0] (= f' aus B2.1), A(-1|4/3), Q mit y = -g(-x_Q), g'(-x_Q) = 0
g = Rational(8, 3)*x**3 + 4*x**2; p('B7', solve(diff(g, x), x), g.subs(x, -1), -g.subs(x, -1))
# Mehr
f = (8*x - 2)*exp(-x); fp = diff(f, x); p('M1', factor(fp), solve(fp, x), fp.subs(x, 0), N(fp.subs(x, 2.25), 3))
f = x**3/2 - Rational(1, 2); p('M2', diff(f, x))
f = x**3/3 - 3*x + 2; p('M3', solve(diff(f, x), x))
