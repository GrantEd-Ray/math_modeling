import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 50, 0.1)

def radius(s, t):
    a = (np.pi / 12) * (t - 12)
    dsdt = -k * np.sqrt(s / np.pi) * E * s * np.cos(a)
    return dsdt


E = 1367
s0 = 1600
k = 400 * 10 ** (-8)

solve_Bi = odeint(radius, s0, t)

plt.plot(t, solve_Bi[:,0])

plt.show()