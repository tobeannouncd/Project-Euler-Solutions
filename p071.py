# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Problem 71

Ordered Fractions

NOTE: This code does not really work. I just used it as a scratchpad for 
coming up with the answer analytically. This problem doesn't need programming.
"""
from timeit import Timer

def main():
    frac = 3/7
#    res = []
    minval = float('Inf')
    
    for i in range(1,10**6 + 1):
        if i % 7 == 0:
            continue
        f = frac * i - int(frac * i)
        if 
    print(min(res))
    input()
# =============================================================================
#     for i in range(len(res)):
#         if res[i] == minval:
#             print(i+1)
# =============================================================================
    
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

