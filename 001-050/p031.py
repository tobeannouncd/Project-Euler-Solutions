# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:57:37 2017

@author: Tyler
"""
import time
start = time.clock()

target = 200
coins  = [1, 2, 5, 10, 20, 50, 100, 200]
ways   = [1] + [0] * target

for coin in coins:
    for i in range(coin, target + 1):
        ways[i] += ways[i - coin]

print(ways[target])

print(time.clock() - start)