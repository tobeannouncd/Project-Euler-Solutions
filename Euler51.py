# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:58:52 2017

@author: Tyler

Primes_051.py

Useful functions involving prime numbers
"""

def is_prime(num):
    '''
    num: int
    
    returns: True if num is prime, False otherwise
    '''
    if type(num) == str or type(num) == float:
        num = int(num)
        
    if num < 2 or num % 2 == 0:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    '''
    num: int
    
    returns: int, next prime number greater than num
    '''
    if type(num) == float:
        if num.is_integer():
            num = int(num)
        else:
            raise ValueError('not an integer')
    if type(num) != int:
        raise TypeError('not an integer')
        
    num += 1
    if num % 2 == 0:
        if num == 2:
            return num
        num += 1
    while not is_prime(num):
        num += 2
    return num

def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

