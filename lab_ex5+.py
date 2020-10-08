# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:04:43 2020

@author: student
"""
a = int(input())
for i in range(1, a):
    A = 0
    for x in range(1, i // 2 + 1):
        if i % x == 0:
            A += x
    if A == i:
        print(A)




