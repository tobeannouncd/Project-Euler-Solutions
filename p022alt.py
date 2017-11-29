# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:02:42 2017

@author: Tyler
"""

def p22():
    with open('p022_names.txt') as f:
        names = sorted([n.strip('"') for n in f.read().split(',')])
    
    total = 0
    a = ord('A')
    for i in range(len(names)):
        total += sum([ord(c)-a+1 for c in names[i]]) * (i+1)
    print(total)
        
def main():
    from timeit import Timer
    print(Timer('p22()').timeit(1))
    
if __name__ == '__main__': main()