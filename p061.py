# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Cyclical figurate numbers
Problem 61 
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are 
all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	   P4,n=n2	 	       1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three 
interesting properties.

The set is cyclic, in that the last two digits of each number is the first two 
digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and 
pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which 
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and 
octagonal, is represented by a different number in the set.
"""
from timeit import Timer
from itertools import permutations as perm

def figurate_num_range(n, min_num, max_num):
    '''
    returns list of figurate numbers of order n in range(min_num, max_num)
    '''
    if n not in range(3,9):
        raise ValueError
        
    val_range = range(min_num, max_num)
    
    i = 1
    o = []
    if n == 3:
        while True:
            x = i*(i+1)/2
            if x in val_range:
                o.append(int(x))
            if x > max(val_range):
                break
            i += 1
    elif n == 4:
        while True:
            x = i**2
            if x in val_range:
                o.append(int(x))
            if x > max(val_range):
                break
            i += 1
    elif n == 5:
        while True:
            x = i*(3*i-1)/2
            if x in val_range:
                o.append(int(x))
            if x > max(val_range):
                break
            i += 1
    elif n == 6:
        while True:
            x = i*(2*i-1)
            if x in val_range:
                o.append(int(x))
            if x > max(val_range):
                break
            i += 1
    elif n == 7:
        while True:
            x = i*(5*i-3)/2
            if x in val_range:
                o.append(int(x))
            if x > max(val_range):
                break
            i += 1
    else:
        while True:
            x = i*(3*i-2)
            if x in val_range:
                o.append(int(x))
            if x > max(val_range):
                break
            i += 1
            
    return o

def fig_range_trim(fig_ranges):
    fig_pre_suf = [[],[]]
    for i in range(6):
        fig_pre_suf[0].append([num // 100 for num in fig_ranges[i]])
        fig_pre_suf[1].append([num % 100 for num in fig_ranges[i]])
        
    for i in range(6):
        fig_pre_suf[0][i] = [num for num in fig_pre_suf[0][i] if num in 
                    fig_pre_suf[1][i-1]]
        
    for i in range(5):
        fig_pre_suf[1][i] = fig_pre_suf[0][i+1]
    fig_pre_suf[1][5] = fig_pre_suf[0][0]
    
    for i in range(6):
        fig_ranges[i] = [num for num in fig_ranges[i] if num // 100 in 
                   fig_pre_suf[0][i] and num % 100 in fig_pre_suf[1][i]]
    
    for i in range(len(fig_ranges)):
        if len(fig_ranges[i]) == 0:
            return False
        if len(fig_ranges[i]) > 1:
            return fig_range_trim(fig_ranges)
    
    return fig_ranges

def main():
    fig_ranges = []
    for i in range(3,9):
        fig_ranges.append(figurate_num_range(i, 1000, 10000))
    
    for r in perm(fig_ranges):
        l = fig_range_trim(list(r))
        if l:
            l = [num[0] for num in l]
            print('{} + {} + {} + {} + {} + {} = {}'.format(l[0], l[1], l[2], 
                  l[3], l[4], l[5], sum(l)))
            break
    pass


if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

