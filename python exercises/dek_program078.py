#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program078:
# Please write a program to generate a list with 5 random numbers between
# 100 and 200 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

import random


def main(startLimit, endLimit):
    print random.sample(range(startLimit, endLimit + 1), 5)

if __name__ == '__main__':
    # startLimit = int(raw_input("Input Start Value: "))
    # endLimit = int(raw_input("Input Stop Value: "))
    # main(startLimit, endLimit)
    main(100, 200)
