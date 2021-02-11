import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1000, 0.1)

def advence(F, t):
    dfdt = (b - k * F) / m
    return dfdt


m = 1000
b = 20
k = 5
f0 = 0

solve_Bi = odeint(advence, f0, t)

plt.plot(t, solve_Bi[:,0], label='Тяга')
plt.xlabel('Время, секунды')
plt.ylabel('Тяга')
plt.title('ТЯга')
plt.legend()

plt.show()
