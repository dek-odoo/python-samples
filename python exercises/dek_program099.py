#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program099:
# Please write a program which prints all permutations of [1,2,3]

# Hints:
# Use itertools.permutations() to get permutations of list.

import itertools


def main(numlist):
    return list(itertools.permutations(numlist))


if __name__ == '__main__':
    print main([1, 2, 3])
