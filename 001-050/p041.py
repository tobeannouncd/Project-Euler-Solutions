# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:31:45 2017

@author: tobeannouncd

Pandigital prime
Problem 41 
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
"""
from factor_functions import is_prime


def is_n_dig_pandigital(n):
    n_list = [int(c) for c in str(n)]
    for i in range(len(n_list)):
        if n_list[i] not in range(1,len(n_list)+1): return False
        if n_list[i] in n_list[:i]: return False
    return True

n_max = 7654321
while True:
    if is_n_dig_pandigital(n_max) and is_prime(n_max):
        print(n_max)
        break
    n_max -= 2