#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program076:
# Please write a program to output a random even number between 0 and 10
# inclusive using random module and list comprehension.

# Hints:
# Use random.choice() to a random element from a list.

import random


def main(limit):
    print random.choice([num for num in range(limit + 1) if num % 2 == 0])


if __name__ == '__main__':
    # limit = int(raw_input("Input limit: "))
    # main(limit)
    main(10)
