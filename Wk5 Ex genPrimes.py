# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 14:29:40 2018

@author: kandi
"""

def genPrimes():
    primes = []
    numerator = 2
    last = numerator
    
    while True:
        for denom in primes:
            if numerator % denom == 0:
                numerator += 1
                break
        else:
            primes.append(numerator)
            last = numerator
            numerator += 1
            yield last
        
