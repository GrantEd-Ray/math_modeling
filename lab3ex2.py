import lab3ex1 as phys
import numpy as np

h = 100
a = np.pi / 3
b = 30
beta = np.pi * b / 180
v1 = phys.g * h * np.power(np.tan(beta), 2)
v2 = 2 *np.power(np.cos(a), 2)
v3 = 1 - np.tan(beta) * np.tan(a)
v = np.sqrt(v1 / (v2 * v3))
print(v1, v2, v3, sep='\n')
print(v)