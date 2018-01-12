# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:36:12 2017

@author: tobeannouncd
"""
s = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        s += i
        
print(s)