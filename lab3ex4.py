import lab3ex1 as phys
import numpy as np

N = 3
M = 8
s = np.zeros(shape=(N, M))

for (i,j) , x in np.ndenumerate(s):
    s[i, j] = np.sin(N * (i + 1) + M * (j + 1))
    print(i, j, x)
    if s[i, j] < 0:
        s[i, j] = 0
print(s)

