"""Nachrechnung mehr-abi-gk/binomialverteilung.csv (AS60 Bernoulli-Kette, AS70 Binomialwahrscheinlichkeit,
AS80 Säulendiagramm und Erwartungswert), sympy exakt, gerundet verglichen. Läuft ohne Ausgabe = alles stimmt."""
from sympy import binomial as C, Rational as R, log, N, ceiling
import math


def pmf(k, n, p): return C(n, k) * p**k * (1 - p)**(n - k)
def F(k, n, p): return sum(pmf(i, n, p) for i in range(0, k + 1))
def gl(x, soll, d=3): assert round(float(x), d) == soll, (float(x), soll)
def mind(q, ziel): return int(ceiling(log(1 - ziel) / log(q)))   # kleinstes n mit 1 - q^n >= ziel


h, t = R(1, 2), R(1, 3)
# ---- AS60
assert h**6 + 6 * h * h**5 == R(7, 64)                                        # 26 A1.3a
gl(pmf(4, 12, R(8, 10)), 0.0005, 4)                                            # 26 B4a (80 % wie AS10/AS40)
gl(1 - F(69, 100, R(7, 10)), 0.549)                                            # 23 B4.1e
assert [x for x in range(101) if x >= 3 * (100 - x)][0] == 75                  # 23 B4.1d
gl(1 - F(74, 100, R(7, 10)), 0.163)
gl(150 * R(97, 100)**149 * R(3, 100) + R(97, 100)**150, 0.058)                 # 17 B3.1f (≈ 0,0585)
gl(sum(pmf(k, 24, R(5, 12)) for k in (8, 9, 10)), 0.436)                       # 19 B4.2e
gl(pmf(12, 40, t) + pmf(13, 40, t), 0.256)                                     # 20 B4.2b
assert pmf(4, 7, t) == C(7, 4) * R(2, 3)**3 * t**4                            # IQB 21 A2a
assert 2 * R(2, 10) * R(8, 10) == R(32, 100)                                   # IQB 24 A1.2a
gl(F(9, 25, R(28, 100)), 0.866)                                                # IQB 26 B2.1d
assert 1 - R(3, 4)**2 < h < 1 - R(3, 4)**3                                     # IQB 20 A2b
# ---- AS70
gl(F(9, 12, R(8, 10)), 0.442)                                                  # 26 B4b
p8 = R(8, 100)   # Ziel B 8 % wie AS10/AS30/AS50 (2022 B4)
gl(F(10, 100, p8) - F(9, 100, p8), 0.102); gl(F(9, 100, p8), 0.722)            # 22 B4b (Tabelle 0,7220 / 0,8243)
gl(F(9, 100, p8), 0.7220, 4); gl(F(10, 100, p8), 0.8243, 4)
assert mind(R(7, 10), R(95, 100)) == 9                                        # 23 B4.1f
assert mind(R(92, 100), R(9, 10)) == 28                                       # 22 B4d
gl(1 - 0.67**(1 / 20), 0.020)                                                  # 22 B4e
pp = R(824, 10000)   # 8,24 % wie AS10 (2025 B4b)
gl(F(75, 800, pp), 0.8895, 4); gl(F(76, 800, pp), 0.9110, 4)                   # 25 B4d
gl(1 - F(6, 10, R(35, 100)), 0.026); gl(F(7, 10, R(35, 100)) - F(3, 10, R(35, 100)), 0.481)   # 21 B4a
gl(1 - F(14, 40, t), 0.342)                                                    # 20 B4.2a
gl(pmf(75, 100, R(3, 4)), 0.092); gl(1 - F(29, 100, R(1, 4)), 0.150)           # 19 B4.1a
gl(F(70, 100, R(3, 4)), 0.150)
gl(F(6, 50, R(15, 100)), 0.361); gl(F(11, 50, R(15, 100)) - F(7, 50, R(15, 100)), 0.418)       # 18 B3.2a
assert mind(R(3, 4), R(99, 100)) == 17                                        # 19 B4.1b
assert mind(R(4, 5), R(95, 100)) == 14                                        # 20 B4.1c
assert mind(R(65, 100), R(95, 100)) == 7                                      # 21 B4e
gl(1 - 0.2**(1 / 30), 0.052)                                                   # 18 B3.2d
best = min(range(15, 30), key=lambda p: abs(F(2, 10, R(p, 100)) - R(62, 100)))
assert best == 22                                                              # IQB 21 B2.1d
gl(pmf(150, 750, R(1, 5)), 0.036)                                              # IQB 22 B2.2a
gl(1 - F(6, 25, R(28, 100)), 0.575)                                            # IQB 26 B2.1c
gl(F(157, 250, R(3, 5)) - F(142, 250, R(3, 5)), 0.667)                         # IQB 19 B1.1a
# ---- AS80
gl(pmf(5, 10, R(2, 5)) + pmf(6, 10, R(2, 5)), 0.312)                          # 23 A1.7a (Ablesung ≈ 0,31)
q = R(1, 4)
assert round(float(pmf(5, 16, q)), 2) == 0.18                                  # 26 A1.6b: v = 5
assert F(1, 16, q) < 0.15 < F(2, 16, q) < 0.25 < F(3, 16, q)                  # w = 2
assert pmf(8, 12, R(8, 10)) == pmf(4, 12, R(2, 10)); gl(pmf(4, 12, R(2, 10)), 0.13, 2)        # 26 B4c
gl(1 - F(7, 19, h), 0.82, 2); gl(pmf(11, 19, h), 0.14, 2); gl(pmf(9, 19, h), 0.18, 2)         # 25 A1.9b
assert max(range(17), key=lambda k: pmf(k, 16, q)) == 4 and 16 * q == 4       # 26 A1.6a
assert max(range(16), key=lambda k: pmf(k, 15, R(1, 5))) == 3                  # 23 A1.7b: B
assert max(range(16), key=lambda k: pmf(k, 15, t)) == 5
assert pmf(9, 19, h) == pmf(10, 19, h) and 19 * h == R(19, 2)                 # 25 A1.9a
assert max(range(801), key=lambda k: pmf(k, 800, pp)) == 66 and 800 * pp == R(1648, 25)       # 25 B4c
assert (10 - 100 * p8) / (100 * p8) == R(1, 4)                                 # 22 B4c
p = 1 - R(9, 36); n = 36 / p                                                   # 26 A1.9a
assert p == R(3, 4) and n == 48 and n * p * (1 - p) == 9
gl(pmf(37, 48, p), 0.128)
assert max(range(41), key=lambda k: pmf(k, 40, t)) == 13                       # 20 B4.2d
assert max(range(241), key=lambda k: pmf(k, 240, R(15, 100))) == 36            # 18 B3.2b
assert 24 * R(5, 12) == 10                                                     # 19 B4.2c
gl(pmf(4, 18, R(35, 100)) + pmf(5, 18, R(35, 100)) + pmf(6, 18, R(35, 100)), 0.471)           # IQB 17 A1.1a
gl(F(13, 23, h), 0.80, 2); gl(pmf(10, 23, h), 0.14, 2); gl(pmf(12, 23, h), 0.16, 2)          # IQB 21 A2b
assert max(range(11), key=lambda k: pmf(k, 10, R(2, 5))) == 4                  # IQB 19 A1.2b
assert 6 * t == 2 and pmf(6, 6, t) == R(1, 729)                                # IQB 20 A2a
print('alles nachgerechnet')
