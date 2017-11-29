# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:37:16 2017

@author: Tyler
"""
def rn_to_dec(rn):
    letter_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 
                   'M': 1000}
    letter_pair_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 
                        'CM': 900}
    i = 0
    val = 0
    while i < len(rn) - 1:
        if rn[i:i+2] in letter_pair_dict.keys():
            val += letter_pair_dict[rn[i:i+2]]
            i += 2
        else:
            val += letter_dict[rn[i]]
            i += 1
    if i < len(rn):
        val += letter_dict[rn[i]]
    return val

def dec_to_rn(dec):
    def deduct(rn, dec, s, n):
        rn += s * (dec // n)
        dec -= (dec // n)*n
        return (rn, dec)
    
    rn = ''
    (rn, dec) = deduct(rn, dec, 'M', 1000)
    (rn, dec) = deduct(rn, dec, 'CM', 900)
    (rn, dec) = deduct(rn, dec, 'D', 500)
    (rn, dec) = deduct(rn, dec, 'CD', 400)
    (rn, dec) = deduct(rn, dec, 'C', 100)
    (rn, dec) = deduct(rn, dec, 'XC', 90)
    (rn, dec) = deduct(rn, dec, 'L', 50)
    (rn, dec) = deduct(rn, dec, 'XL', 40)
    (rn, dec) = deduct(rn, dec, 'X', 10)
    (rn, dec) = deduct(rn, dec, 'IX', 9)
    (rn, dec) = deduct(rn, dec, 'V', 5)
    (rn, dec) = deduct(rn, dec, 'IV', 4)
    (rn, dec) = deduct(rn, dec, 'I', 1)
    return rn
    

numbers = []
with open('p089_roman.txt') as f:
    for line in f:
        numbers.append(line.strip())
        
#numbers = ['CMXX'] # sample case

vals = []
for num in numbers:
    vals.append(rn_to_dec(num))
            
rns = []
for val in vals:
    rns.append(dec_to_rn(val))
    
saved = 0
for i in range(len(numbers)):
    saved += len(numbers[i]) - len(rns[i])