# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Problem 206

Concealed Square

find x for x^2 = 1_2_3_4_5_6_7_8_9_0
"""
from timeit import Timer

def main():
    r = []
    for k in range(101010103, 138902663):
        if k % 10 == 3 or k % 10 == 7:
            r.append(k)
    for j in r:
        i = str(j**2)
        if i[::2] == '123456789':
            print(int(j*10))
            break
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print('Executed in {:.3G} seconds.'.format(t.timeit(1)))

