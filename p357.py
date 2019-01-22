# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Problem 357: Prime Generating Integers
"""
from time import clock
from Euler51 import prime_list


def euler_357(limit):
    is_prime = prime_list(limit + 1)
    
    def is_prime_gen(num):
        return all((num % d != 0 or is_prime[d + num//d]) for 
                   d in range(2, int(num**(1/2)) + 1))
    
    res = 1
    res += sum(n for n in range(2, limit + 1, 4) 
              if is_prime[n + 1] and is_prime_gen(n))
    
    return res


start_time = clock()
print(euler_357(10**8)) # limit is int > 1
print('Executed in {:.3G} seconds.'.format(clock() - start_time))