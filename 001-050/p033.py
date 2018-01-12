# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:20:19 2017

@author: tobeannouncd
"""
res = []
for a in range(1,10):
    for b in range(10):
        for c in range(a,10):
            for d in range(10):
                if a == c and b == d: break
                if a == c and d != 0:
                    if (10*a +b) / (10*c + d) == b / d:
                        res.append([a, b, c, d])
                if a == d:
                    if (10*a +b) / (10*c + d) == b / c:
                        res.append([a, b, c, d])
                if b == c and d != 0:
                    if (10*a +b) / (10*c + d) == a / d:
                        res.append([a, b, c, d])
                if b == d and b != 0:
                    if (10*a +b) / (10*c + d) == a / c:
                        res.append([a, b, c, d])
                        
print(res)