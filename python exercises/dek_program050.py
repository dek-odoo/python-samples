# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a class named American which has a static method called
# printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.


class American(object):

    @staticmethod
    def printNationality():
        print 'I Am American'


def main():
    object1 = American()
    object1.printNationality()
    American.printNationality()
if __name__ == '__main__':
    main()
