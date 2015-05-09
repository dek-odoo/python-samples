#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program004 :
# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# tuple() method can convert list to tuple


def main():
    print "sample input ", '34, 67, 55, 33, 12, 98'
    # csv = raw_input('Enter Comma Separated values: ')
    csv = '34, 67, 55, 33, 12, 98'
    wds = csv.split(',')
    print wds  # list
    wdsn = tuple(wds)
    return wdsn  # tuple
    # print wdsn[0]+1 #won't work bcoz string+int not possible

if __name__ == '__main__':
    print main()
# checked
