# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:53:37 2017

@author: tobeannouncd

Consecutive prime sum
Problem 50 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""

from primes import list_primes
from timeit import Timer

def main():
    P = list_primes(2,10**6)
    n_max = 21      # data given from problem
    p_n_max = 953   # data given from problem
    i = 0
    while i < len(P) - n_max:
        s = sum(P[i:i+n_max])
        for j in range(i+n_max, len(P)):
            s += P[j]
            if s > P[-1]:
                break
            if s in P:
                n_max = j - i + 1
                p_n_max = s
#                p_n_primes = P[i:j+1]
        i += 1
    print('{} is the sum of {} consecutive primes'.format(p_n_max, n_max))
#    print('The primes are {}'.format(p_n_primes))
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    t_main = t.timeit(1)
    if t_main < 1:
        print('{:.2f} ms'.format(1000*t_main))
    else:
        print('{:.2f} s'.format(t_main))
