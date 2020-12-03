import matplotlib.pyplot as plt
import numpy as np

#from sympy import symbols
#from sympy import exp, sin, cos

#r = symbols('r')

def logspi(b):
    f = np.arange(0, 8 * np.pi, 0.01)
    
    r = np.exp(b * f)
        
    rx = r * np.cos(f)
    ry = r * np.sin(f)
    plt.plot(rx, ry)
    plt.axis('equal')
    plt.show()
    
def archspi(k):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = k * f
    
    rx = r * np.cos(f)
    ry = r * np.sin(f)
    plt.plot(rx, ry)
    plt.axis('equal')
    plt.show()
    
def wand(k):
    f = np.arange(0.01, 8 * np.pi, 0.01)
    
    r = k / f ** 0.5
    
    rx = r * np.cos(f)
    ry = r * np.sin(f)
    plt.plot(rx, ry)
    plt.axis('equal')
    plt.show()
    
def rose(k):
    f = np.arange(0.01, 8 * np.pi, 0.01)
    
    r = np.sin(k * f)
    
    rx = r * np.cos(f)
    ry = r * np.sin(f)
    plt.plot(rx, ry)
    plt.axis('equal')
    plt.show()
    
    
print('1: логарифмическая спираль', '2: архимедова спираль', '3: спираль "жезл"', '4: роза', sep='\n')
x = int(input())
if x == 1:
    logspi(float(input()))
elif x == 2:
    archspi(float(input()))
elif x == 3:
    wand(float(input()))
elif x == 4:
    rose(float(input()))
else:
    print('ИДИОТ!!!')