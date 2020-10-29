import random as rn

def average(s):
  x = sum(s) / len(s)
  return x

m = []
for i in range(rn.randint(1, 100)):
  m.append(rn.randint(1, 100))
print(m)
print(average(m))
