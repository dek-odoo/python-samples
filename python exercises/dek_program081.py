#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program081:
# Please write a program to randomly print an integer number between 7 and
# 15 inclusive.

# Hints:
# Use random.randrange() to a random integer in a given range.

import random


def main(startLimit, endLimit):
    print random.randrange(startLimit, endLimit + 1)

if __name__ == '__main__':
    # startLimit = int(raw_input("Input StartLimit : "))
    # endLimit = int(raw_input("Input EndLimit : "))
    # main(startLimit, endLimit)
    main(7, 15)
