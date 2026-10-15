from sympy import *
x,u=symbols('x u',real=True)
def p(*a): print(*a)
# B1 2026-B2.2g
k=55*exp(-x/300)+18; p('k(0)',k.subs(x,0))
# B2 2025-A1.4a
f=2*exp(x)-2*exp(-1); p('f(-1)',simplify(f.subs(x,-1)), 'f(1)~',N(f.subs(x,1)),'asym',N(-2*exp(-1)))
# B3 2022-A1.1a
f=x**3-10*x**2+21*x; p('NS',solve(f,x), factor(f))
# B4 2023-B2.2a
f=x**3-9*x**2+24*x-16; p('fakt',factor(f), expand((x-4)*(x**2-5*x+4))==f, 'f0',f.subs(x,0), solve(f,x))
# B5 2024-B2.2b
f=Rational(1,2)*x**4-3*x**2+Rational(5,2); p('f(1)',f.subs(x,1),'f(-x)=f',simplify(f.subs(x,-x)-f)==0, solve(f,x), solve(Rational(1,2)*u**2-3*u+Rational(5,2),u))
# B6 2026-B2.2a
f=2*exp(x)+3; p('min', limit(f,x,-oo))
# B7 2024-B2.1a
f=(x-3)*exp(-x/3+2); fp=simplify(diff(f,x)); p('fp',fp, simplify(fp-(2-x/3)*exp(-x/3+2))==0, solve(f,x), f.subs(x,0), N(f.subs(x,0),4))
# B8 2022-B2.1a
f=(x+3)*exp(-x); fp=diff(f,x); p(simplify(fp+(x+2)*exp(-x))==0, solve(f,x), f.subs(x,0), solve(fp,x), f.subs(x,-2), N(exp(2),4), 'vz', fp.subs(x,-3)>0, fp.subs(x,-1)<0)
# B9 2023-B2.1b
f=Rational(1,2)*(x**2-9)*exp(x); fp=diff(f,x); p(simplify(fp-(Rational(1,2)*x**2+x-Rational(9,2))*exp(x))==0, solve(f,x), f.subs(x,0))
# Mehr
pp=-x**2+Rational(19,5)*x-Rational(48,25); p('M1',pp.subs(x,Rational(3,5)),pp.subs(x,Rational(16,5)))
f=x**3/8-x**2+2*x; p('M2',factor(f),solve(f,x))
f=(-x**2/5+3*x)*exp(-x/5); p('M3',solve(f,x), f.subs(x,0))
f=(8*x-2)*exp(-x); p('M4',solve(f,x), f.subs(x,0))
f=-Rational(2,100)*(x-6)*(x+2)**2; p('M5',solve(f,x))
f=(x**2-4*x+4)*exp(-x); p('M6',solve(f,x), f.subs(x,0))
h=-Rational(1,5)*x**4+30*x**2; p('M7',h.subs(x,2),h.subs(x,5), N(h.subs(x,2)))
f=x**3-3*x**2; p('M8',solve(f,x),factor(f))
f=x**5/60-x**3/4+2*x; p('M9',f.subs(x,0))
g=-450*exp(-Rational(2,5)*x)+950; p('M10',g.subs(x,0))
