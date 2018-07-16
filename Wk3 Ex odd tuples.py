# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:03:11 2018

@author: Kandis
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[0::2]

aTup = ('I', 'am', 'a', 'test', 'tuple')

aTup = oddTuples(aTup)

print(aTup)