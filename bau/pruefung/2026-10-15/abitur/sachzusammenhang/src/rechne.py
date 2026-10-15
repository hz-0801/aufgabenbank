# AA130 Graph im Sachzusammenhang – andere Zahlen nachgerechnet (sympy); Zeilen in mathe-nachhilfe/abitur/mehr-abi-gk/kurvenuntersuchung.csv
from sympy import *
x, t = symbols('x t', real=True)
def p(*a): print(*a)
# B1 2023-B2.2h  Backofen (Graph als Modell, nur zum Zeichnen): Dauerphase ab 5 min
T = 195 - 175*exp(-x*Rational(4, 5)) + 13*sin(pi*(x - 3)/2)*(1 - exp(-x*Rational(4, 5)))
werte = [float(T.subs(x, 5 + i*0.05)) for i in range(301)]
p('B1', round(min(werte), 1), round(max(werte), 1), 'Mittel', round(sum(werte)/len(werte), 1))
# B2 2025-B2.2e  a(x) = 2400(1 - e^(-x²/4))
a = 2400*(1 - exp(-x**2/4)); p('B2', solve(diff(a, x, 2), x), limit(a, x, oo))
# B3 2023-B2.2e  f = x³ - 9x² + 24x - 16
f = x**3 - 9*x**2 + 24*x - 16; m = diff(f, x).subs(x, 3); tw = m*(x - 3) + f.subs(x, 3)
p('B3', f.subs(x, 0), f.subs(x, 6), expand(tw), factor(f - tw))
# B4 2026-A1.4a  f = 2 sin x, A(π/2|2), B(3π/2|-2), C(5π/2|2)
p('B4', Rational(1, 2)*2*pi*4)
# B5 2022-B2.1k  h = 1/8 t (t-36)^2
h = t*(t - 36)**2/8; p('B5', h.subs(t, 12), h.subs(t, 18), 2*h.subs(t, 12) - h.subs(t, 18))
# B6 2026-B2.1f / B7 2026-B2.1i  g = 8/3 x³ + 4x² auf [-1; 0], Halbkreise um (±1|0) mit r = 4/3
g = Rational(8, 3)*x**3 + 4*x**2; r = g.subs(x, -1)
p('B6', 2*r, N(2*r, 4), 2*(1 + r), N(2*(1 + r), 4))
L = Integral(sqrt(1 + diff(g, x)**2), (x, -1, 0)).evalf(); U = 4*Rational(17, 10) + 2*pi*r
p('B7', round(L, 3), N(U, 4), N(U/3, 4), N((U/3 - 5)*60, 3))
# B8 2023-B2.1k  Tisch: f = 0,5(x²-9)e^x, Spitzen (±3|0), (0|±4,5), 1 LE = 10 cm
f = Rational(1, 2)*(x**2 - 9)*exp(x); p('B8', f.subs(x, 0), [N(f.subs(x, v), 3) for v in (-3, -2, -1, 0)], 'Kante 90 cm', 90*90*50/1000)
# B9 2024-B2.1h  Knauf f = (x-3)e^(-x/3+2), 3 <= x <= 12, HP (6|3), 1 LE = 0,5 cm, Dichte 0,86
f = (x - 3)*exp(-x/3 + 2); V = Rational(9, 2)*3*3; p('B9', f.subs(x, 6), V, N(V*Rational(86, 100), 4))
# B10 2024-B2.1g neben  Sockel
p('B10', N(2*f.subs(x, 12)*5, 3))
# Mehr
hh = Rational(5, 100)*x**2 + 30; gg = Rational(1, 1000)*(x**4/1600 - 8*x**2 + 25600)
p('M1', 'S-C', hh.subs(x, 0) - gg.subs(x, 0), 'A', hh.subs(x, -20), 'AB', hh.subs(x, -20) - gg.subs(x, 0))
ff = (-x**2/5 + 3*x)*exp(-x/5); p('M2', N(ff.subs(x, 20), 3))
K = x**3 - 15*x**2 + 80*x + 30; p('M3', discriminant(diff(K, x), x), K.subs(x, 0), K.subs(x, 10), solve(diff(K, x, 2), x))
