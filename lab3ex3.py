import lab3ex1 as phys
import numpy as np

x0, y0, v0 = map(int, input().split())
for t in range(0, 6):
    x = x0 + v0 * t
    y = y0 + v0 * t - phys.g * np.power(t, 2) / 2
    listed = []
    listed.append(t)
    listed.append(x)
    listed.append(y)
    print(listed)


