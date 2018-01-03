# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Spiral primes
Problem 58 
Starting with 1 and spiralling anticlockwise in the following way, a square 
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right 
diagonal, but what is more interesting is that 8 out of the 13 numbers lying 
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral 
with side length 9 will be formed. If this process is continued, what is the 
side length of the square spiral for which the ratio of primes along both 
diagonals first falls below 10%?
"""
from timeit import Timer
from Euler51 import is_prime

def corner_values(l):
    """
    l
        side length, must be odd
    return
        list of values on corners 
    """
    corner_vals = [l**2]
    corner_vals.append(corner_vals[0] - (l - 1))
    corner_vals.append(corner_vals[1] - (l - 1))
    corner_vals.append(corner_vals[2] - (l - 1))
    return sorted(corner_vals)

def prime_count(l):
    """
    l
        list of values
    return
        number of values that are prime
    """
    c = 0
    for num in l:
        if is_prime(num):
            c += 1
    return c

def main():
    l = 7
    n_primes = 8
    n_diags = 13
    while n_primes / n_diags >= .10:
        l += 2
        n_primes += prime_count(corner_values(l))
        n_diags += 4
    print(l)
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))
