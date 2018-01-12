# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:34:03 2017

@author: tobeannouncd

Project Euler problem 35: circular primes

The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
73, 79, and 97.

How many circular primes are there below one million?
"""
def rotations(n):
    out = []
    n_list = list(str(n))
    
    if len(n_list) == 1:
        return [n]
    for i in range(len(n_list)):
        out.append(int(''.join(n_list[i:] + n_list[:i])))
    return out

def is_circ_prime_candidate(n):
    from factor_functions import is_prime
    
    if not is_prime(n): return False
    
    n_l = list(str(n))
    if len(n_l) == 1: return True
    for c in n_l:
        if c not in ('1', '3', '7', '9'): return False
    return True
    
def main():
    prime_max = 10**6
    candidates = [x for x in range(2,prime_max) if is_circ_prime_candidate(x)]
    
    circ_primes = []
    for prime in candidates:
        fl = True
        for rotation in rotations(prime):
            if rotation not in candidates:
                fl = False
                break
        if fl: circ_primes.append(prime)
    print(len(circ_primes))
    pass

if __name__ == '__main__': main()