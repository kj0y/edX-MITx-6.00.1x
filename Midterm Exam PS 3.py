# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 11:02:03 2018

@author: Kandis
"""
secretNumber = 9
def isMyNumber(guess):
    if guess == secretNumber:
        return 0
    elif guess > secretNumber:
        return 1
    else:
        return -1

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    while isMyNumber(guess) != 0:
        if isMyNumber(guess) == -1:
            guess += 1
        else:
            guess -= 1
    return guess

print(jumpAndBackpedal(isMyNumber))
