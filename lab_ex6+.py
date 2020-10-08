# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:26:12 2020

@author: student
"""
a, b = input().split(', ')
a = int(a)
if 'до' in b:
    x = (776 - a) // 4 + 1
    y = (776 - a) % 4 + 1
else:
    x = (776 + a) // 4 + 1
    y = (776 + a) % 4 + 1
print('OL', ' ', x, '.',  y, sep='')
