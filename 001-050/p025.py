# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:24:51 2017

@author: tobeannouncd
"""

a, b, i = 1, 1, 2

while b < 10**999:
    a, b = b, a + b
    i += 1
    
print(i)