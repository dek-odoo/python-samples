#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program# : Name
# =>
# Write a program that accepts a sentence and
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# modular code
# independent code
# cohesion
# coupling
# reuse
# efficient
# maintainable


def isInRange(cvalue, minn, maxn):
    if cvalue >= minn and cvalue <= maxn:
        return True


def isAlphaUpper(char):
    if isInRange(char, minn='A', maxn='Z'):
        return True


def isAlphaLower(char):
    if isInRange(char, minn='a', maxn='z'):
        return True


def countUpLower(sentence):
    upper = 0
    lower = 0
    for char in sentence:
        # checks for upper
        if isAlphaUpper(char):
            upper = upper + 1
        # checks for lower
        elif isAlphaLower(char):
            lower = lower + 1
        # else:
        #     print char
    result = {}
    result['upper'] = upper
    result['lower'] = lower
    return result


def main():
    # start from here
    # sentence = "Hello world!"
    print "sample input\n", "Hello world!"
    #!IMP****** Just comment the below line to TEST
    sentence = raw_input('Enter sentence (with Upper And Lower chars): ')
    result = countUpLower(sentence)
    print sentence
    print "# Upper ", result['upper']
    print "# Lower ", result['lower']
    # print result

if __name__ == '__main__':
    main()
# checked
