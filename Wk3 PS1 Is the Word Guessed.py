# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:59:12 2018

@author: Kandis
"""
secretWord = 'durian'
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord = list(secretWord)
    if set(secretWord).issubset(lettersGuessed) == True:
        return True
    else:
        return False              

print(isWordGuessed(secretWord, lettersGuessed))