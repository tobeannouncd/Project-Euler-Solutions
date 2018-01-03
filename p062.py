# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler
"""
from timeit import Timer

def main():
    cubes = {}
    min_cube = 0
    n = 100
    target = 5
    while min_cube == 0:
        c = n**3
        digits = ''.join(sorted(str(c)))
        if digits in cubes:
            cubes[digits] += [c]
            if len(cubes[digits]) == target:
                min_cube = cubes[digits][0]
        else:
            cubes[digits] = [c]
        n += 1
            
    print(min_cube)
    
    pass
    
if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

