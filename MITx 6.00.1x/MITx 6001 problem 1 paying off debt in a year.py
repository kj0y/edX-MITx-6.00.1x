# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 23:34:06 2018

@author: Kandis
"""
def ccbal(balance, annualInterestRate, monthlyPaymentRate):
    '''
    a, b, c: positive integers
    returns: a positive integer, the balance after a year.
    '''
    month = 1
    monthlyInterestRate = annualInterestRate/12.0
    while month <= 12:
        month += 1
        balance = balance - ((monthlyPaymentRate)*balance)
        balance += ((monthlyInterestRate)*balance)
    balance = (round(balance,2))
    return balance
    
balance = ccbal(balance, annualInterestRate, monthlyPaymentRate)

print('Remaining Balance:' + ' ' + str(balance))