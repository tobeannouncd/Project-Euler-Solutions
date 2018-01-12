# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:32:21 2017

@author: tobeannouncd
"""

def factors(num):
    out = []
    for i in range(1, num // 2 + 1):
        if num % i == 0: out.append(i)
    out.append(num)
    return out

def is_prime(n):
    '''
    n: int
    
    return: True if n is prime, False otherwise
    '''
    if n == 2 or n == 3: return True
    if n%2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return False
    return True

def prime_factors(n):
    '''
    n: int
    
    return: list of prime factors
    '''
    o = []
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            o.append(i)
    if n > 1:
        o.append(n)
    return list(set(o))

def main():
    pass
    
if __name__ == '__main__': main()