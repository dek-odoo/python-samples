# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a function that can accept an integer number as input and print
# the "It is an even number" if the number is even,
# otherwise print "It is an odd number".

# Hints:
# Use '%' operator to check if a number is even or odd.


def main(number):
    try:
        if int(number) % 2 == 0:
            print 'Inputted number ', number, ' is Even Number'
        elif not int(number) % 2 == 0:
            print 'Inputted number ', number, ' is Odd Number'
        else:
            pass
    except:
        print 'Please input a number Instead of ',\
            type(str(number)), str(number)

if __name__ == '__main__':
    main(raw_input('Enter Number :'))
