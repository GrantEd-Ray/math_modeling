from sympy import symbols
from sympy import sin, cos, exp

alp = symbols('alp')

expr_ch = (exp(alp) + exp(-alp)) / 2
expr_sh = (exp(alp) - exp(-alp)) / 2

a = int(input())
p, q = map(int, input().split())

x = a * expr_sh.subs(alp, p) / (expr_ch.subs(alp, p) - cos(q))
y = a * sin(p) / (expr_ch.subs(alp, p) - cos(q))
print(x.evalf())
print(y.evalf())