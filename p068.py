# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler
"""
from timeit import Timer
from itertools import permutations

def is_magic_5_gon(s):
    if s[5] != min(s[5:]):
        return False
    out = []
    for i in range(4):
        out.append(s[i] + s[i + 1] + s[i + 5])
    out.append(s[0] + s[4] + s[9])
    if len(set(out)) != 1:
        return False
    return True

def magic_5_gon_str(s):
    st = ''
    for i in range(4):
        st += str(s[i + 5]) + str(s[i]) + str(s[i + 1])
    st += str(s[9]) + str(s[4]) + str(s[0])
    return st

def main():
    #count = 0
    magic_5_gons = []
    for perm in permutations(range(1,11)):
        if is_magic_5_gon(perm):
    #        count += 1
            magic_5_gons.append(perm)
    
    #print(count)
#    print(len(magic_5_gons))
            
    max_concat = ''
    for gon in magic_5_gons:
        st = magic_5_gon_str(gon)
        if len(st) != 16:
            continue
        if st > max_concat:
            max_concat = st
    
    print(max_concat)
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

