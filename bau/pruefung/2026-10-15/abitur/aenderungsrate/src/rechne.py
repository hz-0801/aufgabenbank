# AA30 Änderungsrate – andere Zahlen, nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/ableitung-tangente.csv
from sympy import *
x, t = symbols('x t', real=True)
def p(*a): print(*a)
# 1 2025-B2.2f Likes: a(x) = 2400(1 - e^(-x^2/4)) wie B2.2e/g, 13 bis 15 Uhr
a = 2400*(1-exp(-x**2/4))
p('1 a(1)', N(a.subs(x, 1), 4), 'a(3)', N(a.subs(x, 3), 4), 'mittel', N((a.subs(x, 3)-a.subs(x, 1))/2, 4), 'abgelesen (2150-530)/2 =', (2150-530)/2,
  'Wendestelle', [N(s, 3) for s in solve(diff(a, x, 2), x) if s > 0])
# 2 2026-B2.2h Ofen k(x) = 55e^(-x/300) + 18 (wie Pilot B2.2g), 50 Minuten
k = 55*exp(-x/300)+18; kp = diff(k, x); assert simplify(kp + Rational(11, 60)*exp(-x/300)) == 0
m = (k.subs(x, 50)-k.subs(x, 0))/50; mo = kp.subs(x, 50)
p('2 k(50)', N(k.subs(x, 50), 5), 'mittel', N(m, 4), 'k\'(50)', N(mo, 4), 'Abw', N((m-mo)/mo, 3))
assert N((m-mo)/mo) < 0.10
# 3 2024-A1.4a g(x) = 3e^x - 3
g = 3*exp(x)-3; p('3 g\'(0)', diff(g, x).subs(x, 0), 'g(0)', g.subs(x, 0))
# 4 2026-B2.2i k(x) - 18 = c k'(x)
p('4 c', simplify((k-18)/kp))
# 5 2022-B2.1m Tauchroboter h(t) = 1/8 t^3 - 9t^2 + 162t
h = Rational(1, 8)*t**3-9*t**2+162*t; hp = diff(h, t)
p('5 h\'', factor(hp), 'Max', h.subs(t, 12), 'h(36)', h.subs(t, 36), 'h\'=19,5:', solve(Eq(hp, Rational(39, 2)), t), expand(8*(hp-Rational(39, 2))/3))
# 6 2025-A1.7b f(x) = -x^2 + 6x - 4 (wie A1.7a)
f = -x**2+6*x-4; p('6 Lösungen', solve(Eq(f/x, diff(f, x)), x), 'Tangente in 2:', expand(diff(f, x).subs(x, 2)*(x-2)+f.subs(x, 2)), 'in -2:', expand(diff(f, x).subs(x, -2)*(x+2)+f.subs(x, -2)))
# 7 2022-B2.2c f(x) = -1/18 x^3 + 1/3 x^2, [0; 4]
f = -x**3/18+x**2/3; s = (f.subs(x, 4)-f.subs(x, 0))/4; xs = solve(Eq(diff(f, x), s), x)
p('7 f(4)', f.subs(x, 4), 'Sekante', s, 'x0', xs, [N(v, 3) for v in xs], expand(-6*(diff(f, x)-s)))
# Mehr
h = 6*t*exp(-t/20)+40
p('M1 2019-B2.2d', 'h(8)', N(h.subs(t, 8), 4), 'mittel', N((h.subs(t, 8)-h.subs(t, 0))/8, 3))
f = -x**3/250+Rational(3, 50)*x**2+2; s = (f.subs(x, 10)-f.subs(x, 0))/10; xs = solve(Eq(diff(f, x), s), x)
p('M2 2017-B1.1b', 'f(10)', f.subs(x, 10), 'f\'(0), f\'(10)', diff(f, x).subs(x, 0), diff(f, x).subs(x, 10), 'm', s, xs, [N(v, 3) for v in xs])
f = sqrt(x); xs = solve(Eq(f, x/3), x); p('M3 IQB 2024 A22', xs, 'mittel', (3-0)/9, solve(Eq(diff(f, x), Rational(1, 3)), x))
