# !/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar

# Define a class with a generator which can iterate the numbers, which are
# divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield


def generator():
    for number in range(0, 100):
        if (number % 7 == 0):
            yield number


def main():
    gener = generator()
    # one liner
    # yield number
    print gener.next()
    print gener.next()
    print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # print gener.next()
    # for i in gener:
    #     print i

if __name__ == '__main__':
    main()
# Of particular note is the memory overhead savings.
# Values are computed on-demand,
# so you never have the entire result of the list
#  comprehension in memory.
#  This is particularly desirable if you later iterate over only part of
#   the list comprehension. –
