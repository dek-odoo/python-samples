# !/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program094:
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program
# to print this list after removing all duplicate values with original
# order reserved.

# Hints:
# Use set() to store a number of values without duplicate.


def main(numbers):
    newlist = []
    uniqueD = set()
    # print "asdfasdf ", set(lst)
    # set(list) unuseful since "with original order reserved" required.
    for num in numbers:
        if num not in uniqueD:
            uniqueD.add(num)
            newlist.append(num)

    print newlist


if __name__ == '__main__':
    main([12, 24, 35, 24, 88, 120, 155, 88, 120, 155])
