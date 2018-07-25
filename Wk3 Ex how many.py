# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:24:25 2018

@author: Kandis
"""

aDict = {'B': [15], 'u': [10, 15, 5, 2, 6]}


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    x = 0
    for i in aDict.values():
        for word in i:
            x += 1
    return x

print(how_many(aDict))