import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def diff_func(z, t):
    T1, T2 = z
    dT1dt = a1 * (Tg - T1) + a2 * (Te - T1) + a3 * (T2 - T1) + 30
    dT2dt = a3 * (T1 - T2) + a2 * (Te - T2)
    return dT1dt, dT2dt


a1 = 1.3
a2 = 1.5
a3 = 1.8
Tg = 7
Te = 5

T10 = 15
T20 = 20
z0 = T10, T20

sol = odeint(diff_func, z0, t)
plt.plot(t, sol)

plt.show()
