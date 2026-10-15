# AS20 Ziehen ohne Zurücklegen – neue Zahlen, nachgerechnet (sympy)
from sympy import *
from itertools import combinations, permutations, product
R=Rational; p=lambda *a: print(*a)
# 2024-A1.3a/b: acht Stühle, vier mit Lücke
a=[c for c in combinations(range(1,9),4) if all(c[i+1]-c[i]>=2 for i in range(3))]; p('A1.3a',a); assert len(a)==5
p('A1.3b',len(a)*factorial(4))
# 2026-A1.3b: fünf Würfe, A höchstens einmal Z, B letzte zwei mind. einmal Z
e=[''.join(w) for w in product('ZW',repeat=5) if not (w.count('Z')<=1) and not ('Z' in w[3:])]; p('A1.3b26',e); assert len(e)==4
# 2025-A1.6a: 16 Kinder, 6 Bronze
P=R(6,16)*R(5,15); p('A1.6a25',P); assert P==R(1,8)
# 2022-A1.6a/b: 3 rot, 2 grün
P=1-R(3,5)*R(2,4)*R(1,3); p('A1.6a22',P); assert P==R(9,10)
p('A1.6b22 rot weg',2*R(2,4)*R(2,3),'grün weg',2*R(3,4)*R(1,3))
# 2023-A1.6b: 4 rot, 2 weiß, drei ohne Zurücklegen, mehr rote
P3=R(4,6)*R(3,5)*R(2,4); P2=3*R(4,6)*R(3,5)*R(2,4); p('A1.6b23',P3,P2,P3+P2)
P3b=binomial(4,3)/binomial(6,3); P2b=binomial(4,2)*2/binomial(6,3); assert (P3b,P2b)==(P3,P2)
# 2023-B4.1g/h: 24 Lehrkräfte, 14 weiblich, 5 ausgewählt
g=binomial(14,5)/binomial(24,5); p('B4.1g',binomial(14,5),binomial(24,5),g,N(g,4))
h0=binomial(10,5)/binomial(24,5); h1=14*binomial(10,4)/binomial(24,5); p('B4.1h',binomial(10,5),14*binomial(10,4),h0+h1,N(h0,4),N(h1,4),N(h0+h1,4))
# Mehr
P=R(5,8)*R(4,7); p('M 2018-B3.1a',P); assert P==R(5,14)
P=2*R(12,20)*R(8,19); p('M 2019-A1.4c',P,N(P,3))
P=2*R(4,6)*R(2,5); p('M 2020-A1.5a',P)
A=binomial(36,8)/binomial(40,8); p('M 2017-B3.1b',A,N(A,3),N(1-A,3))
w3=R(7,10)*R(6,9)*R(5,8)+2*R(7,10)*R(3,9)*R(6,8)+R(3,10)*R(2,9)*R(7,8); p('M 2021-A1.7b',w3); assert w3==R(7,10)
P=(binomial(6,2)*binomial(4,4)+binomial(6,3)*binomial(4,3))/binomial(10,6); p('M 2019-B4.2f',binomial(6,2),binomial(6,3)*binomial(4,3),binomial(10,6),P)
p('M 2018-iqb-A11a',R(2,10)*R(1,9)); p('M 2018-iqb-A11b',1-R(6,10)*R(5,9)*R(4,8))
p('M 2023-iqb-A12a',[(z,m) for z in range(1,7) for m in 'ZW' if z%2==1 and m=='W' and z>2])
k=symbols('k'); p('M 2019-iqb-A2b',solve(Eq(2*k*(8-k)/(8*7),R(4,7)),k))
