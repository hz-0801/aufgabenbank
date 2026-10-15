# AA110 Funktion aufstellen – andere Zahlen nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x, t, u, a, b, c, d = symbols('x t u a b c d', real=True)
def p(*z): print(*z)
# B1 2022-B2.2g  Gerade durch C(0,4|-0,5), D(2|1,1)
m = (Rational(11, 10) + Rational(1, 2))/(2 - Rational(2, 5)); n = Rational(11, 10) - 2*m; p('B1', m, n)
# B2 2022-B2.2k  k = a x^4 + b x^2, R(2|1), S(4|3,5)
k = a*x**4 + b*x**2; mRS = (Rational(7, 2) - 1)/(4 - 2)
s = solve([k.subs(x, 2) - 1, diff(k, x).subs(x, 2) - mRS], [a, b]); p('B2', mRS, s, diff(k, x).subs(x, 0), k.subs(x, 0))
kk = k.subs(s); p('B2 Gegenstück rechts: 4,5 - k(6 - x) bei 6:', Rational(9, 2) - kk.subs(x, 0), 'Steigung bei 4:', diff(Rational(9, 2) - kk.subs(x, 6 - x), x).subs(x, 4))
# B3 2023-B2.2k  Grad 3, k(0)=20, k'(0)=120, H(6|272)
k = a*x**3 + b*x**2 + c*x + d; s = solve([k.subs(x, 0) - 20, diff(k, x).subs(x, 0) - 120, k.subs(x, 6) - 272, diff(k, x).subs(x, 6)], [a, b, c, d])
p('B3', s, diff(k, x, 2).subs(s).subs(x, 6))
# B4 2022-B2.1h  A(u) = u (u+3) e^-u
A = u*(u + 3)*exp(-u); Ap = simplify(diff(A, u)); us = [r for r in solve(Ap, u) if r > 0][0]
p('B4', factor(Ap), us, N(us, 4), N((us + 3)*exp(-us), 4), N(A.subs(u, us), 4))
# B5 2024-B2.2g  d = p - f
f = Rational(1, 2)*x**4 - 3*x**2 + Rational(5, 2); pp = -Rational(5, 2)*x**2 + Rational(5, 2); dd = expand(pp - f)
p('B5', dd, solve(diff(dd, x), x), [dd.subs(x, v) for v in (0, 1, -1, 1/sqrt(2))])
# Mehr
g = Rational(1, 1000)*(x**4/1600 - 8*x**2 + 25600); fl = a*x**2 + b*x + 30
s = solve([diff(fl, x).subs(x, 0) - diff(Rational(5, 100)*x**2 + 30, x).subs(x, 0), fl.subs(x, 40) - g.subs(x, 40) - Rational(44, 10)], [a, b]); p('M1', g.subs(x, 40), s)
gg = a*t**3 + b*t**2; p('M2', solve([gg.subs(t, 4) - 384, diff(gg, t).subs(t, 4) - 144], [a, b]))
q = a*x**2 + b*x; p('M3', solve([q.subs(x, 3) - Rational(27, 10), diff(q, x).subs(x, 3)], [a, b]))
gb = a*x**3 + b*x**2 + 2; p('M4', solve([diff(gb, x).subs(x, 20), gb.subs(x, 20) - 10], [a, b]))
fl = -Rational(7, 1000)*x**2 + 30; dd = fl - g; s = [r for r in solve(diff(dd, x), x) if r > 0]; p('M5', s, N(s[0], 4), dd.subs(x, s[0]), fl.subs(x, s[0]), g.subs(x, s[0]))
f = x**3 - 6*x**2 + 32; A = x*f; p('M6', expand(diff(A, x)), diff(A, x).subs(x, 2))
p('M7', solve([a - Rational(3, 2), a*b - 3], [a, b]))
