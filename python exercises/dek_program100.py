#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program100:
# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits
# in a farm. How many rabbits and how many chickens do we have?

# Hint:
# Use for loop to iterate all possible solutions.


def main(total, numLegs):
    for rabbits in range(total + 1):
        chickens = total - rabbits
        if 2 * chickens + 4 * rabbits == numLegs:
            return chickens, rabbits
    return None, None


if __name__ == '__main__':
    try:
        numHeads = int(raw_input("Input number of heads: "))
        numLegs = int(raw_input("Input number of legs: "))
        result = main(numHeads, numLegs)
        print "Number of chickens are %d and rabbits are %d." % result
    except TypeError:
        print 'TypeError: invalid input'
