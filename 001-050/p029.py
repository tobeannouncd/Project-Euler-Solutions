# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:29:46 2017

@author: tobeannouncd
"""

seq = []
for a in range(2,101):
    for b in range(2, 101):
        if a**b not in seq:
            seq.append(a**b)
print(len(seq))