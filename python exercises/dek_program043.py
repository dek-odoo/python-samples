# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program to generate and print another tuple whose values are
# even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.


def main():
    val = tuple([value for value in range(1, 11)])
    print val
    list = []
    for number in val:
        if number % 2 == 0:
            list.append(str(number))
    print ','.join(list)

if __name__ == '__main__':
    main()
