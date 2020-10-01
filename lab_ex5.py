a = int(input())
b = int(input())
if b == 0:
    print('Ошибка!')
else:
    if a % b == 0:
        print(a // b)
    else:
        print(a // b, 'остаток', a % b)
