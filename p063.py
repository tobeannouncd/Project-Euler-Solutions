# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Powerful digit counts
Problem 63 
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit 
number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from timeit import Timer

def power_digits(num, power):
    return len(str(num**power)) == power

def main():
    count = 0
    for j in range(1,1000):
        for i in range(1,10):
            if power_digits(i,j):
                count += 1
            
    print(count)
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

