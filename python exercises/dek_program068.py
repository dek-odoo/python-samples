#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program068:
# Please write a program using generator to print the even numbers between
# 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10

# Hints:
# Use yield to produce the next value in generator.

# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def evenGenerator(endValue):
    eveniter = 0
    while eveniter <= endValue:
        if eveniter % 2 == 0:
            yield eveniter
        eveniter += 1


def main(endValue):
    result = []
    evenGen = evenGenerator(int(endValue))

    for res in evenGen:
        result.append(str(res))
    # print result
    print ",".join(result)


if __name__ == '__main__':
    main(raw_input("Input endLimit: "))
