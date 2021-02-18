import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.1)

def diff_func(a, t):
    y, z = a
    dy_dx = y ** 2 * z
    dz_dx  = z / t - y * z ** 2
    return dy_dx, dz_dx


y0 = 1
z0 = -3
a0 = y0, z0

sol = odeint(diff_func, a0, t)

plt.plot(t, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.show()