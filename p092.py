# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler
"""
from timeit import Timer
set1 = set()
set89 = set()

def sum_sq_digits(n):
    l = [int(c)**2 for c in str(n)]
    if sum(l) == 1 or sum(l) in set1:
        set1.add(n)
        return 1
    if sum(l) == 89 or sum(l) in set89:
        set89.add(n)
        return 89
    else:
        return sum_sq_digits(sum(l))

def main():
    count = 0
    for i in range(1,10**6):
        if sum_sq_digits(i) == 89:
            count += 1
    print(count)
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

