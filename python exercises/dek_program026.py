# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments.
# You can compute the sum in the function and return the value.


def main(number1, Number2):
    print 'Sum of Two Number is  :', number1 + Number2
if __name__ == '__main__':
    main(int(raw_input('Enter Number 1 :')),
         int(raw_input('Enter Number 2 :')))
