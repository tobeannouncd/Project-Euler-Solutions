# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:47:58 2017

@author: tobeannouncd

Project Euler problem 38: pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
def concat_products(num):
    '''
    num: number to multiply
    
    output: result of multiplying num by 1, 2, ..., n and concatenating to 
    prior products until 9 digit number is formed
    '''
    out = ''
    i = 1
    while len(out) < 9:
        out += str(num * i)
        i += 1
    return int(out)

def is_pandigital(num):
    '''
    num: number to check
    
    output: True if number is pandigital (1-9), False otherwise
    '''
    num = str(num)
    if len(num) != 9: return False
    for i in range(1, len(num)):
        if num[i] in num[:i] or num[i] == '0': return False
    return True

def main():
    c = []
    for i in range(1,10**6):
        if is_pandigital(concat_products(i)): c.append((i, concat_products(i)))
    print(c)
    pass

if __name__ == '__main__': main()