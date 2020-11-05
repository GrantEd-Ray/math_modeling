def fib(n):
    y = 0
    if n > 0:
        x1 = 1
        for i in range(2, n + 1):
            x2 = x1 + y
            y = x1
            x1 = x2
    if n < 0:
        x1 = 1
        for i in range(-2, n - 1, -1):
            x2 = y - x1
            y = x1
            x1 = x2
    return x2

x = int(input())
print(fib(x))