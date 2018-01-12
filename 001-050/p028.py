# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:09:41 2017

@author: tobeannouncd
"""

'''
1    +2
3    +2
5    +2
7    +2
9    +4
13   +4
17   +4
21   +4
25

size = (length-1)/2 + 1
increment = orig_size + 1
'''

diag = [1]
inc = 2
size = 1
target_size = 1001
while size < target_size:
    for i in range(4):
        diag.append(diag[-1]+inc)
    size += 2
    inc += 2
        
print(sum(diag))