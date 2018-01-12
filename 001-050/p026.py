# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:33:06 2017

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

def prime_factors(num):
    out = []
    for n in factors(num):
        if is_prime(n): out.append(n)
    return out

def relative_prime_factors(num, base):
    num_prime_factors = prime_factors(num)
    base_prime_factors = prime_factors(base)
    out = []
    for n in num_prime_factors:
        if n not in base_prime_factors: out.append(n)
    return out

def cross_product(l):
    o = 1
    for n in l:
        o *= n
    return o

#print(relative_prime_factors(10, 10))
#print(is_prime(6))
d = [[x, relative_prime_factors(x, 10)] for x in range(2,1000)]
d = [x for x in d if len(x[1]) > 0]
d = [[x[0], cross_product(x[1])] for x in d]

maxDigits = 0
maxRecur = 0

for i in d:
    digits = 1
    while True:
        if (10**digits - 1) % i[1] == 0: break
        digits += 1
    if digits >= maxDigits: 
        maxDigits = digits
        maxRecur = i[0]