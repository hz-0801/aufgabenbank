# AS10 Baumdiagramm – neue Zahlen, nachgerechnet (sympy); Abschnitt je Zeile von mehr-abi-gk/baum-bedingte-wahrscheinlichkeit.csv
from sympy import *
R=Rational; p=lambda *a: print(*a)
# 2024-A1.9a: F1 0,7, F2 0,3, Ja|F1 = p, Ja|F2 = 1 - p (Baum, ohne Zahl)
# 2025-B4a / B4b: K 0,315; B|K 0,142; B|nicht K 0,055
PB=R(315,1000)*R(142,1000)+R(685,1000)*R(55,1000); p('B4b',PB,N(PB,4)); assert abs(N(PB)-0.0824)<0.0001
# 2024-B4.2a: P(6)^2 = 1/16
q=symbols('q',positive=True); s=solve(q**2-R(1,16),q); p('B4.2a',s,(1-s[0])**2); assert s==[R(1,4)] and (1-s[0])**2==R(9,16)
# 2024-B4.2b: 6 Personen, genau vier kleinster Rabatt, hintereinander: 3 Lagen
P=3*R(9,16)**4*R(7,16)**2; p('B4.2b',P,N(P,4))
# 2024-A1.6a: 0,3^3 < 0,03
p('A1.6a',R(3,10)**3); assert R(3,10)**3<R(3,100)
# 2026-B4d: T 0,8; w|T 0,7; a = 0,3
x=R(8,10)*R(7,10); y=R(2,10)*(1-R(3,10)); p('B4d',x,y,x/y); assert x==4*y
# 2023-A1.6a: 4 rot, 2 weiß, mit Zurücklegen
P=R(4,6)**2+R(2,6)**2; p('A1.6a',P); assert P==R(5,9)
# 2025-A1.3b: fünfmal 3, zweimal 2, einmal 1
g=R(2,8); u=R(6,8); P=g*u+u*g; p('A1.3b',P); assert P==R(3,8)
# 2022-B4f: Ziel A 12 %, je 12 Pakete
q12=R(88,100)**12; P=1-(1-q12)**2; p('B4f',N(q12,4),N(P,4))
# Mehr
P=1-R(2,3)**4; p('M 2020-B4.1b',P,N(P,4)); assert P==R(65,81)
p('M 2025-iqb-A11a', R(49,100)/R(7,10))
p('M 2019-B4.2a', R(1,6)*R(3,6))
p('M 2021-B4g', R(1,10)*R(3,10)*R(6,10))
p('M 2021-iqb-B1.1a', R(1,8)**2*R(7,8))
P=R(2,10)*R(4,100)+R(3,10)*R(2,100)+R(1,10)*R(5,100)+R(4,10)*R(3,100); p('M 2017-B3.1c',P); assert P==R(31,1000)
P=R(7,10)*R(6,9)+R(3,10)*R(7,9); p('M 2021-A1.7a',P); assert P==R(7,10)
P=4*R(1,10)*R(6,10)**3+R(3,10)**4; p('M 2021-B4h',P,N(P))
# Mehr (Fortsetzung)
x=1-R(12,100); y=R(1,4)*R(4,100); p('M 2020-B4.2e',x,y); assert (x,y)==(R(88,100),R(1,100))
x=R(1,10)/R(1,2); y=R(1,2)*R(1,4); p('M 2026-iqb-A13a',x,y)
