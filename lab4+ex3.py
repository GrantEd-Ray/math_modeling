def picture(lens, S, F):
    total = 'Изображение: '
    if lens == 'собирающая':
        if S == F:
            total = 'Изображение: отсутствует'
        elif S < F:
            pic = 'мнимое, '
            pos = 'прямое, '
            size = 'увеличенное'
            total = total + pic + pos + size
        else:
            pic = 'действительное, '
            pos = 'обратное, '
            if S < 2 * F:
                size = 'увеличенное'
            elif S == 2 * F:
                size = 'равное'
            else:
                size = 'уменьшенное'
            total = total + pic + pos + size
    else:
        pic = 'мнимое, '
        pos = 'прямое, '
        size = 'уменьшенное'
        total = total + pic + pos + size
    return total

a = input('Линза: ')
b = int(input('Расстояние от линзы до предмета: '))
x = int(input('Фокусное расстояние: '))
print(picture(a, b, x))
