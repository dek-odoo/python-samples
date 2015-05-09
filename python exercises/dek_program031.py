# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function that can accept two strings as input and print
# the string with maximum length in console.
# If two strings have the same length,
# then the function should print al l strings line by line.

# Hints:
# Use len() function to get the length of a string


def main(first_string, second_string):
    if len(first_string) > len(second_string):
        print first_string
    elif len(second_string) > len(first_string):
        print second_string
    elif len(first_string) == len(second_string):
        print first_string
        print second_string
    else:
        pass
if __name__ == '__main__':
    main(raw_input('Enter First String :'), raw_input('Enter Second String :'))
