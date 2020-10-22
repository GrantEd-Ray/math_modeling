import numpy as np
import random as rn

n, m = map(int, input().split())
arr = np.zeros(shape=(n, m))
my_arr = np.zeros(shape=(n, m))
my_arr2 = np.zeros(shape=(n, m))

for (x, y), i in np.ndenumerate(my_arr):
    my_arr[x, y] = rn.randint(1, 1000)

for (x, y), i in np.ndenumerate(my_arr2):
    my_arr2[x, y] = rn.randint(1, 1000)
    
for (x, y), i in np.ndenumerate(arr):
    arr[x, y] = max(my_arr[x, y], my_arr2[x, y])

print(my_arr)
print(my_arr2)
print(arr)
