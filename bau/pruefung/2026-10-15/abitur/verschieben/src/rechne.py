# AA120 Verschieben, spiegeln, strecken – andere Zahlen nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x, t, k = symbols('x t k', real=True)
def p(*a): print(*a)
# B1 2023-B2.1i  f = 1/3(x²-9)e^(x/2), Spitzen (±3|0), (0|±3)
f = Rational(1, 3)*(x**2 - 9)*exp(x/2); p('B1', solve(f, x), f.subs(x, 0), N(f.subs(x, -1.5), 3), 'Sehne', -Rational(3, 2))
g = f.subs(x, -x); h = -f; kk = -f.subs(x, -x); p('B1 g(3)', g.subs(x, 3), 'h(-1)>0', N(h.subs(x, -1), 3), 'k(1)>0', N(kk.subs(x, 1), 3))
# B2 2024-B2.1g  f = (x-3)e^(-x/3+2), Knauf 3 <= x <= 12
f = (x - 3)*exp(-x/3 + 2); p('B2', -f, f.subs(x, 12), N(f.subs(x, 12), 4), 'Durchm. LE', N(2*f.subs(x, 12), 4), 'mm', N(2*f.subs(x, 12)*5, 3), 'HP', f.subs(x, 6))
# B3 2024-A1.7b  f = e^(x/4) - e, Nullstelle 4
f = exp(x/4) - E; h = f.subs(x, x + 4); p('B3', solve(f, x), expand(h), h.subs(x, 0))
# B4 2025-B2.1c  f = x³/18 - 3/2 x, g: y = x/2
f = x**3/18 - Rational(3, 2)*x; p('B4', solve(Eq(f, x/2), x), 'A(6|3), r²', 36 + 9, 'gedreht (x|y)->(-y|x): A*(-3|6)', '-2 * (-3) =', -2*(-3))
# B5 2026-B2.1e  t = 4/3 x + 8/3 (Tangente in (-1|4/3) an f = 2/3 x^4 + 4/3 x^3 + 2), Abstand 4
f = Rational(2, 3)*x**4 + Rational(4, 3)*x**3 + 2; m = diff(f, x).subs(x, -1); n = f.subs(x, -1) - m*(-1); p('B5', m, n, 'z = 4 * 5/3 =', Rational(4)*Rational(5, 3), N(Rational(20, 3), 3))
z = symbols('z'); p('B5 Abstand Gerade y = 4/3x + n - z:', solve(Eq(z*Rational(3, 5), 4), z))
# B6 2026-B2.2f  f = 2e^x + 3, k = 15 f(-x/300) = 30e^(-x/300) + 45
f = 2*exp(x) + 3; p('B6', expand(15*f.subs(x, -x/300)))
# B7 2023-B2.2j  f = x³ - 9x² + 24x - 16, h = 4x³ - 36x² + 96x + 20 = c (f + d)
f = x**3 - 9*x**2 + 24*x - 16; c, d = symbols('c d'); hh = 4*x**3 - 36*x**2 + 96*x + 20
p('B7', solve(Poly(c*(f + d) - hh, x).all_coeffs(), [c, d]))
# B8 2024-A1.4b  g = 3e^x - 3, h = e^x + 2
g = 3*exp(x) - 3; h = exp(x) + 2; p('B8', diff(g, x).subs(x, 0), diff(h, x).subs(x, 0), simplify(h - g))
# B9 2026-A1.4b  f = 2 sin x, g = 3 sin(x/2)
p('B9', N(sqrt(pi**2 + 16), 4), N(sqrt(4*pi**2 + 36), 4), 'Dreieck', Rational(1, 2)*2*pi*4)
# Mehr
hk = k*t*exp(-t/20) + 40; p('M1', solve(diff(hk, t), t), hk.subs(t, 0), limit(hk, t, oo), N(hk.subs({k: 8, t: 20}), 4), N(hk.subs({k: 6, t: 20}), 4))
p('M2', simplify(2**(x + 3) / 2**x))
f = cos(x) + 2; p('M3', f.subs(x, 2*x) - 1)
p('M4', Rational(8, 10), Rational(9, 6))
