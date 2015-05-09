# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or
# Python 3.

# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


import collections


def main(sentence):

    res = collections.Counter()
    sortedwords = sorted(sentence.split(' '))
    for word in sortedwords:
        res[word] += 1

    result = sorted(res)
    print result
    for result_word in result:
        print result_word, ':', res[result_word]

if __name__ == '__main__':
    main('New to Python or choosing between Python 2\
         and Python 3? Read Python 2 or Python 3')
    # main(raw_input())
