# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:09:12 2017

@author: tobeannouncd

Distinct primes factors

Problem 47 

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors 
each. What is the first of these numbers?
"""
from factor_functions import prime_factors
import time

def main():
    i = 2*3*5*7
    consec = 0
    while consec < 4:
        if len(prime_factors(i)) == 4:
            consec += 1
        else:
            consec = 0
        i += 1
    
    print(i-4)

if __name__ == '__main__':
    t_begin = time.clock()
    main()
    t_exec = time.clock() - t_begin
    print('Execution time: {}ms'.format(int(t_exec*1000)))