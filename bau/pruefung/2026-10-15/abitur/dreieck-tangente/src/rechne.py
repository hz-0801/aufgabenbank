# AA90 Dreieck aus Tangente und Normale – andere Zahlen, nachgerechnet (sympy)
from sympy import *
x = symbols('x', real=True)
def tang(f, x0):
    m = diff(f, x).subs(x, x0); y0 = f.subs(x, x0); return m, y0, expand(m*(x-x0)+y0)
# 2023-A1.1: t1: y = 3/4 x + 3, t2: y = -3/4 x + 3
assert solve(Rational(3, 4)*x+3, x) == [-4] and sqrt(4**2+3**2) == 5; print('2023-A1.1b Umfang', 8+5+5)
f = 2*exp(x)+3; m, y0, t = tang(f, 0); x0 = solve(t, x)[0]; hyp = sqrt(x0**2+y0**2)
print('2026-B2.2c', t, x0, hyp, 'U', -x0+y0+hyp, N(-x0+y0+hyp, 4))
f = (x+3)*exp(-x); m, y0, t = tang(f, 0); x0 = solve(t, x)[0]; hyp = sqrt(x0**2+y0**2)
print('2022-B2.1g', t, x0, simplify(hyp), 'U', N(x0+y0+hyp, 4), 'M', (x0/2, y0/2), 'Abstand', N(hyp/2, 4), N(sqrt((x0/2)**2+(y0/2)**2), 4))
f = x**4 - 6*x**2 + 5; m, y0, t = tang(f, -1); n = expand(-1/m*(x+1)+y0)
print('2024-B2.2d', t, n, 'Grundseite', t.subs(x, 0)-n.subs(x, 0), 'A', Rational(1, 2)*(t.subs(x, 0)-n.subs(x, 0))*1)
f = Rational(1, 3)*(x**2-9)*exp(x/2); fp = diff(f, x); fpp = diff(fp, x)
assert simplify(fp-(x**2/6+2*x/3-Rational(3, 2))*exp(x/2)) == 0
w = [s for s in solve(simplify(fpp*exp(-x/2)), x) if N(s) > -3][0]; yw = f.subs(x, w); mw = fp.subs(x, w)
print('2023-B2.1g W', w, N(w, 3), N(yw, 3), 'm', N(mw, 3), 'T', N(w-yw/mw, 3), N(yw-mw*w, 3), 'N', N(w+yw*mw, 3), N(yw+w/mw, 3))
f = (x-3)*exp(-x/3+2); fp = diff(f, x)
assert solve(diff(f, x, 2), x) == [9] and simplify(fp.subs(x, 9)+exp(-1)) == 0 and simplify(f.subs(x, 9)-6*exp(-1)) == 0
print('2024-B2.1d f\'(9)', fp.subs(x, 9), 'AB', (E-0)/(4-3), 'Produkt', simplify(E*fp.subs(x, 9)))
h = -x**3/16+Rational(3, 8)*x**2; assert h.subs(x, 4) == 2 and simplify(h-Rational(9, 8)*(-x**3/18+x**2/3)) == 0
s = solve(Eq(diff(h, x), Rational(1, 2)), x); print('2022-B2.2j x0', s, [N(v, 3) for v in s])
assert solve(Eq(-2*x, x/2-1), x) == [Rational(2, 5)]
b = symbols('b', positive=True); hh = -x*exp(-x/5)
print('2021-B2.2f', diff(hh, x).subs(x, 0), solve(Eq(b**2/2, 32), b))
