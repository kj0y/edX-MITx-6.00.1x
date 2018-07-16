# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 08:25:32 2018

@author: Kandis
"""

def lpymt(balance, annualInterestRate):
    '''
    a, b: positive integers
    returns: a positive integer, the balance after a year.
    '''
    month = 1
    monthlyInterestRate = annualInterestRate/12.0
    lpymt = 10
    ebal = balance
    while ebal != 0:
        ebal = balance
        for month in range(0, 12):
            month += 1
            ebal = ebal - lpymt
            ebal += ((monthlyInterestRate)*ebal)
        if ebal <= -10:
            return lpymt
        else:
            lpymt = lpymt + 10
            
lpmyt = lpymt(balance, annualInterestRate)

print('Lowest Payment:' + ' ' + str(lpmyt))