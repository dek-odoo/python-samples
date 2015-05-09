# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program which can filter even numbers in a list by using filter
# function. The list is:
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.


def do(start_number, end_number):
    list = [value for value in range(start_number, end_number + 1)]
    print 'list :', list
    result = filter(lambda number: number % 2 == 0, list)
    print 'Even Number From list :', result


def main():
    do(int(raw_input('Enter Starting Number :')),
       int(raw_input('Enter Ending Number :')))

if __name__ == '__main__':
    main()
