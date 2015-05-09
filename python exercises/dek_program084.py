#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program084:
# Please write a program to shuffle and print the list [3,6,7,8].

# Hints:
# Use shuffle() function to shuffle a list.

from random import shuffle


def main(numlist):
    shuffle(numlist)
    print numlist


if __name__ == '__main__':
    print main(list(raw_input("Enter List: ")))
