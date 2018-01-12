# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:08:46 2017

@author: tobeannouncd
"""
        
def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return False
    return True
    
def list_primes(low, high):
    '''
    low, high: int
    
    return: list of primes in range(low, high)
    '''
    o = []
    for i in range(low, high):
        if is_prime(i): o.append(i)
    return o
    