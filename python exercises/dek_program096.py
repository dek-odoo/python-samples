#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program096:
# Please write a program which count and print the numbers of
# each character in a string input by console.

# Example:
# If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

# Hints:
# Use dict to store key/value pairs.
# Use dict.get() method to lookup a key with default value.


def main(data):
    result = {}

    for char in data:
        result[char] = result.get(char, 0) + 1
    return result


if __name__ == '__main__':
    result = main(raw_input("Input String: "))
    print '\n'.join(['%s,%s' % (k, v) for k, v in result.items()])
