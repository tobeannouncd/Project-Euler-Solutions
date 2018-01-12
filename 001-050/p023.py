# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:19:45 2017

@author: tobeannouncd
"""
def isAbundant(num):
    s = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0: s += i
    return s > num

abundants = []
for x in range(1,28124):
    if isAbundant(x): abundants.append(x)
    
sums = [0]*28124
for x in range(len(abundants)):
    for y in range(x,len(abundants)):
        s = abundants[x]+abundants[y]
        if s < 28124:
            sums[s] = s
            
total = 0
for x in range(1,len(sums)):
    if sums[x] == 0:
        total += x
        
print(total)