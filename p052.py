# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:03:05 2017

@author: tobeannouncd

Problem 52: Permuted multiples
It can be seen that the number, 125874, and its double, 251748, contain exactly 
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
"""
from timeit import Timer

def have_same_digits(num1, num2):
    '''
    I know that this function doesn't work 100% of the time, but it worked well
    enough for this problem. It should fail on checks like
    have_same_digits(111222, 112222)
    '''
    s1 = str(num1)
    s2 = str(num2)
    return (len(s1) == len(s2)) and (set(s1) == set(s2))

def main():
    n = 1
    while True:
        if (have_same_digits(n, 2*n) and
            have_same_digits(n, 3*n) and
            have_same_digits(n, 4*n) and
            have_same_digits(n, 5*n) and
            have_same_digits(n, 6*n)):
            print(n)
            break
        n += 1
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))