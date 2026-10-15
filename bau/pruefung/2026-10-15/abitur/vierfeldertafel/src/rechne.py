# AS30 Vierfeldertafel – neue Zahlen, nachgerechnet (sympy)
from sympy import *
R=lambda s: Rational(s); p=lambda *a: print(*a)
def tafel(A,B,AB):  # P(A), P(B), P(A∩B) -> vier Felder
    return dict(AB=AB, nAB=B-AB, AnB=A-AB, nAnB=1-A-B+AB)
# 2023-B4.1a/b: G 0,30, W∩G 0,20, W 0,65
t=tafel(R('0.30'),R('0.65'),R('0.20')); p('2023 a',t); p('2023 b P(W∪G)',1-t['nAnB']); assert 1-t['nAnB']==R('0.75')
# 2024-B4.1b/c/d: T 0,7, M 0,3, P(¬T∩M) 0,06
TM=R('0.3')-R('0.06'); t=tafel(R('0.7'),R('0.3'),TM); p('2024 b',t); p('2024 c entweder',t['AnB']+t['nAB']); p('2024 d',R('0.7')*R('0.3'),TM)
# 2022-B4h: S 0,06, Z 0,12, P_Z(S) 0,10
SZ=R('0.12')*R('0.10'); t=tafel(R('0.12'),R('0.06'),SZ); p('2022 h',t)
p('2022 i',SZ/R('0.06'),N(t['AnB']/R('0.94'),4))
# 2022-A1.7b: A 0,5, B 0,4, A∩B 0,15
p('2022 A1.7b',R('0.5')+R('0.4')-2*R('0.15'))
# Mehr
DN=R('0.124')+R('0.035')-(1-R('0.854')); p('2018 e',DN,R('0.124')-DN,R('0.035')-DN)
p('2019 c',12500-2600-7700); p('2019 d',Rational(10000-7700,2600),N(Rational(2300,2600),4),Rational(10000,12500))
p('2026iqb a',tafel(R('0.35'),R('0.45'),R('0.15')))
t=tafel(R('0.68'),R('0.70'),R('0.70')-R('0.20')); p('2025iqb a',t, 'entweder G oder nicht J',t['AB']+t['nAnB'])
LD=R('0.6')+R('0.3')-(1-R('0.25')); p('2024iqb b',LD,R('0.6')-LD,R('0.3')-LD)
m2=symbols('m2'); p('2023iqb e',solve(Eq((1-R('0.02'))*m2,R('0.049')),m2))
p('2020iqb a',1-(R('0.15')+R('0.5')*R('0.7')))
