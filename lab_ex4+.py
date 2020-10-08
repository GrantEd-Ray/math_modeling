# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:02:32 2020

@author: student
"""

a = int(input())
while a > 1:
    for i in range(2, a + 1):
        if a % i == 0:
            a //= i
            print(i, end=' ')
            break


