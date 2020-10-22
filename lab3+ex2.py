import numpy as np
import random as rn

arr = np.zeros(5)

for i in range(4):
    arr[i] = rn.randint(1, 200)

print(arr)

a, x = map(int, input().split())

for i in range(4, x, -1):
    arr[i] = arr[i - 1]
arr[x] = a

print(arr)