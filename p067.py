# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:39:08 2017

@author: Tyler
"""
tri = []
with open('p067_triangle.txt') as f:
#    i = 0
    for line in f:
        line = line.strip()
        line = [int(x) for x in line.split(' ')]
        tri.append(line)
#        i += 1

wRow = len(tri) - 2
#print(tri[wRow])
while(wRow > -1):
    for i in range(len(tri[wRow])):
        tri[wRow][i] += max(tri[wRow + 1][i], tri[wRow + 1][i + 1])
    
    wRow -= 1
    
#maxVal = tri[0] + max(tri[1])

print(tri[0][0])