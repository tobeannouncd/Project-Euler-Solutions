# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:02:19 2017

@author: Tyler
"""

def isLeapYear(year):
    '''
    year: integer
    
    return: bool, True if leap year, False otherwise
    '''
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    '''
    year, month: integer
    
    return: days in the month, int
    '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        return 28 + isLeapYear(year)
    else:
        return 30
    
def countSundays(yb, mb, ye, me, d):
    '''
    yb: year begin
    ye: year end
    mb: month begin
    me: month end
    d: beginning day of week
    
    return: (year, month, dayOfWeek, sundays)
    '''
    sundays = 0
    
    while yb < ye or mb < me:
        if d == 0:
            sundays += 1
        d += daysInMonth(yb,mb)
        d = d % 7
        mb += 1
        if mb == 13:
            mb = 1
            yb += 1
    
    return (yb, mb, d, sundays)

(y, m, d, s) = countSundays(1900, 1, 1901, 1, 1)
s = 0

(y, m, d, s) = countSundays(y,m,2001, 1, d)