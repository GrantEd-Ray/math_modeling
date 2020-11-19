from sympy import symbols
from sympy import sin, sqrt
from sympy import simplify, trigsimp

x, y, z, alp = symbols('x y z alp')

a = (x*y**2 - 2*x*y*z + x*z**2
 + y*2 - 2*y*z + z**2) / (x**2 - 1)

b = sqrt((1 + sin(alp)) / (1 - sin(alp))) + sqrt((1 - sin(alp)) / (1 + sin(alp)))

print(simplify(a))
print(trigsimp(b))