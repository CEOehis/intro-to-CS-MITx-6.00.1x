#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:28:58 2019

@author: celestineekoh-ordan
"""
# Problem 4 - Hand Length
# 0.0/10.0 points (graded)
# We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.
#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    letterCount = 0
    for letter in hand.keys():
        letterCount += hand[letter]
    return letterCount