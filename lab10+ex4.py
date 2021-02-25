import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0.0001, 1, 0.01)

def diff_func(a, x):
    y, w = a
    dydt = w
    dwdt = (-(x ** 2 - 0.5) * y - x * w) / x ** 2
    return dydt, dwdt


y0 = 3
w0 = 0
a0 = y0, w0

sol = odeint(diff_func, a0, x)

#plt.ylim(0, 1000)
plt.plot(x, sol[:, 0], 'b')

plt.show()