#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program079:
# Please write a program to randomly generate a list with 5 even numbers
# between 100 and 200 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

import random


def main(startLimit, endLimit):
    print random.sample([number for number in range(startLimit, endLimit + 1)
                         if number % 2 == 0], 5)

if __name__ == '__main__':
    # startLimit = int(raw_input("Input startLimit : "))
    # endLimit = int(raw_input("Input endLimit : "))
    # main(startLimit, endLimit)
    main(100, 200)
