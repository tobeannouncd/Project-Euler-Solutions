# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:01:02 2017

@author: tobeannouncd
"""

def pythag_triples(m):
    '''
    m: maximum perimeter
    
    output: list of tuples of pythagorean triples with perimeter less than m
    '''
    out = []
    for i in range(1,m):
        j = i + 1
        k = j + 1
        while k <= m:
            while k**2 < i**2 + j**2:
                k +=1
            if k**2 == i**2 + j**2 and k <= m and i + j + k <= m:
                out.append((i, j, k))
            j += 1
    return out

def main():
    count = [0]*1000
    for triple in pythag_triples(1000):
        count[sum(triple)-1] += 1
    #print index + 1 where largest value is
    print(count.index(max(count)) + 1)
    pass

if __name__ == '__main__': main()