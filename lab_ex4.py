a = int(input())
x1 = 1
y = 0
for i in range(0, a + 1):
    x2 = x1 + y
    print(x2, end=' ')
    x1 = y
    y = x2