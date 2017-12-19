# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler
"""
from timeit import Timer

def main():
    pass

if __name__ == '__main__':
    t = Timer('main()', 'from __main__ import main')
    print(t.timeit(1))
