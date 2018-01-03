# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:58:24 2017

@author: Tyler

Problem 51: Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
number is the first example having seven primes among the ten generated 
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 
56993. Consequently 56003, being the first member of this family, is the 
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily 
adjacent digits) with the same digit, is part of an eight prime value family.
"""
from timeit import Timer
from Euler51 import is_prime, next_prime

def replace_digit(num, init, final):
    n_list = [int(x) for x in list(str(num))]
    for i in range(len(n_list)):
        if n_list[i] == init:
            n_list[i] = final
    return int(''.join([str(x) for x in n_list]))

def prime_family_members(num):
    n_list = [int(x) for x in list(str(num))]
    out = []
    for digit in set(n_list):
        fam_members = []
        for i in range(10):
            fam_members.append(replace_digit(num, digit, i))
        out.append(fam_members)
    
    o2 = []
    for l in out:
        prime_fam_mems = []
        for i in l:
            if len(str(i)) == len(n_list) and is_prime(i):
                prime_fam_mems.append(i)
        o2.append(prime_fam_mems)
        
    m = 0
    for i in o2:
        m = max(m, len(i))
    return m

def main():
    x = next_prime(56003)
    while prime_family_members(x) < 8:
        x = next_prime(x)
    
    print(x)
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))