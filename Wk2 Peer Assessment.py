# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 17:28:44 2018

@author: Kandis
"""
def square(y):
    x = y*y
    return x

def fourthPower(x):
    return square(square(x))

x = 3
fourthPower(x)