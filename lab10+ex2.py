import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0.01, 5, 0.0001)

def diff_func(a, x):
    y, w = a
    dydt = w
    dwdt = (w ** 2 - (3 * y ** 2) / x ** 0.5) / y
    return dydt, dwdt


y0 = 0.01
w0 = 1
a0 = y0, w0

sol = odeint(diff_func, a0, x)

plt.plot(x, sol[:, 0], 'b')

plt.show()