# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:12:13 2017

@author: Tyler
"""

from math import factorial

#print(factorial(100))

def sumDigits(n):
    s = 0
    while n >= 10:
        s += n % 10
        n //= 10
    
    s += n
        
    return s

#print(sumDigits(15))

print(sumDigits(factorial(100)))