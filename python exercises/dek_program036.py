# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.
# The function should just print the values only.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary.
# Also we can use item() to get key/value pairs.


def main():
    dictionary = dict()

    for value in range(1, 21):
        dictionary[value] = value ** 2
    print dictionary.keys()
if __name__ == '__main__':
    main()
