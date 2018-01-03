# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Diophantine equation
Problem 66
"""
from timeit import Timer

def pell(D):
    """
    returns x, y where x and y are the minimum integer solutions of 
    x**2 - D*y**2 == 1
    """
    m = 0
    d = 1
    a = a0 = int(D ** (1/2))
    
    hm1 = 1
    h = a0
    km1 = 0
    k = 1
    
    while h ** 2 - D * (k ** 2) != 1:
        m = d * a - m
        d = (D - m ** 2) // d
        a = (a0 + m) // d
        
        hm1, h = h, a * h + hm1
        km1, k = k, a * k + km1
    
    return h, k

def main():
    x_max = y_max = D_max = 0
    
    for D in range(2, 1001):
        sqrt_D =  int(D ** (1 / 2))
        if D == sqrt_D ** 2:
            continue
        
        x, y = pell(D)
        if x > x_max:
            x_max, y_max, D_max = x, y, D
    
    print(D_max)
    
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

