#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program069:
# Please write a program using generator to print the numbers which can be
# divisible by 5 and 7 between 0 and n in comma separated form while n is
# input by console.

# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70

# Hints:
# Use yield to produce the next value in generator.
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def evenGenerator(endValue):
    eveniter = 0
    while eveniter <= endValue:
        print eveniter
        if eveniter % 5 == 0 and eveniter % 7 == 0:
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
    main(raw_input("Input endLimit : "))
