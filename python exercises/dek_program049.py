# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program which can map() to make a list whose elements are square
# of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.


def do(start_number, end_number):
    list = [value for value in range(start_number, end_number + 1)]
    print 'list :', list
    val = map(lambda number: number ** 2, list)
    print 'square of list Elements .......'
    print val


def main():
    do(int(raw_input('Enter Starting Number :')),
        int(raw_input('Enter Ending Number :')))
if __name__ == '__main__':
    main()
