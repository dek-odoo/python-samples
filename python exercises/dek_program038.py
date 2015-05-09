# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function which can generate a list where the values are square
# of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list


def main():
    numbers = []

    for value in range(1, 21):
        numbers.append(str(value ** 2))
    print ','.join(numbers)
    print numbers[0:5]
if __name__ == '__main__':
    main()
