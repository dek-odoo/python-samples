#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program066:
# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value of f(n)
# with a given n input by console.

# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 13

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.


def recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number > 1:
        result = recursive(number - 1) + recursive(number - 2)
        return result
    # else:
    #     return -1


def main():
    result = recursive(int(raw_input("Input Number: ")))
    print result
    # print 'final', result
if __name__ == '__main__':
    main()
