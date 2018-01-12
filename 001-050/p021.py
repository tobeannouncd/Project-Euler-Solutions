# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:23:20 2017

@author: tobeannouncd
"""

def sumDivisors(n):
    s = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            s += i
    return s

def isAmicable(n):
    if sumDivisors(n) == n:    #perfect numbers aren't amicable
        return False    
    elif sumDivisors(sumDivisors(n)) == n:
        return True
    else:
        return False
    
s = 0
for i in range(1,10000):
    if isAmicable(i):
        s += i
        
print(s)


