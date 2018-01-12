# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:52:45 2017

@author: tobeannouncd
"""
def factors(num):
    out = []
    for i in range(1, num // 2 + 1):
        if num % i == 0: out.append(i)
    out.append(num)
    return out

def is_prime(num):
    return len(factors(num)) == 2

def quadra(a, b, n):
    return n**2 + a*n + b

max_n = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        while True:
            if not is_prime(quadra(a,b,n)): break
            n += 1
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b
            
print(max_a*max_b)