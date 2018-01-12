# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:42:17 2017

@author: tobeannouncd

Self powers

Problem 48 

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1*1 + 2*2 + 3*3 + ... + 1000*1000.
"""
from timeit import Timer

def main():
    su = 0
    for i in range(1, 1001):
        su += i**i % 10**10
        su %= 10**10
    print(su)
        
if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('{:.2f} ms'.format(1000*t.timeit(1)))