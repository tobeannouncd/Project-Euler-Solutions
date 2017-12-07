# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:11:08 2017

@author: Tyler

Project Euler Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

# Check for pattern

def isCurious(num):
    from math import factorial
    num_list = [int(c) for c in str(num)]
    s = 0
    for i in num_list:
        s += factorial(i)
    return s == num

def main():
    i_max = 2540160
    for i in range(3,i_max):
        if isCurious(i): print(i)
    pass

if __name__ == '__main__': main()