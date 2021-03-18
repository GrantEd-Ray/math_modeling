import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def diff_func(z, t):
    v, y = z
    dvdt = (y / L) * g
    dydt = v
    return dvdt, dydt


L = 2.5
g = 9.8

v0 = 0
y0 = 0.1
z0 = v0, y0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1])

plt.ylim(0, L)
plt.show()
