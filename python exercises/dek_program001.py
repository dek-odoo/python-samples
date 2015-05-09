#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program001 : divisibleBy7not5
# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).

# The numbers obtained should be printed in a comma-separated sequence
# on a single line.

# Hints:
# Consider use range(#begin, #end) method


def divisibleBy7not5(startLimit, endLimit):
    result = []
    for number in range(startLimit, endLimit + 1):
        # "endLimit + 1" bcoz limits too,should be included
        # print number
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result


def main():
    print 'numbers divisible by 7 and not 5'
    print divisibleBy7not5(int(raw_input('Enter Value:')),
                           int(raw_input('Enter Value:')))

if __name__ == '__main__':
    main()
# checked
