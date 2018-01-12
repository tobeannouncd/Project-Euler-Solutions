# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:19:54 2017

@author: tobeannouncd
"""

irr_num = '0.'
i = 1
n = 1000000
while len(irr_num) - 2 < n:
    irr_num += str(i)
    i += 1

j = 1
o = 1
while j <= n:
    o *= int(irr_num[j + 1])
    j *= 10
    
print(o)