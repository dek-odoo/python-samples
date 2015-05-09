#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program# : Name
# =>
# Write a program that accepts a sentence and calculate
# the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def isInRange(cn, minn, maxn):
    if cn >= minn and cn <= maxn:
        return True


def isLetter(c):
    if isInRange(c, minn='a', maxn='z') or isInRange(c, minn='A', maxn='Z'):
        return True


def isDigit(c):
    if isInRange(c, minn='0', maxn='9'):
        return True


def countOccurences(sentence):
    letters = 0
    digits = 0
    for c in sentence:
        # checks for letters
        if isLetter(c):
            letters = letters + 1
        # checks for digits
        if isDigit(c):
            digits = digits + 1
    result = {}
    result['letters'] = letters
    result['digits'] = digits
    return result


def main():
    # start from here
    # sentence = "hello world! 123"
    print "sample input\n", "hello world! 123"
    #*************** comment the below line to TEST
    sentence = raw_input('Enter sentence')
    result = countOccurences(sentence)
    print sentence
    print "# LETTERS ", result['letters']
    print "# DIGITS  ", result['digits']
    # print result
    # print a

if __name__ == '__main__':
    main()
# checked
