#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:40:57 2019

@author: celestineekoh-ordan
"""
# Exercise: how many
#  Bookmark this page
# Exercise: how many
# 0.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 6 minutes

# Consider the following sequence of expressions:

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.

# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

# >>> print(how_many(animals))
# 6
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for item in aDict.values():
        count += len(item)
    return count