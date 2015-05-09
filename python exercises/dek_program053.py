# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a class named Rectangle which can be constructed by a length and
# width. The Rectangle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.


class Ractangle(object):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def areaOfRactangle(self):
        return self.length * self.width


def main():
    ractangleObj = Ractangle(
        int(raw_input('Enter Value for length of Ractangle :')),
        int(raw_input('Enter Value for Width of Ractangle :')))

    print 'Area of Ractangle is : ', ractangleObj.areaOfRactangle()

if __name__ == '__main__':
    main()
