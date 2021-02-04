import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 0.1)

def advence(v, t):
    f = v ** 2 * y
    dvdt = a0 - f / m
    return dvdt

m = 1000
a0 = 9.8
v0 = 0
y = 0.2

solve_Bi = odeint(advence, v0, t)

plt.plot(t, solve_Bi[:,0], label='Скорость падения')
plt.xlabel('Период падения, секунды')
plt.ylabel('Функция падения')
plt.title('Падение')
plt.legend()

plt.show()