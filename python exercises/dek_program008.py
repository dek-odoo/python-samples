#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program008 :
# Write a program that accepts a comma separated
# sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main():
    print "sample input ", 'without,hello,bag,world'
    str = raw_input('Enter : ')
    li1 = str.split(',')
    # print li1
    li1.sort()
    print li1

if __name__ == '__main__':
    main()
# checked
