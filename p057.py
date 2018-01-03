# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Square root convergents
Problem 57 
It is possible to show that the square root of two can be expressed as an 
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth 
expansion, 1393/985, is the first example where the number of digits in the 
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator 
with more digits than denominator?
"""
from timeit import Timer

def cont_frac(n):
    '''
    n
        number of iterations
    return
        result of continued fraction of form 1 + 1/(2 + 1/(2 + 1/(2 + ...))) after
        *i* iterations as tuple of numerator and denominator (numer, denom)
    notes
        resultant fraction shouldn't need reducing?
    '''
    numer = 1
    denom = 2
    for i in range(n - 1):
        numer += 2 * denom
        numer, denom = denom, numer
    numer += denom
    return numer, denom

def main():
    c = 0
    for i in range(1,1001):
        n, d = cont_frac(i)
        if len(str(n)) > len(str(d)):
            c += 1
    print('c = {}'.format(c))
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))
