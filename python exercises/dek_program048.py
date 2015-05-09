# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program which can filter() to make a list whose elements are
# even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.


def do(start_number, end_number):
    list = [value for value in range(start_number, end_number + 1)]
    print 'List :', list
    result = filter(lambda number: number % 2 == 0, list)
    print 'Even Number From List :', result


def main():
    do(int(raw_input('Enter Starting Number :')),
       int(raw_input('Enter Ending Number :')))

if __name__ == '__main__':
    main()
