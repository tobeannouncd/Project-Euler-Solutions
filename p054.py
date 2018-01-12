# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:39:29 2017

@author: tobeannouncd

Problem 54: Poker hands

In the card game poker, a hand consists of five cards and are ranked, from 
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest 
value wins; for example, a pair of eights beats a pair of fives (see example 1 
below). But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); if the 
highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the 
first five are Player 1's cards and the last five are Player 2's cards. You can 
assume that all hands are valid (no invalid characters or repeated cards), each 
player's hand is in no specific order, and in each hand there is a clear 
winner.

How many hands does Player 1 win?
"""
from timeit import Timer

def poker_value(hand):
    vals = []
    suits = []
    for card in hand:
        vals.append(card[0])
        suits.append(card[1])
    
    num_vals = []
    for val in vals:
        if val == 'T':
            num_vals.append(10)
        elif val == 'J':
            num_vals.append(11)
        elif val == 'Q':
            num_vals.append(12)
        elif val == 'K':
            num_vals.append(13)
        elif val == 'A':
            num_vals.append(14)
        else:
            num_vals.append(int(val))
    num_vals.sort()
    
    set_vals = sorted(set(num_vals))
    isFlush = (len(set(suits)) == 1)
    isStraight = (len(set_vals) == 5 and num_vals[-1] - num_vals[0] == 4)
    if isFlush:
        if isStraight:
            if num_vals[0] == 10:
                hand_value = 9
            else:
                hand_value = 8 + num_vals[-1] / 15
        else:
            hand_value = 5 + num_vals[-1] / 15
    elif len(set_vals) == 2:
        c = 0
        for val in num_vals:
            if val == set_vals[0]:
                c += 1
        if c == 1:
            hand_value = 7 + set_vals[1] / 15
        elif c == 2:
            hand_value = 6 + set_vals[1] / 15
        elif c == 3:
            hand_value = 6 + set_vals[0] / 15
        else:
            hand_value = 7 + set_vals[0] / 15
    elif isStraight:
        hand_value = 4 + set_vals[-1] / 15
    elif len(set_vals) == 3:
        c = 0
        for val in num_vals:
            if val == set_vals[0]:
                c += 1
        if c == 1:
            d = 0
            for val in num_vals:
                if val == set_vals[1]:
                    d += 1
            if d == 1:
                hand_value = 3 + set_vals[2] / 15
            elif d == 2:
                hand_value = (2 + set_vals[2] / 15 + set_vals[1] / 15**2 + 
                              set_vals[0] / 15**3)
            else:
                hand_value = 3 + set_vals[1] / 15
        elif c == 2:
            d = 0
            for val in num_vals:
                if val == set_vals[1]:
                    d += 1
            if d == 1:
                hand_value = (2 + set_vals[2] / 15 + set_vals[0] / 15**2 + 
                              set_vals[1] / 15**3)
            else:
                hand_value = (2 + set_vals[1] / 15 + set_vals[0] / 15**2 + 
                              set_vals[2] / 15**3)
        else:
            hand_value = 3 + set_vals[0] / 15
    elif len(set_vals) == 4:
        if set_vals[0] == num_vals[1]:
            hand_value = (1 + set_vals[0] / 15 + set_vals[3] / 15**2 + 
                          set_vals[2] / 15**3 + set_vals[1] / 15**4)
        elif set_vals[1] == num_vals[2]:
            hand_value = (1 + set_vals[1] / 15 + set_vals[3] / 15**2 +
                          set_vals[2] / 15**3 + set_vals[0] / 15**4)
        elif set_vals[2] == num_vals[3]:
            hand_value = (1 + set_vals[2] / 15 + set_vals[3] / 15**2 +
                          set_vals[1] / 15**3 + set_vals[0] / 15**4)
        else:
            hand_value = (1 + set_vals[3] / 15 + set_vals[2] / 15**2 +
                          set_vals[1] / 15**3 + set_vals[0] / 15**4)
    else:
        hand_value = 0
        for i in range(5):
            hand_value += set_vals[4 - i] / 15**(i+1)
    return hand_value
        

def main():
    infile = 'p054_poker.txt'
    with open(infile) as f:
        hands = [line.split() for line in f.readlines()]
    
    p1_wins = 0
    for hand in hands:
        hand1 = hand[:5]
        hand2 = hand[5:]
        if poker_value(hand1) > poker_value(hand2):
            p1_wins += 1
        pass
    print('Player 1 wins {} times.'.format(p1_wins))
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))