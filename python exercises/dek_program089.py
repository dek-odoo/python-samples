#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program089:
# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.


def main(numlist):
    return [value for (index, value) in enumerate(numlist) if index % 2]

if __name__ == '__main__':
    print main([12, 24, 35, 70, 88, 120, 155])
