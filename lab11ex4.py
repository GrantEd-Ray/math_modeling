import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.1)

def diff_func(z, t):
    m, v, y = z
    dmdt = - w
    dvdt = - g + u * w / m
    dydt = v
    return dmdt, dvdt, dydt


m0 = 250 * 10 ** 3
g = 9.8
v0 = 0
y0 = 0
u = 3000
w = 1000
z0 = m0, v0, y0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1], 'b')

plt.show()