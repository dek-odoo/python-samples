#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program070:
# Please write assert statements to verify that every number in the list
# [2,4,6,8] is even.

# Hints:
# Use "assert expression" to make assertion.


def main(numlist):
    for num in numlist:
        assert num % 2 == 0
    print numlist, " Even Numbers"

if __name__ == '__main__':
    main([2, 4, 6, 8])
