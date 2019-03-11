#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:09:33 2019

@author: celestineekoh-ordan
"""
# Exercise: biggest
#  Bookmark this page
# Exercise: biggest
# 0.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 7 minutes

# Consider the following sequence of expressions:

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.

# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

# Example usage:

# >>> biggest(animals)
# 'd'
# If there are no values in the dictionary, biggest should return None.
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if(len(aDict) == 0):
        return None
    count = 0
    key = ''
    for dictKey in aDict:
        totalItems = len(aDict[dictKey])
        if(count < totalItems):
            count = totalItems
            key = dictKey
    return key
