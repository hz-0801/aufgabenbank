# AA140/AA150/AA160 Integral – andere Zahlen, nachgerechnet (sympy)
from sympy import *
x, b, m = symbols('x b m', real=True)
p = print
# --- AA140 Integral berechnen
f = (x-3)*exp(-x/3+2); F = -3*x*exp(-x/3+2); assert simplify(diff(F, x)-f) == 0
f = -x**3/18+x**2/3; F = -x**4/72+x**3/9; assert simplify(diff(F, x)-f) == 0 and set(solve(f, x)) == {0, 6} and F.subs(x, 8) == 0
f = Rational(1, 3)*(x**2-9)*exp(x/2); H = (Rational(2, 3)*x**2-Rational(8, 3)*x+Rational(16, 3))*exp(x/2)
assert simplify(diff(H, x)-x**2/3*exp(x/2)) == 0
F = H-6*exp(x/2); assert simplify(diff(F, x)-f) == 0; I = F.subs(x, 0)-F.subs(x, -3)
p('2023-B2.1l F', factor(simplify(F)), 'I', simplify(I), N(I, 5), 'Tisch', N(-4*I, 5), 'LE², cm²', N(-400*I, 5))
f = x**3+2*x**2-3*x; p('2026-A1.1a', factor(f), integrate(f, (x, -1, 0)))
f = (3-x)*exp(x); F = (4-x)*exp(x); assert simplify(diff(F, x)-f) == 0; I = F.subs(x, 2)-F.subs(x, -2)
p('2025-B2.2d', simplify(I), N(I, 5), 'Näherung', N(2*E**2, 5), 'Abw %', N((2*E**2-I)/I*100, 3), 'HP', solve(diff(f, x), x))
h = 4*x**3-45*x**2+162*x+20; p('2023-B2.2i', integrate(h, (x, 0, 5)), integrate(h, (x, 0, 5))/5, 'max', solve(diff(h, x), x), h.subs(x, 3), h.subs(x, 5))
f = Rational(1, 2)*x**4-3*x**2+Rational(5, 2); I = integrate(f, (x, -1, 1)); p('2024-B2.2f', I, 'a', 1/I)
p('2022-A1.3a', integrate(m*x-x**2, (x, m, 0)), solve(Eq(-m**3/6, Rational(9, 2)), m))
u = -log(4); tot = 2-2*exp(u); p('2026-B2.2e', tot, solve(Eq(2-2*exp(x), tot/2), x), N(log(Rational(5, 8)), 3))
# Mehr AA140
F = (-8*x-6)*exp(-x); assert simplify(diff(F, x)-(8*x-2)*exp(-x)) == 0; p('2020-B2.1h H', F+16, (F+16).subs(x, 0))
F = (-3*x-12)*exp(-x/3); assert simplify(diff(F, x)-(x+1)*exp(-x/3)) == 0
F = -(x**2-2*x+2)*exp(-x); assert simplify(diff(F, x)-(x**2-4*x+4)*exp(-x)) == 0
h = 6*x*exp(-x/20)+40; p('2019-B2.2e', N(integrate(h, (x, 0, 60)), 6), N(integrate(h, (x, 0, 60))/60, 4))
p('IQB23', integrate(x**4-2*x**3, (x, 0, 1)), 'IQB18', integrate((x**3-12*x**2+32*x)/6, (x, 0, 4)))
p('2020-A1.1', diff(3*x**4-2*x+5, x), '2019-A1.1a', diff(-4*x**4-6*x**2+x, x), integrate(-4*x**4-6*x**2+x, x))
# --- AA150 Flächeninhalt
f = 2*exp(x)-2*exp(-1); I = integrate(f, (x, -1, 0)); p('2025-A1.4b', simplify(I), N(I, 3))
f = x**3-9*x; p('2024-A1.1b', solve(f, x), integrate(f, (x, -3, 0)), 2*integrate(f, (x, -3, 0)))
u = symbols('u'); p('2026-B2.2d', integrate(2*exp(x), (x, u, 0)))
F = -3*x*exp(-x/3+2); I = F.subs(x, 12)-F.subs(x, 3); p('2024-B2.1j', simplify(I), N(I, 4), 'cm²', N(2*I/4, 4))
g = x**3/4+x**2; I = integrate(g, (x, -2, 0)); p('2026-B2.1g', g.subs(x, -2), I, 'gesamt', 2*(2*I+2*pi), N(2*(2*I+2*pi), 4))
h = -x**3/16+Rational(3, 8)*x**2; A = integrate(h, (x, 0, 4))-integrate(-2*x, (x, 0, Rational(2, 5)))-integrate(x/2-1, (x, Rational(2, 5), 4))
p('2022-B2.2h', integrate(h, (x, 0, 4)), integrate(-2*x, (x, 0, Rational(2, 5))), integrate(x/2-1, (x, Rational(2, 5), 4)), A)
f = x**3/12-x; g = x/3; I = integrate(g-f, (x, 0, 4)); r2 = 4**2+Rational(4, 3)**2
p('2025-B2.1e', f.subs(x, 4), r2, I, 4*I, 'A1', r2*pi, N(r2*pi, 4), 'A1-A2', N(r2*pi-4*I, 4))
f = Rational(1, 2)*x**4-3*x**2+Rational(5, 2); s = Rational(5, 2)*x+Rational(5, 2)
p('2024-B2.2e', [v for v in solve(f-s, x) if v.is_rational], integrate(f-s, (x, -1, 0)), Rational(1, 2)*f.subs(x, 0))
f = Rational(1, 3)*(x**2-9)*exp(x/2); I = integrate(f, (x, -3, 0)); zw = Rational(9, 2)+I
p('2023-B2.1m Dreieck 9/2, Zwischenraum', N(zw, 4), 'Zuwachs', N(8*zw, 4), 'cm²', N(800*zw, 4))
f = (x+3)*exp(-x); Ab = f.subs(x, 0)-f.subs(x, b); assert simplify(Ab+integrate(diff(f, x), (x, 0, b))) == 0
p('2022-B2.1i', simplify(Ab), limit(Ab, b, oo), nsolve(Ab-2, b, 1.5))
p('Mehr 2021-A1.1b', 2*integrate(2*x**3-2*x, (x, -1, 0)), '2019-A1.2b', solve((-x**2+4*x+2)-(x**2-4), x), integrate((-x**2+4*x+2)-(x**2-4), (x, -1, 3)), 'IQB17', integrate(x**3+3*x**2, (x, -3, 0)))
# --- AA160 Integral am Graphen
from mpmath import quad as mq, exp as mexp
ff = lambda t: 1/(1+mexp(2*(t-4)))+(1.4*(t-1)**2*mexp(-0.8*(t-1)) if t > 1 else 0)
xs = [1+k/1000 for k in range(4000)]; i = max(range(4000), key=lambda k: ff(xs[k]))
p('2023-A1.2a HP', xs[i], round(float(ff(xs[i])), 3), 'f(1)', round(float(ff(1)), 3), 'I13', round(float(mq(ff, [1, 3])), 3), 'F(5)', round(float(mq(ff, [1, 5])), 2), 'F(oo)', round(float(mq(ff, [1, 4, 80])), 2))
f = (3-x)*exp(x); p('2025-B2.2c', f.subs(x, 2), N(2*E**2, 4), 'Sehne bei 0', N(E**2/2*2, 3), 'f(0)', f.subs(x, 0))
p('2022-B2.2i', integrate(x/2, (x, 0, 4)))
f = x**3+2*x**2-3*x; p('2026-A1.1b', integrate(f, (x, -3, 0)), integrate(f, (x, 0, 1)))
f = (x+3)*exp(-x); fp = diff(f, x); p('2022-B2.1f', simplify(integrate(fp, (x, -4, -3))), simplify(integrate(fp, (x, -1, 0))), N(integrate(fp, (x, -1, 0)), 3))
fp = x**3/4+x**2; p('2026-B2.1b', factor(fp), solve(fp, x))
fp = 3*(x+2)*exp(-x-1); p('2026-A1.7b', solve(fp, x), solve(diff(fp, x), x), fp.subs(x, -1))
f = (x-3)*exp(-x/3+2); p('2024-B2.1f', solve(diff(f, x), x))
p('IQB19', solve(-x*(x-6)/3, x))
