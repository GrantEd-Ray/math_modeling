import numpy as np
import matplotlib.pyplot as plt

def cycloida(R):
    t = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    
    plt.plot(x, y, ls='--', lw=3)
    
    plt.axis('equal')
    
    plt.show()

def astroida(R):
    t = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    
    x = R * np.cos(t) ** 3
    y = R * np.sin(t) ** 3
    
    plt.plot(x, y, ls='--', lw=3)
    
    plt.axis('exual')
    
    plt.show()
    

n = input()
if n == 'циклоида':
    R = int(input())
    cycloida(R)
elif n == 'астроида':
    R = int(input())
    astroida(R)
else:
    print('Try again!')