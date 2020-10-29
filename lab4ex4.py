def func(i, j):
    s = []
    for x in range(i + 1, j):
        y = x ** 2    #можете поменять на любую простую функцию
        s.append(y)
    return s

a, b = map(int, input().split())
print(func(a, b))