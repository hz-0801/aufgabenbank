# AA80 Winkel am Graphen – andere Zahlen, nachgerechnet (sympy)
from sympy import *
x = symbols('x', real=True)
d = lambda v: N(deg(v), 4)
f = -x**3/18+x**2/3
assert solve(diff(f, x, 2), x) == [2] and f.subs(x, 2) == Rational(8, 9)
m = diff(f, x).subs(x, 2); print('2022-B2.2e m', m, 'Winkel', d(atan(m)), 'y-Abschnitt', f.subs(x, 2)-2*m)
tq = tan(rad(31)); s = solve(Eq(diff(f, x), tq), x); print('2022-B2.2f tan31', N(tq, 4), [N(v, 4) for v in s], 'mit 0,6:', solve(Eq(diff(f, x), Rational(3, 5)), x))
f = (x-3)*exp(-x/3+2); fp = diff(f, x); assert simplify(fp-(2-x/3)*exp(-x/3+2)) == 0
print('2024-B2.1i f\'(3)', fp.subs(x, 3), d(atan(E)), 'alpha', N(2*deg(atan(E)), 4))
f = x**3/18-Rational(3, 2)*x; g = x/2; k = diff(f, x).subs(x, 3*sqrt(3)); assert f.subs(x, 3*sqrt(3)) == 0 and k == 3
print('2025-B2.1d Steigungswinkel', d(atan(3)), 'tan alpha', Abs((3-Rational(1, 2))/(1+3*Rational(1, 2))))
f = (x+3)*exp(-x); fp = diff(f, x); fpp = diff(fp, x)
assert simplify(fp+(x+2)*exp(-x)) == 0 and simplify(fpp-(x+1)*exp(-x)) == 0 and solve(Eq(f, fp), x) == [-Rational(5, 2)]
m1, m2 = fp.subs(x, -Rational(5, 2)), fpp.subs(x, -Rational(5, 2)); tp = Abs((m1-m2)/(1+m1*m2))
print('2022-B2.1e m1', N(m1, 4), 'm2', N(m2, 4), 'tan', N(tp, 3), 'phi', d(atan(tp)))
f = Rational(1, 2)*(x**2-9)*exp(x); fp = diff(f, x); assert simplify(fp-(x**2/2+x-Rational(9, 2))*exp(x)) == 0
print('2023-B2.1j f\'(-3)', fp.subs(x, -3), N(fp.subs(x, -3), 3), 'halber Winkel', d(atan(Abs(fp.subs(x, -3)))), 'Winkel', N(2*deg(atan(Abs(fp.subs(x, -3)))), 4))
print('  Sehne bei -1,5:', -2.25, 'Graph', N(f.subs(x, -1.5), 3))
# Mehr
f = (8*x-2)*exp(-x); fp = diff(f, x); assert simplify(fp-(10-8*x)*exp(-x)) == 0
print('2020-B2.1f f(1)', f.subs(x, 1), 'm', fp.subs(x, 1), 't', expand(fp.subs(x, 1)*(x-1)+f.subs(x, 1)), d(atan(fp.subs(x, 1))))
f = (x+1)*exp(-x/3); fp = diff(f, x); assert simplify(fp-(2-x)/3*exp(-x/3)) == 0
m = fp.subs(x, 0); tp = Abs((1-m)/(1+m)); print('2018-B1.2b m', m, 'tan', tp, 'phi', d(atan(tp)))
f = -x**3/250+Rational(3, 50)*x**2+2; fp = diff(f, x)
print('2017-B1.1c W', solve(diff(f, x, 2), x), 'f(5)', f.subs(x, 5), 'f\'(5)', fp.subs(x, 5), d(atan(fp.subs(x, 5))))
