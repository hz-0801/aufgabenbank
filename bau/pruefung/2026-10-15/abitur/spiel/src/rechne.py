# AS90 Erwartungswert im Spiel – neue Zahlen, nachgerechnet (sympy)
from sympy import *
R=Rational; p=lambda *a: print(*a)
w=R(2,7); E=27*w**2+2*3*w*(1-w)+R(1,3)*(1-w)**2; p('2023 a/b',E,N(E,4),'Summand 2',2*3*w*(1-w)); assert E==R(529,147)
pp=symbols('p'); E=27*pp**2+6*pp*(1-pp)+(1-pp)**2/3; p('2023 c',expand(3*(E-3)),solve(Eq(E,3),pp))
q=symbols('q'); E=16*q**2+8*2*q*(1-q)+4*(1-q)**2; p('2024 c',expand(E-9),solve(E-9,q)); assert expand(E-9)==4*q**2+8*q-5
# Mehr
p('2018 d',R(3,10)*5)
x=symbols('x'); qx=15/(18+x)*14/(17+x); p('2018 e',qx.subs(x,2),N(qx.subs(x,2),3),solve(Eq(qx,R(1,2)),x),expand((18+x)*(17+x)-420))
y=symbols('y'); p('2021 i',solve(Eq(10*y+20*(R(9,10)-y)+5,R(3200,200)),y))
p('2021 A1.6b',R(4,16)+2*R(6,16))
p('2018iqb',R(1,2)*1+R(1,3)*3+R(1,6)*9)
p('2024iqb',5*R(32,100)+10*R(4,100), 2*R(2,10)*R(8,10))
p('2023iqb',solve(Eq(R(1,2)*1+R(1,4)*2+R(1,8)*5+R(1,8)*x,3),x))
w_=symbols('w',positive=True); p('2025iqb',solve(Eq(9/(w_+1)+6*w_/(w_+1)/w_,3),w_))
