#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program087:
# Please write a program to print the list after removing delete even
# numbers in [5,6,77,45,22,12,24].

# Hints:
# Use list comprehension to delete a bunch of element from a list.


def main(numlist):
    return [num for num in numlist if int(num) % 2]


if __name__ == '__main__':
    # main(list(raw_input("Input List: ")))
    print main([23, 34, 45, 56, 67, 78, 89, 12, 11])
