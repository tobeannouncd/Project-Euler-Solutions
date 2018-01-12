# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:43:27 2017

@author: tobeannouncd
"""
def nameValue(name, ind):
    nameNums = []
    for letter in name:
        nameNums.append(ord(letter)-ord('A')+1)
        
    return sum(nameNums)*ind

def main():
    names = []
    with open('p022_names.txt') as file:
        for line in file:
            names.extend(line.split(','))
    
    names = [name.strip('"') for name in names]
    names.sort()
    for i in range(len(names)):
        names[i] = nameValue(names[i],i+1)
        
    print(sum(names))
    
if __name__ == '__main__':
    from timeit import Timer
    print(Timer('main()', 'from __main__ import main').timeit(1))