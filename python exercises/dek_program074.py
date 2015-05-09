#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program074:
# Please generate a random float where the value is between 10 and 100
# using Python math module.

# Hints:
# Use random.random() to generate a random float in [0,1].

import random


def main(limit):
    print(random.random() * 100) % 100

if __name__ == '__main__':
    limit = int(raw_input("Input limit: "))
    main(limit)
