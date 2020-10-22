import numpy as np
import random as rn

n, m = map(int, input().split())
arr = np.zeros(m)
arr2 = np.zeros(shape=(n, m))

for (x, y), i in np.ndenumerate(arr2):
    arr2[x, y] = rn.randint(1, 1000)
    
print(arr2)

for (x, y), i in np.ndenumerate(arr2):
    a = 0
    for k in range(n):
        if arr2[k, y] > a:
            a = arr2[k, y]
    arr[y] = a
print(arr)