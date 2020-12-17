import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

butterfly, = plt.plot([], [], '-', lw=2)

x, y = [],[]

def draw(t):
    x.append( np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5))
    y.append( np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5))
    return x, y

plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def animate(i):
    butterfly.set_data(draw(t=i))

ani = FuncAnimation(fig,
                    animate,
                    frames=np.arange(0, 12 * np.pi, 0.05),
                    interval=30
                    )

ani.save('lec_7_complex_animation_2.gif')