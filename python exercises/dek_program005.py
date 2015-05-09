#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program005 : Name
# =>
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters


class cString:

    def __init__(self):
        print 'inside __init__(self):'
        self.x = 'Default String'

    def getString(self):  # input from console
        self.x = raw_input('Enter String : ')
        return self.x

    def printString(self):
        print 'in upper: ', self.x.upper()
        return self.x.upper()


def test():
    ac = cString()
    ac.getString()
    ac.printString()
    print 'TEST Class Methods'


def main():
    # start from here
    test()

if __name__ == '__main__':
    main()
# checked
