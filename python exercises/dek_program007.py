#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program007 :
# Write a program which takes 2 digits, X,Y as input and generates
# a 2-dimensional array. The element value in the i-th row and
# j-th column of the array should be i*j.

# Note: i=0,1.., X-1; j=0,1,Y-1.

# Example
# Suppose the following inputs are given to the

# program:
# 3,5

# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints:
# Note: In case of input data being supplied to the question,
# it should be assumed to be a console input in a comma-separated form.


def getNumberListFromConsole(prompt):
    try:
        d = raw_input(prompt)  # '100,150,180'
        d = d.split(',')  # ['100','150','180']
        d = [int(x) for x in d]  # [100,150,180]
        return d
    except:
        print 'Invalid Format'


def main():
    print "sample input ", '3,5'
    twod = []
    # print getNumberListFromConsole('Enter i,j: ')
    x, y = getNumberListFromConsole('Enter i,j: ')
    print x, y
    for i in range(0, x):
        # print i
        oned = []  # one Dimesional array
        for j in range(0, y):
            # print j
            # print i,',',j,'=',i*j
            # print j
            oned.append(i * j)
            # print oned
        twod.append(oned)
    print twod

if __name__ == '__main__':
    main()
# checked
