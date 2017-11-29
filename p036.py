# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:11:13 2017

@author: Tyler

Project Euler problem 36: Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def dec_to_bin(d):
    b = list(bin(d))
    b = int(''.join(b[2:]))
    return b

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def main():
    s = []
    for i in range(1,10**6):
        if is_palindrome(i) and is_palindrome(dec_to_bin(i)): s.append(i)
    print(sum(s))
    pass

if __name__ == "__main__": main()
