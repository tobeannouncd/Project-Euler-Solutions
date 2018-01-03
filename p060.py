# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:11:57 2018

@author: tobeannouncd

Prime pair sets
Problem 60 
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
and concatenating them in any order the result will always be prime. For 
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
primes, 792, represents the lowest sum for a set of four primes with this 
property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
"""
from timeit import Timer
from Euler51 import prime_sieve, is_prime
from itertools import permutations as perm
prime_max = 10**4
set_size = 5
primes = [prime for prime in prime_sieve(prime_max) if prime > 2]

def all_prime(chain):
    return all(is_prime(str(p[0]) + str(p[1])) for p in perm(chain, 2))

def make_chain(chain):
    if len(chain) == set_size:
        return chain
    for p in primes:
        if p > chain[-1] and all_prime(chain + [p]):
            newchain = make_chain(chain + [p])
            if newchain:
                return newchain
    return False
        
def main():
    chain = 0
    while not chain:
        chain = make_chain([primes.pop(0)])
    print('{} + {} + {} + {} + {} = {}'.format(chain[0], chain[1], chain[2], 
          chain[3], chain[4], sum(chain)))
    pass
    
if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))
