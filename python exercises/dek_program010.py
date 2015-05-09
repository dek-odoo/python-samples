#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar

# program010 :
# Write a program that accepts a sequence of whitespace
# separated words as input and prints the words after
# removing all duplicate words and sorting
# them alphanumerically.

# Suppose the following input is supplied to the
# program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and
# then use sorted() to sort the data.


def main():
    print "sample input\n", 'hello world and\
 practice makes perfect and hello world again'
    sentence = raw_input(
        'Enter A Sentence(with words Whitespace separated) : ')
    # separate each word with whitespace as delimeter
    sentence = sentence.split(' ')

    # set(parameter) to remove all duplicate words from parameter and
    # sorted(parameter) to sort parameter alphanumerically.
    sortedstrtokens = sorted(set(sentence))
    print sortedstrtokens
    # , \'
if __name__ == '__main__':
    main()
# checked
