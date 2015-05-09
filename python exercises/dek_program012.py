#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program# : Name
# =>
# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma - separated sequence
# on a single line.

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def evensBetween(startLimit, endLimit):
    return [x for x in range(startLimit, endLimit) if x % 2 == 0]


def main():
    # start from here
    # print "main starts here"
    startLimit = int(raw_input('Enter StartLimit: '))
    endLimit = int(raw_input('Enter EndLimit: '))
    evensBetweenAnd = evensBetween(startLimit, endLimit)
    print evensBetweenAnd

if __name__ == '__main__':
    main()
# checked
