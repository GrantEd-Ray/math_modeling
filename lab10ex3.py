import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.1)

def diff_func(z, t):
    y, w = z
    dy_dt = w
    d0dt = np.sin(t) + np.cos(t)
    return dy_dt, d0dt


y0 = 3
w0 = 0
z0 = y0, w0

sol = odeint(diff_func, z0, t)

#plt.plot(t, sol[:, 1], 'b', label='theta(t)')
plt.plot(sol[:, 1], sol[:, 0], 'b', label='theta(t)')

plt.legend()
plt.show()