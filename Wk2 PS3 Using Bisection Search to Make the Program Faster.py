# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:32:31 2018

@author: Kandis
"""

def lpymt(balance, annualInterestRate):
    '''
    a, b: positive integers
    returns: a positive integer, the minimum monthly fixed payment to pay off the debt in 12 months.
    '''
    month = 1
    monthlyInterestRate = annualInterestRate/12.0   
    low = balance/12
    high = ((balance*(1 + monthlyInterestRate)**12))/12.0
    lpymt = (high + low)/2.0
    ebal = balance
    pmbal = ebal
    
    while abs(ebal) >= .01:
        lpymt = (high + low)/2.0
        ebal = balance
        for month in range(0, 12):
            month += 1
            ebal = pmbal - lpymt
            ebal += ((monthlyInterestRate)*ebal)
            pmbal = ebal
        if ebal < 0:
            high = (high + lpymt)/2
            pmbal = balance
        if ebal > 0:
            low = (low + lpymt)/2
            pmbal = balance
        if abs(ebal) <= .01:
            return round(lpymt,2)
            
balance = 320000
annualInterestRate = 0.2

lpymt = lpymt(balance, annualInterestRate)

print('Lowest Payment:' + ' ' + str(lpymt))