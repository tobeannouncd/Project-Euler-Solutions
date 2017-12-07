# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:39:43 2017

@author: Tyler
"""
from math import factorial

digits = [0,1,2,3,4,5,6,7,8,9]
n_perm = 999999

for i in range(len(digits)-1):
    f = factorial(len(digits)-(i+1))
    if n_perm >= f:
        digits.insert(i,digits.pop(i + n_perm // f))
        n_perm %= f
        
print(digits)