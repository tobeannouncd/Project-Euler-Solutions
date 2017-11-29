# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:44:44 2017

@author: Tyler
"""
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
#print(isLeapYear(2011))
    
def daysInMonth(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        return 28 + isLeapYear(year)
    else:
        return 30
    
#print(daysInMonth(2,2015))

def dayOfWeek(month, day, year):
    d = 1
#    if year != 1900:
    for y in range(1900, year):
        d += 365 + isLeapYear(y)
        
#    if month != 1:
    for m in range(1, month):
        d += daysInMonth(m, year)
            
    d += day - 1
    return d % 7
    
    
#print(dayOfWeek(11,27,2017))

s = 0

for year in range(1900, 2001):
    for month in range(1,13):
        if dayOfWeek(month, 1, year) == 0:
            s += 1
            
print(s)