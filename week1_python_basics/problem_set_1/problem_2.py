#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:15:39 2019

@author: celestineekoh-ordan
"""

# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

count = 0
for i in range(len(s)):
    if('bob' in s[i:(i+3)]):
        count += 1
print('Number of times bob occurs is:', count)
