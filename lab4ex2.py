import random as rn
import numpy as np

def average(s):
  x = 1
  for i in s:
      x *= i
  return x

m = np.zeros(int(input()))
for (i), x in np.ndenumerate(m):
    m[i] = rn.randint(1, 500)
print(m)
print(average(m))

