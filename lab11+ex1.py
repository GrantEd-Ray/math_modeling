import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.1)

def diff_func(z, t):
    a, b, c = z
    dadt = - a * k1
    dbdt = - b * k2 + a * k1
    dcdt = - c * k3 + b * k2
    return dadt, dbdt, dcdt

#A = 500
k1 = 0.5
k2 = 0.61
k3 = 0.27

a0 = 500
b0 = 0
c0 = 0
z0 = a0, b0, c0

sol = odeint(diff_func, z0, t)
plt.plot(sol)

plt.show()