#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program009 :
# Definition
# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the

# program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main():
    print "sample input\n",  'Hello world', '\n', 'Practice makes perfect'
    print 'Enter lines below: '
    words = ''
    while True:
        inn = raw_input('>>')
        if not inn:
            break
        words = words + inn + ' '
    print 'In Upper Case : ', words.upper()

if __name__ == '__main__':
    main()
# checked
