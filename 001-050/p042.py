# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:17:38 2017

@author: tobeannouncd

Coded triangle numbers
Problem 42 
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so 
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?
"""
def tri_number(n):
    return n * (n + 1) // 2

def is_tri_number(n):
    n *= 2
    return n == int(n ** 0.5) ** 2 + int(n ** 0.5)

def is_tri_word(word):
    score = 0
    for letter in word:
        score += ord(letter) - ord('A') + 1
    return is_tri_number(score)

def main():
    filename = 'p042_words.txt'
    with open(filename) as f:
        words = [word.strip('"') for word in f.read().split(',')]
    c = 0
    for word in words:
        if is_tri_word(word): c += 1
    print(c)

if __name__ == '__main__': main()