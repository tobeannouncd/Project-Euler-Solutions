# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Convergents of e
Problem 65
"""
from timeit import Timer
#from math import gcd

def sum_converg_numer(l):
    numer, denom = l.pop(-1), 1
    while l:
        numer, denom = denom, numer
        numer += denom * l.pop(-1)
#        numer, denom = numer // gcd(numer, denom), denom // gcd(numer, denom)
#    print('Numerator is {}'.format(numer))
    numer = str(numer)
    
    s = 0
    for c in numer:
        s += int(c)
    
    return s
        
        

def main():
    #generate continued fraction for e
    e_cont = [2]
    k = 1
    while len(e_cont) < 100:
        e_cont.append(1)
        e_cont.append(2*k)
        e_cont.append(1)
        k += 1
    e_cont = e_cont[:100]
#    print(len(e_cont))
    
    print(sum_converg_numer(e_cont))
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

