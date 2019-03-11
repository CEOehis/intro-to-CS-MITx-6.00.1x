#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:23:15 2019

@author: celestineekoh-ordan
"""
# Exercise: apply to each 2
# 0.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 4 minutes

#   >>> print(testList)
#   [2, -3, 9, -8]

# Here is the code for a function applyToEach:

# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])
# Assume that

# testList = [1, -4, 8, -9]
# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

# Example Question:

# >>> print(testList)
# [5, -20, 40, -45]
# Solution to Example Question


#   >>> print(testList)
#   [1, 4, 8, 9]

def addOne(a):
    return a + 1


applyToEach(testList, addOne)
