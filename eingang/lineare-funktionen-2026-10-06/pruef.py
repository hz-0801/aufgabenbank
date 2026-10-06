"""Rechenprobe aller Lösungen des Blatts lineare-funktionen 2026-10-06 (sympy)."""
from sympy import Rational as R, symbols, solve, Eq, nsimplify, ceiling, sympify
x = symbols('x')
fehler = 0
n = 0
def ok(name, ist, soll):
    global fehler, n
    n += 1
    if sympify(ist) - sympify(soll) != 0:
        fehler += 1
        print('FEHLER', name, ist, '!=', soll)
def gerade(A, B):
    m = R(B[1] - A[1]) / R(B[0] - A[0]) if not isinstance(A[0], float) else nsimplify((B[1]-A[1])/(B[0]-A[0]))
    return m, nsimplify(A[1]) - m * nsimplify(A[0])
def null(m, b, w=0):
    return solve(Eq(nsimplify(m)*x + nsimplify(b), nsimplify(w)), x)[0]
def schnitt(m1, b1, m2, b2):
    xs = solve(Eq(nsimplify(m1)*x+nsimplify(b1), nsimplify(m2)*x+nsimplify(b2)), x)[0]
    return xs, nsimplify(m1)*xs+nsimplify(b1)
# Blatt 0
for nm, a, s in [('1a',(-3)*4,-12),('1b',R(-20,5),-4),('1c',R(-3,2)*(-4),6),('1d',-4*(-2)+1,9),
                 ('2a',R(1,2)*8,4),('2b',R(-3,4)*8,-6),('2c',R(1,2)*(-6),-3),('2d',R(-2,5)*(-5),2)]:
    ok(nm, a, s)
for nm, m, b, s in [('3a',2,-8,4),('3b',-4,12,3),('3c',-0.2,6,30),('3d',-3,-6,-2)]:
    ok(nm, null(m, b), s)
ok('4a', 3*x+4*x, 7*x); ok('4b', 2*x+5-4*x+1, -2*x+6); ok('4c', 7-3*x-2*x, -5*x+7)
ok('4d', R(3,2)*x-4-R(5,2)*x, -x-4)
# 5: zweiter Punkt nach Steigungsdreieck
for nm, m, b, P in [('5a',2,4,(1,6)),('5b',4,3,(1,7)),('5c',-1,3,(1,2)),('5d',R(1,2),3,(2,4)),
                    ('5e',3,-5,(1,-2)),('5f',R(-2,3),-1,(3,-3)),('5g',-4,3,(1,-1))]:
    ok(nm, m*P[0]+b, P[1])
# 6: Geraden p 3x-2, q -2x+4, r x/3+1 (Grafik) – abgelesen
ok('6a', 4, 4); ok('6b', -2, -2); ok('6c', 3, 3); ok('6d', -2, -2); ok('6e', R(1,3), R(1,3))
# 7a parallel: m gleich
ok('7a', 4-4, 0)
# 8
for nm, m, b, xv, s in [('8a',2,5,4,13),('8b',3,-4,5,11),('8c',-2,5,-4,13),('8d',10,-4,R(3,10),-1),
                        ('8e',R(-2,5),3,-5,5),('8f',R(1,3),-2,-9,-5)]:
    ok(nm, m*xv+b, s)
# 9
for nm, m, b, w, s in [('9a',2,3,11,4),('9b',-3,5,-10,5),('9c',R(1,2),2,6,8),('9d',3,-12,0,4),
                       ('9e',-2,12,0,6),('9f',4,6,0,R(-3,2)),('9g',R(-2,5),60,0,150)]:
    ok(nm, null(m, b, w), s)
# 10: Funktionswerte
ok('10a', 3*3-1, 8); ok('10b', -4*(-2)-2, 6); ok('10c', -5+6, 1); ok('10d', R(-3,2)*(-2)-1, 2)
ok('10e', sum(1 for xv,yv in ((-1,8),(2,-10),(-3,16)) if -6*xv+2 != yv), 1)
ok('10e2', -6*(-3)+2, 20)
# 11
for v, w in zip((-1,0,1,2,3),(10,7,4,1,-2)): ok('11a', -3*v+7, w)
ok('11c', nsimplify('-0.06')*700+45, 3)
# 12
for nm, A, B, s in [('12c',(0,4),(2,10),(3,4)),('12d',(2,1),(4,9),(4,-7)),('12e',(-2,9),(2,1),(-2,5)),
                    ('12f',(-3,1),(3,5),(R(2,3),3)),('12g',(-2,-3),(4,6),(R(3,2),0)),
                    ('12h',(10,800),(40,440),(-12,920)),('13a',(-1,-5),(3,3),(2,-3)),
                    ('13b',(-2,8),(4,-1),(R(-3,2),5)),('15c',(3,R(19,10)),(8,R(22,5)),(R(1,2),R(2,5))),
                    ('18b',(1,5),(3,-1),(-3,8))]:
    m, b = gerade(A, B); ok(nm+'m', m, s[0]); ok(nm+'n', b, s[1])
ok('12a', 7-2*4, -1); ok('12b', 1-(-3)*2, 7)
# 14
for nm, g, s in [('14a',(3,-4,-1,8),(3,5)),('14b',(2,5,-3,-10),(-3,-1)),('14c',(R(1,2),4,2,-2),(4,6)),
                 ('14d',(4,-3,-2,6),(R(3,2),3)),('14e',(R(-3,2),5,1,0),(2,2)),('18d',(1,3,-2,9),(2,5))]:
    xs, ys = schnitt(*g); ok(nm+'x', xs, s[0]); ok(nm+'y', ys, s[1])
ok('15a', -2*1+7, 5)
# 16
ok('16c', R(42,10)-8*R(15,100), 3)
ok('16dA', 20+R(3,10)*60, 38); ok('16dB', R(7,10)*60, 42)
ok('16f', ceiling(R(1500-640,45)), 20)
ok('16gA', 4*32+(420-300)*R(3,10), 164); ok('16gB', 95+420*R(12,100), R(14540,100))
# 17a: I startet bei 30 (Hoch), II durch Ursprung (Weit)
ok('17a', 5*0+30, 30)
# 18
ok('18a', -3*(-2)+1, 7); ok('18e', 20+12*8, 116)
ok('18f', R(-2,3)*(-6)-3, 1); ok('18g', ceiling(R(1000-380,45)), 14)
print(f'{n} Proben, {fehler} Fehler')
