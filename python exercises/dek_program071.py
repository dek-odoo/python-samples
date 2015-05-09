#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program071:
# Please write a program which accepts basic mathematic expression from
# console and print the evaluation result.

# Example:
# If the following string is given as input to the program:
# 35+3
# Then, the output of the program should be:
# 38

# Hints:
# Use eval() to evaluate an expression.


def main(expression):
    print eval(expression)


if __name__ == '__main__':
    expression = raw_input("Enter expression: ")
    main(expression)
    # main('34+5')
