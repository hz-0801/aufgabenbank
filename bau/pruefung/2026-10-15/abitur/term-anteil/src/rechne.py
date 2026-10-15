# AS50 Term und Anteil am Baum – neue Zahlen, nachgerechnet (sympy)
from sympy import *
R=lambda s: Rational(s); p=lambda *a: print(*a)
p('2025 A1.3a',Rational(2,8)**2)
t=Rational(7,10)**4+4*Rational(7,10)**3*Rational(3,10); p('2024 A1.6b',t,N(t,4))
t=binomial(6,2)*binomial(10,3)/binomial(16,5); p('2025 A1.6b',t,N(t,3))
a=symbols('a'); p('2026 B4e',solve(Eq(R('0.8')*R('0.3')+R('0.2')*(1-a),R('0.34')),a))
x=symbols('x'); s=solve(Eq(R('0.12')*R('0.10')+R('0.08')*R('0.025')+R('0.80')*x,R('0.06')),x); p('2022 B4j',s)
q=symbols('q'); p('2024 A1.9b',solve(Eq(R('0.7')*q+R('0.3')*(1-q),Rational(360,1000)),q))
# Mehr
p('2020 g',solve(Eq(3*a*R('0.05'),(1-a)*R('0.1')),a))
s=solve(Eq(q+(1-q)*q/2,R('0.84')),q); p('2019 e',s,[N(v,4) for v in s])
p('2021 f',1-(R('0.7')**12+12*R('0.3')*R('0.7')**11),N(1-(R('0.7')**12+12*R('0.3')*R('0.7')**11),4))
p('2025iqb b',1-(R('0.3')*R('0.6')+R('0.49')))
p('2019iqb B3.2a',1-R('0.4')**3)

