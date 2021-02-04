import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def advence(m, t):
    dmdt = -k * m * t
    return dmdt

m = 1000
k = 0.08

solve_Bi = odeint(advence, m, t)

plt.plot(t, solve_Bi[:,0], label='Инвестиции')
plt.xlabel('Период работы, годы')
plt.ylabel('Функция падения')
plt.title('Инвестиции')
plt.legend()

plt.show()