# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Problem 99: Largest exponential
"""
from time import clock
from math import log


def euler_099():
    with open('p099_base_exp.txt') as f:
        nums = [[int(num) for num in line.split(',')] for line in f]
    
    b_log_a = [b*log(a) for a, b in nums]
    max_b_log_a = max(b_log_a)
    for i in range(len(b_log_a)):
        if b_log_a[i] == max_b_log_a:
            return i + 1
    return 0

start_time = clock()

print(euler_099())

print('Executed in {:.3G} seconds.'.format(clock() - start_time))