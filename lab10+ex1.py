import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(a, t):
    x, y, z = a
    dxdt = 3 * x - y + z
    dydt = x + y + z
    dzdt = 4 * x - y + 4 * z
    return dxdt, dydt, dzdt


x0 = -71
y0 = 1
z0 = -3
a0 = x0, y0, z0

sol = odeint(diff_func, a0, t)

plt.plot(sol, 'b')

plt.show()