# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a function to compute 5 / 0 and use try / except to catch the
# exceptions.

# Hints:
# Use try / except to catch exceptions.


def devideByZero():
    return 5 / 0


def main():
    try:
        devideByZero()
    except ZeroDivisionError:
        print 'ZeroDivisionError DivideBy Zero..'


if __name__ == '__main__':
    main()
