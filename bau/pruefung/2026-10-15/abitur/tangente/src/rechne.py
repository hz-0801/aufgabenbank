# AA40 Tangente – andere Zahlen, nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/ableitung-tangente.csv
from sympy import *
x, t = symbols('x t', real=True)
def tang(f, x0):
    m = diff(f, x).subs(x, x0); y0 = f.subs(x, x0); return m, y0, expand(m*(x-x0)+y0)
f = x**3-10*x**2+21*x; assert tang(f, 1) == (4, 12, 4*x+8)                       # 2022-A1.1b
f = x**3/3-x**2+2; assert tang(f, 3) == (3, 2, 3*x-7)                            # 2025-A1.1a
assert set(solve(Eq(diff(f, x), 3), x)) == {-1, 3} and f.subs(x, -1) == Rational(2, 3)   # 2025-A1.1b
print('2025-A1.1 HP/TP', f.subs(x, 0), f.subs(x, 2), 'f(-2)', f.subs(x, -2))
f = 2*exp(x)+3; assert tang(f, 0) == (2, 5, 2*x+5)                               # 2026-B2.2b
f = Rational(1, 48)*(3*x**4+16*x**3+96); assert expand(diff(f, x)-(x**3/4+x**2)) == 0
assert tang(f, -2) == (2, Rational(1, 3), 2*x+Rational(13, 3))                   # 2026-B2.1d
f = x**3-6*x**2; assert tang(f, -1) == (15, -7, 15*x+8)                          # 2023-A1.3b
f = x**3-9*x**2+24*x-16; m, y0, tt = tang(f, 0); assert tt == 24*x-16 and factor(f-tt) == x**2*(x-9) and f.subs(x, 9) == 200  # 2023-B2.2d
# Mehr
h = 6*t*exp(-t/20)+40; hp = diff(h, t); m = hp.subs(t, 60); n = h.subs(t, 60)-60*m
print('2019-B2.2f m', N(m, 4), 'n', N(n, 5), 'g<=40 ab', simplify((40-n)/m))
assert simplify((40-n)/m) == 90
f = -Rational(2, 100)*(x - 6)*(x + 2)**2; fp = diff(f, x)
assert expand(f - (-x**3/50 + x**2/25 + 2*x/5 + Rational(12, 25))) == 0
assert solve(diff(fp, x), x) == [Rational(2, 3)] and fp.subs(x, Rational(2, 3)) == Rational(32, 75)
print('2020-B2.2h', solve(Eq(fp, -Rational(32, 75)), x), [N(s, 3) for s in solve(Eq(fp, -Rational(32, 75)), x)])
f = 4*exp(-x/2); assert tang(f, 0)[2] == -2*x+4                                  # IQB 2017 A11a
r = -(x**2-2*x-1); s = exp(2*x); assert r.subs(x, 0) == s.subs(x, 0) == 1 and diff(r, x).subs(x, 0) == diff(s, x).subs(x, 0) == 2  # IQB 2023
print('ok')
