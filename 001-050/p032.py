# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:56:09 2017

@author: tobeannouncd
"""
def isPandigital(n1, n2, n3):
    n_str = sorted(list(str(n1) + str(n2) + str(n3)))
    return n_str == ['1','2','3','4','5','6','7','8','9']

def main():
    prods = []
    for a in range(1, 10000):
        b_max = 10000 // a + 1
        for b in range(1, b_max):
            if isPandigital(a, b, a*b):
                if a*b not in prods: prods.append(a*b)
    print(sum(prods))
    pass

if __name__ == '__main__' : main()