# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:27:15 2020

@author: student
"""
a, b, c = map(int, input().split())
if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b == c:
        print('равносторонний')
    elif a == b != c or a == c != b or b == c != a:
        print('равнобедренный')
    else:
        print('разносторонний')
else:
    print('не существует')
