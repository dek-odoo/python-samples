#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program097:
# Please write a program which accepts a string from
# console and print it in reverse order.

# Example:
# If the following string is given as input to the program:
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir

# Hints:
# Use list[::-1] to iterate a list in a reverse order.


def main(data):
    return data[::-1]

if __name__ == '__main__':
    print main(raw_input("Input String: "))
