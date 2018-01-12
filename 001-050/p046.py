# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:23:48 2017

@author: tobeannouncd

Goldbach's other conjecture

Problem 46

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime 
and twice a square?
"""

from factor_functions import is_prime

def next_prime(prime):
    prime += 2
    while not is_prime(prime): prime += 2
    return prime

def main():
    notFound = True
    c = 33
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    while notFound:
        c += 2
        while is_prime(c): c += 2
        while c > primes[-1]: primes.append(next_prime(primes[-1]))
        for prime in primes[:-1]:
            i = ((c - prime)/2)**0.5
            if i == int(i): break
            if prime == primes[-2]: notFound = False
    print(c)

if __name__ == '__main__':
    import time
    
    t_beg = time.clock()
    main()
    t_end = time.clock()
    t_exec = t_end - t_beg
    
    print('Executed in', t_exec*1000, 'ms')