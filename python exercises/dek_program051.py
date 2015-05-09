# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a class named Indian and its subclass .

# Hints:
# Use class Subclass(ParentClass) to define a subclass.


class Indian(object):

    def printIndian(self):
        print 'I am an Indian'


class Gujarati(Indian):

    def printGujarati(self):
        print 'I am Gujarati'

    def printMarathi(self):
        print 'I am Marathi'

    def printKathiyawadi(self):
        print 'I am Kathiyawadi'


def main():
    superObj = Indian()
    subObj = Gujarati()

    print superObj.printIndian()
    print subObj.printGujarati()

if __name__ == '__main__':
    main()
