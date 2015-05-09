#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program065:
# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=0

# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 500

# In case of input data being supplied to the question,# it should be
# assumed to be a console input.

# Hints:
# We can define recursive function in Python.

# import timeit


def recursive(number):
    if number == 0:
        return 0
    else:
        # python has no tail call optimization,no advantange ;)
        return recursive(number - 1) + 100


def main():
    # print timeit.timeit()
    print recursive(int(raw_input("Input Number: ")))
    # print timeit.timeit()

if __name__ == '__main__':
    main()
