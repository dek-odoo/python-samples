# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program which can map() and filter() to make a list whose
# elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.


def do(start_number, end_number):
    list = [value for value in range(start_number, end_number + 1)]
    print 'List :', list
    filtr = filter(lambda number: number % 2 == 0, list)
    print 'Even number from List : ', filtr
    maping = map(lambda number: number ** 2, filtr)
    print 'Square of Even number from List :', maping


def main():
    do(int(raw_input('Enter Starting Number :')),
       int(raw_input('Enter Ending Number :')))

if __name__ == '__main__':
    main()
