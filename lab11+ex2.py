import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.arange(0, 20, 0.01)

def move_func(z, t):
    x, vx, y, vy = z
    dxdt = vx
    dvxdt = - mu * vx ** 2

    dydt = vy
    dvydt = -g + - mu * vy ** 2
    return dxdt, dvxdt, dydt, dvydt

a = 60
g = 9.8
v = 20
m = 50
mu = 0.5

x0 = 0
vx0 = v * np.cos(a * np.pi / 180)
y0 = 0
vy0 = v * np.sin(a * np.pi / 180)
z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)
plt.plot(sol[:, 0],sol[:, 2], 'b')
plt.ylim(0,10)

plt.show()