# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 19:15:32 2018

@author: Kandis
"""

aDict = {'B': [15], 'u': [10, 15, 5, 2, 6]}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    if aDict == {}:
        return result
    else:
        for i in aDict.keys():
            if len(aDict[i]) > 0:
                result = i
                
    return result

print(biggest(aDict))

