import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.01)

def diff_func(z, t):
    y, w = z
    dydt = w
    dwdt = -4 * w - 5 * y
    return dydt, dwdt


y0 = 4
w0 = -1
z0 = y0, w0

sol = odeint(diff_func, z0, t)

plt.plot(sol[:, 1], sol[:, 0], 'b', label='theta(t)')

plt.legend()
plt.show()