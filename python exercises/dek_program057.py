# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a custom exception class which takes a string message as attribute.

# Hints:
# To define a custom exception, we need to define a class inherited from
# Exception.


class MyException(Exception):

    def __init__(self, message):
        self.message = message


def main():
    try:
        raise MyException('This is My Custom Exeption...')

    except MyException, errror:
        print 'Error :', errror.message


if __name__ == '__main__':
    main()
