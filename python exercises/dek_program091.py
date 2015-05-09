# !/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program091:
# By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.


def main(lst):
    return [value for (index, value) in enumerate(lst)
            if index not in (0, 4, 5)]

if __name__ == '__main__':
    print main([12, 24, 35, 70, 88, 120, 155])
