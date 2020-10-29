import numpy as np
import random as rn

def tri(a, b, y):
    S = a * b * np.sin(np.radians(y)) / 2
    return S

def circle(a):
    S = np.pi * a ** 2
    return S

def quadra(a, b):
    S = a * b
    return S

shape = input()
if shape == 'круг':
    r = int(input())
    print(circle(r))
elif shape == 'прямоугольник':
    x, y = map(int, input().split())
    print(quadra(x, y))
else:
    a, b, alp = map(int, input().split())
    print(tri(a, b, alp))