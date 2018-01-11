# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler
"""
from timeit import Timer
from Euler51 import prime_sieve
primes = prime_sieve(20)

def pe69(L):
    maxn = 1
    for p in primes:
        if maxn*p > L: return maxn
        maxn *= p
    return 'Not enough primes'


def main():
    print('The maximum  value of n/phi(n) for n <= 1,000,000 is {}'.format(pe69(10**6)))

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

