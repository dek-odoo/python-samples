#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program072:
# Please write a binary search function which searches an item in a sorted
# list. The function should return the index of element to be searched in
# the list.

# Hints:
# Use if/elif to deal with conditions.

import math


def main(numlist, searchnum):
    bottom = 0
    top = len(numlist) - 1
    index = -1

    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))

        if numlist[mid] > searchnum:
            top = mid - 1
        elif numlist[mid] == searchnum:
            index = mid
        else:
            bottom = mid + 1

    return index


if __name__ == '__main__':
    print main([23, 34, 45, 56, 67, 78, 89, 123], 23)
    print main([23, 34, 45, 56, 67, 78, 89, 123], 123)
