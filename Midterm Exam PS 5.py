# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:23:50 2018

@author: Kandis
"""
d = {1:10, 2:20, 3:30}
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #create empty inverse dictionary
    inverse = {}
    for key in d.keys():
        if d[key] in inverse:
            inverse[d[key]].append(key)
        else:
            inverse[d[key]] = [key]
    for val in inverse.values():
        val.sort()
    return inverse

print(dict_invert(d))