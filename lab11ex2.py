import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.linspace(0, 5, frames)

def diff_func(z, t):
    x, y = z
    dxdt = (A - x - y) * k1
    dydt = (A - x - y) * k2
    return dxdt, dydt


A = 50
k1 = 0.65
k2 = 0.35

x0 = 0
y0 = 0
z0 = x0, y0

sol = odeint(diff_func, z0, t)
plt.plot(sol, 'b')

plt.show()