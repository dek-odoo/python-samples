#!/user/bin/python
# -*- coding: utf-8 -*-

# program# : Name
# =>
# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# Simple Approach
# joining strings
def concat(value, limit):
    tempvar = ''
    for iter in range(1, limit + 1):
        tempvar = tempvar + value
    print tempvar
    return tempvar


def main():
    try:
        print "sample input\n", "9,4"
        num = int(raw_input('Enter a Number: '))
        limit = int(raw_input('Enter a Number: '))
        ans = 0
        stru = str(num)  # !IMP
        for iter in range(1, limit + 1):
            # print int(concat('9', j))
            ans = ans + int(concat(stru, iter))  # performs 9+99+999+9999
        print ans
    except:
        print 'Exception:', 'Invalid Input'
if __name__ == '__main__':
    main()

# 9, 4
# 9000
# 900
# 90
# 9
# 9999 + 999+ 99+9
