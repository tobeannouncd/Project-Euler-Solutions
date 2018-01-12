# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:31:03 2017

@author: tobeannouncd

Project Euler problem 37: truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from factor_functions import is_prime

def is_trunc_prime(num):
    '''
    num: number to check
    
    output: true if num is truncatable prime, false otherwise
    '''
    for i in range(len(str(num)) - 1):
        if not is_prime(int(''.join(list(str(num))[:i+1]))): return False
        if not is_prime(int(''.join(list(str(num))[len(str(num))-i-1:]))):
            return False
    return True

def next_candidate(num):
    '''
    num: truncatable prime candidate
    
    output: prime number that might be truncatable
    '''
    while True:
        if num % 10 == 3: num += 4
        elif num % 10 == 7:
            num += 6
            num_list = list(str(num))
            first_digit = int(num_list[0])
            if first_digit in (1, 4, 6):
                num_list[0] = str(int(num_list[0]) + 1)
            elif first_digit > 7:
                num_list[0] = '20'
            num = int(''.join(num_list))
        if is_prime(num): break
    return num

def main():
    count = 0
    n = 23
    s = 0
    while count < 11:
        if is_trunc_prime(n):
            count += 1
            s += n
        n = next_candidate(n)
    print(s)
    pass

if __name__ == '__main__': main()