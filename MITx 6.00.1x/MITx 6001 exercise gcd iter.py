# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 21:00:28 2018

@author: Kandis
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if a < b:
        result = b
    else:
        result = a
    while result != 1:
        if a % result == 0 and b % result == 0:
            return result
        else:
            result -= 1
    if result == 1:
        return result
        
 



