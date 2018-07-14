# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:49:40 2018

@author: Kandis
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
        
    
