# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.


def main():
    dictonary = dict()

    dictonary[1] = 1 ** 2
    dictonary[2] = 2 ** 2
    dictonary[3] = 3 ** 2

    print dictonary
if __name__ == '__main__':
    main()
