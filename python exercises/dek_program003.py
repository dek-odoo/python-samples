#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program003 : Use Of Dictionary
# With a given integral number n, write a program to generate a
# dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included). and then the program should
# print the dictionary.

# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Consider use dict()


def mulTable(limit):  # mulTable returns the multiplication table
    dict1 = dict()
    for number in range(1, limit + 1):
        dict1[number] = number * number
        # print iter
    # returns {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    return dict1


def main():
    print "sample input ", '8'
    num = int(raw_input('Enter A number: '))
    # num = 5
    dict = mulTable(num)
    print dict
    # for key, value in dict.iteritems():
    #     print key, value

if __name__ == '__main__':
    main()
