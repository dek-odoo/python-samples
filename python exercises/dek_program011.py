#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program# : Name
# =>
# Write a program which accepts a sequence of comma separated
# 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible
# by 5 are to be printed in a comma separated sequence.
# Example:
# a='0100,0011,1010,1001'
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def start(binString):
    binString = binString.split(',')
    print binString
    newa = []
    for x in binString:
        if int(x, 2) % 5 == 0:
            newa.append(x)
    return newa


def main():
    # start from here
    print "sample input\n", '0100,0011,1010,1011,1110,1001'
    # binString = '0100,0011,1010,1011,1110,1001'
    #*************** comment the below line to TEST
    binString = raw_input('Enter a Binary Number String: ')
    try:
        print start(binString)
    except:
        print 'Invalid Format',\
            '0100,0011,1010,1011,1110,1001', '(Sample Format)'
if __name__ == '__main__':
    main()
# checked
