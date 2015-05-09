#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program067:
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program using list comprehension to
# print the Fibonacci Sequence in comma separated form with a given n
# input by console.

# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13

# Hints:
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# python has no tail call optimization,no advantange of using recursion ;)

i = 0


def fibonacci(number):
    global i
    i += 1
    print i
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def main(number):
    result = [str(fibonacci(num)) for num in range(0, number + 1)]
    print ",".join(result)


if __name__ == '__main__':
    main(int(raw_input("Input Number: ")))
