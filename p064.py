# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler
"""
from timeit import Timer

def cont_frac(num):
    cf = [int(num**(1/2))]
    m = [0]
    d = [1]
    i = 0
    while cf[-1] != 2*cf[0]:
        m.append(d[i]*cf[i] - m[i])
        d.append((num - m[i+1]**2) // d[i])
        cf.append((cf[0] + m[i+1]) // d[i+1])
        i += 1
    
    
    return cf

def main():
    not_squares = list(range(1,10001))
    i = 1
    while i**2 <= 10000:
        not_squares.remove(i**2)
        i += 1
    c = 0
    for num in not_squares:
        if len(cont_frac(num)) % 2 == 0:
            c += 1
    print('There are {} continued fractions with an odd period'.format(c))
    print(cont_frac(14))
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

