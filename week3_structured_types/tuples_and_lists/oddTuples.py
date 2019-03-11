#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:37:05 2019

@author: celestineekoh-ordan
"""
# Exercise: odd tuples
# 1/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    elements = ()
    for i in range(len(aTup)):
        if(i % 2 == 0):
            elements += (aTup[i],)
    return elements
