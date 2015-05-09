# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
# console (n>0).

# Example:
# If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 3.55

# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Hints:
# Use float() to convert an integer to a float


def do(number):
    sum = 0
    for value in range(1, number + 1):
        # print "({0}) / ({0} + 1)".format(value)
        sum += ((float)(value) / (value + 1))
        # print sum
    # print sum
    return sum


def main():
    print 'Press Enter To Exit'
    print 'compute 1/2+2/3+3/4+...+n/n+1'
    while True:
        try:
            indata = raw_input("Enter Limit :")
            if not indata:  # if indata is nothing then exit the loop
                break
            print do(int(indata))
        except ValueError:
            print 'Only Numeric Value'

if __name__ == '__main__':
    main()
