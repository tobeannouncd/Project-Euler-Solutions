# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Powerful digit sum
Problem 56 

A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the 
maximum digital sum?
"""
from timeit import Timer

def main():
    out = max([sum([int(digit) for digit in str(a ** b)]) for 
               a in range(1,100) for b in range(1,100)])
    print('The maximum digital sum is {}.'.format(out))
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))
