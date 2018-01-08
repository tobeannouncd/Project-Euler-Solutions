# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:57:37 2017

@author: Tyler
"""
count = 0
#1 2 5 10 20 50 100 200
for p1 in range(11):
    p1_2 = 11 - p1
    for p2 in range(0, p1_2, 2):
        p2_5 = p1_2 - p2
        for p5 in range(0, p2_5, 5):
            p5_10 = p2_5 - p5
            for p10 in range(0, p5_10, 10):
                p10_20 = p5_10 - p10
                for p20 in range(0, p10_20, 20):
                    p20_50 = p10_20 - p20
                    for p50 in range(0, p20_50, 50):
                        p50_100 = p20_50 - p50
                        for p100 in range(0, p50_100, 100):
                            p100_200 = p50_100 - p100
                            for p200 in range(0, p100_200, 200):
                                if (p1 + p2 + p5 + p10 + p20 + p50 + p100 +
                                    p200 == 200):
                                    count += 1
                                    
print(count)