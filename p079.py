# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler
Problem 79
"""
from timeit import Timer

def main():
    filename = 'p079_keylog.txt'
    
    with open(filename) as f:
        keys = [key.strip() for key in f.readlines()]
        
#    keys.sort()
    digits = set()
    for key in keys:
        digits.update(int(c) for c in key)
    digits_after = {i: set() for i in digits}
    for key in keys:
        n = [int(c) for c in key]
        digits_after[n[0]].update(n[1:])
        digits_after[n[1]].update(n[2:])
        
    print(digits_after)
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

