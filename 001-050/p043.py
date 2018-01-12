# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:39:03 2017

@author: tobeannouncd

Sub-string divisibility
Problem 43 
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note 
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import time

def int_to_n_dig_str(num, n):
    '''
    n: int
    
    return: 3 character string representation of n
    '''
    if num not in range(10 ** n): raise ValueError
    n_str = str(num)
    while len(n_str) < n:
        n_str = '0' + n_str
    return n_str

def digits_unique(n_str):
    '''
    n_str: integer as n-digit string
    
    return: True if n digits are distinct, False otherwise
    '''
    if type(n_str) != str: raise TypeError
    for i in range(len(n_str)):
        if n_str[i] in n_str[:i]: return False
    return True

def substrings():
    '''
    returns list of lists of possible substrings
    [[d234], [d345], ..., [d8910]]
    '''
    primes = [2, 3, 5, 7, 11, 13, 17]
    o = []
    i = 0
    for prime in primes:
        p = prime
        o.append([])
        while True:
            if p > 999: break
            if digits_unique(int_to_n_dig_str(p, 3)):
                o[i].append(int_to_n_dig_str(p, 3))
            p += prime
        i+= 1
    return o

def consec_substr(l):
    '''
    l: list of lists of possible n-digit substrings
    
    return: list of lists of (n+1)-digit substrings
    '''
    o = []
    for i in range(len(l) - 1):
        o.append([])
        for j in l[i]:
            j_end = j[1:]
            for k in l[i+1]:
                k_beg = k[:-1]
                if (j_end == k_beg and
                    digits_unique(j + k[-1])):
                    o[i].append(j + k[-1])
    return o
                
                

def main():
    l = substrings()
    while len(l) > 1:
        l = consec_substr(l)
    l = l[0]
    for i in range(len(l)):
        for j in range(1, 10):
            if str(j) not in l[i]:
                l[i] = str(j) + l[i]
                break
    l = [int(i) for i in l]
    print(sum(l))
        

if __name__ == '__main__':  
    begin = time.clock()
    main()
    t_end = time.clock()
    print('Executed in', t_end - begin, 'seconds')