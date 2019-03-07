#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:30:58 2019

@author: celestineekoh-ordan
"""

# Problem 3
# 0.0/15.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'aaaaaazcbobobegghaklmnopqrstvu'

count = 0
maxCount = 0
prevChar = s[0]
substring = ''
maxSub = ''
for c in range(len(s)):
    if(s[c] >= prevChar):
        count += 1
        substring += s[c]
    else:
        maxCount = maxCount if maxCount > count else count
        maxSub = maxSub if maxCount > count else substring
        count = 1
        substring = s[c]
    prevChar = s[c]
maxSub = maxSub if maxCount > count else substring
print(maxSub)