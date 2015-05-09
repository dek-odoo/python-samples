# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function which can generate and print a tuple where
# the value are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.


def main():
    numbers = []

    for value in range(1, 21):
        numbers.append(str(value ** 2))
    print tuple(numbers)

if __name__ == '__main__':
    main()
