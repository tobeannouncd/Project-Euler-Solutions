# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:19:08 2017

@author: tobeannouncd

Problem 53: Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n! / r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are 
greater than one-million?
"""
from timeit import Timer

def nCr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = 1
    for i in range(n, n - r, -1):
        numer *= i
    denom = 1
    for i in range(1, r + 1):
        denom *= i
    
    return numer // denom

def main():
    count = 0
    for i in range(1, 101):
        for j in range(1, i + 1):
            if nCr(i,j) > 10**6:
                count += 1
    print(count)
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))