#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program006 :  Modified Version of Prg6_sqrt.py
# Write a program that calculates and prints the value according to the
# given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a
# comma-separated sequence.

# Example
# Let us assume the following comma separated input
# sequence is given to the program:
# 100,150,180

# The output of the program should be:
# 18,22,24

# Hints:
# If the output received is in decimal form, it should be rounded off
# to its nearest value (for example, if the output received is 26.0,
# it should be printed as 26)
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# A more generalized form of the previous program prg6_sqrt.py

import math


def getNumberListFromConsole():  # returns a list like [100,150,180]
    try:
        d = raw_input('Enter Number: ')  # '100,150,180'
        d = d.split(',')  # ['100','150','180']
        d = [int(x) for x in d]  # [100,150,180]
        return d
    except:
        print 'Invalid Format'


def nsqrt():
    print "sample input ", '100,150,180'
    c = 50
    h = 30
    d = getNumberListFromConsole()
    # [18.24828759089466, 22.360679774997898, 24.49489742783178]
    q = [math.sqrt((2 * c * dk) / h) for dk in d]
    q = [int(x) for x in q]  # [18, 22, 24]
    print 'nsqrt : ', q
    return q


def main():
    nsqrt()

if __name__ == '__main__':
    main()
