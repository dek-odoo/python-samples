# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a class named Circle which can be constructed by a radius. The
# Circle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14


def main():
    circleObj = Circle(int(raw_input('Enter Value for Radius :')))
    print 'Area of Circle is : ', circleObj.area()

if __name__ == '__main__':
    main()
