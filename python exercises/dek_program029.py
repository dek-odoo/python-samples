# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function that can receive two integral numbers in string form
# and compute their sum and then print it in console.

# Hints:
# Use int() to convert a string to integer.


def main(first_number, second_number):
    print int(first_number) + int(second_number)
if __name__ == '__main__':
    main(raw_input('Enter First Number :'), raw_input('Enter Second Number :'))
