# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Problem 76

Counting Summations

How many ways can 
"""
from timeit import Timer

def main():
    target = 100
    ns = range(1, target)
    ways = [1] + [0]*target
    
    for n in ns:
        for i in range(n, target + 1):
            ways[i] += ways[i - n]
            
    print(ways[target])
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

