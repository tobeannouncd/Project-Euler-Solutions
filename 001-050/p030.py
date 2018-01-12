# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:39:49 2017

@author: tobeannouncd
"""

def digit_power_sum(num, power):
    s = (num % 10)**power
    while num > 9:
        num //= 10
        s += (num % 10)**power
    return s

p = 7
d = 1
while d * 9**p > 10**d:
    d += 1
    
su = 0
for i in range(2, d * 9**p):
    if i == digit_power_sum(i, p):
        print(i)
        su += i
        
print('sum: %d' % su)