import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-0.99999, 1, 0.01)
n = int(input('n = '))

def diff_func(a, x):
    y, w = a
    dydt = w
    dwdt = (3 * x * dydt - n * (n + 2) * y) / (1 - x ** 2)
    return dydt, dwdt


y0 = 3
w0 = 0
a0 = y0, w0

sol = odeint(diff_func, a0, x)

plt.plot(x, sol[:, 0], 'b')

plt.show()