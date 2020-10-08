# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:15:32 2020

@author: student
"""
from math import sqrt

a, b, c = map(int, input().split())
D = b ** 2 - (4 * a* c)
if D < 0:
    print('Нет корней')
elif D == 0:
    print(-b / (2 * a))
else:
    print((-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a))