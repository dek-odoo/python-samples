#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program080:
# Please write a program to randomly generate a list with 5 numbers, which
# are divisible by 5 and 7 , between 1 and 1000 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

import random


def main(startLimit, endLimit):
    print random.sample([number for number in range(startLimit, endLimit + 1)
                         if number % 5 == 0 and number % 7 == 0], 5)

if __name__ == '__main__':
    # startLimit = int(raw_input("Input startLimit : "))
    # endLimit = int(raw_input("Input stopLimit : "))
    # main(startLimit, endLimit)
    main(1, 1000)
