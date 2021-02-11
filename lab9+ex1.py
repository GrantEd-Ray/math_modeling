import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = 500 * 1000

x = np.arange(0, h, 10)

def falling(v, x):
    dvdh = G * M / (v * (R + h - x) ** 2)
    return dvdh

M = 5.97 * 10 ** 24
R = 6371 * 1000
G = 6.67 * 10 ** (-11)
v0 = 0.00000000000000001

solve_Bi = odeint(falling, v0, x)

plt.plot(x, solve_Bi[:,0])
plt.show()