#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:33:56 2019

@author: celestineekoh-ordan
"""
# Exercise: genPrimes
# 0.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
def genPrimes():
    primes = []
    num = 1
    while True:
        num += 1
        for n in primes:
            if (num % n) == 0:
                break
        else:
            primes.append(num)
            yield num