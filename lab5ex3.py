from sympy import symbols
from sympy import sin
from sympy import Eq, solve, solveset

x = symbols('x')

expr = x**2 + x + 1/x + 1/x**2
a = Eq(expr, 4)
print(solve(a, x))

E = symbols('E')
e = 0.8
M = 9

expr = E - e * sin(E)
b = Eq(expr, M)
print(solveset(b, E))