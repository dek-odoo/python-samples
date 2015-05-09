#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program075:
# Please generate a random float where the value is between 5 and 95 using
# Python math module.

# Hints:
# Use random.random() to generate a random float in [0,1].

import random


def main(limit):
    print random.random() * 100 % 95


if __name__ == '__main__':
    # main(int(raw_input("Input limit: ")))
    main(1000)
