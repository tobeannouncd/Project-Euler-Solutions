# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:08:07 2017

@author: Tyler

Prime permutations

Problem 49 

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
"""

from timeit import Timer
from primes import list_primes, is_prime

def is_perm(x, y):
    x = sorted(list(str(x)))
    y = sorted(list(str(y)))
    return x == y

def main():
    P = list_primes(10**3, 10**4)
    for i in range(len(P) - 3):
        for j in range(i+1, len(P) - 2):
            if is_perm(P[i], P[j]):
                arith_const = P[j] - P[i]
                if (is_prime(P[j] + arith_const) and 
                    is_perm(P[j], P[j] + arith_const)):
                    print('{}{}{}'.format(P[i], P[j], P[j] + arith_const))
                        
if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('{:.2f} ms'.format(t.timeit(1)*1000))
