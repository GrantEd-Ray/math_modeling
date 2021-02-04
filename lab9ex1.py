import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.1)

def advence(m, t):
    dmdt = k * m
    return dmdt

m = 2
k = 2

solve_Bi = odeint(advence, m, t)

plt.plot(t, solve_Bi[:,0], label='Размножение бактерий')
plt.xlabel('Период размножения, часы')
plt.ylabel('Функция размножения')
plt.title('Размножение бактерий')
plt.legend()

plt.show()