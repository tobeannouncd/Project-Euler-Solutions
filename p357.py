# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 19:11:57 2017

@author: Tyler
"""

def factors(num):
    out = []
    for i in range(1, num // 2 + 1):
        if num % i == 0: out.append(i)
    out.append(num)
    return out

def is_prime(num):
    return len(factors(num)) == 2

def is_prime_gen_int(num):
    f = factors(num)
    out = False
    for n in f[:len(f)//2]:
        if not is_prime(n + num // n): 
            out = False
            break
        out = True
    return out

s = 0
for i in range(1, 100000001):
    if is_prime_gen_int(i): s+=1
    
print(s)